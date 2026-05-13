/* Muavin Canlı Harita - taşınmış ek JS blokları */


/* MUAVIN_GOOGLE_LOCATION_V2_JS */
(function () {
  if (window.MUAVIN_GOOGLE_LOCATION_V2) return;
  window.MUAVIN_GOOGLE_LOCATION_V2 = true;

  let gmMarker = null;
  let accuracyCircle = null;
  let lastLatLng = null;
  let firstFocusDone = false;
  let following = true;
  let locateBtn = null;
  let internalMove = false;

  function asNumber(v) {
    v = Number(v);
    return Number.isFinite(v) ? v : null;
  }

  function getMap() {
    if (window.MUAVIN_LIVE_MAP && typeof window.MUAVIN_LIVE_MAP.addLayer === "function") {
      return window.MUAVIN_LIVE_MAP;
    }

    if (window.map && typeof window.map.addLayer === "function") {
      return window.map;
    }

    for (const key of Object.keys(window)) {
      try {
        const v = window[key];
        if (
          v &&
          v._container &&
          typeof v.addLayer === "function" &&
          typeof v.setView === "function" &&
          v._container.classList &&
          v._container.classList.contains("leaflet-container")
        ) {
          return v;
        }
      } catch (e) {}
    }

    return null;
  }

  function makeIcon() {
    return L.divIcon({
      className: "muavin-gm-marker-icon",
      iconSize: [44, 44],
      iconAnchor: [22, 22],
      html: `
        <div class="muavin-gm-live-marker" aria-label="Canlı konum">
          <div class="muavin-gm-aura"></div>
          <div class="muavin-gm-dot"></div>
        </div>
      `
    });
  }

  function focusToLocation(map, zoom) {
    if (!lastLatLng) return;

    internalMove = true;
    map.setView(lastLatLng, Math.max(map.getZoom ? map.getZoom() : 15, zoom || 16), {
      animate: true
    });

    setTimeout(function () {
      internalMove = false;
    }, 650);
  }

  function setButtonState() {
    if (!locateBtn) return;

    locateBtn.classList.toggle("has-no-location", !lastLatLng);
    locateBtn.classList.toggle("is-active", !!following);
  }

  function ensureLocateButton(map) {
    if (!map || !map._container) return;

    if (locateBtn && locateBtn.isConnected) {
      setButtonState();
      return;
    }

    locateBtn = document.createElement("button");
    locateBtn.type = "button";
    locateBtn.className = "muavin-locate-control";
    locateBtn.title = "Konumuma dön";
    locateBtn.setAttribute("aria-label", "Konumuma dön");
    locateBtn.innerHTML = `<span class="muavin-locate-inner"></span>`;

    locateBtn.addEventListener("click", function () {
      following = true;
      focusToLocation(map, 16);
      setButtonState();
    });

    map._container.appendChild(locateBtn);

    try {
      map.on("dragstart zoomstart", function () {
        if (!internalMove) {
          following = false;
          setButtonState();
        }
      });
    } catch (e) {}

    setButtonState();
  }

  function hideOldBusMarker() {
    document.querySelectorAll(".leaflet-marker-icon").forEach(function (el) {
      if (el.classList.contains("muavin-gm-marker-icon")) return;

      const text = (el.textContent || "").toLocaleLowerCase("tr-TR");
      const html = (el.innerHTML || "").toLocaleLowerCase("tr-TR");

      if (
        text.includes("canlı") ||
        text.includes("canli") ||
        html.includes("otobüs") ||
        html.includes("otobus") ||
        html.includes("bus-marker") ||
        html.includes("vehicle") ||
        html.includes("muavin-live-dot-wrap")
      ) {
        el.classList.add("muavin-old-vehicle-hidden");
      }
    });
  }

  window.MUAVIN_UPDATE_BLUE_LOCATION = function (lat, lng, accuracy) {
    const map = getMap();
    if (!map || !window.L) return false;

    lat = asNumber(lat);
    lng = asNumber(lng);

    if (lat === null || lng === null) return false;

    accuracy = asNumber(accuracy) || 20;
    lastLatLng = L.latLng(lat, lng);

    if (!gmMarker) {
      gmMarker = L.marker(lastLatLng, {
        icon: makeIcon(),
        zIndexOffset: 10000,
        interactive: false
      }).addTo(map);
    } else {
      gmMarker.setLatLng(lastLatLng);
      gmMarker.setIcon(makeIcon());
    }

    if (accuracy > 0 && accuracy < 3000) {
      if (!accuracyCircle) {
        accuracyCircle = L.circle(lastLatLng, {
          radius: accuracy,
          color: "#1a73e8",
          weight: 1,
          opacity: 0.22,
          fillColor: "#1a73e8",
          fillOpacity: 0.09,
          interactive: false
        }).addTo(map);
      } else {
        accuracyCircle.setLatLng(lastLatLng);
        accuracyCircle.setRadius(accuracy);
      }
    }

    ensureLocateButton(map);
    hideOldBusMarker();

    if (!firstFocusDone || following) {
      focusToLocation(map, 16);
      firstFocusDone = true;
    }

    setButtonState();
    return true;
  };

  function startWatch() {
    if (!navigator.geolocation) return;

    navigator.geolocation.watchPosition(
      function (pos) {
        const c = pos.coords || {};
        window.MUAVIN_UPDATE_BLUE_LOCATION(
          c.latitude,
          c.longitude,
          c.accuracy || 20
        );
      },
      function (err) {
        console.warn("Muavin canlı konum alınamadı:", err);
        setButtonState();
      },
      {
        enableHighAccuracy: true,
        maximumAge: 1000,
        timeout: 10000
      }
    );
  }

  function boot() {
    const map = getMap();

    if (!window.L || !map) {
      setTimeout(boot, 500);
      return;
    }

    ensureLocateButton(map);
    startWatch();
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", boot);
  } else {
    boot();
  }
})();












