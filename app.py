# app.py
import os
import json
import sqlite3
import secrets
from datetime import datetime
from typing import Tuple, Optional
from pathlib import Path

from flask import (
    Flask, render_template, request, redirect, url_for,
    jsonify, g, session, abort, send_from_directory
)
from werkzeug.utils import secure_filename

# === Hız limiti (OSM) için blueprint (harici modülde url_prefix ayarlı olmalı) ===
# Örn: speedlimit.py içinde: bp_speed = Blueprint("speed", __name__, url_prefix="/api/speedlimit")
from speedlimit import bp_speed

# ===================== Ayarlar =====================

def env_bool(name: str, default: bool = False) -> bool:
    v = os.getenv(name)
    if v is None:
        return default
    return v.lower() in ("1", "true", "yes", "on")

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "degistir-beni")

DB_PATH = os.getenv("DB_PATH", "db.sqlite3")
DEBUG = env_bool("FLASK_DEBUG", True)
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD", "volkan")

# ============== Emanet/Foto Ayarları ==============
UPLOAD_DIR = os.getenv(
    "UPLOAD_DIR", os.path.join(os.getcwd(), "uploads", "consignments")
)
ALLOWED_IMAGE_EXTS = {".jpg", ".jpeg", ".png", ".webp"}
ALLOWED_IMAGE_MIMES = {"image/jpeg", "image/png", "image/webp"}
MAX_UPLOAD_MB = int(os.getenv("MAX_UPLOAD_MB", "10"))
app.config["MAX_CONTENT_LENGTH"] = MAX_UPLOAD_MB * 1024 * 1024

def ensure_upload_dir():
    Path(UPLOAD_DIR).mkdir(parents=True, exist_ok=True)

def _allowed_file(filename: str) -> bool:
    if not filename or "." not in filename:
        return False
    ext = "." + filename.rsplit(".", 1)[1].lower()
    return ext in ALLOWED_IMAGE_EXTS

# ==== Rapor sabitleri (koltuk numaraları) ====
SEAT_NUMBERS = [
    1, 3, 4, 5, 7, 8, 9, 11, 12, 13, 15, 16, 17, 19, 20, 21, 23, 24,
    25, 27, 28, 29, 31, 33, 34, 35, 37, 38, 39, 41, 42, 43, 45, 46,
    49, 50, 51, 52, 53, 54
]

# Whitelist & normalizer’lar
TICKET_TYPES = {"biletli", "biletsiz", "ucretsiz"}
PAYMENT_TYPES = {"nakit", "iban", "online", "pos", "ucretsiz"}

def norm_ticket_type(val: str) -> str:
    v = (val or "").strip().lower()
    return v if v in TICKET_TYPES else "biletsiz"

def norm_payment(val: str) -> str:
    v = (val or "").strip().lower()
    return v if v in PAYMENT_TYPES else "nakit"

def norm_gender(val: str) -> str:
    v = (val or "").strip().lower()
    return v if v in ("bay", "bayan", "") else ""

def norm_bool(val) -> int:
    if isinstance(val, bool):
        return 1 if val else 0
    s = str(val or "").strip().lower()
    return 1 if s in ("1", "true", "yes", "on") else 0

# ===================== DB Yardımcıları =====================

def get_db():
    if "db" not in g:
        g.db = sqlite3.connect(DB_PATH)
        g.db.row_factory = sqlite3.Row
        g.db.execute("PRAGMA foreign_keys=ON;")
        g.db.execute("PRAGMA journal_mode=WAL;")
    return g.db

@app.teardown_appcontext
def close_db(exc):
    db = g.pop("db", None)
    if db is not None:
        db.close()

