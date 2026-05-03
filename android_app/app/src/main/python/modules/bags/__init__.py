from __future__ import annotations

import json
import os
import secrets
import time
from pathlib import Path
from urllib.parse import urlparse

from flask import (
    Blueprint,
    abort,
    current_app,
    jsonify,
    redirect,
    render_template_string,
    request,
    send_from_directory,
    session,
    url_for,
)
from PIL import Image

bp = Blueprint("bags", __name__, url_prefix="/bags")


# ---------------- CSRF ----------------
def _get_csrf() -> str:
    token = session.get("csrf_token")
    if not token:
        token = secrets.token_hex(16)
        session["csrf_token"] = token
    return token


def _check_csrf() -> None:
    token = request.form.get("csrf_token", "") or request.headers.get("X-CSRF-Token", "")
    if token != session.get("csrf_token"):
        abort(403, description="CSRF doğrulaması başarısız")


# ------------- URL yardımcılar ----------
def _normalize_next(url: str | None) -> str:
    path = urlparse(url or "").path
    if not path:
        return "/seats"
    if path.endswith(".html"):
        path = path[:-5]
    if not path.startswith("/"):
        path = "/" + path
    return path or "/seats"


def _back_url() -> str:
    return _normalize_next(request.values.get("next") or request.headers.get("Referer") or "/seats")


# ------------- Depo yolları ----------
def bag_root() -> Path:
    root = Path(current_app.root_path).parent / "storage" / "bags"
    root.mkdir(parents=True, exist_ok=True)
    return root


def safe(s: str) -> str:
    return "".join(c for c in (s or "") if c.isalnum() or c in "-_")


def seat_dir(trip: str, seat: str) -> Path:
    return bag_root() / safe(trip) / safe(seat)


def thumb_path(img_path: Path) -> Path:
    return img_path.with_suffix(".thumb.jpg")


def _is_image(p: Path) -> bool:
    return p.suffix.lower() in {".jpg", ".jpeg", ".png", ".webp"} and ".thumb." not in p.name.lower()


def ensure_thumb(img_path: Path):
    """Var olmayan thumb'ı üret."""
    if ".thumb." in img_path.name.lower():
        return
    t = thumb_path(img_path)
    if t.exists():
        return
    try:
        with Image.open(img_path) as im:
            im.thumbnail((480, 480))
            im.convert("RGB").save(t, "JPEG", quality=82, optimize=True)
    except Exception:
        pass


# ------------- meta.json (adet kaydı) ----------
def meta_path(trip: str, seat: str) -> Path:
    return seat_dir(trip, seat) / "meta.json"


def read_meta(trip: str, seat: str) -> dict:
    p = meta_path(trip, seat)
    if not p.exists():
        return {}
    try:
        return json.loads(p.read_text(encoding="utf-8"))
    except Exception:
        return {}


def write_meta(trip: str, seat: str, meta: dict) -> None:
    d = seat_dir(trip, seat)
    d.mkdir(parents=True, exist_ok=True)
    p = meta_path(trip, seat)
    try:
        p.write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8")
    except Exception:
        # yazamazsa sessiz geç (uygulama çökmemeli)
        pass


def get_counts(trip: str, seat: str) -> tuple[int, int, int]:
    """
    Önce meta.json -> counts.
    Eğer meta yoksa klasörden scan ile MAX prefix'i yakala.
    """
    meta = read_meta(trip, seat) or {}
    counts = meta.get("counts")
    if isinstance(counts, dict):
        try:
            r = int(counts.get("R", 0) or 0)
            lf = int(counts.get("LF", 0) or 0)
            lb = int(counts.get("LB", 0) or 0)
            return max(0, r), max(0, lf), max(0, lb)
        except Exception:
            pass

    # fallback: klasörden tara
    d = seat_dir(trip, seat)
    return _scan_counts(d)


def _scan_counts(d: Path) -> tuple[int, int, int]:
    """
    Klasördeki dosya adlarına bakarak
    sağ / sol ön / sol arka için MAX bagaj adetlerini bulur.
    Dosya adı formatı: R3_..., LF2_..., LB10_...
    """
    right = left_front = left_back = 0
    if not (d.exists() and d.is_dir()):
        return right, left_front, left_back

    for p in d.iterdir():
        if not (p.is_file() and _is_image(p)):
            continue

        name = p.name
        side_key = "R"
        bag_count = 1

        if "_" in name:
            prefix = name.split("_", 1)[0]  # R3, LF2, LB10...
            letters = "".join(ch for ch in prefix if ch.isalpha()).upper()
            digits = "".join(ch for ch in prefix if ch.isdigit())

            if digits:
                try:
                    bag_count = max(1, int(digits))
                except ValueError:
                    bag_count = 1

            if letters in ("R", "LF", "LB"):
                side_key = letters

        if side_key == "R":
            right = max(right, bag_count)
        elif side_key == "LF":
            left_front = max(left_front, bag_count)
        elif side_key == "LB":
            left_back = max(left_back, bag_count)
        else:
            right = max(right, bag_count)

    return right, left_front, left_back


