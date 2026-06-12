const STOPS = [
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
  if(currentKm <= 5){
    color = "#e03030";
  }else if(currentKm <= 15){
    color = "#e08820";
  }

  ring.style.stroke = color;
  ring.style.filter = "drop-shadow(0 0 8px " + color + ")";
  txt.style.color = color;
  txt.style.textShadow = "0 0 14px " + color;

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
