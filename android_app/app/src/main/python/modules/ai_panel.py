import re
import sqlite3
import shutil
from typing import Optional

from flask import request, jsonify, url_for


def register_ai_routes(app, deps):
    get_db = deps["get_db"]
    get_active_trip_row = deps["get_active_trip_row"]
    get_stops = deps["get_stops"]
    parse_int = deps["parse_int"]
    parse_float = deps["parse_float"]
    norm_payment = deps["norm_payment"]
    norm_ticket_type = deps["norm_ticket_type"]
    norm_gender = deps["norm_gender"]
    validate_seat_no = deps["validate_seat_no"]
    validate_stop_for_active_trip = deps["validate_stop_for_active_trip"]
    neighbor_rule_ok = deps["neighbor_rule_ok"]
    delete_walkon_rows = deps["delete_walkon_rows"]
    fetch_live_runtime_state = deps["fetch_live_runtime_state"]
    bag_root = deps["bag_root"]
    safe = deps["safe"]

    normalize_ai_text = deps["normalize_ai_text"]
    ai_extract_seat_list = deps["ai_extract_seat_list"]
    ai_make_skeleton = deps["ai_make_skeleton"]
    ai_find_learned_match = deps["ai_find_learned_match"]

    def _trip_key_from_row(trip_row) -> str:
        if not trip_row:
            return ""
        try:
            return ((trip_row["route"] or "") + "|" + (trip_row["plate"] or "")).replace(" ", "_")
        except Exception:
            return ""

    def clear_bags_for_seat(trip_key: str, seat_no) -> int:
        if not trip_key or seat_no is None:
            return 0

        deleted = 0

        try:
            d = bag_root() / safe(trip_key) / safe(str(seat_no))
            if not (d.exists() and d.is_dir()):
                return 0

            for fp in d.rglob("*"):
                try:
                    if fp.is_file():
                        deleted += 1
                except Exception:
                    pass

            shutil.rmtree(d, ignore_errors=True)
        except Exception:
            return deleted

        return deleted

    # =========================================================
    # AI Console v2 Intent Tanımları
    # =========================================================

    AI_INTENTS = {
        "seat_add_single": {
            "title": "Tek koltuk ekleme",
            "pattern": "seat + add",
            "description": "Tek koltuğa yolcu ekler",
            "examples": [
                "12 numaraya yolcu ekle",
                "11 i salihliye yaz",
                "9 numarayı manisaya bindir",
            ],
        },
        "seat_add_group": {
            "title": "Çoklu koltuk ekleme",
            "pattern": "seat_list + add",
            "description": "Birden fazla koltuğa toplu yolcu ekler",
            "examples": [
                "12 13 14 salihliye yaz",
                "7-8 numaraya yolcu ekle",
                "3,4,5 i manisaya bindir",
            ],
        },
        "seat_remove_single": {
            "title": "Tek koltuk boşaltma",
            "pattern": "seat + offload",
            "description": "Tek koltuğu boşaltır",
            "examples": [
                "12 numarayı boşalt",
                "7 insin",
            ],
        },
        "seat_remove_group": {
            "title": "Çoklu koltuk boşaltma",
            "pattern": "seat_list + offload",
            "description": "Birden fazla koltuğu boşaltır",
            "examples": [
                "7-8 numarayı boşalt",
                "7 ve 8 insin",
                "12 13 14 indir",
            ],
        },
        "standing_add": {
            "title": "Ayakta ekleme",
            "pattern": "standing + add",
            "description": "Ayakta yolcu kaydı ekler",
            "examples": [
                "ayakta 3 yaz",
                "3 ayakta manisaya",
                "2 kişi ayakta ekle",
            ],
        },
        "standing_remove": {
            "title": "Ayakta indirme",
            "pattern": "standing + offload",
            "description": "Ayakta yolcu kaydını siler",
            "examples": [
                "ayakta manisada indir",
                "manisa ayaktaları sil",
            ],
        },
        "service_mark": {
            "title": "Servis işaretleme",
            "pattern": "seat_list + service_on",
            "description": "Koltuklara servis verildi olarak işaret koyar",
            "examples": [
                "12 numara servis tamam",
                "7 8 servis verildi",
            ],
        },
        "service_unmark": {
            "title": "Servis kaldırma",
            "pattern": "seat_list + service_off",
            "description": "Koltuklardan servis işaretini kaldırır",
            "examples": [
                "12 numara servisi kaldır",
                "7 8 servis iptal",
            ],
        },
        "stop_select": {
            "title": "Durak seçme",
            "pattern": "stop + select",
            "description": "Canlı seçim için durağı hedefler",
            "examples": [
                "sıradaki durak alaşehir otogar",
                "durak seç salihli garaj",
            ],
        },
        "stop_offload": {
            "title": "Durak bazlı indirme",
            "pattern": "stop + offload",
            "description": "Seçilen durak için koltuk ve ayakta kayıtlarını indirir",
            "examples": [
                "manisada indir",
                "salihli garaj için iniş yap",
            ],
        },
        "query_total_passengers": {
            "title": "Toplam yolcu sorgu",
            "pattern": "query + total_passengers",
            "description": "Toplam yolcu sayısını verir",
            "examples": [
                "kaç yolcu var",
                "toplam yolcu kaç",
            ],
        },
        "query_standing_count": {
            "title": "Ayakta yolcu sorgu",
            "pattern": "query + standing",
            "description": "Ayakta yolcu sayısını verir",
            "examples": [
                "ayakta kaç kişi var",
                "kaç ayakta var",
            ],
        },
        "query_live_stop": {
            "title": "Canlı durak sorgu",
            "pattern": "query + live_stop",
            "description": "Sistemde bilinen son durağı söyler",
            "examples": [
                "hangi duraktayız",
                "neredeyiz",
            ],
        },
        "query_next_stop": {
            "title": "Sıradaki durak sorgu",
            "pattern": "query + next_stop",
            "description": "Sıradaki durağı söyler",
            "examples": [
                "bir sonraki durak ne",
                "sıradaki durak hangisi",
            ],
        },
        "query_delay": {
            "title": "Rötar sorgu",
            "pattern": "query + delay",
            "description": "Rötar durumu hakkında cevap verir",
            "examples": [
                "rötar kaç",
                "gecikme var mı",
            ],
        },
        "open_hesap": {
            "title": "Hesap sayfasını aç",
            "pattern": "nav + hesap",
            "description": "Hesap ekranına yönlendirir",
            "examples": [
                "hesap aç",
            ],
        },
        "open_emanet": {
            "title": "Emanet sayfasını aç",
            "pattern": "nav + emanet",
            "description": "Emanet ekranına yönlendirir",
            "examples": [
                "emanet aç",
                "emanetler aç",
            ],
        },
    }


    # =========================================================
    # AI yardımcıları v2
    # =========================================================

    def ai_intent_title(intent: str) -> str:
        return AI_INTENTS.get(intent, {}).get("title", intent or "")


    def ai_intent_pattern(intent: str) -> str:
        return AI_INTENTS.get(intent, {}).get("pattern", "")


    def ai_extract_stop_mentions(command: str, route_stops: list[str]) -> list[str]:
        cmd_norm = normalize_ai_text(command)
        hits = []

        for stop in route_stops:
            stop_norm = normalize_ai_text(stop)
            if not stop_norm:
                continue
            pos = cmd_norm.find(stop_norm)
            if pos >= 0:
                hits.append((pos, -len(stop_norm), stop))

        hits.sort(key=lambda x: (x[0], x[1]))

        ordered = []
        seen = set()
        for _, _, stop in hits:
            ns = normalize_ai_text(stop)
            if ns not in seen:
                ordered.append(stop)
                seen.add(ns)

        return ordered


    def ai_extract_payment(command: str) -> str:
        text = normalize_ai_text(command)
        if "iban" in text:
            return "iban"
        if "online" in text:
            return "online"
        if "pos" in text:
            return "pos"
        if "ucretsiz" in text or "ücretsiz" in command.lower():
            return "ucretsiz"
        if "nakit" in text:
            return "nakit"
        return ""


    def ai_extract_gender(command: str) -> str:
        text = normalize_ai_text(command)
        if re.search(r"\b(bayan|kadin|kadın)\b", text):
            return "bayan"
        if re.search(r"\b(bay|erkek)\b", text):
            return "bay"
        return ""


    def ai_extract_amount(command: str) -> Optional[float]:
        text = normalize_ai_text(command)
        m = re.search(r"(\d+(?:[.,]\d+)?)\s*(tl|lira)\b", text)
        if not m:
            return None
        raw = m.group(1).replace(",", ".")
        try:
            return float(raw)
        except Exception:
            return None


    def ai_extract_count(command: str, seats: list[int]) -> Optional[int]:
        text = normalize_ai_text(command)
        nums = [int(x) for x in re.findall(r"\b\d{1,3}\b", text)]

        if "ayakta" in text:
            has_seat_words = bool(re.search(r"\b(numara|koltuk)\b", text))
            if nums and not has_seat_words:
                return nums[0]

        if nums and not seats:
            return nums[0]

        return None


    def ai_extract_entities(command: str, trip_row=None) -> dict:
        text = normalize_ai_text(command)
        seats = ai_extract_seat_list(command)

        if "ayakta" in text and seats and not re.search(r"\b(numara|koltuk)\b", text):
            count_guess = seats[0]
            seats = []
        else:
            count_guess = None

        route_stops = get_stops(trip_row["route"]) if trip_row else []
        stop_hits = ai_extract_stop_mentions(command, route_stops)

        from_stop = ""
        to_stop = ""
        stop_name = ""

        if len(stop_hits) >= 2:
            from_stop = stop_hits[0]
            to_stop = stop_hits[-1]
            stop_name = stop_hits[-1]
        elif len(stop_hits) == 1:
            to_stop = stop_hits[0]
            stop_name = stop_hits[0]

        entities = {
            "seats": seats,
            "count": count_guess or ai_extract_count(command, seats),
            "from_stop": from_stop,
            "to_stop": to_stop,
            "stop_name": stop_name,
            "payment": ai_extract_payment(command),
            "amount": ai_extract_amount(command),
            "ticket_type": "ucretsiz" if ("ucretsiz" in text or "ücretsiz" in command.lower()) else "",
            "gender": ai_extract_gender(command),
            "pair_ok": bool(re.search(r"\b(istisna|izinli|yan yana olur)\b", text)),
            "service": bool(re.search(r"\b(servis|ikram)\b", text)),
            "service_clear": bool(re.search(r"\b(servisi kaldir|servisi kaldır|servis iptal|servis yok)\b", text)),
            "note": "",
        }

        return entities


    def ai_parse_default_command(command: str, entities: dict):
        text = normalize_ai_text(command)
        seats = entities.get("seats") or []

        has_add = bool(re.search(r"\b(ekle|yaz|kaydet|oturt|bindir)\b", text))
        has_offload = bool(re.search(r"\b(bosalt|boşalt|indir|insin|sil)\b", text))
        has_standing = "ayakta" in text
        has_service = bool(re.search(r"\b(servis|ikram)\b", text))
        has_query = bool(re.search(r"\b(kac|kaç|hangi|nerede|toplam|siradaki|sıradaki|rotar|rötar|gecikme)\b", text))

        if re.search(r"\b(hesap ac|hesap aç)\b", text):
            return {"intent": "open_hesap", "pattern": ai_intent_pattern("open_hesap"), "confidence": 0.99}

        if re.search(r"\b(emanet ac|emanet aç|emanetler ac|emanetler aç)\b", text):
            return {"intent": "open_emanet", "pattern": ai_intent_pattern("open_emanet"), "confidence": 0.99}

        if re.search(r"\b(hangi duraktayiz|hangi duraktayız|neredeyiz)\b", text):
            return {"intent": "query_live_stop", "pattern": ai_intent_pattern("query_live_stop"), "confidence": 0.93}

        if re.search(r"\b(ayakta kac|ayakta kaç|kac ayakta|kaç ayakta)\b", text):
            return {"intent": "query_standing_count", "pattern": ai_intent_pattern("query_standing_count"), "confidence": 0.93}

        if re.search(r"\b(toplam yolcu|kac yolcu var|kaç yolcu var)\b", text):
            return {"intent": "query_total_passengers", "pattern": ai_intent_pattern("query_total_passengers"), "confidence": 0.93}

        if re.search(r"\b(bir sonraki durak|siradaki durak|sıradaki durak)\b", text):
            return {"intent": "query_next_stop", "pattern": ai_intent_pattern("query_next_stop"), "confidence": 0.91}

        if re.search(r"\b(rotar|rötar|gecikme)\b", text):
            return {"intent": "query_delay", "pattern": ai_intent_pattern("query_delay"), "confidence": 0.88}

        if has_standing and has_offload and entities.get("to_stop"):
            return {"intent": "standing_remove", "pattern": ai_intent_pattern("standing_remove"), "confidence": 0.90}

        if has_standing and (has_add or entities.get("count")):
            return {"intent": "standing_add", "pattern": ai_intent_pattern("standing_add"), "confidence": 0.87}

        if entities.get("service_clear") and seats:
            return {"intent": "service_unmark", "pattern": ai_intent_pattern("service_unmark"), "confidence": 0.84}

        if has_service and seats:
            return {"intent": "service_mark", "pattern": ai_intent_pattern("service_mark"), "confidence": 0.86}

        if has_offload and entities.get("to_stop") and not seats:
            return {"intent": "stop_offload", "pattern": ai_intent_pattern("stop_offload"), "confidence": 0.70}

        if re.search(r"\b(durak sec|durak seç|siradaki durak|sıradaki durak)\b", text) and entities.get("stop_name"):
            return {"intent": "stop_select", "pattern": ai_intent_pattern("stop_select"), "confidence": 0.78}

        if has_offload and len(seats) >= 2:
            return {"intent": "seat_remove_group", "pattern": ai_intent_pattern("seat_remove_group"), "confidence": 0.86}

        if has_offload and len(seats) == 1:
            return {"intent": "seat_remove_single", "pattern": ai_intent_pattern("seat_remove_single"), "confidence": 0.84}

        if has_add and len(seats) >= 2:
            return {"intent": "seat_add_group", "pattern": ai_intent_pattern("seat_add_group"), "confidence": 0.82}

        if has_add and len(seats) == 1:
            return {"intent": "seat_add_single", "pattern": ai_intent_pattern("seat_add_single"), "confidence": 0.81}

        if has_query:
            return {"intent": "query_total_passengers", "pattern": ai_intent_pattern("query_total_passengers"), "confidence": 0.42}

        return {"intent": None, "pattern": None, "confidence": 0.10}


    def ai_required_fields(intent: str, entities: dict) -> list[str]:
        seats = entities.get("seats") or []
        count = entities.get("count")
        to_stop = (entities.get("to_stop") or "").strip()
        stop_name = (entities.get("stop_name") or "").strip()

        missing = []

        if intent == "seat_add_single":
            if len(seats) != 1:
                missing.append("seats")
            if not to_stop:
                missing.append("to_stop")

        elif intent == "seat_add_group":
            if not seats:
                missing.append("seats")
            if not to_stop:
                missing.append("to_stop")

        elif intent == "seat_remove_single":
            if len(seats) != 1:
                missing.append("seats")

        elif intent == "seat_remove_group":
            if not seats:
                missing.append("seats")

        elif intent == "standing_add":
            if not count:
                missing.append("count")
            if not to_stop:
                missing.append("to_stop")

        elif intent == "standing_remove":
            if not to_stop:
                missing.append("to_stop")

        elif intent in {"service_mark", "service_unmark"}:
            if not seats:
                missing.append("seats")

        elif intent in {"stop_select", "stop_offload"}:
            if not stop_name and not to_stop:
                missing.append("stop_name")

        return missing


    def ai_preview_text(intent: str, entities: dict) -> str:
        seats = entities.get("seats") or []
        to_stop = entities.get("to_stop") or entities.get("stop_name") or ""
        from_stop = entities.get("from_stop") or ""
        count = entities.get("count")

        if intent == "seat_add_single":
            return f"{seats[0] if seats else '-'} numaralı koltuğa yolcu eklenecek. Hedef: {to_stop or '-'}."

        if intent == "seat_add_group":
            return f"{', '.join(map(str, seats)) if seats else '-'} koltuklarına toplu kayıt yapılacak. Hedef: {to_stop or '-'}."

        if intent == "seat_remove_single":
            return f"{seats[0] if seats else '-'} numaralı koltuk boşaltılacak."

        if intent == "seat_remove_group":
            return f"{', '.join(map(str, seats)) if seats else '-'} koltukları boşaltılacak."

        if intent == "standing_add":
            return f"{count or '-'} ayakta yolcu kaydı eklenecek. {from_stop + ' → ' if from_stop else ''}{to_stop or '-'}"

        if intent == "standing_remove":
            return f"{to_stop or '-'} durağı için ayakta kayıtları indirilecek."

        if intent == "service_mark":
            return f"{', '.join(map(str, seats)) if seats else '-'} koltukları servis verildi olarak işaretlenecek."

        if intent == "service_unmark":
            return f"{', '.join(map(str, seats)) if seats else '-'} koltuklarından servis işareti kaldırılacak."

        if intent == "stop_select":
            return f"Hedef durak olarak {to_stop or '-'} seçilecek."

        if intent == "stop_offload":
            return f"{to_stop or '-'} durağı için toplu iniş uygulanacak."

        if intent.startswith("query_"):
            return f"{ai_intent_title(intent)} çalıştırılacak."

        if intent.startswith("open_"):
            return f"{ai_intent_title(intent)} çalıştırılacak."

        return "Komut çözüldü."


    def resolve_ai_command(command: str):
        trip = get_active_trip_row()
        entities = ai_extract_entities(command, trip)

        learned, match_type = ai_find_learned_match(command)
        if learned:
            intent = learned["intent"]
            missing = ai_required_fields(intent, entities)
            return {
                "status": "matched",
                "source": f"learned_{match_type}",
                "intent": intent,
                "title": ai_intent_title(intent),
                "pattern": learned.get("pattern") or ai_intent_pattern(intent),
                "confidence": 0.98,
                "command": command,
                "entities": entities,
                "seats": entities.get("seats") or [],
                "missing_fields": missing,
                "actionable": len(missing) == 0,
                "preview_text": ai_preview_text(intent, entities),
            }

        parsed = ai_parse_default_command(command, entities)
        intent = parsed["intent"]
        confidence = parsed["confidence"]

        if intent and confidence >= 0.80:
            missing = ai_required_fields(intent, entities)
            return {
                "status": "matched",
                "source": "default_parser",
                "intent": intent,
                "title": ai_intent_title(intent),
                "pattern": parsed["pattern"],
                "confidence": confidence,
                "command": command,
                "entities": entities,
                "seats": entities.get("seats") or [],
                "missing_fields": missing,
                "actionable": len(missing) == 0,
                "preview_text": ai_preview_text(intent, entities),
            }

        if intent and confidence >= 0.45:
            missing = ai_required_fields(intent, entities)
            return {
                "status": "suggest",
                "source": "default_parser",
                "intent": intent,
                "title": ai_intent_title(intent),
                "pattern": parsed["pattern"],
                "confidence": confidence,
                "command": command,
                "entities": entities,
                "seats": entities.get("seats") or [],
                "missing_fields": missing,
                "actionable": len(missing) == 0,
                "preview_text": ai_preview_text(intent, entities),
                "suggestion": {
                    "intent": intent,
                    "pattern": parsed["pattern"],
                },
            }

        return {
            "status": "unknown",
            "source": "none",
            "intent": None,
            "title": "",
            "pattern": None,
            "confidence": confidence,
            "command": command,
            "entities": entities,
            "seats": entities.get("seats") or [],
            "missing_fields": [],
            "actionable": False,
            "preview_text": "Komut çözülemedi.",
        }


    def ai_last_stop_info(trip_id: int):
        row = get_db().execute(
            """
            SELECT stop_name, event, ts
            FROM stop_logs
            WHERE trip_id=?
            ORDER BY id DESC
            LIMIT 1
            """,
            (trip_id,),
        ).fetchone()
        return dict(row) if row else None


    def ai_answer_query(intent: str, trip_row):
        tid = trip_row["id"]
        db = get_db()

        try:
            live_runtime = fetch_live_runtime_state(tid) or {}
        except Exception:
            live_runtime = {}

        def stop_key(v):
            s = (v or "").strip().lower()
            for ch in ["–", "-", "_", "/", "\\", ".", ",", "(", ")", "[", "]"]:
                s = s.replace(ch, " ")
            return " ".join(s.split())

        def find_stop_index(stops, name):
            if not stops or not name:
                return -1

            raw_key = stop_key(name)

            for i, stop in enumerate(stops):
                if stop == name:
                    return i

            for i, stop in enumerate(stops):
                if stop_key(stop) == raw_key:
                    return i

            for i, stop in enumerate(stops):
                sk = stop_key(stop)
                if raw_key and (raw_key in sk or sk in raw_key):
                    return i

            return -1

        if intent == "query_total_passengers":
            seat_row = db.execute("SELECT COUNT(*) AS c FROM seats WHERE trip_id=?", (tid,)).fetchone()
            standing_row = db.execute(
                "SELECT COALESCE(SUM(pax),0) AS c, COALESCE(SUM(total_amount),0) AS t FROM walk_on_sales WHERE trip_id=?",
                (tid,),
            ).fetchone()
            seated = int(seat_row["c"] or 0)
            standing = int(standing_row["c"] or 0)
            total = seated + standing
            return f"Toplam {total} yolcu var. {seated} oturan, {standing} ayakta."

        if intent == "query_standing_count":
            row = db.execute(
                "SELECT COALESCE(SUM(pax),0) AS c, COALESCE(SUM(total_amount),0) AS t FROM walk_on_sales WHERE trip_id=?",
                (tid,),
            ).fetchone()
            return f"Ayakta {int(row['c'] or 0)} kişi var. Tahsilat {float(row['t'] or 0):.2f} TL."

        if intent == "query_live_stop":
            live_stop = (live_runtime.get("live_stop") or "").strip()
            if live_stop:
                return f"Son canlı durak: {live_stop}."

            last = ai_last_stop_info(tid)
            if not last:
                return "Canlı durak için henüz kayıt yok."
            return f"Son bilinen durak: {last['stop_name']} ({last['event']})."

        if intent == "query_next_stop":
            stops = get_stops(trip_row["route"])
            if not stops:
                return "Bu hat için durak listesi bulunamadı."

            live_stop = (live_runtime.get("live_stop") or "").strip()
            base_stop = live_stop

            if not base_stop:
                last = ai_last_stop_info(tid)
                base_stop = (last or {}).get("stop_name") or ""

            if not base_stop:
                return f"Sıradaki durak: {stops[0]}"

            idx = find_stop_index(stops, base_stop)
            if idx < 0:
                return f"Sıradaki durak hesaplanamadı. Son kayıt: {base_stop}"

            next_idx = idx + 1
            if next_idx >= len(stops):
                return "Güzergâhın son durağındasın."

            return f"Sıradaki durak: {stops[next_idx]}"

        if intent == "query_delay":
            eta_main = (live_runtime.get("eta_main") or "").strip()
            eta_sub = (live_runtime.get("eta_sub") or "").strip()

            if eta_main or eta_sub:
                if eta_main and eta_sub:
                    return f"Rötar durumu: {eta_main}. {eta_sub}"
                return f"Rötar durumu: {eta_main or eta_sub}"

            return "Rötar bilgisi henüz hazır değil."

        return "Sorgu cevabı üretilemedi."


    def ai_upsert_single_seat(
        trip_id: int,
        seat_no: int,
        *,
        from_stop: str = "",
        to_stop: str = "",
        payment: str = "nakit",
        amount: float = 0.0,
        ticket_type: str = "biletsiz",
        gender: str = "",
        pair_ok: bool = False,
        service: bool = False,
        service_note: str = "",
    ):
        if not validate_seat_no(seat_no):
            raise ValueError(f"Geçersiz koltuk numarası: {seat_no}")

        trip = get_active_trip_row()
        if not trip:
            raise ValueError("Aktif sefer yok")

        if from_stop and not validate_stop_for_active_trip(from_stop):
            raise ValueError(f"Durak hat üzerinde değil: {from_stop}")
        if to_stop and not validate_stop_for_active_trip(to_stop):
            raise ValueError(f"Durak hat üzerinde değil: {to_stop}")

        gender = norm_gender(gender)
        payment = norm_payment(payment)
        ticket_type = norm_ticket_type(ticket_type)
        amount = parse_float(amount, 0.0) or 0.0

        ok, msg = neighbor_rule_ok(trip_id, seat_no, gender, pair_ok)
        if not ok:
            raise ValueError(msg)

        db = get_db()
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
                trip_id, seat_no, from_stop, to_stop, ticket_type, payment, amount,
                gender, 1 if pair_ok else 0, 1 if service else 0, service_note, "", "",
            ),
        )


    def ai_execute_intent(intent: str, entities: dict, command: str = ""):
        trip = get_active_trip_row()

        if intent in {"open_hesap", "open_emanet"}:
            return {
                "ok": True,
                "intent": intent,
                "answer_text": ai_preview_text(intent, entities),
                "redirect_url": url_for("hesap_page" if intent == "open_hesap" else "consignments_page"),
            }

        if not trip:
            raise ValueError("Aktif sefer yok")

        tid = trip["id"]
        db = get_db()

        if intent.startswith("query_"):
            return {
                "ok": True,
                "intent": intent,
                "answer_text": ai_answer_query(intent, trip),
            }

        if intent == "seat_remove_single":
            seat_no = (entities.get("seats") or [None])[0]
            if seat_no is None:
                raise ValueError("Koltuk gerekli")

            bag_deleted = 0
            try:
                trip_key = _trip_key_from_row(trip)
                bag_deleted = clear_bags_for_seat(trip_key, seat_no)
            except Exception:
                bag_deleted = 0

            db.execute("DELETE FROM seats WHERE trip_id=? AND seat_no=?", (tid, seat_no))
            db.commit()
            return {
                "ok": True,
                "intent": intent,
                "deleted": [seat_no],
                "bag_deleted": bag_deleted,
                "answer_text": f"{seat_no} numaralı koltuk boşaltıldı.",
            }

        if intent == "seat_remove_group":
            seats = entities.get("seats") or []
            if not seats:
                raise ValueError("Koltuk listesi gerekli")
            invalid = [s for s in seats if not validate_seat_no(s)]
            if invalid:
                raise ValueError(f"Geçersiz koltuklar: {invalid}")

            bag_deleted = 0
            try:
                trip_key = _trip_key_from_row(trip)
                for s in seats:
                    bag_deleted += clear_bags_for_seat(trip_key, s)
            except Exception:
                bag_deleted = 0

            db.executemany("DELETE FROM seats WHERE trip_id=? AND seat_no=?", [(tid, s) for s in seats])
            db.commit()
            return {
                "ok": True,
                "intent": intent,
                "deleted": seats,
                "bag_deleted": bag_deleted,
                "answer_text": f"Koltuklar boşaltıldı: {', '.join(map(str, seats))}",
            }

        if intent == "seat_add_single":
            seats = entities.get("seats") or []
            if len(seats) != 1:
                raise ValueError("Tek koltuk gerekli")
            ai_upsert_single_seat(
                tid,
                seats[0],
                from_stop=entities.get("from_stop") or "",
                to_stop=entities.get("to_stop") or "",
                payment=entities.get("payment") or "nakit",
                amount=entities.get("amount") or 0.0,
                ticket_type=entities.get("ticket_type") or "biletsiz",
                gender=entities.get("gender") or "",
                pair_ok=bool(entities.get("pair_ok")),
                service=bool(entities.get("service")),
                service_note=entities.get("note") or "",
            )
            db.commit()
            return {
                "ok": True,
                "intent": intent,
                "saved": seats,
                "answer_text": f"{seats[0]} numaralı koltuk kaydedildi.",
            }

        if intent == "seat_add_group":
            seats = entities.get("seats") or []
            if not seats:
                raise ValueError("Koltuk listesi gerekli")
            for seat_no in seats:
                ai_upsert_single_seat(
                    tid,
                    seat_no,
                    from_stop=entities.get("from_stop") or "",
                    to_stop=entities.get("to_stop") or "",
                    payment=entities.get("payment") or "nakit",
                    amount=entities.get("amount") or 0.0,
                    ticket_type=entities.get("ticket_type") or "biletsiz",
                    gender=entities.get("gender") or "",
                    pair_ok=bool(entities.get("pair_ok")),
                    service=bool(entities.get("service")),
                    service_note=entities.get("note") or "",
                )
            db.commit()
            return {
                "ok": True,
                "intent": intent,
                "saved": seats,
                "answer_text": f"Toplu koltuk kaydı yapıldı: {', '.join(map(str, seats))}",
            }

        if intent == "standing_add":
            count = parse_int(entities.get("count"), 1) or 1
            from_stop = entities.get("from_stop") or ""
            to_stop = entities.get("to_stop") or ""

            if from_stop and not validate_stop_for_active_trip(from_stop):
                raise ValueError(f"Durak hat üzerinde değil: {from_stop}")
            if to_stop and not validate_stop_for_active_trip(to_stop):
                raise ValueError(f"Durak hat üzerinde değil: {to_stop}")

            unit_price = parse_float(entities.get("amount"), 0.0) or 0.0
            total_amount = count * unit_price

            db.execute(
                """
                INSERT INTO walk_on_sales(trip_id, from_stop, to_stop, pax, unit_price, total_amount, payment, note)
                VALUES(?,?,?,?,?,?,?,?)
                """,
                (
                    tid,
                    from_stop,
                    to_stop,
                    count,
                    unit_price,
                    total_amount,
                    norm_payment(entities.get("payment") or "nakit"),
                    entities.get("note") or "",
                ),
            )
            db.commit()

            return {
                "ok": True,
                "intent": intent,
                "count": count,
                "answer_text": f"{count} ayakta yolcu kaydı eklendi.",
            }

        if intent == "standing_remove":
            to_stop = entities.get("to_stop") or entities.get("stop_name") or ""
            if not to_stop:
                raise ValueError("Durak gerekli")
            if not validate_stop_for_active_trip(to_stop):
                raise ValueError(f"Durak hat üzerinde değil: {to_stop}")

            deleted_ids = delete_walkon_rows(db, tid, to_stop=to_stop)
            db.commit()

            return {
                "ok": True,
                "intent": intent,
                "deleted": deleted_ids,
                "answer_text": f"{to_stop} durağı için ayakta kayıtları silindi. Kayıt: {len(deleted_ids)}",
            }

        if intent == "service_mark":
            seats = entities.get("seats") or []
            if not seats:
                raise ValueError("Koltuk listesi gerekli")
            invalid = [s for s in seats if not validate_seat_no(s)]
            if invalid:
                raise ValueError(f"Geçersiz koltuklar: {invalid}")

            db.executemany(
                "UPDATE seats SET service=1, service_note=? WHERE trip_id=? AND seat_no=?",
                [(entities.get("note") or "AI Console", tid, s) for s in seats],
            )
            db.commit()

            return {
                "ok": True,
                "intent": intent,
                "updated": seats,
                "answer_text": f"Servis işlendi: {', '.join(map(str, seats))}",
            }

        if intent == "service_unmark":
            seats = entities.get("seats") or []
            if not seats:
                raise ValueError("Koltuk listesi gerekli")
            invalid = [s for s in seats if not validate_seat_no(s)]
            if invalid:
                raise ValueError(f"Geçersiz koltuklar: {invalid}")

            db.executemany(
                "UPDATE seats SET service=0, service_note='' WHERE trip_id=? AND seat_no=?",
                [(tid, s) for s in seats],
            )
            db.commit()

            return {
                "ok": True,
                "intent": intent,
                "updated": seats,
                "answer_text": f"Servis kaldırıldı: {', '.join(map(str, seats))}",
            }

        if intent == "stop_select":
            stop_name = entities.get("stop_name") or entities.get("to_stop") or ""
            if not stop_name:
                raise ValueError("Durak gerekli")
            if not validate_stop_for_active_trip(stop_name):
                raise ValueError(f"Durak hat üzerinde değil: {stop_name}")

            return {
                "ok": True,
                "intent": intent,
                "selected_stop": stop_name,
                "answer_text": f"Durak seçildi: {stop_name}",
            }

        if intent == "stop_offload":
            stop_name = entities.get("stop_name") or entities.get("to_stop") or ""
            if not stop_name:
                raise ValueError("Durak gerekli")
            if not validate_stop_for_active_trip(stop_name):
                raise ValueError(f"Durak hat üzerinde değil: {stop_name}")

            seat_rows = db.execute(
                "SELECT seat_no FROM seats WHERE trip_id=? AND to_stop=? ORDER BY seat_no",
                (tid, stop_name),
            ).fetchall()
            seat_list = [r["seat_no"] for r in seat_rows]

            bag_deleted = 0
            try:
                trip_key = _trip_key_from_row(trip)
                for s in seat_list:
                    bag_deleted += clear_bags_for_seat(trip_key, s)
            except Exception:
                bag_deleted = 0

            if seat_list:
                db.executemany("DELETE FROM seats WHERE trip_id=? AND seat_no=?", [(tid, s) for s in seat_list])

            deleted_walkon = delete_walkon_rows(db, tid, to_stop=stop_name)
            db.commit()

            return {
                "ok": True,
                "intent": intent,
                "deleted_seats": seat_list,
                "deleted_standing_ids": deleted_walkon,
                "bag_deleted": bag_deleted,
                "answer_text": f"{stop_name} için iniş uygulandı. Koltuk: {len(seat_list)}, ayakta kayıt: {len(deleted_walkon)}",
            }

        raise ValueError(f"Bu intent için execute tanımlı değil: {intent}")


    # =========================================================
    # AI Console API v2
    # =========================================================

    @app.get("/api/ai/bootstrap")
    def api_ai_bootstrap():
        trip = get_active_trip_row()
        learned_count = get_db().execute("SELECT COUNT(*) AS c FROM learned_commands").fetchone()["c"]

        return jsonify({
            "ok": True,
            "active_trip": dict(trip) if trip else None,
            "stops": get_stops(trip["route"]) if trip else [],
            "learned_count": int(learned_count or 0),
            "intents": [
                {
                    "key": key,
                    "title": meta["title"],
                    "pattern": meta["pattern"],
                    "description": meta.get("description", ""),
                    "examples": meta.get("examples", []),
                }
                for key, meta in AI_INTENTS.items()
            ],
        })


    @app.get("/api/ai/intents")
    def api_ai_intents():
        return jsonify({
            "ok": True,
            "items": [
                {
                    "key": key,
                    "title": meta["title"],
                    "pattern": meta["pattern"],
                    "description": meta.get("description", ""),
                    "examples": meta.get("examples", []),
                }
                for key, meta in AI_INTENTS.items()
            ],
        })


    @app.get("/api/ai/learned")
    def api_ai_learned():
        rows = get_db().execute(
            """
            SELECT id, phrase, intent, pattern, created_at, updated_at
            FROM learned_commands
            ORDER BY id DESC
            """
        ).fetchall()
        return jsonify({"ok": True, "items": [dict(r) for r in rows]})


    @app.post("/api/ai/resolve")
    def api_ai_resolve():
        data = request.get_json(force=True) or {}
        command = (data.get("command") or "").strip()
        if not command:
            return jsonify({"ok": False, "msg": "command gerekli"}), 400
        return jsonify({"ok": True, "result": resolve_ai_command(command)})


    @app.post("/api/ai/execute")
    def api_ai_execute():
        data = request.get_json(force=True) or {}

        intent = (data.get("intent") or "").strip()
        command = (data.get("command") or "").strip()
        entities = data.get("entities") or {}

        if not intent:
            return jsonify({"ok": False, "msg": "intent gerekli"}), 400
        if intent not in AI_INTENTS:
            return jsonify({"ok": False, "msg": "intent geçersiz"}), 400

        try:
            result = ai_execute_intent(intent, entities, command)
            return jsonify({"ok": True, "result": result})
        except ValueError as e:
            return jsonify({"ok": False, "msg": str(e)}), 400
        except Exception as e:
            return jsonify({"ok": False, "msg": f"execute hatası: {e}"}), 500


    @app.post("/api/ai/learn")
    def api_ai_learn():
        data = request.get_json(force=True) or {}
        phrase = (data.get("phrase") or "").strip()
        intent = (data.get("intent") or "").strip()
        pattern = (data.get("pattern") or "").strip()

        if not phrase:
            return jsonify({"ok": False, "msg": "phrase gerekli"}), 400
        if intent not in AI_INTENTS:
            return jsonify({"ok": False, "msg": "intent geçersiz"}), 400
        if not pattern:
            pattern = AI_INTENTS[intent]["pattern"]

        phrase_norm = normalize_ai_text(phrase)
        skeleton = ai_make_skeleton(phrase)
        db = get_db()

        row = db.execute("SELECT id FROM learned_commands WHERE phrase_norm=?", (phrase_norm,)).fetchone()

        try:
            if row:
                db.execute(
                    """
                    UPDATE learned_commands
                    SET phrase=?, skeleton=?, intent=?, pattern=?, updated_at=datetime('now','localtime')
                    WHERE id=?
                    """,
                    (phrase, skeleton, intent, pattern, row["id"]),
                )
                item_id = row["id"]
            else:
                cur = db.execute(
                    """
                    INSERT INTO learned_commands(phrase, phrase_norm, skeleton, intent, pattern)
                    VALUES(?,?,?,?,?)
                    """,
                    (phrase, phrase_norm, skeleton, intent, pattern),
                )
                item_id = cur.lastrowid
            db.commit()
        except sqlite3.IntegrityError:
            return jsonify({"ok": False, "msg": "Bu ifade zaten başka bir kayıtla çakışıyor"}), 409

        saved = db.execute(
            """
            SELECT id, phrase, intent, pattern, created_at, updated_at
            FROM learned_commands
            WHERE id=?
            """,
            (item_id,),
        ).fetchone()

        return jsonify({"ok": True, "item": dict(saved)})


    @app.put("/api/ai/learned/<int:item_id>")
    def api_ai_learned_update(item_id):
        data = request.get_json(force=True) or {}
        phrase = (data.get("phrase") or "").strip()
        intent = (data.get("intent") or "").strip()
        pattern = (data.get("pattern") or "").strip()

        if not phrase:
            return jsonify({"ok": False, "msg": "phrase gerekli"}), 400
        if intent not in AI_INTENTS:
            return jsonify({"ok": False, "msg": "intent geçersiz"}), 400
        if not pattern:
            pattern = AI_INTENTS[intent]["pattern"]

        phrase_norm = normalize_ai_text(phrase)
        skeleton = ai_make_skeleton(phrase)
        db = get_db()

        try:
            db.execute(
                """
                UPDATE learned_commands
                SET phrase=?, phrase_norm=?, skeleton=?, intent=?, pattern=?, updated_at=datetime('now','localtime')
                WHERE id=?
                """,
                (phrase, phrase_norm, skeleton, intent, pattern, item_id),
            )
            db.commit()
        except sqlite3.IntegrityError:
            return jsonify({"ok": False, "msg": "Bu ifade başka bir kayıtla çakışıyor"}), 409

        row = db.execute(
            """
            SELECT id, phrase, intent, pattern, created_at, updated_at
            FROM learned_commands
            WHERE id=?
            """,
            (item_id,),
        ).fetchone()

        if not row:
            return jsonify({"ok": False, "msg": "Kayıt bulunamadı"}), 404

        return jsonify({"ok": True, "item": dict(row)})


    @app.delete("/api/ai/learned/<int:item_id>")
    def api_ai_learned_delete(item_id):
        db = get_db()
        db.execute("DELETE FROM learned_commands WHERE id=?", (item_id,))
        db.commit()
        return jsonify({"ok": True, "id": item_id})

    return {
        "AI_INTENTS": AI_INTENTS,
        "ai_intent_title": ai_intent_title,
        "ai_intent_pattern": ai_intent_pattern,
        "ai_extract_stop_mentions": ai_extract_stop_mentions,
        "ai_extract_payment": ai_extract_payment,
        "ai_extract_gender": ai_extract_gender,
        "ai_extract_amount": ai_extract_amount,
        "ai_extract_count": ai_extract_count,
        "ai_extract_entities": ai_extract_entities,
        "ai_parse_default_command": ai_parse_default_command,
        "ai_required_fields": ai_required_fields,
        "ai_preview_text": ai_preview_text,
        "resolve_ai_command": resolve_ai_command,
        "ai_last_stop_info": ai_last_stop_info,
        "ai_answer_query": ai_answer_query,
        "ai_upsert_single_seat": ai_upsert_single_seat,
        "ai_execute_intent": ai_execute_intent,
    }
