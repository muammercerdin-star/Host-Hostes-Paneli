from pathlib import Path
import re

ROOT = Path(".").resolve()

FILES = [
    "templates/seats.html",
    "android_app/app/src/main/python/templates/seats.html",

    "templates/seats_parts/deck.html",
    "android_app/app/src/main/python/templates/seats_parts/deck.html",

    "static/seats/seats.js",
    "android_app/app/src/main/python/static/seats/seats.js",

    "static/seats/seats.css",
    "android_app/app/src/main/python/static/seats/seats.css",

    "static/seats/seats-final.css",
    "android_app/app/src/main/python/static/seats/seats-final.css",
]

# patch dosyalarını da ekle
for base in [
    ROOT / "static/seats/patches",
    ROOT / "android_app/app/src/main/python/static/seats/patches",
]:
    if base.exists():
        for p in sorted(base.glob("*")):
            if p.suffix in [".css", ".js", ".html"]:
                FILES.append(str(p.relative_to(ROOT)))

KEYS = [
    "bell", "zil", "alarm", "alert", "uyarı", "warning",
    "offload", "inecek", "dropoff", "due",
    "badge", "bag-badge", "svc-badge", "service",
    "seat-alert", "seat-badge", "corner", "pulse",
    "before", "after",
    "overflow", "z-index", "border-radius",
    ".seat", "seat::", "seat ."
]

print("===== MUAVIN BELL / BADGE AUDIT V57 =====")
print("ROOT:", ROOT)
print()

def read(rel):
    p = ROOT / rel
    if not p.exists():
        return ""
    return p.read_text(encoding="utf-8", errors="ignore")

def show_hits(rel, limit=120):
    p = ROOT / rel
    if not p.exists():
        return

    s = read(rel)
    lines = s.splitlines()
    hits = []

    for i, line in enumerate(lines, 1):
        low = line.lower()
        if any(k.lower() in low for k in KEYS):
            hits.append((i, line[:260]))

    if hits:
        print()
        print("-----", rel, "-----")
        print("Satır:", len(lines), "Hit:", len(hits))
        for i, line in hits[:limit]:
            print(f"{i:5d}: {line}")
        if len(hits) > limit:
            print("... devamı:", len(hits) - limit)

print("===== 1) ZİL / BADGE / INECEK İZLERİ =====")
for f in FILES:
    show_hits(f, limit=160)

print()
print("===== 2) SEAT CSS BLOKLARI =====")
css_files = [f for f in FILES if f.endswith(".css")]

for f in css_files:
    s = read(f)
    if not s:
        continue

    lines = s.splitlines()
    print()
    print("-----", f, "-----")

    for i, line in enumerate(lines, 1):
        low = line.lower()
        if (
            ".seat" in low
            or "bag-badge" in low
            or "svc-badge" in low
            or "badge" in low
            or "offload" in low
            or "due" in low
            or "alert" in low
        ):
            start = max(1, i - 4)
            end = min(len(lines), i + 12)
            print(f"\n### BLOK {start}-{end}")
            for j in range(start, end + 1):
                print(f"{j:5d}: {lines[j-1][:260]}")

print()
print("===== 3) SEATS.JS SETSEAT / VISUAL / BADGE BLOKLARI =====")
for f in [
    "static/seats/seats.js",
    "android_app/app/src/main/python/static/seats/seats.js",
]:
    s = read(f)
    if not s:
        continue

    lines = s.splitlines()
    print()
    print("-----", f, "-----")

    for i, line in enumerate(lines, 1):
        low = line.lower()
        if (
            "function setseatvisual" in low
            or "bag-badge" in low
            or "svc-badge" in low
            or "offload" in low
            or "dropoff" in low
            or "alert" in low
            or "badge" in low
        ):
            start = max(1, i - 8)
            end = min(len(lines), i + 18)
            print(f"\n### BLOK {start}-{end}")
            for j in range(start, end + 1):
                print(f"{j:5d}: {lines[j-1][:260]}")

print()
print("===== 4) KISA TEŞHİS NOTU =====")
print("Özellikle şunlara bakacağız:")
print("1. Zil/badge hangi class ile geliyor?")
print("2. Badge absolute ise left/bottom negatif mi?")
print("3. .seat veya parent overflow:hidden mı?")
print("4. Badge z-index koltuk içeriğinin altında mı?")
print("5. Badge koltuk border-radius yüzünden kırpılıyor mu?")
