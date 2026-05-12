import argparse
import json
import sys
import time
import urllib.parse
import urllib.request
from datetime import datetime
from pathlib import Path

# Proje kökünü Python import yoluna ekle.
# Böylece tools/ içinden çalışırken app.py bulunur.
ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from app import app, get_db, get_active_trip, get_stops


OSRM_BASE = "https://router.project-osrm.org/route/v1/driving"


def norm_stop(v):
    s = (v or "").strip().lower()
    for ch in ["–", "-", "_", "/", "\\", ".", ",", "(", ")", "[", "]"]:
        s = s.replace(ch, " ")
    return " ".join(s.split())


def ensure_table(db):
    db.execute("""
        CREATE TABLE IF NOT EXISTS route_segments(
            route TEXT NOT NULL,
            from_stop TEXT NOT NULL,
            to_stop TEXT NOT NULL,
            sort_order INTEGER NOT NULL,
            distance_m REAL DEFAULT 0,
            duration_s REAL DEFAULT 0,
            geometry_json TEXT NOT NULL,
            provider TEXT DEFAULT 'osrm',
            updated_at TEXT DEFAULT CURRENT_TIMESTAMP,
            PRIMARY KEY(route, from_stop, to_stop)
        )
    """)
    db.commit()


def get_active_route(db):
    tid = get_active_trip()
    if not tid:
        raise SystemExit("Aktif sefer yok. --route ile rota adı ver veya aktif sefer başlat.")

    trip = db.execute("SELECT * FROM trips WHERE id=?", (tid,)).fetchone()
    if not trip:
        raise SystemExit("Aktif sefer kaydı bulunamadı.")

    return trip["route"]


def load_coords(db, route, stops):
    coords = {}

    # Önce rota adı birebir eşleşsin
    rows = db.execute("""
        SELECT route, stop, lat, lng
        FROM route_stop_coords
        WHERE route=?
    """, (route,)).fetchall()

    for r in rows:
        coords[norm_stop(r["stop"])] = {
            "lat": float(r["lat"]),
            "lng": float(r["lng"]),
        }

    # Eksik durak varsa durak adına göre fallback
    wanted = {norm_stop(x) for x in stops}
    missing = wanted - set(coords.keys())

    if missing:
        rows = db.execute("""
            SELECT route, stop, lat, lng
            FROM route_stop_coords
        """).fetchall()

        for r in rows:
            k = norm_stop(r["stop"])
            if k in missing and k not in coords:
                coords[k] = {
                    "lat": float(r["lat"]),
                    "lng": float(r["lng"]),
                }

    return coords


def osrm_route(a, b):
    # OSRM koordinat sırası: lng,lat
    coord = f"{a['lng']},{a['lat']};{b['lng']},{b['lat']}"
    url = f"{OSRM_BASE}/{coord}?overview=full&geometries=geojson&steps=false"

    with urllib.request.urlopen(url, timeout=30) as resp:
        data = json.loads(resp.read().decode("utf-8"))

    if data.get("code") != "Ok" or not data.get("routes"):
        raise RuntimeError(f"OSRM cevap hatası: {data.get('code')}")

    route = data["routes"][0]
    geometry = route.get("geometry", {}).get("coordinates", [])

    # Leaflet için lat,lng sırasına çeviriyoruz
    lat_lng = [[lat, lng] for lng, lat in geometry]

    return {
        "distance_m": float(route.get("distance") or 0),
        "duration_s": float(route.get("duration") or 0),
        "geometry": lat_lng,
    }


def build_segments(route, force=False, sleep_s=0.35):
    with app.app_context():
        db = get_db()
        ensure_table(db)

        stops = get_stops(route)
        if len(stops) < 2:
            raise SystemExit(f"Rota durakları bulunamadı veya yetersiz: {route}")

        coords = load_coords(db, route, stops)

        print(f"Rota: {route}")
        print(f"Durak sayısı: {len(stops)}")

        ok = 0
        skipped = 0
        failed = 0

        for i in range(len(stops) - 1):
            from_stop = stops[i]
            to_stop = stops[i + 1]

            a = coords.get(norm_stop(from_stop))
            b = coords.get(norm_stop(to_stop))

            if not a or not b:
                print(f"SKIP koordinat eksik: {from_stop} -> {to_stop}")
                skipped += 1
                continue

            exists = db.execute("""
                SELECT route
                FROM route_segments
                WHERE route=? AND from_stop=? AND to_stop=?
            """, (route, from_stop, to_stop)).fetchone()

            if exists and not force:
                print(f"VAR: {from_stop} -> {to_stop}")
                ok += 1
                continue

            try:
                print(f"OSRM: {from_stop} -> {to_stop}")
                res = osrm_route(a, b)

                db.execute("""
                    INSERT INTO route_segments(
                        route, from_stop, to_stop, sort_order,
                        distance_m, duration_s, geometry_json,
                        provider, updated_at
                    )
                    VALUES(?,?,?,?,?,?,?,?,?)
                    ON CONFLICT(route, from_stop, to_stop)
                    DO UPDATE SET
                        sort_order=excluded.sort_order,
                        distance_m=excluded.distance_m,
                        duration_s=excluded.duration_s,
                        geometry_json=excluded.geometry_json,
                        provider=excluded.provider,
                        updated_at=excluded.updated_at
                """, (
                    route,
                    from_stop,
                    to_stop,
                    i,
                    res["distance_m"],
                    res["duration_s"],
                    json.dumps(res["geometry"], ensure_ascii=False),
                    "osrm",
                    datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                ))

                db.commit()
                ok += 1
                time.sleep(sleep_s)

            except Exception as e:
                print(f"HATA: {from_stop} -> {to_stop}: {e}")
                failed += 1

        print()
        print("Özet:")
        print("Kaydedilen/var:", ok)
        print("Atlanan:", skipped)
        print("Hatalı:", failed)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--route", help="Rota adı")
    ap.add_argument("--active", action="store_true", help="Aktif seferin rotasını kullan")
    ap.add_argument("--force", action="store_true", help="Var olan segmentleri yeniden üret")
    args = ap.parse_args()

    with app.app_context():
        db = get_db()
        route = args.route or (get_active_route(db) if args.active else "")

    if not route:
        raise SystemExit("--route 'Rota Adı' veya --active kullan.")

    build_segments(route, force=args.force)


if __name__ == "__main__":
    main()
