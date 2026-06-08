from pathlib import Path
import re

ROOT = Path(".").resolve()

print("===== MUAVİN ASİSTANI STEP-7 GLOBAL app.js DENETİMİ =====")
print("ROOT:", ROOT)
print()

def read(p):
    return Path(p).read_text(encoding="utf-8", errors="ignore")

def rel(p):
    try:
        return str(Path(p).resolve().relative_to(ROOT))
    except Exception:
        return str(p)

def section(t):
    print()
    print("===== " + t + " =====")

def show(path):
    p = ROOT / path
    print()
    print(f"--- {path} ---")
    if not p.exists():
        print("❌ dosya yok")
        return

    lines = read(p).splitlines()
    for i, line in enumerate(lines, 1):
        print(f"{i:5}: {line}")

def grep_all(patterns, exts={".html", ".js", ".py"}):
    skip = {".git", "__pycache__", ".venv", "venv", "env", "build", "dist", ".gradle", "node_modules", "audit_reports"}
    hits = []

    for p in ROOT.rglob("*"):
        if any(part in skip for part in p.parts):
            continue
        if not p.is_file() or p.suffix.lower() not in exts:
            continue

        s = str(p).replace("\\", "/")
        if "/vendor/" in s or "/apk_payload/" in s:
            continue

        txt = read(p)
        lines = txt.splitlines()

        for i, line in enumerate(lines, 1):
            for pat in patterns:
                if pat in line:
                    hits.append((p, i, pat, line.strip()[:240]))

    return hits

section("1) static/app.js TAM İÇERİK")
show("static/app.js")

section("2) Android static/app.js TAM İÇERİK")
show("android_app/app/src/main/python/static/app.js")

section("3) base.html app.js/jQuery bağlamı")
for path in [
    "templates/base.html",
    "android_app/app/src/main/python/templates/base.html",
]:
    p = ROOT / path
    print()
    print(f"--- {path} ---")
    if p.exists():
        lines = read(p).splitlines()
        for i, line in enumerate(lines, 1):
            if "jquery" in line.lower() or "app.js" in line or "bootstrap" in line:
                print(f"{i:5}: {line}")

section("4) app.js içindeki fonksiyon isimleri")
for path in ["static/app.js", "android_app/app/src/main/python/static/app.js"]:
    p = ROOT / path
    print()
    print(f"--- {path} ---")
    if not p.exists():
        print("yok")
        continue

    txt = read(p)

    names = []
    names += re.findall(r"function\s+([A-Za-z_$][\w$]*)\s*\(", txt)
    names += re.findall(r"const\s+([A-Za-z_$][\w$]*)\s*=\s*(?:async\s*)?\(", txt)
    names += re.findall(r"let\s+([A-Za-z_$][\w$]*)\s*=\s*(?:async\s*)?\(", txt)
    names += re.findall(r"var\s+([A-Za-z_$][\w$]*)\s*=\s*(?:async\s*)?\(", txt)
    names += re.findall(r"window\.([A-Za-z_$][\w$]*)\s*=", txt)

    if names:
        for n in sorted(set(names)):
            print("FUNC:", n)
    else:
        print("Fonksiyon ismi bulunamadı")

section("5) app.js fonksiyonları template/JS içinde kullanılıyor mu?")

app_path = ROOT / "static/app.js"
app_txt = read(app_path) if app_path.exists() else ""

names = []
names += re.findall(r"function\s+([A-Za-z_$][\w$]*)\s*\(", app_txt)
names += re.findall(r"window\.([A-Za-z_$][\w$]*)\s*=", app_txt)
names = sorted(set(names))

if not names:
    print("static/app.js içinde yakalanan global fonksiyon yok.")
else:
    for name in names:
        print()
        print(f"--- kullanım araması: {name} ---")
        hits = grep_all([name])
        real_hits = []
        for p, i, pat, line in hits:
            # static/app.js içindeki tanımı sayma
            if rel(p) == "static/app.js":
                continue
            if rel(p) == "android_app/app/src/main/python/static/app.js":
                continue
            real_hits.append((p, i, line))

        if real_hits:
            for p, i, line in real_hits[:80]:
                print(f"{rel(p)}:{i}: {line}")
        else:
            print("Kullanım bulunamadı")

section("6) Eski endpoint kullanım araması")

patterns = [
    "/api/seat/clear",
    "/api/seats",
    "/api/report/seat-detail",
    "/api/route-stop",
    "/api/consignments/${id}/status",
]

hits = grep_all(patterns)

if hits:
    for p, i, pat, line in hits:
        print(f"{rel(p)}:{i}: [{pat}] {line}")
else:
    print("Eski endpoint izi bulunamadı")

section("7) jQuery kullanımı var mı?")

jq_patterns = [
    "$(",
    "jQuery",
    "$.",
    ".modal(",
    ".dropdown(",
]

hits = grep_all(jq_patterns, exts={".html", ".js"})

if hits:
    count = 0
    for p, i, pat, line in hits:
        s = rel(p)
        if "/vendor/" in s:
            continue
        print(f"{s}:{i}: [{pat}] {line}")
        count += 1
        if count >= 160:
            print("... ilk 160 kayıt gösterildi")
            break
else:
    print("jQuery kullanım izi bulunamadı")

print()
print("===== STEP-7 BİTTİ =====")
