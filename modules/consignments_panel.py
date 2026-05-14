import secrets
from pathlib import Path
from datetime import datetime

from flask import (
    render_template,
    request,
    redirect,
    url_for,
    jsonify,
    send_from_directory,
)
from werkzeug.utils import secure_filename


def register_consignments_routes(app, deps):
    get_active_trip = deps["get_active_trip"]
    get_db = deps["get_db"]
    get_stops = deps["get_stops"]
    validate_stop_for_active_trip = deps["validate_stop_for_active_trip"]
    norm_payment = deps["norm_payment"]
    parse_float = deps["parse_float"]
    allowed_file = deps["allowed_file"]
    ensure_upload_dir = deps["ensure_upload_dir"]
    UPLOAD_DIR = deps["UPLOAD_DIR"]
    ALLOWED_IMAGE_MIMES = deps["ALLOWED_IMAGE_MIMES"]

    def consignments_page():
        tid = get_active_trip()
        if not tid:
            return redirect(url_for("trip_start"))

        db = get_db()
        trip = db.execute("SELECT * FROM trips WHERE id=?", (tid,)).fetchone()
        rows = db.execute(
            "SELECT * FROM consignments WHERE trip_id=? ORDER BY created_at DESC",
            (tid,),
        ).fetchall()

        return render_template(
            "consignments.html",
            trip=trip,
            stops=get_stops(trip["route"]),
            items=[dict(r) for r in rows],
        )

    def api_consignments():
        tid = get_active_trip()
        if not tid:
            return jsonify({"ok": False, "msg": "Aktif sefer yok"}), 400

        db = get_db()

        if request.method == "GET":
            rows = db.execute(
                "SELECT * FROM consignments WHERE trip_id=? ORDER BY created_at DESC",
                (tid,),
            ).fetchall()
            return jsonify({"ok": True, "items": [dict(r) for r in rows]})

        data = request.get_json(force=True) or {}

        code = (data.get("code") or "").strip() or secrets.token_hex(3).upper()
        item_name = (data.get("item_name") or "").strip()
        item_type = (data.get("item_type") or "").strip()
        from_name = (data.get("from_name") or "").strip()
        from_phone = (data.get("from_phone") or "").strip()
        to_name = (data.get("to_name") or "").strip()
        to_phone = (data.get("to_phone") or "").strip()
        from_stop = (data.get("from_stop") or "").strip()
        to_stop = (data.get("to_stop") or "").strip()
        payment = norm_payment(data.get("payment"))
        amount = parse_float(data.get("amount"), 0.0) or 0.0

        if not item_name:
            return jsonify({"ok": False, "msg": "Eşya adı gerekli"}), 400

        if from_stop and not validate_stop_for_active_trip(from_stop):
            return jsonify({"ok": False, "msg": f"Durak hat üzerinde değil: {from_stop}"}), 400

        if to_stop and not validate_stop_for_active_trip(to_stop):
            return jsonify({"ok": False, "msg": f"Durak hat üzerinde değil: {to_stop}"}), 400

        db.execute(
            """
            INSERT INTO consignments(
                trip_id, code, item_name, item_type, from_name, from_phone,
                to_name, to_phone, from_stop, to_stop, amount, payment, status
            )
            VALUES(?,?,?,?,?,?,?,?,?,?,?,?, 'bekliyor')
            """,
            (
                tid, code, item_name, item_type, from_name, from_phone,
                to_name, to_phone, from_stop, to_stop, amount, payment,
            ),
        )
        db.commit()

        new_id = db.execute("SELECT last_insert_rowid()").fetchone()[0]
        return jsonify({"ok": True, "id": new_id, "code": code})

    def api_parcels():
        tid = get_active_trip()
        if not tid:
            return jsonify({"ok": False, "msg": "Aktif sefer yok", "items": []}), 400

        status = (request.args.get("status") or "bekliyor").strip().lower()

        rows = get_db().execute(
            """
            SELECT COALESCE(to_stop,'') AS to_stop, COUNT(*) AS cnt
            FROM consignments
            WHERE trip_id=? AND status=?
            GROUP BY to_stop
            """,
            (tid, status),
        ).fetchall()

        items = [{"to": r["to_stop"], "count": int(r["cnt"])} for r in rows if r["to_stop"]]
        return jsonify({"ok": True, "items": items})

    def api_consignment_photos(cid):
        tid = get_active_trip()
        if not tid:
            return jsonify({"ok": False, "msg": "Aktif sefer yok"}), 400

        db = get_db()

        if request.method == "GET":
            rows = db.execute(
                """
                SELECT id, role, file_path, mime, size_bytes, created_at
                FROM consignment_photos
                WHERE consignment_id=?
                ORDER BY id DESC
                """,
                (cid,),
            ).fetchall()

            items = [{
                "id": r["id"],
                "role": r["role"],
                "file": r["file_path"],
                "mime": r["mime"],
                "size": r["size_bytes"],
                "created_at": r["created_at"],
                "url": url_for("serve_uploaded", filename=r["file_path"]),
            } for r in rows]

            return jsonify({"ok": True, "items": items})

        role = (request.form.get("role") or "").strip().lower()
        file = request.files.get("file")

        if not file or not file.filename:
            return jsonify({"ok": False, "msg": "Dosya gerekli"}), 400

        if not allowed_file(file.filename):
            return jsonify({"ok": False, "msg": "İzin verilmeyen dosya türü"}), 400

        if file.mimetype not in ALLOWED_IMAGE_MIMES:
            return jsonify({"ok": False, "msg": "Desteklenmeyen MIME"}), 400

        row = db.execute("SELECT id FROM consignments WHERE id=? AND trip_id=?", (cid, tid)).fetchone()
        if not row:
            return jsonify({"ok": False, "msg": "Emanet bulunamadı"}), 404

        ext = file.filename.rsplit(".", 1)[1].lower()
        rid = secrets.token_hex(3)
        fname = secure_filename(f"c{cid}_{int(datetime.now().timestamp())}_{rid}.{ext}")

        ensure_upload_dir()
        save_path = Path(UPLOAD_DIR) / fname
        file.save(save_path)
        size_bytes = save_path.stat().st_size

        db.execute(
            """
            INSERT INTO consignment_photos(consignment_id, role, file_path, mime, size_bytes)
            VALUES(?,?,?,?,?)
            """,
            (cid, role, fname, file.mimetype, size_bytes),
        )
        db.commit()

        return jsonify({
            "ok": True,
            "url": url_for("serve_uploaded", filename=fname),
            "file": fname,
            "size": size_bytes,
        })

    def api_consignment_delete(cid):
        tid = get_active_trip()
        if not tid:
            return jsonify({"ok": False, "msg": "Aktif sefer yok"}), 400

        db = get_db()
        photos = db.execute("SELECT file_path FROM consignment_photos WHERE consignment_id=?", (cid,)).fetchall()

        for r in photos:
            try:
                (Path(UPLOAD_DIR) / r["file_path"]).unlink(missing_ok=True)
            except Exception:
                pass

        db.execute("DELETE FROM consignment_photos WHERE consignment_id=?", (cid,))
        db.execute("DELETE FROM consignments WHERE id=? AND trip_id=?", (cid, tid))
        db.commit()

        return jsonify({"ok": True})

    def serve_uploaded(filename):
        safe_name = secure_filename(filename)
        return send_from_directory(UPLOAD_DIR, safe_name, as_attachment=False)

    app.add_url_rule("/emanetler", endpoint="consignments_page", view_func=consignments_page, methods=["GET"])
    app.add_url_rule("/api/consignments", endpoint="api_consignments", view_func=api_consignments, methods=["GET", "POST"])
    app.add_url_rule("/api/parcels", endpoint="api_parcels", view_func=api_parcels, methods=["GET"])
    app.add_url_rule("/api/consignments/<int:cid>/photos", endpoint="api_consignment_photos", view_func=api_consignment_photos, methods=["GET", "POST"])
    app.add_url_rule("/api/consignments/<int:cid>", endpoint="api_consignment_delete", view_func=api_consignment_delete, methods=["DELETE"])
    app.add_url_rule("/u/<path:filename>", endpoint="serve_uploaded", view_func=serve_uploaded, methods=["GET"])
