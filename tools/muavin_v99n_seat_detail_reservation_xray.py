from pathlib import Path
from datetime import datetime
import sys, re, json

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from app import app, get_db, get_active_trip, get_active_trip_row

print("===== V99N KOLTUK DETAY / REZERVASYON RÖNTGEN =====")
print("ROOT:", ROOT)
print("TIME:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

def rows_to_dicts(rows):
    out = []
    for r in rows:
        try:
            out.append(dict(r))
        except Exception:
            out.append(r)
    return out

def safe_cols(db, table):
    try:
        return [dict(r) for r in db.execute(f"PRAGMA table_info({table})").fetchall()]
    except Exception:
        return []

def safe_count(db, table):
    try:
        return db.execute(f"SELECT COUNT(*) AS c FROM {table}").fetchone()["c"]
    except Exception:
        return "?"

with app.app_context():
    db = get_db()
    tid = get_active_trip()
    trip = get_active_trip_row()

    print()
    print("===== 1) AKTİF SEFER =====")
    print("ACTIVE_TRIP_ID:", tid)
    if trip:
        print("ROUTE:", trip["route"])
        print("PLATE:", trip["plate"] or "")
        print("DATE:", trip["date"] or "")

    print()
    print("===== 2) KOLTUK / BİLET / REZERVASYON TABLOLARI =====")
    tables = [r["name"] for r in db.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name").fetchall()]

    interesting = []
    for t in tables:
        low = t.lower()
        if any(k in low for k in ["seat", "ticket", "passenger", "reservation", "reserve", "booking", "bag", "consignment"]):
            interesting.append(t)
            print()
            print("TABLO:", t, "rows=", safe_count(db, t))
            cols = safe_cols(db, t)
            print("COLS:", [c["name"] for c in cols])

            try:
                rows = db.execute(f"SELECT * FROM {t} LIMIT 8").fetchall()
                for d in rows_to_dicts(rows):
                    print(" ", d)
            except Exception as e:
                print(" SAMPLE HATA:", repr(e))

    print()
    print("===== 3) AKTİF SEFERE GÖRE KOLTUK VERİSİ =====")
    for t in interesting:
        cols = [c["name"] for c in safe_cols(db, t)]
        if "trip_id" not in cols:
            continue

        try:
            rows = db.execute(f"SELECT * FROM {t} WHERE trip_id=? LIMIT 20", (tid,)).fetchall()
            if rows:
                print()
                print("TABLO:", t)
                for d in rows_to_dicts(rows):
                    print(" ", d)
        except Exception as e:
            pass

    print()
    print("===== 4) FLASK ROUTE / API KONTROL =====")
    for r in sorted(app.url_map.iter_rules(), key=lambda x: str(x.rule)):
        s = str(r.rule)
        if any(k in s.lower() for k in ["seat", "ticket", "passenger", "reservation", "bag", "live"]):
            methods = ",".join(sorted([m for m in r.methods if m not in ["HEAD", "OPTIONS"]]))
            print(f"{s:55} {methods:10} -> {r.endpoint}")

    print()
    print("===== 5) API /api/live-seat-map ÖRNEK =====")
    with app.test_client() as c:
        with c.session_transaction() as sess:
            sess["auth_ok"] = True

        r = c.get("/api/live-seat-map?_v=v99n_xray")
        raw = r.get_data().decode("utf-8", errors="ignore")
        print("STATUS:", r.status_code)
        print("SIZE:", len(raw))

        out = ROOT / "run_logs" / "v99n_live_seat_map.json"
        out.parent.mkdir(exist_ok=True)
        out.write_text(raw, encoding="utf-8")
        print("OUT:", out)

        try:
            data = json.loads(raw)
            seats = data.get("seats") or []
            print("SEAT_COUNT:", len(seats))
            for s in seats[:12]:
                print(" ", s)
        except Exception as e:
            print("JSON HATA:", repr(e))

print()
print("===== 6) KODDA KOLTUK KAYIT / API SATIRLARI =====")
for p in [
    ROOT / "app.py",
    ROOT / "static/seats/seats.js",
    ROOT / "templates/seats.html",
    ROOT / "static/continue/continue_trip_v99_clean.js",
]:
    if not p.exists():
        continue

    print()
    print("DOSYA:", p)
    txt = p.read_text(encoding="utf-8", errors="ignore")
    for i, line in enumerate(txt.splitlines(), 1):
        low = line.lower()
        if any(k in low for k in [
            "api/seat",
            "api/seats",
            "live-seat-map",
            "passenger_name",
            "ticket",
            "reservation",
            "reserve",
            "booking",
            "bag_count",
            "from_stop",
            "to_stop",
            "occupied",
        ]):
            print(f"{i:5}: {line[:220]}")

print()
print("===== RAPOR BİTTİ =====")
