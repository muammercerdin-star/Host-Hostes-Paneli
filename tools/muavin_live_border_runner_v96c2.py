from pathlib import Path
from datetime import datetime
import shutil
import re

ROOT = Path(".").resolve()
STAMP = datetime.now().strftime("%Y%m%d-%H%M%S")

WEB_JS = ROOT / "static/continue/continue_trip_core.js"
WEB_CSS = ROOT / "static/continue/css_parts/50-live-v2-top-glow.css"
WEB_MAIN_CSS = ROOT / "static/continue/continue_trip.css"
WEB_TPL = ROOT / "templates/continue_trip.html"

ANDROID_JS = ROOT / "android_app/app/src/main/python/static/continue/continue_trip_core.js"
ANDROID_CSS = ROOT / "android_app/app/src/main/python/static/continue/css_parts/50-live-v2-top-glow.css"
ANDROID_MAIN_CSS = ROOT / "android_app/app/src/main/python/static/continue/continue_trip.css"
ANDROID_TPL = ROOT / "android_app/app/src/main/python/templates/continue_trip.html"

FILES = [WEB_JS, WEB_CSS, WEB_MAIN_CSS, WEB_TPL, ANDROID_JS, ANDROID_CSS, ANDROID_MAIN_CSS, ANDROID_TPL]

MARK = "LIVE_BORDER_RUNNER_PROGRESS_V96C2"

print("===== LIVE BORDER RUNNER V96C2 - ANCHOR YOK, BAĞIMSIZ =====")
print("ROOT:", ROOT)

missing = [p for p in FILES if not p.exists()]
if missing:
    print("❌ Eksik dosyalar:")
    for p in missing:
        print(" -", p.relative_to(ROOT))
    raise SystemExit(1)

def read(p):
    return p.read_text(encoding="utf-8", errors="ignore")

def write(p, s):
    p.write_text(s, encoding="utf-8")

def backup(p):
    b = p.with_name(p.name + f".bak-v96c2-{STAMP}")
    shutil.copy2(p, b)
    return b

def patch_file(p, fn):
    old = read(p)
    new = fn(old)
    if new != old:
        b = backup(p)
        write(p, new)
        print("✅ Değişti:", p.relative_to(ROOT))
        print("   backup:", b.relative_to(ROOT))
    else:
        print("ℹ️ Değişmedi:", p.relative_to(ROOT))

CSS_BLOCK = r'''

/* LIVE_BORDER_RUNNER_PROGRESS_V96C2
   Sabit nokta yerine SVG tabanlı gerçek kart çevresi runner.
   Eski V96/V96B katmanlarını kapatır.
*/
#liveCurrentCard{
  position:relative !important;
  overflow:hidden !important;
  isolation:isolate !important;
}

/* Eski sol sabit çizgi / eski pseudo katmanı kapat */
#liveCurrentCard.card.live::before{
  content:none !important;
  display:none !important;
}

/* Önceki V96/V96B sabit nokta ve conic border katmanlarını kapat */
#liveCurrentCard .live-stop-progress-border-v96,
#liveCurrentCard .live-stop-progress-runner-v96{
  display:none !important;
  animation:none !important;
  opacity:0 !important;
}

#liveCurrentCard .live-border-progress-v96c2{
  position:absolute !important;
  inset:0 !important;
  z-index:2 !important;
  pointer-events:none !important;
  border-radius:inherit !important;
}

#liveCurrentCard .live-border-progress-v96c2 svg{
  width:100% !important;
  height:100% !important;
  display:block !important;
  overflow:visible !important;
}

#liveCurrentCard .live-border-track-v96c2{
  fill:none !important;
  stroke:rgba(255,72,110,.16) !important;
  stroke-width:2.2 !important;
}

#liveCurrentCard .live-border-done-v96c2{
  fill:none !important;
  stroke:rgba(255,45,85,.70) !important;
  stroke-width:3.2 !important;
  stroke-linecap:round !important;
  filter:
    drop-shadow(0 0 4px rgba(255,45,85,.42))
    drop-shadow(0 0 11px rgba(255,45,85,.22)) !important;
  transition:stroke-dasharray .35s linear, stroke-dashoffset .35s linear !important;
}

#liveCurrentCard .live-border-runner-v96c2{
  fill:none !important;
  stroke:#ff4a74 !important;
  stroke-width:5.4 !important;
  stroke-linecap:round !important;
  filter:
    drop-shadow(0 0 5px rgba(255,255,255,.80))
    drop-shadow(0 0 10px rgba(255,74,116,.90))
    drop-shadow(0 0 18px rgba(255,74,116,.55)) !important;
}

#liveCurrentCard.is-live-border-near-v96c2 .live-border-runner-v96c2{
  stroke:#ff1744 !important;
  stroke-width:6 !important;
}

#liveCurrentCard.is-live-border-arrived-v96c2 .live-border-runner-v96c2,
#liveCurrentCard.is-live-border-arrived-v96c2 .live-border-done-v96c2{
  stroke:#22c55e !important;
}

#liveCurrentCard > :not(.live-border-progress-v96c2){
  position:relative !important;
  z-index:4 !important;
}
'''

