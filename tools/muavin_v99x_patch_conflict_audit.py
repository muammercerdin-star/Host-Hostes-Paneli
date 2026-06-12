from pathlib import Path
from datetime import datetime
import hashlib
import re
import sys
import subprocess
import shutil
from collections import Counter, defaultdict

ROOT = Path(".").resolve()
STAMP = datetime.now().strftime("%Y%m%d-%H%M%S")

print("===== MUAVİN V99X GENEL YAMA ÇAKIŞMA DENETİMİ =====")
print("ROOT:", ROOT)
print("TIME:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
print("NOT: Bu script uygulama dosyalarını değiştirmez. Sadece rapor üretir.")

FILES = {
    "WEB_TEMPLATE_CONTINUE": ROOT / "templates/continue_trip.html",
    "ANDROID_TEMPLATE_CONTINUE": ROOT / "android_app/app/src/main/python/templates/continue_trip.html",

    "WEB_JS_V99": ROOT / "static/continue/continue_trip_v99_clean.js",
    "ANDROID_JS_V99": ROOT / "android_app/app/src/main/python/static/continue/continue_trip_v99_clean.js",

    "WEB_CSS_V99": ROOT / "static/continue/continue_trip_v99_clean.css",
    "ANDROID_CSS_V99": ROOT / "android_app/app/src/main/python/static/continue/continue_trip_v99_clean.css",

    "WEB_JS_CORE": ROOT / "static/continue/continue_trip_core.js",
    "ANDROID_JS_CORE": ROOT / "android_app/app/src/main/python/static/continue/continue_trip_core.js",

    "WEB_JS_UI": ROOT / "static/continue/continue_trip_ui.js",
    "ANDROID_JS_UI": ROOT / "android_app/app/src/main/python/static/continue/continue_trip_ui.js",

    "APP": ROOT / "app.py",
    "ANDROID_APP": ROOT / "android_app/app/src/main/python/app.py",
}

def read(p):
    return p.read_text(encoding="utf-8", errors="ignore") if p.exists() else ""

def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()[:12] if p.exists() else "-"

def section(title):
    print()
    print("===== " + title + " =====")

def warn(msg):
    print("⚠️", msg)

def ok(msg):
    print("✅", msg)

def bad(msg):
    print("❌", msg)

def line_hits(txt, patterns, pad=5, max_hits=120):
    lines = txt.splitlines()
    hit_lines = []
    for i, line in enumerate(lines, 1):
        low = line.lower()
        if any(p.lower() in low for p in patterns):
            hit_lines.append(i)

    shown = set()
    for i in hit_lines[:max_hits]:
        for n in range(max(1, i-pad), min(len(lines), i+pad)+1):
            if n in shown:
                continue
            shown.add(n)
            print(f"{n:5}: {lines[n-1][:260]}")
        print("-----")

    if len(hit_lines) > max_hits:
        print("... kesildi. Toplam hit:", len(hit_lines))

section("1) DOSYA DURUMU")
for name, p in FILES.items():
    print(f"{name:28} {'VAR' if p.exists() else 'YOK'} size={p.stat().st_size if p.exists() else '-':<8} sha={sha(p)} {p}")

section("2) WEB / ANDROID SENKRON KONTROL")
pairs = [
    ("continue_trip.html", FILES["WEB_TEMPLATE_CONTINUE"], FILES["ANDROID_TEMPLATE_CONTINUE"]),
    ("continue_trip_v99_clean.js", FILES["WEB_JS_V99"], FILES["ANDROID_JS_V99"]),
    ("continue_trip_v99_clean.css", FILES["WEB_CSS_V99"], FILES["ANDROID_CSS_V99"]),
    ("continue_trip_core.js", FILES["WEB_JS_CORE"], FILES["ANDROID_JS_CORE"]),
    ("continue_trip_ui.js", FILES["WEB_JS_UI"], FILES["ANDROID_JS_UI"]),
    ("app.py", FILES["APP"], FILES["ANDROID_APP"]),
]

for label, a, b in pairs:
    if not a.exists() or not b.exists():
        warn(f"{label}: web/android kontrol edilemedi")
    elif sha(a) == sha(b):
        ok(f"{label}: AYNI sha={sha(a)}")
    else:
        bad(f"{label}: FARKLI web={sha(a)} android={sha(b)}")

tpl = read(FILES["WEB_TEMPLATE_CONTINUE"])
js = read(FILES["WEB_JS_V99"])
css = read(FILES["WEB_CSS_V99"])

section("3) TEMPLATE SCRIPT SIRASI VE BOZUK SATIR KONTROLÜ")
script_lines = []
for i, line in enumerate(tpl.splitlines(), 1):
    if "<script" in line and "src=" in line:
        script_lines.append((i, line.strip()))
        print(f"{i:5}: {line.strip()}")

if "}}'id']" in tpl or "v99g-{{ trip['id'] }}'id']" in tpl:
    bad("Template içinde bozuk cache/Jinja izi var: }}'id'] veya v99g-{{ trip['id'] }}'id']")
else:
    ok("Template script cache satırında bariz bozuk Jinja izi yok")

if "continue_trip_v99_clean.js" not in tpl:
    bad("continue_trip_v99_clean.js template içinde çağrılmıyor")
else:
    ok("continue_trip_v99_clean.js template içinde çağrılıyor")

section("4) MARKER BLOK DENETİMİ")
def marker_audit(label, txt):
    print()
    print("---", label, "---")
    markers = []
    for i, line in enumerate(txt.splitlines(), 1):
        m = re.search(r"/\*\s*([A-Z0-9_]+)_(START|END)\s*\*/", line)
        if m:
            markers.append((i, m.group(1), m.group(2), line.strip()))

    if not markers:
        print("Marker yok")
        return {}

    starts = defaultdict(list)
    ends = defaultdict(list)

    stack = []
    overlap_warnings = []

    for line_no, name, kind, raw in markers:
        if kind == "START":
            starts[name].append(line_no)
            if stack:
                overlap_warnings.append((line_no, name, "önceki blok kapanmadan yeni START", stack[-1]))
            stack.append((name, line_no))
        else:
            ends[name].append(line_no)
            if not stack:
                overlap_warnings.append((line_no, name, "END var ama açık blok yok", None))
            else:
                last_name, last_line = stack.pop()
                if last_name != name:
                    overlap_warnings.append((line_no, name, f"END uyuşmuyor, açık blok {last_name}", last_line))

    for name in sorted(set(list(starts.keys()) + list(ends.keys()))):
        s_count = len(starts[name])
        e_count = len(ends[name])
        status = "OK" if s_count == e_count == 1 else "RISK"
        print(f"{status:4} {name:42} START={starts[name]} END={ends[name]}")

    if stack:
        for name, line_no in stack:
            bad(f"{label}: kapanmamış blok: {name} START line {line_no}")

    if overlap_warnings:
        print()
        print("ÇAKIŞMA / NESTED RİSKLERİ:")
        for w in overlap_warnings[:80]:
            warn(str(w))

    return {"starts": starts, "ends": ends, "markers": markers}

ma_js = marker_audit("WEB_JS_V99", js)
ma_css = marker_audit("WEB_CSS_V99", css)

section("5) ÖZEL V99 RİSK MARKER KONTROLÜ")
risk_keys = [
    "V99M_OCCUPANCY_PANEL_START",
    "V99Q_ONLY_OCCUPANCY_CLICK_START",
    "V99U",
    "V99V_DOLULUK_DIRECT_CLICK_START",
    "V99T_DOLULUK_CLICK_GUARD",
    "V99S_SPEED_ANALOG_TOGGLE",
    "V99P_BAG_BADGE_CLICK_FIX_START",
    "V99O_SEAT_GENDER_SELECTED_JS_START",
    "V99W",
]

for k in risk_keys:
    print(("VAR  " if k in js or k in css or k in tpl else "YOK  ") + k)

if "V99Q_ONLY_OCCUPANCY_CLICK_START" in js and "V99M_OCCUPANCY_PANEL_START" in js:
    warn("V99M doluluk paneli + V99Q click guard birlikte duruyor. Tıklama davranışı burada ezilebilir.")

if "V99U SAFE" in js:
    warn("V99U SAFE bloğu duruyor. .v99-gauge-cell hedefi yoksa DOLULUK açılmaz.")

if "V99V_DOLULUK_DIRECT_CLICK_START" in js:
    warn("V99V direct click bloğu hâlâ duruyor. Rollback tam olmamış olabilir.")

if ".v99-gauge-cell" not in js and "isDolulukTarget" in js:
    bad("JS içinde .v99-gauge-cell yok. Template üst kutuları .v99-gauge-cell olduğu için DOLULUK hedeflenemeyebilir.")

section("6) CLICK HANDLER DENETİMİ")
click_files = [
    FILES["WEB_JS_V99"],
    FILES["WEB_JS_CORE"],
    FILES["WEB_JS_UI"],
]

for p in click_files:
    txt = read(p)
    if not txt:
        continue

    print()
    print("---", p, "---")
    count = 0
    lines = txt.splitlines()
    for i, line in enumerate(lines, 1):
        low = line.lower()
        if "addeventlistener" in low and "click" in low:
            count += 1
            print(f"\nCLICK_HANDLER #{count} line {i}")
            for n in range(max(1, i-8), min(len(lines), i+12)+1):
                print(f"{n:5}: {lines[n-1][:260]}")

    if count == 0:
        print("Click handler bulunmadı")
    else:
        print("TOPLAM CLICK HANDLER:", count)

section("7) DOLULUK PANELİ BLOĞU KISA RÖNTGEN")
line_hits(js, [
    "V99M_OCCUPANCY_PANEL_START",
    "ensurePanel",
    "openPanel",
    "closePanel",
    "isDolulukTarget",
    "markDolulukCards",
    "v99m-occ-clickable",
    "MuavinV99OccupancyPanel",
    "V99Q_ONLY_OCCUPANCY_CLICK_START",
    "isDolulukCard",
    "stopImmediatePropagation",
], pad=8, max_hits=80)

section("8) CSS DUPLICATE SELECTOR DENETİMİ")
def css_duplicate_selectors(css_txt):
    no_comments = re.sub(r"/\*.*?\*/", "", css_txt, flags=re.S)
    selectors = []
    buf = ""
    for line in no_comments.splitlines():
        stripped = line.strip()
        if not stripped:
            continue
        buf += " " + stripped
        if "{" in stripped:
            sel = buf.split("{", 1)[0].strip()
            buf = ""
            if not sel or sel.startswith("@"):
                continue
            selectors.append(sel)

    c = Counter(selectors)
    dups = [(sel, n) for sel, n in c.items() if n > 1]
    return sorted(dups, key=lambda x: (-x[1], x[0]))

dups = css_duplicate_selectors(css)
print("DUPLICATE_SELECTOR_COUNT:", len(dups))
for sel, n in dups[:120]:
    important = any(k in sel for k in [
        "v99m", "v99-gauge", "v99-seat", "v99-ring", "v99-tl", "v99-dock"
    ])
    tag = "RISK" if important else "INFO"
    print(f"{tag:4} x{n:<3} {sel[:220]}")

section("9) STATİK REFERANS VE RENDER TEST")
render_html = ""
try:
    sys.path.insert(0, str(ROOT))
    from app import app

    out = ROOT / "run_logs" / f"v99x_render_{STAMP}.html"
    out.parent.mkdir(exist_ok=True)

    with app.test_client() as c:
        with c.session_transaction() as sess:
            sess["auth_ok"] = True

        r = c.get("/continue-trip?v=v99x_audit", follow_redirects=False)
        render_html = r.get_data().decode("utf-8", errors="ignore")
        out.write_text(render_html, encoding="utf-8")

        print("STATUS:", r.status_code)
        print("HTML_SIZE:", len(render_html))
        print("OUT:", out)

        if r.status_code != 200:
            bad("Render 200 dönmedi")

        if "{{" in render_html or "}}" in render_html:
            warn("Render HTML içinde Jinja artığı var: {{ veya }}")

        if "}}'id']" in render_html or "'id'] }}" in render_html:
            bad("Render HTML içinde bozuk script/cache izi var: }}'id']")

        ids = re.findall(r'\bid=["\']([^"\']+)["\']', render_html)
        dup_ids = [(k, v) for k, v in Counter(ids).items() if v > 1]
        print("DUPLICATE_ID_COUNT:", len(dup_ids))
        for k, v in dup_ids[:80]:
            warn(f"duplicate id: {k} x{v}")

        print()
        print("SCRIPT SRC KONTROL:")
        srcs = re.findall(r'<script[^>]+src=["\']([^"\']+)["\']', render_html)
        for src in srcs:
            clean = src.split("?", 1)[0]
            if clean.startswith("/static/"):
                p = ROOT / clean.lstrip("/")
                print(("VAR  " if p.exists() else "YOK  ") + src + " -> " + str(p))
            else:
                print("EXT  " + src)

except Exception as e:
    bad("Render test hata: " + repr(e))

section("10) NODE JS SYNTAX CHECK")
node = shutil.which("node")
if not node:
    warn("node yok, JS syntax check atlandı")
else:
    for p in [FILES["WEB_JS_V99"], FILES["WEB_JS_CORE"], FILES["WEB_JS_UI"]]:
        if not p.exists():
            continue
        res = subprocess.run([node, "--check", str(p)], capture_output=True, text=True)
        if res.returncode == 0:
            ok(f"JS syntax OK: {p}")
        else:
            bad(f"JS syntax HATA: {p}")
            print(res.stdout)
            print(res.stderr)

section("11) BACKUP HARİTASI")
for p in [
    FILES["WEB_JS_V99"],
    FILES["WEB_CSS_V99"],
    FILES["WEB_TEMPLATE_CONTINUE"],
]:
    if not p.exists():
        continue
    baks = sorted(p.parent.glob(p.name + ".bak-*"), key=lambda x: x.stat().st_mtime, reverse=True)
    print()
    print("---", p.name, "backup count:", len(baks), "---")
    for b in baks[:25]:
        marks = []
        t = read(b)
        for m in ["V99M", "V99Q", "V99U", "V99V", "V99W", "V99S", "V99T"]:
            if m in t:
                marks.append(m)
        print(f"{b.name} size={b.stat().st_size} sha={sha(b)} markers={marks}")

section("12) KISA OTOMATİK YORUM")
issues = []

if "}}'id']" in tpl:
    issues.append("Template script cache satırında bozuk Jinja izi var.")

if "V99Q_ONLY_OCCUPANCY_CLICK_START" in js and "V99M_OCCUPANCY_PANEL_START" in js:
    issues.append("Doluluk paneli ve click guard aynı dosyada; tıklama ezilmesi kontrol edilmeli.")

if "V99U SAFE" in js and ".v99-gauge-cell" not in js:
    issues.append("V99U SAFE aktif ama .v99-gauge-cell yok; DOLULUK hedefi kaçabilir.")

if "V99V_DOLULUK_DIRECT_CLICK_START" in js:
    issues.append("V99V bloğu kalmış; rollback eksik olabilir.")

if "V99M_OCCUPANCY_PANEL_START" in js and "v99m-occ-overlay" not in css:
    issues.append("JS panel oluşturuyor ama CSS panel selector izi eksik görünüyor.")

if issues:
    for x in issues:
        bad(x)
else:
    ok("Otomatik kontrolde büyük çakışma sinyali yakalanmadı. Detay çıktısı yine incelenmeli.")

print()
print("===== RAPOR BİTTİ =====")
