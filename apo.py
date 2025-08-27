from flask import (
    Flask, render_template, request, redirect, url_for,
    jsonify, g, session, flash
)
import sqlite3
import json
from datetime import datetime

app = Flask(__name__)
app.secret_key = "degistir-beni"  # prod'da ortam değişkeni kullan
DB_PATH = "db.sqlite3"

# ---------------- DB yardımcıları ----------------
def get_db():
    if "db" not in g:
        g.db = sqlite3.connect(DB_PATH)
        g.db.row_factory = sqlite3.Row
    return g.db

@app.teardown_appcontext
def close_db(exc):
    db = g.pop("db", None)
    if db is not None:
        db.close()

def ensure_schema():
    db = get_db()
    db.executescripts(
        """
        PRAGMA journal_mode=WAL;

        CREATE TABLE IF NOT EXISTS trips(
            id INTEGER PRIMARY KEY,
            date TEXT,
            route TEXT,
            departure_time TEXT,
            plate TEXT,
            captain1 TEXT,
            captain2 TEXT,
            attendant TEXT,
            note TEXT
        );

        CREATE TABLE IF NOT EXISTS app_state(
            id INTEGER PRIMARY KEY CHECK(id=1),
            active_trip_id INTEGER
        );
        INSERT OR IGNORE INTO app_state(id, active_trip_id) VALUES (1, NULL);

        CREATE TABLE IF NOT EXISTS seats(
            trip_id INTEGER,
            seat_no INTEGER,
            stop TEXT,
            ticket_type TEXT,   -- 'biletli' | 'biletsiz' | 'ucretsiz'
            payment TEXT,       -- 'nakit' | 'iban' | 'online' | 'pos' | 'ucretsiz'
            amount REAL,
            PRIMARY KEY(trip_id, seat_no)
        );

        -- Dinamik hatlar
        CREATE TABLE IF NOT EXISTS routes(
            id INTEGER PRIMARY KEY,
            name TEXT UNIQUE,
            stops TEXT           -- JSON list (["Durak1","Durak2",...])
        );
        """
    )
    db.commit()

def set_active_trip(trip_id: int | None):
    db = get_db()
    db.execute("UPDATE app_state SET active_trip_id=?", (trip_id,))
    db.commit()

def get_active_trip():
    db = get_db()
    row = db.execute("SELECT active_trip_id FROM app_state WHERE id=1").fetchone()
    return row["active_trip_id"] if row else None

# ---------------- Rotalar & Duraklar (sabitler) ----------------
ROUTE_STOPS = {
    "Denizli – İstanbul": [
        "Denizli otogar","Sarayköy","Buldan","Bozalan","Derbent(Denizli)",
        "Kadıköy","İl Sınırı(Manisa)","Dindarlı","Dadağlı","Sarıgöl Garaj","Afşar",
        "Bereketli","Hacıaliler","Ortahan","Belenyaka","Alaşehir Otogar",
        "Alaşehir Stadyum","Akkeçili","Piyadeler","Kavaklıdere","Salihli Garaj",
        "Sart","Ahmetli","Gökkaya","Akçapınar","Derbent(Turgutlu)","Turgutlu Garaj",
        "Özdilek(Turgutlu)","Manisa Otogar","Akhisar","Saruhanlı","Soma","Kırkağaç",
        "Balıkesir","Susurluk","Mustafa K.P(Bursa)","Bursa Otogar","Gebze Garaj",
        "Harem","Alibeyköy","Esenler Otogar"
    ],
    "Denizli – İzmir": [
        "Denizli otogar","Sarayköy","Alaşehir","Salihli Garaj","Turgutlu",
        "Manisa Otogar","Bornova","İzmir Otogar"
    ],
    "İstanbul – Denizli": [
        "Esenler Otogar","Alibeyköy","Harem","Gebze Garaj","Bursa Otogar",
        "Susurluk","Balıkesir","Kırkağaç","Soma","Akhisar","Manisa Otogar",
        "Turgutlu Garaj","Salihli Garaj","Alaşehir Otogar","Denizli otogar"
    ],
    "İzmir – Denizli": [
        "İzmir Otogar","Bornova","Manisa Otogar","Turgutlu Garaj","Salihli Garaj",
        "Alaşehir Otogar","Sarayköy","Denizli otogar"
    ],
    "İstanbul – Antalya": [
        "Esenler","Alibeyköy","Harem","Gebze","Bursa","Korkuteli","Antalya Otogar"
    ],
    "Antalya – İstanbul": [
        "Antalya Otogar","Korkuteli","Bursa","Gebze","Harem","Alibeyköy","Esenler"
    ],
}

