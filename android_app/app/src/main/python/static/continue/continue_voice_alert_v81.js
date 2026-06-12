
/* CONTINUE_VOICE_ALERT_V81
   Tek uyarı:
   "{Durak} durağına 2 kilometre kaldı. İnecek yolcu yok."
   veya
   "{Durak} durağına 2 kilometre kaldı. 3 yolcu inecek."
*/
(function(){
  if(window.CONTINUE_VOICE_ALERT_V81_READY) return;
  window.CONTINUE_VOICE_ALERT_V81_READY = true;

  const BOOT = window.CONTINUE_BOOT || {};
  const tripId = BOOT.tripId || BOOT.trip_id || "active";
  const ENABLE_KEY = "continueVoiceAlertV81:enabled";

  if(localStorage.getItem(ENABLE_KEY) === null){
    localStorage.setItem(ENABLE_KEY, "1");
  }

  function cleanText(v){
    return String(v == null ? "" : v)
      .replace(/\s+/g, " ")
      .trim();
  }

  function getText(selectors){
    for(const sel of selectors){
      const el = document.querySelector(sel);
      const t = cleanText(el && el.textContent);
      if(t) return t;
    }
    return "";
  }

  function currentStopName(){
    let stop = getText([
      "#liveCurrentStopName",
      "[data-live-current-stop]",
      ".live-current-stop-name",
      ".current-stop-name",
      ".live-stop-name",
      ".stop-title"
    ]);

    if(stop) return stop;

    const body = cleanText(document.body && document.body.textContent);
    const m = body.match(/CANLI\s+([A-ZÇĞİÖŞÜa-zçğıöşü0-9 .'-]{2,40})\s+Kalan mesafe/i);
    return m ? cleanText(m[1]) : "";
  }

  function distanceText(){
    let t = getText([
      "#liveDistanceValue",
      "[data-live-distance]",
      ".live-distance-value",
      ".current-distance",
      ".stop-distance-value"
    ]);

    if(t) return t;

    const body = cleanText(document.body && document.body.textContent);
    const m = body.match(/Kalan mesafe[:\s]+([0-9.,]+)\s*(km|m|metre|kilometre)/i);
    return m ? `${m[1]} ${m[2]}` : "";
  }

  function parseKm(t){
    t = cleanText(t).replace(",", ".");
    if(!t) return NaN;

    const m = t.match(/([0-9]+(?:\.[0-9]+)?)/);
    if(!m) return NaN;

    const n = Number(m[1]);
    if(!Number.isFinite(n)) return NaN;

    if(/\b(m|metre)\b/i.test(t) && !/\bkm\b/i.test(t)){
      return n / 1000;
    }

    return n;
  }

  function offloadCount(){
    let t = getText([
      "#liveOffloadCount",
      "[data-live-offload-count]",
      ".live-offload-count",
      ".offload-count"
    ]);

    let m = t.match(/\d+/);
    if(m) return Number(m[0]);

    const body = cleanText(document.body && document.body.textContent);
    m = body.match(/([0-9]+)\s*yolcu\s*İNECEK/i) || body.match(/İNECEK\s*([0-9]+)/i);
    return m ? Number(m[1]) : 0;
  }

  function speakTr(msg){
    msg = cleanText(msg);
    if(!msg) return;

    try{
      if(window.speechSynthesis){
        window.speechSynthesis.cancel();

        const u = new SpeechSynthesisUtterance(msg);
        u.lang = "tr-TR";
        u.rate = 0.95;
        u.pitch = 1;
        u.volume = 1;

        window.speechSynthesis.speak(u);
        return;
      }
    }catch(err){
      console.warn("voice alert speak error", err);
    }

    try{
      if(window.Android && typeof window.Android.speak === "function"){
        window.Android.speak(msg);
      }
    }catch(err){}
  }

  function storageKey(stop){
    return "continueVoiceAlertV81:" + tripId + ":" + stop.toLocaleLowerCase("tr-TR") + ":2km";
  }

  function check(){
    if(localStorage.getItem(ENABLE_KEY) !== "1") return;

    const stop = currentStopName();
    if(!stop) return;

    const km = parseKm(distanceText());
    if(!Number.isFinite(km)) return;

    /*
      Tek kademe:
      2 km ve altına düşünce 1 kere konuşur.
    */
    if(km > 2.05) return;

    const key = storageKey(stop);
    if(localStorage.getItem(key) === "1") return;

    const count = offloadCount();

    const msg = count > 0
      ? `${stop} durağına 2 kilometre kaldı. ${count} yolcu inecek.`
      : `${stop} durağına 2 kilometre kaldı. İnecek yolcu yok.`;

    localStorage.setItem(key, "1");
    speakTr(msg);
  }

  window.continueVoiceAlertV81 = {
    check,
    enable(){
      localStorage.setItem(ENABLE_KEY, "1");
    },
    disable(){
      localStorage.setItem(ENABLE_KEY, "0");
    },
    resetForTest(){
      Object.keys(localStorage).forEach(k => {
        if(k.startsWith("continueVoiceAlertV81:" + tripId + ":")){
          localStorage.removeItem(k);
        }
      });
    }
  };

  setTimeout(check, 1200);
  setInterval(check, 2500);
})();
