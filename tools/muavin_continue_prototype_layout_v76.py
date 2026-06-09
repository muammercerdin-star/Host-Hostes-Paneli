from pathlib import Path
from datetime import datetime
import shutil

ROOT = Path(".").resolve()
STAMP = datetime.now().strftime("%Y%m%d-%H%M%S")

CSS_WEB = ROOT / "static/continue/continue_v76.css"
CSS_AND = ROOT / "android_app/app/src/main/python/static/continue/continue_v76.css"

JS_WEB = ROOT / "static/continue/continue_v76.js"
JS_AND = ROOT / "android_app/app/src/main/python/static/continue/continue_v76.js"

TPLS = [
    ROOT / "templates/continue_trip.html",
    ROOT / "android_app/app/src/main/python/templates/continue_trip.html",
]

CSS = r'''
/* CONTINUE_PROTOTYPE_LAYOUT_V76 */
:root{
  --bg:#0b0d10;
  --panel:#12151a;
  --panel2:#181c23;
  --border:#1f2530;
  --red:#e03030;
  --red-dim:#3a1010;
  --amber:#e08820;
  --amber-dim:#2c1f08;
  --green:#1db87a;
  --green-dim:#0a2418;
  --blue:#3a8bff;
  --text:#d8dde8;
  --muted:#5a6478;
  --label:#8a95a8;
}

*,
*::before,
*::after{
  box-sizing:border-box;
}

html,
body{
  margin:0;
  padding:0;
  min-height:100vh;
  background:var(--bg);
  color:var(--text);
  font-family:"Rajdhani","Segoe UI",system-ui,sans-serif;
  overflow-x:hidden;
}

body{
  padding-bottom:86px;
}

.v76-shell{
  max-width:760px;
  margin:0 auto;
}

/* HEADER */
.hdr{
  display:flex;
  align-items:center;
  justify-content:space-between;
  padding:14px 20px;
  border-bottom:1px solid var(--border);
  background:var(--panel);
}

.hdr-brand{
  display:flex;
  align-items:center;
  gap:10px;
  min-width:0;
}

.hdr-icon{
  width:34px;
  height:34px;
  background:var(--red);
  border-radius:8px;
  display:grid;
  place-items:center;
  font-size:16px;
  box-shadow:0 0 12px #e0303055;
  flex:0 0 auto;
}

.hdr-title{
  font-size:18px;
  font-weight:800;
  letter-spacing:4px;
  color:#fff;
  line-height:1;
}

.hdr-sub{
  margin-top:5px;
  font-size:10px;
  letter-spacing:3px;
  color:var(--muted);
  font-family:ui-monospace,Menlo,monospace;
}

.hdr-clock{
  font-family:ui-monospace,Menlo,monospace;
  font-size:22px;
  font-weight:800;
  color:var(--amber);
  text-shadow:0 0 16px #e0882055;
  letter-spacing:2px;
  white-space:nowrap;
}

/* ROUTE BAR */
.route-bar{
  background:var(--panel2);
  border-bottom:1px solid var(--border);
  padding:10px 20px;
  display:flex;
  align-items:center;
  gap:12px;
  font-family:ui-monospace,Menlo,monospace;
  font-size:12px;
  color:var(--label);
  min-width:0;
}

.route-name{
  color:var(--text);
  font-size:13px;
  font-weight:800;
  letter-spacing:1px;
  white-space:nowrap;
  overflow:hidden;
  text-overflow:ellipsis;
  min-width:0;
}

.route-dot{
  color:var(--muted);
}

.route-plate{
  white-space:nowrap;
}

.live-badge{
  margin-left:auto;
  display:flex;
  align-items:center;
  gap:6px;
  font-size:11px;
  color:var(--red);
  letter-spacing:1px;
  font-weight:800;
  white-space:nowrap;
}

.live-dot{
  width:7px;
  height:7px;
  background:var(--red);
  border-radius:50%;
  animation:pulse-red 1.4s ease-in-out infinite;
  box-shadow:0 0 6px var(--red);
}

@keyframes pulse-red{
  0%,100%{opacity:1;transform:scale(1);}
  50%{opacity:.4;transform:scale(.7);}
}

/* GAUGES */
.gauges{
  display:grid;
  grid-template-columns:1fr 1fr 1fr;
  gap:1px;
  background:var(--border);
  border-bottom:1px solid var(--border);
}

.gauge-cell{
  min-width:0;
  background:var(--panel);
  padding:14px 8px;
  display:flex;
  flex-direction:column;
  align-items:center;
  gap:4px;
  text-align:center;
}

.gauge-label{
  font-size:10px;
  letter-spacing:2px;
  color:var(--muted);
  font-family:ui-monospace,Menlo,monospace;
  text-transform:uppercase;
}

.gauge-val{
  font-family:ui-monospace,Menlo,monospace;
  font-size:22px;
  font-weight:800;
  color:var(--text);
  line-height:1;
  max-width:100%;
  overflow:hidden;
  text-overflow:ellipsis;
  white-space:nowrap;
}

.gauge-val.amber{
  color:var(--amber);
  text-shadow:0 0 10px #e0882040;
}

.gauge-val.green{
  color:var(--green);
  text-shadow:0 0 10px #1db87a40;
}

.gauge-val.red{
  color:var(--red);
  text-shadow:0 0 10px #e0303040;
}

.gauge-unit{
  font-size:10px;
  color:var(--muted);
  letter-spacing:1px;
}

.occ-bar-track{
  width:80px;
  max-width:100%;
  height:4px;
  background:var(--border);
  border-radius:2px;
  overflow:hidden;
  margin-top:2px;
}

.occ-bar-fill{
  height:100%;
  background:linear-gradient(90deg,var(--green),var(--amber));
  border-radius:2px;
}

.occ-genders{
  display:flex;
  gap:8px;
  font-size:10px;
  font-family:ui-monospace,Menlo,monospace;
  margin-top:3px;
}

.g-m{color:var(--blue);}
.g-f{color:#e060c0;}

/* PROXIMITY */
.prox-section{
  padding:20px 20px 0;
}

.prox-card{
  background:var(--panel);
  border:1px solid var(--border);
  border-radius:16px;
  padding:20px;
  position:relative;
  overflow:hidden;
}

.prox-card::before{
  content:"";
  position:absolute;
  inset:0;
  background:repeating-linear-gradient(0deg,transparent,transparent 3px,rgba(255,255,255,.012) 3px,rgba(255,255,255,.012) 4px);
  pointer-events:none;
}

.prox-top{
  display:flex;
  align-items:flex-start;
  gap:18px;
  position:relative;
  z-index:1;
}

.ring-wrap{
  flex:0 0 110px;
  position:relative;
  width:110px;
  height:110px;
}

.ring-svg{
  width:110px;
  height:110px;
  transform:rotate(-90deg);
}

.ring-track{
  fill:none;
  stroke:var(--red-dim);
  stroke-width:6;
}

.ring-fill{
  fill:none;
  stroke:var(--blue);
  stroke-width:6;
  stroke-linecap:round;
  filter:drop-shadow(0 0 6px var(--blue));
  transition:stroke-dashoffset .9s cubic-bezier(.4,0,.2,1),stroke .4s ease,filter .4s ease;
}

.ring-center{
  position:absolute;
  inset:0;
  display:flex;
  flex-direction:column;
  align-items:center;
  justify-content:center;
}

.ring-km{
  font-family:ui-monospace,Menlo,monospace;
  font-size:24px;
  font-weight:900;
  color:var(--blue);
  text-shadow:0 0 14px var(--blue);
  line-height:1;
}

.ring-km-label{
  font-size:10px;
  letter-spacing:2px;
  color:var(--muted);
  font-family:ui-monospace,Menlo,monospace;
  margin-top:2px;
}

.ring-wrap[data-zone="mid"] .ring-fill{
  stroke:var(--amber);
  filter:drop-shadow(0 0 8px var(--amber));
}

.ring-wrap[data-zone="mid"] .ring-km{
  color:var(--amber);
  text-shadow:0 0 14px var(--amber);
}

.ring-wrap[data-zone="close"] .ring-fill{
  stroke:var(--red);
  filter:drop-shadow(0 0 12px var(--red));
  animation:ring-pulse 1s ease-in-out infinite;
}

.ring-wrap[data-zone="close"] .ring-km{
  color:var(--red);
  text-shadow:0 0 18px var(--red);
}

@keyframes ring-pulse{
  0%,100%{filter:drop-shadow(0 0 6px var(--red));}
  50%{filter:drop-shadow(0 0 20px var(--red)) drop-shadow(0 0 30px var(--red));}
}

.prox-info{
  flex:1;
  min-width:0;
  display:flex;
  flex-direction:column;
  gap:8px;
}

.prox-kicker{
  font-size:10px;
  letter-spacing:3px;
  color:var(--muted);
  font-family:ui-monospace,Menlo,monospace;
  text-transform:uppercase;
}

.prox-stop-name{
  font-size:30px;
  font-weight:900;
  color:#fff;
  line-height:1.05;
  letter-spacing:.3px;
  white-space:normal;
  word-break:break-word;
}

.prox-eta-row{
  display:flex;
  align-items:center;
  gap:8px;
  flex-wrap:wrap;
}

.prox-eta-val{
  font-family:ui-monospace,Menlo,monospace;
  font-size:18px;
  font-weight:900;
  color:var(--amber);
}

.prox-eta-label{
  font-size:11px;
  color:var(--muted);
  letter-spacing:1px;
}

.status-pill{
  display:inline-flex;
  align-items:center;
  gap:5px;
  padding:4px 10px;
  border-radius:20px;
  font-size:11px;
  font-weight:900;
  letter-spacing:1.5px;
  text-transform:uppercase;
  font-family:ui-monospace,Menlo,monospace;
  background:var(--red-dim);
  color:var(--red);
  border:1px solid #e0303033;
  margin-top:4px;
  width:fit-content;
}

.prox-distance-raw{
  position:absolute;
  left:-9999px;
  width:1px;
  height:1px;
  overflow:hidden;
}

.prox-metrics{
  display:grid;
  grid-template-columns:1fr 1fr;
  gap:10px;
  margin-top:16px;
  position:relative;
  z-index:1;
}

.pm-cell{
  background:var(--panel2);
  border:1px solid var(--border);
  border-radius:10px;
  padding:12px 14px;
  display:flex;
  align-items:center;
  gap:12px;
  cursor:pointer;
  color:inherit;
  font:inherit;
  text-align:left;
  min-width:0;
}

.pm-icon{
  font-size:20px;
  line-height:1;
  flex:0 0 auto;
}

.pm-val{
  font-family:ui-monospace,Menlo,monospace;
  font-size:20px;
  font-weight:900;
  color:var(--text);
  line-height:1;
}

.pm-lbl{
  font-size:10px;
  color:var(--muted);
  letter-spacing:1.5px;
  margin-top:2px;
}

.dist-track-wrap{
  margin-top:14px;
  position:relative;
  z-index:1;
}

.dist-labels{
  display:flex;
  justify-content:space-between;
  gap:8px;
  font-size:10px;
  font-family:ui-monospace,Menlo,monospace;
  color:var(--muted);
  margin-bottom:5px;
}

.dist-labels span{
  white-space:nowrap;
  overflow:hidden;
  text-overflow:ellipsis;
}

.dist-track{
  height:6px;
  background:var(--border);
  border-radius:3px;
  overflow:hidden;
  position:relative;
}

.dist-fill{
  height:100%;
  width:0%;
  background:linear-gradient(90deg,var(--red-dim),var(--red));
  border-radius:3px;
  transition:width .9s cubic-bezier(.4,0,.2,1);
  position:relative;
}

.dist-fill::after{
  content:"";
  position:absolute;
  right:0;
  top:-2px;
  width:10px;
  height:10px;
  background:var(--red);
  border-radius:50%;
  box-shadow:0 0 8px var(--red);
}

/* TIMELINE */
.timeline-section{
  padding:20px 20px 0;
}

.section-label{
  font-size:10px;
  letter-spacing:3px;
  color:var(--muted);
  font-family:ui-monospace,Menlo,monospace;
  margin-bottom:14px;
  display:flex;
  align-items:center;
  gap:8px;
}

.section-label::after{
  content:"";
  flex:1;
  height:1px;
  background:var(--border);
}

.tl{
  display:flex;
  flex-direction:column;
  gap:0;
  position:relative;
}

.tl-item{
  display:flex;
  gap:14px;
  position:relative;
}

.tl-spine{
  display:flex;
  flex-direction:column;
  align-items:center;
  flex:0 0 20px;
  width:20px;
}

.tl-node{
  width:14px;
  height:14px;
  border-radius:50%;
  border:2px solid var(--muted);
  background:var(--bg);
  flex:0 0 auto;
  z-index:1;
  margin-top:14px;
}

.tl-node.live{
  border-color:var(--red);
  background:var(--red);
  box-shadow:0 0 10px var(--red);
  animation:pulse-red 1.4s ease-in-out infinite;
}

.tl-node.next{
  border-color:var(--amber);
  background:transparent;
}

.tl-node.passed{
  border-color:var(--green);
  background:var(--green);
  opacity:.8;
}

.tl-node.upcoming{
  border-color:var(--border);
  background:transparent;
}

.tl-line{
  flex:1;
  width:1px;
  background:var(--border);
  margin:0 auto;
}

.tl-line.live{
  background:linear-gradient(var(--red),var(--border));
}

.tl-line.passed{
  background:var(--green);
  opacity:.4;
}

.tl-card{
  flex:1;
  min-width:0;
  background:var(--panel);
  border:1px solid var(--border);
  border-radius:10px;
  padding:12px 14px;
  margin-bottom:10px;
}

.tl-card.live-card{
  border-color:#e0303044;
  background:#12100e;
}

.tl-card.next-card{
  border-color:#e0882033;
}

.tl-card-head{
  display:flex;
  justify-content:space-between;
  align-items:flex-start;
  gap:10px;
  margin-bottom:8px;
}

.tl-stop-name{
  min-width:0;
  font-size:18px;
  font-weight:800;
  color:#fff;
  letter-spacing:.3px;
  word-break:break-word;
}

.tl-stop-name.muted{
  color:var(--label);
  font-weight:600;
}

.pill{
  flex:0 0 auto;
  font-size:9px;
  font-weight:900;
  letter-spacing:1.5px;
  padding:3px 8px;
  border-radius:20px;
  font-family:ui-monospace,Menlo,monospace;
  white-space:nowrap;
}

.pill.live{background:#3a0a0a;color:var(--red);border:1px solid #e0303033;}
.pill.next{background:var(--amber-dim);color:var(--amber);border:1px solid #e0882033;}
.pill.passed{background:var(--green-dim);color:var(--green);border:1px solid #1db87a33;}
.pill.upcoming{background:var(--panel2);color:var(--muted);border:1px solid var(--border);}

.tl-metrics{
  display:grid;
  grid-template-columns:repeat(4,minmax(0,1fr));
  gap:10px;
}

.tl-metric{
  min-width:0;
  display:flex;
  flex-direction:column;
  gap:1px;
}

.tl-m-val{
  font-family:ui-monospace,Menlo,monospace;
  font-size:15px;
  font-weight:900;
  color:var(--text);
  white-space:nowrap;
  overflow:hidden;
  text-overflow:ellipsis;
}

.tl-m-lbl{
  font-size:9px;
  color:var(--muted);
  letter-spacing:1px;
}

/* DOCK */
.dock{
  position:fixed;
  bottom:0;
  left:0;
  right:0;
  background:var(--panel);
  border-top:1px solid var(--border);
  display:flex;
  padding:8px 0 max(env(safe-area-inset-bottom),8px);
  z-index:100;
}

.dock-btn{
  flex:1;
  display:flex;
  flex-direction:column;
  align-items:center;
  gap:4px;
  padding:8px 0;
  background:none;
  border:0;
  color:var(--muted);
  font-family:inherit;
  font-size:11px;
  letter-spacing:1px;
  cursor:pointer;
  text-decoration:none;
}

.dock-btn.active{
  color:var(--red);
}

.dock-btn i{
  font-size:20px;
  line-height:1;
}

/* END TRIP */
.end-wrap{
  padding:20px 20px 100px;
  text-align:center;
}

.end-btn{
  width:100%;
  padding:14px;
  background:#1a0a0a;
  border:1px solid #e0303033;
  border-radius:10px;
  color:var(--red);
  font-family:inherit;
  font-size:14px;
  font-weight:900;
  letter-spacing:2px;
  cursor:pointer;
}

/* MODALS / SHEETS */
.live-sheet-overlay,
.end-trip-overlay{
  position:fixed;
  inset:0;
  background:rgba(0,0,0,.62);
  opacity:0;
  pointer-events:none;
  transition:.2s;
  z-index:200;
}

.live-sheet-overlay.show,
.end-trip-overlay.show{
  opacity:1;
  pointer-events:auto;
}

.live-stop-sheet{
  position:fixed;
  left:12px;
  right:12px;
  bottom:92px;
  max-height:72vh;
  overflow:auto;
  background:var(--panel);
  border:1px solid var(--border);
  border-radius:18px;
  padding:14px;
  z-index:210;
  transform:translateY(120%);
  transition:.25s;
}

.live-stop-sheet.show{
  transform:translateY(0);
}

.sheet-head{
  display:flex;
  justify-content:space-between;
  gap:12px;
  align-items:flex-start;
}

.sheet-kicker{
  font-size:11px;
  letter-spacing:2px;
  color:var(--muted);
}

.sheet-title{
  margin:2px 0;
  color:#fff;
}

.sheet-sub{
  margin:0;
  color:var(--muted);
}

.sheet-close{
  width:34px;
  height:34px;
  border-radius:999px;
  border:1px solid var(--border);
  background:var(--panel2);
  color:var(--text);
  font-size:22px;
}

.sheet-body{
  margin-top:12px;
}

.sheet-empty{
  color:var(--muted);
  padding:20px;
  text-align:center;
}

.end-trip-box{
  position:fixed;
  left:18px;
  right:18px;
  top:50%;
  transform:translateY(-50%);
  background:var(--panel);
  border:1px solid var(--border);
  border-radius:18px;
  padding:18px;
  z-index:220;
}

.end-trip-top{
  display:flex;
  gap:12px;
  align-items:center;
}

.end-trip-mark{
  font-size:28px;
}

.end-trip-title{
  margin:0;
  color:#fff;
}

.end-trip-small,
.end-trip-text{
  color:var(--muted);
}

.end-trip-actions{
  display:flex;
  gap:10px;
  margin-top:14px;
}

.end-trip-btn{
  flex:1;
  border:1px solid var(--border);
  background:var(--panel2);
  color:var(--text);
  border-radius:12px;
  padding:12px;
  font-weight:800;
}

.end-trip-ok{
  color:var(--red);
  border-color:#e0303033;
  background:#1a0a0a;
}

.bag-photo-viewer{
  display:none;
}

.continue-refresh-v49-btn{
  position:fixed;
  right:18px;
  top:90px;
  z-index:150;
  width:58px;
  height:58px;
  border-radius:18px;
  border:1px solid var(--border);
  background:#111827;
  color:#fff;
  box-shadow:0 0 22px rgba(58,139,255,.25);
  font-size:26px;
}

@media(max-width:420px){
  .hdr{padding:13px 16px;}
  .route-bar{padding:10px 16px;}
  .prox-section,
  .timeline-section{padding-left:14px;padding-right:14px;}

  .gauge-cell{padding:12px 5px;}
  .gauge-val{font-size:19px;}
  .gauge-label{font-size:9px;letter-spacing:2px;}

  .prox-card{padding:16px;}
  .prox-top{gap:12px;}
  .ring-wrap{width:92px;height:92px;flex-basis:92px;}
  .ring-svg{width:92px;height:92px;}
  .prox-stop-name{font-size:25px;}
  .ring-km{font-size:22px;}

  .pm-cell{padding:11px 10px;gap:8px;}
  .tl-metrics{gap:7px;}
  .tl-m-val{font-size:13px;}
}
'''

