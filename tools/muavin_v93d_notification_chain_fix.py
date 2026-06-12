from pathlib import Path
from datetime import datetime
import shutil
import re

ROOT = Path(".").resolve()
STAMP = datetime.now().strftime("%Y%m%d-%H%M%S")
JAVA = ROOT / "android_app/app/src/main/java/com/muavinasistani/app/LiveStopAlertService.java"

print("===== V93D NOTIFICATION BUILDER CHAIN FIX =====")

if not JAVA.exists():
    raise SystemExit("❌ LiveStopAlertService.java yok")

s = JAVA.read_text(encoding="utf-8", errors="ignore")
old = s

bak = JAVA.with_name(JAVA.name + f".bak-v93d-{STAMP}")
shutil.copy2(JAVA, bak)
print("📦 Yedek:", bak.relative_to(ROOT))

# Asıl hata: .setContentText(monitorBody( satırı builder zincirini açık bırakıyor.
s = s.replace(
    ".setContentText(monitorBody()\n                .setContentIntent",
    ".setContentText(monitorBody())\n                .setContentIntent"
)

s = s.replace(
    ".setContentText(monitorBody(\n                .setContentIntent",
    ".setContentText(monitorBody())\n                .setContentIntent"
)

# Genel güvenlik: monitorBody çağrısı kırık kaldıysa toparla.
s = re.sub(
    r"\.setContentText\(monitorBody\(\s*\n\s*\.setContentIntent",
    ".setContentText(monitorBody())\n                .setContentIntent",
    s
)

# buildLockMessage de kırılmışsa toparla.
s = re.sub(
    r"\.setContentText\(buildLockMessage\(\s*\n\s*\.setContentIntent",
    ".setContentText(buildLockMessage())\n                .setContentIntent",
    s
)

JAVA.write_text(s, encoding="utf-8")

print()
print("===== 293-323 KONTROL =====")
lines = s.splitlines()
for i in range(293, min(323, len(lines)) + 1):
    print(f"{i}: {lines[i-1]}")

print()
print("===== ŞÜPHELİ BUILDER SATIRLARI =====")
bad = False
for i, line in enumerate(lines, 1):
    if ".setContentText(monitorBody(" in line and ".setContentText(monitorBody())" not in line:
        print(f"❌ Kırık monitorBody: {i}: {line}")
        bad = True
    if ".setContentText(buildLockMessage(" in line and ".setContentText(buildLockMessage())" not in line:
        print(f"❌ Kırık buildLockMessage: {i}: {line}")
        bad = True
    if "setCustomContentView" in line or "setCustomBigContentView" in line or "DecoratedCustomViewStyle" in line:
        print(f"✅ {i}: {line.strip()}")

print()
print("Durum:", "HATA ŞÜPHESİ VAR ❌" if bad else "TEMİZ ✅")
print("Değişiklik:", "YAPILDI ✅" if s != old else "YOK")
print("✅ V93D tamam.")