def _pick_default_side(trip: str, seat: str, requested: str | None) -> str:
    """
    side gelirse onu kullan.
    side gelmezse:
      - meta/scan ile hangi göz doluysa onu seç
      - karışık/boş ise R
    """
    s = (requested or "").upper().strip()
    if s in ("R", "LF", "LB"):
        return s

    r, lf, lb = get_counts(trip, seat)
    if r > 0 and lf == 0 and lb == 0:
        return "R"
    if lf > 0 and r == 0 and lb == 0:
        return "LF"
    if lb > 0 and r == 0 and lf == 0:
        return "LB"
    return "R"


# =========================
#        /bags  (GALERİ)
# =========================

def _side_from_filename(filename: str) -> str:
    """
    Dosya adından bagaj gözünü bulur.
    Destek: R1_..., LF2_..., LB3_..., eski R_ / LF_ / LB_ formatları.
    """
    name = filename or ""
    prefix = name.split("_", 1)[0] if "_" in name else name
    letters = "".join(ch for ch in prefix if ch.isalpha()).upper()

    if letters in ("R", "LF", "LB"):
        return letters

    if name.upper().startswith("LF"):
        return "LF"
    if name.upper().startswith("LB"):
        return "LB"
    return "R"


def _side_label(side: str) -> str:
    return {
        "R": "Sağ göz",
        "LF": "Sol ön",
        "LB": "Sol arka",
    }.get((side or "").upper(), "Sağ göz")


def _side_icon(side: str) -> str:
    return {
        "R": "➡️",
        "LF": "⬅️🔺",
        "LB": "⬅️🔻",
    }.get((side or "").upper(), "➡️")


def _clamp_bag_count(raw, default: int = 1) -> int:
    try:
        n = int(raw)
    except Exception:
        n = default
    return max(1, min(n, 10))


