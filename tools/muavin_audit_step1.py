from pathlib import Path
import py_compile
import re
import sys
import hashlib

ROOT = Path(".").resolve()

SKIP_DIRS = {
    ".git", "__pycache__", ".venv", "venv", "env",
    "build", "dist", ".gradle", "node_modules"
}

print("===== MUAVİN ASİSTANI STEP-1 DENETİM =====")
print("ROOT:", ROOT)
print()

def is_skipped(path: Path):
    return any(part in SKIP_DIRS for part in path.parts)

def rel(path: Path):
    try:
        return str(path.resolve().relative_to(ROOT))
    except Exception:
        return str(path)

# ------------------------------------------------------------
# 1) PYTHON SYNTAX KONTROL
# ------------------------------------------------------------
print("===== 1) PYTHON SYNTAX KONTROL =====")

py_files = [
    p for p in ROOT.rglob("*.py")
    if not is_skipped(p)
]

py_errors = []

for p in py_files:
    try:
        py_compile.compile(str(p), doraise=True)
    except Exception as e:
        py_errors.append((p, e))

print(f"Python dosya sayısı: {len(py_files)}")

if py_errors:
    print("❌ PYTHON SYNTAX HATASI VAR")
    for p, e in py_errors:
        print()
        print("DOSYA:", rel(p))
        print(e)
else:
    print("✅ Python syntax sağlam")

print()

# ------------------------------------------------------------
# 2) JINJA TEMPLATE PARSE KONTROL
# ------------------------------------------------------------
print("===== 2) JINJA TEMPLATE PARSE KONTROL =====")

jinja_errors = []
template_files = []

try:
    from jinja2 import Environment, FileSystemLoader
    templates_dir = ROOT / "templates"

    if templates_dir.exists():
        env = Environment(loader=FileSystemLoader(str(templates_dir)))

        template_files = [
            p for p in templates_dir.rglob("*")
            if p.is_file() and p.suffix.lower() in {".html", ".jinja", ".j2"}
        ]

        for p in template_files:
            name = str(p.relative_to(templates_dir))
            try:
                src = p.read_text(encoding="utf-8", errors="ignore")
                env.parse(src)
            except Exception as e:
                jinja_errors.append((p, e))

        print(f"Template dosya sayısı: {len(template_files)}")

        if jinja_errors:
            print("❌ JINJA TEMPLATE HATASI VAR")
            for p, e in jinja_errors:
                print()
                print("DOSYA:", rel(p))
                print(e)
        else:
            print("✅ Jinja parse sağlam")
    else:
        print("⚠️ templates klasörü bulunamadı")

except Exception as e:
    print("⚠️ Jinja kontrolü çalışmadı:", e)

print()

# ------------------------------------------------------------
# 3) STATIC BAĞLANTI KONTROLÜ
# ------------------------------------------------------------
print("===== 3) STATIC DOSYA BAĞLANTI KONTROLÜ =====")

missing_static = []
static_refs = []

html_like_files = []
for folder in ["templates", "android_app/app/src/main/python/templates"]:
    base = ROOT / folder
    if base.exists():
        html_like_files.extend([
            p for p in base.rglob("*")
            if p.is_file() and p.suffix.lower() in {".html", ".jinja", ".j2"}
        ])

patterns = [
    re.compile(r'''(?:src|href)=["'](/?static/[^"'\?#]+)''', re.I),
    re.compile(r'''url_for\(["']static["']\s*,\s*filename=["']([^"']+)["']''', re.I),
]

def static_path_from_ref(ref):
    ref = ref.strip()
    if ref.startswith("/static/"):
        return ROOT / ref.lstrip("/")
    if ref.startswith("static/"):
        return ROOT / ref
    return ROOT / "static" / ref

for p in html_like_files:
    txt = p.read_text(encoding="utf-8", errors="ignore")

    for m in patterns[0].finditer(txt):
        ref = m.group(1)
        static_refs.append((p, ref))
        target = static_path_from_ref(ref)
        if not target.exists():
            missing_static.append((p, ref, target))

    for m in patterns[1].finditer(txt):
        ref = m.group(1)
        static_refs.append((p, ref))
        target = static_path_from_ref(ref)
        if not target.exists():
            missing_static.append((p, ref, target))

print(f"Static referans sayısı: {len(static_refs)}")

if missing_static:
    print("❌ Eksik static dosya var")
    for p, ref, target in missing_static[:120]:
        print(f"{rel(p)} -> {ref}  | BULUNAMADI: {rel(target)}")
    if len(missing_static) > 120:
        print(f"... {len(missing_static)-120} kayıt daha var")
else:
    print("✅ Static dosya bağlantılarında eksik görünmüyor")

