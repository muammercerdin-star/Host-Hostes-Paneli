from pathlib import Path
from datetime import datetime
import shutil
import hashlib

ROOT = Path(".").resolve()
STAMP = datetime.now().strftime("%Y%m%d-%H%M%S")

WEB_TPL = ROOT / "templates/continue_trip.html"
AND_TPL = ROOT / "android_app/app/src/main/python/templates/continue_trip.html"

WEB_JS = ROOT / "static/continue/continue_speed_widget_v101.js"
AND_JS = ROOT / "android_app/app/src/main/python/static/continue/continue_speed_widget_v101.js"

WEB_CSS = ROOT / "static/continue/continue_speed_widget_v101.css"
AND_CSS = ROOT / "android_app/app/src/main/python/static/continue/continue_speed_widget_v101.css"

print("===== V101 KOMPAKT HIZ WIDGET PAKETİ =====")

def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()[:12] if p.exists() else "-"

def backup(p):
    if p.exists():
        bak = p.with_name(p.name + f".bak-v101-speed-widget-{STAMP}")
        shutil.copy2(p, bak)
        print("📦 backup:", bak)

for p in [WEB_TPL, AND_TPL, WEB_JS, AND_JS, WEB_CSS, AND_CSS]:
    if p.parent.exists():
        backup(p)

css_text = r'''
/* V101_SPEED_WIDGET_START */
.v101-speed-card{
  position:relative !important;
  cursor:pointer;
  user-select:none;
  -webkit-user-select:none;
  overflow:hidden;
}

.v101-speed-card .v99-gauge-label{
  position:relative;
  z-index:2;
}

.v101-speed-card .v99-gauge-val,
.v101-speed-card .v99-gauge-unit{
  position:relative;
  z-index:2;
}

.v101-speed-card .v99-gauge-val{
  transition:.18s ease;
}

.v101-speed-card .v101-speed-bar{
  width:100%;
  max-width:92px;
  margin-top:2px;
  position:relative;
  z-index:2;
}

.v101-speed-card .v101-speed-bar-track{
  width:100%;
  height:5px;
  border-radius:999px;
  background:rgba(255,255,255,.10);
  overflow:hidden;
  box-shadow:inset 0 1px 2px rgba(0,0,0,.35);
}

.v101-speed-card .v101-speed-bar-fill{
  width:0%;
  height:100%;
  border-radius:999px;
  background:linear-gradient(90deg,#1db87a 0%, #e6a23c 58%, #ff6b57 100%);
  box-shadow:0 0 12px rgba(230,162,60,.22);
  transition:width .22s ease;
}

.v101-speed-card .v101-speed-bar-scale{
  margin-top:3px;
  display:flex;
  justify-content:space-between;
  font-size:8px;
  letter-spacing:.7px;
  color:rgba(255,255,255,.38);
  font-family:'JetBrains Mono',monospace;
}

.v101-speed-card .v101-speed-hint{
  margin-top:2px;
  font-size:8px;
  color:rgba(255,255,255,.32);
  letter-spacing:.8px;
  line-height:1;
  position:relative;
  z-index:2;
}

.v101-speed-card .v101-analog{
  display:none;
  width:100%;
  height:70px;
  position:relative;
  margin-top:2px;
  z-index:2;
  pointer-events:none;
}

.v101-speed-card .v101-analog-face{
  width:100%;
  height:100%;
  position:relative;
}

.v101-speed-card .v101-arc{
  position:absolute;
  left:50%;
  top:4px;
  width:78px;
  height:39px;
  transform:translateX(-50%);
  border:4px solid rgba(255,255,255,.10);
  border-bottom:none;
  border-radius:78px 78px 0 0;
  box-sizing:border-box;
}

.v101-speed-card .v101-arc-glow{
  position:absolute;
  left:50%;
  top:4px;
  width:78px;
  height:39px;
  transform:translateX(-50%);
  border:4px solid transparent;
  border-bottom:none;
  border-radius:78px 78px 0 0;
  box-sizing:border-box;
  border-top-color:rgba(29,184,122,.85);
  border-left-color:rgba(29,184,122,.85);
  border-right-color:rgba(230,162,60,.85);
  filter:drop-shadow(0 0 8px rgba(29,184,122,.20));
  opacity:.92;
}

.v101-speed-card .v101-needle-wrap{
  position:absolute;
  left:50%;
  top:43px;
  width:0;
  height:0;
  transform:translateX(-50%) rotate(-88deg);
  transform-origin:center center;
  transition:transform .22s ease;
}

.v101-speed-card .v101-needle{
  position:absolute;
  left:-2px;
  top:-2px;
  width:3px;
  height:29px;
  border-radius:999px;
  background:linear-gradient(180deg,#ffe3a0 0%, #f0a33f 100%);
  transform:translateY(-27px);
  box-shadow:0 0 10px rgba(240,163,63,.35);
}

.v101-speed-card .v101-center-dot{
  position:absolute;
  left:50%;
  top:39px;
  width:12px;
  height:12px;
  transform:translateX(-50%);
  border-radius:50%;
  background:#f5d49a;
  box-shadow:0 0 10px rgba(245,212,154,.28);
}

.v101-speed-card .v101-analog-number{
  position:absolute;
  left:50%;
  top:24px;
  transform:translateX(-50%);
  font-family:'JetBrains Mono',monospace;
  font-size:18px;
  font-weight:700;
  color:#f0b548;
  line-height:1;
  text-shadow:0 0 10px rgba(240,181,72,.20);
}

.v101-speed-card .v101-analog-unit{
  position:absolute;
  left:50%;
  top:46px;
  transform:translateX(-50%);
  font-size:8px;
  color:rgba(255,255,255,.46);
  letter-spacing:1.2px;
  font-family:'JetBrains Mono',monospace;
}

.v101-speed-card .v101-scale-0,
.v101-speed-card .v101-scale-70,
.v101-speed-card .v101-scale-140{
  position:absolute;
  top:10px;
  font-size:9px;
  color:rgba(255,255,255,.50);
  font-family:'JetBrains Mono',monospace;
  line-height:1;
}

.v101-speed-card .v101-scale-0{ left:18px; }
.v101-speed-card .v101-scale-70{ left:50%; transform:translateX(-50%); }
.v101-speed-card .v101-scale-140{ right:18px; }

.v101-speed-card.v101-mode-analog{
  padding-top:10px !important;
  padding-bottom:10px !important;
  gap:1px !important;
}

.v101-speed-card.v101-mode-analog .v99-gauge-val,
.v101-speed-card.v101-mode-analog .v99-gauge-unit,
.v101-speed-card.v101-mode-analog .v101-speed-bar{
  display:none !important;
}

.v101-speed-card.v101-mode-analog .v101-analog{
  display:block !important;
}

.v101-speed-card.v101-mode-analog .v101-speed-hint{
  margin-top:0;
}

.v101-speed-card.v101-mode-digital .v101-analog{
  display:none !important;
}

.v101-speed-card.v101-mode-digital .v101-speed-bar{
  display:block !important;
}
/* V101_SPEED_WIDGET_END */
'''.strip() + "\n"

