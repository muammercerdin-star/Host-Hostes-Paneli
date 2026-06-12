from pathlib import Path
from datetime import datetime
import shutil
import subprocess
import re

ROOT = Path(".").resolve()
STAMP = datetime.now().strftime("%Y%m%d-%H%M%S")
GRADLE = ROOT / "android_app/app/build.gradle"

print("===== V85E CHAQUOPY PYTHON 3.13 FIX =====")

if not GRADLE.exists():
    raise SystemExit("❌ android_app/app/build.gradle bulunamadı")

try:
    py = subprocess.check_output(["command", "-v", "python3"], shell=True, text=True).strip()
except Exception:
    py = "/data/data/com.termux/files/usr/bin/python3"

print("Python:", py)

b = GRADLE.with_name(GRADLE.name + f".bak-chaquopy-py313-v85e-{STAMP}")
shutil.copy2(GRADLE, b)
print("📦 Yedek:", b.relative_to(ROOT))

s = GRADLE.read_text(encoding="utf-8", errors="ignore")
old = s

# Python 3.11 yerine Termux'taki Python 3.13 kullan.
s = re.sub(r'version\s+"3\.11"', 'version "3.13"', s)
s = re.sub(r'buildPython\s+"python3\.11"', f'buildPython "{py}"', s)

# Python 3.12+ Chaquopy tarafında sadece 64-bit ABI desteklediği için 32-bit'i kaldır.
s = re.sub(
    r'abiFilters\s+"arm64-v8a",\s*"armeabi-v7a"',
    'abiFilters "arm64-v8a"',
    s
)

GRADLE.write_text(s, encoding="utf-8")

print()
print("===== DEĞİŞİKLİK =====")
if s != old:
    print("✅ build.gradle güncellendi")
else:
    print("ℹ️ build.gradle zaten güncel olabilir")

print()
print("===== KONTROL =====")
for i, line in enumerate(s.splitlines(), 1):
    if "python" in line or "version" in line or "buildPython" in line or "abiFilters" in line:
        print(f"{i:4}: {line}")

print()
print("✅ V85E tamam.")
