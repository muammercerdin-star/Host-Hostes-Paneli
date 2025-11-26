from __future__ import annotations

import os
import time
import secrets
from pathlib import Path
from urllib.parse import urlparse

from flask import (
    Blueprint,
    request,
    render_template_string,
    jsonify,
    send_from_directory,
    current_app,
    abort,
    session,
    redirect,
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
    token = request.form.get("csrf_token", "") or request.headers.get(
        "X-CSRF-Token", ""
    )
    if token != session.get("csrf_token"):
        abort(403, description="CSRF doğrulaması başarısız")


# ------------- Yardımcılar -----------
def _normalize_next(url: str | None) -> str:
    """Tam URL gelse bile sadece path'i al; .html uzantısını at; / ile başlat."""
    path = urlparse(url or "").path
    if not path:
        return "/seats"
    if path.endswith(".html"):
        path = path[:-5]
    if not path.startswith("/"):
        path = "/" + path
    return path or "/seats"


def _back_url() -> str:
    # Önce açıkça verilen next, yoksa Referer, en son /seats
    return _normalize_next(
        request.values.get("next") or request.headers.get("Referer") or "/seats"
    )


# ------------- Depo yolları ----------
def bag_root() -> Path:
    # proje kökünde storage/bags
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
    """Orijinal görsel mi? (thumb değil)"""
    return (
        p.suffix.lower() in {".jpg", ".jpeg", ".png", ".webp"}
        and ".thumb." not in p.name.lower()
    )


def ensure_thumb(img_path: Path):
    # Zaten thumbnail dosyasıysa dokunma
    name = img_path.name.lower()
    if ".thumb." in name:
        return
    t = thumb_path(img_path)
    if t.exists():
        return
    try:
        with Image.open(img_path) as im:
            im.thumbnail((480, 480))
            im.convert("RGB").save(t, "JPEG", quality=82, optimize=True)
    except Exception:
        # thumb üretilemese de akışı bozma
        pass


# ------------- Görüntüleme -----------
@bp.route("")
def gallery():
    """
    HTML galeri veya ?format=json ile sayaç döndürür.
    """

    trip = request.args.get("trip", "") or request.args.get("trip_code", "")
    seat = request.args.get("seat", "")
    fmt  = request.args.get("format", "").lower()
    nxt  = _back_url()

    d = seat_dir(trip, seat)

    # ---- JSON sayaç: toplam + sağ / sol ön / sol arka bagaj adedi ----
    if fmt == "json":
        right = left_front = left_back = 0  # her göz için MAX değer

        if d.exists():
            for p in d.iterdir():
                if not (p.is_file() and _is_image(p)):
                    continue

                name = p.name
                # Varsayılanlar (eski dosyalar için)
                side_key = "R"   # sağ göz
                bag_count = 1    # sayı yoksa 1 kabul

                # Yeni isim formatı: R3_..., LF2_..., LB10_...
                if "_" in name:
                    prefix  = name.split("_", 1)[0]  # "R3", "LF2", "LB10"...
                    letters = "".join(ch for ch in prefix if ch.isalpha()).upper()
                    digits  = "".join(ch for ch in prefix if ch.isdigit())

                    if digits:
                        try:
                            bag_count = max(1, int(digits))
                        except ValueError:
                            bag_count = 1

                    if letters in ("R", "LF", "LB"):
                        side_key = letters

                # Her göz için MAX sayıyı tut
                if side_key == "R":
                    right = max(right, bag_count)
                elif side_key == "LF":
                    left_front = max(left_front, bag_count)
                elif side_key == "LB":
                    left_back = max(left_back, bag_count)
                else:
                    right = max(right, bag_count)

        total = right + left_front + left_back
        return jsonify(
            ok=True,
            count=int(total),
            right=int(right),
            left_front=int(left_front),
            left_back=int(left_back),
        )

    # ---- HTML galeri ----
    imgs: list[tuple[str, str]] = []
    if d.exists():
        for p in sorted(d.iterdir()):
            if p.is_file() and _is_image(p):
                ensure_thumb(p)
                imgs.append((p.name, thumb_path(p).name))

    csrf_token   = _get_csrf()
    bag_options  = list(range(1, 11))  # 1–10
    upload_action = url_for("bags.capture")
    gallery_url   = url_for("bags.gallery", trip=trip, seat=seat)

    tpl = """
    <meta name=viewport content="width=device-width, initial-scale=1, viewport-fit=cover">
    <style>
      body{
        background:#101417;
        color:#eef;
        font-family:system-ui,-apple-system,Segoe UI,Roboto,Arial,sans-serif;
        margin:0;
      }
      .wrap{max-width:940px;margin:auto;padding:10px}
      .top-card{
        background:#020617;
        border-radius:18px;
        padding:12px 14px 14px;
        border:1px solid #111827;
        margin-bottom:16px;
      }
      .top-row{
        display:flex;
        flex-wrap:wrap;
        gap:8px 10px;
        align-items:flex-end;
      }
      label{font-size:13px;opacity:.9;display:block;margin-bottom:2px;}
      select,input[type="file"]{
        padding:6px 8px;
        border-radius:10px;
        border:1px solid #1f2933;
        background:#020617;
        color:#e5e7eb;
        font-size:13px;
      }
      .btn-main{
        padding:9px 14px;
        border-radius:999px;
        border:none;
        background:#22c55e;
        color:#022c22;
        font-weight:700;
        font-size:14px;
      }
      .bar{display:flex;gap:8px;align-items:center;margin:8px 0 14px;justify-content:space-between}
      a.btn{
        background:#2563eb;
        color:#fff;
        text-decoration:none;
        padding:8px 12px;
        border-radius:10px;
        display:inline-block;
        font-size:14px;
      }
      .muted{opacity:.8;font-size:13px}
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
        padding:5px 8px;
        border-radius:999px;
        border:none;
        font-size:12px;
        background:#b91c1c;
        color:#fee2e2;
        font-weight:600;
      }
    </style>
    <div class="wrap">

      <div class="bar">
        <div class="muted">
          Sefer: <b>{{trip}}</b> • Koltuk: <b>{{seat}}</b>
        </div>
        <a class="btn" href="{{ nxt }}">Koltuk ekranına dön</a>
      </div>

      <!-- Üstte hızlı fotoğraf ekleme formu -->
      <div class="top-card">
        <form method="post"
              action="{{ upload_action }}"
              enctype="multipart/form-data">
          <input type="hidden" name="csrf_token" value="{{ csrf_token }}">
          <input type="hidden" name="trip_code"  value="{{ trip }}">
          <input type="hidden" name="seat"       value="{{ seat }}">
          <input type="hidden" name="to_stop"    value="">
          <!-- Başarılı olunca tekrar galeriye dön -->
          <input type="hidden" name="next"       value="{{ gallery_url }}">

          <div class="top-row">
            <div>
              <label for="side">Göz</label>
              <select name="side" id="side">
                <option value="R">Sağ göz</option>
                <option value="LF">Sol ön</option>
                <option value="LB">Sol arka</option>
              </select>
            </div>

            <div>
              <label for="bag_count">Bagaj adedi</label>
              <select name="bag_count" id="bag_count">
                <option value="">- - -</option>
                {% for i in bag_options %}
                  <option value="{{ i }}">{{ i }}</option>
                {% endfor %}
              </select>
            </div>

            <div style="flex:1;min-width:140px;">
              <label for="files">Fotoğraf(lar)</label>
              <input id="files" name="files"
                     type="file"
                     accept="image/*"
                     capture="environment"
                     multiple>
            </div>

            <div>
              <button type="submit" class="btn-main">
                Fotoğraf ekle
              </button>
            </div>
          </div>
        </form>
      </div>

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
    """

    return render_template_string(
        tpl,
        trip=trip,
        seat=seat,
        imgs=imgs,
        nxt=nxt,
        csrf_token=csrf_token,
        bag_options=bag_options,
        upload_action=upload_action,
        gallery_url=gallery_url,
    )

@bp.route("/clear", methods=["DELETE"])
def clear_bags():
    """
    Belirli bir trip + koltuk için TÜM bagaj dosyalarını sil.
    İniş (boşalt) sırasında çağrılacak.
    """
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
                # Tek dosya silinmese bile devam et
                pass
        # Klasör boş kaldıysa temizlemeye çalış
        try:
            d.rmdir()
        except OSError:
            pass

    return jsonify(ok=True, removed=removed)


@bp.route("/delete-one", methods=["POST"])
def delete_one():
    """Tek bir fotoğrafı (ve thumbnail'ini) sil."""
    _check_csrf()

    trip = request.form.get("trip", "")
    seat = request.form.get("seat", "")
    filename = request.form.get("filename", "")

    if not (trip and seat and filename):
        return redirect(_back_url())

    d = seat_dir(trip, seat)
    p = d / filename

    # Orijinal dosya
    try:
        if p.exists():
            p.unlink()
    except Exception:
        pass

    # Thumb
    try:
        t = thumb_path(p)
        if t.exists():
            t.unlink()
    except Exception:
        pass

    # Aynı koltuğun galeri ekranına dön
    return redirect(url_for("bags.gallery", trip=trip, seat=seat))


# ------------- Yükleme ---------------
@bp.route("/capture", methods=["GET", "POST"])
def capture():
    """Bagaj fotoğrafı yükleme formu (kamera/galeri)."""

    # === POST: fotoğraf(lar)ı kaydet ===
    if request.method == "POST":
        _check_csrf()  # ✅ CSRF

        trip = request.form.get("trip_code", "")
        seat = request.form.get("seat", "")
        to = request.form.get("to_stop", "")
        nxt = _normalize_next(
            request.form.get("next") or request.headers.get("Referer")
        )

        # Bagaj gözü: R (sağ), LF (sol ön), LB (sol arka)
        side = (request.form.get("side", "R") or "R").upper()
        if side not in ("R", "LF", "LB"):
            side = "R"

        # 🔢 Bagaj adedi (1–10) – foto sayısından bağımsız
        bag_raw = request.form.get("bag_count") or "1"
        try:
            bag_count = int(bag_raw)
        except ValueError:
            bag_count = 1
        bag_count = max(1, min(bag_count, 10))

        files = request.files.getlist("files") or []
        d = seat_dir(trip, seat)
        d.mkdir(parents=True, exist_ok=True)

        saved = 0
        for f in files:
            if not f or not f.filename:
                continue

            ext = (os.path.splitext(f.filename)[1] or ".jpg").lower()
            ts = int(time.time() * 1000)

            # 🔑 Dosya adı: R3_..., LF2_..., LB10_...
            # Sayaç JSON tarafında bu sayıların MAX'ını kullanıyor.
            name = f"{side}{bag_count}_{ts}_{safe(to) or 'bag'}{ext}"

            p = d / name
            f.save(p)
            try:
                ensure_thumb(p)
            except Exception:
                pass
            saved += 1

        # Başarı ekranı + hızlı geri dönüş
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
              <h2 style="margin:0;font-size:22px">
                ✅ {{ n }} fotoğraf kaydedildi
              </h2>
              <p style="margin:0 16px 6px;text-align:center;opacity:.85">
                Sefer: <b>{{ trip or '-' }}</b> •
                Koltuk: <b>{{ seat or '-' }}</b>
              </p>
              <div style="display:flex;gap:8px;">
                <a href="{{ nxt }}"
                   style="padding:8px 14px;border-radius:999px;
                          background:#22c55e;color:#022c22;
                          text-decoration:none;font-weight:700;">
                  ◀ Koltuk ekranına dön
                </a>
                <a href="{{ url_for('bags.capture',
                                    trip_code=trip,
                                    seat=seat,
                                    to_stop=to,
                                    next=nxt) }}"
                   style="padding:8px 14px;border-radius:999px;
                          background:#1f2937;color:#e5e7eb;
                          text-decoration:none;font-weight:500;">
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

    # === GET: tam ekran formu göster ===
    trip = request.args.get("trip_code", "") or request.args.get("trip", "")
    seat = request.args.get("seat", "")
    to = request.args.get("to_stop", "")
    nxt = _back_url()

    side = (request.args.get("side", "R") or "R").upper()
    if side not in ("R", "LF", "LB"):
        side = "R"

    bag_options = list(range(1, 11))  # 1–10

    return render_template_string(
        """
        <!doctype html>
        <html lang="tr">
        <head>
          <meta name="viewport" content="width=device-width,initial-scale=1">
          <title>Bagaj Yükle</title>
          <style>
            body{
              margin:0;
              font-family:system-ui,sans-serif;
              background:#020617;
              color:#e5e7eb;
            }
            .page{
              max-width:480px;
              margin:0 auto;
              padding:16px 16px 32px;
            }
            h1{
              font-size:24px;
              margin:0 0 16px;
              display:flex;
              align-items:center;
              gap:8px;
            }
            .card{
              background:#020617;
              border-radius:16px;
              padding:16px 14px 20px;
              box-shadow:0 18px 45px rgba(0,0,0,0.55);
              border:1px solid #0f172a;
            }
            .row{ margin-bottom:12px; }
            label{
              font-size:13px;
              opacity:.8;
              display:block;
              margin-bottom:4px;
            }
            select,input[type="text"]{
              width:100%;
              padding:7px 10px;
              border-radius:10px;
              border:1px solid #1f2933;
              background:#020617;
              color:#e5e7eb;
              font-size:15px;
            }
            input[type="file"]{
              width:100%;
              font-size:14px;
            }
            .btn-main{
              width:100%;
              padding:10px 14px;
              border-radius:999px;
              border:none;
              background:#22c55e;
              color:#022c22;
              font-weight:700;
              font-size:16px;
            }
            .back{
              margin-top:14px;
              display:inline-flex;
              align-items:center;
              gap:6px;
              color:#93c5fd;
              text-decoration:none;
              font-size:14px;
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

                <div class="row">
                  <label for="files">Fotoğraf(lar):</label>
                  <input id="files"
                         name="files"
                         type="file"
                         accept="image/*"
                         capture="environment"
                         multiple>
                </div>

                <button class="btn-main" type="submit">
                  Kaydet
                </button>
              </form>
            </div>

            <a class="back" href="{{ nxt }}">
              ◀ Koltuk ekranına dön
            </a>
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
