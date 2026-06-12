from pathlib import Path
from datetime import datetime
import sys, re, json, math

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from app import app, get_db, get_active_trip, get_active_trip_row

print("===== V99H KM SOURCE XRAY =====")
print("ROOT:", ROOT)
print("TIME:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

def norm(s):
    return (
        str(s or "")
        .replace("–", "-")
        .replace("—", "-")
        .replace("İ", "i")
        .replace("I", "i")
        .lower()
        .replace("ı", "i")
        .replace("ğ", "g")
        .replace("ü", "u")
        .replace("ş", "s")
        .replace("ö", "o")
        .replace("ç", "c")
        .replace(" ", "")
        .strip()
    )

def soft_eq(a, b):
    na, nb = norm(a), norm(b)
    if not na or not nb:
        return False
    return na == nb or na in nb or nb in na

def km_fmt(v):
    if v is None:
        return "-"
    try:
        v = float(v)
    except Exception:
        return "-"
    if abs(v) < 0.05:
        return "0"
    if v >= 10:
        return str(round(v))
    return f"{v:.1f}"

def parse_json_array_from_boot(html, key):
    # Örnek: routeStops: [...],
    m = re.search(rf"{re.escape(key)}\s*:\s*(\[.*?\])\s*,\s*\n", html, re.S)
    if not m:
        return []
    raw = m.group(1)
    try:
        return json.loads(raw)
    except Exception as e:
        print(f"BOOT_PARSE_HATA {key}:", repr(e))
        return []

def get_cols(db, table):
    try:
        return [r["name"] for r in db.execute(f"PRAGMA table_info({table})").fetchall()]
    except Exception:
        return []

def table_count(db, table):
    try:
        return db.execute(f"SELECT COUNT(*) AS c FROM {table}").fetchone()["c"]
    except Exception:
        return "?"

def distinct_routes(db, table):
    try:
        return [r["route"] for r in db.execute(f"SELECT DISTINCT route FROM {table} ORDER BY route").fetchall()]
    except Exception:
        return []

def match_route_name(db, table, active_route):
    routes = distinct_routes(db, table)
    wanted = norm(active_route)

    exact = [r for r in routes if norm(r) == wanted]
    if exact:
        return exact[0]

    soft = [r for r in routes if wanted in norm(r) or norm(r) in wanted]
    if soft:
        return soft[0]

    return ""

def get_segments(db, table, active_route):
    matched = match_route_name(db, table, active_route)
    if not matched:
        return "", []

    try:
        rows = db.execute(
            f"""
            SELECT route, from_stop, to_stop, sort_order, distance_m, duration_s, provider
            FROM {table}
            WHERE route=?
            ORDER BY sort_order ASC
            """,
            (matched,)
        ).fetchall()
    except Exception as e:
        print(f"SEGMENT_QUERY_HATA {table}:", repr(e))
        return matched, []

    out = []
    for r in rows:
        try:
            m = float(r["distance_m"] or 0)
        except Exception:
            m = 0
        out.append({
            "route": r["route"],
            "from": r["from_stop"],
            "to": r["to_stop"],
            "order": r["sort_order"],
            "m": m,
            "km": m / 1000 if m else None,
            "provider": r["provider"],
        })
    return matched, out

def find_segment_between(segments, a, b):
    # direkt / yumuşak eşleşme
    for s in segments:
        if soft_eq(s["from"], a) and soft_eq(s["to"], b):
            return s

    # ters yön ihtimali
    for s in segments:
        if soft_eq(s["from"], b) and soft_eq(s["to"], a):
            ss = dict(s)
            ss["reverse_match"] = True
            return ss

    return None

def schedule_map(items):
    mp = {}
    for it in items:
        if not isinstance(it, dict):
            continue
        name = it.get("stop_name") or it.get("stop") or it.get("name") or ""
        if not name:
            continue
        mp[norm(name)] = it
    return mp

def find_schedule_item(mp, stop):
    k = norm(stop)
    if k in mp:
        return mp[k]
    for kk, item in mp.items():
        if k and (k in kk or kk in k):
            return item
    return None

def num(x):
    if x is None:
        return None
    m = re.search(r"-?\d+(?:[.,]\d+)?", str(x))
    if not m:
        return None
    try:
        return float(m.group(0).replace(",", "."))
    except Exception:
        return None

with app.app_context():
    db = get_db()

    print()
    print("===== 1) AKTIF SEFER / CANLI DURUM =====")
    tid = get_active_trip()
    trip = get_active_trip_row()
    print("ACTIVE_TRIP_ID:", tid)

    route = ""
    if trip:
        route = trip["route"] or ""
        print("ROUTE:", route)
        print("PLATE:", trip["plate"] or "")
        print("DATE:", trip["date"] or "")
    else:
        print("AKTIF SEFER YOK")

    rt = db.execute(
        "SELECT * FROM live_runtime_state WHERE trip_id=?",
        (tid or 0,)
    ).fetchone()

    live_stop = ""
    runtime_km = None

    if rt:
        live_stop = rt["live_stop"] or ""
        runtime_km = num(rt["gps_km"])
        print("LIVE_STOP:", live_stop)
        print("RUNTIME_GPS_KM:", rt["gps_km"])
        print("ETA_MAIN:", rt["eta_main"])
        print("ETA_SUB:", rt["eta_sub"])
    else:
        print("LIVE_RUNTIME_STATE: YOK")

    print()
    print("===== 2) TABLO ÖZETİ =====")
    for t in [
        "route_schedule_profiles",
        "route_schedule_items",
        "route_segments",
        "route_profile_segments",
        "route_stop_coords",
        "stop_logs",
    ]:
        print(f"{t:24} rows={table_count(db,t)} cols={get_cols(db,t)}")

    print()
    print("===== 3) RENDER CONTINUE_BOOT =====")
    with app.test_client() as c:
        with c.session_transaction() as sess:
            sess["auth_ok"] = True

        r = c.get("/continue-trip?v=v99h_xray", follow_redirects=False)
        html = r.get_data().decode("utf-8", errors="ignore")

    out_html = ROOT / "run_logs" / "v99h_km_xray_render.html"
    out_html.parent.mkdir(parents=True, exist_ok=True)
    out_html.write_text(html, encoding="utf-8")

    route_stops = parse_json_array_from_boot(html, "routeStops")
    schedule_items_boot = parse_json_array_from_boot(html, "scheduleItems")
    route_coords = parse_json_array_from_boot(html, "routeCoords")

    print("HTML_SIZE:", len(html))
    print("OUT_HTML:", out_html)
    print("BOOT routeStops:", len(route_stops))
    print("BOOT scheduleItems:", len(schedule_items_boot))
    print("BOOT routeCoords:", len(route_coords))

    print()
    print("İLK 12 routeStops:")
    for i, s in enumerate(route_stops[:12], 1):
        print(f"{i:02d}. {s}")

    print()
    print("===== 4) SCHEDULE PROFIL / ITEM =====")
    profs = db.execute(
        """
        SELECT id, route_name, title, direction, is_default
        FROM route_schedule_profiles
        WHERE route_name=?
        ORDER BY is_default DESC, id ASC
        """,
        (route,)
    ).fetchall()

    if not profs:
        print("SCHEDULE_PROFILE exact yok:", route)
    else:
        for p in profs:
            print("PROFILE:", dict(p))

    profile_id = profs[0]["id"] if profs else None

    schedule_items_db = []
    if profile_id:
        rows = db.execute(
            """
            SELECT stop_name, planned_time, segment_km, is_timed, sort_order
            FROM route_schedule_items
            WHERE profile_id=?
            ORDER BY sort_order ASC
            """,
            (profile_id,)
        ).fetchall()
        schedule_items_db = [dict(r) for r in rows]

    print("DB schedule_items:", len(schedule_items_db))
    print("İLK 18 schedule item:")
    for it in schedule_items_db[:18]:
        print(
            f"{str(it.get('sort_order')):>3} | "
            f"{it.get('stop_name'):<28} | "
            f"time={it.get('planned_time') or '-':<6} | "
            f"segment_km={it.get('segment_km')}"
        )

    schedule_items = schedule_items_boot if schedule_items_boot else schedule_items_db
    smap = schedule_map(schedule_items)

    print()
    print("===== 5) ROUTE SEGMENT KAYNAKLARI =====")

    seg_route_name, segs = get_segments(db, "route_segments", route)
    prof_route_name, prof_segs = get_segments(db, "route_profile_segments", route)

    print("route_segments matched route:", seg_route_name or "YOK", "count:", len(segs))
    print("route_profile_segments matched route:", prof_route_name or "YOK", "count:", len(prof_segs))

    print()
    print("İLK 18 route_segments:")
    for s in segs[:18]:
        print(
            f"{str(s['order']):>3} | "
            f"{s['from']:<26} -> {s['to']:<26} | "
            f"{km_fmt(s['km'])} km"
        )

    print()
    print("İLK 18 route_profile_segments:")
    for s in prof_segs[:18]:
        print(
            f"{str(s['order']):>3} | "
            f"{s['from']:<26} -> {s['to']:<26} | "
            f"{km_fmt(s['km'])} km"
        )

    # Öncelik route_segments, yoksa profile
    seg_source = "route_segments" if segs else "route_profile_segments"
    active_segments = segs if segs else prof_segs

    print()
    print("AKTIF KM KAYNAĞI:", seg_source, "segment_count:", len(active_segments))

    print()
    print("===== 6) DURAK BAZLI KM HESAP RÖNTGENİ =====")

    stops = route_stops[:]
    if not stops:
        # render vermezse schedule sırasına düş
        stops = [it.get("stop_name") for it in schedule_items if isinstance(it, dict) and it.get("stop_name")]

    live_idx = -1
    for i, st in enumerate(stops):
        if soft_eq(st, live_stop):
            live_idx = i
            break

    print("STOP_COUNT:", len(stops))
    print("LIVE_STOP:", live_stop)
    print("LIVE_INDEX:", live_idx)
    print("RUNTIME_KM:", km_fmt(runtime_km))

    cumulative = []
    total = 0.0
    missing = []

    for i, st in enumerate(stops):
        item = find_schedule_item(smap, st)
        planned = item.get("planned_time") if item else ""
        sched_seg = num(item.get("segment_km")) if item else None

        if i == 0:
            cumulative.append({
                "stop": st,
                "planned": planned or "",
                "seg_source": "start",
                "seg_km": 0.0,
                "cum_km": 0.0,
                "missing": False,
            })
            continue

        prev = stops[i-1]
        seg = find_segment_between(active_segments, prev, st)

        seg_km = None
        seg_src = ""

        if seg and seg.get("km"):
            seg_km = float(seg["km"])
            seg_src = seg_source
        elif sched_seg is not None and sched_seg > 0:
            seg_km = float(sched_seg)
            seg_src = "schedule.segment_km"
        else:
            seg_km = None
            seg_src = "MISSING"
            missing.append((prev, st))

        if seg_km is not None:
            total += seg_km

        cumulative.append({
            "stop": st,
            "planned": planned or "",
            "seg_source": seg_src,
            "seg_km": seg_km,
            "cum_km": total if seg_km is not None else None,
            "missing": seg_km is None,
        })

    live_cum = None
    if 0 <= live_idx < len(cumulative):
        live_cum = cumulative[live_idx]["cum_km"]

    def current_relative_km(i):
        if live_idx < 0:
            return None
        if i < live_idx:
            return None
        if i == live_idx:
            return runtime_km
        if live_cum is None or cumulative[i]["cum_km"] is None:
            return None
        return (runtime_km or 0) + (cumulative[i]["cum_km"] - live_cum)

    print()
    print("İLK 18 DURAK HESABI:")
    print("NO | DURAK                         | SAAT  | SEG_KM | SEG_SRC              | TOPLAM_KM | CANLIYE_GORE")
    for i, row in enumerate(cumulative[:18]):
        rel = current_relative_km(i)
        print(
            f"{i+1:02d} | "
            f"{row['stop'][:29]:<29} | "
            f"{(row['planned'] or '-'):<5} | "
            f"{km_fmt(row['seg_km']):>6} | "
            f"{row['seg_source'][:20]:<20} | "
            f"{km_fmt(row['cum_km']):>8} | "
            f"{km_fmt(rel):>10}"
        )

    print()
    print("CANLI ÇEVRESİ DURAK HESABI:")
    start = max(0, live_idx - 8)
    end = min(len(cumulative), live_idx + 10)
    print("NO | DURAK                         | SAAT  | SEG_KM | SEG_SRC              | TOPLAM_KM | CANLIYE_GORE")
    for i in range(start, end):
        row = cumulative[i]
        rel = current_relative_km(i)
        marker = " <-- CANLI" if i == live_idx else ""
        print(
            f"{i+1:02d} | "
            f"{row['stop'][:29]:<29} | "
            f"{(row['planned'] or '-'):<5} | "
            f"{km_fmt(row['seg_km']):>6} | "
            f"{row['seg_source'][:20]:<20} | "
            f"{km_fmt(row['cum_km']):>8} | "
            f"{km_fmt(rel):>10}{marker}"
        )

    print()
    print("SON 8 DURAK HESABI:")
    print("NO | DURAK                         | SAAT  | SEG_KM | SEG_SRC              | TOPLAM_KM | CANLIYE_GORE")
    for i in range(max(0, len(cumulative)-8), len(cumulative)):
        row = cumulative[i]
        rel = current_relative_km(i)
        print(
            f"{i+1:02d} | "
            f"{row['stop'][:29]:<29} | "
            f"{(row['planned'] or '-'):<5} | "
            f"{km_fmt(row['seg_km']):>6} | "
            f"{row['seg_source'][:20]:<20} | "
            f"{km_fmt(row['cum_km']):>8} | "
            f"{km_fmt(rel):>10}"
        )

    print()
    print("===== 7) EKSİK SEGMENTLER =====")
    print("MISSING_COUNT:", len(missing))
    for idx, (a, b) in enumerate(missing[:40], 1):
        print(f"{idx:02d}. {a} -> {b}")

    print()
    print("===== 8) MEVCUT HTML KART DEĞERLERİ =====")
    cards = re.findall(
        r'<div class="v99-tl-stop-name[^"]*">\s*([^<]+?)\s*</div>.*?<div class="v99-pill\s+([^"]+)">\s*([^<]+?)\s*</div>.*?<div class="v99-tl-metrics">(.*?)</div>\s*</div>',
        html,
        re.S
    )

    print("HTML_CARD_COUNT:", len(cards))
    for idx, (name, cls, pill, metrics_html) in enumerate(cards[:25], 1):
        vals = re.findall(
            r'<div class="v99-tl-m-val[^"]*".*?>\s*([^<]*?)\s*</div>\s*<div class="v99-tl-m-lbl">\s*([^<]+?)\s*</div>',
            metrics_html,
            re.S
        )
        clean = " | ".join([f"{b.strip()}={a.strip()}" for a, b in vals])
        print(f"{idx:02d}. {name.strip():28} | {cls.strip():9} | {pill.strip():12} | {clean}")

print()
print("===== RAPOR BITTI =====")