def ensure_schema():
    """İlk açılışta tablo ve indeksleri hazırla; eksik kolonları ekle."""
    db = get_db()
    db.executescript(
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
            ticket_type TEXT,
            payment TEXT,
            amount REAL,
            gender TEXT DEFAULT '',
            pair_ok INTEGER DEFAULT 0,
            service INTEGER DEFAULT 0,
            service_note TEXT,
            PRIMARY KEY(trip_id, seat_no)
        );

        CREATE TABLE IF NOT EXISTS routes(
            id INTEGER PRIMARY KEY,
            name TEXT UNIQUE,
            stops TEXT
        );

        CREATE TABLE IF NOT EXISTS walk_on_sales(
            id INTEGER PRIMARY KEY,
            trip_id INTEGER NOT NULL,
            from_stop TEXT NOT NULL,
            to_stop TEXT NOT NULL,
            pax INTEGER NOT NULL DEFAULT 1,
            unit_price REAL NOT NULL DEFAULT 0,
            total_amount REAL NOT NULL DEFAULT 0,
            payment TEXT NOT NULL DEFAULT 'nakit',
            note TEXT,
            created_at TEXT DEFAULT (datetime('now','localtime'))
        );

        CREATE INDEX IF NOT EXISTS idx_walkon_trip        ON walk_on_sales(trip_id);
        CREATE INDEX IF NOT EXISTS idx_seats_trip         ON seats(trip_id);
        CREATE INDEX IF NOT EXISTS idx_seats_trip_payment ON seats(trip_id, payment);
        CREATE INDEX IF NOT EXISTS idx_seats_trip_stop    ON seats(trip_id, stop);
        CREATE INDEX IF NOT EXISTS idx_trips_date         ON trips(date);

        -- Durak koordinatları
        CREATE TABLE IF NOT EXISTS route_stop_coords(
            route TEXT NOT NULL,
            stop  TEXT NOT NULL,
            lat   REAL NOT NULL,
            lng   REAL NOT NULL,
            PRIMARY KEY(route, stop)
        );
        CREATE INDEX IF NOT EXISTS idx_coords_route ON route_stop_coords(route);

        -- Durak olay günlüğü
        CREATE TABLE IF NOT EXISTS stop_logs(
            id             INTEGER PRIMARY KEY,
            trip_id        INTEGER NOT NULL,
            stop_name      TEXT    NOT NULL,
            event          TEXT    NOT NULL,  -- 'approach' | 'arrive' | 'depart'
            distance_km    REAL,
            seats_for_stop INTEGER,
            meta_json      TEXT,
            ts             TEXT NOT NULL DEFAULT (datetime('now','localtime'))
        );
        CREATE INDEX IF NOT EXISTS idx_stoplogs_trip_ts ON stop_logs(trip_id, ts);

        -- Emanetler
        CREATE TABLE IF NOT EXISTS consignments(
            id            INTEGER PRIMARY KEY,
            trip_id       INTEGER,
            code          TEXT UNIQUE,
            item_name     TEXT,
            item_type     TEXT,
            from_name     TEXT,
            from_phone    TEXT,
            to_name       TEXT,
            to_phone      TEXT,
            from_stop     TEXT,
            to_stop       TEXT,
            amount        REAL    DEFAULT 0,
            payment       TEXT    DEFAULT 'nakit',
            status        TEXT    DEFAULT 'bekliyor',
            notes         TEXT,
            created_at    TEXT    DEFAULT (datetime('now','localtime')),
            updated_at    TEXT,
            delivered_at  TEXT,
            FOREIGN KEY(trip_id) REFERENCES trips(id)
        );

        CREATE INDEX IF NOT EXISTS idx_cons_trip    ON consignments(trip_id);
        CREATE INDEX IF NOT EXISTS idx_cons_status  ON consignments(status);
        CREATE INDEX IF NOT EXISTS idx_cons_created ON consignments(created_at);

        -- Emanet Fotoğrafları (çoklu)
        CREATE TABLE IF NOT EXISTS consignment_photos(
            id              INTEGER PRIMARY KEY,
            consignment_id  INTEGER NOT NULL,
            role            TEXT,      -- pickup|delivery|other
            file_path       TEXT NOT NULL,
            mime            TEXT,
            size_bytes      INTEGER,
            created_at      TEXT DEFAULT (datetime('now','localtime')),
            FOREIGN KEY(consignment_id) REFERENCES consignments(id) ON DELETE CASCADE
        );

        CREATE INDEX IF NOT EXISTS idx_cphotos_cons    ON consignment_photos(consignment_id);
        CREATE INDEX IF NOT EXISTS idx_cphotos_created ON consignment_photos(created_at);

        -- Fiyatlar
        CREATE TABLE IF NOT EXISTS fares(
            route      TEXT    NOT NULL,
            from_stop  TEXT    NOT NULL,
            to_stop    TEXT    NOT NULL,
            price      REAL    NOT NULL,
            updated_at TEXT    DEFAULT (datetime('now','localtime')),
            PRIMARY KEY(route, from_stop, to_stop)
        );
        CREATE INDEX IF NOT EXISTS idx_fares_route ON fares(route);
        """
    )

    # Eski tablolarda eksik kolonlar
    cols = [r["name"] for r in db.execute("PRAGMA table_info(seats)").fetchall()]
    if "gender" not in cols:
        db.execute("ALTER TABLE seats ADD COLUMN gender TEXT DEFAULT ''")
    if "pair_ok" not in cols:
        db.execute("ALTER TABLE seats ADD COLUMN pair_ok INTEGER DEFAULT 0")
    if "service" not in cols:
        db.execute("ALTER TABLE seats ADD COLUMN service INTEGER DEFAULT 0")
    if "service_note" not in cols:
        db.execute("ALTER TABLE seats ADD COLUMN service_note TEXT")
    db.commit()

def set_active_trip(trip_id: Optional[int]):
    db = get_db()
    db.execute("UPDATE app_state SET active_trip_id=?", (trip_id,))
    db.commit()

def get_active_trip() -> Optional[int]:
    db = get_db()
    row = db.execute("SELECT active_trip_id FROM app_state WHERE id=1").fetchone()
    return row["active_trip_id"] if row else None

# ===================== Rotalar & Duraklar =====================

ROUTE_STOPS = {
    "Denizli – İstanbul": [
        "Denizli otogar","Sarayköy","Buldan","Bozalan","Derbent(Denizli)","Kadıköy",
        "İl Sınırı(Manisa)","Dindarlı","Dadağlı","Sarıgöl Garaj","Afşar","Bereketli",
        "Hacıaliler","Ortahan","Belenyaka","Alaşehir Otogar","Alaşehir Stadyum",
        "Akkeçili","Piyadeler","Kavaklıdere","Salihli Garaj","Sart","Ahmetli",
        "Gökkaya","Akçapınar","Derbent(Turgutlu)","Turgutlu Garaj","Özdilek(Turgutlu)",
        "Manisa Otogar","Akhisar","Saruhanlı","Soma","Kırkağaç","Balıkesir","Susurluk",
        "Mustafa K.P(Bursa)","Bursa Otogar","Gebze Garaj","Harem","Alibeyköy","Esenler Otogar"
    ],
    "Denizli – İzmir": [
        "Denizli otogar","Sarayköy","Alaşehir","Salihli Garaj","Turgutlu","Manisa Otogar","Bornova","İzmir Otogar"
    ],
    "İstanbul – Denizli": [
        "Esenler Otogar","Alibeyköy","Harem","Gebze Garaj","Bursa Otogar","Susurluk","Balıkesir",
        "Kırkağaç","Soma","Akhisar","Manisa Otogar","Turgutlu Garaj","Salihli Garaj","Alaşehir Otogar","Denizli otogar"
    ],
    "İzmir – Denizli": [
        "İzmir Otogar","Bornova","Manisa Otogar","Turgutlu Garaj","Salihli Garaj","Alaşehir Otogar","Sarayköy","Denizli otogar"
    ],
    "İstanbul – Antalya": ["Esenler","Alibeyköy","Harem","Gebze","Bursa","Korkuteli","Antalya Otogar"],
    "Antalya – İstanbul": ["Antalya Otogar","Korkuteli","Bursa","Gebze","Harem","Alibeyköy","Esenler"],
}

def get_stops(route_name: str):
    db = get_db()
    row = db.execute("SELECT stops FROM routes WHERE name=?", (route_name,)).fetchone()
    if row:
        try:
            return json.loads(row["stops"]) or []
        except Exception:
            pass
    if route_name in ROUTE_STOPS:
        return ROUTE_STOPS[route_name]
    return ROUTE_STOPS.get("Denizli – İstanbul", [])

# ===================== Yan koltuk kuralı =====================

NEIGHBORS = {
    3:4, 4:3, 7:8, 8:7, 11:12, 12:11, 15:16, 16:15,
    19:20, 20:19, 23:24, 24:23, 27:28, 28:27, 33:34, 34:33,
    37:38, 38:37, 41:42, 42:41, 45:46, 46:45, 49:50, 50:49, 53:54, 54:53,
    # 51-52 yan yana ise aç:
    # 51:52, 52:51,
}

def neighbor_rule_ok(trip_id:int, seat_no:int, gender:str, pair_ok:bool) -> Tuple[bool, str]:
    nb = NEIGHBORS.get(seat_no)
    if not nb or not gender:
        return True, ""
    db = get_db()
    row = db.execute(
        "SELECT gender, COALESCE(pair_ok,0) AS pair_ok FROM seats WHERE trip_id=? AND seat_no=?",
        (trip_id, nb)
    ).fetchone()
    if not row:
        return True, ""  # komşu boş
    nb_gender = norm_gender(row["gender"])
    nb_pair_ok = bool(row["pair_ok"])
    if gender in ("bay","bayan") and nb_gender in ("bay","bayan"):
        if gender != nb_gender and not (pair_ok or nb_pair_ok):
            return False, f"Yan koltuk {nb} '{nb_gender}' kayıtlı. İstisna işaretlenmeden farklı cins yan yana oturtulamaz."
    return True, ""

# ===================== CSRF & Kimlik =====================

def issue_csrf():
    token = secrets.token_urlsafe(32)
    session["csrf_token"] = token
    return token

def get_csrf():
    tok = session.get("csrf_token")
    if not tok:
        tok = issue_csrf()
    return tok

def check_csrf():
    form_tok = request.form.get("csrf_token")
    header_tok = request.headers.get("X-CSRF-Token")
    json_tok = None
    if request.is_json:
        data = request.get_json(silent=True) or {}
        json_tok = data.get("csrf_token")
    supplied = form_tok or header_tok or json_tok
    if not supplied or supplied != session.get("csrf_token"):
        abort(403, description="CSRF doğrulaması başarısız")

PROTECTED_PREFIXES = ("/",)  # Tam koruma; istersen daraltabilirsin
EXCLUDE_PREFIXES = ("/login", "/logout", "/health", "/api/speedlimit")  # Gerekirse "/u" ekle

def is_excluded_path(p: str) -> bool:
    return any(p == x or p.startswith(x + "/") for x in EXCLUDE_PREFIXES)

# ---- Tek before_request: hem schema+upload hazırlar, hem kimlik/CSRF kontrol eder ----
@app.before_request
def bootstrap_and_guard():
    if not app.config.get("_schema_ready"):
        ensure_schema()
        ensure_upload_dir()
        app.config["_schema_ready"] = True

    p = request.path
    if any(p.startswith(pref) for pref in PROTECTED_PREFIXES) and not is_excluded_path(p):
        if not session.get("auth_ok"):
            return redirect(url_for("login", next=p))
        if request.method in ("POST", "PUT", "PATCH", "DELETE"):
            check_csrf()

@app.context_processor
def inject_globals():
    try:
        tid = get_active_trip()
        trip = None
        if tid:
            db = get_db()
            trip = db.execute("SELECT * FROM trips WHERE id=?", (tid,)).fetchone()
        return dict(active_trip=trip, csrf_token=get_csrf())
    except Exception:
        return dict(active_trip=None, csrf_token=get_csrf())

# ===================== Kimlik sayfaları =====================

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        pwd = (request.form.get("password") or "").strip()
        if pwd == ADMIN_PASSWORD:
            session["auth_ok"] = True
            issue_csrf()
            nxt = request.args.get("next") or url_for("index")
            return redirect(nxt)
        return render_template("login.html", error="Hatalı şifre", csrf_token=get_csrf())
    return render_template("login.html", csrf_token=get_csrf())

@app.route("/logout", methods=["POST"])
def logout():
    session.clear()
    return redirect(url_for("login"))

# ===================== Sayfalar =====================

@app.route("/")
def index():
    db = get_db()
    dyn = [r["name"] for r in db.execute("SELECT name FROM routes ORDER BY name").fetchall()]
    all_routes = list(dict.fromkeys(list(ROUTE_STOPS.keys()) + dyn))
    current_route = session.get("route", all_routes[0] if all_routes else "Denizli – İstanbul")
    return render_template("index.html", current_route=current_route, all_routes=all_routes)

@app.route("/set-route", methods=["POST"])
def set_route():
    payload = request.get_json(silent=True) or {}
    route = (request.form.get("route") or payload.get("route") or "").strip()
    if not route:
        return jsonify({"ok": False, "msg": "route gerekli"}), 400
    db = get_db()
    dyn = [r["name"] for r in db.execute("SELECT name FROM routes").fetchall()]
    all_routes = set(list(ROUTE_STOPS.keys()) + dyn)
    if route not in all_routes:
        return jsonify({"ok": False, "msg": "Geçersiz hat"}), 400
    session["route"] = route
    return jsonify({"ok": True, "route": route})

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
        "SELECT seat_no, stop, gender, COALESCE(service,0) AS service, COALESCE(service_note,'') AS service_note "
        "FROM seats WHERE trip_id=? ORDER BY seat_no",
        (tid,)
    ).fetchall()

    assigned_map   = {r["seat_no"]: True for r in rows}
    stops_map      = {r["seat_no"]: (r["stop"] or "") for r in rows}
    gender_map     = {r["seat_no"]: (r["gender"] or "") for r in rows}
    service_map    = {r["seat_no"]: bool(r["service"]) for r in rows}
    service_notes  = {r["seat_no"]: (r["service_note"] or "") for r in rows}

    return render_template(
        "seats.html",
        trip=trip,
        stops=stops,
        assigned=assigned_map,
        stops_map=stops_map,
        genders=gender_map,
        service_map=service_map,
        service_notes=service_notes
    )

@app.route("/api/seats/list")
def api_seats_list():
    tid = get_active_trip()
    if not tid:
        return jsonify({"ok": False, "msg": "Aktif sefer yok", "items": []}), 400
    rows = get_db().execute("""
        SELECT seat_no, stop, ticket_type, payment, amount, gender,
               COALESCE(service,0) AS service, COALESCE(service_note,'') AS service_note
        FROM seats
        WHERE trip_id=?
        ORDER BY seat_no
    """, (tid,)).fetchall()
    items = [dict(r) for r in rows]
    return jsonify({"ok": True, "items": items})

@app.route("/yolcu-kontrol")
def passenger_control():
    tid = get_active_trip()
    if not tid:
        return redirect(url_for("trip_start"))
    db = get_db()
    trip = db.execute("SELECT * FROM trips WHERE id=?", (tid,)).fetchone()
    stops = get_stops(trip["route"])
    return render_template("passenger_control.html", trip=trip, stops=stops)

# --- /fiyat (sorgu) ---
@app.route("/fiyat", methods=["GET"])
def fare_query():
    routes = all_route_names()
    route = (request.args.get("route") or (routes[0] if routes else "")).strip()
    stops = list_stops_for_route(route)
    from_stop = (request.args.get("from") or "").strip()
    to_stop   = (request.args.get("to") or "").strip()

    price = None
    method = None
    msg = None
    if route and from_stop and to_stop:
        price, method = quote_price_segmented(route, from_stop, to_stop)
        if price is None:
            if method == "wrong-order":
                msg = "Biniş durak, inişten önce olmalı."
            elif method == "segment-missing":
                msg = "Segment fiyatı eksik. Yönetimden ekleyin."
            elif method == "missing-stops":
                msg = "Durak(lar) bu hatta yok."
            else:
                msg = "Fiyat bulunamadı."
        elif method == "same-stop":
            msg = "Aynı durak seçildi (0 TL)."

    return render_template(
        "fare_query.html",
        routes=routes,
        current_route=route,
        stops=stops,
        from_stop=from_stop,
        to_stop=to_stop,
        price=price,
        method=method,
        msg=msg,
        csrf_token=get_csrf(),
    )

# --- /fiyat-g (yönetim) ---
@app.route("/fiyat-g", methods=["GET", "POST"])
def fare_admin():
    routes = all_route_names()

    if request.method == "POST":
        route = (request.form.get("route") or (routes[0] if routes else "")).strip()
        from_stop = (request.form.get("from") or "").strip()
        to_stop   = (request.form.get("to") or "").strip()
        price_val = request.form.get("price")
        try:
            price = float(price_val)
        except (TypeError, ValueError):
            price = None
        if not from_stop or not to_stop or price is None:
            stops = list_stops_for_route(route)
            fare_list = get_db().execute(
                "SELECT from_stop, to_stop, price FROM fares WHERE route=? ORDER BY rowid",
                (route,)
            ).fetchall()
            return render_template(
                "fare_admin.html",
                routes=routes,
                current_route=route,
                stops=stops,
                from_stop=from_stop,
                to_stop=to_stop,
                current_price=price,
                fare_list=fare_list,
                csrf_token=get_csrf(),
            )
        db = get_db()
        db.execute("""
            INSERT INTO fares(route, from_stop, to_stop, price)
            VALUES(?, ?, ?, ?)
            ON CONFLICT(route, from_stop, to_stop) DO UPDATE SET
                price=excluded.price,
                updated_at=datetime('now','localtime')
        """, (route, from_stop, to_stop, price))
        db.commit()
    else:
        route = (request.args.get("route") or (routes[0] if routes else "")).strip()
        from_stop = (request.args.get("from") or "").strip()
        to_stop   = (request.args.get("to") or "").strip()

    stops = list_stops_for_route(route)
    row = get_db().execute(
        "SELECT price FROM fares WHERE route=? AND from_stop=? AND to_stop=?",
        (route, from_stop, to_stop)
    ).fetchone()
    current_price = float(row["price"]) if row else None

    fare_list = get_db().execute(
        "SELECT from_stop, to_stop, price FROM fares WHERE route=? ORDER BY rowid",
        (route,)
    ).fetchall()

    return render_template(
        "fare_admin.html",
        routes=routes,
        current_route=route,
        stops=stops,
        from_stop=from_stop,
        to_stop=to_stop,
        current_price=current_price,
        fare_list=fare_list,
        csrf_token=get_csrf(),
    )

# ===================== Raporlar & Olay Görüntüleyici =====================

def _parse_date(s: Optional[str]) -> Optional[str]:
    if not s:
        return None
    try:
        datetime.strptime(s, "%Y-%m-%d")
        return s
    except Exception:
        return None

@app.route("/raporlar")
def reports_page():
    db = get_db()
    dyn = [r["name"] for r in db.execute("SELECT name FROM routes ORDER BY name").fetchall()]
    all_routes = list(dict.fromkeys(list(ROUTE_STOPS.keys()) + dyn))
    return render_template("reports.html", all_routes=all_routes)

@app.route("/api/report/seat-stats")
def api_report_seat_stats():
    route = (request.args.get("route") or "").strip()
    d1 = _parse_date(request.args.get("date_from"))
    d2 = _parse_date(request.args.get("date_to"))

    sql_where = ["1=1"]
    args: list = []
    if route:
        sql_where.append("t.route = ?"); args.append(route)
    if d1:
        sql_where.append("t.date >= ?"); args.append(d1)
    if d2:
        sql_where.append("t.date <= ?"); args.append(d2)
    where = " AND ".join(sql_where)

    db = get_db()

    per = db.execute(
        f"""
        SELECT s.seat_no,
               COUNT(*)                  AS times,
               COALESCE(SUM(s.amount),0) AS revenue
        FROM seats s
        JOIN trips t ON t.id = s.trip_id
        WHERE {where}
        GROUP BY s.seat_no
        ORDER BY s.seat_no
        """,
        args
    ).fetchall()
    per_seat = [
        {"seat_no": int(r["seat_no"]), "times": int(r["times"]), "revenue": float(r["revenue"])}
        for r in per
    ]

    sold_seats = {p["seat_no"] for p in per_seat}
    never_sold = [n for n in SEAT_NUMBERS if n not in sold_seats]

    seat_tot = db.execute(
        f"""
        SELECT COALESCE(SUM(s.amount),0) AS revenue,
               COUNT(*) AS cnt
        FROM seats s JOIN trips t ON t.id=s.trip_id
        WHERE {where}
        """,
        args
    ).fetchone()

    walk_tot = db.execute(
        f"""
        SELECT COALESCE(SUM(w.total_amount),0) AS revenue,
               COALESCE(SUM(w.pax),0)         AS pax
        FROM walk_on_sales w JOIN trips t ON t.id=w.trip_id
        WHERE {where}
        """,
        args
    ).fetchone()

    top_seat = None
    if per_seat:
        top_seat = max(per_seat, key=lambda x: (x["times"], x["revenue"]))

    return jsonify({
        "ok": True,
        "filters": {"route": route or None, "date_from": d1, "date_to": d2},
        "totals": {
            "seated_count": int(seat_tot["cnt"] or 0),
            "seated_revenue": float(seat_tot["revenue"] or 0),
            "walk_pax": int(walk_tot["pax"] or 0),
            "walk_revenue": float(walk_tot["revenue"] or 0),
            "overall_revenue": float(seat_tot["revenue"] or 0) + float(walk_tot["revenue"] or 0),
        },
        "per_seat": per_seat,
        "top_seat": top_seat,
        "never_sold": never_sold,
    })

@app.route("/olaylar")
def events_page():
    return render_template("events.html")

@app.route("/api/events")
def api_events():
    route = (request.args.get("route") or "").strip()
    d1 = _parse_date(request.args.get("date_from"))
    d2 = _parse_date(request.args.get("date_to"))

    sql = """
    SELECT l.id, l.trip_id, t.date, t.route, l.stop_name, l.event, l.distance_km,
           l.seats_for_stop, l.meta_json, l.ts
    FROM stop_logs l
    JOIN trips t ON t.id = l.trip_id
    WHERE 1=1
    """
    args = []
    if route:
        sql += " AND t.route=?"; args.append(route)
    if d1:
        sql += " AND t.date >= ?"; args.append(d1)
    if d2:
        sql += " AND t.date <= ?"; args.append(d2)
    sql += " ORDER BY l.ts DESC, l.id DESC LIMIT 500"

    rows = get_db().execute(sql, args).fetchall()
    items = []
    for r in rows:
        try:
            meta = json.loads(r["meta_json"]) if r["meta_json"] else None
        except Exception:
            meta = None
        items.append({
            "id": r["id"], "trip_id": r["trip_id"], "date": r["date"], "route": r["route"],
            "stop_name": r["stop_name"], "event": r["event"], "distance_km": r["distance_km"],
            "seats_for_stop": r["seats_for_stop"], "meta": meta, "ts": r["ts"]
        })
    return jsonify({"ok": True, "items": items})

# ===================== Yardımcı =====================

def parse_stops(text: str) -> list[str]:
    if not text:
        return []
    parts = []
    for line in text.splitlines():
        parts.extend(x.strip() for x in line.split(","))
    return [p for p in (x.strip() for x in parts) if p]

# ===================== Hat CRUD (opsiyonel) =====================

@app.route("/hatlar")
def routes_list():
    db = get_db()
    rows = db.execute("SELECT id, name FROM routes ORDER BY name").fetchall()
    db_names = {r["name"] for r in rows}
    builtin_routes = []
    for k in ROUTE_STOPS.keys():
        builtin_routes.append({
            "name": k,
            "overridden": (k in db_names),
            "edit_url": url_for("builtin_route_edit", name=k),
        })
    return render_template("routes_list.html", routes=rows, builtin_routes=builtin_routes)

@app.route("/hat-ekle", methods=["GET", "POST"])
def add_route():
    if request.method == "POST":
        name = (request.form.get("name") or "").strip()
        stops_text = (request.form.get("stops") or "").strip()
        if not name or not stops_text:
            return "Hat adı ve duraklar zorunludur", 400
        stops = parse_stops(stops_text)
        db = get_db()
        db.execute(
            "INSERT OR REPLACE INTO routes(name, stops) VALUES(?, ?)",
            (name, json.dumps(stops, ensure_ascii=False))
        )
        db.commit()
        session["route"] = name
        return redirect(url_for("index"))
    return render_template("add_route.html")

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
        session["route"] = name
        return redirect(url_for("routes_list"))

    try:
        stops_text = "\n".join(json.loads(row["stops"]) or [])
    except Exception:
        stops_text = ""
    return render_template("route_edit.html", route=row, stops_text=stops_text)

def materialize_builtin_route(name: str) -> Optional[int]:
    stops = ROUTE_STOPS.get(name)
    if not stops:
        return None
    db = get_db()
    db.execute(
        "INSERT OR REPLACE INTO routes(name, stops) VALUES(?, ?)",
        (name, json.dumps(stops, ensure_ascii=False))
    )
    db.commit()
    row = db.execute("SELECT id FROM routes WHERE name=?", (name,)).fetchone()
    return row["id"] if row else None

@app.route("/hat/builtin/duzenle")
def builtin_route_edit():
    name = (request.args.get("name") or "").strip()
    if name not in ROUTE_STOPS:
        abort(404, description="Sabit hat bulunamadı")
    rid = materialize_builtin_route(name)
    if not rid:
        abort(500, description="Sabit hat DB'ye kopyalanamadı")
    session["route"] = name
    return redirect(url_for("route_edit", rid=rid))

@app.route("/hat/<int:rid>/sil", methods=["POST"])
def route_delete(rid):
    db = get_db()
    cur_name = session.get("route")
    row = db.execute("SELECT name FROM routes WHERE id=?", (rid,)).fetchone()
    db.execute("DELETE FROM routes WHERE id=?", (rid,))
    db.commit()
    if row and cur_name == row["name"]:
        session.pop("route", None)
    return redirect(url_for("routes_list"))

def all_route_names() -> list[str]:
    db = get_db()
    dyn = [r["name"] for r in db.execute("SELECT name FROM routes ORDER BY name").fetchall()]
    return list(dict.fromkeys(list(ROUTE_STOPS.keys()) + dyn))

def list_stops_for_route(route_name: str) -> list[str]:
    return get_stops(route_name)

def fetch_fare_exact(route: str, from_stop: str, to_stop: str) -> Optional[float]:
    row = get_db().execute(
        "SELECT price FROM fares WHERE route=? AND from_stop=? AND to_stop=?",
        (route, from_stop, to_stop)
    ).fetchone()
    return float(row["price"]) if row else None

def quote_price_segmented(route: str, from_stop: str, to_stop: str) -> tuple[Optional[float], str]:
    stops = list_stops_for_route(route)
    if not stops or from_stop not in stops or to_stop not in stops:
        return None, "missing-stops"
    i, j = stops.index(from_stop), stops.index(to_stop)
    if i == j:
        return 0.0, "same-stop"
    if i > j:
        return None, "wrong-order"
    exact = fetch_fare_exact(route, from_stop, to_stop)
    if exact is not None:
        return exact, "direct"
    total = 0.0
    db = get_db()
    for k in range(i, j):
        a, b = stops[k], stops[k+1]
        row = db.execute(
            "SELECT price FROM fares WHERE route=? AND from_stop=? AND to_stop=?",
            (route, a, b)
        ).fetchone()
        if not row:
            return None, "segment-missing"
        total += float(row["price"])
    return total, "summed"

# ===================== Durak doğrulama =====================

def validate_stop_for_active_trip(stop: str) -> bool:
    tid = get_active_trip()
    if not tid:
        return False
    db = get_db()
    trip = db.execute("SELECT route FROM trips WHERE id=?", (tid,)).fetchone()
    if not trip:
        return False
    allowed = set(get_stops(trip["route"]))
    return (stop or "").strip() in allowed

# ===================== API: Seat (tekli) =====================

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
    if stop and not validate_stop_for_active_trip(stop):
        return jsonify({"ok": False, "msg": "Durak bu hat üzerinde değil"}), 400

    ticket_type = norm_ticket_type(data.get("ticket_type") or "biletsiz")
    payment = norm_payment(data.get("payment") or "nakit")

    raw_amount = data.get("amount", 0)
    try:
        amount = float(raw_amount or 0)
    except (TypeError, ValueError):
        amount = 0.0

    gender = norm_gender(data.get("gender") or "")
    pair_ok = bool(data.get("pair_ok"))
    service = norm_bool(data.get("service"))
    service_note = (data.get("service_note") or "").strip()

    ok, msg = neighbor_rule_ok(tid, seat_no, gender, pair_ok)
    if not ok:
        return jsonify({"ok": False, "msg": msg}), 400

    db.execute(
        """
        INSERT INTO seats(trip_id, seat_no, stop, ticket_type, payment, amount, gender, pair_ok, service, service_note)
        VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ON CONFLICT(trip_id, seat_no) DO UPDATE SET
            stop=excluded.stop,
            ticket_type=excluded.ticket_type,
            payment=excluded.payment,
            amount=excluded.amount,
            gender=excluded.gender,
            pair_ok=excluded.pair_ok,
            service=excluded.service,
            service_note=excluded.service_note
        """,
        (tid, seat_no, stop, ticket_type, payment, amount, gender, 1 if pair_ok else 0, service, service_note),
    )
    db.commit()
    return jsonify({"ok": True})

# ===================== API: Seats bulk =====================

@app.route("/api/seats/bulk", methods=["POST", "DELETE"])
def api_seats_bulk():
    tid = get_active_trip()
    if not tid:
        return jsonify({"ok": False, "msg": "Aktif sefer yok"}), 400
    db = get_db()

    if request.method == "DELETE":
        raw = (request.args.get("seats") or "").strip()
        if not raw:
            return jsonify({"ok": False, "msg": "seats parametresi gerekli"}), 400
        try:
            seat_list = [int(x) for x in raw.split(",") if x.strip()]
        except ValueError:
            return jsonify({"ok": False, "msg": "seats geçersiz"}), 400
        db.executemany(
            "DELETE FROM seats WHERE trip_id=? AND seat_no=?",
            [(tid, s) for s in seat_list]
        )
        db.commit()
        return jsonify({"ok": True, "deleted": seat_list})

    data = request.get_json(force=True) or {}
    seats = data.get("seats")
    if not seats or not isinstance(seats, list):
        return jsonify({"ok": False, "msg": "seats listesi gerekli"}), 400

    stop = (data.get("stop") or "").strip()
    if stop and not validate_stop_for_active_trip(stop):
        return jsonify({"ok": False, "msg": "Durak bu hat üzerinde değil"}), 400

    ticket_type = norm_ticket_type(data.get("ticket_type") or "biletsiz")
    payment = norm_payment(data.get("payment") or "nakit")
    default_amount = data.get("amount", 0)
    try:
        default_amount = float(default_amount or 0)
    except (TypeError, ValueError):
        default_amount = 0.0

    rows = []
    try:
        for item in seats:
            if isinstance(item, dict):
                s_no = int(item.get("seat_no"))
                stp = (item.get("stop") or stop).strip()
                if stp and not validate_stop_for_active_trip(stp):
                    return jsonify({"ok": False, "msg": f"Durak hat üzerinde değil: {stp}"}), 400
                ttype = norm_ticket_type(item.get("ticket_type") or ticket_type)
                pay = norm_payment(item.get("payment") or payment)
                amt_raw = item.get("amount", default_amount)
                try:
                    amt = float(amt_raw or 0)
                except (TypeError, ValueError):
                    amt = 0.0
                gen = norm_gender(item.get("gender") or "")
                p_ok = bool(item.get("pair_ok"))
                svc = norm_bool(item.get("service"))
                svc_note = (item.get("service_note") or "").strip()
                ok, msg = neighbor_rule_ok(tid, s_no, gen, p_ok) if gen else (True, "")
                if not ok:
                    return jsonify({"ok": False, "msg": msg}), 400
            else:
                s_no = int(item)
                stp, ttype, pay, amt = stop, ticket_type, payment, default_amount
                gen, p_ok = "", False
                svc, svc_note = 0, ""
            rows.append((tid, s_no, stp, ttype, pay, amt, gen, 1 if p_ok else 0, svc, svc_note))
    except (TypeError, ValueError):
        return jsonify({"ok": False, "msg": "seats içeriği geçersiz"}), 400

    db.executemany(
        """
        INSERT INTO seats(trip_id, seat_no, stop, ticket_type, payment, amount, gender, pair_ok, service, service_note)
        VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ON CONFLICT(trip_id, seat_no) DO UPDATE SET
            stop=excluded.stop,
            ticket_type=excluded.ticket_type,
            payment=excluded.payment,
            amount=excluded.amount,
            gender=excluded.gender,
            pair_ok=excluded.pair_ok,
            service=excluded.service,
            service_note=excluded.service_note
        """,
        rows
    )
    db.commit()
    return jsonify({"ok": True, "count": len(rows)})

# === ALIAS: /api/seats/offload (frontend uyumu) ===
@app.route("/api/seats/offload", methods=["POST"])
def api_seats_offload_alias():
    tid = get_active_trip()
    if not tid:
        return jsonify({"ok": False, "msg": "Aktif sefer yok"}), 400
    data = request.get_json(force=True) or {}
    seats = data.get("seats")
    if not seats or not isinstance(seats, list):
        return jsonify({"ok": False, "msg": "seats listesi gerekli"}), 400
    try:
        seat_list = [int(x if not isinstance(x, dict) else x.get("seat_no")) for x in seats]
        seat_list = [s for s in seat_list if isinstance(s, int)]
    except Exception:
        return jsonify({"ok": False, "msg": "seats geçersiz"}), 400
    db = get_db()
    db.executemany(
        "DELETE FROM seats WHERE trip_id=? AND seat_no=?",
        [(tid, s) for s in seat_list]
    )
    db.commit()
    return jsonify({"ok": True, "deleted": seat_list})

# ===================== API: Stops =====================

@app.route("/api/stops")
def api_stops():
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

# ===================== API: Koordinatlar =====================

@app.route("/api/coords", methods=["GET", "POST", "DELETE"])
def api_coords():
    tid = get_active_trip()
    if not tid:
        return jsonify({"ok": False, "msg": "Aktif sefer yok"}), 400

    db = get_db()
    trip = db.execute("SELECT route FROM trips WHERE id=?", (tid,)).fetchone()
    if not trip:
        return jsonify({"ok": False, "msg": "Sefer bulunamadı"}), 404
    route_name = trip["route"]

    if request.method == "GET":
        rows = db.execute(
            "SELECT stop, lat, lng FROM route_stop_coords WHERE route=? ORDER BY stop",
            (route_name,)
        ).fetchall()
        return jsonify({
            "ok": True,
            "route": route_name,
            "items": [{"stop": r["stop"], "lat": float(r["lat"]), "lng": float(r["lng"])} for r in rows]
        })

    if request.method == "POST":
        data = request.get_json(force=True) or {}
        stop = (data.get("stop") or "").strip()
        try:
            lat = float(data.get("lat")); lng = float(data.get("lng"))
        except (TypeError, ValueError):
            return jsonify({"ok": False, "msg": "lat/lng geçersiz"}), 400
        if not stop:
            return jsonify({"ok": False, "msg": "stop gerekli"}), 400
        if not validate_stop_for_active_trip(stop):
            return jsonify({"ok": False, "msg": "Durak hat üzerinde değil"}), 400

        db.execute(
            """
            INSERT INTO route_stop_coords(route, stop, lat, lng)
            VALUES(?, ?, ?, ?)
            ON CONFLICT(route, stop) DO UPDATE SET
                lat=excluded.lat,
                lng=excluded.lng
            """,
            (route_name, stop, lat, lng)
        )
        db.commit()
        return jsonify({"ok": True})

    # DELETE
    stop = (request.args.get("stop") or "").strip()
    if not stop:
        return jsonify({"ok": False, "msg": "stop gerekli"}), 400
    db.execute("DELETE FROM route_stop_coords WHERE route=? AND stop=?", (route_name, stop))
    db.commit()
    return jsonify({"ok": True})

# ===================== API: Walk-on (ayakta satışlar) =====================

@app.route("/api/walkon", methods=["GET", "POST", "DELETE"])
def api_walkon():
    tid = get_active_trip()
    if not tid:
        return jsonify({"ok": False, "msg": "Aktif sefer yok"}), 400
    db = get_db()

    if request.method == "GET":
        aggregate = request.args.get("aggregate")
        if aggregate:
            row = db.execute(
                "SELECT COALESCE(SUM(total_amount),0) AS total_amount, COALESCE(SUM(pax),0) AS pax "
                "FROM walk_on_sales WHERE trip_id=?", (tid,)
            ).fetchone()
            return jsonify({"ok": True, "pax": int(row["pax"]), "total_amount": float(row["total_amount"])})
        rows = db.execute(
            "SELECT * FROM walk_on_sales WHERE trip_id=? ORDER BY id DESC", (tid,)
        ).fetchall()
        return jsonify({"ok": True, "items": [dict(r) for r in rows]})

    if request.method == "POST":
        data = request.get_json(force=True) or {}
        from_stop = (data.get("from_stop") or data.get("from") or "").strip()
        to_stop = (data.get("to_stop") or data.get("to") or "").strip()
        if not from_stop or not to_stop:
            return jsonify({"ok": False, "msg": "from_stop ve to_stop gerekli"}), 400

        if not validate_stop_for_active_trip(from_stop):
            return jsonify({"ok": False, "msg": f"Durak hat üzerinde değil: {from_stop}"}), 400
        if not validate_stop_for_active_trip(to_stop):
            return jsonify({"ok": False, "msg": f"Durak hat üzerinde değil: {to_stop}"}), 400

        try:
            pax = int(data.get("pax") or data.get("count") or 1)
        except (TypeError, ValueError):
            pax = 1
        try:
            unit_price = float(data.get("unit_price") or data.get("price") or 0)
        except (TypeError, ValueError):
            unit_price = 0.0
        try:
            total_amount = float(data.get("total_amount") or pax * unit_price)
        except (TypeError, ValueError):
            total_amount = pax * unit_price

        payment = norm_payment(data.get("payment") or "nakit")
        note = (data.get("note") or "").strip()

        db.execute(
            """
            INSERT INTO walk_on_sales(trip_id, from_stop, to_stop, pax, unit_price, total_amount, payment, note)
            VALUES(?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (tid, from_stop, to_stop, pax, unit_price, total_amount, payment, note)
        )
        db.commit()
        new_id = db.execute("SELECT last_insert_rowid()").fetchone()[0]
        return jsonify({"ok": True, "id": new_id, "pax": pax, "total_amount": total_amount})

    # DELETE
    to_param = (request.args.get("to_stop") or request.args.get("to") or "").strip()
    if not to_param:
        return jsonify({"ok": False, "msg": "to veya to_stop gerekli"}), 400
    if not validate_stop_for_active_trip(to_param):
        return jsonify({"ok": False, "msg": f"Durak hat üzerinde değil: {to_param}"}), 400
    rows = db.execute(
        "SELECT id FROM walk_on_sales WHERE trip_id=? AND lower(to_stop)=lower(?)",
        (tid, to_param)
    ).fetchall()
    ids = [r["id"] for r in rows]
    if ids:
        db.executemany(
            "DELETE FROM walk_on_sales WHERE trip_id=? AND id=?",
            [(tid, i) for i in ids]
        )
        db.commit()
    return jsonify({"ok": True, "deleted": ids, "count": len(ids)})

