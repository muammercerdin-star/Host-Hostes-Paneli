from pathlib import Path
import re
import sys
from collections import defaultdict

ROOT = Path(".").resolve()
sys.path.insert(0, str(ROOT))

print("===== MUAVİN ASİSTANI STEP-3 FLASK GERÇEK ROUTE DENETİMİ =====")
print("ROOT:", ROOT)
print()

def rel(p):
    try:
        return str(Path(p).resolve().relative_to(ROOT))
    except Exception:
        return str(p)

def read(p):
    return Path(p).read_text(encoding="utf-8", errors="ignore")

def line_of(text, pos):
    return text.count("\n", 0, pos) + 1

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

def section(t):
    print()
    print("===== " + t + " =====")

# ------------------------------------------------------------
# 1) APP IMPORT VE GERÇEK URL MAP
# ------------------------------------------------------------
section("1) FLASK APP IMPORT / URL MAP")

try:
    import app as app_module
    flask_app = getattr(app_module, "app", None)

    if flask_app is None:
        print("❌ app.py içinde app nesnesi bulunamadı")
        raise SystemExit(1)

    print("✅ Flask app import edildi")
    print("Endpoint sayısı:", len(flask_app.view_functions))
    print("Rule sayısı:", len(list(flask_app.url_map.iter_rules())))

except Exception as e:
    print("❌ Flask app import edilemedi")
    print(type(e).__name__ + ":", e)
    raise SystemExit(1)

routes = []
endpoint_to_rules = defaultdict(list)

for rule in flask_app.url_map.iter_rules():
    methods = sorted(m for m in rule.methods if m not in {"HEAD", "OPTIONS"})
    routes.append((rule.endpoint, str(rule), ",".join(methods)))
    endpoint_to_rules[rule.endpoint].append(str(rule))

routes_sorted = sorted(routes, key=lambda x: (x[1], x[0]))

print()
print("İlk 120 route:")
for endpoint, rule, methods in routes_sorted[:120]:
    print(f"{methods:18} {rule:45} -> {endpoint}")

if len(routes_sorted) > 120:
    print(f"... {len(routes_sorted)-120} route daha var")

# ------------------------------------------------------------
# 2) URL_FOR GERÇEK ENDPOINT KONTROLÜ
# ------------------------------------------------------------
section("2) url_for GERÇEK ENDPOINT KONTROLÜ")

html_py_files = all_files({".html", ".jinja", ".j2", ".py"})
urlfor_hits = []
bad_urlfor = []

for p in html_py_files:
    txt = read(p)
    for m in re.finditer(r"url_for\s*\(\s*['\"]([^'\"]+)['\"]", txt):
        endpoint = m.group(1)
        if endpoint == "static":
            continue

        ln = line_of(txt, m.start())
        urlfor_hits.append((p, ln, endpoint))

        if endpoint not in flask_app.view_functions:
            bad_urlfor.append((p, ln, endpoint))

print("url_for kullanımı:", len(urlfor_hits))

if bad_urlfor:
    print("❌ Gerçek Flask endpoint içinde bulunamayan url_for var")
    for p, ln, endpoint in bad_urlfor[:160]:
        print(f"{rel(p)}:{ln} -> url_for('{endpoint}')")
    if len(bad_urlfor) > 160:
        print(f"... {len(bad_urlfor)-160} kayıt daha var")
else:
    print("✅ url_for endpointleri gerçek Flask app içinde mevcut")

# ------------------------------------------------------------
# 3) FETCH/API GERÇEK ROUTE KONTROLÜ
# ------------------------------------------------------------
section("3) fetch/API GERÇEK ROUTE KONTROLÜ")

js_html_files = all_files({".html", ".js"})
fetch_re = re.compile(r"""fetch\s*\(\s*([`'"])(.+?)\1""", re.S)

fetch_hits = []

for p in js_html_files:
    s = str(p).replace("\\", "/")
    if "/vendor/" in s or "/apk_payload/" in s:
        continue

    txt = read(p)

    for m in fetch_re.finditer(txt):
        raw = m.group(2).strip()
        ln = line_of(txt, m.start())

        if raw.startswith("http"):
            fetch_hits.append((p, ln, raw, "ABSOLUTE"))
            continue

        if not raw.startswith("/"):
            fetch_hits.append((p, ln, raw, "RELATIVE"))
            continue

        clean = raw.split("?")[0].split("#")[0]
        clean = re.sub(r"\$\{[^}]+\}", "__VAR__", clean)
        clean = re.sub(r"\{[^}]+\}", "__VAR__", clean)
        fetch_hits.append((p, ln, clean, "ROOT"))

