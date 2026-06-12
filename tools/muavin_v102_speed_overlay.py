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

WEB_JS = ROOT / "static/continue/continue_speed_overlay_v102.js"
AND_JS = ROOT / "android_app/app/src/main/python/static/continue/continue_speed_overlay_v102.js"

WEB_CSS = ROOT / "static/continue/continue_speed_overlay_v102.css"
AND_CSS = ROOT / "android_app/app/src/main/python/static/continue/continue_speed_overlay_v102.css"

print("===== V102 HIZ OVERLAY MODU =====")

def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()[:12] if p.exists() else "-"

for p in [WEB_TPL, AND_TPL, WEB_JS, AND_JS, WEB_CSS, AND_CSS]:
    if p.exists():
        bak = p.with_name(p.name + f".bak-v102-speed-overlay-{STAMP}")
        shutil.copy2(p, bak)
        print("📦 backup:", bak)

if not WEB_TPL.exists():
    raise SystemExit("❌ template yok")

WEB_JS.parent.mkdir(parents=True, exist_ok=True)
WEB_CSS.parent.mkdir(parents=True, exist_ok=True)

css = r'''
/* V102_SPEED_OVERLAY_START */
.v102-speed-card{
  position:relative !important;
  overflow:hidden !important;
  cursor:pointer !important;
  user-select:none !important;
  -webkit-user-select:none !important;
  touch-action:manipulation !important;
}

.v102-speed-card .v99-gauge-label,
.v102-speed-card .v99-gauge-val,
.v102-speed-card .v99-gauge-unit{
  position:relative !important;
  z-index:4 !important;
}

.v102-speed-overlay{
  position:absolute;
  inset:0;
  z-index:1;
  pointer-events:none;
  opacity:.75;
}

.v102-speed-card::after{
  content:"";
  position:absolute;
  inset:6px;
  border-radius:16px;
  border:1px solid rgba(224,136,32,0);
  box-shadow:none;
  pointer-events:none;
  transition:.18s ease;
  z-index:2;
}

.v102-speed-card:active::after{
  border-color:rgba(224,136,32,.38);
  box-shadow:0 0 18px rgba(224,136,32,.18);
}

.v102-speed-bar{
  position:absolute;
  left:13px;
  right:13px;
  bottom:6px;
  height:3px;
  border-radius:999px;
  background:rgba(255,255,255,.10);
  overflow:hidden;
}

.v102-speed-fill{
  width:0%;
  height:100%;
  border-radius:999px;
  background:linear-gradient(90deg,#1db87a 0%,#e08820 58%,#e03030 100%);
  box-shadow:0 0 10px rgba(224,136,32,.24);
  transition:width .22s ease;
}

.v102-speed-arc,
.v102-speed-needle,
.v102-speed-dot{
  opacity:0;
  transition:opacity .18s ease, transform .24s ease;
}

.v102-speed-arc{
  position:absolute;
  left:50%;
  top:27px;
  width:82px;
  height:42px;
  transform:translateX(-50%);
  border-radius:82px 82px 0 0;
  border:3px solid rgba(224,136,32,.62);
  border-bottom:0;
  box-shadow:
    0 0 16px rgba(224,136,32,.20),
    inset 0 0 14px rgba(224,136,32,.08);
}

.v102-speed-needle{
  position:absolute;
  left:50%;
  top:31px;
  width:3px;
  height:34px;
  border-radius:99px;
  background:linear-gradient(180deg,#ffe7ad,#e08820);
  transform-origin:50% 100%;
  transform:translateX(-50%) rotate(var(--v102-speed-deg, -115deg));
  box-shadow:0 0 10px rgba(224,136,32,.45);
}

.v102-speed-dot{
  position:absolute;
  left:50%;
  top:60px;
  width:10px;
  height:10px;
  border-radius:50%;
  transform:translateX(-50%);
  background:#ffe0a5;
  box-shadow:0 0 12px rgba(255,224,165,.42);
}

.v102-speed-card.v102-speed-analog-on{
  background:
    radial-gradient(circle at 50% 64%, rgba(224,136,32,.13), transparent 50%),
    var(--v99-panel) !important;
}

.v102-speed-card.v102-speed-analog-on .v102-speed-arc,
.v102-speed-card.v102-speed-analog-on .v102-speed-needle,
.v102-speed-card.v102-speed-analog-on .v102-speed-dot{
  opacity:1;
}

.v102-speed-card.v102-speed-analog-on .v102-speed-bar{
  opacity:.55;
}

.v102-speed-card.v102-low .v102-speed-arc{
  border-color:rgba(29,184,122,.70);
  box-shadow:0 0 14px rgba(29,184,122,.18);
}

.v102-speed-card.v102-low .v102-speed-needle{
  background:linear-gradient(180deg,#bfffe2,#1db87a);
  box-shadow:0 0 10px rgba(29,184,122,.40);
}

.v102-speed-card.v102-high .v102-speed-arc{
  border-color:rgba(224,48,48,.72);
  box-shadow:0 0 14px rgba(224,48,48,.24);
}

.v102-speed-card.v102-high .v102-speed-needle{
  background:linear-gradient(180deg,#ffd0d0,#e03030);
  box-shadow:0 0 12px rgba(224,48,48,.48);
}
/* V102_SPEED_OVERLAY_END */
'''.strip() + "\n"

