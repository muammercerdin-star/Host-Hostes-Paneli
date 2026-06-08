from pathlib import Path
from datetime import datetime
import shutil

ROOT = Path(".").resolve()
STAMP = datetime.now().strftime("%Y%m%d-%H%M%S")

SERVER = ROOT / "android_app/app/src/main/python/android_server.py"
MAIN = ROOT / "android_app/app/src/main/java/com/muavinasistani/app/MainActivity.java"

print("===== APK START TIMEOUT FIX V36 =====")

def backup(p):
    bak = p.with_name(p.name + f".bak-apk-start-timeout-v36-{STAMP}")
    shutil.copy2(p, bak)
    print("📦 Yedek:", bak.relative_to(ROOT))

if not SERVER.exists():
    print("❌ android_server.py yok")
    raise SystemExit

if not MAIN.exists():
    print("❌ MainActivity.java yok")
    raise SystemExit

# 1) Python tarafı: 35 saniye -> 180 saniye
backup(SERVER)
s = SERVER.read_text(encoding="utf-8", errors="ignore")

s = s.replace(
    "def wait_for_port(host=HOST, port=PORT, timeout=35):",
    "def wait_for_port(host=HOST, port=PORT, timeout=180):"
)

s = s.replace(
    "wait_for_port(HOST, PORT, timeout=35)",
    "wait_for_port(HOST, PORT, timeout=180)"
)

# Daha net APK başlangıç logları
if "MUAVIN_APK_V36_START_LOG" not in s:
    s = s.replace(
        "def start_flask_server(app_files_dir=None):\n    global SERVER_ERROR\n\n    try:",
        "def start_flask_server(app_files_dir=None):\n    global SERVER_ERROR\n\n    try:\n        print('MUAVIN_APK_V36_START_LOG: Flask thread başladı', flush=True)"
    )

    s = s.replace(
        "        base_dir, data_dir = prepare_android_data_dir(app_files_dir)\n\n        import app as webapp",
        "        print('MUAVIN_APK_V36_START_LOG: data klasörü hazırlanıyor', flush=True)\n        base_dir, data_dir = prepare_android_data_dir(app_files_dir)\n        print('MUAVIN_APK_V36_START_LOG: app.py import başlıyor', flush=True)\n\n        import app as webapp\n        print('MUAVIN_APK_V36_START_LOG: app.py import tamam', flush=True)"
    )

    s = s.replace(
        "        flask_app.run(\n            host=HOST,",
        "        print('MUAVIN_APK_V36_START_LOG: Flask run başlıyor', HOST, PORT, flush=True)\n\n        flask_app.run(\n            host=HOST,"
    )

SERVER.write_text(s, encoding="utf-8")
print("✅ android_server.py güncellendi")

# 2) Android tarafı: 35000 ms -> 180000 ms
backup(MAIN)
m = MAIN.read_text(encoding="utf-8", errors="ignore")

m = m.replace("}, 35000);", "}, 180000);")
m = m.replace(
    "Flask sunucusu APK içinde başlamamış olabilir.",
    "Flask sunucusu APK içinde 180 saniye içinde başlamamış olabilir."
)

MAIN.write_text(m, encoding="utf-8")
print("✅ MainActivity.java güncellendi")

print()
print("===== KONTROL =====")
for p in [SERVER, MAIN]:
    txt = p.read_text(encoding="utf-8", errors="ignore")
    print()
    print(p.relative_to(ROOT))
    for key in ["timeout=180", "timeout=35", "180000", "35000", "MUAVIN_APK_V36_START_LOG"]:
        print(key, "=", txt.count(key))

print()
print("✅ V36 tamam.")
