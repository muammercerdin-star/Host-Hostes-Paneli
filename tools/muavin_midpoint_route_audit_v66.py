from pathlib import Path
import re
import sqlite3
import os
import json

ROOT = Path(".").resolve()

FILES = [
    "app.py",
    "android_app/app/src/main/python/app.py",
    "templates/continue_trip.html",
    "android_app/app/src/main/python/templates/continue_trip.html",
    "static/continue/continue_trip_core.js",
    "android_app/app/src/main/python/static/continue/continue_trip_core.js",
    "static/seats/seats.js",
    "android_app/app/src/main/python/static/seats/seats.js",
]

KEYS = [
    "continue_route_coords",
    "routeCoords",
    "findCoord",
    "distKm",
    "nearestRouteStopByGpsV61",
    "switchStaleLiveRuntimeV61",
    "CONTINUE_WAITING_LIVE_ACQUIRE_V64B",
    "LIVE_SWITCH_DISTANCE_FIX_V65",
    "LIVE_DETECT_KM",
    "LIVE_CLEAR_KM",
    "autoDetectLiveStop",
    "live-runtime-state",
    "live_stop",
    "current_stop",
    "first_stop",
    "selected_stops",
]

print("===== MIDPOINT ROUTE AUDIT V66 =====")
print("ROOT:", ROOT)
print()

def read(p):
    f = ROOT / p
    if not f.exists():
        return ""
    return f.read_text(encoding="utf-8", errors="ignore")

print("===== 1) DOSYA İZLERİ =====")
for f in FILES:
    s = read(f)
    if not s:
        print("YOK:", f)
        continue

    print()
    print("-----", f, "-----")
    for i, line in enumerate(s.splitlines(), 1):
        low = line.lower()
        if any(k.lower() in low for k in KEYS):
            print(f"{i:5d}: {line[:260]}")

print()
print("===== 2) CONTINUE CORE ÖNEMLİ BLOK =====")
core = read("static/continue/continue_trip_core.js")
for start, end, title in [
    (1760, 1825, "mesafe / coord fonksiyonları"),
    (1988, 2145, "V61-V65 canlı durak aktarım bloğu"),
    (2145, 2185, "compute devamı"),
]:
    print()
    print("-----", title, f"{start}-{end}", "-----")
    lines = core.splitlines()
    for i in range(start, min(end, len(lines)) + 1):
        print(f"{i:5d}: {lines[i-1][:260]}")

print()
print("===== 3) DB / ROTA KOORDİNAT TABLOSU ARA =====")

db_candidates = []
for p in ROOT.rglob("*.db"):
    if "backup" in str(p).lower():
        continue
    db_candidates.append(p)

if not db_candidates:
    print("DB bulunamadı.")
else:
    for db_path in db_candidates:
        print()
        print("DB:", db_path.relative_to(ROOT))
        try:
            con = sqlite3.connect(str(db_path))
            con.row_factory = sqlite3.Row

            tables = [r[0] for r in con.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name").fetchall()]
            print("TABLOLAR:", ", ".join(tables[:80]))

            for t in tables:
                low = t.lower()
                if any(x in low for x in ["route", "stop", "coord", "trip", "runtime"]):
                    try:
                        cols = [c["name"] for c in con.execute(f"PRAGMA table_info({t})").fetchall()]
                        print()
                        print("TABLO:", t)
                        print("KOLON:", cols)

                        rows = con.execute(f"SELECT * FROM {t} LIMIT 8").fetchall()
                        for r in rows:
                            d = dict(r)
                            print(json.dumps(d, ensure_ascii=False)[:500])
                    except Exception as e:
                        print("OKUMA HATA:", t, e)

            try:
                print()
                print("LIVE_RUNTIME SON KAYIT:")
                for r in con.execute("SELECT * FROM live_runtime_state ORDER BY updated_at DESC LIMIT 5"):
                    print(dict(r))
            except Exception as e:
                print("live_runtime_state okunamadı:", e)

        except Exception as e:
            print("DB HATA:", e)

print()
print("===== 4) KARAR =====")
print("Bu raporda routeCoords içinde durak sırası + lat/lng doğru görünürse V67'de orta nokta mantığı kuracağız.")
print("Yanlış/eksik görünürse önce rota koordinat kaynağını düzelteceğiz.")
