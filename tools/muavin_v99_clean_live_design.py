from pathlib import Path
from datetime import datetime
import shutil

ROOT = Path(".").resolve()
STAMP = datetime.now().strftime("%Y%m%d-%H%M%S")

WEB_TPL = ROOT / "templates/continue_trip.html"
AND_TPL = ROOT / "android_app/app/src/main/python/templates/continue_trip.html"

WEB_CSS = ROOT / "static/continue/continue_trip_v99_clean.css"
WEB_JS  = ROOT / "static/continue/continue_trip_v99_clean.js"

AND_CSS = ROOT / "android_app/app/src/main/python/static/continue/continue_trip_v99_clean.css"
AND_JS  = ROOT / "android_app/app/src/main/python/static/continue/continue_trip_v99_clean.js"

print("===== MUAVIN V99 CLEAN LIVE DESIGN =====")

for p in [WEB_TPL, AND_TPL, WEB_CSS, WEB_JS, AND_CSS, AND_JS]:
    if p.exists():
        bak = p.with_name(p.name + f".bak-v99-clean-{STAMP}")
        shutil.copy2(p, bak)
        print("📦 backup:", bak)

TEMPLATE = r'''<!doctype html>
<html lang="tr">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
  <title>Canlı Durak Akışı</title>

  <link rel="stylesheet" href="{{ url_for('static', filename='continue/continue_trip.css') }}?v=refresh-v49">
  <link rel="stylesheet" href="{{ url_for('static', filename='continue/continue_trip_v99_clean.css') }}?v=v99-clean-{{ trip['id'] }}">
</head>

<body class="v99-live-body">

{% set occ_total = live_summary.total_seats or 1 %}
{% set occ_count = live_summary.passenger_count or 0 %}
{% set occ_pct = ((occ_count * 100) / occ_total) | round(0) %}
{% set current_stop_name = (live_runtime.live_stop if live_runtime and live_runtime.live_stop else live_current.name) or "Durak seçilmedi" %}
{% set current_eta = (live_runtime.eta_main if live_runtime and live_runtime.eta_main else live_current.eta) or "-" %}
{% set current_distance = (live_runtime.gps_km if live_runtime and live_runtime.gps_km else live_current.distance) or "-" %}

<header class="v99-hdr">
  <div class="v99-hdr-brand">
    <div class="v99-hdr-icon">🎙️</div>
    <div>
      <div class="v99-hdr-title">MUAVİN</div>
      <div class="v99-hdr-sub">ASİSTAN V99</div>
    </div>
  </div>

  <div class="v99-hdr-clock" id="liveClockText">--:--</div>
</header>

<div class="v99-route-bar">
  <span class="v99-route-name">
    {{ (trip["route"] or "Denizli – İstanbul") | replace(" – ", " → ") | replace("–", " → ") | replace("-", " → ") }}
  </span>
  <span class="v99-route-dot">·</span>
  <span>{{ trip["plate"] or "45KH999" }}</span>

  <div class="v99-live-badge">
    <div class="v99-live-dot"></div>
    CANLI
  </div>
</div>

<div class="v99-gauges">
  <div class="v99-gauge-cell">
    <div class="v99-gauge-label">HIZ</div>
    <div class="v99-gauge-val amber" id="v99SpeedVal">0</div>
    <div class="v99-gauge-unit">km/sa</div>
    <span class="v99-core-hidden" id="liveSpeedText">— km/sa</span>
  </div>

  <div class="v99-gauge-cell">
    <div class="v99-gauge-label">DOLULUK</div>
    <div class="v99-gauge-val">{{ live_summary.passenger_count }} / {{ live_summary.total_seats }}</div>

    <div class="v99-occ-bar-track">
      <div class="v99-occ-bar-fill" style="width:{{ occ_pct }}%"></div>
    </div>

    <div class="v99-occ-genders">
      <span class="g-m">♂ {{ live_summary.male_count or 0 }}</span>
      <span class="g-f">♀ {{ live_summary.female_count or 0 }}</span>
      {% if live_summary.unknown_gender_count %}
        <span class="g-u">? {{ live_summary.unknown_gender_count }}</span>
      {% endif %}
    </div>
  </div>

  <div class="v99-gauge-cell">
    <div class="v99-gauge-label">DURUM</div>
    <div class="v99-gauge-val green v99-status-val" id="liveTopStatusText">Planında</div>
    <div class="v99-gauge-unit" id="v99StatusSub">canlı takip</div>
  </div>
</div>

<main class="v99-main">

  <section class="v99-prox-section">
    <div class="v99-prox-card live-summary-trigger" id="liveCurrentCard" role="button" tabindex="0" aria-label="Canlı durak özetini aç">

      <div class="v99-prox-top">
        <div class="v99-ring-wrap">
          <svg class="v99-ring-svg" viewBox="0 0 110 110" aria-hidden="true">
            <circle class="v99-ring-track" cx="55" cy="55" r="44"></circle>
            <circle class="v99-ring-fill" id="ringFill" cx="55" cy="55" r="44"
              stroke-dasharray="276.46"
              stroke-dashoffset="276.46"></circle>
          </svg>

          <div class="v99-ring-center">
            <div class="v99-ring-km" id="ringKm">—</div>
            <div class="v99-ring-km-label">KM</div>
          </div>
        </div>

        <div class="v99-prox-info">
          <div class="v99-prox-kicker">ŞU ANKİ DURAK</div>

          <div class="v99-prox-stop-name" id="liveCurrentStopName">{{ current_stop_name }}</div>

          <div class="v99-prox-eta-row">
            <span class="v99-prox-eta-val" id="liveEtaValue">{{ current_eta }}</span>
            <span class="v99-prox-eta-label">TAHMİNİ VARIŞ</span>
          </div>

          <div class="v99-status-pill">
            <div class="v99-live-dot"></div>
            CANLI TAKİP
          </div>

          <b id="liveDistanceValue"
             class="v99-core-hidden stop-distance-value"
             data-stop-name="{{ current_stop_name }}">{{ current_distance }}</b>
        </div>
      </div>

      <div class="v99-prox-metrics">
        <button class="v99-pm-cell" type="button" id="liveOffloadMetric" data-kind="offload" aria-label="Bu durakta inecek koltukları göster">
          <div class="v99-pm-icon">🧍</div>
          <div class="v99-pm-data">
            <div class="v99-pm-val" id="liveOffloadCount">{{ live_current.off_count or 0 }}</div>
            <div class="v99-pm-lbl">İNECEK YOLCU</div>
          </div>
        </button>

        <button class="v99-pm-cell" type="button" id="liveBagajMetric" data-kind="bagaj" aria-label="Bu durakta indirilecek bagajları göster">
          <div class="v99-pm-icon">🧳</div>
          <div class="v99-pm-data">
            <div class="v99-pm-val" id="liveBagajCount">{{ live_current.bagaj_count or 0 }}</div>
            <span id="liveEmanetCount" hidden></span>
            <div class="v99-pm-lbl">BAGAJ</div>
          </div>
        </button>
      </div>

      <div class="v99-dist-track-wrap">
        <div class="v99-dist-labels">
          <span>{{ stops[0] if stops else "DENİZLİ" }}</span>
          <span id="distPct">%0 tamamlandı</span>
          <span>{{ stops[-1] if stops else "İSTANBUL" }}</span>
        </div>

        <div class="v99-dist-track">
          <div class="v99-dist-fill" id="routeBar" style="width:0%"></div>
        </div>
      </div>

    </div>
  </section>

  <section class="v99-timeline-section">
    <div class="v99-section-label">GÜZERGAH</div>

    <div class="v99-tl" id="tlContainer">
      {% for stop in live_stops %}
      <div class="v99-tl-item">
        <div class="v99-tl-spine">
          <div class="v99-tl-node {{ stop.kind }}"></div>
          {% if not loop.last %}
            <div class="v99-tl-line {{ stop.kind }}"></div>
          {% endif %}
        </div>

        <div class="v99-tl-card {% if stop.kind == "live" %}live-card{% elif stop.kind == "next" %}next-card{% endif %}">
          <div class="v99-tl-card-head">
            <div class="v99-tl-stop-name {% if stop.kind == "passed" %}muted{% endif %}">{{ stop.name }}</div>

            {% if stop.kind == "live" %}
              <div class="v99-pill live">● CANLI</div>
            {% elif stop.kind == "next" %}
              <div class="v99-pill next">⟶ SONRAKİ</div>
            {% elif stop.kind == "passed" %}
              <div class="v99-pill passed">✓ GEÇİLDİ</div>
            {% else %}
              <div class="v99-pill upcoming">{{ stop.status or stop.eta }}</div>
            {% endif %}
          </div>

          <div class="v99-tl-metrics">
            <div class="v99-tl-metric">
              <div class="v99-tl-m-val">{{ stop.eta }}</div>
              <div class="v99-tl-m-lbl">VARIŞ</div>
            </div>

            <div class="v99-tl-metric">
              <div class="v99-tl-m-val stop-distance-value" data-stop-name="{{ stop.name }}">{{ stop.distance }}</div>
              <div class="v99-tl-m-lbl">MESAFE</div>
            </div>

            <div class="v99-tl-metric">
              <div class="v99-tl-m-val">{{ stop.off_count }}</div>
              <div class="v99-tl-m-lbl">İNECEK</div>
            </div>

            <div class="v99-tl-metric">
              <div class="v99-tl-m-val">{{ stop.bagaj_label }}</div>
              <div class="v99-tl-m-lbl">BAGAJ</div>
            </div>
          </div>
        </div>
      </div>
      {% endfor %}
    </div>
  </section>

  <section class="v99-end-wrap danger-zone">
    <form id="endTripForm" method="post" action="{{ url_for('end_trip') }}">
      {% if csrf_token is defined %}
        <input type="hidden" name="csrf_token" value="{{ csrf_token }}">
      {% endif %}
      <button class="v99-end-btn danger-btn" type="submit">⛔ &nbsp;SEFERİ BİTİR</button>
    </form>
  </section>

</main>

<div class="live-sheet-overlay" id="liveStopSheetOverlay"></div>

<section class="live-stop-sheet" id="liveStopSheet" aria-hidden="true">
  <div class="sheet-grip"></div>

  <div class="sheet-head">
    <div>
      <div class="sheet-kicker" id="liveStopSheetKicker">Canlı durak</div>
      <h2 class="sheet-title" id="liveStopSheetTitle">Durak detayı</h2>
      <p class="sheet-sub" id="liveStopSheetSub">Yükleniyor...</p>
    </div>

    <button class="sheet-close" type="button" id="liveStopSheetClose" aria-label="Kapat">×</button>
  </div>

  <div class="sheet-body" id="liveStopSheetBody">
    <div class="sheet-empty">Yükleniyor...</div>
  </div>
</section>

<nav class="v99-dock dock">
  <a class="v99-dock-btn active dock-item" href="{{ url_for('continue_trip') }}">
    <i>🚌</i><span>CANLI</span>
  </a>

  <a class="v99-dock-btn dock-item" id="continueSeatMapBtn" href="{{ url_for('seats_page') }}">
    <i>💺</i><span>KOLTUK</span>
  </a>

  <a class="v99-dock-btn dock-item" href="{{ url_for('passenger_control') }}">
    <i>👥</i><span>YOLCU</span>
  </a>

  <a class="v99-dock-btn dock-item" href="{{ url_for('live_map_page') }}">
    <i>🗺️</i><span>HARİTA</span>
  </a>

  <button class="v99-dock-btn dock-item" type="button">
    <i>📣</i><span>ANONS</span>
  </button>
</nav>

<div class="end-trip-overlay" id="endTripOverlay" aria-hidden="true">
  <div class="end-trip-box" role="dialog" aria-modal="true" aria-labelledby="endTripTitle">
    <div class="end-trip-top">
      <div class="end-trip-mark">⛔</div>
      <div>
        <h2 class="end-trip-title" id="endTripTitle">Seferi bitirelim mi?</h2>
        <p class="end-trip-small">Aktif sefer sonlandırılacak.</p>
      </div>
    </div>

    <div class="end-trip-content">
      <p class="end-trip-text">
        Sefer tamamlandıysa işlemi bitirebilirsin. Emin değilsen iptal edip ekrana dönebilirsin.
      </p>
      <div class="end-trip-note">
        Bitirilen sefer aktif ekrandan kalkar, raporlardan görüntülenir.
      </div>
    </div>

    <div class="end-trip-actions">
      <button type="button" class="end-trip-btn end-trip-cancel" id="endTripCancel">İptal</button>
      <button type="button" class="end-trip-btn end-trip-ok" id="endTripOk">Seferi Bitir</button>
    </div>
  </div>
</div>

<script>
(function(){
  const form = document.getElementById("endTripForm");
  const overlay = document.getElementById("endTripOverlay");
  const cancel = document.getElementById("endTripCancel");
  const ok = document.getElementById("endTripOk");

  if(!form || !overlay || !cancel || !ok) return;

  let confirmed = false;

  function openModal(){
    overlay.classList.add("show");
    overlay.setAttribute("aria-hidden", "false");
    document.body.style.overflow = "hidden";
  }

  function closeModal(){
    overlay.classList.remove("show");
    overlay.setAttribute("aria-hidden", "true");
    document.body.style.overflow = "";
  }

  form.addEventListener("submit", function(e){
    if(confirmed) return;
    e.preventDefault();
    openModal();
  });

  cancel.addEventListener("click", closeModal);

  overlay.addEventListener("click", function(e){
    if(e.target === overlay) closeModal();
  });

  document.addEventListener("keydown", function(e){
    if(e.key === "Escape" && overlay.classList.contains("show")){
      closeModal();
    }
  });

  function clearTripLocalMemory(){
    try{
      const tripKey = {{ ((trip['route'] ~ '|' ~ trip['plate'])|replace(' ','_')) | tojson | safe }};

      const exactKeys = [
        "liveStop:" + tripKey,
        "passedStops:" + tripKey,
        "boardsMap:" + tripKey,
        "standingTotals:" + tripKey,
        "standingItems:" + tripKey,
        "continueTripStop:" + tripKey,
        "continueTripStop:last",
        "stopFlowSummary:" + tripKey,
        "stopFlowLiveEvents:" + tripKey
      ];

      exactKeys.forEach(k => localStorage.removeItem(k));

      Object.keys(localStorage).forEach(k => {
        if(
          k.includes(tripKey) &&
          (
            k.startsWith("liveStop:") ||
            k.startsWith("passedStops:") ||
            k.startsWith("boardsMap:") ||
            k.startsWith("standingTotals:") ||
            k.startsWith("standingItems:") ||
            k.startsWith("continueTripStop:") ||
            k.startsWith("stopFlowSummary:") ||
            k.startsWith("stopFlowLiveEvents:")
          )
        ){
          localStorage.removeItem(k);
        }
      });
    }catch(_){}
  }

  ok.addEventListener("click", function(){
    confirmed = true;
    clearTripLocalMemory();
    closeModal();
    form.submit();
  });
})();
</script>

<!-- CONTINUE_TTS_BRIDGE_START -->
<script src="/static/seats/voice-tts.js?v=continue-tts-bridge-1"></script>
<!-- CONTINUE_TTS_BRIDGE_END -->

<div class="bag-photo-viewer" id="bagPhotoViewer" aria-hidden="true">
  <div class="bag-viewer-top">
    <div class="bag-viewer-title">
      <div class="bag-viewer-kicker">Bagaj fotoğrafı</div>
      <div class="bag-viewer-name" id="bagViewerTitle">Fotoğraf</div>
    </div>

    <button class="bag-viewer-close" type="button" id="bagViewerClose" aria-label="Kapat">×</button>
  </div>

  <div class="bag-viewer-stage">
    <div class="bag-viewer-img-wrap">
      <img class="bag-viewer-img" id="bagViewerImg" src="" alt="Bagaj fotoğrafı">
    </div>
  </div>

  <div class="bag-viewer-bottom">
    <div class="bag-viewer-caption" id="bagViewerCaption">—</div>

    <div class="bag-viewer-actions">
      <button class="bag-viewer-btn" type="button" id="bagViewerPrev">← Önceki</button>
      <button class="bag-viewer-btn" type="button" id="bagViewerNext">Sonraki →</button>
    </div>
  </div>
</div>

<script id="continue-boot-data">
window.CONTINUE_BOOT = {
  tripId: {{ trip['id'] | tojson | safe }},
  tripDate: {{ (trip['date'] or '') | tojson | safe }},
  tripKey: {{ ((trip['route'] ~ '|' ~ trip['plate'])|replace(' ','_')) | tojson | safe }},

  runtimeGpsKm: {{ (live_runtime.gps_km if live_runtime and live_runtime.gps_km else "") | tojson | safe }},
  runtimeSpeed: {{ (live_runtime.speed if live_runtime else 0) | tojson | safe }},
  runtimeStop: {{ (live_runtime.live_stop if live_runtime and live_runtime.live_stop else "") | tojson | safe }},
  runtimeEta: {{ (live_runtime.eta_main if live_runtime and live_runtime.eta_main else "") | tojson | safe }},

  routeStops: {{ stops | tojson | safe }},
  csrfToken: {{ (csrf_token if csrf_token is defined else "") | tojson | safe }},

  routeCoords: {{ continue_route_coords | default([]) | tojson | safe }},
  scheduleItems: {{ continue_schedule_items | default([]) | tojson | safe }},

  liveBagajCount: {{ (live_current.bagaj_count if live_current and live_current.bagaj_count is defined else 0) | tojson | safe }},
  liveEmanetCount: {{ (live_current.emanet_count if live_current and live_current.emanet_count is defined else (live_current.consignment_count if live_current and live_current.consignment_count is defined else 0)) | tojson | safe }}
};
</script>

<script src="{{ url_for('static', filename='continue/continue_trip_core.js') }}?v=live-stop-lock-v82"></script>
<script src="{{ url_for('static', filename='continue/continue_bag_emanet.js') }}?v=bag-emanet-clean-1"></script>
<script src="{{ url_for('static', filename='continue/continue_flow_refresh.js') }}?v=flow-refresh-1"></script>
<script src="{{ url_for('static', filename='continue/continue_trip_ui.js') }}?v=js-safe-split-1"></script>
<script src="{{ url_for('static', filename='continue/continue_refresh_button_v49.js') }}?v=refresh-v49"></script>
<script src="{{ url_for('static', filename='continue/continue_native_lock_alarm_v85.js') }}?v=native-lock-alarm-v87"></script>
<script src="{{ url_for('static', filename='continue/continue_trip_v99_clean.js') }}?v=v99-clean-{{ trip['id'] }}"></script>

</body>
</html>
'''

