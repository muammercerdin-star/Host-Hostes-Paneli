from pathlib import Path
from datetime import datetime
import shutil
import re

ROOT = Path(".").resolve()
STAMP = datetime.now().strftime("%Y%m%d-%H%M%S")

SERVER = ROOT / "android_app/app/src/main/python/android_server.py"
MAIN = ROOT / "android_app/app/src/main/java/com/muavinasistani/app/MainActivity.java"

print("===== APK STARTUP FILE LOG V38 =====")

def backup(p):
    bak = p.with_name(p.name + f".bak-apk-startup-file-log-v38-{STAMP}")
    shutil.copy2(p, bak)
    print("📦 Yedek:", bak.relative_to(ROOT))

if not SERVER.exists():
    print("❌ android_server.py yok")
    raise SystemExit

if not MAIN.exists():
    print("❌ MainActivity.java yok")
    raise SystemExit

backup(SERVER)

SERVER_CODE = r'''import os
import shutil
import sys
import threading
import time
import traceback
import urllib.request
from pathlib import Path
from datetime import datetime

SERVER_ERROR = None

HOST = "127.0.0.1"
PORT = 8765

PING_PATH = "/__apk_ping__"
PING_TEXT = "MUAVIN_APK_OK"

STARTUP_LOG = None


def _now():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def _set_startup_log(app_files_dir=None):
    global STARTUP_LOG

    try:
        if app_files_dir:
            log_dir = Path(str(app_files_dir))
        else:
            log_dir = Path(__file__).resolve().parent / "_android_data"

        log_dir.mkdir(parents=True, exist_ok=True)
        STARTUP_LOG = log_dir / "muavin_startup.log"
        STARTUP_LOG.write_text(
            f"[{_now()}] MUAVIN_APK_STARTUP_FILE_LOG_V38 başladı\n",
            encoding="utf-8",
        )
    except Exception:
        STARTUP_LOG = None


def _log(msg):
    try:
        line = f"[{_now()}] {msg}\n"
        print(line, flush=True)
        if STARTUP_LOG:
            with STARTUP_LOG.open("a", encoding="utf-8") as f:
                f.write(line)
    except Exception:
        pass


def _http_ping(host=HOST, port=PORT, timeout=1.2):
    try:
        url = f"http://{host}:{port}{PING_PATH}"
        with urllib.request.urlopen(url, timeout=timeout) as r:
            data = r.read(128).decode("utf-8", errors="ignore")
            return PING_TEXT in data
    except Exception:
        return False


def wait_for_port(host=HOST, port=PORT, timeout=60):
    start = time.time()
    last_log = 0

    while time.time() - start < timeout:
        global SERVER_ERROR

        if SERVER_ERROR:
            raise RuntimeError("Flask başlatılamadı:\n" + SERVER_ERROR)

        if _http_ping(host, port):
            _log(f"PING başarılı: {host}:{port}")
            return True

        elapsed = int(time.time() - start)
        if elapsed != last_log and elapsed % 5 == 0:
            last_log = elapsed
            _log(f"Bekleniyor... {elapsed}/{timeout} sn - port henüz hazır değil")

        time.sleep(0.35)

    raise RuntimeError(
        f"Flask {timeout} saniye içinde {host}:{port} üzerinde başlamadı."
    )


def prepare_android_data_dir(app_files_dir=None):
    _log("prepare_android_data_dir başladı")

    base_dir = Path(__file__).resolve().parent
    _log(f"base_dir={base_dir}")

    if str(base_dir) not in sys.path:
        sys.path.insert(0, str(base_dir))
        _log("base_dir sys.path içine eklendi")

    if app_files_dir:
        data_dir = Path(str(app_files_dir))
    else:
        data_dir = base_dir / "_android_data"

    data_dir.mkdir(parents=True, exist_ok=True)
    _log(f"data_dir={data_dir}")

    db_path = data_dir / "db.sqlite3"
    seed_db = base_dir / "seed" / "db.sqlite3"

    _log(f"db_path={db_path}")
    _log(f"seed_db={seed_db} exists={seed_db.exists()} size={seed_db.stat().st_size if seed_db.exists() else 0}")

    if not db_path.exists() and seed_db.exists():
        _log("seed db kopyalanıyor")
        shutil.copyfile(str(seed_db), str(db_path))
        _log("seed db kopyalandı")

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

    _log("ENV hazırlandı")
    _log(f"DB_PATH={os.environ.get('DB_PATH')}")
    _log(f"UPLOAD_DIR={os.environ.get('UPLOAD_DIR')}")

    os.chdir(str(data_dir))
    _log(f"chdir yapıldı: {data_dir}")

    return base_dir, data_dir


def start_flask_server(app_files_dir=None):
    global SERVER_ERROR

    try:
        _log("Flask thread başladı")

        _log("data klasörü hazırlanıyor")
        base_dir, data_dir = prepare_android_data_dir(app_files_dir)

        _log("app.py import başlıyor")
        import app as webapp
        _log("app.py import tamam")

        flask_app = webapp.app
        _log("flask_app alındı")

        if "__apk_ping__" not in flask_app.view_functions:
            _log("APK ping route ekleniyor")

            @flask_app.get(PING_PATH, endpoint="__apk_ping__")
            def __apk_ping__():
                return PING_TEXT, 200, {
                    "Content-Type": "text/plain; charset=utf-8"
                }

            _log("APK ping route eklendi")

        with flask_app.app_context():
            _log("app_context başladı")

            if hasattr(webapp, "ensure_schema"):
                _log("ensure_schema başlıyor")
                webapp.ensure_schema()
                _log("ensure_schema tamam")

            if hasattr(webapp, "ensure_upload_dir"):
                _log("ensure_upload_dir başlıyor")
                webapp.ensure_upload_dir()
                _log("ensure_upload_dir tamam")

            _log("app_context tamam")

        _log(f"Flask run başlıyor: {HOST}:{PORT}")

        flask_app.run(
            host=HOST,
            port=PORT,
            debug=False,
            use_reloader=False,
            threaded=True,
        )

    except Exception:
        SERVER_ERROR = traceback.format_exc()
        _log("PYTHON HATA BAŞLADI")
        _log(SERVER_ERROR)
        _log("PYTHON HATA BİTTİ")
        print(SERVER_ERROR, flush=True)


def start_in_background(app_files_dir=None):
    _set_startup_log(app_files_dir)
    _log(f"start_in_background çağrıldı app_files_dir={app_files_dir}")

    t = threading.Thread(
        target=start_flask_server,
        args=(app_files_dir,),
        daemon=True,
    )
    t.start()

    _log("Flask thread start edildi")
    wait_for_port(HOST, PORT, timeout=60)
    _log("start_in_background başarılı döndü")
    return True
'''

