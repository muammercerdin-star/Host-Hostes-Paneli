from pathlib import Path
from datetime import datetime
import shutil

ROOT = Path(".").resolve()
STAMP = datetime.now().strftime("%Y%m%d-%H%M%S")

TPLS = [
    ROOT / "templates/seats.html",
    ROOT / "android_app/app/src/main/python/templates/seats.html",
]

CSS_FILES = [
    ROOT / "static/seats/patches/ios-drive-clean-v25.css",
    ROOT / "android_app/app/src/main/python/static/seats/patches/ios-drive-clean-v25.css",
]

print("===== IOS DRIVE CLEAN V25 GERİ ALMA =====")

for tpl in TPLS:
    if not tpl.exists():
        print("⚠️ Template yok:", tpl.relative_to(ROOT))
        continue

    backups = sorted(
        tpl.parent.glob(tpl.name + ".bak-ios-drive-clean-v25-*"),
        key=lambda p: p.stat().st_mtime,
        reverse=True
    )

    safety = tpl.with_name(tpl.name + f".before-rollback-ios-drive-clean-v25-{STAMP}")
    shutil.copy2(tpl, safety)

    if backups:
        shutil.copy2(backups[0], tpl)
        print("✅ Geri alındı:", tpl.relative_to(ROOT))
        print("   Kullanılan yedek:", backups[0].relative_to(ROOT))
        print("   Geri alma öncesi emniyet:", safety.relative_to(ROOT))
    else:
        s = tpl.read_text(encoding="utf-8", errors="ignore")
        lines = [ln for ln in s.splitlines() if "ios-drive-clean-v25.css" not in ln]
        tpl.write_text("\n".join(lines) + "\n", encoding="utf-8")
        print("✅ V25 linki manuel kaldırıldı:", tpl.relative_to(ROOT))
        print("   Yedek bulunamadı, emniyet alındı:", safety.relative_to(ROOT))

for css in CSS_FILES:
    if css.exists():
        disabled = css.with_name(css.name + f".disabled_{STAMP}")
        css.rename(disabled)
        print("✅ CSS devre dışı bırakıldı:", disabled.relative_to(ROOT))
    else:
        print("ℹ️ CSS zaten yok:", css.relative_to(ROOT))

print()
print("===== KONTROL =====")
for tpl in TPLS:
    if tpl.exists():
        txt = tpl.read_text(encoding="utf-8", errors="ignore")
        print(tpl.relative_to(ROOT), "ios-drive-clean-v25:", txt.count("ios-drive-clean-v25"))

for css in CSS_FILES:
    print(css.relative_to(ROOT), "var mı:", css.exists())

print()
print("✅ V25 geri alma tamamlandı.")
