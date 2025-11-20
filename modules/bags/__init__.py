# modules/bags/__init__.py
from __future__ import annotations

import os, time, secrets
from pathlib import Path
from urllib.parse import urlparse

from flask import (
    Blueprint, request, render_template_string, jsonify,
    send_from_directory, current_app, abort, session
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
    return _normalize_next(request.values.get("next") or request.headers.get("Referer") or "/seats")

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
    trip  = request.args.get("trip", "") or request.args.get("trip_code", "")
    seat  = request.args.get("seat", "")
    fmt   = request.args.get("format", "").lower()
    nxt   = _back_url()

    d = seat_dir(trip, seat)

    if fmt == "json":
        n = 0
        if d.exists():
            n = sum(1 for p in d.iterdir() if p.is_file() and _is_image(p))
        return jsonify(ok=True, count=int(n))

    imgs: list[tuple[str, str]] = []
    if d.exists():
        for p in sorted(d.iterdir()):
            if p.is_file() and _is_image(p):
                ensure_thumb(p)
                imgs.append((p.name, thumb_path(p).name))

    tpl = """
    <meta name=viewport content="width=device-width, initial-scale=1, viewport-fit=cover">
    <style>
      body{background:#101417;color:#eef;font-family:system-ui,-apple-system,Segoe UI,Roboto,Arial,sans-serif}
      .wrap{max-width:940px;margin:auto;padding:10px}
      .grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(160px,1fr));gap:10px}
      .card{background:#1b2126;border:1px solid #30363d;border-radius:14px;overflow:hidden}
      .t{text-align:center;padding:8px;font-weight:700}
      img{display:block;width:100%;height:160px;object-fit:cover;background:#0b0e10}
      .bar{display:flex;gap:8px;align-items:center;margin:8px 0 14px;justify-content:space-between}
      a.btn,button.btn{background:#2563eb;color:#fff;text-decoration:none;padding:8px 12px;border-radius:10px;border:none;display:inline-block}
      .muted{opacity:.8}
    </style>
    <div class=wrap>
      <div class=bar>
        <div class=muted>Trip: <b>{{trip}}</b> • Koltuk: <b>{{seat}}</b></div>
        <div style="display:flex;gap:8px">
          <a class=btn href="{{ url_for('bags.capture', trip_code=trip, seat=seat, next=nxt) }}">Bagaj Ekle</a>
          <a class=btn style="background:#374151" href="{{ nxt }}">Koltuk ekranına dön</a>
        </div>
      </div>
      {% if not imgs %}
        <p class=muted>Bu koltuk için kayıt yok.</p>
      {% else %}
        <div class=grid>
          {% for fn,tn in imgs %}
            <div class=card>
              <a href="{{ url_for('bags.raw', trip=trip, seat=seat, filename=fn) }}">
                <img loading="lazy" src="{{ url_for('bags.thumb', trip=trip, seat=seat, filename=tn) }}">
              </a>
              <div class=t>{{ loop.index }}</div>
            </div>
          {% endfor %}
        </div>
      {% endif %}
    </div>
    """
    return render_template_string(tpl, trip=trip, seat=seat, imgs=imgs, nxt=nxt)

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

# ------------- Yükleme ---------------
@bp.route("/capture", methods=["GET","POST"])
def capture():
    """Basit çoklu yükleme formu (kamera/galeri)."""
    if request.method == "POST":
        _check_csrf()  # ✅ CSRF

        trip = request.form.get("trip_code", "")
        seat = request.form.get("seat", "")
        to   = request.form.get("to_stop", "")
        nxt  = _normalize_next(request.form.get("next") or request.headers.get("Referer") or "/seats")

        files = request.files.getlist("files")  # input name=files multiple
        d = seat_dir(trip, seat)
        d.mkdir(parents=True, exist_ok=True)

        saved = 0
        for f in files:
            if not f or not f.filename:
                continue
            ext = (os.path.splitext(f.filename)[1] or ".jpg").lower()
            ts  = int(time.time() * 1000)
            name = f"{ts}_{safe(to) or 'bag'}{ext}"
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
            <meta name=viewport content="width=device-width, initial-scale=1">
            <meta http-equiv="refresh" content="1.2;url={{ nxt }}">
            <p style='color:#22c55e;font-weight:700'>{{n}} dosya kaydedildi.</p>
            <p style="display:flex;gap:8px">
              <a class="btn" href="{{ url_for('bags.gallery', trip=trip, seat=seat, next=nxt) }}">Galeriyi Aç</a>
              <a class="btn" style="background:#374151" href="{{ nxt }}">Koltuk ekranına dön</a>
              <a class="btn" href="{{ url_for('bags.capture', trip_code=trip, seat=seat, next=nxt) }}">Yeni Yükleme</a>
            </p>
            """,
            n=saved, trip=trip, seat=seat, nxt=nxt
        )

    # GET → form
    trip = request.args.get("trip_code", "")
    seat = request.args.get("seat", "")
    to   = request.args.get("to_stop", "")
    nxt  = _back_url()

    form = """
    <meta name=viewport content="width=device-width, initial-scale=1">
    <form method="post" enctype="multipart/form-data" style="max-width:620px;margin:auto;padding:12px;background:#0f172a;color:#e5e7eb;border-radius:14px">
      <!-- ✅ CSRF -->
      <input type="hidden" name="csrf_token" value="{{ csrf }}">
      <input type="hidden" name="trip_code" value="{{trip}}">
      <input type="hidden" name="seat" value="{{seat}}">
      <input type="hidden" name="next" value="{{nxt}}">

      <label>İniş (opsiyonel): <input name="to_stop" value="{{to}}" style="width:100%"></label>
      <div style="margin:10px 0">
        <input type="file" name="files" accept=".jpg,.jpeg,.png,.webp,image/*" multiple>
      </div>

      <button type="submit" style="padding:8px 12px;font-weight:700;border-radius:10px;background:#2563eb;color:#fff">Yükle</button>
      <a href="{{ url_for('bags.gallery', trip=trip, seat=seat, next=nxt) }}" style="padding:8px 12px;border-radius:10px;background:#334155;color:#fff;text-decoration:none">Galeri</a>
      <a href="{{ nxt }}" style="padding:8px 12px;border-radius:10px;background:#111827;color:#fff;text-decoration:none">Koltuk ekranına dön</a>
    </form>
    """
    return render_template_string(form, trip=trip, seat=seat, to=to, csrf=_get_csrf(), nxt=nxt)

# ----------- Ham ve Thumb servisleri -----------
@bp.route("/raw/<trip>/<seat>/<path:filename>")
def raw(trip: str, seat: str, filename: str):
    return send_from_directory(seat_dir(trip, seat), filename, as_attachment=False)

@bp.route("/thumb/<trip>/<seat>/<path:filename>")
def thumb(trip: str, seat: str, filename: str):
    return send_from_directory(seat_dir(trip, seat), filename, as_attachment=False)