CSS = r'''@import url('https://fonts.googleapis.com/css2?family=Rajdhani:wght@400;500;600;700&family=JetBrains+Mono:wght@400;700&display=swap');

:root{
  --v99-bg:#0b0d10;
  --v99-panel:#12151a;
  --v99-panel2:#181c23;
  --v99-border:#1f2530;
  --v99-red:#e03030;
  --v99-red-dim:#3a1010;
  --v99-amber:#e08820;
  --v99-amber-dim:#2c1f08;
  --v99-green:#1db87a;
  --v99-green-dim:#0a2418;
  --v99-blue:#3a8bff;
  --v99-blue-dim:#0d1e38;
  --v99-text:#d8dde8;
  --v99-muted:#5a6478;
  --v99-label:#8a95a8;
}

.v99-live-body{
  background:var(--v99-bg) !important;
  color:var(--v99-text) !important;
  font-family:'Rajdhani',system-ui,-apple-system,BlinkMacSystemFont,sans-serif !important;
  font-size:15px;
  min-height:100vh;
  overflow-x:hidden;
  padding:0 0 92px 0;
}

.v99-live-body *,
.v99-live-body *::before,
.v99-live-body *::after{
  box-sizing:border-box;
}

.v99-live-body a{
  text-decoration:none;
}

.v99-core-hidden{
  position:absolute !important;
  width:1px !important;
  height:1px !important;
  overflow:hidden !important;
  clip:rect(0 0 0 0) !important;
  white-space:nowrap !important;
  opacity:0 !important;
  pointer-events:none !important;
}

/* HEADER */
.v99-hdr{
  display:flex;
  align-items:center;
  justify-content:space-between;
  padding:14px 20px;
  border-bottom:1px solid var(--v99-border);
  background:var(--v99-panel);
}

.v99-hdr-brand{
  display:flex;
  align-items:center;
  gap:10px;
}

.v99-hdr-icon{
  width:34px;
  height:34px;
  background:var(--v99-red);
  border-radius:8px;
  display:grid;
  place-items:center;
  font-size:16px;
  box-shadow:0 0 12px #e0303055;
}

.v99-hdr-title{
  font-size:18px;
  font-weight:700;
  letter-spacing:3px;
  color:#fff;
  line-height:1;
}

.v99-hdr-sub{
  font-size:10px;
  letter-spacing:2px;
  color:var(--v99-muted);
  font-family:'JetBrains Mono',monospace;
  margin-top:4px;
}

.v99-hdr-clock{
  font-family:'JetBrains Mono',monospace;
  font-size:22px;
  font-weight:700;
  color:var(--v99-amber);
  text-shadow:0 0 16px #e0882055;
  letter-spacing:2px;
}

/* ROUTE BAR */
.v99-route-bar{
  background:var(--v99-panel2);
  border-bottom:1px solid var(--v99-border);
  padding:10px 20px;
  display:flex;
  align-items:center;
  gap:12px;
  font-family:'JetBrains Mono',monospace;
  font-size:12px;
  color:var(--v99-label);
}

.v99-route-name{
  color:var(--v99-text);
  font-size:13px;
  font-weight:700;
  letter-spacing:1px;
}

.v99-route-dot{
  color:var(--v99-muted);
}

.v99-live-badge{
  margin-left:auto;
  display:flex;
  align-items:center;
  gap:6px;
  font-size:11px;
  color:var(--v99-red);
  letter-spacing:1px;
  font-weight:700;
}

.v99-live-dot{
  width:7px;
  height:7px;
  background:var(--v99-red);
  border-radius:50%;
  animation:v99-pulse-red 1.4s ease-in-out infinite;
  box-shadow:0 0 6px var(--v99-red);
}

@keyframes v99-pulse-red{
  0%,100%{opacity:1;transform:scale(1);}
  50%{opacity:.4;transform:scale(.7);}
}

/* GAUGES */
.v99-gauges{
  display:grid;
  grid-template-columns:1fr 1fr 1fr;
  gap:1px;
  background:var(--v99-border);
  border-bottom:1px solid var(--v99-border);
}

.v99-gauge-cell{
  background:var(--v99-panel);
  padding:14px 12px;
  display:flex;
  flex-direction:column;
  align-items:center;
  gap:4px;
  min-width:0;
}

.v99-gauge-label{
  font-size:10px;
  letter-spacing:2px;
  color:var(--v99-muted);
  font-family:'JetBrains Mono',monospace;
  text-transform:uppercase;
}

.v99-gauge-val{
  font-family:'JetBrains Mono',monospace;
  font-size:22px;
  font-weight:700;
  color:var(--v99-text);
  line-height:1;
  white-space:nowrap;
}

.v99-gauge-val.amber{
  color:var(--v99-amber);
  text-shadow:0 0 10px #e0882040;
}

.v99-gauge-val.green{
  color:var(--v99-green);
  text-shadow:0 0 10px #1db87a40;
}

.v99-status-val{
  font-size:14px !important;
  letter-spacing:0;
  max-width:100%;
  overflow:hidden;
  text-overflow:ellipsis;
}

.v99-gauge-unit{
  font-size:10px;
  color:var(--v99-muted);
  letter-spacing:1px;
  text-align:center;
}

.v99-occ-bar-track{
  width:80px;
  height:4px;
  background:var(--v99-border);
  border-radius:2px;
  overflow:hidden;
  margin-top:2px;
}

.v99-occ-bar-fill{
  height:100%;
  background:linear-gradient(90deg,var(--v99-green),var(--v99-amber));
  border-radius:2px;
  transition:width 1s ease;
}

.v99-occ-genders{
  display:flex;
  gap:8px;
  font-size:10px;
  font-family:'JetBrains Mono',monospace;
  margin-top:3px;
}

.g-m{color:var(--v99-blue);}
.g-f{color:#e060c0;}
.g-u{color:var(--v99-muted);}

/* MAIN */
.v99-main{
  width:100%;
  max-width:720px;
  margin:0 auto;
}

/* PROXIMITY CARD */
.v99-prox-section{
  padding:20px 20px 0;
}

.v99-prox-card{
  background:var(--v99-panel);
  border:1px solid var(--v99-border);
  border-radius:16px;
  padding:20px;
  position:relative;
  overflow:hidden;
}

.v99-prox-card::before{
  content:'';
  position:absolute;
  inset:0;
  background:repeating-linear-gradient(
    0deg,
    transparent,
    transparent 3px,
    rgba(255,255,255,.012) 3px,
    rgba(255,255,255,.012) 4px
  );
  pointer-events:none;
}

.v99-prox-top{
  display:flex;
  align-items:flex-start;
  gap:20px;
  position:relative;
  z-index:1;
}

.v99-ring-wrap{
  flex-shrink:0;
  position:relative;
  width:110px;
  height:110px;
}

.v99-ring-svg{
  width:110px;
  height:110px;
  transform:rotate(-90deg);
}

.v99-ring-track{
  fill:none;
  stroke:var(--v99-red-dim);
  stroke-width:6;
}

.v99-ring-fill{
  fill:none;
  stroke:var(--v99-red);
  stroke-width:6;
  stroke-linecap:round;
  filter:drop-shadow(0 0 6px var(--v99-red));
  transition:stroke-dashoffset 1.2s cubic-bezier(.4,0,.2,1), stroke .6s ease;
}

.v99-ring-center{
  position:absolute;
  inset:0;
  display:flex;
  flex-direction:column;
  align-items:center;
  justify-content:center;
}

.v99-ring-km{
  font-family:'JetBrains Mono',monospace;
  font-size:24px;
  font-weight:700;
  color:var(--v99-red);
  text-shadow:0 0 14px var(--v99-red);
  line-height:1;
  transition:color .6s ease,text-shadow .6s ease;
}

.v99-ring-km-label{
  font-size:10px;
  letter-spacing:2px;
  color:var(--v99-muted);
  font-family:'JetBrains Mono',monospace;
  margin-top:2px;
}

@keyframes v99-ring-pulse{
  0%,100%{filter:drop-shadow(0 0 6px var(--v99-red));}
  50%{filter:drop-shadow(0 0 18px var(--v99-red)) drop-shadow(0 0 30px var(--v99-red));}
}

.v99-ring-fill.urgent{
  animation:v99-ring-pulse 1s ease-in-out infinite;
}

.v99-prox-info{
  flex:1;
  display:flex;
  flex-direction:column;
  gap:8px;
  min-width:0;
  position:relative;
  z-index:1;
}

.v99-prox-kicker{
  font-size:10px;
  letter-spacing:3px;
  color:var(--v99-muted);
  font-family:'JetBrains Mono',monospace;
  text-transform:uppercase;
}

.v99-prox-stop-name{
  font-size:22px;
  font-weight:700;
  color:#fff;
  line-height:1.1;
  letter-spacing:.5px;
  word-break:break-word;
}

.v99-prox-eta-row{
  display:flex;
  align-items:center;
  gap:8px;
  flex-wrap:wrap;
}

.v99-prox-eta-val{
  font-family:'JetBrains Mono',monospace;
  font-size:18px;
  font-weight:700;
  color:var(--v99-amber);
}

.v99-prox-eta-label{
  font-size:11px;
  color:var(--v99-muted);
  letter-spacing:1px;
}

.v99-status-pill{
  display:inline-flex;
  align-items:center;
  gap:5px;
  padding:4px 10px;
  border-radius:20px;
  font-size:11px;
  font-weight:700;
  letter-spacing:1.5px;
  text-transform:uppercase;
  font-family:'JetBrains Mono',monospace;
  background:var(--v99-red-dim);
  color:var(--v99-red);
  border:1px solid #e0303033;
  margin-top:4px;
  width:fit-content;
}

.v99-prox-metrics{
  display:grid;
  grid-template-columns:1fr 1fr;
  gap:10px;
  margin-top:16px;
  position:relative;
  z-index:1;
}

.v99-pm-cell{
  background:var(--v99-panel2);
  border:1px solid var(--v99-border);
  border-radius:10px;
  padding:12px 14px;
  display:flex;
  align-items:center;
  gap:12px;
  cursor:pointer;
  transition:border-color .2s,background .2s;
  color:inherit;
  font:inherit;
  text-align:left;
  min-width:0;
}

.v99-pm-cell:hover{
  border-color:var(--v99-red);
  background:var(--v99-red-dim);
}

.v99-pm-icon{
  font-size:20px;
  line-height:1;
}

.v99-pm-val{
  font-family:'JetBrains Mono',monospace;
  font-size:18px;
  font-weight:700;
  color:var(--v99-text);
  line-height:1;
}

.v99-pm-lbl{
  font-size:10px;
  color:var(--v99-muted);
  letter-spacing:1.5px;
  margin-top:2px;
}

.v99-dist-track-wrap{
  margin-top:14px;
  position:relative;
  z-index:1;
}

.v99-dist-labels{
  display:flex;
  justify-content:space-between;
  gap:8px;
  font-size:10px;
  font-family:'JetBrains Mono',monospace;
  color:var(--v99-muted);
  margin-bottom:5px;
}

.v99-dist-labels span{
  min-width:0;
  overflow:hidden;
  text-overflow:ellipsis;
  white-space:nowrap;
}

.v99-dist-track{
  height:6px;
  background:var(--v99-border);
  border-radius:3px;
  overflow:hidden;
  position:relative;
}

.v99-dist-fill{
  height:100%;
  background:linear-gradient(90deg,var(--v99-red-dim),var(--v99-red));
  border-radius:3px;
  transition:width 1.2s cubic-bezier(.4,0,.2,1);
  position:relative;
}

.v99-dist-fill::after{
  content:'';
  position:absolute;
  right:0;
  top:-2px;
  width:10px;
  height:10px;
  background:var(--v99-red);
  border-radius:50%;
  box-shadow:0 0 8px var(--v99-red);
}

/* TIMELINE */
.v99-timeline-section{
  padding:20px 20px 0;
}

.v99-section-label{
  font-size:10px;
  letter-spacing:3px;
  color:var(--v99-muted);
  font-family:'JetBrains Mono',monospace;
  margin-bottom:14px;
  display:flex;
  align-items:center;
  gap:8px;
}

.v99-section-label::after{
  content:'';
  flex:1;
  height:1px;
  background:var(--v99-border);
}

.v99-tl{
  display:flex;
  flex-direction:column;
  gap:0;
  position:relative;
}

.v99-tl-item{
  display:flex;
  gap:14px;
  position:relative;
}

.v99-tl-spine{
  display:flex;
  flex-direction:column;
  align-items:center;
  flex-shrink:0;
  width:20px;
}

.v99-tl-node{
  width:14px;
  height:14px;
  border-radius:50%;
  border:2px solid var(--v99-muted);
  background:var(--v99-bg);
  flex-shrink:0;
  z-index:1;
  margin-top:14px;
}

.v99-tl-node.live{
  border-color:var(--v99-red);
  background:var(--v99-red);
  box-shadow:0 0 10px var(--v99-red);
  animation:v99-pulse-red 1.4s ease-in-out infinite;
}

.v99-tl-node.next{
  border-color:var(--v99-amber);
  background:transparent;
}

.v99-tl-node.passed{
  border-color:var(--v99-green);
  background:var(--v99-green);
  opacity:.7;
}

.v99-tl-node.upcoming{
  border-color:var(--v99-border);
  background:transparent;
}

.v99-tl-line{
  flex:1;
  width:1px;
  background:var(--v99-border);
  margin:0 auto;
}

.v99-tl-line.live{
  background:linear-gradient(var(--v99-red),var(--v99-border));
}

.v99-tl-line.passed{
  background:var(--v99-green);
  opacity:.4;
}

.v99-tl-card{
  flex:1;
  background:var(--v99-panel);
  border:1px solid var(--v99-border);
  border-radius:10px;
  padding:12px 14px;
  margin-bottom:10px;
  transition:border-color .2s;
  min-width:0;
}

.v99-tl-card.live-card{
  border-color:#e0303044;
  background:#12100e;
}

.v99-tl-card.next-card{
  border-color:#e0882033;
}

.v99-tl-card-head{
  display:flex;
  justify-content:space-between;
  align-items:flex-start;
  gap:10px;
  margin-bottom:8px;
}

.v99-tl-stop-name{
  font-size:15px;
  font-weight:700;
  color:#fff;
  letter-spacing:.3px;
  min-width:0;
  overflow:hidden;
  text-overflow:ellipsis;
}

.v99-tl-stop-name.muted{
  color:var(--v99-label);
  font-weight:500;
}

.v99-pill{
  font-size:9px;
  font-weight:700;
  letter-spacing:1.5px;
  padding:3px 8px;
  border-radius:20px;
  font-family:'JetBrains Mono',monospace;
  white-space:nowrap;
}

.v99-pill.live{
  background:#3a0a0a;
  color:var(--v99-red);
  border:1px solid #e0303033;
}

.v99-pill.next{
  background:var(--v99-amber-dim);
  color:var(--v99-amber);
  border:1px solid #e0882033;
}

.v99-pill.passed{
  background:var(--v99-green-dim);
  color:var(--v99-green);
  border:1px solid #1db87a33;
}

.v99-pill.upcoming{
  background:var(--v99-panel2);
  color:var(--v99-muted);
  border:1px solid var(--v99-border);
}

.v99-tl-metrics{
  display:flex;
  gap:16px;
  flex-wrap:wrap;
}

.v99-tl-metric{
  display:flex;
  flex-direction:column;
  gap:1px;
  min-width:44px;
}

.v99-tl-m-val{
  font-family:'JetBrains Mono',monospace;
  font-size:14px;
  font-weight:700;
  color:var(--v99-text);
}

.v99-tl-m-lbl{
  font-size:9px;
  color:var(--v99-muted);
  letter-spacing:1px;
}

/* DOCK */
.v99-dock{
  position:fixed !important;
  bottom:0 !important;
  left:0 !important;
  right:0 !important;
  background:var(--v99-panel) !important;
  border-top:1px solid var(--v99-border) !important;
  display:flex !important;
  padding:8px 0 max(env(safe-area-inset-bottom), 8px) !important;
  z-index:100 !important;
  height:auto !important;
  min-height:74px !important;
}

.v99-dock-btn{
  flex:1;
  display:flex !important;
  flex-direction:column;
  align-items:center;
  justify-content:center;
  gap:4px;
  padding:8px 0;
  background:none;
  border:none;
  color:var(--v99-muted) !important;
  font-family:'Rajdhani',sans-serif;
  font-size:11px;
  letter-spacing:1px;
  cursor:pointer;
  transition:color .2s;
  text-decoration:none;
  min-width:0;
}

.v99-dock-btn.active{
  color:var(--v99-red) !important;
}

.v99-dock-btn:hover{
  color:var(--v99-text) !important;
}

.v99-dock-btn i{
  font-size:20px;
  line-height:1;
  font-style:normal;
}

.v99-dock-btn span{
  white-space:nowrap;
}

/* END TRIP */
.v99-end-wrap{
  padding:20px 20px 100px;
  text-align:center;
}

.v99-end-btn{
  width:100%;
  padding:14px;
  background:#1a0a0a;
  border:1px solid #e0303033;
  border-radius:10px;
  color:var(--v99-red);
  font-family:'Rajdhani',sans-serif;
  font-size:14px;
  font-weight:700;
  letter-spacing:2px;
  cursor:pointer;
  transition:background .2s,border-color .2s;
}

.v99-end-btn:hover{
  background:var(--v99-red-dim);
  border-color:var(--v99-red);
}

/* eski CSS çakışmalarını sakinleştir */
.v99-live-body .shell,
.v99-live-body .timeline,
.v99-live-body .journey-card,
.v99-live-body .card,
.v99-live-body .metric-grid{
  all:unset;
}

@media (max-width:380px){
  .v99-hdr{padding:12px 16px;}
  .v99-route-bar{padding:9px 16px;font-size:11px;}
  .v99-prox-section{padding:16px 16px 0;}
  .v99-timeline-section{padding:18px 16px 0;}
  .v99-prox-card{padding:16px;}
  .v99-prox-top{gap:14px;}
  .v99-ring-wrap,
  .v99-ring-svg{
    width:96px;
    height:96px;
  }
  .v99-prox-stop-name{font-size:20px;}
  .v99-gauge-val{font-size:19px;}
  .v99-tl-metrics{gap:12px;}
}

@media (min-width:700px){
  .v99-main{
    max-width:760px;
  }
}
'''

