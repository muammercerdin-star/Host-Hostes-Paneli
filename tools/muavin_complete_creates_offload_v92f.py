from pathlib import Path
from datetime import datetime
import shutil

ROOT = Path(".").resolve()
STAMP = datetime.now().strftime("%Y%m%d-%H%M%S")

FILES = [
    ROOT / "app.py",
    ROOT / "android_app/app/src/main/python/app.py",
]

print("===== V92F TAMAMLA = GERÇEK İNİŞ LOGU =====")

OLD_SEAT_BLOCK = '''        # 1) Bu durakta inecek koltuklu yolcuları temizle.
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
'''

NEW_SEAT_BLOCK = '''        # 1) Bu durakta inecek koltuklu yolcuları önce oku.
        # V92F:
        # Tamamla butonu artık her koltuk için gerçek "offload" hareketi üretir.
        # Sonra aktif seats kaydını siler. Böylece Toplam İnen ve Koltuk Hareket Haritası doğru sayar.
        seat_rows = cur.execute("""
            SELECT seat_no,
                   COALESCE(stop,'') AS stop,
                   COALESCE(from_stop,'') AS from_stop,
                   COALESCE(to_stop,'') AS to_stop,
                   COALESCE(ticket_type,'') AS ticket_type,
                   COALESCE(payment,'') AS payment,
                   COALESCE(amount,0) AS amount,
                   COALESCE(gender,'') AS gender,
                   COALESCE(service,0) AS service,
                   COALESCE(service_note,'') AS service_note,
                   COALESCE(passenger_name,'') AS passenger_name,
                   COALESCE(passenger_phone,'') AS passenger_phone
            FROM seats
            WHERE trip_id = ?
              AND (
                    lower(trim(to_stop)) = lower(trim(?))
                 OR lower(trim(stop)) = lower(trim(?))
              )
            ORDER BY seat_no
        """, (trip_id, stop, stop)).fetchall()

        seat_numbers = [str(r["seat_no"]) for r in seat_rows]

        for sr in seat_rows:
            try:
                seat_meta = {
                    "seat_no": sr["seat_no"],
                    "from_stop": sr["from_stop"] or "",
                    "to_stop": sr["to_stop"] or stop,
                    "ticket_type": sr["ticket_type"] or "",
                    "payment": sr["payment"] or "",
                    "amount": float(sr["amount"] or 0),
                    "gender": sr["gender"] or "",
                    "service": int(sr["service"] or 0),
                    "service_note": sr["service_note"] or "",
                    "passenger_name": sr["passenger_name"] or "",
                    "passenger_phone": sr["passenger_phone"] or "",
                    "source": "seat",
                    "action": "live_stop_complete_v92f",
                    "completed_stop": stop,
                    "completed_by": "tamamla_button",
                }

                cur.execute("""
                    INSERT INTO stop_logs
                    (trip_id, stop_name, event, distance_km, seats_for_stop, meta_json)
                    VALUES (?, ?, 'offload', NULL, 1, ?)
                """, (trip_id, stop, json.dumps(seat_meta, ensure_ascii=False)))
            except Exception:
                pass

        cur.execute("""
            DELETE FROM seats
            WHERE trip_id = ?
              AND (
                    lower(trim(to_stop)) = lower(trim(?))
                 OR lower(trim(stop)) = lower(trim(?))
              )
        """, (trip_id, stop, stop))
        removed_seats = cur.rowcount if cur.rowcount is not None else 0
'''

OLD_WALK_BLOCK = '''        # 2) Bu durakta inen ara yolcu kayıtlarını temizle.
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
'''

NEW_WALK_BLOCK = '''        # 2) Bu durakta inen ara yolcu kayıtlarını önce logla, sonra temizle.
        removed_walk_on = 0
        try:
            walk_rows = cur.execute("""
                SELECT id,
                       COALESCE(from_stop,'') AS from_stop,
                       COALESCE(to_stop,'') AS to_stop,
                       COALESCE(pax,1) AS pax,
                       COALESCE(unit_price,0) AS unit_price,
                       COALESCE(total_amount,0) AS total_amount,
                       COALESCE(payment,'') AS payment,
                       COALESCE(note,'') AS note,
                       COALESCE(created_at,'') AS created_at
                FROM walk_on_sales
                WHERE trip_id = ?
                  AND lower(trim(to_stop)) = lower(trim(?))
                ORDER BY id
            """, (trip_id, stop)).fetchall()

            for wr in walk_rows:
                try:
                    pax = int(wr["pax"] or 1)
                except Exception:
                    pax = 1

                try:
                    walk_meta = {
                        "id": wr["id"],
                        "from_stop": wr["from_stop"] or "",
                        "to_stop": wr["to_stop"] or stop,
                        "pax": pax,
                        "unit_price": float(wr["unit_price"] or 0),
                        "total_amount": float(wr["total_amount"] or 0),
                        "payment": wr["payment"] or "",
                        "note": wr["note"] or "",
                        "created_at": wr["created_at"] or "",
                        "source": "walk_on_sale",
                        "action": "live_stop_complete_v92f",
                        "completed_stop": stop,
                        "completed_by": "tamamla_button",
                    }

                    cur.execute("""
                        INSERT INTO stop_logs
                        (trip_id, stop_name, event, distance_km, seats_for_stop, meta_json)
                        VALUES (?, ?, 'standing_off', NULL, ?, ?)
                    """, (trip_id, stop, pax, json.dumps(walk_meta, ensure_ascii=False)))
                except Exception:
                    pass

            cur.execute("""
                DELETE FROM walk_on_sales
                WHERE trip_id = ?
                  AND lower(trim(to_stop)) = lower(trim(?))
            """, (trip_id, stop))
            removed_walk_on = cur.rowcount if cur.rowcount is not None else 0
        except Exception:
            removed_walk_on = 0
'''

