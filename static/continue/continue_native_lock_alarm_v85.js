/* CONTINUE_NATIVE_LOCK_ALARM_V86
   WebView -> Android kilit ekranı alarm servisi.
   V82 kuralı: canlı durak GPS ile değişmez.
   V86: Koordinat eşleşmese bile takip bildirimi başlatılır.
*/
(function(){
  if(window.CONTINUE_NATIVE_LOCK_ALARM_V86_READY) return;
  window.CONTINUE_NATIVE_LOCK_ALARM_V86_READY = true;

  const BOOT = window.CONTINUE_BOOT || {};
  const tripId = String(BOOT.tripId || BOOT.trip_id || "active");
  const routeCoords = Array.isArray(BOOT.routeCoords) ? BOOT.routeCoords : [];

  let started = false;
  let lastSig = "";

  function clean(v){
    return String(v == null ? "" : v).replace(/\s+/g, " ").trim();
  }

  function norm(v){
    return clean(v).toLocaleLowerCase("tr-TR");
  }

  function numFromText(v){
    const m = clean(v).match(/\d+/);
    return m ? Number(m[0]) : 0;
  }

  function currentStop(){
    const el = document.getElementById("liveCurrentStopName");
    return clean(el && el.textContent);
  }

  function offloadCount(){
    const el = document.getElementById("liveOffloadCount");
    return numFromText(el && el.textContent);
  }

  function bagCount(){
    const selectors = [
      "#liveBagajCount",
      "#liveBagCount",
      "#liveBagajMetric",
      "#liveBagMetric",
      "[data-live-bag-count]"
    ];

    for(const sel of selectors){
      const el = document.querySelector(sel);
      if(el){
        const n = numFromText(el.textContent);
        if(Number.isFinite(n)) return n;
      }
    }

    return 0;
  }

  function findCoord(stop){
    const key = norm(stop);
    if(!key) return null;

    for(const item of routeCoords){
      const name = clean(item.stop || item.name || item.title || item.durak || "");
      if(norm(name) !== key) continue;

      const lat = Number(item.lat ?? item.latitude ?? item.enlem);
      const lng = Number(item.lng ?? item.lon ?? item.longitude ?? item.boylam);

      if(Number.isFinite(lat) && Number.isFinite(lng)){
        return { lat, lng };
      }
    }

    return null;
  }

  function sync(){
    try{
      if(!window.AndroidLockAlarm) return;

      const stop = currentStop();
      if(!stop) return;

      const off = offloadCount();
      const bag = bagCount();
      const c = findCoord(stop);

      const sig = [tripId, stop, c ? c.lat : "NO_LAT", c ? c.lng : "NO_LNG", off, bag].join("|");

      if(sig !== lastSig){
        lastSig = sig;

        window.AndroidLockAlarm.updateTarget(
          tripId,
          stop,
          c ? String(c.lat) : "",
          c ? String(c.lng) : "",
          String(off),
          String(bag)
        );
      }

      // V86: Koordinat yoksa bile servis başlasın, bildirim kanalı canlansın.
      if(!started){
        started = true;
        window.AndroidLockAlarm.start();
      }

    }catch(err){
      console.warn("CONTINUE_NATIVE_LOCK_ALARM_V86 sync error", err);
    }
  }

  window.continueNativeLockAlarmV86 = {
    sync,
    stopAlarm(){
      try{ if(window.AndroidLockAlarm) window.AndroidLockAlarm.stopAlarm(); }catch(_){}
    },
    stopService(){
      try{ if(window.AndroidLockAlarm) window.AndroidLockAlarm.stopService(); }catch(_){}
    },
    reset(){
      try{ if(window.AndroidLockAlarm) window.AndroidLockAlarm.reset(); }catch(_){}
    }
  };

  if(document.readyState === "loading"){
    document.addEventListener("DOMContentLoaded", sync);
  }else{
    sync();
  }

  setTimeout(sync, 800);
  setTimeout(sync, 2000);
  setInterval(sync, 3000);

  if(window.MutationObserver){
    const targets = [
      document.getElementById("liveCurrentStopName"),
      document.getElementById("liveOffloadCount"),
      document.getElementById("liveBagajCount"),
      document.getElementById("liveBagajMetric")
    ].filter(Boolean);

    const obs = new MutationObserver(sync);
    targets.forEach(el => obs.observe(el, { childList:true, characterData:true, subtree:true }));
  }
})();
