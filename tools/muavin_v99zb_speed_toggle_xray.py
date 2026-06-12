from pathlib import Path
from datetime import datetime
import hashlib
import re
import sys
import subprocess
import shutil

ROOT = Path(".").resolve()

WEB_TPL = ROOT / "templates/continue_trip.html"
WEB_JS = ROOT / "static/continue/continue_trip_v99_clean.js"
WEB_CSS = ROOT / "static/continue/continue_trip_v99_clean.css"

AND_TPL = ROOT / "android_app/app/src/main/python/templates/continue_trip.html"
AND_JS = ROOT / "android_app/app/src/main/python/static/continue/continue_trip_v99_clean.js"
AND_CSS = ROOT / "android_app/app/src/main/python/static/continue/continue_trip_v99_clean.css"

print("===== V99ZB HIZ ANALOG TOGGLE RÖNTGEN =====")
print("ROOT:", ROOT)
print("TIME:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
print("NOT: Bu script dosya değiştirmez.")

def read(p):
    return p.read_text(encoding="utf-8", errors="ignore") if p.exists() else ""

def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()[:12] if p.exists() else "-"

def section(t):
    print()
    print("===== " + t + " =====")

def print_hits(title, txt, keys, pad=8, max_hits=80):
    section(title)
    lines = txt.splitlines()
    hits = []
    for i, line in enumerate(lines, 1):
        low = line.lower()
        if any(k.lower() in low for k in keys):
            hits.append(i)

    print("HIT_COUNT:", len(hits))
    shown = set()
    for i in hits[:max_hits]:
        for n in range(max(1, i-pad), min(len(lines), i+pad)+1):
            if n in shown:
                continue
            shown.add(n)
            print(f"{n:5}: {lines[n-1][:260]}")
        print("-----")

    if len(hits) > max_hits:
        print("... kesildi")

section("1) DOSYA DURUMU")
for name, p in [
    ("WEB_TPL", WEB_TPL),
    ("WEB_JS", WEB_JS),
    ("WEB_CSS", WEB_CSS),
    ("AND_TPL", AND_TPL),
    ("AND_JS", AND_JS),
    ("AND_CSS", AND_CSS),
]:
    print(f"{name:8} {'VAR' if p.exists() else 'YOK'} size={p.stat().st_size if p.exists() else '-':<8} sha={sha(p)} {p}")

section("2) WEB / ANDROID SENKRON")
for label, a, b in [
    ("template", WEB_TPL, AND_TPL),
    ("js", WEB_JS, AND_JS),
    ("css", WEB_CSS, AND_CSS),
]:
    if a.exists() and b.exists():
        print(f"{label:10} {'AYNI' if sha(a)==sha(b) else 'FARKLI'} web={sha(a)} android={sha(b)}")
    else:
        print(f"{label:10} kontrol edilemedi")

tpl = read(WEB_TPL)
js = read(WEB_JS)
css = read(WEB_CSS)

section("3) HIZ TOGGLE MARKER KONTROLÜ")
markers = [
    "V99Z_SPEED_ANALOG_TOGGLE_START",
    "V99Z_SPEED_ANALOG_TOGGLE_CSS_START",
    "V99ZA_SPEED_TOGGLE_START",
    "V99ZA_SPEED_TOGGLE_CSS_START",
    "MuavinV99SpeedToggle",
    "MuavinV99ZASpeedToggle",
    "v99z-speed-card",
    "v99za-speed-card",
]
for m in markers:
    print(("VAR  " if m in js or m in css or m in tpl else "YOK  ") + m)

if "V99ZA_SPEED_TOGGLE_START" not in js and "V99Z_SPEED_ANALOG_TOGGLE_START" not in js:
    print()
    print("SONUÇ: Şu an aktif HIZ analog toggle JS bloğu görünmüyor.")
    print("Rollback çalıştıysa mevcut dosyada analog hızın çalışmaması normal.")
else:
    print()
    print("SONUÇ: HIZ analog toggle bloğu mevcut. Neden çalışmadığını aşağıda arıyoruz.")

section("4) TEMPLATE SCRIPT CACHE SATIRI")
for i, line in enumerate(tpl.splitlines(), 1):
    if "continue_trip_v99_clean.js" in line:
        print(f"{i}: {line}")

if "v99za-speed" in tpl:
    print("✅ Template v99za-speed cache ile çağırıyor.")
elif "v99speed-rollback" in tpl:
    print("ℹ️ Template rollback cache ile çağırıyor. Bu durumda hız toggle silinmiş olabilir.")
else:
    print("⚠️ Template başka cache sürümüyle çağırıyor.")

section("5) RENDER HTML TEST")
render_html = ""
try:
    sys.path.insert(0, str(ROOT))
    from app import app

    out = ROOT / "run_logs" / "v99zb_speed_toggle_render.html"
    out.parent.mkdir(exist_ok=True)

    with app.test_client() as c:
        with c.session_transaction() as sess:
            sess["auth_ok"] = True

        r = c.get("/continue-trip?v=v99zb_xray", follow_redirects=False)
        render_html = r.get_data().decode("utf-8", errors="ignore")
        out.write_text(render_html, encoding="utf-8")

        print("STATUS:", r.status_code)
        print("HTML_SIZE:", len(render_html))
        print("OUT:", out)

        print()
        print("SCRIPT SATIRLARI:")
        for i, line in enumerate(render_html.splitlines(), 1):
            if "<script" in line and "src=" in line:
                print(f"{i}: {line[:260]}")

        print()
        print("ÜST HIZ / DOLULUK / DURUM BLOĞU:")
        for i, line in enumerate(render_html.splitlines(), 1):
            low = line.lower()
            if any(k.lower() in low for k in [
                "v99-gauges", "v99-gauge-cell", "v99-gauge-label",
                "v99SpeedVal", "liveSpeedText", "DOLULUK", "DURUM", "HIZ"
            ]):
                print(f"{i}: {line[:260]}")

except Exception as e:
    print("RENDER HATA:", repr(e))

section("6) DOM SEÇİCİ SİMÜLASYONU")
if render_html:
    gauge_cells = re.findall(r'<div class="v99-gauge-cell">(.*?)</div>\s*(?=<div class="v99-gauge-cell">|</div>\s*<main|\Z)', render_html, flags=re.S)
    print("v99-gauge-cell regex count:", len(gauge_cells))

    for idx, block in enumerate(gauge_cells[:5], 1):
        text = re.sub(r"<.*?>", " ", block)
        text = re.sub(r"\s+", " ", text).strip()
        print(f"CELL {idx}: {text[:180]}")

    print()
    print("HIZ label var mı:", "HIZ" in render_html)
    print("id=v99SpeedVal var mı:", 'id="v99SpeedVal"' in render_html)
    print("id=liveSpeedText var mı:", 'id="liveSpeedText"' in render_html)
    print(".v99-gauges .v99-gauge-cell yapısı var mı:", 'class="v99-gauges"' in render_html and 'class="v99-gauge-cell"' in render_html)

section("7) JS HIZ BLOĞU / EVENT SIRASI")
print_hits("JS speed / click / stopImmediatePropagation izleri", js, [
    "V99Z_SPEED_ANALOG_TOGGLE_START",
    "V99ZA_SPEED_TOGGLE_START",
    "findSpeedCard",
    "v99SpeedVal",
    "liveSpeedText",
    "v99zaBound",
    "addEventListener(\"click\"",
    "addEventListener('click'",
    "stopImmediatePropagation",
    "preventDefault",
    "V99M_OCCUPANCY_PANEL_START",
    "V99Q_ONLY_OCCUPANCY_CLICK_START",
], pad=6, max_hits=120)

section("8) CSS HIZ BLOĞU / GAUGE STİLİ")
print_hits("CSS gauge / speed analog izleri", css, [
    ".v99-gauges",
    ".v99-gauge-cell",
    ".v99-gauge-val",
    ".v99-gauge-unit",
    "overflow",
    "pointer-events",
    "V99Z_SPEED_ANALOG_TOGGLE_CSS_START",
    "V99ZA_SPEED_TOGGLE_CSS_START",
    "v99z-speed-card",
    "v99za-speed-card",
], pad=6, max_hits=120)

section("9) BACKUPLARDA HIZ TOGGLE VAR MI")
baks = sorted(WEB_JS.parent.glob(WEB_JS.name + ".bak-*"), key=lambda p: p.stat().st_mtime, reverse=True)[:35]
for b in baks:
    t = read(b)
    marks = []
    for m in [
        "V99Z_SPEED_ANALOG_TOGGLE_START",
        "V99ZA_SPEED_TOGGLE_START",
        "MuavinV99SpeedToggle",
        "MuavinV99ZASpeedToggle",
        "V99Q_ONLY_OCCUPANCY_CLICK_START",
        "V99M_OCCUPANCY_PANEL_START",
    ]:
        if m in t:
            marks.append(m)
    if marks:
        print(f"- {b.name} size={b.stat().st_size} sha={sha(b)} markers={marks}")

section("10) STATİK JS GERÇEKTEN SERVİS EDİLİYOR MU")
try:
    sys.path.insert(0, str(ROOT))
    from app import app

    with app.test_client() as c:
        r = c.get("/static/continue/continue_trip_v99_clean.js?v=v99zb_static")
        body = r.get_data().decode("utf-8", errors="ignore")
        print("STATUS:", r.status_code)
        print("SIZE:", len(body))
        for m in [
            "V99Z_SPEED_ANALOG_TOGGLE_START",
            "V99ZA_SPEED_TOGGLE_START",
            "MuavinV99ZASpeedToggle",
            "V99M_OCCUPANCY_PANEL_START",
        ]:
            print(("VAR  " if m in body else "YOK  ") + m)

except Exception as e:
    print("STATIC TEST HATA:", repr(e))

section("11) JS SYNTAX CHECK")
node = shutil.which("node")
if node:
    res = subprocess.run(["node", "--check", str(WEB_JS)], capture_output=True, text=True)
    if res.returncode == 0:
        print("✅ JS syntax OK")
    else:
        print("❌ JS syntax HATA")
        print(res.stdout)
        print(res.stderr)
else:
    print("node yok, atlandı")

section("12) KISA OTOMATİK YORUM")
issues = []

if "V99ZA_SPEED_TOGGLE_START" not in js and "V99Z_SPEED_ANALOG_TOGGLE_START" not in js:
    issues.append("Aktif JS içinde hız analog toggle bloğu yok. Rollback sonrası normal.")

if "v99za-speed" not in tpl and "V99ZA_SPEED_TOGGLE_START" in js:
    issues.append("JS içinde V99ZA var ama template cache v99za-speed değil. Tarayıcı eski JS kullanmış olabilir.")

if "V99ZA_SPEED_TOGGLE_START" in js and ".v99-gauge-cell" not in js:
    issues.append("V99ZA var ama .v99-gauge-cell selector yok. HIZ kartını bulamaz.")

if "V99ZA_SPEED_TOGGLE_START" in js and "stopImmediatePropagation" in js:
    issues.append("Dosyada stopImmediatePropagation var. Click event başka blok tarafından kesiliyor olabilir; satır sırasına bakılmalı.")

if "V99ZA_SPEED_TOGGLE_CSS_START" in css and "overflow:hidden" in css:
    issues.append("CSS içinde overflow:hidden kullanımları var. Analog UI kart içinde görünse bile taşma/kırpılma olabilir.")

if issues:
    for x in issues:
        print("❌", x)
else:
    print("✅ Otomatik yorumda bariz sebep yakalanmadı; üstteki DOM/CSS/Event satırlarına bakmak lazım.")

print()
print("===== RAPOR BİTTİ =====")
