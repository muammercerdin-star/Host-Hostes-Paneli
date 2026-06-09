from pathlib import Path
import sys
import json
import sqlite3
from datetime import datetime

ROOT = Path(".").resolve()

for _p in [
    ROOT,
    ROOT / "modules",
    ROOT / "blueprints",
    ROOT / "routes",
    ROOT / "utils",
]:
    sp = str(_p)
    if sp not in sys.path:
        sys.path.insert(0, sp)

print("===== FIX DUPLICATE DERBENT V69 =====")

try:
    import app as muavin
except Exception as e:
    print("❌ app.py import edilemedi:", e)
    raise SystemExit

def norm(v):
    return " ".join((v or "").strip().lower().split())

def midpoint(a, b):
    return ((float(a[0]) + float(b[0])) / 2, (float(a[1]) + float(b[1])) / 2)

with muavin.app.app_context():
    db = muavin.get_db()

    tid = muavin.get_active_trip()
    if not tid:
        print("❌ Aktif sefer yok")
        raise SystemExit

    trip = db.execute("SELECT * FROM trips WHERE id=?", (tid,)).fetchone()
    if not trip:
        print("❌ Aktif sefer bulunamadı")
        raise SystemExit

    route = trip["route"]
    print("Aktif sefer:", tid)
    print("Hat:", route)

    stops = muavin.get_stops(route)
    print("Durak adedi:", len(stops))

    derbent_positions = [i for i, s in enumerate(stops) if norm(s) == "derbent"]
    print("Derbent sıra indexleri:", [i + 1 for i in derbent_positions])

    if len(derbent_positions) < 2:
        print("ℹ️ Bu hatta iki Derbent yok. İşlem yapılmadı.")
        raise SystemExit

    # Yedek tablo
    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_table = f"route_stop_coords_backup_v69_{stamp}"

    db.execute(f"""
        CREATE TABLE IF NOT EXISTS {backup_table} AS
        SELECT * FROM route_stop_coords
        WHERE route=?
    """, (route,))
    print("📦 Koordinat yedeği:", backup_table)

    # 1) Durak listesindeki iki Derbent'i ayır
    new_stops = list(stops)
    new_stops[derbent_positions[0]] = "Derbent (Denizli)"
    new_stops[derbent_positions[1]] = "Derbent (Manisa)"

    row = db.execute("SELECT * FROM routes WHERE name=?", (route,)).fetchone()
    if row:
        db.execute(
            "UPDATE routes SET stops=? WHERE name=?",
            (json.dumps(new_stops, ensure_ascii=False), route)
        )
        print("✅ routes.stops güncellendi")
    else:
        db.execute(
            "INSERT INTO routes(name, stops) VALUES(?, ?)",
            (route, json.dumps(new_stops, ensure_ascii=False))
        )
        print("✅ routes kaydı oluşturuldu")

    # 2) Eski tek Derbent koordinatını Manisa Derbent olarak taşı
    old_derbent = db.execute(
        "SELECT route, stop, lat, lng FROM route_stop_coords WHERE route=? AND stop=? LIMIT 1",
        (route, "Derbent"),
    ).fetchone()

    if old_derbent:
        db.execute(
            "DELETE FROM route_stop_coords WHERE route=? AND stop=?",
            (route, "Derbent"),
        )
        db.execute(
            """
            INSERT OR REPLACE INTO route_stop_coords(route, stop, lat, lng)
            VALUES(?,?,?,?)
            """,
            (route, "Derbent (Manisa)", old_derbent["lat"], old_derbent["lng"])
        )
        print("✅ Eski Derbent koordinatı Derbent (Manisa) yapıldı:", old_derbent["lat"], old_derbent["lng"])
    else:
        print("⚠️ Eski Derbent koordinatı yoktu")

    # 3) Denizli Derbent için Baraj Yolu ile Kadıköy arasından geçici koordinat üret
    baraj = db.execute(
        "SELECT lat, lng FROM route_stop_coords WHERE route=? AND stop=? LIMIT 1",
        (route, "Baraj Yolu"),
    ).fetchone()

    kadikoy = db.execute(
        "SELECT lat, lng FROM route_stop_coords WHERE route=? AND stop=? LIMIT 1",
        (route, "Kadıköy"),
    ).fetchone()

    if baraj and kadikoy:
        lat, lng = midpoint((baraj["lat"], baraj["lng"]), (kadikoy["lat"], kadikoy["lng"]))
        db.execute(
            """
            INSERT OR REPLACE INTO route_stop_coords(route, stop, lat, lng)
            VALUES(?,?,?,?)
            """,
            (route, "Derbent (Denizli)", lat, lng)
        )
        print("✅ Derbent (Denizli) geçici koordinat eklendi:", round(lat, 6), round(lng, 6))
    else:
        print("⚠️ Baraj Yolu / Kadıköy koordinatı bulunamadı, Derbent (Denizli) eklenemedi")

    # 4) canlı durak boşaltılsın, GPS yeniden doğru yakalasın
    try:
        db.execute(
            """
            INSERT INTO live_runtime_state(trip_id, live_stop, speed, gps_km, eta_main, eta_sub, updated_at)
            VALUES(?,?,?,?,?,?,datetime('now','localtime'))
            ON CONFLICT(trip_id)
            DO UPDATE SET
                live_stop='',
                gps_km='',
                eta_main='',
                eta_sub='duplicate-derbent-fixed-v69',
                updated_at=datetime('now','localtime')
            """,
            (tid, "", 0, "", "", "duplicate-derbent-fixed-v69")
        )
        print("✅ live_runtime_state temizlendi")
    except Exception as e:
        print("⚠️ live_runtime temizlenemedi:", e)

    db.commit()

    print()
    print("===== SON DURAK LİSTESİ =====")
    final_stops = muavin.get_stops(route)
    for i, s in enumerate(final_stops, 1):
        if "Derbent" in s or i in [5,6,7,25,26,27]:
            print(f"{i:02d}. {s}")

    print()
    print("===== SON KOORDİNATLAR =====")
    rows = db.execute(
        """
        SELECT stop, lat, lng
        FROM route_stop_coords
        WHERE route=? AND stop LIKE 'Derbent%'
        ORDER BY stop
        """,
        (route,),
    ).fetchall()

    for r in rows:
        print(dict(r))

print()
print("✅ V69 tamam. Şimdi V68 teşhisi tekrar çalıştırıp mesafeler düzelmiş mi bak.")
