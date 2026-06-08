from pathlib import Path
import re
import sys

ROOT = Path(".").resolve()
sys.path.insert(0, str(ROOT))

print("===== MUAVİN ASİSTANI STEP-4 ŞÜPHELİ NOKTA BAĞLAM DENETİMİ =====")
print("ROOT:", ROOT)
print()

def rel(p):
    try:
        return str(Path(p).resolve().relative_to(ROOT))
    except Exception:
        return str(p)

def read(p):
    return Path(p).read_text(encoding="utf-8", errors="ignore")

def section(t):
    print()
    print("===== " + t + " =====")

def show_lines(path, start, end):
    p = ROOT / path
    print()
    print(f"--- {path}:{start}-{end} ---")
    if not p.exists():
        print("❌ dosya yok")
        return

    lines = read(p).splitlines()
    start = max(1, start)
    end = min(len(lines), end)

    for i in range(start, end + 1):
        print(f"{i:5}: {lines[i-1]}")

def grep_context(path, pattern, before=8, after=12):
    p = ROOT / path
    print()
    print(f"--- {path} içinde arama: {pattern} ---")
    if not p.exists():
        print("❌ dosya yok")
        return

    txt = read(p)
    lines = txt.splitlines()
    found = False

    for idx, line in enumerate(lines, start=1):
        if pattern in line:
            found = True
            s = max(1, idx-before)
            e = min(len(lines), idx+after)
            print()
            print(f"### Eşleşme satır {idx}")
            for i in range(s, e+1):
                mark = ">>" if i == idx else "  "
                print(f"{mark} {i:5}: {lines[i-1]}")

    if not found:
        print("Bulunamadı")

def all_files(exts):
    skip = {".git", "__pycache__", ".venv", "venv", "env", "build", "dist", ".gradle", "node_modules", "audit_reports"}
    out = []
    for p in ROOT.rglob("*"):
        if any(part in skip for part in p.parts):
            continue
        if not p.is_file():
            continue
        if p.suffix.lower() in exts:
            out.append(p)
    return out

# ------------------------------------------------------------
# 1) ROUTE HARİTASINDA İLGİLİ KELİMELER
# ------------------------------------------------------------
section("1) GERÇEK FLASK ROUTE HARİTASINDA ŞÜPHELİ KONULAR")

try:
    import app as app_module
    flask_app = app_module.app

    keywords = [
        "consignment",
        "report",
        "route",
        "seat",
        "stop",
        "csrf",
        "trip",
    ]

    rules = sorted(
        [(str(r), r.endpoint, ",".join(sorted(m for m in r.methods if m not in {"HEAD","OPTIONS"}))) for r in flask_app.url_map.iter_rules()],
        key=lambda x: x[0]
    )

    for kw in keywords:
        print()
        print(f"--- keyword: {kw} ---")
        hit = False
        for rule, endpoint, methods in rules:
            if kw.lower() in rule.lower() or kw.lower() in endpoint.lower():
                hit = True
                print(f"{methods:16} {rule:45} -> {endpoint}")
        if not hit:
            print("eşleşme yok")

except Exception as e:
    print("❌ app import/route haritası okunamadı:", type(e).__name__, e)

# ------------------------------------------------------------
# 2) ŞÜPHELİ FETCH KOD BAĞLAMLARI
# ------------------------------------------------------------
section("2) ŞÜPHELİ FETCH KOD BAĞLAMLARI")

targets = [
    ("templates/consignments.html", "/api/consignments/${id}/status"),
    ("templates/reports.html", "/api/report/seat-detail"),
    ("templates/route_stops.html", "/api/route-stop"),
    ("static/app.js", "/api/seat/clear"),
    ("static/app.js", "/api/seats"),
    ("static/seats/seats-time-prayer.js", "nominatim.openstreetmap.org"),
]

for path, pat in targets:
    grep_context(path, pat, before=10, after=16)

# ------------------------------------------------------------
# 3) ANDROID KOPYASINDA AYNI BAĞLAMLAR
# ------------------------------------------------------------
section("3) ANDROID KOPYASINDA AYNI ŞÜPHELİ BAĞLAMLAR")

