/* =========================================================
   continue_trip_core.js
   Otomatik çıkarıldı: continue_trip.html
   Jinja verileri window.CONTINUE_BOOT üzerinden alınır.
========================================================= */


/* ===== SCRIPT BLOCK: continue-trip-runtime-sync ===== */
(function(){
  const BOOT = window.CONTINUE_BOOT || {};
    const tripId = BOOT.tripId || 0;
    const runtimeGpsKm = BOOT.runtimeGpsKm || "";
    const runtimeSpeed = BOOT.runtimeSpeed || 0;
    const runtimeStop = BOOT.runtimeStop || "";
    const runtimeEta = BOOT.runtimeEta || "";

  function parseKmAny(value){
    const raw = String(value ?? "").trim();
    if(!raw) return NaN;

    const cleaned = raw
      .replace(/km/gi, "")
      .replace(/m/gi, "")
      .trim()
      .replace(",", ".");

    const n = Number(cleaned);
    return Number.isFinite(n) ? n : NaN;
  }

  function formatGpsKm(value){
    const raw = String(value ?? "").trim();
    if(!raw) return "—";

    const km = parseKmAny(raw);
    if(!Number.isFinite(km)) return raw;

    if(km < 0) return "—";
    if(km < 1) return `${Math.round(km * 1000)} m`;
    return `${km.toFixed(2)} km`;
  }

  function setInitial(){
    const speedEl = document.getElementById("liveSpeedText");
    const stopEl  = document.getElementById("liveCurrentStopName");
    const distEl  = document.getElementById("liveDistanceValue");
    const etaEl   = document.getElementById("liveEtaValue");

    if(speedEl && !window.CONTINUE_LIVE_SPEED_ENGINE_ACTIVE){
      const n = parseInt(runtimeSpeed || 0, 10) || 0;
      speedEl.textContent = `${n} km/sa`;
    }

    if(stopEl && runtimeStop){
      stopEl.textContent = runtimeStop;
    }

    if(distEl && runtimeGpsKm){
      distEl.textContent = formatGpsKm(runtimeGpsKm);
    }

    if(etaEl && runtimeEta){
      etaEl.textContent = runtimeEta;
    }
  }

  function sync(){
    fetch(`/api/live-runtime-state?trip_id=${encodeURIComponent(tripId)}&_=${Date.now()}`, {
      method: "GET",
      credentials: "same-origin",
      cache: "no-store"
    })
    .then(r => r.json())
    .then(j => {
      const s = j && j.state ? j.state : null;
      if(!s) return;

      const speedEl = document.getElementById("liveSpeedText");
      const stopEl  = document.getElementById("liveCurrentStopName");
      const distEl  = document.getElementById("liveDistanceValue");
      const etaEl   = document.getElementById("liveEtaValue");

      if(speedEl && !window.CONTINUE_LIVE_SPEED_ENGINE_ACTIVE){
        const n = parseInt(s.speed || 0, 10) || 0;
        speedEl.textContent = `${n} km/sa`;
      }

      if(stopEl && s.live_stop){
        stopEl.textContent = s.live_stop;
      }

      if(distEl){
        distEl.textContent = formatGpsKm(s.gps_km);
      }

      if(etaEl && s.eta_main){
        etaEl.textContent = s.eta_main;
      }
    })
    .catch(() => {});
  }

  if(document.readyState === "loading"){
    document.addEventListener("DOMContentLoaded", function(){
      setInitial();
      sync();
    });
  }else{
    setInitial();
    sync();
  }

  setInterval(sync, 1500);
})();
/* ===== END SCRIPT BLOCK: continue-trip-runtime-sync ===== */


