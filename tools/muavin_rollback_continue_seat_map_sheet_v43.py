from pathlib import Path
from datetime import datetime
import shutil
import re

ROOT = Path(".").resolve()
STAMP = datetime.now().strftime("%Y%m%d-%H%M%S")

APP_FILES = [
    ROOT / "app.py",
    ROOT / "android_app/app/src/main/python/app.py",
]

TPL_FILES = [
    ROOT / "templates/continue_trip.html",
    ROOT / "android_app/app/src/main/python/templates/continue_trip.html",
]

CORE_FILES = [
    ROOT / "static/continue/continue_trip_core.js",
    ROOT / "android_app/app/src/main/python/static/continue/continue_trip_core.js",
]

CSS_MAIN_FILES = [
    ROOT / "static/continue/continue_trip.css",
    ROOT / "android_app/app/src/main/python/static/continue/continue_trip.css",
]

CSS_PART_FILES = [
    ROOT / "static/continue/css_parts/70-seat-map-sheet-v43.css",
    ROOT / "android_app/app/src/main/python/static/continue/css_parts/70-seat-map-sheet-v43.css",
]

print("===== ROLLBACK CONTINUE SEAT MAP SHEET V43 =====")

def backup(p):
    b = p.with_name(p.name + f".bak-rollback-seat-map-v43-{STAMP}")
    shutil.copy2(p, b)
    print("📦 Yedek:", b.relative_to(ROOT))

# 1) app.py içinden API bloğunu kaldır
for p in APP_FILES:
    if not p.exists():
        print("⚠️ Yok:", p.relative_to(ROOT))
        continue

    backup(p)
    s = p.read_text(encoding="utf-8", errors="ignore")
    old = s

    s = re.sub(
        r'\n?# ===== CONTINUE_SEAT_MAP_SHEET_V43_API_START =====.*?# ===== CONTINUE_SEAT_MAP_SHEET_V43_API_END =====\n?',
        '\n',
        s,
        flags=re.S
    )

    p.write_text(s, encoding="utf-8")

    if s != old:
        print("✅ V43 API kaldırıldı:", p.relative_to(ROOT))
    else:
        print("ℹ️ V43 API yoktu:", p.relative_to(ROOT))

# 2) continue_trip.html içinden buton bağlantısını eski haline getir
for p in TPL_FILES:
    if not p.exists():
        print("⚠️ Yok:", p.relative_to(ROOT))
        continue

    backup(p)
    s = p.read_text(encoding="utf-8", errors="ignore")
    old = s

    s = s.replace(
        'class="dock-item" id="continueSeatMapBtn" data-seat-map-sheet="1" href="{{ url_for(\'seats_page\') }}"',
        'class="dock-item" href="{{ url_for(\'seats_page\') }}"'
    )

    s = s.replace(
        'class="dock-item" id="continueSeatMapBtn" data-seat-map-sheet="1" href="{{ url_for("seats_page") }}"',
        'class="dock-item" href="{{ url_for("seats_page") }}"'
    )

    s = re.sub(r'\s+id="continueSeatMapBtn"', '', s)
    s = re.sub(r'\s+data-seat-map-sheet="1"', '', s)

    # Sadece ilk alt menü yazısını eski hale getirir.
    s = s.replace("<span>Koltuklar</span>", "<span>Koltuk</span>", 1)

    # Cache versiyonlarını eski haline döndür.
    s = s.replace("continue_trip.css') }}?v=seat-map-v43", "continue_trip.css') }}?v=css-parts-1")
    s = s.replace('continue_trip.css") }}?v=seat-map-v43', 'continue_trip.css") }}?v=css-parts-1')
    s = s.replace("continue_trip_core.js') }}?v=seat-map-v43", "continue_trip_core.js') }}?v=core-split-1")
    s = s.replace('continue_trip_core.js") }}?v=seat-map-v43', 'continue_trip_core.js") }}?v=core-split-1')

    p.write_text(s, encoding="utf-8")

    if s != old:
        print("✅ Template V43 geri alındı:", p.relative_to(ROOT))
    else:
        print("ℹ️ Template içinde V43 izi yoktu:", p.relative_to(ROOT))

# 3) continue_trip_core.js içinden JS bloğunu kaldır
for p in CORE_FILES:
    if not p.exists():
        print("⚠️ Yok:", p.relative_to(ROOT))
        continue

    backup(p)
    s = p.read_text(encoding="utf-8", errors="ignore")
    old = s

    s = re.sub(
        r'\n?\s*/\* ===== CONTINUE_SEAT_MAP_SHEET_V43_START ===== \*/.*?/\* ===== CONTINUE_SEAT_MAP_SHEET_V43_END ===== \*/\n?',
        '\n',
        s,
        flags=re.S
    )

    p.write_text(s, encoding="utf-8")

    if s != old:
        print("✅ Core JS V43 kaldırıldı:", p.relative_to(ROOT))
    else:
        print("ℹ️ Core JS içinde V43 izi yoktu:", p.relative_to(ROOT))

# 4) CSS import kaldır
for p in CSS_MAIN_FILES:
    if not p.exists():
        print("⚠️ Yok:", p.relative_to(ROOT))
        continue

    backup(p)
    s = p.read_text(encoding="utf-8", errors="ignore")
    old = s

    lines = []
    for line in s.splitlines():
        if "70-seat-map-sheet-v43.css" in line:
            continue
        lines.append(line)

    s = "\n".join(lines).rstrip() + "\n"
    p.write_text(s, encoding="utf-8")

    if s != old:
        print("✅ CSS import kaldırıldı:", p.relative_to(ROOT))
    else:
        print("ℹ️ CSS import yoktu:", p.relative_to(ROOT))

# 5) CSS dosyasını sil
for p in CSS_PART_FILES:
    if p.exists():
        p.unlink()
        print("🗑️ Silindi:", p.relative_to(ROOT))
    else:
        print("ℹ️ Zaten yok:", p.relative_to(ROOT))

print()
print("===== KONTROL =====")
hits = 0
CHECK = APP_FILES + TPL_FILES + CORE_FILES + CSS_MAIN_FILES + CSS_PART_FILES

for p in CHECK:
    if not p.exists():
        continue

    txt = p.read_text(encoding="utf-8", errors="ignore")
    c = (
        txt.count("CONTINUE_SEAT_MAP_SHEET_V43") +
        txt.count("api/live-seat-map") +
        txt.count("continueSeatMapBtn") +
        txt.count("70-seat-map-sheet-v43") +
        txt.count("v43-seatmap")
    )
    hits += c
    print(p.relative_to(ROOT), "V43 iz:", c)

print()
if hits == 0:
    print("✅ V43 tamamen geri alındı.")
else:
    print("⚠️ Hâlâ V43 izi var:", hits)
