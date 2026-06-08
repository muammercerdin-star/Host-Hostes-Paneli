from pathlib import Path
from datetime import datetime
import shutil

ROOT = Path(".").resolve()
STAMP = datetime.now().strftime("%Y%m%d-%H%M%S")

TARGETS = [
    ROOT / "static/seats/patches/seat-layout-fab-pack.js",
    ROOT / "android_app/app/src/main/python/static/seats/patches/seat-layout-fab-pack.js",
    ROOT / "templates/seats.html",
    ROOT / "android_app/app/src/main/python/templates/seats.html",
]

def latest_backup_for(p: Path):
    backups = sorted(
        p.parent.glob(p.name + ".bak-fab-overlap-v16b-*"),
        key=lambda x: x.stat().st_mtime,
        reverse=True
    )
    return backups[0] if backups else None

print("===== V16B GERİ ALMA =====")

for p in TARGETS:
    if not p.exists():
        print("⚠️ Orijinal dosya yok:", p.relative_to(ROOT))
        continue

    b = latest_backup_for(p)

    if not b:
        print("❌ V16B yedeği bulunamadı:", p.relative_to(ROOT))
        continue

    safety = p.with_name(p.name + f".before-rollback-v16b-{STAMP}")
    shutil.copy2(p, safety)

    shutil.copy2(b, p)

    print("✅ Geri alındı:", p.relative_to(ROOT))
    print("   kullanılan yedek:", b.relative_to(ROOT))
    print("   rollback öncesi emniyet:", safety.relative_to(ROOT))

print()
print("===== KONTROL =====")
for p in TARGETS:
    if not p.exists():
        continue

    txt = p.read_text(encoding="utf-8", errors="ignore")
    print(p.relative_to(ROOT))
    print("  FAB_LEGEND_OVERLAP_FIX_V16B:", txt.count("FAB_LEGEND_OVERLAP_FIX_V16B"))
    print("  fab-overlap-v16b:", txt.count("fab-overlap-v16b"))

print()
print("✅ V16B geri alma tamamlandı.")
