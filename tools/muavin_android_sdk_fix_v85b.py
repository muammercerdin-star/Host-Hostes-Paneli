from pathlib import Path
import os
import re

ROOT = Path(".").resolve()
ANDROID = ROOT / "android_app"
LOCAL = ANDROID / "local.properties"

print("===== V85B ANDROID SDK YOLU DENETİMİ =====")

print("\n===== local.properties =====")
if LOCAL.exists():
    print(LOCAL.read_text(encoding="utf-8", errors="ignore"))
else:
    print("❌ local.properties yok")

print("\n===== ENV =====")
for k in ["ANDROID_HOME", "ANDROID_SDK_ROOT", "ANDROID_SDK_HOME"]:
    print(k, "=", os.environ.get(k, ""))

print("\n===== OLASI SDK DİZİNLERİ =====")
candidates = []

for env in ["ANDROID_HOME", "ANDROID_SDK_ROOT"]:
    v = os.environ.get(env)
    if v:
        candidates.append(Path(v))

home = Path.home()
candidates += [
    home / "android-sdk",
    home / "Android/Sdk",
    home / "sdk",
    Path("/data/data/com.termux/files/usr/opt/android-sdk"),
    Path("/data/data/com.termux/files/usr/share/android-sdk"),
    Path("/sdcard/Android/Sdk"),
]

# android.jar arayarak gerçek SDK bul
for base in [home, Path("/data/data/com.termux/files/usr"), Path("/sdcard")]:
    try:
        for jar in base.rglob("platforms/android-*/android.jar"):
            candidates.append(jar.parent.parent)
    except Exception:
        pass

seen = set()
valid = []

for c in candidates:
    c = c.expanduser()
    key = str(c)
    if key in seen:
        continue
    seen.add(key)

    platforms = c / "platforms"
    build_tools = c / "build-tools"
    ok = c.exists() and platforms.exists()

    print(("✅" if ok else "❌"), c)

    if ok:
        valid.append(c)

print("\n===== SONUÇ =====")
if not valid:
    print("❌ Android SDK bulunamadı.")
    print("Önce SDK kurulmalı ya da doğru sdk.dir yolu bulunmalı.")
    raise SystemExit(2)

sdk = valid[0]
print("✅ Kullanılacak SDK:", sdk)

# local.properties güncelle
old = LOCAL.read_text(encoding="utf-8", errors="ignore") if LOCAL.exists() else ""
lines = []
written = False

for line in old.splitlines():
    if line.strip().startswith("sdk.dir="):
        lines.append("sdk.dir=" + str(sdk))
        written = True
    else:
        lines.append(line)

if not written:
    lines.append("sdk.dir=" + str(sdk))

LOCAL.write_text("\n".join(lines).strip() + "\n", encoding="utf-8")

print("\n✅ local.properties güncellendi:")
print(LOCAL.read_text(encoding="utf-8", errors="ignore"))
