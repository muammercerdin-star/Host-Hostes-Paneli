/* =========================================================
   BAGS MODULE
   Bagaj rozetleri + bagaj ses özeti + bagaj temizleme
========================================================= */

// Bagaj göz bilgisi sesli uyarıda kullanılacak.
// Örnek: bagMetaCache["3"] = {count:1, right:0, left_front:1, left_back:0, eyes:["LF"]}
const bagMetaCache = {};

function bagSeatsForStop(stopName){
  const seats = seatsForStop(stopName).map(Number).filter(Boolean);
  const bagSeats = [];

  seats.forEach(seatNo => {
    const el = document.querySelector(`.seat[data-seat="${seatNo}"]`);
    if(!el) return;

    const cntText = el.querySelector(".bag-count")?.textContent || "0";
    const cnt = parseInt(cntText, 10) || 0;
    const hasBag = el.classList.contains("has-bag") || cnt > 0;

    if(hasBag){
      bagSeats.push(seatNo);
    }
  });

  return bagSeats;
}

function formatSeatListForVoice(seats){
  const list = seats.map(String);

  if(list.length === 0) return "";
  if(list.length === 1) return `${list[0]} numaralı koltukta`;

  const last = list.pop();
  return `${list.join(", ")} ve ${last} numaralı koltuklarda`;
}

function bagEyeVoicePartsForSeat(seatNo){
  const meta = bagMetaCache[String(seatNo)] || {};
  const parts = [];

  const right = Number(meta.right || 0);
  const leftFront = Number(meta.left_front || 0);
  const leftBack = Number(meta.left_back || 0);

  function add(label, count){
    if(count <= 0) return;
    if(count === 1) parts.push(`${label} gözde bagaj`);
    else parts.push(`${label} gözde ${count} bagaj`);
  }

  add("sağ", right);
  add("sol ön", leftFront);
  add("sol arka", leftBack);

  if(!parts.length && Array.isArray(meta.eyes)){
    if(meta.eyes.includes("R")) parts.push("sağ gözde bagaj");
    if(meta.eyes.includes("LF")) parts.push("sol ön gözde bagaj");
    if(meta.eyes.includes("LB")) parts.push("sol arka gözde bagaj");
  }

  return parts;
}

function bagVoiceSummaryForStop(stopName){
  const seats = bagSeatsForStop(stopName).map(Number).filter(Boolean);
  if(!seats.length) return "";

  const chunks = seats.map(seatNo => {
    const parts = bagEyeVoicePartsForSeat(seatNo);

    if(parts.length){
      return `${seatNo} numarada ${parts.join(", ")}`;
    }

    return `${seatNo} numarada bagaj`;
  });

  return `Bagaj uyarısı: ${chunks.join(". ")} var.`;
}

async function fetchBagMeta(seatNo){
  const key = String(seatNo);

  try{
    const u = `/api/bags/meta?trip=${encodeURIComponent(BAG_TRIP)}&seat=${encodeURIComponent(seatNo)}`;
    const j = await safeJsonFetch(u);

    const right = Number(j?.right || 0);
    const leftFront = Number(j?.left_front || 0);
    const leftBack = Number(j?.left_back || 0);
    const total = Number(j?.count || (right + leftFront + leftBack));

    const eyes = [];
    if(right > 0) eyes.push("R");
    if(leftFront > 0) eyes.push("LF");
    if(leftBack > 0) eyes.push("LB");

    const meta = {
      count: total,
      right,
      left_front: leftFront,
      left_back: leftBack,
      eyes
    };

    bagMetaCache[key] = meta;
    return meta;
  }catch(_){
    return bagMetaCache[key] || { count:0, right:0, left_front:0, left_back:0, eyes:[] };
  }
}

function eyesToIcons(eyes){
  if(!eyes || !eyes.length) return "";

  const set = new Set(eyes);
  const parts = [];

  if(set.has("R")) parts.push("➡️");
  if(set.has("LF")) parts.push("⬅️🔺");
  if(set.has("LB")) parts.push("⬅️🔻");

  return parts.join(" ");
}

async function refreshBagBadgeForSeat(seatNo){
  const el = $("#seat-" + seatNo);
  if(!el) return;

  const meta = await fetchBagMeta(seatNo);
  const cnt = meta.count;
  const eyes = meta.eyes || [];

  el.classList.toggle("has-bag", cnt > 0);

  const bagCount = el.querySelector(".bag-count");
  const bagDir = el.querySelector(".bag-dir");
  const badge = el.querySelector(".bag-badge");

  if(bagCount) bagCount.textContent = String(cnt || 0);
  if(bagDir) bagDir.textContent = eyesToIcons(eyes) || "";
  if(badge) badge.title = cnt ? `Bagaj: ${cnt} adet` : "Bagaj yok";
}

async function refreshBagsAll(){
  const seats = $$(".seat").map(el => Number(el.dataset.seat));
  for(const n of seats){
    await refreshBagBadgeForSeat(n);
  }
}

async function clearBagsForSeat(seatNo){
  try{
    const u = `/bags/clear?trip=${encodeURIComponent(BAG_TRIP)}&seat=${encodeURIComponent(seatNo)}`;
    await safeJsonFetch(u, {
      method:"DELETE",
      headers:{ "X-CSRF-Token":csrf }
    });
  }catch(_){}

  const el = $("#seat-" + seatNo);
  if(el){
    el.classList.remove("has-bag");

    const cnt = el.querySelector(".bag-count");
    const dir = el.querySelector(".bag-dir");

    if(cnt) cnt.textContent = "0";
    if(dir) dir.textContent = "";
  }
}

window.SeatsBags = {
  bagMetaCache,
  bagSeatsForStop,
  formatSeatListForVoice,
  bagEyeVoicePartsForSeat,
  bagVoiceSummaryForStop,
  fetchBagMeta,
  eyesToIcons,
  refreshBagBadgeForSeat,
  refreshBagsAll,
  clearBagsForSeat
};
