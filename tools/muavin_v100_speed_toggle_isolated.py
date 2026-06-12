from pathlib import Path
from datetime import datetime
import shutil
import re
import subprocess
import hashlib

ROOT = Path(".").resolve()
STAMP = datetime.now().strftime("%Y%m%d-%H%M%S")

WEB_TPL = ROOT / "templates/continue_trip.html"
AND_TPL = ROOT / "android_app/app/src/main/python/templates/continue_trip.html"

WEB_JS = ROOT / "static/continue/continue_speed_toggle_v100.js"
AND_JS = ROOT / "android_app/app/src/main/python/static/continue/continue_speed_toggle_v100.js"

WEB_CSS = ROOT / "static/continue/continue_speed_toggle_v100.css"
AND_CSS = ROOT / "android_app/app/src/main/python/static/continue/continue_speed_toggle_v100.css"

V99_JS = ROOT / "static/continue/continue_trip_v99_clean.js"

print("===== V100 İZOLE HIZ ANALOG / DİJİTAL TOGGLE =====")

def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()[:12] if p.exists() else "-"

for p in [WEB_TPL, AND_TPL, WEB_JS, AND_JS, WEB_CSS, AND_CSS]:
    if p.exists():
        bak = p.with_name(p.name + f".bak-v100-speed-isolated-{STAMP}")
        shutil.copy2(p, bak)
        print("📦 backup:", bak)

if not WEB_TPL.exists():
    raise SystemExit("❌ Template yok: " + str(WEB_TPL))

WEB_JS.parent.mkdir(parents=True, exist_ok=True)
WEB_CSS.parent.mkdir(parents=True, exist_ok=True)

