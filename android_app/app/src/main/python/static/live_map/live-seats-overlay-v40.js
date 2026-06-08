/* =========================================================
   LIVE_SEATS_OVERLAY_V40
   Canlı takip ekranında Koltuklar butonu + açılır panel.
========================================================= */
(function(){
  const MARK = "LIVE_SEATS_OVERLAY_V40_READY";
  if (window[MARK]) return;
  window[MARK] = true;

  function ready(fn){
    if (document.readyState === "loading"){
      document.addEventListener("DOMContentLoaded", fn);
    } else {
      fn();
    }
  }

  function cleanIds(root){
    if (!root) return;
    if (root.removeAttribute) root.removeAttribute("id");
    root.querySelectorAll("[id]").forEach(function(n){
      n.removeAttribute("id");
    });
  }

  function makeOverlay(){
    if (document.getElementById("liveSeatsOverlayV40")) return;

    const overlay = document.createElement("div");
    overlay.id = "liveSeatsOverlayV40";
    overlay.setAttribute("aria-hidden", "true");

    overlay.innerHTML = `
      <div class="v40-live-seats-panel" role="dialog" aria-modal="true" aria-label="Koltuklar">
        <div class="v40-live-seats-head">
          <div class="v40-live-seats-title">
            <strong>🪑 Koltuklar</strong>
            <span>Canlı takipten çıkmadan hızlı kontrol</span>
          </div>
          <button type="button" class="v40-live-seats-close" id="liveSeatsCloseV40" aria-label="Kapat">×</button>
        </div>

        <div class="v40-live-stop-strip" id="liveStopCardsV40"></div>

        <div class="v40-live-seat-frame-wrap">
          <iframe id="liveSeatsFrameV40" title="Koltuk Planı"></iframe>
        </div>
      </div>
    `;

    document.body.appendChild(overlay);

    overlay.addEventListener("click", function(e){
      if (e.target === overlay) closeOverlay();
    });

    const closeBtn = document.getElementById("liveSeatsCloseV40");
    if (closeBtn) closeBtn.addEventListener("click", closeOverlay);

    document.addEventListener("keydown", function(e){
      if (e.key === "Escape") closeOverlay();
    });

    const frame = document.getElementById("liveSeatsFrameV40");
    if (frame){
      frame.addEventListener("load", function(){
        injectFrameStyle(frame);
      });
    }
  }

  function makeButton(){
    if (document.getElementById("liveSeatsOpenBtnV40")) return;

    const btn = document.createElement("button");
    btn.type = "button";
    btn.id = "liveSeatsOpenBtnV40";
    btn.className = "v40-live-seats-btn";
    btn.innerHTML = `<span class="v40-ico">🪑</span><b>Koltuklar</b>`;

    btn.addEventListener("click", function(e){
      e.preventDefault();
      e.stopPropagation();
      openOverlay();
    });

    document.body.appendChild(btn);
  }

  function isVisible(el){
    try{
      const r = el.getBoundingClientRect();
      const st = window.getComputedStyle(el);
      return (
        r.width > 80 &&
        r.height > 38 &&
        r.height < 260 &&
        st.display !== "none" &&
        st.visibility !== "hidden" &&
        Number(st.opacity || 1) > 0.05
      );
    }catch(e){
      return false;
    }
  }

  function findStopCards(){
    const words = /(canlı|sıradaki|bekliyor|durak|otogar|ortahan|belenyaka|alaşehir|inecek|bagaj|kalan|plan\/eta|eta)/i;
    const bad = /(koltuklar|muavin asistanı açılıyor|aktif sefer var)/i;
    const nodes = Array.from(document.body.querySelectorAll("article, section, div, button"));
    const picked = [];

    for (const el of nodes){
      if (el.closest("#liveSeatsOverlayV40")) continue;
      if (el.id === "liveSeatsOpenBtnV40") continue;
      if (!isVisible(el)) continue;

      const txt = (el.innerText || "").trim().replace(/\s+/g, " ");
      const cls = (el.className && el.className.toString ? el.className.toString() : "");

      if (!txt || txt.length < 5 || txt.length > 320) continue;
      if (bad.test(txt)) continue;
      if (!words.test(txt + " " + cls)) continue;

      const r = el.getBoundingClientRect();

      for (let i = picked.length - 1; i >= 0; i--){
        const old = picked[i];
        try{
          const or = old.getBoundingClientRect();
          if (el.contains(old) && r.height <= 220 && r.width <= 540){
            picked.splice(i, 1);
          }
        }catch(e){}
      }

      if (picked.some(function(x){ return x.contains(el); })) continue;

      picked.push(el);
      if (picked.length >= 4) break;
    }

    return picked;
  }

  function fillStopCards(){
    const box = document.getElementById("liveStopCardsV40");
    if (!box) return;

    box.innerHTML = "";

    const cards = findStopCards();

    if (!cards.length){
      const empty = document.createElement("div");
      empty.className = "v40-stop-empty";
      empty.textContent = "Durak kartları okunamadı. Koltuk planı aşağıda açılıyor.";
      box.appendChild(empty);
      return;
    }

    cards.forEach(function(card){
      const wrap = document.createElement("div");
      wrap.className = "v40-stop-clone";

      const clone = card.cloneNode(true);
      cleanIds(clone);

      wrap.appendChild(clone);
      box.appendChild(wrap);
    });
  }

  function injectFrameStyle(frame){
    try{
      const doc = frame.contentDocument || frame.contentWindow.document;
      if (!doc || doc.getElementById("liveSeatsFrameStyleV40")) return;

      const style = doc.createElement("style");
      style.id = "liveSeatsFrameStyleV40";
      style.textContent = `
        html,body{
          background:#07111f !important;
          overflow:auto !important;
        }

        .topbar,
        #driveInlineDock,
        .driveInlineDock,
        .bottom-nav,
        .bottom-bar,
        .simple-bottom-bar,
        #seatSimpleBottomBar,
        #bottomNav,
        .seat-bottom-nav,
        .fab-column{
          display:none !important;
        }

        .seats-shell,
        .layout{
          margin:0 !important;
          padding:0 !important;
          max-width:none !important;
          background:transparent !important;
        }

        .layout{
          gap:8px !important;
        }

        .board-card,
        .board-inner{
          margin:0 !important;
          padding:8px !important;
          border-radius:24px !important;
          background:#07111f !important;
        }

        .board-head,
        .legend,
        .voice-row,
        .drive-voice-row,
        #driveVoiceRow,
        .selected-stop-chip{
          display:none !important;
        }

        .deck,
        .deck-wrap,
        .seat-grid{
          margin-top:0 !important;
        }
      `;

      doc.head.appendChild(style);
    }catch(e){
      // Aynı origin değilse sessiz geç.
    }
  }

  function openOverlay(){
    makeOverlay();
    fillStopCards();

    const overlay = document.getElementById("liveSeatsOverlayV40");
    const frame = document.getElementById("liveSeatsFrameV40");

    if (frame && !frame.dataset.loaded){
      frame.src = "/seats?live_overlay_v40=1";
      frame.dataset.loaded = "1";
    }

    if (overlay){
      overlay.classList.add("v40-show");
      overlay.setAttribute("aria-hidden", "false");
      document.documentElement.classList.add("v40-live-seats-lock");
    }
  }

  function closeOverlay(){
    const overlay = document.getElementById("liveSeatsOverlayV40");
    if (overlay){
      overlay.classList.remove("v40-show");
      overlay.setAttribute("aria-hidden", "true");
    }
    document.documentElement.classList.remove("v40-live-seats-lock");
  }

  ready(function(){
    makeOverlay();
    makeButton();
  });
})();
