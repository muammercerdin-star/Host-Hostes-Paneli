from pathlib import Path
from datetime import datetime
import shutil
import re

ROOT = Path(".").resolve()
STAMP = datetime.now().strftime("%Y%m%d-%H%M%S")

SERVER = ROOT / "android_app/app/src/main/python/android_server.py"
MAIN = ROOT / "android_app/app/src/main/java/com/muavinasistani/app/MainActivity.java"

print("===== APK START PORT GUARD V37 =====")

def backup(p):
    bak = p.with_name(p.name + f".bak-apk-start-port-guard-v37-{STAMP}")
    shutil.copy2(p, bak)
    print("📦 Yedek:", bak.relative_to(ROOT))

if not SERVER.exists():
    print("❌ android_server.py yok")
    raise SystemExit

if not MAIN.exists():
    print("❌ MainActivity.java yok")
    raise SystemExit

backup(SERVER)
s = SERVER.read_text(encoding="utf-8", errors="ignore")

# socket import yoksa ekle
if "import socket" not in s:
    s = s.replace("import shutil\n", "import shutil\nimport socket\n")

# Eski HTTP ping fonksiyonunu port kontrolüne çevir
s = re.sub(
    r"def _http_ping\(host=HOST, port=PORT, timeout=1\.2\):\n(?:    .+\n)+?\n\ndef wait_for_port",
    """def _port_open(host=HOST, port=PORT, timeout=1.2):
    try:
        with socket.create_connection((host, port), timeout=timeout):
            return True
    except Exception:
        return False


def wait_for_port""",
    s
)

# Eğer regex yakalamadıysa basit fallback
s = s.replace("_http_ping(host, port)", "_port_open(host, port)")

# wait_for_port içindeki açıklamayı ve ping çağrısını düzelt
s = s.replace(
    "# Sadece port açık mı diye bakmıyoruz.\n        # Muavin Flask gerçekten açıldı mı diye özel ping kontrolü yapıyoruz.\n        if _http_ping(host, port):",
    "# APK içinde burada özel URL ping yapmıyoruz.\n        # Çünkü app.py yönlendirme/koruma filtreleri ping yolunu kesebilir.\n        # Port açıldıysa Flask çalışıyor kabul edip WebView'i yüklüyoruz.\n        if _port_open(host, port):"
)

s = s.replace(
    "f\"Flask {timeout} saniye içinde {host}:{port} üzerinde başlamadı.\"",
    "f\"Flask portu {timeout} saniye içinde {host}:{port} üzerinde açılmadı.\""
)

# V36 timeout 180 ise çok bekletmesin, 60 yeter
s = s.replace("timeout=180", "timeout=60")
s = s.replace("wait_for_port(HOST, PORT, timeout=180)", "wait_for_port(HOST, PORT, timeout=60)")

SERVER.write_text(s, encoding="utf-8")
print("✅ android_server.py port kontrolüne alındı")

backup(MAIN)
m = MAIN.read_text(encoding="utf-8", errors="ignore")

# Android tarafı 60 saniye beklesin
m = m.replace("}, 180000);", "}, 60000);")
m = m.replace("}, 35000);", "}, 60000);")

m = m.replace(
    "Flask sunucusu APK içinde 180 saniye içinde başlamamış olabilir.",
    "Flask sunucusu APK içinde 60 saniye içinde başlamamış olabilir."
)
m = m.replace(
    "Flask sunucusu APK içinde başlamamış olabilir.",
    "Flask sunucusu APK içinde 60 saniye içinde başlamamış olabilir."
)

MAIN.write_text(m, encoding="utf-8")
print("✅ MainActivity.java 60 saniye kontrolüne alındı")

print()
print("===== KONTROL =====")
for p in [SERVER, MAIN]:
    txt = p.read_text(encoding="utf-8", errors="ignore")
    print()
    print(p.relative_to(ROOT))
    for key in ["_port_open", "_http_ping", "timeout=60", "timeout=180", "60000", "180000", "__apk_ping__"]:
        print(key, "=", txt.count(key))

print()
print("✅ V37 tamam. Bu düzeltme Flask ping kilidini kaldırır.")