@bp.route("", methods=["GET", "POST"])
def gallery():
    """
    Profesyonel bagaj ekranı:
    - Göz kartları
    - +/- adet seçici
    - Fotoğrafları sağ / sol ön / sol arka olarak gruplar
    - Fotoğraf olmasa bile adet meta.json içine kaydedilir
    - ?format=json sayaç döndürür
    """

    trip = request.values.get("trip", "") or request.values.get("trip_code", "")
    seat = request.values.get("seat", "")
    fmt = (request.args.get("format", "") or "").lower()
    nxt = _back_url()

    d = seat_dir(trip, seat)
    side = _pick_default_side(trip, seat, request.values.get("side"))
    bag_count_default = _clamp_bag_count(request.values.get("bag_count", ""), 1)

    # -------- JSON sayaç --------
    if request.method == "GET" and fmt == "json":
        if not (trip and seat):
            return jsonify(ok=False, msg="trip/seat gerekli"), 400

        r, lf, lb = get_counts(trip, seat)
        total = r + lf + lb

        return jsonify(
            ok=True,
            count=int(total),
            right=int(r),
            left_front=int(lf),
            left_back=int(lb),
            eyes=[x for x, v in {"R": r, "LF": lf, "LB": lb}.items() if v > 0],
        )

    # -------- POST: foto yükleme + adet kaydı --------
    if request.method == "POST":
        _check_csrf()

        if not (trip and seat):
            return redirect("/seats")

        nxt = _normalize_next(request.values.get("next") or request.headers.get("Referer") or "/seats")
        side = _pick_default_side(trip, seat, request.values.get("side"))
        bag_count_in = _clamp_bag_count(request.values.get("bag_count", ""), 1)

        files = [f for f in (request.files.getlist("files") or []) if f and f.filename]
        d.mkdir(parents=True, exist_ok=True)

        # Fotoğraf olmasa bile adet kaydı
        meta = read_meta(trip, seat) or {}
        meta.setdefault("trip", trip)
        meta.setdefault("seat", seat)
        meta.setdefault("counts", {"R": 0, "LF": 0, "LB": 0})
        meta.setdefault("events", [])

        meta["counts"][side] = int(bag_count_in)
        meta["updated_at"] = int(time.time())
        meta["events"].append({
            "t": int(time.time()),
            "type": "set_counts",
            "side": side,
            "count": int(bag_count_in),
            "has_photos": bool(files),
        })
        write_meta(trip, seat, meta)

        # Foto eklemek yeni adet yaratmaz; seçili adet neyse dosya prefix'i odur.
        for f in files:
            ext = (os.path.splitext(f.filename)[1] or ".jpg").lower()
            ts = int(time.time() * 1000)
            name = f"{side}{bag_count_in}_{ts}_{safe(seat) or 'bag'}{ext}"
            img = d / name

            f.save(img)

            try:
                ensure_thumb(img)
            except Exception:
                pass

        return redirect(url_for("bags.gallery", trip=trip, seat=seat, next=nxt))

    # -------- GET: HTML ekran --------
    counts = {"R": 0, "LF": 0, "LB": 0}
    if trip and seat:
        r, lf, lb = get_counts(trip, seat)
        counts = {"R": int(r), "LF": int(lf), "LB": int(lb)}

    if not request.values.get("bag_count") and counts.get(side, 0) > 0:
        bag_count_default = counts.get(side, 1)

    total_count = sum(counts.values())

    photos = []
    if trip and seat and d.exists():
        for p in sorted(d.iterdir(), key=lambda x: x.stat().st_mtime if x.exists() else 0, reverse=True):
            if p.is_file() and _is_image(p):
                ensure_thumb(p)
                side_key = _side_from_filename(p.name)
                photos.append({
                    "fn": p.name,
                    "tn": thumb_path(p).name,
                    "side": side_key,
                    "side_label": _side_label(side_key),
                    "side_icon": _side_icon(side_key),
                })

    sections = []
    for key, label, hint in [
        ("R", "Sağ göz", "Otobüs sağ bagaj gözü"),
        ("LF", "Sol ön", "Sol taraf ön göz"),
        ("LB", "Sol arka", "Sol taraf arka göz"),
    ]:
        sections.append({
            "key": key,
            "label": label,
            "hint": hint,
            "icon": _side_icon(key),
            "count": counts.get(key, 0),
            "photos": [x for x in photos if x["side"] == key],
        })

    display_trip = (trip or "-").replace("_", " ").replace("|", " · Plaka: ")
    csrf_token = _get_csrf()
    gallery_url = url_for("bags.gallery", trip=trip, seat=seat, next=nxt)

    tpl = """
    <!doctype html>
    <html lang="tr">
    <head>
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
      <title>Bagaj Takibi</title>

      <style>
        :root{
          --bg:#070b12;
          --card:#0c1220;
          --card2:#111827;
          --line:rgba(255,255,255,.10);
          --text:#f3f6fb;
          --muted:#9ca8bb;
          --blue:#2563eb;
          --green:#22c55e;
          --red:#dc2626;
          --amber:#f59e0b;
          --shadow:0 18px 42px rgba(0,0,0,.38);
        }

        *{box-sizing:border-box}

        body{
          margin:0;
          background:
            radial-gradient(circle at top left, rgba(37,99,235,.16), transparent 24%),
            radial-gradient(circle at bottom right, rgba(34,197,94,.09), transparent 24%),
            var(--bg);
          color:var(--text);
          font-family:system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;
        }

        .page{
          width:min(980px,100%);
          margin:0 auto;
          padding:14px 14px 28px;
        }

        .hero{
          display:grid;
          grid-template-columns:1fr auto;
          gap:12px;
          align-items:start;
          margin-bottom:14px;
        }

        .title{
          min-width:0;
        }

        .kicker{
          display:inline-flex;
          align-items:center;
          gap:7px;
          padding:7px 11px;
          border-radius:999px;
          background:rgba(255,255,255,.06);
          border:1px solid var(--line);
          color:#dbeafe;
          font-weight:900;
          font-size:12px;
          margin-bottom:10px;
        }

        h1{
          margin:0;
          font-size:30px;
          line-height:1;
          letter-spacing:-.04em;
        }

        .sub{
          margin-top:8px;
          color:var(--muted);
          font-size:14px;
          line-height:1.45;
        }

        .back{
          display:inline-flex;
          align-items:center;
          justify-content:center;
          min-height:52px;
          padding:12px 16px;
          border-radius:18px;
          background:linear-gradient(180deg,#3b82f6,#1d4ed8);
          color:#fff;
          text-decoration:none;
          font-weight:900;
          box-shadow:var(--shadow);
          white-space:nowrap;
        }

        .summary{
          display:grid;
          grid-template-columns:repeat(4,minmax(0,1fr));
          gap:10px;
          margin:14px 0;
        }

        .sum-card{
          min-height:82px;
          border-radius:20px;
          padding:13px;
          background:linear-gradient(180deg,rgba(255,255,255,.055),rgba(255,255,255,.025));
          border:1px solid var(--line);
          box-shadow:0 12px 28px rgba(0,0,0,.22);
        }

        .sum-card .k{
          color:var(--muted);
          font-size:12px;
          font-weight:800;
        }

        .sum-card .v{
          margin-top:7px;
          font-size:27px;
          line-height:1;
          font-weight:950;
        }

        .main{
          display:grid;
          grid-template-columns:minmax(0,1fr) 360px;
          gap:14px;
          align-items:start;
        }

        .panel,
        .gallery-panel{
          border-radius:26px;
          background:linear-gradient(180deg,rgba(255,255,255,.055),rgba(255,255,255,.025));
          border:1px solid var(--line);
          box-shadow:var(--shadow);
          overflow:hidden;
        }

        .panel{
          padding:16px;
          position:sticky;
          top:10px;
        }

        .gallery-panel{
          padding:14px;
        }

        .panel h2,
        .gallery-panel h2{
          margin:0 0 12px;
          font-size:22px;
          line-height:1.1;
          letter-spacing:-.02em;
        }

        .eye-grid{
          display:grid;
          gap:10px;
          margin:12px 0 16px;
        }

        .eye-card{
          width:100%;
          border:1px solid var(--line);
          background:#0b1220;
          color:#fff;
          border-radius:19px;
          padding:13px;
          display:grid;
          grid-template-columns:auto 1fr auto;
          gap:12px;
          align-items:center;
          cursor:pointer;
          text-align:left;
          box-shadow:0 10px 22px rgba(0,0,0,.20);
        }

        .eye-card.active{
          border-color:rgba(96,165,250,.90);
          background:linear-gradient(135deg,rgba(37,99,235,.45),rgba(14,165,233,.18));
          box-shadow:
            0 0 0 2px rgba(96,165,250,.24) inset,
            0 16px 32px rgba(0,0,0,.26);
        }

        .eye-ico{
          width:42px;
          height:42px;
          border-radius:15px;
          display:flex;
          align-items:center;
          justify-content:center;
          background:rgba(255,255,255,.08);
          font-size:20px;
        }

        .eye-name{
          font-weight:950;
          font-size:16px;
        }

        .eye-hint{
          margin-top:3px;
          color:var(--muted);
          font-size:12px;
        }

        .eye-count{
          min-width:46px;
          height:38px;
          border-radius:999px;
          display:flex;
          align-items:center;
          justify-content:center;
          background:rgba(255,255,255,.10);
          font-weight:950;
          font-size:17px;
        }

        .count-box{
          margin:12px 0 14px;
          padding:13px;
          border-radius:20px;
          background:#080f1c;
          border:1px solid var(--line);
        }

        .label{
          color:#dbe6f5;
          font-weight:900;
          font-size:14px;
          margin-bottom:10px;
        }

        .counter{
          display:grid;
          grid-template-columns:58px 1fr 58px;
          gap:10px;
          align-items:center;
        }

        .count-btn{
          height:54px;
          border:none;
          border-radius:17px;
          background:#182235;
          color:#fff;
          font-size:28px;
          font-weight:950;
        }

        .count-view{
          height:54px;
          border-radius:17px;
          display:flex;
          align-items:center;
          justify-content:center;
          background:#020617;
          border:1px solid var(--line);
          font-size:28px;
          font-weight:950;
        }

        .pick-row{
          display:grid;
          grid-template-columns:1fr 1fr;
          gap:10px;
          margin-top:10px;
        }

        .hidden-file{display:none}

        .pick-btn{
          min-height:54px;
          border-radius:18px;
          display:flex;
          align-items:center;
          justify-content:center;
          gap:9px;
          background:#0b1220;
          border:1px solid var(--line);
          color:#fff;
          font-size:16px;
          font-weight:950;
          cursor:pointer;
        }

        .file-hint{
          margin-top:9px;
          color:var(--muted);
          font-size:13px;
        }

        .save{
          width:100%;
          min-height:58px;
          margin-top:14px;
          border:none;
          border-radius:999px;
          background:linear-gradient(180deg,#2dd46d,#16a34a);
          color:#04130a;
          font-weight:950;
          font-size:20px;
          box-shadow:0 16px 34px rgba(34,197,94,.22);
        }

        .note{
          margin:12px 0 0;
          color:var(--muted);
          font-size:13px;
          line-height:1.4;
        }

        .side-section{
          margin-bottom:14px;
          border-radius:22px;
          background:#0b1220;
          border:1px solid var(--line);
          overflow:hidden;
        }

        .side-head{
          display:flex;
          justify-content:space-between;
          align-items:center;
          gap:10px;
          padding:13px;
          border-bottom:1px solid var(--line);
        }

        .side-head b{
          font-size:16px;
        }

        .side-head span{
          color:var(--muted);
          font-size:13px;
          font-weight:800;
        }

        .photo-grid{
          display:grid;
          grid-template-columns:repeat(auto-fill,minmax(150px,1fr));
          gap:10px;
          padding:12px;
        }

        .empty{
          padding:14px;
          color:var(--muted);
          font-size:14px;
        }

        .photo{
          background:#121a2a;
          border:1px solid var(--line);
          border-radius:18px;
          overflow:hidden;
        }

        .photo img{
          display:block;
          width:100%;
          height:145px;
          object-fit:cover;
          background:#020617;
        }

        .photo-meta{
          padding:9px 10px;
          display:flex;
          align-items:center;
          justify-content:space-between;
          gap:8px;
          font-weight:900;
        }

        .small{
          color:var(--muted);
          font-size:12px;
          font-weight:800;
        }

        .del-form{
          padding:0 10px 10px;
        }

        .del-btn{
          width:100%;
          min-height:38px;
          border:none;
          border-radius:999px;
          background:#b91c1c;
          color:#fee2e2;
          font-weight:950;
        }

        .no-trip{
          padding:18px;
          border-radius:22px;
          background:#0b1220;
          border:1px solid var(--line);
          color:var(--muted);
        }

        @media(max-width:760px){
          .page{padding:12px 10px 24px}
          .hero{grid-template-columns:1fr}
          .back{width:100%}
          .summary{
            grid-template-columns:repeat(2,minmax(0,1fr));
          }
          .main{
            grid-template-columns:1fr;
          }
          .panel{
            position:relative;
            top:auto;
            order:-1;
          }
          h1{font-size:28px}
        }
      </style>
    </head>

    <body>
      <div class="page">
        <div class="hero">
          <div class="title">
            <div class="kicker">🧳 Bagaj Operasyon Paneli</div>
            <h1>Koltuk {{ seat or "-" }} Bagaj</h1>
            <div class="sub">
              {{ display_trip }}
            </div>
          </div>

          <a class="back" href="{{ nxt }}">Koltuk ekranına dön</a>
        </div>

        {% if not trip or not seat %}
          <div class="no-trip">
            Önce koltuk ekranından bir koltuk seçip bagaj ekranına gel.
          </div>
        {% else %}

        <div class="summary">
          <div class="sum-card">
            <div class="k">Toplam</div>
            <div class="v">{{ total_count }}</div>
          </div>
          {% for sec in sections %}
            <div class="sum-card">
              <div class="k">{{ sec.icon }} {{ sec.label }}</div>
              <div class="v">{{ sec.count }}</div>
            </div>
          {% endfor %}
        </div>

        <div class="main">
          <div class="gallery-panel">
            <h2>Fotoğraflar</h2>

            {% for sec in sections %}
              <div class="side-section">
                <div class="side-head">
                  <b>{{ sec.icon }} {{ sec.label }}</b>
                  <span>{{ sec.count }} bagaj · {{ sec.photos|length }} foto</span>
                </div>

                {% if sec.photos %}
                  <div class="photo-grid">
                    {% for photo in sec.photos %}
                      <div class="photo">
                        <a href="{{ url_for('bags.raw', trip=trip, seat=seat, filename=photo.fn) }}">
                          <img loading="lazy"
                               src="{{ url_for('bags.thumb', trip=trip, seat=seat, filename=photo.tn) }}">
                        </a>

                        <div class="photo-meta">
                          <b>#{{ loop.index }}</b>
                          <div class="small">{{ photo.side_label }}</div>
                        </div>

                        <form class="del-form" method="post" action="{{ url_for('bags.delete_one') }}">
                          <input type="hidden" name="csrf_token" value="{{ csrf_token }}">
                          <input type="hidden" name="trip" value="{{ trip }}">
                          <input type="hidden" name="seat" value="{{ seat }}">
                          <input type="hidden" name="filename" value="{{ photo.fn }}">
                          <input type="hidden" name="next" value="{{ nxt }}">
                          <button type="submit" class="del-btn"
                                  onclick="return confirm('Bu fotoğraf silinsin mi?')">
                            🗑 Fotoğrafı sil
                          </button>
                        </form>
                      </div>
                    {% endfor %}
                  </div>
                {% else %}
                  <div class="empty">Bu göz için fotoğraf yok.</div>
                {% endif %}
              </div>
            {% endfor %}
          </div>

          <div class="panel">
            <h2>Yeni kayıt</h2>

            <form method="post" action="{{ gallery_url }}" enctype="multipart/form-data">
              <input type="hidden" name="csrf_token" value="{{ csrf_token }}">
              <input type="hidden" name="trip" value="{{ trip }}">
              <input type="hidden" name="seat" value="{{ seat }}">
              <input type="hidden" name="next" value="{{ nxt }}">
              <input type="hidden" name="side" id="sideInput" value="{{ side }}">
              <input type="hidden" name="bag_count" id="countInput" value="{{ bag_count }}">

              <div class="label">Bagaj gözü</div>

              <div class="eye-grid">
                {% for sec in sections %}
                  <button type="button"
                          class="eye-card {{ 'active' if sec.key == side else '' }}"
                          data-side="{{ sec.key }}"
                          data-count="{{ sec.count }}">
                    <div class="eye-ico">{{ sec.icon }}</div>
                    <div>
                      <div class="eye-name">{{ sec.label }}</div>
                      <div class="eye-hint">{{ sec.hint }}</div>
                    </div>
                    <div class="eye-count">{{ sec.count }}</div>
                  </button>
                {% endfor %}
              </div>

              <div class="count-box">
                <div class="label">Bagaj adedi</div>
                <div class="counter">
                  <button type="button" class="count-btn" id="decCount">−</button>
                  <div class="count-view" id="countView">{{ bag_count }}</div>
                  <button type="button" class="count-btn" id="incCount">+</button>
                </div>
              </div>

              <div class="label">Fotoğraf ekle</div>

              <input id="camFiles" class="hidden-file"
                     name="files" type="file" accept="image/*"
                     capture="environment" multiple>

              <input id="galFiles" class="hidden-file"
                     name="files" type="file" accept="image/*" multiple>

              <div class="pick-row">
                <label class="pick-btn" for="camFiles">📷 Kamera</label>
                <label class="pick-btn" for="galFiles">🖼️ Galeri</label>
              </div>

              <div class="file-hint" id="selectedFiles">Fotoğraf seçilmedi</div>

              <button type="submit" class="save">Kaydet</button>

              <p class="note">
                Fotoğraf seçmesen bile seçili göz ve bagaj adedi kaydedilir.
              </p>
            </form>
          </div>
        </div>

        {% endif %}
      </div>

      <script>
        const counts = {{ counts|tojson }};
        const sideInput = document.getElementById("sideInput");
        const countInput = document.getElementById("countInput");
        const countView = document.getElementById("countView");
        const selectedFiles = document.getElementById("selectedFiles");

        function setCount(v){
          let n = Number(v || 1);
          if(!Number.isFinite(n)) n = 1;
          n = Math.max(1, Math.min(10, Math.round(n)));
          if(countInput) countInput.value = String(n);
          if(countView) countView.textContent = String(n);
        }

        document.querySelectorAll(".eye-card").forEach(btn => {
          btn.addEventListener("click", () => {
            document.querySelectorAll(".eye-card").forEach(x => x.classList.remove("active"));
            btn.classList.add("active");

            const side = btn.dataset.side || "R";
            const existing = Number(btn.dataset.count || 0);

            if(sideInput) sideInput.value = side;
            setCount(existing > 0 ? existing : 1);
          });
        });

        document.getElementById("decCount")?.addEventListener("click", () => {
          setCount(Number(countInput?.value || 1) - 1);
        });

        document.getElementById("incCount")?.addEventListener("click", () => {
          setCount(Number(countInput?.value || 1) + 1);
        });

        function syncFileText(input){
          const n = input?.files?.length || 0;
          selectedFiles.textContent = n ? `${n} fotoğraf seçildi` : "Fotoğraf seçilmedi";
        }

        document.getElementById("camFiles")?.addEventListener("change", e => syncFileText(e.target));
        document.getElementById("galFiles")?.addEventListener("change", e => syncFileText(e.target));
      </script>
    </body>
    </html>
    """

    return render_template_string(
        tpl,
        trip=trip,
        seat=seat,
        display_trip=display_trip,
        counts=counts,
        total_count=total_count,
        sections=sections,
        photos=photos,
        nxt=nxt,
        csrf_token=csrf_token,
        gallery_url=gallery_url,
        side=side,
        bag_count=bag_count_default,
    )