# === ALIAS: /api/standing & /api/standing/list ===

@app.route("/api/standing", methods=["GET", "POST", "DELETE"])
def api_standing_alias():
    tid = get_active_trip()
    if not tid:
        return jsonify({"ok": False, "msg": "Aktif sefer yok"}), 400
    db = get_db()

    if request.method == "GET":
        row = db.execute(
            "SELECT COALESCE(SUM(total_amount),0) AS total_amount, COALESCE(SUM(pax),0) AS pax "
            "FROM walk_on_sales WHERE trip_id=?", (tid,)
        ).fetchone()
        return jsonify({"ok": True, "count": int(row["pax"] or 0), "revenue": float(row["total_amount"] or 0.0)})

    if request.method == "DELETE":
        to_param = (request.args.get("to_stop") or request.args.get("to") or "").strip()
        if not to_param:
            return jsonify({"ok": False, "msg": "to veya to_stop gerekli"}), 400
        if not validate_stop_for_active_trip(to_param):
            return jsonify({"ok": False, "msg": f"Durak hat üzerinde değil: {to_param}"}), 400
        rows = db.execute(
            "SELECT id FROM walk_on_sales WHERE trip_id=? AND lower(to_stop)=lower(?)",
            (tid, to_param)
        ).fetchall()
        ids = [r["id"] for r in rows]
        if ids:
            db.executemany("DELETE FROM walk_on_sales WHERE trip_id=? AND id=?", [(tid, i) for i in ids])
            db.commit()
        return jsonify({"ok": True, "deleted": ids, "count": len(ids)})

    # POST
    data = request.get_json(force=True) or {}
    from_stop = (data.get("from_stop") or data.get("from") or "").strip()
    to_stop   = (data.get("to_stop")   or data.get("to")   or "").strip()
    if not from_stop or not to_stop:
        return jsonify({"ok": False, "msg": "from ve to gerekli"}), 400
    if not validate_stop_for_active_trip(from_stop):
        return jsonify({"ok": False, "msg": f"Durak hat üzerinde değil: {from_stop}"}), 400
    if not validate_stop_for_active_trip(to_stop):
        return jsonify({"ok": False, "msg": f"Durak hat üzerinde değil: {to_stop}"}), 400
    try:
        pax = int(data.get("pax") or data.get("count") or 1)
    except (TypeError, ValueError):
        pax = 1
    try:
        unit_price = float(data.get("unit_price") or data.get("price") or 0)
    except (TypeError, ValueError):
        unit_price = 0.0
    total_amount = pax * unit_price
    payment = norm_payment(data.get("payment") or "nakit")
    note = (data.get("note") or "").strip()

    db.execute(
        "INSERT INTO walk_on_sales(trip_id, from_stop, to_stop, pax, unit_price, total_amount, payment, note) "
        "VALUES(?, ?, ?, ?, ?, ?, ?, ?)",
        (tid, from_stop, to_stop, pax, unit_price, total_amount, payment, note)
    )
    db.commit()
    return jsonify({"ok": True, "pax": pax, "total_amount": total_amount})

