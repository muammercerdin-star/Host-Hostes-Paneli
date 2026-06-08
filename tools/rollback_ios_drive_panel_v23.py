from pathlib import Path
from datetime import datetime
import shutil
import re

ROOT = Path(".").resolve()
STAMP = datetime.now().strftime("%Y%m%d-%H%M%S")

TPL_TARGETS = [
    ROOT / "templates/seats.html",
    ROOT / "android_app/app/src/main/python/templates/seats.html",
]

CSS_TARGETS = [
    ROOT / "static/seats/patches/ios-drive-panel-v23.css",
    ROOT / "android_app/app/src/main/python/static/seats/patches/ios-drive-panel-v23.css",
]

LINK_RE = re.compile(
    r'^\s*<link\s+rel=["\']stylesheet["\']\s+href=["\']/static/seats/patches/ios-drive-panel-v23\.css[^"\']*["\']\s*>\s*\n?',
    re.M
)

print("===== IOS DRIVE PANEL V23 GERİ ALMA =====")

for p in TPL_TARGETS:
    if not p.exists():
        print("⚠️ Template yok:", p.relative_to(ROOT))
        continue

    s = p.read_text(encoding="utf-8", errors="ignore")

    if "ios-drive-panel-v23.css" not in s:
        print("ℹ️ Link zaten yok:", p.relative_to(ROOT))
        continue

    backup = p.with_name(p.name + f".bak-rollback-ios-v23-{STAMP}")
    shutil.copy2(p, backup)

    s2, removed = LINK_RE.subn("", s)

    if removed:
        p.write_text(s2, encoding="utf-8")
        print("✅ Link kaldırıldı:", p.relative_to(ROOT))
        print("   Kaldırılan link:", removed)
        print("   Yedek:", backup.relative_to(ROOT))
    else:
        print("⚠️ Link bulundu ama regex kaldıramadı:", p.relative_to(ROOT))

for p in CSS_TARGETS:
    if not p.exists():
        print("ℹ️ CSS zaten yok/pasif:", p.relative_to(ROOT))
        continue

    disabled = p.with_name(p.name + f".disabled-rollback-ios-v23-{STAMP}")
    shutil.move(str(p), str(disabled))
    print("✅ CSS pasifleştirildi:", p.relative_to(ROOT))
    print("   Yeni ad:", disabled.relative_to(ROOT))

print()
print("===== KONTROL =====")

for p in TPL_TARGETS:
    if p.exists():
        txt = p.read_text(encoding="utf-8", errors="ignore")
        print(p.relative_to(ROOT), "ios-drive-panel-v23.css:", txt.count("ios-drive-panel-v23.css"))

for p in CSS_TARGETS:
    print(p.relative_to(ROOT), "aktif dosya var mı:", p.exists())

print()
print("✅ V23 geri alma tamamlandı.")
