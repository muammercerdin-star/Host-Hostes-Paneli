from pathlib import Path
from datetime import datetime
import shutil
import re

ROOT = Path(".").resolve()
STAMP = datetime.now().strftime("%Y%m%d-%H%M%S")

WEB_CSS = ROOT / "static/continue/continue_trip_v99_clean.css"
WEB_JS  = ROOT / "static/continue/continue_trip_v99_clean.js"

AND_CSS = ROOT / "android_app/app/src/main/python/static/continue/continue_trip_v99_clean.css"
AND_JS  = ROOT / "android_app/app/src/main/python/static/continue/continue_trip_v99_clean.js"

print("===== V99M DOLULUK PANELI =====")

for p in [WEB_CSS, WEB_JS, AND_CSS, AND_JS]:
    if p.exists():
        bak = p.with_name(p.name + f".bak-v99m-{STAMP}")
        shutil.copy2(p, bak)
        print("📦 backup:", bak)

if not WEB_CSS.exists():
    raise SystemExit("❌ CSS yok: " + str(WEB_CSS))

if not WEB_JS.exists():
    raise SystemExit("❌ JS yok: " + str(WEB_JS))

css = WEB_CSS.read_text(encoding="utf-8", errors="ignore")
css = re.sub(
    r"/\* V99M_OCCUPANCY_PANEL_START \*/.*?/\* V99M_OCCUPANCY_PANEL_END \*/",
    "",
    css,
    flags=re.S
)

