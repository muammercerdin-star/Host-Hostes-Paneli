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

print("===== V99O KOLTUK DETAY POPUP + BAGAJ ROZETİ =====")

for p in [WEB_JS, WEB_CSS]:
    if not p.exists():
        raise SystemExit("❌ Dosya yok: " + str(p))

for p in [WEB_JS, WEB_CSS, AND_JS, AND_CSS]:
    if p.exists():
        bak = p.with_name(p.name + f".bak-v99o-seat-popup-{STAMP}")
        shutil.copy2(p, bak)
        print("📦 backup:", bak)

css = WEB_CSS.read_text(encoding="utf-8", errors="ignore")
js = WEB_JS.read_text(encoding="utf-8", errors="ignore")

css = re.sub(
    r"\n?/\* V99O_SEAT_DETAIL_POPUP_CSS_START \*/.*?/\* V99O_SEAT_DETAIL_POPUP_CSS_END \*/\n?",
    "\n",
    css,
    flags=re.S
)

js = re.sub(
    r"\n?/\* V99O_SEAT_DETAIL_POPUP_JS_START \*/.*?/\* V99O_SEAT_DETAIL_POPUP_JS_END \*/\n?",
    "\n",
    js,
    flags=re.S
)

css_block = r'''

/* V99O_SEAT_DETAIL_POPUP_CSS_START */
.v99n-seat-occupied{
  box-shadow:0 0 14px rgba(255,43,91,.45), inset 0 0 18px rgba(255,43,91,.18) !important;
}

.v99n-seat-empty{
  box-shadow:0 0 10px rgba(31,213,108,.28), inset 0 0 14px rgba(31,213,108,.12) !important;
}

.v99n-seat-live-off{
  background:linear-gradient(180deg,#ffbf2e,#d88900) !important;
  color:#111 !important;
  box-shadow:0 0 18px rgba(255,191,46,.65), inset 0 0 18px rgba(255,255,255,.22) !important;
}

.v99n-seat-next-off{
  outline:2px solid rgba(255,191,46,.75) !important;
  box-shadow:0 0 18px rgba(255,191,46,.42), inset 0 0 16px rgba(255,191,46,.12) !important;
}

.v99n-seat-reserved{
  background:linear-gradient(180deg,#ff9d2f,#d96c00) !important;
  color:#10131a !important;
  box-shadow:0 0 18px rgba(255,157,47,.55), inset 0 0 18px rgba(255,255,255,.18) !important;
}

.v99n-seat-clickable{
  cursor:pointer;
  position:relative !important;
}

.v99n-seat-bag-dot{
  position:absolute;
  right:-7px;
  top:-7px;
  min-width:22px;
  height:22px;
  padding:0 5px;
  border-radius:999px;
  display:flex;
  align-items:center;
  justify-content:center;
  font-size:12px;
  font-weight:900;
  color:#fff;
  background:linear-gradient(180deg,#1e90ff,#0757cc);
  border:1px solid rgba(255,255,255,.45);
  box-shadow:0 0 12px rgba(30,144,255,.75);
  z-index:4;
}

.v99n-seat-detail-mask{
  position:fixed;
  inset:0;
  z-index:99999;
  background:rgba(0,0,0,.62);
  backdrop-filter:blur(7px);
  display:none;
  align-items:flex-end;
  justify-content:center;
}

.v99n-seat-detail-mask.show{
  display:flex;
}

.v99n-seat-detail-card{
  width:min(680px,100%);
  max-height:82vh;
  overflow:auto;
  border-radius:34px 34px 0 0;
  background:
    radial-gradient(circle at 20% 0%, rgba(255,43,91,.20), transparent 34%),
    radial-gradient(circle at 90% 20%, rgba(47,133,255,.18), transparent 38%),
    linear-gradient(180deg,#171b26,#0c1018);
  border:1px solid rgba(255,255,255,.12);
  box-shadow:0 -20px 70px rgba(0,0,0,.55);
  padding:22px;
  color:#f3f6ff;
  font-family:Rajdhani, system-ui, sans-serif;
}

.v99n-seat-detail-head{
  display:flex;
  justify-content:space-between;
  gap:14px;
  align-items:flex-start;
  margin-bottom:18px;
}

.v99n-seat-detail-kicker{
  letter-spacing:.28em;
  color:#8c94aa;
  font-weight:800;
  font-size:13px;
}

.v99n-seat-detail-title{
  font-size:38px;
  font-weight:900;
  line-height:.95;
  margin-top:5px;
}

.v99n-seat-detail-close{
  width:54px;
  height:54px;
  border-radius:18px;
  border:1px solid rgba(255,255,255,.14);
  background:rgba(255,255,255,.08);
  color:#fff;
  font-size:26px;
  font-weight:900;
}

.v99n-seat-status-pill{
  display:inline-flex;
  align-items:center;
  gap:8px;
  padding:9px 13px;
  border-radius:999px;
  font-weight:900;
  letter-spacing:.14em;
  margin-top:10px;
  font-size:14px;
  border:1px solid rgba(255,255,255,.12);
}

.v99n-seat-status-pill.empty{
  color:#38e587;
  background:rgba(31,213,108,.12);
  border-color:rgba(31,213,108,.35);
}

.v99n-seat-status-pill.occupied{
  color:#ff4773;
  background:rgba(255,43,91,.12);
  border-color:rgba(255,43,91,.35);
}

.v99n-seat-status-pill.reserved{
  color:#ffbd4a;
  background:rgba(255,157,47,.13);
  border-color:rgba(255,157,47,.38);
}

.v99n-seat-detail-grid{
  display:grid;
  grid-template-columns:1fr 1fr;
  gap:12px;
}

.v99n-seat-info-box{
  border-radius:20px;
  background:rgba(255,255,255,.055);
  border:1px solid rgba(255,255,255,.08);
  padding:15px;
  min-height:74px;
}

.v99n-seat-info-label{
  color:#838ca3;
  letter-spacing:.18em;
  font-size:12px;
  font-weight:800;
  margin-bottom:6px;
}

.v99n-seat-info-value{
  font-size:23px;
  font-weight:900;
  line-height:1.05;
  word-break:break-word;
}

.v99n-seat-detail-note{
  margin-top:14px;
  border-radius:20px;
  padding:14px 16px;
  background:rgba(255,191,46,.08);
  border:1px solid rgba(255,191,46,.20);
  color:#dfe6f6;
  font-size:18px;
  font-weight:700;
  line-height:1.35;
}

.v99n-seat-detail-actions{
  display:grid;
  grid-template-columns:1fr 1fr;
  gap:12px;
  margin-top:16px;
}

.v99n-seat-action{
  border:0;
  border-radius:20px;
  padding:16px;
  font-weight:900;
  letter-spacing:.08em;
  font-size:16px;
  color:#fff;
  background:linear-gradient(180deg,#232b3b,#121722);
  border:1px solid rgba(255,255,255,.10);
}

.v99n-seat-action.primary{
  background:linear-gradient(180deg,#1f75ff,#1348b9);
}

@media(max-width:420px){
  .v99n-seat-detail-card{padding:18px;}
  .v99n-seat-detail-title{font-size:34px;}
  .v99n-seat-detail-grid{grid-template-columns:1fr 1fr;}
  .v99n-seat-info-value{font-size:21px;}
}
/* V99O_SEAT_DETAIL_POPUP_CSS_END */
'''