js = r'''
/* V102_SPEED_OVERLAY_START */
(function(){
  "use strict";

  if(window.__MUAVIN_V102_SPEED_OVERLAY__) return;
  window.__MUAVIN_V102_SPEED_OVERLAY__ = true;

  var STORE_KEY = "muavin.v102.speed.overlay.mode";

  function q(sel, root){
    return (root || document).querySelector(sel);
  }

  function qa(sel, root){
    return Array.prototype.slice.call((root || document).querySelectorAll(sel));
  }

  function norm(v){
    return String(v || "")
      .toLocaleUpperCase("tr-TR")
      .replace(/\s+/g, " ")
      .trim();
  }

  function text(el){
    return el ? String(el.textContent || "").trim() : "";
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

  function parseSpeed(v){
    var raw = String(v || "")
      .replace(",", ".")
      .replace(/km\/sa|km\/h|kmh|km|sa/gi, " ")
      .trim();

    var m = raw.match(/-?\d+(\.\d+)?/);
    if(!m) return 0;

    var n = Number(m[0]);
    if(!Number.isFinite(n)) n = 0;
    if(n < 0) n = 0;
    if(n > 180) n = 180;
    return n;
  }

  function readSpeed(){
    var visible = q("#v99SpeedVal");
    var hidden = q("#liveSpeedText");

    var n = parseSpeed(text(visible));
    if(!n && hidden){
      n = parseSpeed(text(hidden));
    }

    return n;
  }

  function savedMode(){
    try{
      return localStorage.getItem(STORE_KEY) === "analog" ? "analog" : "digital";
    }catch(_){
      return "digital";
    }
  }

  function saveMode(mode){
    try{
      localStorage.setItem(STORE_KEY, mode);
    }catch(_){}
  }

  function ensureOverlay(card){
    if(!card) return;

    card.classList.add("v102-speed-card");

    if(!q(".v102-speed-overlay", card)){
      var overlay = document.createElement("div");
      overlay.className = "v102-speed-overlay";
      overlay.setAttribute("aria-hidden", "true");
      overlay.innerHTML = ''
        + '<div class="v102-speed-arc"></div>'
        + '<div class="v102-speed-needle"></div>'
        + '<div class="v102-speed-dot"></div>'
        + '<div class="v102-speed-bar"><div class="v102-speed-fill"></div></div>';
      card.appendChild(overlay);
    }

    if(!card.dataset.v102ModeReady){
      card.dataset.v102ModeReady = "1";
      if(savedMode() === "analog"){
        card.classList.add("v102-speed-analog-on");
      }
    }

    if(!card.dataset.v102Bound){
      card.dataset.v102Bound = "1";

      card.addEventListener("click", function(ev){
        ev.preventDefault();
        ev.stopPropagation();

        card.classList.toggle("v102-speed-analog-on");
        saveMode(card.classList.contains("v102-speed-analog-on") ? "analog" : "digital");
        paint();
      }, true);
    }
  }

  function paint(){
    var card = findSpeedCard();
    if(!card) return;

    ensureOverlay(card);

    var speed = readSpeed();
    var capped = Math.max(0, Math.min(speed, 140));
    var pct = capped / 140;
    var deg = -115 + (pct * 230);

    card.style.setProperty("--v102-speed-deg", deg.toFixed(1) + "deg");

    var fill = q(".v102-speed-fill", card);
    if(fill){
      fill.style.width = (pct * 100).toFixed(1) + "%";
    }

    card.classList.toggle("v102-low", speed < 50);
    card.classList.toggle("v102-high", speed >= 95);
  }

  function boot(){
    var card = findSpeedCard();
    if(card){
      ensureOverlay(card);
      paint();
    }

    try{
      var a = q("#v99SpeedVal");
      if(a && !a.dataset.v102Observed){
        a.dataset.v102Observed = "1";
        new MutationObserver(paint).observe(a, {
          childList:true,
          subtree:true,
          characterData:true
        });
      }

      var b = q("#liveSpeedText");
      if(b && !b.dataset.v102Observed){
        b.dataset.v102Observed = "1";
        new MutationObserver(paint).observe(b, {
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
    paint();
    tries--;
    if(tries <= 0) clearInterval(timer);
  }, 500);

  window.MuavinV102SpeedOverlay = {
    boot: boot,
    paint: paint
  };
})();
/* V102_SPEED_OVERLAY_END */
'''.strip() + "\n"