js = r'''
/* V100_SPEED_TOGGLE_ISOLATED_START */
(function(){
  "use strict";

  if(window.__MUAVIN_V100_SPEED_TOGGLE__) return;
  window.__MUAVIN_V100_SPEED_TOGGLE__ = true;

  var STORAGE_KEY = "muavin.v100.speed.mode";

  function q(sel, root){
    return (root || document).querySelector(sel);
  }

  function qa(sel, root){
    return Array.prototype.slice.call((root || document).querySelectorAll(sel));
  }

  function text(el){
    return el ? String(el.textContent || "").trim() : "";
  }

  function norm(s){
    return String(s || "")
      .toLocaleUpperCase("tr-TR")
      .replace(/\s+/g, " ")
      .trim();
  }

  function findSpeedCard(){
    var cells = qa(".v99-gauges .v99-gauge-cell");

    for(var i = 0; i < cells.length; i++){
      var label = q(".v99-gauge-label", cells[i]);
      if(norm(text(label)) === "HIZ"){
        return cells[i];
      }
    }

    return null;
  }

  function readSpeed(){
    var visible = q("#v99SpeedVal");
    var hidden = q("#liveSpeedText");

    var raw = text(visible);
    if(!raw || raw === "—"){
      raw = text(hidden);
    }

    raw = String(raw || "")
      .replace(",", ".")
      .replace(/km\/sa|km\/h|kmh|km|sa/gi, "")
      .replace(/[^\d.]/g, "")
      .trim();

    var n = Number(raw);
    if(!Number.isFinite(n)) n = 0;
    if(n < 0) n = 0;
    if(n > 180) n = 180;

    return n;
  }

  function ensureUi(card){
    if(!card) return;

    card.classList.add("v100-speed-card");
    card.setAttribute("data-v100-speed-toggle", "1");
    card.setAttribute("title", "Hız görünümünü değiştir");

    if(q(".v100-speed-analog", card)) return;

    var box = document.createElement("div");
    box.className = "v100-speed-analog";
    box.innerHTML = ''
      + '<div class="v100-speed-dial">'
      + '  <div class="v100-speed-scale"></div>'
      + '  <div class="v100-speed-mark m0">0</div>'
      + '  <div class="v100-speed-mark m70">70</div>'
      + '  <div class="v100-speed-mark m140">140</div>'
      + '  <div class="v100-speed-needle"></div>'
      + '  <div class="v100-speed-center"></div>'
      + '  <div class="v100-speed-num">0</div>'
      + '</div>'
      + '<div class="v100-speed-sub">km/sa</div>';

    card.appendChild(box);
  }

  function setMode(card, mode){
    if(!card) return;

    if(mode === "analog"){
      card.classList.add("v100-speed-analog-on");
    }else{
      card.classList.remove("v100-speed-analog-on");
    }

    try{
      localStorage.setItem(STORAGE_KEY, mode === "analog" ? "analog" : "digital");
    }catch(_){}

    paint();
  }

  function currentMode(card){
    if(!card) return "digital";
    return card.classList.contains("v100-speed-analog-on") ? "analog" : "digital";
  }

  function paint(){
    var card = findSpeedCard();
    if(!card) return;

    ensureUi(card);

    var speed = readSpeed();
    var capped = Math.max(0, Math.min(speed, 140));
    var deg = -120 + ((capped / 140) * 240);

    card.style.setProperty("--v100-speed-deg", deg.toFixed(1) + "deg");

    var num = q(".v100-speed-num", card);
    if(num){
      num.textContent = String(Math.round(speed));
    }

    card.classList.toggle("v100-speed-low", speed < 50);
    card.classList.toggle("v100-speed-mid", speed >= 50 && speed < 95);
    card.classList.toggle("v100-speed-high", speed >= 95);
  }

  function bind(){
    var card = findSpeedCard();
    if(!card) return false;

    ensureUi(card);

    if(!card.dataset.v100SpeedInitialMode){
      card.dataset.v100SpeedInitialMode = "1";

      var saved = "digital";
      try{
        saved = localStorage.getItem(STORAGE_KEY) || "digital";
      }catch(_){}

      if(saved === "analog"){
        card.classList.add("v100-speed-analog-on");
      }
    }

    if(card.dataset.v100SpeedBound === "1"){
      paint();
      return true;
    }

    card.dataset.v100SpeedBound = "1";

    card.addEventListener("click", function(ev){
      /*
        Sadece HIZ kartına bağlı.
        DOLULUK paneli ve DURUM kartına karışmaz.
      */
      ev.preventDefault();
      ev.stopPropagation();

      var next = currentMode(card) === "analog" ? "digital" : "analog";
      setMode(card, next);
    }, true);

    paint();
    return true;
  }

  function boot(){
    bind();
    paint();

    try{
      var speedEl = q("#v99SpeedVal");
      if(speedEl && !speedEl.dataset.v100SpeedObserved){
        speedEl.dataset.v100SpeedObserved = "1";
        new MutationObserver(function(){
          paint();
        }).observe(speedEl, {
          childList:true,
          subtree:true,
          characterData:true
        });
      }
    }catch(_){}
  }

  if(document.readyState === "loading"){
    document.addEventListener("DOMContentLoaded", boot);
  }else{
    boot();
  }

  window.addEventListener("load", boot);
  document.addEventListener("continueEtaUpdated", paint);

  var tries = 80;
  var timer = setInterval(function(){
    boot();
    tries--;
    if(tries <= 0) clearInterval(timer);
  }, 500);

  window.MuavinV100SpeedToggle = {
    boot: boot,
    paint: paint,
    mode: function(){
      return currentMode(findSpeedCard());
    }
  };
})();
/* V100_SPEED_TOGGLE_ISOLATED_END */
'''.strip() + "\n"

