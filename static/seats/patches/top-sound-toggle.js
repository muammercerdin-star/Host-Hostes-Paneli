(function(){
  if(window.__topSoundToggleLoaded) return;
  window.__topSoundToggleLoaded = true;

  var KEY = "ttsEnabled";

  function q(sel){
    return document.querySelector(sel);
  }

  function fallbackIsEnabled(){
    try{
      return (localStorage.getItem(KEY) ?? "1") === "1";
    }catch(_){
      return true;
    }
  }

  function isEnabled(){
    try{
      if(window.SeatsVoice && typeof window.SeatsVoice.isEnabled === "function"){
        return !!window.SeatsVoice.isEnabled();
      }
    }catch(_){}
    return fallbackIsEnabled();
  }

  function setEnabled(on){
    on = !!on;

    try{
      if(window.SeatsVoice && typeof window.SeatsVoice.setEnabled === "function"){
        window.SeatsVoice.setEnabled(on);
      }else{
        localStorage.setItem(KEY, on ? "1" : "0");
      }
    }catch(_){
      try{ localStorage.setItem(KEY, on ? "1" : "0"); }catch(e){}
    }

    var sound = q("#soundToggle");
    if(sound){
      sound.checked = on;
      try{ sound.dispatchEvent(new Event("change", {bubbles:true})); }catch(_){}
    }

    var tts = q("#ttsToggle");
    if(tts){
      tts.classList.toggle("muted", !on);
      tts.title = on ? "Sesli uyarı açık" : "Sesli uyarı kapalı";
    }

    if(!on){
      try{
        if(window.SeatsVoice && typeof window.SeatsVoice.stop === "function"){
          window.SeatsVoice.stop();
        }else if(window.SeatsStopVoice){
          window.SeatsStopVoice();
        }else if("speechSynthesis" in window){
          speechSynthesis.cancel();
        }
      }catch(_){}
    }

    try{
      window.dispatchEvent(new CustomEvent("ttsEnabledChanged", {detail:{enabled:on}}));
    }catch(_){}

    syncButton();
  }

  function syncButton(){
    var btn = q("#seatSimpleSoundToggle");
    if(!btn) return;

    var on = isEnabled();

    btn.classList.toggle("is-off", !on);
    btn.setAttribute("aria-pressed", on ? "true" : "false");
    btn.title = on ? "Sesli asistan açık" : "Sesli asistan kapalı";
    btn.innerHTML = on
      ? '<span>🔊</span><span>Ses Açık</span>'
      : '<span>🔇</span><span>Sessiz</span>';
  }

  function ensureButton(){
    var modeBtn = q("#seatSimpleModeToggle");
    if(!modeBtn) return;

    var row = q("#seatSimpleTopSoundRow");

    if(!row){
      row = document.createElement("div");
      row.id = "seatSimpleTopSoundRow";
      modeBtn.parentNode.insertBefore(row, modeBtn);
    }

    if(modeBtn.parentNode !== row){
      row.insertBefore(modeBtn, row.firstChild);
    }

    var btn = q("#seatSimpleSoundToggle");

    if(!btn){
      btn = document.createElement("button");
      btn.type = "button";
      btn.id = "seatSimpleSoundToggle";

      btn.addEventListener("click", function(e){
        e.preventDefault();
        e.stopPropagation();

        var next = !isEnabled();
        setEnabled(next);

        if(next && window.SeatsSpeak){
          try{ window.SeatsSpeak("Sesli asistan açık.", {force:true}); }catch(_){}
        }
      });

      row.appendChild(btn);
    }

    syncButton();
  }

  var timer = null;

  function schedule(){
    clearTimeout(timer);
    timer = setTimeout(ensureButton, 80);
  }

  if(document.readyState === "loading"){
    document.addEventListener("DOMContentLoaded", schedule);
  }else{
    schedule();
  }

  window.addEventListener("load", schedule);
  window.addEventListener("resize", schedule);
  window.addEventListener("ttsEnabledChanged", syncButton);

  document.addEventListener("change", function(e){
    if(e.target && e.target.id === "soundToggle"){
      setEnabled(!!e.target.checked);
    }
  }, true);

  var obs = new MutationObserver(schedule);
  obs.observe(document.documentElement, {
    childList:true,
    subtree:true
  });

  setTimeout(ensureButton, 150);
  setTimeout(ensureButton, 600);
  setTimeout(ensureButton, 1400);
})();
