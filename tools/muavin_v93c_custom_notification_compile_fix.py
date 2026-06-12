from pathlib import Path
from datetime import datetime
import shutil
import re

ROOT = Path(".").resolve()
STAMP = datetime.now().strftime("%Y%m%d-%H%M%S")
JAVA = ROOT / "android_app/app/src/main/java/com/muavinasistani/app/LiveStopAlertService.java"

print("===== V93C CUSTOM NOTIFICATION JAVA CLEAN FIX =====")

if not JAVA.exists():
    raise SystemExit("❌ LiveStopAlertService.java yok")

s = JAVA.read_text(encoding="utf-8", errors="ignore")
old = s

bak = JAVA.with_name(JAVA.name + f".bak-v93c-{STAMP}")
shutil.copy2(JAVA, bak)
print("📦 Java yedek:", bak.relative_to(ROOT))

# 1) Bilinen fazla parantez hatalarını satır satır temizle
fixed_lines = []
for line in s.splitlines():
    line = line.replace(".setContentText(monitorBody()))", ".setContentText(monitorBody())")
    line = line.replace(".setContentText(buildLockMessage()))", ".setContentText(buildLockMessage())")
    line = line.replace(".setContentText(message))", ".setContentText(message)")
    line = line.replace(".setContentTitle(monitorTitle()))", ".setContentTitle(monitorTitle())")
    fixed_lines.append(line)

s = "\n".join(fixed_lines) + "\n"

# 2) setContentText(...) sonunda çift parantez kalmışsa genel düzelt
s = re.sub(
    r"(\.setContentText\([^;\n]*?\))\)+(\s*(?:\.|;|\n))",
    r"\1\2",
    s
)

# 3) Custom view + Decorated style aynı bildirime ekli kalsın ama BigTextStyle varsa custom style'ı ezmesin
s = re.sub(
    r"\n\s*\.setStyle\(new Notification\.BigTextStyle\(\)\.bigText\([^;]+?\)\)",
    "",
    s,
    flags=re.S
)

JAVA.write_text(s, encoding="utf-8")

print()
print("===== 280-360 ARASI JAVA KONTROL =====")
lines = s.splitlines()
for i in range(280, min(360, len(lines)) + 1):
    print(f"{i}: {lines[i-1]}")

print()
print("===== ŞÜPHELİ SATIRLAR =====")
bad = False
for i, line in enumerate(lines, 1):
    if ".setContentText" in line and "))" in line:
        print(f"⚠️ {i}: {line}")
        bad = True
    if "DecoratedCustomViewStyle" in line or "setCustomBigContentView" in line or "setCustomContentView" in line:
        print(f"✅ {i}: {line.strip()}")

print()
print("Fazla parantez şüphesi:", "VAR ⚠️" if bad else "YOK ✅")
print("Değişiklik:", "YAPILDI ✅" if s != old else "YOK")
print("✅ V93C temizlik tamam.")