print()

# ------------------------------------------------------------
# 4) AYNI HTML İÇİNDE TEKRAR EDEN ID KONTROLÜ
# ------------------------------------------------------------
print("===== 4) DUPLICATE HTML ID KONTROLÜ =====")

dup_id_results = []

for p in html_like_files:
    txt = p.read_text(encoding="utf-8", errors="ignore")
    ids = re.findall(r'''\bid=["']([^"']+)["']''', txt)
    seen = {}
    for idv in ids:
        seen[idv] = seen.get(idv, 0) + 1

    dups = {k: v for k, v in seen.items() if v > 1}

    if dups:
        dup_id_results.append((p, dups))

if dup_id_results:
    print("⚠️ Tekrarlanan id bulundu")
    for p, dups in dup_id_results[:80]:
        print()
        print("DOSYA:", rel(p))
        for k, v in sorted(dups.items(), key=lambda x: (-x[1], x[0]))[:40]:
            print(f"  id='{k}' tekrar: {v}")
else:
    print("✅ Duplicate id görünmüyor")

print()

# ------------------------------------------------------------
# 5) SEATS / KOLTUK KRİTİK İZLER
# ------------------------------------------------------------
print("===== 5) KOLTUK EKRANI KRİTİK İZLER =====")

critical_files = [
    ROOT / "static/seats/seats.js",
    ROOT / "android_app/app/src/main/python/static/seats/seats.js",
    ROOT / "templates/seats.html",
    ROOT / "android_app/app/src/main/python/templates/seats.html",
]

needles = [
    "filled + standingCount",
    "pillTotal",
    "standingCount",
    "ttsEnabled",
    "neighbor_rule_ok",
    "pair_ok",
    "bag-badge",
    "liveStop",
]

for f in critical_files:
    print()
    print("DOSYA:", rel(f))
    if not f.exists():
        print("❌ Yok")
        continue

    txt = f.read_text(encoding="utf-8", errors="ignore")
    print("satır:", txt.count("\\n") + 1)

    for n in needles:
        count = txt.count(n)
        if count:
            print(f"  {n}: {count}")

print()

# ------------------------------------------------------------
# 6) WEB - ANDROID AYNA DOSYA FARKI
# ------------------------------------------------------------
print("===== 6) WEB / ANDROID AYNA DOSYA FARKI =====")

pairs = [
    ("app.py", "android_app/app/src/main/python/app.py"),
    ("templates/seats.html", "android_app/app/src/main/python/templates/seats.html"),
    ("templates/index.html", "android_app/app/src/main/python/templates/index.html"),
    ("templates/continue_trip.html", "android_app/app/src/main/python/templates/continue_trip.html"),
    ("static/seats/seats.js", "android_app/app/src/main/python/static/seats/seats.js"),
]

def sha(p):
    if not p.exists():
        return None
    return hashlib.sha256(p.read_bytes()).hexdigest()

for a, b in pairs:
    pa = ROOT / a
    pb = ROOT / b
    ha = sha(pa)
    hb = sha(pb)

    if ha is None and hb is None:
        print(f"⚠️ ikisi de yok: {a} | {b}")
    elif ha is None:
        print(f"❌ web yok: {a}")
    elif hb is None:
        print(f"❌ android yok: {b}")
    elif ha == hb:
        print(f"✅ aynı: {a} == {b}")
    else:
        print(f"⚠️ farklı: {a} != {b}")

print()

# ------------------------------------------------------------
# 7) TODO / FIXME / HACK / ERROR İZLERİ
# ------------------------------------------------------------
print("===== 7) ŞÜPHELİ NOT / HATA İZLERİ =====")

scan_exts = {".py", ".html", ".js", ".css"}
suspicious = re.compile(r"\b(TODO|FIXME|HACK|BUG|XXX|console\.error|alert\(|debugger)\b", re.I)

hits = []
for p in ROOT.rglob("*"):
    if is_skipped(p):
        continue
    if not p.is_file():
        continue
    if p.suffix.lower() not in scan_exts:
        continue
    txt = p.read_text(encoding="utf-8", errors="ignore")
    for i, line in enumerate(txt.splitlines(), start=1):
        if suspicious.search(line):
            hits.append((p, i, line.strip()))

if hits:
    print(f"⚠️ Şüpheli iz sayısı: {len(hits)}")
    for p, i, line in hits[:120]:
        print(f"{rel(p)}:{i}: {line[:180]}")
    if len(hits) > 120:
        print(f"... {len(hits)-120} kayıt daha var")
else:
    print("✅ Şüpheli TODO/FIXME/HACK/BUG/debugger izi yok")

print()
print("===== STEP-1 DENETİM BİTTİ =====")
