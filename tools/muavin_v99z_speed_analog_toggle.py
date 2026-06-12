from pathlib import Path
from datetime import datetime
import shutil
import subprocess

ROOT = Path(".").resolve()
STAMP = datetime.now().strftime("%Y%m%d-%H%M%S")

WEB_JS = ROOT / "static/continue/continue_trip_v99_clean.js"
AND_JS = ROOT / "android_app/app/src/main/python/static/continue/continue_trip_v99_clean.js"

WEB_CSS = ROOT / "static/continue/continue_trip_v99_clean.css"
AND_CSS = ROOT / "android_app/app/src/main/python/static/continue/continue_trip_v99_clean.css"

print("===== V99Z HIZ ANALOG / DİJİTAL TOGGLE =====")

for p in [WEB_JS, AND_JS, WEB_CSS, AND_CSS]:
    if p.exists():
        bak = p.with_name(p.name + f".bak-v99z-speed-toggle-{STAMP}")
        shutil.copy2(p, bak)
        print("📦 backup:", bak)

if not WEB_JS.exists():
    raise SystemExit("❌ JS yok: " + str(WEB_JS))
if not WEB_CSS.exists():
    raise SystemExit("❌ CSS yok: " + str(WEB_CSS))

js = WEB_JS.read_text(encoding="utf-8", errors="ignore")
css = WEB_CSS.read_text(encoding="utf-8", errors="ignore")

JS_START = "/* V99Z_SPEED_ANALOG_TOGGLE_START */"
JS_END   = "/* V99Z_SPEED_ANALOG_TOGGLE_END */"
CSS_START = "/* V99Z_SPEED_ANALOG_TOGGLE_CSS_START */"
CSS_END   = "/* V99Z_SPEED_ANALOG_TOGGLE_CSS_END */"

js_block = r'''
/* V99Z_SPEED_ANALOG_TOGGLE_START */
(function(){
  "use strict";

  function q(sel, root){
    return (root || document).querySelector(sel);
  }

  function qa(sel, root){
    return Array.prototype.slice.call((root || document).querySelectorAll(sel));
  }

  function txt(el){
    return el ? String(el.textContent || "").trim() : "";
  }

  function findSpeedCard(){
    var cells = qa(".v99-gauges .v99-gauge-cell");
    for(var i = 0; i < cells.length; i++){
      var label = q(".v99-gauge-label", cells[i]);
      var t = txt(label).toLocaleUpperCase("tr-TR");
      if(t === "HIZ"){
        return cells[i];
      }
    }
    return null;
  }

  function speedValue(){
    var raw = "";
    var speedEl = q("#v99SpeedVal");
    var hiddenEl = q("#liveSpeedText");

    if(speedEl) raw = txt(speedEl);
    if(!raw && hiddenEl) raw = txt(hiddenEl);

    raw = String(raw || "")
      .replace(",", ".")
      .replace(/[^\d.]/g, "");

    var n = Number(raw);
    return Number.isFinite(n) ? n : 0;
  }

  function ensureAnalogUI(){
    var card = findSpeedCard();
    if(!card) return null;

    card.classList.add("v99z-speed-card");
    card.setAttribute("title", "Hız görünümünü değiştir");

    if(!q(".v99z-speed-analog", card)){
      var analog = document.createElement("div");
      analog.className = "v99z-speed-analog";
      analog.innerHTML = `
        <div class="v99z-speed-dial">
          <div class="v99z-speed-arc"></div>
          <div class="v99z-speed-needle"></div>
          <div class="v99z-speed-center"></div>
          <div class="v99z-speed-readout">0</div>
        </div>
        <div class="v99z-speed-mode">analog</div>
      `;
      card.appendChild(analog);
    }

    if(!card.getAttribute("data-v99z-speed-bound")){
      card.setAttribute("data-v99z-speed-bound", "1");
      card.addEventListener("click", function(e){
        if(e.target.closest("button, a")) return;
        card.classList.toggle("v99z-analog-on");
        syncAnalog();
      }, true);
    }

    return card;
  }

  function syncAnalog(){
    var card = ensureAnalogUI();
    if(!card) return;

    var n = speedValue();
    var max = 140;
    var ratio = Math.max(0, Math.min(n, max)) / max;
    var angle = -120 + (ratio * 240);

    card.style.setProperty("--v99z-needle-angle", angle + "deg");

    var readout = q(".v99z-speed-readout", card);
    if(readout){
      readout.textContent = String(Math.round(n));
    }
  }

  function boot(){
    ensureAnalogUI();
    syncAnalog();

    try{
      var speedEl = document.getElementById("v99SpeedVal");
      if(speedEl){
        var mo = new MutationObserver(function(){
          syncAnalog();
        });
        mo.observe(speedEl, {
          childList: true,
          subtree: true,
          characterData: true
        });
      }
    }catch(_){}
  }

  document.addEventListener("DOMContentLoaded", boot);
  window.addEventListener("load", boot);
  document.addEventListener("continueEtaUpdated", syncAnalog);

  var left = 180;
  var timer = setInterval(function(){
    syncAnalog();
    left--;
    if(left <= 0) clearInterval(timer);
  }, 1000);

  window.MuavinV99SpeedToggle = {
    sync: syncAnalog
  };
})();
/* V99Z_SPEED_ANALOG_TOGGLE_END */
'''

