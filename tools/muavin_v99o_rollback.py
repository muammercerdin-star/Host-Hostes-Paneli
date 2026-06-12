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

print("===== V99O KOLTUK POPUP İŞLEMİ GERİ ALMA =====")

def latest_backup(p):
    backups = sorted(
        p.parent.glob(p.name + ".bak-v99o-seat-popup-*"),
        key=lambda x: x.stat().st_mtime,
        reverse=True
    )
    return backups[0] if backups else None

for p in FILES:
    if not p.exists():
        print("⚠️ dosya yok:", p)
        continue

    safety = p.with_name(p.name + f".before-v99o-rollback-{STAMP}")
    shutil.copy2(p, safety)
    print("📦 rollback öncesi yedek:", safety)

    bak = latest_backup(p)

    if bak and bak.exists():
        shutil.copy2(bak, p)
        print("✅ geri yüklendi:", bak, "->", p)
    else:
        print("⚠️ V99O backup bulunamadı, blok temizleme deneniyor:", p)

        s = p.read_text(encoding="utf-8", errors="ignore")
        old = s

        s = re.sub(
            r"\n?/\* V99O_SEAT_DETAIL_POPUP_CSS_START \*/.*?/\* V99O_SEAT_DETAIL_POPUP_CSS_END \*/\n?",
            "\n",
            s,
            flags=re.S
        )

        s = re.sub(
            r"\n?/\* V99O_SEAT_DETAIL_POPUP_JS_START \*/.*?/\* V99O_SEAT_DETAIL_POPUP_JS_END \*/\n?",
            "\n",
            s,
            flags=re.S
        )

        if s != old:
            p.write_text(s, encoding="utf-8")
            print("✅ V99O bloğu temizlendi:", p)
        else:
            print("ℹ️ V99O izi yok:", p)

print()
print("===== KONTROL =====")

for p in FILES:
    if not p.exists():
        continue

    txt = p.read_text(encoding="utf-8", errors="ignore")
    has = any(k in txt for k in [
        "V99O_SEAT_DETAIL_POPUP",
        "v99n-seat-detail",
        "MuavinV99SeatDetailReload",
        "v99n-seat-bag-dot",
    ])

    print(("❌ V99O İZİ VAR  " if has else "✅ TEMİZ        ") + str(p))

print()
print("✅ V99O rollback bitti. Tarayıcıda /continue-trip?v=rollback ile yenile.")