/* MUAVIN_BOTTOM_DOCK_FINAL_V5_JS */
(function () {
  if (window.MUAVIN_BOTTOM_DOCK_FINAL_V5) return;
  window.MUAVIN_BOTTOM_DOCK_FINAL_V5 = true;

  let originals = {};
  let lastTap = 0;

  function norm(s) {
    return String(s || "")
      .toLocaleLowerCase("tr-TR")
      .replace(/\s+/g, " ")
      .trim();
  }

  function getMapContainer() {
    if (window.MUAVIN_LIVE_MAP && window.MUAVIN_LIVE_MAP._container) return window.MUAVIN_LIVE_MAP._container;
    if (window.map && window.map._container) return window.map._container;
    return document.querySelector(".leaflet-container");
  }

  function visibleEnough(el) {
    try {
      const r = el.getBoundingClientRect();
      return r.width > 18 && r.height > 18;
    } catch (e) {
      return false;
    }
  }

  function isExcluded(el) {
    return !!(
      el.closest(".muavin-bottom-dock-final-v5") ||
      el.closest(".muavin-bottom-dock-v2") ||
      el.closest(".muavin-bottom-minibar") ||
      el.closest(".muavin-tools-fab") ||
      el.closest(".muavin-tools-sheet") ||
      el.closest(".muavin-summary-bubble") ||
      el.closest(".muavin-route-summary-card") ||
      el.closest(".leaflet-control") ||
      el.closest(".leaflet-marker-icon")
    );
  }

  function smallestByText(labels) {
    labels = Array.isArray(labels) ? labels : [labels];
    const targets = labels.map(norm);

    const all = Array.from(document.querySelectorAll("button,a,[role='button'],[onclick],div,span"));

    const matches = all.filter(function (el) {
      if (isExcluded(el)) return false;

      const txt = norm(el.innerText || el.textContent || "");
      if (!targets.some(t => txt.includes(t))) return false;
      if (!visibleEnough(el)) return false;

      try {
        const r = el.getBoundingClientRect();
        return r.top > window.innerHeight * 0.45;
      } catch (e) {
        return false;
      }
    });

    matches.sort(function (a, b) {
      const ar = a.getBoundingClientRect();
      const br = b.getBoundingClientRect();
      return (ar.width * ar.height) - (br.width * br.height);
    });

    return matches[0] || null;
  }

  function clickReal(el) {
    if (!el) return false;

    const oldClass = el.className || "";
    const oldStyle = el.getAttribute("style") || "";

    try {
      el.classList.remove("muavin-original-bottom-action-hidden");
      el.setAttribute(
        "style",
        oldStyle + ";position:fixed!important;left:-9999px!important;top:-9999px!important;opacity:0!important;display:block!important;pointer-events:auto!important;"
      );
    } catch (e) {}

    const clickable =
      (el.closest && el.closest("button,a,[role='button'],[onclick]")) ||
      (el.querySelector && el.querySelector("button,a,[role='button'],[onclick]")) ||
      el;

    setTimeout(function () {
      try {
        clickable.dispatchEvent(new MouseEvent("mousedown", { bubbles: true, cancelable: true }));
        clickable.dispatchEvent(new MouseEvent("mouseup", { bubbles: true, cancelable: true }));
        clickable.dispatchEvent(new MouseEvent("click", { bubbles: true, cancelable: true }));
      } catch (e) {
        try { clickable.click(); } catch (err) {}
      }

      setTimeout(function () {
        try {
          el.className = oldClass;
          if (oldStyle) el.setAttribute("style", oldStyle);
          else el.removeAttribute("style");
          el.classList.add("muavin-original-bottom-action-hidden");
        } catch (e) {}
      }, 80);
    }, 20);

    return true;
  }

  function captureOriginals() {
    if (!originals.duraklar) originals.duraklar = smallestByText(["Tüm Duraklar", "Duraklar"]);
    if (!originals.rota) originals.rota = smallestByText("Rota");
    if (!originals.konumum) originals.konumum = smallestByText("Konumum");
    if (!originals.islemli) originals.islemli = smallestByText("İşlemli");

    Object.keys(originals).forEach(function (k) {
      const el = originals[k];
      if (el) el.classList.add("muavin-original-bottom-action-hidden");
    });
  }

  function mainHtml() {
    return `
      <button type="button" class="dock-dark" data-final-dock="duraklar">
        <span class="dock-icon">🗺️</span>
        <span>Duraklar</span>
      </button>

      <button type="button" class="dock-dark" data-final-dock="rota">
        <span class="dock-icon">〽️</span>
        <span>Rota</span>
      </button>

      <button type="button" class="dock-light" data-final-dock="more">
        <span>•••</span>
      </button>
    `;
  }

  function moreHtml() {
    return `
      <button type="button" class="dock-dark" data-final-dock="konumum">
        <span class="dock-icon">📍</span>
        <span>Konumum</span>
      </button>

      <button type="button" class="dock-dark" data-final-dock="islemli">
        <span class="dock-icon">🎯</span>
        <span>İşlemli</span>
      </button>

      <button type="button" class="dock-close" data-final-dock="close">
        <span>×</span>
      </button>
    `;
  }

  function render(mode) {
    const dock = document.querySelector(".muavin-bottom-dock-final-v5");
    if (!dock) return;

    const row = dock.querySelector(".dock-row");
    if (!row) return;

    row.innerHTML = mode === "more" ? moreHtml() : mainHtml();
    dock.dataset.mode = mode === "more" ? "more" : "main";
  }

  function runAction(action) {
    captureOriginals();

    if (action === "more") {
      render("more");
      return;
    }

    if (action === "close") {
      render("main");
      return;
    }

    if (action === "duraklar") {
      clickReal(originals.duraklar);
      render("main");
      return;
    }

    if (action === "rota") {
      clickReal(originals.rota);
      render("main");
      return;
    }

    if (action === "konumum") {
      clickReal(originals.konumum);
      render("main");
      return;
    }

    if (action === "islemli") {
      clickReal(originals.islemli);
      render("main");
      return;
    }
  }

  function setupDock() {
    const container = getMapContainer();

    if (!container) {
      setTimeout(setupDock, 500);
      return;
    }

    captureOriginals();

    document.querySelectorAll(".muavin-bottom-dock-v2, .muavin-bottom-minibar").forEach(function (el) {
      el.style.display = "none";
    });

    let dock = container.querySelector(".muavin-bottom-dock-final-v5");

    if (!dock) {
      dock = document.createElement("div");
      dock.className = "muavin-bottom-dock-final-v5";
      dock.innerHTML = `<div class="dock-row"></div>`;
      container.appendChild(dock);
    }

    if (dock.dataset.ready !== "1") {
      dock.dataset.ready = "1";

      try {
        if (window.L && L.DomEvent) {
          L.DomEvent.disableClickPropagation(dock);
          L.DomEvent.disableScrollPropagation(dock);
        }
      } catch (e) {}

      function handle(e) {
        const btn = e.target.closest("[data-final-dock]");
        if (!btn || !dock.contains(btn)) return;

        const now = Date.now();

        if (now - lastTap < 260) {
          e.preventDefault();
          e.stopPropagation();
          if (e.stopImmediatePropagation) e.stopImmediatePropagation();
          return;
        }

        lastTap = now;

        e.preventDefault();
        e.stopPropagation();
        if (e.stopImmediatePropagation) e.stopImmediatePropagation();

        runAction(btn.getAttribute("data-final-dock"));
      }

      dock.addEventListener("touchend", handle, { capture: true, passive: false });
      dock.addEventListener("click", handle, true);
    }

    render("main");
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", setupDock);
  } else {
    setupDock();
  }

  setTimeout(setupDock, 800);
  setTimeout(setupDock, 1800);
  setTimeout(setupDock, 3200);
})();

