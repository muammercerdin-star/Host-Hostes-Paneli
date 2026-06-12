from pathlib import Path
from datetime import datetime
import shutil
import re

ROOT = Path(".").resolve()
STAMP = datetime.now().strftime("%Y%m%d-%H%M%S")

WEB_CSS = ROOT / "static/continue/continue_trip_v99_clean.css"
WEB_JS  = ROOT / "static/continue/continue_trip_v99_clean.js"

AND_CSS = ROOT / "android_app/app/src/main/python/static/continue/continue_trip_v99_clean.css"
AND_JS  = ROOT / "android_app/app/src/main/python/static/continue/continue_trip_v99_clean.js"

print("===== V99L RING CIZGI PULSE FIX =====")

for p in [WEB_CSS, WEB_JS, AND_CSS, AND_JS]:
    if p.exists():
        bak = p.with_name(p.name + f".bak-v99l-{STAMP}")
        shutil.copy2(p, bak)
        print("📦 backup:", bak)

if not WEB_CSS.exists():
    raise SystemExit("❌ CSS yok: " + str(WEB_CSS))

if not WEB_JS.exists():
    raise SystemExit("❌ JS yok: " + str(WEB_JS))

css = WEB_CSS.read_text(encoding="utf-8", errors="ignore")
js = WEB_JS.read_text(encoding="utf-8", errors="ignore")

# Eski V99L bloğu varsa temizle
css = re.sub(
    r"\n?/\* V99L_RING_LINE_PULSE_START \*/.*?/\* V99L_RING_LINE_PULSE_END \*/\n?",
    "\n",
    css,
    flags=re.S
)

# Kare gibi görünen glow'u öldür, pulse'u sadece ring çizgisine taşı.
css += r'''

/* V99L_RING_LINE_PULSE_START */

/* Kare/parça glow olmasın: ışık sadece SVG çizgisinde hissedilsin */
.v99-ring-wrap,
.v99-ring-svg,
.v99-ring-center{
  filter:none !important;
  box-shadow:none !important;
}

/* JS inline drop-shadow yazsa bile çizgi filter kullanmasın */
.v99-ring-fill{
  filter:none !important;
  transform-origin:center !important;
  transition:
    stroke .25s ease,
    stroke-dashoffset .35s ease,
    stroke-width .25s ease,
    opacity .25s ease !important;
}

/* Yakın mesafe pulse: çizginin kendisi nefes alsın */
.v99-ring-fill.urgent{
  filter:none !important;
  animation:v99l-ring-line-pulse 1.05s ease-in-out infinite !important;
}

@keyframes v99l-ring-line-pulse{
  0%,100%{
    stroke-width:8;
    opacity:.88;
  }
  50%{
    stroke-width:12;
    opacity:1;
  }
}

/* Yazı sabit kalsın, sadece renk/glow sabit olsun */
.v99-ring-km,
#ringKm{
  animation:none !important;
}

/* V99L_RING_LINE_PULSE_END */
'''

# JS tarafında stroke renkleri kalsın, drop-shadow filter'ları none olsun.
replacements = [
    ('ring.style.filter = "drop-shadow(0 0 4px #5a6478)";', 'ring.style.filter = "none";'),
    ('ring.style.filter = "drop-shadow(0 0 8px #e03030)";', 'ring.style.filter = "none";'),
    ('ring.style.filter = "drop-shadow(0 0 8px #e08820)";', 'ring.style.filter = "none";'),
    ('ring.style.filter = "drop-shadow(0 0 6px #3a8bff)";', 'ring.style.filter = "none";'),
]

changed = []
for old, new in replacements:
    if old in js:
        js = js.replace(old, new)
        changed.append(old)

WEB_CSS.write_text(css, encoding="utf-8")
WEB_JS.write_text(js, encoding="utf-8")

print("✅ web CSS yazıldı:", WEB_CSS)
print("✅ web JS yazıldı:", WEB_JS)

if AND_CSS.parent.exists():
    AND_CSS.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(WEB_CSS, AND_CSS)
    print("✅ android CSS senkron:", AND_CSS)

if AND_JS.parent.exists():
    AND_JS.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(WEB_JS, AND_JS)
    print("✅ android JS senkron:", AND_JS)

print()
print("===== KONTROL =====")
css2 = WEB_CSS.read_text(encoding="utf-8", errors="ignore")
js2 = WEB_JS.read_text(encoding="utf-8", errors="ignore")

for key in [
    "V99L_RING_LINE_PULSE_START",
    "v99l-ring-line-pulse",
    ".v99-ring-fill.urgent",
]:
    print(("CSS VAR  " if key in css2 else "CSS YOK  ") + key)

for key in [
    "#e03030",
    "#e08820",
    "#3a8bff",
    "ring.classList.add(\"urgent\")",
    "ring.style.filter = \"none\"",
    "drop-shadow(0 0 8px #e03030)",
]:
    print(("JS  VAR  " if key in js2 else "JS  YOK  ") + key)

print()
print("DEĞİŞEN FILTER SATIRI:", len(changed))
print("✅ V99L tamam. Tarayıcıda /continue-trip?v=v99l ile yenile.")
