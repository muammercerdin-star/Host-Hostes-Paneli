/* =========================================================
   DRIVE ETA CHIP MODULE
   Paneldeki Rötar / ETA bilgisini üst sürüş kutusuna taşır.
========================================================= */

(function(){
  const q = (sel) => document.querySelector(sel);

  function etaClassFromText(text){
    const t = String(text || "").toLocaleLowerCase("tr-TR");

    if(t.includes("erken") || t.includes("zamanında") || t.includes("zamaninda")){
      return "good";
    }

    if(t.includes("rötar") || t.includes("rotar") || t.includes("gecik")){
      return "warn";
    }

    if(t.includes("kritik") || t.includes("çok") || t.includes("cok")){
      return "bad";
    }

    return "neutral";
  }

  function syncDriveEtaChip(){
    const chip = q("#driveEtaChip");
    const main = q("#driveEtaMain");
    const sub = q("#driveEtaSub");

    if(!chip || !main || !sub) return;

    const delayMain = q("#delayMain")?.textContent?.trim() || "";
    const delaySub = q("#delaySub")?.textContent?.trim() || "";
    const target = q("#routeNextTimed")?.textContent?.trim() || "";

    let mainText = delayMain && delayMain !== "—" ? delayMain : "Rötar";
    let subText = delaySub && delaySub !== "—" ? delaySub : "ETA bekleniyor";

    if(target && target !== "—"){
      subText = target + " · " + subText;
    }

    main.textContent = mainText;
    sub.textContent = subText;

    chip.classList.remove("good","warn","bad","neutral");
    chip.classList.add(etaClassFromText(mainText + " " + subText));
  }

  window.syncDriveEtaChip = syncDriveEtaChip;

  function boot(){
    syncDriveEtaChip();
    setInterval(syncDriveEtaChip, 1500);
  }

  if(document.readyState === "loading"){
    document.addEventListener("DOMContentLoaded", boot);
  }else{
    boot();
  }
})();
