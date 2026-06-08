# Muavin Asistanı Fonksiyonel Fark Raporu V5

- Tarih: `20260608-164505`

## 1) Dosya Bazlı Ham / Normalize Karşılaştırma

Normalize karşılaştırma boş satır ve yorum farklarını ayıklar. Ham farklı ama normalize aynıysa çoğu zaman fonksiyonel fark yoktur.

| Dosya | Ham | Normalize | WEB satır | ANDROID satır | WEB hash | ANDROID hash | WEB norm | ANDROID norm |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| app.py | FARKLI | AYNI | 4512 | 4507 | 7d03ec46f6c0 | cf451e1df53e | 18f2982be0f6 | 18f2982be0f6 |
| templates/seats.html | FARKLI | FARKLI | 1090 | 1089 | ed8d71df17a4 | 144cb05b9f9e | 8bc313a72eaf | f8bd944bce95 |
| templates/index.html | FARKLI | FARKLI | 2002 | 1778 | e35932eeab6b | 25f6b94cbb7b | 18d65c905492 | a1f413145339 |
| templates/trip_report.html | FARKLI | FARKLI | 1483 | 1151 | 5a07387882e7 | d178f59a71e0 | 1adc27ba189a | 270febf08234 |
| templates/report_archive.html | FARKLI | FARKLI | 496 | 101 | 9e36f61fa04f | 3b8702f4d24a | bf2d1486ced0 | a0823ea8baa5 |
| templates/settings.html | FARKLI | FARKLI | 585 | 204 | 0556e96d2b4b | 25b8553debc6 | d9a80957c26d | 2613a65afa55 |

## 2) app.py Kritik Fonksiyon Karşılaştırması
| Fonksiyon | WEB | ANDROID | Ham | Normalize | WEB satır | ANDROID satır | WEB norm | ANDROID norm |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| trip_start | VAR | VAR | FARKLI | AYNI | 55 | 50 | b388d6d62ca7 | b388d6d62ca7 |
| continue_trip | VAR | VAR | AYNI | AYNI | 136 | 136 | 0b57454206da | 0b57454206da |
| api_walkon | VAR | VAR | AYNI | AYNI | 147 | 147 | 0d0271819d70 | 0d0271819d70 |
| api_standing | VAR | VAR | AYNI | AYNI | 91 | 91 | 23bdc68bb677 | 23bdc68bb677 |
| api_standing_list | VAR | VAR | AYNI | AYNI | 33 | 33 | f5edadd6c4ad | f5edadd6c4ad |
| api_stats | VAR | VAR | AYNI | AYNI | 60 | 60 | 5d87f099c47e | 5d87f099c47e |
| api_stoplog | VAR | VAR | AYNI | AYNI | 89 | 89 | 275fda07bc50 | 275fda07bc50 |
| trip_report_page | VAR | VAR | AYNI | AYNI | 4 | 4 | 1dc818dfcb60 | 1dc818dfcb60 |
| api_trip_report | VAR | VAR | AYNI | AYNI | 25 | 25 | cef60aec5766 | cef60aec5766 |
| latest_trip_report_redirect | VAR | VAR | AYNI | AYNI | 23 | 23 | 38a764163672 | 38a764163672 |
| report_archive_page | VAR | VAR | AYNI | AYNI | 26 | 26 | ddde7502b575 | ddde7502b575 |
| end_trip | VAR | VAR | AYNI | AYNI | 137 | 137 | 52fcfdec3ffd | 52fcfdec3ffd |

## 3) Route Farkları

### WEB'de var ANDROID'de yok
_Kayıt yok._

### ANDROID'de var WEB'de yok
_Kayıt yok._

## 4) seats.html Static Link Karşılaştırması
| Static link | WEB | ANDROID |
| --- | --- | --- |
| /static/seats/bags.js?v=1 | VAR | VAR |
| /static/seats/drive-controls.js?v=drive-toggle-fix-1 | VAR | VAR |
| /static/seats/drive-eta-chip.js?v=1 | VAR | VAR |
| /static/seats/patches/bottom-voice-command.css?v=1 | VAR | VAR |
| /static/seats/patches/fab-sheet-solid-fix.css?v=1 | VAR | VAR |
| /static/seats/patches/manual-ticket-system.css?v=1 | VAR | VAR |
| /static/seats/patches/manual-ticket-system.js?v=1 | VAR | VAR |
| /static/seats/patches/mobile-performance-fix.css?v=2 | VAR | VAR |
| /static/seats/patches/modal-bottom-nav-autohide.css?v=1 | VAR | VAR |
| /static/seats/patches/modal-bottom-nav-autohide.js?v=1 | VAR | VAR |
| /static/seats/patches/seat-label-ghost-clean.css?v=1 | VAR | VAR |
| /static/seats/patches/seat-layout-fab-pack.css?v=1 | VAR | VAR |
| /static/seats/patches/seat-layout-fab-pack.js?v=1 | VAR | VAR |
| /static/seats/patches/seat-simple-ui-pack.css?v=1 | VAR | VAR |
| /static/seats/patches/seat-simple-ui-pack.js?v=1 | VAR | VAR |
| /static/seats/patches/stop-flow-compact-mobile.css?v=1 | VAR | VAR |
| /static/seats/patches/stop-flow-focus-patch.css?v=1 | VAR | VAR |
| /static/seats/patches/stop-flow-focus-patch.js?v=simple-scope-1 | VAR | VAR |
| /static/seats/patches/stop-selected-toast.css?v=1 | VAR | VAR |
| /static/seats/patches/stop-selected-toast.js?v=1 | VAR | VAR |
| /static/seats/patches/top-sound-toggle.css?v=1 | VAR | VAR |
| /static/seats/patches/top-sound-toggle.js?v=1 | VAR | VAR |
| /static/seats/patches/unified-seat-deck-report-style.css?v=seat-smaller-removed-2 | VAR | - |
| /static/seats/route-marquee.js?v=route-clean-ticker-single-1 | VAR | VAR |
| /static/seats/seats-final.css?v=drive-voice-real-width-test-1 | VAR | VAR |
| /static/seats/seats-time-prayer.js?v=time-prayer-apk-1 | VAR | VAR |
| /static/seats/seats.css?v=41 | VAR | VAR |
| /static/seats/seats.js?v=tripkey-by-id-1 | VAR | VAR |
| /static/seats/standing.js?v=1 | VAR | VAR |
| /static/seats/voice-commands.js?v=voice-listen-guard-1 | VAR | VAR |
| /static/seats/voice-tts.js?v=voice-owner-fix-1 | VAR | VAR |
| /static/style.css | VAR | VAR |