/* ===== SCRIPT BLOCK: live-stop-sheet-script ===== */
(function(){
  const offBtn = document.getElementById("liveOffloadMetric");
  const bagBtn = document.getElementById("liveBagajMetric");
  const stopNameEl = document.getElementById("liveCurrentStopName");

  const overlay = document.getElementById("liveStopSheetOverlay");
  const sheet = document.getElementById("liveStopSheet");
  const closeBtn = document.getElementById("liveStopSheetClose");
  const titleEl = document.getElementById("liveStopSheetTitle");
  const subEl = document.getElementById("liveStopSheetSub");
  const bodyEl = document.getElementById("liveStopSheetBody");
  const kickerEl = document.getElementById("liveStopSheetKicker");

  const BOOT = window.CONTINUE_BOOT || {};
    const routeStops = BOOT.routeStops || [];
    const csrfToken = BOOT.csrfToken || "";

  let lastDetailData = null;
  let lastKind = "offload";

  function text(v){
    return String(v == null ? "" : v);
  }

  function escapeHtml(v){
    return text(v)
      .replaceAll("&","&amp;")
      .replaceAll("<","&lt;")
      .replaceAll(">","&gt;")
      .replaceAll('"',"&quot;")
      .replaceAll("'","&#039;");
  }

  function currentStopName(){
    return (stopNameEl && stopNameEl.textContent ? stopNameEl.textContent : "").trim();
  }

  function openSheet(){
    if(overlay) overlay.classList.add("open");
    if(sheet){
      sheet.classList.add("open");
      sheet.setAttribute("aria-hidden", "false");
    }
    document.body.style.overflow = "hidden";
  }

  function closeSheet(){
    if(overlay) overlay.classList.remove("open");
    if(sheet){
      sheet.classList.remove("open");
      sheet.setAttribute("aria-hidden", "true");
    }
    document.body.style.overflow = "";
  }

  function renderEmpty(message){
    bodyEl.innerHTML = `<div class="sheet-empty">${escapeHtml(message)}</div>`;
  }

  function routeOptions(currentToStop){
    const current = text(currentToStop || "").trim();

    return (Array.isArray(routeStops) ? routeStops : []).map(stop => {
      const selected = stop === current ? "selected" : "";
      return `<option value="${escapeHtml(stop)}" ${selected}>${escapeHtml(stop)}</option>`;
    }).join("");
  }

  function findPassenger(seatNo){
    const passengers = lastDetailData && Array.isArray(lastDetailData.passengers)
      ? lastDetailData.passengers
      : [];

    return passengers.find(p => text(p.seat_no) === text(seatNo));
  }

  function renderChangeDestinationForm(passenger){
    if(!passenger){
      renderEmpty("Koltuk bilgisi bulunamadı.");
      return;
    }

    kickerEl.textContent = "İniş durağı değiştir";
    titleEl.textContent = `Koltuk ${passenger.seat_no}`;
    subEl.textContent = "Yeni ineceği durağı seç.";

    bodyEl.innerHTML = `
      <div class="sheet-change-form">
        <div class="sheet-change-card">
          <div class="sheet-change-title">Koltuk ${escapeHtml(passenger.seat_no)}</div>
          <div class="sheet-change-sub">
            Mevcut: ${escapeHtml(passenger.from_stop || "Biniş yok")} → ${escapeHtml(passenger.to_stop || "İniş yok")}
          </div>
        </div>

        <label>
          <div class="sheet-kicker" style="margin-bottom:8px;">Yeni iniş durağı</div>
          <select class="sheet-select" id="sheetNewToStop">
            ${routeOptions(passenger.to_stop)}
          </select>
        </label>

        <div class="sheet-note">
          Kaydedince koltuğun iniş durağı değişir. Koltuğa bağlı bagaj bilgisi de yeni durağın bagaj listesinde görünür.
        </div>

        <div class="sheet-form-actions">
          <button class="sheet-cancel-btn" type="button" id="sheetCancelChange">Vazgeç</button>
          <button class="sheet-save-btn" type="button" id="sheetSaveChange" data-seat-no="${escapeHtml(passenger.seat_no)}">Kaydet</button>
        </div>
      </div>
    `;

    const cancelBtn = document.getElementById("sheetCancelChange");
    const saveBtn = document.getElementById("sheetSaveChange");

    if(cancelBtn){
      cancelBtn.addEventListener("click", function(){
        if(lastKind === "bagaj") renderBags(lastDetailData || {});
        else renderPassengers(lastDetailData || {});
      });
    }

    if(saveBtn){
      saveBtn.addEventListener("click", saveDestinationChange);
    }
  }

  async function saveDestinationChange(){
    const seatNo = this.getAttribute("data-seat-no") || "";
    const select = document.getElementById("sheetNewToStop");
    const toStop = select ? select.value : "";

    if(!seatNo || !toStop){
      renderEmpty("Koltuk veya durak bilgisi eksik.");
      return;
    }

    this.disabled = true;
    this.textContent = "Kaydediliyor...";

    try{
      const headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"
      };

      if(csrfToken){
        headers["X-CSRFToken"] = csrfToken;
        headers["X-CSRF-Token"] = csrfToken;
      }

      const res = await fetch("/api/live-seat-destination", {
        method: "POST",
        headers,
        body: JSON.stringify({
          seat_no: seatNo,
          to_stop: toStop
        })
      });

      const data = await res.json();

      if(!data.ok){
        this.disabled = false;
        this.textContent = "Kaydet";
        alert(data.error || "İniş durağı değiştirilemedi.");
        return;
      }

      titleEl.textContent = "Güncellendi";
      subEl.textContent = data.message || "İniş durağı güncellendi.";
      bodyEl.innerHTML = `
        <div class="sheet-empty">
          ${escapeHtml(data.message || "İniş durağı güncellendi.")}
          <br><br>
          Ekran yenileniyor...
        </div>
      `;

      setTimeout(function(){
        window.location.reload();
      }, 650);

    }catch(err){
      console.error("destination change error", err);
      this.disabled = false;
      this.textContent = "Kaydet";
      alert("Bağlantı hatası. İniş durağı değiştirilemedi.");
    }
  }



  function askLiveOffloadConfirm(passenger){
    return new Promise(resolve => {
      const bag = Number(passenger.bag_count || 0);
      const seatNo = passenger.seat_no || "-";
      const routeText = `${passenger.from_stop || "Biniş yok"} → ${passenger.to_stop || currentStopName() || "İniş yok"}`;

      kickerEl.textContent = "İndirme onayı";
      titleEl.textContent = `Koltuk ${seatNo}`;
      subEl.textContent = "Yolcu indirilsin mi?";

      bodyEl.innerHTML = `
        <div class="sheet-confirm-wrap">
          <div class="sheet-confirm-card">
            <div class="sheet-confirm-title">Koltuk ${escapeHtml(seatNo)} indirilsin mi?</div>
            <div class="sheet-confirm-sub">
              ${escapeHtml(routeText)}
              <br>
              ${bag > 0 ? `🧳 ${bag} bagaj teslim edildi sayılıp temizlenecek.` : "🧳 Bagaj yok."}
            </div>
          </div>

          <div class="sheet-confirm-warning">
            <span>⚠️</span>
            <span>Bu işlem koltuğu boşaltır. Yolcu artık canlı durak listesinde görünmez.</span>
          </div>

          <div class="sheet-confirm-actions">
            <button class="sheet-confirm-cancel" type="button" id="sheetConfirmCancel">Vazgeç</button>
            <button class="sheet-confirm-ok" type="button" id="sheetConfirmOk">İNDİR</button>
          </div>
        </div>
      `;

      const cancelBtn = document.getElementById("sheetConfirmCancel");
      const okBtn = document.getElementById("sheetConfirmOk");

      if(cancelBtn){
        cancelBtn.addEventListener("click", function(){
          if(lastKind === "bagaj") renderBags(lastDetailData || {});
          else renderPassengers(lastDetailData || {});
          resolve(false);
        }, {once:true});
      }

      if(okBtn){
        okBtn.addEventListener("click", function(){
          resolve(true);
        }, {once:true});
      }
    });
  }


  async function offloadSeatFromSheet(seatNo){
    const passenger = findPassenger(seatNo);

    if(!passenger){
      alert("Koltuk bilgisi bulunamadı.");
      return;
    }

    const okConfirm = await askLiveOffloadConfirm(passenger);
    if(!okConfirm) return;

    try{
      const headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"
      };

      if(csrfToken){
        headers["X-CSRFToken"] = csrfToken;
        headers["X-CSRF-Token"] = csrfToken;
      }

      kickerEl.textContent = "Yolcu indiriliyor";
      titleEl.textContent = `Koltuk ${seatNo}`;
      subEl.textContent = "İşlem yapılıyor...";
      bodyEl.innerHTML = '<div class="sheet-empty">Koltuk indiriliyor...</div>';

      const res = await fetch("/api/live-seat-offload", {
        method: "POST",
        headers,
        body: JSON.stringify({
          seat_no: seatNo,
          stop: currentStopName()
        })
      });

      const data = await res.json();

      if(!data.ok){
        titleEl.textContent = "İşlem yapılamadı";
        subEl.textContent = "Koltuk indirilemedi.";
        renderEmpty(data.error || "Bir hata oluştu.");
        return;
      }

      titleEl.textContent = "İndirildi";
      subEl.textContent = data.message || `Koltuk ${seatNo} indirildi.`;

      bodyEl.innerHTML = `
        <div class="sheet-empty">
          ${escapeHtml(data.message || `Koltuk ${seatNo} indirildi.`)}
          ${Number(data.bag_deleted || 0) > 0 ? `<br><br>🧳 ${Number(data.bag_deleted || 0)} bagaj kaydı temizlendi.` : ""}
          <br><br>
          Ekran yenileniyor...
        </div>
      `;

      setTimeout(function(){
        window.location.reload();
      }, 650);

    }catch(err){
      console.error("live seat offload error", err);
      titleEl.textContent = "Bağlantı hatası";
      subEl.textContent = "İndirme işlemi tamamlanamadı.";
      renderEmpty("Bağlantı hatası. Koltuk indirilemedi.");
    }
  }



  function askBulkOffloadConfirm(data){
    return new Promise(resolve => {
      const passengers = Array.isArray(data.passengers) ? data.passengers : [];
      const stop = data.stop || currentStopName() || "seçili durak";
      const seats = passengers.map(p => p.seat_no).join(", ");
      const bagTotal = passengers.reduce((sum, p) => sum + Number(p.bag_count || 0), 0);

      kickerEl.textContent = "Toplu indirme onayı";
      titleEl.textContent = `${stop} durağı`;
      subEl.textContent = `${passengers.length} yolcu indirilsin mi?`;

      bodyEl.innerHTML = `
        <div class="sheet-confirm-wrap">
          <div class="sheet-confirm-card">
            <div class="sheet-confirm-title">${escapeHtml(stop)} durağındaki yolcular indirilsin mi?</div>
            <div class="sheet-confirm-sub">
              Koltuklar: ${escapeHtml(seats || "-")}
              <br>
              ${bagTotal > 0 ? `🧳 Toplam ${bagTotal} bagaj teslim edildi sayılıp temizlenecek.` : "🧳 Bagaj görünmüyor."}
            </div>
          </div>

          <div class="sheet-confirm-warning">
            <span>⚠️</span>
            <span>Bu işlem listedeki tüm yolcuları indirir ve koltukları boşaltır.</span>
          </div>

          <div class="sheet-confirm-actions">
            <button class="sheet-confirm-cancel" type="button" id="sheetBulkCancel">Vazgeç</button>
            <button class="sheet-confirm-ok" type="button" id="sheetBulkOk">TOPLU İNDİR</button>
          </div>
        </div>
      `;

      const cancelBtn = document.getElementById("sheetBulkCancel");
      const okBtn = document.getElementById("sheetBulkOk");

      if(cancelBtn){
        cancelBtn.addEventListener("click", function(){
          renderPassengers(lastDetailData || {});
          resolve(false);
        }, {once:true});
      }

      if(okBtn){
        okBtn.addEventListener("click", function(){
          resolve(true);
        }, {once:true});
      }
    });
  }

  async function bulkOffloadCurrentStop(){
    const data = lastDetailData || {};
    const passengers = Array.isArray(data.passengers) ? data.passengers : [];

    if(!passengers.length){
      renderEmpty("Bu durakta indirilecek yolcu bulunmuyor.");
      return;
    }

    const okConfirm = await askBulkOffloadConfirm(data);
    if(!okConfirm) return;

    try{
      const headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"
      };

      if(csrfToken){
        headers["X-CSRFToken"] = csrfToken;
        headers["X-CSRF-Token"] = csrfToken;
      }

      kickerEl.textContent = "Toplu indirme";
      titleEl.textContent = data.stop || currentStopName() || "Durak";
      subEl.textContent = "İşlem yapılıyor...";
      bodyEl.innerHTML = '<div class="sheet-empty">Yolcular indiriliyor...</div>';

      const res = await fetch("/api/live-stop-offload", {
        method: "POST",
        headers,
        body: JSON.stringify({
          stop: data.stop || currentStopName()
        })
      });

      const j = await res.json();

      if(!j.ok){
        titleEl.textContent = "İşlem yapılamadı";
        subEl.textContent = "Toplu indirme başarısız.";
        renderEmpty(j.error || "Bir hata oluştu.");
        return;
      }

      titleEl.textContent = "İndirildi";
      subEl.textContent = j.message || "Yolcular indirildi.";

      bodyEl.innerHTML = `
        <div class="sheet-empty">
          ${escapeHtml(j.message || "Yolcular indirildi.")}
          <br><br>
          Koltuklar: ${escapeHtml((j.deleted || []).join(", "))}
          ${Number(j.bag_deleted || 0) > 0 ? `<br><br>🧳 ${Number(j.bag_deleted || 0)} bagaj kaydı temizlendi.` : ""}
          <br><br>
          Ekran yenileniyor...
        </div>
      `;

      setTimeout(function(){
        window.location.reload();
      }, 750);

    }catch(err){
      console.error("bulk stop offload error", err);
      titleEl.textContent = "Bağlantı hatası";
      subEl.textContent = "Toplu indirme tamamlanamadı.";
      renderEmpty("Bağlantı hatası. Yolcular indirilemedi.");
    }
  }




  function renderBagPhotoGallery(photos){
    photos = Array.isArray(photos) ? photos : [];

    if(!photos.length){
      return `
        <div class="sheet-bag-no-photo">
          Bu koltuk için görünür bagaj fotoğrafı bulunamadı.
        </div>
      `;
    }

    return `
      <div class="sheet-bag-gallery">
        <div class="sheet-bag-gallery-head">
          <div class="sheet-bag-gallery-title">Bagaj Fotoğrafları</div>
          <div class="sheet-bag-gallery-count">${photos.length} fotoğraf</div>
        </div>

        <div class="sheet-bag-photo-grid">
          ${photos.map((photo, idx) => `
            <a class="sheet-bag-photo"
               href="${escapeHtml(photo.url || photo.thumb_url || "#")}"
               target="_blank"
               rel="noopener"
               title="Fotoğrafı aç">
              <img src="${escapeHtml(photo.thumb_url || photo.url || "")}" alt="Bagaj fotoğrafı ${idx + 1}" loading="lazy">
              <span class="sheet-bag-photo-badge">${idx + 1} / ${photos.length}</span>
              <span class="sheet-bag-photo-side">${escapeHtml(photo.side_label || "Bagaj")}</span>
              <span class="sheet-bag-photo-open">Aç</span>
            </a>
          `).join("")}
        </div>
      </div>
    `;
  }



  async function renderConsignmentDetail(cid){
    if(!cid){
      renderEmpty("Emanet bilgisi bulunamadı.");
      return;
    }

    kickerEl.textContent = "Emanet detayı";
    titleEl.textContent = "Yükleniyor...";
    subEl.textContent = "Emanet bilgisi alınıyor...";
    bodyEl.innerHTML = '<div class="sheet-empty">Yükleniyor...</div>';

    try{
      const res = await fetch(`/api/live-consignment-detail/${encodeURIComponent(cid)}?_=${Date.now()}`, {
        headers: {"Accept":"application/json"}
      });

      const data = await res.json();

      if(!data.ok){
        titleEl.textContent = "Bulunamadı";
        subEl.textContent = "Emanet bilgisi alınamadı.";
        renderEmpty(data.error || "Bir hata oluştu.");
        return;
      }

      const item = data.item || {};
      const photos = Array.isArray(item.photos) ? item.photos : [];

      kickerEl.textContent = "Emanet detayı";
      titleEl.textContent = item.code || `Emanet ${item.id || ""}`;
      subEl.textContent = item.item_name || "Emanet / Kargo";

      bodyEl.innerHTML = `
        <div class="sheet-cargo-detail-card">
          <div class="sheet-cargo-detail-title">${escapeHtml(item.item_name || "Emanet / Kargo")}</div>
          <div class="sheet-cargo-detail-sub">Kod: ${escapeHtml(item.code || "-")}</div>

          <div class="sheet-cargo-detail-grid">
            <div class="sheet-cargo-line"><span>Teslim durağı</span><b>${escapeHtml(item.to_stop || "-")}</b></div>
            <div class="sheet-cargo-line"><span>Alıcı</span><b>${escapeHtml(item.to_name || "-")}</b></div>
            <div class="sheet-cargo-line"><span>Alıcı telefon</span><b>${escapeHtml(item.to_phone || "-")}</b></div>
            <div class="sheet-cargo-line"><span>Gönderen</span><b>${escapeHtml(item.from_name || "-")}</b></div>
            <div class="sheet-cargo-line"><span>Ücret</span><b>${Number(item.amount || 0).toFixed(2)} ₺</b></div>
            <div class="sheet-cargo-line"><span>Ödeme</span><b>${escapeHtml(item.payment || "-")}</b></div>
            <div class="sheet-cargo-line"><span>Durum</span><b>${escapeHtml(item.status || "-")}</b></div>
            ${item.notes ? `<div class="sheet-cargo-line"><span>Not</span><b>${escapeHtml(item.notes)}</b></div>` : ""}
          </div>
        </div>

        ${photos.length ? `
          <div class="sheet-section-title">
            <span>Fotoğraflar</span>
            <span class="sheet-section-count">${photos.length} foto</span>
          </div>
          <div class="sheet-cargo-photo-grid">
            ${photos.map((ph, idx) => `
              <a class="sheet-cargo-photo" href="${escapeHtml(ph.url || "#")}" data-cargo-photo="1">
                <img src="${escapeHtml(ph.url || "")}" alt="Emanet fotoğrafı ${idx + 1}">
                <span class="sheet-bag-photo-badge">${idx + 1} / ${photos.length}</span>
                <span class="sheet-bag-photo-side">Emanet</span>
                <span class="sheet-bag-photo-open">Aç</span>
              </a>
            `).join("")}
          </div>
        ` : ""}

        <button class="sheet-cargo-back" type="button" id="sheetCargoBackBtn">Listeye Dön</button>
      `;

      const backBtn = document.getElementById("sheetCargoBackBtn");
      if(backBtn){
        backBtn.addEventListener("click", function(){
          renderBags(lastDetailData || {});
        }, {once:true});
      }

    }catch(err){
      console.error("consignment detail error", err);
      titleEl.textContent = "Bağlantı hatası";
      subEl.textContent = "Emanet detayı alınamadı.";
      renderEmpty("Bağlantı hatası. Emanet detayı alınamadı.");
    }
  }

  function askConsignmentDeliverConfirm(cid){
    const consignments = lastDetailData && Array.isArray(lastDetailData.consignments)
      ? lastDetailData.consignments
      : [];

    const item = consignments.find(x => String(x.id || "") === String(cid || "")) || {};

    return new Promise(resolve => {
      kickerEl.textContent = "Teslim onayı";
      titleEl.textContent = item.code || "Emanet";
      subEl.textContent = "Emanet teslim edilsin mi?";

      bodyEl.innerHTML = `
        <div class="sheet-confirm-wrap">
          <div class="sheet-confirm-card">
            <div class="sheet-confirm-title">${escapeHtml(item.item_label || "Emanet / Kargo")} teslim edilsin mi?</div>
            <div class="sheet-confirm-sub">
              Kod: ${escapeHtml(item.code || "-")}
              <br>
              Teslim durağı: ${escapeHtml(item.stop_name || currentStopName() || "-")}
              ${item.receiver ? `<br>Alıcı: ${escapeHtml(item.receiver)}` : ""}
            </div>
          </div>

          <div class="sheet-confirm-warning">
            <span>⚠️</span>
            <span>Bu işlem emaneti teslim edildi olarak işaretler.</span>
          </div>

          <div class="sheet-confirm-actions">
            <button class="sheet-confirm-cancel" type="button" id="sheetCargoCancel">Vazgeç</button>
            <button class="sheet-confirm-ok" type="button" id="sheetCargoOk">TESLİM ET</button>
          </div>
        </div>
      `;

      const cancelBtn = document.getElementById("sheetCargoCancel");
      const okBtn = document.getElementById("sheetCargoOk");

      if(cancelBtn){
        cancelBtn.addEventListener("click", function(){
          renderBags(lastDetailData || {});
          resolve(false);
        }, {once:true});
      }

      if(okBtn){
        okBtn.addEventListener("click", function(){
          resolve(true);
        }, {once:true});
      }
    });
  }

  async function deliverConsignmentFromSheet(cid){
    if(!cid){
      renderEmpty("Emanet bilgisi bulunamadı.");
      return;
    }

    const okConfirm = await askConsignmentDeliverConfirm(cid);
    if(!okConfirm) return;

    try{
      const headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"
      };

      if(csrfToken){
        headers["X-CSRFToken"] = csrfToken;
        headers["X-CSRF-Token"] = csrfToken;
      }

      kickerEl.textContent = "Emanet teslimi";
      titleEl.textContent = "Teslim ediliyor...";
      subEl.textContent = "İşlem yapılıyor...";
      bodyEl.innerHTML = '<div class="sheet-empty">Emanet teslim ediliyor...</div>';

      const res = await fetch(`/api/live-consignment-deliver/${encodeURIComponent(cid)}`, {
        method: "POST",
        headers,
        body: JSON.stringify({})
      });

      const data = await res.json();

      if(!data.ok){
        titleEl.textContent = "Teslim edilemedi";
        subEl.textContent = "İşlem başarısız.";
        renderEmpty(data.error || "Bir hata oluştu.");
        return;
      }

      titleEl.textContent = "Teslim edildi";
      subEl.textContent = data.message || "Emanet teslim edildi.";
      bodyEl.innerHTML = `
        <div class="sheet-empty">
          ${escapeHtml(data.message || "Emanet teslim edildi.")}
          <br><br>
          Ekran yenileniyor...
        </div>
      `;

      setTimeout(function(){
        window.location.reload();
      }, 700);

    }catch(err){
      console.error("consignment deliver error", err);
      titleEl.textContent = "Bağlantı hatası";
      subEl.textContent = "Emanet teslim edilemedi.";
      renderEmpty("Bağlantı hatası. Emanet teslim edilemedi.");
    }
  }


  async function renderSeatBagDetail(seatNo){
    if(!seatNo){
      renderEmpty("Koltuk bilgisi bulunamadı.");
      return;
    }

    kickerEl.textContent = "Detay";
    titleEl.textContent = `Koltuk ${seatNo}`;
    subEl.textContent = "Bagaj konumu yükleniyor...";
    bodyEl.innerHTML = '<div class="sheet-empty">Bagaj bilgisi alınıyor...</div>';

    try{
      const res = await fetch(`/api/live-seat-bag-detail?seat_no=${encodeURIComponent(seatNo)}&_=${Date.now()}`, {
        headers: {"Accept":"application/json"}
      });

      const data = await res.json();

      if(!data.ok){
        subEl.textContent = "Bagaj bilgisi alınamadı.";
        renderEmpty(data.error || "Bir hata oluştu.");
        return;
      }

      const locations = Array.isArray(data.locations) ? data.locations : [];
      subEl.textContent = `${Number(data.total || 0)} bagaj`;

      bodyEl.innerHTML = `
        <div class="sheet-change-card" style="margin:14px 14px 0;">
          <div class="sheet-change-title">Koltuk ${escapeHtml(data.seat_no || seatNo)}</div>
          <div class="sheet-change-sub">
            ${escapeHtml((data.from_stop || "Biniş yok") + " → " + (data.to_stop || "İniş yok"))}
            ${data.passenger_name ? "<br>Yolcu: " + escapeHtml(data.passenger_name) : ""}
          </div>
        </div>

        <div class="sheet-bag-grid">
          ${locations.map(loc => `
            <div class="sheet-bag-cell ${Number(loc.count || 0) > 0 ? "active" : ""}">
              <div class="sheet-bag-label">${escapeHtml(loc.label)}</div>
              <div class="sheet-bag-count">${Number(loc.count || 0)}</div>
            </div>
          `).join("")}
        </div>

        <div class="sheet-bag-info">
          Toplam: <b>${Number(data.total || 0)}</b> bagaj.
          <br>
          Fotoğraf kaydı: <b>${Array.isArray(data.photos) && data.photos.length ? "Var" : "Yok"}</b>
        </div>

        ${renderBagPhotoGallery(data.photos)}

        <button class="sheet-bag-back" type="button" id="sheetBagBackBtn">Listeye Dön</button>
      `;

      const backBtn = document.getElementById("sheetBagBackBtn");
      if(backBtn){
        backBtn.addEventListener("click", function(){
          if(lastKind === "bagaj") renderBags(lastDetailData || {});
          else renderPassengers(lastDetailData || {});
        }, {once:true});
      }

    }catch(err){
      console.error("seat bag detail error", err);
      subEl.textContent = "Bağlantı hatası.";
      renderEmpty("Detay alınamadı.");
    }
  }



  function sheetGenderClass(p){
    const g = String((p && p.gender) || "").trim().toLowerCase();

    if(g === "bay" || g === "erkek" || g === "male"){
      return "gender-male";
    }

    if(g === "bayan" || g === "kadın" || g === "kadin" || g === "female"){
      return "gender-female";
    }

    return "gender-neutral";
  }

  function sheetGenderLabel(p){
    const g = String((p && p.gender) || "").trim().toLowerCase();

    if(g === "bay" || g === "erkek" || g === "male"){
      return "Bay";
    }

    if(g === "bayan" || g === "kadın" || g === "kadin" || g === "female"){
      return "Bayan";
    }

    return "";
  }

  function sheetGenderChip(p){
    const label = sheetGenderLabel(p);
    return label ? `<span class="sheet-gender-chip">${escapeHtml(label)}</span>` : "";
  }


  function renderPassengers(data){
    lastDetailData = data;
    const passengers = Array.isArray(data.passengers) ? data.passengers : [];

    if(!passengers.length){
      renderEmpty("Bu durakta inecek yolcu bulunmuyor.");
      return;
    }

    bodyEl.innerHTML = `
      <div class="sheet-bulk-bar">
        <button class="sheet-bulk-btn" type="button" id="sheetBulkOffloadBtn">TOPLU İNDİR</button>
      </div>

      <div class="sheet-list">
        ${passengers.map(p => {
          const bag = Number(p.bag_count || 0);
          const name = text(p.passenger_name || "").trim();
          const route = `${p.from_stop || "Biniş yok"} → ${p.to_stop || data.stop || "İniş yok"}`;

          return `
            <div class="sheet-seat-row ${sheetGenderClass(p)}">
              <div class="sheet-seat-no">${escapeHtml(p.seat_no || "-")}</div>

              <div class="sheet-seat-main">
                <div class="sheet-seat-title">
                  Koltuk ${escapeHtml(p.seat_no || "-")}${sheetGenderChip(p)}${name ? " • " + escapeHtml(name) : ""}
                </div>
                <div class="sheet-seat-route">${escapeHtml(route)}</div>
              </div>

              <div class="sheet-seat-extra">
                ${bag ? `<button class="sheet-bag-detail-btn" type="button" data-bag-seat="${escapeHtml(p.seat_no || "")}">🧳 ${bag} bagaj</button>` : `<span class="sheet-badge">🧳 Bagaj yok</span>`}
                ${Number(p.service || 0) ? '<span class="sheet-badge">🚌 Servis</span>' : ''}
                <button class="sheet-action-btn" type="button" data-change-seat="${escapeHtml(p.seat_no || "")}">
                  Durağı Değiştir
                </button>
                <button class="sheet-offload-btn ${bag ? "danger" : ""}" type="button" data-offload-seat="${escapeHtml(p.seat_no || "")}">
                  İNDİR
                </button>
              </div>
            </div>
          `;
        }).join("")}
      </div>
    `;
  }

  function renderBags(data){
    lastDetailData = data;

    const passengers = Array.isArray(data.passengers) ? data.passengers : [];
    const bagSeats = passengers.filter(p => Number(p.bag_count || 0) > 0);
    const consignments = Array.isArray(data.consignments) ? data.consignments : [];

    if(!bagSeats.length && !consignments.length){
      renderEmpty("Bu durakta indirilecek bagaj veya emanet görünmüyor.");
      return;
    }

    const rightTotal = bagSeats.reduce((sum, p) => sum + Number(p.bag_right || 0), 0);
    const leftFrontTotal = bagSeats.reduce((sum, p) => sum + Number(p.bag_left_front || 0), 0);
    const leftBackTotal = bagSeats.reduce((sum, p) => sum + Number(p.bag_left_back || 0), 0);
    const bagTotal = rightTotal + leftFrontTotal + leftBackTotal;

    subEl.textContent = `${bagTotal} bagaj • ${consignments.length} emanet`;

    function locLine(p){
      const parts = [];
      const r = Number(p.bag_right || 0);
      const lf = Number(p.bag_left_front || 0);
      const lb = Number(p.bag_left_back || 0);

      if(r > 0) parts.push(`Sağ göz ${r}`);
      if(lf > 0) parts.push(`Sol ön ${lf}`);
      if(lb > 0) parts.push(`Sol arka ${lb}`);

      return parts.length ? parts.join(" • ") : "Konum bilgisi yok";
    }

    const seatHtml = bagSeats.map(p => {
      const bag = Number(p.bag_count || 0);
      const photos = Number(p.bag_photo_count || 0);
      const route = `${p.from_stop || "Biniş yok"} → ${p.to_stop || data.stop || "İniş yok"}`;

      return `
        <div class="sheet-bag-item">
          <div class="sheet-bag-item-head">
            <div class="sheet-bag-icon">🧳</div>

            <div>
              <div class="sheet-bag-item-title">${bag} bagaj</div>
              <div class="sheet-bag-item-sub">${escapeHtml(locLine(p))}</div>
            </div>
          </div>

          <div class="sheet-bag-mini">
            Koltuk ${escapeHtml(p.seat_no || "-")} • ${escapeHtml(route)}
            <br>
            Fotoğraf: ${photos > 0 ? photos + " adet" : "Yok"}
          </div>

          <div class="sheet-bag-actions">
            <button class="sheet-bag-detail-open" type="button" data-bag-seat="${escapeHtml(p.seat_no || "")}">
              Bagajı Aç
            </button>

            <button class="sheet-action-btn" type="button" data-change-seat="${escapeHtml(p.seat_no || "")}">
              Durağı Değiştir
            </button>

            <button class="sheet-offload-btn danger" type="button" data-offload-seat="${escapeHtml(p.seat_no || "")}">
              İNDİR
            </button>
          </div>
        </div>
      `;
    }).join("");

    const consHtml = consignments.map((c, idx) => {
      const code = c.code || `Emanet ${idx + 1}`;
      const item = c.item_label || "Emanet / Kargo";
      const receiver = c.receiver || "";
      const stop = c.stop_name || data.stop || currentStopName() || "";

      return `
        <div class="sheet-cargo-item">
          <div class="sheet-cargo-head">
            <div class="sheet-cargo-icon">📦</div>

            <div>
              <div class="sheet-cargo-title">${escapeHtml(item)}</div>
              <div class="sheet-cargo-sub">Kod: ${escapeHtml(code)}</div>
            </div>
          </div>

          <div class="sheet-cargo-meta">
            Teslim durağı: ${escapeHtml(stop || "-")}
            ${receiver ? `<br>Alıcı: ${escapeHtml(receiver)}` : ""}
          </div>

          <div class="sheet-cargo-actions">
            <button class="sheet-cargo-btn" type="button" data-cargo-detail="${escapeHtml(c.id || "")}">
              Detay
            </button>
            <button class="sheet-cargo-btn" type="button" data-cargo-deliver="${escapeHtml(c.id || "")}">
              Teslim Et
            </button>
          </div>
        </div>
      `;
    }).join("");

    bodyEl.innerHTML = `
      ${bagSeats.length ? `
        <div class="sheet-bag-stop-summary">
          <div class="sheet-bag-stop-cell ${rightTotal > 0 ? "active" : ""}">
            <small>Sağ göz</small>
            <b>${rightTotal}</b>
          </div>

          <div class="sheet-bag-stop-cell ${leftFrontTotal > 0 ? "active" : ""}">
            <small>Sol ön</small>
            <b>${leftFrontTotal}</b>
          </div>

          <div class="sheet-bag-stop-cell ${leftBackTotal > 0 ? "active" : ""}">
            <small>Sol arka</small>
            <b>${leftBackTotal}</b>
          </div>
        </div>
      ` : ""}

      ${bagSeats.length ? `
        <div class="sheet-section-title">
          <span>Yolcu Bagajları</span>
          <span class="sheet-section-count">${bagTotal} bagaj</span>
        </div>

        <div class="sheet-list">
          ${seatHtml}
        </div>
      ` : ""}

      ${consignments.length ? `
        <div class="sheet-section-title">
          <span>Emanet / Kargo</span>
          <span class="sheet-section-count">${consignments.length} emanet</span>
        </div>

        <div class="sheet-list">
          ${consHtml}
        </div>
      ` : ""}
    `;
  }



  function stopSummaryBagLocationText(p){
    const parts = [];

    const r = Number(p.bag_right || 0);
    const lf = Number(p.bag_left_front || 0);
    const lb = Number(p.bag_left_back || 0);

    if(r > 0) parts.push(`Sağ göz ${r}`);
    if(lf > 0) parts.push(`Sol ön ${lf}`);
    if(lb > 0) parts.push(`Sol arka ${lb}`);

    return parts.length ? parts.join(" • ") : "Konum bilgisi yok";
  }

  function stopSummaryBagSpeechText(p){
    const parts = [];

    const r = Number(p.bag_right || 0);
    const lf = Number(p.bag_left_front || 0);
    const lb = Number(p.bag_left_back || 0);

    if(r > 0) parts.push(`sağ gözde ${r}`);
    if(lf > 0) parts.push(`sol önde ${lf}`);
    if(lb > 0) parts.push(`sol arkada ${lb}`);

    return parts.length ? parts.join(", ") : "konum bilgisi yok";
  }


  function passengerGenderCounts(passengers){
    let male = 0;
    let female = 0;
    let unknown = 0;

    passengers.forEach(p => {
      const g = String((p && p.gender) || "").trim().toLowerCase();

      if(g === "bay" || g === "erkek" || g === "male") male++;
      else if(g === "bayan" || g === "kadın" || g === "kadin" || g === "female") female++;
      else unknown++;
    });

    return {male, female, unknown};
  }

  function buildStopSummarySentence(data){
    const passengers = Array.isArray(data.passengers) ? data.passengers : [];
    const consignments = Array.isArray(data.consignments) ? data.consignments : [];
    const g = passengerGenderCounts(passengers);

    const seats = passengers.map(p => p.seat_no).filter(Boolean).join(", ");
    const bagTotal = Number(data.bag_total || 0);
    const consCount = consignments.length;

    const parts = [];

    parts.push(`${data.stop || currentStopName() || "Bu"} durağında ${passengers.length} yolcu inecek.`);

    if(passengers.length){
      const genderParts = [];
      if(g.male) genderParts.push(`${g.male} bay`);
      if(g.female) genderParts.push(`${g.female} bayan`);
      if(g.unknown) genderParts.push(`${g.unknown} belirsiz`);
      if(genderParts.length) parts.push(genderParts.join(", ") + ".");
      if(seats) parts.push(`Koltuklar: ${seats}.`);
    }

    if(bagTotal > 0){
      const bagDetails = passengers
        .filter(p => Number(p.bag_count || 0) > 0)
        .map(p => `Koltuk ${p.seat_no}: ${Number(p.bag_count || 0)} bagaj, ${stopSummaryBagSpeechText(p)}`);

      parts.push(`${bagTotal} bagaj var.`);
      if(bagDetails.length){
        parts.push(`Bagaj uyarısı: ${bagDetails.join(". ")}.`);
      }
    }

    if(consCount > 0){
      parts.push(`${consCount} emanet teslim var.`);
    }

    return parts.join(" ");
  }

  function speakStopSummary(data){
    const msg = buildStopSummarySentence(data);

    function setSpeakState(text){
      try{
        const btn = document.getElementById("sheetSummarySpeak");
        if(!btn) return;

        if(!btn.dataset.originalText){
          btn.dataset.originalText = btn.textContent || "Sesli Oku";
        }

        btn.textContent = text || btn.dataset.originalText || "Sesli Oku";

        setTimeout(function(){
          btn.textContent = btn.dataset.originalText || "Sesli Oku";
        }, 900);
      }catch(_){}
    }

    if(!msg){
      setSpeakState("Metin yok");
      return;
    }

    // 1) Ortak ses köprüsü: APK'da AndroidTTS, tarayıcıda speechSynthesis kullanır.
    try{
      if(window.SeatsSpeak && typeof window.SeatsSpeak === "function"){
        window.SeatsSpeak(msg, { force:true });
        setSpeakState("Okunuyor...");
        return;
      }
    }catch(err){
      console.warn("SeatsSpeak summary error", err);
    }

    // 2) APK native TTS köprüsü
    try{
      if(window.AndroidTTS && typeof window.AndroidTTS.speak === "function"){
        if(typeof window.AndroidTTS.stop === "function"){
          try{ window.AndroidTTS.stop(); }catch(_){}
        }

        window.AndroidTTS.speak(msg);
        setSpeakState("Okunuyor...");
        return;
      }
    }catch(err){
      console.warn("AndroidTTS summary error", err);
    }

    // 3) Tarayıcı fallback
    try{
      if(window.speechSynthesis && window.SpeechSynthesisUtterance){
        window.speechSynthesis.cancel();

        const u = new SpeechSynthesisUtterance(msg);
        u.lang = "tr-TR";
        u.rate = 0.95;
        u.pitch = 1;

        const voices = window.speechSynthesis.getVoices ? window.speechSynthesis.getVoices() : [];
        const trVoice = voices.find(v => String(v.lang || "").toLowerCase().startsWith("tr"));
        if(trVoice) u.voice = trVoice;

        window.speechSynthesis.speak(u);
        setSpeakState("Okunuyor...");
        return;
      }
    }catch(err){
      console.error("summary speak error", err);
    }

    setSpeakState("Ses yok");
  }

  async function completeStopFromSummary(data){
    const stop = (data && data.stop) || currentStopName();

    if(!stop){
      renderEmpty("Durak bilgisi bulunamadı.");
      return;
    }

    kickerEl.textContent = "Durak kontrolü";
    titleEl.textContent = `${stop} durağı`;
    subEl.textContent = "Eksik işlem kontrol ediliyor...";
    bodyEl.innerHTML = '<div class="sheet-empty">Durak işlemleri kontrol ediliyor...</div>';

    try{
      const headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"
      };

      if(csrfToken){
        headers["X-CSRFToken"] = csrfToken;
        headers["X-CSRF-Token"] = csrfToken;
      }

      const res = await fetch("/api/live-stop-complete", {
        method:"POST",
        headers,
        body:JSON.stringify({ stop })
      });

      const j = await res.json();

      if(!j.ok){
        subEl.textContent = "Kontrol yapılamadı.";
        renderEmpty(j.error || "Bir hata oluştu.");
        return;
      }

      if(j.completed){
        kickerEl.textContent = "Durak tamamlandı";
        titleEl.textContent = `${j.stop || stop}`;
        subEl.textContent = "Bu durakta bekleyen işlem kalmadı.";

        bodyEl.innerHTML = `
          <div class="sheet-complete-success">
            ✅ ${escapeHtml(j.message || "Durak tamamlandı.")}
          </div>

          <div class="sheet-complete-actions">
            <button type="button" id="completeBackSummary">Özete Dön</button>
            <button type="button" id="completeCloseSheet">Kapat</button>
          </div>
        `;

        document.getElementById("completeBackSummary")?.addEventListener("click", () => {
          renderStopSummary(data);
        });

        document.getElementById("completeCloseSheet")?.addEventListener("click", () => {
          closeSheet();
          setTimeout(() => window.location.reload(), 250);
        });

        return;
      }

      const p = j.pending || {};

      kickerEl.textContent = "Eksik işlem var";
      titleEl.textContent = `${j.stop || stop}`;
      subEl.textContent = "Durak tamamlanamaz.";

      bodyEl.innerHTML = `
        <div class="sheet-incomplete-card">
          <div class="sheet-incomplete-title">${escapeHtml(j.stop || stop)} tamamlanamaz.</div>
          <div class="sheet-incomplete-sub">
            Önce kalan yolcuları indir. Bagaj veya emanet varsa onları da tamamla.
          </div>
        </div>

        <div class="sheet-pending-grid">
          <div class="sheet-pending-cell">
            <b>${Number(p.seat_count || 0)}</b>
            <span>İnecek yolcu</span>
          </div>

          <div class="sheet-pending-cell">
            <b>${Number(p.bag_count || 0)}</b>
            <span>Bagaj</span>
          </div>

          <div class="sheet-pending-cell">
            <b>${Number(p.consignment_count || 0)}</b>
            <span>Emanet</span>
          </div>

          <div class="sheet-pending-cell">
            <b>${Number(p.standing_count || 0)}</b>
            <span>Ayakta</span>
          </div>
        </div>

        <div class="sheet-summary-actions">
          <button class="sheet-summary-action" type="button" id="pendingPassengersBtn">Yolcu Listesi</button>
          <button class="sheet-summary-action bag" type="button" id="pendingBagsBtn">Bagaj Detayı</button>
        </div>
      `;

      document.getElementById("pendingPassengersBtn")?.addEventListener("click", () => {
        lastKind = "offload";
        kickerEl.textContent = "İnecek yolcular";
        titleEl.textContent = `${data.stop || currentStopName() || "Durak"} durağı`;
        subEl.textContent = `${Number(data.off_count || 0)} yolcu inecek`;
        renderPassengers(data);
      });

      document.getElementById("pendingBagsBtn")?.addEventListener("click", () => {
        lastKind = "bagaj";
        kickerEl.textContent = "Detay";
        titleEl.textContent = `${data.stop || currentStopName() || "Durak"} durağı`;
        subEl.textContent = `${Number(data.bag_total || 0)} bagaj / emanet`;
        renderBags(data);
      });

    }catch(err){
      console.error("complete stop error", err);
      subEl.textContent = "Bağlantı hatası.";
      renderEmpty("Durak kontrolü yapılamadı.");
    }
  }


  function renderStopSummary(data){
    lastDetailData = data;
    lastKind = "summary";

    const passengers = Array.isArray(data.passengers) ? data.passengers : [];
    const consignments = Array.isArray(data.consignments) ? data.consignments : [];
    const g = passengerGenderCounts(passengers);

    const seats = passengers.map(p => p.seat_no).filter(Boolean);
    const bagTotal = Number(data.bag_total || 0);
    const consCount = consignments.length;

    kickerEl.textContent = "Durak özeti";
    titleEl.textContent = `${data.stop || currentStopName() || "Durak"} durağı`;
    subEl.textContent = `${passengers.length} yolcu • ${bagTotal} bagaj • ${consCount} emanet`;

    const bagRows = passengers
      .filter(p => Number(p.bag_count || 0) > 0)
      .map(p => `Koltuk ${p.seat_no}: ${Number(p.bag_count || 0)} bagaj · ${stopSummaryBagLocationText(p)}`)
      .join(" • ");

    const consRows = consignments
      .map(c => `${c.code || "Emanet"}${c.item_label ? " · " + c.item_label : ""}`)
      .join(" • ");

    bodyEl.innerHTML = `
      <div class="sheet-summary-grid">
        <div class="sheet-summary-cell">
          <strong>${passengers.length}</strong>
          <span>İnecek</span>
        </div>
        <div class="sheet-summary-cell">
          <strong>${bagTotal}</strong>
          <span>Bagaj</span>
        </div>
        <div class="sheet-summary-cell">
          <strong>${consCount}</strong>
          <span>Emanet</span>
        </div>
      </div>

      <div class="sheet-summary-card">
        <div class="sheet-summary-title">Yolcu dağılımı</div>
        <div class="sheet-summary-pill-row">
          <span class="sheet-summary-pill">Bay: ${g.male}</span>
          <span class="sheet-summary-pill female">Bayan: ${g.female}</span>
          ${g.unknown ? `<span class="sheet-summary-pill">Belirsiz: ${g.unknown}</span>` : ""}
        </div>
      </div>

      <div class="sheet-summary-card">
        <div class="sheet-summary-title">Koltuklar</div>
        <div class="sheet-summary-text">
          ${seats.length ? escapeHtml(seats.join(", ")) : "Bu durakta inecek yolcu görünmüyor."}
        </div>
      </div>

      <div class="sheet-summary-card">
        <div class="sheet-summary-title">Bagaj uyarısı</div>
        <div class="sheet-summary-text">
          ${bagRows ? escapeHtml(bagRows) : "Yolcu bagajı görünmüyor."}
        </div>
      </div>

      <div class="sheet-summary-card">
        <div class="sheet-summary-title">Emanet / Kargo</div>
        <div class="sheet-summary-text">
          ${consRows ? escapeHtml(consRows) : "Teslim edilecek emanet görünmüyor."}
        </div>
      </div>

      <div class="sheet-summary-actions">
        <button class="sheet-summary-action speak" type="button" id="sheetSummarySpeak">Sesli Oku</button>
        <button class="sheet-summary-action done" type="button" id="sheetSummaryComplete">Tamamla</button>
        <button class="sheet-summary-action" type="button" id="sheetSummaryPassengers">Yolcu Listesi</button>
        <button class="sheet-summary-action bag" type="button" id="sheetSummaryBags">Bagaj Detayı</button>
      </div>
    `;

    const speakBtn = document.getElementById("sheetSummarySpeak");
    const completeBtn = document.getElementById("sheetSummaryComplete");
    const passengerBtn = document.getElementById("sheetSummaryPassengers");
    const bagBtn2 = document.getElementById("sheetSummaryBags");

    if(speakBtn){
      speakBtn.addEventListener("click", function(){
        speakStopSummary(data);
      });
    }

    if(completeBtn){
      completeBtn.addEventListener("click", function(){
        completeStopFromSummary(data);
      });
    }

    if(passengerBtn){
      passengerBtn.addEventListener("click", function(){
        lastKind = "offload";
        kickerEl.textContent = "İnecek yolcular";
        titleEl.textContent = `${data.stop || currentStopName() || "Durak"} durağı`;
        subEl.textContent = `${Number(data.off_count || 0)} yolcu inecek`;
        renderPassengers(data);
      });
    }

    if(bagBtn2){
      bagBtn2.addEventListener("click", function(){
        lastKind = "bagaj";
        kickerEl.textContent = "Detay";
        titleEl.textContent = `${data.stop || currentStopName() || "Durak"} durağı`;
        subEl.textContent = `${Number(data.bag_total || 0)} bagaj / emanet`;
        renderBags(data);
      });
    }
  }

  async function loadStopSummary(){
    const stop = currentStopName();

    if(!stop || stop === "Durak seçilmedi"){
      openSheet();
      kickerEl.textContent = "Durak özeti";
      titleEl.textContent = "Durak seçilmedi";
      subEl.textContent = "Önce canlı durak belirlenmeli.";
      renderEmpty("Canlı durak bilgisi bulunamadı.");
      return;
    }

    openSheet();

    kickerEl.textContent = "Durak özeti";
    titleEl.textContent = `${stop} durağı`;
    subEl.textContent = "Yükleniyor...";
    bodyEl.innerHTML = '<div class="sheet-empty">Durak özeti hazırlanıyor...</div>';

    try{
      const res = await fetch(`/api/live-stop-detail?stop=${encodeURIComponent(stop)}&_=${Date.now()}`, {
        headers: {"Accept":"application/json"}
      });

      const data = await res.json();

      if(!data.ok){
        subEl.textContent = "Bilgi alınamadı.";
        renderEmpty(data.error || "Bir hata oluştu.");
        return;
      }

      renderStopSummary(data);

    }catch(err){
      console.error("stop summary error", err);
      subEl.textContent = "Bağlantı hatası.";
      renderEmpty("Durak özeti alınamadı.");
    }
  }


  async function loadDetail(kind){
    lastKind = kind;
    const stop = currentStopName();

    if(!stop || stop === "Durak seçilmedi"){
      openSheet();
      titleEl.textContent = "Durak seçilmedi";
      subEl.textContent = "Önce canlı durak belirlenmeli.";
      renderEmpty("Canlı durak bilgisi bulunamadı.");
      return;
    }

    openSheet();

    kickerEl.textContent = kind === "bagaj" ? "Detay" : "İnecek yolcular";
    titleEl.textContent = `${stop} durağı`;
    subEl.textContent = "Yükleniyor...";
    bodyEl.innerHTML = '<div class="sheet-empty">Yükleniyor...</div>';

    try{
      const res = await fetch(`/api/live-stop-detail?stop=${encodeURIComponent(stop)}&_=${Date.now()}`, {
        headers: {"Accept":"application/json"}
      });

      const data = await res.json();

      if(!data.ok){
        subEl.textContent = "Bilgi alınamadı.";
        renderEmpty(data.error || "Bir hata oluştu.");
        return;
      }

      lastDetailData = data;

      if(kind === "bagaj"){
        subEl.textContent = `${Number(data.bag_total || 0)} bagaj / emanet`;
        renderBags(data);
      }else{
        subEl.textContent = `${Number(data.off_count || 0)} yolcu inecek`;
        renderPassengers(data);
      }

    }catch(err){
      subEl.textContent = "Bağlantı hatası.";
      renderEmpty("Durak detayı alınamadı.");
      console.error("live stop detail error", err);
    }
  }

  function refreshMetricState(){
    const offCountEl = document.getElementById("liveOffloadCount");
    const bagCountEl = document.getElementById("liveBagajCount");

    const offN = parseInt((offCountEl && offCountEl.textContent || "0").replace(/\D+/g, "") || "0", 10);
    const bagN = parseInt((bagCountEl && bagCountEl.textContent || "0").replace(/\D+/g, "") || "0", 10);

    if(offBtn){
      offBtn.classList.toggle("has-work", offN > 0);
      offBtn.classList.toggle("is-empty", offN <= 0);
    }

    if(bagBtn){
      bagBtn.classList.toggle("has-work", bagN > 0);
      bagBtn.classList.toggle("is-empty", bagN <= 0);
    }
  }


  const liveCard = document.getElementById("liveCurrentCard");
  if(liveCard){
    liveCard.addEventListener("click", function(e){
      if(e.target.closest("button, a, .metric-action, .status-pill")) return;
      loadStopSummary();
    });

    liveCard.addEventListener("keydown", function(e){
      if(e.key === "Enter" || e.key === " "){
        e.preventDefault();
        loadStopSummary();
      }
    });
  }


  if(offBtn){
    offBtn.addEventListener("click", function(){
      loadDetail("offload");
    });
  }

  if(bagBtn){
    bagBtn.addEventListener("click", function(){
      loadDetail("bagaj");
    });
  }

  if(bodyEl){
    bodyEl.addEventListener("click", function(e){
      const cargoDetailBtn = e.target.closest("[data-cargo-detail]");
      if(cargoDetailBtn){
        const cid = cargoDetailBtn.getAttribute("data-cargo-detail") || "";
        renderConsignmentDetail(cid);
        return;
      }

      const cargoDeliverBtn = e.target.closest("[data-cargo-deliver]");
      if(cargoDeliverBtn){
        const cid = cargoDeliverBtn.getAttribute("data-cargo-deliver") || "";
        deliverConsignmentFromSheet(cid);
        return;
      }

      const bagDetailBtn = e.target.closest("[data-bag-seat]");
      if(bagDetailBtn){
        const seatNo = bagDetailBtn.getAttribute("data-bag-seat") || "";
        renderSeatBagDetail(seatNo);
        return;
      }

      const bulkBtn = e.target.closest("#sheetBulkOffloadBtn");
      if(bulkBtn){
        bulkOffloadCurrentStop();
        return;
      }

      const offloadBtn = e.target.closest("[data-offload-seat]");
      if(offloadBtn){
        const seatNo = offloadBtn.getAttribute("data-offload-seat") || "";
        offloadSeatFromSheet(seatNo);
        return;
      }

      const btn = e.target.closest("[data-change-seat]");
      if(!btn) return;

      const seatNo = btn.getAttribute("data-change-seat") || "";
      const passenger = findPassenger(seatNo);
      renderChangeDestinationForm(passenger);
    });
  }

  if(closeBtn) closeBtn.addEventListener("click", closeSheet);
  if(overlay) overlay.addEventListener("click", closeSheet);

  document.addEventListener("keydown", function(e){
    if(e.key === "Escape") closeSheet();
  });

  refreshMetricState();
})();
/* ===== END SCRIPT BLOCK: live-stop-sheet-script ===== */