JS_BLOCK = r'''

/* LIVE_BORDER_RUNNER_PROGRESS_V96C2
   Bağımsız çalışır. #liveDistanceValue ve #liveCurrentStopName değişimini izler.
   Runner sürekli kart etrafında yürür; progress çizgisi km azaldıkça dolar.
*/
(function(){
  if(window.__liveBorderRunnerV96C2) return;
  window.__liveBorderRunnerV96C2 = true;

  const BOOT = window.CONTINUE_BOOT || {};
  const tripPart = String(BOOT.tripId || BOOT.tripKey || "trip");

  const state = {
    card:null,
    host:null,
    track:null,
    done:null,
    runner:null,
    total:0,
    seg:120,
    progress:0,
    startKm:NaN,
    stopKey:"",
    raf:0
  };

  function q(sel){
    return document.querySelector(sel);
  }

  function norm(value){
    return String(value || "")
      .toLocaleLowerCase("tr-TR")
      .replace(/\s+/g, " ")
      .trim();
  }

  function parseKm(value){
    const raw = String(value ?? "").trim();
    if(!raw || raw === "—" || raw === "-") return NaN;

    const lower = raw.toLocaleLowerCase("tr-TR").replace(",", ".");
    const m = lower.match(/-?\d+(?:\.\d+)?/);
    if(!m) return NaN;

    const n = Number(m[0]);
    if(!Number.isFinite(n)) return NaN;

    if(/(^|\s|[0-9])m\s*$/.test(lower) && !/km\s*$/.test(lower)){
      return n / 1000;
    }

    return n;
  }

  function clamp01(n){
    return Math.max(0, Math.min(1, n));
  }

  function keyBase(stopKey){
    return "liveBorderRunnerV96C2:start:" + tripPart + ":" + stopKey;
  }

  function keyProg(stopKey){
    return "liveBorderRunnerV96C2:prog:" + tripPart + ":" + stopKey;
  }

  function readNum(key){
    try{
      const n = Number(localStorage.getItem(key));
      return Number.isFinite(n) ? n : NaN;
    }catch(_){
      return NaN;
    }
  }

  function writeNum(key, value){
    try{
      if(Number.isFinite(value)) localStorage.setItem(key, String(value));
    }catch(_){}
  }

  function ensure(){
    const card = q("#liveCurrentCard");
    if(!card) return false;

    if(state.card !== card){
      state.card = card;

      let host = card.querySelector(".live-border-progress-v96c2");
      if(!host){
        host = document.createElement("div");
        host.className = "live-border-progress-v96c2";
        host.setAttribute("aria-hidden", "true");
        host.innerHTML =
          '<svg viewBox="0 0 100 100" preserveAspectRatio="none">' +
            '<rect class="live-border-track-v96c2" x="4" y="4" width="92" height="92" rx="24" ry="24"></rect>' +
            '<rect class="live-border-done-v96c2" x="4" y="4" width="92" height="92" rx="24" ry="24"></rect>' +
            '<rect class="live-border-runner-v96c2" x="4" y="4" width="92" height="92" rx="24" ry="24"></rect>' +
          '</svg>';
        card.insertBefore(host, card.firstChild);
      }

      state.host = host;
      state.track = host.querySelector(".live-border-track-v96c2");
      state.done = host.querySelector(".live-border-done-v96c2");
      state.runner = host.querySelector(".live-border-runner-v96c2");
    }

    layout();
    return !!state.runner;
  }

  function layout(){
    if(!state.card || !state.host || !state.track || !state.done || !state.runner) return;

    const box = state.card.getBoundingClientRect();
    const w = Math.max(100, Math.round(box.width || 100));
    const h = Math.max(100, Math.round(box.height || 100));
    const pad = 5;
    const rx = Math.max(20, Math.min(32, Math.round(Math.min(w, h) * .105)));

    const svg = state.host.querySelector("svg");
    if(svg) svg.setAttribute("viewBox", "0 0 " + w + " " + h);

    [state.track, state.done, state.runner].forEach(node => {
      node.setAttribute("x", pad);
      node.setAttribute("y", pad);
      node.setAttribute("width", Math.max(10, w - pad * 2));
      node.setAttribute("height", Math.max(10, h - pad * 2));
      node.setAttribute("rx", rx);
      node.setAttribute("ry", rx);
    });

    try{
      state.total = state.runner.getTotalLength();
    }catch(_){
      state.total = 2 * (w + h);
    }

    if(!Number.isFinite(state.total) || state.total <= 0){
      state.total = 2 * (w + h);
    }

    state.seg = Math.max(90, Math.min(190, state.total * .16));
    paintProgress();
  }

  function paintProgress(){
    if(!state.done || !state.runner || !state.total) return;

    const total = state.total;
    const progress = clamp01(state.progress || 0);
    const doneLen = Math.max(0.01, total * progress);

    state.done.style.strokeDasharray = doneLen + " " + total;
    state.done.style.strokeDashoffset = "0";

    state.runner.style.strokeDasharray = state.seg + " " + total;
  }

  function currentStopName(){
    const el = q("#liveCurrentStopName");
    return String(el ? el.textContent : "").trim();
  }

  function currentDistanceText(){
    const el = q("#liveDistanceValue");
    return String(el ? el.textContent : "").trim();
  }

  function update(){
    if(!ensure()) return;

    const stop = currentStopName();
    const stopKey = norm(stop);
    const km = parseKm(currentDistanceText());

    if(!stopKey || stopKey.includes("seçilmedi") || stopKey.includes("secilmedi") || stopKey.includes("bekleniyor")){
      state.progress = 0;
      paintProgress();
      return;
    }

    if(state.stopKey !== stopKey){
      state.stopKey = stopKey;
      state.startKm = readNum(keyBase(stopKey));
      state.progress = readNum(keyProg(stopKey));
      if(!Number.isFinite(state.progress)) state.progress = 0;
    }

    if(!Number.isFinite(km) || km < 0){
      paintProgress();
      return;
    }

    if(!Number.isFinite(state.startKm) || state.startKm <= 0 || km > state.startKm * 1.15){
      state.startKm = Math.max(km, .15);
      state.progress = 0;
      writeNum(keyBase(stopKey), state.startKm);
      writeNum(keyProg(stopKey), state.progress);
      paintProgress();
      return;
    }

    let next = clamp01(1 - (km / Math.max(state.startKm, .15)));

    // GPS zıplarsa ışık geri sarmasın.
    next = Math.max(next, clamp01(state.progress || 0));

    state.progress = next;
    writeNum(keyProg(stopKey), state.progress);

    state.card.classList.toggle("is-live-border-near-v96c2", km <= 1 || state.progress >= .75);
    state.card.classList.toggle("is-live-border-arrived-v96c2", km <= .25 || state.progress >= .97);

    paintProgress();
  }

  function animate(ts){
    if(state.runner && state.total){
      const card = state.card;
      const fast = card && (card.classList.contains("is-live-border-near-v96c2") || card.classList.contains("is-live-border-arrived-v96c2"));
      const period = fast ? 1200 : 2300;
      const offset = -((ts % period) / period) * state.total;
      state.runner.style.strokeDashoffset = String(offset);
    }

    state.raf = requestAnimationFrame(animate);
  }

  function bind(){
    ensure();
    update();

    const distEl = q("#liveDistanceValue");
    const stopEl = q("#liveCurrentStopName");

    if(distEl){
      new MutationObserver(update).observe(distEl, {childList:true, characterData:true, subtree:true});
    }

    if(stopEl){
      new MutationObserver(update).observe(stopEl, {childList:true, characterData:true, subtree:true});
    }

    window.addEventListener("resize", function(){
      setTimeout(function(){
        layout();
        update();
      }, 80);
    });

    setInterval(update, 1200);

    if(!state.raf){
      state.raf = requestAnimationFrame(animate);
    }
  }

  if(document.readyState === "loading"){
    document.addEventListener("DOMContentLoaded", bind);
  }else{
    bind();
  }
})();
'''

