# Muavin Asistanı Route / Hat Seçimi Audit V13

- Tarih: `20260608-171859`
- Bu rapor sadece tespittir. Dosya değiştirmez.

## 1) Dosya Durumu

| Dosya | Var mı | Satır | Hash |
| --- | --- | ---: | --- |
| WEB index | VAR | 2002 | e35932eeab6b |
| ANDROID index | VAR | 1778 | 25f6b94cbb7b |
| WEB app.py | VAR | 4512 | 7d03ec46f6c0 |
| ANDROID app.py | VAR | 4507 | cf451e1df53e |

## 2) WEB ↔ ANDROID index.html Farkı
- WEB hash: `e35932eeab6b`
- ANDROID hash: `25f6b94cbb7b`
- Durum: **FARKLI**

## 3) WEB index.html Hat/Route/Kilit İzleri

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 70 | `lock` | `      display:block;` |
| 75 | `hidden` | `      overflow:hidden;` |
| 89 | `lock` | `      display:block;` |
| 95 | `hidden` | `      overflow:hidden;` |
| 154 | `lock` | `    .lock-btn{` |
| 173 | `lock` | `    .lock-btn:active{` |
| 267 | `hidden` | `  overflow-x:hidden;` |
| 274 | `pointer-events` | `  pointer-events:none;` |
| 348 | `hidden` | `  overflow:hidden !important;` |
| 369 | `lock` | `  display:block !important;` |
| 374 | `hidden` | `  overflow:hidden !important;` |
| 389 | `pointer-events` | `  pointer-events:none;` |
| 420 | `lock` | `  display:block !important;` |
| 425 | `lock` | `.active-trip-locked::after{` |
| 437 | `hidden` | `  overflow:hidden !important;` |
| 504 | `kilit` | `/* Ayarlar / kilitle butonları da dark uyumlu */` |
| 506 | `lock` | `.lock-btn{` |
| 527 | `lock` | `.lock-form{` |
| 744 | `lock` | `.lock-btn{` |
| 751 | `lock` | `.active-trip-locked::after{` |
| 852 | `lock` | `.active-trip-locked::after{` |
| 895 | `lock` | `.lock-btn{` |
| 1031 | `route-sheet-no-flash-fix` | `<style id="route-sheet-no-flash-fix">` |
| 1033 | `routeSheet` | `  #routeSheet[hidden],` |
| 1034 | `routeSheet` | `  #routeSheetBackdrop[hidden]{` |
| 1038 | `routeSheet` | `  #routeSheet:not(.show),` |
| 1039 | `routeSheet` | `  #routeSheetBackdrop:not(.show){` |
| 1050 | `active_trip` | `    {% set current_route = selected_route if selected_route is defined and selected_route else (active_trip.route if active_trip is defined and active_trip else 'Denizli – İstanbul') %}` |
| 1052 | `active_trip` | `    {% set current_route = selected_route if selected_route is defined and selected_route else (active_trip.route if active_trip is defined and active_trip else 'Denizli – İstanbul') %}` |
| 1055 | `routePicker` | `      <button class="route-picker-premium" id="routePickerBtn" type="button">` |
| 1057 | `routePicker` | `        <span class="route-name" id="routePickerText">{{ current_route }}</span>` |
| 1061 | `routeSelect` | `      <select id="homeRouteSelect" name="route" hidden>` |
| 1072 | `routeSheet` | `    <div class="route-sheet-backdrop" id="routeSheetBackdrop" hidden aria-hidden="true"></div>` |
| 1074 | `routeSheet` | `    <section class="route-sheet" id="routeSheet" hidden aria-hidden="true">` |
| 1082 | `routeSheet` | `        <button class="route-sheet-close" id="routeSheetClose" type="button">×</button>` |
| 1114 | `continue` | `    <a class="hero-link" href="{{ url_for('continue_trip') }}" aria-label="Devam Eden Sefer">` |
| 1115 | `devam` | `      <img src="{{ url_for('static', filename='img/seat-card-final.png', v='final1') }}" alt="Devam Eden Sefer">` |
| 1201 | `lock` | `    <form class="lock-form" method="post" action="{{ url_for('logout') }}">` |
| 1203 | `hidden` | `        <input type="hidden" name="csrf_token" value="{{ csrf_token }}">` |
| 1205 | `lock` | `      <button class="lock-btn" type="submit">🔒 KİLİTLE</button>` |
| 1210 | `home-route-lock-fix` | `<style id="home-route-lock-fix">` |
| 1231 | `routeSelect` | `#homeRouteSelect{` |
| 1248 | `pointer-events` | `  pointer-events:none;` |
| 1251 | `lock` | `.lock-form{` |
| 1256 | `lock` | `.lock-form .lock-btn{` |
| 1261 | `home-route-link-fix` | `<script id="home-route-link-fix">` |
| 1263 | `routeSelect` | `  const routeSelect = document.getElementById("homeRouteSelect");` |
| 1267 | `routeSelect` | `    if(!routeSelect \|\| !startLink) return;` |
| 1269 | `routeSelect` | `    const route = routeSelect.value \|\| "";` |
| 1270 | `sefer-baslat` | `    const base = startLink.dataset.base \|\| startLink.getAttribute("href") \|\| "/sefer-baslat";` |
| 1279 | `routeSelect` | `  if(routeSelect){` |
| 1283 | `routeSelect` | `        const opt = Array.from(routeSelect.options).find(o => o.value === saved);` |
| 1284 | `routeSelect` | `        if(opt) routeSelect.value = saved;` |
| 1288 | `routeSelect` | `    routeSelect.addEventListener("change", syncStartLink);` |
| 1342 | `hidden` | `  overflow:hidden;` |
| 1369 | `lock` | `  display:block;` |
| 1380 | `hidden` | `  overflow:hidden;` |
| 1479 | `lock` | `  display:block;` |
| 1487 | `lock` | `  display:block;` |
| 1547 | `routePicker` | `  const btn = document.getElementById("routePickerBtn");` |
| 1548 | `routePicker` | `  const text = document.getElementById("routePickerText");` |
| 1549 | `routeSelect` | `  const select = document.getElementById("homeRouteSelect");` |
| 1550 | `routeSheet` | `  const sheet = document.getElementById("routeSheet");` |
| 1551 | `routeSheet` | `  const backdrop = document.getElementById("routeSheetBackdrop");` |
| 1552 | `routeSheet` | `  const closeBtn = document.getElementById("routeSheetClose");` |
| 1560 | `hidden` | `    sheet.setAttribute("aria-hidden", "false");` |
| 1566 | `hidden` | `    sheet.setAttribute("aria-hidden", "true");` |
| 1571 | `sefer-baslat` | `    const base = startLink.dataset.base \|\| startLink.getAttribute("href") \|\| "/sefer-baslat";` |
| 1622 | `lock` | `.active-trip-locked{` |
| 1626 | `lock` | `.active-trip-locked::after{` |
| 1644 | `lock` | `.active-trip-locked img{` |
| 1659 | `lock` | `  display:block;` |
| 1682 | `lock` | `  display:block;` |
| 1683 | `tripGuard` | `  animation:tripGuardIn .16s ease forwards;` |
| 1686 | `tripGuard` | `@keyframes tripGuardIn{` |
| 1764 | `active_trip` | `  const HAS_ACTIVE_TRIP = {% if active_trip is defined and active_trip %}true{% else %}false{% endif %};` |
| 1765 | `active_trip` | `  const ACTIVE_TRIP_ROUTE = {% if active_trip is defined and active_trip %}{{ active_trip.route\|tojson }}{% else %}""{% endif %};` |
| 1767 | `active_trip` | `  if(!HAS_ACTIVE_TRIP) return;` |
| 1773 | `continue` | `  const continueLink =` |
| 1775 | `continue` | `    document.querySelector('a[href*="continue"]') \|\|` |
| 1778 | `routePicker` | `  const routeBtn = document.getElementById("routePickerBtn");` |
| 1779 | `routePicker` | `  const routeText = document.getElementById("routePickerText");` |
| 1780 | `routeSelect` | `  const routeSelect = document.getElementById("homeRouteSelect");` |
| 1783 | `active_trip` | `  if(ACTIVE_TRIP_ROUTE){` |
| 1784 | `active_trip` | `    if(routeText) routeText.textContent = ACTIVE_TRIP_ROUTE;` |
| 1785 | `routeSelect` | `    if(routeSelect){` |
| 1786 | `routeSelect` | `      const opt = Array.from(routeSelect.options).find(o => o.value === ACTIVE_TRIP_ROUTE);` |
| 1787 | `routeSelect` | `      if(opt) routeSelect.value = ACTIVE_TRIP_ROUTE;` |
| 1790 | `active_trip` | `      localStorage.setItem("homeSelectedRoute", ACTIVE_TRIP_ROUTE);` |
| 1795 | `lock` | `    startLink.classList.add("active-trip-locked");` |
| 1796 | `disabled` | `    startLink.setAttribute("aria-disabled", "true");` |
| 1800 | `tripGuard` | `    let backdrop = document.getElementById("tripGuardBackdrop");` |
| 1801 | `tripGuard` | `    let modal = document.getElementById("tripGuardModal");` |
| 1806 | `tripGuard` | `    backdrop.id = "tripGuardBackdrop";` |
| 1810 | `tripGuard` | `    modal.id = "tripGuardModal";` |
| 1815 | `devam` | `      <p>Yeni sefer başlatmadan önce mevcut seferi devam ettirmen veya seferi sonlandırman gerekir.</p>` |
| 1817 | `tripGuard` | `        <a class="trip-guard-go" id="tripGuardGo" href="#">Devam eden sefere git</a>` |
| 1818 | `tripGuard` | `        <button class="trip-guard-ok" id="tripGuardOk" type="button">Tamam</button>` |
| 1831 | `tripGuard` | `    modal.querySelector("#tripGuardOk").addEventListener("click", close);` |
| 1833 | `tripGuard` | `    const go = modal.querySelector("#tripGuardGo");` |
| 1834 | `continue` | `    if(go && continueLink){` |
| 1835 | `continue` | `      go.href = continueLink.getAttribute("href") \|\| "/seats";` |
| 1850 | `preventDefault` | `      e.preventDefault();` |
| 1851 | `stopPropagation` | `      e.stopPropagation();` |
| 1852 | `stopImmediatePropagation` | `      e.stopImmediatePropagation();` |
| 1861 | `preventDefault` | `      e.preventDefault();` |
| 1862 | `stopPropagation` | `      e.stopPropagation();` |
| 1863 | `stopImmediatePropagation` | `      e.stopImmediatePropagation();` |
| 1873 | `lock` | `<!-- ACTIVE_ROUTE_LOCK_FINAL_START -->` |
| 1874 | `active-route-lock` | `<script id="active-route-lock-final">` |
| 1876 | `active_trip` | `  const HAS_ACTIVE_TRIP = {% if active_trip is defined and active_trip %}true{% else %}false{% endif %};` |
| 1877 | `active_trip` | `  const ACTIVE_TRIP_ROUTE = {% if active_trip is defined and active_trip %}{{ active_trip.route\|tojson }}{% else %}""{% endif %};` |
| 1879 | `active_trip` | `  if(!HAS_ACTIVE_TRIP) return;` |
| 1881 | `routePicker` | `  const routeBtn = document.getElementById("routePickerBtn");` |
| 1882 | `routePicker` | `  const routeText = document.getElementById("routePickerText");` |
| 1883 | `routeSelect` | `  const routeSelect = document.getElementById("homeRouteSelect");` |
| 1886 | `continue` | `  const continueLink =` |
| 1888 | `continue` | `    document.querySelector('a[href*="continue"]') \|\|` |
| 1891 | `routeSheet` | `  const sheet = document.getElementById("routeSheet");` |
| 1892 | `routeSheet` | `  const backdrop = document.getElementById("routeSheetBackdrop");` |
| 1894 | `routeSheet` | `  function hardCloseRouteSheet(){` |
| 1897 | `hidden` | `      sheet.hidden = true;` |
| 1898 | `hidden` | `      sheet.setAttribute("aria-hidden", "true");` |
| 1902 | `hidden` | `      backdrop.hidden = true;` |
| 1903 | `hidden` | `      backdrop.setAttribute("aria-hidden", "true");` |
| 1908 | `active_trip` | `    if(!ACTIVE_TRIP_ROUTE) return;` |
| 1910 | `active_trip` | `    if(routeText) routeText.textContent = ACTIVE_TRIP_ROUTE;` |
| 1912 | `routeSelect` | `    if(routeSelect){` |
| 1913 | `routeSelect` | `      const opt = Array.from(routeSelect.options \|\| []).find(o => o.value === ACTIVE_TRIP_ROUTE);` |
| 1914 | `routeSelect` | `      if(opt) routeSelect.value = ACTIVE_TRIP_ROUTE;` |
| 1918 | `active_trip` | `      localStorage.setItem("homeSelectedRoute", ACTIVE_TRIP_ROUTE);` |
| 1923 | `tripGuard` | `    let bd = document.getElementById("tripGuardBackdrop");` |
| 1924 | `tripGuard` | `    let modal = document.getElementById("tripGuardModal");` |
| 1929 | `tripGuard` | `    bd.id = "tripGuardBackdrop";` |
| 1933 | `tripGuard` | `    modal.id = "tripGuardModal";` |
| 1938 | `devam` | `      <p>Yeni sefer başlatmadan önce mevcut seferi devam ettirmen veya seferi sonlandırman gerekir.</p>` |
| 1940 | `tripGuard` | `        <a class="trip-guard-go" id="tripGuardGo" href="#">Devam eden sefere git</a>` |
| 1941 | `tripGuard` | `        <button class="trip-guard-ok" id="tripGuardOk" type="button">Tamam</button>` |
| 1954 | `tripGuard` | `    modal.querySelector("#tripGuardOk")?.addEventListener("click", close);` |
| 1956 | `tripGuard` | `    const go = modal.querySelector("#tripGuardGo");` |
| 1957 | `continue` | `    if(go && continueLink){` |
| 1958 | `continue` | `      go.href = continueLink.getAttribute("href") \|\| "/continue-trip";` |
| 1965 | `routeSheet` | `    hardCloseRouteSheet();` |
| 1974 | `routeSheet` | `  hardCloseRouteSheet();` |
| 1977 | `lock` | `    startLink.classList.add("active-trip-locked");` |
| 1978 | `disabled` | `    startLink.setAttribute("aria-disabled", "true");` |
| 1982 | `kilit` | `    En son kilit:` |
| 1987 | `routePicker` | `    const hitRoute = e.target.closest && e.target.closest("#routePickerBtn");` |
| 1990 | `preventDefault` | `      e.preventDefault();` |
| 1991 | `stopPropagation` | `      e.stopPropagation();` |
| 1992 | `stopImmediatePropagation` | `      e.stopImmediatePropagation();` |
| 1999 | `lock` | `<!-- ACTIVE_ROUTE_LOCK_FINAL_END -->` |

