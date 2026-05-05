
/* =========================================================
   HIZLI KOLTUK → OTOMATİK SÜRÜŞ MODU
   /seats?drive=1 ile gelirse sürüş modunu açar
========================================================= */
(function autoOpenDriveModeFromUrl(){
  try{
    const params = new URLSearchParams(window.location.search);
    const drive = params.get("drive");

    if(drive !== "1") return;

    const boot = window.SEATS_BOOT || {};
    const tripKey = window.BAG_TRIP || boot.tripKey || "default";
    const key = "driveMode:" + tripKey;

    localStorage.setItem(key, "1");
    document.body.classList.add("drive-mode");

    setTimeout(() => {
      try{
        if(typeof renderRouteStrip === "function") renderRouteStrip();
        if(typeof updateCompactHeader === "function") updateCompactHeader();
      }catch(_){}
    }, 120);

    // Adres çubuğundan ?drive=1 temizle, ama mod açık kalsın
    if(window.history && window.history.replaceState){
      const cleanUrl = window.location.pathname;
      window.history.replaceState({}, document.title, cleanUrl);
    }
  }catch(e){
    console.warn("Hızlı koltuk sürüş modu açılamadı:", e);
  }
})();

/* =========================================================
   DRIVE CONTROLS
   Sürüş modu + hız kutusu + ses açık/sessiz
   Butonlar HTML'de sabit, JS sadece çalıştırır
========================================================= */