js_text = r'''
/* V101_SPEED_WIDGET_START */
(function(){
  "use strict";

  var KEY = "muavin_v101_speed_mode";

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

  function clamp(n, min, max){
    return Math.max(min, Math.min(max, n));
  }

  function parseSpeed(v){
    var m = String(v || "").replace(",", ".").match(/-?\d+(\.\d+)?/);
    if(!m) return 0;
    var n = Number(m[0]);
    return Number.isFinite(n) ? Math.round(Math.max(0, n)) : 0;
  }

  function loadMode(){
    try{
      return localStorage.getItem(KEY) === "analog" ? "analog" : "digital";
    }catch(_){
      return "digital";
    }
  }

  function saveMode(mode){
    try{
      localStorage.setItem(KEY, mode);
    }catch(_){}
  }

  function findSpeedCard(){
    var cells = qa(".v99-gauge-cell");
    for(var i=0; i<cells.length; i++){
      var label = q(".v99-gauge-label", cells[i]);
      if(norm(label ? label.textContent : "") === "HIZ"){
        return cells[i];
      }
    }
    return null;
  }

  function applyMode(card, mode){
    if(!card) return;
    card.classList.toggle("v101-mode-analog", mode === "analog");
    card.classList.toggle("v101-mode-digital", mode !== "analog");
  }

  function toggleMode(card){
    if(!card) return;
    var next = card.classList.contains("v101-mode-analog") ? "digital" : "analog";
    applyMode(card, next);
    saveMode(next);
  }

  function ensureMarkup(card){
    if(!card || card.dataset.v101Ready === "1") return;

    card.dataset.v101Ready = "1";
    card.classList.add("v101-speed-card");
    card.classList.add("v101-mode-" + loadMode());
    card.setAttribute("role", "button");
    card.setAttribute("tabindex", "0");
    card.setAttribute("aria-label", "Hız görünümünü değiştir");

    var bar = document.createElement("div");
    bar.className = "v101-speed-bar";
    bar.innerHTML = ''
      + '<div class="v101-speed-bar-track"><div class="v101-speed-bar-fill"></div></div>'
      + '<div class="v101-speed-bar-scale"><span>0</span><span>70</span><span>140</span></div>';

    var analog = document.createElement("div");
    analog.className = "v101-analog";
    analog.innerHTML = ''
      + '<div class="v101-analog-face">'
      +   '<div class="v101-scale-0">0</div>'
      +   '<div class="v101-scale-70">70</div>'
      +   '<div class="v101-scale-140">140</div>'
      +   '<div class="v101-arc"></div>'
      +   '<div class="v101-arc-glow"></div>'
      +   '<div class="v101-needle-wrap"><div class="v101-needle"></div></div>'
      +   '<div class="v101-center-dot"></div>'
      +   '<div class="v101-analog-number">0</div>'
      +   '<div class="v101-analog-unit">km/sa</div>'
      + '</div>';

    var hint = document.createElement("div");
    hint.className = "v101-speed-hint";
    hint.textContent = "dokun: dijital / analog";

    card.appendChild(bar);
    card.appendChild(analog);
    card.appendChild(hint);

    card.addEventListener("click", function(e){
      e.preventDefault();
      toggleMode(card);
    });

    card.addEventListener("keydown", function(e){
      if(e.key === "Enter" || e.key === " "){
        e.preventDefault();
        toggleMode(card);
      }
    });

    applyMode(card, loadMode());
  }

  function sync(){
    var card = findSpeedCard();
    if(!card) return;

    ensureMarkup(card);

    var valEl = q("#v99SpeedVal", card) || document.getElementById("v99SpeedVal");
    var raw = (q("#liveSpeedText") ? q("#liveSpeedText").textContent : "") || (valEl ? valEl.textContent : "0");
    var speed = clamp(parseSpeed(raw), 0, 140);

    if(valEl){
      valEl.textContent = String(speed);
    }

    var fill = q(".v101-speed-bar-fill", card);
    if(fill){
      fill.style.width = ((speed / 140) * 100).toFixed(1) + "%";
    }

    var analogNum = q(".v101-analog-number", card);
    if(analogNum){
      analogNum.textContent = String(speed);
    }

    var needle = q(".v101-needle-wrap", card);
    if(needle){
      var deg = -88 + ((speed / 140) * 176);
      needle.style.transform = "translateX(-50%) rotate(" + deg.toFixed(1) + "deg)";
    }
  }

  function start(){
    sync();

    var liveSpeed = document.getElementById("liveSpeedText");
    if(liveSpeed && !liveSpeed.dataset.v101Observed){
      liveSpeed.dataset.v101Observed = "1";
      try{
        var mo = new MutationObserver(sync);
        mo.observe(liveSpeed, { childList:true, subtree:true, characterData:true });
      }catch(_){}
    }

    var v = document.getElementById("v99SpeedVal");
    if(v && !v.dataset.v101Observed){
      v.dataset.v101Observed = "1";
      try{
        var mo2 = new MutationObserver(sync);
        mo2.observe(v, { childList:true, subtree:true, characterData:true });
      }catch(_){}
    }
  }

  document.addEventListener("DOMContentLoaded", start);
  window.addEventListener("load", start);
  setInterval(sync, 700);

  window.MuavinV101SpeedWidget = {
    refresh: sync
  };
})();
/* V101_SPEED_WIDGET_END */
'''.strip() + "\n"

