from pathlib import Path
from datetime import datetime
import shutil
import re

ROOT = Path(".").resolve()
STAMP = datetime.now().strftime("%Y%m%d-%H%M%S")

print("===== V92C TAMAMLA = YOLCU + EMANET + BAGAJ TEMİZLE =====")

SKIP_PARTS = {
    ".git", "__pycache__", ".gradle", "build", ".idea",
    "node_modules", "venv", ".venv", "tools"
}

def skip(p: Path):
    return any(x in SKIP_PARTS for x in p.parts)

py_files = [
    p for p in ROOT.rglob("*.py")
    if not skip(p)
    and "site-packages" not in str(p)
    and ".bak-" not in p.name
]

def find_route_block(txt):
    m = re.search(r'^[ \t]*@app\.route\([^\n]*live-stop-complete[^\n]*\)[\s\S]*?^[ \t]*def\s+\w+\s*\(', txt, re.M)
    if not m:
        return None

    start = m.start()
    def_start = txt.rfind("\ndef ", start, m.end())
    if def_start == -1:
        def_match = re.search(r'^[ \t]*def\s+\w+\s*\(', txt[m.start():], re.M)
        if not def_match:
            return None
        def_start = m.start() + def_match.start()
    else:
        def_start += 1

    # route decorator'ından başlamalı
    route_start = txt.rfind("\n@app.route", 0, def_start)
    if route_start == -1:
        route_start = txt.rfind("\n    @app.route", 0, def_start)
    if route_start == -1:
        route_start = start
    else:
        route_start += 1

    # def bitişi: sonraki satır başı decorator veya def
    after_def = txt.find("\n", def_start)
    if after_def == -1:
        return None

    m2 = re.search(r'\n(?=(?:@app\.route|def\s+|@[\w\.]+|if\s+__name__\s*==))', txt[after_def:], re.M)
    if m2:
        end = after_def + m2.start() + 1
    else:
        end = len(txt)

    return route_start, end

