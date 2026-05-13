import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from app import app, get_db, get_active_trip
from tools.build_route_segments import ensure_table, norm_stop


def active_route():
    db = get_db()
    tid = get_active_trip()
    if not tid:
        return ""

    row = db.execute("SELECT route FROM trips WHERE id=?", (tid,)).fetchone()
    return (row["route"] or "").strip() if row else ""


def find_coord(db, route, stop_name):
    # Önce aktif rota içinde ara
    row = db.execute("""
        SELECT stop, lat, lng
        FROM route_stop_coords
        WHERE route=? AND lower(stop)=lower(?)
    """, (route, stop_name)).fetchone()

    if row:
        return row

    # Normalize eşleşme
    rows = db.execute("""
        SELECT route, stop, lat, lng
        FROM route_stop_coords
    """).fetchall()

    target = norm_stop(stop_name)

    for r in rows:
        if norm_stop(r["stop"]) == target:
            return r

    # Kısmi arama
    for r in rows:
        if target and (target in norm_stop(r["stop"]) or norm_stop(r["stop"]) in target):
            return r

    return None


def main():
    ap = argparse.ArgumentParser()

    ap.add_argument("--route", help="Rota adı")
    ap.add_argument("--active", action="store_true", help="Aktif sefer rotasını kullan")
    ap.add_argument("--from", dest="from_stop", required=True, help="Segment başlangıç durağı")
    ap.add_argument("--to", dest="to_stop", required=True, help="Segment bitiş durağı")

    ap.add_argument("--name", help="Via adı")
    ap.add_argument("--lat", type=float, help="Via lat")
    ap.add_argument("--lng", type=float, help="Via lng")
    ap.add_argument("--copy-stop", help="Koordinatı route_stop_coords içinden kopyalanacak durak adı")
    ap.add_argument("--order", type=int, default=1, help="Sıra")

    args = ap.parse_args()

    with app.app_context():
        db = get_db()
        ensure_table(db)

        route = args.route or (active_route() if args.active else "")

        if not route:
            raise SystemExit("--route veya --active gerekli.")

        via_name = (args.name or args.copy_stop or "").strip()
        lat = args.lat
        lng = args.lng

        if args.copy_stop:
            row = find_coord(db, route, args.copy_stop)
            if not row:
                raise SystemExit(f"Koordinat bulunamadı: {args.copy_stop}")

            lat = float(row["lat"])
            lng = float(row["lng"])
            via_name = via_name or row["stop"]

        if not via_name:
            raise SystemExit("--name veya --copy-stop gerekli.")

        if lat is None or lng is None:
            raise SystemExit("--lat ve --lng gerekli veya --copy-stop kullan.")

        db.execute("""
            INSERT INTO route_segment_vias(
                route, from_stop, to_stop, via_name, lat, lng, sort_order
            )
            VALUES(?,?,?,?,?,?,?)
            ON CONFLICT(route, from_stop, to_stop, via_name)
            DO UPDATE SET
                lat=excluded.lat,
                lng=excluded.lng,
                sort_order=excluded.sort_order
        """, (
            route,
            args.from_stop,
            args.to_stop,
            via_name,
            lat,
            lng,
            args.order,
        ))

        db.commit()

        print("Via kaydedildi:")
        print("Rota:", route)
        print("Segment:", args.from_stop, "->", args.to_stop)
        print("Via:", via_name)
        print("Koordinat:", lat, lng)
        print("Sıra:", args.order)


if __name__ == "__main__":
    main()
