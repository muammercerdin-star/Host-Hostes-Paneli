/* =========================================================
   continue_live_diagnostics.js
   Katlanır canlı durak motoru teşhis paneli.
   Mantığı değiştirmez, sadece backend live_runtime_state durumunu gösterir.
========================================================= */

(function(){
  const BOOT = window.CONTINUE_BOOT || {};
  const tripId = BOOT.tripId || "";

  const POLL_MS = 3000;
  const STORE_KEY = "continueLiveDiagnosticsOpen";

  function text(v){
    return String(v == null ? "" : v).trim();
  }

  function readOpen(){
    try{
      return localStorage.getItem(STORE_KEY) === "1";
    }catch(_){
      return false;
    }
  }

  function saveOpen(open){
    try{
      localStorage.setItem(STORE_KEY, open ? "1" : "0");
    }catch(_){}
  }

  function pickPayload(j){
    if(!j) return {};
    return j.state || j.runtime || j.live_runtime || j.data || j;
  }

  function parseDateMs(v){
    const s = text(v);
    if(!s) return NaN;

    const candidates = [
      s,
      s.replace(" ", "T"),
      s.replace(" ", "T") + "+03:00"
    ];

    for(const c of candidates){
      const t = new Date(c).getTime();
      if(Number.isFinite(t)) return t;
    }

    return NaN;
  }

  function ageText(updatedAt){
    const t = parseDateMs(updatedAt);
    if(!Number.isFinite(t)) return "zaman yok";

    const sec = Math.max(0, Math.round((Date.now() - t) / 1000));

    if(sec < 5) return "az önce";
    if(sec < 60) return sec + " sn önce";

    const min = Math.round(sec / 60);
    return min + " dk önce";
  }

  function freshness(updatedAt){
    const t = parseDateMs(updatedAt);
    if(!Number.isFinite(t)) return "warn";

    const sec = Math.max(0, Math.round((Date.now() - t) / 1000));

    if(sec <= 12) return "ok";
    if(sec <= 45) return "warn";
    return "bad";
  }

  function setText(id, value){
    const el = document.getElementById(id);
    if(el) el.textContent = text(value) || "—";
  }

  function setOpen(box, open){
    if(!box) return;

    box.classList.toggle("is-collapsed", !open);
    box.dataset.open = open ? "1" : "0";

    const head = box.querySelector(".diag-head");
    const caret = box.querySelector("#diagCaret");

    if(head){
      head.setAttribute("aria-expanded", open ? "true" : "false");
      head.title = open ? "Teşhisi küçült" : "Teşhisi aç";
    }

    if(caret){
      caret.textContent = open ? "▴" : "▾";
    }

    saveOpen(open);
  }

  function ensurePanel(){
    let box = document.getElementById("continueLiveDiagnostics");
    if(box) return box;

    const host =
      document.getElementById("liveCurrentCard") ||
      document.querySelector(".timeline") ||
      document.querySelector("main") ||
      document.body;

    if(!host) return null;

    box = document.createElement("div");
    box.id = "continueLiveDiagnostics";
    box.className = "continue-live-diagnostics";
    box.innerHTML = `
      <button type="button" class="diag-head" aria-expanded="false">
        <span class="diag-dot" id="diagLiveDot"></span>
        <div class="diag-titlebox">
          <b>Canlı takip durumu</b>
          <small id="diagLiveSource">seats.js → backend → continue</small>
        </div>
        <span class="diag-caret" id="diagCaret">▾</span>
      </button>

      <div class="diag-body">
        <div class="diag-grid">
          <div>
            <span>Backend canlı durak</span>
            <b id="diagLiveStop">—</b>
          </div>
          <div>
            <span>Mesafe</span>
            <b id="diagGpsKm">—</b>
          </div>
          <div>
            <span>Hız</span>
            <b id="diagSpeed">—</b>
          </div>
          <div>
            <span>Güncelleme</span>
            <b id="diagUpdatedAt">—</b>
          </div>
        </div>

        <div class="diag-note" id="diagLiveNote">
          Canlı durak motoru koltuk ekranındaki GPS verisinden beslenir.
        </div>
      </div>
    `;

    host.appendChild(box);

    const head = box.querySelector(".diag-head");

    if(head){
      head.addEventListener("click", function(){
        setOpen(box, box.classList.contains("is-collapsed"));
      });
    }

    setOpen(box, readOpen());

    return box;
  }

  function applyState(data){
    const box = ensurePanel();
    if(!box) return;

    const liveStop = text(data.live_stop || data.liveStop || BOOT.runtimeStop || "");
    const gpsKmRaw = data.gps_km ?? data.gpsKm ?? BOOT.runtimeGpsKm ?? "";
    const speedRaw = data.speed ?? BOOT.runtimeSpeed ?? "";
    const updatedAt = text(data.updated_at || data.updatedAt || "");

    let gpsKm = "—";
    const nKm = Number(gpsKmRaw);

    if(Number.isFinite(nKm) && text(gpsKmRaw)){
      gpsKm = nKm.toFixed(2) + " km";
    }else if(text(gpsKmRaw)){
      gpsKm = text(gpsKmRaw);
    }

    let speed = "—";
    const nSpeed = Number(speedRaw);

    if(Number.isFinite(nSpeed) && text(speedRaw)){
      speed = Math.round(nSpeed) + " km/h";
    }else if(text(speedRaw)){
      speed = text(speedRaw);
    }

    const updatedText = updatedAt ? ageText(updatedAt) : "zaman yok";
    const fresh = freshness(updatedAt);

    box.dataset.state = fresh;

    setText("diagLiveStop", liveStop || "Canlı durak bekleniyor");
    setText("diagGpsKm", gpsKm);
    setText("diagSpeed", speed);
    setText("diagUpdatedAt", updatedText);

    const source = document.getElementById("diagLiveSource");
    if(source){
      if(liveStop){
        source.textContent = `${liveStop} · ${gpsKm} · ${updatedText}`;
      }else{
        source.textContent = `bekleniyor · ${gpsKm} · ${updatedText}`;
      }
    }

    const note = document.getElementById("diagLiveNote");

    if(note){
      if(!liveStop){
        note.textContent = "Backend'de canlı durak boş. Koltuk ekranında GPS açık olmalı veya araç 5 km eşiğine girmeli.";
      }else if(fresh === "bad"){
        note.textContent = "Veri bayat görünüyor. Koltuk ekranı kapalı olabilir veya GPS yazmayı bırakmış olabilir.";
      }else if(fresh === "warn"){
        note.textContent = "Veri geliyor ama biraz gecikmeli. GPS / ekran uyku durumunu kontrol et.";
      }else{
        note.textContent = "Veri canlı. Continue ekranı backend live_runtime_state değerini takip ediyor.";
      }
    }
  }

  async function poll(){
    ensurePanel();

    if(!tripId){
      applyState({
        live_stop: "",
        gps_km: "",
        speed: "",
        updated_at: ""
      });

      const note = document.getElementById("diagLiveNote");
      if(note){
        note.textContent = "tripId bulunamadı. CONTINUE_BOOT kontrol edilmeli.";
      }

      return;
    }

    try{
      const res = await fetch(`/api/live-runtime-state?trip_id=${encodeURIComponent(tripId)}&_=${Date.now()}`, {
        method: "GET",
        credentials: "same-origin",
        cache: "no-store",
        headers: {
          "Accept": "application/json"
        }
      });

      const j = await res.json();
      const data = pickPayload(j);

      applyState(data || {});
    }catch(err){
      const box = ensurePanel();

      if(box){
        box.dataset.state = "bad";
      }

      setText("diagLiveStop", "API okunamadı");
      setText("diagUpdatedAt", "hata");

      const source = document.getElementById("diagLiveSource");
      if(source){
        source.textContent = "API okunamadı · hata";
      }

      const note = document.getElementById("diagLiveNote");
      if(note){
        note.textContent = "Canlı teşhis API hatası: " + (err && err.message ? err.message : "bilinmeyen hata");
      }
    }
  }

  if(document.readyState === "loading"){
    document.addEventListener("DOMContentLoaded", poll);
  }else{
    poll();
  }

  setInterval(poll, POLL_MS);

  document.addEventListener("visibilitychange", function(){
    if(!document.hidden){
      poll();
    }
  });

  window.ContinueLiveDiagnostics = {
    refresh: poll
  };
})();