## 4) ANDROID index.html Hat/Route/Kilit İzleri

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 70 | `lock` | `      display:block;` |
| 75 | `hidden` | `      overflow:hidden;` |
| 89 | `lock` | `      display:block;` |
| 95 | `hidden` | `      overflow:hidden;` |
| 154 | `lock` | `    .lock-btn{` |
| 173 | `lock` | `    .lock-btn:active{` |
| 267 | `hidden` | `  overflow-x:hidden;` |
| 274 | `pointer-events` | `  pointer-events:none;` |
| 348 | `hidden` | `  overflow:hidden !important;` |
| 369 | `lock` | `  display:block !important;` |
| 374 | `hidden` | `  overflow:hidden !important;` |
| 389 | `pointer-events` | `  pointer-events:none;` |
| 420 | `lock` | `  display:block !important;` |
| 425 | `lock` | `.active-trip-locked::after{` |
| 437 | `hidden` | `  overflow:hidden !important;` |
| 504 | `kilit` | `/* Ayarlar / kilitle butonları da dark uyumlu */` |
| 506 | `lock` | `.lock-btn{` |
| 527 | `lock` | `.lock-form{` |
| 744 | `lock` | `.lock-btn{` |
| 751 | `lock` | `.active-trip-locked::after{` |
| 852 | `lock` | `.active-trip-locked::after{` |
| 895 | `lock` | `.lock-btn{` |
| 956 | `active_trip` | `    {% set current_route = selected_route if selected_route is defined and selected_route else (active_trip.route if active_trip is defined and active_trip else 'Denizli – İstanbul') %}` |
| 958 | `active_trip` | `    {% set current_route = selected_route if selected_route is defined and selected_route else (active_trip.route if active_trip is defined and active_trip else 'Denizli – İstanbul') %}` |
| 961 | `routePicker` | `      <button class="route-picker-premium" id="routePickerBtn" type="button">` |
| 963 | `routePicker` | `        <span class="route-name" id="routePickerText">{{ current_route }}</span>` |
| 967 | `routeSelect` | `      <select id="homeRouteSelect" name="route" hidden>` |
| 978 | `routeSheet` | `    <div class="route-sheet-backdrop" id="routeSheetBackdrop"></div>` |
| 980 | `routeSheet` | `    <section class="route-sheet" id="routeSheet" aria-hidden="true">` |
| 988 | `routeSheet` | `        <button class="route-sheet-close" id="routeSheetClose" type="button">×</button>` |
| 1020 | `continue` | `    <a class="hero-link" href="{{ url_for('continue_trip') }}" aria-label="Devam Eden Sefer">` |
| 1021 | `devam` | `      <img src="{{ url_for('static', filename='img/seat-card-final.png', v='final1') }}" alt="Devam Eden Sefer">` |
| 1107 | `lock` | `    <form class="lock-form" method="post" action="{{ url_for('logout') }}">` |
| 1109 | `hidden` | `        <input type="hidden" name="csrf_token" value="{{ csrf_token }}">` |
| 1111 | `lock` | `      <button class="lock-btn" type="submit">🔒 KİLİTLE</button>` |
| 1116 | `home-route-lock-fix` | `<style id="home-route-lock-fix">` |
| 1137 | `routeSelect` | `#homeRouteSelect{` |
| 1154 | `pointer-events` | `  pointer-events:none;` |
| 1157 | `lock` | `.lock-form{` |
| 1162 | `lock` | `.lock-form .lock-btn{` |
| 1167 | `home-route-link-fix` | `<script id="home-route-link-fix">` |
| 1169 | `routeSelect` | `  const routeSelect = document.getElementById("homeRouteSelect");` |
| 1173 | `routeSelect` | `    if(!routeSelect \|\| !startLink) return;` |
| 1175 | `routeSelect` | `    const route = routeSelect.value \|\| "";` |
| 1176 | `sefer-baslat` | `    const base = startLink.dataset.base \|\| startLink.getAttribute("href") \|\| "/sefer-baslat";` |
| 1185 | `routeSelect` | `  if(routeSelect){` |
| 1189 | `routeSelect` | `        const opt = Array.from(routeSelect.options).find(o => o.value === saved);` |
| 1190 | `routeSelect` | `        if(opt) routeSelect.value = saved;` |
| 1194 | `routeSelect` | `    routeSelect.addEventListener("change", syncStartLink);` |
| 1248 | `hidden` | `  overflow:hidden;` |
| 1275 | `lock` | `  display:block;` |
| 1286 | `hidden` | `  overflow:hidden;` |
| 1385 | `lock` | `  display:block;` |
| 1393 | `lock` | `  display:block;` |
| 1453 | `routePicker` | `  const btn = document.getElementById("routePickerBtn");` |
| 1454 | `routePicker` | `  const text = document.getElementById("routePickerText");` |
| 1455 | `routeSelect` | `  const select = document.getElementById("homeRouteSelect");` |
| 1456 | `routeSheet` | `  const sheet = document.getElementById("routeSheet");` |
| 1457 | `routeSheet` | `  const backdrop = document.getElementById("routeSheetBackdrop");` |
| 1458 | `routeSheet` | `  const closeBtn = document.getElementById("routeSheetClose");` |
| 1466 | `hidden` | `    sheet.setAttribute("aria-hidden", "false");` |
| 1472 | `hidden` | `    sheet.setAttribute("aria-hidden", "true");` |
| 1477 | `sefer-baslat` | `    const base = startLink.dataset.base \|\| startLink.getAttribute("href") \|\| "/sefer-baslat";` |
| 1528 | `lock` | `.active-trip-locked{` |
| 1532 | `lock` | `.active-trip-locked::after{` |
| 1550 | `lock` | `.active-trip-locked img{` |
| 1565 | `lock` | `  display:block;` |
| 1588 | `lock` | `  display:block;` |
| 1589 | `tripGuard` | `  animation:tripGuardIn .16s ease forwards;` |
| 1592 | `tripGuard` | `@keyframes tripGuardIn{` |
| 1670 | `active_trip` | `  const HAS_ACTIVE_TRIP = {% if active_trip is defined and active_trip %}true{% else %}false{% endif %};` |
| 1671 | `active_trip` | `  const ACTIVE_TRIP_ROUTE = {% if active_trip is defined and active_trip %}{{ active_trip.route\|tojson }}{% else %}""{% endif %};` |
| 1673 | `active_trip` | `  if(!HAS_ACTIVE_TRIP) return;` |
| 1679 | `continue` | `  const continueLink =` |
| 1681 | `continue` | `    document.querySelector('a[href*="continue"]') \|\|` |
| 1684 | `routePicker` | `  const routeBtn = document.getElementById("routePickerBtn");` |
| 1685 | `routePicker` | `  const routeText = document.getElementById("routePickerText");` |
| 1686 | `routeSelect` | `  const routeSelect = document.getElementById("homeRouteSelect");` |
| 1689 | `active_trip` | `  if(ACTIVE_TRIP_ROUTE){` |
| 1690 | `active_trip` | `    if(routeText) routeText.textContent = ACTIVE_TRIP_ROUTE;` |
| 1691 | `routeSelect` | `    if(routeSelect){` |
| 1692 | `routeSelect` | `      const opt = Array.from(routeSelect.options).find(o => o.value === ACTIVE_TRIP_ROUTE);` |
| 1693 | `routeSelect` | `      if(opt) routeSelect.value = ACTIVE_TRIP_ROUTE;` |
| 1696 | `active_trip` | `      localStorage.setItem("homeSelectedRoute", ACTIVE_TRIP_ROUTE);` |
| 1701 | `lock` | `    startLink.classList.add("active-trip-locked");` |
| 1702 | `disabled` | `    startLink.setAttribute("aria-disabled", "true");` |
| 1706 | `tripGuard` | `    let backdrop = document.getElementById("tripGuardBackdrop");` |
| 1707 | `tripGuard` | `    let modal = document.getElementById("tripGuardModal");` |
| 1712 | `tripGuard` | `    backdrop.id = "tripGuardBackdrop";` |
| 1716 | `tripGuard` | `    modal.id = "tripGuardModal";` |
| 1721 | `devam` | `      <p>Yeni sefer başlatmadan önce mevcut seferi devam ettirmen veya seferi sonlandırman gerekir.</p>` |
| 1723 | `tripGuard` | `        <a class="trip-guard-go" id="tripGuardGo" href="#">Devam eden sefere git</a>` |
| 1724 | `tripGuard` | `        <button class="trip-guard-ok" id="tripGuardOk" type="button">Tamam</button>` |
| 1737 | `tripGuard` | `    modal.querySelector("#tripGuardOk").addEventListener("click", close);` |
| 1739 | `tripGuard` | `    const go = modal.querySelector("#tripGuardGo");` |
| 1740 | `continue` | `    if(go && continueLink){` |
| 1741 | `continue` | `      go.href = continueLink.getAttribute("href") \|\| "/seats";` |
| 1756 | `preventDefault` | `      e.preventDefault();` |
| 1757 | `stopPropagation` | `      e.stopPropagation();` |
| 1758 | `stopImmediatePropagation` | `      e.stopImmediatePropagation();` |
| 1767 | `preventDefault` | `      e.preventDefault();` |
| 1768 | `stopPropagation` | `      e.stopPropagation();` |
| 1769 | `stopImmediatePropagation` | `      e.stopImmediatePropagation();` |