/* MUAVIN_MAP_UI_FINAL_V6_JS */
(function () {
  if (window.MUAVIN_MAP_UI_FINAL_V6) return;
  window.MUAVIN_MAP_UI_FINAL_V6 = true;

  const AVG_SPEED_KMH = 70;
  const BUBBLE_POS_KEY = "muavinRouteBubblePositionV2";

  let toolsFab = null;
  let toolsSheet = null;
  let kmGroup = null;
  let kmOn = false;
  let nav3dOn = true;
  let bearing = 0;
  let currentLatLng = null;
  let currentSpeedKmh = 0;
  let summaryCard = null;
  let summaryBubble = null;
  let summaryOpen = false;
  let updateTimer = null;
  let drag = null;
  let suppressBubbleClickUntil = 0;
  let rotateGesture = null;

  function getMap() {
    if (window.MUAVIN_LIVE_MAP && window.MUAVIN_LIVE_MAP._container) return window.MUAVIN_LIVE_MAP;
    if (window.map && window.map._container) return window.map;

    for (const key of Object.keys(window)) {
      try {
        const v = window[key];
        if (
          v &&
          v._container &&
          typeof v.addLayer === "function" &&
          typeof v.setView === "function" &&
          v._container.classList &&
          v._container.classList.contains("leaflet-container")
        ) return v;
      } catch (e) {}
    }

    return null;
  }

  function getContainer() {
    const map = getMap();
    return map && map._container ? map._container : document.querySelector(".leaflet-container");
  }

  function kmBetween(a, b) {
    if (!a || !b) return 0;

    const R = 6371;
    const dLat = (b.lat - a.lat) * Math.PI / 180;
    const dLng = (b.lng - a.lng) * Math.PI / 180;
    const lat1 = a.lat * Math.PI / 180;
    const lat2 = b.lat * Math.PI / 180;

    const x =
      Math.sin(dLat / 2) * Math.sin(dLat / 2) +
      Math.cos(lat1) * Math.cos(lat2) *
      Math.sin(dLng / 2) * Math.sin(dLng / 2);

    return 2 * R * Math.atan2(Math.sqrt(x), Math.sqrt(1 - x));
  }

  function formatKm(v) {
    v = Number(v) || 0;
    if (v < 0.05) return "0 m";
    if (v < 1) return Math.round(v * 1000) + " m";
    if (v < 10) return v.toFixed(1) + " km";
    return Math.round(v) + " km";
  }

  function formatEta(hours) {
    hours = Number(hours) || 0;
    if (hours <= 0) return "—";

    const totalMin = Math.max(1, Math.round(hours * 60));
    const h = Math.floor(totalMin / 60);
    const m = totalMin % 60;

    if (h <= 0) return m + " dk.";
    if (m <= 0) return h + " sa.";
    return h + " sa. " + m + " dk.";
  }

  function flattenLatLngs(latlngs) {
    const out = [];

    function walk(arr) {
      if (!arr) return;

      if (arr.lat !== undefined && arr.lng !== undefined) {
        out.push(arr);
        return;
      }

      if (Array.isArray(arr)) arr.forEach(walk);
    }

    walk(latlngs);
    return out;
  }

  function getMainRouteLine(map) {
    let best = null;
    let bestCount = 0;

    map.eachLayer(function (layer) {
      try {
        if (!window.L || !(layer instanceof L.Polyline)) return;
        if (layer instanceof L.Circle) return;
        if (layer instanceof L.Polygon) return;

        const pts = flattenLatLngs(layer.getLatLngs ? layer.getLatLngs() : []);
        if (pts.length > bestCount) {
          best = pts;
          bestCount = pts.length;
        }
      } catch (e) {}
    });

    return best && best.length >= 2 ? best : null;
  }

  function routeCumulative(points) {
    const cum = [0];

    for (let i = 1; i < points.length; i++) {
      cum[i] = cum[i - 1] + kmBetween(points[i - 1], points[i]);
    }

    return cum;
  }

  function nearestRouteIndex(points, latlng) {
    let bestI = 0;
    let bestD = Infinity;

    for (let i = 0; i < points.length; i++) {
      const d = kmBetween(points[i], latlng);
      if (d < bestD) {
        bestD = d;
        bestI = i;
      }
    }

    return bestI;
  }

  function isSystemMarker(layer) {
    try {
      const icon = layer.getIcon && layer.getIcon();
      const cls = icon && icon.options && icon.options.className || "";

      if (cls.includes("muavin-gm-marker-icon")) return true;
      if (cls.includes("muavin-km-label")) return true;
      if (cls.includes("muavin-live-marker-icon")) return true;
    } catch (e) {}

    return false;
  }

  function getStopMarkers(map, routePoints) {
    const markers = [];

    map.eachLayer(function (layer) {
      try {
        if (!window.L || !(layer instanceof L.Marker)) return;
        if (isSystemMarker(layer)) return;

        const latlng = layer.getLatLng && layer.getLatLng();
        if (!latlng) return;

        const iconEl = layer._icon;
        const html = iconEl ? (iconEl.innerHTML || "") : "";
        const text = iconEl ? (iconEl.textContent || "") : "";

        if (html.includes("muavin-gm-live-marker")) return;
        if (html.includes("muavin-km-label")) return;
        if (text.includes("km/sa")) return;

        markers.push({
          layer,
          latlng,
          order: routePoints ? nearestRouteIndex(routePoints, latlng) : markers.length
        });
      } catch (e) {}
    });

    markers.sort(function (a, b) {
      return a.order - b.order;
    });

    const unique = [];

    markers.forEach(function (m) {
      const last = unique[unique.length - 1];

      if (!last || kmBetween(last.latlng, m.latlng) > 0.08) {
        unique.push(m);
      }
    });

    return unique;
  }

  function calcRouteDistance(routePoints, cum, fromIndex, toIndex, fromLatLng, toLatLng) {
    if (
      routePoints &&
      cum &&
      Number.isFinite(fromIndex) &&
      Number.isFinite(toIndex) &&
      toIndex > fromIndex
    ) {
      const d = Math.abs(cum[toIndex] - cum[fromIndex]);
      if (d > 0.03) return d;
    }

    return kmBetween(fromLatLng, toLatLng);
  }

  function fallbackRemaining(current, stops) {
    if (!current || !stops.length) return 0;

    const sorted = stops
      .map(function (s, i) {
        return { s, i, d: kmBetween(current, s.latlng) };
      })
      .sort(function (a, b) { return a.d - b.d; });

    const nearest = sorted[0];
    if (!nearest) return 0;

    let total = kmBetween(current, nearest.s.latlng);

    for (let i = nearest.i; i < stops.length - 1; i++) {
      total += kmBetween(stops[i].latlng, stops[i + 1].latlng);
    }

    return total;
  }

  function getRouteStats() {
    const map = getMap();
    if (!map || !window.L || !currentLatLng) {
      return {
        liveNext: "—",
        nextNext: "—",
        remaining: "—",
        eta: "—",
        note: "Konum bekleniyor..."
      };
    }

    const routePoints = getMainRouteLine(map);
    const cum = routePoints ? routeCumulative(routePoints) : null;
    const stops = getStopMarkers(map, routePoints);

    if (!stops.length) {
      return {
        liveNext: "—",
        nextNext: "—",
        remaining: "—",
        eta: "—",
        note: "Durak koordinatları bulunamadı."
      };
    }

    const currentOrder = routePoints ? nearestRouteIndex(routePoints, currentLatLng) : null;

    let nextStop = null;
    let nextIndex = -1;

    if (routePoints) {
      for (let i = 0; i < stops.length; i++) {
        if (stops[i].order > currentOrder + 2) {
          nextStop = stops[i];
          nextIndex = i;
          break;
        }
      }

      if (!nextStop) {
        nextStop = stops[stops.length - 1];
        nextIndex = stops.length - 1;
      }
    } else {
      const sorted = stops
        .map(function (s, i) {
          return { s, i, d: kmBetween(currentLatLng, s.latlng) };
        })
        .sort(function (a, b) { return a.d - b.d; });

      nextStop = sorted[0].s;
      nextIndex = sorted[0].i;
    }

    const afterStop = stops[nextIndex + 1] || null;

    const liveToNext = nextStop
      ? calcRouteDistance(routePoints, cum, currentOrder, nextStop.order, currentLatLng, nextStop.latlng)
      : 0;

    const nextToAfter = nextStop && afterStop
      ? calcRouteDistance(routePoints, cum, nextStop.order, afterStop.order, nextStop.latlng, afterStop.latlng)
      : 0;

    let remaining = 0;

    if (routePoints && cum && Number.isFinite(currentOrder)) {
      remaining = Math.max(0, cum[cum.length - 1] - cum[currentOrder]);
    } else {
      remaining = fallbackRemaining(currentLatLng, stops);
    }

    const speed = currentSpeedKmh >= 15 ? currentSpeedKmh : AVG_SPEED_KMH;
    const note = currentSpeedKmh >= 15
      ? "Canlı hızla hesaplandı: " + Math.round(currentSpeedKmh) + " km/sa"
      : "Tahmini varış " + AVG_SPEED_KMH + " km/sa ortalama ile hesaplandı.";

    return {
      liveNext: formatKm(liveToNext),
      nextNext: afterStop ? formatKm(nextToAfter) : "Son durak",
      remaining: formatKm(remaining),
      eta: remaining > 0 ? formatEta(remaining / speed) : "—",
      note
    };
  }

  function setNav3d(on) {
    const map = getMap();
    if (!map || !map._container) return;

    nav3dOn = !!on;
    map._container.classList.toggle("muavin-nav-3d-final", nav3dOn);

    try {
      localStorage.setItem("muavinNav3dModeFinal", nav3dOn ? "1" : "0");
    } catch (e) {}

    updateToolStates();
  }

  function normalizeDeg(v) {
    v = Number(v) || 0;
    while (v > 180) v -= 360;
    while (v < -180) v += 360;
    if (Math.abs(v) < 0.4) v = 0;
    return v;
  }

  function setBearing(deg) {
    const map = getMap();
    if (!map || !map._container) return;

    bearing = normalizeDeg(deg);

    map._container.classList.toggle("muavin-bearing-final", Math.abs(bearing) > 0.4);
    map._container.style.setProperty("--muavin-map-bearing-final", bearing + "deg");
    map._container.style.setProperty("--muavin-map-scale-final", Math.abs(bearing) > 0.4 ? "1.18" : "1");

    try {
      localStorage.setItem("muavinMapBearing", String(bearing));
    } catch (e) {}
  }

  function angleFromTouches(t1, t2) {
    return Math.atan2(t2.clientY - t1.clientY, t2.clientX - t1.clientX) * 180 / Math.PI;
  }

  function shortestDelta(start, current) {
    let d = current - start;
    while (d > 180) d -= 360;
    while (d < -180) d += 360;
    return d;
  }

  function bindRotateGesture() {
    const container = getContainer();
    if (!container || container.dataset.muavinFinalRotateBound === "1") return;

    container.dataset.muavinFinalRotateBound = "1";

    container.addEventListener("touchstart", function (e) {
      if (!e.touches || e.touches.length !== 2) return;

      rotateGesture = {
        startAngle: angleFromTouches(e.touches[0], e.touches[1]),
        baseBearing: bearing,
        rotating: false
      };
    }, { passive: true, capture: true });

    container.addEventListener("touchmove", function (e) {
      if (!rotateGesture || !e.touches || e.touches.length !== 2) return;

      const currentAngle = angleFromTouches(e.touches[0], e.touches[1]);
      const delta = shortestDelta(rotateGesture.startAngle, currentAngle);

      if (!rotateGesture.rotating && Math.abs(delta) > 8) {
        rotateGesture.rotating = true;
      }

      if (rotateGesture.rotating) {
        e.preventDefault();
        e.stopPropagation();
        if (e.stopImmediatePropagation) e.stopImmediatePropagation();

        setBearing(rotateGesture.baseBearing + delta);
      }
    }, { passive: false, capture: true });

    container.addEventListener("touchend", function (e) {
      if (!e.touches || e.touches.length < 2) rotateGesture = null;
    }, { passive: true, capture: true });

    container.addEventListener("touchcancel", function () {
      rotateGesture = null;
    }, { passive: true, capture: true });
  }

  function makeKmIcon(text, live) {
    return L.divIcon({
      className: "muavin-km-label-final-icon",
      iconSize: null,
      iconAnchor: [34, 14],
      html: '<div class="muavin-km-label-final ' + (live ? "is-live" : "") + '">' + text + '</div>'
    });
  }

  function addKmLabel(latlng, text, live) {
    if (!kmGroup || !window.L) return;

    L.marker(latlng, {
      icon: makeKmIcon(text, live),
      interactive: false,
      zIndexOffset: live ? 9900 : 8500
    }).addTo(kmGroup);
  }

  function midpoint(a, b) {
    return L.latLng((a.lat + b.lat) / 2, (a.lng + b.lng) / 2);
  }

  function refreshKmLabels() {
    const map = getMap();
    if (!map || !window.L) return;

    if (!kmGroup) kmGroup = L.layerGroup().addTo(map);
    kmGroup.clearLayers();

    if (!kmOn) return;

    const routePoints = getMainRouteLine(map);
    const cum = routePoints ? routeCumulative(routePoints) : null;
    const stops = getStopMarkers(map, routePoints);

    for (let i = 0; i < stops.length - 1; i++) {
      const a = stops[i];
      const b = stops[i + 1];

      const d = calcRouteDistance(routePoints, cum, a.order, b.order, a.latlng, b.latlng);
      const mid = routePoints && b.order > a.order
        ? routePoints[Math.round((a.order + b.order) / 2)]
        : midpoint(a.latlng, b.latlng);

      addKmLabel(mid, formatKm(d), false);
    }

    if (currentLatLng && stops.length) {
      const currentOrder = routePoints ? nearestRouteIndex(routePoints, currentLatLng) : null;
      let next = null;

      if (routePoints) {
        next = stops.find(function (s) {
          return s.order > currentOrder;
        }) || stops[0];
      } else {
        next = stops
          .map(function (s) {
            return { s, d: kmBetween(currentLatLng, s.latlng) };
          })
          .sort(function (a, b) { return a.d - b.d; })[0].s;
      }

      if (next) {
        const dLive = routePoints && next.order > currentOrder
          ? Math.abs(cum[next.order] - cum[currentOrder])
          : kmBetween(currentLatLng, next.latlng);

        addKmLabel(midpoint(currentLatLng, next.latlng), formatKm(dLive) + "<br><small>Sıradaki</small>", true);
      }
    }
  }

  function setKm(on) {
    const map = getMap();
    if (!map || !window.L) return;

    kmOn = !!on;

    if (!kmGroup) kmGroup = L.layerGroup().addTo(map);

    try {
      localStorage.setItem("muavinKmLabelsOnFinal", kmOn ? "1" : "0");
    } catch (e) {}

    refreshKmLabels();
    updateToolStates();
  }

  function ensureTools() {
    const container = getContainer();
    if (!container) return;

    if (!toolsFab) {
      toolsFab = document.createElement("button");
      toolsFab.type = "button";
      toolsFab.className = "muavin-tools-fab-final";
      toolsFab.title = "Araçlar";
      toolsFab.setAttribute("aria-label", "Araçlar");
      toolsFab.innerHTML = '<span class="fab-icon">⚙️</span><span class="fab-text">Araçlar</span>';

      toolsFab.addEventListener("click", function (e) {
        e.preventDefault();
        e.stopPropagation();
        if (toolsSheet) toolsSheet.classList.toggle("is-open");
      });

      container.appendChild(toolsFab);
    }

    if (!toolsSheet) {
      toolsSheet = document.createElement("div");
      toolsSheet.className = "muavin-tools-sheet-final";
      toolsSheet.innerHTML = `
        <div class="muavin-tools-title-final">HARİTA ARAÇLARI</div>
        <div class="muavin-tools-list-final">
          <button type="button" class="muavin-tools-btn-final" data-map-tool="3d">
            <span>3D görünüm</span><small>Aç / Kapat</small>
          </button>
          <button type="button" class="muavin-tools-btn-final" data-map-tool="km">
            <span>KM etiketleri</span><small>Aç / Kapat</small>
          </button>
        </div>
      `;

      toolsSheet.addEventListener("click", function (e) {
        const btn = e.target.closest("[data-map-tool]");
        if (!btn) return;

        const action = btn.getAttribute("data-map-tool");

        if (action === "3d") setNav3d(!nav3dOn);
        if (action === "km") setKm(!kmOn);
        /* pusula kaldırıldı */

        toolsSheet.classList.remove("is-open");
      });

      container.appendChild(toolsSheet);

      document.addEventListener("click", function (e) {
        if (!toolsSheet || !toolsFab) return;
        if (toolsSheet.contains(e.target) || toolsFab.contains(e.target)) return;
        toolsSheet.classList.remove("is-open");
      }, true);
    }

    updateToolStates();
  }

  function updateToolStates() {
    if (!toolsSheet) return;

    const btn3d = toolsSheet.querySelector('[data-map-tool="3d"]');
    const btnKm = toolsSheet.querySelector('[data-map-tool="km"]');

    if (btn3d) btn3d.classList.toggle("is-on", !!nav3dOn);
    if (btnKm) btnKm.classList.toggle("is-on", !!kmOn);
  }

  function ensureSummary() {
    const container = getContainer();
    if (!container) return;

    if (!summaryBubble) {
      summaryBubble = document.createElement("button");
      summaryBubble.type = "button";
      summaryBubble.className = "muavin-summary-bubble-final";
      summaryBubble.title = "Rota özeti";
      summaryBubble.setAttribute("aria-label", "Rota özeti");
      summaryBubble.innerHTML = `
        <span class="bubble-icon">🧭</span>
        <span class="bubble-text">
          <span class="bubble-main" data-final-summary="bubbleRemaining">—</span>
          <span class="bubble-sub" data-final-summary="bubbleEta">—</span>
        </span>
      `;

      summaryBubble.addEventListener("click", function (e) {
        if (Date.now() < suppressBubbleClickUntil) {
          e.preventDefault();
          e.stopPropagation();
          if (e.stopImmediatePropagation) e.stopImmediatePropagation();
          return;
        }

        setSummaryOpen(!summaryOpen);
      });

      container.appendChild(summaryBubble);
      bindBubbleDrag();
      restoreBubblePosition();
    }

    if (!summaryCard) {
      summaryCard = document.createElement("div");
      summaryCard.className = "muavin-route-summary-card-final";
      summaryCard.innerHTML = `
        <div class="summary-head">
          <div class="summary-title">ROTA ÖZETİ</div>
          <button type="button" class="summary-close" aria-label="Kapat">×</button>
        </div>

        <div class="summary-grid">
          <div class="summary-item">
            <div class="summary-label">Canlı → Sıradaki</div>
            <div class="summary-value is-blue" data-final-summary="liveNext">—</div>
          </div>

          <div class="summary-item">
            <div class="summary-label">Sıradaki → Sonraki</div>
            <div class="summary-value" data-final-summary="nextNext">—</div>
          </div>

          <div class="summary-item">
            <div class="summary-label">Kalan toplam rota</div>
            <div class="summary-value is-green" data-final-summary="remaining">—</div>
          </div>

          <div class="summary-item">
            <div class="summary-label">Tahmini varış</div>
            <div class="summary-value is-yellow" data-final-summary="eta">—</div>
          </div>
        </div>

        <div class="summary-note" data-final-summary="note">Konum bekleniyor...</div>
      `;

      summaryCard.querySelector(".summary-close").addEventListener("click", function () {
        setSummaryOpen(false);
      });

      container.appendChild(summaryCard);
    }
  }

  function setSummaryOpen(open) {
    summaryOpen = !!open;

    if (summaryCard) summaryCard.classList.toggle("is-open", summaryOpen);
    if (summaryBubble) summaryBubble.classList.toggle("is-open", summaryOpen);

    try {
      localStorage.setItem("muavinRouteSummaryBubbleOpen", summaryOpen ? "1" : "0");
    } catch (e) {}
  }

  function setSummaryValue(key, value) {
    document.querySelectorAll('[data-final-summary="' + key + '"]').forEach(function (el) {
      el.textContent = value;
    });
  }

  function updateSummary() {
    ensureSummary();

    const s = getRouteStats();

    setSummaryValue("bubbleRemaining", s.remaining);
    setSummaryValue("bubbleEta", s.eta);
    setSummaryValue("liveNext", s.liveNext);
    setSummaryValue("nextNext", s.nextNext);
    setSummaryValue("remaining", s.remaining);
    setSummaryValue("eta", s.eta);
    setSummaryValue("note", s.note);

    refreshKmLabels();
  }

  function scheduleUpdate() {
    clearTimeout(updateTimer);
    updateTimer = setTimeout(updateSummary, 250);
  }

  function clamp(v, min, max) {
    return Math.max(min, Math.min(max, v));
  }

  function getPoint(e) {
    if (e.touches && e.touches.length) return { x: e.touches[0].clientX, y: e.touches[0].clientY };
    if (e.changedTouches && e.changedTouches.length) return { x: e.changedTouches[0].clientX, y: e.changedTouches[0].clientY };
    return { x: e.clientX, y: e.clientY };
  }

  function applyBubblePosition(x, y, save) {
    const container = getContainer();
    if (!container || !summaryBubble) return;

    const cRect = container.getBoundingClientRect();
    const bRect = summaryBubble.getBoundingClientRect();

    const margin = 8;
    const maxX = Math.max(margin, cRect.width - bRect.width - margin);
    const maxY = Math.max(margin, cRect.height - bRect.height - margin);

    x = clamp(x, margin, maxX);
    y = clamp(y, margin, maxY);

    summaryBubble.classList.add("is-positioned");
    summaryBubble.style.setProperty("--muavin-bubble-left-final", x + "px");
    summaryBubble.style.setProperty("--muavin-bubble-top-final", y + "px");

    if (save) {
      try {
        localStorage.setItem(BUBBLE_POS_KEY, JSON.stringify({
          xPct: x / Math.max(cRect.width, 1),
          yPct: y / Math.max(cRect.height, 1)
        }));
      } catch (e) {}
    }
  }

  function restoreBubblePosition() {
    const container = getContainer();
    if (!container || !summaryBubble) return;

    try {
      const saved = JSON.parse(localStorage.getItem(BUBBLE_POS_KEY) || "null");
      if (!saved || typeof saved.xPct !== "number" || typeof saved.yPct !== "number") return;

      const cRect = container.getBoundingClientRect();
      applyBubblePosition(saved.xPct * cRect.width, saved.yPct * cRect.height, false);
    } catch (e) {}
  }

  function disableMapMove() {
    const map = getMap();
    if (!map) return;

    try { map.dragging.disable(); } catch (e) {}
    try { map.touchZoom.disable(); } catch (e) {}
    try { map.doubleClickZoom.disable(); } catch (e) {}
  }

  function enableMapMove() {
    const map = getMap();
    if (!map) return;

    try { map.dragging.enable(); } catch (e) {}
    try { map.touchZoom.enable(); } catch (e) {}
    try { map.doubleClickZoom.enable(); } catch (e) {}
  }

  function bindBubbleDrag() {
    if (!summaryBubble || summaryBubble.dataset.dragFinal === "1") return;
    summaryBubble.dataset.dragFinal = "1";

    function start(e) {
      const container = getContainer();
      if (!container) return;

      const p = getPoint(e);
      const cRect = container.getBoundingClientRect();
      const bRect = summaryBubble.getBoundingClientRect();

      drag = {
        startX: p.x,
        startY: p.y,
        baseX: bRect.left - cRect.left,
        baseY: bRect.top - cRect.top,
        moved: false
      };

      summaryBubble.classList.add("is-dragging");
      disableMapMove();
    }

    function move(e) {
      if (!drag) return;

      const p = getPoint(e);
      const dx = p.x - drag.startX;
      const dy = p.y - drag.startY;

      if (Math.abs(dx) > 5 || Math.abs(dy) > 5) drag.moved = true;
      if (!drag.moved) return;

      e.preventDefault();
      e.stopPropagation();
      if (e.stopImmediatePropagation) e.stopImmediatePropagation();

      applyBubblePosition(drag.baseX + dx, drag.baseY + dy, true);
    }

    function end(e) {
      if (!drag) return;

      if (drag.moved) {
        suppressBubbleClickUntil = Date.now() + 500;
        e.preventDefault();
        e.stopPropagation();
        if (e.stopImmediatePropagation) e.stopImmediatePropagation();
      }

      summaryBubble.classList.remove("is-dragging");
      drag = null;
      enableMapMove();
    }

    summaryBubble.addEventListener("touchstart", start, { passive: false, capture: true });
    summaryBubble.addEventListener("touchmove", move, { passive: false, capture: true });
    summaryBubble.addEventListener("touchend", end, { passive: false, capture: true });
    summaryBubble.addEventListener("touchcancel", end, { passive: false, capture: true });

    summaryBubble.addEventListener("mousedown", start, true);
    window.addEventListener("mousemove", move, true);
    window.addEventListener("mouseup", end, true);

    window.addEventListener("resize", restoreBubblePosition);
  }

  function wrapLocationUpdate() {
    if (window.MUAVIN_MAP_UI_FINAL_LOCATION_WRAPPED) return;

    if (typeof window.MUAVIN_UPDATE_BLUE_LOCATION !== "function") {
      setTimeout(wrapLocationUpdate, 500);
      return;
    }

    const oldFn = window.MUAVIN_UPDATE_BLUE_LOCATION;

    window.MUAVIN_UPDATE_BLUE_LOCATION = function (lat, lng, accuracy, heading) {
      const result = oldFn.apply(this, arguments);

      lat = Number(lat);
      lng = Number(lng);

      if (Number.isFinite(lat) && Number.isFinite(lng) && window.L) {
        currentLatLng = L.latLng(lat, lng);
        scheduleUpdate();
      }

      return result;
    };

    window.MUAVIN_MAP_UI_FINAL_LOCATION_WRAPPED = true;
  }

  function startSpeedWatch() {
    if (!navigator.geolocation || window.MUAVIN_MAP_UI_FINAL_SPEED_WATCH) return;
    window.MUAVIN_MAP_UI_FINAL_SPEED_WATCH = true;

    navigator.geolocation.watchPosition(
      function (pos) {
        const c = pos.coords || {};
        const speedMs = Number(c.speed);

        if (Number.isFinite(speedMs) && speedMs > 0) currentSpeedKmh = speedMs * 3.6;

        if (Number.isFinite(c.latitude) && Number.isFinite(c.longitude) && window.L) {
          currentLatLng = L.latLng(c.latitude, c.longitude);
          scheduleUpdate();
        }
      },
      function () {},
      {
        enableHighAccuracy: true,
        maximumAge: 1000,
        timeout: 10000
      }
    );
  }

  function boot() {
    const map = getMap();

    if (!map || !map._container || !window.L) {
      setTimeout(boot, 500);
      return;
    }

    try {
      nav3dOn = (localStorage.getItem("muavinNav3dModeFinal") || localStorage.getItem("muavinNav3dMode") || "1") !== "0";
      kmOn = (localStorage.getItem("muavinKmLabelsOnFinal") || "0") === "1";
      bearing = 0; try { localStorage.setItem("muavinMapBearing", "0"); } catch (e) {}
      summaryOpen = (localStorage.getItem("muavinRouteSummaryBubbleOpen") || "0") === "1";
    } catch (e) {}

    ensureTools();
    ensureSummary();
    setNav3d(nav3dOn);
    setKm(kmOn);
    setBearing(bearing);
    setSummaryOpen(summaryOpen);
    /* pusula/harita döndürme kaldırıldı */
    wrapLocationUpdate();
    startSpeedWatch();

    try {
      map.on("zoomend moveend layeradd layerremove", scheduleUpdate);
    } catch (e) {}

    setTimeout(updateSummary, 800);
    setTimeout(updateSummary, 2000);
    setInterval(updateSummary, 5000);
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", boot);
  } else {
    boot();
  }
})();

