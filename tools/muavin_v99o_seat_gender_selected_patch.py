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

print("===== V99O KOLTUK RENK + SEÇİLİ PATCH =====")

for p in [WEB_CSS, WEB_JS, AND_CSS, AND_JS]:
    if p.exists():
        bak = p.with_name(p.name + f".bak-v99o-seat-color-{STAMP}")
        shutil.copy2(p, bak)
        print("📦 backup:", bak)

if not WEB_CSS.exists():
    raise SystemExit("❌ CSS yok: " + str(WEB_CSS))

if not WEB_JS.exists():
    raise SystemExit("❌ JS yok: " + str(WEB_JS))


css = WEB_CSS.read_text(encoding="utf-8", errors="ignore")
js = WEB_JS.read_text(encoding="utf-8", errors="ignore")

css = re.sub(
    r"\n?/\* V99O_SEAT_GENDER_SELECTED_CSS_START \*/.*?/\* V99O_SEAT_GENDER_SELECTED_CSS_END \*/\n?",
    "\n",
    css,
    flags=re.S
)

js = re.sub(
    r"\n?/\* V99O_SEAT_GENDER_SELECTED_JS_START \*/.*?/\* V99O_SEAT_GENDER_SELECTED_JS_END \*/\n?",
    "\n",
    js,
    flags=re.S
)

