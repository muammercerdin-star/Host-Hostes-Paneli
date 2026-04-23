import os
import csv
import json
import secrets
import sqlite3
import re
from io import StringIO
from pathlib import Path
from datetime import datetime
from typing import Any, Optional, Tuple

from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    jsonify,
    g,
    session,
    abort,
    send_from_directory,
    make_response,
)
from werkzeug.utils import secure_filename

from speedlimit import bp_speed
from modules.bags import bp as bags_bp
from modules.bags import bag_root, safe


# =========================================================
# Ayarlar
# =========================================================

def env_bool(name: str, default: bool = False) -> bool:
    raw = os.getenv(name)
    if raw is None:
        return default
    return raw.strip().lower() in {"1", "true", "yes", "on"}


app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "degistir-beni")

DB_PATH = os.getenv("DB_PATH", "db.sqlite3")
DEBUG = env_bool("FLASK_DEBUG", True)
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD", "yusuf")
PORT = int(os.getenv("PORT", "5000"))

UPLOAD_DIR = os.getenv(
    "UPLOAD_DIR",
    os.path.join(os.getcwd(), "uploads", "consignments"),
)
MAX_UPLOAD_MB = int(os.getenv("MAX_UPLOAD_MB", "10"))
app.config["MAX_CONTENT_LENGTH"] = MAX_UPLOAD_MB * 1024 * 1024

ALLOWED_IMAGE_EXTS = {".jpg", ".jpeg", ".png", ".webp"}
ALLOWED_IMAGE_MIMES = {"image/jpeg", "image/png", "image/webp"}

app.register_blueprint(bags_bp)
app.register_blueprint(bp_speed)


# =========================================================
# Sabitler
# =========================================================

SEAT_NUMBERS = [
    1, 3, 4, 5, 7, 8, 9, 11, 12, 13, 15, 16, 17, 19, 20, 21, 23, 24,
    25, 27, 28, 29, 31, 33, 34, 35, 37, 38, 39, 41, 42, 43, 45, 46,
    49, 50, 51, 52, 53, 54,
]

SEAT_POSITIONS = {
    1: [1, 1], 3: [1, 3], 4: [1, 4],
    5: [2, 1], 7: [2, 3], 8: [2, 4],
    9: [3, 1], 11: [3, 3], 12: [3, 4],
    13: [4, 1], 15: [4, 3], 16: [4, 4],
    17: [5, 1], 19: [5, 3], 20: [5, 4],
    21: [6, 1], 23: [6, 3], 24: [6, 4],
    25: [7, 1], 27: [7, 3], 28: [7, 4],
    29: [8, 1],
    31: [9, 1], 33: [9, 3], 34: [9, 4],
    35: [10, 1], 37: [10, 3], 38: [10, 4],
    39: [11, 1], 41: [11, 3], 42: [11, 4],
    43: [12, 1], 45: [12, 3], 46: [12, 4],
    49: [13, 3], 50: [13, 4],
    51: [14, 1], 52: [14, 2], 53: [14, 3], 54: [14, 4],
}

ROUTE_STOPS = {
    "Denizli – İstanbul": [
        "Denizli otogar", "Sarayköy", "Buldan", "Bozalan", "Derbent(Denizli)", "Kadıköy",
        "İl Sınırı(Manisa)", "Dindarlı", "Dadağlı", "Sarıgöl Garaj", "Afşar", "Bereketli",
        "Hacıaliler", "Ortahan", "Belenyaka", "Alaşehir Otogar", "Alaşehir Stadyum",
        "Akkeçili", "Piyadeler", "Kavaklıdere", "Salihli Garaj", "Sart", "Ahmetli",
        "Gökkaya", "Akçapınar", "Derbent(Turgutlu)", "Turgutlu Garaj", "Özdilek(Turgutlu)",
        "Manisa Otogar", "Akhisar", "Saruhanlı", "Soma", "Kırkağaç", "Balıkesir", "Susurluk",
        "Mustafa K.P(Bursa)", "Bursa Otogar", "Gebze Garaj", "Harem", "Alibeyköy", "Esenler Otogar",
    ],
    "Denizli – İzmir": [
        "Denizli otogar", "Sarayköy", "Alaşehir Otogar", "Salihli Garaj", "Turgutlu Garaj",
        "Manisa Otogar", "Bornova", "İzmir Otogar",
    ],
    "İstanbul – Denizli": [
        "Esenler Otogar", "Alibeyköy", "Harem", "Gebze Garaj", "Bursa Otogar", "Susurluk",
        "Balıkesir", "Kırkağaç", "Soma", "Akhisar", "Manisa Otogar", "Turgutlu Garaj",
        "Salihli Garaj", "Alaşehir Otogar", "Denizli otogar",
    ],
    "İzmir – Denizli": [
        "İzmir Otogar", "Bornova", "Manisa Otogar", "Turgutlu Garaj", "Salihli Garaj",
        "Alaşehir Otogar", "Sarayköy", "Denizli otogar",
    ],
    "İstanbul – Antalya": [
        "Esenler", "Alibeyköy", "Harem", "Gebze", "Bursa", "Korkuteli", "Antalya Otogar",
    ],
    "Antalya – İstanbul": [
        "Antalya Otogar", "Korkuteli", "Bursa", "Gebze", "Harem", "Alibeyköy", "Esenler",
    ],
}

TICKET_TYPES = {"biletli", "biletsiz", "ucretsiz"}
PAYMENT_TYPES = {"nakit", "iban", "online", "pos", "ucretsiz"}
GENDERS = {"bay", "bayan", ""}

NEIGHBORS = {
    3: 4, 4: 3, 7: 8, 8: 7, 11: 12, 12: 11, 15: 16, 16: 15,
    19: 20, 20: 19, 23: 24, 24: 23, 27: 28, 28: 27, 33: 34, 34: 33,
    37: 38, 38: 37, 41: 42, 42: 41, 45: 46, 46: 45, 49: 50, 50: 49, 53: 54, 54: 53,
}

DEFAULT_CATS_IN = ["Devir", "Garaj", "Harem", "Eşya", "Nakit Bilet", "Avans", "Diğer"]
DEFAULT_CATS_OUT = ["Yıkama", "Sigara", "Yemek", "Otoyol", "Otogar", "İkram", "Temizlik", "Su/Çay", "Bakım", "Diğer"]

AI_INTENTS = {
    "seat_add_single": {"title": "Tek koltuk ekleme", "pattern": "seat + add"},
    "seat_add_group": {"title": "Çoklu koltuk ekleme", "pattern": "seat_list + add"},
    "seat_remove_single": {"title": "Tek koltuk boşaltma", "pattern": "seat + offload"},
    "seat_remove_group": {"title": "Çoklu koltuk boşaltma", "pattern": "seat_list + offload"},
    "standing_add": {"title": "Ayakta ekleme", "pattern": "standing + add"},
    "service_mark": {"title": "Servis işaretleme", "pattern": "service + mark"},
    "query": {"title": "Sorgu", "pattern": "query"},
}


# =========================================================
# Genel yardımcılar
# =========================================================

def norm_ticket_type(val: str) -> str:
    v = (val or "").strip().lower()
    return v if v in TICKET_TYPES else "biletsiz"


def norm_payment(val: str) -> str:
    v = (val or "").strip().lower()
    return v if v in PAYMENT_TYPES else "nakit"


def norm_gender(val: str) -> str:
    v = (val or "").strip().lower()
    return v if v in GENDERS else ""


def norm_bool(val: Any) -> int:
    if isinstance(val, bool):
        return 1 if val else 0
    s = str(val or "").strip().lower()
    return 1 if s in {"1", "true", "yes", "on"} else 0


def parse_float(val: Any, default: Optional[float] = 0.0) -> Optional[float]:
    try:
        return float(val)
    except Exception:
        return default


def parse_int(val: Any, default: Optional[int] = 0) -> Optional[int]:
    try:
        return int(val)
    except Exception:
        return default


def ensure_upload_dir() -> None:
    Path(UPLOAD_DIR).mkdir(parents=True, exist_ok=True)


def allowed_file(filename: str) -> bool:
    if not filename or "." not in filename:
        return False
    ext = "." + filename.rsplit(".", 1)[1].lower()
    return ext in ALLOWED_IMAGE_EXTS

def validate_seat_no(seat_no: int) -> bool:
    return seat_no in SEAT_NUMBERS


def parse_int_list(raw: str):
    if not raw:
        return []
    out = []
    for part in raw.split(","):
        n = parse_int(part.strip(), None)
        if n is not None and n not in out:
            out.append(n)
    return out


