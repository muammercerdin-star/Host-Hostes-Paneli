from pathlib import Path
from datetime import datetime
import shutil
import re

ROOT = Path(".").resolve()
STAMP = datetime.now().strftime("%Y%m%d-%H%M%S")

APP_GRADLE = ROOT / "android_app/app/build.gradle"
GP = ROOT / "android_app/gradle.properties"

print("===== V91B GITHUB ANDROIDX CORE VERSION FIX =====")

if not APP_GRADLE.exists():
    raise SystemExit("❌ app/build.gradle yok")

bak = APP_GRADLE.with_name(APP_GRADLE.name + f".bak-v91b-{STAMP}")
shutil.copy2(APP_GRADLE, bak)
print("📦 build.gradle yedek:", bak.relative_to(ROOT))

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

if GP.exists():
    bak2 = GP.with_name(GP.name + f".bak-v91b-{STAMP}")
    shutil.copy2(GP, bak2)

    g = GP.read_text(encoding="utf-8", errors="ignore")
    lines = []
    for line in g.splitlines():
        if "android.aapt2FromMavenOverride" in line:
            continue
        if "TERMUX_NATIVE_AAPT2" in line or "V85H" in line or "V90B" in line or "V91" in line:
            continue
        lines.append(line)

    cleaned = "\n".join(lines).strip() + "\n"
    GP.write_text(cleaned, encoding="utf-8")
    print("✅ repo gradle.properties GitHub için temizlendi")

print()
print("===== KONTROL =====")
for i, line in enumerate(APP_GRADLE.read_text(encoding="utf-8").splitlines(), 1):
    if any(k in line for k in ["muavinCoreVersion", "androidx.core", "compileSdk", "targetSdk", "buildPython"]):
        print(f"{i:3}: {line}")

print()
print("===== BOZUK SÜRÜM ARAMA =====")
txt = APP_GRADLE.read_text(encoding="utf-8")
print("1.13.11.13.1 sayısı:", txt.count("1.13.11.13.1"))
print("✅ V91B tamam.")
