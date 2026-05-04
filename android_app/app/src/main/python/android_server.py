import os
import socket
import shutil
import threading
import time
import traceback
from pathlib import Path

SERVER_ERROR = None


def wait_for_port(host="127.0.0.1", port=5000, timeout=25):
    start = time.time()

    while time.time() - start < timeout:
        global SERVER_ERROR

        if SERVER_ERROR:
            raise RuntimeError("Flask başlatılamadı:\n" + SERVER_ERROR)

        try:
            with socket.create_connection((host, port), timeout=1):
                return True
        except OSError:
            time.sleep(0.4)

    raise RuntimeError("Flask 25 saniye içinde 127.0.0.1:5000 üzerinde başlamadı.")


def prepare_android_data_dir(app_files_dir=None):
    base_dir = Path(__file__).resolve().parent

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

    os.chdir(str(data_dir))

    return base_dir, data_dir


def start_flask_server(app_files_dir=None):
    global SERVER_ERROR

    try:
        base_dir, data_dir = prepare_android_data_dir(app_files_dir)

        from app import app

        app.run(
            host="127.0.0.1",
            port=5000,
            debug=False,
            use_reloader=False,
            threaded=True,
        )

    except Exception:
        SERVER_ERROR = traceback.format_exc()
        print(SERVER_ERROR)


def start_in_background(app_files_dir=None):
    t = threading.Thread(target=start_flask_server, args=(app_files_dir,), daemon=True)
    t.start()

    wait_for_port("127.0.0.1", 5000, timeout=25)
    return True
