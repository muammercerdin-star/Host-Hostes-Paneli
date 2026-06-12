from pathlib import Path
from datetime import datetime
import shutil
import re

ROOT = Path(".").resolve()
STAMP = datetime.now().strftime("%Y%m%d-%H%M%S")

TPLS = [
    ROOT / "templates/continue_trip.html",
    ROOT / "android_app/app/src/main/python/templates/continue_trip.html",
]

FILES = [
    ROOT / "static/continue/continue_speed_widget_v101.js",
    ROOT / "static/continue/continue_speed_widget_v101.css",
    ROOT / "android_app/app/src/main/python/static/continue/continue_speed_widget_v101.js",
    ROOT / "android_app/app/src/main/python/static/continue/continue_speed_widget_v101.css",
]

print("===== V101 HIZ WIDGET GERİ AL =====")

# 1) Template içinden V101 link/script kaldır
for p in TPLS:
    if not p.exists():
        print("YOK:", p)
        continue

    bak = p.with_name(p.name + f".bak-v101-speed-widget-rollback-{STAMP}")
    shutil.copy2(p, bak)
    print("📦 backup:", bak)

    s = p.read_text(encoding="utf-8", errors="ignore")
    old = s

    s = re.sub(
        r'\n?\s*<link[^>]+continue_speed_widget_v101\.css[^>]*>\s*',
        "\n",
        s
    )

    s = re.sub(
        r'\n?\s*<script[^>]+continue_speed_widget_v101\.js[^>]*></script>\s*',
        "\n",
        s
    )

    if s != old:
        p.write_text(s, encoding="utf-8")
        print("✅ V101 çağrıları kaldırıldı:", p)
    else:
        print("ℹ️ V101 çağrısı zaten yok:", p)

# 2) V101 dosyaları pasifleştir
for p in FILES:
    if p.exists():
        bak = p.with_name(p.name + f".disabled-{STAMP}")
        shutil.move(str(p), str(bak))
        print("✅ pasifleştirildi:", bak)
    else:
        print("ℹ️ zaten yok:", p)

print()
print("===== KONTROL =====")

for p in TPLS:
    if p.exists():
        txt = p.read_text(encoding="utf-8", errors="ignore")
        ok = "continue_speed_widget_v101" not in txt
        print(("✅ TEMİZ  " if ok else "❌ HALA VAR  ") + str(p))

for p in FILES:
    print(("❌ HALA AKTİF  " if p.exists() else "✅ PASİF       ") + str(p))

print()
print("===== AKTİF SCRIPT SATIRLARI =====")
tpl = TPLS[0]
if tpl.exists():
    txt = tpl.read_text(encoding="utf-8", errors="ignore")
    for i, line in enumerate(txt.splitlines(), 1):
        if "continue_trip_v99_clean.js" in line or "continue_speed_widget_v101" in line:
            print(f"{i}: {line}")

print()
print("✅ V101 hız widget geri alındı.")
print("Yenile:")
print("http://127.0.0.1:5000/continue-trip?v=v101-speed-rollback")
