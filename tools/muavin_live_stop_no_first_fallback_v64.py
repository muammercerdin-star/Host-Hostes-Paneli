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

CONTINUE_JS_FILES = [
    ROOT / "static/continue/continue_trip_core.js",
    ROOT / "android_app/app/src/main/python/static/continue/continue_trip_core.js",
]

TPL_FILES = [
    ROOT / "templates/continue_trip.html",
    ROOT / "android_app/app/src/main/python/templates/continue_trip.html",
]

def backup(p):
    if p.exists():
        b = p.with_name(p.name + f".bak-live-stop-v64-{STAMP}")
        shutil.copy2(p, b)
        print("📦 Yedek:", b.relative_to(ROOT))

print("===== LIVE STOP NO FIRST FALLBACK V64 =====")

# 1) Backend: canlı durak boşsa ilk durağa / eski session'a / ilk işlem durağına düşme
for p in APP_FILES:
    if not p.exists():
        print("⚠️ Yok:", p.relative_to(ROOT))
        continue

    backup(p)
    s = p.read_text(encoding="utf-8", errors="ignore")
    old = s

    if "LIVE_STOP_NO_FIRST_FALLBACK_V64" not in s:
        pattern = re.compile(
            r'''    if matched_requested_stop:\n'''
            r'''        current_stop = matched_requested_stop\n'''
            r'''        session\["continue_current_stop"\] = current_stop\n'''
            r'''    elif matched_runtime_stop:\n'''
            r'''        current_stop = matched_runtime_stop\n'''
            r'''        session\["continue_current_stop"\] = current_stop\n'''
            r'''    elif matched_session_stop:\n'''
            r'''        current_stop = matched_session_stop\n'''
            r'''    else:\n'''
            r'''        # Rotadaki sıraya göre, iniş/biniş/bagaj/servis işlemi olan ilk durağı seç\.\n'''
            r'''        operation_keys = set\(\)\n'''
            r'''        operation_keys\.update\(k for k, v in stop_off_counts\.items\(\) if v\)\n'''
            r'''        operation_keys\.update\(k for k, v in stop_board_counts\.items\(\) if v\)\n'''
            r'''        operation_keys\.update\(k for k, v in stop_walkon_counts\.items\(\) if v\)\n'''
            r'''        operation_keys\.update\(k for k, v in stop_consignment_counts\.items\(\) if v\)\n'''
            r'''        operation_keys\.update\(k for k, v in stop_bag_counts\.items\(\) if v\)\n'''
            r'''        operation_keys\.update\(k for k, v in stop_service_counts\.items\(\) if v\)\n\n'''
            r'''        for stop_name in stops:\n'''
            r'''            if norm_stop\(stop_name\) in operation_keys:\n'''
            r'''                current_stop = stop_name\n'''
            r'''                break\n''',
            re.M
        )

        repl = '''    if matched_requested_stop:
        current_stop = matched_requested_stop
        session["continue_current_stop"] = current_stop
    elif matched_runtime_stop:
        current_stop = matched_runtime_stop
        session["continue_current_stop"] = current_stop
    else:
        # LIVE_STOP_NO_FIRST_FALLBACK_V64
        # Canlı durak boşsa session/ilk işlem/ilk durak tahmini yapma.
        # GPS yakalayana kadar ekranda "Canlı durak bekleniyor" göster.
        current_stop = ""
        try:
            session.pop("continue_current_stop", None)
        except Exception:
            pass
'''

        s, n = pattern.subn(repl, s, count=1)
        if n:
            print("✅ Session / ilk işlem fallback kapatıldı:", p.relative_to(ROOT))
        else:
            print("⚠️ Büyük fallback bloğu bulunamadı:", p.relative_to(ROOT))

        s = s.replace(
            '''    if not current_stop:
        current_stop = first_stop
''',
            '''    if not current_stop:
        # LIVE_STOP_NO_FIRST_FALLBACK_V64
        # Boş canlı durakta ilk durağa düşme.
        current_stop = ""
'''
        )

    if s != old:
        p.write_text(s, encoding="utf-8")

# 2) Continue ekranı: canlı durak bekleniyorsa GPS ile en yakın rota durağını yakalamayı dene
for p in CONTINUE_JS_FILES:
    if not p.exists():
        print("⚠️ Yok:", p.relative_to(ROOT))
        continue

    backup(p)
    s = p.read_text(encoding="utf-8", errors="ignore")
    old = s

    if "CONTINUE_WAITING_LIVE_ACQUIRE_V64" not in s:
        target = '''      const liveName = liveStopName();
      if(!liveName) return;
'''
        repl = '''      const liveName = liveStopName();

      // CONTINUE_WAITING_LIVE_ACQUIRE_V64
      // Backend canlı durak boşsa veya bekleniyor durumundaysa
      // ilk durağı canlı sanma; GPS'e göre en yakın rota durağını yakalamayı dene.
      const liveNormV64 = norm(liveName || "");
      if(
        !liveName ||
        liveNormV64.includes("bekleniyor") ||
        liveNormV64.includes("secilmedi") ||
        liveNormV64.includes("seçilmedi") ||
        liveNormV64.includes("durak secilmedi") ||
        liveNormV64.includes("durak seçilmedi")
      ){
        try{
          if(
            typeof nearestRouteStopByGpsV61 === "function" &&
            typeof switchStaleLiveRuntimeV61 === "function"
          ){
            const nextLiveV64 = nearestRouteStopByGpsV61("");
            if(nextLiveV64){
              switchStaleLiveRuntimeV61(liveName || "Canlı durak bekleniyor", nextLiveV64, "");
            }
          }
        }catch(_){}
        return;
      }
'''

        if target in s:
            s = s.replace(target, repl, 1)
            print("✅ Bekleyen canlı durak GPS yakalama eklendi:", p.relative_to(ROOT))
        else:
            print("⚠️ compute liveName bloğu bulunamadı:", p.relative_to(ROOT))

    if s != old:
        p.write_text(s, encoding="utf-8")

# 3) Cache kır
for p in TPL_FILES:
    if not p.exists():
        print("⚠️ Yok:", p.relative_to(ROOT))
        continue

    backup(p)
    s = p.read_text(encoding="utf-8", errors="ignore")
    old = s

    s = re.sub(
        r"continue_trip_core\.js'\) }}\?v=[^\"']+",
        "continue_trip_core.js') }}?v=live-stop-v64",
        s
    )
    s = re.sub(
        r'continue_trip_core\.js"\) }}\?v=[^"\']+',
        'continue_trip_core.js") }}?v=live-stop-v64',
        s
    )

    if s != old:
        p.write_text(s, encoding="utf-8")
        print("✅ Cache kırıldı:", p.relative_to(ROOT))

print()
print("✅ V64 tamam. Şimdi sayfayı yenile.")
print("Beklenen: canlı durak boşsa Denizli yazmayacak; GPS yakalayınca gerçek durağa geçecek.")
