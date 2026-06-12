from pathlib import Path
from datetime import datetime
import shutil
import re

ROOT = Path(".").resolve()
STAMP = datetime.now().strftime("%Y%m%d-%H%M%S")
JAVA = ROOT / "android_app/app/src/main/java/com/muavinasistani/app/LiveStopAlertService.java"

print("===== V93B2 JAVA PARANTEZ FIX =====")

if not JAVA.exists():
    raise SystemExit("❌ LiveStopAlertService.java yok")

s = JAVA.read_text(encoding="utf-8", errors="ignore")
old = s

bak = JAVA.with_name(JAVA.name + f".bak-v93b2-{STAMP}")
shutil.copy2(JAVA, bak)
print("📦 Java yedek:", bak.relative_to(ROOT))

# Bilinen hata: .setContentText(monitorBody()))
s = s.replace(".setContentText(monitorBody()))", ".setContentText(monitorBody())")
s = s.replace(".setContentText(buildLockMessage()))", ".setContentText(buildLockMessage())")
s = s.replace(".setContentText(message))", ".setContentText(message)")

# Aynı türden zincir sonu fazla parantez kalırsa genel temizlik
s = re.sub(r"(\.setContentText\([^)]+\))\)+(\s*[;\n])", r"\1\2", s)

JAVA.write_text(s, encoding="utf-8")

print()
print("===== HATA SATIRI KONTROL =====")
bad = False
for i, line in enumerate(s.splitlines(), 1):
    if ".setContentText" in line or ".setCustomContentView" in line or ".setCustomBigContentView" in line or "DecoratedCustomViewStyle" in line:
        print(f"{i}: {line.strip()}")
    if ".setContentText" in line and line.strip().endswith("))"):
        bad = True

print()
print("Fazla parantez şüphesi:", "VAR ⚠️" if bad else "YOK ✅")
print("Değişiklik:", "YAPILDI ✅" if s != old else "YOK")
print("✅ V93B2 tamam.")
