from pathlib import Path
from datetime import datetime
import shutil

ROOT = Path(".").resolve()
STAMP = datetime.now().strftime("%Y%m%d-%H%M%S")

WEB_TPL = ROOT / "templates/continue_trip.html"
AND_TPL = ROOT / "android_app/app/src/main/python/templates/continue_trip.html"

WEB_CSS_PREVIEW = ROOT / "static/continue/v97_proximity_preview.css"
AND_CSS_PREVIEW = ROOT / "android_app/app/src/main/python/static/continue/v97_proximity_preview.css"

WEB_JS_PREVIEW = ROOT / "static/continue/v97_proximity_preview.js"
AND_JS_PREVIEW = ROOT / "android_app/app/src/main/python/static/continue/v97_proximity_preview.js"

WEB_HTML_PREVIEW = ROOT / "static/continue/v97_proximity_preview.html"
AND_HTML_PREVIEW = ROOT / "android_app/app/src/main/python/static/continue/v97_proximity_preview.html"

WEB_CSS = ROOT / "static/continue/v97_real_data.css"
AND_CSS = ROOT / "android_app/app/src/main/python/static/continue/v97_real_data.css"

WEB_JS = ROOT / "static/continue/v97_real_bind.js"
AND_JS = ROOT / "android_app/app/src/main/python/static/continue/v97_real_bind.js"

print("===== V98 V97 GERÇEK VERİ BAĞLAMA =====")
print("ROOT:", ROOT)

if not WEB_TPL.exists():
    raise SystemExit("❌ templates/continue_trip.html yok")

if not WEB_CSS_PREVIEW.exists():
    raise SystemExit("❌ static/continue/v97_proximity_preview.css yok")

def backup(p: Path):
    if p.exists():
        b = p.with_name(p.name + f".bak-v98-{STAMP}")
        shutil.copy2(p, b)
        print("YEDEK:", b.relative_to(ROOT))

backup(WEB_TPL)
backup(AND_TPL)
backup(WEB_CSS)
backup(AND_CSS)
backup(WEB_JS)
backup(AND_JS)

