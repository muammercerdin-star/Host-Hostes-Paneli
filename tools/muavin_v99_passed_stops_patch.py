from pathlib import Path
from datetime import datetime
import shutil
import re

ROOT = Path(".").resolve()
STAMP = datetime.now().strftime("%Y%m%d-%H%M%S")

APP = ROOT / "app.py"
AND_APP = ROOT / "android_app/app/src/main/python/app.py"

TPL = ROOT / "templates/continue_trip.html"
AND_TPL = ROOT / "android_app/app/src/main/python/templates/continue_trip.html"

CSS = ROOT / "static/continue/continue_trip_v99_clean.css"
AND_CSS = ROOT / "android_app/app/src/main/python/static/continue/continue_trip_v99_clean.css"

print("===== V99 PASSED STOPS PATCH =====")

for p in [APP, AND_APP, TPL, AND_TPL, CSS, AND_CSS]:
    if p.exists():
        bak = p.with_name(p.name + f".bak-v99-passed-{STAMP}")
        shutil.copy2(p, bak)
        print("📦 backup:", bak)

if not APP.exists():
    raise SystemExit("❌ app.py yok")

s = APP.read_text(encoding="utf-8", errors="ignore")
old = s

target = 'selected_stops = stops[show_start:show_start + 4] if stops else []'
replacement = '''# V99_PASSED_STOPS_START
    # Canlı güzergah listesinde sadece canlı/sonraki değil,
    # örnekteki gibi son geçilen duraklar da yeşil kart olarak görünsün.
    if stops and current_index is not None and current_index >= 0:
        v99_before = 4
        v99_after = 4
        show_start = max(0, current_index - v99_before)
        show_end = min(len(stops), current_index + v99_after)
        selected_stops = stops[show_start:show_end]
    else:
        selected_stops = stops[show_start:show_start + 4] if stops else []
    # V99_PASSED_STOPS_END'''

if target not in s:
    print("❌ hedef satır bulunamadı:", target)
    raise SystemExit(1)

s = s.replace(target, replacement, 1)
APP.write_text(s, encoding="utf-8")
print("✅ app.py geçmiş durak penceresi eklendi")

# Android app.py senkron
if AND_APP.parent.exists():
    AND_APP.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(APP, AND_APP)
    print("✅ android app.py senkron:", AND_APP)

# Template: passed-card class desteği
if TPL.exists():
    t = TPL.read_text(encoding="utf-8", errors="ignore")
    before = t

    t = t.replace(
        '{% if stop.kind == "live" %}live-card{% elif stop.kind == "next" %}next-card{% endif %}',
        '{% if stop.kind == "live" %}live-card{% elif stop.kind == "next" %}next-card{% elif stop.kind == "passed" %}passed-card{% endif %}'
    )

    if t != before:
        TPL.write_text(t, encoding="utf-8")
        print("✅ template passed-card class eklendi")
    else:
        print("⚠️ template class hedefi bulunamadı veya zaten değişmiş")

    if AND_TPL.parent.exists():
        AND_TPL.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(TPL, AND_TPL)
        print("✅ android template senkron")

# CSS: yeşil geçmiş kart border/background
if CSS.exists():
    c = CSS.read_text(encoding="utf-8", errors="ignore")
    c = re.sub(r"/\* V99_PASSED_CARD_STYLE_START \*/.*?/\* V99_PASSED_CARD_STYLE_END \*/", "", c, flags=re.S)

    c += r'''

/* V99_PASSED_CARD_STYLE_START */
.v99-tl-card.passed-card{
  border-color:#1db87a55 !important;
  background:linear-gradient(180deg, rgba(10,36,24,.42), rgba(18,21,26,.92)) !important;
}

.v99-tl-card.passed-card .v99-tl-stop-name{
  color:#dceee7 !important;
}

.v99-tl-card.passed-card .v99-tl-m-val{
  color:#d8eee5 !important;
}

.v99-tl-card.passed-card .v99-tl-m-lbl{
  color:#658d7d !important;
}
/* V99_PASSED_CARD_STYLE_END */
'''
    CSS.write_text(c, encoding="utf-8")
    print("✅ CSS passed-card yeşil stil eklendi")

    if AND_CSS.parent.exists():
        AND_CSS.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(CSS, AND_CSS)
        print("✅ android css senkron")

print()
print("===== KONTROL =====")
app_txt = APP.read_text(encoding="utf-8", errors="ignore")
tpl_txt = TPL.read_text(encoding="utf-8", errors="ignore") if TPL.exists() else ""
css_txt = CSS.read_text(encoding="utf-8", errors="ignore") if CSS.exists() else ""

for key, txt in [
    ("V99_PASSED_STOPS_START", app_txt),
    ("passed-card", tpl_txt),
    ("V99_PASSED_CARD_STYLE_START", css_txt),
]:
    print(("VAR  " if key in txt else "YOK  ") + key)

print()
print("✅ V99 passed stops patch tamam")
