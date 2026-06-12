from pathlib import Path
from datetime import datetime
import shutil
import re
import subprocess

ROOT = Path(".").resolve()
STAMP = datetime.now().strftime("%Y%m%d-%H%M%S")

WEB_TPL = ROOT / "templates/continue_trip.html"
AND_TPL = ROOT / "android_app/app/src/main/python/templates/continue_trip.html"

WEB_JS = ROOT / "static/continue/continue_trip_v99_clean.js"
AND_JS = ROOT / "android_app/app/src/main/python/static/continue/continue_trip_v99_clean.js"

WEB_CSS = ROOT / "static/continue/continue_trip_v99_clean.css"
AND_CSS = ROOT / "android_app/app/src/main/python/static/continue/continue_trip_v99_clean.css"

print("===== V99ZA / V99Z HIZ TOGGLE GERİ AL =====")

for p in [WEB_TPL, AND_TPL, WEB_JS, AND_JS, WEB_CSS, AND_CSS]:
    if p.exists():
        bak = p.with_name(p.name + f".bak-before-speed-rollback-{STAMP}")
        shutil.copy2(p, bak)
        print("📦 backup:", bak)

if not WEB_TPL.exists():
    raise SystemExit("❌ template yok")
if not WEB_JS.exists():
    raise SystemExit("❌ JS yok")
if not WEB_CSS.exists():
    raise SystemExit("❌ CSS yok")

# 1) Template cache satırını temiz bir sürüme al
tpl = WEB_TPL.read_text(encoding="utf-8", errors="ignore")

clean_script = """<script src="{{ url_for('static', filename='continue/continue_trip_v99_clean.js') }}?v=v99speed-rollback-{{ trip['id'] }}"></script>"""

tpl2, n_tpl = re.subn(
    r'''<script src="\{\{\s*url_for\('static',\s*filename='continue/continue_trip_v99_clean\.js'\)\s*\}\}\?v=[^"]*"></script>''',
    clean_script,
    tpl,
    count=1
)

WEB_TPL.write_text(tpl2, encoding="utf-8")
print("✅ template cache satırı temizlendi:", n_tpl)

# 2) JS içinden hız analog/dijital bloklarını kaldır
js = WEB_JS.read_text(encoding="utf-8", errors="ignore")

for start, end in [
    ("V99Z_SPEED_ANALOG_TOGGLE_START", "V99Z_SPEED_ANALOG_TOGGLE_END"),
    ("V99ZA_SPEED_TOGGLE_START", "V99ZA_SPEED_TOGGLE_END"),
]:
    js, n = re.subn(
        rf"\n?/\* {start} \*/.*?/\* {end} \*/\n?",
        "\n",
        js,
        flags=re.S
    )
    print(f"✅ JS temizle {start}: {n}")

WEB_JS.write_text(js, encoding="utf-8")

# 3) CSS içinden hız analog/dijital bloklarını kaldır
css = WEB_CSS.read_text(encoding="utf-8", errors="ignore")

for start, end in [
    ("V99Z_SPEED_ANALOG_TOGGLE_CSS_START", "V99Z_SPEED_ANALOG_TOGGLE_CSS_END"),
    ("V99ZA_SPEED_TOGGLE_CSS_START", "V99ZA_SPEED_TOGGLE_CSS_END"),
]:
    css, n = re.subn(
        rf"\n?/\* {start} \*/.*?/\* {end} \*/\n?",
        "\n",
        css,
        flags=re.S
    )
    print(f"✅ CSS temizle {start}: {n}")

WEB_CSS.write_text(css, encoding="utf-8")

# 4) Android sync
if AND_TPL.parent.exists():
    shutil.copy2(WEB_TPL, AND_TPL)
    print("✅ android template senkron")

if AND_JS.parent.exists():
    shutil.copy2(WEB_JS, AND_JS)
    print("✅ android JS senkron")

if AND_CSS.parent.exists():
    shutil.copy2(WEB_CSS, AND_CSS)
    print("✅ android CSS senkron")

print()
print("===== NODE JS SYNTAX CHECK =====")
try:
    res = subprocess.run(["node", "--check", str(WEB_JS)], capture_output=True, text=True)
    if res.returncode == 0:
        print("✅ JS syntax OK")
    else:
        print("❌ JS syntax HATA")
        print(res.stdout)
        print(res.stderr)
except FileNotFoundError:
    print("ℹ️ node yok, syntax check atlandı")

print()
print("===== KONTROL =====")

tpl_now = WEB_TPL.read_text(encoding="utf-8", errors="ignore")
js_now = WEB_JS.read_text(encoding="utf-8", errors="ignore")
css_now = WEB_CSS.read_text(encoding="utf-8", errors="ignore")

checks = [
    ("V99ZA JS kaldırıldı", "V99ZA_SPEED_TOGGLE_START" not in js_now),
    ("V99Z JS kaldırıldı", "V99Z_SPEED_ANALOG_TOGGLE_START" not in js_now),
    ("V99ZA CSS kaldırıldı", "V99ZA_SPEED_TOGGLE_CSS_START" not in css_now),
    ("V99Z CSS kaldırıldı", "V99Z_SPEED_ANALOG_TOGGLE_CSS_START" not in css_now),
    ("speed API kaldırıldı", "MuavinV99ZASpeedToggle" not in js_now and "MuavinV99SpeedToggle" not in js_now),
    ("Doluluk paneli duruyor", "V99M_OCCUPANCY_PANEL_START" in js_now),
    ("Koltuk renkleri duruyor", "V99O_SEAT_GENDER_SELECTED_JS_START" in js_now),
    ("Template temiz cache", "v99speed-rollback" in tpl_now),
]

for name, ok in checks:
    print(("✅ " if ok else "❌ ") + name)

print()
print("===== SCRIPT SATIRI =====")
for i, line in enumerate(tpl_now.splitlines(), 1):
    if "continue_trip_v99_clean.js" in line:
        print(f"{i}: {line}")

print()
print("✅ Hız analog/dijital işlemi geri alındı.")
print("Yenile:")
print("http://127.0.0.1:5000/continue-trip?v=v99speed-rollback")