def delete_walkon_rows(
    db: sqlite3.Connection,
    trip_id: int,
    *,
    item_id: Optional[int] = None,
    ids: Optional[list[int]] = None,
    to_stop: Optional[str] = None,
    clear_all: bool = False,
):
    rows = []

    if item_id is not None:
        rows = db.execute(
            "SELECT id FROM walk_on_sales WHERE trip_id=? AND id=?",
            (trip_id, item_id),
        ).fetchall()

    elif ids:
        placeholders = ",".join("?" * len(ids))
        rows = db.execute(
            f"SELECT id FROM walk_on_sales WHERE trip_id=? AND id IN ({placeholders})",
            [trip_id, *ids],
        ).fetchall()

    elif clear_all:
        rows = db.execute(
            "SELECT id FROM walk_on_sales WHERE trip_id=?",
            (trip_id,),
        ).fetchall()

    elif to_stop:
        rows = db.execute(
            "SELECT id FROM walk_on_sales WHERE trip_id=? AND lower(to_stop)=lower(?)",
            (trip_id, to_stop),
        ).fetchall()

    deleted_ids = [r["id"] for r in rows]

    if deleted_ids:
        db.executemany(
            "DELETE FROM walk_on_sales WHERE trip_id=? AND id=?",
            [(trip_id, i) for i in deleted_ids],
        )

    return deleted_ids
# =========================================================
# DB
# =========================================================

def get_db() -> sqlite3.Connection:
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


