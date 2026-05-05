/* =========================================================
   SEATS UNIFIED VOICE MODULE
   Tüm ses çıkışlarını tek merkezden yönetir.
   Tarayıcıda speechSynthesis, APK’da AndroidTTS kullanır.
========================================================= */

(function(){
  if(window.__SeatsVoiceUnifiedReady) return;
  window.__SeatsVoiceUnifiedReady = true;

  const KEY = "ttsEnabled";

  function isEnabled(){
    try{
      return (localStorage.getItem(KEY) ?? "1") === "1";
    }catch(e){
      return true;
    }
  }

  function setEnabled(value){
    try{
      localStorage.setItem(KEY, value ? "1" : "0");
    }catch(e){}
    syncButtons();
  }

  function stop(){
    if(window.AndroidTTS && typeof window.AndroidTTS.stop === "function"){
      try{ window.AndroidTTS.stop(); }catch(e){}
    }

    try{
      if("speechSynthesis" in window) speechSynthesis.cancel();
    }catch(e){}
  }

  function speak(text, opts = {}){
    const msg = String(text || "").trim();
    if(!msg) return;

    if(!opts.force && !isEnabled()) return;

    if(window.AndroidTTS && typeof window.AndroidTTS.speak === "function"){
      try{
        window.AndroidTTS.speak(msg);
        return;
      }catch(e){
        console.warn("AndroidTTS hata:", e);
      }
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
    }catch(e){
      console.warn("speechSynthesis hata:", e);
    }
  }

  function syncButtons(){
    const on = isEnabled();

    const nightBtn = document.getElementById("nightVoiceToggle");
    if(nightBtn){
      nightBtn.classList.toggle("is-off", !on);
      nightBtn.dataset.voiceOn = on ? "1" : "0";
      nightBtn.title = on ? "Durak akışı sesi açık" : "Durak akışı sesi kapalı";
      nightBtn.innerHTML = on
        ? '<span class="nv-ico">🔊</span><span>Ses Açık</span>'
        : '<span class="nv-ico">🔇</span><span>Sessiz</span>';
    }

    const ttsBtn = document.getElementById("ttsToggle");
    if(ttsBtn){
      ttsBtn.classList.toggle("muted", !on);
      ttsBtn.title = on ? "Sesli uyarı açık" : "Sesli uyarı kapalı";
    }
  }

  function cleanText(x){
    return String(x || "")
      .replace(/\s+/g, " ")
      .trim();
  }

  // Dışarıya tek merkez olarak aç
  window.SeatsSpeak = speak;
  window.SeatsStopVoice = stop;
  window.SeatsVoice = {
    speak,
    stop,
    isEnabled,
    setEnabled,
    syncButtons
  };

  // Durak Akışı kartlarına doğrudan ses desteği
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
            speak(stopHumanVoiceSummary(stop));
          }else{
            speak(stop + " seçildi.");
          }
        }catch(_){
          speak(stop + " seçildi.");
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
          speak("Canlı durak " + live + ".");
        }
        return;
      }

      if(nextEl){
        const next = cleanText(nextEl.textContent);
        if(next && next !== "—" && next !== "-"){
          speak("Sıradaki durak " + next + ".");
        }
        return;
      }
    }
  }, true);

  // Yeşil Ses Açık / Sessiz butonu
  document.addEventListener("click", function(e){
    const btn = e.target.closest && e.target.closest("#nightVoiceToggle");
    if(!btn) return;

    e.preventDefault();
    e.stopPropagation();

    const next = !isEnabled();
    setEnabled(next);

    if(next){
      speak("Durak akışı sesi açık.", { force:true });
    }else{
      stop();
    }
  }, false);

  function boot(){
    syncButtons();

    let n = 0;
    const timer = setInterval(function(){
      syncButtons();
      n++;
      if(n >= 4) clearInterval(timer);
    }, 500);
  }

  if(document.readyState === "loading"){
    document.addEventListener("DOMContentLoaded", boot);
  }else{
    boot();
  }
})();
