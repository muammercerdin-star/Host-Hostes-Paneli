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

CLEAR_FUNC = r'''
    // CONTINUE_STALE_LIVE_CLEAR_V60B
    // Bu ekran canlı durak seçmez; çok uzakta kalmış eski canlı durağı temizler.
    function clearStaleLiveRuntimeV60B(liveName, gpsKm){
      const staleName = String(liveName || "").trim();
      if(!staleName) return;

      const key = "continueStaleLiveClearV60B:" + tripId + ":" + staleName;

      try{
        if(sessionStorage.getItem(key) === "1") return;
        sessionStorage.setItem(key, "1");
      }catch(_){}

      const displaySpeed = liveDisplaySpeed();

      const url =
        `/api/live-runtime-state?write=1` +
        `&trip_id=${encodeURIComponent(tripId)}` +
        `&live_stop=` +
        `&speed=${encodeURIComponent(displaySpeed)}` +
        `&gps_km=${encodeURIComponent(gpsKm || "")}` +
        `&eta_main=` +
        `&eta_sub=${encodeURIComponent("continue-stale-live-clear-v60b")}` +
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

          if(stopEl) stopEl.textContent = "Canlı durak bekleniyor";
          if(distEl) distEl.textContent = "—";
          if(etaEl) etaEl.textContent = "—";
        }catch(_){}

        setTimeout(() => {
          try{ location.reload(); }catch(_){}
        }, 350);
      });
    }

'''

CHECK_CODE = r'''
        // CONTINUE_STALE_LIVE_CLEAR_V60B
        // Eski canlı durak 6 km'den fazla uzaktaysa temizle.
        if(Number.isFinite(liveKm) && liveKm > 6){
          clearStaleLiveRuntimeV60B(liveName, gpsKm);
          return;
        }
'''

def backup(p):
    if p.exists():
        b = p.with_name(p.name + f".bak-stale-live-clear-v60b-{STAMP}")
        shutil.copy2(p, b)
        print("📦 Yedek:", b.relative_to(ROOT))

print("===== CONTINUE STALE LIVE CLEAR V60B =====")

for p in FILES:
    if not p.exists():
        print("⚠️ Yok:", p.relative_to(ROOT))
        continue

    backup(p)
    s = p.read_text(encoding="utf-8", errors="ignore")
    old = s

    if "CONTINUE_STALE_LIVE_CLEAR_V60B" in s:
        print("ℹ️ V60B zaten var:", p.relative_to(ROOT))
        continue

    # 1) writeRuntime fonksiyonundan önce clear fonksiyonunu ekle, boşluk fark etmez
    m = re.search(r'(\n\s*function\s+writeRuntime\s*\(\s*liveName\s*,\s*gpsKm\s*,\s*etaMain\s*\)\s*\{)', s)
    if not m:
        print("❌ writeRuntime fonksiyonu yine bulunamadı:", p.relative_to(ROOT))
        continue

    s = s[:m.start()] + "\n" + CLEAR_FUNC.rstrip() + s[m.start():]
    print("✅ Clear fonksiyonu eklendi:", p.relative_to(ROOT))

    # 2) liveKm hesaplandıktan sonra 6 km kontrolü ekle
    target = '        setText("#liveDistanceValue", gpsKm);'
    if target not in s:
        print("❌ liveDistanceValue setText satırı bulunamadı:", p.relative_to(ROOT))
        p.write_text(s, encoding="utf-8")
        continue

    s = s.replace(target, target + "\n" + CHECK_CODE.rstrip(), 1)
    print("✅ 6 km eski canlı durak kontrolü eklendi:", p.relative_to(ROOT))

    p.write_text(s, encoding="utf-8")

# Cache tekrar kır
for p in TPLS:
    if not p.exists():
        print("⚠️ Yok:", p.relative_to(ROOT))
        continue

    backup(p)
    s = p.read_text(encoding="utf-8", errors="ignore")
    old = s

    s = re.sub(
        r"continue_trip_core\.js'\) }}\?v=[^\"']+",
        "continue_trip_core.js') }}?v=stale-clear-v60b",
        s
    )
    s = re.sub(
        r'continue_trip_core\.js"\) }}\?v=[^"\']+',
        'continue_trip_core.js") }}?v=stale-clear-v60b',
        s
    )

    if s != old:
        p.write_text(s, encoding="utf-8")
        print("✅ Cache kırıldı:", p.relative_to(ROOT))

print()
print("✅ V60B tamam.")