android_targets = [
    ("android_app/app/src/main/python/templates/consignments.html", "/api/consignments/${id}/status"),
    ("android_app/app/src/main/python/templates/reports.html", "/api/report/seat-detail"),
    ("android_app/app/src/main/python/templates/route_stops.html", "/api/route-stop"),
    ("android_app/app/src/main/python/static/app.js", "/api/seat/clear"),
    ("android_app/app/src/main/python/static/app.js", "/api/seats"),
    ("android_app/app/src/main/python/static/seats/seats-time-prayer.js", "nominatim.openstreetmap.org"),
]

for path, pat in android_targets:
    grep_context(path, pat, before=8, after=12)

# ------------------------------------------------------------
# 4) static/app.js GLOBAL YÜKLENİYOR MU VE NE YAPIYOR?
# ------------------------------------------------------------
section("4) static/app.js GLOBAL BAĞLANTI VE İÇERİK")

grep_context("templates/base.html", "app.js", before=8, after=8)
grep_context("android_app/app/src/main/python/templates/base.html", "app.js", before=8, after=8)

show_lines("static/app.js", 1, 120)
show_lines("android_app/app/src/main/python/static/app.js", 1, 120)

# ------------------------------------------------------------
# 5) CSRF TOKEN NASIL SUNULUYOR?
# ------------------------------------------------------------
section("5) CSRF TOKEN SUNUMU VE BEFORE_REQUEST KONTROLÜ")

for path in [
    "templates/base.html",
    "templates/seats.html",
    "templates/continue_trip.html",
    "templates/trip_new.html",
    "android_app/app/src/main/python/templates/base.html",
    "android_app/app/src/main/python/templates/trip_new.html",
]:
    grep_context(path, "csrf", before=8, after=12)
    grep_context(path, "csrf_token", before=8, after=12)
    grep_context(path, "X-CSRF", before=8, after=12)

for path in ["app.py", "android_app/app/src/main/python/app.py"]:
    grep_context(path, "PROTECTED_PREFIXES", before=8, after=20)
    grep_context(path, "EXCLUDE_PREFIXES", before=8, after=20)
    grep_context(path, "csrf", before=10, after=18)
    grep_context(path, "X-CSRF", before=10, after=18)

# ------------------------------------------------------------
# 6) CONTINUE_TRIP_CORE headers DEĞİŞKENİ CSRF İÇERİYOR MU?
# ------------------------------------------------------------
section("6) continue_trip_core.js HEADERS DEĞİŞKENİ")

for path in [
    "static/continue/continue_trip_core.js",
    "android_app/app/src/main/python/static/continue/continue_trip_core.js",
]:
    grep_context(path, "const headers", before=10, after=20)
    grep_context(path, "X-CSRF", before=10, after=20)
    grep_context(path, "csrf", before=10, after=20)

# ------------------------------------------------------------
# 7) settings_subscription POST CSRF BAĞLAMI
# ------------------------------------------------------------
section("7) settings_subscription.html POST CSRF BAĞLAMI")

for path in [
    "templates/settings_subscription.html",
    "android_app/app/src/main/python/templates/settings_subscription.html",
]:
    grep_context(path, 'method: "POST"', before=12, after=20)
    grep_context(path, "csrf", before=8, after=12)

# ------------------------------------------------------------
# 8) route_stops.html SAYFASI RENDER EDİLİYOR MU?
# ------------------------------------------------------------
section("8) route_stops.html GERÇEKTEN KULLANILIYOR MU?")

for p in all_files({".py", ".html", ".js"}):
    s = str(p).replace("\\", "/")
    if "/vendor/" in s or "/apk_payload/" in s:
        continue

    txt = read(p)
    if "route_stops.html" in txt or "route_stops" in txt or "/api/route-stop" in txt:
        print()
        print(f"--- {rel(p)} ---")
        for i, line in enumerate(txt.splitlines(), start=1):
            if "route_stops.html" in line or "route_stops" in line or "/api/route-stop" in line:
                print(f"{i:5}: {line[:220]}")

print()
print("===== STEP-4 BİTTİ =====")
