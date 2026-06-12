from pathlib import Path
from datetime import datetime
import shutil
import re

ROOT = Path(".").resolve()
STAMP = datetime.now().strftime("%Y%m%d-%H%M%S")
GRADLE = ROOT / "android_app/app/build.gradle"

print("===== V85J ANDROIDX CORE SDK33 UYUM FIX =====")

if not GRADLE.exists():
    raise SystemExit("❌ app/build.gradle yok")

b = GRADLE.with_name(GRADLE.name + f".bak-androidx-core-v85j-{STAMP}")
shutil.copy2(GRADLE, b)
print("📦 Yedek:", b.relative_to(ROOT))

s = GRADLE.read_text(encoding="utf-8", errors="ignore")
old = s

# Termux native aapt2 için SDK33 profilini koru
s = re.sub(r'compileSdk\s+\d+', 'compileSdk 33', s)
s = re.sub(r'targetSdk\s+\d+', 'targetSdk 33', s)

# AndroidX core 1.12+ compileSdk 34 ister. SDK33 için güvenli sürüme çek.
s = re.sub(
    r'androidx\.core:core:[0-9.]+',
    'androidx.core:core:1.10.1',
    s
)

# Chaquopy / Termux Python ayarı kalsın
s = re.sub(r'version\s+"3\.\d+"', 'version "3.13"', s)
s = re.sub(
    r'buildPython\s+"[^"]*"',
    'buildPython "/data/data/com.termux/files/usr/bin/python3.13"',
    s
)

# Python 3.13 için arm64
s = re.sub(
    r'abiFilters\s+"arm64-v8a",\s*"armeabi-v7a"',
    'abiFilters "arm64-v8a"',
    s
)

GRADLE.write_text(s, encoding="utf-8")

print()
print("===== build.gradle KONTROL =====")
for i, line in enumerate(s.splitlines(), 1):
    if any(k in line for k in ["compileSdk", "targetSdk", "version ", "buildPython", "abiFilters", "androidx.core"]):
        print(f"{i:4}: {line}")

print()
print("✅ V85J tamam.")