/* MUAVIN_REMOVE_COMPASS_V7_JS */
(function () {
  if (window.MUAVIN_REMOVE_COMPASS_V7) return;
  window.MUAVIN_REMOVE_COMPASS_V7 = true;

  try {
    localStorage.setItem("muavinMapBearing", "0");
  } catch (e) {}

  function cleanCompass() {
    const map =
      (window.MUAVIN_LIVE_MAP && window.MUAVIN_LIVE_MAP._container ? window.MUAVIN_LIVE_MAP : null) ||
      (window.map && window.map._container ? window.map : null);

    const container = map && map._container ? map._container : document.querySelector(".leaflet-container");

    if (container) {
      container.classList.remove("muavin-bearing-final");
      container.style.setProperty("--muavin-map-bearing-final", "0deg");
      container.style.setProperty("--muavin-map-scale-final", "1");
    }

    document.querySelectorAll('[data-map-tool="north"]').forEach(function (el) {
      el.remove();
    });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", cleanCompass);
  } else {
    cleanCompass();
  }

  setTimeout(cleanCompass, 700);
  setTimeout(cleanCompass, 1800);
  setInterval(cleanCompass, 4000);
})();

/* MUAVIN_NEXT_OPS_FINAL_V1_JS */
(function () {
  if (window.MUAVIN_NEXT_OPS_FINAL_V1) return;
  window.MUAVIN_NEXT_OPS_FINAL_V1 = true;

  const DONE_KEY = "muavinNextOpsDoneStopsV1";

  function esc(v) {
    return String(v == null ? "" : v)
      .replaceAll("&", "&amp;")
      .replaceAll('"', "&quot;")
      .replaceAll("<", "&lt;")
      .replaceAll(">", "&gt;");
  }

  function getDoneList() {
    try {
      const arr = JSON.parse(sessionStorage.getItem(DONE_KEY) || "[]");
      return Array.isArray(arr) ? arr : [];
    } catch (e) {
      return [];
    }
  }

  function setDone(name) {
    const arr = getDoneList();
    if (!arr.includes(name)) arr.push(name);
    try {
      sessionStorage.setItem(DONE_KEY, JSON.stringify(arr));
    } catch (e) {}
  }

  function isDone(name) {
    return getDoneList().includes(name);
  }

  function safeStops() {
    try {
      if (typeof nextOperationStops === "function") return nextOperationStops();
    } catch (e) {}
    return [];
  }

  function safeOperationText(stop) {
    try {
      if (typeof operationText === "function") return operationText(stop);
    } catch (e) {}
    return "İşlem yok";
  }

  function safeDistance(stop) {
    try {
      if (typeof distanceToStopText === "function") return distanceToStopText(stop);
    } catch (e) {}
    return "—";
  }

  function findMarkerItem(name) {
    try {
      if (Array.isArray(markerItems)) {
        return markerItems.find(x => x.stop && x.stop.name === name);
      }
    } catch (e) {}
    return null;
  }

  function openStop(name) {
    const item = findMarkerItem(name);
    try {
      if (item && item.marker && typeof map !== "undefined") {
        map.setView(item.marker.getLatLng(), 14);
        item.marker.openPopup();
      }
    } catch (e) {}
  }

  function speakStop(stop) {
    if (!stop) return;

    const name = stop.name || "Durak";
    const km = safeDistance(stop);
    const op = safeOperationText(stop);

    const msg = `${name} yaklaşıyor. Kalan mesafe ${km}. ${op}.`;

    try {
      if (window.speechSynthesis) {
        window.speechSynthesis.cancel();
        const u = new SpeechSynthesisUtterance(msg);
        u.lang = "tr-TR";
        u.rate = 0.95;
        window.speechSynthesis.speak(u);
      }
    } catch (e) {}
  }

  function metricChip(label, value, cls) {
    return `<span class="next-op-chip ${cls || ""}">${label}: ${value}</span>`;
  }

  function renderHero(stop) {
    const off = Number(stop.off_count || 0);
    const board = Number(stop.board_count || 0);
    const bag = Number(stop.bag_count || 0);
    const parcel = Number(stop.parcel_count || 0);
    const done = isDone(stop.name);

    const chips = [
      metricChip("İnecek", off, off ? "warn" : "good"),
      metricChip("Binecek", board, board ? "warn" : "good"),
      metricChip("Bagaj", bag, bag ? "warn" : "good"),
      metricChip("Emanet", parcel, parcel ? "warn" : "good"),
    ].join("");

    return `
      <div class="next-op-hero">
        <div class="next-op-hero-top">
          <div>
            <div class="next-op-hero-kicker">Sıradaki Durak</div>
            <div class="next-op-hero-title">${esc(stop.name)}</div>
          </div>
          <div class="next-op-hero-distance" data-op-km="${esc(stop.name)}">${esc(safeDistance(stop))}</div>
        </div>

        <div class="next-op-hero-meta">
          ${chips}
        </div>

        <div class="next-op-task-grid">
          <button class="next-op-task-btn speak" type="button" data-next-task="speak" data-stop="${esc(stop.name)}">🔊 Anons</button>
          <button class="next-op-task-btn people" type="button" data-next-task="people" data-stop="${esc(stop.name)}">👥 Yolcu</button>
          <button class="next-op-task-btn bag" type="button" data-next-task="bag" data-stop="${esc(stop.name)}">🎒 Bagaj</button>
          <button class="next-op-task-btn done ${done ? "is-done" : ""}" type="button" data-next-task="done" data-stop="${esc(stop.name)}">${done ? "✅ Tamam" : "✅ Tamamla"}</button>
        </div>
      </div>
    `;
  }

  function renderMini(stop) {
    return `
      <button class="next-op-mini" type="button" data-next-op-stop="${esc(stop.name)}">
        <div>
          <div class="next-op-mini-name">${esc(stop.name)}</div>
          <div class="next-op-mini-meta">${esc(safeOperationText(stop))}</div>
        </div>
        <div class="next-op-mini-km" data-op-km="${esc(stop.name)}">${esc(safeDistance(stop))}</div>
      </button>
    `;
  }

  function renderEnhancedNextOps() {
    const listEl = document.getElementById("nextOpsList");
    const countEl = document.getElementById("nextOpsCount");

    if (!listEl) return;

    const items = safeStops();

    if (countEl) countEl.textContent = `${items.length} durak`;

    if (!items.length) {
      listEl.innerHTML = `
        <div class="next-ops-final-wrap">
          <div class="next-ops-final-empty">İşlemli durak bulunmuyor.</div>
        </div>
      `;
      return;
    }

    const first = items[0];
    const rest = items.slice(1, 5);

    listEl.innerHTML = `
      <div class="next-ops-final-wrap">
        ${renderHero(first)}

        ${rest.length ? `
          <div class="next-op-section-title">Sonraki İşlemler</div>
          <div class="next-op-mini-list">
            ${rest.map(renderMini).join("")}
          </div>
        ` : ""}
      </div>
    `;
  }

  function refreshDistances() {
    document.querySelectorAll("[data-op-km]").forEach(el => {
      const name = el.getAttribute("data-op-km") || "";
      let stop = null;

      try {
        if (typeof stops !== "undefined" && Array.isArray(stops)) {
          stop = stops.find(s => s.name === name);
        }
      } catch (e) {}

      if (stop) el.textContent = safeDistance(stop);
    });
  }

  function bindActions() {
    const listEl = document.getElementById("nextOpsList");
    if (!listEl || listEl.dataset.nextOpsFinalBound === "1") return;

    listEl.dataset.nextOpsFinalBound = "1";

    listEl.addEventListener("click", function (e) {
      const task = e.target.closest("[data-next-task]");
      if (task) {
        e.preventDefault();
        e.stopPropagation();

        const name = task.getAttribute("data-stop") || "";
        let stop = null;

        try {
          if (typeof stops !== "undefined" && Array.isArray(stops)) {
            stop = stops.find(s => s.name === name);
          }
        } catch (err) {}

        const action = task.getAttribute("data-next-task");

        if (action === "speak") speakStop(stop);
        if (action === "people") openStop(name);
        if (action === "bag") openStop(name);
        if (action === "done") {
          setDone(name);
          renderEnhancedNextOps();
        }

        return;
      }

      const mini = e.target.closest("[data-next-op-stop]");
      if (mini) {
        e.preventDefault();
        e.stopPropagation();
        openStop(mini.getAttribute("data-next-op-stop") || "");
      }
    }, true);
  }

  function boot() {
    try {
      window.renderNextOpsPanel = renderEnhancedNextOps;
    } catch (e) {}

    bindActions();
    renderEnhancedNextOps();
    refreshDistances();

    setInterval(refreshDistances, 2500);
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", boot);
  } else {
    boot();
  }

  setTimeout(boot, 800);
  setTimeout(boot, 1800);
})();

