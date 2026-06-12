from pathlib import Path
from datetime import datetime
import sys, re, json

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

print("===== V99D SCHEDULE / DISTANCE REPORT =====")
print("ROOT:", ROOT)
print("TIME:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

from app import app, get_db, get_active_trip, get_active_trip_row

def rows_to_dicts(rows):
    out = []
    for r in rows:
        try:
            out.append(dict(r))
        except Exception:
            out.append(r)
    return out

with app.app_context():
    db = get_db()

    print()
    print("===== 1) AKTIF SEFER =====")
    tid = get_active_trip()
    trip = get_active_trip_row()
    print("ACTIVE_TRIP_ID:", tid)
    if trip:
        try:
            print("ROUTE:", trip["route"])
            print("PLATE:", trip["plate"])
            print("DATE:", trip["date"])
        except Exception:
            print("TRIP_ROW:", dict(trip))
    else:
        print("AKTIF SEFER YOK")

    route = ""
    if trip:
        try:
            route = trip["route"] or ""
        except Exception:
            route = ""

    print()
    print("===== 2) TABLO LISTESI: route / stop / schedule / coord / time =====")
    tables = [r["name"] for r in db.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name").fetchall()]
    interesting = []
    for t in tables:
        low = t.lower()
        if any(k in low for k in ["route", "stop", "schedule", "coord", "time", "trip"]):
            interesting.append(t)
            cols = db.execute(f"PRAGMA table_info({t})").fetchall()
            col_names = [c["name"] for c in cols]
            try:
                cnt = db.execute(f"SELECT COUNT(*) AS c FROM {t}").fetchone()["c"]
            except Exception:
                cnt = "?"
            print(f"- {t}  rows={cnt}  cols={col_names}")

    print()
    print("===== 3) AKTIF ROUTE ILE ESLESEN VERILER =====")
    for t in interesting:
        cols = [c["name"] for c in db.execute(f"PRAGMA table_info({t})").fetchall()]
        low_cols = [c.lower() for c in cols]

        route_cols = [c for c in cols if c.lower() in ["route", "route_name", "name", "trip_route"]]
        stop_cols = [c for c in cols if "stop" in c.lower() or c.lower() in ["name", "station", "durak"]]
        time_cols = [c for c in cols if "time" in c.lower() or "eta" in c.lower() or "hour" in c.lower() or "saat" in c.lower()]
        km_cols = [c for c in cols if "km" in c.lower() or "distance" in c.lower() or "mesafe" in c.lower()]

        if not cols:
            continue

        print()
        print("TABLO:", t)
        print("  route_cols:", route_cols)
        print("  stop_cols :", stop_cols)
        print("  time_cols :", time_cols)
        print("  km_cols   :", km_cols)

        # Route eşleşmesi varsa route'a göre örnek çek
        printed = False
        for rc in route_cols:
            try:
                q = f"SELECT * FROM {t} WHERE {rc}=? LIMIT 12"
                rows = db.execute(q, (route,)).fetchall()
                if rows:
                    print(f"  SAMPLE route match by {rc}:")
                    for d in rows_to_dicts(rows[:12]):
                        print("   ", d)
                    printed = True
                    break
            except Exception as e:
                pass

        if not printed:
            try:
                rows = db.execute(f"SELECT * FROM {t} LIMIT 5").fetchall()
                if rows:
                    print("  SAMPLE first rows:")
                    for d in rows_to_dicts(rows[:5]):
                        print("   ", d)
            except Exception as e:
                print("  SAMPLE HATA:", repr(e))

    print()
    print("===== 4) RENDER CONTINUE_BOOT KONTROL =====")
    out = ROOT / "run_logs" / "v99d_schedule_distance_render.html"
    out.parent.mkdir(parents=True, exist_ok=True)

    with app.test_client() as c:
        with c.session_transaction() as sess:
            sess["auth_ok"] = True

        r = c.get("/continue-trip?v=schedule_distance_report", follow_redirects=False)
        html = r.get_data().decode("utf-8", errors="ignore")
        out.write_text(html, encoding="utf-8")
        print("STATUS:", r.status_code)
        print("HTML_SIZE:", len(html))
        print("OUT:", out)

        boot_match = re.search(r"window\.CONTINUE_BOOT\s*=\s*(\{.*?\});", html, re.S)
        if boot_match:
            raw = boot_match.group(1)
            print("BOOT_RAW_SIZE:", len(raw))

            for key in ["routeStops", "routeCoords", "scheduleItems", "runtimeGpsKm", "runtimeStop", "runtimeEta"]:
                m = re.search(rf"{key}\s*:\s*(.*?)(?:,\n|,\r\n|\n\s*\}})", raw, re.S)
                if m:
                    val = m.group(1).strip()
                    print()
                    print("BOOT", key, "=", val[:900])
                else:
                    print("BOOT", key, "YOK")
        else:
            print("CONTINUE_BOOT bulunamadı")

        print()
        print("===== 5) HTML TIMELINE KARTLARI ILK 25 =====")
        cards = re.findall(
            r'<div class="v99-tl-stop-name[^"]*">\s*([^<]+?)\s*</div>.*?<div class="v99-pill\s+([^"]+)">\s*([^<]+?)\s*</div>.*?<div class="v99-tl-metrics">(.*?)</div>\s*</div>',
            html,
            re.S
        )

        print("CARD_COUNT:", len(cards))
        for idx, (name, cls, pill, metrics_html) in enumerate(cards[:25], 1):
            vals = re.findall(r'<div class="v99-tl-m-val[^"]*"(?:\s+data-stop-name="[^"]*")?>\s*([^<]+?)\s*</div>\s*<div class="v99-tl-m-lbl">\s*([^<]+?)\s*</div>', metrics_html, re.S)
            clean_vals = [(a.strip(), b.strip()) for a,b in vals]
            print(f"{idx:02d}. {name.strip():28} | {cls.strip():9} | {pill.strip():12} | {clean_vals}")

    print()
    print("===== 6) APP.PY CONTINUE_TRIP BLOK =====")
    lines = (ROOT / "app.py").read_text(encoding="utf-8", errors="ignore").splitlines()
    for i in range(1720, min(1865, len(lines))):
        line = lines[i-1]
        if any(k in line for k in [
            "make_stop_payload", "eta", "distance", "status", "schedule", "coord",
            "selected_stops", "live_stops", "current_index", "passed", "upcoming", "next"
        ]):
            print(f"{i:5}: {line[:220]}")

print()
print("===== RAPOR BITTI =====")