for p in [WEB_CSS, AND_CSS]:
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(css_text, encoding="utf-8")
    print("✅ CSS yazıldı:", p)

for p in [WEB_JS, AND_JS]:
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(js_text, encoding="utf-8")
    print("✅ JS yazıldı:", p)

css_tag = """<link rel="stylesheet" href="{{ url_for('static', filename='continue/continue_speed_widget_v101.css') }}?v=v101-{{ trip['id'] }}">"""
js_tag = """<script src="{{ url_for('static', filename='continue/continue_speed_widget_v101.js') }}?v=v101-{{ trip['id'] }}"></script>"""

def patch_template(path):
    if not path.exists():
        return

    s = path.read_text(encoding="utf-8", errors="ignore")
    old = s

    if "continue_speed_widget_v101.css" not in s:
        if "</head>" in s:
            s = s.replace("</head>", css_tag + "\n</head>")
        else:
            s = s.replace("</body>", css_tag + "\n</body>")

    if "continue_speed_widget_v101.js" not in s:
        if "continue_trip_v99_clean.js" in s:
            s = s.replace(
                "</body>",
                js_tag + "\n</body>"
            )
        else:
            s = s.replace("</body>", js_tag + "\n</body>")

    if s != old:
        path.write_text(s, encoding="utf-8")
        print("✅ template patch:", path)
    else:
        print("ℹ️ template zaten güncel:", path)

for p in [WEB_TPL, AND_TPL]:
    patch_template(p)

print()
print("===== KONTROL =====")
for p in [WEB_TPL, AND_TPL]:
    txt = p.read_text(encoding="utf-8", errors="ignore")
    print(("✅ " if "continue_speed_widget_v101.js" in txt and "continue_speed_widget_v101.css" in txt else "❌ ") + str(p))

print()
print("===== AKTİF SCRIPT SATIRLARI =====")
txt = WEB_TPL.read_text(encoding="utf-8", errors="ignore")
for i, line in enumerate(txt.splitlines(), 1):
    if "continue_trip_v99_clean.js" in line or "continue_speed_widget_v101" in line:
        print(f"{i}: {line}")

print()
print("✅ V101 kompakt hız widget paketi kuruldu.")
print("Yenile:")
print("http://127.0.0.1:5000/continue-trip?v=v101-speed-widget")
