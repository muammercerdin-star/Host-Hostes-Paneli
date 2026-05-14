import json
import re

from flask import request, jsonify


def register_coords_routes(app, deps):
    get_db = deps["get_db"]
    get_active_trip = deps["get_active_trip"]
    get_active_trip_row = deps["get_active_trip_row"]
    get_stops = deps["get_stops"]

    def _route_name_variants(name: str) -> list[str]:
        raw = (name or "").strip()
        if not raw:
            return []

        variants = []

        def add(v):
            v = (v or "").strip()
            if v and v not in variants:
                variants.append(v)

        add(raw)
        add(raw.replace("–", "-"))
        add(raw.replace("-", "–"))
        add(raw.replace("—", "-"))
        add(raw.replace("—", "–"))

        no_paren = re.sub(r"\s*\([^)]*\)\s*", "", raw).strip()
        if no_paren:
            add(no_paren)
            add(no_paren.replace("–", "-"))
            add(no_paren.replace("-", "–"))
            add(no_paren.replace("—", "-"))
            add(no_paren.replace("—", "–"))

        return variants

    def _best_route_for_coords(db, requested_route: str) -> str:
        variants = _route_name_variants(requested_route)
        if not variants:
            return requested_route

        for cand in variants:
            row = db.execute(
                "SELECT route, COUNT(*) AS c FROM route_stop_coords WHERE route=? GROUP BY route LIMIT 1",
                (cand,),
            ).fetchone()
            if row and int(row["c"] or 0) > 0:
                return row["route"]

        wanted_norms = set()
        for v in variants:
            wanted_norms.add(
                re.sub(r"\s+", " ", v.replace("–", "-").replace("—", "-")).strip().lower()
            )

        rows = db.execute(
            "SELECT route, COUNT(*) AS c FROM route_stop_coords GROUP BY route ORDER BY c DESC, route ASC"
        ).fetchall()

        for row in rows:
            r = (row["route"] or "").strip()
            rn = re.sub(r"\s*\([^)]*\)\s*", "", r)
            rn = re.sub(r"\s+", " ", rn.replace("–", "-").replace("—", "-")).strip().lower()
            if rn in wanted_norms:
                return r

        return requested_route

    def _coords_items_for_route(db, route_name: str):
        """
        Durak sırası routes/get_stops kaynağından gelir.
        Koordinatlar route_stop_coords tablosundan aynı sıraya giydirilir.
        Dönüş:
          best_route: koordinat için eşleşen route adı
          ordered_names: string durak listesi
          items: koordinatlı obje listesi
        """
        best_route = _best_route_for_coords(db, route_name)
        ordered_names = get_stops(route_name) or get_stops(best_route) or []

        rows = db.execute(
            "SELECT route, stop, lat, lng FROM route_stop_coords WHERE route=?",
            (best_route,),
        ).fetchall()

        def norm_stop(v):
            v = (v or "").strip().lower()
            v = re.sub(r"\s+", " ", v)
            return v

        coord_map = {}
        for r in rows:
            key = norm_stop(r["stop"])
            if key and key not in coord_map:
                coord_map[key] = {
                    "route": r["route"],
                    "name": r["stop"],
                    "stop": r["stop"],
                    "lat": r["lat"],
                    "lng": r["lng"],
                }

        items = []
        for stop_name in ordered_names:
            key = norm_stop(stop_name)
            hit = coord_map.get(key)

            items.append({
                "route": best_route,
                "name": stop_name,
                "stop": stop_name,
                "lat": (hit["lat"] if hit else None),
                "lng": (hit["lng"] if hit else None),
            })

        return best_route, ordered_names, items

    def ensure_route_stop_coords_table(db=None):
        db = db or get_db()
        db.execute("""
            CREATE TABLE IF NOT EXISTS route_stop_coords(
                route TEXT NOT NULL,
                stop TEXT NOT NULL,
                lat REAL NOT NULL,
                lng REAL NOT NULL,
                PRIMARY KEY(route, stop)
            )
        """)
        db.commit()

    def api_stops():
        trip = get_active_trip_row()
        if not trip:
            return jsonify({
                "ok": False,
                "msg": "Aktif sefer yok",
                "stops": [],
                "items": [],
            }), 400

        db = get_db()
        route_name = (request.args.get("route") or trip["route"] or "").strip()

        best_route, ordered_names, items = _coords_items_for_route(db, route_name)

        # Sözleşme:
        # stops = sadece string isim listesi
        # items = koordinatlı obje listesi
        return jsonify({
            "ok": True,
            "route": route_name,
            "matched_route": best_route,
            "stops": ordered_names,
            "items": items,
        })

    def api_coords():
        """
        TEMİZ KOORDİNAT API
        - İnternet yok
        - Başka hat yok
        - Sadece verilen route içindeki route_stop_coords kayıtları
        """
        db = get_db()
        ensure_route_stop_coords_table(db)

        def active_route_name():
            try:
                tid = get_active_trip()
                if not tid:
                    return ""
                row = db.execute("SELECT route FROM trips WHERE id=?", (tid,)).fetchone()
                return (row["route"] if row else "") or ""
            except Exception:
                return ""

        if request.method == "GET":
            route_name = (request.args.get("route") or active_route_name() or "").strip()
            stop_name = (request.args.get("stop") or "").strip()

            if not route_name:
                return jsonify({"ok": False, "msg": "Hat adı yok", "items": []}), 400

            if stop_name:
                row = db.execute(
                    "SELECT route, stop, lat, lng FROM route_stop_coords WHERE route=? AND stop=? LIMIT 1",
                    (route_name, stop_name),
                ).fetchone()

                if not row:
                    return jsonify({
                        "ok": True,
                        "route": route_name,
                        "stop": stop_name,
                        "found": False,
                        "item": None,
                        "items": [],
                    })

                item = {
                    "route": row["route"],
                    "stop": row["stop"],
                    "lat": row["lat"],
                    "lng": row["lng"],
                }

                return jsonify({
                    "ok": True,
                    "route": route_name,
                    "stop": stop_name,
                    "found": True,
                    "item": item,
                    "items": [item],
                })

            rows = db.execute(
                "SELECT route, stop, lat, lng FROM route_stop_coords WHERE route=? ORDER BY stop",
                (route_name,),
            ).fetchall()

            return jsonify({
                "ok": True,
                "route": route_name,
                "items": [
                    {
                        "route": r["route"],
                        "stop": r["stop"],
                        "lat": r["lat"],
                        "lng": r["lng"],
                    }
                    for r in rows
                ],
            })

        data = request.get_json(silent=True) or request.form or {}

        route_name = (data.get("route") or data.get("route_name") or active_route_name() or "").strip()
        stop_name = (data.get("stop") or data.get("stop_name") or "").strip()

        if not route_name:
            return jsonify({"ok": False, "msg": "Hat adı yok"}), 400

        if not stop_name:
            return jsonify({"ok": False, "msg": "Durak adı yok"}), 400

        if request.method == "DELETE":
            db.execute(
                "DELETE FROM route_stop_coords WHERE route=? AND stop=?",
                (route_name, stop_name),
            )
            db.commit()
            return jsonify({"ok": True, "msg": "Koordinat silindi", "route": route_name, "stop": stop_name})

        try:
            lat = float(data.get("lat"))
            lng = float(data.get("lng"))
        except Exception:
            return jsonify({"ok": False, "msg": "Lat/Lng geçersiz"}), 400

        if not (-90 <= lat <= 90 and -180 <= lng <= 180):
            return jsonify({"ok": False, "msg": "Koordinat aralığı geçersiz"}), 400

        db.execute(
            """
            INSERT INTO route_stop_coords(route, stop, lat, lng)
            VALUES(?,?,?,?)
            ON CONFLICT(route, stop)
            DO UPDATE SET lat=excluded.lat, lng=excluded.lng
            """,
            (route_name, stop_name, lat, lng),
        )
        db.commit()

        return jsonify({
            "ok": True,
            "msg": "Koordinat kaydedildi",
            "route": route_name,
            "stop": stop_name,
            "lat": lat,
            "lng": lng,
        })

    def _coords_norm_text(x):
        x = str(x or "").strip()
        x = re.sub(r"\s+", " ", x)
        return x

    def _parse_stops_local(raw):
        if raw is None:
            return []

        if isinstance(raw, list):
            arr = raw
        else:
            txt = str(raw).strip()
            if not txt:
                return []

            try:
                obj = json.loads(txt)
                arr = obj if isinstance(obj, list) else re.split(r"[\n,]+", txt)
            except Exception:
                arr = re.split(r"[\n,]+", txt)

        out = []
        seen = set()

        for item in arr:
            stop = _coords_norm_text(item)
            key = stop.casefold()
            if stop and key not in seen:
                seen.add(key)
                out.append(stop)

        return out

    def _save_route_stop_coord_local(route_name, stop_name, lat, lng):
        db = get_db()
        db.execute(
            """
            INSERT INTO route_stop_coords(route, stop, lat, lng)
            VALUES(?,?,?,?)
            ON CONFLICT(route, stop)
            DO UPDATE SET lat=excluded.lat, lng=excluded.lng
            """,
            (route_name, stop_name, lat, lng),
        )
        db.commit()

    def api_route_coord_status(rid):
        ensure_route_stop_coords_table()

        db = get_db()
        route = db.execute("SELECT * FROM routes WHERE id=?", (rid,)).fetchone()
        if not route:
            return jsonify({"ok": False, "msg": "Hat bulunamadı"}), 404

        data = request.get_json(silent=True) or {}

        route_name = (data.get("route_name") or route["name"] or "").strip()
        stops = _parse_stops_local(data.get("stops"))

        if not stops:
            stops = _parse_stops_local(route["stops"])

        if not route_name:
            return jsonify({"ok": False, "msg": "Hat adı boş"}), 400

        if not stops:
            return jsonify({"ok": False, "msg": "Durak listesi boş"}), 400

        items = []
        saved = 0
        missing = 0

        for stop in stops:
            row = db.execute(
                "SELECT route, stop, lat, lng FROM route_stop_coords WHERE route=? AND stop=? LIMIT 1",
                (route_name, stop),
            ).fetchone()

            if row:
                saved += 1
                items.append({
                    "stop": stop,
                    "status": "saved",
                    "msg": "Bu hatta kayıtlı",
                    "lat": row["lat"],
                    "lng": row["lng"],
                })
            else:
                missing += 1
                items.append({
                    "stop": stop,
                    "status": "missing",
                    "msg": "Koordinat yok. Elle girilecek.",
                })

        return jsonify({
            "ok": True,
            "route": route_name,
            "total": len(stops),
            "saved": saved,
            "copied": 0,
            "missing": missing,
            "items": items,
        })

    def api_route_coord_save_manual(rid):
        ensure_route_stop_coords_table()

        db = get_db()
        route = db.execute("SELECT * FROM routes WHERE id=?", (rid,)).fetchone()
        if not route:
            return jsonify({"ok": False, "msg": "Hat bulunamadı"}), 404

        data = request.get_json(silent=True) or {}

        route_name = (data.get("route_name") or route["name"] or "").strip()
        stop = (data.get("stop") or "").strip()

        try:
            lat = float(data.get("lat"))
            lng = float(data.get("lng"))
        except Exception:
            return jsonify({"ok": False, "msg": "Lat/Lng geçersiz"}), 400

        if not route_name:
            return jsonify({"ok": False, "msg": "Hat adı boş"}), 400

        if not stop:
            return jsonify({"ok": False, "msg": "Durak adı boş"}), 400

        if not (-90 <= lat <= 90 and -180 <= lng <= 180):
            return jsonify({"ok": False, "msg": "Koordinat aralığı geçersiz"}), 400

        _save_route_stop_coord_local(route_name, stop, lat, lng)

        return jsonify({
            "ok": True,
            "msg": "Koordinat kaydedildi",
            "route": route_name,
            "stop": stop,
            "lat": lat,
            "lng": lng,
        })

    app.add_url_rule("/api/stops", endpoint="api_stops", view_func=api_stops, methods=["GET"])
    app.add_url_rule("/api/coords", endpoint="api_coords", view_func=api_coords, methods=["GET", "POST", "DELETE"])
    app.add_url_rule("/api/routes/<int:rid>/coord-status", endpoint="api_route_coord_status", view_func=api_route_coord_status, methods=["POST"])
    app.add_url_rule("/api/routes/<int:rid>/coord-save-manual", endpoint="api_route_coord_save_manual", view_func=api_route_coord_save_manual, methods=["POST"])

    app.ensure_route_stop_coords_table = ensure_route_stop_coords_table
    app.coords_items_for_route = _coords_items_for_route
