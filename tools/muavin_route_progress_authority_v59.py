from pathlib import Path
from datetime import datetime
import shutil
import re

ROOT = Path(".").resolve()
STAMP = datetime.now().strftime("%Y%m%d-%H%M%S")

APP_FILES = [
    ROOT / "app.py",
    ROOT / "android_app/app/src/main/python/app.py",
]

SEATS_JS_FILES = [
    ROOT / "static/seats/seats.js",
    ROOT / "android_app/app/src/main/python/static/seats/seats.js",
]

CONTINUE_JS_FILES = [
    ROOT / "static/continue/continue_trip_core.js",
    ROOT / "android_app/app/src/main/python/static/continue/continue_trip_core.js",
]

TPL_FILES = [
    ROOT / "templates/seats.html",
    ROOT / "android_app/app/src/main/python/templates/seats.html",
    ROOT / "templates/continue_trip.html",
    ROOT / "android_app/app/src/main/python/templates/continue_trip.html",
]

def backup(p):
    if p.exists():
        b = p.with_name(p.name + f".bak-route-progress-v59-{STAMP}")
        shutil.copy2(p, b)
        print("📦 Yedek:", b.relative_to(ROOT))

print("===== ROUTE PROGRESS AUTHORITY V59 =====")

# 1) Backend: preserve_live_stop desteği
for p in APP_FILES:
    if not p.exists():
        print("⚠️ Yok:", p.relative_to(ROOT))
        continue

    backup(p)
    s = p.read_text(encoding="utf-8", errors="ignore")
    old = s

    if "preserve_live_stop" not in s:
        target = '''    if write_mode:
        live_stop = (request.args.get("live_stop") or "").strip()
        gps_km = (request.args.get("gps_km") or "").strip()
'''
        repl = '''    if write_mode:
        # ROUTE_PROGRESS_AUTHORITY_V59
        # Canlı Durak Akışı ekranı live_stop seçicisi değildir.
        # preserve_live_stop=1 gelirse mevcut canlı durak korunur.
        preserve_live_stop = (request.args.get("preserve_live_stop") or "").strip() == "1"
        live_stop_arg_present = "live_stop" in request.args

        if preserve_live_stop and not live_stop_arg_present:
            try:
                live_stop = (fetch_live_runtime_state(tid).get("live_stop") or "").strip()
            except Exception:
                live_stop = ""
        else:
            live_stop = (request.args.get("live_stop") or "").strip()

        if not live_stop:
            try:
                session.pop("continue_current_stop", None)
            except Exception:
                pass

        gps_km = (request.args.get("gps_km") or "").strip()
'''
        if target in s:
            s = s.replace(target, repl, 1)
            print("✅ Backend preserve_live_stop eklendi:", p.relative_to(ROOT))
        else:
            print("⚠️ Backend hedef blok bulunamadı:", p.relative_to(ROOT))
    else:
        print("ℹ️ Backend preserve_live_stop zaten var:", p.relative_to(ROOT))

    if s != old:
        p.write_text(s, encoding="utf-8")

# 2) Continue ekranı: live_stop yazmasın
for p in CONTINUE_JS_FILES:
    if not p.exists():
        print("⚠️ Yok:", p.relative_to(ROOT))
        continue

    backup(p)
    s = p.read_text(encoding="utf-8", errors="ignore")
    old = s

    s = s.replace(
        '`&live_stop=${encodeURIComponent(liveName || "")}` +',
        '`&preserve_live_stop=1` +'
    )

    if "ROUTE_PROGRESS_AUTHORITY_V59_CONTINUE_READONLY" not in s:
        s = s.replace(
            "function writeRuntime(liveName, gpsKm, etaMain){",
            "function writeRuntime(liveName, gpsKm, etaMain){\n    // ROUTE_PROGRESS_AUTHORITY_V59_CONTINUE_READONLY\n    // Bu ekran canlı durak seçmez; sadece hız/mesafe/ETA senkronlar."
        )

    if s != old:
        p.write_text(s, encoding="utf-8")
        print("✅ Continue ekranı live_stop yazıcılıktan çıkarıldı:", p.relative_to(ROOT))
    else:
        print("ℹ️ Continue JS değişmedi:", p.relative_to(ROOT))

