from pathlib import Path
import sqlite3, json, os, re, sys

ROOT = Path(__file__).resolve().parents[1]

VALID_SEATS = [
    1,3,4,5,7,8,9,11,12,13,15,16,17,19,20,21,23,24,25,
    27,28,29,31,33,34,35,37,38,39,41,42,43,45,46,49,50,51,52,53,54
]
VALID_SET = set(VALID_SEATS)

def is_sqlite_db(p: Path):
    try:
        if not p.is_file() or p.stat().st_size < 100:
            return False
        with p.open("rb") as f:
            return f.read(16).startswith(b"SQLite format 3")
    except Exception:
        return False

def find_dbs():
    out = []
    for p in ROOT.rglob("*"):
        if ".git" in p.parts or "__pycache__" in p.parts:
            continue
        if p.suffix.lower() in [".db", ".sqlite", ".sqlite3"] or is_sqlite_db(p):
            if is_sqlite_db(p):
                out.append(p)
    return sorted(set(out), key=lambda x: str(x))

def table_exists(con, name):
    return con.execute(
        "SELECT 1 FROM sqlite_master WHERE type='table' AND name=?",
        (name,)
    ).fetchone() is not None

def cols(con, table):
    try:
        return [r[1] for r in con.execute(f"PRAGMA table_info({table})").fetchall()]
    except Exception:
        return []

def safe(v):
    if v is None:
        return ""
    return str(v).replace("\n", " ").strip()

dbs = find_dbs()

print("===== DB DOSYALARI =====")
if not dbs:
    print("DB bulunamadı.")
    sys.exit()

for i, db in enumerate(dbs, 1):
    print(f"{i}) {db.relative_to(ROOT)}  ({db.stat().st_size} byte)")

print()
print("===== KOLTUK SAYIM DENETİMİ =====")

for db in dbs:
    print()
    print("############################################################")
    print("DB:", db.relative_to(ROOT))
    print("############################################################")

    try:
        con = sqlite3.connect(str(db))
        con.row_factory = sqlite3.Row
    except Exception as e:
        print("AÇILAMADI:", e)
        continue

    try:
        tables = [r[0] for r in con.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name")]
        print("TABLOLAR:", ", ".join(tables))
    except Exception as e:
        print("TABLO OKUMA HATASI:", e)
        continue

    if not table_exists(con, "seats"):
        print("Bu DB içinde seats tablosu yok, geçildi.")
        continue

    seat_cols = cols(con, "seats")
    print("SEATS KOLONLARI:", ", ".join(seat_cols))

    active_trip_id = None
    if table_exists(con, "app_state"):
        st_cols = cols(con, "app_state")
        if "active_trip_id" in st_cols:
            row = con.execute("SELECT active_trip_id FROM app_state WHERE id=1").fetchone()
            if row:
                active_trip_id = row["active_trip_id"]

    if active_trip_id is None and table_exists(con, "trips"):
        row = con.execute("SELECT id FROM trips ORDER BY id DESC LIMIT 1").fetchone()
        if row:
            active_trip_id = row["id"]

    print("AKTİF/LATEST TRIP ID:", active_trip_id)

    if table_exists(con, "trips") and active_trip_id is not None:
        try:
            trip = con.execute("SELECT * FROM trips WHERE id=?", (active_trip_id,)).fetchone()
            if trip:
                print("TRIP:", dict(trip))
        except Exception as e:
            print("TRIP OKUMA HATASI:", e)

    if active_trip_id is None:
        print("Trip bulunamadı.")
        continue

    try:
        rows = con.execute("SELECT * FROM seats WHERE trip_id=? ORDER BY CAST(seat_no AS INTEGER), seat_no", (active_trip_id,)).fetchall()
    except Exception as e:
        print("SEATS OKUMA HATASI:", e)
        continue

    seat_nos = []
    invalid = []
    empty_no = []
    for r in rows:
        raw = r["seat_no"] if "seat_no" in r.keys() else None
        try:
            n = int(raw)
            seat_nos.append(n)
            if n not in VALID_SET:
                invalid.append(dict(r))
        except Exception:
            empty_no.append(dict(r))

    distinct = sorted(set(seat_nos))
    dupes = sorted([n for n in set(seat_nos) if seat_nos.count(n) > 1])

    print()
    print("---- ÖZET ----")
    print("DB seats satır sayısı:", len(rows))
    print("Distinct seat_no:", len(distinct), distinct)
    print("Geçerli oturma planındaki kayıt:", len([n for n in distinct if n in VALID_SET]))
    print("Planda OLMAYAN seat_no:", [n for n in distinct if n not in VALID_SET])
    print("Duplicate seat_no:", dupes)
    print("Boş/bozuk seat_no satırı:", len(empty_no))
    print("Beklenen toplam koltuk planı:", len(VALID_SEATS))

    if "gender" in seat_cols:
        gender_counts = {}
        for r in rows:
            g = safe(r["gender"]).lower()
            gender_counts[g] = gender_counts.get(g, 0) + 1
        print("Gender dağılımı:", gender_counts)

    if "ticket_type" in seat_cols:
        ticket_counts = {}
        for r in rows:
            t = safe(r["ticket_type"]).lower()
            ticket_counts[t] = ticket_counts.get(t, 0) + 1
        print("Ticket dağılımı:", ticket_counts)

    print()
    print("---- KOLTUK SATIRLARI ----")
    for r in rows:
        d = dict(r)
        parts = []
        for k in ["seat_no", "gender", "from_stop", "to_stop", "ticket_type", "payment", "amount", "service", "service_note", "passenger_name"]:
            if k in d:
                parts.append(f"{k}={safe(d[k])}")
        print(" | ".join(parts))

    if invalid:
        print()
        print("!!!! PLANA GÖRE GÖRÜNMEYEN/GEÇERSİZ KOLTUK KAYDI VAR !!!!")
        for r in invalid:
            print(r)

    if table_exists(con, "walk_on_sales"):
        print()
        print("---- WALK_ON / YOLDAN SATIŞ ----")
        try:
            wcols = cols(con, "walk_on_sales")
            print("walk_on_sales kolonları:", ", ".join(wcols))
            if "trip_id" in wcols:
                wrows = con.execute("SELECT * FROM walk_on_sales WHERE trip_id=? ORDER BY id", (active_trip_id,)).fetchall()
            else:
                wrows = con.execute("SELECT * FROM walk_on_sales ORDER BY rowid").fetchall()

            total_pax = 0
            for w in wrows:
                wd = dict(w)
                pax = wd.get("pax", 0) or 0
                try:
                    total_pax += int(pax)
                except Exception:
                    pass
                print(wd)
            print("Yoldan satış satır:", len(wrows), "Toplam pax:", total_pax)
            print("Eğer burada Toplam pax 1 ise sayaç 18 + 1 = 19 yapıyor olabilir.")
        except Exception as e:
            print("walk_on_sales okunamadı:", e)

print()
print("===== WEB / ANDROID TEMPLATE FARK KONTROL =====")
files = [
    ROOT / "templates/seats.html",
    ROOT / "android_app/app/src/main/python/templates/seats.html",
]
for f in files:
    if f.exists():
        print(f"{f.relative_to(ROOT)} -> {f.stat().st_size} byte")
    else:
        print(f"{f.relative_to(ROOT)} -> YOK")