rules = list(flask_app.url_map.iter_rules())

def path_matches_rule(path, rule_text):
    # /api/consignments/__VAR__/status
    # /api/consignments/<int:id>/status
    pr = [x for x in path.strip("/").split("/") if x]
    rr = [x for x in rule_text.strip("/").split("/") if x]

    if len(pr) != len(rr):
        return False

    for a, b in zip(pr, rr):
        if a == "__VAR__":
            continue
        if b.startswith("<") and b.endswith(">"):
            continue
        if a != b:
            return False

    return True

bad_fetch = []
ok_fetch = []

for p, ln, path, kind in fetch_hits:
    if kind == "ABSOLUTE":
        bad_fetch.append((p, ln, path, "Dış URL / APK internet bağımlılığı"))
        continue

    if kind == "RELATIVE":
        # relative fetch kesin hata değil
        ok_fetch.append((p, ln, path, "relative"))
        continue

    matches = []
    for rule in rules:
        if path_matches_rule(path, str(rule)):
            matches.append((str(rule), rule.endpoint, ",".join(sorted(m for m in rule.methods if m not in {"HEAD","OPTIONS"}))))

    if matches:
        ok_fetch.append((p, ln, path, matches[0]))
    else:
        bad_fetch.append((p, ln, path, "Flask url_map içinde eşleşmedi"))

print("fetch çağrısı:", len(fetch_hits))
print("eşleşen/relative:", len(ok_fetch))
print("şüpheli:", len(bad_fetch))

if bad_fetch:
    print()
    print("⚠️ Şüpheli fetch/API:")
    for p, ln, path, reason in bad_fetch[:160]:
        print(f"{rel(p)}:{ln} -> {path}  [{reason}]")
    if len(bad_fetch) > 160:
        print(f"... {len(bad_fetch)-160} kayıt daha var")
else:
    print("✅ fetch/API yolları gerçek route haritasıyla uyumlu görünüyor")

# ------------------------------------------------------------
# 4) CSRF KORUMASI VE YAZMA ROUTE'LARI
# ------------------------------------------------------------
section("4) CSRF KORUMALI YAZMA ROUTE'LARI")

protected_prefixes = getattr(app_module, "PROTECTED_PREFIXES", None)
exclude_prefixes = getattr(app_module, "EXCLUDE_PREFIXES", None)

print("PROTECTED_PREFIXES:", protected_prefixes)
print("EXCLUDE_PREFIXES:", exclude_prefixes)

write_rules = []

for rule in flask_app.url_map.iter_rules():
    methods = set(rule.methods) - {"HEAD", "OPTIONS"}
    if methods & {"POST", "PUT", "PATCH", "DELETE"}:
        write_rules.append((str(rule), rule.endpoint, ",".join(sorted(methods))))

print()
print("Yazma route sayısı:", len(write_rules))

for rule, endpoint, methods in sorted(write_rules)[:160]:
    print(f"{methods:18} {rule:45} -> {endpoint}")

if len(write_rules) > 160:
    print(f"... {len(write_rules)-160} kayıt daha var")

# ------------------------------------------------------------
# 5) STATIK APP.JS GERÇEKTEN KULLANILIYOR MU?
# ------------------------------------------------------------
section("5) static/app.js GERÇEKTEN SAYFALARA BAĞLI MI?")

targets = [
    "static/app.js",
    "/static/app.js",
    "app.js"
]

for target in targets:
    hits = []
    for p in all_files({".html", ".jinja", ".j2"}):
        txt = read(p)
        if target in txt:
            for m in re.finditer(re.escape(target), txt):
                hits.append((p, line_of(txt, m.start())))

    if hits:
        print(f"'{target}' izi:")
        for p, ln in hits[:80]:
            print(f"  {rel(p)}:{ln}")
    else:
        print(f"'{target}' izi yok")

print()
print("===== STEP-3 BİTTİ =====")
