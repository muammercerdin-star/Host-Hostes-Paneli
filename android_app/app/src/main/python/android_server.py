import os
import shutil
import sys
import threading
import time
import traceback
import urllib.request
from pathlib import Path

SERVER_ERROR = None

HOST = "127.0.0.1"
PORT = 8765

PING_PATH = "/__apk_ping__"
PING_TEXT = "MUAVIN_APK_OK"


def _http_ping(host=HOST, port=PORT, timeout=1.2):
    try:
        url = f"http://{host}:{port}{PING_PATH}"
        with urllib.request.urlopen(url, timeout=timeout) as r:
            data = r.read(128).decode("utf-8", errors="ignore")
            return PING_TEXT in data
    except Exception:
        return False


def wait_for_port(host=HOST, port=PORT, timeout=180):
    start = time.time()

    while time.time() - start < timeout:
        global SERVER_ERROR

        if SERVER_ERROR:
            raise RuntimeError("Flask başlatılamadı:\n" + SERVER_ERROR)

        # Sadece port açık mı diye bakmıyoruz.
        # Muavin Flask gerçekten açıldı mı diye özel ping kontrolü yapıyoruz.
        if _http_ping(host, port):
            return True

        time.sleep(0.35)

    raise RuntimeError(
        f"Flask {timeout} saniye içinde {host}:{port} üzerinde başlamadı."
    )


def prepare_android_data_dir(app_files_dir=None):
    base_dir = Path(__file__).resolve().parent

    if str(base_dir) not in sys.path:
        sys.path.insert(0, str(base_dir))

    if app_files_dir:
        data_dir = Path(str(app_files_dir))
    else:
        data_dir = base_dir / "_android_data"

    data_dir.mkdir(parents=True, exist_ok=True)

    db_path = data_dir / "db.sqlite3"
    seed_db = base_dir / "seed" / "db.sqlite3"

    if not db_path.exists() and seed_db.exists():
        shutil.copyfile(str(seed_db), str(db_path))

    uploads_dir = data_dir / "uploads" / "consignments"
    reports_dir = data_dir / "storage" / "reports"
    backups_dir = data_dir / "storage" / "backups"

    uploads_dir.mkdir(parents=True, exist_ok=True)
    reports_dir.mkdir(parents=True, exist_ok=True)
    backups_dir.mkdir(parents=True, exist_ok=True)

    os.environ["DB_PATH"] = str(db_path)
    os.environ["UPLOAD_DIR"] = str(uploads_dir)
    os.environ["MUAVIN_ANDROID"] = "1"
    os.environ["MUAVIN_APK_PORT"] = str(PORT)

    os.chdir(str(data_dir))

    return base_dir, data_dir


def start_flask_server(app_files_dir=None):
    global SERVER_ERROR

    try:
        print('MUAVIN_APK_V36_START_LOG: Flask thread başladı', flush=True)
        print('MUAVIN_APK_V36_START_LOG: data klasörü hazırlanıyor', flush=True)
        base_dir, data_dir = prepare_android_data_dir(app_files_dir)
        print('MUAVIN_APK_V36_START_LOG: app.py import başlıyor', flush=True)

        import app as webapp
        print('MUAVIN_APK_V36_START_LOG: app.py import tamam', flush=True)

        flask_app = webapp.app

        if "__apk_ping__" not in flask_app.view_functions:
            @flask_app.get(PING_PATH, endpoint="__apk_ping__")
            def __apk_ping__():
                return PING_TEXT, 200, {
                    "Content-Type": "text/plain; charset=utf-8"
                }

        with flask_app.app_context():
            if hasattr(webapp, "ensure_schema"):
                webapp.ensure_schema()
            if hasattr(webapp, "ensure_upload_dir"):
                webapp.ensure_upload_dir()

        print('MUAVIN_APK_V36_START_LOG: Flask run başlıyor', HOST, PORT, flush=True)

        flask_app.run(
            host=HOST,
            port=PORT,
            debug=False,
            use_reloader=False,
            threaded=True,
        )

    except Exception:
        SERVER_ERROR = traceback.format_exc()
        print(SERVER_ERROR)


def start_in_background(app_files_dir=None):
    t = threading.Thread(
        target=start_flask_server,
        args=(app_files_dir,),
        daemon=True,
    )
    t.start()

    wait_for_port(HOST, PORT, timeout=180)
    return True
