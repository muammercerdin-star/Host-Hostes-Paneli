import csv
from io import StringIO

from flask import render_template, request, redirect, url_for, make_response


def register_cash_routes(app, deps):
    get_active_trip = deps["get_active_trip"]
    get_db = deps["get_db"]
    get_cash_categories = deps["get_cash_categories"]
    save_cash_categories = deps["save_cash_categories"]
    parse_int = deps["parse_int"]
    get_csrf = deps["get_csrf"]

    def cash_sums(trip_id: int):
        db = get_db()

        r_in = db.execute(
            "SELECT COALESCE(SUM(amount),0) FROM cash_moves WHERE trip_id=? AND direction='+'",
            (trip_id,),
        ).fetchone()

        r_out = db.execute(
            "SELECT COALESCE(SUM(amount),0) FROM cash_moves WHERE trip_id=? AND direction='-'",
            (trip_id,),
        ).fetchone()

        r_dev = db.execute(
            "SELECT COALESCE(SUM(amount),0) FROM cash_moves WHERE trip_id=? AND direction='+' AND lower(category)='devir'",
            (trip_id,),
        ).fetchone()

        total_in = int(r_in[0] or 0)
        total_out = int(r_out[0] or 0)
        devir = int(r_dev[0] or 0)

        return {
            "devir": devir,
            "giris": total_in - devir,
            "cikis": total_out,
            "kalan": total_in - total_out,
        }

    def hesap_page():
        tid = get_active_trip()

        if not tid:
            return render_template(
                "no_active_trip.html",
                title="Hesap",
                message="Hesap ekranını açmak için önce aktif bir sefer başlatmalısın.",
                action_text="Yeni Sefer Başlat",
                action_url=url_for("trip_start"),
                home_url=url_for("index"),
            )

        db = get_db()
        trip_row = db.execute("SELECT * FROM trips WHERE id=?", (tid,)).fetchone()
        trip = dict(trip_row) if trip_row else {}
        sums = dict(cash_sums(tid))

        moves = [
            dict(r) for r in db.execute(
                """
                SELECT id, created_at, direction, category, amount, COALESCE(note,'') AS note
                FROM cash_moves
                WHERE trip_id=?
                ORDER BY id DESC
                LIMIT 100
                """,
                (tid,),
            ).fetchall()
        ]

        cats_in, cats_out = get_cash_categories()

        return render_template(
            "hesap.html",
            trip=trip,
            sums=sums,
            moves=moves,
            categories_in=cats_in,
            categories_out=cats_out,
            csrf_token=get_csrf(),
        )

    def hesap_devir():
        tid = get_active_trip()
        if not tid:
            return redirect(url_for("trip_start"))

        amount = parse_int(request.form.get("amount"), 0)
        note = (request.form.get("note") or "").strip()

        if amount and amount > 0:
            db = get_db()
            db.execute(
                "INSERT INTO cash_moves(trip_id, direction, category, amount, note) VALUES(?,?,?,?,?)",
                (tid, "+", "Devir", amount, note),
            )
            db.commit()

        return redirect(url_for("hesap_page"))

    def hesap_giris():
        tid = get_active_trip()
        if not tid:
            return redirect(url_for("trip_start"))

        amount = parse_int(request.form.get("amount"), 0)
        category = (request.form.get("category") or "Diğer").strip()
        note = (request.form.get("note") or "").strip()

        if amount and amount > 0:
            db = get_db()
            db.execute(
                "INSERT INTO cash_moves(trip_id, direction, category, amount, note) VALUES(?,?,?,?,?)",
                (tid, "+", category, amount, note),
            )
            db.commit()

        return redirect(url_for("hesap_page"))

    def hesap_cikis():
        tid = get_active_trip()
        if not tid:
            return redirect(url_for("trip_start"))

        amount = parse_int(request.form.get("amount"), 0)
        category = (request.form.get("category") or "Diğer").strip()
        note = (request.form.get("note") or "").strip()

        if amount and amount > 0:
            db = get_db()
            db.execute(
                "INSERT INTO cash_moves(trip_id, direction, category, amount, note) VALUES(?,?,?,?,?)",
                (tid, "-", category, amount, note),
            )
            db.commit()

        return redirect(url_for("hesap_page"))

    def hesap_kategoriler_kaydet():
        save_cash_categories(
            request.form.get("cats_in") or "",
            request.form.get("cats_out") or "",
        )
        return redirect(url_for("hesap_page"))

    def hesap_moves_csv():
        tid = get_active_trip()
        if not tid:
            return redirect(url_for("trip_start"))

        rows = [
            dict(r) for r in get_db().execute(
                """
                SELECT created_at, direction, category, note, amount
                FROM cash_moves
                WHERE trip_id=?
                ORDER BY id DESC
                """,
                (tid,),
            ).fetchall()
        ]

        buf = StringIO()
        writer = csv.writer(buf)
        writer.writerow(["Zaman", "Yön", "Kategori", "Açıklama", "Tutar (TL)"])

        for r in rows:
            writer.writerow([
                r.get("created_at", ""),
                "+" if r.get("direction") == "+" else "-",
                r.get("category", ""),
                r.get("note", ""),
                r.get("amount", 0),
            ])

        out = buf.getvalue().encode("utf-8-sig")
        resp = make_response(out)
        resp.headers["Content-Type"] = "text/csv; charset=utf-8"
        resp.headers["Content-Disposition"] = 'attachment; filename="son_hareketler.csv"'
        return resp

    app.add_url_rule("/hesap", endpoint="hesap_page", view_func=hesap_page, methods=["GET"])
    app.add_url_rule("/hesap/devir", endpoint="hesap_devir", view_func=hesap_devir, methods=["POST"])
    app.add_url_rule("/hesap/giris", endpoint="hesap_giris", view_func=hesap_giris, methods=["POST"])
    app.add_url_rule("/hesap/cikis", endpoint="hesap_cikis", view_func=hesap_cikis, methods=["POST"])
    app.add_url_rule("/hesap/kategoriler", endpoint="hesap_kategoriler_kaydet", view_func=hesap_kategoriler_kaydet, methods=["POST"])
    app.add_url_rule("/hesap/moves.csv", endpoint="hesap_moves_csv", view_func=hesap_moves_csv, methods=["GET"])

    # İleride başka modüller cash_sums kullanmak isterse diye app'e bağla.
    app.cash_sums = cash_sums