/* ===== SCRIPT BLOCK: continue-live-eta-engine ===== */
(function(){
  window.CONTINUE_LIVE_SPEED_ENGINE_ACTIVE = true;

  const BOOT = window.CONTINUE_BOOT || {};
    const tripId = BOOT.tripId || 0;
    const tripDate = BOOT.tripDate || "";
    const routeStops = BOOT.routeStops || [];
    const routeCoords = BOOT.routeCoords || [];
    const scheduleItems = BOOT.scheduleItems || [];

  let lastPos = null;
  let lastGpsPoint = null;
  let lastMeasuredSpeedKmh = NaN;
  let speedHistory = [];
  let lastWriteSig = "";
  let lastWriteAt = 0;

  function q(sel){ return document.querySelector(sel); }

  function setText(sel, val){
    const el = q(sel);
    if(el) el.textContent = val;
  }

  function norm(v){
    return String(v || "")
      .trim()
      .toLocaleLowerCase("tr-TR")
      .replace(/[–—_\/\\.,()[\]]/g, " ")
      .replace(/\s+/g, " ");
  }

  function pad(n){ return String(n).padStart(2, "0"); }

  function fmtHour(d){
    if(!(d instanceof Date) || isNaN(d.getTime())) return "—";
    return pad(d.getHours()) + ":" + pad(d.getMinutes());
  }

  function parseTime(t){
    const m = String(t || "").trim().match(/^(\d{1,2}):(\d{2})$/);
    if(!m) return NaN;
    return (parseInt(m[1],10) || 0) * 60 + (parseInt(m[2],10) || 0);
  }

  function minutesDiff(a,b){
    return Math.round((a.getTime() - b.getTime()) / 60000);
  }

  function fmtDelay(min){
    const n = Number(min || 0);
    if(n <= -1) return Math.abs(n) + " dk erken";
    if(n >= 1) return n + " dk geç";
    return "Planında";
  }

  function formatKm(km){
    if(!Number.isFinite(km) || km < 0) return "—";
    if(km < 1) return Math.round(km * 1000) + " m";
    return km.toFixed(2) + " km";
  }

  function distKm(a,b){
    const R = 6371;
    const toRad = x => x * Math.PI / 180;
    const dLat = toRad(Number(b.lat) - Number(a.lat));
    const dLng = toRad(Number(b.lng) - Number(a.lng));
    const lat1 = toRad(Number(a.lat));
    const lat2 = toRad(Number(b.lat));

    const h =
      Math.sin(dLat/2) * Math.sin(dLat/2) +
      Math.cos(lat1) * Math.cos(lat2) *
      Math.sin(dLng/2) * Math.sin(dLng/2);

    return 2 * R * Math.atan2(Math.sqrt(h), Math.sqrt(1-h));
  }

  function routeIndex(name){
    const n = norm(name);
    if(!n || !Array.isArray(routeStops)) return -1;
    return routeStops.findIndex(x => norm(x) === n);
  }

  function findCoord(name){
    const n = norm(name);
    if(!n || !Array.isArray(routeCoords)) return null;

    const item = routeCoords.find(x => norm(x.stop) === n);
    if(!item) return null;

    const lat = Number(item.lat);
    const lng = Number(item.lng);
    if(!Number.isFinite(lat) || !Number.isFinite(lng)) return null;

    return { lat, lng };
  }

  function baseDate(){
    if(tripDate && /^\d{4}-\d{2}-\d{2}$/.test(tripDate)){
      return new Date(tripDate + "T00:00:00");
    }

    const d = new Date();
    d.setHours(0,0,0,0);
    return d;
  }

  function buildSchedule(){
    if(!Array.isArray(scheduleItems) || !scheduleItems.length) return [];

    let prev = null;
    let carry = 0;

    return scheduleItems
      .map(x => ({
        stop: String(x.stop || x.stop_name || "").trim(),
        time: String(x.time || x.planned_time || "").trim(),
        isTimed: Number(x.is_timed || x.isTimed || 0)
      }))
      .filter(x => x.stop && x.time)
      .map(x => {
        let cur = parseTime(x.time);
        if(!Number.isFinite(cur)) return null;

        cur += carry;

        if(prev !== null && cur < prev){
          carry += 1440;
          cur += 1440;
        }

        prev = cur;

        const d = baseDate();
        d.setMinutes(d.getMinutes() + cur);

        return {
          stop:x.stop,
          plan:x.time,
          planDate:d,
          routeIndex:routeIndex(x.stop),
          isTimed:x.isTimed
        };
      })
      .filter(Boolean);
  }

  function liveStopName(){
    return String(q("#liveCurrentStopName")?.textContent || "").trim();
  }

  function liveDisplaySpeed(){
    if(!Number.isFinite(lastMeasuredSpeedKmh)) return 0;
    if(lastMeasuredSpeedKmh < 3) return 0;
    return Math.round(lastMeasuredSpeedKmh);
  }

  function updateSpeedDisplay(){
    setText("#liveSpeedText", liveDisplaySpeed() + " km/sa");
  }

  function acceptSpeed(kmh){
    if(!Number.isFinite(kmh)) return;

    if(kmh < 3) kmh = 0;
    if(kmh > 160) return;

    if(!Number.isFinite(lastMeasuredSpeedKmh)){
      lastMeasuredSpeedKmh = kmh;
    }else{
      lastMeasuredSpeedKmh = (lastMeasuredSpeedKmh * 0.55) + (kmh * 0.45);
    }

    if(lastMeasuredSpeedKmh < 3) lastMeasuredSpeedKmh = 0;

    const shown = liveDisplaySpeed();

    if(shown >= 15){
      speedHistory.push(shown);
      if(speedHistory.length > 10) speedHistory.shift();
    }

    updateSpeedDisplay();
  }

  function measureSpeedFromGps(coords, point){
    const gpsSpeed = Number(coords.speed);

    if(Number.isFinite(gpsSpeed) && gpsSpeed > 0.5){
      acceptSpeed(gpsSpeed * 3.6);
      return;
    }

    if(!lastGpsPoint){
      acceptSpeed(0);
      return;
    }

    const dt = Math.max(0, (point.t - lastGpsPoint.t) / 1000);
    if(dt < 1 || dt > 20) return;

    const km = distKm(lastGpsPoint, point);
    const meters = km * 1000;

    const acc = Number(point.accuracy || 999);
    const jitterLimit = Math.max(4, Math.min(25, acc * 0.35));

    if(meters < jitterLimit){
      acceptSpeed(0);
      return;
    }

    const kmh = km / (dt / 3600);
    acceptSpeed(kmh);
  }

  function etaSpeedKmh(){
    const live = liveDisplaySpeed();

    if(live >= 25){
      return Math.min(95, Math.max(35, live));
    }

    const hist = speedHistory.filter(x => Number.isFinite(x) && x >= 15);

    if(hist.length){
      const avg = hist.reduce((a,b) => a + b, 0) / hist.length;
      if(avg >= 20) return Math.min(95, Math.max(35, avg));
    }

    return 70; // Sadece ETA iç hesabı. Ekrana yazılmaz.
  }

  function pickTarget(schedule, liveName){
    if(!schedule.length) return null;

    const liveIdx = routeIndex(liveName);
    const liveNorm = norm(liveName);

    let target = null;

    if(liveIdx >= 0){
      target = schedule.find(x => x.routeIndex >= liveIdx);
    }

    if(!target && liveNorm){
      target = schedule.find(x => norm(x.stop) === liveNorm);
    }

    if(!target){
      const now = new Date();
      target = schedule.find(x => x.planDate.getTime() >= now.getTime() - 5 * 60000);
    }

    return target || schedule[schedule.length - 1];
  }

  function updateAllDistances(){
    if(!lastPos) return;

    document.querySelectorAll(".stop-distance-value[data-stop-name]").forEach(el => {
      const name = el.getAttribute("data-stop-name") || "";
      const c = findCoord(name);
      if(!c) return;

      el.textContent = formatKm(distKm(lastPos, c));
    });
  }

  function updateStatus(etaMain){
    const etaEl = q("#liveEtaValue");
    const statusPill = q("#liveCurrentCard .status-pill.live");

    if(etaEl) etaEl.textContent = etaMain;
    if(statusPill) statusPill.textContent = etaMain;

    window.dispatchEvent(new CustomEvent("continueEtaUpdated", {
      detail:{ etaMain }
    }));
  }

  function writeRuntime(liveName, gpsKm, etaMain){
    const now = Date.now();
    const displaySpeed = liveDisplaySpeed();
    const sig = [liveName, displaySpeed, gpsKm, etaMain].join("|");

    if(sig === lastWriteSig && now - lastWriteAt < 2500) return;

    lastWriteSig = sig;
    lastWriteAt = now;

    const url =
      `/api/live-runtime-state?write=1` +
      `&trip_id=${encodeURIComponent(tripId)}` +
      `&live_stop=${encodeURIComponent(liveName || "")}` +
      `&speed=${encodeURIComponent(displaySpeed)}` +
      `&gps_km=${encodeURIComponent(gpsKm || "")}` +
      `&eta_main=${encodeURIComponent(etaMain || "")}` +
      `&eta_sub=${encodeURIComponent("continue-live-speed-engine")}` +
      `&_=${Date.now()}`;

    fetch(url, {
      method:"GET",
      credentials:"same-origin",
      cache:"no-store"
    }).catch(() => {});
  }

  function compute(){
    if(!lastPos) return;

    const liveName = liveStopName();
    if(!liveName) return;

    const liveCoord = findCoord(liveName);
    let gpsKm = "—";

    if(liveCoord){
      const liveKm = distKm(lastPos, liveCoord);
      gpsKm = formatKm(liveKm);
      setText("#liveDistanceValue", gpsKm);
    }

    updateAllDistances();

    const schedule = buildSchedule();
    const target = pickTarget(schedule, liveName);

    if(!target) return;

    const targetCoord = findCoord(target.stop);
    if(!targetCoord) return;

    const km = distKm(lastPos, targetCoord);
    const speed = etaSpeedKmh();
    const travelMin = Math.max(1, Math.round((km / speed) * 60));
    const etaDate = new Date(Date.now() + travelMin * 60000);
    const delayMin = minutesDiff(etaDate, target.planDate);
    const etaMain = fmtDelay(delayMin);

    updateStatus(etaMain);
    writeRuntime(liveName, gpsKm, etaMain);
  }

  function onPosition(pos){
    const c = pos && pos.coords ? pos.coords : null;
    if(!c) return;

    const lat = Number(c.latitude);
    const lng = Number(c.longitude);

    if(!Number.isFinite(lat) || !Number.isFinite(lng)) return;

    const point = {
      lat,
      lng,
      t: Date.now(),
      accuracy: Number(c.accuracy || 999)
    };

    measureSpeedFromGps(c, point);

    lastPos = { lat, lng };
    lastGpsPoint = point;

    compute();
  }

  function start(){
    updateSpeedDisplay();
    compute();

    if(!navigator.geolocation){
      console.warn("Canlı hız: geolocation yok");
      return;
    }

    navigator.geolocation.watchPosition(onPosition, function(err){
      console.warn("Canlı hız GPS hatası:", err && err.message ? err.message : err);
    }, {
      enableHighAccuracy:true,
      timeout:10000,
      maximumAge:1000
    });

    setInterval(compute, 1500);
  }

  if(document.readyState === "loading"){
    document.addEventListener("DOMContentLoaded", start);
  }else{
    start();
  }
})();
/* ===== END SCRIPT BLOCK: continue-live-eta-engine ===== */