def ensure_schema() -> None:
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

        CREATE TABLE IF NOT EXISTS routes(
            id INTEGER PRIMARY KEY,
            name TEXT UNIQUE,
            stops TEXT
        );

        CREATE TABLE IF NOT EXISTS seats(
            trip_id INTEGER NOT NULL,
            seat_no INTEGER NOT NULL,
            from_stop TEXT DEFAULT '',
            to_stop TEXT DEFAULT '',
            ticket_type TEXT DEFAULT 'biletsiz',
            payment TEXT DEFAULT 'nakit',
            amount REAL DEFAULT 0,
            gender TEXT DEFAULT '',
            pair_ok INTEGER DEFAULT 0,
            service INTEGER DEFAULT 0,
            service_note TEXT DEFAULT '',
            passenger_name TEXT DEFAULT '',
            passenger_phone TEXT DEFAULT '',
            PRIMARY KEY(trip_id, seat_no),
            FOREIGN KEY(trip_id) REFERENCES trips(id) ON DELETE CASCADE
        );

        CREATE INDEX IF NOT EXISTS idx_seats_trip ON seats(trip_id);
        CREATE INDEX IF NOT EXISTS idx_seats_trip_to_stop ON seats(trip_id, to_stop);
        CREATE INDEX IF NOT EXISTS idx_seats_trip_from_stop ON seats(trip_id, from_stop);
        CREATE INDEX IF NOT EXISTS idx_seats_trip_payment ON seats(trip_id, payment);

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
            created_at TEXT DEFAULT (datetime('now','localtime')),
            FOREIGN KEY(trip_id) REFERENCES trips(id) ON DELETE CASCADE
        );

        CREATE INDEX IF NOT EXISTS idx_walkon_trip ON walk_on_sales(trip_id);

        CREATE TABLE IF NOT EXISTS route_stop_coords(
            route TEXT NOT NULL,
            stop TEXT NOT NULL,
            lat REAL NOT NULL,
            lng REAL NOT NULL,
            PRIMARY KEY(route, stop)
        );

        CREATE TABLE IF NOT EXISTS stop_logs(
            id INTEGER PRIMARY KEY,
            trip_id INTEGER NOT NULL,
            stop_name TEXT NOT NULL,
            event TEXT NOT NULL,
            distance_km REAL,
            seats_for_stop INTEGER,
            meta_json TEXT,
            ts TEXT NOT NULL DEFAULT (datetime('now','localtime')),
            FOREIGN KEY(trip_id) REFERENCES trips(id) ON DELETE CASCADE
        );

        CREATE INDEX IF NOT EXISTS idx_stoplogs_trip_ts ON stop_logs(trip_id, ts);

        CREATE TABLE IF NOT EXISTS consignments(
            id INTEGER PRIMARY KEY,
            trip_id INTEGER,
            code TEXT UNIQUE,
            item_name TEXT,
            item_type TEXT,
            from_name TEXT,
            from_phone TEXT,
            to_name TEXT,
            to_phone TEXT,
            from_stop TEXT,
            to_stop TEXT,
            amount REAL DEFAULT 0,
            payment TEXT DEFAULT 'nakit',
            status TEXT DEFAULT 'bekliyor',
            notes TEXT,
            created_at TEXT DEFAULT (datetime('now','localtime')),
            updated_at TEXT,
            delivered_at TEXT,
            FOREIGN KEY(trip_id) REFERENCES trips(id) ON DELETE CASCADE
        );

        CREATE INDEX IF NOT EXISTS idx_cons_trip ON consignments(trip_id);
        CREATE INDEX IF NOT EXISTS idx_cons_status ON consignments(status);

        CREATE TABLE IF NOT EXISTS consignment_photos(
            id INTEGER PRIMARY KEY,
            consignment_id INTEGER NOT NULL,
            role TEXT,
            file_path TEXT NOT NULL,
            mime TEXT,
            size_bytes INTEGER,
            created_at TEXT DEFAULT (datetime('now','localtime')),
            FOREIGN KEY(consignment_id) REFERENCES consignments(id) ON DELETE CASCADE
        );

        CREATE TABLE IF NOT EXISTS fares(
            route TEXT NOT NULL,
            from_stop TEXT NOT NULL,
            to_stop TEXT NOT NULL,
            price REAL NOT NULL,
            updated_at TEXT DEFAULT (datetime('now','localtime')),
            PRIMARY KEY(route, from_stop, to_stop)
        );

        CREATE TABLE IF NOT EXISTS settings(
            key TEXT PRIMARY KEY,
            value TEXT
        );

        CREATE TABLE IF NOT EXISTS cash_moves(
            id INTEGER PRIMARY KEY,
            trip_id INTEGER NOT NULL,
            direction TEXT NOT NULL CHECK(direction IN ('+','-')),
            category TEXT NOT NULL,
            amount INTEGER NOT NULL DEFAULT 0,
            note TEXT,
            created_at TEXT DEFAULT (datetime('now','localtime')),
            FOREIGN KEY(trip_id) REFERENCES trips(id) ON DELETE CASCADE
        );

        CREATE INDEX IF NOT EXISTS idx_cash_moves_trip ON cash_moves(trip_id);

        CREATE TABLE IF NOT EXISTS learned_commands(
            id INTEGER PRIMARY KEY,
            phrase TEXT NOT NULL,
            phrase_norm TEXT NOT NULL UNIQUE,
            skeleton TEXT,
            intent TEXT NOT NULL,
            pattern TEXT,
            created_at TEXT DEFAULT (datetime('now','localtime')),
            updated_at TEXT DEFAULT (datetime('now','localtime'))
        );

        CREATE INDEX IF NOT EXISTS idx_learned_commands_phrase_norm
        ON learned_commands(phrase_norm);

        CREATE INDEX IF NOT EXISTS idx_learned_commands_skeleton
        ON learned_commands(skeleton);

        CREATE INDEX IF NOT EXISTS idx_learned_commands_intent
        ON learned_commands(intent);
        """
    )

    seat_cols = [r["name"] for r in db.execute("PRAGMA table_info(seats)").fetchall()]
    migrations = {
        "from_stop": "ALTER TABLE seats ADD COLUMN from_stop TEXT DEFAULT ''",
        "to_stop": "ALTER TABLE seats ADD COLUMN to_stop TEXT DEFAULT ''",
        "gender": "ALTER TABLE seats ADD COLUMN gender TEXT DEFAULT ''",
        "pair_ok": "ALTER TABLE seats ADD COLUMN pair_ok INTEGER DEFAULT 0",
        "service": "ALTER TABLE seats ADD COLUMN service INTEGER DEFAULT 0",
        "service_note": "ALTER TABLE seats ADD COLUMN service_note TEXT DEFAULT ''",
        "passenger_name": "ALTER TABLE seats ADD COLUMN passenger_name TEXT DEFAULT ''",
        "passenger_phone": "ALTER TABLE seats ADD COLUMN passenger_phone TEXT DEFAULT ''",
    }

    for col, sql in migrations.items():
        if col not in seat_cols:
            db.execute(sql)

    db.commit()


# =========================================================
# Template filter
# =========================================================

@app.template_filter("tl")
def format_tl(value):
    try:
        value = float(value)
        s = f"{value:,.2f} ₺"
        return s.replace(",", "X").replace(".", ",").replace("X", ".")
    except Exception:
        return "0,00 ₺"


# =========================================================
# Settings helper
# =========================================================

def settings_get(key: str, default=None):
    row = get_db().execute("SELECT value FROM settings WHERE key=?", (key,)).fetchone()
    if not row:
        return default
    raw = row["value"]
    try:
        return json.loads(raw)
    except Exception:
        return raw


def settings_set(key: str, value) -> None:
    raw = json.dumps(value, ensure_ascii=False) if not isinstance(value, str) else value
    db = get_db()
    db.execute("INSERT OR REPLACE INTO settings(key, value) VALUES(?, ?)", (key, raw))
    db.commit()


def ensure_list(x):
    if isinstance(x, list):
        return x
    if isinstance(x, str):
        parts = [p.strip() for p in x.replace("\n", ",").split(",")]
        return [p for p in parts if p]
    return []


def get_cash_categories():
    cats_in = ensure_list(settings_get("cash_cat_in"))
    cats_out = ensure_list(settings_get("cash_cat_out"))
    if not cats_in:
        cats_in = DEFAULT_CATS_IN
    if not cats_out:
        cats_out = DEFAULT_CATS_OUT
    settings_set("cash_cat_in", cats_in)
    settings_set("cash_cat_out", cats_out)
    return cats_in, cats_out


def save_cash_categories(text_in: str, text_out: str) -> None:
    def parse_lines(s: str):
        return [x.strip() for x in (s or "").replace("\n", ",").split(",") if x.strip()]

    settings_set("cash_cat_in", parse_lines(text_in) or DEFAULT_CATS_IN)
    settings_set("cash_cat_out", parse_lines(text_out) or DEFAULT_CATS_OUT)


# =========================================================
# Aktif sefer
# =========================================================

def set_active_trip(trip_id: Optional[int]) -> None:
    db = get_db()
    db.execute("UPDATE app_state SET active_trip_id=? WHERE id=1", (trip_id,))
    db.commit()


def get_active_trip() -> Optional[int]:
    row = get_db().execute("SELECT active_trip_id FROM app_state WHERE id=1").fetchone()
    return row["active_trip_id"] if row else None


def get_active_trip_row():
    tid = get_active_trip()
    if not tid:
        return None
    return get_db().execute("SELECT * FROM trips WHERE id=?", (tid,)).fetchone()


# =========================================================
# Hat / durak yardımcıları
# =========================================================

def parse_stops(text: str):
    if not text:
        return []
    parts = []
    for line in text.splitlines():
        parts.extend(x.strip() for x in line.split(","))
    return [x for x in parts if x]


def get_stops(route_name: str):
    row = get_db().execute("SELECT stops FROM routes WHERE name=?", (route_name,)).fetchone()
    if row:
        try:
            return json.loads(row["stops"]) or []
        except Exception:
            pass
    return ROUTE_STOPS.get(route_name, ROUTE_STOPS.get("Denizli – İstanbul", []))


def all_route_names():
    dyn = [r["name"] for r in get_db().execute("SELECT name FROM routes ORDER BY name").fetchall()]
    return list(dict.fromkeys(list(ROUTE_STOPS.keys()) + dyn))


def validate_stop_for_trip(route_name: str, stop: str) -> bool:
    return (stop or "").strip() in set(get_stops(route_name))


def validate_stop_for_active_trip(stop: str) -> bool:
    trip = get_active_trip_row()
    if not trip:
        return False
    return validate_stop_for_trip(trip["route"], stop)


# =========================================================
# Yan koltuk kuralı
# =========================================================

def neighbor_rule_ok(trip_id: int, seat_no: int, gender: str, pair_ok: bool) -> Tuple[bool, str]:
    nb = NEIGHBORS.get(seat_no)
    if not nb or not gender:
        return True, ""

    row = get_db().execute(
        """
        SELECT gender, COALESCE(pair_ok,0) AS pair_ok
        FROM seats
        WHERE trip_id=? AND seat_no=?
        """,
        (trip_id, nb),
    ).fetchone()

    if not row:
        return True, ""

    nb_gender = norm_gender(row["gender"])
    nb_pair_ok = bool(row["pair_ok"])

    if gender in {"bay", "bayan"} and nb_gender in {"bay", "bayan"}:
        if gender != nb_gender and not (pair_ok or nb_pair_ok):
            return False, f"Yan koltuk {nb} '{nb_gender}' kayıtlı. İstisna olmadan farklı cins yan yana olmaz."

    return True, ""


# =========================================================
# CSRF / Auth
# =========================================================

def issue_csrf() -> str:
    token = secrets.token_urlsafe(32)
    session["csrf_token"] = token
    return token


def get_csrf() -> str:
    tok = session.get("csrf_token")
    if not tok:
        tok = issue_csrf()
    return tok


def check_csrf() -> None:
    form_tok = request.form.get("csrf_token")
    header_tok = request.headers.get("X-CSRF-Token")
    json_tok = None
    if request.is_json:
        data = request.get_json(silent=True) or {}
        json_tok = data.get("csrf_token")
    supplied = form_tok or header_tok or json_tok
    if not supplied or supplied != session.get("csrf_token"):
        abort(403, description="CSRF doğrulaması başarısız")


PROTECTED_PREFIXES = ("/",)
EXCLUDE_PREFIXES = ("/login", "/logout", "/health", "/api/speedlimit")


def is_excluded_path(path: str) -> bool:
    return any(path == x or path.startswith(x + "/") for x in EXCLUDE_PREFIXES)


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
        if request.method in {"POST", "PUT", "PATCH", "DELETE"}:
            check_csrf()


@app.context_processor
def inject_globals():
    try:
        return {
            "active_trip": get_active_trip_row(),
            "csrf_token": get_csrf(),
        }
    except Exception:
        return {
            "active_trip": None,
            "csrf_token": get_csrf(),
        }


# =========================================================
# AI yardımcıları
# =========================================================

def normalize_ai_text(text: str) -> str:
    text = (text or "").strip().lower()
    text = text.replace("’", "").replace("'", "").replace("`", "")
    text = re.sub(r"[^0-9a-zçğıöşü\s-]", " ", text, flags=re.IGNORECASE)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def ai_extract_seat_list(text: str):
    text = text or ""
    text = re.sub(r"(\d+)\s*-\s*(\d+)", r"\1 \2", text)
    text = re.sub(r"(\d+)\sve\s(\d+)", r"\1 \2", text, flags=re.IGNORECASE)
    text = re.sub(r"(\d+)\sile\s(\d+)", r"\1 \2", text, flags=re.IGNORECASE)

    nums = re.findall(r"\b\d{1,2}\b", text)
    out = []
    for n in nums:
        x = int(n)
        if 1 <= x <= 60 and x not in out:
            out.append(x)
    return out


def ai_make_skeleton(text: str) -> str:
    text = normalize_ai_text(text)
    text = re.sub(r"\d+", "{n}", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def ai_find_learned_match(command: str):
    db = get_db()
    phrase_norm = normalize_ai_text(command)
    skeleton = ai_make_skeleton(command)

    row = db.execute(
        """
        SELECT id, phrase, intent, pattern
        FROM learned_commands
        WHERE phrase_norm=?
        LIMIT 1
        """,
        (phrase_norm,),
    ).fetchone()
    if row:
        return dict(row), "exact"

    row = db.execute(
        """
        SELECT id, phrase, intent, pattern
        FROM learned_commands
        WHERE skeleton=?
        LIMIT 1
        """,
        (skeleton,),
    ).fetchone()
    if row:
        return dict(row), "skeleton"

    return None, None


def ai_parse_default_command(command: str):
    text = normalize_ai_text(command)
    seats = ai_extract_seat_list(command)

    has_add = bool(re.search(r"\b(ekle|yaz|kaydet|oturt|bindir)\b", text))
    has_offload = bool(re.search(r"\b(boşalt|indir|indirdim|insin|sil)\b", text))
    has_service = bool(re.search(r"\b(servis|ikram|tamam|işaretle|verildi)\b", text))
    has_standing = "ayakta" in text
    has_query = bool(re.search(r"\b(hangi|kaç|sıradaki|durak|nerede|dolu|boş|kim)\b", text))

    if has_offload and len(seats) >= 2:
        return {"intent": "seat_remove_group", "pattern": "seat_list + offload", "confidence": 0.86, "seats": seats}
    if has_offload and len(seats) == 1:
        return {"intent": "seat_remove_single", "pattern": "seat + offload", "confidence": 0.83, "seats": seats}
    if has_standing and has_add:
        return {"intent": "standing_add", "pattern": "standing + add", "confidence": 0.84, "seats": seats}
    if has_add and len(seats) >= 2:
        return {"intent": "seat_add_group", "pattern": "seat_list + add", "confidence": 0.81, "seats": seats}
    if has_add and len(seats) == 1:
        return {"intent": "seat_add_single", "pattern": "seat + add", "confidence": 0.82, "seats": seats}
    if has_service:
        return {"intent": "service_mark", "pattern": "service + mark", "confidence": 0.58, "seats": seats}
    if has_query:
        return {"intent": "query", "pattern": "query", "confidence": 0.55, "seats": seats}

    return {"intent": None, "pattern": None, "confidence": 0.12, "seats": seats}


def resolve_ai_command(command: str):
    learned, match_type = ai_find_learned_match(command)
    if learned:
        return {
            "status": "matched",
            "source": f"learned_{match_type}",
            "intent": learned["intent"],
            "pattern": learned.get("pattern"),
            "confidence": 0.98,
            "seats": ai_extract_seat_list(command),
            "command": command,
        }

    parsed = ai_parse_default_command(command)

    if parsed["intent"] and parsed["confidence"] >= 0.80:
        return {
            "status": "matched",
            "source": "default_parser",
            "intent": parsed["intent"],
            "pattern": parsed["pattern"],
            "confidence": parsed["confidence"],
            "seats": parsed["seats"],
            "command": command,
        }

    if parsed["intent"] and parsed["confidence"] >= 0.45:
        return {
            "status": "suggest",
            "source": "default_parser",
            "intent": parsed["intent"],
            "pattern": parsed["pattern"],
            "confidence": parsed["confidence"],
            "seats": parsed["seats"],
            "command": command,
            "suggestion": {
                "intent": parsed["intent"],
                "pattern": parsed["pattern"],
            },
        }

    return {
        "status": "unknown",
        "source": "none",
        "intent": None,
        "pattern": None,
        "confidence": parsed["confidence"],
        "seats": parsed["seats"],
        "command": command,
    }


# =========================================================
# Auth sayfaları
# =========================================================

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


# =========================================================
# Ana sayfalar
# =========================================================

@app.route("/ai-console")
def ai_console_page():
    return render_template("ai_console.html")


@app.route("/")
def index():
    routes = all_route_names()
    current_route = session.get("route", routes[0] if routes else "Denizli – İstanbul")
    return render_template("index.html", current_route=current_route, all_routes=routes)


@app.route("/set-route", methods=["POST"])
def set_route():
    payload = request.get_json(silent=True) or {}
    route = (request.form.get("route") or payload.get("route") or "").strip()

    if not route:
        return jsonify({"ok": False, "msg": "route gerekli"}), 400
    if route not in set(all_route_names()):
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
            INSERT INTO trips(date, route, departure_time, plate, captain1, captain2, attendant, note)
            VALUES(?, ?, ?, ?, ?, ?, ?, ?)
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
        return redirect(url_for("seats_page"))

    now_str = datetime.now().strftime("%Y-%m-%d %H:%M")
    return render_template(
        "start_trip.html",
        now=now_str,
        current_route=session.get("route", "Denizli – İstanbul"),
    )


@app.route("/continue-trip")
def continue_trip():
    tid = get_active_trip()
    if tid:
        return redirect(url_for("seats_page"))
    return redirect(url_for("trip_start"))


@app.route("/seats")
def seats_page():
    tid = get_active_trip()
    if not tid:
        return redirect(url_for("trip_start"))

    db = get_db()
    trip = db.execute("SELECT * FROM trips WHERE id=?", (tid,)).fetchone()
    if not trip:
        set_active_trip(None)
        return redirect(url_for("trip_start"))

    rows = db.execute(
        """
        SELECT seat_no, from_stop, to_stop, gender,
               COALESCE(service,0) AS service,
               COALESCE(service_note,'') AS service_note
        FROM seats
        WHERE trip_id=?
        ORDER BY seat_no
        """,
        (tid,),
    ).fetchall()

    assigned = {r["seat_no"]: True for r in rows}
    stops_map = {r["seat_no"]: (r["to_stop"] or "") for r in rows}
    boards_map = {r["seat_no"]: (r["from_stop"] or "") for r in rows}
    genders = {r["seat_no"]: (r["gender"] or "") for r in rows}
    service_map = {r["seat_no"]: bool(r["service"]) for r in rows}
    service_notes = {r["seat_no"]: (r["service_note"] or "") for r in rows}

    return render_template(
        "seats.html",
        trip=trip,
        stops=get_stops(trip["route"]),
        seat_positions=SEAT_POSITIONS,
        assigned=assigned,
        stops_map=stops_map,
        boards_map=boards_map,
        genders=genders,
        service_map=service_map,
        service_notes=service_notes,
    )


@app.route("/yolcu-kontrol")
def passenger_control():
    tid = get_active_trip()
    if not tid:
        return redirect(url_for("trip_start"))
    trip = get_db().execute("SELECT * FROM trips WHERE id=?", (tid,)).fetchone()
    return render_template("passenger_control.html", trip=trip, stops=get_stops(trip["route"]))


# =========================================================
# Hat CRUD
# =========================================================

@app.route("/hatlar")
def routes_list():
    db = get_db()
    rows = db.execute("SELECT id, name FROM routes ORDER BY name").fetchall()
    db_names = {r["name"] for r in rows}

    builtin_routes = []
    for name in ROUTE_STOPS.keys():
        builtin_routes.append({
            "name": name,
            "overridden": name in db_names,
            "edit_url": url_for("builtin_route_edit", name=name),
        })

    return render_template("routes_list.html", routes=rows, builtin_routes=builtin_routes)


@app.route("/hat-ekle", methods=["GET", "POST"])
def add_route():
    if request.method == "POST":
        name = (request.form.get("name") or "").strip()
        stops_text = (request.form.get("stops") or "").strip()

        if not name or not stops_text:
            return "Hat adı ve duraklar zorunludur", 400

        db = get_db()
        db.execute(
            "INSERT OR REPLACE INTO routes(name, stops) VALUES(?, ?)",
            (name, json.dumps(parse_stops(stops_text), ensure_ascii=False)),
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

        db.execute(
            "UPDATE routes SET name=?, stops=? WHERE id=?",
            (name, json.dumps(stops, ensure_ascii=False), rid),
        )
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
        (name, json.dumps(stops, ensure_ascii=False)),
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
    row = db.execute("SELECT name FROM routes WHERE id=?", (rid,)).fetchone()
    db.execute("DELETE FROM routes WHERE id=?", (rid,))
    db.commit()

    if row and session.get("route") == row["name"]:
        session.pop("route", None)

    return redirect(url_for("routes_list"))


# =========================================================
# Fiyatlar
# =========================================================

def fetch_fare_exact(route: str, from_stop: str, to_stop: str) -> Optional[float]:
    row = get_db().execute(
        "SELECT price FROM fares WHERE route=? AND from_stop=? AND to_stop=?",
        (route, from_stop, to_stop),
    ).fetchone()
    return float(row["price"]) if row else None


def quote_price_segmented(route: str, from_stop: str, to_stop: str):
    stops = get_stops(route)
    if not stops or from_stop not in stops or to_stop not in stops:
        return None, "missing-stops"

    i = stops.index(from_stop)
    j = stops.index(to_stop)

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
        a, b = stops[k], stops[k + 1]
        row = db.execute(
            "SELECT price FROM fares WHERE route=? AND from_stop=? AND to_stop=?",
            (route, a, b),
        ).fetchone()
        if not row:
            return None, "segment-missing"
        total += float(row["price"])

    return total, "summed"


@app.route("/fiyat", methods=["GET"])
def fare_query():
    routes = all_route_names()
    route = (request.args.get("route") or (routes[0] if routes else "")).strip()
    stops = get_stops(route)
    from_stop = (request.args.get("from") or "").strip()
    to_stop = (request.args.get("to") or "").strip()

    price = None
    method = None
    msg = None

    if route and from_stop and to_stop:
        price, method = quote_price_segmented(route, from_stop, to_stop)
        if price is None:
            if method == "wrong-order":
                msg = "Biniş, inişten önce olmalı."
            elif method == "segment-missing":
                msg = "Segment fiyatı eksik."
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


@app.route("/fiyat-g", methods=["GET", "POST"])
def fare_admin():
    routes = all_route_names()

    if request.method == "POST":
        route = (request.form.get("route") or (routes[0] if routes else "")).strip()
        from_stop = (request.form.get("from") or "").strip()
        to_stop = (request.form.get("to") or "").strip()
        price = parse_float(request.form.get("price"), None)

        if not from_stop or not to_stop or price is None:
            stops = get_stops(route)
            fare_list = get_db().execute(
                "SELECT from_stop, to_stop, price FROM fares WHERE route=? ORDER BY rowid",
                (route,),
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
        db.execute(
            """
            INSERT INTO fares(route, from_stop, to_stop, price)
            VALUES(?, ?, ?, ?)
            ON CONFLICT(route, from_stop, to_stop) DO UPDATE SET
                price=excluded.price,
                updated_at=datetime('now','localtime')
            """,
            (route, from_stop, to_stop, price),
        )
        db.commit()

    route = (request.args.get("route") or (routes[0] if routes else "")).strip()
    from_stop = (request.args.get("from") or "").strip()
    to_stop = (request.args.get("to") or "").strip()
    stops = get_stops(route)

    row = get_db().execute(
        "SELECT price FROM fares WHERE route=? AND from_stop=? AND to_stop=?",
        (route, from_stop, to_stop),
    ).fetchone()
    current_price = float(row["price"]) if row else None

    fare_list = get_db().execute(
        "SELECT from_stop, to_stop, price FROM fares WHERE route=? ORDER BY rowid",
        (route,),
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


# =========================================================
# Hesap / kasa
# =========================================================

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


@app.route("/hesap")
def hesap_page():
    tid = get_active_trip()
    if not tid:
        return redirect(url_for("trip_start"))

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


@app.post("/hesap/devir")
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


@app.post("/hesap/giris")
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


@app.post("/hesap/cikis")
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


@app.post("/hesap/kategoriler")
def hesap_kategoriler_kaydet():
    save_cash_categories(request.form.get("cats_in") or "", request.form.get("cats_out") or "")
    return redirect(url_for("hesap_page"))


@app.route("/hesap/moves.csv")
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

    if intent == "query_total_passengers":
        seat_row = db.execute("SELECT COUNT(*) AS c FROM seats WHERE trip_id=?", (tid,)).fetchone()
        standing_row = db.execute(
            "SELECT COALESCE(SUM(pax),0) AS c FROM walk_on_sales WHERE trip_id=?",
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
        last = ai_last_stop_info(tid)
        if not last:
            return "Canlı durak için henüz stop log kaydı yok."
        return f"Son bilinen durak: {last['stop_name']} ({last['event']})."

    if intent == "query_next_stop":
        last = ai_last_stop_info(tid)
        stops = get_stops(trip_row["route"])

        if not stops:
            return "Bu hat için durak listesi bulunamadı."

        if not last:
            return f"Sıradaki durak: {stops[0]}"

        if last["stop_name"] not in stops:
            return f"Sıradaki durak hesaplanamadı. Son kayıt: {last['stop_name']}"

        idx = stops.index(last["stop_name"])
        next_idx = idx + 1

        if next_idx >= len(stops):
            return "Güzergâhın son durağındasın."

        return f"Sıradaki durak: {stops[next_idx]}"

    if intent == "query_delay":
        return "Rötar hesabı için saatli durak / ETA verisi backend tarafına henüz bağlanmadı."

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
        db.execute("DELETE FROM seats WHERE trip_id=? AND seat_no=?", (tid, seat_no))
        db.commit()
        return {
            "ok": True,
            "intent": intent,
            "deleted": [seat_no],
            "answer_text": f"{seat_no} numaralı koltuk boşaltıldı.",
        }

    if intent == "seat_remove_group":
        seats = entities.get("seats") or []
        if not seats:
            raise ValueError("Koltuk listesi gerekli")
        invalid = [s for s in seats if not validate_seat_no(s)]
        if invalid:
            raise ValueError(f"Geçersiz koltuklar: {invalid}")
        db.executemany("DELETE FROM seats WHERE trip_id=? AND seat_no=?", [(tid, s) for s in seats])
        db.commit()
        return {
            "ok": True,
            "intent": intent,
            "deleted": seats,
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

        if seat_list:
            db.executemany("DELETE FROM seats WHERE trip_id=? AND seat_no=?", [(tid, s) for s in seat_list])

        deleted_walkon = delete_walkon_rows(db, tid, to_stop=stop_name)
        db.commit()

        return {
            "ok": True,
            "intent": intent,
            "deleted_seats": seat_list,
            "deleted_standing_ids": deleted_walkon,
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

# =========================================================
# Koltuk API
# =========================================================

@app.route("/api/seats/list")
def api_seats_list():
    tid = get_active_trip()
    if not tid:
        return jsonify({"ok": False, "msg": "Aktif sefer yok", "items": []}), 400

    rows = get_db().execute(
        """
        SELECT seat_no,
               from_stop,
               to_stop AS stop,
               to_stop,
               ticket_type,
               payment,
               amount,
               gender,
               COALESCE(service,0) AS service,
               COALESCE(service_note,'') AS service_note
        FROM seats
        WHERE trip_id=?
        ORDER BY seat_no
        """,
        (tid,),
    ).fetchall()

    return jsonify({"ok": True, "items": [dict(r) for r in rows]})


@app.route("/api/seat", methods=["POST", "DELETE"])
def api_seat():
    tid = get_active_trip()
    if not tid:
        return jsonify({"ok": False, "msg": "Aktif sefer yok"}), 400

    db = get_db()

    if request.method == "DELETE":
        seat_no = parse_int(request.args.get("seat_no"), None)
        if seat_no is None:
            return jsonify({"ok": False, "msg": "seat_no geçersiz"}), 400
        if not validate_seat_no(seat_no):
            return jsonify({"ok": False, "msg": "Geçersiz koltuk numarası"}), 400

        db.execute("DELETE FROM seats WHERE trip_id=? AND seat_no=?", (tid, seat_no))
        db.commit()
        return jsonify({"ok": True})

    data = request.get_json(force=True) or {}
    seat_no = parse_int(data.get("seat_no"), None)

    if seat_no is None:
        return jsonify({"ok": False, "msg": "seat_no gerekli"}), 400
    if not validate_seat_no(seat_no):
        return jsonify({"ok": False, "msg": "Geçersiz koltuk numarası"}), 400

    from_stop = (data.get("from") or data.get("from_stop") or "").strip()
    to_stop = (data.get("stop") or data.get("to_stop") or data.get("to") or "").strip()

    if from_stop and not validate_stop_for_active_trip(from_stop):
        return jsonify({"ok": False, "msg": f"Durak hat üzerinde değil: {from_stop}"}), 400
    if to_stop and not validate_stop_for_active_trip(to_stop):
        return jsonify({"ok": False, "msg": f"Durak hat üzerinde değil: {to_stop}"}), 400

    ticket_type = norm_ticket_type(data.get("ticket_type"))
    payment = norm_payment(data.get("payment"))
    amount = parse_float(data.get("amount"), 0.0) or 0.0
    gender = norm_gender(data.get("gender"))
    pair_ok = bool(data.get("pair_ok"))
    service = norm_bool(data.get("service"))
    service_note = (data.get("service_note") or "").strip()
    passenger_name = (data.get("passenger_name") or "").strip()
    passenger_phone = (data.get("passenger_phone") or "").strip()

    ok, msg = neighbor_rule_ok(tid, seat_no, gender, pair_ok)
    if not ok:
        return jsonify({"ok": False, "msg": msg}), 400

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
            tid, seat_no, from_stop, to_stop, ticket_type, payment, amount,
            gender, 1 if pair_ok else 0, service, service_note,
            passenger_name, passenger_phone,
        ),
    )
    db.commit()
    return jsonify({"ok": True})

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
            tid, seat_no, from_stop, to_stop, ticket_type, payment, amount,
            gender, 1 if pair_ok else 0, service, service_note,
            passenger_name, passenger_phone,
        ),
    )
    db.commit()
    return jsonify({"ok": True})

@app.route("/api/seats/bulk", methods=["POST", "DELETE"])
def api_seats_bulk():
    tid = get_active_trip()
    if not tid:
        return jsonify({"ok": False, "msg": "Aktif sefer yok"}), 400

    db = get_db()

    if request.method == "DELETE":
        raw = (request.args.get("seats") or "").strip()
        if not raw:
            return jsonify({"ok": False, "msg": "seats gerekli"}), 400

        seat_list = parse_int_list(raw)
        if not seat_list:
            return jsonify({"ok": False, "msg": "seats geçersiz"}), 400

        invalid = [s for s in seat_list if not validate_seat_no(s)]
        if invalid:
            return jsonify({"ok": False, "msg": f"Geçersiz koltuklar: {invalid}"}), 400

        db.executemany(
            "DELETE FROM seats WHERE trip_id=? AND seat_no=?",
            [(tid, s) for s in seat_list],
        )
        db.commit()
        return jsonify({"ok": True, "deleted": seat_list})

    data = request.get_json(force=True) or {}
    seats = data.get("seats")

    if not isinstance(seats, list) or not seats:
        return jsonify({"ok": False, "msg": "seats listesi gerekli"}), 400

    from_stop = (data.get("from") or data.get("from_stop") or "").strip()
    to_stop = (data.get("stop") or data.get("to_stop") or data.get("to") or "").strip()

    if from_stop and not validate_stop_for_active_trip(from_stop):
        return jsonify({"ok": False, "msg": f"Durak hat üzerinde değil: {from_stop}"}), 400
    if to_stop and not validate_stop_for_active_trip(to_stop):
        return jsonify({"ok": False, "msg": f"Durak hat üzerinde değil: {to_stop}"}), 400

    ticket_type = norm_ticket_type(data.get("ticket_type"))
    payment = norm_payment(data.get("payment") or "nakit")
    amount = parse_float(data.get("amount"), 0.0) or 0.0
    service = norm_bool(data.get("service"))
    service_note = (data.get("service_note") or "").strip()

    rows = []

    for item in seats:
        if isinstance(item, dict):
            seat_no = parse_int(item.get("seat_no"), None)
            if seat_no is None:
                return jsonify({"ok": False, "msg": "seat_no geçersiz"}), 400
            if not validate_seat_no(seat_no):
                return jsonify({"ok": False, "msg": f"Geçersiz koltuk numarası: {seat_no}"}), 400

            row_from = (item.get("from") or item.get("from_stop") or from_stop or "").strip()
            row_to = (item.get("stop") or item.get("to_stop") or item.get("to") or to_stop or "").strip()
            row_ticket = norm_ticket_type(item.get("ticket_type") or ticket_type)
            row_payment = norm_payment(item.get("payment") or payment)
            row_amount = parse_float(item.get("amount"), amount) or 0.0
            row_gender = norm_gender(item.get("gender"))
            row_pair_ok = bool(item.get("pair_ok"))
            row_service = norm_bool(item.get("service"))
            row_service_note = (item.get("service_note") or service_note or "").strip()

            if row_from and not validate_stop_for_active_trip(row_from):
                return jsonify({"ok": False, "msg": f"Durak hat üzerinde değil: {row_from}"}), 400
            if row_to and not validate_stop_for_active_trip(row_to):
                return jsonify({"ok": False, "msg": f"Durak hat üzerinde değil: {row_to}"}), 400

            ok, msg = neighbor_rule_ok(tid, seat_no, row_gender, row_pair_ok)
            if not ok:
                return jsonify({"ok": False, "msg": msg}), 400

            rows.append((
                tid, seat_no, row_from, row_to, row_ticket, row_payment, row_amount,
                row_gender, 1 if row_pair_ok else 0, row_service, row_service_note, "", "",
            ))

        else:
            seat_no = parse_int(item, None)
            if seat_no is None:
                return jsonify({"ok": False, "msg": "seat_no geçersiz"}), 400
            if not validate_seat_no(seat_no):
                return jsonify({"ok": False, "msg": f"Geçersiz koltuk numarası: {seat_no}"}), 400

            rows.append((
                tid, seat_no, from_stop, to_stop, ticket_type, payment, amount,
                "", 0, service, service_note, "", "",
            ))

    db.executemany(
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
        rows,
    )
    db.commit()

    return jsonify({"ok": True, "count": len(rows)})

@app.route("/api/seats/offload", methods=["POST"])
def api_seats_offload():
    tid = get_active_trip()
    if not tid:
        return jsonify({"ok": False, "msg": "Aktif sefer yok"}), 400

    data = request.get_json(force=True) or {}
    seats = data.get("seats")

    if not isinstance(seats, list) or not seats:
        return jsonify({"ok": False, "msg": "seats listesi gerekli"}), 400

    try:
        seat_list = [int(x if not isinstance(x, dict) else x.get("seat_no")) for x in seats]
    except Exception:
        return jsonify({"ok": False, "msg": "seats geçersiz"}), 400

    invalid = [s for s in seat_list if not validate_seat_no(s)]
    if invalid:
        return jsonify({"ok": False, "msg": f"Geçersiz koltuklar: {invalid}"}), 400

    db = get_db()
    db.executemany("DELETE FROM seats WHERE trip_id=? AND seat_no=?", [(tid, s) for s in seat_list])
    db.commit()

    return jsonify({"ok": True, "deleted": seat_list})

@app.post("/api/seats/service")
def api_seats_service():
    tid = get_active_trip()
    if not tid:
        return jsonify({"ok": False, "msg": "Aktif sefer yok"}), 400

    data = request.get_json(force=True) or {}
    seats = data.get("seats")
    if not isinstance(seats, list) or not seats:
        return jsonify({"ok": False, "msg": "seats listesi gerekli"}), 400

    service = norm_bool(data.get("service", 1))
    service_note = (data.get("service_note") or "").strip()

    try:
        seat_list = [int(x if not isinstance(x, dict) else x.get("seat_no")) for x in seats]
    except Exception:
        return jsonify({"ok": False, "msg": "seats geçersiz"}), 400

    db = get_db()
    db.executemany(
        """
        UPDATE seats
        SET service=?, service_note=?
        WHERE trip_id=? AND seat_no=?
        """,
        [(service, service_note, tid, s) for s in seat_list],
    )
    db.commit()

    return jsonify({
        "ok": True,
        "updated": seat_list,
        "service": service,
        "service_note": service_note,
    })


# =========================================================
# Durak / koordinat API
# =========================================================

@app.route("/api/stops")
def api_stops():
    trip = get_active_trip_row()
    if not trip:
        return jsonify({"ok": False, "msg": "Aktif sefer yok", "stops": []}), 400

    route_name = trip["route"]
    return jsonify({"ok": True, "route": route_name, "stops": get_stops(route_name)})


@app.route("/api/coords", methods=["GET", "POST", "DELETE"])
def api_coords():
    trip = get_active_trip_row()
    if not trip:
        return jsonify({"ok": False, "msg": "Aktif sefer yok"}), 400

    db = get_db()
    route_name = trip["route"]

    if request.method == "GET":
        rows = db.execute(
            "SELECT stop, lat, lng FROM route_stop_coords WHERE route=? ORDER BY stop",
            (route_name,),
        ).fetchall()
        return jsonify({
            "ok": True,
            "route": route_name,
            "items": [{"stop": r["stop"], "lat": float(r["lat"]), "lng": float(r["lng"])} for r in rows],
        })

    if request.method == "POST":
        data = request.get_json(force=True) or {}
        stop = (data.get("stop") or "").strip()
        lat = parse_float(data.get("lat"), None)
        lng = parse_float(data.get("lng"), None)

        if not stop:
            return jsonify({"ok": False, "msg": "stop gerekli"}), 400
        if lat is None or lng is None:
            return jsonify({"ok": False, "msg": "lat/lng geçersiz"}), 400
        if not validate_stop_for_trip(route_name, stop):
            return jsonify({"ok": False, "msg": "Durak hat üzerinde değil"}), 400

        db.execute(
            """
            INSERT INTO route_stop_coords(route, stop, lat, lng)
            VALUES(?,?,?,?)
            ON CONFLICT(route, stop) DO UPDATE SET
                lat=excluded.lat,
                lng=excluded.lng
            """,
            (route_name, stop, lat, lng),
        )
        db.commit()
        return jsonify({"ok": True})

    stop = (request.args.get("stop") or "").strip()
    if not stop:
        return jsonify({"ok": False, "msg": "stop gerekli"}), 400

    db.execute("DELETE FROM route_stop_coords WHERE route=? AND stop=?", (route_name, stop))
    db.commit()
    return jsonify({"ok": True})


# =========================================================
# Ayakta / walk-on API
# =========================================================
@app.route("/api/walkon", methods=["GET", "POST", "DELETE"])
def api_walkon():
    tid = get_active_trip()
    if not tid:
        return jsonify({"ok": False, "msg": "Aktif sefer yok"}), 400

    db = get_db()

    if request.method == "GET":
        if request.args.get("aggregate"):
            row = db.execute(
                """
                SELECT COALESCE(SUM(total_amount),0) AS total_amount,
                       COALESCE(SUM(pax),0) AS pax
                FROM walk_on_sales
                WHERE trip_id=?
                """,
                (tid,),
            ).fetchone()
            return jsonify({
                "ok": True,
                "pax": int(row["pax"]),
                "total_amount": float(row["total_amount"]),
            })

        rows = db.execute(
            "SELECT * FROM walk_on_sales WHERE trip_id=? ORDER BY id DESC",
            (tid,),
        ).fetchall()
        return jsonify({"ok": True, "items": [dict(r) for r in rows]})

    if request.method == "POST":
        data = request.get_json(force=True) or {}

        from_stop = (data.get("from_stop") or data.get("from") or "").strip()
        to_stop = (data.get("to_stop") or data.get("to") or "").strip()

        if not to_stop:
            return jsonify({"ok": False, "msg": "to gerekli"}), 400

        if from_stop and not validate_stop_for_active_trip(from_stop):
            return jsonify({"ok": False, "msg": f"Durak hat üzerinde değil: {from_stop}"}), 400
        if to_stop and not validate_stop_for_active_trip(to_stop):
            return jsonify({"ok": False, "msg": f"Durak hat üzerinde değil: {to_stop}"}), 400

        pax = max(1, parse_int(data.get("pax") or data.get("count"), 1) or 1)
        unit_price = parse_float(data.get("unit_price") or data.get("price"), 0.0) or 0.0
        total_amount = parse_float(data.get("total_amount"), None)
        if total_amount is None:
            total_amount = pax * unit_price

        payment = norm_payment(data.get("payment"))
        note = (data.get("note") or "").strip()

        db.execute(
            """
            INSERT INTO walk_on_sales(trip_id, from_stop, to_stop, pax, unit_price, total_amount, payment, note)
            VALUES(?,?,?,?,?,?,?,?)
            """,
            (tid, from_stop, to_stop, pax, unit_price, total_amount, payment, note),
        )
        db.commit()
        new_id = db.execute("SELECT last_insert_rowid()").fetchone()[0]

        return jsonify({
            "ok": True,
            "id": new_id,
            "pax": pax,
            "total_amount": total_amount,
        })

    item_id = parse_int(request.args.get("id"), None)
    ids = parse_int_list(request.args.get("ids") or "")
    to_param = (request.args.get("to_stop") or request.args.get("to") or "").strip()
    clear_all = bool(norm_bool(request.args.get("all")))

    if to_param and not validate_stop_for_active_trip(to_param):
        return jsonify({"ok": False, "msg": f"Durak hat üzerinde değil: {to_param}"}), 400

    if item_id is None and not ids and not to_param and not clear_all:
        return jsonify({"ok": False, "msg": "id, ids, to/to_stop veya all gerekli"}), 400

    deleted_ids = delete_walkon_rows(
        db,
        tid,
        item_id=item_id,
        ids=ids or None,
        to_stop=to_param or None,
        clear_all=clear_all,
    )
    db.commit()

    return jsonify({
        "ok": True,
        "deleted": deleted_ids,
        "count": len(deleted_ids),
    })

@app.route("/api/standing", methods=["GET", "POST", "DELETE"])
def api_standing():
    tid = get_active_trip()
    if not tid:
        return jsonify({"ok": False, "msg": "Aktif sefer yok"}), 400

    db = get_db()

    if request.method == "GET":
        row = db.execute(
            """
            SELECT COALESCE(SUM(total_amount),0) AS total_amount,
                   COALESCE(SUM(pax),0) AS pax
            FROM walk_on_sales
            WHERE trip_id=?
            """,
            (tid,),
        ).fetchone()

        return jsonify({
            "ok": True,
            "count": int(row["pax"] or 0),
            "revenue": float(row["total_amount"] or 0.0),
        })

    if request.method == "POST":
        data = request.get_json(force=True) or {}

        from_stop = (data.get("from_stop") or data.get("from") or "").strip()
        to_stop = (data.get("to_stop") or data.get("to") or "").strip()

        if not to_stop:
            return jsonify({"ok": False, "msg": "to gerekli"}), 400

        if from_stop and not validate_stop_for_active_trip(from_stop):
            return jsonify({"ok": False, "msg": f"Durak hat üzerinde değil: {from_stop}"}), 400
        if to_stop and not validate_stop_for_active_trip(to_stop):
            return jsonify({"ok": False, "msg": f"Durak hat üzerinde değil: {to_stop}"}), 400

        pax = max(1, parse_int(data.get("pax") or data.get("count"), 1) or 1)
        unit_price = parse_float(data.get("unit_price") or data.get("price"), 0.0) or 0.0
        total_amount = parse_float(data.get("total_amount"), None)
        if total_amount is None:
            total_amount = pax * unit_price

        payment = norm_payment(data.get("payment"))
        note = (data.get("note") or "").strip()

        db.execute(
            """
            INSERT INTO walk_on_sales(trip_id, from_stop, to_stop, pax, unit_price, total_amount, payment, note)
            VALUES(?,?,?,?,?,?,?,?)
            """,
            (tid, from_stop, to_stop, pax, unit_price, total_amount, payment, note),
        )
        db.commit()
        new_id = db.execute("SELECT last_insert_rowid()").fetchone()[0]

        return jsonify({
            "ok": True,
            "id": new_id,
            "pax": pax,
            "total_amount": total_amount,
        })

    item_id = parse_int(request.args.get("id"), None)
    ids = parse_int_list(request.args.get("ids") or "")
    to_param = (request.args.get("to_stop") or request.args.get("to") or "").strip()
    clear_all = bool(norm_bool(request.args.get("all")))

    if to_param and not validate_stop_for_active_trip(to_param):
        return jsonify({"ok": False, "msg": f"Durak hat üzerinde değil: {to_param}"}), 400

    if item_id is None and not ids and not to_param and not clear_all:
        return jsonify({"ok": False, "msg": "id, ids, to/to_stop veya all gerekli"}), 400

    deleted_ids = delete_walkon_rows(
        db,
        tid,
        item_id=item_id,
        ids=ids or None,
        to_stop=to_param or None,
        clear_all=clear_all,
    )
    db.commit()

    return jsonify({
        "ok": True,
        "deleted": deleted_ids,
        "count": len(deleted_ids),
    })

@app.route("/api/standing/list")
def api_standing_list():
    tid = get_active_trip()
    if not tid:
        return jsonify({"ok": False, "msg": "Aktif sefer yok", "items": []}), 400

    rows = get_db().execute(
        """
        SELECT id, from_stop, to_stop, pax, unit_price, total_amount, payment, note, created_at
        FROM walk_on_sales
        WHERE trip_id=?
        ORDER BY id DESC
        """,
        (tid,),
    ).fetchall()

    items = [{
        "id": r["id"],
        "from": r["from_stop"],
        "to": r["to_stop"],
        "count": r["pax"],
        "price": r["unit_price"],
        "total_amount": r["total_amount"],
        "payment": r["payment"],
        "note": r["note"],
        "ts": r["created_at"],
    } for r in rows]

    return jsonify({"ok": True, "items": items})

# =========================================================
# İstatistik API
# =========================================================

@app.route("/api/stats")
def api_stats():
    tid = get_active_trip()
    if not tid:
        return jsonify({"ok": False, "msg": "Aktif sefer yok"}), 400

    db = get_db()

    seat_row = db.execute(
        """
        SELECT COUNT(*) AS c,
               COALESCE(SUM(amount),0) AS s,
               COALESCE(SUM(service),0) AS svc
        FROM seats
        WHERE trip_id=?
        """,
        (tid,),
    ).fetchone()

    walk_row = db.execute(
        """
        SELECT COALESCE(SUM(pax),0) AS pax,
               COALESCE(SUM(total_amount),0) AS tot
        FROM walk_on_sales
        WHERE trip_id=?
        """,
        (tid,),
    ).fetchone()

    by_pay = {}
    for r in db.execute(
        "SELECT payment, COALESCE(SUM(amount),0) AS s FROM seats WHERE trip_id=? GROUP BY payment",
        (tid,),
    ).fetchall():
        by_pay[r["payment"]] = by_pay.get(r["payment"], 0.0) + float(r["s"])

    for r in db.execute(
        "SELECT payment, COALESCE(SUM(total_amount),0) AS s FROM walk_on_sales WHERE trip_id=? GROUP BY payment",
        (tid,),
    ).fetchall():
        by_pay[r["payment"]] = by_pay.get(r["payment"], 0.0) + float(r["s"])

    seats_revenue = float(seat_row["s"] or 0)
    walkon_revenue = float(walk_row["tot"] or 0)

    return jsonify({
        "ok": True,
        "seats_reserved": int(seat_row["c"] or 0),
        "seats_revenue": seats_revenue,
        "walkon_pax": int(walk_row["pax"] or 0),
        "walkon_revenue": walkon_revenue,
        "total_revenue": seats_revenue + walkon_revenue,
        "by_payment": by_pay,
        "service_count": int(seat_row["svc"] or 0),
    })


# =========================================================
# Stop log API
# =========================================================

def seats_count_for_stop(tid: int, stop_name: str) -> int:
    row = get_db().execute(
        "SELECT COUNT(*) AS c FROM seats WHERE trip_id=? AND to_stop=?",
        (tid, stop_name),
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
            SELECT id, trip_id, stop_name, event, distance_km, seats_for_stop, meta_json, ts
            FROM stop_logs
            WHERE trip_id=?
            ORDER BY ts DESC, id DESC
            """,
            (tid,),
        ).fetchall()

        items = []
        for r in rows:
            try:
                meta = json.loads(r["meta_json"]) if r["meta_json"] else None
            except Exception:
                meta = None

            items.append({
                "id": r["id"],
                "trip_id": r["trip_id"],
                "stop_name": r["stop_name"],
                "event": r["event"],
                "distance_km": r["distance_km"],
                "seats_for_stop": r["seats_for_stop"],
                "meta": meta,
                "ts": r["ts"],
            })

        return jsonify({"ok": True, "items": items})

    data = request.get_json(force=True) or {}
    stop_name = (data.get("stop_name") or data.get("stop") or "").strip()
    event = (data.get("event") or "arrive").strip().lower()

    if not stop_name:
        return jsonify({"ok": False, "msg": "stop_name gerekli"}), 400
    if not validate_stop_for_active_trip(stop_name):
        return jsonify({"ok": False, "msg": "Durak bu hat üzerinde değil"}), 400
    if event not in {"arrive", "depart", "approach"}:
        return jsonify({"ok": False, "msg": "event geçersiz"}), 400

    distance_km = data.get("distance_km")
    if distance_km is not None:
        distance_km = parse_float(distance_km, None)
        if distance_km is None:
            return jsonify({"ok": False, "msg": "distance_km geçersiz"}), 400

    seats_for_stop = seats_count_for_stop(tid, stop_name)
    meta = data.get("meta")
    try:
        meta_json = json.dumps(meta, ensure_ascii=False) if isinstance(meta, (dict, list)) else None
    except Exception:
        meta_json = None

    db.execute(
        """
        INSERT INTO stop_logs(trip_id, stop_name, event, distance_km, seats_for_stop, meta_json)
        VALUES(?,?,?,?,?,?)
        """,
        (tid, stop_name, event, distance_km, seats_for_stop, meta_json),
    )
    db.commit()

    return jsonify({
        "ok": True,
        "stop_name": stop_name,
        "event": event,
        "distance_km": distance_km,
        "seats_for_stop": seats_for_stop,
    })