/* MUAVIN_NEXT_OPS_BUBBLE_DRAG_V4_JS */
(function () {
  if (window.MUAVIN_NEXT_OPS_BUBBLE_DRAG_V4) return;
  window.MUAVIN_NEXT_OPS_BUBBLE_DRAG_V4 = true;

  const STORAGE_KEY = "muavinNextOpsBubblePositionV4";
  let drag = null;
  let suppressClickUntil = 0;

  function getMap() {
    if (window.MUAVIN_LIVE_MAP && window.MUAVIN_LIVE_MAP._container) return window.MUAVIN_LIVE_MAP;
    if (window.map && window.map._container) return window.map;
    return null;
  }

  function getContainer() {
    const map = getMap();
    return map && map._container ? map._container : document.querySelector(".leaflet-container");
  }

  function getPanel() {
    return document.getElementById("nextOpsPanel");
  }

  function clamp(v, min, max) {
    return Math.max(min, Math.min(max, v));
  }

  function getPoint(e) {
    if (e.touches && e.touches.length) {
      return { x: e.touches[0].clientX, y: e.touches[0].clientY };
    }

    if (e.changedTouches && e.changedTouches.length) {
      return { x: e.changedTouches[0].clientX, y: e.changedTouches[0].clientY };
    }

    return { x: e.clientX, y: e.clientY };
  }

  function disableMapMove() {
    const map = getMap();
    if (!map) return;

    try { map.dragging.disable(); } catch (e) {}
    try { map.touchZoom.disable(); } catch (e) {}
    try { map.doubleClickZoom.disable(); } catch (e) {}
  }

  function enableMapMove() {
    const map = getMap();
    if (!map) return;

    try { map.dragging.enable(); } catch (e) {}
    try { map.touchZoom.enable(); } catch (e) {}
    try { map.doubleClickZoom.enable(); } catch (e) {}
  }

  function applyPosition(panel, x, y, save) {
    const container = getContainer();
    if (!container || !panel) return;

    const cRect = container.getBoundingClientRect();
    const pRect = panel.getBoundingClientRect();

    const margin = 8;
    const maxX = Math.max(margin, cRect.width - pRect.width - margin);
    const maxY = Math.max(margin, cRect.height - pRect.height - margin);

    x = clamp(x, margin, maxX);
    y = clamp(y, margin, maxY);

    panel.classList.add("is-nextops-positioned");
    panel.style.setProperty("--nextops-left", x + "px");
    panel.style.setProperty("--nextops-top", y + "px");

    if (save) {
      try {
        localStorage.setItem(STORAGE_KEY, JSON.stringify({
          xPct: x / Math.max(cRect.width, 1),
          yPct: y / Math.max(cRect.height, 1)
        }));
      } catch (e) {}
    }
  }

  function restorePosition() {
    const panel = getPanel();
    const container = getContainer();

    if (!panel || !container) return;

    try {
      const saved = JSON.parse(localStorage.getItem(STORAGE_KEY) || "null");
      if (!saved || typeof saved.xPct !== "number" || typeof saved.yPct !== "number") return;

      const cRect = container.getBoundingClientRect();

      applyPosition(
        panel,
        saved.xPct * cRect.width,
        saved.yPct * cRect.height,
        false
      );
    } catch (e) {}
  }

  function bindDrag() {
    const panel = getPanel();
    const container = getContainer();

    if (!panel || !container) {
      setTimeout(bindDrag, 500);
      return;
    }

    restorePosition();

    if (panel.dataset.nextOpsDragV4 === "1") return;
    panel.dataset.nextOpsDragV4 = "1";

    function start(e) {
      if (!panel.classList.contains("collapsed")) return;

      const p = getPoint(e);
      const cRect = container.getBoundingClientRect();
      const pRect = panel.getBoundingClientRect();

      drag = {
        startX: p.x,
        startY: p.y,
        baseX: pRect.left - cRect.left,
        baseY: pRect.top - cRect.top,
        moved: false
      };

      panel.classList.add("is-nextops-dragging");
      disableMapMove();
    }

    function move(e) {
      if (!drag) return;
      if (!panel.classList.contains("collapsed")) return;

      const p = getPoint(e);
      const dx = p.x - drag.startX;
      const dy = p.y - drag.startY;

      if (Math.abs(dx) > 5 || Math.abs(dy) > 5) {
        drag.moved = true;
      }

      if (!drag.moved) return;

      e.preventDefault();
      e.stopPropagation();
      if (e.stopImmediatePropagation) e.stopImmediatePropagation();

      applyPosition(panel, drag.baseX + dx, drag.baseY + dy, true);
    }

    function end(e) {
      if (!drag) return;

      if (drag.moved) {
        suppressClickUntil = Date.now() + 500;
        e.preventDefault();
        e.stopPropagation();
        if (e.stopImmediatePropagation) e.stopImmediatePropagation();
      }

      panel.classList.remove("is-nextops-dragging");
      drag = null;
      enableMapMove();
    }

    panel.addEventListener("touchstart", start, { passive:false, capture:true });
    panel.addEventListener("touchmove", move, { passive:false, capture:true });
    panel.addEventListener("touchend", end, { passive:false, capture:true });
    panel.addEventListener("touchcancel", end, { passive:false, capture:true });

    panel.addEventListener("mousedown", start, true);
    window.addEventListener("mousemove", move, true);
    window.addEventListener("mouseup", end, true);

    panel.addEventListener("click", function (e) {
      if (Date.now() < suppressClickUntil) {
        e.preventDefault();
        e.stopPropagation();
        if (e.stopImmediatePropagation) e.stopImmediatePropagation();
      }
    }, true);

    window.addEventListener("resize", restorePosition);

    const toggle = document.getElementById("nextOpsToggle");
    if (toggle && toggle.dataset.dragAwareV4 !== "1") {
      toggle.dataset.dragAwareV4 = "1";

      toggle.addEventListener("click", function () {
        setTimeout(function () {
          if (panel.classList.contains("collapsed")) {
            restorePosition();
          }
        }, 80);
      }, true);
    }
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", bindDrag);
  } else {
    bindDrag();
  }

  setTimeout(bindDrag, 800);
  setTimeout(bindDrag, 1800);
  setTimeout(bindDrag, 3200);
})();

