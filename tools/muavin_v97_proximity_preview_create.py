from pathlib import Path
from datetime import datetime

ROOT = Path(".").resolve()
OUTDIR = ROOT / "static" / "continue"
OUTDIR.mkdir(parents=True, exist_ok=True)

HTML = OUTDIR / "v97_proximity_preview.html"
CSS = OUTDIR / "v97_proximity_preview.css"
JS = OUTDIR / "v97_proximity_preview.js"

print("===== V97 PROXIMITY RING PREVIEW OLUŞTURMA =====")
print("ROOT:", ROOT)

html = r'''<!doctype html>
<html lang="tr">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
  <title>V97 Canlı Durak Proximity Preview</title>
  <link rel="stylesheet" href="./v97_proximity_preview.css?v=1">
</head>
<body>

<header class="v97-hdr">
  <div class="v97-brand">
    <div class="v97-logo">🎙️</div>
    <div>
      <div class="v97-title">MUAVİN</div>
      <div class="v97-sub">ASİSTAN V97</div>
    </div>
  </div>
  <div class="v97-clock" id="clockEl">--:--</div>
</header>

<section class="v97-route">
  <b>DENİZLİ → İSTANBUL</b>
  <span>·</span>
  <span>45KH999</span>
  <em><i></i> CANLI</em>
</section>

<section class="v97-gauges">
  <div>
    <small>HIZ</small>
    <b id="speedVal">86</b>
    <span>km/sa</span>
  </div>
  <div>
    <small>DOLULUK</small>
    <b>38/45</b>
    <div class="v97-occ"><i style="width:84%"></i></div>
    <span class="v97-gender">♂ 21&nbsp;&nbsp;♀ 17</span>
  </div>
  <div>
    <small>DURUM</small>
    <b class="green">Planında</b>
    <span>+0 dk</span>
  </div>
</section>

<main class="v97-shell">

  <section class="v97-prox-card">
    <div class="v97-prox-top">
      <div class="v97-ring-wrap">
        <svg class="v97-ring" viewBox="0 0 120 120">
          <circle class="v97-ring-track" cx="60" cy="60" r="48"></circle>
          <circle class="v97-ring-fill" id="ringFill" cx="60" cy="60" r="48"></circle>
        </svg>
        <div class="v97-ring-center">
          <b id="ringKm">—</b>
          <span>KM</span>
        </div>
      </div>

      <div class="v97-info">
        <small>ŞU ANKİ DURAK</small>
        <h1 id="currentStopName">Uşak</h1>
        <p><b id="etaVal">14:45</b> <span>TAHMİNİ VARIŞ</span></p>
        <div class="v97-live-pill"><i></i> CANLI TAKİP</div>
      </div>
    </div>

    <div class="v97-mini-grid">
      <button>
        <i>🧍</i>
        <b id="offloadCount">3</b>
        <span>İNECEK YOLCU</span>
      </button>
      <button>
        <i>🧳</i>
        <b id="bagajCount">2</b>
        <span>BAGAJ</span>
      </button>
    </div>

    <div class="v97-route-progress">
      <div>
        <span>DENİZLİ</span>
        <b id="routePct">%61 tamamlandı</b>
        <span>İSTANBUL</span>
      </div>
      <div class="v97-progress-track">
        <i id="routeBar" style="width:61%"></i>
      </div>
    </div>
  </section>

  <section class="v97-timeline-section">
    <div class="v97-section-title">GÜZERGAH</div>
    <div class="v97-timeline" id="timeline"></div>
  </section>

</main>

<nav class="v97-dock">
  <button class="active">🚌<span>CANLI</span></button>
  <button>💺<span>KOLTUK</span></button>
  <button>👥<span>YOLCU</span></button>
  <button>🗺️<span>HARİTA</span></button>
  <button>📣<span>ANONS</span></button>
</nav>

<div class="v97-demo">
  <small>SİMÜLASYON</small>
  <button onclick="simKm(48)">48 km</button>
  <button onclick="simKm(20)">20 km</button>
  <button onclick="simKm(8)">8 km</button>
  <button onclick="simKm(2)">2 km</button>
  <button onclick="simKm(0)">0 km</button>
  <button onclick="simAuto()">▶ OTO</button>
</div>

<script src="./v97_proximity_preview.js?v=1"></script>
</body>
</html>
'''

