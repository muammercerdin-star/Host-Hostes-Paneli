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

V61_FUNC = r'''
    // CONTINUE_STALE_LIVE_SWITCH_V61
    // Eski canlı durak çok uzakta kaldıysa boşaltma; GPS'e göre en yakın rota durağına aktar.
    function nearestRouteStopByGpsV61(oldName){
      const routeCoords = Array.isArray(BOOT.routeCoords) ? BOOT.routeCoords : [];
      if(!lastPos || !routeCoords.length) return "";

      let best = null;

      for(const item of routeCoords){
        const name = String(item.stop || item.name || "").trim();
        if(!name) continue;

        if(oldName && norm(name) === norm(oldName)) continue;

        const lat = Number(item.lat ?? item.latitude);
        const lng = Number(item.lng ?? item.lon ?? item.longitude);

        if(!Number.isFinite(lat) || !Number.isFinite(lng)) continue;

        const km = distKm(lastPos, { lat, lng });
        if(!Number.isFinite(km)) continue;

        // Çok uzaktaki durağa zıplamasın.
        if(km > 18) continue;

        if(!best || km < best.km){
          best = { name, km };
        }
      }

      return best ? best.name : "";
    }

    function switchStaleLiveRuntimeV61(oldName, newName, gpsKm){
      const fromName = String(oldName || "").trim();
      const toName = String(newName || "").trim();

      if(!fromName || !toName) return;
      if(norm(fromName) === norm(toName)) return;

      const key = "continueStaleLiveSwitchV61:" + tripId + ":" + fromName + ">" + toName;

      try{
        if(sessionStorage.getItem(key) === "1") return;
        sessionStorage.setItem(key, "1");
      }catch(_){}

      const displaySpeed = liveDisplaySpeed();

      const url =
        `/api/live-runtime-state?write=1` +
        `&trip_id=${encodeURIComponent(tripId)}` +
        `&live_stop=${encodeURIComponent(toName)}` +
        `&speed=${encodeURIComponent(displaySpeed)}` +
        `&gps_km=` +
        `&eta_main=` +
        `&eta_sub=${encodeURIComponent("continue-stale-live-switch-v61")}` +
        `&_=${Date.now()}`;

      fetch(url, {
        method:"GET",
        credentials:"same-origin",
        cache:"no-store"
      }).finally(() => {
        try{
          const stopEl = document.getElementById("liveCurrentStopName");
          const distEl = document.getElementById("liveDistanceValue");
          const etaEl = document.getElementById("liveEtaValue");

          if(stopEl) stopEl.textContent = toName;
          if(distEl) distEl.textContent = "yakalanıyor";
          if(etaEl) etaEl.textContent = "—";
        }catch(_){}

        setTimeout(() => {
          try{ location.reload(); }catch(_){}
        }, 350);
      });
    }

'''

V61_HOOK = r'''
        // CONTINUE_STALE_LIVE_SWITCH_V61_HOOK
        // Eski canlı durak 6 km'den fazla uzaktaysa en yakın rota durağına aktar.
        if(Number.isFinite(liveKm) && liveKm > 6){
          const nextLiveV61 = nearestRouteStopByGpsV61(liveName);
          if(nextLiveV61){
            switchStaleLiveRuntimeV61(liveName, nextLiveV61, gpsKm);
            return;
          }
        }
'''

def backup(p):
    if p.exists():
        b = p.with_name(p.name + f".bak-stale-live-switch-v61-{STAMP}")
        shutil.copy2(p, b)
        print("📦 Yedek:", b.relative_to(ROOT))

print("===== CONTINUE STALE LIVE SWITCH V61 =====")

for p in FILES:
    if not p.exists():
        print("⚠️ Yok:", p.relative_to(ROOT))
        continue

    backup(p)
    s = p.read_text(encoding="utf-8", errors="ignore")

    # Eski V60B fonksiyonunu kaldır
    s = re.sub(
        r'\n\s*// CONTINUE_STALE_LIVE_CLEAR_V60B.*?\n\s*function\s+writeRuntime',
        '\n    function writeRuntime',
        s,
        flags=re.S
    )

    # Eski V60C hook'u kaldır
    s = re.sub(
        r'\n\s*// CONTINUE_STALE_LIVE_CLEAR_V60C_HOOK.*?clearStaleLiveRuntimeV60B\(liveName,\s*gpsKm\);\s*return;\s*\}\s*',
        '\n',
        s,
        flags=re.S
    )

    # V61 zaten varsa tekrar ekleme
    if "CONTINUE_STALE_LIVE_SWITCH_V61" not in s:
        m = re.search(r'(\n\s*function\s+writeRuntime\s*\(\s*liveName\s*,\s*gpsKm\s*,\s*etaMain\s*\)\s*\{)', s)
        if not m:
          print("❌ writeRuntime bulunamadı:", p.relative_to(ROOT))
          continue
        s = s[:m.start()] + "\n" + V61_FUNC.rstrip() + s[m.start():]
        print("✅ V61 switch fonksiyonu eklendi:", p.relative_to(ROOT))

    if "CONTINUE_STALE_LIVE_SWITCH_V61_HOOK" not in s:
        pattern = re.compile(
            r'(const\s+liveKm\s*=\s*distKm\s*\(\s*lastPos\s*,\s*liveCoord\s*\)\s*;\s*\n\s*gpsKm\s*=\s*formatKm\s*\(\s*liveKm\s*\)\s*;)',
            re.M
        )
        m = pattern.search(s)
        if not m:
            print("❌ liveKm/gpsKm bloğu bulunamadı:", p.relative_to(ROOT))
            continue

        s = s[:m.end()] + "\n" + V61_HOOK.rstrip() + s[m.end():]
        print("✅ V61 hook eklendi:", p.relative_to(ROOT))

    p.write_text(s, encoding="utf-8")

for p in TPLS:
    if not p.exists():
        print("⚠️ Yok:", p.relative_to(ROOT))
        continue

    backup(p)
    s = p.read_text(encoding="utf-8", errors="ignore")

    s = re.sub(
        r"continue_trip_core\.js'\) }}\?v=[^\"']+",
        "continue_trip_core.js') }}?v=stale-switch-v61",
        s
    )
    s = re.sub(
        r'continue_trip_core\.js"\) }}\?v=[^"\']+',
        'continue_trip_core.js") }}?v=stale-switch-v61',
        s
    )

    p.write_text(s, encoding="utf-8")
    print("✅ Cache kırıldı:", p.relative_to(ROOT))

print()
print("✅ V61 tamam. Eski canlı durak artık boşaltılmayacak, yakın rota durağına aktarılacak.")