/* MUAVIN_CLEAN_START_MODE_V10_JS */
(function () {
  if (window.MUAVIN_CLEAN_START_MODE_V10) return;
  window.MUAVIN_CLEAN_START_MODE_V10 = true;

  let btn = null;
  let clean = true;

  function getMap() {
    if (window.MUAVIN_LIVE_MAP && window.MUAVIN_LIVE_MAP._container) return window.MUAVIN_LIVE_MAP;
    if (window.map && window.map._container) return window.map;
    return null;
  }

  function getContainer() {
    const map = getMap();
    return map && map._container ? map._container : document.querySelector(".leaflet-container");
  }

  function setButtonText() {
    if (!btn) return;

    btn.innerHTML = clean
      ? '<span class="clean-icon">☰</span><span>Kontroller</span>'
      : '<span class="clean-icon">⌄</span><span>Sade</span>';
  }

  function closeHeavyPanels() {
    const nextOps = document.getElementById("nextOpsPanel");
    const nextOpsToggle = document.getElementById("nextOpsToggle");

    if (nextOps) nextOps.classList.add("collapsed");
    if (nextOpsToggle) nextOpsToggle.textContent = "Göster";

    document.querySelectorAll(".muavin-route-summary-card-final").forEach(function (el) {
      el.classList.remove("is-open");
    });

    document.querySelectorAll(".muavin-summary-bubble-final").forEach(function (el) {
      el.classList.remove("is-open");
    });

    document.querySelectorAll(".muavin-tools-sheet-final").forEach(function (el) {
      el.classList.remove("is-open");
    });
  }

  function applyCleanMode(on) {
    clean = !!on;

    if (clean) {
      closeHeavyPanels();
      document.body.classList.add("muavin-map-clean-start");
    } else {
      document.body.classList.remove("muavin-map-clean-start");
      closeHeavyPanels();
    }

    setButtonText();

    setTimeout(function () {
      try {
        const map = getMap();
        if (map && map.invalidateSize) map.invalidateSize(true);
      } catch (e) {}
    }, 120);
  }

  function ensureButton() {
    const container = getContainer();

    if (!container) {
      setTimeout(ensureButton, 500);
      return;
    }

    if (btn && btn.isConnected) return;

    btn = document.createElement("button");
    btn.type = "button";
    btn.className = "muavin-clean-toggle-v10";
    btn.title = "Kontrolleri aç/kapat";
    btn.setAttribute("aria-label", "Kontrolleri aç/kapat");

    btn.addEventListener("click", function (e) {
      e.preventDefault();
      e.stopPropagation();
      applyCleanMode(!clean);
    });

    try {
      if (window.L && L.DomEvent) {
        L.DomEvent.disableClickPropagation(btn);
        L.DomEvent.disableScrollPropagation(btn);
      }
    } catch (e) {}

    container.appendChild(btn);
    setButtonText();
  }

  function boot() {
    ensureButton();

    // Her sayfa açılışında temiz başlasın.
    applyCleanMode(true);
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", boot);
  } else {
    boot();
  }

  setTimeout(boot, 700);
  setTimeout(boot, 1600);
})();