def patch_css(s):
    if MARK in s:
        return s
    return s.rstrip() + "\n" + CSS_BLOCK + "\n"

def patch_js(s):
    if MARK in s:
        return s
    return s.rstrip() + "\n" + JS_BLOCK + "\n"

def patch_main_css(s):
    return re.sub(
        r'@import\s+url\("\./css_parts/50-live-v2-top-glow\.css(?:\?v=[^"]*)?"\)\s*;',
        '@import url("./css_parts/50-live-v2-top-glow.css?v=live-border-runner-v96c2");',
        s
    )

def patch_tpl(s):
    s = re.sub(
        r"(filename='continue/continue_trip\.css'\)\s*\}\})\?v=[^\"']+",
        r"\1?v=live-border-runner-v96c2",
        s
    )
    s = re.sub(
        r"(filename='continue/continue_trip_core\.js'\)\s*\}\})\?v=[^\"']+",
        r"\1?v=live-border-runner-v96c2",
        s
    )
    return s

for p in [WEB_CSS, ANDROID_CSS]:
    patch_file(p, patch_css)

for p in [WEB_JS, ANDROID_JS]:
    patch_file(p, patch_js)

for p in [WEB_MAIN_CSS, ANDROID_MAIN_CSS]:
    patch_file(p, patch_main_css)

for p in [WEB_TPL, ANDROID_TPL]:
    patch_file(p, patch_tpl)

print()
print("===== KONTROL =====")
for p in [WEB_CSS, WEB_JS, ANDROID_CSS, ANDROID_JS]:
    txt = read(p)
    print(("OK " if MARK in txt else "NO "), p.relative_to(ROOT))

print()
print("✅ V96C2 tamam. Bu sürüm anchor aramaz; bağımsız çalışır.")