## 5) WEB routeSheet bölgesi

| Satır | İçerik |
| ---: | --- |
| 1018 | `  .quick-desc,` |
| 1019 | `  .card-desc,` |
| 1020 | `  .tile-desc,` |
| 1021 | `  .status-desc,` |
| 1022 | `  .small,` |
| 1023 | `  .label,` |
| 1024 | `  .meta,` |
| 1025 | `  .hint{` |
| 1026 | `    font-family:var(--font-body) !important;` |
| 1027 | `  }` |
| 1028 | `</style>` |
| 1029 | `` |
| 1030 | `` |
| 1031 | `<style id="route-sheet-no-flash-fix">` |
| 1032 | `  /* Route picker ilk render parlamasını engeller */` |
| 1033 | `  #routeSheet[hidden],` |
| 1034 | `  #routeSheetBackdrop[hidden]{` |
| 1035 | `    display:none !important;` |
| 1036 | `  }` |
| 1037 | `` |
| 1038 | `  #routeSheet:not(.show),` |
| 1039 | `  #routeSheetBackdrop:not(.show){` |
| 1040 | `    display:none !important;` |
| 1041 | `  }` |
| 1042 | `</style>` |
| 1043 | `` |
| 1044 | `` |
| 1045 | `</head>` |
| 1046 | `` |
| 1047 | `<body>` |
| 1048 | `  <main class="home-shell">` |
| 1049 | `` |
| 1050 | `    {% set current_route = selected_route if selected_route is defined and selected_route else (active_trip.route if active_trip is defined and active_trip else 'Denizli – İstanbul') %}` |
| 1051 | `` |
| 1052 | `    {% set current_route = selected_route if selected_route is defined and selected_route else (active_trip.route if active_trip is defined and active_trip else 'Denizli – İstanbul') %}` |
| 1053 | `` |
| 1054 | `    <div class="route-form route-premium">` |
| 1055 | `      <button class="route-picker-premium" id="routePickerBtn" type="button">` |
| 1056 | `        <span class="route-pin">📍</span>` |
| 1057 | `        <span class="route-name" id="routePickerText">{{ current_route }}</span>` |
| 1058 | `        <span class="route-caret">⌄</span>` |
| 1059 | `      </button>` |
| 1060 | `` |
| 1061 | `      <select id="homeRouteSelect" name="route" hidden>` |
| 1062 | `        {% if all_routes is defined and all_routes %}` |
| 1063 | `          {% for r in all_routes %}` |
| 1064 | `            <option value="{{ r }}" {% if r == current_route %}selected{% endif %}>{{ r }}</option>` |
| 1065 | `          {% endfor %}` |
| 1066 | `        {% else %}` |
| 1067 | `          <option value="{{ current_route }}">{{ current_route }}</option>` |
| 1068 | `        {% endif %}` |

