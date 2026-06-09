from pathlib import Path
from datetime import datetime
import shutil
import re

ROOT = Path(".").resolve()
STAMP = datetime.now().strftime("%Y%m%d-%H%M%S")

CSS_FILES = [
    ROOT / "static/continue/continue_v76.css",
    ROOT / "android_app/app/src/main/python/static/continue/continue_v76.css",
]

TPLS = [
    ROOT / "templates/continue_trip.html",
    ROOT / "android_app/app/src/main/python/templates/continue_trip.html",
]

print("===== ROLLBACK SHEET CARD V80 =====")

for p in CSS_FILES:
    if not p.exists():
        print("⚠️ Yok:", p.relative_to(ROOT))
        continue

    b = p.with_name(p.name + f".bak-rollback-v80-{STAMP}")
    shutil.copy2(p, b)
    print("📦 Yedek:", b.relative_to(ROOT))

    s = p.read_text(encoding="utf-8", errors="ignore")
    old = s

    # V80 en sona eklenmişti. Sadece V80 kart yamasını kaldırıyoruz.
    s = re.sub(
        r'\n\s*/\*\s*CONTINUE_SHEET_CARD_RESTORE_V80\s*\*/[\s\S]*$',
        '\n',
        s
    )

    if s != old:
        p.write_text(s, encoding="utf-8")
        print("✅ V80 CSS yaması kaldırıldı:", p.relative_to(ROOT))
    else:
        print("ℹ️ V80 yaması bulunamadı:", p.relative_to(ROOT))

print()
print("===== CACHE V79'A AL =====")

for p in TPLS:
    if not p.exists():
        print("⚠️ Yok:", p.relative_to(ROOT))
        continue

    b = p.with_name(p.name + f".bak-rollback-v80-cache-{STAMP}")
    shutil.copy2(p, b)
    print("📦 Yedek:", b.relative_to(ROOT))

    s = p.read_text(encoding="utf-8", errors="ignore")

    s = re.sub(
        r"continue/continue_v76\.css'\) }}\?v=[^\"']+",
        "continue/continue_v76.css') }}?v=prototype-layout-v79",
        s
    )

    p.write_text(s, encoding="utf-8")
    print("✅ Cache V79'a çekildi:", p.relative_to(ROOT))

print()
print("✅ V80 geri alındı.")
