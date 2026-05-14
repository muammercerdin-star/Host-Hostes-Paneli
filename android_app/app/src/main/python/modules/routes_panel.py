import json

from flask import render_template, request, redirect, url_for, jsonify, abort


def register_routes_routes(app, deps):
    get_db = deps["get_db"]
    get_stops = deps["get_stops"]
    all_route_names = deps["all_route_names"]
    parse_stops = deps["parse_stops"]
    ROUTE_STOPS = deps["ROUTE_STOPS"]

    norm_bool = deps["norm_bool"]
    parse_int = deps["parse_int"]
    parse_float = deps["parse_float"]
    normalize_hhmm = deps["normalize_hhmm"]
    get_csrf = deps["get_csrf"]

    schedule_profiles_for_route = deps["schedule_profiles_for_route"]
    schedule_profile_get = deps["schedule_profile_get"]
    schedule_editor_rows = deps["schedule_editor_rows"]
    schedule_default_profile_for_route = deps["schedule_default_profile_for_route"]

    def routes_list():
        db = get_db()
        rows = db.execute("SELECT id, name FROM routes ORDER BY name").fetchall()
        db_names = {r["name"] for r in rows}

        builtin_routes = []
        for name in ROUTE_STOPS.keys():
            builtin_routes.append({
                "name": name,
                "overridden": name in db_names,
                "edit_url": url_for("builtin_route_edit", name=name),
            })

        return render_template("routes_list.html", routes=rows, builtin_routes=builtin_routes)

    def add_route():
        if request.method == "POST":
            name = (request.form.get("name") or "").strip()
            stops_text = (request.form.get("stops") or "").strip()

            if not name or not stops_text:
                return "Hat adı ve duraklar zorunludur", 400

            db = get_db()
            db.execute(
                "INSERT OR REPLACE INTO routes(name, stops) VALUES(?, ?)",
                (name, json.dumps(parse_stops(stops_text), ensure_ascii=False)),
            )
            db.commit()

            from flask import session
            session["route"] = name
            return redirect(url_for("index"))

        return render_template("add_route.html")

    def route_edit(rid):
        db = get_db()
        row = db.execute("SELECT * FROM routes WHERE id=?", (rid,)).fetchone()

        if not row:
            return "Hat bulunamadı", 404

        if request.method == "POST":
            name = (request.form.get("name") or "").strip()
            stops_text = request.form.get("stops") or ""
            stops = parse_stops(stops_text)

            if not name or not stops:
                return "Hat adı ve en az bir durak gerekli", 400

            db.execute(
                "UPDATE routes SET name=?, stops=? WHERE id=?",
                (name, json.dumps(stops, ensure_ascii=False), rid),
            )
            db.commit()

            from flask import session
            session["route"] = name
            return redirect(url_for("routes_list"))

        try:
            stops_text = "\n".join(json.loads(row["stops"]) or [])
        except Exception:
            stops_text = ""

        return render_template("route_edit.html", route=row, stops_text=stops_text)

    def materialize_builtin_route(name: str):
        stops = ROUTE_STOPS.get(name)

        if not stops:
            return None

        db = get_db()
        db.execute(
            "INSERT OR REPLACE INTO routes(name, stops) VALUES(?, ?)",
            (name, json.dumps(stops, ensure_ascii=False)),
        )
        db.commit()

        row = db.execute("SELECT id FROM routes WHERE name=?", (name,)).fetchone()
        return row["id"] if row else None

    def builtin_route_edit():
        name = (request.args.get("name") or "").strip()

        if name not in ROUTE_STOPS:
            abort(404, description="Sabit hat bulunamadı")

        rid = materialize_builtin_route(name)

        if not rid:
            abort(500, description="Sabit hat DB'ye kopyalanamadı")

        from flask import session
        session["route"] = name

        return redirect(url_for("route_edit", rid=rid))

    def route_delete(rid):
        db = get_db()
        row = db.execute("SELECT name FROM routes WHERE id=?", (rid,)).fetchone()
        db.execute("DELETE FROM routes WHERE id=?", (rid,))
        db.commit()

        from flask import session
        if row and session.get("route") == row["name"]:
            session.pop("route", None)

        return redirect(url_for("routes_list"))

    def route_schedule_edit(rid):
        db = get_db()
        route_row = db.execute("SELECT * FROM routes WHERE id=?", (rid,)).fetchone()

        if not route_row:
            return "Hat bulunamadı", 404

        route_name = route_row["name"]

        if request.method == "POST":
            action = (request.form.get("action") or "save").strip()
            profile_id = parse_int(request.form.get("profile_id"), None)

            if action == "delete_profile":
                if profile_id:
                    db.execute(
                        "DELETE FROM route_schedule_profiles WHERE id=? AND route_name=?",
                        (profile_id, route_name),
                    )
                    db.commit()
                return redirect(url_for("route_schedule_edit", rid=rid))

            title = (request.form.get("title") or "").strip() or "Varsayılan"
            direction = (request.form.get("direction") or "gidis").strip().lower()

            if direction not in {"gidis", "donus"}:
                direction = "gidis"

            is_default = norm_bool(request.form.get("is_default"))
            profile_note = (request.form.get("profile_note") or "").strip()

            existing = None
            if profile_id:
                existing = db.execute(
                    "SELECT id, route_name FROM route_schedule_profiles WHERE id=?",
                    (profile_id,),
                ).fetchone()

            if is_default:
                db.execute(
                    """
                    UPDATE route_schedule_profiles
                    SET is_default=0, updated_at=datetime('now','localtime')
                    WHERE route_name=? AND direction=?
                    """,
                    (route_name, direction),
                )

            if existing and existing["route_name"] == route_name:
                db.execute(
                    """
                    UPDATE route_schedule_profiles
                    SET title=?, direction=?, is_default=?, note=?, updated_at=datetime('now','localtime')
                    WHERE id=?
                    """,
                    (title, direction, is_default, profile_note, profile_id),
                )
            else:
                cur = db.execute(
                    """
                    INSERT INTO route_schedule_profiles(route_name, title, direction, is_default, note)
                    VALUES(?,?,?,?,?)
                    """,
                    (route_name, title, direction, is_default, profile_note),
                )
                profile_id = cur.lastrowid

            posted_stops = request.form.getlist("stop_name")
            posted_times = request.form.getlist("planned_time")
            posted_kms = request.form.getlist("segment_km")
            posted_notes = request.form.getlist("item_note")
            posted_timed = set(request.form.getlist("is_timed"))

            allowed_stops = set(get_stops(route_name))

            db.execute("DELETE FROM route_schedule_items WHERE profile_id=?", (profile_id,))

            for idx, stop_name in enumerate(posted_stops):
                stop_name = (stop_name or "").strip()

                if not stop_name or stop_name not in allowed_stops:
                    continue

                planned_time = normalize_hhmm(posted_times[idx] if idx < len(posted_times) else "")
                seg_raw = (posted_kms[idx] if idx < len(posted_kms) else "").strip()
                segment_km = parse_float(seg_raw, None) if seg_raw else None
                item_note = (posted_notes[idx] if idx < len(posted_notes) else "").strip()
                is_timed_item = 1 if stop_name in posted_timed else 0

                db.execute(
                    """
                    INSERT INTO route_schedule_items(
                        profile_id, stop_name, planned_time, segment_km, is_timed, sort_order, note
                    )
                    VALUES(?,?,?,?,?,?,?)
                    """,
                    (
                        profile_id,
                        stop_name,
                        planned_time,
                        segment_km,
                        is_timed_item,
                        idx,
                        item_note,
                    ),
                )

            db.commit()

            return redirect(url_for("route_schedule_edit", rid=rid, profile_id=profile_id))

        profiles = schedule_profiles_for_route(route_name)

        selected_profile_id = parse_int(request.args.get("profile_id"), None)

        if not selected_profile_id and profiles:
            default_profile = next((x for x in profiles if int(x.get("is_default", 0) or 0) == 1), None)
            selected_profile_id = (default_profile or profiles[0]).get("id")

        selected_profile = schedule_profile_get(selected_profile_id) if selected_profile_id else None
        editor_rows = schedule_editor_rows(route_name, selected_profile_id)

        return render_template(
            "route_schedule_edit.html",
            route=route_row,
            route_name=route_name,
            profiles=profiles,
            selected_profile=selected_profile,
            editor_rows=editor_rows,
        )

    def api_route_schedule():
        route_name = (request.args.get("route") or "").strip()
        direction = (request.args.get("direction") or "gidis").strip().lower()

        if direction not in {"gidis", "donus"}:
            direction = "gidis"

        if not route_name:
            trip = deps["get_active_trip_row"]()
            if not trip:
                return jsonify({"ok": False, "msg": "Aktif sefer yok"}), 400
            route_name = trip["route"]

        profile = schedule_default_profile_for_route(route_name, direction)

        if not profile:
            return jsonify({
                "ok": True,
                "route_name": route_name,
                "direction": direction,
                "profile": None,
                "items": [],
            })

        items = get_db().execute(
            """
            SELECT stop_name, planned_time, segment_km, is_timed, sort_order, note
            FROM route_schedule_items
            WHERE profile_id=?
            ORDER BY sort_order, id
            """,
            (profile["id"],),
        ).fetchall()

        return jsonify({
            "ok": True,
            "route_name": route_name,
            "direction": direction,
            "profile": profile,
            "items": [dict(r) for r in items],
        })

    def fetch_fare_exact(route: str, from_stop: str, to_stop: str):
        row = get_db().execute(
            "SELECT price FROM fares WHERE route=? AND from_stop=? AND to_stop=?",
            (route, from_stop, to_stop),
        ).fetchone()

        return float(row["price"]) if row else None

    def quote_price_segmented(route: str, from_stop: str, to_stop: str):
        stops = get_stops(route)

        if not stops or from_stop not in stops or to_stop not in stops:
            return None, "missing-stops"

        i = stops.index(from_stop)
        j = stops.index(to_stop)

        if i == j:
            return 0.0, "same-stop"

        if i > j:
            return None, "wrong-order"

        exact = fetch_fare_exact(route, from_stop, to_stop)

        if exact is not None:
            return exact, "direct"

        total = 0.0
        db = get_db()

        for k in range(i, j):
            a, b = stops[k], stops[k + 1]
            row = db.execute(
                "SELECT price FROM fares WHERE route=? AND from_stop=? AND to_stop=?",
                (route, a, b),
            ).fetchone()

            if not row:
                return None, "segment-missing"

            total += float(row["price"])

        return total, "summed"

    def fare_query():
        routes = all_route_names()
        route = (request.args.get("route") or (routes[0] if routes else "")).strip()
        stops = get_stops(route)
        from_stop = (request.args.get("from") or "").strip()
        to_stop = (request.args.get("to") or "").strip()

        price = None
        method = None
        msg = None

        if route and from_stop and to_stop:
            price, method = quote_price_segmented(route, from_stop, to_stop)

            if price is None:
                if method == "wrong-order":
                    msg = "Biniş, inişten önce olmalı."
                elif method == "segment-missing":
                    msg = "Segment fiyatı eksik."
                elif method == "missing-stops":
                    msg = "Durak(lar) bu hatta yok."
                else:
                    msg = "Fiyat bulunamadı."
            elif method == "same-stop":
                msg = "Aynı durak seçildi (0 TL)."

        return render_template(
            "fare_query.html",
            routes=routes,
            current_route=route,
            stops=stops,
            from_stop=from_stop,
            to_stop=to_stop,
            price=price,
            method=method,
            msg=msg,
            csrf_token=get_csrf(),
        )

    def fare_admin():
        routes = all_route_names()

        if request.method == "POST":
            route = (request.form.get("route") or (routes[0] if routes else "")).strip()
            from_stop = (request.form.get("from") or "").strip()
            to_stop = (request.form.get("to") or "").strip()
            price = parse_float(request.form.get("price"), None)

            if not from_stop or not to_stop or price is None:
                stops = get_stops(route)
                fare_list = get_db().execute(
                    "SELECT from_stop, to_stop, price FROM fares WHERE route=? ORDER BY rowid",
                    (route,),
                ).fetchall()

                return render_template(
                    "fare_admin.html",
                    routes=routes,
                    current_route=route,
                    stops=stops,
                    from_stop=from_stop,
                    to_stop=to_stop,
                    current_price=price,
                    fare_list=fare_list,
                    csrf_token=get_csrf(),
                )

            db = get_db()
            db.execute(
                """
                INSERT INTO fares(route, from_stop, to_stop, price)
                VALUES(?, ?, ?, ?)
                ON CONFLICT(route, from_stop, to_stop) DO UPDATE SET
                    price=excluded.price,
                    updated_at=datetime('now','localtime')
                """,
                (route, from_stop, to_stop, price),
            )
            db.commit()

        route = (request.args.get("route") or (routes[0] if routes else "")).strip()
        from_stop = (request.args.get("from") or "").strip()
        to_stop = (request.args.get("to") or "").strip()
        stops = get_stops(route)

        row = get_db().execute(
            "SELECT price FROM fares WHERE route=? AND from_stop=? AND to_stop=?",
            (route, from_stop, to_stop),
        ).fetchone()

        current_price = float(row["price"]) if row else None

        fare_list = get_db().execute(
            "SELECT from_stop, to_stop, price FROM fares WHERE route=? ORDER BY rowid",
            (route,),
        ).fetchall()

        return render_template(
            "fare_admin.html",
            routes=routes,
            current_route=route,
            stops=stops,
            from_stop=from_stop,
            to_stop=to_stop,
            current_price=current_price,
            fare_list=fare_list,
            csrf_token=get_csrf(),
        )

    app.add_url_rule("/hatlar", endpoint="routes_list", view_func=routes_list, methods=["GET"])
    app.add_url_rule("/hat-ekle", endpoint="add_route", view_func=add_route, methods=["GET", "POST"])
    app.add_url_rule("/hat/<int:rid>/duzenle", endpoint="route_edit", view_func=route_edit, methods=["GET", "POST"])
    app.add_url_rule("/hat/builtin/duzenle", endpoint="builtin_route_edit", view_func=builtin_route_edit, methods=["GET"])
    app.add_url_rule("/hat/<int:rid>/sil", endpoint="route_delete", view_func=route_delete, methods=["POST"])
    app.add_url_rule("/hat/<int:rid>/saatler", endpoint="route_schedule_edit", view_func=route_schedule_edit, methods=["GET", "POST"])
    app.add_url_rule("/api/route-schedule", endpoint="api_route_schedule", view_func=api_route_schedule, methods=["GET"])
    app.add_url_rule("/fiyat", endpoint="fare_query", view_func=fare_query, methods=["GET"])
    app.add_url_rule("/fiyat-g", endpoint="fare_admin", view_func=fare_admin, methods=["GET", "POST"])

    app.fetch_fare_exact = fetch_fare_exact
    app.quote_price_segmented = quote_price_segmented
    app.materialize_builtin_route = materialize_builtin_route