@app.route("/olaylar")
def events_page():
    return render_template("events.html")


@app.route("/api/events")
def api_events():
    route = (request.args.get("route") or "").strip()
    d1 = request.args.get("date_from")
    d2 = request.args.get("date_to")

    sql = """
    SELECT l.id, l.trip_id, t.date, t.route, l.stop_name, l.event, l.distance_km,
           l.seats_for_stop, l.meta_json, l.ts
    FROM stop_logs l
    JOIN trips t ON t.id = l.trip_id
    WHERE 1=1
    """
    args = []

    if route:
        sql += " AND t.route=?"
        args.append(route)
    if d1:
        sql += " AND t.date >= ?"
        args.append(d1)
    if d2:
        sql += " AND t.date <= ?"
        args.append(d2)

    sql += " ORDER BY l.ts DESC, l.id DESC LIMIT 500"
    rows = get_db().execute(sql, args).fetchall()

    items = []
    for r in rows:
        try:
            meta = json.loads(r["meta_json"]) if r["meta_json"] else None
        except Exception:
            meta = None

        items.append({
            "id": r["id"],
            "trip_id": r["trip_id"],
            "date": r["date"],
            "route": r["route"],
            "stop_name": r["stop_name"],
            "event": r["event"],
            "distance_km": r["distance_km"],
            "seats_for_stop": r["seats_for_stop"],
            "meta": meta,
            "ts": r["ts"],
        })

    return jsonify({"ok": True, "items": items})


