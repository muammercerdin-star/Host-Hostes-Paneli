from pathlib import Path
from datetime import datetime
import shutil
import re
import hashlib

ROOT = Path(".").resolve()
STAMP = datetime.now().strftime("%Y%m%d-%H%M%S")

WEB_TPL = ROOT / "templates/continue_trip.html"
AND_TPL = ROOT / "android_app/app/src/main/python/templates/continue_trip.html"

WEB_JS = ROOT / "static/continue/continue_speed_toggle_v100.js"
AND_JS = ROOT / "android_app/app/src/main/python/static/continue/continue_speed_toggle_v100.js"

WEB_CSS = ROOT / "static/continue/continue_speed_toggle_v100.css"
AND_CSS = ROOT / "android_app/app/src/main/python/static/continue/continue_speed_toggle_v100.css"

print("===== V100 HIZ TOGGLE İZOLE PAKET GERİ AL =====")

def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()[:12] if p.exists() else "-"

for p in [WEB_TPL, AND_TPL, WEB_JS, AND_JS, WEB_CSS, AND_CSS]:
    if p.exists():
        bak = p.with_name(p.name + f".bak-v100-speed-rollback-{STAMP}")
        shutil.copy2(p, bak)
        print("📦 backup:", bak)

# Template içinden V100 CSS/JS çağrılarını kaldır
for tpl_path in [WEB_TPL, AND_TPL]:
    if not tpl_path.exists():
        continue

    s = tpl_path.read_text(encoding="utf-8", errors="ignore")
    old = s

    s = re.sub(
        r'\n?\s*<link[^>]+continue_speed_toggle_v100\.css[^>]*>\s*',
        "\n",
        s
    )

    s = re.sub(
        r'\n?\s*<script[^>]+continue_speed_toggle_v100\.js[^>]*></script>\s*',
        "\n",
        s
    )

    if s != old:
        tpl_path.write_text(s, encoding="utf-8")
        print("✅ template V100 link/script kaldırıldı:", tpl_path)
    else:
        print("ℹ️ template içinde V100 çağrısı yok:", tpl_path)

# İzole dosyaları pasifleştir
for p in [WEB_JS, AND_JS, WEB_CSS, AND_CSS]:
    if p.exists():
        disabled = p.with_name(p.name + f".disabled-{STAMP}")
        shutil.move(str(p), str(disabled))
        print("✅ pasifleştirildi:", disabled)
    else:
        print("ℹ️ zaten yok:", p)

print()
print("===== KONTROL =====")

for tpl_path in [WEB_TPL, AND_TPL]:
    if tpl_path.exists():
        txt = tpl_path.read_text(encoding="utf-8", errors="ignore")
        print(("❌ HALA VAR  " if "continue_speed_toggle_v100" in txt else "✅ TEMİZ     ") + str(tpl_path))

for p in [WEB_JS, AND_JS, WEB_CSS, AND_CSS]:
    print(("❌ HALA AKTİF " if p.exists() else "✅ PASİF      ") + str(p))

print()
print("===== AKTİF TEMPLATE SCRIPT SATIRLARI =====")
if WEB_TPL.exists():
    txt = WEB_TPL.read_text(encoding="utf-8", errors="ignore")
    for i, line in enumerate(txt.splitlines(), 1):
        if "continue_trip_v99_clean.js" in line or "continue_speed_toggle_v100" in line:
            print(f"{i}: {line}")

print()
print("✅ V100 hız analog paketi geri alındı.")
print("Yenile:")
print("http://127.0.0.1:5000/continue-trip?v=v100-speed-clean")