css = r'''
/* V100_SPEED_TOGGLE_ISOLATED_CSS_START */

.v100-speed-card{
  cursor:pointer !important;
  user-select:none !important;
  -webkit-user-select:none !important;
  touch-action:manipulation !important;
  position:relative !important;
}

.v100-speed-card::after{
  content:"";
  position:absolute;
  inset:7px;
  border-radius:18px;
  border:1px solid rgba(224,136,32,0);
  pointer-events:none;
  transition:.16s ease;
}

.v100-speed-card:active::after{
  border-color:rgba(224,136,32,.45);
  box-shadow:0 0 18px rgba(224,136,32,.22);
}

.v100-speed-analog{
  display:none;
  margin-top:4px;
  width:100%;
  align-items:center;
  justify-content:center;
  flex-direction:column;
}

.v100-speed-card.v100-speed-analog-on #v99SpeedVal,
.v100-speed-card.v100-speed-analog-on .v99-gauge-unit,
.v100-speed-card.v100-speed-analog-on #liveSpeedText{
  display:none !important;
}

.v100-speed-card.v100-speed-analog-on .v100-speed-analog{
  display:flex !important;
}

.v100-speed-dial{
  position:relative;
  width:86px;
  height:49px;
  margin:0 auto;
  overflow:visible;
}

.v100-speed-scale{
  position:absolute;
  left:6px;
  right:6px;
  bottom:-30px;
  height:72px;
  border-radius:80px 80px 0 0;
  border:4px solid rgba(224,136,32,.68);
  border-bottom:0;
  background:
    radial-gradient(circle at 50% 100%, rgba(224,136,32,.14), transparent 56%),
    linear-gradient(180deg, rgba(255,255,255,.035), rgba(255,255,255,0));
  box-shadow:
    0 0 15px rgba(224,136,32,.28),
    inset 0 0 18px rgba(224,136,32,.08);
}

.v100-speed-needle{
  position:absolute;
  left:50%;
  bottom:5px;
  width:3px;
  height:36px;
  border-radius:4px;
  background:linear-gradient(180deg,#fff1bf,#e08820);
  transform-origin:50% calc(100% - 2px);
  transform:translateX(-50%) rotate(var(--v100-speed-deg, -120deg));
  box-shadow:0 0 12px rgba(224,136,32,.72);
  transition:transform .25s ease;
}

.v100-speed-center{
  position:absolute;
  left:50%;
  bottom:0;
  width:13px;
  height:13px;
  border-radius:50%;
  transform:translateX(-50%);
  background:#ffe0a5;
  box-shadow:0 0 12px rgba(255,224,165,.6);
}

.v100-speed-num{
  position:absolute;
  left:50%;
  bottom:15px;
  transform:translateX(-50%);
  font-family:'JetBrains Mono', monospace;
  font-size:13px;
  font-weight:900;
  color:#e08820;
  line-height:1;
  text-shadow:0 0 12px rgba(224,136,32,.52);
}

.v100-speed-sub{
  margin-top:0;
  font-family:'JetBrains Mono', monospace;
  font-size:9px;
  letter-spacing:1.8px;
  color:var(--v99-muted);
  text-transform:uppercase;
}

.v100-speed-mark{
  position:absolute;
  font-family:'JetBrains Mono', monospace;
  font-size:7px;
  color:rgba(232,238,248,.55);
  line-height:1;
  pointer-events:none;
}

.v100-speed-mark.m0{
  left:1px;
  bottom:4px;
}

.v100-speed-mark.m70{
  left:50%;
  top:0;
  transform:translateX(-50%);
}

.v100-speed-mark.m140{
  right:0;
  bottom:4px;
}

.v100-speed-card.v100-speed-low .v100-speed-scale{
  border-color:rgba(29,184,122,.72);
  box-shadow:0 0 15px rgba(29,184,122,.28);
}

.v100-speed-card.v100-speed-low .v100-speed-num{
  color:var(--v99-green);
  text-shadow:0 0 12px rgba(29,184,122,.48);
}

.v100-speed-card.v100-speed-high .v100-speed-scale{
  border-color:rgba(224,48,48,.76);
  box-shadow:0 0 15px rgba(224,48,48,.34);
}

.v100-speed-card.v100-speed-high .v100-speed-num{
  color:var(--v99-red);
  text-shadow:0 0 12px rgba(224,48,48,.58);
}

/* V100_SPEED_TOGGLE_ISOLATED_CSS_END */
'''.strip() + "\n"

WEB_JS.write_text(js, encoding="utf-8")
WEB_CSS.write_text(css, encoding="utf-8")
print("✅ Web V100 JS yazıldı:", WEB_JS)
print("✅ Web V100 CSS yazıldı:", WEB_CSS)