## 5) WEB routePicker bölgesi

| Satır | İçerik |
| ---: | --- |
| 1040 | `    display:none !important;` |
| 1041 | `  }` |
| 1042 | `</style>` |
| 1043 | `` |
| 1044 | `` |
| 1045 | `</head>` |
| 1046 | `` |
| 1047 | `<body>` |
| 1048 | `  <main class="home-shell">` |
| 1049 | `` |
| 1050 | `    {% set current_route = selected_route if selected_route is defined and selected_route else (active_trip.route if active_trip is defined and active_trip else 'Denizli – İstanbul') %}` |
| 1051 | `` |
| 1052 | `    {% set current_route = selected_route if selected_route is defined and selected_route else (active_trip.route if active_trip is defined and active_trip else 'Denizli – İstanbul') %}` |
| 1053 | `` |
| 1054 | `    <div class="route-form route-premium">` |
| 1055 | `      <button class="route-picker-premium" id="routePickerBtn" type="button">` |
| 1056 | `        <span class="route-pin">📍</span>` |
| 1057 | `        <span class="route-name" id="routePickerText">{{ current_route }}</span>` |
| 1058 | `        <span class="route-caret">⌄</span>` |
| 1059 | `      </button>` |
| 1060 | `` |
| 1061 | `      <select id="homeRouteSelect" name="route" hidden>` |
| 1062 | `        {% if all_routes is defined and all_routes %}` |
| 1063 | `          {% for r in all_routes %}` |
| 1064 | `            <option value="{{ r }}" {% if r == current_route %}selected{% endif %}>{{ r }}</option>` |
| 1065 | `          {% endfor %}` |
| 1066 | `        {% else %}` |
| 1067 | `          <option value="{{ current_route }}">{{ current_route }}</option>` |
| 1068 | `        {% endif %}` |
| 1069 | `      </select>` |
| 1070 | `    </div>` |
| 1071 | `` |
| 1072 | `    <div class="route-sheet-backdrop" id="routeSheetBackdrop" hidden aria-hidden="true"></div>` |
| 1073 | `` |
| 1074 | `    <section class="route-sheet" id="routeSheet" hidden aria-hidden="true">` |
| 1075 | `      <div class="route-sheet-handle"></div>` |
| 1076 | `` |
| 1077 | `      <div class="route-sheet-head">` |
| 1078 | `        <div>` |
| 1079 | `          <div class="route-sheet-kicker">Aktif hat seçimi</div>` |
| 1080 | `          <h2>Güzergâh Seç</h2>` |
| 1081 | `        </div>` |
| 1082 | `        <button class="route-sheet-close" id="routeSheetClose" type="button">×</button>` |
| 1083 | `      </div>` |
| 1084 | `` |
| 1085 | `      <div class="route-sheet-list">` |
| 1086 | `        {% if all_routes is defined and all_routes %}` |
| 1087 | `          {% for r in all_routes %}` |
| 1088 | `            <button class="route-option {% if r == current_route %}active{% endif %}" type="button" data-route="{{ r }}">` |
| 1089 | `              <span class="route-option-icon">🚌</span>` |
| 1090 | `              <span class="route-option-text">` |

