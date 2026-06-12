from pathlib import Path
import re

ROOT = Path(".").resolve()

FILES = [
    "app.py",
    "android_app/app/src/main/python/app.py",
    "static/continue/continue_trip_core.js",
    "android_app/app/src/main/python/static/continue/continue_trip_core.js",
    "templates/continue_trip.html",
    "android_app/app/src/main/python/templates/continue_trip.html",
]

KEYS = [
    "Toplam İnen",
    "toplam_inen",
    "total_offload",
    "offload",
    "inen",
    "to_stop",
    "from_stop",
    "live-stop-complete",
    "api_live_stop_complete",
    "completed_v92c",
    "stop_logs",
    "seats",
    "walk_on_sales",
]

print("===== V92D RAPOR İNEN SAYACI DENETİMİ =====")
print("ROOT:", ROOT)
print()

for f in FILES:
    p = ROOT / f
    if not p.exists():
        print("❌ Yok:", f)
        continue

    print()
    print("===== DOSYA:", f, "=====")
    txt = p.read_text(encoding="utf-8", errors="ignore")
    lines = txt.splitlines()

    hit = 0
    for i, line in enumerate(lines, 1):
        low = line.lower()
        if any(k.lower() in low for k in KEYS):
            print(f"{i}: {line[:240]}")
            hit += 1

    if hit == 0:
        print("⚠️ İz bulunamadı")

print()
print("===== DB HIZLI KONTROL =====")
import sqlite3
db = ROOT / "db.sqlite3"

if not db.exists():
    print("❌ db.sqlite3 yok")
else:
    con = sqlite3.connect(db)
    con.row_factory = sqlite3.Row
    cur = con.cursor()

    print()
    print("Son aktif trip:")
    try:
        row = cur.execute("SELECT active_trip_id FROM app_state LIMIT 1").fetchone()
        active_trip = row["active_trip_id"] if row else None
        print("active_trip_id =", active_trip)
    except Exception as e:
        active_trip = None
        print("app_state hata:", e)

    if active_trip:
        print()
        print("Seats to_stop sayımı:")
        try:
            rows = cur.execute("""
                SELECT to_stop, COUNT(*) AS adet
                FROM seats
                WHERE trip_id = ?
                  AND COALESCE(to_stop,'') <> ''
                GROUP BY to_stop
                ORDER BY adet DESC, to_stop
            """, (active_trip,)).fetchall()
            for r in rows:
                print(dict(r))
        except Exception as e:
            print("seats hata:", e)

        print()
        print("Stop logs completed/offload benzeri kayıtlar:")
        try:
            rows = cur.execute("""
                SELECT stop_name, event, seats_for_stop, meta_json, ts
                FROM stop_logs
                WHERE trip_id = ?
                ORDER BY id DESC
                LIMIT 30
            """, (active_trip,)).fetchall()
            for r in rows:
                print(dict(r))
        except Exception as e:
            print("stop_logs hata:", e)

print()
print("✅ V92D audit tamam. Çıktıyı gönder reis.")
