from pathlib import Path
from datetime import datetime
import shutil

ROOT = Path(".").resolve()
STAMP = datetime.now().strftime("%Y%m%d-%H%M%S")

ACT = ROOT / "android_app/app/src/main/java/com/muavinasistani/app/LockAlarmActivity.java"

print("===== V90C LOCK ALARM JAVA TYPO FIX =====")

if not ACT.exists():
    raise SystemExit("❌ LockAlarmActivity.java yok")

backup = ACT.with_name(ACT.name + f".bak-v90c-{STAMP}")
shutil.copy2(ACT, backup)
print("📦 Yedek:", backup.relative_to(ROOT))

s = ACT.read_text(encoding="utf-8", errors="ignore")
old = s

s = s.replace(
    'stopName.toLocaleUpperCase(new Locale("tr", "TR"))',
    'stopName.toUpperCase(new Locale("tr", "TR"))'
)

ACT.write_text(s, encoding="utf-8")

print()
print("===== KONTROL =====")
for i, line in enumerate(s.splitlines(), 1):
    if "toUpperCase" in line or "toLocaleUpperCase" in line:
        print(f"{i}: {line}")

print()
if s != old:
    print("✅ V90C düzeltme yapıldı")
else:
    print("ℹ️ Değişiklik yok")

print("✅ V90C tamam.")