css_block = r'''

/* V99O_SEAT_GENDER_SELECTED_CSS_START */

/* Koltuk renk sistemi:
   Yeşil = boş
   Mavi  = bay
   Pembe = bayan
   Kırmızı = cinsiyet bilinmiyor / manuel dolu
   Sarı dış halka = bu durakta inecek
*/

.v99-seat-color-cell{
  position:relative !important;
  overflow:visible !important;
  transition:
    transform .16s ease,
    box-shadow .16s ease,
    border-color .16s ease,
    filter .16s ease !important;
}

/* BOŞ */
.v99-seat-color-cell.v99-seat-free{
  background:linear-gradient(180deg,#23e875 0%,#0eaa52 100%) !important;
  color:#06150c !important;
  border-color:#41ff95 !important;
  box-shadow:
    inset 0 1px 0 rgba(255,255,255,.35),
    0 8px 18px rgba(0,0,0,.30),
    0 0 0 1px rgba(53,255,138,.22) !important;
}

/* BAY */
.v99-seat-color-cell.v99-seat-male{
  background:linear-gradient(180deg,#3a8bff 0%,#095ed6 100%) !important;
  color:#eef6ff !important;
  border-color:#73adff !important;
  box-shadow:
    inset 0 1px 0 rgba(255,255,255,.34),
    0 8px 18px rgba(0,0,0,.32),
    0 0 0 1px rgba(58,139,255,.28),
    0 0 14px rgba(58,139,255,.20) !important;
}

/* BAYAN */
.v99-seat-color-cell.v99-seat-female{
  background:linear-gradient(180deg,#ff5ab1 0%,#d41467 100%) !important;
  color:#fff1f8 !important;
  border-color:#ff8ccd !important;
  box-shadow:
    inset 0 1px 0 rgba(255,255,255,.34),
    0 8px 18px rgba(0,0,0,.32),
    0 0 0 1px rgba(255,90,177,.28),
    0 0 14px rgba(255,90,177,.20) !important;
}

/* Cinsiyet bilinmiyorsa / manuel dolu */
.v99-seat-color-cell.v99-seat-unknown{
  background:linear-gradient(180deg,#ff365f 0%,#b70f31 100%) !important;
  color:#fff !important;
  border-color:#ff6d88 !important;
  box-shadow:
    inset 0 1px 0 rgba(255,255,255,.30),
    0 8px 18px rgba(0,0,0,.32),
    0 0 0 1px rgba(255,40,80,.25) !important;
}

/* Bu durakta inecek: ana rengi bozma, sadece sarı halka ver */
.v99-seat-color-cell.v99-seat-off-here{
  border-color:#ffbf2e !important;
  box-shadow:
    inset 0 1px 0 rgba(255,255,255,.36),
    0 8px 18px rgba(0,0,0,.34),
    0 0 0 3px rgba(255,191,46,.80),
    0 0 18px rgba(255,191,46,.58),
    0 0 32px rgba(255,191,46,.28) !important;
}

/* Seçili koltuk */
.v99-seat-color-cell.v99-seat-selected{
  transform:scale(1.075) !important;
  z-index:12 !important;
  border-color:#ffffff !important;
  box-shadow:
    inset 0 1px 0 rgba(255,255,255,.45),
    0 0 0 3px rgba(255,255,255,.95),
    0 0 0 6px rgba(58,139,255,.45),
    0 0 28px rgba(58,139,255,.70),
    0 12px 28px rgba(0,0,0,.46) !important;
  filter:saturate(1.12) brightness(1.07) !important;
}

.v99-seat-color-cell.v99-seat-selected::after{
  content:"✓";
  position:absolute;
  top:-9px;
  right:-9px;
  width:22px;
  height:22px;
  border-radius:999px;
  display:flex;
  align-items:center;
  justify-content:center;
  font-size:13px;
  font-weight:1000;
  color:#061018;
  background:linear-gradient(180deg,#fff 0%,#bdd8ff 100%);
  box-shadow:0 0 14px rgba(255,255,255,.75);
}

/* Bagaj rozeti */
.v99-seat-bag-dot{
  position:absolute;
  right:-8px;
  bottom:-8px;
  min-width:22px;
  height:22px;
  padding:0 5px;
  border-radius:999px;
  display:flex;
  align-items:center;
  justify-content:center;
  font-size:13px;
  line-height:1;
  background:linear-gradient(180deg,#1d2634 0%,#101722 100%);
  border:1px solid rgba(255,255,255,.22);
  box-shadow:0 0 12px rgba(0,0,0,.55);
  z-index:15;
}

.v99-seat-bag-dot b{
  margin-left:2px;
  font-size:11px;
  color:#fff;
}

/* Legend ekleri */
.v99-seat-gender-legend{
  display:flex;
  flex-wrap:wrap;
  gap:10px;
  margin:14px 0 0;
}

.v99-seat-legend-chip{
  display:inline-flex;
  align-items:center;
  gap:8px;
  min-height:36px;
  padding:8px 13px;
  border-radius:999px;
  background:rgba(255,255,255,.055);
  border:1px solid rgba(255,255,255,.12);
  color:#dce6f8;
  font-weight:900;
  letter-spacing:.02em;
}

.v99-seat-legend-dot{
  width:15px;
  height:15px;
  border-radius:999px;
  display:inline-block;
  box-shadow:0 0 10px currentColor;
}

.v99-seat-legend-dot.male{
  background:#3a8bff;
  color:#3a8bff;
}

.v99-seat-legend-dot.female{
  background:#ff5ab1;
  color:#ff5ab1;
}

.v99-seat-legend-dot.selected{
  background:#ffffff;
  color:#ffffff;
}

/* V99O_SEAT_GENDER_SELECTED_CSS_END */
'''

