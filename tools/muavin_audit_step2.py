from pathlib import Path
import re
import sys
import shutil
import subprocess
import tempfile
import difflib
from collections import defaultdict

ROOT = Path(".").resolve()

SKIP_DIRS = {
    ".git", "__pycache__", ".venv", "venv", "env",
    "build", "dist", ".gradle", "node_modules",
    "audit_reports"
}

TEXT_EXTS = {".py", ".html", ".jinja", ".j2", ".js", ".css"}

print("===== MUAVİN ASİSTANI STEP-2 DERİN DENETİM =====")
print("ROOT:", ROOT)
print()

def is_skipped(path: Path):
    return any(part in SKIP_DIRS for part in path.parts)

def rel(path: Path):
    try:
        return str(path.resolve().relative_to(ROOT))
    except Exception:
        return str(path)

def read(path: Path):
    return path.read_text(encoding="utf-8", errors="ignore")

def line_of(text, pos):
    return text.count("\n", 0, pos) + 1

def all_files(exts=None):
    out = []
    for p in ROOT.rglob("*"):
        if is_skipped(p):
            continue
        if not p.is_file():
            continue
        if exts and p.suffix.lower() not in exts:
            continue
        out.append(p)
    return out

def section(title):
    print()
    print("===== " + title + " =====")

# ------------------------------------------------------------
# 1) JAVASCRIPT SYNTAX CHECK
# ------------------------------------------------------------
section("1) JAVASCRIPT SYNTAX KONTROLÜ")

node = shutil.which("node")
js_files = [
    p for p in all_files({".js"})
    if "/vendor/" not in str(p).replace("\\", "/")
    and "/apk_payload/" not in str(p).replace("\\", "/")
    and not p.name.endswith(".min.js")
]

if not node:
    print("⚠️ node bulunamadı; JS syntax kontrolü atlandı.")
    print("Not: Termux'ta istersen sonra sadece kontrol için: pkg install nodejs")
else:
    js_errors = []
    for p in js_files:
        try:
            r = subprocess.run(
                [node, "--check", str(p)],
                capture_output=True,
                text=True,
                timeout=20
            )
            if r.returncode != 0:
                js_errors.append((p, r.stderr.strip() or r.stdout.strip()))
        except Exception as e:
            js_errors.append((p, str(e)))

    print(f"JS dosya sayısı: {len(js_files)}")
    if js_errors:
        print("❌ JS syntax hatası bulundu")
        for p, err in js_errors[:80]:
            print()
            print("DOSYA:", rel(p))
            print(err[:2000])
    else:
        print("✅ Harici JS dosyalarında syntax hatası görünmüyor")

# Embedded script blokları
section("1B) HTML İÇİ SCRIPT BLOKLARI KABA KONTROL")

script_issues = []
html_files = all_files({".html", ".jinja", ".j2"})

if node:
    checked = 0
    skipped = 0

    for p in html_files:
        txt = read(p)
        for m in re.finditer(r"<script\b(?![^>]*\bsrc=)[^>]*>(.*?)</script>", txt, flags=re.I | re.S):
            code = m.group(1).strip()
            if not code:
                continue

            # Jinja içeren blokları node ile kontrol etmiyoruz; yanlış alarm verir.
            if "{{" in code or "{%" in code or "{#" in code:
                skipped += 1
                continue

            checked += 1
            with tempfile.NamedTemporaryFile("w", suffix=".js", delete=False, encoding="utf-8") as f:
                f.write(code)
                tmp = f.name

            try:
                r = subprocess.run(
                    [node, "--check", tmp],
                    capture_output=True,
                    text=True,
                    timeout=20
                )
                if r.returncode != 0:
                    script_issues.append((p, line_of(txt, m.start()), r.stderr.strip() or r.stdout.strip()))
            except Exception as e:
                script_issues.append((p, line_of(txt, m.start()), str(e)))
            finally:
                try:
                    Path(tmp).unlink()
                except Exception:
                    pass

    print(f"Kontrol edilen script bloğu: {checked}")
    print(f"Jinja içerdiği için atlanan script bloğu: {skipped}")

    if script_issues:
        print("❌ HTML içi script syntax sorunu olabilir")
        for p, ln, err in script_issues[:80]:
            print()
            print(f"DOSYA: {rel(p)}:{ln}")
            print(err[:1600])
    else:
        print("✅ Kontrol edilen HTML içi script bloklarında syntax hatası görünmüyor")
