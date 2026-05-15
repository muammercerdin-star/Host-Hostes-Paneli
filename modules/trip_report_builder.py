import json
from pathlib import Path


def register_trip_report_builder(app, deps):
    get_db = deps["get_db"]
    _row_dict = deps["_row_dict"]
    log_trip_stop_event = deps["log_trip_stop_event"]
    _seat_event_meta = deps["_seat_event_meta"]
    _walkon_event_meta = deps["_walkon_event_meta"]

    def _report_slug(v):
        raw = str(v or "").strip()
        out = []
        for c in raw:
            if c.isalnum() or c in "-_":
                out.append(c)
            else:
                out.append("_")
        return "".join(out).strip("_") or "rapor"


    def build_trip_report_payload_for_trip(db, tid):
        trip = db.execute(
            "SELECT * FROM trips WHERE id=?",
            (tid,),
        ).fetchone()

        rows = db.execute(
            """
            SELECT id, stop_name, event, seats_for_stop, meta_json, ts
            FROM stop_logs
            WHERE trip_id=?
            ORDER BY id ASC
            """,
            (tid,),
        ).fetchall()

        groups = {}
        order = []

        def group_for(stop):
            if stop not in groups:
                groups[stop] = {
                    "stop_name": stop,
                    "board": [],
                    "offload": [],
                    "standing_add": [],
                    "standing_off": [],
                    "parcel_deliver": [],
                    "pass_stop": [],
                    "other": [],
                    "summary": {
                        "board_count": 0,
                        "offload_count": 0,
                        "standing_board_count": 0,
                        "standing_off_count": 0,
                        "parcel_count": 0,
                    },
                }
                order.append(stop)
            return groups[stop]

        for r in rows:
            stop = r["stop_name"] or "—"
            event = r["event"] or "other"

            try:
                meta = json.loads(r["meta_json"]) if r["meta_json"] else {}
            except Exception:
                meta = {}

            item = {
                "id": r["id"],
                "event": event,
                "ts": r["ts"],
                "seats_for_stop": r["seats_for_stop"],
                "meta": meta,
            }

            g = group_for(stop)

            if event == "board":
                g["board"].append(item)
                g["summary"]["board_count"] += 1
            elif event == "offload":
                g["offload"].append(item)
                g["summary"]["offload_count"] += 1
            elif event == "standing_add":
                g["standing_add"].append(item)
                g["summary"]["standing_board_count"] += int(meta.get("pax") or 0)
            elif event == "standing_off":
                g["standing_off"].append(item)
                g["summary"]["standing_off_count"] += int(meta.get("pax") or 0)
            elif event == "parcel_deliver":
                g["parcel_deliver"].append(item)
                g["summary"]["parcel_count"] += int(meta.get("count") or 1)
            elif event == "pass_stop":
                g["pass_stop"].append(item)
            else:
                g["other"].append(item)

        return {
            "ok": True,
            "trip": _row_dict(trip),
            "stops": [groups[x] for x in order],
        }


    def finalize_remaining_trip_events(db, tid):
        """
        Sefer bitirilirken hâlâ koltukta görünen yolcu varsa,
        rapor eksik kalmasın diye final iniş kaydı atar.
        """
        seat_rows = db.execute(
            "SELECT * FROM seats WHERE trip_id=? ORDER BY seat_no",
            (tid,),
        ).fetchall()

        for r in seat_rows:
            to_stop = (r["to_stop"] or "").strip()
            if not to_stop:
                continue

            log_trip_stop_event(
                db,
                tid,
                to_stop,
                "offload",
                _seat_event_meta(r, {"action": "final_trip_offload"}),
            )

        walk_rows = db.execute(
            "SELECT * FROM walk_on_sales WHERE trip_id=? ORDER BY id",
            (tid,),
        ).fetchall()

        for r in walk_rows:
            to_stop = (r["to_stop"] or "").strip()
            if not to_stop:
                continue

            log_trip_stop_event(
                db,
                tid,
                to_stop,
                "standing_off",
                _walkon_event_meta(r, {"action": "final_trip_standing_offload"}),
            )


    def trip_report_text(payload):
        trip = payload.get("trip") or {}
        lines = []

        lines.append("SEFER RAPORU")
        lines.append("=" * 34)
        lines.append(f"Hat: {trip.get('route') or '-'}")
        lines.append(f"Plaka: {trip.get('plate') or '-'}")
        lines.append(f"Tarih: {trip.get('date') or '-'}")
        lines.append(f"Çıkış: {trip.get('departure_time') or '-'}")
        lines.append("")

        total_board = 0
        total_off = 0
        total_stand_board = 0
        total_stand_off = 0

        for stop in payload.get("stops") or []:
            sm = stop.get("summary") or {}
            total_board += int(sm.get("board_count") or 0)
            total_off += int(sm.get("offload_count") or 0)
            total_stand_board += int(sm.get("standing_board_count") or 0)
            total_stand_off += int(sm.get("standing_off_count") or 0)

        lines.append(f"Toplam Binen: {total_board}")
        lines.append(f"Toplam İnen: {total_off}")
        lines.append(f"Ayakta Binen: {total_stand_board}")
        lines.append(f"Ayakta İnen: {total_stand_off}")
        lines.append("")

        for stop in payload.get("stops") or []:
            sm = stop.get("summary") or {}

            lines.append(f"Durak: {stop.get('stop_name')}")
            lines.append("-" * 34)
            lines.append(
                f"Binen {sm.get('board_count') or 0} | "
                f"İnen {sm.get('offload_count') or 0} | "
                f"Ayakta binen {sm.get('standing_board_count') or 0} | "
                f"Ayakta inen {sm.get('standing_off_count') or 0}"
            )

            if stop.get("board"):
                lines.append("Binenler:")
                for it in stop.get("board") or []:
                    m = it.get("meta") or {}
                    lines.append(
                        f"  + Koltuk {m.get('seat_no') or '-'} | "
                        f"{m.get('from_stop') or '-'} -> {m.get('to_stop') or '-'} | "
                        f"{m.get('gender') or '-'} | {m.get('payment') or '-'} | "
                        f"{it.get('ts') or '-'}"
                    )

            if stop.get("offload"):
                lines.append("İnenler:")
                for it in stop.get("offload") or []:
                    m = it.get("meta") or {}
                    lines.append(
                        f"  - Koltuk {m.get('seat_no') or '-'} | "
                        f"{m.get('from_stop') or '-'} -> {m.get('to_stop') or '-'} | "
                        f"{m.get('gender') or '-'} | {m.get('payment') or '-'} | "
                        f"{it.get('ts') or '-'}"
                    )

            if stop.get("standing_add"):
                lines.append("Ayakta Binen:")
                for it in stop.get("standing_add") or []:
                    m = it.get("meta") or {}
                    lines.append(
                        f"  + {m.get('pax') or 0} kişi | "
                        f"{m.get('from_stop') or '-'} -> {m.get('to_stop') or '-'} | "
                        f"{m.get('payment') or '-'} | {it.get('ts') or '-'}"
                    )

            if stop.get("standing_off"):
                lines.append("Ayakta İnen:")
                for it in stop.get("standing_off") or []:
                    m = it.get("meta") or {}
                    lines.append(
                        f"  - {m.get('pax') or 0} kişi | "
                        f"{m.get('from_stop') or '-'} -> {m.get('to_stop') or '-'} | "
                        f"{m.get('payment') or '-'} | {it.get('ts') or '-'}"
                    )

            lines.append("")

        return "\n".join(lines)


    def trip_report_csv(payload):
        rows = [
            ["durak", "islem", "koltuk", "kisi", "nereden", "nereye", "cinsiyet", "odeme", "tutar", "zaman"]
        ]

        def add(stop_name, label, items):
            for it in items or []:
                m = it.get("meta") or {}
                rows.append([
                    stop_name,
                    label,
                    m.get("seat_no") or "",
                    m.get("pax") or "",
                    m.get("from_stop") or "",
                    m.get("to_stop") or "",
                    m.get("gender") or "",
                    m.get("payment") or "",
                    m.get("amount") or m.get("total_amount") or "",
                    it.get("ts") or "",
                ])

        for stop in payload.get("stops") or []:
            name = stop.get("stop_name") or ""
            add(name, "bindi", stop.get("board"))
            add(name, "indi", stop.get("offload"))
            add(name, "ayakta_bindi", stop.get("standing_add"))
            add(name, "ayakta_indi", stop.get("standing_off"))

        out = []
        for r in rows:
            out.append(",".join('"' + str(v).replace('"', '""') + '"' for v in r))

        return "\ufeff" + "\n".join(out)


    def save_finished_trip_report(tid):
        db = get_db()

        trip = db.execute(
            "SELECT * FROM trips WHERE id=?",
            (tid,),
        ).fetchone()

        if not trip:
            return {}

        reports_dir = Path(app.root_path) / "storage" / "reports"
        reports_dir.mkdir(parents=True, exist_ok=True)

        base = "sefer_{id}_{date}_{plate}".format(
            id=trip["id"],
            date=_report_slug(trip["date"]),
            plate=_report_slug(trip["plate"]),
        )

        payload = build_trip_report_payload_for_trip(db, tid)

        json_path = reports_dir / f"{base}.json"
        txt_path = reports_dir / f"{base}.txt"
        csv_path = reports_dir / f"{base}.csv"

        json_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
        txt_path.write_text(trip_report_text(payload), encoding="utf-8")
        csv_path.write_text(trip_report_csv(payload), encoding="utf-8-sig")

        return {
            "json": str(json_path),
            "txt": str(txt_path),
            "csv": str(csv_path),
            "base": base,
        }

    return {
        "_report_slug": _report_slug,
        "build_trip_report_payload_for_trip": build_trip_report_payload_for_trip,
        "finalize_remaining_trip_events": finalize_remaining_trip_events,
        "trip_report_text": trip_report_text,
        "trip_report_csv": trip_report_csv,
        "save_finished_trip_report": save_finished_trip_report,
    }
