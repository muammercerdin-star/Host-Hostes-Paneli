from pathlib import Path
from datetime import datetime
import shutil
import re

ROOT = Path(".").resolve()
STAMP = datetime.now().strftime("%Y%m%d-%H%M%S")

FILES = [
    ROOT / "static/continue/continue_trip_core.js",
    ROOT / "android_app/app/src/main/python/static/continue/continue_trip_core.js",
]

TPLS = [
    ROOT / "templates/continue_trip.html",
    ROOT / "android_app/app/src/main/python/templates/continue_trip.html",
]

HOOK = r'''
      // CONTINUE_WAITING_LIVE_ACQUIRE_V64B
      // Canlı durak boşsa / bekleniyorsa / seçilmediyse
      // bu ekran ilk durağa düşmez; GPS'e göre en yakın rota durağını yakalar.
      const liveNormV64B = norm(liveName || "");

      if(
        !liveName ||
        liveNormV64B.includes("bekleniyor") ||
        liveNormV64B.includes("secilmedi") ||
        liveNormV64B.includes("seçilmedi") ||
        liveNormV64B === "denizli"
      ){
        try{
          if(
            typeof nearestRouteStopByGpsV61 === "function" &&
            typeof switchStaleLiveRuntimeV61 === "function"
          ){
            const nextLiveV64B = nearestRouteStopByGpsV61("");
            if(nextLiveV64B){
              switchStaleLiveRuntimeV61(liveName || "Canlı durak bekleniyor", nextLiveV64B, "");
            }
          }
        }catch(_){}
        return;
      }
'''

def backup(p):
    if p.exists():
        b = p.with_name(p.name + f".bak-live-stop-v64b-{STAMP}")
        shutil.copy2(p, b)
        print("📦 Yedek:", b.relative_to(ROOT))

print("===== LIVE STOP ACQUIRE HOOK V64B =====")

for p in FILES:
    if not p.exists():
        print("⚠️ Yok:", p.relative_to(ROOT))
        continue

    backup(p)
    s = p.read_text(encoding="utf-8", errors="ignore")
    old = s

    if "CONTINUE_WAITING_LIVE_ACQUIRE_V64B" in s:
        print("ℹ️ V64B zaten var:", p.relative_to(ROOT))
        continue

    # compute() içinde const liveName = liveStopName(); satırından hemen sonra ekle
    pattern = re.compile(
        r'(function\s+compute\s*\(\)\s*\{\s*\n\s*if\(!lastPos\)\s*return;\s*\n\s*const\s+liveName\s*=\s*liveStopName\(\)\s*;)',
        re.M
    )

    m = pattern.search(s)
    if not m:
        print("❌ compute/liveName bloğu bulunamadı:", p.relative_to(ROOT))
        continue

    s = s[:m.end()] + "\n" + HOOK.rstrip() + s[m.end():]

    # Eski boş liveName return satırı varsa kalsın; hook zaten ondan önce çalışacak.
    p.write_text(s, encoding="utf-8")
    print("✅ GPS canlı durak yakalama hook'u eklendi:", p.relative_to(ROOT))

for p in TPLS:
    if not p.exists():
        print("⚠️ Yok:", p.relative_to(ROOT))
        continue

    backup(p)
    s = p.read_text(encoding="utf-8", errors="ignore")
    old = s

    s = re.sub(
        r"continue_trip_core\.js'\) }}\?v=[^\"']+",
        "continue_trip_core.js') }}?v=live-stop-v64b",
        s
    )
    s = re.sub(
        r'continue_trip_core\.js"\) }}\?v=[^"\']+',
        'continue_trip_core.js") }}?v=live-stop-v64b',
        s
    )

    if s != old:
        p.write_text(s, encoding="utf-8")
        print("✅ Cache kırıldı:", p.relative_to(ROOT))

print()
print("✅ V64B tamam. Şimdi /continue sayfasını yenile.")