JS = r'''
/* CONTINUE_PROTOTYPE_LAYOUT_V76_JS */
(function(){
  if(window.CONTINUE_V76_READY) return;
  window.CONTINUE_V76_READY = true;

  const CIRC = 276.46;
  const BOOT = window.CONTINUE_BOOT || {};
  let maxKm = 50;

  function q(sel){
    return document.querySelector(sel);
  }

  function text(v){
    return String(v == null ? "" : v).trim();
  }

  function norm(v){
    return text(v).toLocaleLowerCase("tr-TR").replace(/\s+/g, " ");
  }

  function parseKm(v){
    const s = text(v).replace(",", ".");
    const m = s.match(/-?\d+(?:\.\d+)?/);
    if(!m) return NaN;
    return Number(m[0]);
  }

  function fmtKm(n){
    if(!Number.isFinite(n)) return "—";
    if(n >= 10) return String(Math.round(n));
    return String(Math.round(n * 10) / 10).replace(".0", "");
  }

  function updateClockFallback(){
    const el = document.getElementById("liveClockText");
    if(!el) return;
    if(text(el.textContent) && text(el.textContent) !== "--:--") return;

    const now = new Date();
    const h = String(now.getHours()).padStart(2,"0");
    const m = String(now.getMinutes()).padStart(2,"0");
    el.textContent = h + ":" + m;
  }

  function updateRing(){
    const dist = document.getElementById("liveDistanceValue");
    const ring = document.getElementById("ringFill");
    const ringKm = document.getElementById("ringKm");
    const wrap = document.getElementById("ringWrap");

    if(!dist || !ring || !ringKm || !wrap) return;

    const km = parseKm(dist.textContent);

    if(!Number.isFinite(km)){
      ring.style.strokeDashoffset = CIRC;
      ringKm.textContent = "—";
      wrap.dataset.zone = "far";
      return;
    }

    maxKm = Math.max(maxKm, Math.ceil(km / 10) * 10, 10);

    const ratio = Math.max(0, Math.min(1, 1 - km / maxKm));
    ring.style.strokeDashoffset = String(CIRC * (1 - ratio));
    ringKm.textContent = fmtKm(km);

    if(km <= 5){
      wrap.dataset.zone = "close";
    }else if(km <= 15){
      wrap.dataset.zone = "mid";
    }else{
      wrap.dataset.zone = "far";
    }
  }

  function updateRouteProgress(){
    const stops = Array.isArray(BOOT.routeStops) ? BOOT.routeStops : [];
    const cur = text(document.getElementById("liveCurrentStopName")?.textContent);
    const bar = document.getElementById("routeBar");
    const pct = document.getElementById("distPct");
    const start = document.getElementById("routeStartLabel");
    const end = document.getElementById("routeEndLabel");

    if(start && stops.length) start.textContent = stops[0];
    if(end && stops.length) end.textContent = stops[stops.length - 1];

    if(!bar || !pct || !stops.length || !cur) return;

    const idx = stops.findIndex(s => norm(s) === norm(cur));
    if(idx < 0 || stops.length < 2) return;

    const p = Math.max(0, Math.min(100, Math.round((idx / (stops.length - 1)) * 100)));
    bar.style.width = p + "%";
    pct.textContent = "%" + p + " tamamlandı";
  }

  function syncTopStatus(){
    const top = document.getElementById("liveTopStatusText");
    const eta = document.getElementById("liveEtaValue");
    if(!top || !eta) return;

    const v = text(eta.textContent);
    if(!v || v === "-" || v === "—") return;

    if(/geç/i.test(v)){
      top.textContent = v;
      top.classList.remove("green");
      top.classList.add("red");
    }else if(/erken/i.test(v)){
      top.textContent = v;
      top.classList.remove("red");
      top.classList.add("green");
    }
  }

  function boot(){
    updateClockFallback();
    updateRing();
    updateRouteProgress();
    syncTopStatus();

    const targets = [
      document.getElementById("liveDistanceValue"),
      document.getElementById("liveCurrentStopName"),
      document.getElementById("liveEtaValue")
    ].filter(Boolean);

    if(window.MutationObserver){
      const obs = new MutationObserver(function(){
        updateRing();
        updateRouteProgress();
        syncTopStatus();
      });
      targets.forEach(el => obs.observe(el, {childList:true, characterData:true, subtree:true}));
    }

    setInterval(function(){
      updateClockFallback();
      updateRing();
      updateRouteProgress();
      syncTopStatus();
    }, 1000);
  }

  if(document.readyState === "loading"){
    document.addEventListener("DOMContentLoaded", boot);
  }else{
    boot();
  }
})();
'''

