from pathlib import Path
from datetime import datetime
import shutil
import re

ROOT = Path(".").resolve()
STAMP = datetime.now().strftime("%Y%m%d-%H%M%S")

GRADLE = ROOT / "android_app/app/build.gradle"
GP = ROOT / "android_app/gradle.properties"

print("===== V85I TERMUX AAPT2 SDK33 BUILD PROFİLİ =====")

if not GRADLE.exists():
    raise SystemExit("❌ app/build.gradle yok")

b = GRADLE.with_name(GRADLE.name + f".bak-sdk33-v85i-{STAMP}")
shutil.copy2(GRADLE, b)
print("📦 build.gradle yedeği:", b.relative_to(ROOT))

s = GRADLE.read_text(encoding="utf-8", errors="ignore")
old = s

# Termux aapt2 uyumu için SDK 33
s = re.sub(r'compileSdk\s+\d+', 'compileSdk 33', s)
s = re.sub(r'targetSdk\s+\d+', 'targetSdk 33', s)

# Chaquopy Python 3.13 ayarı kalsın
s = re.sub(r'version\s+"3\.\d+"', 'version "3.13"', s)

if 'buildPython "/data/data/com.termux/files/usr/bin/python3.13"' not in s:
    s = re.sub(
        r'buildPython\s+"[^"]*"',
        'buildPython "/data/data/com.termux/files/usr/bin/python3.13"',
        s
    )

# Python 3.13 için sadece arm64
s = re.sub(
    r'abiFilters\s+"arm64-v8a",\s*"armeabi-v7a"',
    'abiFilters "arm64-v8a"',
    s
)

# AndroidX core 1.13.1 yüksek SDK isteyebilir, 1.12.0 Termux SDK33 için daha güvenli
s = s.replace('androidx.core:core:1.13.1', 'androidx.core:core:1.12.0')

GRADLE.write_text(s, encoding="utf-8")

print()
print("===== build.gradle KONTROL =====")
for i, line in enumerate(s.splitlines(), 1):
    if any(k in line for k in ["compileSdk", "targetSdk", "version ", "buildPython", "abiFilters", "androidx.core"]):
        print(f"{i:4}: {line}")

if GP.exists():
    g = GP.read_text(encoding="utf-8", errors="ignore")
    if "android.aapt2FromMavenOverride=" not in g:
        b2 = GP.with_name(GP.name + f".bak-aapt2-v85i-{STAMP}")
        shutil.copy2(GP, b2)
        g += "\n# V85I_TERMUX_NATIVE_AAPT2\nandroid.aapt2FromMavenOverride=/data/data/com.termux/files/usr/bin/aapt2\n"
        GP.write_text(g, encoding="utf-8")
        print("✅ gradle.properties aapt2 override eklendi")
    else:
        print("✅ gradle.properties aapt2 override zaten var")

print()
print("===== CACHE TEMİZLİK ÖNERİSİ =====")
print("rm -rf android_app/app/build android_app/build ~/.gradle/caches/9.5.1/transforms")

print()
print("✅ V85I tamam.")