# DB'deki hatlarla birleşik durak getirici
def get_stops(route_name: str):
    if route_name in ROUTE_STOPS:
        return ROUTE_STOPS[route_name]
    db = get_db()
    row = db.execute("SELECT stops FROM routes WHERE name=?", (route_name,)).fetchone()
    if row:
        try:
            return json.loads(row["stops"]) or []
        except Exception:
            return []
    return ROUTE_STOPS["Denizli – İstanbul"]

# ---------------- Global şablon değişkeni ----------------
@app.context_processor
def inject_active_trip():
    try:
        tid = get_active_trip()
        if not tid:
            return dict(active_trip=None)
        db = get_db()
        trip = db.execute("SELECT * FROM trips WHERE id=?", (tid,)).fetchone()
        return dict(active_trip=trip)
    except Exception:
        return dict(active_trip=None)

# ---------------- Sayfalar ----------------
@app.route("/")
def index():
    db = get_db()
    dyn = [r["name"] for r in db.execute("SELECT name FROM routes ORDER BY name").fetchall()]
    all_routes = list(ROUTE_STOPS.keys()) + dyn
    current_route = session.get("route", all_routes[0] if all_routes else "Denizli – İstanbul")
    return render_template("index.html", current_route=current_route, all_routes=all_routes)

@app.route("/hizli-koltuk")
def quick_seat():
    return redirect(url_for("seats"))

@app.route("/set-route", methods=["POST"])
def set_route():
    payload = request.get_json(silent=True) or {}
    route = request.form.get("route") or payload.get("route")
    if not route:
        return jsonify({"ok": False, "msg": "route gerekli"}), 400
    session["route"] = route
    return jsonify({"ok": True, "route": route})

# --------- Hat Ekle ----------
@app.route("/hat-ekle", methods=["GET", "POST"])
def add_route():
    if request.method == "POST":
        name = (request.form.get("name") or "").strip()
        stops_text = (request.form.get("stops") or "").strip()
        if not name or not stops_text:
            return "Hat adı ve duraklar zorunludur", 400
        stops = [s.strip() for s in stops_text.split(",") if s.strip()]
        db = get_db()
        db.execute(
            "INSERT OR REPLACE INTO routes(name, stops) VALUES(?, ?)",
            (name, json.dumps(stops, ensure_ascii=False))
        )
        db.commit()
        session["route"] = name
        flash("Hat kaydedildi ve seçildi.", "success")
        return redirect(url_for("index"))
    return render_template("add_route.html")

