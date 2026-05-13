import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from app import app, get_db
from tools.build_route_segments import ensure_table


with app.app_context():
    db = get_db()
    ensure_table(db)

    rows = db.execute("""
        SELECT route, from_stop, to_stop, via_name, lat, lng, sort_order
        FROM route_segment_vias
        ORDER BY route, from_stop, to_stop, sort_order
    """).fetchall()

    if not rows:
        print("Via noktası yok.")
    else:
        for r in rows:
            print(
                f"{r['route']} | {r['from_stop']} -> {r['to_stop']} | "
                f"{r['sort_order']}. {r['via_name']} ({r['lat']}, {r['lng']})"
            )
