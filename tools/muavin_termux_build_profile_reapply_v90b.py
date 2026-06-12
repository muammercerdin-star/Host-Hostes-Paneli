from pathlib import Path
from datetime import datetime
import shutil
import re

ROOT = Path(".").resolve()
STAMP = datetime.now().strftime("%Y%m%d-%H%M%S")

GRADLE = ROOT / "android_app/app/build.gradle"
GP = ROOT / "android_app/gradle.properties"

print("===== V90B TERMUX BUILD PROFİLİNİ GERİ KUR =====")

if not GRADLE.exists():
    raise SystemExit("❌ android_app/app/build.gradle yok")

b = GRADLE.with_name(GRADLE.name + f".bak-termux-v90b-{STAMP}")
shutil.copy2(GRADLE, b)
print("📦 build.gradle yedeği:", b.relative_to(ROOT))

s = GRADLE.read_text(encoding="utf-8", errors="ignore")

s = re.sub(r'compileSdk\s+\d+', 'compileSdk 33', s)
s = re.sub(r'targetSdk\s+\d+', 'targetSdk 33', s)

s = re.sub(
    r'androidx\.core:core:[0-9.]+',
    'androidx.core:core:1.10.1',
    s
)

s = re.sub(r'version\s+"3\.\d+"', 'version "3.13"', s)

if re.search(r'buildPython\s+"[^"]*"', s):
    s = re.sub(
        r'buildPython\s+"[^"]*"',
        'buildPython "/data/data/com.termux/files/usr/bin/python3.13"',
        s
    )
else:
    s = s.replace(
        'version "3.13"',
        'version "3.13"\n            buildPython "/data/data/com.termux/files/usr/bin/python3.13"'
    )

s = re.sub(
    r'abiFilters\s+"arm64-v8a",\s*"armeabi-v7a"',
    'abiFilters "arm64-v8a"',
    s
)

GRADLE.write_text(s, encoding="utf-8")

if not GP.exists():
    GP.write_text("", encoding="utf-8")

g = GP.read_text(encoding="utf-8", errors="ignore")
g = re.sub(r'\n?# V\d+_TERMUX_NATIVE_AAPT2\nandroid\.aapt2FromMavenOverride=.*\n?', '\n', g)
g = re.sub(r'\n?android\.aapt2FromMavenOverride=.*\n?', '\n', g)

if "android.useAndroidX=true" not in g:
    g = "android.useAndroidX=true\n" + g

if "android.enableJetifier=true" not in g:
    g = "android.enableJetifier=true\n" + g

if "org.gradle.jvmargs=" not in g:
    g += "\norg.gradle.jvmargs=-Xmx2048m -Dfile.encoding=UTF-8\n"

g += "\n# V90B_TERMUX_NATIVE_AAPT2\nandroid.aapt2FromMavenOverride=/data/data/com.termux/files/usr/bin/aapt2\n"

GP.write_text(g.strip() + "\n", encoding="utf-8")

print()
print("===== build.gradle KONTROL =====")
for i, line in enumerate(s.splitlines(), 1):
    if any(k in line for k in ["compileSdk", "targetSdk", "version ", "buildPython", "abiFilters", "androidx.core"]):
        print(f"{i}: {line}")

print()
print("===== gradle.properties KONTROL =====")
print(GP.read_text(encoding="utf-8", errors="ignore"))

print("✅ V90B Termux build profili kuruldu.")
