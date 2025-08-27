// static/app.js  — koltuk kayıtları (DB ile)

// --- API yardımcıları ---
async function apiSave(seat_no, payload){
  await fetch("/api/seat", {
    method:"POST",
    headers:{"Content-Type":"application/json"},
    body: JSON.stringify({seat_no, ...payload})
  });
}
async function apiClear(seat_no){
  await fetch("/api/seat/clear", {
    method:"POST",
    headers:{"Content-Type":"application/json"},
    body: JSON.stringify({seat_no})
  });
}
async function apiLoad(){
  const r = await fetch("/api/seats");
  return await r.json(); // {"3": {stop:"Balıkesir", pay:"Nakit", price:150}, ...}
}

// --- sayfa içi durum ---
window.seatStates = {}; // num -> {stop, pay, price}

// --- koltuk tıklama ---
async function onSeatClick(ev) {
  const seatEl  = ev.currentTarget;
  if (!seatEl.classList.contains("seat")) return;

  const num     = seatEl.dataset.num;                 // koltuk no (string)
  const labelEl = seatEl.parentElement.querySelector(".label");

  // BOŞ → KAYDET
  if (!seatEl.classList.contains("occupied")) {
    const stop = prompt("Nerede ineceksiniz? (durak adı)", "");
    if (!stop) return;

    const pay = prompt("Ödeme türü (Biletli/Nakit/IBAN/Online/Ücretsiz)", "Nakit") || "";
    let price = "";
    if (pay.toLowerCase() !== "biletli" && pay.toLowerCase() !== "ücretsiz") {
      price = prompt("Tutar (₺)", "") || "";
    }

    // ekrana yansıt
    seatEl.classList.add("occupied");
    labelEl.textContent = stop;
    window.seatStates[num] = { stop, pay, price };

    // DB'ye yaz
    await apiSave(num, { stop, pay, price });

  } else {
    // DOLU → İNDİR / DÜZENLE
    const act = prompt("Seçim: indir / düzenle / iptal", "indir");
    if (!act) return;

    if (act.toLowerCase() === "indir") {
      seatEl.classList.remove("occupied");
      labelEl.textContent = "";
      delete window.seatStates[num];
      await apiClear(num); // DB'den sil

    } else if (act.toLowerCase() === "düzenle") {
      const old  = window.seatStates[num] || {};
      const stop = prompt("İniş yeri", old.stop || "")   || old.stop || "";
      const pay  = prompt("Ödeme türü", old.pay || "Nakit") || old.pay || "";
      const price= prompt("Tutar (₺)", old.price || "")  || old.price || "";
      window.seatStates[num] = { stop, pay, price };
      labelEl.textContent = stop;
      await apiSave(num, { stop, pay, price }); // DB'de güncelle
    }
  }
}

// --- bağlama ve ilk yük ---
function bindSeats(){
  document.querySelectorAll(".seat[data-num]").forEach(el=>{
    el.style.cursor = "pointer";
    el.addEventListener("click", onSeatClick);
  });
}

document.addEventListener("DOMContentLoaded", async () => {
  bindSeats();
  // DB'deki mevcut koltukları ekrana bas
  const data = await apiLoad();
  for (const [num, v] of Object.entries(data)){
    const s   = document.querySelector(`.seat[data-num='${num}']`);
    const lbl = s?.parentElement.querySelector(".label");
    if (s && lbl){
      s.classList.add("occupied");
      lbl.textContent = v.stop || "";
      window.seatStates[num] = v;
    }
  }
});