NEW_ROUTE = r'''
@app.route("/api/live-stop-complete", methods=["POST"])
def api_live_stop_complete_v92c():
    """
    V92C:
    Canlı durak özetindeki TAMAMLA butonu artık o durağı sahada bitirir.
    - Bu durakta inecek koltuklu yolcular temizlenir.
    - Bu durakta inen ara yolcular temizlenir.
    - Bu durağa teslim edilecek emanet/kargo teslim edildi yapılır.
    - Canlı durak sıradaki durağa alınır.
    """
    from flask import request, jsonify
    import sqlite3
    import json
    from pathlib import Path
    from datetime import datetime

    def db_path_v92c():
        bases = []
        try:
            bases.append(Path.cwd())
        except Exception:
            pass
        try:
            here = Path(__file__).resolve()
            bases.append(here.parent)
            bases.extend(list(here.parents))
        except Exception:
            pass

        seen = set()
        for b in bases:
            try:
                key = str(b)
                if key in seen:
                    continue
                seen.add(key)
                cand = b / "db.sqlite3"
                if cand.exists():
                    return str(cand)
            except Exception:
                pass

        return "db.sqlite3"

    def now_text():
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def norm(x):
        return str(x or "").strip()

    def lower(x):
        return norm(x).lower()

    def active_trip_id(cur, payload):
        raw = payload.get("trip_id") or payload.get("tripId")
        try:
            if raw:
                return int(raw)
        except Exception:
            pass

        try:
            row = cur.execute("SELECT active_trip_id FROM app_state WHERE id=1").fetchone()
            if row and row["active_trip_id"]:
                return int(row["active_trip_id"])
        except Exception:
            pass

        try:
            row = cur.execute("SELECT trip_id FROM live_runtime_state ORDER BY updated_at DESC LIMIT 1").fetchone()
            if row and row["trip_id"]:
                return int(row["trip_id"])
        except Exception:
            pass

        row = cur.execute("SELECT id FROM trips ORDER BY id DESC LIMIT 1").fetchone()
        return int(row["id"]) if row else 0

    def active_stop(cur, trip_id, payload):
        stop = norm(payload.get("stop") or payload.get("stop_name") or payload.get("live_stop"))
        if stop:
            return stop

        try:
            row = cur.execute("SELECT live_stop FROM live_runtime_state WHERE trip_id=?", (trip_id,)).fetchone()
            if row and norm(row["live_stop"]):
                return norm(row["live_stop"])
        except Exception:
            pass

        return ""

    def route_name(cur, trip_id):
        row = cur.execute("SELECT route FROM trips WHERE id=?", (trip_id,)).fetchone()
        return norm(row["route"]) if row else ""

    def next_stop_from_segments(cur, route, stop):
        # En güvenilir kaynak: route_segments. Örnek: Ortahan -> Belenyaka.
        try:
            row = cur.execute("""
                SELECT to_stop
                FROM route_segments
                WHERE route = ?
                  AND lower(trim(from_stop)) = lower(trim(?))
                ORDER BY sort_order ASC
                LIMIT 1
            """, (route, stop)).fetchone()
            if row and norm(row["to_stop"]):
                return norm(row["to_stop"])
        except Exception:
            pass

        try:
            row = cur.execute("""
                SELECT to_stop
                FROM route_profile_segments
                WHERE route = ?
                  AND lower(trim(from_stop)) = lower(trim(?))
                ORDER BY sort_order ASC
                LIMIT 1
            """, (route, stop)).fetchone()
            if row and norm(row["to_stop"]):
                return norm(row["to_stop"])
        except Exception:
            pass

        # Yedek: routes.stops JSON/metin listesinden sıradakini bul.
        try:
            row = cur.execute("SELECT stops FROM routes WHERE name=? LIMIT 1", (route,)).fetchone()
            if row and norm(row["stops"]):
                raw = norm(row["stops"])
                stops = []
                try:
                    data = json.loads(raw)
                    if isinstance(data, list):
                        stops = [norm(x) for x in data]
                except Exception:
                    stops = [norm(x) for x in re.split(r"[,\n>|→]+", raw) if norm(x)]

                for i, s in enumerate(stops):
                    if lower(s) == lower(stop) and i + 1 < len(stops):
                        return stops[i + 1]
        except Exception:
            pass

        return ""

    payload = request.get_json(silent=True) or {}
    if not isinstance(payload, dict):
        payload = {}

    db = db_path_v92c()
    con = sqlite3.connect(db)
    con.row_factory = sqlite3.Row
    cur = con.cursor()

    try:
        trip_id = active_trip_id(cur, payload)
        stop = active_stop(cur, trip_id, payload)

        if not trip_id:
            return jsonify({"ok": False, "completed": False, "error": "Aktif sefer bulunamadı."}), 400

        if not stop:
            return jsonify({"ok": False, "completed": False, "error": "Canlı durak bulunamadı."}), 400

        route = route_name(cur, trip_id)
        next_stop = next_stop_from_segments(cur, route, stop)

        # 1) Bu durakta inecek koltuklu yolcuları temizle.
        seat_rows = cur.execute("""
            SELECT seat_no
            FROM seats
            WHERE trip_id = ?
              AND (
                    lower(trim(to_stop)) = lower(trim(?))
                 OR lower(trim(stop)) = lower(trim(?))
              )
        """, (trip_id, stop, stop)).fetchall()

        seat_numbers = [str(r["seat_no"]) for r in seat_rows]

        cur.execute("""
            DELETE FROM seats
            WHERE trip_id = ?
              AND (
                    lower(trim(to_stop)) = lower(trim(?))
                 OR lower(trim(stop)) = lower(trim(?))
              )
        """, (trip_id, stop, stop))
        removed_seats = cur.rowcount if cur.rowcount is not None else 0

        # 2) Bu durakta inen ara yolcu kayıtlarını temizle.
        removed_walk_on = 0
        try:
            cur.execute("""
                DELETE FROM walk_on_sales
                WHERE trip_id = ?
                  AND lower(trim(to_stop)) = lower(trim(?))
            """, (trip_id, stop))
            removed_walk_on = cur.rowcount if cur.rowcount is not None else 0
        except Exception:
            removed_walk_on = 0

        # 3) Bu durağa teslim edilecek emanet/kargoyu teslim edildi yap.
        delivered_consignments = 0
        try:
            cur.execute("""
                UPDATE consignments
                SET status = 'teslim_edildi',
                    updated_at = ?,
                    delivered_at = ?
                WHERE trip_id = ?
                  AND lower(trim(to_stop)) = lower(trim(?))
                  AND lower(trim(COALESCE(status, 'bekliyor'))) NOT IN (
                      'teslim_edildi', 'iptal', 'cancelled', 'delivered'
                  )
            """, (now_text(), now_text(), trip_id, stop))
            delivered_consignments = cur.rowcount if cur.rowcount is not None else 0
        except Exception:
            delivered_consignments = 0

        # 4) Canlı durak sıradaki durağa geçsin.
        if next_stop:
            cur.execute("""
                UPDATE live_runtime_state
                SET live_stop = ?,
                    gps_km = '',
                    eta_main = '',
                    eta_sub = 'v92c-complete-next-stop',
                    updated_at = CURRENT_TIMESTAMP
                WHERE trip_id = ?
            """, (next_stop, trip_id))

            if cur.rowcount == 0:
                cur.execute("""
                    INSERT INTO live_runtime_state
                    (trip_id, live_stop, speed, gps_km, eta_main, eta_sub, updated_at)
                    VALUES (?, ?, 0, '', '', 'v92c-complete-next-stop', CURRENT_TIMESTAMP)
                """, (trip_id, next_stop))

            try:
                cur.execute("""
                    UPDATE track_state
                    SET next_stop = ?,
                        updated_at = datetime('now','localtime')
                    WHERE trip_id = ?
                """, (next_stop, trip_id))
            except Exception:
                pass

        # 5) Log at.
        meta = {
            "v": "v92c",
            "route": route,
            "stop": stop,
            "next_stop": next_stop,
            "removed_seats": removed_seats,
            "removed_walk_on": removed_walk_on,
            "delivered_consignments": delivered_consignments,
            "seat_numbers": seat_numbers,
        }

        try:
            cur.execute("""
                INSERT INTO stop_logs
                (trip_id, stop_name, event, distance_km, seats_for_stop, meta_json)
                VALUES (?, ?, 'completed_v92c', NULL, ?, ?)
            """, (trip_id, stop, removed_seats + removed_walk_on, json.dumps(meta, ensure_ascii=False)))
        except Exception:
            pass

        con.commit()

        parts = []
        if removed_seats:
            parts.append(f"{removed_seats} koltuk temizlendi")
        if removed_walk_on:
            parts.append(f"{removed_walk_on} ara yolcu temizlendi")
        if delivered_consignments:
            parts.append(f"{delivered_consignments} emanet teslim edildi")
        if not parts:
            parts.append("Durakta temizlenecek aktif kayıt yoktu")

        if next_stop:
            parts.append(f"canlı durak {next_stop} oldu")
        else:
            parts.append("sıradaki durak bulunamadı")

        return jsonify({
            "ok": True,
            "completed": True,
            "trip_id": trip_id,
            "stop": stop,
            "next_stop": next_stop,
            "removed_seats": removed_seats,
            "removed_walk_on": removed_walk_on,
            "delivered_consignments": delivered_consignments,
            "seat_numbers": seat_numbers,
            "message": " • ".join(parts)
        })

    except Exception as e:
        try:
            con.rollback()
        except Exception:
            pass
        return jsonify({
            "ok": False,
            "completed": False,
            "error": str(e)
        }), 500
    finally:
        try:
            con.close()
        except Exception:
            pass
'''

