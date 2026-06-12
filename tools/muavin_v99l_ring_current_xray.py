from pathlib import Path
from datetime import datetime
import re
import hashlib

ROOT = Path(".").resolve()

FILES = {
    "WEB_TEMPLATE": ROOT / "templates/continue_trip.html",
    "WEB_CSS": ROOT / "static/continue/continue_trip_v99_clean.css",
    "WEB_JS": ROOT / "static/continue/continue_trip_v99_clean.js",
    "ANDROID_TEMPLATE": ROOT / "android_app/app/src/main/python/templates/continue_trip.html",
    "ANDROID_CSS": ROOT / "android_app/app/src/main/python/static/continue/continue_trip_v99_clean.css",
    "ANDROID_JS": ROOT / "android_app/app/src/main/python/static/continue/continue_trip_v99_clean.js",
}

print("===== V99L MEVCUT RING / RENK / PULSE RÖNTGEN =====")
print("TIME:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
print("ROOT:", ROOT)

def read(p):
    return p.read_text(encoding="utf-8", errors="ignore") if p.exists() else ""

def sha(p):
    if not p.exists():
        return "-"
    return hashlib.sha256(p.read_bytes()).hexdigest()[:12]

print()
print("===== 1) DOSYA DURUMU =====")
for name, p in FILES.items():
    if p.exists():
        print(f"{name:18} VAR size={p.stat().st_size:<8} sha={sha(p)} {p}")
    else:
        print(f"{name:18} YOK {p}")

print()
print("===== 2) WEB / ANDROID SENKRON =====")
pairs = [
    ("TEMPLATE", FILES["WEB_TEMPLATE"], FILES["ANDROID_TEMPLATE"]),
    ("CSS", FILES["WEB_CSS"], FILES["ANDROID_CSS"]),
    ("JS", FILES["WEB_JS"], FILES["ANDROID_JS"]),
]
for label, a, b in pairs:
    if a.exists() and b.exists():
        print(f"{label:10} {'AYNI' if sha(a)==sha(b) else 'FARKLI'} web={sha(a)} android={sha(b)}")
    else:
        print(f"{label:10} KONTROL_EDILEMEDI")

tpl = read(FILES["WEB_TEMPLATE"])
css = read(FILES["WEB_CSS"])
js = read(FILES["WEB_JS"])

print()
print("===== 3) TEMPLATE RING ID / CLASS KONTROL =====")
for key in [
    'id="ringFill"',
    'id="ringKm"',
    'class="ring-fill"',
    'class="v99-ring-fill"',
    'class="ring-wrap"',
    'class="v99-ring-wrap"',
    'class="ring-svg"',
    'class="v99-ring-svg"',
    'id="ring"',
    'v99-prox-card',
]:
    print(("TPL VAR  " if key in tpl else "TPL YOK  ") + key)

print()
print("===== 4) CSS RING / ANIMATION / GLOW KONTROL =====")
for key in [
    "ring-fill",
    "v99-ring-fill",
    "ring-wrap",
    "v99-ring-wrap",
    "ring-pulse",
    "pulse",
    "@keyframes",
    "box-shadow",
    "drop-shadow",
    "filter",
    "animation",
    "urgent",
    "stroke",
]:
    print(("CSS VAR  " if key in css else "CSS YOK  ") + key)

print()
print("===== 5) JS RING RENK MOTORU KONTROL =====")
for key in [
    "function setRing",
    "setRing(km)",
    "ringFill",
    "ringKm",
    "safeKm <= 5",
    "safeKm <= 15",
    "#e03030",
    "#e08820",
    "#3a8bff",
    "textShadow",
    "drop-shadow",
    "classList.add",
    "urgent",
]:
    print(("JS VAR   " if key in js else "JS YOK   ") + key)

print()
print("===== 6) TEMPLATE RING SATIRLARI =====")
for i, line in enumerate(tpl.splitlines(), 1):
    if any(k in line for k in ["ring", "Ring", "ringFill", "ringKm", "svg", "circle"]):
        print(f"{i:4}: {line[:240]}")

print()
print("===== 7) CSS RING / PULSE SATIRLARI =====")
for i, line in enumerate(css.splitlines(), 1):
    low = line.lower()
    if any(k in low for k in ["ring", "pulse", "keyframes", "animation", "box-shadow", "drop-shadow", "filter", "urgent"]):
        print(f"{i:4}: {line[:260]}")

print()
print("===== 8) JS setRing BLOĞU =====")
lines = js.splitlines()
for i, line in enumerate(lines, 1):
    if "function setRing" in line:
        start = max(1, i - 8)
        end = min(len(lines), i + 70)
        for n in range(start, end + 1):
            print(f"{n:4}: {lines[n-1][:260]}")
        break

print()
print("===== 9) SONUÇ NOTU =====")
renk_var = all(x in js for x in ["#e03030", "#e08820", "#3a8bff"]) or ("safeKm <= 5" in js and "safeKm <= 15" in js)
ring_id = "ringFill" if 'id="ringFill"' in tpl or "ringFill" in js else ("ring" if 'id="ring"' in tpl else "BULUNAMADI")

print("RING_ID_ADAYI:", ring_id)
print("RENK_DEGISIM_MANTIGI:", "VAR" if renk_var else "NET_DEGIL")
print("PULSE_ANIMATION:", "VAR" if ("animation" in css or "pulse" in css or "urgent" in js) else "YOK")
print()
print("✅ RÖNTGEN BİTTİ - dosyaya dokunulmadı")