WEB_CSS.write_text(css, encoding="utf-8")
WEB_JS.write_text(js, encoding="utf-8")

print("✅ web CSS yazıldı:", WEB_CSS)
print("✅ web JS yazıldı:", WEB_JS)

# Android sync
AND_CSS.parent.mkdir(parents=True, exist_ok=True)
AND_JS.parent.mkdir(parents=True, exist_ok=True)
shutil.copy2(WEB_CSS, AND_CSS)
shutil.copy2(WEB_JS, AND_JS)
print("✅ android CSS/JS senkron")

css_tag = """<link rel="stylesheet" href="{{ url_for('static', filename='continue/continue_speed_overlay_v102.css') }}?v=v102-{{ trip['id'] }}">"""
js_tag = """<script src="{{ url_for('static', filename='continue/continue_speed_overlay_v102.js') }}?v=v102-{{ trip['id'] }}"></script>"""

def patch_tpl(p):
    s = p.read_text(encoding="utf-8", errors="ignore")
    old = s

    s = re.sub(r'\n?\s*<link[^>]+continue_speed_overlay_v102\.css[^>]*>\s*', "\n", s)
    s = re.sub(r'\n?\s*<script[^>]+continue_speed_overlay_v102\.js[^>]*></script>\s*', "\n", s)

    if "</head>" in s:
        s = s.replace("</head>", css_tag + "\n</head>")
    else:
        s = css_tag + "\n" + s

    if "</body>" in s:
        s = s.replace("</body>", js_tag + "\n</body>")
    else:
        s = s.rstrip() + "\n" + js_tag + "\n"

    p.write_text(s, encoding="utf-8")
    print("✅ template patch:", p, "changed=", s != old)

for p in [WEB_TPL, AND_TPL]:
    patch_tpl(p)

print()
print("===== NODE JS SYNTAX CHECK =====")
try:
    res = subprocess.run(["node", "--check", str(WEB_JS)], capture_output=True, text=True)
    if res.returncode == 0:
        print("✅ JS syntax OK")
    else:
        print("❌ JS syntax HATA")
        print(res.stdout)
        print(res.stderr)
except FileNotFoundError:
    print("ℹ️ node yok, atlandı")

print()
print("===== KONTROL =====")
tpl = WEB_TPL.read_text(encoding="utf-8", errors="ignore")
js2 = WEB_JS.read_text(encoding="utf-8", errors="ignore")
css2 = WEB_CSS.read_text(encoding="utf-8", errors="ignore")

checks = [
    ("template CSS link var", "continue_speed_overlay_v102.css" in tpl),
    ("template JS script var", "continue_speed_overlay_v102.js" in tpl),
    ("JS marker var", "V102_SPEED_OVERLAY_START" in js2),
    ("CSS marker var", "V102_SPEED_OVERLAY_START" in css2),
    ("API var", "MuavinV102SpeedOverlay" in js2),
]

for name, ok in checks:
    print(("✅ " if ok else "❌ ") + name)

print()
print("===== TEMPLATE SATIRLARI =====")
for i, line in enumerate(tpl.splitlines(), 1):
    if "continue_speed_overlay_v102" in line or "continue_trip_v99_clean.js" in line:
        print(f"{i}: {line}")

print()
print("===== SHA =====")
for label, a, b in [
    ("template", WEB_TPL, AND_TPL),
    ("v102 js", WEB_JS, AND_JS),
    ("v102 css", WEB_CSS, AND_CSS),
]:
    print(f"{label}: {'AYNI' if sha(a)==sha(b) else 'FARKLI'} web={sha(a)} android={sha(b)}")

print()
print("✅ V102 overlay hız modu hazır.")
print("Aç:")
print("http://127.0.0.1:5000/continue-trip?v=v102-speed-overlay")