(function(){
  const boot = window.SEATS_BOOT || {};
  const tripKey = window.BAG_TRIP || boot.tripKey || "default";

  const DRIVE_MODE_KEY = "driveMode:" + tripKey;
  const VOICE_SOUND_KEY = "voiceSoundEnabled:" + tripKey;

  function safeToast(msg, ms=1600){
    try{
      if(typeof toast === "function") toast(msg, ms);
    }catch(_){}
  }

  function safeSpeak(msg){
    try{
      if(window.SeatsSpeak){
        window.SeatsSpeak(msg, { force:true });
        return;
      }

      if(typeof speak === "function") speak(msg);
    }catch(_){}
  }

  function getLiveStop(){
    try{
      if(typeof getDisplayLiveStop === "function"){
        return getDisplayLiveStop() || "";
      }
    }catch(_){}

    try{
      return speedState?.liveStop || "";
    }catch(_){}

    return "";
  }

  function getSpeedLimitData(){
    let speed = 0;
    let limit = 0;

    try{
      speed = Math.round(Number(speedState?.current || 0));
      limit = Number(speedState?.lastLimitValue || speedState?.lastLimitObj?.limit || 0);
    }catch(_){}

    return { speed, limit };
  }

  function isDriveOn(){
    return localStorage.getItem(DRIVE_MODE_KEY) === "1";
  }

  function syncDriveMode(){
    const btn = document.getElementById("driveModeToggle");
    const on = isDriveOn();

    document.body.classList.toggle("drive-mode", on);
    document.documentElement.classList.toggle("drive-mode", on);

    if(btn){
      btn.innerHTML = on ? "↩ Normal" : "🚘 Sürüş";
      btn.title = on ? "Normal moda geç" : "Sürüş moduna geç";
      btn.setAttribute("aria-pressed", on ? "true" : "false");
    }

    try{
      if(typeof renderRouteStrip === "function") renderRouteStrip();
      if(typeof updateCompactHeader === "function") updateCompactHeader();
      if(typeof syncDriveEtaChip === "function") syncDriveEtaChip();
    }catch(_){}

    try{
      window.dispatchEvent(new CustomEvent("driveModeChanged", {
        detail:{ on }
      }));
    }catch(_){}
  }

  function bindDriveMode(){
    const btn = document.getElementById("driveModeToggle");
    if(!btn) return;

    if(btn.dataset.driveBound === "1"){
      syncDriveMode();
      return;
    }

    btn.dataset.driveBound = "1";

    btn.addEventListener("click", (e) => {
      e.preventDefault();

      const next = !isDriveOn();
      localStorage.setItem(DRIVE_MODE_KEY, next ? "1" : "0");

      syncDriveMode();

      setTimeout(syncDriveMode, 80);
      setTimeout(syncDriveMode, 250);
    });

    syncDriveMode();
  }

  function updateDriveSpeedChip(){
    const el = document.getElementById("driveSpeedChip");
    if(!el) return;

    const { speed, limit } = getSpeedLimitData();
    const liveStop = getLiveStop();

    let cls = "neutral";
    if(limit > 0){
      if(speed <= limit) cls = "ok";
      else if(speed <= limit + 10) cls = "warn";
      else cls = "bad";
    }

    el.className = "drive-speed-chip " + cls;

    const limitText = limit > 0 ? `Limit: ${limit}` : "Limit: —";
    const stopText = liveStop ? ` · ${liveStop}` : "";

    el.innerHTML = `
      <div class="drive-speed-top">
        <span class="drive-speed-ico">🚦</span>
        <b>${speed}</b>
        <span>km/h</span>
      </div>
      <div class="drive-speed-sub">${limitText}${stopText}</div>
    `;
  }

  function getVoiceEnabled(){
    try{
      if(window.SeatsVoice && typeof window.SeatsVoice.isEnabled === "function"){
        return window.SeatsVoice.isEnabled();
      }
    }catch(_){}

    const saved = localStorage.getItem("ttsEnabled");
    if(saved !== null) return saved === "1";

    const cb = document.getElementById("soundToggle");
    if(cb) return cb.checked !== false;

    return true;
  }

  function updateNightVoiceToggle(){
    try{
      if(window.SeatsVoice && typeof window.SeatsVoice.syncButtons === "function"){
        window.SeatsVoice.syncButtons();
        return;
      }
    }catch(_){}

    const btn = document.getElementById("nightVoiceToggle");
    if(!btn) return;

    const on = getVoiceEnabled();

    btn.classList.toggle("is-off", !on);
    btn.innerHTML = on
      ? `<span class="nv-ico">🔊</span><span>Ses Açık</span>`
      : `<span class="nv-ico">🔇</span><span>Sessiz</span>`;

    btn.title = on
      ? "Sesli robot açık. Kapatmak için dokun."
      : "Sesli robot kapalı. Açmak için dokun.";
  }

  function setVoiceEnabled(on, opts={}){
    const enabled = !!on;

    try{
      if(window.SeatsVoice && typeof window.SeatsVoice.setEnabled === "function"){
        window.SeatsVoice.setEnabled(enabled);
      }else{
        localStorage.setItem("ttsEnabled", enabled ? "1" : "0");
      }
    }catch(_){
      localStorage.setItem("ttsEnabled", enabled ? "1" : "0");
    }

    const cb = document.getElementById("soundToggle");
    if(cb) cb.checked = enabled;

    updateNightVoiceToggle();

    if(!opts.silent){
      safeToast(enabled ? "Sesli robot açıldı" : "Sesli robot kapatıldı", 1600);
    }

    if(enabled && opts.announce){
      setTimeout(() => safeSpeak("Sesli robot açık."), 80);
    }
  }){
    const enabled = !!on;

    localStorage.setItem(VOICE_SOUND_KEY, enabled ? "1" : "0");

    const cb = document.getElementById("soundToggle");
    if(cb) cb.checked = enabled;

    updateNightVoiceToggle();

    if(!opts.silent){
      safeToast(enabled ? "Sesli robot açıldı" : "Sesli robot kapatıldı", 1600);
    }

    if(enabled && opts.announce){
      setTimeout(() => safeSpeak("Sesli robot açık."), 80);
    }
  }

  function bindNightVoiceToggle(){
    const cb = document.getElementById("soundToggle");

    if(cb){
      cb.checked = getVoiceEnabled();

      if(cb.dataset.voiceBound !== "1"){
        cb.dataset.voiceBound = "1";
        cb.addEventListener("change", () => {
          setVoiceEnabled(cb.checked, { silent:true });
        });
      }
    }

    /*
      #nightVoiceToggle butonunun tek sahibi voice-tts.js.
      Burada click event bağlamıyoruz; çift yönetim bozulma yapıyordu.
    */
    updateNightVoiceToggle();
  }

  function bootDriveControls(){
    bindDriveMode();
    bindNightVoiceToggle();
    updateDriveSpeedChip();
  }

  bootDriveControls();

  window.addEventListener("load", bootDriveControls);
  window.addEventListener("resize", bootDriveControls);

  setTimeout(bootDriveControls, 400);
  setTimeout(bootDriveControls, 1200);

  setInterval(updateDriveSpeedChip, 1000);

  window.DriveControls = {
    boot: bootDriveControls,
    updateSpeed: updateDriveSpeedChip,
    setVoiceEnabled
  };
})();
