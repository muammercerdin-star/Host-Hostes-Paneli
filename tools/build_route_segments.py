import argparse
import json
import sys
import time
import urllib.request
from datetime import datetime
from pathlib import Path

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

    db.execute("""
        CREATE TABLE IF NOT EXISTS route_segment_vias(
            route TEXT NOT NULL,
            from_stop TEXT NOT NULL,
            to_stop TEXT NOT NULL,
            via_name TEXT NOT NULL,
            lat REAL NOT NULL,
            lng REAL NOT NULL,
            sort_order INTEGER NOT NULL DEFAULT 0,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP,
            PRIMARY KEY(route, from_stop, to_stop, via_name)
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


def load_vias(db, route, from_stop, to_stop):
    ensure_table(db)

    rows = db.execute("""
        SELECT via_name, lat, lng, sort_order
        FROM route_segment_vias
        WHERE route=? AND from_stop=? AND to_stop=?
        ORDER BY sort_order ASC, via_name ASC
    """, (route, from_stop, to_stop)).fetchall()

    vias = []

    for r in rows:
        vias.append({
            "name": r["via_name"],
            "lat": float(r["lat"]),
            "lng": float(r["lng"]),
            "sort_order": int(r["sort_order"] or 0),
        })

    return vias


def osrm_route(points):
    """
    points listesi:
    [
      {"lat":..., "lng":...},  # başlangıç
      {"lat":..., "lng":...},  # via varsa
      {"lat":..., "lng":...},  # bitiş
    ]
    """

    if len(points) < 2:
        raise RuntimeError("OSRM için en az 2 nokta gerekir.")

    coord = ";".join(f"{p['lng']},{p['lat']}" for p in points)
    url = f"{OSRM_BASE}/{coord}?overview=full&geometries=geojson&steps=false"

    with urllib.request.urlopen(url, timeout=40) as resp:
        data = json.loads(resp.read().decode("utf-8"))

    if data.get("code") != "Ok" or not data.get("routes"):
        raise RuntimeError(f"OSRM cevap hatası: {data.get('code')}")

    route = data["routes"][0]
    geometry = route.get("geometry", {}).get("coordinates", [])

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
                vias = load_vias(db, route, from_stop, to_stop)

                points = [a]
                points.extend({"lat": v["lat"], "lng": v["lng"]} for v in vias)
                points.append(b)

                via_text = ""
                if vias:
                    via_text = " | VIA: " + " -> ".join(v["name"] for v in vias)

                print(f"OSRM: {from_stop} -> {to_stop}{via_text}")

                res = osrm_route(points)

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
