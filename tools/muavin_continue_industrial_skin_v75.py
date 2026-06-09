from pathlib import Path
from datetime import datetime
import shutil
import re

ROOT = Path(".").resolve()
STAMP = datetime.now().strftime("%Y%m%d-%H%M%S")

CSS_WEB = ROOT / "static/continue/continue_industrial_v75.css"
CSS_AND = ROOT / "android_app/app/src/main/python/static/continue/continue_industrial_v75.css"

JS_WEB = ROOT / "static/continue/continue_ring_v75.js"
JS_AND = ROOT / "android_app/app/src/main/python/static/continue/continue_ring_v75.js"

TPLS = [
    ROOT / "templates/continue_trip.html",
    ROOT / "android_app/app/src/main/python/templates/continue_trip.html",
]

CSS = r'''
/* CONTINUE_INDUSTRIAL_SKIN_V75 */
:root{
  --v75-bg:#0b0d10;
  --v75-panel:#12151a;
  --v75-panel2:#181c23;
  --v75-border:#1f2530;
  --v75-red:#e03030;
  --v75-red-dim:#351010;
  --v75-amber:#e08820;
  --v75-green:#1db87a;
  --v75-blue:#3a8bff;
  --v75-text:#d8dde8;
  --v75-muted:#6b7280;
}

body{
  background:var(--v75-bg) !important;
  color:var(--v75-text) !important;
  font-family:system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif !important;
}

.shell{
  max-width:760px;
  margin:0 auto;
  padding-bottom:96px !important;
}

.top-brand{
  background:var(--v75-panel) !important;
  border-bottom:1px solid var(--v75-border) !important;
  border-radius:0 !important;
  padding:14px 20px !important;
  box-shadow:none !important;
}

.brand-logo{
  width:34px !important;
  height:34px !important;
  border-radius:9px !important;
  background:var(--v75-red) !important;
  box-shadow:0 0 18px rgba(224,48,48,.35) !important;
}

.brand-title{
  letter-spacing:5px !important;
  font-size:20px !important;
}

.brand-sub{
  letter-spacing:4px !important;
  color:var(--v75-muted) !important;
}

.brand-action{
  border-radius:12px !important;
  background:var(--v75-panel2) !important;
  border:1px solid var(--v75-border) !important;
  box-shadow:none !important;
}

.hero{
  min-height:auto !important;
  border-radius:0 !important;
  margin:0 !important;
  padding:12px 20px !important;
  background:var(--v75-panel2) !important;
  border:0 !important;
  border-bottom:1px solid var(--v75-border) !important;
  box-shadow:none !important;
}

.hero-bus-img,
.hero-bus-shade,
.hero-title{
  display:none !important;
}

.hero-meta{
  position:static !important;
  display:flex !important;
  flex-wrap:wrap !important;
  gap:8px 14px !important;
  font-family:ui-monospace,Menlo,monospace !important;
  letter-spacing:1px !important;
  color:var(--v75-muted) !important;
}

.hero-meta-line{
  font-size:14px !important;
  color:var(--v75-text) !important;
}

.hero-meta-line .icon{
  opacity:.65 !important;
}

.stats-row{
  display:grid !important;
  grid-template-columns:repeat(4,1fr) !important;
  gap:1px !important;
  margin:0 !important;
  border-radius:0 !important;
  background:var(--v75-border) !important;
  border-bottom:1px solid var(--v75-border) !important;
}

.stat-box{
  background:var(--v75-panel) !important;
  border:0 !important;
  border-radius:0 !important;
  min-height:86px !important;
  padding:13px 9px !important;
  box-shadow:none !important;
  text-align:center !important;
}

.stat-box small{
  font-size:11px !important;
  letter-spacing:3px !important;
  color:var(--v75-muted) !important;
}

.stat-box b{
  font-family:ui-monospace,Menlo,monospace !important;
  font-size:20px !important;
  color:var(--v75-text) !important;
}

#liveSpeedText{
  color:var(--v75-amber) !important;
}

#liveTopStatusText{
  color:var(--v75-green) !important;
}

.timeline{
  margin:20px 20px 0 !important;
  padding:0 !important;
}

.timeline-line{
  background:linear-gradient(var(--v75-green),var(--v75-red),var(--v75-border)) !important;
  opacity:.5 !important;
}

.journey-card{
  margin-bottom:12px !important;
}

.node.live{
  background:var(--v75-red) !important;
  box-shadow:0 0 16px var(--v75-red) !important;
}

.card{
  background:var(--v75-panel) !important;
  border:1px solid var(--v75-border) !important;
  border-radius:15px !important;
  box-shadow:none !important;
}

.card.live{
  background:#12100e !important;
  border-color:rgba(224,48,48,.35) !important;
}

.card.regular.next-card{
  border-color:rgba(224,136,32,.35) !important;
}

.card-head{
  gap:14px !important;
}

.card-title{
  color:#fff !important;
  letter-spacing:.2px !important;
}

.card-label{
  color:var(--v75-muted) !important;
  letter-spacing:3px !important;
}

.status-pill{
  font-family:ui-monospace,Menlo,monospace !important;
  letter-spacing:2px !important;
  border-radius:999px !important;
}

.status-pill.live{
  background:var(--v75-red-dim) !important;
  color:var(--v75-red) !important;
  border:1px solid rgba(224,48,48,.35) !important;
}

.status-pill.next{
  background:#2c1f08 !important;
  color:var(--v75-amber) !important;
  border:1px solid rgba(224,136,32,.35) !important;
}

.metric{
  background:var(--v75-panel2) !important;
  border:1px solid var(--v75-border) !important;
  border-radius:13px !important;
}

.metric small{
  color:var(--v75-muted) !important;
  letter-spacing:2px !important;
}

.metric b{
  font-family:ui-monospace,Menlo,monospace !important;
}

.v75-ring-wrap{
  width:112px;
  height:112px;
  flex:0 0 112px;
  position:relative;
  margin-right:2px;
}

.v75-ring-svg{
  width:112px;
  height:112px;
  transform:rotate(-90deg);
}

.v75-ring-track{
  fill:none;
  stroke:var(--v75-red-dim);
  stroke-width:7;
}

.v75-ring-fill{
  fill:none;
  stroke:var(--v75-blue);
  stroke-width:7;
  stroke-linecap:round;
  filter:drop-shadow(0 0 7px var(--v75-blue));
  transition:stroke-dashoffset .7s ease,stroke .4s ease,filter .4s ease;
}

.v75-ring-center{
  position:absolute;
  inset:0;
  display:flex;
  flex-direction:column;
  align-items:center;
  justify-content:center;
}

.v75-ring-km{
  font-family:ui-monospace,Menlo,monospace;
  font-size:25px;
  font-weight:800;
  color:var(--v75-blue);
  text-shadow:0 0 12px rgba(58,139,255,.75);
  line-height:1;
}

.v75-ring-label{
  font-family:ui-monospace,Menlo,monospace;
  font-size:10px;
  letter-spacing:3px;
  color:var(--v75-muted);
  margin-top:4px;
}

.v75-ring-wrap[data-zone="mid"] .v75-ring-fill{
  stroke:var(--v75-amber);
  filter:drop-shadow(0 0 9px var(--v75-amber));
}

.v75-ring-wrap[data-zone="mid"] .v75-ring-km{
  color:var(--v75-amber);
  text-shadow:0 0 12px rgba(224,136,32,.75);
}

.v75-ring-wrap[data-zone="close"] .v75-ring-fill{
  stroke:var(--v75-red);
  filter:drop-shadow(0 0 14px var(--v75-red));
  animation:v75RingPulse 1s ease-in-out infinite;
}

.v75-ring-wrap[data-zone="close"] .v75-ring-km{
  color:var(--v75-red);
  text-shadow:0 0 18px rgba(224,48,48,.9);
}

@keyframes v75RingPulse{
  0%,100%{filter:drop-shadow(0 0 8px var(--v75-red));}
  50%{filter:drop-shadow(0 0 22px var(--v75-red));}
}

.dock{
  background:var(--v75-panel) !important;
  border-top:1px solid var(--v75-border) !important;
  box-shadow:0 -8px 24px rgba(0,0,0,.45) !important;
}

.dock-item{
  color:var(--v75-muted) !important;
}

.dock-item:first-child{
  color:var(--v75-red) !important;
}

.danger-zone{
  margin:22px 20px 110px !important;
}

.danger-btn{
  background:#1a0a0a !important;
  border:1px solid rgba(224,48,48,.35) !important;
  color:var(--v75-red) !important;
  letter-spacing:3px !important;
  border-radius:14px !important;
}

.bottom-home{
  display:none !important;
}

@media(max-width:420px){
  .stats-row{
    grid-template-columns:repeat(4,1fr) !important;
  }

  .stat-box{
    min-height:78px !important;
    padding:11px 5px !important;
  }

  .stat-box b{
    font-size:17px !important;
  }

  .v75-ring-wrap{
    width:98px;
    height:98px;
    flex-basis:98px;
  }

  .v75-ring-svg{
    width:98px;
    height:98px;
  }

  .v75-ring-km{
    font-size:23px;
  }
}
'''