js_block = r'''

/* V99O_SEAT_GENDER_SELECTED_JS_START */
(function(){
  "use strict";

  var selectedSeatNo = "";

  function q(sel){
    return document.querySelector(sel);
  }

  function qa(sel, root){
    return Array.from((root || document).querySelectorAll(sel));
  }

  function text(el){
    return el ? String(el.textContent || "").trim() : "";
  }

  function norm(s){
    return String(s || "")
      .replace(/İ/g, "i")
      .replace(/I/g, "i")
      .toLocaleLowerCase("tr-TR")
      .replace(/ı/g, "i")
      .replace(/ğ/g, "g")
      .replace(/ü/g, "u")
      .replace(/ş/g, "s")
      .replace(/ö/g, "o")
      .replace(/ç/g, "c")
      .replace(/\s+/g, "")
      .trim();
  }

  function sameStop(a,b){
    var na = norm(a);
    var nb = norm(b);
    if(!na || !nb) return false;
    return na === nb || na.indexOf(nb) >= 0 || nb.indexOf(na) >= 0;
  }

  function getLiveStop(){
    return text(q("#liveCurrentStopName")) || text(q("[data-live-stop]")) || "";
  }

  function genderClass(seat){
    var g = norm(seat && seat.gender);

    if(g.indexOf("bayan") >= 0 || g.indexOf("kadin") >= 0 || g.indexOf("female") >= 0){
      return "v99-seat-female";
    }

    if(g.indexOf("bay") >= 0 || g.indexOf("erkek") >= 0 || g.indexOf("male") >= 0){
      return "v99-seat-male";
    }

    return "v99-seat-unknown";
  }

  function num(x){
    var n = Number(x || 0);
    return Number.isFinite(n) ? n : 0;
  }

  function isSeatNumberText(t){
    if(!/^\d{1,2}$/.test(t)) return false;
    var n = Number(t);
    return n >= 1 && n <= 60;
  }

  function looksLikeSeatElement(el){
    if(!el) return false;

    var t = text(el);
    var dataNo = el.getAttribute("data-seat-no") || el.getAttribute("data-seat") || el.dataset.seatNo || "";

    if(!isSeatNumberText(dataNo || t)) return false;

    if(el.closest(".v99-dock, .v99-bottom-dock, nav, .bottom-nav, .v99-top, .v99-stats, .v99-tl-card, .v99-prox-card")){
      return false;
    }

    var r = el.getBoundingClientRect();
    if(r.width && r.height){
      if(r.width < 28 || r.height < 28) return false;
      if(r.width > 130 || r.height > 130) return false;
    }

    return true;
  }

  function findSeatEls(){
    var direct = qa("[data-seat-no], [data-seat], .v99-seat, .v99-seat-cell, .v99-seat-btn, .v99-map-seat, .v99-bus-seat, .seat-cell, .seat-btn")
      .filter(looksLikeSeatElement);

    if(direct.length >= 10) return direct;

    return qa("button, .seat, div, span")
      .filter(looksLikeSeatElement);
  }

  function ensureBagDot(el, count){
    var old = el.querySelector(":scope > .v99-seat-bag-dot");
    if(count <= 0){
      if(old) old.remove();
      return;
    }

    if(!old){
      old = document.createElement("span");
      old.className = "v99-seat-bag-dot";
      el.appendChild(old);
    }

    old.innerHTML = "🧳" + (count > 1 ? "<b>" + count + "</b>" : "");
  }

  function applySeatClasses(seats){
    var live = getLiveStop();
    var byNo = {};

    seats.forEach(function(s){
      byNo[String(s.seat_no || "").trim()] = s;
    });

    findSeatEls().forEach(function(el){
      var no = String(
        el.getAttribute("data-seat-no") ||
        el.getAttribute("data-seat") ||
        el.dataset.seatNo ||
        text(el)
      ).trim();

      if(!isSeatNumberText(no)) return;

      var s = byNo[no] || { seat_no:no, occupied:false };

      el.classList.add("v99-seat-color-cell");
      el.setAttribute("data-v99-seat-no", no);

      el.classList.remove(
        "v99-seat-free",
        "v99-seat-male",
        "v99-seat-female",
        "v99-seat-unknown",
        "v99-seat-off-here",
        "v99-seat-has-bag",
        "v99-seat-selected"
      );

      if(s.occupied){
        el.classList.add(genderClass(s));
      }else{
        el.classList.add("v99-seat-free");
      }

      if(s.occupied && live && sameStop(s.to_stop, live)){
        el.classList.add("v99-seat-off-here");
      }

      var bag = num(s.bag_count || s.bag_total || s.bagaj_count);
      if(bag > 0){
        el.classList.add("v99-seat-has-bag");
      }

      ensureBagDot(el, bag);

      if(selectedSeatNo && String(selectedSeatNo) === String(no)){
        el.classList.add("v99-seat-selected");
      }
    });

    ensureLegend();
  }

  function ensureLegend(){
    if(q(".v99-seat-gender-legend")) return;

    var seatEls = findSeatEls();
    if(!seatEls.length) return;

    var host = seatEls[seatEls.length - 1].closest(".v99-seat-map, .v99-seat-grid, .v99-bus-map, .v99-seat-plan, .v99-occupancy-panel, .v99-seat-shell");
    if(!host){
      host = seatEls[seatEls.length - 1].parentElement;
    }

    if(!host || !host.parentElement) return;

    var legend = document.createElement("div");
    legend.className = "v99-seat-gender-legend";
    legend.innerHTML =
      '<span class="v99-seat-legend-chip"><i class="v99-seat-legend-dot male"></i>Bay</span>' +
      '<span class="v99-seat-legend-chip"><i class="v99-seat-legend-dot female"></i>Bayan</span>' +
      '<span class="v99-seat-legend-chip"><i class="v99-seat-legend-dot selected"></i>Seçili</span>';

    host.parentElement.insertBefore(legend, host.nextSibling);
  }

  async function refreshSeatColors(){
    try{
      var res = await fetch("/api/live-seat-map?_v=v99o_" + Date.now(), {
        credentials:"same-origin",
        cache:"no-store"
      });

      if(!res.ok) return;

      var data = await res.json();
      var seats = Array.isArray(data.seats) ? data.seats : [];

      applySeatClasses(seats);
    }catch(e){}
  }

  document.addEventListener("click", function(ev){
    var el = ev.target.closest("[data-v99-seat-no], [data-seat-no], [data-seat], .v99-seat-color-cell");

    if(!el || !looksLikeSeatElement(el)) return;

    var no = String(
      el.getAttribute("data-v99-seat-no") ||
      el.getAttribute("data-seat-no") ||
      el.getAttribute("data-seat") ||
      el.dataset.seatNo ||
      text(el)
    ).trim();

    if(!isSeatNumberText(no)) return;

    selectedSeatNo = no;

    qa(".v99-seat-color-cell.v99-seat-selected").forEach(function(x){
      x.classList.remove("v99-seat-selected");
    });

    el.classList.add("v99-seat-selected");
  }, true);

  window.MuavinV99SeatColorRefresh = refreshSeatColors;

  refreshSeatColors();

  if(document.readyState === "loading"){
    document.addEventListener("DOMContentLoaded", refreshSeatColors);
  }

  window.addEventListener("load", refreshSeatColors);
  document.addEventListener("continueEtaUpdated", refreshSeatColors);

  var left = 40;
  var timer = setInterval(function(){
    refreshSeatColors();
    left--;
    if(left <= 0) clearInterval(timer);
  }, 900);
})();
/* V99O_SEAT_GENDER_SELECTED_JS_END */
'''

css = css.rstrip() + css_block + "\n"
js = js.rstrip() + js_block + "\n"

WEB_CSS.write_text(css, encoding="utf-8")
WEB_JS.write_text(js, encoding="utf-8")

print("✅ web CSS yazıldı:", WEB_CSS)
print("✅ web JS yazıldı:", WEB_JS)

if AND_CSS.parent.exists():
    AND_CSS.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(WEB_CSS, AND_CSS)
    print("✅ android CSS senkron:", AND_CSS)

if AND_JS.parent.exists():
    AND_JS.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(WEB_JS, AND_JS)
    print("✅ android JS senkron:", AND_JS)

print()
print("===== KONTROL =====")
for p in [WEB_CSS, WEB_JS, AND_CSS, AND_JS]:
    if p.exists():
        txt = p.read_text(encoding="utf-8", errors="ignore")
        print(("VAR " if "V99O_SEAT_GENDER_SELECTED" in txt else "YOK "), p)

print()
print("✅ V99O tamam. Tarayıcıda /continue-trip?v=v99o ile yenile.")