css = r''':root{
  --bg:#080b10;
  --panel:#11151c;
  --panel2:#171c25;
  --line:#222938;
  --text:#e8edf7;
  --muted:#7b8496;
  --red:#ff304f;
  --amber:#f0a229;
  --green:#22c982;
  --blue:#3a8bff;
}

*{box-sizing:border-box;margin:0;padding:0}
body{
  min-height:100vh;
  background:
    radial-gradient(circle at top right,rgba(30,80,170,.20),transparent 38%),
    linear-gradient(180deg,#070a0f,#0a0d13 45%,#07090d);
  color:var(--text);
  font-family:system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;
  padding-bottom:92px;
}

.v97-hdr{
  height:78px;
  padding:16px 20px;
  display:flex;
  align-items:center;
  justify-content:space-between;
  background:#10141b;
  border-bottom:1px solid var(--line);
}

.v97-brand{display:flex;align-items:center;gap:12px}
.v97-logo{
  width:48px;height:48px;
  border-radius:14px;
  display:grid;place-items:center;
  background:linear-gradient(135deg,#ff304f,#a70f22);
  box-shadow:0 0 24px rgba(255,48,79,.30);
}
.v97-title{
  font-size:25px;
  letter-spacing:8px;
  font-weight:900;
}
.v97-sub{
  font-size:12px;
  color:var(--muted);
  letter-spacing:6px;
}
.v97-clock{
  font-size:32px;
  color:var(--amber);
  font-family:monospace;
  font-weight:900;
  letter-spacing:5px;
}

.v97-route{
  height:54px;
  padding:0 20px;
  display:flex;
  align-items:center;
  gap:13px;
  background:#141922;
  border-bottom:1px solid var(--line);
  color:var(--muted);
}
.v97-route b{
  color:var(--text);
  letter-spacing:3px;
  font-size:20px;
}
.v97-route em{
  margin-left:auto;
  color:var(--red);
  font-style:normal;
  letter-spacing:3px;
  font-weight:900;
}
.v97-route em i,
.v97-live-pill i{
  display:inline-block;
  width:8px;height:8px;
  border-radius:50%;
  background:var(--red);
  box-shadow:0 0 14px var(--red);
  margin-right:8px;
  animation:v97Blink 1.2s ease-in-out infinite;
}

@keyframes v97Blink{
  0%,100%{opacity:1;transform:scale(1)}
  50%{opacity:.35;transform:scale(.72)}
}

.v97-gauges{
  display:grid;
  grid-template-columns:1fr 1fr 1fr;
  border-bottom:1px solid var(--line);
  background:var(--line);
  gap:1px;
}
.v97-gauges > div{
  min-height:98px;
  background:#10141b;
  display:flex;
  flex-direction:column;
  align-items:center;
  justify-content:center;
  gap:5px;
}
.v97-gauges small{
  color:var(--muted);
  letter-spacing:5px;
  font-weight:800;
}
.v97-gauges b{
  font-size:36px;
  line-height:1;
}
.v97-gauges b.green{
  font-size:23px;
  color:var(--green);
}
.v97-gauges span{
  color:var(--muted);
  font-size:14px;
}
.v97-occ{
  width:110px;height:7px;
  background:#252b38;
  border-radius:99px;
  overflow:hidden;
}
.v97-occ i{
  display:block;
  height:100%;
  background:linear-gradient(90deg,var(--green),var(--amber));
  border-radius:99px;
}
.v97-gender{color:#79a8ff !important}

.v97-shell{
  padding:22px 20px;
}

.v97-prox-card{
  position:relative;
  overflow:hidden;
  border:1px solid var(--line);
  border-radius:28px;
  padding:26px 22px;
  background:
    repeating-linear-gradient(0deg,transparent,transparent 4px,rgba(255,255,255,.018) 5px),
    linear-gradient(180deg,rgba(255,255,255,.035),rgba(255,255,255,.012)),
    #11151c;
  box-shadow:0 20px 50px rgba(0,0,0,.35);
}

.v97-prox-card:before{
  content:"";
  position:absolute;
  width:180px;height:180px;
  left:-40px;top:20px;
  background:radial-gradient(circle,rgba(255,48,79,.25),transparent 66%);
  pointer-events:none;
}

.v97-prox-top{
  position:relative;
  display:flex;
  gap:25px;
  align-items:center;
}

.v97-ring-wrap{
  position:relative;
  width:126px;height:126px;
  flex:0 0 auto;
}
.v97-ring{
  width:126px;height:126px;
  transform:rotate(-90deg);
}
.v97-ring-track{
  fill:none;
  stroke:rgba(255,255,255,.08);
  stroke-width:9;
}
.v97-ring-fill{
  fill:none;
  stroke:var(--blue);
  stroke-width:9;
  stroke-linecap:round;
  stroke-dasharray:301.59;
  stroke-dashoffset:301.59;
  filter:drop-shadow(0 0 10px var(--blue));
  transition:stroke-dashoffset .9s ease, stroke .3s ease, filter .3s ease;
}
.v97-ring-center{
  position:absolute;
  inset:0;
  display:grid;
  place-items:center;
  align-content:center;
}
.v97-ring-center b{
  font-family:monospace;
  font-size:36px;
  color:var(--blue);
  text-shadow:0 0 18px var(--blue);
}
.v97-ring-center span{
  color:var(--muted);
  letter-spacing:4px;
  font-weight:800;
  font-size:13px;
}

.v97-info small{
  color:var(--muted);
  letter-spacing:7px;
  font-weight:900;
}
.v97-info h1{
  margin-top:10px;
  font-size:42px;
  line-height:1;
  color:white;
}
.v97-info p{
  margin-top:14px;
}
.v97-info p b{
  color:var(--amber);
  font-size:30px;
  font-family:monospace;
}
.v97-info p span{
  color:var(--muted);
  letter-spacing:3px;
  margin-left:8px;
}
.v97-live-pill{
  margin-top:18px;
  display:inline-flex;
  align-items:center;
  padding:8px 22px;
  border-radius:99px;
  background:rgba(255,48,79,.14);
  border:1px solid rgba(255,48,79,.35);
  color:#ff687d;
  letter-spacing:5px;
  font-weight:900;
}

.v97-mini-grid{
  position:relative;
  display:grid;
  grid-template-columns:1fr 1fr;
  gap:16px;
  margin-top:24px;
}
.v97-mini-grid button{
  border:1px solid var(--line);
  border-radius:20px;
  background:var(--panel2);
  color:var(--text);
  min-height:92px;
  display:grid;
  grid-template-columns:50px 1fr;
  grid-template-rows:1fr 1fr;
  align-items:center;
  padding:15px;
}
.v97-mini-grid i{
  grid-row:1/3;
  font-style:normal;
  font-size:30px;
}
.v97-mini-grid b{
  font-size:33px;
  justify-self:start;
}
.v97-mini-grid span{
  color:var(--muted);
  letter-spacing:3px;
  font-weight:800;
  justify-self:start;
}

.v97-route-progress{
  margin-top:25px;
}
.v97-route-progress > div:first-child{
  display:flex;
  justify-content:space-between;
  color:var(--muted);
  letter-spacing:3px;
  font-family:monospace;
  margin-bottom:8px;
}
.v97-route-progress b{font-weight:400}
.v97-progress-track{
  height:8px;
  border-radius:99px;
  background:#242a36;
  overflow:hidden;
}
.v97-progress-track i{
  display:block;
  height:100%;
  background:linear-gradient(90deg,#5b0e16,var(--red));
  border-radius:99px;
  box-shadow:0 0 12px rgba(255,48,79,.55);
}

.v97-timeline-section{
  margin-top:34px;
}
.v97-section-title{
  color:var(--muted);
  letter-spacing:8px;
  font-weight:900;
  display:flex;
  align-items:center;
  gap:16px;
  margin-bottom:22px;
}
.v97-section-title:after{
  content:"";
  height:1px;
  background:var(--line);
  flex:1;
}

.v97-timeline{
  display:flex;
  flex-direction:column;
}
.v97-tl-item{
  display:grid;
  grid-template-columns:40px 1fr;
  gap:15px;
}
.v97-spine{
  display:flex;
  flex-direction:column;
  align-items:center;
}
.v97-node{
  width:24px;height:24px;
  border-radius:50%;
  border:4px solid #293142;
  background:#0b0d10;
  margin-top:16px;
  box-shadow:0 0 0 transparent;
}
.v97-node.passed{
  background:var(--green);
  border-color:var(--green);
}
.v97-node.live{
  background:var(--red);
  border-color:var(--red);
  box-shadow:0 0 18px var(--red);
}
.v97-node.next{
  border-color:var(--amber);
}
.v97-line{
  width:2px;
  flex:1;
  min-height:70px;
  background:#293142;
}
.v97-line.passed{background:rgba(34,201,130,.55)}
.v97-line.live{background:linear-gradient(var(--red),#293142)}

.v97-stop-card{
  margin-bottom:14px;
  padding:20px 24px;
  border:1px solid var(--line);
  border-radius:22px;
  background:var(--panel);
}
.v97-stop-card.live{
  border-color:rgba(255,48,79,.38);
  background:#12100f;
}
.v97-stop-card.next{
  border-color:rgba(240,162,41,.42);
}
.v97-stop-head{
  display:flex;
  align-items:center;
  justify-content:space-between;
}
.v97-stop-head h3{
  font-size:29px;
  color:white;
}
.v97-pill{
  padding:8px 15px;
  border-radius:99px;
  font-size:13px;
  font-weight:900;
  letter-spacing:4px;
}
.v97-pill.passed{color:var(--green);border:1px solid rgba(34,201,130,.35);background:rgba(34,201,130,.12)}
.v97-pill.live{color:#ff687d;border:1px solid rgba(255,48,79,.38);background:rgba(255,48,79,.15)}
.v97-pill.next{color:var(--amber);border:1px solid rgba(240,162,41,.42);background:rgba(240,162,41,.12)}
.v97-pill.upcoming{color:var(--muted);background:#1a1f2a}

.v97-stop-metrics{
  display:grid;
  grid-template-columns:repeat(4,1fr);
  margin-top:18px;
  gap:12px;
}
.v97-stop-metrics b{
  font-size:26px;
}
.v97-stop-metrics span{
  display:block;
  color:var(--muted);
  letter-spacing:3px;
  font-size:12px;
  font-weight:800;
}

.v97-dock{
  position:fixed;
  left:0;right:0;bottom:0;
  min-height:82px;
  background:#11151c;
  border-top:1px solid var(--line);
  display:grid;
  grid-template-columns:repeat(5,1fr);
  z-index:100;
}
.v97-dock button{
  border:0;
  background:transparent;
  color:var(--muted);
  display:flex;
  flex-direction:column;
  align-items:center;
  justify-content:center;
  gap:5px;
  font-size:25px;
}
.v97-dock button span{
  font-size:12px;
  letter-spacing:3px;
}
.v97-dock button.active{
  color:var(--red);
}

.v97-demo{
  position:fixed;
  top:135px;
  right:12px;
  display:flex;
  flex-direction:column;
  gap:7px;
  z-index:120;
}
.v97-demo small{
  color:var(--muted);
  letter-spacing:3px;
  text-align:center;
}
.v97-demo button{
  min-width:92px;
  padding:10px 12px;
  border-radius:11px;
  background:#171c25;
  border:1px solid #2a3242;
  color:#b9c1d0;
  font-weight:800;
}

@media(max-width:420px){
  .v97-info h1{font-size:35px}
  .v97-ring-wrap,.v97-ring{width:112px;height:112px}
  .v97-prox-top{gap:16px}
  .v97-demo{right:8px}
}
'''

