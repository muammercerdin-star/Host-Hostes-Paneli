from pathlib import Path
import sys
import traceback

ROOT = Path(".").resolve()
sys.path.insert(0, str(ROOT))

print("===== MUAVİN ASİSTANI STEP-6B RUNTIME SMOKE TEST FIXED =====")
print("ROOT:", ROOT)
print()

def section(t):
    print()
    print("===== " + t + " =====")

def body_text(res, limit=300):
    try:
        return res.get_data(as_text=True)[:limit]
    except TypeError:
        return res.data.decode("utf-8", "ignore")[:limit]
    except Exception:
        return ""

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

client = flask_app.test_client()

with client.session_transaction() as sess:
    sess["auth_ok"] = True
    sess["csrf_token"] = "audit-csrf-token"
    sess["route"] = "Denizli – İstanbul"

print("✅ Test session hazırlandı: auth_ok=True")

section("1) KRİTİK SAYFALAR GET TESTİ")

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
        text = body_text(res, 220).replace("\n", " ")
        page_results.append((url, status, loc, text))

        flag = "✅"
        if status >= 500:
            flag = "❌"
        elif status >= 400:
            flag = "⚠️"
        elif status in (301,302,303,307,308):
            flag = "↪️"

        print(f"{flag} {url:28} -> {status} {('Location=' + loc) if loc else ''} {text[:90]}")

    except Exception as e:
        print(f"❌ {url:28} -> EXCEPTION {type(e).__name__}: {e}")
        traceback.print_exc()

section("2) KRİTİK GET API TESTİ")

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
        body = body_text(res, 220).replace("\n", " ")
        flag = "✅" if res.status_code < 400 else ("⚠️" if res.status_code < 500 else "❌")
        print(f"{flag} {url:35} -> {res.status_code}  {body[:150]}")
    except Exception as e:
        print(f"❌ {url:35} -> EXCEPTION {type(e).__name__}: {e}")
        traceback.print_exc()

section("3) CSRF POST HIZLI KONTROL")

post_tests = [
    ("/set-route", {"route": "Denizli – İstanbul"}),
    ("/api/seat", {"seat_no": 1, "gender": "bay", "to_stop": "Alaşehir"}),
]

for url, data in post_tests:
    try:
        res_no = client.post(url, json=data)
        print(f"CSRF YOK  {url:18} -> {res_no.status_code}")

        res_yes = client.post(
            url,
            json=data,
            headers={"X-CSRF-Token": "audit-csrf-token"}
        )
        print(f"CSRF VAR  {url:18} -> {res_yes.status_code} {body_text(res_yes, 120).replace(chr(10), ' ')}")
    except Exception as e:
        print(f"❌ POST TEST {url} -> EXCEPTION {type(e).__name__}: {e}")
        traceback.print_exc()

section("4) STATIC HTTP TESTİ")

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

section("5) ÖZET")

bad_pages = [x for x in page_results if x[1] >= 500]
warn_pages = [x for x in page_results if 400 <= x[1] < 500]
redirect_pages = [x for x in page_results if x[1] in (301,302,303,307,308)]

print("500 veren sayfa:", len(bad_pages))
for url, status, loc, text in bad_pages:
    print(f"❌ {url} -> {status} {text[:160]}")

print()
print("400 veren sayfa:", len(warn_pages))
for url, status, loc, text in warn_pages:
    print(f"⚠️ {url} -> {status} {text[:160]}")

print()
print("Redirect veren sayfa:", len(redirect_pages))
for url, status, loc, text in redirect_pages:
    print(f"↪️ {url} -> {status} Location={loc}")

print()
print("===== STEP-6B BİTTİ =====")
