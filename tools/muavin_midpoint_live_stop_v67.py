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

V67_FUNCS = r'''
    // MIDPOINT_LIVE_STOP_V67
    // Canlı durak artık "işlem var/yok" veya "6 km geçti" mantığıyla değil,
    // rota koordinatlarına göre en yakın durakla belirlenir.
    // İki durak arasında orta nokta geçilince doğal olarak sonraki durak daha yakın olur.
    let midpointSwitchSigV67 = "";
    let midpointSwitchAtV67 = 0;

    function isEmptyLiveNameV67(name){
      const n = norm(name || "");
      return (
        !n ||
        n.includes("bekleniyor") ||
        n.includes("secilmedi") ||
        n.includes("seçilmedi") ||
        n.includes("durak secilmedi") ||
        n.includes("durak seçilmedi")
      );
    }

    function routeCoordItemsV67(){
      const raw = Array.isArray(BOOT.routeCoords) ? BOOT.routeCoords : [];
      const out = [];

      raw.forEach((item, arrayIndex) => {
        const name = String(item.stop || item.name || "").trim();
        if(!name) return;

        const lat = Number(item.lat ?? item.latitude);
        const lng = Number(item.lng ?? item.lon ?? item.longitude);

        if(!Number.isFinite(lat) || !Number.isFinite(lng)) return;

        let idx = routeIndex(name);
        if(!Number.isFinite(idx) || idx < 0) idx = arrayIndex;

        out.push({
          name,
          lat,
          lng,
          idx,
          arrayIndex
        });
      });

      out.sort((a, b) => {
        if(a.idx !== b.idx) return a.idx - b.idx;
        return a.arrayIndex - b.arrayIndex;
      });

      return out;
    }

    function pickMidpointLiveStopV67(currentName){
      if(!lastPos) return null;

      const items = routeCoordItemsV67();
      if(!items.length) return null;

      const emptyCurrent = isEmptyLiveNameV67(currentName);
      const currentIdx = emptyCurrent ? -1 : routeIndex(currentName);

      let pool = items;

      // Canlı durak belliyse geriye zıplama yapma.
      // Sadece mevcut durak ve önündeki birkaç durağı karşılaştır.
      if(currentIdx >= 0){
        pool = items.filter(x => x.idx >= currentIdx && x.idx <= currentIdx + 6);

        if(!pool.length){
          pool = items.filter(x => x.idx >= currentIdx);
        }

        if(!pool.length){
          pool = items;
        }
      }

      let best = null;

      for(const item of pool){
        const km = distKm(lastPos, { lat:item.lat, lng:item.lng });
        if(!Number.isFinite(km)) continue;

        if(!best || km < best.km){
          best = {
            name:item.name,
            km,
            idx:item.idx
          };
        }
      }

      return best;
    }

    function switchLiveStopMidpointV67(oldName, picked){
      if(!picked || !picked.name) return false;

      const toName = String(picked.name || "").trim();
      const fromName = String(oldName || "").trim();

      if(!toName) return false;
      if(!isEmptyLiveNameV67(fromName) && norm(fromName) === norm(toName)) return false;

      const now = Date.now();
      const sig = `${tripId}|${fromName}|${toName}|${Math.round(Number(picked.km || 0) * 1000)}`;

      if(sig === midpointSwitchSigV67 && now - midpointSwitchAtV67 < 4000){
        return false;
      }

      midpointSwitchSigV67 = sig;
      midpointSwitchAtV67 = now;

      const displaySpeed = liveDisplaySpeed();
      const gpsKm = formatKm(Number(picked.km));

      const url =
        `/api/live-runtime-state?write=1` +
        `&trip_id=${encodeURIComponent(tripId)}` +
        `&live_stop=${encodeURIComponent(toName)}` +
        `&speed=${encodeURIComponent(displaySpeed)}` +
        `&gps_km=${encodeURIComponent(gpsKm || "")}` +
        `&eta_main=` +
        `&eta_sub=${encodeURIComponent("midpoint-live-stop-v67")}` +
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
          if(distEl) distEl.textContent = gpsKm || "—";
          if(etaEl) etaEl.textContent = "—";
        }catch(_){}

        setTimeout(() => {
          try{ location.reload(); }catch(_){}
        }, 350);
      });

      return true;
    }

'''