# =========================================================
# Raporlar
# =========================================================

@app.route("/raporlar")
def reports_page():
    return render_template("reports.html", all_routes=all_route_names())


@app.route("/api/report/seat-stats")
def api_report_seat_stats():
    route = (request.args.get("route") or "").strip()
    d1 = request.args.get("date_from")
    d2 = request.args.get("date_to")

    where = ["1=1"]
    args = []

    if route:
        where.append("t.route=?")
        args.append(route)
    if d1:
        where.append("t.date >= ?")
        args.append(d1)
    if d2:
        where.append("t.date <= ?")
        args.append(d2)

    sql_where = " AND ".join(where)
    db = get_db()

    per = db.execute(
        f"""
        SELECT s.seat_no, COUNT(*) AS times, COALESCE(SUM(s.amount),0) AS revenue
        FROM seats s
        JOIN trips t ON t.id=s.trip_id
        WHERE {sql_where}
        GROUP BY s.seat_no
        ORDER BY s.seat_no
        """,
        args,
    ).fetchall()

    per_seat = [{
        "seat_no": int(r["seat_no"]),
        "times": int(r["times"]),
        "revenue": float(r["revenue"]),
    } for r in per]

    sold_seats = {x["seat_no"] for x in per_seat}
    never_sold = [n for n in SEAT_NUMBERS if n not in sold_seats]

    seat_tot = db.execute(
        f"""
        SELECT COALESCE(SUM(s.amount),0) AS revenue, COUNT(*) AS cnt
        FROM seats s
        JOIN trips t ON t.id=s.trip_id
        WHERE {sql_where}
        """,
        args,
    ).fetchone()

    walk_tot = db.execute(
        f"""
        SELECT COALESCE(SUM(w.total_amount),0) AS revenue, COALESCE(SUM(w.pax),0) AS pax
        FROM walk_on_sales w
        JOIN trips t ON t.id=w.trip_id
        WHERE {sql_where}
        """,
        args,
    ).fetchone()

    top_seat = max(per_seat, key=lambda x: (x["times"], x["revenue"])) if per_seat else None

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


