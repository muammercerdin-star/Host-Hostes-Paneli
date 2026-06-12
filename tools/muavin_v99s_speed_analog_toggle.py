from pathlib import Path
from datetime import datetime
import shutil
import re

ROOT = Path(".").resolve()
STAMP = datetime.now().strftime("%Y%m%d-%H%M%S")

WEB_JS = ROOT / "static/continue/continue_trip_v99_clean.js"
WEB_CSS = ROOT / "static/continue/continue_trip_v99_clean.css"

AND_JS = ROOT / "android_app/app/src/main/python/static/continue/continue_trip_v99_clean.js"
AND_CSS = ROOT / "android_app/app/src/main/python/static/continue/continue_trip_v99_clean.css"

print("===== V99S HIZ DIJITAL / ANALOG IBRE TOGGLE =====")

for p in [WEB_JS, WEB_CSS, AND_JS, AND_CSS]:
    if p.exists():
        bak = p.with_name(p.name + f".bak-v99s-speed-analog-{STAMP}")
        shutil.copy2(p, bak)
        print("📦 backup:", bak)

if not WEB_JS.exists():
    raise SystemExit("❌ JS yok: " + str(WEB_JS))
if not WEB_CSS.exists():
    raise SystemExit("❌ CSS yok: " + str(WEB_CSS))

js = WEB_JS.read_text(encoding="utf-8", errors="ignore")
css = WEB_CSS.read_text(encoding="utf-8", errors="ignore")

# Eski V99S bloklarını temizle
js = re.sub(
    r"\n?/\* V99S_SPEED_ANALOG_TOGGLE_START \*/.*?/\* V99S_SPEED_ANALOG_TOGGLE_END \*/\n?",
    "\n",
    js,
    flags=re.S
)

css = re.sub(
    r"\n?/\* V99S_SPEED_ANALOG_TOGGLE_CSS_START \*/.*?/\* V99S_SPEED_ANALOG_TOGGLE_CSS_END \*/\n?",
    "\n",
    css,
    flags=re.S
)

css_block = r'''

/* V99S_SPEED_ANALOG_TOGGLE_CSS_START */
.v99-speed-toggle-host{
  position:relative !important;
  cursor:pointer !important;
  user-select:none !important;
  -webkit-tap-highlight-color:transparent !important;
}

.v99-speed-toggle-host::after{
  content:"dokun";
  position:absolute;
  right:10px;
  top:8px;
  font-family:"Rajdhani", system-ui, sans-serif;
  font-size:10px;
  letter-spacing:2px;
  text-transform:uppercase;
  color:rgba(224,136,32,.55);
  opacity:.85;
  pointer-events:none;
}

.v99-speed-analog{
  display:none;
  width:88px;
  height:62px;
  margin:0 auto 2px;
  position:relative;
}

.v99-speed-analog .v99-speed-dial{
  position:absolute;
  left:50%;
  top:8px;
  width:76px;
  height:76px;
  transform:translateX(-50%);
  border-radius:50%;
  border:2px solid rgba(224,136,32,.42);
  background:
    radial-gradient(circle at 50% 60%, rgba(224,136,32,.18), transparent 46%),
    linear-gradient(180deg, rgba(20,24,31,.96), rgba(8,10,14,.98));
  box-shadow:
    inset 0 0 18px rgba(0,0,0,.75),
    0 0 18px rgba(224,136,32,.22);
  overflow:hidden;
}

.v99-speed-analog .v99-speed-dial::before{
  content:"";
  position:absolute;
  inset:9px;
  border-radius:50%;
  border:1px dashed rgba(255,255,255,.16);
}

.v99-speed-analog .v99-speed-dial::after{
  content:"0   60   120";
  position:absolute;
  left:0;
  right:0;
  bottom:15px;
  text-align:center;
  font-family:"JetBrains Mono", monospace;
  font-size:9px;
  letter-spacing:1px;
  color:rgba(232,238,248,.62);
}

.v99-speed-needle{
  position:absolute;
  left:50%;
  top:45px;
  width:3px;
  height:31px;
  border-radius:99px;
  background:linear-gradient(180deg, #ffcf5b, #e03030);
  transform-origin:50% 100%;
  transform:translateX(-50%) rotate(-120deg);
  box-shadow:0 0 10px rgba(224,136,32,.75);
  transition:transform .35s cubic-bezier(.2,.8,.2,1);
  z-index:3;
}

.v99-speed-needle-dot{
  position:absolute;
  left:50%;
  top:72px;
  width:13px;
  height:13px;
  transform:translate(-50%,-50%);
  border-radius:50%;
  background:#f3f6fb;
  box-shadow:0 0 12px rgba(255,255,255,.65);
  z-index:4;
}

.v99-speed-analog-num{
  position:absolute;
  left:0;
  right:0;
  top:24px;
  text-align:center;
  font-family:"JetBrains Mono", monospace;
  font-size:20px;
  font-weight:900;
  color:#e08820;
  text-shadow:0 0 12px rgba(224,136,32,.55);
  z-index:5;
}

.v99-speed-analog-unit{
  position:absolute;
  left:0;
  right:0;
  top:47px;
  text-align:center;
  font-family:"Rajdhani", system-ui, sans-serif;
  font-size:10px;
  letter-spacing:2px;
  color:rgba(232,238,248,.58);
  z-index:5;
}

.v99-speed-toggle-host.v99-speed-analog-on #v99SpeedVal{
  display:none !important;
}

.v99-speed-toggle-host.v99-speed-analog-on .v99-speed-analog{
  display:block !important;
}

.v99-speed-toggle-host.v99-speed-analog-on::after{
  content:"analog";
  color:rgba(224,136,32,.9);
}

.v99-speed-toggle-host.v99-speed-analog-on{
  background:
    radial-gradient(circle at 50% 45%, rgba(224,136,32,.13), transparent 55%),
    rgba(14,18,25,.92) !important;
}
/* V99S_SPEED_ANALOG_TOGGLE_CSS_END */
'''

