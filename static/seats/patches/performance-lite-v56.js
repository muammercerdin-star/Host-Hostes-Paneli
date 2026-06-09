/* MUAVIN_PERFORMANCE_LITE_V56 */
(function(){
  if(window.__MUAVIN_PERFORMANCE_LITE_V56__) return;
  window.__MUAVIN_PERFORMANCE_LITE_V56__ = true;

  // GPS callback çok sık gelirse ana thread’i boğmasın.
  try{
    if(navigator.geolocation && navigator.geolocation.watchPosition && !navigator.geolocation.__muavinLiteWrappedV56){
      const originalWatch = navigator.geolocation.watchPosition.bind(navigator.geolocation);

      navigator.geolocation.watchPosition = function(success, error, options){
        const opt = Object.assign({}, options || {});
        opt.enableHighAccuracy = false;
        opt.maximumAge = Math.max(Number(opt.maximumAge || 0), 10000);
        opt.timeout = Math.max(Number(opt.timeout || 0), 18000);

        let lastRun = 0;
        let lastPos = null;
        let timer = null;

        function run(pos){
          const now = Date.now();
          const gap = 5000;

          if(now - lastRun >= gap){
            lastRun = now;
            success(pos);
            return;
          }

          lastPos = pos;

          if(!timer){
            timer = setTimeout(function(){
              timer = null;
              if(lastPos){
                const p = lastPos;
                lastPos = null;
                lastRun = Date.now();
                success(p);
              }
            }, gap - (now - lastRun));
          }
        }

        return originalWatch(run, error, opt);
      };

      navigator.geolocation.__muavinLiteWrappedV56 = true;
    }
  }catch(e){}

  // Arka arkaya tıklamada kullanıcıya anlık his ver.
  document.addEventListener("pointerdown", function(e){
    const el = e.target && e.target.closest
      ? e.target.closest("button,a,.seat,.quick-action,.quick-card,.route-stop")
      : null;

    if(!el) return;

    try{
      el.classList.add("muavin-tap-now-v56");
      setTimeout(function(){
        el.classList.remove("muavin-tap-now-v56");
      }, 120);
    }catch(_){}
  }, {passive:true, capture:true});
})();
