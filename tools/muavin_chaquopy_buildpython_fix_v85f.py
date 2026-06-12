from pathlib import Path
from datetime import datetime
import shutil
import re
import subprocess

ROOT = Path(".").resolve()
STAMP = datetime.now().strftime("%Y%m%d-%H%M%S")
GRADLE = ROOT / "android_app/app/build.gradle"

PYBIN = Path("/data/data/com.termux/files/usr/bin/python3.13")

print("===== V85F CHAQUOPY BUILDPYTHON NET DÜZELTME =====")

if not GRADLE.exists():
    raise SystemExit("❌ build.gradle yok")

if not PYBIN.exists():
    raise SystemExit(f"❌ Python 3.13 yok: {PYBIN}")

print("Python yolu:", PYBIN)

try:
    out = subprocess.check_output([str(PYBIN), "--version"], text=True, stderr=subprocess.STDOUT).strip()
    print("Python test:", out)
except Exception as e:
    raise SystemExit("❌ Python çalışmadı: " + str(e))

b = GRADLE.with_name(GRADLE.name + f".bak-buildpython-v85f-{STAMP}")
shutil.copy2(GRADLE, b)
print("📦 Yedek:", b.relative_to(ROOT))

s = GRADLE.read_text(encoding="utf-8", errors="ignore")
old = s

# python bloğundaki version ve buildPython satırlarını temiz/netleştir
s = re.sub(r'version\s+"3\.\d+"', 'version "3.13"', s)

if re.search(r'buildPython\s+"[^"]*"', s):
    s = re.sub(
        r'buildPython\s+"[^"]*"',
        f'buildPython "{PYBIN}"',
        s
    )
else:
    s = s.replace(
        'version "3.13"',
        f'version "3.13"\n            buildPython "{PYBIN}"'
    )

# Python 3.13 için sadece 64-bit ABI kalsın
s = re.sub(
    r'abiFilters\s+"arm64-v8a",\s*"armeabi-v7a"',
    'abiFilters "arm64-v8a"',
    s
)

# Eğer yanlışlıkla buildPython app klasörü gibi bozulduysa temizle
s = s.replace('buildPython ""', f'buildPython "{PYBIN}"')
s = s.replace('buildPython "app"', f'buildPython "{PYBIN}"')

GRADLE.write_text(s, encoding="utf-8")

print()
print("===== build.gradle KONTROL =====")
for i, line in enumerate(s.splitlines(), 1):
    if "python" in line or "version" in line or "buildPython" in line or "abiFilters" in line:
        print(f"{i:4}: {line}")

print()
if s != old:
    print("✅ build.gradle düzeltildi")
else:
    print("ℹ️ build.gradle zaten aynıydı")

print("✅ V85F tamam")
