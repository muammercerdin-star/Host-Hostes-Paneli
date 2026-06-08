from pathlib import Path
import difflib
import re

ROOT = Path(".").resolve()

print("===== MUAVİN ASİSTANI STEP-5 AKTİF BUG BAĞLAM DENETİMİ =====")
print("ROOT:", ROOT)
print()

def rel(p):
    try:
        return str(Path(p).resolve().relative_to(ROOT))
    except Exception:
        return str(p)

def read(path):
    return Path(path).read_text(encoding="utf-8", errors="ignore")

def show(path, start, end):
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

def grep_context(path, pattern, before=12, after=18):
    p = ROOT / path
    print()
    print(f"--- {path} içinde arama: {pattern} ---")
    if not p.exists():
        print("❌ dosya yok")
        return

    lines = read(p).splitlines()
    found = False

    for idx, line in enumerate(lines, 1):
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

def section(t):
    print()
    print("===== " + t + " =====")

# ------------------------------------------------------------
# 1) base.html ve static/app.js
# ------------------------------------------------------------
section("1) GLOBAL static/app.js BAĞLAMI")

for path in [
    "templates/base.html",
    "android_app/app/src/main/python/templates/base.html",
    "apk_payload/templates/base.html",
]:
    grep_context(path, "app.js", before=10, after=10)

for path in [
    "static/app.js",
    "android_app/app/src/main/python/static/app.js",
    "apk_payload/static/app.js",
]:
    show(path, 1, 160)
    grep_context(path, "fetch", before=6, after=16)
    grep_context(path, "/api/seat", before=8, after=12)
    grep_context(path, "/api/seats", before=8, after=12)
    grep_context(path, "csrf", before=8, after=12)

# ------------------------------------------------------------
# 2) consignments status endpoint
# ------------------------------------------------------------
section("2) EMANETLER STATUS ENDPOINT BAĞLAMI")

for path in [
    "templates/consignments.html",
    "android_app/app/src/main/python/templates/consignments.html",
]:
    grep_context(path, "/api/consignments/${id}/status", before=18, after=26)
    grep_context(path, "setStatus", before=18, after=30)
    grep_context(path, "status", before=6, after=8)

print()
print("--- app.py içinde consignment route/function araması ---")
for path in ["app.py", "android_app/app/src/main/python/app.py"]:
    grep_context(path, "api_consignments", before=10, after=50)
    grep_context(path, "api_consignment_delete", before=10, after=40)
    grep_context(path, "api_consignment_photos", before=10, after=40)
    grep_context(path, "status", before=4, after=6)

# ------------------------------------------------------------
# 3) reports seat-detail endpoint
# ------------------------------------------------------------
section("3) RAPORLAR seat-detail ENDPOINT BAĞLAMI")

for path in [
    "templates/reports.html",
    "android_app/app/src/main/python/templates/reports.html",
]:
    grep_context(path, "/api/report/seat-detail", before=18, after=30)
    grep_context(path, "seat-detail", before=18, after=30)
    grep_context(path, "Detay", before=10, after=16)

for path in ["app.py", "android_app/app/src/main/python/app.py"]:
    grep_context(path, "api_report", before=8, after=50)
    grep_context(path, "seat_detail", before=8, after=30)
    grep_context(path, "seat-detail", before=8, after=30)

# ------------------------------------------------------------
# 4) index duplicate modal blokları
# ------------------------------------------------------------
section("4) index.html DUPLICATE TRIP GUARD BLOKLARI")

for path in [
    "templates/index.html",
    "android_app/app/src/main/python/templates/index.html",
]:
    grep_context(path, "tripGuardBackdrop", before=8, after=18)
    grep_context(path, "tripGuardModal", before=8, after=18)
    grep_context(path, "tripGuardGo", before=8, after=18)
    grep_context(path, "tripGuardOk", before=8, after=18)

# ------------------------------------------------------------
# 5) seats.js eski sayaç formülü bağlamı
# ------------------------------------------------------------
section("5) seats.js pillTotal / standingCount BAĞLAMI")

for path in [
    "static/seats/seats.js",
    "android_app/app/src/main/python/static/seats/seats.js",
]:
    grep_context(path, "filled + standingCount", before=20, after=20)
    grep_context(path, "pillTotal", before=12, after=12)
    grep_context(path, "standingCount", before=8, after=10)

# ------------------------------------------------------------
# 6) Web / Android farklarının mini diff'i
# ------------------------------------------------------------
section("6) WEB / ANDROID FARKLARI MİNİ DIFF")

pairs = [
    ("app.py", "android_app/app/src/main/python/app.py"),
    ("templates/index.html", "android_app/app/src/main/python/templates/index.html"),
    ("templates/seats.html", "android_app/app/src/main/python/templates/seats.html"),
]

for a, b in pairs:
    pa = ROOT / a
    pb = ROOT / b
    print()
    print(f"--- DIFF: {a}  <->  {b} ---")

    if not pa.exists() or not pb.exists():
        print("❌ eşleşme dosyası eksik")
        continue

    la = read(pa).splitlines()
    lb = read(pb).splitlines()

    diff = list(difflib.unified_diff(
        la, lb,
        fromfile=a,
        tofile=b,
        lineterm="",
        n=3
    ))

    if not diff:
        print("✅ aynı")
        continue

    # İlk 220 satır diff yeterli
    for line in diff[:220]:
        print(line)

    if len(diff) > 220:
        print(f"... diff devam ediyor, toplam diff satırı: {len(diff)}")

# ------------------------------------------------------------
# 7) Eksik static dosya referans bağlamı
# ------------------------------------------------------------
section("7) EKSİK STATIC REFERANS BAĞLAMI")

missing_refs = [
    ("templates/base.html", "vendor/icons.css"),
    ("templates/base.html", "css/style.css"),
    ("templates/base.html", "vendor/jquery.min.js"),
    ("templates/rehber.html", "rehber-koltuk-yonetimi-card.png"),
    ("templates/rehber.html", "rehber-durak-akisi.png"),
    ("templates/rehber.html", "rehber-voice-command.png"),
]

for path, pat in missing_refs:
    grep_context(path, pat, before=8, after=8)

print()
print("===== STEP-5 BİTTİ =====")
