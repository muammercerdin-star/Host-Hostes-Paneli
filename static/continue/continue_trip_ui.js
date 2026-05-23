/* =========================================================
   continue_trip_ui.js
   Otomatik çıkarıldı: continue_trip.html
   Bu dosyada Jinja değişkeni içermeyen güvenli UI scriptleri var.
========================================================= */


/* ===== SCRIPT BLOCK: live-clock-script ===== */
(function(){
  const el = document.getElementById("liveClockText");
  if(!el) return;

  function pad(n){
    return String(n).padStart(2, "0");
  }

  function updateClock(){
    const now = new Date();
    el.textContent = pad(now.getHours()) + ":" + pad(now.getMinutes()) + ":" + pad(now.getSeconds());
  }

  updateClock();
  setInterval(updateClock, 1000);
})();
/* ===== END SCRIPT BLOCK: live-clock-script ===== */


/* ===== SCRIPT BLOCK: bag-photo-viewer-script ===== */
(function(){
  const viewer = document.getElementById("bagPhotoViewer");
  const img = document.getElementById("bagViewerImg");
  const title = document.getElementById("bagViewerTitle");
  const caption = document.getElementById("bagViewerCaption");
  const closeBtn = document.getElementById("bagViewerClose");
  const prevBtn = document.getElementById("bagViewerPrev");
  const nextBtn = document.getElementById("bagViewerNext");

  if(!viewer || !img || !title || !caption) return;

  let photos = [];
  let index = 0;

  function getPhotoItems(){
    return Array.from(document.querySelectorAll(".sheet-bag-photo, .sheet-cargo-photo")).map((el, i) => {
      const badge = el.querySelector(".sheet-bag-photo-badge");
      const side = el.querySelector(".sheet-bag-photo-side");
      const image = el.querySelector("img");

      return {
        url: el.getAttribute("href") || (image ? image.getAttribute("src") : ""),
        thumb: image ? image.getAttribute("src") : "",
        badge: badge ? badge.textContent.trim() : `${i + 1}`,
        side: side ? side.textContent.trim() : "",
      };
    }).filter(x => x.url);
  }

  function showPhoto(i){
    if(!photos.length) return;

    index = Math.max(0, Math.min(i, photos.length - 1));
    const p = photos[index];

    img.src = p.url;
    title.textContent = `Fotoğraf ${index + 1} / ${photos.length}`;
    caption.textContent = p.side ? `${p.side} • ${index + 1} / ${photos.length}` : `${index + 1} / ${photos.length}`;

    if(prevBtn) prevBtn.disabled = index <= 0;
    if(nextBtn) nextBtn.disabled = index >= photos.length - 1;
  }

  function openViewer(startIndex){
    photos = getPhotoItems();

    if(!photos.length) return;

    viewer.classList.add("open");
    viewer.setAttribute("aria-hidden", "false");
    document.body.style.overflow = "hidden";

    showPhoto(startIndex || 0);
  }

  function closeViewer(){
    viewer.classList.remove("open");
    viewer.setAttribute("aria-hidden", "true");
    img.src = "";

    // Canlı durak sheet açıksa body kilidi kalsın; yoksa serbest bırak.
    const liveSheet = document.getElementById("liveStopSheet");
    if(!liveSheet || !liveSheet.classList.contains("open")){
      document.body.style.overflow = "";
    }
  }

  document.addEventListener("click", function(e){
    const photo = e.target.closest(".sheet-bag-photo, .sheet-cargo-photo");
    if(!photo) return;

    e.preventDefault();

    const currentList = Array.from(document.querySelectorAll(".sheet-bag-photo, .sheet-cargo-photo"));
    const startIndex = currentList.indexOf(photo);

    openViewer(startIndex >= 0 ? startIndex : 0);
  });

  if(closeBtn) closeBtn.addEventListener("click", closeViewer);

  if(prevBtn){
    prevBtn.addEventListener("click", function(){
      showPhoto(index - 1);
    });
  }

  if(nextBtn){
    nextBtn.addEventListener("click", function(){
      showPhoto(index + 1);
    });
  }

  viewer.addEventListener("click", function(e){
    if(e.target === viewer) closeViewer();
  });

  document.addEventListener("keydown", function(e){
    if(!viewer.classList.contains("open")) return;

    if(e.key === "Escape") closeViewer();
    if(e.key === "ArrowLeft") showPhoto(index - 1);
    if(e.key === "ArrowRight") showPhoto(index + 1);
  });
})();
/* ===== END SCRIPT BLOCK: bag-photo-viewer-script ===== */