css += r'''

/* V99M_OCCUPANCY_PANEL_START */

.v99m-occ-clickable{
  cursor:pointer !important;
  position:relative !important;
}

.v99m-occ-clickable::after{
  content:"";
  position:absolute;
  inset:7px;
  border-radius:18px;
  border:1px solid rgba(58,139,255,.0);
  pointer-events:none;
  transition:.2s ease;
}

.v99m-occ-clickable:active::after{
  border-color:rgba(58,139,255,.45);
  box-shadow:0 0 18px rgba(58,139,255,.22);
}

.v99m-occ-overlay{
  position:fixed;
  inset:0;
  background:rgba(0,0,0,.62);
  backdrop-filter:blur(8px);
  -webkit-backdrop-filter:blur(8px);
  z-index:99980;
  opacity:0;
  pointer-events:none;
  transition:.22s ease;
}

.v99m-occ-overlay.open{
  opacity:1;
  pointer-events:auto;
}

.v99m-occ-sheet{
  position:fixed;
  left:0;
  right:0;
  bottom:0;
  z-index:99990;
  max-height:78vh;
  overflow:auto;
  background:
    radial-gradient(circle at 25% 0%, rgba(58,139,255,.14), transparent 36%),
    radial-gradient(circle at 80% 12%, rgba(255,43,92,.13), transparent 32%),
    linear-gradient(180deg, #141923 0%, #0b0f16 100%);
  border-top:1px solid rgba(160,174,210,.18);
  border-radius:28px 28px 0 0;
  box-shadow:0 -24px 70px rgba(0,0,0,.7);
  transform:translateY(105%);
  transition:.26s cubic-bezier(.2,.85,.2,1);
  padding:10px 18px 118px;
  color:#eef3ff;
  font-family:inherit;
}

.v99m-occ-sheet.open{
  transform:translateY(0);
}

.v99m-handle{
  width:54px;
  height:5px;
  border-radius:999px;
  background:rgba(210,220,245,.25);
  margin:4px auto 14px;
}

.v99m-head{
  display:flex;
  align-items:center;
  justify-content:space-between;
  gap:14px;
  margin-bottom:14px;
}

.v99m-kicker{
  font-size:11px;
  letter-spacing:3px;
  color:#7f8ca5;
  font-weight:900;
}

.v99m-title{
  margin:4px 0 0;
  font-size:25px;
  line-height:1.05;
  letter-spacing:.5px;
  font-weight:900;
}

.v99m-close{
  width:44px;
  height:44px;
  border-radius:16px;
  border:1px solid rgba(255,255,255,.1);
  background:rgba(255,255,255,.06);
  color:#fff;
  font-size:26px;
  font-weight:900;
}

.v99m-refresh{
  border:0;
  border-radius:14px;
  padding:10px 14px;
  background:linear-gradient(180deg, #26344d, #151d2b);
  color:#dfe8ff;
  font-weight:900;
  letter-spacing:1px;
}

.v99m-summary-grid{
  display:grid;
  grid-template-columns:repeat(3, minmax(0,1fr));
  gap:10px;
  margin-bottom:14px;
}

.v99m-stat{
  min-height:72px;
  border-radius:18px;
  border:1px solid rgba(255,255,255,.09);
  background:rgba(255,255,255,.045);
  padding:12px 10px;
  box-shadow:inset 0 0 0 1px rgba(255,255,255,.02);
}

.v99m-stat .v{
  font-size:25px;
  line-height:1;
  font-weight:1000;
  color:#fff;
}

.v99m-stat .l{
  margin-top:7px;
  font-size:10px;
  letter-spacing:2px;
  color:#7d879d;
  font-weight:900;
}

.v99m-stat.good .v{ color:#20d07b; }
.v99m-stat.warn .v{ color:#f4b13c; }
.v99m-stat.danger .v{ color:#ff2b5c; }
.v99m-stat.blue .v{ color:#3a8bff; }
.v99m-stat.pink .v{ color:#ff5db1; }

.v99m-section-title{
  display:flex;
  align-items:center;
  justify-content:space-between;
  gap:10px;
  margin:15px 0 10px;
  color:#7f8ca5;
  font-size:12px;
  letter-spacing:3px;
  font-weight:1000;
}

.v99m-map{
  display:grid;
  gap:8px;
  padding:14px;
  border-radius:22px;
  border:1px solid rgba(255,255,255,.09);
  background:rgba(4,8,14,.46);
  overflow-x:auto;
}

.v99m-seat{
  width:42px;
  height:42px;
  border-radius:13px;
  border:1px solid rgba(255,255,255,.12);
  display:flex;
  align-items:center;
  justify-content:center;
  font-size:16px;
  font-weight:1000;
  color:#071018;
  box-shadow:0 8px 20px rgba(0,0,0,.25);
  user-select:none;
}

.v99m-seat.free{
  background:linear-gradient(180deg, #22d86f, #11964c);
  color:#06220f;
}

.v99m-seat.occ{
  background:linear-gradient(180deg, #ff315e, #a9142d);
  color:#fff;
}

.v99m-seat.off{
  background:linear-gradient(180deg, #ffd75a, #d88900);
  color:#1b1000;
  box-shadow:0 0 22px rgba(255,189,35,.45);
}

.v99m-seat.male{
  border-color:rgba(58,139,255,.75);
}

.v99m-seat.female{
  border-color:rgba(255,93,177,.75);
}

.v99m-seat.spacer{
  opacity:0;
  pointer-events:none;
}

.v99m-legend{
  display:flex;
  flex-wrap:wrap;
  gap:8px;
  margin:12px 0 4px;
}

.v99m-legend span{
  display:inline-flex;
  align-items:center;
  gap:7px;
  padding:8px 10px;
  border-radius:999px;
  background:rgba(255,255,255,.06);
  border:1px solid rgba(255,255,255,.08);
  color:#cbd5ea;
  font-size:12px;
  font-weight:800;
}

.v99m-dot{
  width:10px;
  height:10px;
  border-radius:50%;
  display:inline-block;
}

.v99m-dot.free{ background:#20d07b; }
.v99m-dot.occ{ background:#ff2b5c; }
.v99m-dot.off{ background:#f3b233; }

.v99m-impact{
  border-radius:20px;
  border:1px solid rgba(244,177,60,.18);
  background:linear-gradient(180deg, rgba(244,177,60,.09), rgba(255,255,255,.035));
  padding:13px 14px;
  color:#ecf2ff;
  font-weight:800;
  line-height:1.45;
}

.v99m-detail{
  margin-top:12px;
  min-height:46px;
  border-radius:18px;
  border:1px solid rgba(58,139,255,.18);
  background:rgba(58,139,255,.07);
  padding:12px 14px;
  color:#dce7ff;
  font-weight:850;
  line-height:1.4;
}

.v99m-muted{
  color:#7f8ca5;
}

@media (max-width:380px){
  .v99m-occ-sheet{
    padding-left:14px;
    padding-right:14px;
  }

  .v99m-summary-grid{
    gap:8px;
  }

  .v99m-stat .v{
    font-size:22px;
  }

  .v99m-seat{
    width:38px;
    height:38px;
    border-radius:12px;
    font-size:15px;
  }
}

/* V99M_OCCUPANCY_PANEL_END */
'''

WEB_CSS.write_text(css, encoding="utf-8")
print("✅ CSS yazıldı:", WEB_CSS)