js_block = r'''

/* V99S_SPEED_ANALOG_TOGGLE_START */
(function(){
  "use strict";

  function q(sel){
    return document.querySelector(sel);
  }

  function parseSpeed(raw){
    var s = String(raw || "")
      .replace(",", ".")
      .replace(/km\/sa|km\/h|kmh|km|sa/gi, " ")
      .trim();

    var m = s.match(/-?\d+(?:\.\d+)?/);
    if(!m) return 0;

    var n = Number(m[0]);
    if(!Number.isFinite(n) || n < 0) return 0;
    if(n > 160) n = 160;
    return n;
  }

  function readSpeed(){
    var visual = q("#v99SpeedVal");
    var hidden = q("#liveSpeedText");

    var n = parseSpeed(visual ? visual.textContent : "");
    if(!n && hidden) n = parseSpeed(hidden.textContent);

    return n;
  }

  function findSpeedHost(speedEl){
    if(!speedEl) return null;

    var host =
      speedEl.closest(".v99-mini-card") ||
      speedEl.closest(".v99-stat") ||
      speedEl.closest(".v99-top-cell") ||
      speedEl.parentElement;

    return host;
  }

  function ensureAnalog(host){
    if(!host) return null;

    var old = host.querySelector(".v99-speed-analog");
    if(old) return old;

    var analog = document.createElement("div");
    analog.className = "v99-speed-analog";
    analog.innerHTML = ''
      + '<div class="v99-speed-dial"></div>'
      + '<div class="v99-speed-needle"></div>'
      + '<div class="v99-speed-needle-dot"></div>'
      + '<div class="v99-speed-analog-num">0</div>'
      + '<div class="v99-speed-analog-unit">km/sa</div>';

    var speedEl = q("#v99SpeedVal");
    if(speedEl && speedEl.parentElement === host){
      speedEl.insertAdjacentElement("afterend", analog);
    }else{
      host.appendChild(analog);
    }

    return analog;
  }

  function paint(){
    var host = window.MuavinV99SpeedHost || null;
    if(!host) return;

    var analog = host.querySelector(".v99-speed-analog");
    if(!analog) return;

    var speed = readSpeed();
    var shown = Math.round(speed);

    var needle = analog.querySelector(".v99-speed-needle");
    var num = analog.querySelector(".v99-speed-analog-num");

    var max = 120;
    var clamped = Math.max(0, Math.min(max, speed));
    var deg = -120 + ((clamped / max) * 240);

    if(needle){
      needle.style.transform = "translateX(-50%) rotate(" + deg.toFixed(1) + "deg)";
    }

    if(num){
      num.textContent = String(shown);
      if(shown <= 50){
        num.style.color = "#22c76a";
        num.style.textShadow = "0 0 12px rgba(34,199,106,.55)";
      }else if(shown <= 90){
        num.style.color = "#e08820";
        num.style.textShadow = "0 0 12px rgba(224,136,32,.55)";
      }else{
        num.style.color = "#e03030";
        num.style.textShadow = "0 0 14px rgba(224,48,48,.72)";
      }
    }
  }

  function boot(){
    var speedEl = q("#v99SpeedVal");
    if(!speedEl) return;

    var host = findSpeedHost(speedEl);
    if(!host) return;

    window.MuavinV99SpeedHost = host;

    host.classList.add("v99-speed-toggle-host");
    ensureAnalog(host);
    paint();

    if(!host.dataset.v99SpeedToggleBound){
      host.dataset.v99SpeedToggleBound = "1";

      host.addEventListener("click", function(ev){
        ev.preventDefault();
        ev.stopPropagation();

        host.classList.toggle("v99-speed-analog-on");
        paint();
      }, true);
    }
  }

  if(document.readyState === "loading"){
    document.addEventListener("DOMContentLoaded", boot);
  }else{
    boot();
  }

  window.addEventListener("load", boot);
  document.addEventListener("continueEtaUpdated", paint);

  setInterval(function(){
    boot();
    paint();
  }, 600);
})();
/* V99S_SPEED_ANALOG_TOGGLE_END */
'''

WEB_CSS.write_text(css.rstrip() + css_block + "\n", encoding="utf-8")
WEB_JS.write_text(js.rstrip() + js_block + "\n", encoding="utf-8")

print("✅ web CSS yazıldı:", WEB_CSS)
print("✅ web JS yazıldı:", WEB_JS)

if AND_CSS.parent.exists():
    shutil.copy2(WEB_CSS, AND_CSS)
    print("✅ android CSS senkron:", AND_CSS)

if AND_JS.parent.exists():
    shutil.copy2(WEB_JS, AND_JS)
    print("✅ android JS senkron:", AND_JS)

print()
print("===== KONTROL =====")
for p in [WEB_CSS, WEB_JS]:
    txt = p.read_text(encoding="utf-8", errors="ignore")
    print(p.name)
    for key in [
        "V99S_SPEED_ANALOG_TOGGLE",
        "v99-speed-analog",
        "v99-speed-needle",
        "v99-speed-analog-on",
    ]:
        print(("  VAR  " if key in txt else "  YOK  ") + key)

print()
print("✅ Bitti. /continue-trip?v=v99s-speed-analog ile yenile.")
