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

WEB_V99_JS = ROOT / "static/continue/continue_trip_v99_clean.js"
AND_V99_JS = ROOT / "android_app/app/src/main/python/static/continue/continue_trip_v99_clean.js"

WEB_V99_CSS = ROOT / "static/continue/continue_trip_v99_clean.css"
AND_V99_CSS = ROOT / "android_app/app/src/main/python/static/continue/continue_trip_v99_clean.css"

WEB_JS = ROOT / "static/continue/continue_speed_final_v105.js"
AND_JS = ROOT / "android_app/app/src/main/python/static/continue/continue_speed_final_v105.js"

WEB_CSS = ROOT / "static/continue/continue_speed_final_v105.css"
AND_CSS = ROOT / "android_app/app/src/main/python/static/continue/continue_speed_final_v105.css"

OLD_SPEED_NAMES = [
    "continue_speed_toggle_v100",
    "continue_speed_widget_v101",
    "continue_speed_overlay_v102",
    "continue_speed_bar_v103",
    "continue_speed_final_v105",
]

OLD_SPEED_FILES = []
for base in [
    "continue_speed_toggle_v100",
    "continue_speed_widget_v101",
    "continue_speed_overlay_v102",
    "continue_speed_bar_v103",
]:
    OLD_SPEED_FILES += [
        ROOT / f"static/continue/{base}.js",
        ROOT / f"static/continue/{base}.css",
        ROOT / f"android_app/app/src/main/python/static/continue/{base}.js",
        ROOT / f"android_app/app/src/main/python/static/continue/{base}.css",
    ]

print("===== V105 SON HIZ KUTUSU GÜZELLEŞTİRME =====")
print("ROOT:", ROOT)

def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()[:12] if p.exists() else "-"

def backup(p):
    if p.exists():
        bak = p.with_name(p.name + f".bak-v105-speed-final-{STAMP}")
        shutil.copy2(p, bak)
        print("📦 backup:", bak)

for p in [WEB_TPL, AND_TPL, WEB_V99_JS, AND_V99_JS, WEB_V99_CSS, AND_V99_CSS, WEB_JS, AND_JS, WEB_CSS, AND_CSS]:
    backup(p)

if not WEB_TPL.exists():
    raise SystemExit("❌ template yok")

WEB_JS.parent.mkdir(parents=True, exist_ok=True)
WEB_CSS.parent.mkdir(parents=True, exist_ok=True)

# 1) Ana V99 içine gömülmüş eski hız blokları varsa temizle
for p in [WEB_V99_JS, AND_V99_JS]:
    if not p.exists():
        continue

    s = p.read_text(encoding="utf-8", errors="ignore")
    old = s

    for a, b in [
        ("V99Z_SPEED_ANALOG_TOGGLE_START", "V99Z_SPEED_ANALOG_TOGGLE_END"),
        ("V99ZA_SPEED_TOGGLE_START", "V99ZA_SPEED_TOGGLE_END"),
        ("V100_SPEED_TOGGLE_ISOLATED_START", "V100_SPEED_TOGGLE_ISOLATED_END"),
        ("V101_SPEED_WIDGET_START", "V101_SPEED_WIDGET_END"),
        ("V102_SPEED_OVERLAY_START", "V102_SPEED_OVERLAY_END"),
        ("V103_SPEED_BAR_CLEAN_START", "V103_SPEED_BAR_CLEAN_END"),
    ]:
        s = re.sub(rf"\n?/\* {a} \*/.*?/\* {b} \*/\n?", "\n", s, flags=re.S)

    p.write_text(s, encoding="utf-8")
    print("✅ ana V99 JS eski hız blok temizliği:", p, "changed=", s != old)