JS = r'''(function(){
  "use strict";

  const CIRC = 276.46;
  const MAX_KM = 48;

  function q(sel){
    return document.querySelector(sel);
  }

  function text(sel){
    const el = q(sel);
    return el ? (el.textContent || "").trim() : "";
  }

  function parseKm(raw){
    raw = String(raw || "").replace(",", ".").trim();
    const m = raw.match(/-?\d+(?:\.\d+)?/);
    if(!m) return null;
    const n = Number(m[0]);
    return Number.isFinite(n) ? n : null;
  }

  function cleanSpeed(raw){
    const n = parseKm(raw);
    if(n === null) return "0";
    return String(Math.max(0, Math.round(n)));
  }

  function setRing(km){
    const ring = q("#ringFill");
    const ringKm = q("#ringKm");
    if(!ring || !ringKm) return;

    let display = km;
    if(km === null){
      display = null;
    }

    let safeKm = display === null ? MAX_KM : Math.max(0, display);
    let ratio = Math.max(0, Math.min(1, 1 - safeKm / MAX_KM));
    let offset = CIRC * (1 - ratio);

    ring.style.strokeDashoffset = String(offset);

    if(display === null){
      ringKm.textContent = "—";
      ring.style.stroke = "#5a6478";
      ring.style.filter = "drop-shadow(0 0 4px #5a6478)";
      ring.classList.remove("urgent");
      ringKm.style.color = "#5a6478";
      ringKm.style.textShadow = "none";
      return;
    }

    let label = safeKm <= 0 ? "0" : (safeKm % 1 === 0 ? String(safeKm) : safeKm.toFixed(1));
    ringKm.textContent = label;

    if(safeKm <= 5){
      ring.style.stroke = "#e03030";
      ring.style.filter = "drop-shadow(0 0 8px #e03030)";
      ring.classList.add("urgent");
      ringKm.style.color = "#e03030";
      ringKm.style.textShadow = "0 0 18px #e03030";
    }else if(safeKm <= 15){
      ring.style.stroke = "#e08820";
      ring.style.filter = "drop-shadow(0 0 8px #e08820)";
      ring.classList.remove("urgent");
      ringKm.style.color = "#e08820";
      ringKm.style.textShadow = "0 0 12px #e08820";
    }else{
      ring.style.stroke = "#3a8bff";
      ring.style.filter = "drop-shadow(0 0 6px #3a8bff)";
      ring.classList.remove("urgent");
      ringKm.style.color = "#3a8bff";
      ringKm.style.textShadow = "0 0 10px #3a8bff";
    }
  }

  function setRouteProgress(){
    const boot = window.CONTINUE_BOOT || {};
    const stops = Array.isArray(boot.routeStops) ? boot.routeStops : [];
    const current = text("#liveCurrentStopName");
    const bar = q("#routeBar");
    const pctEl = q("#distPct");

    if(!bar || !pctEl || !stops.length || !current){
      return;
    }

    let idx = stops.findIndex(s => String(s || "").trim().toLowerCase() === current.trim().toLowerCase());

    if(idx < 0){
      idx = stops.findIndex(s => String(s || "").trim().toLowerCase().includes(current.trim().toLowerCase()));
    }

    if(idx < 0) return;

    const pct = stops.length <= 1 ? 0 : Math.round((idx / (stops.length - 1)) * 100);
    bar.style.width = Math.max(0, Math.min(100, pct)) + "%";
    pctEl.textContent = "%" + pct + " tamamlandı";
  }

  function setClock(){
    const el = q("#liveClockText");
    if(!el) return;
    const now = new Date();
    const h = String(now.getHours()).padStart(2, "0");
    const m = String(now.getMinutes()).padStart(2, "0");
    el.textContent = h + ":" + m;
  }

  function sync(){
    const km = parseKm(text("#liveDistanceValue"));
    setRing(km);

    const speedVisual = q("#v99SpeedVal");
    if(speedVisual){
      speedVisual.textContent = cleanSpeed(text("#liveSpeedText"));
    }

    const status = text("#liveTopStatusText");
    const sub = q("#v99StatusSub");
    if(sub && status){
      sub.textContent = /erken|geç/i.test(status) ? "tahmini durum" : "canlı takip";
    }

    setRouteProgress();
  }

  setClock();
  sync();

  setInterval(setClock, 10000);
  setInterval(sync, 700);

  document.addEventListener("continueEtaUpdated", sync);
  window.addEventListener("storage", sync);
  window.MuavinV99CleanSync = sync;
})();
'''