@app.route("/api/standing/list")
def api_standing_list_alias():
    tid = get_active_trip()
    if not tid:
        return jsonify({"ok": False, "msg": "Aktif sefer yok", "items": []}), 400
    rows = get_db().execute(
        "SELECT id, from_stop, to_stop, pax, unit_price, payment, note, created_at "
        "FROM walk_on_sales WHERE trip_id=? ORDER BY id DESC",
        (tid,)
    ).fetchall()
    items = [{
        "id": r["id"], "from": r["from_stop"], "to": r["to_stop"],
        "count": r["pax"], "price": r["unit_price"], "payment": r["payment"],
        "note": r["note"], "ts": r["created_at"],
    } for r in rows]
    return jsonify({"ok": True, "items": items})

# ===================== API: İstatistik =====================

@app.route("/api/stats")
def api_stats():
    tid = get_active_trip()
    if not tid:
        return jsonify({"ok": False, "msg": "Aktif sefer yok"}), 400
    db = get_db()

    seat_row = db.execute(
        "SELECT COUNT(*) AS c, COALESCE(SUM(amount),0) AS s, COALESCE(SUM(service),0) AS svc "
        "FROM seats WHERE trip_id=?", (tid,)
    ).fetchone()
    seats_reserved = int(seat_row["c"])
    seats_revenue = float(seat_row["s"])
    service_count = int(seat_row["svc"])

    walk_row = db.execute(
        "SELECT COALESCE(SUM(pax),0) AS pax, COALESCE(SUM(total_amount),0) AS tot FROM walk_on_sales WHERE trip_id=?",
        (tid,)
    ).fetchone()
    walkon_pax = int(walk_row["pax"])
    walkon_revenue = float(walk_row["tot"])

    by_pay = {}
    for r in db.execute("SELECT payment, COALESCE(SUM(amount),0) AS s FROM seats WHERE trip_id=? GROUP BY payment", (tid,)).fetchall():
        by_pay[r["payment"]] = by_pay.get(r["payment"], 0.0) + float(r["s"])
    for r in db.execute("SELECT payment, COALESCE(SUM(total_amount),0) AS s FROM walk_on_sales WHERE trip_id=? GROUP BY payment", (tid,)).fetchall():
        by_pay[r["payment"]] = by_pay.get(r["payment"], 0.0) + float(r["s"])

    return jsonify({
        "ok": True,
        "seats_reserved": seats_reserved,
        "seats_revenue": seats_revenue,
        "walkon_pax": walkon_pax,
        "walkon_revenue": walkon_revenue,
        "total_revenue": seats_revenue + walkon_revenue,
        "by_payment": by_pay,
        "service_count": service_count
    })

