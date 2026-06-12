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

JS_FILES = [
    ROOT / "static/continue/continue_doluluk_click_guard_v99t.js",
    ROOT / "android_app/app/src/main/python/static/continue/continue_doluluk_click_guard_v99t.js",
]

print("===== V99T DOLULUK CLICK GUARD GERİ AL =====")

for p in TPLS:
    if not p.exists():
        print("YOK:", p)
        continue

    bak = p.with_name(p.name + f".bak-rollback-v99t-{STAMP}")
    shutil.copy2(p, bak)
    print("📦 backup:", bak)

    s = p.read_text(encoding="utf-8", errors="ignore")
    old = s

    s = re.sub(
        r'\n?\s*<script src="/static/continue/continue_doluluk_click_guard_v99t\.js[^"]*"></script>\s*\n?',
        "\n",
        s
    )

    if s != old:
        p.write_text(s, encoding="utf-8")
        print("✅ script tag kaldırıldı:", p)
    else:
        print("ℹ️ script tag zaten yok:", p)

for p in JS_FILES:
    if p.exists():
        disabled = p.with_name(p.name + f".disabled-{STAMP}")
        shutil.move(str(p), str(disabled))
        print("✅ JS pasifleştirildi:", disabled)
    else:
        print("ℹ️ JS zaten yok:", p)

print()
print("===== KONTROL =====")
for p in TPLS:
    if p.exists():
        txt = p.read_text(encoding="utf-8", errors="ignore")
        print(("❌ HALA VAR  " if "continue_doluluk_click_guard_v99t" in txt else "✅ TEMİZ     ") + str(p))

for p in JS_FILES:
    print(("❌ HALA VAR  " if p.exists() else "✅ PASİF     ") + str(p))

print()
print("✅ V99T geri alındı. Sayfayı cache kırarak yenile:")
print("http://127.0.0.1:5000/continue-trip?v=rollback-v99t")
