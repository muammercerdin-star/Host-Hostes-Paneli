/* =========================================================
   VOICE / TTS MODULE
   Durak akışı sesi, AndroidTTS köprüsü ve Ses Açık/Sessiz butonu.
========================================================= */

(function(){
  function routeDirectTtsEnabled(){
    try{
      return (localStorage.getItem("ttsEnabled") ?? "1") === "1";
    }catch(e){
      return true;
    }
  }

  function speakRouteDirect(text){
    const msg = String(text || "").trim();
    if(!msg || !routeDirectTtsEnabled()) return;

    if(window.AndroidTTS && typeof window.AndroidTTS.speak === "function"){
      try{
        window.AndroidTTS.speak(msg);
        return;
      }catch(e){
        console.warn("AndroidTTS route direct hata:", e);
      }
    }

    try{
      if(!("speechSynthesis" in window)) return;

      window.speechSynthesis.cancel();

      const u = new SpeechSynthesisUtterance(msg);
      u.lang = "tr-TR";
      u.rate = 0.95;
      u.pitch = 1;

      const voices = speechSynthesis.getVoices ? speechSynthesis.getVoices() : [];
      const trVoice = voices.find(v =>
        String(v.lang || "").toLowerCase().startsWith("tr") ||
        String(v.name || "").toLowerCase().includes("turk")
      );

      if(trVoice) u.voice = trVoice;

      speechSynthesis.speak(u);
    }catch(e){
      console.warn("route direct speech hata:", e);
    }
  }

  function cleanText(x){
    return String(x || "")
      .replace(/\s+/g, " ")
      .trim();
  }

  document.addEventListener("click", function(e){
    const routeStop = e.target.closest && e.target.closest(".route-stop");

    if(routeStop){
      const stopName =
        routeStop.dataset.stop ||
        routeStop.querySelector(".name")?.textContent ||
        "";

      const stop = cleanText(stopName);

      if(stop && stop !== "Rota hazırlanıyor"){
        try{
          if(typeof stopHumanVoiceSummary === "function"){
            speakRouteDirect(stopHumanVoiceSummary(stop));
          }else{
            speakRouteDirect(stop + " seçildi.");
          }
        }catch(_){
          speakRouteDirect(stop + " seçildi.");
        }
      }

      return;
    }

    const livePill = e.target.closest && e.target.closest(".route-pill");

    if(livePill){
      const liveEl = livePill.querySelector("#routeMiniLive");
      const nextEl = livePill.querySelector("#routeMiniNext");

      if(liveEl){
        const live = cleanText(liveEl.textContent);

        if(live && live !== "—" && live !== "-"){
          speakRouteDirect("Canlı durak " + live + ".");
        }

        return;
      }

      if(nextEl){
        const next = cleanText(nextEl.textContent);

        if(next && next !== "—" && next !== "-"){
          speakRouteDirect("Sıradaki durak " + next + ".");
        }

        return;
      }
    }
  }, true);
})();


/* =========================================================
   NIGHT VOICE SAFE BIND
   Durak Akışı ses butonunu güvenli şekilde bağlar.
========================================================= */

(function(){
  if(window.__nightVoiceSafeBind) return;
  window.__nightVoiceSafeBind = true;

  const KEY = "ttsEnabled";

  function isOn(){
    try{
      return (localStorage.getItem(KEY) ?? "1") === "1";
    }catch(e){
      return true;
    }
  }

  function setOn(value){
    try{
      localStorage.setItem(KEY, value ? "1" : "0");
    }catch(e){}
  }

  function speakTest(text){
    const msg = String(text || "").trim();
    if(!msg) return;

    if(window.AndroidTTS && typeof window.AndroidTTS.speak === "function"){
      try{
        window.AndroidTTS.speak(msg);
        return;
      }catch(e){}
    }

    try{
      if(!("speechSynthesis" in window)) return;

      speechSynthesis.cancel();

      const u = new SpeechSynthesisUtterance(msg);
      u.lang = "tr-TR";
      u.rate = 0.95;
      u.pitch = 1;

      const voices = speechSynthesis.getVoices ? speechSynthesis.getVoices() : [];
      const trVoice = voices.find(v =>
        String(v.lang || "").toLowerCase().startsWith("tr") ||
        String(v.name || "").toLowerCase().includes("turk")
      );

      if(trVoice) u.voice = trVoice;

      speechSynthesis.speak(u);
    }catch(e){}
  }

  function stopVoice(){
    if(window.AndroidTTS && typeof window.AndroidTTS.stop === "function"){
      try{ window.AndroidTTS.stop(); }catch(e){}
    }

    try{
      if("speechSynthesis" in window) speechSynthesis.cancel();
    }catch(e){}
  }

  function syncNightButton(){
    const btn = document.getElementById("nightVoiceToggle");
    if(!btn) return;

    const on = isOn();

    btn.classList.toggle("is-off", !on);
    btn.dataset.voiceOn = on ? "1" : "0";
    btn.title = on ? "Durak akışı sesi açık" : "Durak akışı sesi kapalı";

    btn.innerHTML = on
      ? '<span class="nv-ico">🔊</span><span>Ses Açık</span>'
      : '<span class="nv-ico">🔇</span><span>Sessiz</span>';
  }

  document.addEventListener("click", function(e){
    const btn = e.target.closest && e.target.closest("#nightVoiceToggle");
    if(!btn) return;

    e.preventDefault();
    e.stopPropagation();

    const next = !isOn();
    setOn(next);
    syncNightButton();

    const ttsBtn = document.getElementById("ttsToggle");
    if(ttsBtn){
      ttsBtn.classList.toggle("muted", !next);
      ttsBtn.title = next ? "Sesli uyarı açık" : "Sesli uyarı kapalı";
    }

    if(next){
      speakTest("Durak akışı sesi açık.");
    }else{
      stopVoice();
    }
  }, false);

  function boot(){
    syncNightButton();

    let n = 0;
    const timer = setInterval(function(){
      syncNightButton();
      n++;
      if(n >= 6) clearInterval(timer);
    }, 500);
  }

  if(document.readyState === "loading"){
    document.addEventListener("DOMContentLoaded", boot);
  }else{
    boot();
  }
})();