/* ===== SCRIPT BLOCK: continue-live-v2-script ===== */
(function(){
  function q(sel){ return document.querySelector(sel); }

  function ensureV2(){
    document.body.classList.add("continue-live-v2");

    const card = q("#liveCurrentCard");
    if(!card) return;

    const label = card.querySelector(".card-label");
    if(label && !label.dataset.v2Ready){
      label.dataset.v2Ready = "1";
      label.innerHTML = '<span class="continue-v2-dot"></span> CANLI';
    }

    if(!q("#continueLiveV2Distance")){
      const line = document.createElement("div");
      line.className = "continue-v2-distance-line";
      line.innerHTML = 'Kalan mesafe: <span id="continueLiveV2Distance">—</span>';

      const head = card.querySelector(".card-head");
      const grid = card.querySelector(".metric-grid");

      if(head && grid){
        card.insertBefore(line, grid);
      }
    }

    syncV2Texts();
  }

  function syncV2Texts(){
    const eta = q("#liveEtaValue");
    const distance = q("#liveDistanceValue");
    const distanceMirror = q("#continueLiveV2Distance");
    const status = q("#liveCurrentCard .status-pill.live");

    if(distance && distanceMirror){
      distanceMirror.textContent = distance.textContent || "—";
    }

    if(eta && status){
      status.textContent = eta.textContent || "Plan dışı";
      status.title = eta.textContent || "";
    }
  }

  if(document.readyState === "loading"){
    document.addEventListener("DOMContentLoaded", ensureV2);
  }else{
    ensureV2();
  }

  setTimeout(ensureV2, 150);
  setTimeout(ensureV2, 800);
  setInterval(syncV2Texts, 700);
})();
/* ===== END SCRIPT BLOCK: continue-live-v2-script ===== */


/* ===== SCRIPT BLOCK: continue-top-status-stable-compact-script ===== */
(function(){
  function esc(v){
    return String(v || "").replace(/[&<>"']/g, function(c){
      return {"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[c];
    });
  }

  function clean(v){
    const t = String(v || "").trim();
    if(!t || t === "-" || t === "—" || t === "--:--") return "Planında";
    return t;
  }

  function splitStatus(v){
    const t = clean(v);
    let m = t.match(/^(\d+)\s*(dk|dakika)?\s+(erken|geç)$/i);
    if(m){
      return { main:m[1] + " dk", sub:m[3].toUpperCase(), raw:t };
    }
    return { main:t, sub:"", raw:t };
  }

  function render(){
    const top = document.getElementById("liveTopStatusText");
    const eta = document.getElementById("liveEtaValue");
    if(!top) return;

    const data = splitStatus(eta ? eta.textContent : top.textContent);
    const html = '<span class="status-main">' + esc(data.main) + '</span>' +
                 (data.sub ? '<span class="status-sub">' + esc(data.sub) + '</span>' : '');

    if(top.dataset.lastHtml !== html){
      top.innerHTML = html;
      top.dataset.lastHtml = html;
    }

    top.classList.toggle("status-early", /erken/i.test(data.raw));
    top.classList.toggle("status-late", /ge[cç]/i.test(data.raw));
    top.classList.toggle("status-plan", /plan/i.test(data.raw));
  }

  if(document.readyState === "loading"){
    document.addEventListener("DOMContentLoaded", render);
  }else{
    render();
  }

  setTimeout(render, 150);
  setTimeout(render, 800);
  setInterval(render, 700);
})();
/* ===== END SCRIPT BLOCK: continue-top-status-stable-compact-script ===== */