TPL = r"""<!doctype html>
<html lang="tr">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
  <title>Canlı Durak Akışı</title>

  <link rel="stylesheet" href="{{ url_for('static', filename='continue/continue_trip.css') }}?v=refresh-v49">
  <link rel="stylesheet" href="{{ url_for('static', filename='continue/v97_proximity_preview.css') }}?v=v97-real-1">
  <link rel="stylesheet" href="{{ url_for('static', filename='continue/v97_real_data.css') }}?v=v98-{{ trip['id'] }}">
</head>

<body class="v97-real-page">

<header class="v97-hdr">
  <div class="v97-brand">
    <div class="v97-logo">🎙️</div>
    <div>
      <div class="v97-title">MUAVİN</div>
      <div class="v97-sub">ASİSTAN V97</div>
    </div>
  </div>

  <div class="v97-clock" id="liveClockText">--:--</div>
</header>

<section class="v97-route">
  <div class="v97-route-main">
    {{ (trip["route"] or "DENİZLİ → İSTANBUL")|replace("–", "→")|replace("-", "→") }}
  </div>

  <div class="v97-route-plate">
    · {{ trip["plate"] or "45KH999" }}
  </div>

  <div class="v97-route-live">
    <span class="v97-live-dot"></span>
    CANLI
  </div>
</section>

<section class="v97-gauges">
  <div class="v97-gauge-cell">
    <div class="v97-gauge-label">HIZ</div>
    <div class="v97-gauge-val amber" id="v97SpeedVal">
      {{ live_current.speed if live_current and live_current.speed is defined else 0 }}
    </div>
    <div class="v97-gauge-unit">km/sa</div>
  </div>

  <div class="v97-gauge-cell">
    <div class="v97-gauge-label">DOLULUK</div>
    <div class="v97-gauge-val">
      {{ live_summary.passenger_count or 0 }}/{{ live_summary.total_seats or 40 }}
    </div>

    <div class="v97-occ-track">
      <div class="v97-occ-fill" style="width:{{ (((live_summary.passenger_count or 0) / (live_summary.total_seats or 1)) * 100)|round(0) }}%"></div>
    </div>

    <div class="v97-gender">
      <span class="g-m">♂ {{ live_summary.male_count or 0 }}</span>
      <span class="g-f">♀ {{ live_summary.female_count or 0 }}</span>
    </div>
  </div>

  <div class="v97-gauge-cell">
    <div class="v97-gauge-label">DURUM</div>
    <div class="v97-gauge-val green" id="liveTopStatusText">
      {{ live_current.status or "Planında" }}
    </div>
    <div class="v97-gauge-unit" id="v97StatusSub">canlı takip</div>
  </div>
</section>

<section class="v97-shell">

  <article class="v97-prox-card live-summary-trigger" id="liveCurrentCard" role="button" tabindex="0" aria-label="Canlı durak özetini aç">

    <div class="v97-prox-top">
      <div class="v97-ring-wrap">
        <svg class="v97-ring" viewBox="0 0 110 110" aria-hidden="true">
          <circle class="v97-ring-track" cx="55" cy="55" r="44"></circle>
          <circle class="v97-ring-fill" id="ringFill" cx="55" cy="55" r="44"
            stroke-dasharray="276.46"
            stroke-dashoffset="276.46"></circle>
        </svg>

        <div class="v97-ring-center">
          <div id="ringKm">—</div>
          <div>KM</div>
        </div>
      </div>

      <div class="v97-info">
        <div class="v97-kicker">ŞU ANKİ DURAK</div>

        <div class="v97-stop-name" id="liveCurrentStopName">
          {{ (live_runtime.live_stop if live_runtime and live_runtime.live_stop else live_current.name) or "Durak seçilmedi" }}
        </div>

        <div class="v97-eta-line">
          <span id="v97EtaValue">
            {{ (live_runtime.eta_main if live_runtime and live_runtime.eta_main else live_current.eta) or "-" }}
          </span>
          <small>TAHMİNİ VARIŞ</small>
        </div>

        <div class="v97-live-pill">
          <span class="v97-live-dot"></span>
          CANLI TAKİP
        </div>
      </div>
    </div>

    <div class="v97-mini-grid">
      <button class="v97-mini-card" type="button" id="liveOffloadMetric" data-kind="offload" aria-label="Bu durakta inecek koltukları göster">
        <span class="v97-mini-icon">🧍</span>
        <b id="liveOffloadCount">{{ live_current.off_count or 0 }}</b>
        <small>İNECEK YOLCU</small>
      </button>

      <button class="v97-mini-card" type="button" id="liveBagajMetric" data-kind="bagaj" aria-label="Bu durakta indirilecek bagajları göster">
        <span class="v97-mini-icon">🧳</span>
        <b id="liveBagajCount">{{ live_current.bagaj_count or 0 }}</b>
        <span id="liveEmanetCount" hidden>{{ live_current.emanet_count or 0 }}</span>
        <small>BAGAJ</small>
      </button>
    </div>

    <div class="v97-route-progress">
      <div class="v97-route-progress-labels">
        <span>{{ stats.first_stop or "Başlangıç" }}</span>
        <span id="routePct">—</span>
        <span>{{ stats.last_stop or "Varış" }}</span>
      </div>

      <div class="v97-progress-track">
        <div class="v97-progress-fill" id="routeBar" style="width:0%"></div>
      </div>
    </div>

    <div class="v97-functional-hidden" aria-hidden="true">
      <span id="liveSpeedText">
        {{ live_current.speed if live_current and live_current.speed is defined else (live_runtime.speed if live_runtime else 0) }} km/sa
      </span>

      <b id="liveEtaValue">
        {{ (live_runtime.eta_main if live_runtime and live_runtime.eta_main else live_current.eta) or "-" }}
      </b>

      <b id="liveDistanceValue"
         class="stop-distance-value"
         data-stop-name="{{ (live_runtime.live_stop if live_runtime and live_runtime.live_stop else live_current.name) or '' }}">
        {{ (live_runtime.gps_km if live_runtime and live_runtime.gps_km else live_current.distance) or "-" }}
      </b>
    </div>

  </article>

  <section class="v97-timeline-section">
    <div class="v97-section-title">GÜZERGAH</div>

    <div class="v97-timeline" id="timeline">
      {% for stop in live_stops %}
      <article class="v97-tl-item">
        <div class="v97-tl-spine">
          <span class="v97-tl-node {{ stop.kind }}"></span>
          {% if not loop.last %}
            <span class="v97-tl-line {{ stop.kind }}"></span>
          {% endif %}
        </div>

        <div class="v97-tl-card {% if stop.kind == 'live' %}live-card{% elif stop.kind == 'next' %}next-card{% endif %}">
          <div class="v97-tl-head">
            <h3>{{ stop.name }}</h3>

            {% if stop.kind == "live" %}
              <span class="v97-pill live">● CANLI</span>
            {% elif stop.kind == "next" %}
              <span class="v97-pill next">→ SIRADAKİ</span>
            {% elif stop.kind == "passed" %}
              <span class="v97-pill passed">✓ GEÇİLDİ</span>
            {% else %}
              <span class="v97-pill upcoming">{{ stop.status }}</span>
            {% endif %}
          </div>

          <div class="v97-tl-metrics">
            <div>
              <b>{{ stop.eta }}</b>
              <small>VARIŞ</small>
            </div>

            <div>
              <b class="stop-distance-value" data-stop-name="{{ stop.name }}">{{ stop.distance }}</b>
              <small>MESAFE</small>
            </div>

            <div>
              <b>{{ stop.off_count }}</b>
              <small>İNECEK</small>
            </div>

            <div>
              <b>{{ stop.bagaj_label }}</b>
              <small>BAGAJ</small>
            </div>
          </div>
        </div>
      </article>
      {% endfor %}
    </div>
  </section>

  <div class="v97-end-wrap">
    <form id="endTripForm" method="post" action="{{ url_for('end_trip') }}">
      {% if csrf_token is defined %}
        <input type="hidden" name="csrf_token" value="{{ csrf_token }}">
      {% endif %}
      <button class="v97-end-btn" type="submit">⛔ SEFERİ BİTİR</button>
    </form>
  </div>

</section>

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

<nav class="v97-dock">
  <a class="v97-dock-item active" id="continueSeatMapBtn" href="{{ url_for('seats_page') }}">
    <i>🚌</i>
    <span>CANLI</span>
  </a>

  <a class="v97-dock-item" href="{{ url_for('seats_page') }}">
    <i>💺</i>
    <span>KOLTUK</span>
  </a>

  <a class="v97-dock-item" href="{{ url_for('passenger_control') }}">
    <i>👥</i>
    <span>YOLCU</span>
  </a>

  <a class="v97-dock-item" href="{{ url_for('live_map_page') }}">
    <i>🗺️</i>
    <span>HARİTA</span>
  </a>

  <button class="v97-dock-item" type="button">
    <i>📣</i>
    <span>ANONS</span>
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
<script src="{{ url_for('static', filename='continue/v97_real_bind.js') }}?v=v98-{{ trip['id'] }}"></script>

</body>
</html>
"""

