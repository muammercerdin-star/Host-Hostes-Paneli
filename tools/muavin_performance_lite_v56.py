from pathlib import Path
from datetime import datetime
import shutil
import re

ROOT = Path(".").resolve()
STAMP = datetime.now().strftime("%Y%m%d-%H%M%S")

TPLS = [
    ROOT / "templates/seats.html",
    ROOT / "android_app/app/src/main/python/templates/seats.html",
]

JS_MAIN = [
    ROOT / "static/seats/seats.js",
    ROOT / "android_app/app/src/main/python/static/seats/seats.js",
]

PERF_JS = [
    ROOT / "static/seats/patches/performance-lite-v56.js",
    ROOT / "android_app/app/src/main/python/static/seats/patches/performance-lite-v56.js",
]

PERF_CSS = [
    ROOT / "static/seats/patches/performance-lite-v56.css",
    ROOT / "android_app/app/src/main/python/static/seats/patches/performance-lite-v56.css",
]

CSS = r'''
/* MUAVIN_PERFORMANCE_LITE_V56 */
/* Mobil WebView/Chrome için ağır blur, gölge ve animasyonları hafifletir. */

@media (max-width: 820px){
  html, body{
    scroll-behavior:auto !important;
  }

  body,
  .app,
  .page,
  .board,
  .board-inner,
  .glass,
  .card,
  .route-card,
  .route-stop,
  .modal,
  .sheet-modal,
  .modal-backdrop,
  .drive-panel,
  .quick-action,
  .quick-card,
  .tab-panel,
  .dock,
  .bottom-nav{
    -webkit-backdrop-filter:none !important;
    backdrop-filter:none !important;
  }

  .glass,
  .card,
  .route-card,
  .route-stop,
  .modal,
  .sheet-modal,
  .quick-action,
  .quick-card,
  .seat,
  .dock,
  .bottom-nav{
    transition:none !important;
    animation:none !important;
  }

  .seat{
    will-change:auto !important;
    contain:layout paint !important;
    box-shadow:
      inset 0 1px 0 rgba(255,255,255,.12),
      0 8px 18px rgba(0,0,0,.20) !important;
  }

  .route-stop,
  .route-card{
    contain:layout paint !important;
    box-shadow:
      inset 0 1px 0 rgba(255,255,255,.08),
      0 8px 18px rgba(0,0,0,.18) !important;
  }

  button,
  a,
  .seat,
  .route-stop,
  .quick-action,
  .quick-card{
    touch-action:manipulation !important;
    -webkit-tap-highlight-color:rgba(255,255,255,.08) !important;
  }

  button:active,
  a:active,
  .seat:active,
  .quick-action:active,
  .quick-card:active{
    transform:scale(.985) !important;
  }

  .modal-backdrop,
  .route-sheet-backdrop,
  .trip-guard-backdrop{
    background:rgba(2,6,23,.62) !important;
  }
}

/* Durak Akışı kartları dışarı taşmasın */
.route-strip-shell,
.route-strip,
.route-scroll,
.route-list,
.stop-flow,
.stop-flow-list{
  max-width:100% !important;
  overflow-x:auto !important;
  overflow-y:hidden !important;
  -webkit-overflow-scrolling:touch !important;
}

.route-stop,
.route-card{
  min-width:0 !important;
  flex-shrink:0 !important;
}

.route-stop .name,
.route-stop .meta,
.route-card .name,
.route-card .meta{
  overflow:hidden !important;
  text-overflow:ellipsis !important;
  white-space:nowrap !important;
}
'''

JS = r'''
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
'''

def backup(p):
    if p.exists():
        b = p.with_name(p.name + f".bak-perf-v56-{STAMP}")
        shutil.copy2(p, b)
        print("📦 Yedek:", b.relative_to(ROOT))

print("===== MUAVIN PERFORMANCE LITE V56 =====")

for p, content in [(PERF_CSS[0], CSS), (PERF_CSS[1], CSS), (PERF_JS[0], JS), (PERF_JS[1], JS)]:
    p.parent.mkdir(parents=True, exist_ok=True)
    backup(p)
    p.write_text(content.strip() + "\n", encoding="utf-8")
    print("✅ Yazıldı:", p.relative_to(ROOT))

for p in TPLS:
    if not p.exists():
        print("⚠️ Yok:", p.relative_to(ROOT))
        continue

    backup(p)
    s = p.read_text(encoding="utf-8", errors="ignore")

    css_line = '<link rel="stylesheet" href="/static/seats/patches/performance-lite-v56.css?v=1">'
    js_line = '<script src="/static/seats/patches/performance-lite-v56.js?v=1"></script>'

    if "performance-lite-v56.css" not in s:
      if "</head>" in s:
        s = s.replace("</head>", css_line + "\n</head>", 1)
      else:
        s = css_line + "\n" + s
      print("✅ CSS link eklendi:", p.relative_to(ROOT))
    else:
      print("ℹ️ CSS link zaten var:", p.relative_to(ROOT))

    if "performance-lite-v56.js" not in s:
      target = '<script src="/static/seats/seats.js'
      idx = s.find(target)
      if idx >= 0:
        s = s[:idx] + js_line + "\n" + s[idx:]
      else:
        s = s.replace("</body>", js_line + "\n</body>", 1)
      print("✅ JS preloader eklendi:", p.relative_to(ROOT))
    else:
      print("ℹ️ JS preloader zaten var:", p.relative_to(ROOT))

    # Cache kır
    s = re.sub(r'/static/seats/seats\.css\?v=[^"]+', '/static/seats/seats.css?v=perf-v56', s)
    s = re.sub(r'/static/seats/seats\.js\?v=[^"]+', '/static/seats/seats.js?v=perf-v56', s)

    p.write_text(s, encoding="utf-8")

for p in JS_MAIN:
    if not p.exists():
        print("⚠️ Yok:", p.relative_to(ROOT))
        continue

    backup(p)
    s = p.read_text(encoding="utf-8", errors="ignore")
    old = s

    # Speed/GPS render eşiğini yükselt
    s = s.replace(
        "nowRender - window.__seatsLastSpeedRenderAt > 2500",
        "nowRender - window.__seatsLastSpeedRenderAt > 7000"
    )

    # GPS seçeneklerini hafiflet
    s = s.replace("enableHighAccuracy:true", "enableHighAccuracy:false")
    s = s.replace("maximumAge:3000", "maximumAge:10000")
    s = s.replace("timeout:12000", "timeout:18000")

    if s != old:
        p.write_text(s, encoding="utf-8")
        print("✅ seats.js hafifletildi:", p.relative_to(ROOT))
    else:
        print("ℹ️ seats.js değişmedi:", p.relative_to(ROOT))

print()
print("===== KONTROL =====")
for p in TPLS + JS_MAIN + PERF_CSS + PERF_JS:
    if p.exists():
        txt = p.read_text(encoding="utf-8", errors="ignore")
        print(p.relative_to(ROOT), "V56:", txt.count("performance-lite-v56") + txt.count("MUAVIN_PERFORMANCE_LITE_V56") + txt.count("7000") + txt.count("enableHighAccuracy:false"))

print()
print("✅ V56 performans yaması uygulandı.")
print("Commit/push yok. Önce tarayıcıda test et.")