# =========================
#      /bags/clear
# =========================
@bp.route("/clear", methods=["DELETE"])
def clear_bags():
    _check_csrf()

    trip = request.args.get("trip", "") or request.args.get("trip_code", "")
    seat = request.args.get("seat", "")
    if not trip or not seat:
        return jsonify(ok=False, msg="trip/seat gerekli"), 400

    d = seat_dir(trip, seat)
    removed = 0

    if d.exists():
        for p in d.iterdir():
            try:
                if p.is_file():
                    p.unlink()
                    removed += 1
            except Exception:
                pass
        try:
            d.rmdir()
        except OSError:
            pass

    return jsonify(ok=True, removed=removed)


# =========================
#    /bags/delete-one
# =========================
@bp.route("/delete-one", methods=["POST"])
def delete_one():
    _check_csrf()

    trip = request.form.get("trip", "")
    seat = request.form.get("seat", "")
    filename = request.form.get("filename", "")
    nxt = _normalize_next(request.form.get("next") or request.headers.get("Referer") or "/seats")

    if not (trip and seat and filename):
        return redirect(nxt)

    d = seat_dir(trip, seat)
    p = d / filename

    try:
        if p.exists():
            p.unlink()
    except Exception:
        pass

    try:
        t = thumb_path(p)
        if t.exists():
            t.unlink()
    except Exception:
        pass

    return redirect(url_for("bags.gallery", trip=trip, seat=seat, next=nxt))