OLD_REPORT_BLOCK = '''        elif event == "completed_v92c":
            try:
                completed_count = int(r["seats_for_stop"] or 0)
            except Exception:
                completed_count = 0

            # V92E:
            # "Tamamla" işlemi duraktaki yolcu/ayakta yolcu kayıtlarını toplu temizler.
            # Bu kayıtlar raporda da "inen yolcu" olarak sayılmalı.
            item["event_label"] = "Durak tamamlandı"
            item["completed_count"] = completed_count
            g["offload"].append(item)
            g["summary"]["offload_count"] += completed_count
'''

NEW_REPORT_BLOCK = '''        elif event == "completed_v92c":
            # V92F:
            # completed_v92c artık sadece "durak tamamlandı / sıradaki durağa geçildi" kaydıdır.
            # İnen yolcu sayısı gerçek offload kayıtlarından sayılır.
            item["event_label"] = "Durak tamamlandı"
            g["other"].append(item)
'''

for path in FILES:
    if not path.exists():
        print("❌ Yok:", path.relative_to(ROOT))
        continue

    txt = path.read_text(encoding="utf-8", errors="ignore")
    old_txt = txt

    # next_stop fallback içinde re.split kullanılıyor; route içi importta re yoksa ekle.
    if "def api_live_stop_complete_v92c():" in txt:
        txt = txt.replace(
            "    import sqlite3\n    import json\n",
            "    import sqlite3\n    import json\n    import re\n",
            1
        )

    if OLD_SEAT_BLOCK not in txt:
        print("❌ Seat blok bulunamadı:", path.relative_to(ROOT))
    else:
        txt = txt.replace(OLD_SEAT_BLOCK, NEW_SEAT_BLOCK, 1)
        print("✅ Seat complete/offload log bloğu eklendi:", path.relative_to(ROOT))

    if OLD_WALK_BLOCK not in txt:
        print("❌ Walk-on blok bulunamadı:", path.relative_to(ROOT))
    else:
        txt = txt.replace(OLD_WALK_BLOCK, NEW_WALK_BLOCK, 1)
        print("✅ Ara yolcu standing_off log bloğu eklendi:", path.relative_to(ROOT))

    if OLD_REPORT_BLOCK not in txt:
        print("⚠️ V92E rapor bloğu bulunamadı, belki daha önce değişti:", path.relative_to(ROOT))
    else:
        txt = txt.replace(OLD_REPORT_BLOCK, NEW_REPORT_BLOCK, 1)
        print("✅ completed_v92c çift sayma engellendi:", path.relative_to(ROOT))

    if txt != old_txt:
        bak = path.with_name(path.name + f".bak-v92f-{STAMP}")
        shutil.copy2(path, bak)
        path.write_text(txt, encoding="utf-8")
        print("📦 Yedek:", bak.relative_to(ROOT))
    else:
        print("ℹ️ Değişiklik yapılmadı:", path.relative_to(ROOT))

print()
print("===== KONTROL =====")
for path in FILES:
    if not path.exists():
        continue
    txt = path.read_text(encoding="utf-8", errors="ignore")
    for i, line in enumerate(txt.splitlines(), 1):
        if any(k in line for k in [
            "live_stop_complete_v92f",
            "completed_by",
            "completed_v92c",
            "İnen yolcu sayısı gerçek offload",
            "standing_off",
            "VALUES (?, ?, 'offload'",
            "VALUES (?, ?, 'standing_off'",
        ]):
            if 2600 <= i <= 2895 or 4210 <= i <= 4255:
                print(f"{path.relative_to(ROOT)}:{i}: {line}")

print()
print("✅ V92F tamam.")
