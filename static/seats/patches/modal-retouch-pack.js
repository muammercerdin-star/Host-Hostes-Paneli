(function(){
  function isVisible(el){
    if(!el) return false;
    const cs = window.getComputedStyle(el);
    return cs.display !== "none" && cs.visibility !== "hidden" && el.offsetHeight > 0;
  }

  function syncModalState(){
    const selectors = [
      ".modal.show",
      ".modal[style*='display: block']",
      ".seat-modal.show",
      ".seat-modal.is-open",
      ".overlay-modal.show",
      ".overlay-card.show"
    ];

    let open = false;
    for(const sel of selectors){
      const found = document.querySelectorAll(sel);
      for(const el of found){
        if(isVisible(el)){
          open = true;
          break;
        }
      }
      if(open) break;
    }

    document.body.classList.toggle("seat-any-modal-open", open);
  }

  const obs = new MutationObserver(function(){
    syncModalState();
  });

  function boot(){
    if(document.body){
      obs.observe(document.body, {
        childList: true,
        subtree: true,
        attributes: true,
        attributeFilter: ["class", "style"]
      });
      syncModalState();
    }
  }

  document.addEventListener("DOMContentLoaded", boot);
  window.addEventListener("load", syncModalState);
  document.addEventListener("click", function(){ setTimeout(syncModalState, 0); }, true);
})();