else:
    print("⚠️ node olmadığı için HTML içi script kontrolü atlandı")

# ------------------------------------------------------------
# 2) CSS / STYLE BRACE CHECK
# ------------------------------------------------------------
section("2) CSS / STYLE PARANTEZ KONTROLÜ")

css_issues = []

def brace_report(name, text):
    # String/comment temizliği değil; kaba erken uyarı kontrolü.
    open_count = text.count("{")
    close_count = text.count("}")
    if open_count != close_count:
        return f"{{ sayısı={open_count}, }} sayısı={close_count}"
    return None

for p in all_files({".css"}):
    if "/vendor/" in str(p).replace("\\", "/") or "/apk_payload/" in str(p).replace("\\", "/"):
        continue
    txt = read(p)
    rep = brace_report(rel(p), txt)
    if rep:
        css_issues.append((p, None, rep))

for p in html_files:
    txt = read(p)
    for m in re.finditer(r"<style\b[^>]*>(.*?)</style>", txt, flags=re.I | re.S):
        css = m.group(1)
        rep = brace_report(rel(p), css)
        if rep:
            css_issues.append((p, line_of(txt, m.start()), rep))

if css_issues:
    print("⚠️ CSS/style bloklarında parantez dengesizliği olabilir")
    for p, ln, rep in css_issues[:100]:
        loc = f"{rel(p)}:{ln}" if ln else rel(p)
        print(f"{loc} -> {rep}")
else:
    print("✅ CSS/style kaba parantez kontrolü temiz")

# ------------------------------------------------------------
# 3) FLASK ROUTE / URL_FOR / RENDER_TEMPLATE KONTROLÜ
# ------------------------------------------------------------
section("3) FLASK ROUTE / URL_FOR / TEMPLATE REFERANS KONTROLÜ")

py_files = all_files({".py"})
py_text_all = "\n".join(read(p) for p in py_files)

# Route fonksiyonları ve pathleri
route_func_names = set()
route_paths = set()
route_hits = []

for p in py_files:
    txt = read(p)

    # @app.route("/x") / @bp.route("/x")
    for m in re.finditer(r"@\s*[\w\.]+\.route\s*\(\s*['\"]([^'\"]+)['\"]", txt):
        path = m.group(1)
        route_paths.add(path)
        ln = line_of(txt, m.start())
        # Dekoratörden sonraki fonksiyonu bul
        after = txt[m.end():m.end()+500]
        fm = re.search(r"def\s+([A-Za-z_]\w*)\s*\(", after)
        fn = fm.group(1) if fm else "?"
        route_func_names.add(fn)
        route_hits.append((p, ln, path, fn))

print(f"Route decorator sayısı: {len(route_hits)}")
print(f"Route path sayısı: {len(route_paths)}")
print(f"Route function sayısı: {len(route_func_names)}")

# url_for çağrıları
urlfor_hits = []
urlfor_suspect = []

for p in html_files + py_files:
    txt = read(p)
    for m in re.finditer(r"url_for\s*\(\s*['\"]([^'\"]+)['\"]", txt):
        endpoint = m.group(1)
        if endpoint == "static":
            continue
        urlfor_hits.append((p, line_of(txt, m.start()), endpoint))

        fn = endpoint.split(".")[-1]
        # Blueprint endpointlerinde sadece fonksiyon adını kontrol ediyoruz.
        if fn not in route_func_names:
            urlfor_suspect.append((p, line_of(txt, m.start()), endpoint))

print(f"url_for endpoint sayısı: {len(urlfor_hits)}")

if urlfor_suspect:
    print("⚠️ url_for endpoint şüpheli / route fonksiyonu bulunamadı")
    for p, ln, endpoint in urlfor_suspect[:100]:
        print(f"{rel(p)}:{ln} -> url_for('{endpoint}')")
