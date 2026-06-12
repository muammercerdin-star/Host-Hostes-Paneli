from pathlib import Path
from datetime import datetime
import shutil
import re

ROOT = Path(".").resolve()
STAMP = datetime.now().strftime("%Y%m%d-%H%M%S")

GRADLE = ROOT / "android_app/app/build.gradle"
GP = ROOT / "android_app/gradle.properties"
WF = ROOT / ".github/workflows/android-debug-apk.yml"

print("===== V85L GITHUB ACTIONS APK BUILD PROFİLİ =====")

if not GRADLE.exists():
    raise SystemExit("❌ android_app/app/build.gradle yok")

b = GRADLE.with_name(GRADLE.name + f".bak-github-actions-v85l-{STAMP}")
shutil.copy2(GRADLE, b)
print("📦 build.gradle yedeği:", b.relative_to(ROOT))

s = GRADLE.read_text(encoding="utf-8", errors="ignore")

# GitHub Actions gerçek Linux ortamında Android 35 ile derlesin.
s = re.sub(r'compileSdk\s+\d+', 'compileSdk 35', s)
s = re.sub(r'targetSdk\s+\d+', 'targetSdk 35', s)

# Chaquopy 17 + Python 3.13.
s = re.sub(r'version\s+"3\.\d+"', 'version "3.13"', s)
s = re.sub(r'buildPython\s+"[^"]*"', 'buildPython "python3.13"', s)

# Python 3.13 için 64-bit ABI.
s = re.sub(
    r'abiFilters\s+"arm64-v8a",\s*"armeabi-v7a"',
    'abiFilters "arm64-v8a"',
    s
)

# Android 35 için yeni core sürümüne geri dönelim.
s = re.sub(
    r'androidx\.core:core:[0-9.]+',
    'androidx.core:core:1.13.1',
    s
)

GRADLE.write_text(s, encoding="utf-8")

print("✅ build.gradle GitHub Actions profiline alındı")

if GP.exists():
    b2 = GP.with_name(GP.name + f".bak-github-actions-v85l-{STAMP}")
    shutil.copy2(GP, b2)
    g = GP.read_text(encoding="utf-8", errors="ignore")
    # Termux native aapt2 override GitHub Actions'ta kullanılmayacak.
    lines = []
    skip_next_comment = False
    for line in g.splitlines():
        if "TERMUX_NATIVE_AAPT2" in line or "aapt2FromMavenOverride" in line:
            continue
        lines.append(line)
    GP.write_text("\n".join(lines).strip() + "\n", encoding="utf-8")
    print("✅ gradle.properties Termux aapt2 override temizlendi")

WF.parent.mkdir(parents=True, exist_ok=True)

WF.write_text(r'''name: Android Debug APK

on:
  workflow_dispatch:
  push:
    branches:
      - main
      - master

jobs:
  build-debug-apk:
    runs-on: ubuntu-latest

    defaults:
      run:
        working-directory: android_app

    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Set up Java 21
        uses: actions/setup-java@v4
        with:
          distribution: temurin
          java-version: '21'
          cache: gradle

      - name: Set up Python 3.13
        uses: actions/setup-python@v5
        with:
          python-version: '3.13'

      - name: Show versions
        run: |
          java -version
          python3.13 --version
          gradle -v

      - name: Accept Android licenses
        run: |
          yes | "$ANDROID_HOME/cmdline-tools/latest/bin/sdkmanager" --licenses || true

      - name: Install Android SDK packages
        run: |
          "$ANDROID_HOME/cmdline-tools/latest/bin/sdkmanager" \
            "platforms;android-35" \
            "build-tools;35.0.0" \
            "platform-tools"

      - name: Build debug APK
        run: |
          gradle :app:assembleDebug --stacktrace

      - name: Upload APK artifact
        uses: actions/upload-artifact@v4
        with:
          name: muavin-asistani-v85-debug-apk
          path: android_app/app/build/outputs/apk/debug/*.apk
''', encoding="utf-8")

print("✅ Workflow yazıldı:", WF.relative_to(ROOT))

print()
print("===== KONTROL =====")
for p in [GRADLE, GP, WF]:
    print()
    print("----", p.relative_to(ROOT), "----")
    txt = p.read_text(encoding="utf-8", errors="ignore")
    for i, line in enumerate(txt.splitlines(), 1):
        if any(k in line for k in [
            "compileSdk", "targetSdk", "version ", "buildPython",
            "abiFilters", "androidx.core", "aapt2FromMavenOverride",
            "python-version", "assembleDebug", "upload-artifact",
            "platforms;android-35"
        ]):
            print(f"{i:4}: {line}")

print()
print("✅ V85L tamam.")