TPL = r'''<!doctype html>
<html lang="tr">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
  <title>Canlı Durak — Muavin</title>
  <link rel="stylesheet" href="{{ url_for('static', filename='continue/continue_v76.css') }}?v=prototype-layout-v76">
</head>

<body>
<div class="v76-shell">

  <header class="hdr">
    <div class="hdr-brand">
      <div class="hdr-icon">🎙️</div>
      <div>
        <div class="hdr-title">MUAVİN</div>
        <div class="hdr-sub">ASİSTAN v2</div>
      </div>
    </div>

    <div class="hdr-clock" id="liveClockText">--:--</div>
  </header>

  <div class="route-bar">
    <span class="route-name">{{ trip["route"] or "Denizli-İstanbul" }}</span>
    <span class="route-dot">·</span>
    <span class="route-plate">{{ trip["plate"] or "45KH999" }}</span>
    <div class="live-badge">
      <div class="live-dot"></div>
      CANLI
    </div>
  </div>

  <div class="gauges">
    <div class="gauge-cell">
      <div class="gauge-label">HIZ</div>
      <div class="gauge-val amber" id="liveSpeedText">{{ (live_runtime.speed|int if live_runtime and live_runtime.speed else 0) }} km/sa</div>
      <div class="gauge-unit">km/sa</div>
    </div>

    <div class="gauge-cell">
      <div class="gauge-label">DOLULUK</div>
      <div class="gauge-val">{{ live_summary.passenger_count }} / {{ live_summary.total_seats }}</div>
      <div class="occ-bar-track">
        <div class="occ-bar-fill" style="width:{{ ((live_summary.passenger_count * 100 / live_summary.total_seats) if live_summary.total_seats else 0)|round(0) }}%"></div>
      </div>
      <div class="occ-genders">
        <span class="g-m">♂ {{ live_summary.male_count or 0 }}</span>
        <span class="g-f">♀ {{ live_summary.female_count or 0 }}</span>
      </div>
    </div>

    <div class="gauge-cell">
      <div class="gauge-label">DURUM</div>
      <div class="gauge-val green" id="liveTopStatusText">Planında</div>
      <div class="gauge-unit">canlı takip</div>
    </div>
  </div>

  {% set current_name = (live_runtime.live_stop if live_runtime and live_runtime.live_stop else live_current.name) or "Durak seçilmedi" %}
  {% set current_distance = (live_runtime.gps_km if live_runtime and live_runtime.gps_km else live_current.distance) or "—" %}
  {% set current_eta = (live_runtime.eta_main if live_runtime and live_runtime.eta_main else live_current.eta) or "—" %}

  <section class="prox-section">
    <div class="prox-card live-summary-trigger" id="liveCurrentCard" role="button" tabindex="0" aria-label="Canlı durak özetini aç">

      <div class="prox-top">
        <div class="ring-wrap" id="ringWrap">
          <svg class="ring-svg" viewBox="0 0 110 110">
            <circle class="ring-track" cx="55" cy="55" r="44"></circle>
            <circle class="ring-fill" id="ringFill" cx="55" cy="55" r="44" stroke-dasharray="276.46" stroke-dashoffset="276.46"></circle>
          </svg>
          <div class="ring-center">
            <div class="ring-km" id="ringKm">—</div>
            <div class="ring-km-label">KM</div>
          </div>
        </div>

        <div class="prox-info">
          <div class="prox-kicker">ŞU ANKİ DURAK</div>
          <div class="prox-stop-name" id="liveCurrentStopName">{{ current_name }}</div>
          <div class="prox-eta-row">
            <span class="prox-eta-val" id="liveEtaValue">{{ current_eta }}</span>
            <span class="prox-eta-label">TAHMİNİ / DURUM</span>
          </div>
          <div class="status-pill">
            <div class="live-dot"></div>
            CANLI TAKİP
          </div>
        </div>
      </div>

      <div id="liveDistanceValue" class="stop-distance-value prox-distance-raw" data-stop-name="{{ current_name }}">{{ current_distance }}</div>

      <div class="prox-metrics">
        <button class="pm-cell" type="button" id="liveOffloadMetric" data-kind="offload" aria-label="Bu durakta inecek yolcuları göster">
          <div class="pm-icon">🧍</div>
          <div class="pm-data">
            <div class="pm-val" id="liveOffloadCount">{{ live_current.off_count or 0 }}</div>
            <div class="pm-lbl">İNECEK YOLCU</div>
          </div>
        </button>

        <button class="pm-cell" type="button" id="liveBagajMetric" data-kind="bagaj" aria-label="Bu durakta indirilecek bagajları göster">
          <div class="pm-icon">🧳</div>
          <div class="pm-data">
            <div class="pm-val" id="liveBagajCount">{{ live_current.bagaj_count or 0 }}</div>
            <span id="liveEmanetCount" hidden></span>
            <div class="pm-lbl">BAGAJ</div>
          </div>
        </button>
      </div>

      <div class="dist-track-wrap">
        <div class="dist-labels">
          <span id="routeStartLabel">Başlangıç</span>
          <span id="distPct">%0 tamamlandı</span>
          <span id="routeEndLabel">Varış</span>
        </div>
        <div class="dist-track">
          <div class="dist-fill" id="routeBar"></div>
        </div>
      </div>
    </div>
  </section>

  <section class="timeline-section">
    <div class="section-label">GÜZERGAH</div>

    <div class="tl" id="tlContainer">
      {% for stop in live_stops %}
      {% set kind = stop.kind or "upcoming" %}
      <div class="tl-item">
        <div class="tl-spine">
          <div class="tl-node {{ kind }}"></div>
          {% if not loop.last %}
            <div class="tl-line {{ kind }}"></div>
          {% endif %}
        </div>

        <div class="tl-card {% if kind == 'live' %}live-card{% elif kind == 'next' %}next-card{% endif %}">
          <div class="tl-card-head">
            <div class="tl-stop-name {% if kind == 'passed' %}muted{% endif %}">{{ stop.name }}</div>

            {% if kind == "live" %}
              <div class="pill live">● CANLI</div>
            {% elif kind == "next" %}
              <div class="pill next">⟶ SONRAKI</div>
            {% elif kind == "passed" %}
              <div class="pill passed">✓ GEÇİLDİ</div>
            {% else %}
              <div class="pill upcoming">{{ stop.eta or stop.status or "Bekliyor" }}</div>
            {% endif %}
          </div>

          <div class="tl-metrics">
            <div class="tl-metric">
              <div class="tl-m-val">{{ stop.eta or "—" }}</div>
              <div class="tl-m-lbl">VARIŞ</div>
            </div>

            <div class="tl-metric">
              <div class="tl-m-val stop-distance-value" data-stop-name="{{ stop.name }}">{{ stop.distance or "—" }}</div>
              <div class="tl-m-lbl">MESAFE</div>
            </div>

            <div class="tl-metric">
              <div class="tl-m-val">{{ stop.off_count or 0 }}</div>
              <div class="tl-m-lbl">İNECEK</div>
            </div>

            <div class="tl-metric">
              <div class="tl-m-val">{{ stop.bagaj_label or stop.bagaj_count or 0 }}</div>
              <div class="tl-m-lbl">BAGAJ</div>
            </div>
          </div>
        </div>
      </div>
      {% endfor %}
    </div>
  </section>

  <div class="end-wrap">
    <form id="endTripForm" method="post" action="{{ url_for('end_trip') }}">
      {% if csrf_token is defined %}
        <input type="hidden" name="csrf_token" value="{{ csrf_token }}">
      {% endif %}
      <button class="end-btn" type="submit">⛔ &nbsp;SEFERİ BİTİR</button>
    </form>
  </div>

</div>

<nav class="dock">
  <a class="dock-btn active" href="{{ url_for('continue_trip') }}">
    <i>🚌</i><span>CANLI</span>
  </a>

  <a class="dock-btn" id="continueSeatMapBtn" href="{{ url_for('seats_page') }}">
    <i>💺</i><span>KOLTUK</span>
  </a>

  <a class="dock-btn" href="{{ url_for('passenger_control') }}">
    <i>👥</i><span>YOLCU</span>
  </a>

  <a class="dock-btn" href="{{ url_for('live_map_page') }}">
    <i>🗺️</i><span>HARİTA</span>
  </a>

  <button class="dock-btn" type="button">
    <i>📣</i><span>ANONS</span>
  </button>
</nav>

<div class="live-sheet-overlay" id="liveStopSheetOverlay"></div>

<section class="live-stop-sheet" id="liveStopSheet" aria-hidden="true">
  <div class="sheet-head">
    <div>
      <div class="sheet-kicker" id="liveStopSheetKicker">Canlı durak</div>
      <h2 class="sheet-title" id="liveStopSheetTitle">Durak detayı</h2>
      <p class="sheet-sub" id="liveStopSheetSub">Yükleniyor...</p>
    </div>

    <button class="sheet-close" type="button" id="liveStopSheetClose" aria-label="Kapat">×</button>
  </div>

  <div class="sheet-body" id="liveStopSheetBody">
    <div class="sheet-empty">Yükleniyor...</div>
  </div>
</section>

<div class="end-trip-overlay" id="endTripOverlay" aria-hidden="true">
  <div class="end-trip-box" role="dialog" aria-modal="true" aria-labelledby="endTripTitle">
    <div class="end-trip-top">
      <div class="end-trip-mark">⛔</div>
      <div>
        <h2 class="end-trip-title" id="endTripTitle">Seferi bitirelim mi?</h2>
        <p class="end-trip-small">Aktif sefer sonlandırılacak.</p>
      </div>
    </div>

    <p class="end-trip-text">Sefer tamamlandıysa işlemi bitirebilirsin. Emin değilsen iptal edip ekrana dönebilirsin.</p>

    <div class="end-trip-actions">
      <button type="button" class="end-trip-btn end-trip-cancel" id="endTripCancel">İptal</button>
      <button type="button" class="end-trip-btn end-trip-ok" id="endTripOk">Seferi Bitir</button>
    </div>
  </div>
</div>

<div class="bag-photo-viewer" id="bagPhotoViewer" aria-hidden="true">
  <button type="button" id="bagViewerClose">×</button>
  <img id="bagViewerImg" src="" alt="Bagaj fotoğrafı">
  <div id="bagViewerTitle">Fotoğraf</div>
  <div id="bagViewerCaption">—</div>
  <button type="button" id="bagViewerPrev">← Önceki</button>
  <button type="button" id="bagViewerNext">Sonraki →</button>
</div>

<script>
(function(){
  const form = document.getElementById("endTripForm");
  const overlay = document.getElementById("endTripOverlay");
  const cancel = document.getElementById("endTripCancel");
  const ok = document.getElementById("endTripOk");

  if(!form || !overlay || !cancel || !ok) return;

  let confirmed = false;

  function openModal(){
    overlay.classList.add("show");
    overlay.setAttribute("aria-hidden", "false");
    document.body.style.overflow = "hidden";
  }

  function closeModal(){
    overlay.classList.remove("show");
    overlay.setAttribute("aria-hidden", "true");
    document.body.style.overflow = "";
  }

  function clearTripLocalMemory(){
    try{
      const tripKey = {{ ((trip['route'] ~ '|' ~ trip['plate'])|replace(' ','_')) | tojson | safe }};

      const exactKeys = [
        "liveStop:" + tripKey,
        "passedStops:" + tripKey,
        "boardsMap:" + tripKey,
        "standingTotals:" + tripKey,
        "standingItems:" + tripKey,
        "continueTripStop:" + tripKey,
        "continueTripStop:last",
        "stopFlowSummary:" + tripKey,
        "stopFlowLiveEvents:" + tripKey
      ];

      exactKeys.forEach(k => localStorage.removeItem(k));

      Object.keys(localStorage).forEach(k => {
        if(
          k.includes(tripKey) &&
          (
            k.startsWith("liveStop:") ||
            k.startsWith("passedStops:") ||
            k.startsWith("boardsMap:") ||
            k.startsWith("standingTotals:") ||
            k.startsWith("standingItems:") ||
            k.startsWith("continueTripStop:") ||
            k.startsWith("stopFlowSummary:") ||
            k.startsWith("stopFlowLiveEvents:")
          )
        ){
          localStorage.removeItem(k);
        }
      });
    }catch(_){}
  }

  form.addEventListener("submit", function(e){
    if(confirmed) return;
    e.preventDefault();
    openModal();
  });

  cancel.addEventListener("click", closeModal);

  overlay.addEventListener("click", function(e){
    if(e.target === overlay) closeModal();
  });

  document.addEventListener("keydown", function(e){
    if(e.key === "Escape" && overlay.classList.contains("show")){
      closeModal();
    }
  });

  ok.addEventListener("click", function(){
    confirmed = true;
    clearTripLocalMemory();
    closeModal();
    form.submit();
  });
})();
</script>

<script src="/static/seats/voice-tts.js?v=continue-tts-bridge-1"></script>

<script id="continue-boot-data">
window.CONTINUE_BOOT = {
  tripId: {{ trip['id'] | tojson | safe }},
  tripDate: {{ (trip['date'] or '') | tojson | safe }},
  tripKey: {{ ((trip['route'] ~ '|' ~ trip['plate'])|replace(' ','_')) | tojson | safe }},

  runtimeGpsKm: {{ (live_runtime.gps_km if live_runtime and live_runtime.gps_km else "") | tojson | safe }},
  runtimeSpeed: {{ (live_runtime.speed if live_runtime else 0) | tojson | safe }},
  runtimeStop: {{ (live_runtime.live_stop if live_runtime and live_runtime.live_stop else "") | tojson | safe }},
  runtimeEta: {{ (live_runtime.eta_main if live_runtime and live_runtime.eta_main else "") | tojson | safe }},

  routeStops: {{ stops | tojson | safe }},
  csrfToken: {{ (csrf_token if csrf_token is defined else "") | tojson | safe }},

  routeCoords: {{ continue_route_coords | default([]) | tojson | safe }},
  scheduleItems: {{ continue_schedule_items | default([]) | tojson | safe }},

  liveBagajCount: {{ (live_current.bagaj_count if live_current and live_current.bagaj_count is defined else 0) | tojson | safe }},
  liveEmanetCount: {{ (live_current.emanet_count if live_current and live_current.emanet_count is defined else (live_current.consignment_count if live_current and live_current.consignment_count is defined else 0)) | tojson | safe }}
};
</script>

<script src="{{ url_for('static', filename='continue/continue_trip_core.js') }}?v=sync-blank-guard-v72b"></script>
<script src="{{ url_for('static', filename='continue/continue_v76.js') }}?v=prototype-layout-v76"></script>
<script src="{{ url_for('static', filename='continue/continue_bag_emanet.js') }}?v=bag-emanet-clean-1"></script>
<script src="{{ url_for('static', filename='continue/continue_refresh_button_v49.js') }}?v=refresh-v49"></script>
</body>
</html>
'''

print("===== CONTINUE PROTOTYPE LAYOUT V76 =====")

for p, content in [(CSS_WEB, CSS), (CSS_AND, CSS), (JS_WEB, JS), (JS_AND, JS)]:
    p.parent.mkdir(parents=True, exist_ok=True)
    if p.exists():
        b = p.with_name(p.name + f".bak-prototype-v76-{STAMP}")
        shutil.copy2(p, b)
        print("📦 Yedek:", b.relative_to(ROOT))
    p.write_text(content, encoding="utf-8")
    print("✅ Yazıldı:", p.relative_to(ROOT))

for p in TPLS:
    if not p.exists():
        print("⚠️ Template yok:", p.relative_to(ROOT))
        continue

    b = p.with_name(p.name + f".bak-prototype-v76-{STAMP}")
    shutil.copy2(p, b)
    print("📦 Yedek:", b.relative_to(ROOT))

    p.write_text(TPL, encoding="utf-8")
    print("✅ V76 prototype template yazıldı:", p.relative_to(ROOT))

print()
print("✅ V76 tamam. Sayfa yapısı prototipe çevrildi, canlı motor scriptleri korundu.")