V67_HOOK = r'''
    // MIDPOINT_LIVE_STOP_V67_HOOK
    const pickedLiveV67 = pickMidpointLiveStopV67(liveName);

    if(pickedLiveV67){
      const mustSwitchV67 =
        isEmptyLiveNameV67(liveName) ||
        norm(pickedLiveV67.name) !== norm(liveName || "");

      if(mustSwitchV67){
        switchLiveStopMidpointV67(liveName || "", pickedLiveV67);
        return;
      }
    }
'''

def backup(p):
    if p.exists():
        b = p.with_name(p.name + f".bak-midpoint-live-v67-{STAMP}")
        shutil.copy2(p, b)
        print("📦 Yedek:", b.relative_to(ROOT))

print("===== MIDPOINT LIVE STOP V67 =====")

for p in FILES:
    if not p.exists():
        print("⚠️ Yok:", p.relative_to(ROOT))
        continue

    backup(p)
    s = p.read_text(encoding="utf-8", errors="ignore")

    # Eski V61/V64/V65 canlı durak değiştirme mantığını temizle
    s = re.sub(
        r'\n\s*// CONTINUE_STALE_LIVE_SWITCH_V61.*?\n\s*function\s+writeRuntime',
        '\n    function writeRuntime',
        s,
        flags=re.S
    )

    s = re.sub(
        r'\n\s*// CONTINUE_WAITING_LIVE_ACQUIRE_V64B.*?\n\s*if\(!liveName\)\s*return;',
        '\n    if(!liveName) return;',
        s,
        flags=re.S
    )

    s = re.sub(
        r'\n\s*// CONTINUE_STALE_LIVE_SWITCH_V61_HOOK.*?\n\s*setText\("#liveDistanceValue",\s*gpsKm\);',
        '\n      setText("#liveDistanceValue", gpsKm);',
        s,
        flags=re.S
    )

    if "MIDPOINT_LIVE_STOP_V67" not in s:
        m = re.search(r'\n\s*function\s+writeRuntime\s*\(', s)
        if not m:
            print("❌ writeRuntime bulunamadı:", p.relative_to(ROOT))
            continue

        s = s[:m.start()] + "\n" + V67_FUNCS.rstrip() + s[m.start():]
        print("✅ V67 orta nokta fonksiyonları eklendi:", p.relative_to(ROOT))
    else:
        print("ℹ️ V67 fonksiyon zaten var:", p.relative_to(ROOT))

    if "MIDPOINT_LIVE_STOP_V67_HOOK" not in s:
        m = re.search(r'const\s+liveName\s*=\s*liveStopName\(\)\s*;', s)
        if not m:
            print("❌ compute liveName satırı bulunamadı:", p.relative_to(ROOT))
            continue

        s = s[:m.end()] + "\n" + V67_HOOK.rstrip() + s[m.end():]
        print("✅ V67 compute hook eklendi:", p.relative_to(ROOT))
    else:
        print("ℹ️ V67 hook zaten var:", p.relative_to(ROOT))

    p.write_text(s, encoding="utf-8")

for p in TPLS:
    if not p.exists():
        print("⚠️ Yok:", p.relative_to(ROOT))
        continue

    backup(p)
    s = p.read_text(encoding="utf-8", errors="ignore")

    s = re.sub(
        r"continue_trip_core\.js'\) }}\?v=[^\"']+",
        "continue_trip_core.js') }}?v=midpoint-live-v67",
        s
    )
    s = re.sub(
        r'continue_trip_core\.js"\) }}\?v=[^"\']+',
        'continue_trip_core.js") }}?v=midpoint-live-v67',
        s
    )

    p.write_text(s, encoding="utf-8")
    print("✅ Cache kırıldı:", p.relative_to(ROOT))

print()
print("✅ V67 tamam. Commit/push yok. Önce tarayıcıda test et.")
