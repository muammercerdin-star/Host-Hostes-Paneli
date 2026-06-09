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

def backup(p):
    if p.exists():
        b = p.with_name(p.name + f".bak-stale-live-clear-v60-{STAMP}")
        shutil.copy2(p, b)
        print("📦 Yedek:", b.relative_to(ROOT))

print("===== CONTINUE STALE LIVE CLEAR V60 =====")

for p in FILES:
    if not p.exists():
        print("⚠️ Yok:", p.relative_to(ROOT))
        continue

    backup(p)
    s = p.read_text(encoding="utf-8", errors="ignore")
    old = s

    if "CONTINUE_STALE_LIVE_CLEAR_V60" in s:
        print("ℹ️ V60 zaten var:", p.relative_to(ROOT))
        continue

    # 1) writeRuntime fonksiyonundan önce clear fonksiyonunu ekle
    marker = "    function writeRuntime(liveName, gpsKm, etaMain){"
    insert = r'''
    // CONTINUE_STALE_LIVE_CLEAR_V60
    // Bu ekran canlı durak seçmez; ama çok uzakta kalmış eski canlı durağı temizler.
    function clearStaleLiveRuntimeV60(liveName, gpsKm){
      const staleName = String(liveName || "").trim();
      if(!staleName) return;

      const key = "continueStaleLiveClearV60:" + tripId + ":" + staleName;

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
        `&eta_main=${encodeURIComponent("")}` +
        `&eta_sub=${encodeURIComponent("continue-stale-live-clear-v60")}` +
        `&_=${Date.now()}`;

      fetch(url, {
        method:"GET",
        credentials:"same-origin",
        cache:"no-store"
      })
      .finally(() => {
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
    if marker in s:
        s = s.replace(marker, insert + marker, 1)
        print("✅ clearStaleLiveRuntimeV60 eklendi:", p.relative_to(ROOT))
    else:
        print("❌ writeRuntime marker bulunamadı:", p.relative_to(ROOT))
        continue

    # 2) compute içinde liveKm hesaplandığı yere uzaklık kontrolü ekle
    target = '''      if(liveCoord){
        const liveKm = distKm(lastPos, liveCoord);
        gpsKm = formatKm(liveKm);
        setText("#liveDistanceValue", gpsKm);
      }
'''
    repl = '''      if(liveCoord){
        const liveKm = distKm(lastPos, liveCoord);
        gpsKm = formatKm(liveKm);
        setText("#liveDistanceValue", gpsKm);

        // CONTINUE_STALE_LIVE_CLEAR_V60
        // Eski canlı durak 6 km'den fazla uzaktaysa bu ekran onu seçmez, sadece temizler.
        if(Number.isFinite(liveKm) && liveKm > 6){
          clearStaleLiveRuntimeV60(liveName, gpsKm);
          return;
        }
      }
'''
    if target in s:
        s = s.replace(target, repl, 1)
        print("✅ compute içine 6 km stale kontrolü eklendi:", p.relative_to(ROOT))
    else:
        print("❌ liveCoord bloğu bulunamadı:", p.relative_to(ROOT))

    p.write_text(s, encoding="utf-8")

# 3) cache kır
for p in TPLS:
    if not p.exists():
        print("⚠️ Yok:", p.relative_to(ROOT))
        continue

    backup(p)
    s = p.read_text(encoding="utf-8", errors="ignore")
    old = s

    s = re.sub(
        r"continue_trip_core\.js'\) }}\?v=[^\"']+",
        "continue_trip_core.js') }}?v=stale-clear-v60",
        s
    )
    s = re.sub(
        r'continue_trip_core\.js"\) }}\?v=[^"\']+',
        'continue_trip_core.js") }}?v=stale-clear-v60',
        s
    )

    if s != old:
        p.write_text(s, encoding="utf-8")
        print("✅ Cache kırıldı:", p.relative_to(ROOT))
    else:
        print("ℹ️ Template değişmedi:", p.relative_to(ROOT))

print()
print("✅ V60 tamam. Commit/push yok. Önce tarayıcıda test et.")
