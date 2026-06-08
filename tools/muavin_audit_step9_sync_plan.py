from pathlib import Path
import hashlib
import difflib

ROOT = Path(".").resolve()

print("===== MUAVİN ASİSTANI STEP-9 WEB/ANDROID SENKRON PLANI =====")
print("ROOT:", ROOT)
print()

def read(p):
    return Path(p).read_text(encoding="utf-8", errors="ignore")

def sha(p):
    p = ROOT / p
    if not p.exists():
        return None
    return hashlib.sha256(p.read_bytes()).hexdigest()[:12]

def exists(p):
    return (ROOT / p).exists()

def lines(p):
    p = ROOT / p
    if not p.exists():
        return 0
    return read(p).count("\n") + 1

def section(t):
    print()
    print("===== " + t + " =====")

pairs = [
    ("app.py", "android_app/app/src/main/python/app.py"),
    ("templates/base.html", "android_app/app/src/main/python/templates/base.html"),
    ("templates/index.html", "android_app/app/src/main/python/templates/index.html"),
    ("templates/seats.html", "android_app/app/src/main/python/templates/seats.html"),
    ("templates/continue_trip.html", "android_app/app/src/main/python/templates/continue_trip.html"),
    ("templates/consignments.html", "android_app/app/src/main/python/templates/consignments.html"),
    ("templates/reports.html", "android_app/app/src/main/python/templates/reports.html"),
    ("templates/rehber.html", "android_app/app/src/main/python/templates/rehber.html"),
    ("static/app.js", "android_app/app/src/main/python/static/app.js"),
    ("static/seats/seats.js", "android_app/app/src/main/python/static/seats/seats.js"),
    ("static/seats/voice-commands.js", "android_app/app/src/main/python/static/seats/voice-commands.js"),
    ("static/continue/continue_trip_core.js", "android_app/app/src/main/python/static/continue/continue_trip_core.js"),
]

section("1) ANA WEB / ANDROID DOSYA EŞLEŞMELERİ")

for web, andr in pairs:
    ew = exists(web)
    ea = exists(andr)
    sw = sha(web)
    sa = sha(andr)

    if not ew or not ea:
        print(f"❌ EKSİK: {web} exists={ew} | {andr} exists={ea}")
        continue

    if sw == sa:
        print(f"✅ AYNI: {web}")
    else:
        print(f"⚠️ FARKLI: {web}")
        print(f"   web     sha={sw} satır={lines(web)}")
        print(f"   android sha={sa} satır={lines(andr)}")

section("2) BİLİNEN YAMA İZLERİ WEB/ANDROID")

needles = [
    "ACTIVE_ROUTE_LOCK_FINAL_START",
    "route-sheet-no-flash-fix",
    "home-font-barlow-settings",
    "unified-seat-deck-report-style.css",
    "filled + standingCount",
    "/api/report/seat-detail",
    "/api/consignments/${id}/status",
    "static/app.js",
    "vendor/jquery.min.js",
]

files = [
    "templates/index.html",
    "android_app/app/src/main/python/templates/index.html",
    "templates/seats.html",
    "android_app/app/src/main/python/templates/seats.html",
    "static/seats/seats.js",
    "android_app/app/src/main/python/static/seats/seats.js",
    "templates/reports.html",
    "android_app/app/src/main/python/templates/reports.html",
    "templates/consignments.html",
    "android_app/app/src/main/python/templates/consignments.html",
    "templates/base.html",
    "android_app/app/src/main/python/templates/base.html",
]

for f in files:
    print()
    print(f"--- {f} ---")
    if not exists(f):
        print("YOK")
        continue
    txt = read(ROOT / f)
    for n in needles:
        c = txt.count(n)
        if c:
            print(f"{n}: {c}")

section("3) MINI DIFF ÖZETİ")

for web, andr in pairs[:8]:
    if not exists(web) or not exists(andr):
        continue

    a = read(ROOT / web).splitlines()
    b = read(ROOT / andr).splitlines()

    if a == b:
        continue

    print()
    print(f"--- DIFF ÖZET: {web} ---")
    diff = list(difflib.unified_diff(a, b, fromfile=web, tofile=andr, n=2, lineterm=""))

    shown = 0
    for line in diff:
        if shown >= 120:
            print(f"... diff kesildi, toplam diff satırı: {len(diff)}")
            break
        print(line)
        shown += 1

section("4) SENKRON ADAYLARI - NOT")

print("""
Düzeltme yapmıyoruz. Sadece aday notu:

A) Web -> Android kopyalanması muhtemel dosyalar:
   - templates/index.html
   - templates/seats.html

B) İki tarafta beraber değişmesi gereken dosyalar:
   - static/app.js
   - android_app/app/src/main/python/static/app.js
   - static/seats/seats.js
   - android_app/app/src/main/python/static/seats/seats.js
   - templates/base.html
   - android_app/app/src/main/python/templates/base.html
   - templates/reports.html
   - android_app/app/src/main/python/templates/reports.html
   - templates/consignments.html
   - android_app/app/src/main/python/templates/consignments.html

C) Dikkat:
   app.py farklı ama fark küçük görünüyor. Kör kopyalama yapmadan önce route/fonksiyon farkı ayrıca okunmalı.
""")

print()
print("===== STEP-9 BİTTİ =====")
