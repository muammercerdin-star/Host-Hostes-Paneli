from pathlib import Path
from datetime import datetime
import shutil
import re

ROOT = Path(".").resolve()
STAMP = datetime.now().strftime("%Y%m%d-%H%M%S")

TARGETS = [
    ROOT / "templates/seats.html",
    ROOT / "android_app/app/src/main/python/templates/seats.html",
]

PATTERN = re.compile(
    r'^\s*<link\s+rel="stylesheet"\s+href="/static/seats/patches/unified-seat-deck-report-style\.css[^"]*">\s*\n?',
    re.M
)

print("===== UNIFIED SEAT DECK PATCH DEVRE DIŞI BIRAKMA V18 =====")

for p in TARGETS:
    if not p.exists():
        print("⚠️ Yok:", p.relative_to(ROOT))
        continue

    s = p.read_text(encoding="utf-8", errors="ignore")
    old = s

    count_before = s.count("unified-seat-deck-report-style.css")

    if count_before == 0:
        print("ℹ️ Zaten bağlı değil:", p.relative_to(ROOT))
        continue

    backup = p.with_name(p.name + f".bak-disable-unified-seat-deck-v18-{STAMP}")
    shutil.copy2(p, backup)

    s, removed = PATTERN.subn("", s)

    if s != old:
        p.write_text(s, encoding="utf-8")
        print("✅ Devre dışı bırakıldı:", p.relative_to(ROOT))
        print("   Kaldırılan link:", removed)
        print("   Yedek:", backup.relative_to(ROOT))
    else:
        print("⚠️ Link bulundu ama otomatik kaldırılamadı:", p.relative_to(ROOT))

print()
print("===== KONTROL =====")
for p in TARGETS:
    if not p.exists():
        continue
    txt = p.read_text(encoding="utf-8", errors="ignore")
    print(p.relative_to(ROOT), "unified-seat-deck-report-style:", txt.count("unified-seat-deck-report-style.css"))

print()
print("✅ V18 işlem tamam.")
