import json

from flask import render_template, request, jsonify


def register_reports_routes(app, deps):
    get_db = deps["get_db"]
    all_route_names = deps["all_route_names"]
    SEAT_NUMBERS = deps["SEAT_NUMBERS"]

    def events_page():
        get_active_trip = deps.get("get_active_trip")
        tid = get_active_trip() if callable(get_active_trip) else None

        sums = {"devir": 0, "giris": 0, "cikis": 0, "kalan": 0}
        trip = {}

        if tid:
            db = get_db()
            trip_row = db.execute("SELECT * FROM trips WHERE id=?", (tid,)).fetchone()
            trip = dict(trip_row) if trip_row else {}

            try:
                if hasattr(app, "cash_sums"):
                    sums = dict(app.cash_sums(tid))
            except Exception:
                pass

        return render_template("events.html", sums=sums, trip=trip)

    def api_events():
        route = (request.args.get("route") or "").strip()
        d1 = request.args.get("date_from")
        d2 = request.args.get("date_to")

        sql = """
        SELECT l.id, l.trip_id, t.date, t.route, l.stop_name, l.event, l.distance_km,
               l.seats_for_stop, l.meta_json, l.ts
        FROM stop_logs l
        JOIN trips t ON t.id = l.trip_id
        WHERE 1=1
        """
        args = []

        if route:
            sql += " AND t.route=?"
            args.append(route)
        if d1:
            sql += " AND t.date >= ?"
            args.append(d1)
        if d2:
            sql += " AND t.date <= ?"
            args.append(d2)

        sql += " ORDER BY l.ts DESC, l.id DESC LIMIT 500"
        rows = get_db().execute(sql, args).fetchall()

        items = []
        for r in rows:
            try:
                meta = json.loads(r["meta_json"]) if r["meta_json"] else None
            except Exception:
                meta = None

            items.append({
                "id": r["id"],
                "trip_id": r["trip_id"],
                "date": r["date"],
                "route": r["route"],
                "stop_name": r["stop_name"],
                "event": r["event"],
                "distance_km": r["distance_km"],
                "seats_for_stop": r["seats_for_stop"],
                "meta": meta,
                "ts": r["ts"],
            })

        return jsonify({"ok": True, "items": items})

    def reports_page():
        return render_template("reports.html", all_routes=all_route_names())

    def api_report_seat_stats():
        route = (request.args.get("route") or "").strip()
        d1 = request.args.get("date_from")
        d2 = request.args.get("date_to")

        where = ["1=1"]
        args = []

        if route:
            where.append("t.route=?")
            args.append(route)
        if d1:
            where.append("t.date >= ?")
            args.append(d1)
        if d2:
            where.append("t.date <= ?")
            args.append(d2)

        sql_where = " AND ".join(where)
        db = get_db()

        per = db.execute(
            f"""
            SELECT s.seat_no, COUNT(*) AS times, COALESCE(SUM(s.amount),0) AS revenue
            FROM seats s
            JOIN trips t ON t.id=s.trip_id
            WHERE {sql_where}
            GROUP BY s.seat_no
            ORDER BY s.seat_no
            """,
            args,
        ).fetchall()

        per_seat = [{
            "seat_no": int(r["seat_no"]),
            "times": int(r["times"]),
            "revenue": float(r["revenue"]),
        } for r in per]

        sold_seats = {x["seat_no"] for x in per_seat}
        never_sold = [n for n in SEAT_NUMBERS if n not in sold_seats]

        seat_tot = db.execute(
            f"""
            SELECT COALESCE(SUM(s.amount),0) AS revenue, COUNT(*) AS cnt
            FROM seats s
            JOIN trips t ON t.id=s.trip_id
            WHERE {sql_where}
            """,
            args,
        ).fetchone()

        walk_tot = db.execute(
            f"""
            SELECT COALESCE(SUM(w.total_amount),0) AS revenue, COALESCE(SUM(w.pax),0) AS pax
            FROM walk_on_sales w
            JOIN trips t ON t.id=w.trip_id
            WHERE {sql_where}
            """,
            args,
        ).fetchone()

        top_seat = max(per_seat, key=lambda x: (x["times"], x["revenue"])) if per_seat else None

        return jsonify({
            "ok": True,
            "filters": {"route": route or None, "date_from": d1, "date_to": d2},
            "totals": {
                "seated_count": int(seat_tot["cnt"] or 0),
                "seated_revenue": float(seat_tot["revenue"] or 0),
                "walk_pax": int(walk_tot["pax"] or 0),
                "walk_revenue": float(walk_tot["revenue"] or 0),
                "overall_revenue": float(seat_tot["revenue"] or 0) + float(walk_tot["revenue"] or 0),
            },
            "per_seat": per_seat,
            "top_seat": top_seat,
            "never_sold": never_sold,
        })

    app.add_url_rule("/olaylar", endpoint="events_page", view_func=events_page, methods=["GET"])
    app.add_url_rule("/api/events", endpoint="api_events", view_func=api_events, methods=["GET"])
    app.add_url_rule("/raporlar", endpoint="reports_page", view_func=reports_page, methods=["GET"])
    app.add_url_rule("/api/report/seat-stats", endpoint="api_report_seat_stats", view_func=api_report_seat_stats, methods=["GET"])