# =========================================================
# Emanetler
# =========================================================

@app.route("/emanetler")
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


@app.route("/api/consignments", methods=["GET", "POST"])
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


@app.get("/api/parcels")
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


@app.route("/api/consignments/<int:cid>/photos", methods=["GET", "POST"])
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


@app.route("/api/consignments/<int:cid>", methods=["DELETE"])
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


# =========================================================
# Upload serve
# =========================================================

@app.route("/u/<path:filename>")
def serve_uploaded(filename):
    safe_name = secure_filename(filename)
    return send_from_directory(UPLOAD_DIR, safe_name, as_attachment=False)


# =========================================================
# Bagaj meta + clear
# =========================================================

@app.get("/api/bags/meta")
def api_bags_meta():
    trip_code = (request.args.get("trip") or request.args.get("trip_code") or "").strip()
    seat_no = (request.args.get("seat") or "").strip()

    if not trip_code or not seat_no:
        return jsonify({
            "ok": False,
            "msg": "trip ve seat gerekli",
            "count": 0,
            "right": 0,
            "left_front": 0,
            "left_back": 0,
            "eyes": [],
        }), 400

    d = bag_root() / safe(trip_code) / safe(seat_no)
    right = left_front = left_back = 0
    exts = (".jpg", ".jpeg", ".png", ".webp")

    if d.exists() and d.is_dir():
        for p in d.iterdir():
            if not p.is_file():
                continue
            low = p.name.lower()
            if ".thumb." in low or not low.endswith(exts):
                continue
            if p.name.startswith("R_"):
                right += 1
            elif p.name.startswith("LF_"):
                left_front += 1
            elif p.name.startswith("LB_"):
                left_back += 1
            else:
                right += 1

    total = right + left_front + left_back
    eyes = []
    if right:
        eyes.append("R")
    if left_front:
        eyes.append("LF")
    if left_back:
        eyes.append("LB")

    return jsonify({
        "ok": True,
        "count": total,
        "right": right,
        "left_front": left_front,
        "left_back": left_back,
        "eyes": eyes,
    })


