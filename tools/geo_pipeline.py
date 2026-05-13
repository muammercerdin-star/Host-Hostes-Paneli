import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from app import app, get_db, get_stops, get_active_trip
from tools.build_route_segments import build_segments, norm_stop, ensure_table


def get_active_route():
    with app.app_context():
        db = get_db()
        tid = get_active_trip()
        if not tid:
            return ""

        row = db.execute("SELECT route FROM trips WHERE id=?", (tid,)).fetchone()
        return (row["route"] or "").strip() if row else ""


def get_all_routes():
    routes = set()

    with app.app_context():
        db = get_db()

        for sql, col in [
            ("SELECT name FROM routes", "name"),
            ("SELECT DISTINCT route FROM route_stop_coords", "route"),
            ("SELECT DISTINCT route FROM trips", "route"),
        ]:
            try:
                rows = db.execute(sql).fetchall()
                for r in rows:
                    name = (r[col] or "").strip()
                    if name:
                        routes.add(name)
            except Exception:
                pass

    return sorted(routes)


def load_coord_keys(db, route):
    keys = set()

    # Önce route birebir
    try:
        rows = db.execute(
            "SELECT stop FROM route_stop_coords WHERE route=?",
            (route,),
        ).fetchall()

        for r in rows:
            keys.add(norm_stop(r["stop"]))
    except Exception:
        pass

    # Fallback: durak adına göre başka route kayıtlarında varsa da sayalım
    try:
        rows = db.execute("SELECT stop FROM route_stop_coords").fetchall()
        for r in rows:
            keys.add(norm_stop(r["stop"]))
    except Exception:
        pass

    return keys


def segment_count(db, route):
    try:
        ensure_table(db)
        row = db.execute(
            "SELECT COUNT(*) AS c FROM route_segments WHERE route=?",
            (route,),
        ).fetchone()
        return int(row["c"] or 0)
    except Exception:
        return 0


def route_report(route):
    with app.app_context():
        db = get_db()
        stops = get_stops(route)
        coord_keys = load_coord_keys(db, route)

        missing = []
        for stop in stops:
            if norm_stop(stop) not in coord_keys:
                missing.append(stop)

        expected_segments = max(len(stops) - 1, 0)
        existing_segments = segment_count(db, route)

        return {
            "route": route,
            "stop_count": len(stops),
            "expected_segments": expected_segments,
            "existing_segments": existing_segments,
            "missing_count": len(missing),
            "missing": missing,
            "ready": len(stops) >= 2 and not missing,
        }


def print_report(routes):
    print("=== Harita / Gerçek Yol Geometrisi Raporu ===")
    print("Hat sayısı:", len(routes))
    print()

    ready_count = 0

    for route in routes:
        r = route_report(route)

        if r["ready"]:
            ready_count += 1
            state = "HAZIR"
        else:
            state = "EKSİK"

        print(f"[{state}] {route}")
        print(f"  Durak: {r['stop_count']}")
        print(f"  Segment: {r['existing_segments']} / {r['expected_segments']}")
        print(f"  Eksik koordinat: {r['missing_count']}")

        if r["missing"]:
            for m in r["missing"][:12]:
                print(f"    - {m}")
            if len(r["missing"]) > 12:
                print(f"    ... +{len(r['missing']) - 12} eksik daha")

        print()

    print("Hazır hat:", ready_count)
    print("Eksik hat:", len(routes) - ready_count)


def export_segments_json():
    out = ROOT / "static" / "data" / "route_segments.json"
    out.parent.mkdir(parents=True, exist_ok=True)

    with app.app_context():
        db = get_db()
        ensure_table(db)

        rows = db.execute("""
            SELECT route, from_stop, to_stop, sort_order,
                   distance_m, duration_s, geometry_json, provider, updated_at
            FROM route_segments
            ORDER BY route, sort_order
        """).fetchall()

        data = []

        for r in rows:
            try:
                geom = json.loads(r["geometry_json"] or "[]")
            except Exception:
                geom = []

            data.append({
                "route": r["route"],
                "from_stop": r["from_stop"],
                "to_stop": r["to_stop"],
                "sort_order": int(r["sort_order"] or 0),
                "distance_m": float(r["distance_m"] or 0),
                "duration_s": float(r["duration_s"] or 0),
                "geometry": geom,
                "provider": r["provider"] or "osrm",
                "updated_at": r["updated_at"] or "",
            })

    out.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")

    print("JSON yazıldı:", out)
    print("Toplam segment:", len(data))


def main():
    ap = argparse.ArgumentParser()

    ap.add_argument("--report", action="store_true", help="Hat koordinat/segment raporu üret")
    ap.add_argument("--active", action="store_true", help="Sadece aktif seferin hattını işle")
    ap.add_argument("--build-ready", action="store_true", help="Koordinatı tam olan hatları üret")
    ap.add_argument("--force", action="store_true", help="Var olan segmentleri yeniden üret")
    ap.add_argument("--export", action="store_true", help="route_segments.json üret")

    args = ap.parse_args()

    if args.active:
        route = get_active_route()
        routes = [route] if route else []
    else:
        routes = get_all_routes()

    if args.report or not (args.build_ready or args.export):
        print_report(routes)

    if args.build_ready:
        for route in routes:
            r = route_report(route)

            if not r["ready"]:
                print(f"SKIP eksik koordinat: {route}")
                continue

            print()
            print("=" * 70)
            print("ÜRET:", route)
            print("=" * 70)
            build_segments(route, force=args.force)

    if args.export:
        print()
        export_segments_json()


if __name__ == "__main__":
    main()
