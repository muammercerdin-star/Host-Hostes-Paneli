from pathlib import Path
from datetime import datetime
import shutil
import re

ROOT = Path(".").resolve()
STAMP = datetime.now().strftime("%Y%m%d-%H%M%S")

APP_GRADLE = ROOT / "android_app/app/build.gradle"
GP = ROOT / "android_app/gradle.properties"
WF_DIR = ROOT / ".github/workflows"

print("===== V91 ÇİFT BUILD PROFİLİ: TERMUX + GITHUB =====")

if not APP_GRADLE.exists():
    raise SystemExit("❌ app/build.gradle yok")

bak = APP_GRADLE.with_name(APP_GRADLE.name + f".bak-v91-{STAMP}")
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
print("✅ build.gradle çift profil yapıldı")

if GP.exists():
    bak2 = GP.with_name(GP.name + f".bak-v91-{STAMP}")
    shutil.copy2(GP, bak2)
    g = GP.read_text(encoding="utf-8", errors="ignore")
    # GitHub'a gidecek gradle.properties temiz olmalı
    lines = []
    skip_next_blank = False
    for line in g.splitlines():
        if "android.aapt2FromMavenOverride" in line:
            continue
        if "V85H_TERMUX_NATIVE_AAPT2" in line or "V90B_TERMUX_NATIVE_AAPT2" in line or "V91_TERMUX_NATIVE_AAPT2" in line:
            continue
        lines.append(line)
    g2 = "\n".join(lines).strip() + "\n"
    GP.write_text(g2, encoding="utf-8")
    print("✅ gradle.properties GitHub için temizlendi")

# Termux aapt2 override global local'e yazılacak, git'e girmeyecek.
LOCAL_GP = Path.home() / ".gradle/gradle.properties"
LOCAL_GP.parent.mkdir(parents=True, exist_ok=True)
old = LOCAL_GP.read_text(encoding="utf-8", errors="ignore") if LOCAL_GP.exists() else ""
old_lines = [x for x in old.splitlines() if not x.startswith("android.aapt2FromMavenOverride=")]
old_lines.append("android.aapt2FromMavenOverride=/data/data/com.termux/files/usr/bin/aapt2")
LOCAL_GP.write_text("\n".join(old_lines).strip() + "\n", encoding="utf-8")
print("✅ Termux aapt2 override ~/.gradle/gradle.properties içine yazıldı")

# Workflow dosyalarını GitHub profil ile derleyecek şekilde düzelt
if WF_DIR.exists():
    for wf in WF_DIR.glob("*.yml"):
        s = wf.read_text(encoding="utf-8", errors="ignore")
        old = s

        s = s.replace("gradle :app:assembleDebug", "gradle -PmuavinBuildProfile=github :app:assembleDebug")
        s = s.replace("./gradlew :app:assembleDebug", "./gradlew -PmuavinBuildProfile=github :app:assembleDebug")
        s = s.replace("gradle :app:compileDebugJavaWithJavac", "gradle -PmuavinBuildProfile=github :app:compileDebugJavaWithJavac")
        s = s.replace("./gradlew :app:compileDebugJavaWithJavac", "./gradlew -PmuavinBuildProfile=github :app:compileDebugJavaWithJavac")

        # Python 3.13 görünsün
        s = re.sub(r'python-version:\s*[\'"]?3\.\d+[\'"]?', 'python-version: "3.13"', s)

        if s != old:
            bakw = wf.with_name(wf.name + f".bak-v91-{STAMP}")
            shutil.copy2(wf, bakw)
            wf.write_text(s, encoding="utf-8")
            print("✅ workflow güncellendi:", wf.relative_to(ROOT))

print()
print("===== KONTROL =====")
print("app/build.gradle:")
for i, line in enumerate(APP_GRADLE.read_text(encoding="utf-8").splitlines(), 1):
    if any(k in line for k in ["muavinBuildProfile", "compileSdk", "targetSdk", "buildPython", "androidx.core", "abiFilters"]):
        print(f"{i:3}: {line}")

print()
print("android_app/gradle.properties:")
print(GP.read_text(encoding="utf-8", errors="ignore") if GP.exists() else "YOK")

print("~/.gradle/gradle.properties:")
print(LOCAL_GP.read_text(encoding="utf-8", errors="ignore"))

print("✅ V91 tamam.")