# =========================
#     /bags/capture  (ESKİ)
# =========================
@bp.route("/capture", methods=["GET", "POST"])
def capture():
    """Eski tam ekran bagaj yükleme sayfası (ihtiyaç olursa dursun)."""

    if request.method == "POST":
        _check_csrf()

        trip = request.form.get("trip_code", "") or request.form.get("trip", "")
        seat = request.form.get("seat", "")
        to = request.form.get("to_stop", "")
        nxt = _normalize_next(request.form.get("next") or request.headers.get("Referer"))

        side = _pick_default_side(trip, seat, request.form.get("side"))

        bag_raw = request.form.get("bag_count") or "1"
        try:
            bag_count = int(bag_raw)
        except ValueError:
            bag_count = 1
        bag_count = max(1, min(bag_count, 10))

        files = request.files.getlist("files") or []
        d = seat_dir(trip, seat)
        d.mkdir(parents=True, exist_ok=True)

        # ✅ meta kaydı (foto olmasa bile)
        meta = read_meta(trip, seat) or {}
        meta.setdefault("trip", trip)
        meta.setdefault("seat", seat)
        meta.setdefault("counts", {"R": 0, "LF": 0, "LB": 0})
        meta.setdefault("events", [])
        meta["counts"][side] = int(bag_count)
        meta["updated_at"] = int(time.time())
        meta["events"].append(
            {
                "t": int(time.time()),
                "type": "set_counts",
                "side": side,
                "count": int(bag_count),
                "has_photos": bool(files),
            }
        )
        write_meta(trip, seat, meta)

        # Foto isim prefix'i sabit: bag_count
        saved = 0
        for f in files:
            if not f or not f.filename:
                continue

            ext = (os.path.splitext(f.filename)[1] or ".jpg").lower()
            ts = int(time.time() * 1000)
            name = f"{side}{bag_count}_{ts}_{safe(to) or 'bag'}{ext}"

            p = d / name
            f.save(p)
            try:
                ensure_thumb(p)
            except Exception:
                pass
            saved += 1

        return render_template_string(
            """
            <!doctype html>
            <meta name=viewport content="width=device-width,initial-scale=1">
            <meta http-equiv="refresh" content="1.2;url={{ nxt }}">
            <body style="background:#020617;color:#e5e7eb;
                         font-family:system-ui,sans-serif;
                         display:flex;flex-direction:column;
                         align-items:center;justify-content:center;
                         gap:10px;height:100vh;margin:0">
              <h2 style="margin:0;font-size:22px">✅ {{ n }} fotoğraf kaydedildi</h2>
              <p style="margin:0 16px 6px;text-align:center;opacity:.85">
                Sefer: <b>{{ trip or '-' }}</b> • Koltuk: <b>{{ seat or '-' }}</b>
              </p>
              <div style="display:flex;gap:8px;">
                <a href="{{ nxt }}"
                   style="padding:8px 14px;border-radius:999px;
                          background:#22c55e;color:#022c22;
                          text-decoration:none;font-weight:700;">
                  ◀ Koltuk ekranına dön
                </a>
                <a href="{{ url_for('bags.capture', trip_code=trip, seat=seat, to_stop=to, next=nxt) }}"
                   style="padding:8px 14px;border-radius:999px;
                          background:#1f2937;color:#e5e7eb;
                          text-decoration:none;font-weight:600;">
                  Yeni fotoğraf ekle
                </a>
              </div>
            </body>
            """,
            n=saved,
            trip=trip,
            seat=seat,
            to=to,
            nxt=nxt,
        )

    trip = request.args.get("trip_code", "") or request.args.get("trip", "")
    seat = request.args.get("seat", "")
    to = request.args.get("to_stop", "")
    nxt = _back_url()

    side = _pick_default_side(trip, seat, request.args.get("side"))

    bag_options = list(range(1, 11))

    return render_template_string(
        """
        <!doctype html>
        <html lang="tr">
        <head>
          <meta name="viewport" content="width=device-width,initial-scale=1">
          <title>Bagaj Yükle</title>
          <style>
            body{ margin:0; font-family:system-ui,sans-serif; background:#020617; color:#e5e7eb; }
            .page{ max-width:480px; margin:0 auto; padding:16px 16px 32px; }
            h1{ font-size:24px; margin:0 0 16px; display:flex; align-items:center; gap:8px; }
            .card{
              background:#020617; border-radius:16px; padding:16px 14px 20px;
              box-shadow:0 18px 45px rgba(0,0,0,0.55); border:1px solid #0f172a;
            }
            .row{ margin-bottom:12px; }
            label{ font-size:13px; opacity:.8; display:block; margin-bottom:4px; }
            select,input[type="text"]{
              width:100%; padding:8px 10px; border-radius:12px;
              border:1px solid #1f2933; background:#020617; color:#e5e7eb; font-size:15px;
            }
            .pick-row{display:flex; gap:10px; margin-top:10px;}
            .pick-btn{
              flex:1; text-align:center; padding:10px 12px;
              border-radius:999px; border:1px solid #1f2933;
              background:#0b1220; color:#e5e7eb;
              font-weight:800; font-size:14px; cursor:pointer; user-select:none;
            }
            .hidden-file{display:none}
            .btn-main{
              width:100%; padding:12px 14px; border-radius:999px; border:none;
              background:#22c55e; color:#022c22; font-weight:900; font-size:16px;
              margin-top:12px;
            }
            .back{
              margin-top:14px; display:inline-flex; align-items:center; gap:6px;
              color:#93c5fd; text-decoration:none; font-size:14px;
            }
          </style>
        </head>
        <body>
          <div class="page">
            <h1>🧳 Bagaj Yükle</h1>
            <div class="card">
              <form method="post" enctype="multipart/form-data">
                <input type="hidden" name="csrf_token" value="{{ csrf_token }}">
                <input type="hidden" name="trip_code"  value="{{ trip }}">
                <input type="hidden" name="seat"       value="{{ seat }}">
                <input type="hidden" name="to_stop"    value="{{ to }}">
                <input type="hidden" name="next"       value="{{ nxt }}">

                <div class="row" style="font-size:14px;margin-bottom:14px;">
                  Sefer: <strong>{{ trip or '-' }}</strong>
                  &nbsp; • &nbsp;
                  Koltuk: <strong>{{ seat or '-' }}</strong>
                </div>

                <div class="row">
                  <label for="side">Göz:</label>
                  <select name="side" id="side">
                    <option value="R"  {{ "selected" if side=="R"  else "" }}>Sağ göz</option>
                    <option value="LF" {{ "selected" if side=="LF" else "" }}>Sol ön</option>
                    <option value="LB" {{ "selected" if side=="LB" else "" }}>Sol arka</option>
                  </select>
                </div>

                <div class="row">
                  <label for="bag_count">Bagaj adedi:</label>
                  <select name="bag_count" id="bag_count">
                    <option value="" selected>- - -</option>
                    {% for i in bag_options %}
                      <option value="{{ i }}">{{ i }}</option>
                    {% endfor %}
                  </select>
                </div>

                <!-- Kamera/Galeri ayrı -->
                <input id="camFiles" class="hidden-file"
                       name="files" type="file" accept="image/*"
                       capture="environment" multiple>

                <input id="galFiles" class="hidden-file"
                       name="files" type="file" accept="image/*" multiple>

                <div class="row">
                  <label>Fotoğraf:</label>
                  <div class="pick-row">
                    <label class="pick-btn" for="camFiles">📷 Kamera</label>
                    <label class="pick-btn" for="galFiles">🖼️ Galeri</label>
                  </div>
                </div>

                <button class="btn-main" type="submit">Kaydet</button>
                <p style="margin:10px 0 0;opacity:.8;font-size:13px">
                  Not: Fotoğraf seçmesen bile bagaj adedi kaydedilir.
                </p>
              </form>
            </div>

            <a class="back" href="{{ nxt }}">◀ Koltuk ekranına dön</a>
          </div>
        </body>
        </html>
        """,
        trip=trip,
        seat=seat,
        to=to,
        nxt=nxt,
        side=side,
        bag_options=bag_options,
        csrf_token=_get_csrf(),
    )


# ----------- Ham ve Thumb servisleri -----------
@bp.route("/raw/<trip>/<seat>/<path:filename>")
def raw(trip: str, seat: str, filename: str):
    return send_from_directory(seat_dir(trip, seat), filename, as_attachment=False)


@bp.route("/thumb/<trip>/<seat>/<path:filename>")
def thumb(trip: str, seat: str, filename: str):
    return send_from_directory(seat_dir(trip, seat), filename, as_attachment=False)