## 5) seats.html Kritik Kelime Satırları

### WEB templates/seats.html
| Satır | İçerik |
| --- | --- |
| 12 | <link rel="stylesheet" href="/static/seats/patches/modal-bottom-nav-autohide.css?v=1"> |
| 13 | <link rel="stylesheet" href="/static/seats/patches/manual-ticket-system.css?v=1"> |
| 15 | <link rel="stylesheet" href="/static/seats/patches/seat-simple-ui-pack.css?v=1"> |
| 16 | <link rel="stylesheet" href="/static/seats/patches/unified-seat-deck-report-style.css?v=seat-smaller-removed-2"> |
| 17 | <link rel="stylesheet" href="/static/seats/patches/mobile-performance-fix.css?v=2"> |
| 253 | <button class="btn accent" type="button" id="btnSaveCoord">Koordinatı Kaydet</button> |
| 305 | <div class="standing-list" id="quickStandingList"></div> |
| 336 | {% include "seats_parts/modals.html" %} |
| 366 | <script src="/static/seats/standing.js?v=1"></script> |
| 376 | <script src="/static/seats/patches/modal-bottom-nav-autohide.js?v=1"></script> |
| 377 | <script src="/static/seats/patches/manual-ticket-system.js?v=1"></script> |
| 379 | <script src="/static/seats/patches/seat-simple-ui-pack.js?v=1"></script> |
| 628 | {% include "seats_parts/finish_trip_modal.html" %} |

### ANDROID templates/seats.html
| Satır | İçerik |
| --- | --- |
| 12 | <link rel="stylesheet" href="/static/seats/patches/modal-bottom-nav-autohide.css?v=1"> |
| 13 | <link rel="stylesheet" href="/static/seats/patches/manual-ticket-system.css?v=1"> |
| 15 | <link rel="stylesheet" href="/static/seats/patches/seat-simple-ui-pack.css?v=1"> |
| 16 | <link rel="stylesheet" href="/static/seats/patches/mobile-performance-fix.css?v=2"> |
| 252 | <button class="btn accent" type="button" id="btnSaveCoord">Koordinatı Kaydet</button> |
| 304 | <div class="standing-list" id="quickStandingList"></div> |
| 335 | {% include "seats_parts/modals.html" %} |
| 365 | <script src="/static/seats/standing.js?v=1"></script> |
| 375 | <script src="/static/seats/patches/modal-bottom-nav-autohide.js?v=1"></script> |
| 376 | <script src="/static/seats/patches/manual-ticket-system.js?v=1"></script> |
| 378 | <script src="/static/seats/patches/seat-simple-ui-pack.js?v=1"></script> |
| 627 | {% include "seats_parts/finish_trip_modal.html" %} |

## 6) index.html Kritik Kelime Satırları