else:
    print("✅ url_for endpointleri route fonksiyonlarıyla uyumlu görünüyor")

# render_template dosya kontrolü
render_missing = []
render_hits = []

template_roots = [
    ROOT / "templates",
    ROOT / "android_app/app/src/main/python/templates",
]

for p in py_files:
    txt = read(p)
    for m in re.finditer(r"render_template\s*\(\s*['\"]([^'\"]+)['\"]", txt):
        tpl = m.group(1)
        render_hits.append((p, line_of(txt, m.start()), tpl))

        exists_any = any((base / tpl).exists() for base in template_roots if base.exists())
        if not exists_any:
            render_missing.append((p, line_of(txt, m.start()), tpl))

print(f"render_template referans sayısı: {len(render_hits)}")

if render_missing:
    print("❌ render_template ile çağrılan ama bulunamayan template var")
    for p, ln, tpl in render_missing[:100]:
        print(f"{rel(p)}:{ln} -> {tpl}")
else:
    print("✅ render_template template dosyaları mevcut görünüyor")

# ------------------------------------------------------------
# 4) FETCH API YOLU KONTROLÜ
# ------------------------------------------------------------
section("4) FRONTEND FETCH/API YOLU KONTROLÜ")

fetch_hits = []
fetch_paths = set()

fetch_re = re.compile(r"""fetch\s*\(\s*([`'"])(.+?)\1""", re.S)

for p in all_files({".html", ".js"}):
    if "/vendor/" in str(p).replace("\\", "/") or "/apk_payload/" in str(p).replace("\\", "/"):
        continue
    txt = read(p)

    for m in fetch_re.finditer(txt):
        raw = m.group(2).strip()
        ln = line_of(txt, m.start())

        # Template literal içinde ${} olsa bile başı sabitse alıyoruz.
        path = raw.split("?")[0].split("#")[0].strip()
        if path.startswith("http"):
            fetch_hits.append((p, ln, raw, "absolute"))
            fetch_paths.add(path)
        elif path.startswith("/"):
            fetch_hits.append((p, ln, raw, "root"))
            fetch_paths.add(path)
        else:
            fetch_hits.append((p, ln, raw, "relative"))

print(f"fetch çağrısı sayısı: {len(fetch_hits)}")
print(f"fetch path çeşidi: {len(fetch_paths)}")

# Route path karşılaştırma kaba kontrol
# Blueprint prefixleri net çözülemeyebilir, o yüzden kesin hata değil, sadece şüphe.
api_suspects = []

for p, ln, raw, kind in fetch_hits:
    if kind == "relative":
        continue

    clean = raw.split("?")[0].split("#")[0]
    clean = clean.replace("${tripId}", "").replace("${seat}", "").replace("${stop}", "")
    clean = re.sub(r"\$\{[^}]+\}", "", clean)

    if clean.startswith("http"):
        api_suspects.append((p, ln, raw, "absolute URL / APK içinde risk olabilir"))
        continue

    # /api/x/ gibi dinamik parçaları kırpıp kaba eşleşme
    exact = clean in route_paths
    starts = any(clean.startswith(rp.rstrip("/") + "/") for rp in route_paths if rp != "/")
    similar = any(rp.startswith(clean.rstrip("/") + "/") for rp in route_paths if clean != "/")

    if not (exact or starts or similar):
        # /static hariç
        if not clean.startswith("/static/"):
            api_suspects.append((p, ln, raw, "app route listesinde birebir görünmedi"))

if api_suspects:
    print("⚠️ fetch/API yolu şüpheli olabilir")
    for p, ln, raw, reason in api_suspects[:120]:
        print(f"{rel(p)}:{ln} -> {raw}  [{reason}]")
else:
    print("✅ fetch/API yollarında kaba route uyumsuzluğu görünmüyor")

# ------------------------------------------------------------
# 5) CSRF KONTROLÜ
# ------------------------------------------------------------
section("5) CSRF FORM / FETCH KONTROLÜ")

csrf_form_suspects = []
csrf_fetch_suspects = []