for p in [WEB_V99_CSS, AND_V99_CSS]:
    if not p.exists():
        continue

    s = p.read_text(encoding="utf-8", errors="ignore")
    old = s

    for a, b in [
        ("V99Z_SPEED_ANALOG_TOGGLE_CSS_START", "V99Z_SPEED_ANALOG_TOGGLE_CSS_END"),
        ("V99ZA_SPEED_TOGGLE_CSS_START", "V99ZA_SPEED_TOGGLE_CSS_END"),
        ("V100_SPEED_TOGGLE_ISOLATED_CSS_START", "V100_SPEED_TOGGLE_ISOLATED_CSS_END"),
        ("V101_SPEED_WIDGET_START", "V101_SPEED_WIDGET_END"),
        ("V102_SPEED_OVERLAY_START", "V102_SPEED_OVERLAY_END"),
        ("V102A_SPEED_OVERLAY_TUNE_START", "V102A_SPEED_OVERLAY_TUNE_END"),
        ("V102B_SPEED_OVERLAY_FINAL_TUNE_START", "V102B_SPEED_OVERLAY_FINAL_TUNE_END"),
        ("V103_SPEED_BAR_CLEAN_START", "V103_SPEED_BAR_CLEAN_END"),
    ]:
        s = re.sub(rf"\n?/\* {a} \*/.*?/\* {b} \*/\n?", "\n", s, flags=re.S)

    p.write_text(s, encoding="utf-8")
    print("✅ ana V99 CSS eski hız blok temizliği:", p, "changed=", s != old)

# 2) Eski ayrı hız dosyalarını pasifleştir
for p in OLD_SPEED_FILES:
    if p.exists():
        disabled = p.with_name(p.name + f".disabled-v105-{STAMP}")
        shutil.move(str(p), str(disabled))
        print("✅ eski hız dosyası pasif:", disabled)

# 3) V105 CSS
css = r'''
/* V105_SPEED_FINAL_POLISH_START */

/*
  V105 final karar:
  - Analog yok
  - Click/toggle yok
  - Kutu yüksekliği değişmez
  - Sadece dijital hız + premium alt çizgi + yumuşak ışık
*/

.v105-speed-card{
  position:relative !important;
  overflow:hidden !important;
  isolation:isolate !important;
}

.v105-speed-card .v99-gauge-label,
.v105-speed-card .v99-gauge-val,
.v105-speed-card .v99-gauge-unit{
  position:relative !important;
  z-index:5 !important;
}

.v105-speed-card .v99-gauge-label{
  color:rgba(186,198,220,.68) !important;
}

.v105-speed-card .v99-gauge-val{
  color:#f1a340 !important;
  font-weight:800 !important;
  text-shadow:
    0 0 12px rgba(241,163,64,.38),
    0 2px 7px rgba(0,0,0,.82) !important;
}

.v105-speed-card .v99-gauge-unit{
  color:rgba(226,234,246,.54) !important;
  opacity:.78 !important;
  text-shadow:0 2px 5px rgba(0,0,0,.78) !important;
}

.v105-speed-card::before{
  content:"";
  position:absolute;
  left:50%;
  top:52%;
  width:92px;
  height:92px;
  transform:translate(-50%,-50%);
  border-radius:999px;
  background:
    radial-gradient(circle, rgba(241,163,64,.12) 0%, rgba(241,163,64,.055) 34%, transparent 66%);
  pointer-events:none;
  z-index:1;
}

.v105-speed-card::after{
  content:"";
  position:absolute;
  left:18px;
  right:18px;
  bottom:7px;
  height:1px;
  border-radius:999px;
  background:rgba(255,255,255,.06);
  pointer-events:none;
  z-index:2;
}

.v105-speed-track{
  position:absolute;
  left:18px;
  right:18px;
  bottom:8px;
  height:3px;
  border-radius:999px;
  background:rgba(255,255,255,.075);
  overflow:hidden;
  z-index:4;
  pointer-events:none;
  box-shadow:inset 0 1px 2px rgba(0,0,0,.50);
}

.v105-speed-fill{
  height:100%;
  width:4%;
  border-radius:999px;
  background:linear-gradient(90deg,#20bf7d 0%, #e08820 58%, #e03030 100%);
  box-shadow:0 0 12px rgba(224,136,32,.28);
  transition:width .26s ease, box-shadow .26s ease;
}

.v105-speed-dot{
  position:absolute;
  top:50%;
  left:var(--v105-speed-pct, 4%);
  width:7px;
  height:7px;
  border-radius:999px;
  transform:translate(-50%,-50%);
  background:#f1a340;
  box-shadow:
    0 0 12px rgba(241,163,64,.48),
    0 0 3px rgba(255,255,255,.28);
  transition:left .26s ease, background .26s ease, box-shadow .26s ease;
}

.v105-speed-card.v105-speed-low .v105-speed-fill{
  box-shadow:0 0 12px rgba(32,191,125,.24);
}

.v105-speed-card.v105-speed-low .v105-speed-dot{
  background:#20bf7d;
  box-shadow:0 0 12px rgba(32,191,125,.42);
}

.v105-speed-card.v105-speed-high .v105-speed-fill{
  box-shadow:0 0 14px rgba(224,48,48,.30);
}

.v105-speed-card.v105-speed-high .v105-speed-dot{
  background:#e03030;
  box-shadow:0 0 14px rgba(224,48,48,.48);
}

/* V105_SPEED_FINAL_POLISH_END */
'''.strip() + "\n"