# ===================== API: Durak Olay Günlüğü =====================

def _seats_count_for_stop(tid: int, stop_name: str) -> int:
    db = get_db()
    row = db.execute(
        "SELECT COUNT(*) AS c FROM seats WHERE trip_id=? AND stop=?",
        (tid, stop_name)
    ).fetchone()
    return int(row["c"] or 0)

@app.route("/api/stoplog", methods=["GET", "POST"])
def api_stoplog():
    tid = get_active_trip()
    if not tid:
        return jsonify({"ok": False, "msg": "Aktif sefer yok"}), 400
    db = get_db()

    if request.method == "GET":
        rows = db.execute(
            """
            SELECT id, trip_id, stop_name, event, distance_km,
                   seats_for_stop, meta_json, ts
            FROM stop_logs
            WHERE trip_id=?
            ORDER BY ts DESC, id DESC
            """,
            (tid,)
        ).fetchall()
        items = []
        for r in rows:
            try:
                meta = json.loads(r["meta_json"]) if r["meta_json"] else None
            except Exception:
                meta = None
            items.append({
                "id": r["id"], "trip_id": r["trip_id"], "stop_name": r["stop_name"],
                "event": r["event"], "distance_km": r["distance_km"],
                "seats_for_stop": r["seats_for_stop"], "meta": meta, "ts": r["ts"],
            })
        return jsonify({"ok": True, "items": items})

    data = request.get_json(force=True) or {}
    stop_name = (data.get("stop_name") or data.get("stop") or "").strip()
    if not stop_name:
        return jsonify({"ok": False, "msg": "stop_name gerekli"}), 400
    if not validate_stop_for_active_trip(stop_name):
        return jsonify({"ok": False, "msg": "Durak bu hat üzerinde değil"}), 400

    event = (data.get("event") or "arrive").strip().lower()
    if event not in ("arrive", "depart", "approach"):
        return jsonify({"ok": False, "msg": "event geçersiz"}), 400

    try:
        distance_km = float(data.get("distance_km")) if data.get("distance_km") is not None else None
    except (TypeError, ValueError):
        return jsonify({"ok": False, "msg": "distance_km geçersiz"}), 400

    seats_for_stop = _seats_count_for_stop(tid, stop_name)
    meta = data.get("meta")
    try:
        meta_json = json.dumps(meta, ensure_ascii=False) if isinstance(meta, (dict, list)) else None
    except Exception:
        meta_json = None

    db.execute(
        """
        INSERT INTO stop_logs(trip_id, stop_name, event, distance_km, seats_for_stop, meta_json)
        VALUES(?, ?, ?, ?, ?, ?)
        """,
        (tid, stop_name, event, distance_km, seats_for_stop, meta_json)
    )
    db.commit()
    return jsonify({
        "ok": True,
        "stop_name": stop_name,
        "event": event,
        "distance_km": distance_km,
        "seats_for_stop": seats_for_stop
    })