## 5) WEB tripGuard bölgesi

| Satır | İçerik |
| ---: | --- |
| 1668 | `  width:min(90vw,520px);` |
| 1669 | `  display:none;` |
| 1670 | `  border-radius:30px;` |
| 1671 | `  background:` |
| 1672 | `    radial-gradient(circle at 20% 0%, rgba(59,130,246,.18), transparent 34%),` |
| 1673 | `    linear-gradient(180deg,#ffffff,#f1f8ff);` |
| 1674 | `  border:1px solid rgba(255,255,255,.86);` |
| 1675 | `  box-shadow:0 30px 90px rgba(2,6,23,.36);` |
| 1676 | `  padding:22px;` |
| 1677 | `  color:#0f172a;` |
| 1678 | `  font-family:system-ui,-apple-system,"Segoe UI",Roboto,Arial,sans-serif;` |
| 1679 | `}` |
| 1680 | `` |
| 1681 | `.trip-guard-modal.show{` |
| 1682 | `  display:block;` |
| 1683 | `  animation:tripGuardIn .16s ease forwards;` |
| 1684 | `}` |
| 1685 | `` |
| 1686 | `@keyframes tripGuardIn{` |
| 1687 | `  to{ transform:translate(-50%, -50%) scale(1); }` |
| 1688 | `}` |
| 1689 | `` |
| 1690 | `.trip-guard-icon{` |
| 1691 | `  width:62px;` |
| 1692 | `  height:62px;` |
| 1693 | `  display:grid;` |
| 1694 | `  place-items:center;` |
| 1695 | `  border-radius:22px;` |
| 1696 | `  background:linear-gradient(145deg,#fef3c7,#f59e0b);` |
| 1697 | `  font-size:31px;` |
| 1698 | `  margin-bottom:14px;` |
| 1699 | `  box-shadow:0 14px 28px rgba(245,158,11,.20);` |
| 1700 | `}` |
| 1701 | `` |
| 1702 | `.trip-guard-modal h2{` |
| 1703 | `  margin:0 0 8px;` |
| 1704 | `  font-size:27px;` |
| 1705 | `  line-height:1.05;` |
| 1706 | `  font-weight:950;` |
| 1707 | `  color:#0f172a;` |
| 1708 | `}` |
| 1709 | `` |
| 1710 | `.trip-guard-modal p{` |
| 1711 | `  margin:0;` |
| 1712 | `  color:#64748b;` |
| 1713 | `  font-size:16px;` |
| 1714 | `  line-height:1.35;` |
| 1715 | `  font-weight:650;` |
| 1716 | `}` |
| 1717 | `` |
| 1718 | `.trip-guard-actions{` |

## 5) WEB home-route-lock-fix bölgesi

| Satır | İçerik |
| ---: | --- |
| 1195 | `` |
| 1196 | `    ` |
| 1197 | `    <a class="settings-btn" href="/ayarlar">` |
| 1198 | `      ⚙️ AYARLAR` |
| 1199 | `    </a>` |
| 1200 | `` |
| 1201 | `    <form class="lock-form" method="post" action="{{ url_for('logout') }}">` |
| 1202 | `      {% if csrf_token is defined %}` |
| 1203 | `        <input type="hidden" name="csrf_token" value="{{ csrf_token }}">` |
| 1204 | `      {% endif %}` |
| 1205 | `      <button class="lock-btn" type="submit">🔒 KİLİTLE</button>` |
| 1206 | `    </form>` |
| 1207 | `` |
| 1208 | `</main>` |
| 1209 | `` |
| 1210 | `<style id="home-route-lock-fix">` |
| 1211 | `.route-form{` |
| 1212 | `  margin-bottom:14px;` |
| 1213 | `}` |
| 1214 | `` |
| 1215 | `.route-picker{` |
| 1216 | `  height:54px;` |
| 1217 | `  display:flex;` |
| 1218 | `  align-items:center;` |
| 1219 | `  gap:12px;` |
| 1220 | `  padding:0 16px;` |
| 1221 | `  border-radius:19px;` |
| 1222 | `  background:#fff;` |
| 1223 | `  border:1px solid rgba(148,163,184,.22);` |
| 1224 | `  box-shadow:0 10px 24px rgba(15,23,42,.08);` |
| 1225 | `}` |
| 1226 | `` |
| 1227 | `.route-picker .pin{` |
| 1228 | `  font-size:22px;` |
| 1229 | `}` |
| 1230 | `` |
| 1231 | `#homeRouteSelect{` |
| 1232 | `  flex:1;` |
| 1233 | `  min-width:0;` |
| 1234 | `  border:0;` |
| 1235 | `  outline:0;` |
| 1236 | `  background:transparent;` |
| 1237 | `  color:#0f172a;` |
| 1238 | `  font-family:system-ui,-apple-system,"Segoe UI",Roboto,Arial,sans-serif;` |
| 1239 | `  font-size:17px;` |
| 1240 | `  font-weight:900;` |
| 1241 | `  appearance:none;` |
| 1242 | `  -webkit-appearance:none;` |
| 1243 | `}` |
| 1244 | `` |
| 1245 | `.route-picker .caret{` |

## 5) WEB active-route-lock-final bölgesi

