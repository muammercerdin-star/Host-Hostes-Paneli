from pathlib import Path
import re

ROOT = Path(".").resolve()

SEARCH_DIRS = [
    Path("app.py"),
    Path("templates"),
    Path("static"),
    Path("android_app/app/src/main/python/templates"),
    Path("android_app/app/src/main/python/static"),
]

SKIP_PARTS = {
    "__pycache__",
    ".git",
    "node_modules",
}

SKIP_SUFFIXES = (
    ".bak",
    ".bak2",
    ".png",
    ".jpg",
    ".jpeg",
    ".webp",
    ".sqlite",
    ".db",
)

PATTERNS = {
    "GPS takip": [
        "navigator.geolocation",
        "watchPosition",
        "getCurrentPosition",
        "coords.latitude",
        "coords.longitude",
    ],
    "Mesafe hesabı": [
        "distKm",
        "haversine",
        "distance",
        "kalan mesafe",
        "gps_km",
    ],
    "Durak koordinatı": [
        "route_stop_coords",
        "routeCoords",
        "continue_route_coords",
        "lat",
        "lng",
    ],
    "Canlı durak yazma": [
        "live_stop",
        "liveStop",
        "liveStop:",
        "write=1",
        "/api/live-runtime-state",
        "continue_current_stop",
    ],
    "Otomatik seçim ipucu": [
        "nearest",
        "closest",
        "yakın",
        "yaklas",
        "approach",
        "threshold",
        "5 km",
        "500",
        "passed",
        "geçildi",
        "routeIndex",
    ],
}

IMPORTANT_FILES = []

def is_text_file(p: Path):
    if not p.exists():
        return False
    if p.is_dir():
        return False
    if any(part in SKIP_PARTS for part in p.parts):
        return False
    if any(str(p).endswith(s) for s in SKIP_SUFFIXES):
        return False
    if p.suffix.lower() not in {".py", ".html", ".js", ".css", ".json"}:
        return False
    return True

def iter_files():
    seen = set()

    for item in SEARCH_DIRS:
        if not item.exists():
            continue

        if item.is_file():
            files = [item]
        else:
            files = list(item.rglob("*"))

        for p in files:
            if not is_text_file(p):
                continue
            rp = str(p)
            if rp in seen:
                continue
            seen.add(rp)
            yield p

def read(p):
    return p.read_text(encoding="utf-8", errors="ignore")

def rel(p):
    try:
        return str(p.resolve().relative_to(ROOT))
    except Exception:
        return str(p)

def line_context(lines, idx, radius=2):
    a = max(0, idx - radius)
    b = min(len(lines), idx + radius + 1)
    out = []
    for i in range(a, b):
        mark = ">>" if i == idx else "  "
        out.append(f"{mark} {i+1:5d}: {lines[i]}")
    return "\n".join(out)

files = list(iter_files())

print("===== OTOMATİK CANLI DURAK MOTORU DENETİMİ =====")
print(f"Taranan dosya sayısı: {len(files)}")
print()

# 1) Kategori bazlı izler
for category, pats in PATTERNS.items():
    print(f"\n===== {category} izleri =====")

    found_any = False

    for p in files:
        s = read(p)
        hits = []

        for pat in pats:
            if pat.lower() in s.lower():
                hits.append(pat)

        if hits:
            found_any = True
            print(f"- {rel(p)}")
            print(f"  eşleşen: {', '.join(hits[:12])}")

    if not found_any:
        print("Bulunamadı.")

print("\n\n===== GÜÇLÜ ADAY DOSYALAR =====")
print("Kriter: GPS + live_stop yazma + mesafe/route/threshold izleri birlikte olmalı.")
strong = []

for p in files:
    s = read(p)
    low = s.lower()

    has_gps = ("navigator.geolocation" in low or "watchposition" in low or "getcurrentposition" in low)
    has_write = ("/api/live-runtime-state" in s or "write=1" in s or "live_stop" in s or "liveStop" in s)
    has_route = ("routeCoords" in s or "continue_route_coords" in s or "route_stop_coords" in s or "routeStops" in s)
    has_logic = ("nearest" in low or "closest" in low or "threshold" in low or "distkm" in low or "routeindex" in low or "passed" in low)

    score = sum([has_gps, has_write, has_route, has_logic])

    if score >= 3:
        strong.append((score, p, has_gps, has_write, has_route, has_logic))

if not strong:
    print("Güçlü otomatik canlı durak adayı bulunamadı.")
else:
    for score, p, has_gps, has_write, has_route, has_logic in sorted(strong, reverse=True):
        print(f"- {rel(p)} | skor={score} gps={has_gps} write={has_write} route={has_route} logic={has_logic}")

print("\n\n===== KRİTİK SATIR BAĞLAMLARI =====")
critical_terms = [
    "watchPosition",
    "getCurrentPosition",
    "navigator.geolocation",
    "/api/live-runtime-state",
    "write=1",
    "live_stop",
    "routeCoords",
    "continue_route_coords",
    "routeIndex",
    "distKm",
    "nearest",
    "closest",
    "threshold",
    "passed",
    "geçildi",
]

shown = 0

for p in files:
    s = read(p)
    lines = s.splitlines()

    file_printed = False

    for i, line in enumerate(lines):
        low = line.lower()
        if any(term.lower() in low for term in critical_terms):
            if not file_printed:
                print(f"\n--- {rel(p)} ---")
                file_printed = True

            print(line_context(lines, i, radius=2))
            print()
            shown += 1

            if shown > 160:
                print("Çok fazla sonuç var, ilk 160 bağlam gösterildi.")
                raise SystemExit

print("\n===== SONUÇ =====")
print("Eğer güçlü aday sadece continue_trip_core.js içindeki ETA motoru ise, bu sistem canlı durağı otomatik seçmiyor; mevcut canlı durağa göre ETA/mesafe hesaplıyor demektir.")