# ===================== Seferi Sonlandır =====================

@app.route("/end-trip", methods=["POST"])
def end_trip():
    db = get_db()
    tid = get_active_trip()
    if tid:
        db.execute("DELETE FROM seats WHERE trip_id=?", (tid,))
        db.execute("DELETE FROM walk_on_sales WHERE trip_id=?", (tid,))
        db.execute("UPDATE app_state SET active_trip_id=NULL WHERE id=1")
        db.commit()
    else:
        db.execute("UPDATE app_state SET active_trip_id=NULL WHERE id=1")
        db.commit()
    return redirect(url_for("index"))

# ===================== Upload Serve =====================

@app.route("/u/<path:filename>")
def serve_uploaded(filename):
    safe = secure_filename(filename)
    return send_from_directory(UPLOAD_DIR, safe, as_attachment=False)

# ===================== Emanetler (sayfa & API) =====================

@app.route("/emanetler")
def consignments_page():
    tid = get_active_trip()
    if not tid:
        return redirect(url_for("trip_start"))
    db = get_db()
    trip = db.execute("SELECT * FROM trips WHERE id=?", (tid,)).fetchone()
    stops = get_stops(trip["route"])
    rows = db.execute(
        "SELECT * FROM consignments WHERE trip_id=? ORDER BY created_at DESC",
        (tid,)
    ).fetchall()
    items = [dict(r) for r in rows]
    return render_template("consignments.html", trip=trip, stops=stops, items=items)