WEB_TPL.write_text(TEMPLATE, encoding="utf-8")
WEB_CSS.parent.mkdir(parents=True, exist_ok=True)
WEB_JS.parent.mkdir(parents=True, exist_ok=True)
WEB_CSS.write_text(CSS, encoding="utf-8")
WEB_JS.write_text(JS, encoding="utf-8")

print("✅ web template yazıldı:", WEB_TPL)
print("✅ web css yazıldı:", WEB_CSS)
print("✅ web js yazıldı:", WEB_JS)

if AND_TPL.parent.exists():
    AND_TPL.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(WEB_TPL, AND_TPL)
    print("✅ android template senkron:", AND_TPL)

if AND_CSS.parent.exists():
    AND_CSS.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(WEB_CSS, AND_CSS)
    shutil.copy2(WEB_JS, AND_JS)
    print("✅ android css/js senkron")

print()
print("===== KONTROL =====")
txt = WEB_TPL.read_text(encoding="utf-8", errors="ignore")
for key in [
    "continue_trip_v99_clean.css",
    "continue_trip_v99_clean.js",
    "v99-prox-card",
    "liveCurrentStopName",
    "liveDistanceValue",
    "liveOffloadMetric",
    "liveBagajMetric",
    "liveStopSheet",
    "bagPhotoViewer",
    "CONTINUE_BOOT",
    "v97_proximity_preview.css",
    "v97_real_data.css",
]:
    print(("VAR  " if key in txt else "YOK  ") + key)

print()
print("===== SONUC =====")
print("✅ V99 CLEAN tek yama tamam. Preview CSS yok. Demo JS yok.")