# 4) V105 JS
js = r'''
/* V105_SPEED_FINAL_POLISH_START */
(function(){
  "use strict";

  if(window.__MUAVIN_V105_SPEED_FINAL__) return;
  window.__MUAVIN_V105_SPEED_FINAL__ = true;

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

    card.classList.add("v105-speed-card");

    if(!q(".v105-speed-track", card)){
      var track = document.createElement("div");
      track.className = "v105-speed-track";
      track.innerHTML = '<div class="v105-speed-fill"></div><div class="v105-speed-dot"></div>';
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
    var pctText = Math.max(4, pct * 100).toFixed(1) + "%";

    card.style.setProperty("--v105-speed-pct", pctText);

    var fill = q(".v105-speed-fill", card);
    if(fill){
      fill.style.width = pctText;
    }

    card.classList.toggle("v105-speed-low", speed < 50);
    card.classList.toggle("v105-speed-high", speed >= 95);
  }

  function boot(){
    paint();

    try{
      var a = q("#v99SpeedVal");
      if(a && !a.dataset.v105Observed){
        a.dataset.v105Observed = "1";
        new MutationObserver(paint).observe(a, {
          childList:true,
          subtree:true,
          characterData:true
        });
      }

      var b = q("#liveSpeedText");
      if(b && !b.dataset.v105Observed){
        b.dataset.v105Observed = "1";
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

  window.MuavinV105SpeedFinal = {
    boot: boot,
    paint: paint
  };
})();
/* V105_SPEED_FINAL_POLISH_END */
'''.strip() + "\n"

WEB_CSS.write_text(css, encoding="utf-8")
WEB_JS.write_text(js, encoding="utf-8")
print("✅ V105 CSS yazıldı:", WEB_CSS)
print("✅ V105 JS yazıldı:", WEB_JS)

AND_CSS.parent.mkdir(parents=True, exist_ok=True)
AND_JS.parent.mkdir(parents=True, exist_ok=True)
shutil.copy2(WEB_CSS, AND_CSS)
shutil.copy2(WEB_JS, AND_JS)
print("✅ Android V105 JS/CSS senkron")

# 5) Template temizliği + V105 ekleme
css_tag = """<link rel="stylesheet" href="{{ url_for('static', filename='continue/continue_speed_final_v105.css') }}?v=v105-{{ trip['id'] }}">"""
js_tag = """<script src="{{ url_for('static', filename='continue/continue_speed_final_v105.js') }}?v=v105-{{ trip['id'] }}"></script>"""

def patch_template(p):
    if not p.exists():
        print("❌ template yok:", p)
        return

    s = p.read_text(encoding="utf-8", errors="ignore")
    old = s

    for name in OLD_SPEED_NAMES:
        s = re.sub(rf'\n?\s*<link[^>]+{name}\.css[^>]*>\s*', "\n", s)
        s = re.sub(rf'\n?\s*<script[^>]+{name}\.js[^>]*></script>\s*', "\n", s)

    clean_v99 = """<script src="{{ url_for('static', filename='continue/continue_trip_v99_clean.js') }}?v=v105-final-{{ trip['id'] }}"></script>"""
    s = re.sub(
        r'''<script src="\{\{\s*url_for\('static',\s*filename='continue/continue_trip_v99_clean\.js'\)\s*\}\}\?v=[^"]*"></script>''',
        clean_v99,
        s,
        count=1
    )

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