for p in html_files:
    txt = read(p)

    for m in re.finditer(r"<form\b[^>]*method\s*=\s*['\"]?post['\"]?[^>]*>.*?</form>", txt, flags=re.I | re.S):
        block = m.group(0)
        ln = line_of(txt, m.start())
        low = block.lower()

        # login/logout gibi exclude olabilir; yine de not düşelim ama ayrı sebep ile.
        action_m = re.search(r"action\s*=\s*['\"]([^'\"]+)['\"]", block, flags=re.I)
        action = action_m.group(1) if action_m else ""

        if "csrf_token" not in block and "csrf" not in block.lower():
            csrf_form_suspects.append((p, ln, action or "(action yok)"))

    # fetch POST/PUT/PATCH/DELETE bloklarında CSRF header izi var mı?
    for m in re.finditer(
        r"fetch\s*\((?P<body>.*?)(?:\)\s*;|\)\s*\.then|\)\s*catch)",
        txt,
        flags=re.I | re.S
    ):
        body = m.group("body")
        if not re.search(r"method\s*:\s*['\"](?:POST|PUT|PATCH|DELETE)['\"]", body, flags=re.I):
            continue

        ln = line_of(txt, m.start())
        if "csrf" not in body.lower() and "x-csrf" not in body.lower():
            csrf_fetch_suspects.append((p, ln, body[:120].replace("\n", " ")))

for p in all_files({".js"}):
    if "/vendor/" in str(p).replace("\\", "/") or "/apk_payload/" in str(p).replace("\\", "/"):
        continue
    txt = read(p)

    for m in re.finditer(
        r"fetch\s*\((?P<body>.*?)(?:\)\s*;|\)\s*\.then|\)\s*catch)",
        txt,
        flags=re.I | re.S
    ):
        body = m.group("body")
        if not re.search(r"method\s*:\s*['\"](?:POST|PUT|PATCH|DELETE)['\"]", body, flags=re.I):
            continue

        ln = line_of(txt, m.start())
        if "csrf" not in body.lower() and "x-csrf" not in body.lower():
            csrf_fetch_suspects.append((p, ln, body[:120].replace("\n", " ")))

if csrf_form_suspects:
    print("⚠️ POST form içinde CSRF izi yok")
    for p, ln, action in csrf_form_suspects[:100]:
        print(f"{rel(p)}:{ln} -> action={action}")
else:
    print("✅ POST formlarda CSRF izi görünüyor")

if csrf_fetch_suspects:
    print()
    print("⚠️ fetch POST/PUT/PATCH/DELETE içinde CSRF izi yok gibi")
    for p, ln, snippet in csrf_fetch_suspects[:100]:
        print(f"{rel(p)}:{ln} -> {snippet[:160]}")
else:
    print("✅ fetch yazma isteklerinde CSRF izi görünüyor")

# ------------------------------------------------------------
# 6) DUPLICATE ID DETAYLI
# ------------------------------------------------------------
section("6) DUPLICATE ID DETAYLI KONTROL")

dup_results = []

for p in html_files:
    txt = read(p)
    by_id = defaultdict(list)

    for m in re.finditer(r"""\bid\s*=\s*['"]([^'"]+)['"]""", txt):
        by_id[m.group(1)].append(line_of(txt, m.start()))

    dups = {k: v for k, v in by_id.items() if len(v) > 1}
    if dups:
        dup_results.append((p, dups))

if dup_results:
    print("⚠️ Duplicate id bulundu")
    for p, dups in dup_results[:100]:
        print()
        print("DOSYA:", rel(p))
        for k, lines in sorted(dups.items(), key=lambda x: (-len(x[1]), x[0]))[:60]:
            print(f"  id='{k}' tekrar={len(lines)} satırlar={lines[:10]}")
else:
    print("✅ Duplicate id yok")

# ------------------------------------------------------------
# 7) WEB / ANDROID FARK DETAYI
# ------------------------------------------------------------
section("7) WEB / ANDROID FARK DETAYI")

