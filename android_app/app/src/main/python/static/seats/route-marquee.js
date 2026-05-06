/* =========================================================
   ROUTE MINI CLEAN TICKER SINGLE
   Durak metnini data-marquee-text içine kopyalar.
========================================================= */

(function(){
  function setupOne(id){
    const el = document.getElementById(id);
    if(!el) return;

    const text = String(el.textContent || "").trim();
    el.setAttribute("data-marquee-text", text);
  }

  function refresh(){
    setupOne("routeMiniLive");
    setupOne("routeMiniNext");
  }

  window.refreshRouteMarquee = refresh;

  function boot(){
    refresh();

    ["routeMiniLive", "routeMiniNext"].forEach(id => {
      const el = document.getElementById(id);
      if(!el) return;

      new MutationObserver(refresh).observe(el, {
        childList:true,
        characterData:true,
        subtree:true
      });
    });

    setTimeout(refresh, 300);
    setTimeout(refresh, 1000);
  }

  if(document.readyState === "loading"){
    document.addEventListener("DOMContentLoaded", boot);
  }else{
    boot();
  }
})();