CSS = r"""
/* V97_REAL_DATA_CSS_V98 */
.v97-real-page{
  padding-bottom:92px !important;
  background:#0b0d10 !important;
  overflow-x:hidden !important;
}

.v97-functional-hidden{
  position:absolute !important;
  width:1px !important;
  height:1px !important;
  overflow:hidden !important;
  clip:rect(0 0 0 0) !important;
  white-space:nowrap !important;
  opacity:0 !important;
  pointer-events:none !important;
}

.v97-route{
  display:flex !important;
  align-items:center !important;
  gap:14px !important;
}

.v97-route-main{
  flex:1 !important;
  min-width:0 !important;
  overflow:hidden !important;
  text-overflow:ellipsis !important;
}

.v97-route-plate{
  flex:0 0 auto !important;
}

.v97-route-live{
  flex:0 0 auto !important;
  display:flex !important;
  align-items:center !important;
  gap:8px !important;
  color:#ff2d55 !important;
  font-weight:900 !important;
  letter-spacing:4px !important;
}

.v97-live-dot{
  width:8px !important;
  height:8px !important;
  border-radius:999px !important;
  background:#ff2d55 !important;
  box-shadow:0 0 18px rgba(255,45,85,.95) !important;
  display:inline-block !important;
  animation:v97LiveDotPulse 1.4s ease-in-out infinite !important;
}

@keyframes v97LiveDotPulse{
  0%,100%{opacity:1;transform:scale(1);}
  50%{opacity:.45;transform:scale(.72);}
}

.v97-occ-track{
  width:86px !important;
  height:6px !important;
  border-radius:999px !important;
  background:#252b38 !important;
  overflow:hidden !important;
  margin-top:6px !important;
}

.v97-occ-fill{
  height:100% !important;
  border-radius:999px !important;
  background:linear-gradient(90deg,#28d17c,#f0a52a) !important;
}

.v97-prox-card{
  cursor:pointer !important;
}

.v97-mini-card{
  border:1px solid rgba(148,163,184,.16) !important;
  background:#151922 !important;
  border-radius:18px !important;
  color:#d8dde8 !important;
  min-height:110px !important;
  display:flex !important;
  align-items:center !important;
  justify-content:center !important;
  gap:14px !important;
  padding:14px !important;
  font:inherit !important;
  text-align:left !important;
  box-shadow:inset 0 1px 0 rgba(255,255,255,.04) !important;
}

.v97-mini-card:active{
  transform:scale(.985) !important;
}

.v97-mini-icon{
  font-size:28px !important;
  line-height:1 !important;
}

.v97-mini-card b{
  font-size:42px !important;
  line-height:1 !important;
  color:#f2f5ff !important;
  font-weight:900 !important;
}

.v97-mini-card small{
  color:#8a95a8 !important;
  font-size:18px !important;
  letter-spacing:5px !important;
  font-weight:900 !important;
  line-height:1.1 !important;
}

.v97-route-progress-labels{
  display:flex !important;
  align-items:center !important;
  justify-content:space-between !important;
  gap:8px !important;
  color:#8a95a8 !important;
  letter-spacing:3px !important;
  font-family:"JetBrains Mono",monospace !important;
  font-size:15px !important;
  margin-bottom:8px !important;
  text-transform:uppercase !important;
}

.v97-progress-track{
  width:100% !important;
  height:8px !important;
  border-radius:999px !important;
  background:#252b38 !important;
  overflow:hidden !important;
}

.v97-progress-fill{
  height:100% !important;
  width:0% !important;
  border-radius:999px !important;
  background:linear-gradient(90deg,#7f1018,#ff2d55) !important;
  transition:width .7s ease !important;
}

.v97-timeline{
  padding-bottom:24px !important;
}

.v97-tl-item{
  display:flex !important;
  gap:18px !important;
  position:relative !important;
}

.v97-tl-spine{
  width:44px !important;
  flex:0 0 44px !important;
  display:flex !important;
  align-items:center !important;
  flex-direction:column !important;
}

.v97-tl-node{
  width:20px !important;
  height:20px !important;
  border-radius:999px !important;
  margin-top:24px !important;
  border:3px solid #313849 !important;
  background:#0b0d10 !important;
  box-shadow:none !important;
}

.v97-tl-node.passed{
  background:#1db87a !important;
  border-color:#1db87a !important;
  box-shadow:0 0 14px rgba(29,184,122,.35) !important;
}

.v97-tl-node.live{
  background:#e03030 !important;
  border-color:#e03030 !important;
  box-shadow:0 0 18px rgba(224,48,48,.8) !important;
}

.v97-tl-node.next{
  border-color:#e08820 !important;
  background:transparent !important;
}

.v97-tl-line{
  width:2px !important;
  min-height:78px !important;
  flex:1 !important;
  background:#252b38 !important;
}

.v97-tl-line.passed{
  background:rgba(29,184,122,.45) !important;
}

.v97-tl-line.live{
  background:linear-gradient(#e03030,#252b38) !important;
}

.v97-tl-card{
  flex:1 !important;
  background:#12151a !important;
  border:1px solid #1f2530 !important;
  border-radius:18px !important;
  padding:18px 20px !important;
  margin-bottom:18px !important;
}

.v97-tl-card.live-card{
  border-color:rgba(224,48,48,.38) !important;
  background:#130f10 !important;
}

.v97-tl-card.next-card{
  border-color:rgba(224,136,32,.38) !important;
}

.v97-tl-head{
  display:flex !important;
  align-items:center !important;
  justify-content:space-between !important;
  gap:12px !important;
  margin-bottom:14px !important;
}

.v97-tl-head h3{
  color:#f4f6fb !important;
  font-size:27px !important;
  font-weight:900 !important;
  margin:0 !important;
}

.v97-pill{
  border-radius:999px !important;
  padding:7px 14px !important;
  font-family:"JetBrains Mono",monospace !important;
  letter-spacing:3px !important;
  font-weight:900 !important;
  font-size:12px !important;
  white-space:nowrap !important;
}

.v97-pill.live{
  color:#ff6b83 !important;
  background:#3a1018 !important;
  border:1px solid rgba(255,45,85,.35) !important;
}

.v97-pill.next{
  color:#e08820 !important;
  background:#2c1f08 !important;
  border:1px solid rgba(224,136,32,.35) !important;
}

.v97-pill.passed{
  color:#1db87a !important;
  background:#0a2418 !important;
  border:1px solid rgba(29,184,122,.35) !important;
}

.v97-pill.upcoming{
  color:#8a95a8 !important;
  background:#181c23 !important;
  border:1px solid #1f2530 !important;
}

.v97-tl-metrics{
  display:grid !important;
  grid-template-columns:repeat(4,1fr) !important;
  gap:10px !important;
}

.v97-tl-metrics b{
  display:block !important;
  color:#d8dde8 !important;
  font-family:"JetBrains Mono",monospace !important;
  font-size:22px !important;
  font-weight:900 !important;
  line-height:1 !important;
  white-space:nowrap !important;
}

.v97-tl-metrics small{
  display:block !important;
  color:#6d7689 !important;
  font-size:12px !important;
  letter-spacing:2px !important;
  margin-top:7px !important;
  font-weight:900 !important;
}

.v97-end-wrap{
  padding:10px 0 30px !important;
}

.v97-end-btn{
  width:100% !important;
  border:1px solid rgba(224,48,48,.35) !important;
  background:#1b0c10 !important;
  color:#ff6b83 !important;
  border-radius:16px !important;
  padding:16px !important;
  font-weight:900 !important;
  letter-spacing:3px !important;
  font-size:17px !important;
}

.v97-dock{
  position:fixed !important;
  left:0 !important;
  right:0 !important;
  bottom:0 !important;
  z-index:120 !important;
  display:grid !important;
  grid-template-columns:repeat(5,1fr) !important;
  background:#12151a !important;
  border-top:1px solid #1f2530 !important;
  padding:8px 0 calc(8px + env(safe-area-inset-bottom,0px)) !important;
}

.v97-dock-item{
  color:#6d7689 !important;
  text-decoration:none !important;
  border:0 !important;
  background:transparent !important;
  display:flex !important;
  flex-direction:column !important;
  align-items:center !important;
  justify-content:center !important;
  gap:5px !important;
  font-family:"Rajdhani",system-ui,sans-serif !important;
  letter-spacing:3px !important;
  font-size:14px !important;
}

.v97-dock-item i{
  font-style:normal !important;
  font-size:27px !important;
  line-height:1 !important;
}

.v97-dock-item.active{
  color:#ff2d55 !important;
}

@media(max-width:420px){
  .v97-route{
    padding-left:18px !important;
    padding-right:18px !important;
  }

  .v97-route-main{
    font-size:25px !important;
    line-height:1.1 !important;
  }

  .v97-route-plate{
    font-size:18px !important;
  }

  .v97-prox-top{
    gap:18px !important;
  }

  .v97-mini-card{
    min-height:96px !important;
  }

  .v97-mini-card b{
    font-size:36px !important;
  }

  .v97-mini-card small{
    font-size:15px !important;
    letter-spacing:4px !important;
  }

  .v97-tl-card{
    padding:16px !important;
  }

  .v97-tl-head h3{
    font-size:24px !important;
  }

  .v97-tl-metrics{
    gap:7px !important;
  }

  .v97-tl-metrics b{
    font-size:19px !important;
  }
}
"""

