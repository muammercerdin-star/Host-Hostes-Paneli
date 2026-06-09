from pathlib import Path
import re
from collections import Counter, defaultdict

ROOT = Path(".").resolve()

FILES = [
    "templates/index.html",
    "android_app/app/src/main/python/templates/index.html",
    "templates/seats.html",
    "android_app/app/src/main/python/templates/seats.html",
    "templates/seats_parts/modals.html",
    "android_app/app/src/main/python/templates/seats_parts/modals.html",
    "templates/continue_trip.html",
    "android_app/app/src/main/python/templates/continue_trip.html",
    "static/app.js",
    "android_app/app/src/main/python/static/app.js",
    "static/seats/seats.js",
    "android_app/app/src/main/python/static/seats/seats.js",
    "static/seats/seats.css",
    "android_app/app/src/main/python/static/seats/seats.css",
    "static/continue/continue_trip_core.js",
    "android_app/app/src/main/python/static/continue/continue_trip_core.js",
    "static/continue/continue_trip_ui.js",
    "android_app/app/src/main/python/static/continue/continue_trip_ui.js",
]

KEYS = [
    "saveSeat",
    "Kaydet",
    "kaydet",
    "submit",
    "addEventListener",
    "click",
    "touchstart",
    "touchend",
    "pointerdown",
    "preventDefault",
    "stopPropagation",
    "stopImmediatePropagation",
    "disabled",
    "pointer-events",
    "z-index",
    "overlay",
    "backdrop",
    "modal",
    "tripGuard",
    "loading",
    "fetch(",
    "safeJsonFetch",
]

print("===== MUAVIN CLICK RESPONSE AUDIT V51 =====")
print("ROOT:", ROOT)
print()

def read(path):
    p = ROOT / path
    if not p.exists():
        return ""
    return p.read_text(encoding="utf-8", errors="ignore")

def show_hits(path, keys, limit=160):
    p = ROOT / path
    print()
    print("-----", path, "-----")
    if not p.exists():
        print("❌ YOK")
        return

    s = read(path)
    lines = s.splitlines()
    hits = []

    for i, line in enumerate(lines, 1):
        low = line.lower()
        for k in keys:
            if k.lower() in low:
                hits.append((i, line[:260]))
                break

    print("Satır:", len(lines), "Boyut:", round(p.stat().st_size / 1024, 1), "KB", "Hit:", len(hits))
    for i, line in hits[:limit]:
        print(f"{i:5d}: {line}")
    if len(hits) > limit:
        print("... devamı:", len(hits) - limit)

print("===== 1) KAYDET / TIKLAMA / OVERLAY İZLERİ =====")
for f in FILES:
    show_hits(f, KEYS, limit=120)

print()
print("===== 2) DUPLICATE ID KONTROLÜ =====")
for f in FILES:
    if not f.endswith(".html"):
        continue
    s = read(f)
    if not s:
        continue
    ids = re.findall(r'id=["\']([^"\']+)["\']', s)
    dup = [(k, v) for k, v in Counter(ids).items() if v > 1]
    print()
    print("-----", f, "-----")
    print("Toplam id:", len(ids), "Duplicate:", len(dup))
    for k, v in dup[:80]:
        print(f"  {k}: {v}")

print()
print("===== 3) YÜKSEK Z-INDEX / POINTER EVENTS KONTROLÜ =====")
css_like = [f for f in FILES if f.endswith((".css", ".html"))]
for f in css_like:
    s = read(f)
    if not s:
        continue

    lines = s.splitlines()
    findings = []

    for i, line in enumerate(lines, 1):
        low = line.lower()
        if "z-index" in low or "pointer-events" in low or "position:fixed" in low or "position: fixed" in low:
            findings.append((i, line[:240]))

    if findings:
        print()
        print("-----", f, "-----")
        for i, line in findings[:160]:
            print(f"{i:5d}: {line}")
        if len(findings) > 160:
            print("... devamı:", len(findings) - 160)

print()
print("===== 4) CAPTURE TRUE / STOP IMMEDIATE RİSKİ =====")
for f in FILES:
    s = read(f)
    if not s:
        continue

    lines = s.splitlines()
    hits = []
    for i, line in enumerate(lines, 1):
        low = line.lower()
        if "capture" in low or "stopimmediatepropagation" in low or "stoppropagation" in low:
            hits.append((i, line[:260]))

    if hits:
        print()
        print("-----", f, "-----")
        for i, line in hits[:120]:
            print(f"{i:5d}: {line}")
        if len(hits) > 120:
            print("... devamı:", len(hits) - 120)

print()
print("===== 5) KAYDET BUTONU ID / MODAL YAPISI =====")
for f in [
    "templates/seats.html",
    "android_app/app/src/main/python/templates/seats.html",
    "templates/seats_parts/modals.html",
    "android_app/app/src/main/python/templates/seats_parts/modals.html",
    "static/seats/seats.js",
    "android_app/app/src/main/python/static/seats/seats.js",
]:
    show_hits(f, [
        "seatModal", "seatBackdrop", "seatTitle", "pickup", "dropoff",
        "saveSeat", "btnSave", "Kaydet", "offloadSeat", "closeSeat",
        "currentSeat", "addEventListener", "querySelector"
    ], limit=180)

print()
print("===== 6) ANA SAYFA BUTONLARI / AKTİF SEFER KİLİDİ =====")
for f in [
    "templates/index.html",
    "android_app/app/src/main/python/templates/index.html",
    "static/app.js",
    "android_app/app/src/main/python/static/app.js",
]:
    show_hits(f, [
        "tripGuard", "Aktif sefer", "Devam eden sefere git",
        "routeBtn", "start", "click", "preventDefault",
        "disabled", "pointer-events", "modal", "overlay"
    ], limit=180)

print()
print("===== 7) SCRIPT SIRASI =====")
for f in [
    "templates/index.html",
    "android_app/app/src/main/python/templates/index.html",
    "templates/seats.html",
    "android_app/app/src/main/python/templates/seats.html",
    "templates/continue_trip.html",
    "android_app/app/src/main/python/templates/continue_trip.html",
]:
    s = read(f)
    if not s:
        continue
    print()
    print("-----", f, "-----")
    for i, line in enumerate(s.splitlines(), 1):
        if "<script" in line or "</script>" in line or "<link" in line:
            print(f"{i:5d}: {line[:260]}")

print()
print("===== 8) KISA PATRON NOTU =====")
print("Bu raporda özellikle şunlara bakacağız:")
print("1. Duplicate id var mı?")
print("2. Üstte görünmeyen overlay tıklamayı yutuyor mu?")
print("3. stopImmediatePropagation veya capture:true fazla mı kullanılmış?")
print("4. Kaydet butonunun bağlı olduğu JS fonksiyonu tek mi, çok mu?")
print("5. Ana sayfa aktif sefer kilidi bütün butonları yanlışlıkla engelliyor mu?")
