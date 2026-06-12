from pathlib import Path
from datetime import datetime
import shutil
import re

ROOT = Path(".").resolve()
STAMP = datetime.now().strftime("%Y%m%d-%H%M%S")

FILES = [
    ROOT / "static/continue/continue_trip_v99_clean.js",
    ROOT / "static/continue/continue_trip_v99_clean.css",
    ROOT / "android_app/app/src/main/python/static/continue/continue_trip_v99_clean.js",
    ROOT / "android_app/app/src/main/python/static/continue/continue_trip_v99_clean.css",
]

print("===== V99S HIZ ANALOG TOGGLE GERİ AL =====")

def latest_backup(p):
    baks = list(p.parent.glob(p.name + ".bak-v99s-speed-analog-*"))
    if not baks:
        return None
    return sorted(baks, key=lambda x: x.stat().st_mtime, reverse=True)[0]

def remove_block(p):
    if not p.exists():
        return False

    s = p.read_text(encoding="utf-8", errors="ignore")
    old = s

    s = re.sub(
        r"\n?/\* V99S_SPEED_ANALOG_TOGGLE_START \*/.*?/\* V99S_SPEED_ANALOG_TOGGLE_END \*/\n?",
        "\n",
        s,
        flags=re.S
    )

    s = re.sub(
        r"\n?/\* V99S_SPEED_ANALOG_TOGGLE_CSS_START \*/.*?/\* V99S_SPEED_ANALOG_TOGGLE_CSS_END \*/\n?",
        "\n",
        s,
        flags=re.S
    )

    if s != old:
        shutil.copy2(p, p.with_name(p.name + f".pre-v99s-rollback-{STAMP}"))
        p.write_text(s, encoding="utf-8")
        return True

    return False

for p in FILES:
    if not p.exists():
        print("YOK:", p)
        continue

    cur_bak = p.with_name(p.name + f".before-v99s-rollback-{STAMP}")
    shutil.copy2(p, cur_bak)
    print("📦 mevcut yedek:", cur_bak)

    bak = latest_backup(p)

    if bak:
        shutil.copy2(bak, p)
        print("✅ geri yüklendi:", p)
        print("   kaynak:", bak)
    else:
        changed = remove_block(p)
        if changed:
            print("✅ V99S bloğu temizlendi:", p)
        else:
            print("ℹ️ V99S bloğu/backup bulunmadı:", p)

print()
print("===== KONTROL =====")
for p in FILES:
    if not p.exists():
        continue
    txt = p.read_text(encoding="utf-8", errors="ignore")
    bad = any(k in txt for k in [
        "V99S_SPEED_ANALOG_TOGGLE",
        "v99-speed-analog",
        "v99-speed-needle",
        "v99-speed-analog-on",
    ])
    print(("❌ KALDI  " if bad else "✅ TEMİZ  ") + str(p))

print()
print("✅ İşlem bitti. Sayfayı şu şekilde yenile:")
print("http://127.0.0.1:5000/continue-trip?v=v99s-rollback")