JS = r"""
/* V97_REAL_BIND_JS_V98 */
(function(){
  const CIRC = 276.46;
  const BOOT = window.CONTINUE_BOOT || {};
  let maxKm = 48;

  function q(sel){
    return document.querySelector(sel);
  }

  function text(sel){
    const el = q(sel);
    return el ? String(el.textContent || "").trim() : "";
  }

  function setText(sel, value){
    const el = q(sel);
    if(el) el.textContent = value;
  }

  function parseKm(raw){
    let s = String(raw || "").trim().toLocaleLowerCase("tr-TR");
    if(!s || s === "—" || s === "-") return NaN;

    s = s.replace(",", ".");

    const n = Number((s.match(/-?\d+(\.\d+)?/) || [""])[0]);
    if(!Number.isFinite(n)) return NaN;

    if(/\bm\b/.test(s) && !/\bkm\b/.test(s)){
      return n / 1000;
    }

    return n;
  }

  function formatRingNumber(km){
    if(!Number.isFinite(km)) return "—";
    if(km <= 0) return "0";
    if(km < 1) return km.toFixed(2);
    if(km < 10) return km.toFixed(1).replace(".0", "");
    return String(Math.round(km));
  }

  function colorRing(km, ring, ringKm){
    if(!ring || !ringKm) return;

    ring.classList.remove("urgent");

    if(Number.isFinite(km) && km <= 5){
      ring.style.stroke = "#e03030";
      ring.style.filter = "drop-shadow(0 0 8px #e03030)";
      ring.classList.add("urgent");
      ringKm.style.color = "#e03030";
      ringKm.style.textShadow = "0 0 18px #e03030";
    }else if(Number.isFinite(km) && km <= 15){
      ring.style.stroke = "#e08820";
      ring.style.filter = "drop-shadow(0 0 8px #e08820)";
      ringKm.style.color = "#e08820";
      ringKm.style.textShadow = "0 0 12px #e08820";
    }else{
      ring.style.stroke = "#3a8bff";
      ring.style.filter = "drop-shadow(0 0 6px #3a8bff)";
      ringKm.style.color = "#3a8bff";
      ringKm.style.textShadow = "0 0 10px #3a8bff";
    }
  }

  function updateRing(){
    const distRaw = text("#liveDistanceValue");
    const km = parseKm(distRaw);
    const ring = q("#ringFill");
    const ringKm = q("#ringKm");

    if(!ring || !ringKm) return;

    if(!Number.isFinite(km)){
      ring.style.strokeDashoffset = CIRC;
      ringKm.textContent = "—";
      return;
    }

    if(km > maxKm){
      maxKm = Math.max(10, Math.ceil(km / 10) * 10);
    }

    const ratio = Math.max(0, Math.min(1, 1 - (km / maxKm)));
    ring.style.strokeDashoffset = CIRC * (1 - ratio);
    ringKm.textContent = formatRingNumber(km);
    colorRing(km, ring, ringKm);
  }

  function updateSpeed(){
    const raw = text("#liveSpeedText");
    const n = Number((raw.match(/\d+/) || ["0"])[0]);
    setText("#v97SpeedVal", Number.isFinite(n) ? String(n) : "0");
  }

  function updateEta(){
    const eta = text("#liveEtaValue");
    if(eta){
      setText("#v97EtaValue", eta);
    }

    const status = text("#liveTopStatusText");
    const sub = q("#v97StatusSub");
    if(sub){
      if(/erken/i.test(status)) sub.textContent = "erken";
      else if(/ge[cç]/i.test(status)) sub.textContent = "gecikme";
      else sub.textContent = "canlı takip";
    }
  }

  function norm(v){
    return String(v || "")
      .toLocaleLowerCase("tr-TR")
      .replace(/ı/g, "i")
      .replace(/İ/g, "i")
      .replace(/\s+/g, " ")
      .trim();
  }

  function updateRouteProgress(){
    const stops = Array.isArray(BOOT.routeStops) ? BOOT.routeStops : [];
    const live = norm(text("#liveCurrentStopName"));

    const pctEl = q("#routePct");
    const bar = q("#routeBar");

    if(!stops.length || !live){
      if(pctEl) pctEl.textContent = "—";
      if(bar) bar.style.width = "0%";
      return;
    }

    let idx = stops.findIndex(s => norm(s) === live);

    if(idx < 0){
      const current = Array.from(document.querySelectorAll(".v97-tl-card.live-card h3"))
        .map(x => norm(x.textContent))
        .find(Boolean);
      if(current){
        idx = stops.findIndex(s => norm(s) === current);
      }
    }

    if(idx < 0){
      if(pctEl) pctEl.textContent = "—";
      return;
    }

    const denom = Math.max(1, stops.length - 1);
    const pct = Math.max(0, Math.min(100, Math.round((idx / denom) * 100)));

    if(pctEl) pctEl.textContent = "%" + pct + " tamamlandı";
    if(bar) bar.style.width = pct + "%";
  }

  function updateClock(){
    const d = new Date();
    const h = String(d.getHours()).padStart(2, "0");
    const m = String(d.getMinutes()).padStart(2, "0");
    setText("#liveClockText", h + ":" + m);
  }

  function sync(){
    updateClock();
    updateSpeed();
    updateEta();
    updateRing();
    updateRouteProgress();
  }

  if(document.readyState === "loading"){
    document.addEventListener("DOMContentLoaded", sync);
  }else{
    sync();
  }

  setInterval(sync, 700);

  window.addEventListener("continueEtaUpdated", sync);
  window.addEventListener("storage", sync);
})();
"""

