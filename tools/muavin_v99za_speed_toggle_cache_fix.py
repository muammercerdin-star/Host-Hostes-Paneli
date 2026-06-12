from pathlib import Path
from datetime import datetime
import shutil
import re
import subprocess

ROOT = Path(".").resolve()
STAMP = datetime.now().strftime("%Y%m%d-%H%M%S")

WEB_TPL = ROOT / "templates/continue_trip.html"
AND_TPL = ROOT / "android_app/app/src/main/python/templates/continue_trip.html"

WEB_JS = ROOT / "static/continue/continue_trip_v99_clean.js"
AND_JS = ROOT / "android_app/app/src/main/python/static/continue/continue_trip_v99_clean.js"

WEB_CSS = ROOT / "static/continue/continue_trip_v99_clean.css"
AND_CSS = ROOT / "android_app/app/src/main/python/static/continue/continue_trip_v99_clean.css"

print("===== V99ZA HIZ TOGGLE + CACHE FIX =====")

for p in [WEB_TPL, AND_TPL, WEB_JS, AND_JS, WEB_CSS, AND_CSS]:
    if p.exists():
        bak = p.with_name(p.name + f".bak-v99za-speed-toggle-{STAMP}")
        shutil.copy2(p, bak)
        print("📦 backup:", bak)

if not WEB_TPL.exists():
    raise SystemExit("❌ template yok")
if not WEB_JS.exists():
    raise SystemExit("❌ JS yok")
if not WEB_CSS.exists():
    raise SystemExit("❌ CSS yok")

# 1) Template JS cache satırını yükselt
tpl = WEB_TPL.read_text(encoding="utf-8", errors="ignore")

new_script_line = """<script src="{{ url_for('static', filename='continue/continue_trip_v99_clean.js') }}?v=v99za-speed-{{ trip['id'] }}"></script>"""

tpl2, n_tpl = re.subn(
    r'''<script src="\{\{\s*url_for\('static',\s*filename='continue/continue_trip_v99_clean\.js'\)\s*\}\}\?v=[^"]*"></script>''',
    new_script_line,
    tpl,
    count=1
)

if n_tpl:
    WEB_TPL.write_text(tpl2, encoding="utf-8")
    print("✅ template cache satırı v99za-speed yapıldı")
else:
    print("⚠️ template script satırı bulunamadı")

# 2) Eski V99Z bloklarını temizle, V99ZA'yı koy
js = WEB_JS.read_text(encoding="utf-8", errors="ignore")
css = WEB_CSS.read_text(encoding="utf-8", errors="ignore")

for start, end in [
    ("V99Z_SPEED_ANALOG_TOGGLE_START", "V99Z_SPEED_ANALOG_TOGGLE_END"),
    ("V99ZA_SPEED_TOGGLE_START", "V99ZA_SPEED_TOGGLE_END"),
]:
    js = re.sub(
        rf"\n?/\* {start} \*/.*?/\* {end} \*/\n?",
        "\n",
        js,
        flags=re.S
    )

for start, end in [
    ("V99Z_SPEED_ANALOG_TOGGLE_CSS_START", "V99Z_SPEED_ANALOG_TOGGLE_CSS_END"),
    ("V99ZA_SPEED_TOGGLE_CSS_START", "V99ZA_SPEED_TOGGLE_CSS_END"),
]:
    css = re.sub(
        rf"\n?/\* {start} \*/.*?/\* {end} \*/\n?",
        "\n",
        css,
        flags=re.S
    )

js_block = r'''
/* V99ZA_SPEED_TOGGLE_START */
(function(){
  "use strict";

  if(window.__V99ZA_SPEED_TOGGLE__) return;
  window.__V99ZA_SPEED_TOGGLE__ = true;

  function q(sel, root){
    return (root || document).querySelector(sel);
  }

  function qa(sel, root){
    return Array.prototype.slice.call((root || document).querySelectorAll(sel));
  }

  function cleanText(el){
    return el ? String(el.textContent || "").trim() : "";
  }

  function findSpeedCard(){
    var cells = qa(".v99-gauges .v99-gauge-cell");
    for(var i = 0; i < cells.length; i++){
      var label = q(".v99-gauge-label", cells[i]);
      var t = cleanText(label).toLocaleUpperCase("tr-TR");
      if(t === "HIZ"){
        return cells[i];
      }
    }
    return null;
  }

  function readSpeed(){
    var visible = q("#v99SpeedVal");
    var hidden = q("#liveSpeedText");

    var raw = cleanText(visible);
    if(!raw || raw === "—"){
      raw = cleanText(hidden);
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

  function makeAnalog(card){
    if(!card) return;

    if(q(".v99za-speed-analog", card)) return;

    var box = document.createElement("div");
    box.className = "v99za-speed-analog";
    box.innerHTML = ''
      + '<div class="v99za-dial">'
      + '  <div class="v99za-arc"></div>'
      + '  <div class="v99za-needle"></div>'
      + '  <div class="v99za-center"></div>'
      + '  <div class="v99za-num">0</div>'
      + '</div>'
      + '<div class="v99za-unit">km/sa</div>';

    card.appendChild(box);
  }

  function paint(){
    var card = findSpeedCard();
    if(!card) return;

    makeAnalog(card);

    var speed = readSpeed();
    var ratio = Math.max(0, Math.min(speed, 140)) / 140;
    var deg = -120 + (ratio * 240);

    card.style.setProperty("--v99za-speed-deg", deg + "deg");

    var num = q(".v99za-num", card);
    if(num){
      num.textContent = String(Math.round(speed));
    }
  }

  function bind(){
    var card = findSpeedCard();
    if(!card) return;

    card.classList.add("v99za-speed-card");
    makeAnalog(card);
    paint();

    if(card.dataset.v99zaBound === "1") return;
    card.dataset.v99zaBound = "1";

    card.addEventListener("click", function(ev){
      ev.preventDefault();
      ev.stopPropagation();

      card.classList.toggle("v99za-analog-on");
      paint();
    }, true);
  }

  function boot(){
    bind();
    paint();
  }

  if(document.readyState === "loading"){
    document.addEventListener("DOMContentLoaded", boot);
  }else{
    boot();
  }

  window.addEventListener("load", boot);
  document.addEventListener("continueEtaUpdated", paint);

  try{
    var speedEl = document.getElementById("v99SpeedVal");
    if(speedEl){
      new MutationObserver(function(){
        paint();
      }).observe(speedEl, {
        childList:true,
        subtree:true,
        characterData:true
      });
    }
  }catch(_){}

  setInterval(function(){
    bind();
    paint();
  }, 700);

  window.MuavinV99ZASpeedToggle = {
    boot: boot,
    paint: paint
  };
})();
/* V99ZA_SPEED_TOGGLE_END */
'''

