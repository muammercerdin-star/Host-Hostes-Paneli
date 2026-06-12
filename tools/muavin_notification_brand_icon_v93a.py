from pathlib import Path
from datetime import datetime
import shutil
import re

ROOT = Path(".").resolve()
STAMP = datetime.now().strftime("%Y%m%d-%H%M%S")

RES_DRAWABLE = ROOT / "android_app/app/src/main/res/drawable"
JAVA_DIR = ROOT / "android_app/app/src/main/java/com/muavinasistani/app"

print("===== V93A MUAVİN BİLDİRİM MARKA İKONU =====")

RES_DRAWABLE.mkdir(parents=True, exist_ok=True)

ICON = RES_DRAWABLE / "ic_muavin_notify.xml"

ICON_XML = '''<?xml version="1.0" encoding="utf-8"?>
<vector xmlns:android="http://schemas.android.com/apk/res/android"
    android:width="24dp"
    android:height="24dp"
    android:viewportWidth="24"
    android:viewportHeight="24">

    <!-- Muavin Asistanı: otobüs + canlı konum hissi -->
    <path
        android:fillColor="@android:color/white"
        android:pathData="M5,4h11c1.1,0 2,0.9 2,2v8.2c0,1 -0.7,1.8 -1.6,2L17,20h-2l-0.6,-3H7.6L7,20H5l0.6,-3.8C4.7,16 4,15.2 4,14.2V6c0,-1.1 0.9,-2 2,-2zM6,6.2v4.2h10V6.2H6zM7.4,14.8c0.8,0 1.4,-0.6 1.4,-1.4S8.2,12 7.4,12S6,12.6 6,13.4s0.6,1.4 1.4,1.4zM14.6,14.8c0.8,0 1.4,-0.6 1.4,-1.4S15.4,12 14.6,12s-1.4,0.6 -1.4,1.4s0.6,1.4 1.4,1.4z"/>

    <path
        android:fillColor="@android:color/white"
        android:pathData="M18.7,2.5c-1.9,0 -3.3,1.5 -3.3,3.3c0,2.5 3.3,5.8 3.3,5.8S22,8.3 22,5.8c0,-1.8 -1.5,-3.3 -3.3,-3.3zM18.7,7c-0.7,0 -1.2,-0.5 -1.2,-1.2s0.5,-1.2 1.2,-1.2s1.2,0.5 1.2,1.2S19.4,7 18.7,7z"/>
</vector>
'''

if ICON.exists():
    bak = ICON.with_name(ICON.name + f".bak-v93a-{STAMP}")
    shutil.copy2(ICON, bak)
    print("📦 Eski ikon yedek:", bak.relative_to(ROOT))

ICON.write_text(ICON_XML, encoding="utf-8")
print("✅ Yeni bildirim ikonu yazıldı:", ICON.relative_to(ROOT))

changed = 0

for path in JAVA_DIR.rglob("*.java"):
    txt = path.read_text(encoding="utf-8", errors="ignore")
    old = txt

    # Bildirimlerdeki genel Android ikonlarını Muavin marka ikonuna çevir.
    txt = re.sub(
        r"\.setSmallIcon\([^)]+\)",
        ".setSmallIcon(R.drawable.ic_muavin_notify)",
        txt
    )

    if txt != old:
        bak = path.with_name(path.name + f".bak-v93a-{STAMP}")
        shutil.copy2(path, bak)
        path.write_text(txt, encoding="utf-8")
        changed += 1
        print("✅ Java ikon güncellendi:", path.relative_to(ROOT))
        print("📦 Yedek:", bak.relative_to(ROOT))

if changed == 0:
    print("⚠️ Java içinde setSmallIcon bulunamadı. Elle kontrol gerekebilir.")

print()
print("===== KONTROL =====")
for path in JAVA_DIR.rglob("*.java"):
    txt = path.read_text(encoding="utf-8", errors="ignore")
    for i, line in enumerate(txt.splitlines(), 1):
        if "setSmallIcon" in line or "ic_muavin_notify" in line:
            print(f"{path.relative_to(ROOT)}:{i}: {line.strip()}")

print()
print("✅ V93A tamam. Artık bildirimde genel harita ikonu yerine Muavin özel simgesi kullanılacak.")
