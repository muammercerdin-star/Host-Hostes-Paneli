/* =========================================================
   continue_bag_emanet.js
   Bagaj / emanet görünüm yöneticisi
   Not: Bagaj sayısını artık 500 ms'de bir zorla ezmez.
========================================================= */

(function(){
  function boot(){
    return window.CONTINUE_BOOT || {};
  }

  function numberValue(v, fallback){
    const n = Number(v);
    return Number.isFinite(n) ? n : Number(fallback || 0);
  }

  function getBagValue(data){
    const b = boot();

    if(data && data.seat_bag_count !== undefined) return numberValue(data.seat_bag_count, 0);
    if(data && data.bagaj_count !== undefined) return numberValue(data.bagaj_count, 0);
    if(data && data.liveBagajCount !== undefined) return numberValue(data.liveBagajCount, 0);

    return numberValue(b.liveBagajCount, 0);
  }

  function getEmanetValue(data){
    const b = boot();

    if(data && data.emanet_count !== undefined) return numberValue(data.emanet_count, 0);
    if(data && data.consignment_count !== undefined) return numberValue(data.consignment_count, 0);
    if(data && data.liveEmanetCount !== undefined) return numberValue(data.liveEmanetCount, 0);

    return numberValue(b.liveEmanetCount, 0);
  }

  function ensureMini(metric){
    if(!metric) return null;

    let mini = document.getElementById("liveEmanetMini");

    if(!mini){
      mini = document.createElement("span");
      mini.id = "liveEmanetMini";
      metric.appendChild(mini);
    }

    return mini;
  }

  function removeOldMiniDuplicates(metric){
    if(!metric) return;

    Array.from(metric.querySelectorAll("*")).forEach(el => {
      if(el.id === "liveEmanetMini") return;

      const txt = (el.textContent || "").trim();
      if(/^\+\s*\d+\s*emanet$/i.test(txt)){
        el.remove();
      }
    });
  }

  function apply(data){
    const metric = document.getElementById("liveBagajMetric");
    const bagEl = document.getElementById("liveBagajCount");

    const bag = Math.max(0, getBagValue(data));
    const emanet = Math.max(0, getEmanetValue(data));

    if(bagEl){
      bagEl.textContent = String(bag);
      bagEl.dataset.bagCount = String(bag);
      bagEl.dataset.emanetCount = String(emanet);
    }

    if(metric){
      metric.classList.toggle("has-work", (bag + emanet) > 0);
      metric.classList.toggle("is-empty", (bag + emanet) <= 0);
      removeOldMiniDuplicates(metric);
    }

    const mini = ensureMini(metric);

    if(mini){
      if(emanet > 0){
        mini.textContent = "+" + emanet + " emanet";
        mini.style.display = "inline-flex";
      }else{
        mini.textContent = "";
        mini.style.display = "none";
      }
    }
  }

  window.ContinueBagEmanet = {
    apply
  };

  function applyBoot(){
    apply({
      liveBagajCount: boot().liveBagajCount,
      liveEmanetCount: boot().liveEmanetCount
    });
  }

  if(document.readyState === "loading"){
    document.addEventListener("DOMContentLoaded", applyBoot);
  }else{
    applyBoot();
  }

  /*
    İleride canlı refresh tekrar gelirse bu event ile çakışmadan güncellenir.
    Eski hard-fix gibi sürekli eski değere zorlamaz.
  */
  document.addEventListener("continueLiveFlowUpdated", function(e){
    const detail = e && e.detail ? e.detail : {};
    const current = detail.current || detail;

    apply({
      seat_bag_count: current.seat_bag_count,
      bagaj_count: current.bagaj_count,
      emanet_count: current.emanet_count,
      consignment_count: current.consignment_count
    });
  });
})();
