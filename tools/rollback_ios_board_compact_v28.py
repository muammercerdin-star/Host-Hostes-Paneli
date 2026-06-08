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
    ROOT / "static/seats/patches/ios-board-compact-v28.css",
    ROOT / "android_app/app/src/main/python/static/seats/patches/ios-board-compact-v28.css",
]

print("===== IOS BOARD COMPACT V28 GERİ ALMA =====")

for p in TPL_TARGETS:
    if not p.exists():
        print("⚠️ Template yok:", p.relative_to(ROOT))
        continue

    before = p.with_name(p.name + f".before-rollback-ios-board-v28-{STAMP}")
    shutil.copy2(p, before)

    backups = sorted(
        p.parent.glob(p.name + ".bak-ios-board-compact-v28-*"),
        key=lambda x: x.stat().st_mtime,
        reverse=True
    )

    if backups:
        shutil.copy2(backups[0], p)
        print("✅ Template yedekten geri alındı:", p.relative_to(ROOT))
        print("   Kullanılan yedek:", backups[0].relative_to(ROOT))
        print("   Rollback öncesi emniyet:", before.relative_to(ROOT))
    else:
        s = p.read_text(encoding="utf-8", errors="ignore")
        old = s
        s = re.sub(
            r'^\s*<link\s+rel="stylesheet"\s+href="/static/seats/patches/ios-board-compact-v28\.css[^"]*">\s*\n?',
            "",
            s,
            flags=re.M
        )
        if s != old:
            p.write_text(s, encoding="utf-8")
            print("✅ V28 linki manuel kaldırıldı:", p.relative_to(ROOT))
            print("   Rollback öncesi emniyet:", before.relative_to(ROOT))
        else:
            print("ℹ️ V28 linki zaten yok:", p.relative_to(ROOT))

for p in CSS_TARGETS:
    if not p.exists():
        print("ℹ️ CSS zaten yok:", p.relative_to(ROOT))
        continue

    disabled = p.with_name(p.name + f".disabled-rollback-v28-{STAMP}")
    shutil.move(str(p), str(disabled))
    print("✅ CSS devre dışı bırakıldı:", p.relative_to(ROOT))
    print("   Taşındı:", disabled.relative_to(ROOT))

print()
print("===== KONTROL =====")
for p in TPL_TARGETS + CSS_TARGETS:
    if p.exists():
        txt = p.read_text(encoding="utf-8", errors="ignore")
        print(p.relative_to(ROOT), "ios-board-compact-v28:", txt.count("ios-board-compact-v28"))
    else:
        print(p.relative_to(ROOT), "YOK")

print()
print("✅ V28 geri alma tamamlandı.")