js_block = r'''

/* V99O_SEAT_DETAIL_POPUP_JS_START */
(function(){
  "use strict";

  var seatCache = [];
  var seatByNo = {};
  var lastFetch = 0;

  function q(sel, root){
    return (root || document).querySelector(sel);
  }

  function qa(sel, root){
    return Array.prototype.slice.call((root || document).querySelectorAll(sel));
  }

  function txt(v){
    return String(v == null ? "" : v).trim();
  }

  function norm(s){
    return txt(s)
      .toLocaleLowerCase("tr-TR")
      .replace(/\s+/g," ")
      .trim();
  }

  function sameStop(a,b){
    return !!a && !!b && norm(a) === norm(b);
  }

  function num(v){
    var n = Number(v || 0);
    return Number.isFinite(n) ? n : 0;
  }

  function liveStop(){
    return txt(q("#liveCurrentStopName") && q("#liveCurrentStopName").textContent);
  }

  function nextStop(){
    var el = q(".v99-tl-card.next-card .v99-tl-stop-name") ||
             q(".v99-tl-node.next .v99-tl-stop-name") ||
             q(".v99-pill.next");
    if(el && el.classList && el.classList.contains("v99-pill")){
      var card = el.closest(".v99-tl-card");
      var name = card && q(".v99-tl-stop-name", card);
      return txt(name && name.textContent);
    }
    return txt(el && el.textContent);
  }

  function ensureModal(){
    var existing = q("#v99nSeatDetailMask");
    if(existing) return existing;

    var div = document.createElement("div");
    div.id = "v99nSeatDetailMask";
    div.className = "v99n-seat-detail-mask";
    div.innerHTML = `
      <div class="v99n-seat-detail-card" role="dialog" aria-modal="true">
        <div class="v99n-seat-detail-head">
          <div>
            <div class="v99n-seat-detail-kicker">KOLTUK DETAYI</div>
            <div class="v99n-seat-detail-title" id="v99nSeatTitle">Koltuk</div>
            <div id="v99nSeatStatus" class="v99n-seat-status-pill empty">BOŞ</div>
          </div>
          <button class="v99n-seat-detail-close" id="v99nSeatClose" type="button">×</button>
        </div>

        <div class="v99n-seat-detail-grid" id="v99nSeatGrid"></div>

        <div class="v99n-seat-detail-note" id="v99nSeatNote"></div>

        <div class="v99n-seat-detail-actions">
          <button class="v99n-seat-action" id="v99nSeatClose2" type="button">KAPAT</button>
          <button class="v99n-seat-action primary" id="v99nSeatGoSeats" type="button">KOLTUK EKRANI</button>
        </div>
      </div>
    `;

    document.body.appendChild(div);

    q("#v99nSeatClose", div).addEventListener("click", closeModal);
    q("#v99nSeatClose2", div).addEventListener("click", closeModal);
    q("#v99nSeatGoSeats", div).addEventListener("click", function(){
      location.href = "/seats";
    });

    div.addEventListener("click", function(e){
      if(e.target === div) closeModal();
    });

    return div;
  }

  function closeModal(){
    var m = q("#v99nSeatDetailMask");
    if(m) m.classList.remove("show");
  }

  function info(label, value){
    return `
      <div class="v99n-seat-info-box">
        <div class="v99n-seat-info-label">${label}</div>
        <div class="v99n-seat-info-value">${value || "—"}</div>
      </div>
    `;
  }

  function statusOf(seat){
    if(!seat || !seat.occupied){
      if(seat && /rezerv|reserve|booking/i.test(txt(seat.ticket_type || seat.status || seat.seat_status))){
        return {cls:"reserved", text:"REZERVELİ"};
      }
      return {cls:"empty", text:"BOŞ"};
    }

    if(/rezerv|reserve|booking/i.test(txt(seat.ticket_type || seat.status || seat.seat_status))){
      return {cls:"reserved", text:"REZERVELİ"};
    }

    return {cls:"occupied", text:"DOLU"};
  }

  function showSeatDetail(seatNo){
    var seat = seatByNo[String(seatNo)] || {seat_no:String(seatNo), occupied:false};
    var m = ensureModal();

    var st = statusOf(seat);
    var title = q("#v99nSeatTitle", m);
    var status = q("#v99nSeatStatus", m);
    var grid = q("#v99nSeatGrid", m);
    var note = q("#v99nSeatNote", m);

    title.textContent = "Koltuk " + seatNo;
    status.className = "v99n-seat-status-pill " + st.cls;
    status.textContent = st.text;

    var passenger = txt(seat.passenger_name) || (seat.occupied ? "İsimsiz yolcu" : "Boş koltuk");
    var gender = txt(seat.gender);
    if(gender === "bay") gender = "Bay";
    else if(gender === "bayan") gender = "Bayan";
    else gender = "—";

    var bag = num(seat.bag_count || seat.bag_total || seat.bagaj_count);
    var amount = num(seat.amount);
    var amountText = amount > 0 ? (amount + " TL") : "—";

    grid.innerHTML =
      info("YOLCU", passenger) +
      info("CİNSİYET", gender) +
      info("BİNİŞ", txt(seat.from_stop) || "—") +
      info("İNİŞ", txt(seat.to_stop) || "—") +
      info("BİLET", txt(seat.ticket_type) || "—") +
      info("ÖDEME", txt(seat.payment) || "—") +
      info("ÜCRET", amountText) +
      info("BAGAJ", bag > 0 ? (bag + " adet") : "yok");

    if(seat.occupied){
      note.textContent = "Bu koltuk " + (txt(seat.from_stop) || "—") + " → " + (txt(seat.to_stop) || "—") + " yolcusu olarak kayıtlı.";
    }else{
      note.textContent = "Bu koltuk boş görünüyor. Manuel yolcu ekleme/dolu işaretleme işlemini bir sonraki pakette güvenli şekilde bağlayacağız.";
    }

    m.classList.add("show");
  }

  function extractSeatNo(el){
    if(!el) return "";
    var direct = el.getAttribute("data-seat-no") || el.getAttribute("data-seat") || el.dataset.seatNo || el.dataset.seat;
    if(direct) return txt(direct);

    var raw = txt(el.textContent);
    var m = raw.match(/\b([1-9][0-9]?)\b/);
    return m ? m[1] : "";
  }

  function candidateSeatEls(){
    var sels = [
      "[data-seat-no]",
      "[data-seat]",
      ".v99-seat",
      ".v99-seat-cell",
      ".v99-bus-seat",
      ".v99n-seat",
      ".bus-seat",
      ".seat-cell",
      ".seat"
    ];

    var out = [];
    sels.forEach(function(sel){
      qa(sel).forEach(function(el){
        if(out.indexOf(el) < 0) out.push(el);
      });
    });

    // Eğer mevcut koltuklar sadece sayı butonu gibi çizildiyse panel içinden sayısal kutuları da yakala
    qa(".v99-seat-map * , .v99n-seat-map * , .v99-bus-map * , .v99-seat-visual * , .v99n-seat-visual *").forEach(function(el){
      var n = extractSeatNo(el);
      if(n && seatByNo[n] && out.indexOf(el) < 0){
        out.push(el);
      }
    });

    return out;
  }

  function applySeatClasses(){
    var live = liveStop();
    var next = nextStop();

    candidateSeatEls().forEach(function(el){
      var no = extractSeatNo(el);
      if(!no) return;

      var seat = seatByNo[String(no)];
      if(!seat) return;

      el.classList.add("v99n-seat-clickable");

      [
        "v99n-seat-empty",
        "v99n-seat-occupied",
        "v99n-seat-live-off",
        "v99n-seat-next-off",
        "v99n-seat-reserved",
        "v99n-seat-has-bag"
      ].forEach(function(c){
        el.classList.remove(c);
      });

      var st = statusOf(seat);

      if(st.cls === "reserved"){
        el.classList.add("v99n-seat-reserved");
      }else if(seat.occupied){
        el.classList.add("v99n-seat-occupied");
      }else{
        el.classList.add("v99n-seat-empty");
      }

      if(seat.occupied && sameStop(seat.to_stop, live)){
        el.classList.add("v99n-seat-live-off");
      }else if(seat.occupied && sameStop(seat.to_stop, next)){
        el.classList.add("v99n-seat-next-off");
      }

      var bag = num(seat.bag_count || seat.bag_total || seat.bagaj_count);
      var dot = q(".v99n-seat-bag-dot", el);

      if(bag > 0){
        el.classList.add("v99n-seat-has-bag");
        if(!dot){
          dot = document.createElement("span");
          dot.className = "v99n-seat-bag-dot";
          el.appendChild(dot);
        }
        dot.textContent = "🧳" + (bag > 1 ? bag : "");
      }else if(dot){
        dot.remove();
      }
    });
  }

  async function loadSeatMap(force){
    var now = Date.now();
    if(!force && now - lastFetch < 1800 && seatCache.length){
      applySeatClasses();
      return seatCache;
    }

    lastFetch = now;

    try{
      var res = await fetch("/api/live-seat-map?_v=v99o_" + now, {cache:"no-store"});
      var data = await res.json();

      seatCache = Array.isArray(data.seats) ? data.seats : [];
      seatByNo = {};

      seatCache.forEach(function(s){
        seatByNo[String(s.seat_no)] = s;
      });

      window.MuavinV99SeatMap = {
        seats: seatCache,
        byNo: seatByNo,
        updatedAt: now
      };

      applySeatClasses();
      return seatCache;
    }catch(err){
      console.warn("V99O seat map load error", err);
      return seatCache;
    }
  }

  document.addEventListener("click", function(e){
    var el = e.target.closest("[data-seat-no], [data-seat], .v99-seat, .v99-seat-cell, .v99-bus-seat, .v99n-seat, .bus-seat, .seat-cell, .seat");
    if(!el) return;

    var no = extractSeatNo(el);
    if(!no || !seatByNo[String(no)]) return;

    e.preventDefault();
    e.stopPropagation();
    showSeatDetail(no);
  }, true);

  document.addEventListener("DOMContentLoaded", function(){
    loadSeatMap(true);
    setTimeout(function(){ applySeatClasses(); }, 600);
    setTimeout(function(){ applySeatClasses(); }, 1400);
  });

  window.addEventListener("load", function(){
    loadSeatMap(true);
  });

  document.addEventListener("continueEtaUpdated", function(){
    loadSeatMap(false);
  });

  setInterval(function(){
    loadSeatMap(false);
  }, 3500);

  window.MuavinV99SeatDetailReload = function(){
    return loadSeatMap(true);
  };
})();
/* V99O_SEAT_DETAIL_POPUP_JS_END */
'''

css = css.rstrip() + css_block + "\n"
js = js.rstrip() + js_block + "\n"

WEB_CSS.write_text(css, encoding="utf-8")
WEB_JS.write_text(js, encoding="utf-8")

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
for p in [WEB_CSS, WEB_JS, AND_CSS, AND_JS]:
    if p.exists():
        t = p.read_text(encoding="utf-8", errors="ignore")
        print(p.name, "V99O:", "VAR" if "V99O_SEAT_DETAIL_POPUP" in t else "YOK")

print()
print("✅ V99O tamam. /continue-trip?v=v99o ile yenile, doluluk panelinde koltuk 1/3/5/4'e tıkla.")