patch_template(WEB_TPL)

# Web ana dosyaları Android'e son kez eşitle
if AND_TPL.parent.exists():
    shutil.copy2(WEB_TPL, AND_TPL)
    print("✅ Android template web ile eşitlendi")

if WEB_V99_JS.exists() and AND_V99_JS.parent.exists():
    shutil.copy2(WEB_V99_JS, AND_V99_JS)
    print("✅ Android V99 JS web ile eşitlendi")

if WEB_V99_CSS.exists() and AND_V99_CSS.parent.exists():
    shutil.copy2(WEB_V99_CSS, AND_V99_CSS)
    print("✅ Android V99 CSS web ile eşitlendi")

print()
print("===== NODE JS SYNTAX CHECK =====")
for label, p in [("V105", WEB_JS), ("V99", WEB_V99_JS)]:
    try:
        res = subprocess.run(["node", "--check", str(p)], capture_output=True, text=True)
        if res.returncode == 0:
            print(f"✅ {label} JS syntax OK")
        else:
            print(f"❌ {label} JS syntax HATA")
            print(res.stdout)
            print(res.stderr)
    except FileNotFoundError:
        print("ℹ️ node yok, atlandı")
        break

print()
print("===== KONTROL =====")
tpl = WEB_TPL.read_text(encoding="utf-8", errors="ignore")
v99js = WEB_V99_JS.read_text(encoding="utf-8", errors="ignore") if WEB_V99_JS.exists() else ""
v99css = WEB_V99_CSS.read_text(encoding="utf-8", errors="ignore") if WEB_V99_CSS.exists() else ""
v105js = WEB_JS.read_text(encoding="utf-8", errors="ignore")
v105css = WEB_CSS.read_text(encoding="utf-8", errors="ignore")

checks = [
    ("V105 CSS link var", "continue_speed_final_v105.css" in tpl),
    ("V105 JS script var", "continue_speed_final_v105.js" in tpl),
    ("V100 template temiz", "continue_speed_toggle_v100" not in tpl),
    ("V101 template temiz", "continue_speed_widget_v101" not in tpl),
    ("V102 template temiz", "continue_speed_overlay_v102" not in tpl),
    ("V103 template temiz", "continue_speed_bar_v103" not in tpl),
    ("V105 JS marker var", "V105_SPEED_FINAL_POLISH_START" in v105js),
    ("V105 CSS marker var", "V105_SPEED_FINAL_POLISH_START" in v105css),
    ("V105 API var", "MuavinV105SpeedFinal" in v105js),
    ("Doluluk paneli duruyor", "V99M_OCCUPANCY_PANEL_START" in v99js),
    ("Koltuk renkleri duruyor", "V99O_SEAT_GENDER_SELECTED_JS_START" in v99js),
    ("Bagaj rozeti fix duruyor", "V99P_BAG_BADGE_CLICK_FIX_START" in v99css),
]

for name, ok in checks:
    print(("✅ " if ok else "❌ ") + name)

print()
print("===== TEMPLATE SATIRLARI =====")
for i, line in enumerate(tpl.splitlines(), 1):
    if "continue_trip_v99_clean.js" in line or "continue_speed_" in line:
        print(f"{i}: {line}")

print()
print("===== SHA =====")
for label, a, b in [
    ("template", WEB_TPL, AND_TPL),
    ("v99 js", WEB_V99_JS, AND_V99_JS),
    ("v99 css", WEB_V99_CSS, AND_V99_CSS),
    ("v105 js", WEB_JS, AND_JS),
    ("v105 css", WEB_CSS, AND_CSS),
]:
    if a.exists() and b.exists():
        print(f"{label}: {'AYNI' if sha(a)==sha(b) else 'FARKLI'} web={sha(a)} android={sha(b)}")

print()
print("✅ V105 son hız kutusu yaması hazır.")
print("Aç:")
print("http://127.0.0.1:5000/continue-trip?v=v105-speed-final")
