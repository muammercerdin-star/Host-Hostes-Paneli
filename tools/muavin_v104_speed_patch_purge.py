from pathlib import Path
from datetime import datetime
import shutil
import re
import hashlib
import subprocess

ROOT = Path(".").resolve()
STAMP = datetime.now().strftime("%Y%m%d-%H%M%S")

WEB_TPL = ROOT / "templates/continue_trip.html"
AND_TPL = ROOT / "android_app/app/src/main/python/templates/continue_trip.html"

WEB_V99_JS = ROOT / "static/continue/continue_trip_v99_clean.js"
AND_V99_JS = ROOT / "android_app/app/src/main/python/static/continue/continue_trip_v99_clean.js"

WEB_V99_CSS = ROOT / "static/continue/continue_trip_v99_clean.css"
AND_V99_CSS = ROOT / "android_app/app/src/main/python/static/continue/continue_trip_v99_clean.css"

SPEED_FILES = [
    ROOT / "static/continue/continue_speed_toggle_v100.js",
    ROOT / "static/continue/continue_speed_toggle_v100.css",
    ROOT / "static/continue/continue_speed_widget_v101.js",
    ROOT / "static/continue/continue_speed_widget_v101.css",
    ROOT / "static/continue/continue_speed_overlay_v102.js",
    ROOT / "static/continue/continue_speed_overlay_v102.css",
    ROOT / "static/continue/continue_speed_bar_v103.js",
    ROOT / "static/continue/continue_speed_bar_v103.css",

    ROOT / "android_app/app/src/main/python/static/continue/continue_speed_toggle_v100.js",
    ROOT / "android_app/app/src/main/python/static/continue/continue_speed_toggle_v100.css",
    ROOT / "android_app/app/src/main/python/static/continue/continue_speed_widget_v101.js",
    ROOT / "android_app/app/src/main/python/static/continue/continue_speed_widget_v101.css",
    ROOT / "android_app/app/src/main/python/static/continue/continue_speed_overlay_v102.js",
    ROOT / "android_app/app/src/main/python/static/continue/continue_speed_overlay_v102.css",
    ROOT / "android_app/app/src/main/python/static/continue/continue_speed_bar_v103.js",
    ROOT / "android_app/app/src/main/python/static/continue/continue_speed_bar_v103.css",
]

print("===== V104 HIZ YAMA TEMİZLİĞİ =====")
print("ROOT:", ROOT)

def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()[:12] if p.exists() else "-"

def backup(p):
    if p.exists():
        bak = p.with_name(p.name + f".bak-v104-speed-purge-{STAMP}")
        shutil.copy2(p, bak)
        print("📦 backup:", bak)

for p in [WEB_TPL, AND_TPL, WEB_V99_JS, AND_V99_JS, WEB_V99_CSS, AND_V99_CSS]:
    backup(p)

# 1) Template içinden bütün hız denemesi link/script çağrılarını kaldır
speed_names = [
    "continue_speed_toggle_v100",
    "continue_speed_widget_v101",
    "continue_speed_overlay_v102",
    "continue_speed_bar_v103",
]

for tpl in [WEB_TPL, AND_TPL]:
    if not tpl.exists():
        print("❌ template yok:", tpl)
        continue

    s = tpl.read_text(encoding="utf-8", errors="ignore")
    old = s

    for name in speed_names:
        s = re.sub(rf'\n?\s*<link[^>]+{name}\.css[^>]*>\s*', "\n", s)
        s = re.sub(rf'\n?\s*<script[^>]+{name}\.js[^>]*></script>\s*', "\n", s)

    # Ana V99 JS cache'i temiz sürüme çek
    clean_script = """<script src="{{ url_for('static', filename='continue/continue_trip_v99_clean.js') }}?v=v104-speed-purge-{{ trip['id'] }}"></script>"""
    s, n = re.subn(
        r'''<script src="\{\{\s*url_for\('static',\s*filename='continue/continue_trip_v99_clean\.js'\)\s*\}\}\?v=[^"]*"></script>''',
        clean_script,
        s,
        count=1
    )

    tpl.write_text(s, encoding="utf-8")
    print("✅ template temizlendi:", tpl, "changed=", s != old, "v99_script_fix=", n)

# 2) Ana V99 JS içine gömülmüş eski hız blokları varsa temizle
for js_path in [WEB_V99_JS, AND_V99_JS]:
    if not js_path.exists():
        continue

    s = js_path.read_text(encoding="utf-8", errors="ignore")
    old = s

    blocks = [
        ("V99Z_SPEED_ANALOG_TOGGLE_START", "V99Z_SPEED_ANALOG_TOGGLE_END"),
        ("V99ZA_SPEED_TOGGLE_START", "V99ZA_SPEED_TOGGLE_END"),
        ("V100_SPEED_TOGGLE_ISOLATED_START", "V100_SPEED_TOGGLE_ISOLATED_END"),
        ("V101_SPEED_WIDGET_START", "V101_SPEED_WIDGET_END"),
        ("V102_SPEED_OVERLAY_START", "V102_SPEED_OVERLAY_END"),
        ("V103_SPEED_BAR_CLEAN_START", "V103_SPEED_BAR_CLEAN_END"),
    ]

    for a, b in blocks:
        s = re.sub(rf"\n?/\* {a} \*/.*?/\* {b} \*/\n?", "\n", s, flags=re.S)

    js_path.write_text(s, encoding="utf-8")
    print("✅ ana JS hız blok kontrol:", js_path, "changed=", s != old)

