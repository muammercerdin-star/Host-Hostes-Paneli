from pathlib import Path
from datetime import datetime
import shutil
import re

ROOT = Path(".").resolve()
STAMP = datetime.now().strftime("%Y%m%d-%H%M%S")

FILES = [
    ROOT / "static/continue/css_parts/50-live-v2-top-glow.css",
    ROOT / "static/continue/continue_trip_core.js",
    ROOT / "static/continue/continue_trip.css",
    ROOT / "templates/continue_trip.html",

    ROOT / "android_app/app/src/main/python/static/continue/css_parts/50-live-v2-top-glow.css",
    ROOT / "android_app/app/src/main/python/static/continue/continue_trip_core.js",
    ROOT / "android_app/app/src/main/python/static/continue/continue_trip.css",
    ROOT / "android_app/app/src/main/python/templates/continue_trip.html",
]

CSS_WEB = ROOT / "static/continue/css_parts/50-live-v2-top-glow.css"
CSS_ANDROID = ROOT / "android_app/app/src/main/python/static/continue/css_parts/50-live-v2-top-glow.css"

JS_WEB = ROOT / "static/continue/continue_trip_core.js"
JS_ANDROID = ROOT / "android_app/app/src/main/python/static/continue/continue_trip_core.js"

CSS_MAIN_WEB = ROOT / "static/continue/continue_trip.css"
CSS_MAIN_ANDROID = ROOT / "android_app/app/src/main/python/static/continue/continue_trip.css"

TPL_WEB = ROOT / "templates/continue_trip.html"
TPL_ANDROID = ROOT / "android_app/app/src/main/python/templates/continue_trip.html"

MARK_CSS = "LIVE_STOP_PROGRESS_BORDER_V96_CSS"
MARK_JS = "LIVE_STOP_PROGRESS_BORDER_V96_JS"

print("===== V96 CANLI DURAK YÜRÜYEN IŞIK / KM PROGRESS BORDER =====")
print("ROOT:", ROOT)

missing = [p for p in FILES if not p.exists()]
if missing:
    print("❌ Eksik dosyalar:")
    for p in missing:
        print(" -", p.relative_to(ROOT))
    raise SystemExit(1)

def backup(p: Path):
    b = p.with_name(p.name + f".bak-live-progress-v96-{STAMP}")
    shutil.copy2(p, b)
    return b

def read(p: Path):
    return p.read_text(encoding="utf-8", errors="ignore")

def write(p: Path, s: str):
    p.write_text(s, encoding="utf-8")

def patch_file(p: Path, fn):
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

/* LIVE_STOP_PROGRESS_BORDER_V96_CSS
   Aktif canlı durak kartının etrafında km azaldıkça tamamlanan yürüyen ışık.
   Sadece görsel katmandır; GPS / ETA / canlı durak mantığına dokunmaz.
*/
#liveCurrentCard.card.live.live-stop-progress-ready-v96{
  position:relative !important;
  overflow:hidden !important;
  isolation:isolate !important;

  --liveStopProgressDeg:0deg;
  --liveStopProgressGlow:#ff2d55;
  --liveStopProgressSoft:rgba(255,45,85,.18);
  --liveStopRunnerSpeed:1.75s;
}

#liveCurrentCard.card.live.live-stop-progress-ready-v96 > :not(.live-stop-progress-border-v96):not(.live-stop-progress-runner-v96){
  position:relative;
  z-index:3;
}

#liveCurrentCard.card.live .live-stop-progress-border-v96,
#liveCurrentCard.card.live .live-stop-progress-runner-v96{
  position:absolute;
  inset:0;
  border-radius:inherit;
  pointer-events:none;
  z-index:2;
}

#liveCurrentCard.card.live .live-stop-progress-border-v96{
  padding:2px;
  background:
    conic-gradient(
      from -90deg,
      var(--liveStopProgressGlow) 0deg,
      var(--liveStopProgressGlow) var(--liveStopProgressDeg),
      rgba(255,255,255,.075) var(--liveStopProgressDeg),
      rgba(255,255,255,.075) 360deg
    );

  -webkit-mask:
    linear-gradient(#000 0 0) content-box,
    linear-gradient(#000 0 0);
  -webkit-mask-composite:xor;
  mask-composite:exclude;

  filter:
    drop-shadow(0 0 8px var(--liveStopProgressSoft))
    drop-shadow(0 0 14px rgba(255,45,85,.12));
}

#liveCurrentCard.card.live .live-stop-progress-runner-v96{
  inset:-2px;
  padding:3px;
  background:
    conic-gradient(
      from 0deg,
      transparent 0deg,
      transparent 302deg,
      rgba(255,255,255,.92) 328deg,
      var(--liveStopProgressGlow) 348deg,
      transparent 360deg
    );

  -webkit-mask:
    linear-gradient(#000 0 0) content-box,
    linear-gradient(#000 0 0);
  -webkit-mask-composite:xor;
  mask-composite:exclude;

  animation:liveStopProgressRunnerV96 var(--liveStopRunnerSpeed) linear infinite;
  filter:
    drop-shadow(0 0 8px rgba(255,255,255,.45))
    drop-shadow(0 0 13px var(--liveStopProgressGlow));
  opacity:.95;
}

#liveCurrentCard.card.live.is-live-progress-near-v96{
  --liveStopProgressGlow:#ff1744;
  --liveStopProgressSoft:rgba(255,23,68,.34);
  --liveStopRunnerSpeed:.9s;
}

#liveCurrentCard.card.live.is-live-progress-arrived-v96{
  --liveStopProgressGlow:#22c55e;
  --liveStopProgressSoft:rgba(34,197,94,.30);
  --liveStopRunnerSpeed:.7s;
}

