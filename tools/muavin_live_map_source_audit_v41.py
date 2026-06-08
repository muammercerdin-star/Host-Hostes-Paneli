from pathlib import Path
import re

ROOT = Path(".").resolve()

FILES = [
    "templates/live_map.html",
    "android_app/app/src/main/python/templates/live_map.html",
    "templates/seats.html",
    "android_app/app/src/main/python/templates/seats.html",
    "templates/seats_parts/deck.html",
    "android_app/app/src/main/python/templates/seats_parts/deck.html",
    "templates/seats_parts/route_flow.html",
    "android_app/app/src/main/python/templates/seats_parts/route_flow.html",
    "app.py",
    "android_app/app/src/main/python/app.py",
]

STATIC_DIRS = [
    "static/live_map",
    "android_app/app/src/main/python/static/live_map",
    "static/seats",
    "android_app/app/src/main/python/static/seats",
]

KEYWORDS = [
    "Canlı Durak Akışı",
    "Durak Akışı",
    "Sıradaki",
    "Ortahan",
    "Belenyaka",
    "Belenyaka",
    "Aktif sefer",
    "Devam eden sefere git",
    "seat",
    "koltuk",
    "deck",
    "route",
    "stop",
    "live",
    "bag",
    "baggage",
    "yolcu",
    "inecek",
]

print("===== LIVE MAP SOURCE AUDIT V41 =====")
print("ROOT:", ROOT)
print()

def read(p):
    try:
        return p.read_text(encoding="utf-8", errors="ignore")
    except:
        return ""

def show_hits(path, patterns, limit=80):
    p = ROOT / path
    if not p.exists():
        print("❌ YOK:", path)
        return

    s = read(p)
    lines = s.splitlines()
    hits = []

    for i, line in enumerate(lines, 1):
        low = line.lower()
        for pat in patterns:
            if pat.lower() in low:
                hits.append((i, line[:220]))
                break

    print()
    print("-----", path, "-----")
    print("Satır:", len(lines), "Boyut:", round(p.stat().st_size/1024, 1), "KB")
    print("Hit:", len(hits))

    for i, line in hits[:limit]:
        print(f"{i:5d}: {line}")

    if len(hits) > limit:
        print("... devamı:", len(hits) - limit)

print("===== 1) LIVE_MAP TEMPLATE LINK / SCRIPT / ÖNEMLİ SATIRLAR =====")
for path in ["templates/live_map.html", "android_app/app/src/main/python/templates/live_map.html"]:
    show_hits(path, [
        "<link", "<script", "stylesheet", ".css", ".js",
        "Canlı", "Durak", "Sıradaki", "Ortahan", "Belenyaka",
        "id=", "class="
    ], limit=180)

print()
print("===== 2) LIVE_MAP STATIC DOSYALARI =====")
for d in STATIC_DIRS[:2]:
    dd = ROOT / d
    print()
    print("-----", d, "-----")
    if not dd.exists():
        print("❌ YOK")
        continue
    for f in sorted(dd.rglob("*")):
        if f.is_file():
            print(f"{round(f.stat().st_size/1024,1):8.1f} KB  {f.relative_to(ROOT)}")

print()
print("===== 3) LIVE_MAP CSS/JS İÇİNDE ANAHTAR KELİMELER =====")
for d in STATIC_DIRS[:2]:
    dd = ROOT / d
    if not dd.exists():
        continue
    for f in sorted(dd.rglob("*")):
        if f.is_file() and f.suffix.lower() in [".css", ".js"]:
            rel = str(f.relative_to(ROOT))
            show_hits(rel, KEYWORDS + [
                "addEventListener", "onclick", "fetch", "api", "innerHTML",
                "querySelector", "modal", "overlay", "panel"
            ], limit=120)

print()
print("===== 4) KOLTUK EKRANI KAYNAKLARI: DECK / ROUTE_FLOW =====")
for path in [
    "templates/seats_parts/deck.html",
    "android_app/app/src/main/python/templates/seats_parts/deck.html",
    "templates/seats_parts/route_flow.html",
    "android_app/app/src/main/python/templates/seats_parts/route_flow.html",
]:
    show_hits(path, [
        "deck", "seat", "koltuk", "fab", "route", "flow", "Durak", "Sıradaki",
        "id=", "class=", "button"
    ], limit=160)

print()
print("===== 5) APP.PY ROUTE / API KAYNAKLARI =====")
for path in ["app.py", "android_app/app/src/main/python/app.py"]:
    show_hits(path, [
        "@app.route", "@app.get", "@app.post", "live_map", "live", "seats",
        "route_flow", "stop", "seat", "jsonify", "api", "trip"
    ], limit=220)

print()
print("===== 6) HANGİ CSS/JS LIVE_MAP TARAFINDAN ÇAĞRILIYOR? =====")
for path in ["templates/live_map.html", "android_app/app/src/main/python/templates/live_map.html"]:
    p = ROOT / path
    if not p.exists():
        continue

    s = read(p)
    refs = re.findall(r'(?:href|src)=["\']([^"\']+)["\']', s)
    print()
    print("-----", path, "-----")
    for r in refs:
        if "static" in r or r.endswith(".js") or r.endswith(".css"):
            print(r)

print()
print("===== 7) KISA PATRON ÖZETİ =====")
print("Bu rapora göre karar vereceğiz:")
print("1. Canlı takip kartları HTML mi JS ile mi üretiliyor?")
print("2. Koltuk ekranındaki deck doğrudan taşınabilir mi yoksa endpoint ister mi?")
print("3. Açılır panel live_map içine mi konacak, yoksa seats deck component'i mi kopyalanacak?")
print("4. Hangi dosyaya dokunacağımızı rapordan sonra netleştireceğiz.")
