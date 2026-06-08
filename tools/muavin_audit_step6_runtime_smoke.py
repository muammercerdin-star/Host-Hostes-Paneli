from pathlib import Path
import sys
import traceback
import json
import re

ROOT = Path(".").resolve()
sys.path.insert(0, str(ROOT))

print("===== MUAVİN ASİSTANI STEP-6 RUNTIME SMOKE TEST =====")
print("ROOT:", ROOT)
print()

def section(t):
    print()
    print("===== " + t + " =====")

try:
    import app as app_module
    flask_app = app_module.app
    flask_app.config["TESTING"] = True
    print("✅ Flask app import edildi")
except Exception as e:
    print("❌ Flask app import edilemedi")
    print(type(e).__name__ + ":", e)
    traceback.print_exc()
    raise SystemExit(1)

# ------------------------------------------------------------
# 1) LOGIN / SESSION ANAHTARLARI GÖRÜNÜMÜ
# ------------------------------------------------------------
section("1) app.py LOGIN / SESSION İZLERİ")

app_text = Path("app.py").read_text(encoding="utf-8", errors="ignore")
for pat in ["def login", "session[", "session.get", "csrf_token", "admin", "logged"]:
    print()
    print(f"--- arama: {pat} ---")
    lines = app_text.splitlines()
    for i, line in enumerate(lines, start=1):
        if pat in line:
            s = max(1, i-3)
            e = min(len(lines), i+5)
            print(f"### satır {i}")
            for j in range(s, e+1):
                mark = ">>" if j == i else "  "
                print(f"{mark} {j:5}: {lines[j-1]}")
            print()

# ------------------------------------------------------------
# 2) TEST CLIENT SESSION HAZIRLIĞI
# ------------------------------------------------------------
section("2) TEST CLIENT SESSION HAZIRLIĞI")

client = flask_app.test_client()

with client.session_transaction() as sess:
    # Mevcut projelerde görülebilecek olası login/session anahtarlarını set ediyoruz.
    # Bu sadece test client içindir; gerçek dosya/db değiştirmez.
    sess["logged_in"] = True
    sess["admin_logged_in"] = True
    sess["is_admin"] = True
    sess["user"] = "audit"
    sess["username"] = "audit"
    sess["role"] = "admin"
    sess["csrf_token"] = "audit-csrf-token"

print("✅ Test session hazırlandı")

# ------------------------------------------------------------
# 3) KRİTİK SAYFALAR GET TESTİ
# ------------------------------------------------------------
section("3) KRİTİK SAYFALAR GET TESTİ")

pages = [
    "/",
    "/seats",
    "/continue-trip",
    "/emanetler",
    "/raporlar",
    "/sefer-raporu",
    "/rapor-arsiv",
    "/hatlar",
    "/hat-ekle",
    "/hesap",
    "/olaylar",
    "/canli-harita",
    "/ayarlar",
    "/ayarlar/abonelik",
    "/ayarlar/profil",
    "/ayarlar/sifre",
    "/ayarlar/yedekleme",
    "/rehber",
    "/yolcu-kontrol",
    "/fiyat",
    "/fiyat-g",
    "/tanitim",
    "/kurulum",
]

page_results = []

for url in pages:
    try:
        res = client.get(url, follow_redirects=False)
        status = res.status_code
        loc = res.headers.get("Location", "")
        text = res.get_data(as_text=True, errors="ignore")[:300]
        page_results.append((url, status, loc, text))

        flag = "✅"
        if status >= 500:
            flag = "❌"
        elif status >= 400:
            flag = "⚠️"
        elif status in (301,302,303,307,308):
            flag = "↪️"

        print(f"{flag} {url:28} -> {status} {('Location=' + loc) if loc else ''}")

    except Exception as e:
        print(f"❌ {url:28} -> EXCEPTION {type(e).__name__}: {e}")
        traceback.print_exc()

# ------------------------------------------------------------
# 4) KRİTİK GET API TESTİ
# ------------------------------------------------------------
section("4) KRİTİK GET API TESTİ")

api_gets = [
    "/api/stats",
    "/api/stops",
    "/api/seats/list",
    "/api/standing/list",
    "/api/events",
    "/api/report/seat-stats",
    "/api/report/seat-detail",
    "/api/report-archive",
    "/api/trip-report",
    "/api/live-runtime-state",
    "/api/speedlimit?lat=38.35&lng=28.52",
    "/api/route-stop",
    "/api/seats",
]

for url in api_gets:
    try:
        res = client.get(url, follow_redirects=False)
        body = res.get_data(as_text=True, errors="ignore")[:220].replace("\n", " ")
        flag = "✅" if res.status_code < 400 else ("⚠️" if res.status_code < 500 else "❌")
        print(f"{flag} {url:35} -> {res.status_code}  {body[:160]}")
    except Exception as e:
        print(f"❌ {url:35} -> EXCEPTION {type(e).__name__}: {e}")
        traceback.print_exc()

# ------------------------------------------------------------
# 5) EKSİK STATIC GERÇEKTEN 404 MÜ?
# ------------------------------------------------------------
section("5) STATIC DOSYA HTTP TESTİ")

static_urls = [
    "/static/vendor/bootstrap/bootstrap.min.css",
    "/static/vendor/icons.css",
    "/static/css/style.css",
    "/static/vendor/jquery.min.js",
    "/static/vendor/bootstrap/bootstrap.bundle.min.js",
    "/static/app.js",
    "/static/seats/seats.js",
    "/static/seats/patches/unified-seat-deck-report-style.css",
    "/static/img/rehber-koltuk-yonetimi-card.png",
    "/static/img/rehber-durak-akisi.png",
    "/static/img/rehber-voice-command.png",
]

for url in static_urls:
    try:
        res = client.get(url)
        flag = "✅" if res.status_code == 200 else "⚠️"
        print(f"{flag} {url:62} -> {res.status_code} len={len(res.data)}")
    except Exception as e:
        print(f"❌ {url:62} -> EXCEPTION {type(e).__name__}: {e}")

# ------------------------------------------------------------
# 6) BASE EXTEND EDEN SAYFALAR
# ------------------------------------------------------------
section("6) base.html EXTEND EDEN TEMPLATE LİSTESİ")

for folder in ["templates", "android_app/app/src/main/python/templates"]:
    base = ROOT / folder
    if not base.exists():
        continue

    print()
    print(f"--- {folder} ---")
    for p in sorted(base.rglob("*.html")):
        txt = p.read_text(encoding="utf-8", errors="ignore")
        if 'extends "base.html"' in txt or "extends 'base.html'" in txt:
            print(str(p.relative_to(ROOT)))

# ------------------------------------------------------------
# 7) RAPOR ÖZETİ
# ------------------------------------------------------------
section("7) STEP-6 ÖZET")

bad_pages = [x for x in page_results if x[1] >= 500]
warn_pages = [x for x in page_results if 400 <= x[1] < 500]

print("500 veren sayfa sayısı:", len(bad_pages))
for url, status, loc, text in bad_pages:
    print(f"❌ {url} -> {status} {text[:180]}")

print()
print("400 veren sayfa sayısı:", len(warn_pages))
for url, status, loc, text in warn_pages:
    print(f"⚠️ {url} -> {status} {text[:180]}")

print()
print("===== STEP-6 BİTTİ =====")