tpl = WEB_TPL.read_text(encoding="utf-8", errors="ignore")

tpl = re.sub(
    r'\n?\s*<link[^>]+continue_speed_toggle_v100\.css[^>]*>\s*',
    "\n",
    tpl
)
tpl = re.sub(
    r'\n?\s*<script[^>]+continue_speed_toggle_v100\.js[^>]*></script>\s*',
    "\n",
    tpl
)

css_link = """<link rel="stylesheet" href="{{ url_for('static', filename='continue/continue_speed_toggle_v100.css') }}?v=v100-speed-{{ trip['id'] }}">"""
js_script = """<script src="{{ url_for('static', filename='continue/continue_speed_toggle_v100.js') }}?v=v100-speed-{{ trip['id'] }}"></script>"""

if "</head>" in tpl:
    tpl = tpl.replace("</head>", css_link + "\n</head>")
else:
    tpl = css_link + "\n" + tpl

if "</body>" in tpl:
    tpl = tpl.replace("</body>", js_script + "\n</body>")
else:
    tpl = tpl.rstrip() + "\n" + js_script + "\n"

WEB_TPL.write_text(tpl, encoding="utf-8")
print("✅ Template V100 link/script eklendi:", WEB_TPL)

if AND_TPL.parent.exists():
    shutil.copy2(WEB_TPL, AND_TPL)
    print("✅ Android template senkron")

if AND_JS.parent.exists():
    AND_JS.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(WEB_JS, AND_JS)
    print("✅ Android V100 JS senkron")

if AND_CSS.parent.exists():
    AND_CSS.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(WEB_CSS, AND_CSS)
    print("✅ Android V100 CSS senkron")

print()
print("===== NODE JS SYNTAX CHECK =====")
try:
    res = subprocess.run(["node", "--check", str(WEB_JS)], capture_output=True, text=True)
    if res.returncode == 0:
        print("✅ V100 JS syntax OK")
    else:
        print("❌ V100 JS syntax HATA")
        print(res.stdout)
        print(res.stderr)
except FileNotFoundError:
    print("ℹ️ node yok, syntax check atlandı")

print()
print("===== KONTROL =====")
tpl_now = WEB_TPL.read_text(encoding="utf-8", errors="ignore")
js_now = WEB_JS.read_text(encoding="utf-8", errors="ignore")
css_now = WEB_CSS.read_text(encoding="utf-8", errors="ignore")
v99_now = V99_JS.read_text(encoding="utf-8", errors="ignore") if V99_JS.exists() else ""

checks = [
    ("Template CSS link var", "continue_speed_toggle_v100.css" in tpl_now),
    ("Template JS script var", "continue_speed_toggle_v100.js" in tpl_now),
    ("V100 JS marker var", "V100_SPEED_TOGGLE_ISOLATED_START" in js_now),
    ("V100 CSS marker var", "V100_SPEED_TOGGLE_ISOLATED_CSS_START" in css_now),
    ("V100 API var", "MuavinV100SpeedToggle" in js_now),
    ("Ana V99 dosyasına V100 gömülmedi", "V100_SPEED_TOGGLE_ISOLATED_START" not in v99_now),
]

for name, ok in checks:
    print(("✅ " if ok else "❌ ") + name)

print()
print("===== TEMPLATE İLGİLİ SATIRLAR =====")
for i, line in enumerate(tpl_now.splitlines(), 1):
    if "continue_speed_toggle_v100" in line or "continue_trip_v99_clean.js" in line:
        print(f"{i}: {line}")

print()
print("===== WEB/ANDROID SHA =====")
for label, a, b in [
    ("template", WEB_TPL, AND_TPL),
    ("v100 js", WEB_JS, AND_JS),
    ("v100 css", WEB_CSS, AND_CSS),
]:
    if a.exists() and b.exists():
        print(f"{label}: {'AYNI' if sha(a)==sha(b) else 'FARKLI'} web={sha(a)} android={sha(b)}")

print()
print("✅ V100 izole hız toggle hazır.")
print("Aç:")
print("http://127.0.0.1:5000/continue-trip?v=v100-speed")