#liveCurrentCard.card.live.is-live-progress-arrived-v96 .live-stop-progress-border-v96{
  animation:liveStopProgressArrivedV96 1.05s ease-in-out infinite;
}

@keyframes liveStopProgressRunnerV96{
  to{ transform:rotate(360deg); }
}

@keyframes liveStopProgressArrivedV96{
  0%,100%{
    filter:
      drop-shadow(0 0 8px var(--liveStopProgressSoft))
      drop-shadow(0 0 14px rgba(34,197,94,.14));
  }
  50%{
    filter:
      drop-shadow(0 0 13px var(--liveStopProgressSoft))
      drop-shadow(0 0 24px rgba(34,197,94,.24));
  }
}
'''

JS_BLOCK = r'''

/* LIVE_STOP_PROGRESS_BORDER_V96_JS
   #liveDistanceValue değiştikçe #liveCurrentCard çevresindeki progress ışığını günceller.
   Sadece DOM/CSS değişkeni yazar; mesafe/ETA/GPS hesabına müdahale etmez.
*/
(function(){
  const BOOT = window.CONTINUE_BOOT || {};
  const STORE_PREFIX = "muavinLiveStopProgressV96:";

  function q(sel){
    return document.querySelector(sel);
  }

  function norm(value){
    return String(value || "")
      .trim()
      .toLocaleLowerCase("tr-TR")
      .replace(/\s+/g, " ");
  }

  function parseKmText(value){
    const raw = String(value ?? "").trim();
    if(!raw || raw === "—" || raw === "-") return NaN;

    const lower = raw.toLocaleLowerCase("tr-TR").replace(",", ".");
    const match = lower.match(/-?\d+(?:\.\d+)?/);
    if(!match) return NaN;

    const n = Number(match[0]);
    if(!Number.isFinite(n)) return NaN;

    if(/\bkm\b/.test(lower) || /km\s*$/.test(lower)){
      return n;
    }

    if(/(^|\s|[0-9])m\s*$/.test(lower) && !/km\s*$/.test(lower)){
      return n / 1000;
    }

    return n;
  }

  function clamp01(n){
    return Math.max(0, Math.min(1, n));
  }

  function stopName(){
    const el = q("#liveCurrentStopName");
    return String(el ? el.textContent : "").trim();
  }

  function progressKey(stop){
    const tripPart = String(BOOT.tripId || BOOT.tripKey || "trip").trim();
    const stopPart = norm(stop || "stop").slice(0, 90);
    return STORE_PREFIX + tripPart + ":" + stopPart;
  }

  function getStoredNumber(key){
    try{
      const n = Number(localStorage.getItem(key));
      return Number.isFinite(n) ? n : NaN;
    }catch(_){
      return NaN;
    }
  }

  function setStoredNumber(key, value){
    try{
      localStorage.setItem(key, String(value));
    }catch(_){}
  }

  function ensureLayers(card){
    if(!card) return;

    if(!card.querySelector(".live-stop-progress-border-v96")){
      const border = document.createElement("span");
      border.className = "live-stop-progress-border-v96";
      border.setAttribute("aria-hidden", "true");
      card.prepend(border);
    }

    if(!card.querySelector(".live-stop-progress-runner-v96")){
      const runner = document.createElement("span");
      runner.className = "live-stop-progress-runner-v96";
      runner.setAttribute("aria-hidden", "true");
      card.prepend(runner);
    }

    card.classList.add("live-stop-progress-ready-v96");
  }

  function applyLiveStopProgressV96(){
    const card = q("#liveCurrentCard");
    const distEl = q("#liveDistanceValue");
    if(!card || !distEl) return;

    ensureLayers(card);

    const stop = stopName();
    const km = parseKmText(distEl.textContent);

    if(!stop || /durak seçilmedi|durak secilmedi|bekleniyor/i.test(stop)){
      card.style.setProperty("--liveStopProgressDeg", "0deg");
      card.classList.remove("is-live-progress-near-v96", "is-live-progress-arrived-v96");
      return;
    }

    if(!Number.isFinite(km) || km < 0){
      card.style.setProperty("--liveStopProgressDeg", "0deg");
      card.classList.remove("is-live-progress-near-v96", "is-live-progress-arrived-v96");
      return;
    }

    const key = progressKey(stop);
    const startKey = key + ":startKm";
    const maxKey = key + ":maxProgress";

    let startKm = getStoredNumber(startKey);

    if(!Number.isFinite(startKm) || startKm <= 0){
      startKm = Math.max(km, 0.15);
      setStoredNumber(startKey, startKm);
    }

    // GPS ilk açılışta daha uzak bir değer yakalarsa başlangıcı yukarı al.
    if(km > startKm){
      startKm = km;
      setStoredNumber(startKey, startKm);
    }

    let progress = clamp01(1 - (km / Math.max(startKm, 0.15)));

    // Işık geri geri sönmesin; aynı durakta en yüksek ilerlemeyi koru.
    const previousMax = getStoredNumber(maxKey);
    if(Number.isFinite(previousMax)){
      progress = Math.max(progress, clamp01(previousMax));
    }
    setStoredNumber(maxKey, progress);

    const deg = Math.round(progress * 360);
    const pct = Math.round(progress * 100);

    card.style.setProperty("--liveStopProgressDeg", deg + "deg");
    card.dataset.liveStopProgressV96 = String(pct);

    card.classList.toggle("is-live-progress-near-v96", km <= 1 || progress >= .78);
    card.classList.toggle("is-live-progress-arrived-v96", km <= .25 || progress >= .97);

    window.dispatchEvent(new CustomEvent("liveStopProgressV96Updated", {
      detail:{ stop, km, startKm, progress, pct, deg }
    }));
  }

  function scheduleApply(){
    requestAnimationFrame(applyLiveStopProgressV96);
  }

  function bind(){
    const distEl = q("#liveDistanceValue");
    const stopEl = q("#liveCurrentStopName");

    if(distEl){
      new MutationObserver(scheduleApply).observe(distEl, {
        childList:true,
        characterData:true,
        subtree:true
      });
    }

    if(stopEl){
      new MutationObserver(scheduleApply).observe(stopEl, {
        childList:true,
        characterData:true,
        subtree:true
      });
    }

    scheduleApply();
    setInterval(scheduleApply, 1200);
  }

  if(document.readyState === "loading"){
    document.addEventListener("DOMContentLoaded", bind);
  }else{
    bind();
  }
})();
'''

def patch_css_50(s: str) -> str:
    if MARK_CSS in s:
        return s
    return s.rstrip() + "\n" + CSS_BLOCK + "\n"

def patch_js_core(s: str) -> str:
    if MARK_JS in s:
        return s
    return s.rstrip() + "\n" + JS_BLOCK + "\n"

def patch_main_css(s: str) -> str:
    # Imported CSS cache kırılması
    s = re.sub(
        r'@import\s+url\("\./css_parts/50-live-v2-top-glow\.css(?:\?v=[^"]*)?"\)\s*;',
        '@import url("./css_parts/50-live-v2-top-glow.css?v=live-stop-progress-v96");',
        s
    )
    return s

def patch_template(s: str) -> str:
    # Ana CSS ve core JS cache kırılması
    s = re.sub(
        r"(filename='continue/continue_trip\.css'\)\s*\}\})\?v=[^\"']+",
        r"\1?v=live-stop-progress-v96",
        s
    )
    s = re.sub(
        r"(filename='continue/continue_trip_core\.js'\)\s*\}\})\?v=[^\"']+",
        r"\1?v=live-stop-progress-v96",
        s
    )
    return s

for p in [CSS_WEB, CSS_ANDROID]:
    patch_file(p, patch_css_50)

for p in [JS_WEB, JS_ANDROID]:
    patch_file(p, patch_js_core)

for p in [CSS_MAIN_WEB, CSS_MAIN_ANDROID]:
    patch_file(p, patch_main_css)

for p in [TPL_WEB, TPL_ANDROID]:
    patch_file(p, patch_template)

print()
print("===== KONTROL =====")
for p in [CSS_WEB, JS_WEB, CSS_ANDROID, JS_ANDROID]:
    txt = read(p)
    print(("OK " if (MARK_CSS in txt or MARK_JS in txt) else "NO "), p.relative_to(ROOT))

print()
print("✅ V96 tamam.")
print("Not: Bu yama sadece #liveCurrentCard görsel progress ışığı ekler.")