js = WEB_JS.read_text(encoding="utf-8", errors="ignore")
js = re.sub(
    r"\n?/\* V99M_OCCUPANCY_PANEL_START \*/.*?/\* V99M_OCCUPANCY_PANEL_END \*/\n?",
    "\n",
    js,
    flags=re.S
)

js += r'''

/* V99M_OCCUPANCY_PANEL_START */
(function(){
  "use strict";

  function q(sel, root){
    return (root || document).querySelector(sel);
  }

  function qa(sel, root){
    return Array.prototype.slice.call((root || document).querySelectorAll(sel));
  }

  function text(el){
    return el ? String(el.textContent || "").trim() : "";
  }

  function norm(s){
    return String(s || "")
      .toLocaleLowerCase("tr-TR")
      .replace(/ı/g, "i")
      .replace(/ğ/g, "g")
      .replace(/ü/g, "u")
      .replace(/ş/g, "s")
      .replace(/ö/g, "o")
      .replace(/ç/g, "c")
      .replace(/\s+/g, " ")
      .trim();
  }

  function sameStop(a,b){
    var aa = norm(a);
    var bb = norm(b);
    if(!aa || !bb) return false;
    return aa === bb || aa.indexOf(bb) >= 0 || bb.indexOf(aa) >= 0;
  }

  function liveStopName(){
    return text(q("#liveCurrentStopName")) || "";
  }

  function nextStopName(){
    var el = q(".v99-tl-card.next-card .v99-tl-stop-name");
    if(el) return text(el);

    var cards = qa(".v99-tl-card");
    for(var i=0; i<cards.length; i++){
      var pill = text(q(".v99-pill", cards[i]));
      if(/sonraki|sonraki|sonra/i.test(pill)){
        return text(q(".v99-tl-stop-name", cards[i]));
      }
    }
    return "";
  }

  function ensurePanel(){
    if(q("#v99mOccSheet")) return;

    var overlay = document.createElement("div");
    overlay.id = "v99mOccOverlay";
    overlay.className = "v99m-occ-overlay";

    var sheet = document.createElement("section");
    sheet.id = "v99mOccSheet";
    sheet.className = "v99m-occ-sheet";
    sheet.innerHTML = `
      <div class="v99m-handle"></div>

      <div class="v99m-head">
        <div>
          <div class="v99m-kicker">DOLULUK PANELİ</div>
          <h3 class="v99m-title">Koltuk Haritası</h3>
        </div>
        <div style="display:flex; gap:8px; align-items:center;">
          <button class="v99m-refresh" id="v99mOccRefresh" type="button">YENİLE</button>
          <button class="v99m-close" id="v99mOccClose" type="button">×</button>
        </div>
      </div>

      <div class="v99m-summary-grid" id="v99mOccSummary">
        <div class="v99m-stat"><div class="v">—</div><div class="l">DOLULUK</div></div>
        <div class="v99m-stat"><div class="v">—</div><div class="l">BOŞ</div></div>
        <div class="v99m-stat"><div class="v">—</div><div class="l">İNECEK</div></div>
      </div>

      <div class="v99m-impact" id="v99mOccImpact">Veri hazırlanıyor…</div>

      <div class="v99m-section-title">
        <span>GÖRSEL KOLTUK PLANI</span>
        <span id="v99mOccLiveStop">—</span>
      </div>

      <div class="v99m-map" id="v99mSeatMap"></div>

      <div class="v99m-legend">
        <span><i class="v99m-dot free"></i> Boş</span>
        <span><i class="v99m-dot occ"></i> Dolu</span>
        <span><i class="v99m-dot off"></i> Bu durakta inecek</span>
      </div>

      <div class="v99m-detail" id="v99mSeatDetail">
        Koltuğa basınca detay burada görünür.
      </div>
    `;

    document.body.appendChild(overlay);
    document.body.appendChild(sheet);

    overlay.addEventListener("click", closePanel);
    q("#v99mOccClose").addEventListener("click", closePanel);
    q("#v99mOccRefresh").addEventListener("click", loadPanel);
  }

  function openPanel(){
    ensurePanel();
    q("#v99mOccOverlay").classList.add("open");
    q("#v99mOccSheet").classList.add("open");
    loadPanel();
  }

  function closePanel(){
    var overlay = q("#v99mOccOverlay");
    var sheet = q("#v99mOccSheet");
    if(overlay) overlay.classList.remove("open");
    if(sheet) sheet.classList.remove("open");
  }

  function isDolulukTarget(el){
    if(!el || el === document.body || el === document.documentElement) return false;

    var t = text(el).toLocaleUpperCase("tr-TR");
    if(t.indexOf("DOLULUK") < 0) return false;
    if(!/\d+\s*\/\s*\d+/.test(t)) return false;

    var r = el.getBoundingClientRect();
    if(!r || r.width < 70 || r.height < 35) return false;
    if(r.height > 220) return false;

    return true;
  }

  function markDolulukCards(){
    qa("body *").forEach(function(el){
      if(isDolulukTarget(el)){
        el.classList.add("v99m-occ-clickable");
      }
    });
  }

  document.addEventListener("click", function(ev){
    var el = ev.target;
    while(el && el !== document.body){
      if(isDolulukTarget(el)){
        ev.preventDefault();
        openPanel();
        return;
      }
      el = el.parentElement;
    }
  }, true);

  function num(v){
    var n = Number(v);
    return Number.isFinite(n) ? n : 0;
  }

  function seatGenderClass(s){
    var g = norm(s.gender || "");
    if(g.indexOf("bayan") >= 0 || g.indexOf("kadin") >= 0) return "female";
    if(g.indexOf("bay") >= 0 || g.indexOf("erkek") >= 0) return "male";
    return "";
  }

  function renderSummary(data, seats){
    var total = Number(data.total_seats || 40);
    var occupied = seats.filter(function(s){ return !!s.occupied; }).length;
    var free = Math.max(0, total - occupied);

    var male = seats.filter(function(s){ return !!s.occupied && seatGenderClass(s) === "male"; }).length;
    var female = seats.filter(function(s){ return !!s.occupied && seatGenderClass(s) === "female"; }).length;

    var live = liveStopName();
    var next = nextStopName();

    var offLive = seats.filter(function(s){
      return !!s.occupied && sameStop(s.to_stop, live);
    }).length;

    var offNext = seats.filter(function(s){
      return !!s.occupied && sameStop(s.to_stop, next);
    }).length;

    var bag = seats.reduce(function(a,s){
      return a + num(s.bag_count || s.bag_total || s.bagaj_count);
    }, 0);

    var summary = q("#v99mOccSummary");
    if(summary){
      summary.innerHTML = `
        <div class="v99m-stat ${free <= 2 ? "danger" : (free <= 5 ? "warn" : "")}">
          <div class="v">${occupied} / ${total}</div>
          <div class="l">DOLULUK</div>
        </div>
        <div class="v99m-stat good">
          <div class="v">${free}</div>
          <div class="l">BOŞ KOLTUK</div>
        </div>
        <div class="v99m-stat warn">
          <div class="v">${offLive}</div>
          <div class="l">BU DURAKTA İNECEK</div>
        </div>
        <div class="v99m-stat blue">
          <div class="v">${male}</div>
          <div class="l">BAY</div>
        </div>
        <div class="v99m-stat pink">
          <div class="v">${female}</div>
          <div class="l">BAYAN</div>
        </div>
        <div class="v99m-stat">
          <div class="v">${bag}</div>
          <div class="l">BAGAJ</div>
        </div>
      `;
    }

    var afterLive = Math.max(0, occupied - offLive);
    var afterNext = Math.max(0, afterLive - offNext);

    var impact = q("#v99mOccImpact");
    if(impact){
      impact.innerHTML = `
        <b>${live || "Canlı durak"}</b> durağında <b>${offLive}</b> kişi inecek → sonra <b>${afterLive}/${total}</b> kalır.<br>
        ${next ? `<b>${next}</b> durağında <b>${offNext}</b> kişi inecek → sonra <b>${afterNext}/${total}</b> kalır.` : `<span class="v99m-muted">Sıradaki durak bulunamadı.</span>`}
      `;
    }

    var liveTag = q("#v99mOccLiveStop");
    if(liveTag) liveTag.textContent = live ? ("Canlı: " + live) : "Canlı: —";
  }

  function renderSeatMap(data, seats){
    var map = q("#v99mSeatMap");
    if(!map) return;

    var positions = data.seat_positions || {};
    var byNo = {};
    seats.forEach(function(s){
      byNo[String(s.seat_no)] = s;
    });

    var maxRow = 0;
    var maxCol = 0;
    var byPos = {};

    Object.keys(positions).forEach(function(no){
      var pos = positions[no] || [];
      var r = Number(pos[0] || 0);
      var c = Number(pos[1] || 0);
      if(r > maxRow) maxRow = r;
      if(c > maxCol) maxCol = c;
      byPos[r + ":" + c] = String(no);
    });

    if(!maxRow || !maxCol){
      maxRow = Math.ceil(Number(data.total_seats || 40) / 4);
      maxCol = 4;
      for(var i=1; i<=Number(data.total_seats || 40); i++){
        var rr = Math.ceil(i / 4);
        var cc = ((i - 1) % 4) + 1;
        byPos[rr + ":" + cc] = String(i);
      }
    }

    map.style.gridTemplateColumns = "repeat(" + maxCol + ", 42px)";
    map.innerHTML = "";

    var live = liveStopName();

    for(var row=1; row<=maxRow; row++){
      for(var col=1; col<=maxCol; col++){
        var no = byPos[row + ":" + col];

        if(!no){
          var sp = document.createElement("div");
          sp.className = "v99m-seat spacer";
          map.appendChild(sp);
          continue;
        }

        var s = byNo[no] || { seat_no:no, occupied:false };
        var cell = document.createElement("button");
        cell.type = "button";
        cell.className = "v99m-seat";

        if(s.occupied){
          cell.classList.add("occ");
          var g = seatGenderClass(s);
          if(g) cell.classList.add(g);

          if(sameStop(s.to_stop, live)){
            cell.classList.add("off");
          }
        }else{
          cell.classList.add("free");
        }

        cell.textContent = no;
        cell.addEventListener("click", function(seat){
          return function(){
            showSeatDetail(seat);
          };
        }(s));

        map.appendChild(cell);
      }
    }
  }

  function showSeatDetail(s){
    var box = q("#v99mSeatDetail");
    if(!box) return;

    if(!s || !s.occupied){
      box.innerHTML = `<b>Koltuk ${s && s.seat_no ? s.seat_no : "—"}</b> boş görünüyor.`;
      return;
    }

    var g = s.gender ? String(s.gender) : "—";
    var from = s.from_stop || "—";
    var to = s.to_stop || "—";
    var bag = num(s.bag_count || s.bag_total || s.bagaj_count);

    box.innerHTML = `
      <b>Koltuk ${s.seat_no}</b> · ${g}<br>
      ${from} → ${to}<br>
      Bagaj: <b>${bag}</b>
    `;
  }

  async function loadPanel(){
    ensurePanel();

    var impact = q("#v99mOccImpact");
    var map = q("#v99mSeatMap");

    if(impact) impact.textContent = "Koltuk verisi alınıyor…";
    if(map) map.innerHTML = "";

    try{
      var res = await fetch("/api/live-seat-map?_=" + Date.now(), {
        cache:"no-store",
        headers:{ "Accept":"application/json" }
      });

      var data = await res.json();
      if(!data || data.ok === false){
        throw new Error((data && data.msg) || "API veri döndürmedi");
      }

      var seats = Array.isArray(data.seats) ? data.seats : [];
      renderSummary(data, seats);
      renderSeatMap(data, seats);

    }catch(err){
      if(impact){
        impact.innerHTML = `<b>Doluluk verisi alınamadı.</b><br><span class="v99m-muted">${String(err && err.message || err)}</span>`;
      }
    }
  }

  markDolulukCards();
  setInterval(markDolulukCards, 1500);

  window.MuavinV99OccupancyPanel = {
    open: openPanel,
    close: closePanel,
    reload: loadPanel
  };
})();
/* V99M_OCCUPANCY_PANEL_END */
'''

WEB_JS.write_text(js, encoding="utf-8")
print("✅ JS yazıldı:", WEB_JS)

if AND_CSS.parent.exists():
    AND_CSS.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(WEB_CSS, AND_CSS)
    print("✅ Android CSS senkron:", AND_CSS)

if AND_JS.parent.exists():
    AND_JS.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(WEB_JS, AND_JS)
    print("✅ Android JS senkron:", AND_JS)

print()
print("===== KONTROL =====")
for p in [WEB_CSS, WEB_JS, AND_CSS, AND_JS]:
    if p.exists():
        txt = p.read_text(encoding="utf-8", errors="ignore")
        print(p.name, "V99M:", "VAR" if "V99M_OCCUPANCY_PANEL" in txt else "YOK")

print()
print("✅ V99M tamam. /continue-trip?v=v99m ile yenile, DOLULUK kartına bas.")