| Satır | İçerik |
| ---: | --- |
| 1859 | `  if(routeBtn){` |
| 1860 | `    routeBtn.addEventListener("click", function(e){` |
| 1861 | `      e.preventDefault();` |
| 1862 | `      e.stopPropagation();` |
| 1863 | `      e.stopImmediatePropagation();` |
| 1864 | `      showGuard();` |
| 1865 | `      return false;` |
| 1866 | `    }, true);` |
| 1867 | `  }` |
| 1868 | `})();` |
| 1869 | `</script>` |
| 1870 | `` |
| 1871 | `` |
| 1872 | `` |
| 1873 | `<!-- ACTIVE_ROUTE_LOCK_FINAL_START -->` |
| 1874 | `<script id="active-route-lock-final">` |
| 1875 | `(function(){` |
| 1876 | `  const HAS_ACTIVE_TRIP = {% if active_trip is defined and active_trip %}true{% else %}false{% endif %};` |
| 1877 | `  const ACTIVE_TRIP_ROUTE = {% if active_trip is defined and active_trip %}{{ active_trip.route\|tojson }}{% else %}""{% endif %};` |
| 1878 | `` |
| 1879 | `  if(!HAS_ACTIVE_TRIP) return;` |
| 1880 | `` |
| 1881 | `  const routeBtn = document.getElementById("routePickerBtn");` |
| 1882 | `  const routeText = document.getElementById("routePickerText");` |
| 1883 | `  const routeSelect = document.getElementById("homeRouteSelect");` |
| 1884 | `  const startLink = document.getElementById("homeTripStart");` |
| 1885 | `` |
| 1886 | `  const continueLink =` |
| 1887 | `    Array.from(document.querySelectorAll(".hero-link"))[1] \|\|` |
| 1888 | `    document.querySelector('a[href*="continue"]') \|\|` |
| 1889 | `    document.querySelector('a[href*="seats"]');` |
| 1890 | `` |
| 1891 | `  const sheet = document.getElementById("routeSheet");` |
| 1892 | `  const backdrop = document.getElementById("routeSheetBackdrop");` |
| 1893 | `` |
| 1894 | `  function hardCloseRouteSheet(){` |
| 1895 | `    if(sheet){` |
| 1896 | `      sheet.classList.remove("show");` |
| 1897 | `      sheet.hidden = true;` |
| 1898 | `      sheet.setAttribute("aria-hidden", "true");` |
| 1899 | `    }` |
| 1900 | `    if(backdrop){` |
| 1901 | `      backdrop.classList.remove("show");` |
| 1902 | `      backdrop.hidden = true;` |
| 1903 | `      backdrop.setAttribute("aria-hidden", "true");` |
| 1904 | `    }` |
| 1905 | `  }` |
| 1906 | `` |
| 1907 | `  function forceActiveRouteText(){` |
| 1908 | `    if(!ACTIVE_TRIP_ROUTE) return;` |
| 1909 | `` |

## 5) WEB route-sheet-no-flash-fix bölgesi

| Satır | İçerik |
| ---: | --- |
| 1016 | `  .desc,` |
| 1017 | `  .menu-desc,` |
| 1018 | `  .quick-desc,` |
| 1019 | `  .card-desc,` |
| 1020 | `  .tile-desc,` |
| 1021 | `  .status-desc,` |
| 1022 | `  .small,` |
| 1023 | `  .label,` |
| 1024 | `  .meta,` |
| 1025 | `  .hint{` |
| 1026 | `    font-family:var(--font-body) !important;` |
| 1027 | `  }` |
| 1028 | `</style>` |
| 1029 | `` |
| 1030 | `` |
| 1031 | `<style id="route-sheet-no-flash-fix">` |
| 1032 | `  /* Route picker ilk render parlamasını engeller */` |
| 1033 | `  #routeSheet[hidden],` |
| 1034 | `  #routeSheetBackdrop[hidden]{` |
| 1035 | `    display:none !important;` |
| 1036 | `  }` |
| 1037 | `` |
| 1038 | `  #routeSheet:not(.show),` |
| 1039 | `  #routeSheetBackdrop:not(.show){` |
| 1040 | `    display:none !important;` |
| 1041 | `  }` |
| 1042 | `</style>` |
| 1043 | `` |
| 1044 | `` |
| 1045 | `</head>` |
| 1046 | `` |
| 1047 | `<body>` |
| 1048 | `  <main class="home-shell">` |
| 1049 | `` |
| 1050 | `    {% set current_route = selected_route if selected_route is defined and selected_route else (active_trip.route if active_trip is defined and active_trip else 'Denizli – İstanbul') %}` |
| 1051 | `` |
| 1052 | `    {% set current_route = selected_route if selected_route is defined and selected_route else (active_trip.route if active_trip is defined and active_trip else 'Denizli – İstanbul') %}` |
| 1053 | `` |
| 1054 | `    <div class="route-form route-premium">` |
| 1055 | `      <button class="route-picker-premium" id="routePickerBtn" type="button">` |
| 1056 | `        <span class="route-pin">📍</span>` |
| 1057 | `        <span class="route-name" id="routePickerText">{{ current_route }}</span>` |
| 1058 | `        <span class="route-caret">⌄</span>` |
| 1059 | `      </button>` |
| 1060 | `` |
| 1061 | `      <select id="homeRouteSelect" name="route" hidden>` |
| 1062 | `        {% if all_routes is defined and all_routes %}` |
| 1063 | `          {% for r in all_routes %}` |
| 1064 | `            <option value="{{ r }}" {% if r == current_route %}selected{% endif %}>{{ r }}</option>` |
| 1065 | `          {% endfor %}` |
| 1066 | `        {% else %}` |

## 6) app.py Sefer / Route Endpoint İzleri

