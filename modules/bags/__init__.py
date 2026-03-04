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
@bp.route("", methods=["GET", "POST"])
def gallery():
    """
    - GET: galeri sayfası
    - POST: aynı sayfadan fotoğraf yükleme (foto olmasa bile adet kaydı)
    - ?format=json: sağ / sol ön / sol arka sayaç
    """

    trip = request.values.get("trip", "") or request.values.get("trip_code", "")
    seat = request.values.get("seat", "")
    fmt = (request.args.get("format", "") or "").lower()

    # koltuktan gelen default adet
    bag_raw = request.values.get("bag_count", "") or "1"
    try:
        bag_count_default = int(bag_raw)
    except ValueError:
        bag_count_default = 1
    bag_count_default = max(1, min(bag_count_default, 10))

    # side (gelmezse tahmin)
    side = _pick_default_side(trip, seat, request.values.get("side"))

    d = seat_dir(trip, seat)

    # -------- JSON sayaç --------
    if request.method == "GET" and fmt == "json":
        if not (trip and seat):
            return jsonify(ok=False, msg="trip/seat gerekli"), 400
        r, lf, lb = get_counts(trip, seat)
        total = r + lf + lb
        return jsonify(ok=True, count=int(total), right=int(r), left_front=int(lf), left_back=int(lb))

    # -------- POST: foto yükleme + adet kaydı --------
    if request.method == "POST":
        _check_csrf()

        if not (trip and seat):
            return redirect("/seats")

        # side: formdan gelebilir, gelmezse tahmin
        side = _pick_default_side(trip, seat, request.values.get("side"))

        # formdan gelen bag_count (adet)
        bag_raw2 = request.values.get("bag_count", "") or "1"
        try:
            bag_count_in = int(bag_raw2)
        except ValueError:
            bag_count_in = 1
        bag_count_in = max(1, min(bag_count_in, 10))

        files = request.files.getlist("files") or []
        d.mkdir(parents=True, exist_ok=True)

        # ✅ FOTO YOKSA BİLE ADEDİ KAYDET (meta.json)
        meta = read_meta(trip, seat) or {}
        meta.setdefault("trip", trip)
        meta.setdefault("seat", seat)
        meta.setdefault("counts", {"R": 0, "LF": 0, "LB": 0})
        meta.setdefault("events", [])

        meta["counts"][side] = int(bag_count_in)
        meta["updated_at"] = int(time.time())
        meta["events"].append(
            {
                "t": int(time.time()),
                "type": "set_counts",
                "side": side,
                "count": int(bag_count_in),
                "has_photos": bool(files),
            }
        )
        write_meta(trip, seat, meta)

        # ✅ Foto isim prefix’i: "ok gibi artmasın"
        # Foto eklemek "yeni adet" yaratmaz -> her zaman meta'daki sayı ile kaydet.
        bag_count_for_files = int(bag_count_in)

        for f in files:
            if not f or not f.filename:
                continue

            ext = (os.path.splitext(f.filename)[1] or ".jpg").lower()
            ts = int(time.time() * 1000)

            name = f"{side}{bag_count_for_files}_{ts}_{safe(seat) or 'bag'}{ext}"
            p = d / name
            f.save(p)
            try:
                ensure_thumb(p)
            except Exception:
                pass

        return redirect(url_for("bags.gallery", trip=trip, seat=seat))

    # -------- GET: HTML galeri --------
    nxt = "/seats"
    imgs: list[tuple[str, str]] = []

    if trip and seat and d.exists():
        for p in sorted(d.iterdir()):
            if p.is_file() and _is_image(p):
                ensure_thumb(p)
                imgs.append((p.name, thumb_path(p).name))

    csrf_token = _get_csrf()
    gallery_url = url_for("bags.gallery", trip=trip, seat=seat)

    tpl = """
    <meta name=viewport content="width=device-width, initial-scale=1, viewport-fit=cover">
    <style>
      body{
        background:#101417;
        color:#eef;
        font-family:system-ui,-apple-system,Segoe UI,Roboto,Arial,sans-serif;
        margin:0;
      }
      .wrap{max-width:960px;margin:auto;padding:10px}

      .bar{
        display:flex;
        gap:8px;
        align-items:center;
        margin:8px 0 14px;
        justify-content:space-between;
      }
      .muted{opacity:.8;font-size:13px}
      a.btn{
        background:#2563eb;
        color:#fff;
        text-decoration:none;
        padding:8px 12px;
        border-radius:10px;
        display:inline-block;
        font-size:14px;
      }

      .main-row{
        display:flex;
        gap:16px;
        align-items:flex-start;
        flex-wrap:wrap;
      }
      .gallery-col{ flex:1 1 220px; }
      .form-col{ flex:0 0 280px; max-width:280px; }

      .top-card{
        background:#020617;
        border-radius:18px;
        padding:14px 14px 18px;
        border:1px solid #111827;
      }
      .top-card h2{
        margin:0 0 10px;
        font-size:16px;
      }

      label{font-size:13px;opacity:.9;display:block;margin-bottom:4px}
      select{
        width:100%;
        padding:8px 10px;
        border-radius:12px;
        border:1px solid #1f2933;
        background:#020617;
        color:#e5e7eb;
        font-size:14px;
      }

      /* Kamera / Galeri */
      .pick-row{display:flex; gap:10px; margin-top:10px;}
      .pick-btn{
        flex:1;
        text-align:center;
        padding:10px 12px;
        border-radius:999px;
        border:1px solid #1f2933;
        background:#0b1220;
        color:#e5e7eb;
        font-weight:700;
        font-size:14px;
        cursor:pointer;
        user-select:none;
      }
      .pick-btn:active{transform:scale(.98)}
      .hidden-file{display:none}

      .btn-main{
        width:100%;
        margin-top:12px;
        padding:10px 14px;
        border-radius:999px;
        border:none;
        background:#22c55e;
        color:#022c22;
        font-weight:900;
        font-size:15px;
      }

      .grid{
        display:grid;
        grid-template-columns:repeat(auto-fill,minmax(160px,1fr));
        gap:10px;
      }
      .card{
        background:#1b2126;
        border:1px solid #30363d;
        border-radius:14px;
        overflow:hidden;
        display:flex;
        flex-direction:column;
      }
      .t{text-align:center;padding:6px 6px 4px;font-weight:700;font-size:13px}
      img{
        display:block;
        width:100%;
        height:160px;
        object-fit:cover;
        background:#0b0e10;
      }
      .del-form{margin:4px 6px 10px;}
      .del-btn{
        width:100%;
        padding:6px 8px;
        border-radius:999px;
        border:none;
        font-size:12px;
        background:#b91c1c;
        color:#fee2e2;
        font-weight:800;
      }

      @media (max-width: 720px){
        .main-row{flex-direction:column;}
        .form-col{flex:1 1 auto;max-width:none;}
      }
    </style>

    <div class="wrap">
      <div class="bar">
        <div class="muted">
          Sefer: <b>{{trip or "-"}}</b> • Koltuk: <b>{{seat or "-"}}</b>
        </div>
        <a class="btn" href="{{ nxt }}">Koltuk ekranına dön</a>
      </div>

      {% if not trip or not seat %}
        <p class="muted">Önce koltuk ekranından bir koltuk seçip bagaj ekranına gel.</p>
      {% else %}

      <div class="main-row">

        <div class="gallery-col">
          {% if not imgs %}
            <p class="muted">Bu koltuk için kayıtlı bagaj fotoğrafı yok.</p>
          {% else %}
            <div class="grid">
              {% for fn,tn in imgs %}
                <div class="card">
                  <a href="{{ url_for('bags.raw', trip=trip, seat=seat, filename=fn) }}">
                    <img loading="lazy"
                         src="{{ url_for('bags.thumb', trip=trip, seat=seat, filename=tn) }}">
                  </a>
                  <div class="t">#{{ loop.index }}</div>
                  <form class="del-form" method="post" action="{{ url_for('bags.delete_one') }}">
                    <input type="hidden" name="csrf_token" value="{{ csrf_token }}">
                    <input type="hidden" name="trip" value="{{ trip }}">
                    <input type="hidden" name="seat" value="{{ seat }}">
                    <input type="hidden" name="filename" value="{{ fn }}">
                    <button type="submit" class="del-btn">🗑 Fotoğrafı sil</button>
                  </form>
                </div>
              {% endfor %}
            </div>
          {% endif %}
        </div>

        <div class="form-col">
          <div class="top-card">
            <h2>Yeni fotoğraf ekle</h2>

            <form method="post" action="{{ gallery_url }}" enctype="multipart/form-data">
              <input type="hidden" name="csrf_token" value="{{ csrf_token }}">
              <input type="hidden" name="trip"  value="{{ trip }}">
              <input type="hidden" name="seat"  value="{{ seat }}">

              <label>Göz:</label>
              <select name="side">
                <option value="R"  {{ "selected" if side=="R"  else "" }}>Sağ göz</option>
                <option value="LF" {{ "selected" if side=="LF" else "" }}>Sol ön</option>
                <option value="LB" {{ "selected" if side=="LB" else "" }}>Sol arka</option>
              </select>

              <label style="margin-top:10px;">Bagaj adedi:</label>
              <select name="bag_count">
                {% for i in range(1, 11) %}
                  <option value="{{ i }}" {{ "selected" if bag_count==i else "" }}>{{ i }}</option>
                {% endfor %}
              </select>

              <!-- Kamera / Galeri iki ayrı input -->
              <input id="camFiles" class="hidden-file"
                     name="files" type="file" accept="image/*"
                     capture="environment" multiple>

              <input id="galFiles" class="hidden-file"
                     name="files" type="file" accept="image/*"
                     multiple>

              <div class="pick-row">
                <label class="pick-btn" for="camFiles">📷 Kamera</label>
                <label class="pick-btn" for="galFiles">🖼️ Galeri</label>
              </div>

              <button type="submit" class="btn-main">Kaydet</button>

              <p class="muted" style="margin:10px 0 0;">
                Not: Fotoğraf seçmesen bile bagaj adedi kaydedilir.
              </p>
            </form>
          </div>
        </div>

      </div>
      {% endif %}
    </div>
    """

    return render_template_string(
        tpl,
        trip=trip,
        seat=seat,
        imgs=imgs,
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

    if not (trip and seat and filename):
        return redirect(_back_url())

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

    return redirect(url_for("bags.gallery", trip=trip, seat=seat))


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
