from pathlib import Path
from datetime import datetime
import shutil
import re

ROOT = Path(".").resolve()
STAMP = datetime.now().strftime("%Y%m%d-%H%M%S")

WEB_TPL = ROOT / "templates/continue_trip.html"
AND_TPL = ROOT / "android_app/app/src/main/python/templates/continue_trip.html"

WEB_JS = ROOT / "static/continue/continue_trip_v99_clean.js"
AND_JS = ROOT / "android_app/app/src/main/python/static/continue/continue_trip_v99_clean.js"

print("===== V99W DOLULUK GERCEK FIX =====")

for p in [WEB_TPL, AND_TPL, WEB_JS, AND_JS]:
    if p.exists():
        bak = p.with_name(p.name + f".bak-v99w-doluluk-real-fix-{STAMP}")
        shutil.copy2(p, bak)
        print("📦 backup:", bak)

if not WEB_TPL.exists():
    raise SystemExit("❌ template yok")

if not WEB_JS.exists():
    raise SystemExit("❌ JS yok")

# 1) Bozuk script satırını temizle
tpl = WEB_TPL.read_text(encoding="utf-8", errors="ignore")
old_tpl = tpl

tpl = re.sub(
    r'''<script src="\{\{\s*url_for\('static',\s*filename='continue/continue_trip_v99_clean\.js'\)\s*\}\}\?v=[^"]*"></script>''',
    '''<script src="{{ url_for('static', filename='continue/continue_trip_v99_clean.js') }}?v=v99w-{{ trip['id'] }}"></script>''',
    tpl
)

if tpl != old_tpl:
    WEB_TPL.write_text(tpl, encoding="utf-8")
    print("✅ template script satırı düzeltildi")
else:
    print("⚠️ template script satırı değişmedi, kalıp bulunamadı")

# 2) JS içinde .v99-gauge-cell hedefini ekle
js = WEB_JS.read_text(encoding="utf-8", errors="ignore")
old_js = js

selector_old = ".v99-gauge, .v99-stat, .v99-top-stat, .v99-info-cell, .v99-stat-card"
selector_new = ".v99-gauge-cell, .v99-gauge, .v99-stat, .v99-top-stat, .v99-info-cell, .v99-stat-card"

js = js.replace(selector_old, selector_new)

# Tekrarlı eklenmeyi temizle
js = js.replace(".v99-gauge-cell, .v99-gauge-cell,", ".v99-gauge-cell,")

if js != old_js:
    WEB_JS.write_text(js, encoding="utf-8")
    print("✅ JS doluluk hedefi düzeltildi: .v99-gauge-cell eklendi")
else:
    print("⚠️ JS değişmedi, selector zaten düzeltilmiş olabilir")

# Android sync
if AND_TPL.parent.exists():
    shutil.copy2(WEB_TPL, AND_TPL)
    print("✅ android template senkron")

if AND_JS.parent.exists():
    shutil.copy2(WEB_JS, AND_JS)
    print("✅ android JS senkron")

print()
print("===== KONTROL =====")

tpl2 = WEB_TPL.read_text(encoding="utf-8", errors="ignore")
js2 = WEB_JS.read_text(encoding="utf-8", errors="ignore")

for key in [
    "v99w-{{ trip['id'] }}",
    "}}'id']",
    ".v99-gauge-cell",
    "return labelText === \"DOLULUK\"",
    "V99M_OCCUPANCY_PANEL_START",
    "V99Q_ONLY_OCCUPANCY_CLICK_START",
]:
    source = tpl2 if "trip" in key or "}}'id']" in key else js2
    print(("VAR  " if key in source else "YOK  ") + key)

print()
print("===== SCRIPT SATIRI =====")
for i, line in enumerate(tpl2.splitlines(), 1):
    if "continue_trip_v99_clean.js" in line:
        print(f"{i}: {line}")

print()
print("===== JS SELECTOR SATIRLARI =====")
for i, line in enumerate(js2.splitlines(), 1):
    if ".v99-gauge-cell" in line or "return labelText" in line:
        print(f"{i}: {line[:220]}")

print()
print("✅ V99W fix tamam. /continue-trip?v=v99w-fixed ile yenile.")