css_block = r'''
/* V99ZA_SPEED_TOGGLE_CSS_START */
.v99za-speed-card{
  cursor:pointer !important;
  user-select:none !important;
  -webkit-user-select:none !important;
  touch-action:manipulation !important;
}

.v99za-speed-card .v99za-speed-analog{
  display:none;
  margin-top:4px;
}

.v99za-speed-card.v99za-analog-on #v99SpeedVal,
.v99za-speed-card.v99za-analog-on .v99-gauge-unit,
.v99za-speed-card.v99za-analog-on #liveSpeedText{
  display:none !important;
}

.v99za-speed-card.v99za-analog-on .v99za-speed-analog{
  display:flex !important;
  flex-direction:column;
  align-items:center;
  justify-content:center;
}

.v99za-dial{
  position:relative;
  width:78px;
  height:45px;
  margin:0 auto;
  overflow:hidden;
}

.v99za-arc{
  position:absolute;
  left:6px;
  right:6px;
  bottom:-32px;
  height:66px;
  border-radius:70px 70px 0 0;
  border:4px solid rgba(255,176,71,.72);
  border-bottom:0;
  box-shadow:
    0 0 14px rgba(255,176,71,.32),
    inset 0 0 18px rgba(255,176,71,.10);
}

.v99za-needle{
  position:absolute;
  left:50%;
  bottom:5px;
  width:3px;
  height:35px;
  border-radius:4px;
  background:linear-gradient(180deg,#ffd39a,#ff9d24);
  transform-origin:50% calc(100% - 2px);
  transform:translateX(-50%) rotate(var(--v99za-speed-deg, -120deg));
  box-shadow:0 0 12px rgba(255,176,71,.65);
}

.v99za-center{
  position:absolute;
  left:50%;
  bottom:0;
  width:12px;
  height:12px;
  border-radius:50%;
  transform:translateX(-50%);
  background:#ffd39a;
  box-shadow:0 0 12px rgba(255,211,154,.62);
}

.v99za-num{
  position:absolute;
  left:50%;
  bottom:15px;
  transform:translateX(-50%);
  font-family:'JetBrains Mono', monospace;
  font-size:13px;
  font-weight:900;
  color:#ffb347;
  text-shadow:0 0 12px rgba(255,176,71,.48);
}

.v99za-unit{
  margin-top:0;
  font-family:'JetBrains Mono', monospace;
  font-size:9px;
  letter-spacing:1.8px;
  color:var(--v99-muted);
}
/* V99ZA_SPEED_TOGGLE_CSS_END */
'''

WEB_JS.write_text(js.rstrip() + "\n\n" + js_block.strip() + "\n", encoding="utf-8")
WEB_CSS.write_text(css.rstrip() + "\n\n" + css_block.strip() + "\n", encoding="utf-8")

print("✅ V99ZA JS/CSS yazıldı")

# Android sync
if AND_TPL.parent.exists():
    shutil.copy2(WEB_TPL, AND_TPL)
    print("✅ android template senkron")

if AND_JS.parent.exists():
    shutil.copy2(WEB_JS, AND_JS)
    print("✅ android JS senkron")

if AND_CSS.parent.exists():
    shutil.copy2(WEB_CSS, AND_CSS)
    print("✅ android CSS senkron")

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
tpl_now = WEB_TPL.read_text(encoding="utf-8", errors="ignore")
js_now = WEB_JS.read_text(encoding="utf-8", errors="ignore")
css_now = WEB_CSS.read_text(encoding="utf-8", errors="ignore")

checks = [
    ("template cache v99za-speed", "v99za-speed" in tpl_now),
    ("JS V99ZA marker", "V99ZA_SPEED_TOGGLE_START" in js_now),
    ("CSS V99ZA marker", "V99ZA_SPEED_TOGGLE_CSS_START" in css_now),
    ("speed API", "MuavinV99ZASpeedToggle" in js_now),
    ("eski V99Z kaldırıldı", "V99Z_SPEED_ANALOG_TOGGLE_START" not in js_now),
]

for name, ok in checks:
    print(("✅ " if ok else "❌ ") + name)

print()
print("===== SCRIPT SATIRI =====")
for i, line in enumerate(tpl_now.splitlines(), 1):
    if "continue_trip_v99_clean.js" in line:
        print(f"{i}: {line}")

print()
print("✅ Bitti. Şimdi şunu aç:")
print("http://127.0.0.1:5000/continue-trip?v=v99za-speed")
