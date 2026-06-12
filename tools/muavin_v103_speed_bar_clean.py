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

WEB_JS = ROOT / "static/continue/continue_speed_bar_v103.js"
AND_JS = ROOT / "android_app/app/src/main/python/static/continue/continue_speed_bar_v103.js"

WEB_CSS = ROOT / "static/continue/continue_speed_bar_v103.css"
AND_CSS = ROOT / "android_app/app/src/main/python/static/continue/continue_speed_bar_v103.css"

print("===== V103 TEMİZ HIZ BAR =====")

def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()[:12] if p.exists() else "-"

for p in [WEB_TPL, AND_TPL, WEB_JS, AND_JS, WEB_CSS, AND_CSS]:
    if p.exists():
        bak = p.with_name(p.name + f".bak-v103-speed-bar-{STAMP}")
        shutil.copy2(p, bak)
        print("📦 backup:", bak)

if not WEB_TPL.exists():
    raise SystemExit("❌ template yok")

WEB_JS.parent.mkdir(parents=True, exist_ok=True)
WEB_CSS.parent.mkdir(parents=True, exist_ok=True)

css = r'''
/* V103_SPEED_BAR_CLEAN_START */

.v103-speed-card{
  position:relative !important;
  overflow:hidden !important;
  cursor:default !important;
}

.v103-speed-card .v99-gauge-label,
.v103-speed-card .v99-gauge-val,
.v103-speed-card .v99-gauge-unit{
  position:relative !important;
  z-index:5 !important;
}

.v103-speed-card .v99-gauge-val{
  color:#f1a340 !important;
  text-shadow:
    0 0 10px rgba(241,163,64,.36),
    0 2px 6px rgba(0,0,0,.75) !important;
}

.v103-speed-card .v99-gauge-unit{
  opacity:.72 !important;
}

.v103-speed-card::before{
  content:"";
  position:absolute;
  left:50%;
  top:50%;
  width:86px;
  height:86px;
  transform:translate(-50%,-50%);
  border-radius:50%;
  background:radial-gradient(circle, rgba(241,163,64,.08), transparent 62%);
  pointer-events:none;
  z-index:1;
}

.v103-speed-track{
  position:absolute;
  left:18px;
  right:18px;
  bottom:8px;
  height:3px;
  border-radius:999px;
  background:rgba(255,255,255,.09);
  overflow:hidden;
  z-index:4;
  box-shadow:inset 0 1px 2px rgba(0,0,0,.45);
}

.v103-speed-fill{
  width:0%;
  height:100%;
  border-radius:999px;
  background:linear-gradient(90deg,#1db87a 0%, #e08820 58%, #e03030 100%);
  box-shadow:0 0 12px rgba(224,136,32,.26);
  transition:width .24s ease;
}

.v103-speed-card.v103-speed-low .v103-speed-fill{
  box-shadow:0 0 12px rgba(29,184,122,.24);
}

.v103-speed-card.v103-speed-high .v103-speed-fill{
  box-shadow:0 0 12px rgba(224,48,48,.28);
}

/* V103_SPEED_BAR_CLEAN_END */
'''.strip() + "\n"