JS = r'''
/* CONTINUE_RING_V75 */
(function(){
  if(window.CONTINUE_RING_V75_READY) return;
  window.CONTINUE_RING_V75_READY = true;

  const CIRC = 276.46;
  let maxKm = 50;

  function q(sel){
    return document.querySelector(sel);
  }

  function parseKm(v){
    const s = String(v || "").replace(",", ".").trim();
    const m = s.match(/-?\d+(?:\.\d+)?/);
    if(!m) return NaN;
    return Number(m[0]);
  }

  function fmtKm(n){
    if(!Number.isFinite(n)) return "—";
    if(n >= 10) return String(Math.round(n));
    return String(Math.round(n * 10) / 10).replace(".0", "");
  }

  function ensureRing(){
    const card = document.getElementById("liveCurrentCard");
    const head = card ? card.querySelector(".card-head") : null;
    if(!card || !head) return null;

    let wrap = document.getElementById("continueRingV75");
    if(wrap) return wrap;

    wrap = document.createElement("div");
    wrap.id = "continueRingV75";
    wrap.className = "v75-ring-wrap";
    wrap.innerHTML = `
      <svg class="v75-ring-svg" viewBox="0 0 110 110" aria-hidden="true">
        <circle class="v75-ring-track" cx="55" cy="55" r="44"></circle>
        <circle class="v75-ring-fill" id="continueRingFillV75" cx="55" cy="55" r="44"
          stroke-dasharray="${CIRC}" stroke-dashoffset="${CIRC}"></circle>
      </svg>
      <div class="v75-ring-center">
        <div class="v75-ring-km" id="continueRingKmV75">—</div>
        <div class="v75-ring-label">KM</div>
      </div>
    `;

    head.insertBefore(wrap, head.firstChild);
    return wrap;
  }

  function updateRing(){
    const wrap = ensureRing();
    const dist = document.getElementById("liveDistanceValue");
    const fill = document.getElementById("continueRingFillV75");
    const kmEl = document.getElementById("continueRingKmV75");

    if(!wrap || !dist || !fill || !kmEl) return;

    const km = parseKm(dist.textContent);
    if(!Number.isFinite(km)){
      kmEl.textContent = "—";
      fill.style.strokeDashoffset = CIRC;
      wrap.dataset.zone = "far";
      return;
    }

    maxKm = Math.max(maxKm, Math.ceil(km / 10) * 10, 10);

    const ratio = Math.max(0, Math.min(1, 1 - (km / maxKm)));
    const offset = CIRC * (1 - ratio);

    fill.style.strokeDashoffset = String(offset);
    kmEl.textContent = fmtKm(km);

    if(km <= 5){
      wrap.dataset.zone = "close";
    }else if(km <= 15){
      wrap.dataset.zone = "mid";
    }else{
      wrap.dataset.zone = "far";
    }
  }

  function boot(){
    ensureRing();
    updateRing();

    const dist = document.getElementById("liveDistanceValue");
    if(dist && window.MutationObserver){
      const obs = new MutationObserver(updateRing);
      obs.observe(dist, {childList:true, characterData:true, subtree:true});
    }

    setInterval(updateRing, 1000);
  }

  if(document.readyState === "loading"){
    document.addEventListener("DOMContentLoaded", boot);
  }else{
    boot();
  }
})();
'''