WEB_TPL.write_text(TPL, encoding="utf-8")
WEB_CSS.write_text(CSS, encoding="utf-8")
WEB_JS.write_text(JS, encoding="utf-8")

print("WEB template yazıldı:", WEB_TPL.relative_to(ROOT))
print("WEB css yazıldı:", WEB_CSS.relative_to(ROOT))
print("WEB js yazıldı:", WEB_JS.relative_to(ROOT))

# Android sync
AND_TPL.parent.mkdir(parents=True, exist_ok=True)
AND_CSS.parent.mkdir(parents=True, exist_ok=True)
AND_JS.parent.mkdir(parents=True, exist_ok=True)

AND_TPL.write_text(WEB_TPL.read_text(encoding="utf-8"), encoding="utf-8")
AND_CSS.write_text(WEB_CSS.read_text(encoding="utf-8"), encoding="utf-8")
AND_JS.write_text(WEB_JS.read_text(encoding="utf-8"), encoding="utf-8")

print("ANDROID template sync:", AND_TPL.relative_to(ROOT))
print("ANDROID css sync:", AND_CSS.relative_to(ROOT))
print("ANDROID js sync:", AND_JS.relative_to(ROOT))

# Preview dosyalarını Android static içine de kopyala
for src, dst in [
    (WEB_CSS_PREVIEW, AND_CSS_PREVIEW),
    (WEB_JS_PREVIEW, AND_JS_PREVIEW),
    (WEB_HTML_PREVIEW, AND_HTML_PREVIEW),
]:
    if src.exists():
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst)
        print("ANDROID preview sync:", dst.relative_to(ROOT))

print("===== KONTROL =====")
for p in [WEB_TPL, AND_TPL, WEB_CSS, AND_CSS, WEB_JS, AND_JS]:
    print(("VAR " if p.exists() else "YOK "), p.relative_to(ROOT), p.stat().st_size if p.exists() else "")

print("===== TAMAM V98 =====")
print("Canlı Durak ekranını normal uygulama içinden aç. /static preview değil.")