@app.route("/api/consignments", methods=["GET", "POST"])
def api_consignments():
    tid = get_active_trip()
    if not tid:
        return jsonify({"ok": False, "msg": "Aktif sefer yok"}), 400
    db = get_db()

    if request.method == "GET":
        rows = db.execute(
            "SELECT * FROM consignments WHERE trip_id=? ORDER BY created_at DESC",
            (tid,)
        ).fetchall()
        return jsonify({"ok": True, "items": [dict(r) for r in rows]})

    data = request.get_json(force=True) or {}
    code = (data.get("code") or "").strip()
    item_name  = (data.get("item_name")  or "").strip()
    item_type  = (data.get("item_type")  or "").strip()
    from_name  = (data.get("from_name")  or "").strip()
    from_phone = (data.get("from_phone") or "").strip()
    to_name    = (data.get("to_name")    or "").strip()
    to_phone   = (data.get("to_phone")   or "").strip()
    from_stop  = (data.get("from_stop")  or "").strip()
    to_stop    = (data.get("to_stop")    or "").strip()
    payment    = norm_payment(data.get("payment") or "nakit")
    try:
        amount = float(data.get("amount") or 0)
    except Exception:
        amount = 0.0

    if from_stop and not validate_stop_for_active_trip(from_stop):
        return jsonify({"ok": False, "msg": f"Durak hat üzerinde değil: {from_stop}"}), 400
    if to_stop and not validate_stop_for_active_trip(to_stop):
        return jsonify({"ok": False, "msg": f"Durak hat üzerinde değil: {to_stop}"}), 400
    if not item_name:
        return jsonify({"ok": False, "msg": "Eşya adı gerekli"}), 400
    if not code:
        code = secrets.token_hex(3).upper()

    db.execute(
        """
        INSERT INTO consignments(
            trip_id, code, item_name, item_type, from_name, from_phone,
            to_name, to_phone, from_stop, to_stop, amount, payment, status
        )
        VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 'bekliyor')
        """,
        (tid, code, item_name, item_type, from_name, from_phone,
         to_name, to_phone, from_stop, to_stop, amount, payment)
    )
    db.commit()
    new_id = db.execute("SELECT last_insert_rowid()").fetchone()[0]
    return jsonify({"ok": True, "id": new_id, "code": code})