### WEB templates/index.html
| Satır | İçerik |
| --- | --- |
| 602 | /* Aktif sefer uyarı modalı dark */ |
| 607 | .trip-guard-modal{ |
| 616 | .trip-guard-modal h2{ |
| 620 | .trip-guard-modal p{ |
| 1033 | #routeSheet[hidden], |
| 1034 | #routeSheetBackdrop[hidden]{ |
| 1038 | #routeSheet:not(.show), |
| 1039 | #routeSheetBackdrop:not(.show){ |
| 1072 | <div class="route-sheet-backdrop" id="routeSheetBackdrop" hidden aria-hidden="true"></div> |
| 1074 | <section class="route-sheet" id="routeSheet" hidden aria-hidden="true"> |
| 1082 | <button class="route-sheet-close" id="routeSheetClose" type="button">×</button> |
| 1281 | const saved = localStorage.getItem("homeSelectedRoute"); |
| 1282 | if(saved){ |
| 1283 | const opt = Array.from(routeSelect.options).find(o => o.value === saved); |
| 1284 | if(opt) routeSelect.value = saved; |
| 1550 | const sheet = document.getElementById("routeSheet"); |
| 1551 | const backdrop = document.getElementById("routeSheetBackdrop"); |
| 1552 | const closeBtn = document.getElementById("routeSheetClose"); |
| 1604 | const saved = localStorage.getItem("homeSelectedRoute"); |
| 1605 | if(saved && Array.from(select.options).some(o => o.value === saved)){ |
| 1606 | setRoute(saved); |
| 1662 | .trip-guard-modal{ |
| 1681 | .trip-guard-modal.show{ |
| 1683 | animation:tripGuardIn .16s ease forwards; |
| 1686 | @keyframes tripGuardIn{ |
| 1702 | .trip-guard-modal h2{ |
| 1710 | .trip-guard-modal p{ |
| 1751 | .trip-guard-modal{ |
| 1800 | let backdrop = document.getElementById("tripGuardBackdrop"); |
| 1801 | let modal = document.getElementById("tripGuardModal"); |
| 1803 | if(backdrop && modal) return {backdrop, modal}; |
| 1806 | backdrop.id = "tripGuardBackdrop"; |
| 1809 | modal = document.createElement("section"); |
| 1810 | modal.id = "tripGuardModal"; |
| 1811 | modal.className = "trip-guard-modal"; |
| 1812 | modal.innerHTML = ` |
| 1817 | <a class="trip-guard-go" id="tripGuardGo" href="#">Devam eden sefere git</a> |
| 1818 | <button class="trip-guard-ok" id="tripGuardOk" type="button">Tamam</button> |
| 1823 | document.body.appendChild(modal); |
| 1827 | modal.classList.remove("show"); |
| 1831 | modal.querySelector("#tripGuardOk").addEventListener("click", close); |
| 1833 | const go = modal.querySelector("#tripGuardGo"); |
| 1838 | return {backdrop, modal}; |
| 1842 | const {backdrop, modal} = ensureModal(); |
| 1844 | modal.classList.add("show"); |
| 1891 | const sheet = document.getElementById("routeSheet"); |
| 1892 | const backdrop = document.getElementById("routeSheetBackdrop"); |
| 1923 | let bd = document.getElementById("tripGuardBackdrop"); |
| 1924 | let modal = document.getElementById("tripGuardModal"); |
| 1926 | if(bd && modal) return {bd, modal}; |
| 1929 | bd.id = "tripGuardBackdrop"; |
| 1932 | modal = document.createElement("section"); |
| 1933 | modal.id = "tripGuardModal"; |
| 1934 | modal.className = "trip-guard-modal"; |
| 1935 | modal.innerHTML = ` |
| 1940 | <a class="trip-guard-go" id="tripGuardGo" href="#">Devam eden sefere git</a> |
| 1941 | <button class="trip-guard-ok" id="tripGuardOk" type="button">Tamam</button> |
| 1946 | document.body.appendChild(modal); |
| 1950 | modal.classList.remove("show"); |
| 1954 | modal.querySelector("#tripGuardOk")?.addEventListener("click", close); |
| 1956 | const go = modal.querySelector("#tripGuardGo"); |
| 1961 | return {bd, modal}; |
| 1968 | const {bd, modal} = ensureModal(); |
| 1970 | modal.classList.add("show"); |

### ANDROID templates/index.html
| Satır | İçerik |
| --- | --- |
| 602 | /* Aktif sefer uyarı modalı dark */ |
| 607 | .trip-guard-modal{ |
| 616 | .trip-guard-modal h2{ |
| 620 | .trip-guard-modal p{ |
| 978 | <div class="route-sheet-backdrop" id="routeSheetBackdrop"></div> |
| 980 | <section class="route-sheet" id="routeSheet" aria-hidden="true"> |
| 988 | <button class="route-sheet-close" id="routeSheetClose" type="button">×</button> |
| 1187 | const saved = localStorage.getItem("homeSelectedRoute"); |
| 1188 | if(saved){ |
| 1189 | const opt = Array.from(routeSelect.options).find(o => o.value === saved); |
| 1190 | if(opt) routeSelect.value = saved; |
| 1456 | const sheet = document.getElementById("routeSheet"); |
| 1457 | const backdrop = document.getElementById("routeSheetBackdrop"); |
| 1458 | const closeBtn = document.getElementById("routeSheetClose"); |
| 1510 | const saved = localStorage.getItem("homeSelectedRoute"); |
| 1511 | if(saved && Array.from(select.options).some(o => o.value === saved)){ |
| 1512 | setRoute(saved); |
| 1568 | .trip-guard-modal{ |
| 1587 | .trip-guard-modal.show{ |
| 1589 | animation:tripGuardIn .16s ease forwards; |
| 1592 | @keyframes tripGuardIn{ |
| 1608 | .trip-guard-modal h2{ |
| 1616 | .trip-guard-modal p{ |
| 1657 | .trip-guard-modal{ |
| 1706 | let backdrop = document.getElementById("tripGuardBackdrop"); |
| 1707 | let modal = document.getElementById("tripGuardModal"); |
| 1709 | if(backdrop && modal) return {backdrop, modal}; |
| 1712 | backdrop.id = "tripGuardBackdrop"; |
| 1715 | modal = document.createElement("section"); |
| 1716 | modal.id = "tripGuardModal"; |
| 1717 | modal.className = "trip-guard-modal"; |
| 1718 | modal.innerHTML = ` |
| 1723 | <a class="trip-guard-go" id="tripGuardGo" href="#">Devam eden sefere git</a> |
| 1724 | <button class="trip-guard-ok" id="tripGuardOk" type="button">Tamam</button> |
| 1729 | document.body.appendChild(modal); |
| 1733 | modal.classList.remove("show"); |
| 1737 | modal.querySelector("#tripGuardOk").addEventListener("click", close); |
| 1739 | const go = modal.querySelector("#tripGuardGo"); |
| 1744 | return {backdrop, modal}; |
| 1748 | const {backdrop, modal} = ensureModal(); |
| 1750 | modal.classList.add("show"); |

## 7) app.py Fonksiyonel Diff
_Kritik app.py fonksiyonlarında normalize edilmiş fonksiyonel diff yok._

## 8) Dosya Normalize Diff
### templates/seats.html
```diff
--- WEB normalized templates/seats.html
+++ ANDROID normalized templates/seats.html
@@ -11,9 +11,8 @@
 <link rel="stylesheet" href="/static/seats/patches/modal-bottom-nav-autohide.css?v=1">
 <link rel="stylesheet" href="/static/seats/patches/manual-ticket-system.css?v=1">
 <link rel="stylesheet" href="/static/seats/patches/top-sound-toggle.css?v=1">
 <link rel="stylesheet" href="/static/seats/patches/seat-simple-ui-pack.css?v=1">
-<link rel="stylesheet" href="/static/seats/patches/unified-seat-deck-report-style.css?v=seat-smaller-removed-2">
 <link rel="stylesheet" href="/static/seats/patches/mobile-performance-fix.css?v=2">
 <link rel="stylesheet" href="/static/seats/patches/fab-sheet-solid-fix.css?v=1">
 <link rel="stylesheet" href="/static/seats/patches/seat-label-ghost-clean.css?v=1">
 <div class="seats-shell">
```

### templates/index.html
```diff
--- WEB normalized templates/index.html
+++ ANDROID normalized templates/index.html
@@ -810,91 +810,8 @@
 }
 .arrow{
 font-size:24px !important;
 }
-}
-</style>
-<link id="home-font-barlow-settings" href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@400;600;700;800&family=Barlow:wght@400;500;600;700&display=swap" rel="stylesheet">
-<style id="home-font-match-settings">
-:root{
---font-display:'Barlow Condensed',system-ui,-apple-system,"Segoe UI",Arial,sans-serif;
---font-body:'Barlow',system-ui,-apple-system,"Segoe UI",Arial,sans-serif;
-}
-html,
-body{
-font-family:var(--font-body) !important;
--webkit-font-smoothing:antialiased;
-text-rendering:geometricPrecision;
-}
-body,
-button,
-input,
-select,
-textarea,
-a{
-font-family:var(--font-body) !important;
-}
-h1,
-h2,
-h3,
-h4,
-.hero-title,
-.brand-title,
-.app-title,
-.page-title,
-.section-title,
-.menu-title,
-.quick-title,
-.quick-card-title,
-.card-title,
-.tile-title,
-.status-title,
-.route-title,
-.action-title,
-.panel-title,
-.title,
-.big-title{
-font-family:var(--font-display) !important;
-font-weight:800;
-letter-spacing:.01em;
-}
-.menu-item,
-.quick-card,
-.quick-item,
-.btn,
-.button,
-.primary-btn,
-.secondary-btn,
-.back-btn{
-font-family:var(--font-display) !important;
-font-weight:800;
-letter-spacing:.02em;
-}
-p,
-.muted,
-.sub,
-.desc,
-.menu-desc,
-.quick-desc,
-.card-desc,
-.tile-desc,
-.status-desc,
-.small,
-.label,
-.meta,
-.hint{
-font-family:var(--font-body) !important;
-}
-</style>
-<style id="route-sheet-no-flash-fix">
-/* Route picker ilk render parlamasını engeller */
-#routeSheet[hidden],
-#routeSheetBackdrop[hidden]{
-display:none !important;
-}
-#routeSheet:not(.show),
-#routeSheetBackdrop:not(.show){
-display:none !important;
 }
 </style>
 </head>
 <body>
@@ -916,10 +833,10 @@
 <option value="{{ current_route }}">{{ current_route }}</option>
 {% endif %}
 </select>
 </div>
-<div class="route-sheet-backdrop" id="routeSheetBackdrop" hidden aria-hidden="true"></div>
-<section class="route-sheet" id="routeSheet" hidden aria-hidden="true">
+<div class="route-sheet-backdrop" id="routeSheetBackdrop"></div>
+<section class="route-sheet" id="routeSheet" aria-hidden="true">
 <div class="route-sheet-handle"></div>
 <div class="route-sheet-head">
 <div>
 <div class="route-sheet-kicker">Aktif hat seçimi</div>
@@ -1599,107 +1516,6 @@
 }, true);
 }
 })();
 </script>
-<script id="active-route-lock-final">
-(function(){
-const HAS_ACTIVE_TRIP = {% if active_trip is defined and active_trip %}true{% else %}false{% endif %};
-const ACTIVE_TRIP_ROUTE = {% if active_trip is defined and active_trip %}{{ active_trip.route|tojson }}{% else %}""{% endif %};
-if(!HAS_ACTIVE_TRIP) return;
-const routeBtn = document.getElementById("routePickerBtn");
-const routeText = document.getElementById("routePickerText");
-const routeSelect = document.getElementById("homeRouteSelect");
-const startLink = document.getElementById("homeTripStart");
-const continueLink =
-Array.from(document.querySelectorAll(".hero-link"))[1] ||
-document.querySelector('a[href*="continue"]') ||
-document.querySelector('a[href*="seats"]');
-const sheet = document.getElementById("routeSheet");
-const backdrop = document.getElementById("routeSheetBackdrop");
-function hardCloseRouteSheet(){
-if(sheet){
-sheet.classList.remove("show");
-sheet.hidden = true;
-sheet.setAttribute("aria-hidden", "true");
-}
-if(backdrop){
-backdrop.classList.remove("show");
-backdrop.hidden = true;
-backdrop.setAttribute("aria-hidden", "true");
-}
-}
-function forceActiveRouteText(){
-if(!ACTIVE_TRIP_ROUTE) return;
-if(routeText) routeText.textContent = ACTIVE_TRIP_ROUTE;
-if(routeSelect){
-const opt = Array.from(routeSelect.options || []).find(o => o.value === ACTIVE_TRIP_ROUTE);
-if(opt) routeSelect.value = ACTIVE_TRIP_ROUTE;
-}
-try{
-localStorage.setItem("homeSelectedRoute", ACTIVE_TRIP_ROUTE);
-}catch(_){}
-}
-function ensureModal(){
-let bd = document.getElementById("tripGuardBackdrop");
-let modal = document.getElementById("tripGuardModal");
-if(bd && modal) return {bd, modal};
-bd = document.createElement("div");
-bd.id = "tripGuardBackdrop";
-bd.className = "trip-guard-backdrop";
-modal = document.createElement("section");
-modal.id = "tripGuardModal";
-modal.className = "trip-guard-modal";
-modal.innerHTML = `
-<div class="trip-guard-icon">⚠️</div>
-<h2>Aktif sefer var</h2>
-<p>Yeni sefer başlatmadan önce mevcut seferi devam ettirmen veya seferi sonlandırman gerekir.</p>
-<div class="trip-guard-actions">
-<a class="trip-guard-go" id="tripGuardGo" href="#">Devam eden sefere git</a>
-<button class="trip-guard-ok" id="tripGuardOk" type="button">Tamam</button>
-</div>
-`;
-document.body.appendChild(bd);
-document.body.appendChild(modal);
-function close(){
-bd.classList.remove("show");
-modal.classList.remove("show");
-}
-bd.addEventListener("click", close);
-modal.querySelector("#tripGuardOk")?.addEventListener("click", close);
-const go = modal.querySelector("#tripGuardGo");
-if(go && continueLink){
-go.href = continueLink.getAttribute("href") || "/continue-trip";
-}
-return {bd, modal};
-}
-function showGuard(){
-hardCloseRouteSheet();
-forceActiveRouteText();
-const {bd, modal} = ensureModal();
-bd.classList.add("show");
-modal.classList.add("show");
-}
-forceActiveRouteText();
-hardCloseRouteSheet();
-if(startLink){
-startLink.classList.add("active-trip-locked");
-startLink.setAttribute("aria-disabled", "true");
-}
-/*
-En son kilit:
-Aktif sefer varken üstteki hat seçici AÇILMAYACAK.
-Tıklanınca 2. fotoğraftaki aktif sefer uyarısı açılacak.
-*/
-document.addEventListener("click", function(e){
-const hitRoute = e.target.closest && e.target.closest("#routePickerBtn");
-if(hitRoute){
-e.preventDefault();
-e.stopPropagation();
-e.stopImmediatePropagation();
-showGuard();
-return false;
-}
-}, true);
-})();
-</script>
 </body>
 </html>
```

### templates/trip_report.html
```diff
--- WEB normalized templates/trip_report.html
+++ ANDROID normalized templates/trip_report.html
@@ -983,292 +983,5 @@
 box.innerHTML = `<div class="embedded-archive-empty">Arşiv listesi yüklenemedi.</div>`;
 });
 })();
 </script>
-<style id="trip-report-top-premium-v1">
-@import url("https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@400;600;700;800&family=Barlow:wght@400;500;600;700&display=swap");
-.report-wrap{
-max-width:1040px;
-padding-top:18px;
-font-family:'Barlow',system-ui,-apple-system,"Segoe UI",Arial,sans-serif;
-}
-.report-wrap > .hero{
-position:relative;
-overflow:hidden;
-border-radius:28px;
-padding:26px 22px;
-background:linear-gradient(160deg,#0e1624 0%,#0d0f14 62%) !important;
-border:1px solid rgba(255,255,255,.08);
-box-shadow:0 24px 70px rgba(0,0,0,.42);
-}
-.report-wrap > .hero::before{
-content:"";
-position:absolute;
-top:-70px;
-right:-55px;
-width:260px;
-height:260px;
-border-radius:50%;
-background:radial-gradient(circle,rgba(59,139,255,.22),transparent 70%);
-pointer-events:none;
-}
-.report-wrap > .hero::after{
-content:"";
-position:absolute;
-left:0;
-right:0;
-bottom:0;
-height:1px;
-background:linear-gradient(90deg,transparent,#3b8bff,transparent);
-opacity:.45;
-}
-.report-wrap > .hero h1{
-position:relative;
-margin:0 0 8px;
-font-family:'Barlow Condensed',system-ui,-apple-system,"Segoe UI",Arial,sans-serif;
-font-size:54px;
-line-height:.95;
-font-weight:800;
-letter-spacing:-.02em;
-color:#e8edf5;
-}
-.report-wrap > .hero h1::before{
-content:"RAPORLAR";
-display:flex;
-align-items:center;
-gap:7px;
-margin-bottom:10px;
-font-family:'Barlow Condensed',system-ui,-apple-system,"Segoe UI",Arial,sans-serif;
-font-size:11px;
-line-height:1;
-font-weight:800;
-letter-spacing:.18em;
-color:#3b8bff;
-}
-.report-wrap > .hero .muted{
-position:relative;
-max-width:760px;
-color:rgba(232,237,245,.56);
-font-size:17px;
-font-weight:650;
-line-height:1.35;
-}
-.report-wrap > .hero .actions{
-position:relative;
-display:grid;
-grid-template-columns:repeat(4,1fr);
-gap:10px;
-margin-top:18px;
-}
-.report-wrap > .hero .btn{
-min-height:56px;
-border-radius:18px;
-padding:0 12px;
-border:1px solid rgba(255,255,255,.08);
-background:rgba(255,255,255,.035);
-color:#e8edf5;
-display:flex;
-align-items:center;
-justify-content:center;
-text-align:center;
-font-family:'Barlow Condensed',system-ui,-apple-system,"Segoe UI",Arial,sans-serif;
-font-size:18px;
-font-weight:800;
-letter-spacing:.02em;
-box-shadow:none;
-}
-.report-wrap > .hero .btn.blue{
-background:linear-gradient(145deg,#38bdf8,#2563eb);
-border-color:rgba(59,139,255,.35);
-box-shadow:0 16px 34px rgba(37,99,235,.24);
-}
-.report-wrap > .hero .btn.green{
-background:linear-gradient(145deg,#22c55e,#15803d);
-border-color:rgba(48,217,136,.32);
-box-shadow:0 16px 34px rgba(22,163,74,.20);
-}
-.report-wrap > .summary-grid{
-display:grid;
-grid-template-columns:repeat(4,1fr);
-gap:12px;
-margin:14px 0;
-}
-.report-wrap > .summary-grid > .sum-card{
-position:relative;
-overflow:hidden;
-min-height:112px;
-border-radius:22px;
-padding:16px;
-background:#181c27;
-border:1px solid rgba(255,255,255,.075);
-box-shadow:0 18px 55px rgba(0,0,0,.24);
-}
-.report-wrap > .summary-grid > .sum-card::before{
-content:"";
-position:absolute;
-top:-36px;
-right:-36px;
-width:96px;
-height:96px;
-border-radius:50%;
-background:radial-gradient(circle,rgba(59,139,255,.16),transparent 70%);
-}
-.report-wrap > .summary-grid > .sum-card .k{
-position:relative;
-font-size:13px;
-color:rgba(232,237,245,.52);
-font-weight:750;
-line-height:1.25;
-}
-.report-wrap > .summary-grid > .sum-card .v{
-position:relative;
-margin-top:10px;
-font-family:'Barlow Condensed',system-ui,-apple-system,"Segoe UI",Arial,sans-serif;
-font-size:46px;
-line-height:.9;
-font-weight:800;
-color:#e8edf5;
-letter-spacing:-.01em;
-}
-.report-wrap > .summary-grid > .sum-card:nth-child(1) .v{ color:#9af2c8; }
-.report-wrap > .summary-grid > .sum-card:nth-child(2) .v{ color:#ffb1b1; }
-.report-wrap > .summary-grid > .sum-card:nth-child(3) .v{ color:#d9b3ff; }
-.report-wrap > .summary-grid > .sum-card:nth-child(4) .v{ color:#a9ccff; }
-@media(max-width:720px){
-.report-wrap > .hero h1{
-font-size:48px;
-}
-.report-wrap > .hero .actions{
-grid-template-columns:1fr 1fr;
-}
-.report-wrap > .summary-grid{
-grid-template-columns:1fr 1fr;
-}
-}
-@media(max-width:390px){
-.report-wrap{
-padding-left:12px;
-padding-right:12px;
-}
-.report-wrap > .hero{
-padding:24px 18px;
-}
-.report-wrap > .hero h1{
-font-size:44px;
-}
-.report-wrap > .hero .btn{
-min-height:54px;
-font-size:17px;
-}
-.report-wrap > .summary-grid > .sum-card{
-min-height:104px;
-padding:15px;
-}
-.report-wrap > .summary-grid > .sum-card .v{
-font-size:40px;
-}
-}
-</style>
-<style id="trip-report-section-tiny-v1">
-.report-wrap > .section-card{
-position:relative;
-overflow:hidden;
-margin-top:12px;
-border-radius:22px;
-padding:10px;
-background:
-radial-gradient(circle at 12% 0%,rgba(59,139,255,.08),transparent 28%),
-linear-gradient(160deg,#111827 0%,#0b1220 100%) !important;
-border:1px solid rgba(255,255,255,.075);
-box-shadow:0 16px 46px rgba(0,0,0,.24);
-}
-.report-wrap > .section-card::before{
-content:"";
-position:absolute;
-top:-90px;
-right:-80px;
-width:170px;
-height:170px;
-border-radius:50%;
-background:radial-gradient(circle,rgba(59,139,255,.10),transparent 70%);
-pointer-events:none;
-}
-.report-wrap > .section-card > *{
-position:relative;
-}
-.report-wrap .section-head{
-display:grid;
... DIFF KESİLDİ toplam diff satırı: 295
```

### templates/report_archive.html
```diff
--- WEB normalized templates/report_archive.html
+++ ANDROID normalized templates/report_archive.html
@@ -1,436 +1,87 @@
-<!doctype html>
-<html lang="tr">
-<head>
-<meta charset="utf-8">
-<meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
-<title>Sefer Rapor Arşivi</title>
-<link href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@400;600;700;800&family=Barlow:wght@400;500;600;700&display=swap" rel="stylesheet">
+{% extends "base.html" %}
+{% block content %}
 <style>
-:root{
---bg:#0d0f14;
---bg-row:#181c27;
---bg-hover:#1e2333;
---border:rgba(255,255,255,.07);
---border-act:rgba(255,255,255,.14);
---text:#e8edf5;
---text-sub:rgba(232,237,245,.54);
---text-dim:rgba(232,237,245,.32);
---accent:#3b8bff;
---amber:#f5a623;
---green:#30d988;
---red:#ff4f4f;
---font-display:'Barlow Condensed',system-ui,-apple-system,"Segoe UI",Arial,sans-serif;
---font-body:'Barlow',system-ui,-apple-system,"Segoe UI",Arial,sans-serif;
---r-card:20px;
+body{
+background:#06101c;
+color:#eaf2ff;
+font-family:system-ui,-apple-system,Segoe UI,Roboto,Arial,sans-serif;
 }
-*,*::before,*::after{
-box-sizing:border-box;
-margin:0;
-padding:0;
-}
-html,body{
-min-height:100%;
-background:var(--bg);
-color:var(--text);
-font-family:var(--font-body);
--webkit-font-smoothing:antialiased;
-}
-body::before{
-content:"";
-position:fixed;
-inset:0;
-background-image:url("data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)' opacity='0.04'/%3E%3C/svg%3E");
-pointer-events:none;
-z-index:0;
-}
-.page{
-position:relative;
-z-index:1;
-max-width:480px;
-min-height:100vh;
+.wrap{
+max-width:900px;
 margin:0 auto;
-padding:0 0 40px;
+padding:18px 12px 42px;
 }
 .hero{
-position:relative;
-overflow:hidden;
-padding:52px 24px 32px;
-background:linear-gradient(160deg,#0e1624 0%,#0d0f14 62%);
-border-bottom:1px solid var(--border);
+background:linear-gradient(145deg,rgba(37,99,235,.24),rgba(15,23,42,.96));
+border:1px solid rgba(148,163,184,.22);
+border-radius:26px;
+padding:18px;
+box-shadow:0 18px 55px rgba(0,0,0,.42);
+margin-bottom:14px;
 }
-.hero::before{
-content:"";
-position:absolute;
-top:-60px;
-right:-40px;
-width:260px;
-height:260px;
-border-radius:50%;
-background:radial-gradient(circle,rgba(59,139,255,.18) 0%,transparent 70%);
-pointer-events:none;
+h1{
+margin:0 0 8px;
+font-size:32px;
 }
-.hero::after{
-content:"";
-position:absolute;
-left:0;
-right:0;
-bottom:0;
-height:1px;
-background:linear-gradient(90deg,transparent,var(--accent),transparent);
-opacity:.45;
+.muted{
+color:rgba(226,232,240,.65);
 }
-.hero-tag{
-position:relative;
-display:inline-flex;
-align-items:center;
-gap:7px;
-font-family:var(--font-display);
-font-size:11px;
-font-weight:800;
-letter-spacing:.18em;
-text-transform:uppercase;
-color:var(--accent);
+.item{
+background:rgba(15,23,42,.78);
+border:1px solid rgba(148,163,184,.18);
+border-radius:20px;
+padding:14px;
 margin-bottom:10px;
-opacity:0;
-animation:fadeUp .5s .05s forwards;
 }
-.hero-tag::before{
-content:"";
-width:24px;
-height:1px;
-background:var(--accent);
-display:block;
-}
-.hero h1{
-position:relative;
-font-family:var(--font-display);
-font-size:54px;
-font-weight:800;
-letter-spacing:-.02em;
-line-height:.95;
-color:var(--text);
-opacity:0;
-animation:fadeUp .5s .12s forwards;
-}
-.hero h1 span{
-display:block;
-max-width:370px;
+.title{
 font-size:20px;
-font-weight:600;
-color:var(--text-sub);
-margin-top:8px;
-line-height:1.32;
-}
-.content{
-padding:24px 16px 0;
-display:grid;
-gap:12px;
-}
-.summary{
-display:grid;
-grid-template-columns:1fr auto;
-align-items:center;
-gap:14px;
-background:var(--bg-row);
-border:1px solid var(--border);
-border-radius:var(--r-card);
-padding:18px;
-box-shadow:0 20px 60px rgba(0,0,0,.22);
-opacity:0;
-animation:fadeUp .4s .16s forwards;
-}
-.summary-title{
-font-family:var(--font-display);
-font-size:28px;
-font-weight:800;
-line-height:1;
-}
-.summary-sub{
-margin-top:5px;
-color:var(--text-sub);
-font-size:14px;
-font-weight:600;
-line-height:1.35;
-}
-.summary-count{
-min-width:64px;
-height:56px;
-border-radius:17px;
-display:grid;
-place-items:center;
-background:rgba(59,139,255,.12);
-color:#a9ccff;
-border:1px solid rgba(59,139,255,.24);
-font-family:var(--font-display);
-font-size:30px;
-font-weight:800;
-}
-.search-card{
-background:var(--bg-row);
-border:1px solid var(--border);
-border-radius:var(--r-card);
-padding:14px;
-opacity:0;
-animation:fadeUp .4s .22s forwards;
-}
-.search-box{
-position:relative;
-}
-.search-box input{
-width:100%;
-min-height:56px;
-border-radius:17px;
-border:1px solid var(--border);
-background:rgba(255,255,255,.035);
-color:var(--text);
-padding:0 16px 0 48px;
-outline:none;
-font-size:17px;
-font-weight:700;
-font-family:var(--font-body);
-}
... DIFF KESİLDİ toplam diff satırı: 498
```

### templates/settings.html
```diff
--- WEB normalized templates/settings.html
+++ ANDROID normalized templates/settings.html
@@ -1,509 +1,179 @@
-<!DOCTYPE html>
+<!doctype html>
 <html lang="tr">
 <head>
-<meta charset="UTF-8">
-<meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
+<meta charset="utf-8">
+<meta name="viewport" content="width=device-width, initial-scale=1">
 <title>Ayarlar</title>
-<link href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@400;600;700;800&family=Barlow:wght@400;500;600;700&display=swap" rel="stylesheet">
 <style>
-:root {
---bg:#0d0f14;
---bg-card:#13161e;
---bg-row:#181c27;
---bg-hover:#1e2333;
---border:rgba(255,255,255,.07);
---border-act:rgba(255,255,255,.14);
---text:#e8edf5;
---text-sub:rgba(232,237,245,.52);
---text-dim:rgba(232,237,245,.30);
---accent:#3b8bff;
---accent-glow:rgba(59,139,255,.22);
---amber:#f5a623;
---green:#30d988;
---red:#ff4f4f;
---purple:#a769ff;
---slate:#94a3b8;
---font-display:'Barlow Condensed',system-ui,-apple-system,"Segoe UI",Arial,sans-serif;
---font-body:'Barlow',system-ui,-apple-system,"Segoe UI",Arial,sans-serif;
---r-card:20px;
---r-row:14px;
+*{ box-sizing:border-box; }
+body{
+margin:0;
+min-height:100vh;
+background:
+radial-gradient(circle at 18% 0%, rgba(59,130,246,.16), transparent 34%),
+linear-gradient(180deg,#f8fbff,#eaf3ff);
+font-family:system-ui,-apple-system,"Segoe UI",Roboto,Arial,sans-serif;
+color:#0f172a;
 }
-*,*::before,*::after{
-box-sizing:border-box;
+.settings-shell{
+width:min(94vw,720px);
+margin:18px auto 28px;
+padding:16px;
+border-radius:30px;
+background:linear-gradient(180deg,rgba(255,255,255,.96),rgba(241,248,255,.96));
+border:1px solid rgba(255,255,255,.82);
+box-shadow:0 28px 80px rgba(15,23,42,.18);
+}
+.settings-hero{
+padding:24px 20px;
+border-radius:26px;
+background:linear-gradient(145deg,#2563eb,#06b6d4);
+color:#fff;
+box-shadow:0 18px 38px rgba(37,99,235,.22);
+margin-bottom:14px;
+}
+.settings-hero h1{
 margin:0;
-padding:0;
+font-size:34px;
+line-height:1;
+font-weight:950;
 }
-html,body{
-min-height:100%;
-background:var(--bg);
-color:var(--text);
-font-family:var(--font-body);
--webkit-font-smoothing:antialiased;
+.settings-hero p{
+margin:8px 0 0;
+font-size:15px;
+font-weight:700;
+color:rgba(255,255,255,.88);
 }
-body::before{
-content:"";
-position:fixed;
-inset:0;
-background-image:url("data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)' opacity='0.04'/%3E%3C/svg%3E");
-pointer-events:none;
-z-index:0;
+.settings-list{
+overflow:hidden;
+border-radius:24px;
+background:#fff;
+border:1px solid #e5edf6;
+box-shadow:0 14px 34px rgba(15,23,42,.10);
 }
-.page{
-position:relative;
-z-index:1;
-max-width:480px;
-min-height:100vh;
-margin:0 auto;
-padding:0 0 40px;
+.settings-item{
+min-height:72px;
+display:grid;
+grid-template-columns:46px 1fr 30px;
+align-items:center;
+gap:12px;
+padding:12px 14px;
+border-bottom:1px solid #e5edf6;
+text-decoration:none;
+color:#10203a;
 }
-.hero{
-position:relative;
-overflow:hidden;
-padding:52px 24px 32px;
-background:linear-gradient(160deg,#0e1624 0%,#0d0f14 62%);
-border-bottom:1px solid var(--border);
-}
-.hero::before{
-content:"";
-position:absolute;
-top:-60px;
-right:-40px;
-width:260px;
-height:260px;
-border-radius:50%;
-background:radial-gradient(circle,rgba(59,139,255,.18) 0%,transparent 70%);
-pointer-events:none;
-}
-.hero::after{
-content:"";
-position:absolute;
-left:0;
-right:0;
-bottom:0;
-height:1px;
-background:linear-gradient(90deg,transparent,var(--accent),transparent);
-opacity:.45;
-}
-.hero-tag{
-position:relative;
-display:inline-flex;
-align-items:center;
-gap:7px;
-font-family:var(--font-display);
-font-size:11px;
-font-weight:800;
-letter-spacing:.18em;
-text-transform:uppercase;
-color:var(--accent);
-margin-bottom:10px;
-opacity:0;
-animation:fadeUp .5s .05s forwards;
-}
-.hero-tag::before{
-content:"";
-width:24px;
-height:1px;
-background:var(--accent);
-display:block;
-}
-.hero h1{
-position:relative;
-font-family:var(--font-display);
-font-size:54px;
-font-weight:800;
-letter-spacing:-.02em;
-line-height:.95;
-color:var(--text);
-opacity:0;
-animation:fadeUp .5s .12s forwards;
-}
-.hero h1 span{
-display:block;
-max-width:340px;
-font-size:20px;
-font-weight:600;
-letter-spacing:.01em;
-color:var(--text-sub);
-margin-top:8px;
-line-height:1.32;
-}
-.content{
-padding:24px 16px 0;
-display:flex;
-flex-direction:column;
-gap:8px;
-}
-.group-label{
-font-family:var(--font-display);
-font-size:11px;
-font-weight:800;
-letter-spacing:.16em;
-text-transform:uppercase;
-color:var(--text-dim);
-padding:16px 4px 6px;
-opacity:0;
-animation:fadeUp .4s forwards;
-}
-.card-group{
-background:var(--bg-row);
-border:1px solid var(--border);
-border-radius:var(--r-card);
-overflow:hidden;
-opacity:0;
-animation:fadeUp .4s forwards;
-}
-.setting-row{
-position:relative;
-display:flex;
-align-items:center;
-gap:14px;
-min-height:76px;
-padding:14px 16px;
-background:transparent;
-border:none;
... DIFF KESİLDİ toplam diff satırı: 658
```


## 9) Karar Notu

Bu rapor sadece tespit içindir. Hiçbir dosya değiştirilmedi.

Okuma mantığı:
- `app.py` kritik fonksiyonları normalize AYNI çıkarsa, kayıt API tarafında web/android farkı yoktur.
- `seats.js` zaten WEB/ANDROID AYNI çıktı. Bu yüzden koltuk modal kayıt sorunu büyük ihtimalle dosya senkron farkından değil; olay sırası, tarayıcı cache, modal kapanma/submit çakışması veya API cevabı yönetiminden olabilir.
- `templates/seats.html` farkı sadece CSS/link ise işlevsel değil görsel kabul edilir.
