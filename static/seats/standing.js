/* =========================================================
   STANDING MODULE
   Ayakta yolcu + hızlı tahsilat + ayakta liste
========================================================= */

function openCash(){
  populateStops().then(() => {
    const selected = getSelectedStopName() || "";
    const live = getDisplayLiveStop();
    const fromDefault = live || selected || serverStops?.[0] || "";

    if(selected) setValue("#cashTo", selected);
    if(fromDefault) setValue("#cashFrom", fromDefault);

    openModal("#cashBackdrop", "#cashModal");
  });
}

function closeCash(){
  closeModal("#cashBackdrop", "#cashModal");
}

async function saveCash(){
  const cnt = Math.max(1, parseInt($("#cashCount")?.value || "1", 10));
  const price = parseMoney($("#cashPrice")?.value || 0);
  const pay = $("#cashPay")?.value || "nakit";
  const from = $("#cashFrom")?.value || speedState.liveStop || getSelectedStopName() || serverStops?.[0] || "";
  const to = $("#cashTo")?.value || "";
  const note = $("#cashNote")?.value || "";

  if(!to){
    toast("Nereye seç");
    return;
  }

  try{
    const j = await safeJsonFetch("/api/standing", {
      method:"POST",
      headers:{ "Content-Type":"application/json", "X-CSRF-Token":csrf },
      body:JSON.stringify({ count:cnt, price, payment:pay, from, to, note })
    });

    if(!j?.ok) throw new Error(j?.msg || "Ayakta kayıt hatası");

    await loadStandingTotals();
    await loadStandingItems();

    updateStats();
    refreshStopBadges();
    renderAI();
    renderTimeline();
    renderStandingList();
    renderQuickStandingList();
    updateCompactHeader();

    setValue("#cashCount", "1");
    setValue("#cashPrice", "0");
    setValue("#cashNote", "");

    closeCash();
    toast("Ayakta satış eklendi");
  }catch(e){
    toast(e.message || "Tahsilat hatası");
  }
}

async function loadStandingTotals(){
  try{
    const j = await safeJsonFetch("/api/standing");

    if(j?.ok){
      standingCount = Number(j.count || 0);
      standingRevenue = Number(j.revenue || 0);
      return;
    }
  }catch(_){}

  try{
    const x = JSON.parse(localStorage.getItem("standingTotals:" + TRIP_KEY) || "null");
    standingCount = Number(x?.count || 0);
    standingRevenue = Number(x?.revenue || 0);
  }catch(_){
    standingCount = 0;
    standingRevenue = 0;
  }
}

async function loadStandingItems(){
  try{
    const j = await safeJsonFetch("/api/standing/list");

    if(j?.ok && Array.isArray(j.items)){
      standingItems = j.items.slice();
      return;
    }
  }catch(_){}

  try{
    const x = JSON.parse(localStorage.getItem("standingItems:" + TRIP_KEY) || "[]");
    standingItems = Array.isArray(x) ? x : [];
  }catch(_){
    standingItems = [];
  }
}

async function loadParcelItems(){
  try{
    const j = await safeJsonFetch("/api/parcels?status=bekliyor");

    if(j?.ok && Array.isArray(j.items)){
      parcelItems = j.items.slice();
      return;
    }
  }catch(_){}

  parcelItems = [];
}

function renderStandingList(){
  const list = $("#standingList");
  const sum = $("#standingSummary");
  const bulk = $("#standingBulkOff");

  if(!list || !sum || !bulk) return;

  list.innerHTML = "";

  if(!standingItems.length){
    sum.textContent = "Kayıt yok";
    bulk.style.display = "none";
    return;
  }

  const totalPeople = standingItems.reduce((acc, it) => acc + Number(it?.count || 0), 0);
  const totalPrice = standingItems.reduce((acc, it) => {
    if(typeof it?.total_amount !== "undefined" && it?.total_amount !== null){
      return acc + Number(it.total_amount || 0);
    }

    return acc + (Number(it?.count || 0) * Number(it?.price || 0));
  }, 0);

  sum.textContent = `${totalPeople} ayakta · ${fmtTL(totalPrice)}`;
  bulk.style.display = "inline-flex";

  standingItems.forEach((it) => {
    const total = (typeof it.total_amount !== "undefined" && it.total_amount !== null)
      ? Number(it.total_amount || 0)
      : (Number(it.count || 0) * Number(it.price || 0));

    const d = document.createElement("div");
    d.className = "standing-item";
    d.innerHTML = `
      <div>
        <b>${it.from || "—"} → ${it.to || "—"}</b>
        <small>${it.count || 0} kişi · ${fmtTL(total)} · ${it.payment || "nakit"}</small>
      </div>
      <button class="btn danger" style="min-height:40px;padding:8px 12px" data-id="${it.id}">İndir</button>
    `;

    list.appendChild(d);
  });

  list.querySelectorAll("button[data-id]").forEach(btn => {
    btn.addEventListener("click", () => removeStandingById(parseInt(btn.dataset.id, 10)));
  });
}

function openStandingModal(){
  renderStandingList();
  openModal("#standingBackdrop", "#standingModal");
}

function closeStandingModal(){
  closeModal("#standingBackdrop", "#standingModal");
}

async function removeStandingById(itemId){
  if(!itemId) return;

  try{
    const j = await safeJsonFetch(`/api/standing?id=${encodeURIComponent(itemId)}`, {
      method:"DELETE",
      headers:{ "X-CSRF-Token": csrf }
    });

    if(!j?.ok) throw new Error(j?.msg || "Ayakta kayıt silinemedi");

    await loadStandingTotals();
    await loadStandingItems();

    updateStats();
    refreshStopBadges();
    renderStandingList();
    renderQuickStandingList();
    renderAI();
    renderTimeline();
    updateCompactHeader();

    toast("Ayakta kayıt indirildi");
  }catch(e){
    toast(e.message || "Silme hatası");
  }
}

async function offloadStandingForStop(stopName){
  try{
    const j = await safeJsonFetch("/api/standing?to=" + encodeURIComponent(stopName), {
      method:"DELETE",
      headers:{ "X-CSRF-Token": csrf }
    });

    if(!j?.ok) throw new Error(j?.msg || "Ayakta kayıtlar indirilemedi");

    await loadStandingTotals();
    await loadStandingItems();

    updateStats();
    refreshStopBadges();
    renderQuickStandingList();
    renderStandingList();
    renderAI();
    renderTimeline();
    updateCompactHeader();

    return Number(j.count || 0);
  }catch(e){
    toast(e.message || "Ayakta indirme hatası");
    return 0;
  }
}

window.SeatsStanding = {
  openCash,
  closeCash,
  saveCash,
  loadStandingTotals,
  loadStandingItems,
  loadParcelItems,
  renderStandingList,
  openStandingModal,
  closeStandingModal,
  removeStandingById,
  offloadStandingForStop
};