# 3) Seats GPS motoru: rota ilerlemesini işlemden bağımsız yap
for p in SEATS_JS_FILES:
    if not p.exists():
        print("⚠️ Yok:", p.relative_to(ROOT))
        continue

    backup(p)
    s = p.read_text(encoding="utf-8", errors="ignore")
    old = s

    if "LIVE_CLEAR_KM" not in s:
        s = s.replace(
            "  const LIVE_LOOKAHEAD_STOPS = 4;  // Mevcut canlı duraktan sonra kaç durağa bakılsın",
            "  const LIVE_LOOKAHEAD_STOPS = 4;  // Mevcut canlı duraktan sonra kaç durağa bakılsın\n  const LIVE_CLEAR_KM = 6;        // Canlı durak bu mesafeden uzağa düştüyse eski kabul edilir"
        )

    # İşlem yoksa canlı aday olmasın kuralını kaldır
    s = s.replace(
        "          // İşlem yoksa canlı durak yapma.\n          if(!hasLiveStopOperation(canonical)) continue;",
        "          // ROUTE_PROGRESS_AUTHORITY_V59\n          // Rota ilerlemesi işlemden bağımsızdır.\n          // İşlem olmayan durak da geçildi/sıradaki takibi için canlı aday olabilir."
    )

    # İşlem yok diye mevcut canlıyı temizlemeyi kapat
    s = s.replace(
        "if(speedState.liveStop && !hasLiveStopOperation(speedState.liveStop)){",
        "if(false && speedState.liveStop && !hasLiveStopOperation(speedState.liveStop)){"
    )

    # Aday yoksa ve mevcut canlı durak artık uzaktaysa temizle
    if "ROUTE_PROGRESS_V59_NO_CANDIDATE_CLEAR" not in s:
        target = '''        if(!candidates.length){
          liveDetectCandidate = {
            name: "",
            hits: 0,
            lastAt: 0
          };

          // Mevcut canlı durakta artık işlem yoksa canlıyı boşalt.
'''
        repl = '''        if(!candidates.length){
          liveDetectCandidate = {
            name: "",
            hits: 0,
            lastAt: 0
          };

          // ROUTE_PROGRESS_V59_NO_CANDIDATE_CLEAR
          // Aday yoksa ve mevcut canlı durak artık çok uzakta kaldıysa eski canlıyı temizle.
          try{
            if(speedState.liveStop && typeof stopDistanceKmByName === "function"){
              const liveKm = stopDistanceKmByName(speedState.liveStop);
              if(Number.isFinite(liveKm) && liveKm > LIVE_CLEAR_KM){
                speedState.liveStop = "";
                speedState.passedStops = new Set();
                persistVoiceState();
                try{ persistLiveRuntimeStateToServer(); }catch(_){}
                renderRouteStrip();
                renderTimeline();
                renderAI();
                updateCompactHeader();
              }
            }
          }catch(_){}

          // V59: İşlem yok diye canlıyı boşaltma kapalı.
'''
        if target in s:
            s = s.replace(target, repl, 1)
        else:
            print("⚠️ no-candidate blok hedefi bulunamadı:", p.relative_to(ROOT))

    # Backend'e yazarken uzak liveStop'u hem local hem backend tarafında boşalt
    s = s.replace(
        '''          if(Number.isFinite(liveKmCheck) && liveKmCheck > 5.5){
            liveStop = "";
          }''',
        '''          if(Number.isFinite(liveKmCheck) && liveKmCheck > LIVE_CLEAR_KM){
            liveStop = "";
            try{
              speedState.liveStop = "";
              speedState.passedStops = new Set();
              persistVoiceState();
            }catch(_){}
          }'''
    )

    if s != old:
        p.write_text(s, encoding="utf-8")
        print("✅ Seats rota ilerleme mantığı güncellendi:", p.relative_to(ROOT))
    else:
        print("ℹ️ Seats JS değişmedi:", p.relative_to(ROOT))

# 4) Cache kır
for p in TPL_FILES:
    if not p.exists():
        print("⚠️ Yok:", p.relative_to(ROOT))
        continue

    backup(p)
    s = p.read_text(encoding="utf-8", errors="ignore")
    old = s

    s = re.sub(
        r'/static/seats/seats\.js\?v=[^"]+',
        '/static/seats/seats.js?v=route-progress-v59',
        s
    )

    s = re.sub(
        r"continue_trip_core\.js'\) }}\?v=[^\"']+",
        "continue_trip_core.js') }}?v=route-progress-v59",
        s
    )
    s = re.sub(
        r'continue_trip_core\.js"\) }}\?v=[^"\']+',
        'continue_trip_core.js") }}?v=route-progress-v59',
        s
    )

    if s != old:
        p.write_text(s, encoding="utf-8")
        print("✅ Cache kırıldı:", p.relative_to(ROOT))
    else:
        print("ℹ️ Template değişmedi:", p.relative_to(ROOT))

print()
print("✅ V59 tamamlandı. Commit/push yok. Önce tarayıcıda test et.")
