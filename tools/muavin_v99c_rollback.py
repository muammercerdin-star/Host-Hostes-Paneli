from pathlib import Path
import shutil

ROOT = Path(".").resolve()

FILES = [
    ROOT / "static/continue/continue_trip_v99_clean.css",
    ROOT / "static/continue/continue_trip_v99_clean.js",
    ROOT / "android_app/app/src/main/python/static/continue/continue_trip_v99_clean.css",
    ROOT / "android_app/app/src/main/python/static/continue/continue_trip_v99_clean.js",
]

print("===== V99C ROLLBACK =====")

ok = True

for target in FILES:
    if not target.exists():
        print("⚠️ hedef yok, geçildi:", target)
        continue

    backups = sorted(
        target.parent.glob(target.name + ".bak-v99c-*"),
        key=lambda p: p.stat().st_mtime,
        reverse=True
    )

    if not backups:
        print("⚠️ V99C backup yok, değişmeden kaldı:", target)
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
        print(target.name, "V99C var mı:", "VAR" if "V99C_" in txt else "YOK")

print()
print("✅ V99C rollback tamam")