js = r'''const STOPS = [
  { name:"Denizli", status:"passed", eta:"08:00", km:0, off:0, bag:0 },
  { name:"Çardak", status:"passed", eta:"08:52", km:0, off:1, bag:1 },
  { name:"Dinar", status:"passed", eta:"09:30", km:0, off:2, bag:0 },
  { name:"Afyon", status:"passed", eta:"10:15", km:0, off:4, bag:3 },
  { name:"Uşak", status:"live", eta:"14:45", km:38, off:3, bag:2 },
  { name:"Kütahya", status:"next", eta:"15:40", km:86, off:5, bag:1 },
  { name:"Bursa", status:"upcoming", eta:"17:20", km:182, off:8, bag:4 },
  { name:"İstanbul", status:"upcoming", eta:"19:00", km:290, off:17, bag:6 }
];

const CIRC = 301.59;
let startKm = 48;
let currentKm = 38;
let autoTimer = null;

function tick(){
  const d = new Date();
  document.getElementById("clockEl").textContent =
    String(d.getHours()).padStart(2,"0") + ":" +
    String(d.getMinutes()).padStart(2,"0");
}
tick();
setInterval(tick, 10000);

function setRing(km){
  currentKm = Math.max(0, Number(km) || 0);

  const ratio = Math.max(0, Math.min(1, 1 - currentKm / Math.max(startKm, 1)));
  const offset = CIRC * (1 - ratio);

  const ring = document.getElementById("ringFill");
  const txt = document.getElementById("ringKm");

  ring.style.strokeDashoffset = String(offset);
  txt.textContent = currentKm <= 0 ? "0" : String(currentKm);

  let color = "#3a8bff";
  if(currentKm <= 0){
    color = "#22c982";
  }else if(currentKm <= 5){
    color = "#ff304f";
  }else if(currentKm <= 15){
    color = "#f0a229";
  }

  ring.style.stroke = color;
  ring.style.filter = "drop-shadow(0 0 12px " + color + ")";
  txt.style.color = color;
  txt.style.textShadow = "0 0 18px " + color;

  const pct = Math.round(ratio * 100);
  document.getElementById("routePct").textContent = "%" + Math.max(61, pct) + " tamamlandı";
  document.getElementById("routeBar").style.width = Math.max(61, pct) + "%";
}

function buildTimeline(){
  const box = document.getElementById("timeline");
  box.innerHTML = "";

  STOPS.forEach((s, i) => {
    const isLast = i === STOPS.length - 1;
    const statusText =
      s.status === "passed" ? "✓ GEÇİLDİ" :
      s.status === "live" ? "● CANLI" :
      s.status === "next" ? "→ SONRAKİ" :
      s.eta;

    const item = document.createElement("div");
    item.className = "v97-tl-item";
    item.innerHTML = `
      <div class="v97-spine">
        <div class="v97-node ${s.status}"></div>
        ${isLast ? "" : `<div class="v97-line ${s.status}"></div>`}
      </div>
      <article class="v97-stop-card ${s.status === "live" ? "live" : s.status === "next" ? "next" : ""}">
        <div class="v97-stop-head">
          <h3>${s.name}</h3>
          <div class="v97-pill ${s.status}">${statusText}</div>
        </div>
        <div class="v97-stop-metrics">
          <div><b>${s.eta}</b><span>VARIŞ</span></div>
          <div><b>${s.km > 0 ? s.km + " km" : "—"}</b><span>MESAFE</span></div>
          <div><b>${s.off}</b><span>İNECEK</span></div>
          <div><b>${s.bag}</b><span>BAGAJ</span></div>
        </div>
      </article>
    `;
    box.appendChild(item);
  });
}

function simKm(km){
  setRing(km);
}

function simAuto(){
  if(autoTimer){
    clearInterval(autoTimer);
    autoTimer = null;
    return;
  }

  let km = startKm;
  autoTimer = setInterval(() => {
    km = Math.max(0, km - 1);
    simKm(km);
    if(km <= 0){
      clearInterval(autoTimer);
      autoTimer = null;
    }
  }, 260);
}

function flickerSpeed(){
  const el = document.getElementById("speedVal");
  setInterval(() => {
    el.textContent = String(86 + Math.round((Math.random() - .5) * 8));
  }, 1800);
}

buildTimeline();
setRing(currentKm);
flickerSpeed();
'''

HTML.write_text(html, encoding="utf-8")
CSS.write_text(css, encoding="utf-8")
JS.write_text(js, encoding="utf-8")

print("✅ Oluşturuldu:", HTML.relative_to(ROOT))
print("✅ Oluşturuldu:", CSS.relative_to(ROOT))
print("✅ Oluşturuldu:", JS.relative_to(ROOT))

print()
print("Önizleme adresi:")
print("http://127.0.0.1:5000/static/continue/v97_proximity_preview.html")
