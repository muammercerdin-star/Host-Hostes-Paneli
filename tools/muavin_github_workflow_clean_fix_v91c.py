from pathlib import Path
from datetime import datetime
import shutil

ROOT = Path(".").resolve()
STAMP = datetime.now().strftime("%Y%m%d-%H%M%S")

WF = ROOT / ".github/workflows/android-debug-apk.yml"
APP_GRADLE = ROOT / "android_app/app/build.gradle"
GP = ROOT / "android_app/gradle.properties"

print("===== V91C GITHUB WORKFLOW TEMİZ FIX =====")

if not WF.exists():
    raise SystemExit("❌ Workflow yok: .github/workflows/android-debug-apk.yml")
if not APP_GRADLE.exists():
    raise SystemExit("❌ app/build.gradle yok")

for p in [WF, APP_GRADLE, GP]:
    if p.exists():
        b = p.with_name(p.name + f".bak-v91c-{STAMP}")
        shutil.copy2(p, b)
        print("📦 Yedek:", b.relative_to(ROOT))

BUILD_GRADLE = r'''plugins {
    id 'com.android.application'
    id 'com.chaquo.python'
}

def muavinBuildProfile = (project.findProperty("muavinBuildProfile") ?: System.getenv("MUAVIN_BUILD_PROFILE") ?: "github").toString()
def isTermuxBuild = muavinBuildProfile.equalsIgnoreCase("termux")

def muavinCompileSdk = isTermuxBuild ? 33 : 35
def muavinTargetSdk = isTermuxBuild ? 33 : 35
def muavinCoreVersion = isTermuxBuild ? "1.10.1" : "1.13.1"
def muavinBuildPython = isTermuxBuild ? "/data/data/com.termux/files/usr/bin/python3.13" : "python3.13"

android {
    namespace 'com.muavinasistani.app'
    compileSdk muavinCompileSdk

    defaultConfig {
        applicationId 'com.muavinasistani.app'
        minSdk 26
        targetSdk muavinTargetSdk
        versionCode 1
        versionName '0.1-test'

        python {
            version "3.13"
            buildPython muavinBuildPython

            pip {
                install "flask"
                install "werkzeug"
                install "requests"
                install "pillow"
            }
        }

        ndk {
            abiFilters "arm64-v8a"
        }
    }
}

dependencies {
    implementation "androidx.core:core:${muavinCoreVersion}"
}
'''

APP_GRADLE.write_text(BUILD_GRADLE, encoding="utf-8")
print("✅ build.gradle temiz yazıldı")

GP.write_text(
    "android.useAndroidX=true\n"
    "android.enableJetifier=true\n"
    "org.gradle.jvmargs=-Xmx2048m -Dfile.encoding=UTF-8\n",
    encoding="utf-8"
)
print("✅ repo gradle.properties temiz yazıldı")

WORKFLOW = r'''name: Android Debug APK

on:
  push:
    branches:
      - main
  workflow_dispatch:

jobs:
  build-debug-apk:
    name: Build debug APK
    runs-on: ubuntu-latest

    steps:
      - name: Checkout project
        uses: actions/checkout@v4

      - name: Set up Java 17
        uses: actions/setup-java@v4
        with:
          distribution: temurin
          java-version: "17"

      - name: Set up Python 3.13 for Chaquopy
        uses: actions/setup-python@v5
        with:
          python-version: "3.13"

      - name: Prepare Android SDK
        uses: android-actions/setup-android@v3

      - name: Install Android platform
        run: |
          yes | sdkmanager --licenses || true
          sdkmanager "platform-tools" "platforms;android-35" "build-tools;35.0.0"

      - name: Set up Gradle
        uses: gradle/actions/setup-gradle@v4

      - name: Verify build files
        run: |
          echo "===== build.gradle ====="
          grep -nE "muavinBuildProfile|compileSdk|targetSdk|muavinCoreVersion|androidx.core|buildPython|abiFilters" android_app/app/build.gradle
          echo
          echo "===== bad version search ====="
          ! grep -R "1.13.11.13.1" -n android_app .github

      - name: Build debug APK
        working-directory: android_app
        run: gradle -PmuavinBuildProfile=github :app:assembleDebug --stacktrace --no-daemon

      - name: Collect APK
        run: |
          mkdir -p artifacts
          cp android_app/app/build/outputs/apk/debug/app-debug.apk artifacts/muavin-asistani-debug.apk
          ls -lh artifacts

      - name: Upload APK
        uses: actions/upload-artifact@v4
        with:
          name: muavin-asistani-debug-apk
          path: artifacts/muavin-asistani-debug.apk
'''
WF.write_text(WORKFLOW, encoding="utf-8")
print("✅ workflow temiz yazıldı")

print()
print("===== KONTROL =====")
print("Bozuk sürüm sayısı:")
for p in [WF, APP_GRADLE, GP]:
    txt = p.read_text(encoding="utf-8", errors="ignore")
    print(p.relative_to(ROOT), "1.13.11.13.1 =", txt.count("1.13.11.13.1"))

print()
print("Workflow grep:")
for i, line in enumerate(WF.read_text(encoding="utf-8").splitlines(), 1):
    if any(k in line for k in ["muavinBuildProfile", "androidx.core", "sdkmanager", "assembleDebug", "1.13."]):
        print(f"{i:3}: {line}")

print()
print("✅ V91C tamam.")