css_block = r'''
/* V99Z_SPEED_ANALOG_TOGGLE_CSS_START */

.v99z-speed-card{
  cursor:pointer !important;
  user-select:none;
  -webkit-user-select:none;
}

.v99z-speed-card .v99z-speed-analog{
  display:none;
  margin-top:6px;
  align-items:center;
  justify-content:center;
  flex-direction:column;
  gap:4px;
}

.v99z-speed-card.v99z-analog-on .v99-gauge-val,
.v99z-speed-card.v99z-analog-on .v99-gauge-unit,
.v99z-speed-card.v99z-analog-on #liveSpeedText{
  display:none !important;
}

.v99z-speed-card.v99z-analog-on .v99z-speed-analog{
  display:flex;
}

.v99z-speed-dial{
  position:relative;
  width:74px;
  height:40px;
  border-top-left-radius:74px;
  border-top-right-radius:74px;
  overflow:hidden;
  border:1px solid rgba(255,255,255,.12);
  border-bottom:none;
  background:
    radial-gradient(circle at 50% 100%, rgba(255,176,71,.16), transparent 58%),
    linear-gradient(180deg, rgba(255,255,255,.05), rgba(255,255,255,.01));
}

.v99z-speed-arc{
  position:absolute;
  left:7px;
  right:7px;
  top:7px;
  bottom:7px;
  border-top-left-radius:72px;
  border-top-right-radius:72px;
  border:3px solid rgba(255,176,71,.55);
  border-bottom:none;
}

.v99z-speed-needle{
  position:absolute;
  left:50%;
  bottom:4px;
  width:2px;
  height:30px;
  background:#ffb347;
  transform-origin:50% calc(100% - 2px);
  transform:translateX(-50%) rotate(var(--v99z-needle-angle, -120deg));
  box-shadow:0 0 10px rgba(255,179,71,.6);
  border-radius:2px;
}

.v99z-speed-center{
  position:absolute;
  left:50%;
  bottom:3px;
  width:10px;
  height:10px;
  border-radius:50%;
  background:#ffd39a;
  transform:translateX(-50%);
  box-shadow:0 0 10px rgba(255,211,154,.45);
}

.v99z-speed-readout{
  position:absolute;
  left:50%;
  bottom:12px;
  transform:translateX(-50%);
  font-family:'JetBrains Mono', monospace;
  font-size:12px;
  font-weight:800;
  color:#ffb347;
  letter-spacing:1px;
  line-height:1;
}

.v99z-speed-mode{
  font-size:10px;
  color:var(--v99-muted);
  letter-spacing:2px;
  text-transform:uppercase;
  font-family:'JetBrains Mono', monospace;
}

/* V99Z_SPEED_ANALOG_TOGGLE_CSS_END */
'''

if JS_START not in js:
    js = js.rstrip() + "\n\n" + js_block.strip() + "\n"
    WEB_JS.write_text(js, encoding="utf-8")
    print("✅ Web JS eklendi")
else:
    print("ℹ️ JS blok zaten var")

if CSS_START not in css:
    css = css.rstrip() + "\n\n" + css_block.strip() + "\n"
    WEB_CSS.write_text(css, encoding="utf-8")
    print("✅ Web CSS eklendi")
else:
    print("ℹ️ CSS blok zaten var")

if AND_JS.parent.exists():
    shutil.copy2(WEB_JS, AND_JS)
    print("✅ Android JS senkronlandı")

if AND_CSS.parent.exists():
    shutil.copy2(WEB_CSS, AND_CSS)
    print("✅ Android CSS senkronlandı")

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
    print("ℹ️ node yok, syntax check atlandı")

print()
print("===== KONTROL =====")
new_js = WEB_JS.read_text(encoding="utf-8", errors="ignore")
new_css = WEB_CSS.read_text(encoding="utf-8", errors="ignore")

checks = [
    ("JS marker var", JS_START in new_js and JS_END in new_js),
    ("CSS marker var", CSS_START in new_css and CSS_END in new_css),
    ("Toggle API var", "MuavinV99SpeedToggle" in new_js),
    ("Analog class var", ".v99z-speed-card" in new_css),
]
for name, ok in checks:
    print(("✅ " if ok else "❌ ") + name)

print()
print("✅ V99Z hız analog/dijital toggle hazır")
print("Yenile:")
print("http://127.0.0.1:5000/continue-trip?v=v99z-speed-toggle")
