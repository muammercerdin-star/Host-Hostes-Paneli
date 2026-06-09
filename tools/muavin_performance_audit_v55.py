from pathlib import Path
import re
from collections import Counter

ROOT = Path(".").resolve()

FILES = [
    "templates/seats.html",
    "android_app/app/src/main/python/templates/seats.html",
    "templates/index.html",
    "android_app/app/src/main/python/templates/index.html",
    "templates/continue_trip.html",
    "android_app/app/src/main/python/templates/continue_trip.html",

    "static/seats/seats.js",
    "android_app/app/src/main/python/static/seats/seats.js",
    "static/seats/seats.css",
    "android_app/app/src/main/python/static/seats/seats.css",

    "static/continue/continue_trip_core.js",
    "android_app/app/src/main/python/static/continue/continue_trip_core.js",
    "static/continue/continue_trip.css",
    "android_app/app/src/main/python/static/continue/continue_trip.css",
]

JS_KEYS = [
    "setInterval",
    "setTimeout",
    "requestAnimationFrame",
    "watchPosition",
    "getCurrentPosition",
    "renderTimeline",
    "renderRouteStrip",
    "renderAI",
    "render",
    "addEventListener",
    "fetch(",
    "localStorage",
    "getBoundingClientRect",
    "querySelectorAll",
    "innerHTML",
]

CSS_KEYS = [
    "backdrop-filter",
    "-webkit-backdrop-filter",
    "filter:",
    "blur(",
    "box-shadow",
    "text-shadow",
    "animation",
    "transition",
    "position:fixed",
    "position: sticky",
    "z-index",
    "transform",
    "will-change",
]

print("===== MUAVİN PERFORMANS AUDIT V55 =====")
print("ROOT:", ROOT)
print()

def read(path):
    p = ROOT / path
    if not p.exists():
        return ""
    return p.read_text(encoding="utf-8", errors="ignore")

print("===== 1) DOSYA BOYUTLARI =====")
for f in FILES:
    p = ROOT / f
    if p.exists():
        print(f"{f:75s} {p.stat().st_size/1024:8.1f} KB  satır={len(read(f).splitlines())}")
    else:
        print("YOK:", f)

print()
print("===== 2) HTML SCRIPT / CSS LINK SAYISI =====")
for f in FILES:
    if not f.endswith(".html"):
        continue
    s = read(f)
    if not s:
        continue
    scripts = re.findall(r"<script\b", s, flags=re.I)
    links = re.findall(r"<link\b", s, flags=re.I)
    inline_scripts = re.findall(r"<script\b(?![^>]*src=)", s, flags=re.I)
    print()
    print("-----", f, "-----")
    print("link:", len(links), "script:", len(scripts), "inline script:", len(inline_scripts))
    for i, line in enumerate(s.splitlines(), 1):
        if "<script" in line or "<link" in line:
            print(f"{i:5d}: {line[:240]}")

print()
print("===== 3) JS AĞIRLIK İZLERİ =====")
for f in FILES:
    if not f.endswith(".js") and not f.endswith(".html"):
        continue
    s = read(f)
    if not s:
        continue

    counts = {k: s.count(k) for k in JS_KEYS if s.count(k)}
    if counts:
        print()
        print("-----", f, "-----")
        for k, v in sorted(counts.items(), key=lambda x: -x[1]):
            print(f"{k:24s}: {v}")

        print("Önemli satırlar:")
        for i, line in enumerate(s.splitlines(), 1):
            low = line.lower()
            if any(k.lower() in low for k in ["setinterval", "watchposition", "renderroute", "rendertimeline", "renderai", "requestanimationframe", "getboundingclientrect", "queryselectorall"]):
                print(f"{i:5d}: {line[:260]}")

print()
print("===== 4) CSS AĞIRLIK İZLERİ =====")
for f in FILES:
    if not f.endswith(".css") and not f.endswith(".html"):
        continue
    s = read(f)
    if not s:
        continue

    counts = {}
    low = s.lower()
    for k in CSS_KEYS:
        counts[k] = low.count(k.lower())

    counts = {k:v for k,v in counts.items() if v}
    if counts:
        print()
        print("-----", f, "-----")
        for k, v in sorted(counts.items(), key=lambda x: -x[1]):
            print(f"{k:28s}: {v}")

print()
print("===== 5) EN MUHTEMEL KASMA KAYNAKLARI =====")
print("1. Çok fazla CSS glass/backdrop-filter/box-shadow varsa mobilde FPS düşer.")
print("2. watchPosition + highAccuracy + sürekli render varsa dokunmalar geç işlenir.")
print("3. renderTimeline/renderRouteStrip/renderAI sık çalışıyorsa ana thread dolar.")
print("4. Büyük seats.css + çok patch dosyası WebView/Chrome'da layout hesaplamasını ağırlaştırır.")
print("5. fixed/sticky/z-index katmanları fazla ise dokunma ve repaint maliyeti artar.")
