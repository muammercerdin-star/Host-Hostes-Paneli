from pathlib import Path
from datetime import datetime
import shutil
import re

ROOT = Path(".").resolve()
STAMP = datetime.now().strftime("%Y%m%d-%H%M%S")

FILES = [
    ROOT / "static/seats/seats.js",
    ROOT / "android_app/app/src/main/python/static/seats/seats.js",
]

INSERT = r'''
          // ROUTE_PROGRESS_V59B_NO_CANDIDATE_CLEAR
          // Aday yoksa ve mevcut canlı durak artık çok uzakta kaldıysa eski canlıyı temizle.
          try{
            if(speedState.liveStop && typeof stopDistanceKmByName === "function"){
              const liveKm = stopDistanceKmByName(speedState.liveStop);

              if(Number.isFinite(liveKm) && liveKm > LIVE_CLEAR_KM){
                speedState.liveStop = "";
                speedState.passedStops = new Set();

                persistVoiceState();

                try{
                  persistLiveRuntimeStateToServer();
                }catch(_){}

                renderRouteStrip();
                renderTimeline();
                renderAI();
                updateCompactHeader();
              }
            }
          }catch(_){}
'''

def backup(p):
    if p.exists():
        b = p.with_name(p.name + f".bak-route-progress-v59b-{STAMP}")
        shutil.copy2(p, b)
        print("📦 Yedek:", b.relative_to(ROOT))

print("===== ROUTE PROGRESS V59B COMPLETE CLEAR =====")

for p in FILES:
    if not p.exists():
        print("⚠️ Yok:", p.relative_to(ROOT))
        continue

    backup(p)
    s = p.read_text(encoding="utf-8", errors="ignore")
    old = s

    if "ROUTE_PROGRESS_V59B_NO_CANDIDATE_CLEAR" in s:
        print("ℹ️ V59B zaten var:", p.relative_to(ROOT))
        continue

    pattern = re.compile(
        r'''(if\(!candidates\.length\)\{\s*
\s*liveDetectCandidate\s*=\s*\{\s*
\s*name:\s*"",\s*
\s*hits:\s*0,\s*
\s*lastAt:\s*0\s*
\s*\};)''',
        re.M
    )

    m = pattern.search(s)
    if not m:
        print("❌ if(!candidates.length) bloğu bulunamadı:", p.relative_to(ROOT))
        continue

    s = s[:m.end()] + "\n" + INSERT.rstrip() + s[m.end():]

    p.write_text(s, encoding="utf-8")
    print("✅ V59B temizleme bloğu eklendi:", p.relative_to(ROOT))

print()
print("✅ V59B tamam.")
