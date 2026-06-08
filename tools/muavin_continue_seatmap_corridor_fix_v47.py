from pathlib import Path
from datetime import datetime
import shutil
import re

ROOT = Path(".").resolve()
STAMP = datetime.now().strftime("%Y%m%d-%H%M%S")

TPL_FILES = [
    ROOT / "templates/continue_trip.html",
    ROOT / "android_app/app/src/main/python/templates/continue_trip.html",
]

CSS_MAIN_FILES = [
    ROOT / "static/continue/continue_trip.css",
    ROOT / "android_app/app/src/main/python/static/continue/continue_trip.css",
]

CSS_PART_FILES = [
    ROOT / "static/continue/css_parts/74-seat-map-corridor-fix-v47.css",
    ROOT / "android_app/app/src/main/python/static/continue/css_parts/74-seat-map-corridor-fix-v47.css",
]

CSS = r'''
/* =========================================================
   CONTINUE_SEAT_MAP_CORRIDOR_FIX_V47
   Koridor çizgisi koltukların içine girdiği için kaldırıldı.
   Sadece görsel düzeltme.
========================================================= */

#continueSeatMapFullscreenV45 .v45-seatmap-corridor{
  display:none !important;
}

#continueSeatMapFullscreenV45 .v45-seatmap-board{
  background:
    radial-gradient(circle at 50% 0%, rgba(37,99,235,.18), transparent 32%),
    linear-gradient(180deg, rgba(15,23,42,.72), rgba(2,6,23,.74)) !important;
}

/* Koltukların daha temiz görünmesi için orta boşluğa hayalet çizgi ekleme yok.
   Bu modalda çizgisiz düzen daha düzgün duruyor. */
#continueSeatMapFullscreenV45 .v45-seat{
  z-index:2 !important;
}
'''

def backup(p):
    if p.exists():
        b = p.with_name(p.name + f".bak-corridor-fix-v47-{STAMP}")
        shutil.copy2(p, b)
        print("📦 Yedek:", b.relative_to(ROOT))

print("===== SEAT MAP CORRIDOR FIX V47 =====")

for p in CSS_PART_FILES:
    p.parent.mkdir(parents=True, exist_ok=True)
    backup(p)
    p.write_text(CSS.strip() + "\n", encoding="utf-8")
    print("✅ CSS yazıldı:", p.relative_to(ROOT))

for p in CSS_MAIN_FILES:
    if not p.exists():
        print("⚠️ Yok:", p.relative_to(ROOT))
        continue

    backup(p)
    s = p.read_text(encoding="utf-8", errors="ignore")

    lines = []
    for line in s.splitlines():
        if "74-seat-map-corridor-fix-v47.css" in line:
            continue
        lines.append(line)

    lines.append('@import url("./css_parts/74-seat-map-corridor-fix-v47.css");')
    p.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    print("✅ CSS import eklendi:", p.relative_to(ROOT))

for p in TPL_FILES:
    if not p.exists():
        print("⚠️ Yok:", p.relative_to(ROOT))
        continue

    backup(p)
    s = p.read_text(encoding="utf-8", errors="ignore")
    s = re.sub(r"continue_trip\.css'\) }}\?v=[^\"']+", "continue_trip.css') }}?v=seat-map-v47", s)
    s = re.sub(r'continue_trip\.css"\) }}\?v=[^"\']+', 'continue_trip.css") }}?v=seat-map-v47', s)
    p.write_text(s, encoding="utf-8")
    print("✅ Template cache V47:", p.relative_to(ROOT))

print()
print("✅ V47 koridor düzeltmesi tamam.")
