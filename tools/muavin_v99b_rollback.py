from pathlib import Path
import shutil
from datetime import datetime

ROOT = Path(".").resolve()
STAMP = datetime.now().strftime("%Y%m%d-%H%M%S")

FILES = [
    ROOT / "static/continue/continue_trip_v99_clean.css",
    ROOT / "static/continue/continue_trip_v99_clean.js",
    ROOT / "android_app/app/src/main/python/static/continue/continue_trip_v99_clean.css",
    ROOT / "android_app/app/src/main/python/static/continue/continue_trip_v99_clean.js",
]

print("===== V99B ROLLBACK =====")

for target in FILES:
    if not target.exists():
        print("⚠️ hedef yok, geçildi:", target)
        continue

    safety = target.with_name(target.name + f".before-v99b-rollback-{STAMP}")
    shutil.copy2(target, safety)
    print("📦 mevcut hal yedeği:", safety)

    backups = sorted(
        target.parent.glob(target.name + ".bak-v99b-*"),
        key=lambda p: p.stat().st_mtime,
        reverse=True
    )

    if not backups:
        print("❌ V99B backup bulunamadı:", target)
        continue

    src = backups[0]
    shutil.copy2(src, target)
    print("✅ geri alındı:", target)
    print("↩️ kaynak:", src)

print()
print("===== KONTROL =====")
for target in FILES[:2]:
    if target.exists():
        txt = target.read_text(encoding="utf-8", errors="ignore")
        print(target.name)
        print("  V99B var mı:", "VAR" if "V99B_" in txt else "YOK")
        print("  V99C var mı:", "VAR" if "V99C_" in txt else "YOK")
        print("  V99 ana tasarım var mı:", "VAR" if "v99-prox-card" in txt or "v99-ring-wrap" in txt else "YOK")

print()
print("✅ V99B rollback tamam")
