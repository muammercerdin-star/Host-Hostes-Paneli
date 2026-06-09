/* CONTINUE_REFRESH_BUTTON_V49 */
(function(){
  if(window.CONTINUE_REFRESH_BUTTON_V49_READY) return;
  window.CONTINUE_REFRESH_BUTTON_V49_READY = true;

  function ready(fn){
    if(document.readyState === "loading"){
      document.addEventListener("DOMContentLoaded", fn);
    }else{
      fn();
    }
  }

  function hardRefresh(){
    try{
      const url = new URL(window.location.href);
      url.searchParams.set("_refresh", String(Date.now()));
      window.location.replace(url.toString());
    }catch(e){
      window.location.reload();
    }
  }

  ready(function(){
    if(document.getElementById("continueRefreshBtnV49")) return;

    const btn = document.createElement("button");
    btn.type = "button";
    btn.id = "continueRefreshBtnV49";
    btn.className = "continue-refresh-v49-btn";
    btn.setAttribute("aria-label", "Sayfayı yenile");
    btn.setAttribute("title", "Sayfayı yenile");
    btn.innerHTML = '<span class="refresh-ico">↻</span>';

    btn.addEventListener("click", function(e){
      e.preventDefault();
      e.stopPropagation();
      btn.classList.add("is-refreshing");
      hardRefresh();
    }, true);

    document.body.appendChild(btn);
  });
})();