# 3) Ana V99 CSS içine gömülmüş hız blokları varsa temizle
for css_path in [WEB_V99_CSS, AND_V99_CSS]:
    if not css_path.exists():
        continue

    s = css_path.read_text(encoding="utf-8", errors="ignore")
    old = s

    blocks = [
        ("V99Z_SPEED_ANALOG_TOGGLE_CSS_START", "V99Z_SPEED_ANALOG_TOGGLE_CSS_END"),
        ("V99ZA_SPEED_TOGGLE_CSS_START", "V99ZA_SPEED_TOGGLE_CSS_END"),
        ("V100_SPEED_TOGGLE_ISOLATED_CSS_START", "V100_SPEED_TOGGLE_ISOLATED_CSS_END"),
        ("V101_SPEED_WIDGET_START", "V101_SPEED_WIDGET_END"),
        ("V102_SPEED_OVERLAY_START", "V102_SPEED_OVERLAY_END"),
        ("V102A_SPEED_OVERLAY_TUNE_START", "V102A_SPEED_OVERLAY_TUNE_END"),
        ("V102B_SPEED_OVERLAY_FINAL_TUNE_START", "V102B_SPEED_OVERLAY_FINAL_TUNE_END"),
        ("V103_SPEED_BAR_CLEAN_START", "V103_SPEED_BAR_CLEAN_END"),
    ]

    for a, b in blocks:
        s = re.sub(rf"\n?/\* {a} \*/.*?/\* {b} \*/\n?", "\n", s, flags=re.S)

    css_path.write_text(s, encoding="utf-8")
    print("✅ ana CSS hız blok kontrol:", css_path, "changed=", s != old)

# 4) Ayrı hız dosyalarını pasifleştir
for p in SPEED_FILES:
    if p.exists():
        disabled = p.with_name(p.name + f".disabled-v104-{STAMP}")
        shutil.move(str(p), str(disabled))
        print("✅ pasifleştirildi:", disabled)

# 5) Web -> Android ana dosya senkronu
if WEB_TPL.exists() and AND_TPL.parent.exists():
    shutil.copy2(WEB_TPL, AND_TPL)
    print("✅ Android template web ile eşitlendi")

if WEB_V99_JS.exists() and AND_V99_JS.parent.exists():
    shutil.copy2(WEB_V99_JS, AND_V99_JS)
    print("✅ Android V99 JS web ile eşitlendi")

if WEB_V99_CSS.exists() and AND_V99_CSS.parent.exists():
    shutil.copy2(WEB_V99_CSS, AND_V99_CSS)
    print("✅ Android V99 CSS web ile eşitlendi")

print()
print("===== JS SYNTAX CHECK =====")
try:
    res = subprocess.run(["node", "--check", str(WEB_V99_JS)], capture_output=True, text=True)
    if res.returncode == 0:
        print("✅ V99 JS syntax OK")
    else:
        print("❌ V99 JS syntax HATA")
        print(res.stdout)
        print(res.stderr)
except FileNotFoundError:
    print("ℹ️ node yok, atlandı")

print()
print("===== KONTROL =====")

tpl = WEB_TPL.read_text(encoding="utf-8", errors="ignore") if WEB_TPL.exists() else ""
v99js = WEB_V99_JS.read_text(encoding="utf-8", errors="ignore") if WEB_V99_JS.exists() else ""
v99css = WEB_V99_CSS.read_text(encoding="utf-8", errors="ignore") if WEB_V99_CSS.exists() else ""

bad_terms = [
    "continue_speed_toggle_v100",
    "continue_speed_widget_v101",
    "continue_speed_overlay_v102",
    "continue_speed_bar_v103",
    "V99Z_SPEED_ANALOG",
    "V99ZA_SPEED_TOGGLE",
    "V100_SPEED_TOGGLE",
    "V101_SPEED_WIDGET",
    "V102_SPEED_OVERLAY",
    "V102A_SPEED_OVERLAY",
    "V102B_SPEED_OVERLAY",
    "V103_SPEED_BAR",
    "MuavinV100SpeedToggle",
    "MuavinV101SpeedWidget",
    "MuavinV102SpeedOverlay",
    "MuavinV103SpeedBar",
]

alltxt = tpl + "\n" + v99js + "\n" + v99css

for term in bad_terms:
    print(("❌ KALMIŞ  " if term in alltxt else "✅ TEMİZ   ") + term)

print()
print("KORUNAN ÖNEMLİ MARKERLAR:")
keep = [
    "V99M_OCCUPANCY_PANEL_START",
    "V99O_SEAT_GENDER_SELECTED_JS_START",
    "V99P_BAG_BADGE_CLICK_FIX_START",
    "V99L_RING_LINE_PULSE",
]
for term in keep:
    print(("✅ VAR     " if term in alltxt else "⚠️ YOK     ") + term)

print()
print("===== TEMPLATE AKTİF SATIRLAR =====")
for i, line in enumerate(tpl.splitlines(), 1):
    if "continue_trip_v99_clean.js" in line or "continue_speed_" in line:
        print(f"{i}: {line}")

print()
print("===== SHA =====")
pairs = [
    ("template", WEB_TPL, AND_TPL),
    ("v99 js", WEB_V99_JS, AND_V99_JS),
    ("v99 css", WEB_V99_CSS, AND_V99_CSS),
]
for label, a, b in pairs:
    if a.exists() and b.exists():
        print(f"{label}: {'AYNI' if sha(a)==sha(b) else 'FARKLI'} web={sha(a)} android={sha(b)}")

print()
print("✅ Hız kutusundaki V100/V101/V102/V103 yamaları temizlendi.")
print("Aç:")
print("http://127.0.0.1:5000/continue-trip?v=v104-speed-purge")
