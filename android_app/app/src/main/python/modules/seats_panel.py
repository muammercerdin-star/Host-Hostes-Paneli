from flask import render_template, request, redirect, url_for, jsonify


def register_seats_routes(app, deps):
    get_active_trip = deps["get_active_trip"]
    set_active_trip = deps["set_active_trip"]
    get_db = deps["get_db"]
    get_stops = deps["get_stops"]
    SEAT_POSITIONS = deps["SEAT_POSITIONS"]

    validate_seat_no = deps["validate_seat_no"]
    parse_int = deps["parse_int"]
    parse_int_list = deps["parse_int_list"]
    parse_float = deps["parse_float"]

    norm_ticket_type = deps["norm_ticket_type"]
    norm_payment = deps["norm_payment"]
    norm_gender = deps["norm_gender"]
    norm_bool = deps["norm_bool"]

    neighbor_rule_ok = deps["neighbor_rule_ok"]
    validate_stop_for_active_trip = deps["validate_stop_for_active_trip"]

    log_trip_stop_event = deps["log_trip_stop_event"]
    _seat_event_meta = deps["_seat_event_meta"]
    _trip_key_from_row = deps["_trip_key_from_row"]
    clear_bags_for_seat = deps["clear_bags_for_seat"]

    def seats_page():
        tid = get_active_trip()
        if not tid:
            return redirect(url_for("trip_start"))

        db = get_db()
        trip = db.execute("SELECT * FROM trips WHERE id=?", (tid,)).fetchone()
        if not trip:
            set_active_trip(None)
            return redirect(url_for("trip_start"))

        rows = db.execute(
            """
            SELECT seat_no, from_stop, to_stop, gender,
                   COALESCE(service,0) AS service,
                   COALESCE(service_note,'') AS service_note
            FROM seats
            WHERE trip_id=?
            ORDER BY seat_no
            """,
            (tid,),
        ).fetchall()

        assigned = {r["seat_no"]: True for r in rows}
        stops_map = {r["seat_no"]: (r["to_stop"] or "") for r in rows}
        boards_map = {r["seat_no"]: (r["from_stop"] or "") for r in rows}
        genders = {r["seat_no"]: (r["gender"] or "") for r in rows}
        service_map = {r["seat_no"]: bool(r["service"]) for r in rows}
        service_notes = {r["seat_no"]: (r["service_note"] or "") for r in rows}

        return render_template(
            "seats.html",
            trip=trip,
            stops=get_stops(trip["route"]),
            seat_positions=SEAT_POSITIONS,
            assigned=assigned,
            stops_map=stops_map,
            boards_map=boards_map,
            genders=genders,
            service_map=service_map,
            service_notes=service_notes,
        )

    def passenger_control():
        tid = get_active_trip()
        if not tid:
            return redirect(url_for("trip_start"))

        trip = get_db().execute("SELECT * FROM trips WHERE id=?", (tid,)).fetchone()
        return render_template("passenger_control.html", trip=trip, stops=get_stops(trip["route"]))

    def api_seats_list():
        tid = get_active_trip()
        if not tid:
            return jsonify({"ok": False, "msg": "Aktif sefer yok", "items": []}), 400

        rows = get_db().execute(
            """
            SELECT seat_no,
                   from_stop,
                   to_stop AS stop,
                   to_stop,
                   ticket_type,
                   payment,
                   amount,
                   gender,
                   COALESCE(service,0) AS service,
                   COALESCE(service_note,'') AS service_note
            FROM seats
            WHERE trip_id=?
            ORDER BY seat_no
            """,
            (tid,),
        ).fetchall()

        return jsonify({"ok": True, "items": [dict(r) for r in rows]})

    def api_seat():
        tid = get_active_trip()
        if not tid:
            return jsonify({"ok": False, "msg": "Aktif sefer yok"}), 400

        db = get_db()

        if request.method == "DELETE":
            seat_no = parse_int(request.args.get("seat_no"), None)
            if seat_no is None:
                return jsonify({"ok": False, "msg": "seat_no geçersiz"}), 400
            if not validate_seat_no(seat_no):
                return jsonify({"ok": False, "msg": "Geçersiz koltuk numarası"}), 400

            old_row = db.execute(
                "SELECT * FROM seats WHERE trip_id=? AND seat_no=?",
                (tid, seat_no),
            ).fetchone()

            if old_row and (old_row["to_stop"] or "").strip():
                log_trip_stop_event(
                    db,
                    tid,
                    old_row["to_stop"],
                    "offload",
                    _seat_event_meta(old_row, {"action": "offload_single"}),
                )

            bag_deleted = 0
            try:
                trip_row = db.execute("SELECT * FROM trips WHERE id=?", (tid,)).fetchone()
                trip_key = _trip_key_from_row(trip_row)
                bag_deleted = clear_bags_for_seat(trip_key, seat_no)
            except Exception:
                bag_deleted = 0

            db.execute("DELETE FROM seats WHERE trip_id=? AND seat_no=?", (tid, seat_no))
            db.commit()

            return jsonify({"ok": True, "bag_deleted": bag_deleted})

        data = request.get_json(force=True) or {}
        seat_no = parse_int(data.get("seat_no"), None)

        if seat_no is None:
            return jsonify({"ok": False, "msg": "seat_no gerekli"}), 400
        if not validate_seat_no(seat_no):
            return jsonify({"ok": False, "msg": "Geçersiz koltuk numarası"}), 400

        from_stop = (data.get("from") or data.get("from_stop") or "").strip()
        to_stop = (data.get("stop") or data.get("to_stop") or data.get("to") or "").strip()

        if from_stop and not validate_stop_for_active_trip(from_stop):
            return jsonify({"ok": False, "msg": f"Durak hat üzerinde değil: {from_stop}"}), 400
        if to_stop and not validate_stop_for_active_trip(to_stop):
            return jsonify({"ok": False, "msg": f"Durak hat üzerinde değil: {to_stop}"}), 400

        ticket_type = norm_ticket_type(data.get("ticket_type"))
        payment = norm_payment(data.get("payment"))
        amount = parse_float(data.get("amount"), 0.0) or 0.0
        gender = norm_gender(data.get("gender"))
        pair_ok = bool(data.get("pair_ok"))
        service = norm_bool(data.get("service"))
        service_note = (data.get("service_note") or "").strip()
        passenger_name = (data.get("passenger_name") or "").strip()
        passenger_phone = (data.get("passenger_phone") or "").strip()

        ok, msg = neighbor_rule_ok(tid, seat_no, gender, pair_ok)
        if not ok:
            return jsonify({"ok": False, "msg": msg}), 400

        old_row = db.execute(
            "SELECT * FROM seats WHERE trip_id=? AND seat_no=?",
            (tid, seat_no),
        ).fetchone()

        db.execute(
            """
            INSERT INTO seats(
                trip_id, seat_no, from_stop, to_stop, ticket_type, payment, amount,
                gender, pair_ok, service, service_note, passenger_name, passenger_phone
            )
            VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)
            ON CONFLICT(trip_id, seat_no) DO UPDATE SET
                from_stop=excluded.from_stop,
                to_stop=excluded.to_stop,
                ticket_type=excluded.ticket_type,
                payment=excluded.payment,
                amount=excluded.amount,
                gender=excluded.gender,
                pair_ok=excluded.pair_ok,
                service=excluded.service,
                service_note=excluded.service_note,
                passenger_name=excluded.passenger_name,
                passenger_phone=excluded.passenger_phone
            """,
            (
                tid, seat_no, from_stop, to_stop, ticket_type, payment, amount,
                gender, 1 if pair_ok else 0, service, service_note,
                passenger_name, passenger_phone,
            ),
        )

        if from_stop and (
            not old_row
            or (old_row["from_stop"] or "") != from_stop
            or (old_row["to_stop"] or "") != to_stop
        ):
            new_row = db.execute(
                "SELECT * FROM seats WHERE trip_id=? AND seat_no=?",
                (tid, seat_no),
            ).fetchone()

            log_trip_stop_event(
                db,
                tid,
                from_stop,
                "board",
                _seat_event_meta(new_row, {"action": "board_single"}),
            )

        db.commit()
        return jsonify({"ok": True})

    def api_seats_bulk():
        tid = get_active_trip()
        if not tid:
            return jsonify({"ok": False, "msg": "Aktif sefer yok"}), 400

        db = get_db()

        if request.method == "DELETE":
            raw = (request.args.get("seats") or "").strip()
            if not raw:
                return jsonify({"ok": False, "msg": "seats gerekli"}), 400

            seat_list = parse_int_list(raw)
            if not seat_list:
                return jsonify({"ok": False, "msg": "seats geçersiz"}), 400

            invalid = [s for s in seat_list if not validate_seat_no(s)]
            if invalid:
                return jsonify({"ok": False, "msg": f"Geçersiz koltuklar: {invalid}"}), 400

            placeholders = ",".join("?" for _ in seat_list)
            rows_to_log = db.execute(
                f"SELECT * FROM seats WHERE trip_id=? AND seat_no IN ({placeholders})",
                [tid] + seat_list,
            ).fetchall()

            for r in rows_to_log:
                if (r["to_stop"] or "").strip():
                    log_trip_stop_event(
                        db,
                        tid,
                        r["to_stop"],
                        "offload",
                        _seat_event_meta(r, {"action": "offload_bulk_delete"}),
                    )

            bag_deleted = 0
            try:
                trip_row = db.execute("SELECT * FROM trips WHERE id=?", (tid,)).fetchone()
                trip_key = _trip_key_from_row(trip_row)
                for s in seat_list:
                    bag_deleted += clear_bags_for_seat(trip_key, s)
            except Exception:
                bag_deleted = 0

            db.executemany(
                "DELETE FROM seats WHERE trip_id=? AND seat_no=?",
                [(tid, s) for s in seat_list],
            )
            db.commit()

            return jsonify({"ok": True, "deleted": seat_list, "bag_deleted": bag_deleted})

        data = request.get_json(force=True) or {}
        seats = data.get("seats")

        if not isinstance(seats, list) or not seats:
            return jsonify({"ok": False, "msg": "seats listesi gerekli"}), 400

        from_stop = (data.get("from") or data.get("from_stop") or "").strip()
        to_stop = (data.get("stop") or data.get("to_stop") or data.get("to") or "").strip()

        if from_stop and not validate_stop_for_active_trip(from_stop):
            return jsonify({"ok": False, "msg": f"Durak hat üzerinde değil: {from_stop}"}), 400
        if to_stop and not validate_stop_for_active_trip(to_stop):
            return jsonify({"ok": False, "msg": f"Durak hat üzerinde değil: {to_stop}"}), 400

        ticket_type = norm_ticket_type(data.get("ticket_type"))
        payment = norm_payment(data.get("payment") or "nakit")
        amount = parse_float(data.get("amount"), 0.0) or 0.0
        service = norm_bool(data.get("service"))
        service_note = (data.get("service_note") or "").strip()

        rows = []

        for item in seats:
            if isinstance(item, dict):
                seat_no = parse_int(item.get("seat_no"), None)
                if seat_no is None:
                    return jsonify({"ok": False, "msg": "seat_no geçersiz"}), 400
                if not validate_seat_no(seat_no):
                    return jsonify({"ok": False, "msg": f"Geçersiz koltuk numarası: {seat_no}"}), 400

                row_from = (item.get("from") or item.get("from_stop") or from_stop or "").strip()
                row_to = (item.get("stop") or item.get("to_stop") or item.get("to") or to_stop or "").strip()
                row_ticket = norm_ticket_type(item.get("ticket_type") or ticket_type)
                row_payment = norm_payment(item.get("payment") or payment)
                row_amount = parse_float(item.get("amount"), amount) or 0.0
                row_gender = norm_gender(item.get("gender"))
                row_pair_ok = bool(item.get("pair_ok"))
                row_service = norm_bool(item.get("service"))
                row_service_note = (item.get("service_note") or service_note or "").strip()

                if row_from and not validate_stop_for_active_trip(row_from):
                    return jsonify({"ok": False, "msg": f"Durak hat üzerinde değil: {row_from}"}), 400
                if row_to and not validate_stop_for_active_trip(row_to):
                    return jsonify({"ok": False, "msg": f"Durak hat üzerinde değil: {row_to}"}), 400

                ok, msg = neighbor_rule_ok(tid, seat_no, row_gender, row_pair_ok)
                if not ok:
                    return jsonify({"ok": False, "msg": msg}), 400

                rows.append((
                    tid, seat_no, row_from, row_to, row_ticket, row_payment, row_amount,
                    row_gender, 1 if row_pair_ok else 0, row_service, row_service_note, "", "",
                ))
            else:
                seat_no = parse_int(item, None)
                if seat_no is None:
                    return jsonify({"ok": False, "msg": "seat_no geçersiz"}), 400
                if not validate_seat_no(seat_no):
                    return jsonify({"ok": False, "msg": f"Geçersiz koltuk numarası: {seat_no}"}), 400

                rows.append((
                    tid, seat_no, from_stop, to_stop, ticket_type, payment, amount,
                    "", 0, service, service_note, "", "",
                ))

        db.executemany(
            """
            INSERT INTO seats(
                trip_id, seat_no, from_stop, to_stop, ticket_type, payment, amount,
                gender, pair_ok, service, service_note, passenger_name, passenger_phone
            )
            VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)
            ON CONFLICT(trip_id, seat_no) DO UPDATE SET
                from_stop=excluded.from_stop,
                to_stop=excluded.to_stop,
                ticket_type=excluded.ticket_type,
                payment=excluded.payment,
                amount=excluded.amount,
                gender=excluded.gender,
                pair_ok=excluded.pair_ok,
                service=excluded.service,
                service_note=excluded.service_note,
                passenger_name=excluded.passenger_name,
                passenger_phone=excluded.passenger_phone
            """,
            rows,
        )

        for r in rows:
            row_from = r[2]
            seat_no = r[1]

            if row_from:
                saved_row = db.execute(
                    "SELECT * FROM seats WHERE trip_id=? AND seat_no=?",
                    (tid, seat_no),
                ).fetchone()

                log_trip_stop_event(
                    db,
                    tid,
                    row_from,
                    "board",
                    _seat_event_meta(saved_row, {"action": "board_bulk"}),
                )

        db.commit()

        return jsonify({"ok": True, "count": len(rows)})

    def api_seats_offload():
        tid = get_active_trip()
        if not tid:
            return jsonify({"ok": False, "msg": "Aktif sefer yok"}), 400

        data = request.get_json(force=True) or {}
        seats = data.get("seats")

        if not isinstance(seats, list) or not seats:
            return jsonify({"ok": False, "msg": "seats listesi gerekli"}), 400

        try:
            seat_list = [int(x if not isinstance(x, dict) else x.get("seat_no")) for x in seats]
        except Exception:
            return jsonify({"ok": False, "msg": "seats geçersiz"}), 400

        invalid = [s for s in seat_list if not validate_seat_no(s)]
        if invalid:
            return jsonify({"ok": False, "msg": f"Geçersiz koltuklar: {invalid}"}), 400

        db = get_db()

        placeholders = ",".join("?" for _ in seat_list)
        rows_to_log = db.execute(
            f"SELECT * FROM seats WHERE trip_id=? AND seat_no IN ({placeholders})",
            [tid] + seat_list,
        ).fetchall()

        for r in rows_to_log:
            if (r["to_stop"] or "").strip():
                log_trip_stop_event(
                    db,
                    tid,
                    r["to_stop"],
                    "offload",
                    _seat_event_meta(r, {"action": "offload_bulk"}),
                )

        bag_deleted = 0
        try:
            trip_row = db.execute("SELECT * FROM trips WHERE id=?", (tid,)).fetchone()
            trip_key = _trip_key_from_row(trip_row)
            for s in seat_list:
                bag_deleted += clear_bags_for_seat(trip_key, s)
        except Exception:
            bag_deleted = 0

        db.executemany("DELETE FROM seats WHERE trip_id=? AND seat_no=?", [(tid, s) for s in seat_list])
        db.commit()

        return jsonify({"ok": True, "deleted": seat_list, "bag_deleted": bag_deleted})

    def api_seats_service():
        tid = get_active_trip()
        if not tid:
            return jsonify({"ok": False, "msg": "Aktif sefer yok"}), 400

        data = request.get_json(force=True) or {}
        seats = data.get("seats")

        if not isinstance(seats, list) or not seats:
            return jsonify({"ok": False, "msg": "seats listesi gerekli"}), 400

        service = norm_bool(data.get("service", 1))
        service_note = (data.get("service_note") or "").strip()

        try:
            seat_list = [int(x if not isinstance(x, dict) else x.get("seat_no")) for x in seats]
        except Exception:
            return jsonify({"ok": False, "msg": "seats geçersiz"}), 400

        db = get_db()
        db.executemany(
            """
            UPDATE seats
            SET service=?, service_note=?
            WHERE trip_id=? AND seat_no=?
            """,
            [(service, service_note, tid, s) for s in seat_list],
        )
        db.commit()

        return jsonify({
            "ok": True,
            "updated": seat_list,
            "service": service,
            "service_note": service_note,
        })

    def api_seats_gender():
        tid = get_active_trip()
        if not tid:
            return jsonify({"ok": False, "msg": "Aktif sefer yok"}), 400

        data = request.get_json(force=True) or {}
        seats = data.get("seats")

        if not isinstance(seats, list) or not seats:
            return jsonify({"ok": False, "msg": "seats listesi gerekli"}), 400

        raw_gender = (data.get("gender") or "").strip().lower()

        gender_alias = {
            "erkek": "bay",
            "bay": "bay",
            "adam": "bay",
            "kadin": "bayan",
            "kadın": "bayan",
            "bayan": "bayan",
            "kiz": "bayan",
            "kız": "bayan",
            "bos": "",
            "boş": "",
            "temizle": "",
            "sil": "",
            "sifirla": "",
            "sıfırla": "",
        }

        gender = gender_alias.get(raw_gender, raw_gender)
        if gender not in {"bay", "bayan", ""}:
            return jsonify({"ok": False, "msg": "gender geçersiz"}), 400

        try:
            seat_list = [int(x if not isinstance(x, dict) else x.get("seat_no")) for x in seats]
        except Exception:
            return jsonify({"ok": False, "msg": "seats geçersiz"}), 400

        invalid = [s for s in seat_list if not validate_seat_no(s)]
        if invalid:
            return jsonify({"ok": False, "msg": f"Geçersiz koltuklar: {invalid}"}), 400

        db = get_db()
        existing_rows = db.execute(
            f"""
            SELECT seat_no
            FROM seats
            WHERE trip_id=? AND seat_no IN ({",".join("?" * len(seat_list))})
            """,
            [tid, *seat_list],
        ).fetchall()

        existing = {int(r["seat_no"]) for r in existing_rows}
        missing = [s for s in seat_list if s not in existing]

        if not existing:
            return jsonify({"ok": False, "msg": "Bu koltuklarda kayıtlı yolcu yok"}), 400

        db.executemany(
            """
            UPDATE seats
            SET gender=?
            WHERE trip_id=? AND seat_no=?
            """,
            [(gender, tid, s) for s in existing],
        )
        db.commit()

        return jsonify({
            "ok": True,
            "updated": sorted(existing),
            "missing": missing,
            "gender": gender,
        })

    app.add_url_rule("/seats", endpoint="seats_page", view_func=seats_page, methods=["GET"])
    app.add_url_rule("/yolcu-kontrol", endpoint="passenger_control", view_func=passenger_control, methods=["GET"])
    app.add_url_rule("/api/seats/list", endpoint="api_seats_list", view_func=api_seats_list, methods=["GET"])
    app.add_url_rule("/api/seat", endpoint="api_seat", view_func=api_seat, methods=["POST", "DELETE"])
    app.add_url_rule("/api/seats/bulk", endpoint="api_seats_bulk", view_func=api_seats_bulk, methods=["POST", "DELETE"])
    app.add_url_rule("/api/seats/offload", endpoint="api_seats_offload", view_func=api_seats_offload, methods=["POST"])
    app.add_url_rule("/api/seats/service", endpoint="api_seats_service", view_func=api_seats_service, methods=["POST"])
    app.add_url_rule("/api/seats/gender", endpoint="api_seats_gender", view_func=api_seats_gender, methods=["POST"])
