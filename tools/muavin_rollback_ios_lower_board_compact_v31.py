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
    r'^\s*<link\s+rel="stylesheet"\s+href="/static/seats/patches/ios-lower-board-compact-v31\.css[^"]*">\s*\n?',
    re.M
)

print("===== IOS LOWER BOARD COMPACT V31 GERİ ALMA =====")

for p in TARGETS:
    if not p.exists():
        print("⚠️ Yok:", p.relative_to(ROOT))
        continue

    s = p.read_text(encoding="utf-8", errors="ignore")
    before = s.count("ios-lower-board-compact-v31.css")

    if before == 0:
        print("ℹ️ Zaten bağlı değil:", p.relative_to(ROOT))
        continue

    backup = p.with_name(p.name + f".bak-rollback-ios-lower-board-v31-{STAMP}")
    shutil.copy2(p, backup)

    s, removed = PATTERN.subn("", s)
    p.write_text(s, encoding="utf-8")

    print("✅ V31 linki kaldırıldı:", p.relative_to(ROOT))
    print("   Kaldırılan link:", removed)
    print("   Yedek:", backup.relative_to(ROOT))

print()
print("===== KONTROL =====")
for p in TARGETS:
    if not p.exists():
        continue
    txt = p.read_text(encoding="utf-8", errors="ignore")
    print(p.relative_to(ROOT), "ios-lower-board-compact-v31:", txt.count("ios-lower-board-compact-v31.css"))

print()
print("✅ V31 geri alma tamamlandı.")