| Dosya | Satır | İçerik |
| --- | ---: | --- |
| WEB app.py | 461 | `            active_trip_id INTEGER` |
| WEB app.py | 463 | `        INSERT OR IGNORE INTO app_state(id, active_trip_id) VALUES (1, NULL);` |
| WEB app.py | 617 | `            route_name TEXT NOT NULL,` |
| WEB app.py | 627 | `        ON route_schedule_profiles(route_name);` |
| WEB app.py | 630 | `        ON route_schedule_profiles(route_name, direction);` |
| WEB app.py | 790 | `def set_active_trip(trip_id: Optional[int]) -> None:` |
| WEB app.py | 792 | `    db.execute("UPDATE app_state SET active_trip_id=? WHERE id=1", (trip_id,))` |
| WEB app.py | 796 | `def get_active_trip() -> Optional[int]:` |
| WEB app.py | 797 | `    row = get_db().execute("SELECT active_trip_id FROM app_state WHERE id=1").fetchone()` |
| WEB app.py | 798 | `    return row["active_trip_id"] if row else None` |
| WEB app.py | 801 | `def get_active_trip_row():` |
| WEB app.py | 802 | `    tid = get_active_trip()` |
| WEB app.py | 911 | `        tid = int(tid_raw) if tid_raw else int(get_active_trip() or 0)` |
| WEB app.py | 913 | `        tid = int(get_active_trip() or 0)` |
| WEB app.py | 958 | `def get_stops(route_name: str):` |
| WEB app.py | 959 | `    row = get_db().execute("SELECT stops FROM routes WHERE name=?", (route_name,)).fetchone()` |
| WEB app.py | 965 | `    return ROUTE_STOPS.get(route_name, ROUTE_STOPS.get("Denizli – İstanbul", []))` |
| WEB app.py | 968 | `def all_route_names():` |
| WEB app.py | 973 | `def validate_stop_for_trip(route_name: str, stop: str) -> bool:` |
| WEB app.py | 974 | `    return (stop or "").strip() in set(get_stops(route_name))` |
| WEB app.py | 977 | `def validate_stop_for_active_trip(stop: str) -> bool:` |
| WEB app.py | 978 | `    trip = get_active_trip_row()` |
| WEB app.py | 993 | `def schedule_profiles_for_route(route_name: str):` |
| WEB app.py | 996 | `        SELECT id, route_name, title, direction, is_default, note, created_at, updated_at` |
| WEB app.py | 998 | `        WHERE route_name=?` |
| WEB app.py | 1001 | `        (route_name,),` |
| WEB app.py | 1011 | `        SELECT id, route_name, title, direction, is_default, note, created_at, updated_at` |
| WEB app.py | 1033 | `def schedule_editor_rows(route_name: str, profile_id: Optional[int] = None):` |
| WEB app.py | 1034 | `    stops = get_stops(route_name)` |
| WEB app.py | 1055 | `def schedule_default_profile_for_route(route_name: str, direction: str = "gidis"):` |
| WEB app.py | 1058 | `        SELECT id, route_name, title, direction, is_default, note` |
| WEB app.py | 1060 | `        WHERE route_name=? AND direction=?` |
| WEB app.py | 1064 | `        (route_name, direction),` |
| WEB app.py | 1208 | `            "active_trip": get_active_trip_row(),` |
| WEB app.py | 1213 | `            "active_trip": None,` |
| WEB app.py | 1341 | `    routes = all_route_names()` |
| WEB app.py | 1346 | `@app.route("/set-route", methods=["POST"])` |
| WEB app.py | 1353 | `    if route not in set(all_route_names()):` |
| WEB app.py | 1360 | `@app.route("/sefer-baslat", methods=["GET", "POST"])` |
| WEB app.py | 1362 | `    routes = all_route_names()` |
| WEB app.py | 1400 | `        set_active_trip(trip_id)` |
| WEB app.py | 1405 | `        "start_trip.html",` |
| WEB app.py | 1418 | `    tid = get_active_trip()` |
| WEB app.py | 1426 | `        set_active_trip(None)` |
| WEB app.py | 1519 | `            WHERE route_name=?` |
| WEB app.py | 1914 | `    tid = get_active_trip()` |
| WEB app.py | 2024 | `    tid = get_active_trip()` |
| WEB app.py | 2126 | `    tid = get_active_trip()` |
| WEB app.py | 2229 | `    tid = get_active_trip()` |
| WEB app.py | 2354 | `    tid = get_active_trip()` |
| WEB app.py | 2431 | `    tid = get_active_trip()` |
| WEB app.py | 2500 | `    tid = get_active_trip()` |
| WEB app.py | 2711 | `    tid = get_active_trip()` |
| WEB app.py | 2957 | `    tid = get_active_trip()` |
| WEB app.py | 2965 | `        set_active_trip(None)` |
| WEB app.py | 2968 | `    route_name = trip["route"] or ""` |
| WEB app.py | 2969 | `    stops = get_stops(route_name)` |
| WEB app.py | 2988 | `            (route_name,),` |
| WEB app.py | 3203 | `            (route_name,),` |
| WEB app.py | 3240 | `                    if (x.get("route") or "") == route_name` |
| WEB app.py | 3274 | `    "get_active_trip_row": get_active_trip_row,` |
| WEB app.py | 3276 | `    "all_route_names": all_route_names,` |
| WEB app.py | 3297 | `    "get_active_trip": get_active_trip,` |
| WEB app.py | 3313 | `    "get_active_trip_row": get_active_trip_row,` |
| WEB app.py | 3321 | `    "validate_stop_for_active_trip": validate_stop_for_active_trip,` |
| WEB app.py | 3478 | `    "get_active_trip": get_active_trip,` |
| WEB app.py | 3479 | `    "set_active_trip": set_active_trip,` |
| WEB app.py | 3492 | `    "validate_stop_for_active_trip": validate_stop_for_active_trip,` |
| WEB app.py | 3507 | `    "get_active_trip": get_active_trip,` |
| WEB app.py | 3508 | `    "get_active_trip_row": get_active_trip_row,` |
| WEB app.py | 3515 | `    tid = get_active_trip()` |
| WEB app.py | 3553 | `        if from_stop and not validate_stop_for_active_trip(from_stop):` |
| WEB app.py | 3555 | `        if to_stop and not validate_stop_for_active_trip(to_stop):` |
| WEB app.py | 3604 | `    if to_param and not validate_stop_for_active_trip(to_param):` |
| WEB app.py | 3663 | `    tid = get_active_trip()` |
| WEB app.py | 3695 | `        if from_stop and not validate_stop_for_active_trip(from_stop):` |
| WEB app.py | 3697 | `        if to_stop and not validate_stop_for_active_trip(to_stop):` |
| WEB app.py | 3731 | `    if to_param and not validate_stop_for_active_trip(to_param):` |
| WEB app.py | 3755 | `    tid = get_active_trip()` |
| WEB app.py | 3789 | `    tid = get_active_trip()` |
| WEB app.py | 3858 | `    tid = get_active_trip()` |
| WEB app.py | 3901 | `    if not validate_stop_for_active_trip(stop_name):` |
| WEB app.py | 3953 | `    tid = get_active_trip()` |
| WEB app.py | 4065 | `    "get_active_trip": get_active_trip,` |
| WEB app.py | 4066 | `    "all_route_names": all_route_names,` |
| WEB app.py | 4167 | `    tid = get_active_trip()` |
| WEB app.py | 4241 | `    "get_active_trip": get_active_trip,` |
| WEB app.py | 4244 | `    "validate_stop_for_active_trip": validate_stop_for_active_trip,` |
| WEB app.py | 4367 | `    tid = get_active_trip()` |
| WEB app.py | 4404 | `        db.execute("UPDATE app_state SET active_trip_id=NULL WHERE id=1")` |
| WEB app.py | 4412 | `        db.execute("UPDATE app_state SET active_trip_id=NULL WHERE id=1")` |
| ANDROID app.py | 461 | `            active_trip_id INTEGER` |
| ANDROID app.py | 463 | `        INSERT OR IGNORE INTO app_state(id, active_trip_id) VALUES (1, NULL);` |
| ANDROID app.py | 617 | `            route_name TEXT NOT NULL,` |
| ANDROID app.py | 627 | `        ON route_schedule_profiles(route_name);` |
| ANDROID app.py | 630 | `        ON route_schedule_profiles(route_name, direction);` |
| ANDROID app.py | 790 | `def set_active_trip(trip_id: Optional[int]) -> None:` |
| ANDROID app.py | 792 | `    db.execute("UPDATE app_state SET active_trip_id=? WHERE id=1", (trip_id,))` |
| ANDROID app.py | 796 | `def get_active_trip() -> Optional[int]:` |
| ANDROID app.py | 797 | `    row = get_db().execute("SELECT active_trip_id FROM app_state WHERE id=1").fetchone()` |
| ANDROID app.py | 798 | `    return row["active_trip_id"] if row else None` |
| ANDROID app.py | 801 | `def get_active_trip_row():` |
| ANDROID app.py | 802 | `    tid = get_active_trip()` |
| ANDROID app.py | 911 | `        tid = int(tid_raw) if tid_raw else int(get_active_trip() or 0)` |
| ANDROID app.py | 913 | `        tid = int(get_active_trip() or 0)` |
| ANDROID app.py | 958 | `def get_stops(route_name: str):` |
| ANDROID app.py | 959 | `    row = get_db().execute("SELECT stops FROM routes WHERE name=?", (route_name,)).fetchone()` |
| ANDROID app.py | 965 | `    return ROUTE_STOPS.get(route_name, ROUTE_STOPS.get("Denizli – İstanbul", []))` |
| ANDROID app.py | 968 | `def all_route_names():` |
| ANDROID app.py | 973 | `def validate_stop_for_trip(route_name: str, stop: str) -> bool:` |
| ANDROID app.py | 974 | `    return (stop or "").strip() in set(get_stops(route_name))` |
| ANDROID app.py | 977 | `def validate_stop_for_active_trip(stop: str) -> bool:` |
| ANDROID app.py | 978 | `    trip = get_active_trip_row()` |
| ANDROID app.py | 993 | `def schedule_profiles_for_route(route_name: str):` |
| ANDROID app.py | 996 | `        SELECT id, route_name, title, direction, is_default, note, created_at, updated_at` |
| ANDROID app.py | 998 | `        WHERE route_name=?` |
| ANDROID app.py | 1001 | `        (route_name,),` |
| ANDROID app.py | 1011 | `        SELECT id, route_name, title, direction, is_default, note, created_at, updated_at` |
| ANDROID app.py | 1033 | `def schedule_editor_rows(route_name: str, profile_id: Optional[int] = None):` |
| ANDROID app.py | 1034 | `    stops = get_stops(route_name)` |
| ANDROID app.py | 1055 | `def schedule_default_profile_for_route(route_name: str, direction: str = "gidis"):` |
| ANDROID app.py | 1058 | `        SELECT id, route_name, title, direction, is_default, note` |
| ANDROID app.py | 1060 | `        WHERE route_name=? AND direction=?` |
| ANDROID app.py | 1064 | `        (route_name, direction),` |
| ANDROID app.py | 1208 | `            "active_trip": get_active_trip_row(),` |
| ANDROID app.py | 1213 | `            "active_trip": None,` |
| ANDROID app.py | 1341 | `    routes = all_route_names()` |
| ANDROID app.py | 1346 | `@app.route("/set-route", methods=["POST"])` |
| ANDROID app.py | 1353 | `    if route not in set(all_route_names()):` |
| ANDROID app.py | 1360 | `@app.route("/sefer-baslat", methods=["GET", "POST"])` |
| ANDROID app.py | 1362 | `    routes = all_route_names()` |
| ANDROID app.py | 1400 | `        set_active_trip(trip_id)` |
| ANDROID app.py | 1405 | `        "start_trip.html",` |
| ANDROID app.py | 1413 | `    tid = get_active_trip()` |
| ANDROID app.py | 1421 | `        set_active_trip(None)` |
| ANDROID app.py | 1514 | `            WHERE route_name=?` |
| ANDROID app.py | 1909 | `    tid = get_active_trip()` |
| ANDROID app.py | 2019 | `    tid = get_active_trip()` |
| ANDROID app.py | 2121 | `    tid = get_active_trip()` |
| ANDROID app.py | 2224 | `    tid = get_active_trip()` |
| ANDROID app.py | 2349 | `    tid = get_active_trip()` |
| ANDROID app.py | 2426 | `    tid = get_active_trip()` |
| ANDROID app.py | 2495 | `    tid = get_active_trip()` |
| ANDROID app.py | 2706 | `    tid = get_active_trip()` |
| ANDROID app.py | 2952 | `    tid = get_active_trip()` |
| ANDROID app.py | 2960 | `        set_active_trip(None)` |
| ANDROID app.py | 2963 | `    route_name = trip["route"] or ""` |
| ANDROID app.py | 2964 | `    stops = get_stops(route_name)` |
| ANDROID app.py | 2983 | `            (route_name,),` |
| ANDROID app.py | 3198 | `            (route_name,),` |
| ANDROID app.py | 3235 | `                    if (x.get("route") or "") == route_name` |
| ANDROID app.py | 3269 | `    "get_active_trip_row": get_active_trip_row,` |
| ANDROID app.py | 3271 | `    "all_route_names": all_route_names,` |
| ANDROID app.py | 3292 | `    "get_active_trip": get_active_trip,` |
| ANDROID app.py | 3308 | `    "get_active_trip_row": get_active_trip_row,` |
| ANDROID app.py | 3316 | `    "validate_stop_for_active_trip": validate_stop_for_active_trip,` |
| ANDROID app.py | 3473 | `    "get_active_trip": get_active_trip,` |
| ANDROID app.py | 3474 | `    "set_active_trip": set_active_trip,` |
| ANDROID app.py | 3487 | `    "validate_stop_for_active_trip": validate_stop_for_active_trip,` |
| ANDROID app.py | 3502 | `    "get_active_trip": get_active_trip,` |
| ANDROID app.py | 3503 | `    "get_active_trip_row": get_active_trip_row,` |
| ANDROID app.py | 3510 | `    tid = get_active_trip()` |
| ANDROID app.py | 3548 | `        if from_stop and not validate_stop_for_active_trip(from_stop):` |
| ANDROID app.py | 3550 | `        if to_stop and not validate_stop_for_active_trip(to_stop):` |
| ANDROID app.py | 3599 | `    if to_param and not validate_stop_for_active_trip(to_param):` |
| ANDROID app.py | 3658 | `    tid = get_active_trip()` |
| ANDROID app.py | 3690 | `        if from_stop and not validate_stop_for_active_trip(from_stop):` |
| ANDROID app.py | 3692 | `        if to_stop and not validate_stop_for_active_trip(to_stop):` |
| ANDROID app.py | 3726 | `    if to_param and not validate_stop_for_active_trip(to_param):` |
| ANDROID app.py | 3750 | `    tid = get_active_trip()` |
| ANDROID app.py | 3784 | `    tid = get_active_trip()` |
| ANDROID app.py | 3853 | `    tid = get_active_trip()` |
| ANDROID app.py | 3896 | `    if not validate_stop_for_active_trip(stop_name):` |
| ANDROID app.py | 3948 | `    tid = get_active_trip()` |
| ANDROID app.py | 4060 | `    "get_active_trip": get_active_trip,` |
| ANDROID app.py | 4061 | `    "all_route_names": all_route_names,` |
| ANDROID app.py | 4162 | `    tid = get_active_trip()` |
| ANDROID app.py | 4236 | `    "get_active_trip": get_active_trip,` |
| ANDROID app.py | 4239 | `    "validate_stop_for_active_trip": validate_stop_for_active_trip,` |
| ANDROID app.py | 4362 | `    tid = get_active_trip()` |
| ANDROID app.py | 4399 | `        db.execute("UPDATE app_state SET active_trip_id=NULL WHERE id=1")` |
| ANDROID app.py | 4407 | `        db.execute("UPDATE app_state SET active_trip_id=NULL WHERE id=1")` |

## 7) İlk Teknik Yorum

- `disabled`, `hidden`, `pointer-events`, `preventDefault`, `tripGuard` ve `active-route-lock` satırları hat seçimini kilitleyebilir.
- WEB ve ANDROID index.html farklıysa, APK’da hat seçme davranışı webden farklı çalışabilir.
- Özellikle aktif sefer kilidi yeni sefer başlat ekranına yanlış uygulanıyorsa hat seçimi tıklanmaz hale gelir.