@app.route("/sefer-baslat", methods=["GET", "POST"])
def trip_start():
    if request.method == "POST":
        db = get_db()
        date_val = request.form.get("date") or datetime.now().strftime("%Y-%m-%d")
        time_val = request.form.get("departure_time") or datetime.now().strftime("%H:%M")
        db.execute(
            """
            INSERT INTO trips (date, route, departure_time, plate,
                               captain1, captain2, attendant, note)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                date_val,
                session.get("route", "Denizli – İstanbul"),
                time_val,
                request.form.get("plate"),
                request.form.get("captain1"),
                request.form.get("captain2"),
                request.form.get("attendant"),
                request.form.get("note"),
            ),
        )
        trip_id = db.execute("SELECT last_insert_rowid()").fetchone()[0]
        db.commit()
        set_active_trip(trip_id)
        flash("Sefer başlatıldı.", "success")
        return redirect(url_for("seats"))

    now_str = datetime.now().strftime("%Y-%m-%d %H:%M")
    return render_template(
        "start_trip.html",
        now=now_str,
        current_route=session.get("route", "Denizli – İstanbul")
    )

@app.route("/continue-trip")
def continue_trip():
    tid = get_active_trip()
    if tid:
        return redirect(url_for("seats"))
    return redirect(url_for("trip_start"))

@app.route("/seats")
def seats():
    tid = get_active_trip()
    if not tid:
        return redirect(url_for("trip_start"))

    db = get_db()
    trip = db.execute("SELECT * FROM trips WHERE id=?", (tid,)).fetchone()
    if not trip:
        set_active_trip(None)
        return redirect(url_for("trip_start"))

    route_name = trip["route"]
    stops = get_stops(route_name)

    rows = db.execute(
        "SELECT seat_no, stop FROM seats WHERE trip_id=? ORDER BY seat_no", (tid,)
    ).fetchall()
    assigned_map = {r["seat_no"]: r["stop"] for r in rows}

    return render_template("seats.html", trip=trip, stops=stops, assigned=assigned_map)

# ---------- Yardımcı: metinden durak listesi üret ----------
def parse_stops(text: str) -> list[str]:
    if not text:
        return []
    parts = []
    for line in text.splitlines():  # satır satır destek
        parts.extend(x.strip() for x in line.split(","))  # virgül de olur
    return [p for p in (x.strip() for x in parts) if p]

# ---------- Hatlar listesi (/hatlar) ----------
@app.route("/hatlar")
def routes_list():
    db = get_db()
    rows = db.execute("SELECT id, name FROM routes ORDER BY name").fetchall()
    # Sabit (hardcoded) hatlar da gösterilsin ama düzenlenemez/silinemez:
    builtins = [{"name": k} for k in ROUTE_STOPS.keys()]
    return render_template("routes_list.html", routes=rows, builtin_routes=builtins)

# ---------- Hat düzenle (/hat/<id>/duzenle) ----------
@app.route("/hat/<int:rid>/duzenle", methods=["GET", "POST"])
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

        db.execute("UPDATE routes SET name=?, stops=? WHERE id=?",
                   (name, json.dumps(stops, ensure_ascii=False), rid))
        db.commit()
        session["route"] = name  # düzenlenen hattı seçili yap
        flash("Hat güncellendi.", "success")
        return redirect(url_for("routes_list"))

    try:
        stops_text = "\n".join(json.loads(row["stops"]) or [])
    except Exception:
        stops_text = ""
    return render_template("route_edit.html", route=row, stops_text=stops_text)

# ---------- Hat sil (/hat/<id>/sil) ----------
@app.route("/hat/<int:rid>/sil", methods=["POST"])
def route_delete(rid):
    db = get_db()
    cur_name = session.get("route")
    row = db.execute("SELECT name FROM routes WHERE id=?", (rid,)).fetchone()
    db.execute("DELETE FROM routes WHERE id=?", (rid,))
    db.commit()
    if row and cur_name == row["name"]:
        session.pop("route", None)  # seçili rota silindiyse temizle
    flash("Hat silindi.", "info")
    return redirect(url_for("routes_list"))

# ---- Koltuk kayıt/sil API ----
@app.route("/api/seat", methods=["POST", "DELETE"])
def api_seat():
    tid = get_active_trip()
    if not tid:
        return jsonify({"ok": False, "msg": "Aktif sefer yok"}), 400

    db = get_db()

    if request.method == "DELETE":
        try:
            seat_no = int(request.args.get("seat_no"))
        except (TypeError, ValueError):
            return jsonify({"ok": False, "msg": "seat_no geçersiz"}), 400
        db.execute("DELETE FROM seats WHERE trip_id=? AND seat_no=?", (tid, seat_no))
        db.commit()
        return jsonify({"ok": True})

    data = request.get_json(force=True) or {}
    try:
        seat_no = int(data.get("seat_no"))
    except (TypeError, ValueError):
        return jsonify({"ok": False, "msg": "seat_no gerekli"}), 400

    stop = (data.get("stop") or "").strip()
    ticket_type = (data.get("ticket_type") or "biletsiz").strip().lower()
    payment = (data.get("payment") or "nakit").strip().lower()

    raw_amount = data.get("amount", 0)
    try:
        amount = float(raw_amount or 0)
    except (TypeError, ValueError):
        amount = 0.0

    db.execute(
        """
        INSERT INTO seats(trip_id, seat_no, stop, ticket_type, payment, amount)
        VALUES(?, ?, ?, ?, ?, ?)
        ON CONFLICT(trip_id, seat_no) DO UPDATE SET
            stop=excluded.stop,
            ticket_type=excluded.ticket_type,
            payment=excluded.payment,
            amount=excluded.amount
        """,
        (tid, seat_no, stop, ticket_type, payment, amount),
    )
    db.commit()
    return jsonify({"ok": True})

# ---- YENİ: Seferi sonlandır ----
@app.route("/end-trip", methods=["POST"])
def end_trip():
    """
    Aktif seferi kapatır: active_trip_id=NULL yapar, kullanıcıyı ana sayfaya atar.
    (Koltuk verileri DB'de kalır; rapor/özet için kullanılabilir.)
    """
    set_active_trip(None)
    flash("Sefer sonlandırıldı.", "info")
    return redirect(url_for("index"))

# ---- YENİ: Aktif seferin duraklarını ver ----
@app.route("/api/stops")
def api_stops():
    """
    Aktif seferin hattına ait durakları sırayla döner.
    Örn: {"ok": true, "stops": ["İzmir Otogar", "Bornova", ...]}
    """
    tid = get_active_trip()
    if not tid:
        return jsonify({"ok": False, "msg": "Aktif sefer yok", "stops": []}), 400

    db = get_db()
    trip = db.execute("SELECT route FROM trips WHERE id=?", (tid,)).fetchone()
    if not trip:
        return jsonify({"ok": False, "msg": "Sefer bulunamadı", "stops": []}), 404

    route_name = trip["route"]
    stops = get_stops(route_name)
    return jsonify({"ok": True, "stops": stops, "route": route_name})

# ---- Basit sağlık testi ----
@app.route("/health")
def health():
    return {"ok": True, "active_trip": get_active_trip()}

# ---------------- Çalıştırma ----------------
if __name__ == "__main__":
    with app.app_context():
        ensure_schema()
    app.run(host="0.0.0.0", port=5000, debug=True)
