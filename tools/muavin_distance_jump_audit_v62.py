from pathlib import Path
import re

ROOT = Path(".").resolve()

FILES = [
    "static/continue/continue_trip_core.js",
    "android_app/app/src/main/python/static/continue/continue_trip_core.js",
    "templates/continue_trip.html",
    "android_app/app/src/main/python/templates/continue_trip.html",
    "app.py",
    "android_app/app/src/main/python/app.py",
]

KEYS = [
    "liveDistanceValue",
    "gps_km",
    "runtimeGpsKm",
    "formatKm",
    "formatGpsKm",
    "parseKmAny",
    "distKm",
    "findCoord",
    "routeCoords",
    "liveCurrentStopName",
    "writeRuntime",
    "preserve_live_stop",
    "nearestRouteStopByGpsV61",
    "switchStaleLiveRuntimeV61",
    "live-runtime-state",
]

print("===== DISTANCE JUMP AUDIT V62 =====")
print("ROOT:", ROOT)
print()

def read(f):
    p = ROOT / f
    if not p.exists():
        return ""
    return p.read_text(encoding="utf-8", errors="ignore")

for f in FILES:
    s = read(f)
    if not s:
        print("YOK:", f)
        continue

    print()
    print("-----", f, "-----")
    lines = s.splitlines()

    for i, line in enumerate(lines, 1):
        low = line.lower()
        if any(k.lower() in low for k in KEYS):
            print(f"{i:5d}: {line[:260]}")

print()
print("===== APP DB LIVE_RUNTIME_STATE SON KAYIT OKUMA KOMUTU =====")
print("Ayrıca terminalde şunu çalıştır:")
print("python - << 'PY2'")
print("import sqlite3")
print("db='muavin.db'")
print("con=sqlite3.connect(db)")
print("con.row_factory=sqlite3.Row")
print("for r in con.execute('select * from live_runtime_state order by updated_at desc limit 5'):")
print("    print(dict(r))")
print("PY2")