@app.route("/bags/clear", methods=["DELETE"])
def bags_clear_alias():
    trip = (request.args.get("trip") or request.args.get("trip_code") or "").strip()
    seat = (request.args.get("seat") or "").strip()

    if not trip or not seat:
        return jsonify({"ok": False, "msg": "trip ve seat gerekli"}), 400

    d = bag_root() / safe(trip) / safe(seat)
    deleted = 0

    if d.exists() and d.is_dir():
        for p in d.iterdir():
            try:
                if p.is_file():
                    p.unlink(missing_ok=True)
                    deleted += 1
            except Exception:
                pass
        try:
            d.rmdir()
        except Exception:
            pass

    return jsonify({"ok": True, "deleted": deleted})


# =========================================================
# Sefer bitir / health
# =========================================================

@app.route("/end-trip", methods=["POST"])
def end_trip():
    tid = get_active_trip()
    db = get_db()

    if tid:
        db.execute("DELETE FROM seats WHERE trip_id=?", (tid,))
        db.execute("DELETE FROM walk_on_sales WHERE trip_id=?", (tid,))
        db.execute("DELETE FROM stop_logs WHERE trip_id=?", (tid,))
        db.execute("UPDATE app_state SET active_trip_id=NULL WHERE id=1")
        db.commit()
    else:
        db.execute("UPDATE app_state SET active_trip_id=NULL WHERE id=1")
        db.commit()

    return redirect(url_for("index"))

# =========================================================
# Run
# =========================================================

if __name__ == "__main__":
    with app.app_context():
        ensure_schema()
        ensure_upload_dir()

    app.run(host="0.0.0.0", port=PORT, debug=DEBUG)
