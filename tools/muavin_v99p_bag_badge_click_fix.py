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

print("===== V99P BAGAJ ROZETİ TIKLAMA FIX =====")

for p in [WEB_CSS, WEB_JS, AND_CSS, AND_JS]:
    if p.exists():
        bak = p.with_name(p.name + f".bak-v99p-bag-click-{STAMP}")
        shutil.copy2(p, bak)
        print("📦 backup:", bak)

if not WEB_CSS.exists():
    raise SystemExit("❌ CSS yok")

if not WEB_JS.exists():
    raise SystemExit("❌ JS yok")

css = WEB_CSS.read_text(encoding="utf-8", errors="ignore")
js = WEB_JS.read_text(encoding="utf-8", errors="ignore")

# Eski V99P bloğunu temizle
css = re.sub(
    r"\n?/\* V99P_BAG_BADGE_CLICK_FIX_START \*/.*?/\* V99P_BAG_BADGE_CLICK_FIX_END \*/\n?",
    "\n",
    css,
    flags=re.S
)

# 1) Rozet tıklamayı engellemesin
css += r'''

/* V99P_BAG_BADGE_CLICK_FIX_START */
.v99-seat-bag-dot,
.v99-seat-bag-dot *{
  pointer-events:none !important;
}
/* V99P_BAG_BADGE_CLICK_FIX_END */
'''

# 2) looksLikeSeatElement data-v99-seat-no da okusun
old = '''var dataNo = el.getAttribute("data-seat-no") || el.getAttribute("data-seat") || el.dataset.seatNo || "";'''
new = '''var dataNo = el.getAttribute("data-v99-seat-no") || el.getAttribute("data-seat-no") || el.getAttribute("data-seat") || el.dataset.seatNo || "";'''

if old in js:
    js = js.replace(old, new, 1)
    print("✅ looksLikeSeatElement data-v99-seat-no okumaya başladı")
elif 'el.getAttribute("data-v99-seat-no")' in js:
    print("✅ data-v99-seat-no zaten var")
else:
    print("⚠️ JS kalıbı bulunamadı, elle kontrol gerekebilir")

WEB_CSS.write_text(css, encoding="utf-8")
WEB_JS.write_text(js, encoding="utf-8")

print("✅ web CSS yazıldı")
print("✅ web JS yazıldı")

if AND_CSS.parent.exists():
    shutil.copy2(WEB_CSS, AND_CSS)
    print("✅ android CSS senkron")

if AND_JS.parent.exists():
    shutil.copy2(WEB_JS, AND_JS)
    print("✅ android JS senkron")

print()
print("===== KONTROL =====")
for p in [WEB_CSS, WEB_JS]:
    txt = p.read_text(encoding="utf-8", errors="ignore")
    print(p.name, "V99P:", "VAR" if "V99P_BAG_BADGE_CLICK_FIX" in txt or "data-v99-seat-no" in txt else "YOK")

print()
print("✅ V99P tamam. /continue-trip?v=v99p ile yenile.")