patched = []
for p in py_files:
    txt = p.read_text(encoding="utf-8", errors="ignore")
    block = find_route_block(txt)
    if not block:
        continue

    start, end = block
    bak = p.with_name(p.name + f".bak-v92c-{STAMP}")
    shutil.copy2(p, bak)

    new_txt = txt[:start] + NEW_ROUTE.strip() + "\n\n" + txt[end:]
    p.write_text(new_txt, encoding="utf-8")

    patched.append(p)
    print("✅ Patchlendi:", p.relative_to(ROOT))
    print("📦 Yedek:", bak.relative_to(ROOT))

if not patched:
    print("❌ /api/live-stop-complete route bulunamadı.")
    print("Komut:")
    print("grep -RIn \"live-stop-complete\\|api_live_stop_complete\\|completeStopFromSummary\" . --exclude-dir=.git --exclude-dir=build | head -80")
    raise SystemExit(1)

print()
print("===== SYNTAX TEST =====")
for p in patched:
    import py_compile
    try:
        py_compile.compile(str(p), doraise=True)
        print("✅ Python OK:", p.relative_to(ROOT))
    except Exception as e:
        print("❌ Python HATA:", p.relative_to(ROOT), e)
        raise

print()
print("===== ROUTE KONTROL =====")
for p in patched:
    txt = p.read_text(encoding="utf-8", errors="ignore")
    for i, line in enumerate(txt.splitlines(), 1):
        if any(k in line for k in [
            "api_live_stop_complete_v92c",
            "DELETE FROM seats",
            "UPDATE consignments",
            "UPDATE live_runtime_state",
            "v92c-complete-next-stop",
            "completed_v92c"
        ]):
            print(f"{p.relative_to(ROOT)}:{i}: {line}")

print()
print("✅ V92C tamam. Tamamla artık durak kayıtlarını temizleyip sıradaki durağa geçirir.")