# --- Emanet sayacı (durak bazında) ---
@app.get("/api/parcels")
def api_parcels():
    tid = get_active_trip()
    if not tid:
        return jsonify({"ok": False, "msg": "Aktif sefer yok", "items": []}), 400
    status = (request.args.get("status") or "bekliyor").strip().lower()
    db = get_db()
    rows = db.execute(
        """
        SELECT COALESCE(to_stop,'') AS to_stop, COUNT(*) AS cnt
        FROM consignments
        WHERE trip_id=? AND status=?
        GROUP BY to_stop
        """,
        (tid, status)
    ).fetchall()
    items = [{"to": r["to_stop"], "count": int(r["cnt"])} for r in rows if r["to_stop"]]
    return jsonify({"ok": True, "items": items})

# --- Emanet fotoğrafları: GET + POST ---
@app.route("/api/consignments/<int:cid>/photos", methods=["GET", "POST"])
def api_cons_photos(cid):
    tid = get_active_trip()
    if not tid:
        return jsonify({"ok": False, "msg": "Aktif sefer yok"}), 400
    db = get_db()

    if request.method == "GET":
        rows = db.execute(
            "SELECT id, role, file_path, mime, size_bytes, created_at "
            "FROM consignment_photos WHERE consignment_id=? ORDER BY id DESC",
            (cid,)
        ).fetchall()
        items = [{
            "id": r["id"], "role": r["role"], "file": r["file_path"], "mime": r["mime"],
            "size": r["size_bytes"], "created_at": r["created_at"],
            "url": url_for("serve_uploaded", filename=r["file_path"])
        } for r in rows]
        return jsonify({"ok": True, "items": items})

    # POST (yükleme)
    role = (request.form.get("role") or "").strip().lower()  # 'pickup' | 'delivery' | ''
    f = request.files.get("file")
    if not f or f.filename == "":
        return jsonify({"ok": False, "msg": "Dosya gerekli"}), 400
    if not _allowed_file(f.filename):
        return jsonify({"ok": False, "msg": "İzin verilmeyen dosya türü"}), 400
    if f.mimetype not in ALLOWED_IMAGE_MIMES:
        return jsonify({"ok": False, "msg": "Desteklenmeyen MIME türü"}), 400

    ext = f.filename.rsplit(".", 1)[1].lower()
    rid = secrets.token_hex(3)
    fname = secure_filename(f"c{cid}_{int(datetime.now().timestamp())}_{rid}.{ext}")
    save_path = Path(UPLOAD_DIR) / fname
    ensure_upload_dir()
    f.save(save_path)
    size_bytes = save_path.stat().st_size

    # güvenlik: emanet bu seferde mi?
    row = db.execute("SELECT id FROM consignments WHERE id=? AND trip_id=?", (cid, tid)).fetchone()
    if not row:
        save_path.unlink(missing_ok=True)
        return jsonify({"ok": False, "msg": "Emanet bulunamadı"}), 404

    db.execute(
        "INSERT INTO consignment_photos(consignment_id, role, file_path, mime, size_bytes) "
        "VALUES(?, ?, ?, ?, ?)",
        (cid, role, fname, f.mimetype, size_bytes)
    )
    db.commit()
    return jsonify({"ok": True, "url": url_for('serve_uploaded', filename=fname), "file": fname, "size": size_bytes})

@app.route("/api/consignments/<int:cid>", methods=["DELETE"])
def api_cons_delete(cid):
    tid = get_active_trip()
    if not tid:
        return jsonify({"ok": False, "msg": "Aktif sefer yok"}), 400
    db = get_db()
    photos = db.execute(
        "SELECT file_path FROM consignment_photos WHERE consignment_id=?",
        (cid,)
    ).fetchall()
    for r in photos:
        try:
            (Path(UPLOAD_DIR) / r["file_path"]).unlink(missing_ok=True)
        except Exception:
            pass
    db.execute("DELETE FROM consignment_photos WHERE consignment_id=?", (cid,))
    db.execute("DELETE FROM consignments WHERE id=? AND trip_id=?", (cid, tid))
    db.commit()
    return jsonify({"ok": True})

# ===================== Sağlık =====================

@app.route("/health")
def health():
    return "ok"

# === Blueprint kayıtları ===
app.register_blueprint(bp_speed)

# ===================== Çalıştır =====================
if __name__ == "__main__":
    with app.app_context():
        ensure_schema()
        ensure_upload_dir()
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", "5000")), debug=DEBUG)