pairs = [
    ("app.py", "android_app/app/src/main/python/app.py"),
    ("templates/base.html", "android_app/app/src/main/python/templates/base.html"),
    ("templates/index.html", "android_app/app/src/main/python/templates/index.html"),
    ("templates/seats.html", "android_app/app/src/main/python/templates/seats.html"),
    ("templates/continue_trip.html", "android_app/app/src/main/python/templates/continue_trip.html"),
    ("templates/reports.html", "android_app/app/src/main/python/templates/reports.html"),
    ("static/seats/seats.js", "android_app/app/src/main/python/static/seats/seats.js"),
    ("static/seats/voice-commands.js", "android_app/app/src/main/python/static/seats/voice-commands.js"),
    ("static/continue/continue_trip_core.js", "android_app/app/src/main/python/static/continue/continue_trip_core.js"),
]

for a, b in pairs:
    pa = ROOT / a
    pb = ROOT / b

    if not pa.exists() or not pb.exists():
        print(f"❌ eksik eşleşme: {a} | {b}")
        continue

    ta = read(pa)
    tb = read(pb)

    if ta == tb:
        print(f"✅ aynı: {a}")
        continue

    print(f"⚠️ farklı: {a}")
    print(f"   web:     {len(ta)} karakter, {ta.count(chr(10))+1} satır")
    print(f"   android: {len(tb)} karakter, {tb.count(chr(10))+1} satır")

    # İlk fark konumu
    first = None
    for i, (ca, cb) in enumerate(zip(ta, tb)):
        if ca != cb:
            first = i
            break
    if first is None and len(ta) != len(tb):
        first = min(len(ta), len(tb))

    if first is not None:
        la = line_of(ta, first)
        lb = line_of(tb, first)
        print(f"   ilk fark yaklaşık: web satır {la}, android satır {lb}")

# ------------------------------------------------------------
# 8) HARDCODED / OFFLINE RISKLER
# ------------------------------------------------------------
section("8) HARDCODED URL / CDN / LOCALHOST RİSKLERİ")

risk_patterns = [
    ("localhost", re.compile(r"localhost|127\.0\.0\.1", re.I)),
    ("http-url", re.compile(r"https?://", re.I)),
    ("cdn", re.compile(r"unpkg\.com|cdn\.jsdelivr|cdnjs|googleapis|gstatic", re.I)),
]

risk_hits = []

for p in all_files(TEXT_EXTS):
    s = str(p).replace("\\", "/")
    if "/vendor/" in s or "/apk_payload/" in s:
        continue

    txt = read(p)
    for name, pat in risk_patterns:
        for m in pat.finditer(txt):
            ln = line_of(txt, m.start())
            line = txt.splitlines()[ln-1] if txt.splitlines() else ""
            risk_hits.append((p, ln, name, line.strip()[:220]))

if risk_hits:
    print("⚠️ Hardcoded/offline risk izi bulundu")
    for p, ln, name, line in risk_hits[:160]:
        print(f"{rel(p)}:{ln} [{name}] {line}")
    if len(risk_hits) > 160:
        print(f"... {len(risk_hits)-160} kayıt daha var")
else:
    print("✅ Hardcoded localhost/http/CDN izi görünmüyor")

# ------------------------------------------------------------
# 9) BİLİNEN KRİTİK KELİME İZLERİ
# ------------------------------------------------------------
section("9) BİLİNEN KRİTİK BUG İZLERİ")

known_needles = [
    "filled + standingCount",
    "tripGuardGo",
    "tripGuardOk",
    "confirm(",
    "alert(",
    "debugger",
    "TODO",
    "FIXME",
    "HACK",
]

for needle in known_needles:
    hits = []
    for p in all_files(TEXT_EXTS):
        s = str(p).replace("\\", "/")
        if "/vendor/" in s or "/apk_payload/" in s:
            continue
        txt = read(p)
        if needle in txt:
            for m in re.finditer(re.escape(needle), txt):
                hits.append((p, line_of(txt, m.start())))
    if hits:
        print(f"⚠️ '{needle}' izi: {len(hits)}")
        for p, ln in hits[:40]:
            print(f"   {rel(p)}:{ln}")
    else:
        print(f"✅ '{needle}' izi yok")

print()
print("===== STEP-2 DERİN DENETİM BİTTİ =====")