print("===== CONTINUE INDUSTRIAL SKIN V75 =====")

for p, content in [(CSS_WEB, CSS), (CSS_AND, CSS), (JS_WEB, JS), (JS_AND, JS)]:
    p.parent.mkdir(parents=True, exist_ok=True)
    if p.exists():
        b = p.with_name(p.name + f".bak-industrial-v75-{STAMP}")
        shutil.copy2(p, b)
        print("📦 Yedek:", b.relative_to(ROOT))
    p.write_text(content, encoding="utf-8")
    print("✅ Yazıldı:", p.relative_to(ROOT))

for p in TPLS:
    if not p.exists():
        print("⚠️ Template yok:", p.relative_to(ROOT))
        continue

    b = p.with_name(p.name + f".bak-industrial-v75-{STAMP}")
    shutil.copy2(p, b)
    print("📦 Yedek:", b.relative_to(ROOT))

    s = p.read_text(encoding="utf-8", errors="ignore")

    css_line = '<link rel="stylesheet" href="{{ url_for(\'static\', filename=\'continue/continue_industrial_v75.css\') }}?v=industrial-v75">'
    js_line = '  <script src="{{ url_for(\'static\', filename=\'continue/continue_ring_v75.js\') }}?v=industrial-v75"></script>'

    if "continue_industrial_v75.css" not in s:
        s = re.sub(
            r'(<link rel="stylesheet" href="{{ url_for\(\'static\', filename=\'continue/continue_trip\.css\'\) }}\?v=[^"]+">\s*)',
            r'\1\n  ' + css_line + '\n',
            s,
            count=1
        )
        print("✅ V75 CSS eklendi:", p.relative_to(ROOT))
    else:
        print("ℹ️ V75 CSS zaten var:", p.relative_to(ROOT))

    if "continue_ring_v75.js" not in s:
        s = re.sub(
            r'(\s*<script src="{{ url_for\(\'static\', filename=\'continue/continue_trip_core\.js\'\) }}\?v=[^"]+"></script>)',
            r'\1\n' + js_line,
            s,
            count=1
        )
        print("✅ V75 ring JS eklendi:", p.relative_to(ROOT))
    else:
        print("ℹ️ V75 ring JS zaten var:", p.relative_to(ROOT))

    p.write_text(s, encoding="utf-8")

print()
print("✅ V75 tamam. Mantık değişmedi, sadece endüstriyel tasarım kabuğu ve km halkası eklendi.")