js = r'''
/* V103_SPEED_BAR_CLEAN_START */
(function(){
  "use strict";

  if(window.__MUAVIN_V103_SPEED_BAR__) return;
  window.__MUAVIN_V103_SPEED_BAR__ = true;

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

  function ensure(card){
    if(!card) return;

    card.classList.add("v103-speed-card");

    if(!q(".v103-speed-track", card)){
      var track = document.createElement("div");
      track.className = "v103-speed-track";
      track.innerHTML = '<div class="v103-speed-fill"></div>';
      card.appendChild(track);
    }
  }

  function paint(){
    var card = findSpeedCard();
    if(!card) return;

    ensure(card);

    var speed = readSpeed();
    var capped = Math.max(0, Math.min(speed, 140));
    var pct = capped / 140;

    var fill = q(".v103-speed-fill", card);
    if(fill){
      fill.style.width = (pct * 100).toFixed(1) + "%";
    }

    card.classList.toggle("v103-speed-low", speed < 50);
    card.classList.toggle("v103-speed-high", speed >= 95);
  }

  function boot(){
    paint();

    try{
      var a = q("#v99SpeedVal");
      if(a && !a.dataset.v103Observed){
        a.dataset.v103Observed = "1";
        new MutationObserver(paint).observe(a, {
          childList:true,
          subtree:true,
          characterData:true
        });
      }

      var b = q("#liveSpeedText");
      if(b && !b.dataset.v103Observed){
        b.dataset.v103Observed = "1";
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

  var tries = 80;
  var timer = setInterval(function(){
    boot();
    paint();
    tries--;
    if(tries <= 0) clearInterval(timer);
  }, 500);

  window.MuavinV103SpeedBar = {
    boot: boot,
    paint: paint
  };
})();
/* V103_SPEED_BAR_CLEAN_END */
'''.strip() + "\n"

WEB_CSS.write_text(css, encoding="utf-8")
WEB_JS.write_text(js, encoding="utf-8")

print("✅ V103 CSS yazıldı")
print("✅ V103 JS yazıldı")

AND_CSS.parent.mkdir(parents=True, exist_ok=True)
AND_JS.parent.mkdir(parents=True, exist_ok=True)
shutil.copy2(WEB_CSS, AND_CSS)
shutil.copy2(WEB_JS, AND_JS)
print("✅ Android JS/CSS senkron")

css_tag = """<link rel="stylesheet" href="{{ url_for('static', filename='continue/continue_speed_bar_v103.css') }}?v=v103-{{ trip['id'] }}">"""
js_tag = """<script src="{{ url_for('static', filename='continue/continue_speed_bar_v103.js') }}?v=v103-{{ trip['id'] }}"></script>"""

def patch_tpl(p):
    s = p.read_text(encoding="utf-8", errors="ignore")
    old = s

    # Eski hız denemelerini template'den kaldır
    for name in [
        "continue_speed_toggle_v100",
        "continue_speed_widget_v101",
        "continue_speed_overlay_v102",
        "continue_speed_bar_v103",
    ]:
        s = re.sub(rf'\n?\s*<link[^>]+{name}\.css[^>]*>\s*', "\n", s)
        s = re.sub(rf'\n?\s*<script[^>]+{name}\.js[^>]*></script>\s*', "\n", s)

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
    ("V103 CSS link var", "continue_speed_bar_v103.css" in tpl),
    ("V103 JS script var", "continue_speed_bar_v103.js" in tpl),
    ("V102 template'den kalktı", "continue_speed_overlay_v102" not in tpl),
    ("V101 template'den kalktı", "continue_speed_widget_v101" not in tpl),
    ("V100 template'den kalktı", "continue_speed_toggle_v100" not in tpl),
    ("V103 JS marker var", "V103_SPEED_BAR_CLEAN_START" in js2),
    ("V103 CSS marker var", "V103_SPEED_BAR_CLEAN_START" in css2),
]

for name, ok in checks:
    print(("✅ " if ok else "❌ ") + name)

print()
print("===== TEMPLATE SATIRLARI =====")
for i, line in enumerate(tpl.splitlines(), 1):
    if "continue_speed_" in line or "continue_trip_v99_clean.js" in line:
        print(f"{i}: {line}")

print()
print("===== SHA =====")
for label, a, b in [
    ("template", WEB_TPL, AND_TPL),
    ("v103 js", WEB_JS, AND_JS),
    ("v103 css", WEB_CSS, AND_CSS),
]:
    print(f"{label}: {'AYNI' if sha(a)==sha(b) else 'FARKLI'} web={sha(a)} android={sha(b)}")

print()
print("✅ V103 temiz hız bar hazır.")
print("Aç:")
print("http://127.0.0.1:5000/continue-trip?v=v103-speed-bar")
