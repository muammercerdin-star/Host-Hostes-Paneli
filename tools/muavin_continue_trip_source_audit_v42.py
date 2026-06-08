from pathlib import Path
import re

ROOT = Path(".").resolve()

TARGETS = [
    "templates/continue_trip.html",
    "android_app/app/src/main/python/templates/continue_trip.html",
    "static/continue/continue_trip.css",
    "android_app/app/src/main/python/static/continue/continue_trip.css",
    "static/continue/continue_trip_core.js",
    "android_app/app/src/main/python/static/continue/continue_trip_core.js",
    "static/continue/continue_trip_ui.js",
    "android_app/app/src/main/python/static/continue/continue_trip_ui.js",
    "static/continue/continue_flow_refresh.js",
    "android_app/app/src/main/python/static/continue/continue_flow_refresh.js",
    "app.py",
    "android_app/app/src/main/python/app.py",
]

KEYS = [
    "Canlı Durak Akışı",
    "Canlı takip",
    "Canlı takip durumu",
    "Ortahan",
    "Belenyaka",
    "Alaşehir",
    "Aktif sefer var",
    "Devam eden sefere git",
    "Koltuk",
    "koltuk",
    "seat",
    "deck",
    "route",
    "flow",
    "stop",
    "durak",
    "bagaj",
    "inecek",
    "yolcu",
    "continue_trip",
    "render_template",
    "api",
    "fetch",
    "innerHTML",
    "querySelector",
    "addEventListener",
]

print("===== CONTINUE TRIP SOURCE AUDIT V42 =====")
print("ROOT:", ROOT)
print()

def read(p):
    try:
        return p.read_text(encoding="utf-8", errors="ignore")
    except:
        return ""

def show(path, keys, limit=180):
    p = ROOT / path
    print()
    print("-----", path, "-----")

    if not p.exists():
        print("❌ YOK")
        return

    s = read(p)
    lines = s.splitlines()
    hits = []

    for i, line in enumerate(lines, 1):
        low = line.lower()
        for k in keys:
            if k.lower() in low:
                hits.append((i, line[:240]))
                break

    print("Satır:", len(lines), "Boyut:", round(p.stat().st_size / 1024, 1), "KB", "Hit:", len(hits))

    for i, line in hits[:limit]:
        print(f"{i:5d}: {line}")

    if len(hits) > limit:
        print("... devamı:", len(hits) - limit)

print("===== 1) DOĞRU EKRAN DOSYALARI =====")
for t in TARGETS:
    show(t, KEYS, limit=160)

print()
print("===== 2) TÜM PROJEDE EKRAN BAŞLIKLARI NEREDE? =====")
patterns = [
    "Canlı Durak Akışı",
    "Canlı takip durumu",
    "Aktif sefer var",
    "Devam eden sefere git",
    "Ortahan",
    "Belenyaka",
]

for pat in patterns:
    print()
    print("###", pat)
    for p in ROOT.rglob("*"):
        if not p.is_file():
            continue
        if ".git" in p.parts:
            continue
        if p.suffix.lower() not in [".html", ".css", ".js", ".py"]:
            continue

        rel = str(p.relative_to(ROOT))
        try:
            s = p.read_text(encoding="utf-8", errors="ignore")
        except:
            continue

        if pat.lower() in s.lower():
            for i, line in enumerate(s.splitlines(), 1):
                if pat.lower() in line.lower():
                    print(f"{rel}:{i}: {line[:220]}")

print()
print("===== 3) CANLI TAKİP SAYFASI HANGİ CSS/JS DOSYALARINI ÇAĞIRIYOR? =====")
for path in ["templates/continue_trip.html", "android_app/app/src/main/python/templates/continue_trip.html"]:
    p = ROOT / path
    print()
    print("-----", path, "-----")
    if not p.exists():
        print("❌ YOK")
        continue

    s = read(p)
    for i, line in enumerate(s.splitlines(), 1):
        if "<link" in line or "<script" in line:
            print(f"{i:5d}: {line[:240]}")

print()
print("===== 4) KOLTUK PLANI PARÇASI =====")
for path in [
    "templates/seats_parts/deck.html",
    "android_app/app/src/main/python/templates/seats_parts/deck.html",
    "static/seats/seats.js",
    "android_app/app/src/main/python/static/seats/seats.js",
]:
    show(path, [
        "deck",
        "seat",
        "koltuk",
        "openSeat",
        "saveSeat",
        "closeSeat",
        "modal",
        "api",
        "fetch",
        "currentSeat",
        "data-seat",
        "seat-",
    ], limit=180)

print()
print("===== 5) V40 / ÖNCEKİ KOLTUK PANELİ KALINTISI VAR MI? =====")
for pat in [
    "live-seat",
    "koltuklar",
    "Koltuklar",
    "seat-panel",
    "live-map-seat",
    "continue-seat",
]:
    found = []
    for p in ROOT.rglob("*"):
        if not p.is_file():
            continue
        if ".git" in p.parts:
            continue
        if p.suffix.lower() not in [".html", ".css", ".js", ".py"]:
            continue
        s = read(p)
        if pat in s:
            found.append(str(p.relative_to(ROOT)))
    print(pat, "=>", sorted(set(found))[:40])

print()
print("✅ V42 rapor bitti. Bu rapora göre doğru dosyaya dokunacağız.")