SERVER.write_text(SERVER_CODE, encoding="utf-8")
print("✅ android_server.py komple güvenli loglu sürüme alındı")

backup(MAIN)
m = MAIN.read_text(encoding="utf-8", errors="ignore")

# Java içine log okuma metodu ekle
if "readMuavinStartupLogV38" not in m:
    method = r'''
    private String readMuavinStartupLogV38() {
        try {
            java.io.File f = new java.io.File(getFilesDir(), "muavin_startup.log");
            if (!f.exists()) {
                return "\n\nAPK STARTUP LOG:\nLog dosyası oluşmamış.";
            }

            byte[] data = java.nio.file.Files.readAllBytes(f.toPath());
            String text = new String(data, java.nio.charset.StandardCharsets.UTF_8);

            if (text.length() > 12000) {
                text = text.substring(text.length() - 12000);
            }

            return "\n\nAPK STARTUP LOG:\n" + text;
        } catch (Exception ex) {
            return "\n\nAPK STARTUP LOG okunamadı:\n" + ex.toString();
        }
    }

'''
    if "private void showError(" in m:
        m = m.replace("    private void showError(", method + "    private void showError(", 1)
        print("✅ Java log okuma metodu eklendi")
    else:
        print("⚠️ showError metodu bulunamadı, log metodu eklenemedi")

# Catch içindeki hata mesajına startup log ekle
old = 'showError("Flask sunucusu başlatılamadı:\\n" + e.toString());'
new = 'showError("Flask sunucusu başlatılamadı:\\n" + e.toString() + readMuavinStartupLogV38());'

if old in m:
    m = m.replace(old, new, 1)
    print("✅ catch hata ekranına startup log eklendi")
elif "readMuavinStartupLogV38()" in m and "Flask sunucusu başlatılamadı" in m:
    print("ℹ️ catch kısmı zaten değiştirilmiş olabilir")
else:
    print("⚠️ catch showError satırı otomatik bulunamadı")

# Bekleme ekranındaki eski timeout mesajını da sadeleştir
m = m.replace("Flask sunucusu APK içinde 180 saniye içinde başlamamış olabilir.", "Flask sunucusu APK içinde başlamamış olabilir.")
m = m.replace("}, 180000);", "}, 70000);")
m = m.replace("}, 35000);", "}, 70000);")

MAIN.write_text(m, encoding="utf-8")
print("✅ MainActivity.java güncellendi")

print()
print("===== KONTROL =====")
for p in [SERVER, MAIN]:
    txt = p.read_text(encoding="utf-8", errors="ignore")
    print()
    print(p.relative_to(ROOT))
    for key in [
        "MUAVIN_APK_STARTUP_FILE_LOG_V38",
        "muavin_startup.log",
        "readMuavinStartupLogV38",
        "timeout=60",
        "timeout=180",
        "180000",
        "70000",
    ]:
        print(key, "=", txt.count(key))

print()
print("✅ V38 tamam.")
