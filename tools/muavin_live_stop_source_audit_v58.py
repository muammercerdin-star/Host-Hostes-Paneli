from pathlib import Path
import re

ROOT = Path(".").resolve()

FILES = [
    "app.py",
    "android_app/app/src/main/python/app.py",

    "templates/continue_trip.html",
    "android_app/app/src/main/python/templates/continue_trip.html",

    "templates/seats.html",
    "android_app/app/src/main/python/templates/seats.html",

    "static/continue/continue_trip_core.js",
    "android_app/app/src/main/python/static/continue/continue_trip_core.js",

    "static/continue/continue_flow_refresh.js",
    "android_app/app/src/main/python/static/continue/continue_flow_refresh.js",

    "static/seats/seats.js",
    "android_app/app/src/main/python/static/seats/seats.js",
]

KEYS = [
    "runtimeStop",
    "runtime_stop",
    "liveStop",
    "live_stop",
    "liveCurrentStop",
    "liveCurrentStopName",
    "currentStop",
    "selectedStop",
    "selected_stop",
    "getSelectedStopName",
    "setSelectedStop",
    "nextStop",
    "nearest",
    "distance",
    "coords",
    "routeStops",
    "route_coords",
    "watchPosition",
    "geolocation",
    "live-runtime-state",
    "runtime-state",
    "stop-distance",
    "lastStop",
    "passed",
    "Manisa",
    "Denizli",
    "Özdilek",
]

def read(path):
    p = ROOT / path
    if not p.exists():
        return ""
    return p.read_text(encoding="utf-8", errors="ignore")

def print_hits(path, limit=220):
    p = ROOT / path
    if not p.exists():
        print("\n-----", path, "YOK -----")
        return

    s = read(path)
    lines = s.splitlines()
    hits = []

    for i, line in enumerate(lines, 1):
        low = line.lower()
        if any(k.lower() in low for k in KEYS):
            hits.append((i, line[:280]))

    print("\n-----", path, "-----")
    print("Satır:", len(lines), "Hit:", len(hits))

    for i, line in hits[:limit]:
        print(f"{i:5d}: {line}")

    if len(hits) > limit:
        print("... devamı:", len(hits) - limit)

print("===== CANLI DURAK KAYNAK AUDIT V58 =====")
print("ROOT:", ROOT)
print()

print("===== 1) GENEL ARAMA =====")
for f in FILES:
    print_hits(f)

print()
print("===== 2) APP.PY API BLOKLARI =====")
for f in ["app.py", "android_app/app/src/main/python/app.py"]:
    s = read(f)
    if not s:
        continue

    lines = s.splitlines()
    print("\n-----", f, "-----")

    for i, line in enumerate(lines, 1):
        low = line.lower()
        if (
            "live-runtime-state" in low
            or "runtime_state" in low
            or "live_stop" in low
            or "runtime_stop" in low
            or "stop-distance" in low
            or "route_coords" in low
        ):
            start = max(1, i - 20)
            end = min(len(lines), i + 45)
            print(f"\n### BLOK {start}-{end}")
            for j in range(start, end + 1):
                print(f"{j:5d}: {lines[j-1][:300]}")

print()
print("===== 3) CONTINUE CORE CANLI DURAK BLOKLARI =====")
for f in [
    "static/continue/continue_trip_core.js",
    "android_app/app/src/main/python/static/continue/continue_trip_core.js",
]:
    s = read(f)
    if not s:
        continue

    lines = s.splitlines()
    print("\n-----", f, "-----")

    for i, line in enumerate(lines, 1):
        low = line.lower()
        if (
            "livecurrentstopname" in low
            or "runtimestop" in low
            or "live-runtime-state" in low
            or "watchposition" in low
            or "routecoords" in low
            or "stop-distance" in low
            or "compute" in low and "distance" in low
        ):
            start = max(1, i - 18)
            end = min(len(lines), i + 42)
            print(f"\n### BLOK {start}-{end}")
            for j in range(start, end + 1):
                print(f"{j:5d}: {lines[j-1][:300]}")

print()
print("===== 4) SEATS.JS SEÇİLİ DURAK / CANLI DURAK BLOKLARI =====")
for f in [
    "static/seats/seats.js",
    "android_app/app/src/main/python/static/seats/seats.js",
]:
    s = read(f)
    if not s:
        continue

    lines = s.splitlines()
    print("\n-----", f, "-----")

    for i, line in enumerate(lines, 1):
        low = line.lower()
        if (
            "getselectedstopname" in low
            or "setselectedstop" in low
            or "selectedstop" in low
            or "livestop" in low
            or "watchposition" in low
            or "renderroute" in low
            or "routestops" in low
            or "coords" in low
        ):
            start = max(1, i - 16)
            end = min(len(lines), i + 34)
            print(f"\n### BLOK {start}-{end}")
            for j in range(start, end + 1):
                print(f"{j:5d}: {lines[j-1][:300]}")

print()
print("===== 5) KISA NOT =====")
print("Burada ayıracağımız şey:")
print("1. Canlı durak API'den mi geliyor?")
print("2. GPS koordinatından mı hesaplanıyor?")
print("3. Seçili durak localStorage/manuel seçim mi?")
print("4. Denizli eski runtimeStop olarak mı kalmış?")
