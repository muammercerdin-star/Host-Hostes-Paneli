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



/* MUAVIN_NAV_3D_FEEL_V1_JS */
(function () {
  if (window.MUAVIN_NAV_3D_FEEL_V1) return;
  window.MUAVIN_NAV_3D_FEEL_V1 = true;

  let nav3dBtn = null;

  function getMap() {
    if (window.MUAVIN_LIVE_MAP && window.MUAVIN_LIVE_MAP._container) {
      return window.MUAVIN_LIVE_MAP;
    }

    if (window.map && window.map._container) {
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

  function applyState(map, on) {
    if (!map || !map._container) return;

    map._container.classList.toggle("muavin-nav-3d", !!on);

    if (nav3dBtn) {
      nav3dBtn.classList.toggle("is-on", !!on);
      nav3dBtn.innerHTML = on
        ? '<span class="nav3d-icon">◆</span><span>3D</span>'
        : '<span class="nav3d-icon">◇</span><span>3D</span>';
    }

    try {
      localStorage.setItem("muavinNav3dMode", on ? "1" : "0");
    } catch (e) {}
  }

  function ensureButton(map) {
    if (!map || !map._container) return;

    if (nav3dBtn && nav3dBtn.isConnected) return;

    nav3dBtn = document.createElement("button");
    nav3dBtn.type = "button";
    nav3dBtn.className = "muavin-nav3d-control";
    nav3dBtn.title = "3D navigasyon hissi";
    nav3dBtn.setAttribute("aria-label", "3D navigasyon hissi");
    nav3dBtn.innerHTML = '<span class="nav3d-icon">◇</span><span>3D</span>';

    nav3dBtn.addEventListener("click", function () {
      const isOn = map._container.classList.contains("muavin-nav-3d");
      applyState(map, !isOn);
    });

    map._container.appendChild(nav3dBtn);
  }

  function boot() {
    const map = getMap();

    if (!map || !map._container) {
      setTimeout(boot, 500);
      return;
    }

    ensureButton(map);

    let saved = "1";
    try {
      saved = localStorage.getItem("muavinNav3dMode") || "1";
    } catch (e) {}

    applyState(map, saved !== "0");
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", boot);
  } else {
    boot();
  }
})();



/* MUAVIN_ROTATE_GESTURE_V1_JS */
(function () {
  if (window.MUAVIN_ROTATE_GESTURE_V1) return;
  window.MUAVIN_ROTATE_GESTURE_V1 = true;

  let bearing = 0;
  let active = true;
  let gesture = null;
  let rotateControl = null;
  let resetBtn = null;
  let toggleBtn = null;

  function getMap() {
    if (window.MUAVIN_LIVE_MAP && window.MUAVIN_LIVE_MAP._container) {
      return window.MUAVIN_LIVE_MAP;
    }

    if (window.map && window.map._container) {
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

  function normalizeDeg(v) {
    v = Number(v) || 0;
    while (v > 180) v -= 360;
    while (v < -180) v += 360;
    if (Math.abs(v) < 0.4) v = 0;
    return v;
  }

  function angleFromTouches(t1, t2) {
    return Math.atan2(t2.clientY - t1.clientY, t2.clientX - t1.clientX) * 180 / Math.PI;
  }

  function distanceFromTouches(t1, t2) {
    const dx = t2.clientX - t1.clientX;
    const dy = t2.clientY - t1.clientY;
    return Math.sqrt(dx * dx + dy * dy);
  }

  function shortestDelta(start, current) {
    let d = current - start;
    while (d > 180) d -= 360;
    while (d < -180) d += 360;
    return d;
  }

  function updateControl() {
    if (!toggleBtn || !resetBtn) return;

    toggleBtn.classList.toggle("is-on", !!active);
    toggleBtn.classList.toggle("is-off", !active);

    const shown = Math.round(bearing);
    resetBtn.innerHTML = `N<span class="muavin-rotate-deg">${shown}°</span>`;
  }

  function applyBearing(map, nextBearing) {
    if (!map || !map._container) return;

    bearing = normalizeDeg(nextBearing);

    const scale = Math.abs(bearing) > 1 ? 1.18 : 1;

    map._container.classList.add("muavin-bearing-enabled");
    map._container.style.setProperty("--muavin-map-bearing", bearing + "deg");
    map._container.style.setProperty("--muavin-map-scale", String(scale));

    try {
      localStorage.setItem("muavinMapBearing", String(bearing));
    } catch (e) {}

    updateControl();
  }

  function setActive(next) {
    active = !!next;

    try {
      localStorage.setItem("muavinRotateGestureActive", active ? "1" : "0");
    } catch (e) {}

    updateControl();
  }

  function ensureControl(map) {
    if (!map || !map._container) return;

    if (rotateControl && rotateControl.isConnected) {
      updateControl();
      return;
    }

    rotateControl = document.createElement("div");
    rotateControl.className = "muavin-rotate-control";

    resetBtn = document.createElement("button");
    resetBtn.type = "button";
    resetBtn.className = "muavin-rotate-reset";
    resetBtn.title = "Haritayı kuzeye sıfırla";
    resetBtn.setAttribute("aria-label", "Haritayı kuzeye sıfırla");

    toggleBtn = document.createElement("button");
    toggleBtn.type = "button";
    toggleBtn.className = "muavin-rotate-toggle";
    toggleBtn.title = "İki parmakla döndürmeyi aç/kapat";
    toggleBtn.setAttribute("aria-label", "İki parmakla döndürmeyi aç/kapat");
    toggleBtn.textContent = "↻";

    resetBtn.addEventListener("click", function () {
      applyBearing(map, 0);
    });

    toggleBtn.addEventListener("click", function () {
      setActive(!active);
    });

    rotateControl.appendChild(resetBtn);
    rotateControl.appendChild(toggleBtn);
    map._container.appendChild(rotateControl);

    updateControl();
  }

  function bindGesture(map) {
    const el = map && map._container;
    if (!el || el.dataset.muavinRotateGestureBound === "1") return;
    el.dataset.muavinRotateGestureBound = "1";

    el.addEventListener("touchstart", function (e) {
      if (!active) return;
      if (!e.touches || e.touches.length !== 2) return;

      const t1 = e.touches[0];
      const t2 = e.touches[1];

      gesture = {
        startAngle: angleFromTouches(t1, t2),
        startDistance: distanceFromTouches(t1, t2),
        baseBearing: bearing,
        rotating: false
      };
    }, { passive: true, capture: true });

    el.addEventListener("touchmove", function (e) {
      if (!active) return;
      if (!gesture || !e.touches || e.touches.length !== 2) return;

      const t1 = e.touches[0];
      const t2 = e.touches[1];

      const currentAngle = angleFromTouches(t1, t2);
      const currentDistance = distanceFromTouches(t1, t2);
      const angleDelta = shortestDelta(gesture.startAngle, currentAngle);
      const distanceRatio = currentDistance / Math.max(gesture.startDistance, 1);

      /*
        Küçük açı değişimlerinde normal Leaflet pinch zoom'a izin veriyoruz.
        Açı farkı büyüyünce döndürme moduna geçiyoruz.
      */
      if (!gesture.rotating && Math.abs(angleDelta) > 7 && Math.abs(distanceRatio - 1) < 0.32) {
        gesture.rotating = true;
      }

      if (gesture.rotating) {
        e.preventDefault();
        e.stopPropagation();
        if (e.stopImmediatePropagation) e.stopImmediatePropagation();

        applyBearing(map, gesture.baseBearing + angleDelta);
      }
    }, { passive: false, capture: true });

    el.addEventListener("touchend", function (e) {
      if (!e.touches || e.touches.length < 2) {
        gesture = null;
      }
    }, { passive: true, capture: true });

    el.addEventListener("touchcancel", function () {
      gesture = null;
    }, { passive: true, capture: true });
  }

  function boot() {
    const map = getMap();

    if (!map || !map._container) {
      setTimeout(boot, 500);
      return;
    }

    try {
      bearing = normalizeDeg(localStorage.getItem("muavinMapBearing") || "0");
      active = (localStorage.getItem("muavinRotateGestureActive") || "1") !== "0";
    } catch (e) {}

    ensureControl(map);
    bindGesture(map);
    applyBearing(map, bearing);
    setActive(active);
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", boot);
  } else {
    boot();
  }
})();



/* MUAVIN_KM_LABELS_V1_JS */
(function () {
  if (window.MUAVIN_KM_LABELS_V1) return;
  window.MUAVIN_KM_LABELS_V1 = true;

  let kmGroup = null;
  let kmBtn = null;
  let kmOn = false;
  let currentLatLng = null;
  let refreshTimer = null;

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
    if (v < 1) return Math.round(v * 1000) + " m";
    if (v < 10) return v.toFixed(1) + " km";
    return Math.round(v) + " km";
  }

  function flattenLatLngs(latlngs) {
    const out = [];
    function walk(arr) {
      if (!arr) return;
      if (arr.lat !== undefined && arr.lng !== undefined) {
        out.push(arr);
        return;
      }
      if (Array.isArray(arr)) {
        arr.forEach(walk);
      }
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

  function isOurMarker(layer) {
    try {
      const icon = layer.getIcon && layer.getIcon();
      const cls = icon && icon.options && icon.options.className || "";

      if (cls.includes("muavin-gm-marker-icon")) return true;
      if (cls.includes("muavin-km-label-icon")) return true;
    } catch (e) {}
    return false;
  }

  function getStopMarkers(map, routePoints) {
    const markers = [];

    map.eachLayer(function (layer) {
      try {
        if (!window.L || !(layer instanceof L.Marker)) return;
        if (isOurMarker(layer)) return;

        const latlng = layer.getLatLng && layer.getLatLng();
        if (!latlng) return;

        const iconEl = layer._icon;
        const html = iconEl ? (iconEl.innerHTML || "") : "";
        const text = iconEl ? (iconEl.textContent || "") : "";

        // Canlı konum, buton veya km label gibi şeyleri dışarıda bırak
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

    // Aynı noktaya çok yakın tekrarlar varsa azalt
    const unique = [];
    markers.forEach(function (m) {
      const last = unique[unique.length - 1];
      if (!last || kmBetween(last.latlng, m.latlng) > 0.08) {
        unique.push(m);
      }
    });

    return unique;
  }

  function midpoint(a, b) {
    return L.latLng((a.lat + b.lat) / 2, (a.lng + b.lng) / 2);
  }

  function makeKmIcon(text, live) {
    return L.divIcon({
      className: "muavin-km-label-icon",
      iconSize: null,
      iconAnchor: [34, 14],
      html: `<div class="muavin-km-label ${live ? "is-live" : ""}">${text}</div>`
    });
  }

  function addLabel(map, latlng, html, live) {
    L.marker(latlng, {
      icon: makeKmIcon(html, live),
      interactive: false,
      zIndexOffset: live ? 9900 : 8500
    }).addTo(kmGroup);
  }

  function segmentDistance(routePoints, cum, aOrder, bOrder, aLatLng, bLatLng) {
    if (routePoints && cum && aOrder !== undefined && bOrder !== undefined && bOrder > aOrder) {
      const d = Math.abs(cum[bOrder] - cum[aOrder]);
      if (d > 0.03) return d;
    }
    return kmBetween(aLatLng, bLatLng);
  }

  function clearKm() {
    if (kmGroup) kmGroup.clearLayers();
  }

  function refreshKm() {
    const map = getMap();
    if (!map || !window.L) return;

    if (!kmGroup) {
      kmGroup = L.layerGroup().addTo(map);
    }

    clearKm();

    if (!kmOn) return;

    const routePoints = getMainRouteLine(map);
    const cum = routePoints ? routeCumulative(routePoints) : null;
    const stops = getStopMarkers(map, routePoints);

    if (stops.length >= 2) {
      for (let i = 0; i < stops.length - 1; i++) {
        const a = stops[i];
        const b = stops[i + 1];

        const d = segmentDistance(routePoints, cum, a.order, b.order, a.latlng, b.latlng);
        const mid = routePoints && b.order > a.order
          ? routePoints[Math.round((a.order + b.order) / 2)]
          : midpoint(a.latlng, b.latlng);

        addLabel(map, mid, formatKm(d), false);
      }
    }

    // Canlı konumdan sıradaki durağa mesafe
    if (currentLatLng && stops.length) {
      let next = null;
      let currentOrder = routePoints ? nearestRouteIndex(routePoints, currentLatLng) : null;

      if (routePoints) {
        next = stops.find(function (s) {
          return s.order > currentOrder;
        }) || stops[0];
      } else {
        next = stops
          .map(function (s) {
            return { s, d: kmBetween(currentLatLng, s.latlng) };
          })
          .sort(function (a, b) { return a.d - b.d; })[0]?.s;
      }

      if (next) {
        let dLive = routePoints && next.order > currentOrder
          ? Math.abs(cum[next.order] - cum[currentOrder])
          : kmBetween(currentLatLng, next.latlng);

        const liveMid = midpoint(currentLatLng, next.latlng);
        addLabel(map, liveMid, `${formatKm(dLive)}<small>SIRADAKİ</small>`, true);
      }
    }
  }

  function scheduleRefresh() {
    clearTimeout(refreshTimer);
    refreshTimer = setTimeout(refreshKm, 250);
  }

  function ensureButton(map) {
    if (!map || !map._container) return;

    if (kmBtn && kmBtn.isConnected) return;

    kmBtn = document.createElement("button");
    kmBtn.type = "button";
    kmBtn.className = "muavin-km-control";
    kmBtn.textContent = "KM";
    kmBtn.title = "Duraklar arası km göster";
    kmBtn.setAttribute("aria-label", "Duraklar arası km göster");

    kmBtn.addEventListener("click", function () {
      kmOn = !kmOn;
      kmBtn.classList.toggle("is-on", kmOn);

      try {
        localStorage.setItem("muavinKmLabelsOn", kmOn ? "1" : "0");
      } catch (e) {}

      refreshKm();
    });

    map._container.appendChild(kmBtn);
  }

  function wrapLocationUpdate() {
    if (window.MUAVIN_KM_LOCATION_WRAPPED) return;
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
        scheduleRefresh();
      }

      return result;
    };

    window.MUAVIN_KM_LOCATION_WRAPPED = true;
  }

  function boot() {
    const map = getMap();

    if (!map || !window.L || !map._container) {
      setTimeout(boot, 500);
      return;
    }

    if (!kmGroup) {
      kmGroup = L.layerGroup().addTo(map);
    }

    ensureButton(map);
    wrapLocationUpdate();

    try {
      kmOn = (localStorage.getItem("muavinKmLabelsOn") || "0") === "1";
    } catch (e) {
      kmOn = false;
    }

    if (kmBtn) kmBtn.classList.toggle("is-on", kmOn);

    try {
      map.on("zoomend moveend layeradd layerremove", scheduleRefresh);
    } catch (e) {}

    setTimeout(refreshKm, 800);
    setTimeout(refreshKm, 2000);
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", boot);
  } else {
    boot();
  }
})();



/* MUAVIN_ROUTE_SUMMARY_V1_JS */
(function () {
  if (window.MUAVIN_ROUTE_SUMMARY_V1) return;
  window.MUAVIN_ROUTE_SUMMARY_V1 = true;

  let currentLatLng = null;
  let currentSpeedKmh = 0;
  let summaryCard = null;
  let refreshTimer = null;

  const AVG_SPEED_KMH = 70;

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
      if (cls.includes("muavin-km-label-icon")) return true;
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
        if (text.trim() === "KM") return;

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

  function fallbackRemainingFromStops(current, stops) {
    if (!current || !stops.length) return 0;

    const sorted = stops
      .map(function (s) {
        return { s, d: kmBetween(current, s.latlng) };
      })
      .sort(function (a, b) { return a.d - b.d; });

    const nearest = sorted[0]?.s;
    if (!nearest) return 0;

    let idx = stops.indexOf(nearest);
    if (idx < 0) idx = 0;

    let total = kmBetween(current, stops[idx].latlng);

    for (let i = idx; i < stops.length - 1; i++) {
      total += kmBetween(stops[i].latlng, stops[i + 1].latlng);
    }

    return total;
  }

  function ensureCard(map) {
    if (!map || !map._container) return;

    if (summaryCard && summaryCard.isConnected) return;

    summaryCard = document.createElement("div");
    summaryCard.className = "muavin-route-summary-card";
    summaryCard.innerHTML = `
      <div class="muavin-route-summary-head">
        <div class="muavin-route-summary-title">ROTA ÖZETİ</div>
        <div class="muavin-route-summary-pill">CANLI</div>
      </div>

      <div class="muavin-route-summary-grid">
        <div class="muavin-route-summary-item">
          <div class="muavin-route-summary-label">Canlı → Sıradaki</div>
          <div class="muavin-route-summary-value is-blue" data-route-summary="liveNext">—</div>
        </div>

        <div class="muavin-route-summary-item">
          <div class="muavin-route-summary-label">Sıradaki → Sonraki</div>
          <div class="muavin-route-summary-value" data-route-summary="nextNext">—</div>
        </div>

        <div class="muavin-route-summary-item">
          <div class="muavin-route-summary-label">Kalan toplam rota</div>
          <div class="muavin-route-summary-value is-green" data-route-summary="remaining">—</div>
        </div>

        <div class="muavin-route-summary-item">
          <div class="muavin-route-summary-label">Tahmini varış</div>
          <div class="muavin-route-summary-value is-yellow" data-route-summary="eta">—</div>
        </div>
      </div>

      <div class="muavin-route-summary-note" data-route-summary="note">
        Konum bekleniyor...
      </div>
    `;

    map._container.appendChild(summaryCard);
  }

  function setValue(key, value) {
    if (!summaryCard) return;

    const el = summaryCard.querySelector('[data-route-summary="' + key + '"]');
    if (el) el.textContent = value;
  }

  function setNote(value) {
    setValue("note", value);
  }

  function updateSummary() {
    const map = getMap();
    if (!map || !window.L) return;

    ensureCard(map);

    if (!currentLatLng) {
      setValue("liveNext", "—");
      setValue("nextNext", "—");
      setValue("remaining", "—");
      setValue("eta", "—");
      setNote("Konum bekleniyor...");
      return;
    }

    const routePoints = getMainRouteLine(map);
    const cum = routePoints ? routeCumulative(routePoints) : null;
    const stops = getStopMarkers(map, routePoints);

    if (!stops.length) {
      setValue("liveNext", "—");
      setValue("nextNext", "—");
      setValue("remaining", "—");
      setValue("eta", "—");
      setNote("Durak koordinatları bulunamadı.");
      return;
    }

    let currentOrder = routePoints ? nearestRouteIndex(routePoints, currentLatLng) : null;

    let nextStop = null;
    let nextStopIndex = -1;

    if (routePoints) {
      for (let i = 0; i < stops.length; i++) {
        if (stops[i].order > currentOrder + 2) {
          nextStop = stops[i];
          nextStopIndex = i;
          break;
        }
      }

      if (!nextStop) {
        nextStop = stops[stops.length - 1];
        nextStopIndex = stops.length - 1;
      }
    } else {
      const sorted = stops
        .map(function (s, i) {
          return { s, i, d: kmBetween(currentLatLng, s.latlng) };
        })
        .sort(function (a, b) { return a.d - b.d; });

      nextStop = sorted[0]?.s || stops[0];
      nextStopIndex = sorted[0]?.i || 0;
    }

    const afterStop = stops[nextStopIndex + 1] || null;

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
      remaining = fallbackRemainingFromStops(currentLatLng, stops);
    }

    const etaSpeed = currentSpeedKmh >= 15 ? currentSpeedKmh : AVG_SPEED_KMH;
    const eta = remaining > 0 ? formatEta(remaining / etaSpeed) : "—";

    setValue("liveNext", formatKm(liveToNext));
    setValue("nextNext", afterStop ? formatKm(nextToAfter) : "Son durak");
    setValue("remaining", formatKm(remaining));
    setValue("eta", eta);

    const noteSpeed = currentSpeedKmh >= 15
      ? "Canlı hızla hesaplandı: " + Math.round(currentSpeedKmh) + " km/sa"
      : "Tahmini varış " + AVG_SPEED_KMH + " km/sa ortalama ile hesaplandı.";

    setNote(noteSpeed);
  }

  function scheduleUpdate() {
    clearTimeout(refreshTimer);
    refreshTimer = setTimeout(updateSummary, 250);
  }

  function wrapLocation() {
    if (window.MUAVIN_ROUTE_SUMMARY_LOCATION_WRAPPED) return;

    if (typeof window.MUAVIN_UPDATE_BLUE_LOCATION !== "function") {
      setTimeout(wrapLocation, 500);
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

    window.MUAVIN_ROUTE_SUMMARY_LOCATION_WRAPPED = true;
  }

  function startSpeedWatch() {
    if (!navigator.geolocation) return;

    navigator.geolocation.watchPosition(
      function (pos) {
        const c = pos.coords || {};
        const speedMs = Number(c.speed);

        if (Number.isFinite(speedMs) && speedMs > 0) {
          currentSpeedKmh = speedMs * 3.6;
        }

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

  function closeOldDetailedKmLabels() {
    try {
      localStorage.setItem("muavinKmLabelsOn", "0");
    } catch (e) {}

    setTimeout(function () {
      const btn = document.querySelector(".muavin-km-control.is-on");
      if (btn) btn.click();
    }, 500);

    setTimeout(function () {
      document.querySelectorAll(".leaflet-marker-icon.muavin-km-label-icon").forEach(function (el) {
        el.style.display = "none";
      });
    }, 1200);
  }

  function boot() {
    const map = getMap();

    if (!map || !map._container || !window.L) {
      setTimeout(boot, 500);
      return;
    }

    ensureCard(map);
    wrapLocation();
    startSpeedWatch();
    closeOldDetailedKmLabels();

    try {
      map.on("zoomend moveend layeradd layerremove", scheduleUpdate);
    } catch (e) {}

    setTimeout(updateSummary, 700);
    setTimeout(updateSummary, 1800);
    setInterval(updateSummary, 5000);
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", boot);
  } else {
    boot();
  }
})();



/* MUAVIN_ROUTE_SUMMARY_BUBBLE_V1_JS */
(function () {
  if (window.MUAVIN_ROUTE_SUMMARY_BUBBLE_V1) return;
  window.MUAVIN_ROUTE_SUMMARY_BUBBLE_V1 = true;

  let bubble = null;
  let card = null;
  let isOpen = false;
  let observer = null;

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

  function readText(selector, fallback) {
    if (!card) return fallback;
    const el = card.querySelector(selector);
    return el && el.textContent.trim() ? el.textContent.trim() : fallback;
  }

  function updateBubbleText() {
    if (!bubble) return;

    const remaining = readText('[data-route-summary="remaining"]', "—");
    const eta = readText('[data-route-summary="eta"]', "—");

    const remEl = bubble.querySelector('[data-bubble="remaining"]');
    const etaEl = bubble.querySelector('[data-bubble="eta"]');

    if (remEl) remEl.textContent = remaining;
    if (etaEl) etaEl.textContent = eta;
  }

  function applyState(open) {
    isOpen = !!open;

    try {
      localStorage.setItem("muavinRouteSummaryBubbleOpen", isOpen ? "1" : "0");
    } catch (e) {}

    if (card) {
      card.classList.add("muavin-summary-messenger");
      card.classList.toggle("is-open", isOpen);
      card.classList.toggle("is-collapsed", !isOpen);
    }

    if (bubble) {
      bubble.classList.toggle("is-open", isOpen);
      bubble.setAttribute("aria-expanded", isOpen ? "true" : "false");
    }

    updateBubbleText();
  }

  function ensureBubble(map) {
    if (!map || !map._container) return;

    if (bubble && bubble.isConnected) return;

    bubble = document.createElement("button");
    bubble.type = "button";
    bubble.className = "muavin-summary-bubble";
    bubble.title = "Rota özetini aç/kapat";
    bubble.setAttribute("aria-label", "Rota özetini aç/kapat");
    bubble.innerHTML = `
      <span class="muavin-summary-bubble-icon">🧭</span>
      <span class="muavin-summary-bubble-text">
        <b>Rota</b>
        <span data-bubble="remaining">—</span>
        <span data-bubble="eta">—</span>
      </span>
    `;

    bubble.addEventListener("click", function () {
      applyState(!isOpen);
    });

    map._container.appendChild(bubble);
  }

  function ensureCloseButton() {
    if (!card) return;

    const head = card.querySelector(".muavin-route-summary-head");
    if (!head) return;

    if (head.querySelector(".muavin-summary-close")) return;

    const close = document.createElement("button");
    close.type = "button";
    close.className = "muavin-summary-close";
    close.innerHTML = "×";
    close.title = "Kapat";
    close.setAttribute("aria-label", "Rota özetini kapat");

    close.addEventListener("click", function (e) {
      e.preventDefault();
      e.stopPropagation();
      applyState(false);
    });

    head.appendChild(close);
  }

  function setupCard() {
    const map = getMap();

    if (!map || !map._container) {
      setTimeout(setupCard, 500);
      return;
    }

    ensureBubble(map);

    card = map._container.querySelector(".muavin-route-summary-card");

    if (!card) {
      setTimeout(setupCard, 500);
      return;
    }

    card.classList.add("muavin-summary-messenger");
    ensureCloseButton();

    try {
      isOpen = (localStorage.getItem("muavinRouteSummaryBubbleOpen") || "0") === "1";
    } catch (e) {
      isOpen = false;
    }

    applyState(isOpen);

    if (!observer) {
      observer = new MutationObserver(function () {
        updateBubbleText();
      });

      observer.observe(card, {
        childList: true,
        subtree: true,
        characterData: true
      });
    }

    updateBubbleText();
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", setupCard);
  } else {
    setupCard();
  }

  setTimeout(setupCard, 1000);
  setTimeout(setupCard, 2500);
})();



/* MUAVIN_SUMMARY_FLOAT_BUBBLE_V2_JS */
(function () {
  if (window.MUAVIN_SUMMARY_FLOAT_BUBBLE_V2) return;
  window.MUAVIN_SUMMARY_FLOAT_BUBBLE_V2 = true;

  function polishBubble() {
    const bubble = document.querySelector(".muavin-summary-bubble");
    const card = document.querySelector(".muavin-route-summary-card");

    if (bubble) {
      const icon = bubble.querySelector(".muavin-summary-bubble-icon");
      if (icon) icon.textContent = "🧭";

      bubble.title = "Rota özetini aç";
      bubble.setAttribute("aria-label", "Rota özetini aç");
    }

    if (card) {
      card.classList.add("muavin-summary-messenger");
    }
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", function () {
      setTimeout(polishBubble, 500);
      setTimeout(polishBubble, 1500);
    });
  } else {
    setTimeout(polishBubble, 500);
    setTimeout(polishBubble, 1500);
  }
})();



/* MUAVIN_DRAGGABLE_ROUTE_BUBBLE_V1_JS */
(function () {
  if (window.MUAVIN_DRAGGABLE_ROUTE_BUBBLE_V1) return;
  window.MUAVIN_DRAGGABLE_ROUTE_BUBBLE_V1 = true;

  const STORAGE_KEY = "muavinRouteBubblePositionV1";
  let suppressClickUntil = 0;

  function getMapContainer() {
    if (window.MUAVIN_LIVE_MAP && window.MUAVIN_LIVE_MAP._container) {
      return window.MUAVIN_LIVE_MAP._container;
    }

    if (window.map && window.map._container) {
      return window.map._container;
    }

    return document.querySelector(".leaflet-container");
  }

  function clamp(v, min, max) {
    return Math.max(min, Math.min(max, v));
  }

  function applyPosition(bubble, x, y) {
    const container = getMapContainer();
    if (!container || !bubble) return;

    const cRect = container.getBoundingClientRect();
    const bRect = bubble.getBoundingClientRect();

    const margin = 10;
    const maxX = Math.max(margin, cRect.width - bRect.width - margin);
    const maxY = Math.max(margin, cRect.height - bRect.height - margin);

    x = clamp(x, margin, maxX);
    y = clamp(y, margin, maxY);

    bubble.classList.add("is-drag-positioned");
    bubble.style.setProperty("--muavin-bubble-left", x + "px");
    bubble.style.setProperty("--muavin-bubble-top", y + "px");

    try {
      localStorage.setItem(STORAGE_KEY, JSON.stringify({
        xPct: x / Math.max(cRect.width, 1),
        yPct: y / Math.max(cRect.height, 1)
      }));
    } catch (e) {}
  }

  function restorePosition(bubble) {
    const container = getMapContainer();
    if (!container || !bubble) return;

    try {
      const saved = JSON.parse(localStorage.getItem(STORAGE_KEY) || "null");
      if (!saved || typeof saved.xPct !== "number" || typeof saved.yPct !== "number") return;

      const cRect = container.getBoundingClientRect();
      applyPosition(
        bubble,
        saved.xPct * cRect.width,
        saved.yPct * cRect.height
      );
    } catch (e) {}
  }

  function makeDraggable() {
    const bubble = document.querySelector(".muavin-summary-bubble");
    const container = getMapContainer();

    if (!bubble || !container) {
      setTimeout(makeDraggable, 500);
      return;
    }

    if (bubble.dataset.muavinDraggable === "1") {
      restorePosition(bubble);
      return;
    }

    bubble.dataset.muavinDraggable = "1";
    restorePosition(bubble);

    let drag = null;

    bubble.addEventListener("pointerdown", function (e) {
      if (e.button !== undefined && e.button !== 0) return;

      const cRect = container.getBoundingClientRect();
      const bRect = bubble.getBoundingClientRect();

      drag = {
        pointerId: e.pointerId,
        startX: e.clientX,
        startY: e.clientY,
        baseX: bRect.left - cRect.left,
        baseY: bRect.top - cRect.top,
        moved: false
      };

      try {
        bubble.setPointerCapture(e.pointerId);
      } catch (err) {}

      bubble.classList.add("is-dragging");
    });

    bubble.addEventListener("pointermove", function (e) {
      if (!drag) return;

      const dx = e.clientX - drag.startX;
      const dy = e.clientY - drag.startY;

      if (Math.abs(dx) > 4 || Math.abs(dy) > 4) {
        drag.moved = true;
      }

      if (drag.moved) {
        e.preventDefault();
        e.stopPropagation();

        applyPosition(
          bubble,
          drag.baseX + dx,
          drag.baseY + dy
        );
      }
    });

    function endDrag(e) {
      if (!drag) return;

      if (drag.moved) {
        suppressClickUntil = Date.now() + 450;
        e.preventDefault();
        e.stopPropagation();
      }

      try {
        bubble.releasePointerCapture(drag.pointerId);
      } catch (err) {}

      bubble.classList.remove("is-dragging");
      drag = null;
    }

    bubble.addEventListener("pointerup", endDrag);
    bubble.addEventListener("pointercancel", endDrag);

    bubble.addEventListener("click", function (e) {
      if (Date.now() < suppressClickUntil) {
        e.preventDefault();
        e.stopPropagation();
        if (e.stopImmediatePropagation) e.stopImmediatePropagation();
      }
    }, true);

    window.addEventListener("resize", function () {
      restorePosition(bubble);
    });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", makeDraggable);
  } else {
    makeDraggable();
  }

  setTimeout(makeDraggable, 1000);
  setTimeout(makeDraggable, 2500);
})();



/* MUAVIN_ROUTE_BUBBLE_DRAG_V2_JS */
(function () {
  if (window.MUAVIN_ROUTE_BUBBLE_DRAG_V2) return;
  window.MUAVIN_ROUTE_BUBBLE_DRAG_V2 = true;

  const STORAGE_KEY = "muavinRouteBubblePositionV2";
  let drag = null;
  let suppressClickUntil = 0;

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

  function clamp(v, min, max) {
    return Math.max(min, Math.min(max, v));
  }

  function getPoint(e) {
    if (e.touches && e.touches.length) {
      return {
        x: e.touches[0].clientX,
        y: e.touches[0].clientY
      };
    }

    if (e.changedTouches && e.changedTouches.length) {
      return {
        x: e.changedTouches[0].clientX,
        y: e.changedTouches[0].clientY
      };
    }

    return {
      x: e.clientX,
      y: e.clientY
    };
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

  function applyPosition(bubble, x, y, save) {
    const container = getContainer();
    if (!container || !bubble) return;

    const cRect = container.getBoundingClientRect();
    const bRect = bubble.getBoundingClientRect();

    const margin = 8;
    const maxX = Math.max(margin, cRect.width - bRect.width - margin);
    const maxY = Math.max(margin, cRect.height - bRect.height - margin);

    x = clamp(x, margin, maxX);
    y = clamp(y, margin, maxY);

    bubble.classList.add("is-drag-positioned");
    bubble.style.setProperty("--muavin-bubble-left", x + "px");
    bubble.style.setProperty("--muavin-bubble-top", y + "px");

    if (save) {
      try {
        localStorage.setItem(STORAGE_KEY, JSON.stringify({
          xPct: x / Math.max(cRect.width, 1),
          yPct: y / Math.max(cRect.height, 1)
        }));
      } catch (e) {}
    }
  }

  function restorePosition(bubble) {
    const container = getContainer();
    if (!container || !bubble) return;

    try {
      const saved = JSON.parse(localStorage.getItem(STORAGE_KEY) || "null");
      if (!saved || typeof saved.xPct !== "number" || typeof saved.yPct !== "number") return;

      const cRect = container.getBoundingClientRect();

      applyPosition(
        bubble,
        saved.xPct * cRect.width,
        saved.yPct * cRect.height,
        false
      );
    } catch (e) {}
  }

  function bindBubble() {
    const bubble = document.querySelector(".muavin-summary-bubble");
    const container = getContainer();

    if (!bubble || !container) {
      setTimeout(bindBubble, 500);
      return;
    }

    restorePosition(bubble);

    if (bubble.dataset.muavinDragV2 === "1") return;
    bubble.dataset.muavinDragV2 = "1";

    function start(e) {
      const p = getPoint(e);
      const cRect = container.getBoundingClientRect();
      const bRect = bubble.getBoundingClientRect();

      drag = {
        startX: p.x,
        startY: p.y,
        baseX: bRect.left - cRect.left,
        baseY: bRect.top - cRect.top,
        moved: false
      };

      bubble.classList.add("is-dragging");
      disableMapMove();
    }

    function move(e) {
      if (!drag) return;

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

      applyPosition(
        bubble,
        drag.baseX + dx,
        drag.baseY + dy,
        true
      );
    }

    function end(e) {
      if (!drag) return;

      if (drag.moved) {
        suppressClickUntil = Date.now() + 500;
        e.preventDefault();
        e.stopPropagation();
        if (e.stopImmediatePropagation) e.stopImmediatePropagation();
      }

      bubble.classList.remove("is-dragging");
      drag = null;
      enableMapMove();
    }

    bubble.addEventListener("touchstart", start, { passive: false, capture: true });
    bubble.addEventListener("touchmove", move, { passive: false, capture: true });
    bubble.addEventListener("touchend", end, { passive: false, capture: true });
    bubble.addEventListener("touchcancel", end, { passive: false, capture: true });

    bubble.addEventListener("mousedown", start, true);
    window.addEventListener("mousemove", move, true);
    window.addEventListener("mouseup", end, true);

    bubble.addEventListener("click", function (e) {
      if (Date.now() < suppressClickUntil) {
        e.preventDefault();
        e.stopPropagation();
        if (e.stopImmediatePropagation) e.stopImmediatePropagation();
      }
    }, true);

    window.addEventListener("resize", function () {
      restorePosition(bubble);
    });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", bindBubble);
  } else {
    bindBubble();
  }

  setTimeout(bindBubble, 800);
  setTimeout(bindBubble, 2000);
  setTimeout(bindBubble, 3500);
})();



/* MUAVIN_MINIMAL_SIMPLIFY_V1_JS */
(function () {
  if (window.MUAVIN_MINIMAL_SIMPLIFY_V1) return;
  window.MUAVIN_MINIMAL_SIMPLIFY_V1 = true;

  let fab = null;
  let sheet = null;

  function getMapContainer() {
    if (window.MUAVIN_LIVE_MAP && window.MUAVIN_LIVE_MAP._container) return window.MUAVIN_LIVE_MAP._container;
    if (window.map && window.map._container) return window.map._container;
    return document.querySelector(".leaflet-container");
  }

  function clickEl(el) {
    if (!el) return;
    try { el.click(); return; } catch (e) {}
    try {
      el.dispatchEvent(new MouseEvent("click", { bubbles: true, cancelable: true }));
    } catch (e) {}
  }

  function closeSheet() {
    if (sheet) sheet.classList.remove("is-open");
  }

  function toggleSheet() {
    if (!sheet) return;
    sheet.classList.toggle("is-open");
  }

  function ensureTools() {
    const container = getMapContainer();
    if (!container) {
      setTimeout(ensureTools, 500);
      return;
    }

    if (!fab) {
      fab = document.createElement("button");
      fab.type = "button";
      fab.className = "muavin-tools-fab";
      fab.setAttribute("aria-label", "Araçlar");
      fab.title = "Araçlar";
      fab.innerHTML = '<span class="fab-icon">⚙️</span><span class="fab-text">Araçlar</span>';
      fab.addEventListener("click", function (e) {
        e.preventDefault();
        e.stopPropagation();
        toggleSheet();
      });
      container.appendChild(fab);
    }

    if (!sheet) {
      sheet = document.createElement("div");
      sheet.className = "muavin-tools-sheet";
      sheet.innerHTML = `
        <div class="muavin-tools-sheet-head">HARİTA ARAÇLARI</div>
        <div class="muavin-tools-list">
          <button type="button" class="muavin-tools-btn" data-tool-action="3d">
            <span>3D görünüm</span><small>Aç / Kapat</small>
          </button>
          <button type="button" class="muavin-tools-btn" data-tool-action="km">
            <span>KM etiketleri</span><small>Aç / Kapat</small>
          </button>
          <button type="button" class="muavin-tools-btn" data-tool-action="north">
            <span>Kuzeye sıfırla</span><small>Pusula</small>
          </button>
        </div>
      `;

      sheet.addEventListener("click", function (e) {
        const btn = e.target.closest(".muavin-tools-btn");
        if (!btn) return;

        const act = btn.getAttribute("data-tool-action");

        if (act === "3d") {
          clickEl(document.querySelector(".muavin-nav3d-control"));
        } else if (act === "km") {
          clickEl(document.querySelector(".muavin-km-control"));
        } else if (act === "north") {
          clickEl(document.querySelector(".muavin-rotate-control .muavin-rotate-reset"));
        }

        closeSheet();
      });

      container.appendChild(sheet);
    }

    container.addEventListener("click", function (e) {
      if (!sheet || !fab) return;
      if (sheet.contains(e.target) || fab.contains(e.target)) return;
      closeSheet();
    }, true);
  }

  function simplifyBubble() {
    const bubble = document.querySelector(".muavin-summary-bubble");
    if (!bubble || bubble.dataset.muavinMinimalBubble === "1") return;

    bubble.dataset.muavinMinimalBubble = "1";
    bubble.innerHTML = `
      <span class="muavin-summary-bubble-icon">🧭</span>
      <span class="muavin-summary-bubble-text">
        <span data-bubble="remaining">—</span>
        <span data-bubble="eta">—</span>
      </span>
    `;
    bubble.title = "Rota özeti";
    bubble.setAttribute("aria-label", "Rota özeti");
  }

  function boot() {
    ensureTools();
    simplifyBubble();
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", boot);
  } else {
    boot();
  }

  setTimeout(boot, 700);
  setTimeout(boot, 1600);
  setTimeout(boot, 2800);
})();



/* MUAVIN_BOTTOM_ACTIONS_MINIMAL_V1_JS */
(function () {
  if (window.MUAVIN_BOTTOM_ACTIONS_MINIMAL_V1) return;
  window.MUAVIN_BOTTOM_ACTIONS_MINIMAL_V1 = true;

  function norm(s) {
    return String(s || "")
      .toLocaleLowerCase("tr-TR")
      .replace(/\s+/g, " ")
      .trim();
  }

  function visibleEnough(el) {
    try {
      const r = el.getBoundingClientRect();
      return r.width > 20 && r.height > 20;
    } catch (e) {
      return false;
    }
  }

  function findSmallestElementWithText(root, label) {
    const target = norm(label);
    const all = Array.from(root.querySelectorAll("*"));

    const matches = all.filter(function (el) {
      const t = norm(el.innerText || el.textContent || "");
      if (!t.includes(target)) return false;
      if (!visibleEnough(el)) return false;

      const r = el.getBoundingClientRect();
      return r.top > window.innerHeight * 0.45;
    });

    matches.sort(function (a, b) {
      const ar = a.getBoundingClientRect();
      const br = b.getBoundingClientRect();
      return (ar.width * ar.height) - (br.width * br.height);
    });

    return matches[0] || null;
  }

  function clickTarget(el) {
    if (!el) return;

    const clickable = el.closest("button,a,[role='button'],[onclick]") || el;

    try {
      clickable.click();
      return;
    } catch (e) {}

    try {
      clickable.dispatchEvent(new MouseEvent("click", {
        bubbles: true,
        cancelable: true
      }));
    } catch (e) {}
  }

  function commonParent(items) {
    const valid = items.filter(Boolean);
    if (!valid.length) return null;

    let p = valid[0].parentElement;

    while (p && p !== document.body) {
      if (valid.every(function (x) { return p.contains(x); })) {
        return p;
      }
      p = p.parentElement;
    }

    return valid[0].parentElement;
  }

  function setupBottomMinimal() {
    if (document.querySelector(".muavin-bottom-minibar")) return;

    const konumum = findSmallestElementWithText(document, "Konumum");
    const duraklar = findSmallestElementWithText(document, "Tüm Duraklar");
    const rota = findSmallestElementWithText(document, "Rota");
    const islemli = findSmallestElementWithText(document, "İşlemli");

    if (!duraklar || !rota) {
      setTimeout(setupBottomMinimal, 700);
      return;
    }

    const panel = commonParent([konumum, duraklar, rota, islemli]) || duraklar.parentElement;
    if (!panel) return;

    panel.classList.add("muavin-bottom-panel-simplified");

    [konumum, duraklar, rota, islemli].forEach(function (el) {
      if (el) el.classList.add("muavin-original-bottom-action-hidden");
    });

    const bar = document.createElement("div");
    bar.className = "muavin-bottom-minibar";
    bar.innerHTML = `
      <button type="button" class="muavin-mini-action is-primary" data-mini-action="duraklar">
        <span class="mini-icon">🗺️</span>
        <span>Duraklar</span>
      </button>

      <button type="button" class="muavin-mini-action is-primary" data-mini-action="rota">
        <span class="mini-icon">〽️</span>
        <span>Rota</span>
      </button>

      <button type="button" class="muavin-mini-action is-more" data-mini-action="more">
        <span>•••</span>
      </button>

      <div class="muavin-more-menu">
        <button type="button" data-more-action="konumum">
          <span>Konumum</span>
          <small>Canlı</small>
        </button>
        <button type="button" data-more-action="islemli">
          <span>İşlemli</span>
          <small>Durak</small>
        </button>
      </div>
    `;

    panel.appendChild(bar);

    const menu = bar.querySelector(".muavin-more-menu");

    bar.addEventListener("click", function (e) {
      const mini = e.target.closest("[data-mini-action]");
      const more = e.target.closest("[data-more-action]");

      if (mini) {
        const act = mini.getAttribute("data-mini-action");

        if (act === "duraklar") {
          clickTarget(duraklar);
          menu.classList.remove("is-open");
        }

        if (act === "rota") {
          clickTarget(rota);
          menu.classList.remove("is-open");
        }

        if (act === "more") {
          menu.classList.toggle("is-open");
        }
      }

      if (more) {
        const act = more.getAttribute("data-more-action");

        if (act === "konumum") clickTarget(konumum);
        if (act === "islemli") clickTarget(islemli);

        menu.classList.remove("is-open");
      }
    });

    document.addEventListener("click", function (e) {
      if (!bar.contains(e.target)) {
        menu.classList.remove("is-open");
      }
    }, true);
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", setupBottomMinimal);
  } else {
    setupBottomMinimal();
  }

  setTimeout(setupBottomMinimal, 800);
  setTimeout(setupBottomMinimal, 1800);
  setTimeout(setupBottomMinimal, 3200);
})();



/* MUAVIN_BOTTOM_DOCK_FIX_V2_JS */
(function () {
  if (window.MUAVIN_BOTTOM_DOCK_FIX_V2) return;
  window.MUAVIN_BOTTOM_DOCK_FIX_V2 = true;

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

  function findOriginal(label) {
    const target = norm(label);

    const hidden = Array.from(document.querySelectorAll(".muavin-original-bottom-action-hidden"));
    let found = hidden.find(function (el) {
      return norm(el.innerText || el.textContent || "").includes(target);
    });

    if (found) return found;

    const all = Array.from(document.querySelectorAll("button,a,[role='button'],[onclick],div,span"));
    found = all.find(function (el) {
      if (el.closest(".muavin-bottom-dock-v2")) return false;
      if (el.closest(".muavin-bottom-minibar")) return false;
      return norm(el.innerText || el.textContent || "").includes(target);
    });

    return found || null;
  }

  function clickTarget(el) {
    if (!el) return;
    const clickable = el.closest("button,a,[role='button'],[onclick]") || el;

    try {
      clickable.click();
      return;
    } catch (e) {}

    try {
      clickable.dispatchEvent(new MouseEvent("click", {
        bubbles: true,
        cancelable: true
      }));
    } catch (e) {}
  }

  function hideWrongTopMiniBars() {
    document.querySelectorAll(".muavin-bottom-minibar").forEach(function (el) {
      el.style.display = "none";
    });
  }

  function setupDock() {
    const container = getMapContainer();

    if (!container) {
      setTimeout(setupDock, 500);
      return;
    }

    hideWrongTopMiniBars();

    if (container.querySelector(".muavin-bottom-dock-v2")) return;

    const dock = document.createElement("div");
    dock.className = "muavin-bottom-dock-v2";
    dock.innerHTML = `
      <div class="dock-row">
        <button type="button" class="muavin-dock-main" data-dock-action="duraklar">
          <span class="dock-icon">🗺️</span>
          <span>Duraklar</span>
        </button>

        <button type="button" class="muavin-dock-main" data-dock-action="rota">
          <span class="dock-icon">〽️</span>
          <span>Rota</span>
        </button>

        <button type="button" class="muavin-dock-more" data-dock-action="more">
          <span>•••</span>
        </button>
      </div>

      <div class="dock-menu">
        <button type="button" data-dock-more="konumum">
          <span>Konumum</span>
          <small>Canlı</small>
        </button>

        <button type="button" data-dock-more="islemli">
          <span>İşlemli</span>
          <small>Durak</small>
        </button>
      </div>
    `;

    const menu = dock.querySelector(".dock-menu");

    dock.addEventListener("click", function (e) {
      const actionBtn = e.target.closest("[data-dock-action]");
      const moreBtn = e.target.closest("[data-dock-more]");

      if (actionBtn) {
        const action = actionBtn.getAttribute("data-dock-action");

        if (action === "duraklar") {
          clickTarget(findOriginal("Tüm Duraklar") || findOriginal("Duraklar"));
          menu.classList.remove("is-open");
        }

        if (action === "rota") {
          clickTarget(findOriginal("Rota"));
          menu.classList.remove("is-open");
        }

        if (action === "more") {
          menu.classList.toggle("is-open");
        }
      }

      if (moreBtn) {
        const action = moreBtn.getAttribute("data-dock-more");

        if (action === "konumum") clickTarget(findOriginal("Konumum"));
        if (action === "islemli") clickTarget(findOriginal("İşlemli"));

        menu.classList.remove("is-open");
      }
    });

    document.addEventListener("click", function (e) {
      if (!dock.contains(e.target)) {
        menu.classList.remove("is-open");
      }
    }, true);

    container.appendChild(dock);
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", setupDock);
  } else {
    setupDock();
  }

  setTimeout(setupDock, 700);
  setTimeout(setupDock, 1600);
  setTimeout(setupDock, 3000);
})();



/* MUAVIN_BOTTOM_DOCK_SMART_MORE_V3_JS */
(function () {
  if (window.MUAVIN_BOTTOM_DOCK_SMART_MORE_V3) return;
  window.MUAVIN_BOTTOM_DOCK_SMART_MORE_V3 = true;

  function norm(s) {
    return String(s || "")
      .toLocaleLowerCase("tr-TR")
      .replace(/\s+/g, " ")
      .trim();
  }

  function findOriginal(label) {
    const target = norm(label);

    const all = Array.from(document.querySelectorAll("button,a,[role='button'],[onclick],div,span"));

    let found = all.find(function (el) {
      if (el.closest(".muavin-bottom-dock-v2")) return false;
      if (el.closest(".muavin-bottom-minibar")) return false;

      const t = norm(el.innerText || el.textContent || "");
      return t.includes(target);
    });

    return found || null;
  }

  function clickTarget(el) {
    if (!el) return;

    const clickable = el.closest("button,a,[role='button'],[onclick]") || el;

    try {
      clickable.click();
      return;
    } catch (e) {}

    try {
      clickable.dispatchEvent(new MouseEvent("click", {
        bubbles: true,
        cancelable: true
      }));
    } catch (e) {}
  }

  function mainHtml() {
    return `
      <button type="button" class="muavin-smart-action muavin-smart-dark" data-smart-action="duraklar">
        <span>🗺️</span>
        <span>Duraklar</span>
      </button>

      <button type="button" class="muavin-smart-action muavin-smart-dark" data-smart-action="rota">
        <span>〽️</span>
        <span>Rota</span>
      </button>

      <button type="button" class="muavin-smart-action muavin-smart-light" data-smart-action="more">
        <span>•••</span>
      </button>
    `;
  }

  function moreHtml() {
    return `
      <button type="button" class="muavin-smart-action muavin-smart-dark" data-smart-action="konumum">
        <span>📍</span>
        <span>Konumum</span>
      </button>

      <button type="button" class="muavin-smart-action muavin-smart-dark" data-smart-action="islemli">
        <span>🎯</span>
        <span>İşlemli</span>
      </button>

      <button type="button" class="muavin-smart-action muavin-smart-close" data-smart-action="close">
        <span>×</span>
      </button>
    `;
  }

  function renderMain(dock, row) {
    dock.classList.remove("is-more-mode");
    row.innerHTML = mainHtml();
  }

  function renderMore(dock, row) {
    dock.classList.add("is-more-mode");
    row.innerHTML = moreHtml();
  }

  function setupSmartDock() {
    const dock = document.querySelector(".muavin-bottom-dock-v2");
    if (!dock) {
      setTimeout(setupSmartDock, 500);
      return;
    }

    const row = dock.querySelector(".dock-row");
    if (!row) {
      setTimeout(setupSmartDock, 500);
      return;
    }

    const oldMenu = dock.querySelector(".dock-menu");
    if (oldMenu) oldMenu.style.display = "none";

    if (dock.dataset.smartMoreReady !== "1") {
      dock.dataset.smartMoreReady = "1";

      renderMain(dock, row);

      dock.addEventListener("click", function (e) {
        const btn = e.target.closest("[data-smart-action]");
        if (!btn || !dock.contains(btn)) return;

        e.preventDefault();
        e.stopPropagation();
        if (e.stopImmediatePropagation) e.stopImmediatePropagation();

        const action = btn.getAttribute("data-smart-action");

        if (action === "duraklar") {
          clickTarget(findOriginal("Tüm Duraklar") || findOriginal("Duraklar"));
          renderMain(dock, row);
        }

        if (action === "rota") {
          clickTarget(findOriginal("Rota"));
          renderMain(dock, row);
        }

        if (action === "more") {
          renderMore(dock, row);
        }

        if (action === "konumum") {
          clickTarget(findOriginal("Konumum"));
          renderMain(dock, row);
        }

        if (action === "islemli") {
          clickTarget(findOriginal("İşlemli"));
          renderMain(dock, row);
        }

        if (action === "close") {
          renderMain(dock, row);
        }
      }, true);
    }
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", setupSmartDock);
  } else {
    setupSmartDock();
  }

  setTimeout(setupSmartDock, 800);
  setTimeout(setupSmartDock, 1800);
  setTimeout(setupSmartDock, 3200);
})();



/* MUAVIN_BOTTOM_DOCK_CLICK_FIX_V4_JS */
(function () {
  if (window.MUAVIN_BOTTOM_DOCK_CLICK_FIX_V4) return;
  window.MUAVIN_BOTTOM_DOCK_CLICK_FIX_V4 = true;

  let lastHandledAt = 0;

  function norm(s) {
    return String(s || "")
      .toLocaleLowerCase("tr-TR")
      .replace(/\s+/g, " ")
      .trim();
  }

  function getDock() {
    return document.querySelector(".muavin-bottom-dock-v2");
  }

  function safeText(el) {
    if (!el) return "";
    return norm((el.textContent || "") + " " + (el.innerText || ""));
  }

  function excluded(el) {
    return !!(
      el.closest(".muavin-bottom-dock-v2") ||
      el.closest(".muavin-bottom-minibar") ||
      el.closest(".muavin-summary-bubble") ||
      el.closest(".muavin-route-summary-card") ||
      el.closest(".muavin-tools-fab") ||
      el.closest(".muavin-tools-sheet") ||
      el.closest(".leaflet-marker-icon")
    );
  }

  function findOriginal(labels) {
    labels = Array.isArray(labels) ? labels : [labels];

    const targets = labels.map(norm);

    // Önce bizim gizlediğimiz eski butonlarda ara
    const hidden = Array.from(document.querySelectorAll(".muavin-original-bottom-action-hidden"));
    for (const el of hidden) {
      const t = safeText(el);
      if (targets.some(x => t.includes(x))) return el;
    }

    // Sonra genel DOM içinde ara
    const all = Array.from(document.querySelectorAll("button,a,[role='button'],[onclick],div,span"));
    const candidates = all.filter(function (el) {
      if (excluded(el)) return false;
      const t = safeText(el);
      return targets.some(x => t.includes(x));
    });

    candidates.sort(function (a, b) {
      const ar = a.getBoundingClientRect();
      const br = b.getBoundingClientRect();
      return (ar.width * ar.height) - (br.width * br.height);
    });

    return candidates[0] || null;
  }

  function dispatchClick(el) {
    if (!el) return false;

    const possible = [];

    if (el.matches && el.matches("button,a,[role='button'],[onclick]")) possible.push(el);

    el.querySelectorAll &&
      el.querySelectorAll("button,a,[role='button'],[onclick]").forEach(x => possible.push(x));

    const closest = el.closest && el.closest("button,a,[role='button'],[onclick]");
    if (closest) possible.push(closest);

    possible.push(el);

    const unique = [...new Set(possible)].filter(Boolean);

    for (const target of unique) {
      try {
        target.dispatchEvent(new MouseEvent("mousedown", { bubbles: true, cancelable: true }));
        target.dispatchEvent(new MouseEvent("mouseup", { bubbles: true, cancelable: true }));
        target.dispatchEvent(new MouseEvent("click", { bubbles: true, cancelable: true }));
        return true;
      } catch (e) {}

      try {
        target.click();
        return true;
      } catch (e) {}
    }

    return false;
  }

  function activateOriginal(el) {
    if (!el) return;

    const oldClass = el.className;
    const oldStyle = el.getAttribute("style") || "";

    // Gizli butonu çok kısa süre offscreen görünür yapıp tıklıyoruz
    try {
      el.classList.remove("muavin-original-bottom-action-hidden");
      el.setAttribute(
        "style",
        oldStyle + ";position:fixed!important;left:-9999px!important;top:-9999px!important;opacity:0!important;pointer-events:auto!important;display:block!important;"
      );
    } catch (e) {}

    setTimeout(function () {
      dispatchClick(el);

      setTimeout(function () {
        try {
          el.className = oldClass;
          if (oldStyle) el.setAttribute("style", oldStyle);
          else el.removeAttribute("style");
        } catch (e) {}
      }, 80);
    }, 20);
  }

  function mainHtml() {
    return `
      <button type="button" class="muavin-smart-action muavin-smart-dark" data-smart-action="duraklar">
        <span>🗺️</span>
        <span>Duraklar</span>
      </button>

      <button type="button" class="muavin-smart-action muavin-smart-dark" data-smart-action="rota">
        <span>〽️</span>
        <span>Rota</span>
      </button>

      <button type="button" class="muavin-smart-action muavin-smart-light" data-smart-action="more">
        <span>•••</span>
      </button>
    `;
  }

  function moreHtml() {
    return `
      <button type="button" class="muavin-smart-action muavin-smart-dark" data-smart-action="konumum">
        <span>📍</span>
        <span>Konumum</span>
      </button>

      <button type="button" class="muavin-smart-action muavin-smart-dark" data-smart-action="islemli">
        <span>🎯</span>
        <span>İşlemli</span>
      </button>

      <button type="button" class="muavin-smart-action muavin-smart-close" data-smart-action="close">
        <span>×</span>
      </button>
    `;
  }

  function renderMain() {
    const dock = getDock();
    const row = dock && dock.querySelector(".dock-row");
    if (!dock || !row) return;

    dock.classList.remove("is-more-mode");
    row.innerHTML = mainHtml();
  }

  function renderMore() {
    const dock = getDock();
    const row = dock && dock.querySelector(".dock-row");
    if (!dock || !row) return;

    dock.classList.add("is-more-mode");
    row.innerHTML = moreHtml();
  }

  function runAction(action) {
    if (action === "more") {
      renderMore();
      return;
    }

    if (action === "close") {
      renderMain();
      return;
    }

    if (action === "duraklar") {
      activateOriginal(findOriginal(["Tüm Duraklar", "Duraklar"]));
      renderMain();
      return;
    }

    if (action === "rota") {
      activateOriginal(findOriginal("Rota"));
      renderMain();
      return;
    }

    if (action === "konumum") {
      activateOriginal(findOriginal("Konumum"));
      renderMain();
      return;
    }

    if (action === "islemli") {
      activateOriginal(findOriginal("İşlemli"));
      renderMain();
      return;
    }
  }

  function handleDockEvent(e) {
    const dock = getDock();
    if (!dock || !dock.contains(e.target)) return;

    const btn = e.target.closest("[data-smart-action],[data-dock-action],[data-dock-more]");
    if (!btn || !dock.contains(btn)) return;

    const now = Date.now();

    // touchend + click çift çalışmasın
    if (now - lastHandledAt < 280) {
      e.preventDefault();
      e.stopPropagation();
      if (e.stopImmediatePropagation) e.stopImmediatePropagation();
      return;
    }

    lastHandledAt = now;

    e.preventDefault();
    e.stopPropagation();
    if (e.stopImmediatePropagation) e.stopImmediatePropagation();

    const action =
      btn.getAttribute("data-smart-action") ||
      btn.getAttribute("data-dock-action") ||
      btn.getAttribute("data-dock-more");

    runAction(action);
  }

  function setup() {
    const dock = getDock();

    if (!dock) {
      setTimeout(setup, 500);
      return;
    }

    if (dock.dataset.clickFixV4 === "1") return;
    dock.dataset.clickFixV4 = "1";

    // Leaflet harita dokunmayı yutmasın
    try {
      if (window.L && L.DomEvent) {
        L.DomEvent.disableClickPropagation(dock);
        L.DomEvent.disableScrollPropagation(dock);
      }
    } catch (e) {}

    dock.addEventListener("touchend", handleDockEvent, { capture: true, passive: false });
    dock.addEventListener("pointerup", handleDockEvent, true);
    dock.addEventListener("click", handleDockEvent, true);

    // Başlangıçta ana mod düzgün olsun
    renderMain();
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", setup);
  } else {
    setup();
  }

  setTimeout(setup, 800);
  setTimeout(setup, 1800);
  setTimeout(setup, 3200);
})();

