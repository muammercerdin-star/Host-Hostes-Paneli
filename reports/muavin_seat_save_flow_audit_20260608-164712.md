# Muavin Asistanı Koltuk Kaydetme Akışı Audit V6

- Tarih: `20260608-164712`
- Bu rapor sadece tespittir. Dosya değiştirmez.

## 1) İncelenen Dosyalar
| Dosya etiketi | Durum | Yol | Satır |
| --- | --- | --- | --- |
| WEB seats.html | VAR | templates/seats.html | 1091 |
| WEB modals.html | VAR | templates/seats_parts/modals.html | 196 |
| WEB seats.js | VAR | static/seats/seats.js | 2960 |
| WEB standing.js | VAR | static/seats/standing.js | 246 |
| WEB manual-ticket-system.js | VAR | static/seats/patches/manual-ticket-system.js | 228 |
| WEB seat-simple-ui-pack.js | VAR | static/seats/patches/seat-simple-ui-pack.js | 279 |
| WEB modal-bottom-nav-autohide.js | VAR | static/seats/patches/modal-bottom-nav-autohide.js | 150 |
| ANDROID seats.html | VAR | android_app/app/src/main/python/templates/seats.html | 1090 |
| ANDROID modals.html | VAR | android_app/app/src/main/python/templates/seats_parts/modals.html | 196 |
| ANDROID seats.js | VAR | android_app/app/src/main/python/static/seats/seats.js | 2960 |
| ANDROID standing.js | VAR | android_app/app/src/main/python/static/seats/standing.js | 246 |
| ANDROID manual-ticket-system.js | VAR | android_app/app/src/main/python/static/seats/patches/manual-ticket-system.js | 228 |
| ANDROID seat-simple-ui-pack.js | VAR | android_app/app/src/main/python/static/seats/patches/seat-simple-ui-pack.js | 279 |
| ANDROID modal-bottom-nav-autohide.js | VAR | android_app/app/src/main/python/static/seats/patches/modal-bottom-nav-autohide.js | 150 |

## 2) Fetch Endpointleri
| Endpoint | Geçiş |
| --- | --- |
| /api/speedlimit?lat=${lat}&lng=${lng} | 2 |

## 3) Fetch Satırları
| Dosya | Satır | Endpoint |
| --- | --- | --- |
| WEB seats.js | 2586 | /api/speedlimit?lat=${lat}&lng=${lng} |
| ANDROID seats.js | 2586 | /api/speedlimit?lat=${lat}&lng=${lng} |

## 4) Event Listener / Submit İzleri
| Dosya | Satır | Event |
| --- | --- | --- |
| WEB seats.html | 530 | click |
| WEB seats.html | 538 | click |
| WEB seats.html | 586 | click |
| WEB seats.html | 605 | resize |
| WEB seats.html | 606 | orientationchange |
| WEB seats.html | 621 | DOMContentLoaded |
| WEB seats.html | 888 | click |
| WEB seats.html | 900 | DOMContentLoaded |
| WEB seats.html | 934 | click |
| WEB seats.html | 965 | driveModeChanged |
| WEB seats.html | 966 | resize |
| WEB seats.html | 970 | DOMContentLoaded |
| WEB seats.html | 1055 | click |
| WEB seats.html | 1071 | click |
| WEB seats.html | 1081 | DOMContentLoaded |
| WEB seats.js | 95 | click |
| WEB seats.js | 100 | change |
| WEB seats.js | 1190 | click |
| WEB seats.js | 2177 | click |
| WEB seats.js | 2443 | click |
| WEB seats.js | 2490 | click |
| WEB seats.js | 2672 | click |
| WEB seats.js | 2808 | keydown |
| WEB seats.js | 2821 | click |
| WEB seats.js | 2833 | click |
| WEB seats.js | 2955 | beforeunload |
| WEB standing.js | 165 | click |
| WEB manual-ticket-system.js | 202 | DOMContentLoaded |
| WEB manual-ticket-system.js | 207 | load |
| WEB manual-ticket-system.js | 209 | click |
| WEB manual-ticket-system.js | 215 | change |
| WEB seat-simple-ui-pack.js | 61 | click |
| WEB seat-simple-ui-pack.js | 80 | DOMContentLoaded |
| WEB seat-simple-ui-pack.js | 193 | DOMContentLoaded |
| WEB seat-simple-ui-pack.js | 259 | click |
| WEB seat-simple-ui-pack.js | 265 | resize |
| WEB seat-simple-ui-pack.js | 266 | orientationchange |
| WEB seat-simple-ui-pack.js | 274 | DOMContentLoaded |
| WEB modal-bottom-nav-autohide.js | 128 | click |
| WEB modal-bottom-nav-autohide.js | 134 | input |
| WEB modal-bottom-nav-autohide.js | 135 | change |
| WEB modal-bottom-nav-autohide.js | 136 | resize |
| WEB modal-bottom-nav-autohide.js | 137 | scroll |
| ANDROID seats.html | 529 | click |
| ANDROID seats.html | 537 | click |
| ANDROID seats.html | 585 | click |
| ANDROID seats.html | 604 | resize |
| ANDROID seats.html | 605 | orientationchange |
| ANDROID seats.html | 620 | DOMContentLoaded |
| ANDROID seats.html | 887 | click |
| ANDROID seats.html | 899 | DOMContentLoaded |
| ANDROID seats.html | 933 | click |
| ANDROID seats.html | 964 | driveModeChanged |
| ANDROID seats.html | 965 | resize |
| ANDROID seats.html | 969 | DOMContentLoaded |
| ANDROID seats.html | 1054 | click |
| ANDROID seats.html | 1070 | click |
| ANDROID seats.html | 1080 | DOMContentLoaded |
| ANDROID seats.js | 95 | click |
| ANDROID seats.js | 100 | change |
| ANDROID seats.js | 1190 | click |
| ANDROID seats.js | 2177 | click |
| ANDROID seats.js | 2443 | click |
| ANDROID seats.js | 2490 | click |
| ANDROID seats.js | 2672 | click |
| ANDROID seats.js | 2808 | keydown |
| ANDROID seats.js | 2821 | click |
| ANDROID seats.js | 2833 | click |
| ANDROID seats.js | 2955 | beforeunload |
| ANDROID standing.js | 165 | click |
| ANDROID manual-ticket-system.js | 202 | DOMContentLoaded |
| ANDROID manual-ticket-system.js | 207 | load |
| ANDROID manual-ticket-system.js | 209 | click |
| ANDROID manual-ticket-system.js | 215 | change |
| ANDROID seat-simple-ui-pack.js | 61 | click |
| ANDROID seat-simple-ui-pack.js | 80 | DOMContentLoaded |
| ANDROID seat-simple-ui-pack.js | 193 | DOMContentLoaded |
| ANDROID seat-simple-ui-pack.js | 259 | click |
| ANDROID seat-simple-ui-pack.js | 265 | resize |
| ANDROID seat-simple-ui-pack.js | 266 | orientationchange |
| ANDROID seat-simple-ui-pack.js | 274 | DOMContentLoaded |
| ANDROID modal-bottom-nav-autohide.js | 128 | click |
| ANDROID modal-bottom-nav-autohide.js | 134 | input |
| ANDROID modal-bottom-nav-autohide.js | 135 | change |
| ANDROID modal-bottom-nav-autohide.js | 136 | resize |
| ANDROID modal-bottom-nav-autohide.js | 137 | scroll |

## 5) Koltuk/Modal/Kaydet Query Selector İzleri
| Dosya | Satır | Selector/ID |
| --- | --- | --- |
| WEB seats.html | 501 | .route-strip-shell |
| WEB seats.html | 525 | dmaAiBtn |
| WEB seats.html | 526 | dmaEndBtn |
| WEB seats.html | 914 | voiceSeatFilled |
| WEB seats.html | 915 | voiceSeatEmpty |
| WEB seats.html | 928 | btnDeckAIDrive |
| WEB seats.html | 929 | btnDeckAI |
| WEB seats.html | 998 | seatSimpleModeToggle |
| WEB seats.html | 1058 | .tab-btn[data-tab= |
| WEB seats.js | 2452 | .tab-btn[data-tab= |
| WEB manual-ticket-system.js | 48 | seat- |
| WEB manual-ticket-system.js | 94 | .seat[id^= |
| WEB seat-simple-ui-pack.js | 37 | seatSimpleModeToggle |
| WEB seat-simple-ui-pack.js | 52 | seatSimpleModeToggle |
| WEB seat-simple-ui-pack.js | 54 | .seats-shell |
| WEB modal-bottom-nav-autohide.js | 109 | .muavin-hidden-bottom-nav-by-modal |
| ANDROID seats.html | 500 | .route-strip-shell |
| ANDROID seats.html | 524 | dmaAiBtn |
| ANDROID seats.html | 525 | dmaEndBtn |
| ANDROID seats.html | 913 | voiceSeatFilled |
| ANDROID seats.html | 914 | voiceSeatEmpty |
| ANDROID seats.html | 927 | btnDeckAIDrive |
| ANDROID seats.html | 928 | btnDeckAI |
| ANDROID seats.html | 997 | seatSimpleModeToggle |
| ANDROID seats.html | 1057 | .tab-btn[data-tab= |
| ANDROID seats.js | 2452 | .tab-btn[data-tab= |
| ANDROID manual-ticket-system.js | 48 | seat- |
| ANDROID manual-ticket-system.js | 94 | .seat[id^= |
| ANDROID seat-simple-ui-pack.js | 37 | seatSimpleModeToggle |
| ANDROID seat-simple-ui-pack.js | 52 | seatSimpleModeToggle |
| ANDROID seat-simple-ui-pack.js | 54 | .seats-shell |
| ANDROID modal-bottom-nav-autohide.js | 109 | .muavin-hidden-bottom-nav-by-modal |

## 6) İlgili Fonksiyon Adayları
| Dosya | Satır | Fonksiyon |
| --- | --- | --- |
| WEB seats.html | 913 | syncDriveVoiceStats |
| WEB seats.js | 290 | persistStandingTotals |
| WEB seats.js | 297 | persistStandingItems |
| WEB seats.js | 610 | computeSeatCountsByStop |
| WEB seats.js | 618 | computeStandingCountsByStop |
| WEB seats.js | 893 | seatsForStop |
| WEB seats.js | 930 | updateStopSeatBadges |
| WEB seats.js | 941 | setSeatVisual |
| WEB seats.js | 970 | updateStats |
| WEB seats.js | 996 | renderQuickStandingList |
| WEB seats.js | 1376 | openModal |
| WEB seats.js | 1381 | closeModal |
| WEB seats.js | 1386 | openSeat |
| WEB seats.js | 1418 | closeSeat |
| WEB seats.js | 1424 | saveSeat |
| WEB seats.js | 1485 | clearSeatUI |
| WEB seats.js | 1512 | offloadSeat |
| WEB seats.js | 1551 | toggleSeatPick |
| WEB seats.js | 1592 | saveBulk |
| WEB seats.js | 1937 | saveCoord |
| WEB standing.js | 22 | saveCash |
| WEB standing.js | 66 | loadStandingTotals |
| WEB standing.js | 87 | loadStandingItems |
| WEB standing.js | 118 | renderStandingList |
| WEB standing.js | 168 | openStandingModal |
| WEB standing.js | 173 | closeStandingModal |
| WEB standing.js | 177 | removeStandingById |
| WEB standing.js | 205 | offloadStandingForStop |
| WEB manual-ticket-system.js | 34 | saveMap |
| WEB manual-ticket-system.js | 46 | seatEl |
| WEB manual-ticket-system.js | 63 | seatAssigned |
| WEB manual-ticket-system.js | 74 | seatSignature |
| WEB modal-bottom-nav-autohide.js | 23 | isWorkModalText |
| WEB modal-bottom-nav-autohide.js | 42 | workModalIsOpen |
| ANDROID seats.html | 912 | syncDriveVoiceStats |
| ANDROID seats.js | 290 | persistStandingTotals |
| ANDROID seats.js | 297 | persistStandingItems |
| ANDROID seats.js | 610 | computeSeatCountsByStop |
| ANDROID seats.js | 618 | computeStandingCountsByStop |
| ANDROID seats.js | 893 | seatsForStop |
| ANDROID seats.js | 930 | updateStopSeatBadges |
| ANDROID seats.js | 941 | setSeatVisual |
| ANDROID seats.js | 970 | updateStats |
| ANDROID seats.js | 996 | renderQuickStandingList |
| ANDROID seats.js | 1376 | openModal |
| ANDROID seats.js | 1381 | closeModal |
| ANDROID seats.js | 1386 | openSeat |
| ANDROID seats.js | 1418 | closeSeat |
| ANDROID seats.js | 1424 | saveSeat |
| ANDROID seats.js | 1485 | clearSeatUI |
| ANDROID seats.js | 1512 | offloadSeat |
| ANDROID seats.js | 1551 | toggleSeatPick |
| ANDROID seats.js | 1592 | saveBulk |
| ANDROID seats.js | 1937 | saveCoord |
| ANDROID standing.js | 22 | saveCash |
| ANDROID standing.js | 66 | loadStandingTotals |
| ANDROID standing.js | 87 | loadStandingItems |
| ANDROID standing.js | 118 | renderStandingList |
| ANDROID standing.js | 168 | openStandingModal |
| ANDROID standing.js | 173 | closeStandingModal |
| ANDROID standing.js | 177 | removeStandingById |
| ANDROID standing.js | 205 | offloadStandingForStop |
| ANDROID manual-ticket-system.js | 34 | saveMap |
| ANDROID manual-ticket-system.js | 46 | seatEl |
| ANDROID manual-ticket-system.js | 63 | seatAssigned |
| ANDROID manual-ticket-system.js | 74 | seatSignature |
| ANDROID modal-bottom-nav-autohide.js | 23 | isWorkModalText |
| ANDROID modal-bottom-nav-autohide.js | 42 | workModalIsOpen |

## 7) Aynı Dosya İçinde Duplicate ID
_Kayıt yok._

## 8) Koltuk/Modal/Kaydet ile İlgili ID'lerin Dosyalara Dağılımı
| ID | Dosya sayısı | Yerler |
| --- | --- | --- |
| approachModal | 2 | WEB modals.html(1), ANDROID modals.html(1) |
| btnBagAdd | 2 | WEB modals.html(1), ANDROID modals.html(1) |
| btnBagView | 2 | WEB modals.html(1), ANDROID modals.html(1) |
| btnDeckAI | 2 | WEB seats.html(1), ANDROID seats.html(1) |
| btnDeckAIDrive | 2 | WEB seats.html(1), ANDROID seats.html(1) |
| btnGeoWatch | 2 | WEB seats.html(1), ANDROID seats.html(1) |
| btnOffloadNowPane | 2 | WEB seats.html(1), ANDROID seats.html(1) |
| btnOpenRouteTab | 2 | WEB seats.html(1), ANDROID seats.html(1) |
| btnSaveCoord | 2 | WEB seats.html(1), ANDROID seats.html(1) |
| btnSeatClose | 2 | WEB modals.html(1), ANDROID modals.html(1) |
| btnSeatOffload | 2 | WEB modals.html(1), ANDROID modals.html(1) |
| btnSeatSave | 2 | WEB modals.html(1), ANDROID modals.html(1) |
| btnTriggerNow | 2 | WEB seats.html(1), ANDROID seats.html(1) |
| bulkModal | 2 | WEB modals.html(1), ANDROID modals.html(1) |
| bulkSave | 2 | WEB modals.html(1), ANDROID modals.html(1) |
| cashModal | 2 | WEB modals.html(1), ANDROID modals.html(1) |
| cashSave | 2 | WEB modals.html(1), ANDROID modals.html(1) |
| dmaAiBtn | 2 | WEB seats.html(1), ANDROID seats.html(1) |
| dmaEndBtn | 2 | WEB seats.html(1), ANDROID seats.html(1) |
| driveVoiceSeatCard | 2 | WEB seats.html(1), ANDROID seats.html(1) |
| openStandingModalBtn | 2 | WEB seats.html(1), ANDROID seats.html(1) |
| quickStandingList | 2 | WEB seats.html(1), ANDROID seats.html(1) |
| quickStandingMeta | 2 | WEB seats.html(1), ANDROID seats.html(1) |
| seat-simple-bottom-bar-script | 2 | WEB seats.html(1), ANDROID seats.html(1) |
| seatBackdrop | 2 | WEB modals.html(1), ANDROID modals.html(1) |
| seatModal | 2 | WEB modals.html(1), ANDROID modals.html(1) |
| seatSimpleBottomBar | 2 | WEB seats.html(1), ANDROID seats.html(1) |
| seatSimpleModeToggle | 2 | WEB seat-simple-ui-pack.js(1), ANDROID seat-simple-ui-pack.js(1) |
| seatSimpleOcc | 2 | WEB seat-simple-ui-pack.js(1), ANDROID seat-simple-ui-pack.js(1) |
| seatSimpleOpenDurak | 2 | WEB seats.html(1), ANDROID seats.html(1) |
| seatSimpleRoute | 2 | WEB seat-simple-ui-pack.js(1), ANDROID seat-simple-ui-pack.js(1) |
| seatSimpleSpeed | 2 | WEB seat-simple-ui-pack.js(1), ANDROID seat-simple-ui-pack.js(1) |
| seatSimpleStop | 2 | WEB seat-simple-ui-pack.js(1), ANDROID seat-simple-ui-pack.js(1) |
| seatSimpleSummary | 2 | WEB seat-simple-ui-pack.js(1), ANDROID seat-simple-ui-pack.js(1) |
| seatSimpleVoiceBtn | 2 | WEB seats.html(1), ANDROID seats.html(1) |
| seatTitle | 2 | WEB modals.html(1), ANDROID modals.html(1) |
| standingBackdrop | 2 | WEB modals.html(1), ANDROID modals.html(1) |
| standingBulkOff | 2 | WEB modals.html(1), ANDROID modals.html(1) |
| standingClose | 2 | WEB modals.html(1), ANDROID modals.html(1) |
| standingList | 2 | WEB modals.html(1), ANDROID modals.html(1) |
| standingModal | 2 | WEB modals.html(1), ANDROID modals.html(1) |
| standingSummary | 2 | WEB modals.html(1), ANDROID modals.html(1) |
| voiceSeatEmpty | 2 | WEB seats.html(1), ANDROID seats.html(1) |
| voiceSeatFilled | 2 | WEB seats.html(1), ANDROID seats.html(1) |
| voiceSeatMiniStats | 2 | WEB seats.html(1), ANDROID seats.html(1) |

## 9) Kritik Satır Taraması
| Dosya | Satır | İçerik |
| --- | --- | --- |
| WEB seats.html | 12 | <link rel="stylesheet" href="/static/seats/patches/modal-bottom-nav-autohide.css?v=1"> |
| WEB seats.html | 253 | <button class="btn accent" type="button" id="btnSaveCoord">Koordinatı Kaydet</button> |
| WEB seats.html | 336 | {% include "seats_parts/modals.html" %} |
| WEB seats.html | 342 | tripId: {{ trip['id'] \| tojson \| safe }}, |
| WEB seats.html | 376 | <script src="/static/seats/patches/modal-bottom-nav-autohide.js?v=1"></script> |
| WEB seats.html | 530 | ai.addEventListener("click", function(e){ |
| WEB seats.html | 531 | e.preventDefault(); |
| WEB seats.html | 538 | end.addEventListener("click", function(){ |
| WEB seats.html | 586 | btn.addEventListener("click", function(){ |
| WEB seats.html | 605 | window.addEventListener("resize", placeDock); |
| WEB seats.html | 606 | window.addEventListener("orientationchange", function(){ |
| WEB seats.html | 621 | document.addEventListener("DOMContentLoaded", boot); |
| WEB seats.html | 628 | {% include "seats_parts/finish_trip_modal.html" %} |
| WEB seats.html | 864 | document.body.classList.toggle("drive-mode", !!on); |
| WEB seats.html | 865 | document.documentElement.classList.toggle("drive-mode", !!on); |
| WEB seats.html | 888 | document.addEventListener("click", function(e){ |
| WEB seats.html | 892 | e.preventDefault(); |
| WEB seats.html | 900 | document.addEventListener("DOMContentLoaded", sync); |
| WEB seats.html | 934 | fakeBtn.addEventListener("click", function(e){ |
| WEB seats.html | 935 | e.preventDefault(); |
| WEB seats.html | 965 | window.addEventListener("driveModeChanged", syncDriveVoiceStats); |
| WEB seats.html | 966 | window.addEventListener("resize", syncDriveVoiceStats); |
| WEB seats.html | 970 | document.addEventListener("DOMContentLoaded", boot); |
| WEB seats.html | 994 | document.documentElement.classList.remove("seat-simple-mode"); |
| WEB seats.html | 995 | document.body.classList.remove("seat-simple-mode"); |
| WEB seats.html | 1055 | durak.addEventListener("click", function(){ |
| WEB seats.html | 1071 | voice.addEventListener("click", function(e){ |
| WEB seats.html | 1072 | e.preventDefault(); |
| WEB seats.html | 1081 | document.addEventListener("DOMContentLoaded", boot); |
| WEB modals.html | 1 | <div class="modal-backdrop" id="seatBackdrop"></div> |
| WEB modals.html | 2 | <div class="modal glass" id="seatModal"> |
| WEB modals.html | 69 | <div class="modal-actions"> |
| WEB modals.html | 70 | <button class="btn green" type="button" id="btnSeatSave">Kaydet</button> |
| WEB modals.html | 76 | <div class="modal-backdrop" id="bulkBackdrop"></div> |
| WEB modals.html | 77 | <div class="sheet-modal glass" id="bulkModal"> |
| WEB modals.html | 115 | <div class="modal-actions"> |
| WEB modals.html | 117 | <button class="btn primary" type="button" id="bulkSave">Kaydet</button> |
| WEB modals.html | 121 | <div class="modal-backdrop" id="cashBackdrop"></div> |
| WEB modals.html | 122 | <div class="sheet-modal glass" id="cashModal"> |
| WEB modals.html | 164 | <div class="modal-actions"> |
| WEB modals.html | 166 | <button class="btn primary" type="button" id="cashSave">Ekle</button> |
| WEB modals.html | 170 | <div class="modal-backdrop" id="approachBackdrop"></div> |
| WEB modals.html | 171 | <div class="sheet-modal glass" id="approachModal"> |
| WEB modals.html | 176 | <div class="modal-actions"> |
| WEB modals.html | 183 | <div class="modal-backdrop" id="standingBackdrop"></div> |
| WEB modals.html | 184 | <div class="sheet-modal glass" id="standingModal"> |
| WEB modals.html | 189 | <div class="modal-actions"> |
| WEB seats.js | 95 | if(el) el.addEventListener("click", fn); |
| WEB seats.js | 100 | if(el) el.addEventListener("change", fn); |
| WEB seats.js | 113 | function show(el){ |
| WEB seats.js | 117 | function hide(el){ |
| WEB seats.js | 130 | (window.SEATS_BOOT && window.SEATS_BOOT.tripId) \|\| |
| WEB seats.js | 131 | (typeof BOOT !== "undefined" && BOOT && BOOT.tripId) \|\| |
| WEB seats.js | 144 | // Hem trip_id değişince hem de hafıza şeması değişince eski durak akışı silinsin. |
| WEB seats.js | 192 | let currentSeat = null; |
| WEB seats.js | 264 | const res = await fetch(url, opt \|\| {}); |
| WEB seats.js | 455 | const url = `/api/route-schedule?route=${encodeURIComponent(ROUTE_NAME)}&direction=gidis&_=${Date.now()}`; |
| WEB seats.js | 564 | const j = await safeJsonFetch("/api/stops"); |
| WEB seats.js | 570 | const c = await safeJsonFetch("/api/coords"); |
| WEB seats.js | 729 | Object.keys(assigned \|\| {}).forEach(seatNo => { |
| WEB seats.js | 730 | if(!assigned[seatNo]) return; |
| WEB seats.js | 731 | if(norm(boardsMap[String(seatNo)] \|\| "") === key){ |
| WEB seats.js | 933 | $$(".seat").forEach(el => el.classList.remove("has-stop")); |
| WEB seats.js | 938 | if(el) el.classList.add("has-stop"); |
| WEB seats.js | 942 | function setSeatVisual(seatNo){ |
| WEB seats.js | 943 | const key = String(seatNo); |
| WEB seats.js | 944 | const el = $("#seat-" + seatNo); |
| WEB seats.js | 947 | el.classList.remove("male","female","isAssigned","has-service"); |
| WEB seats.js | 952 | if(isAssigned) el.classList.add("isAssigned"); |
| WEB seats.js | 953 | if(gender === "bay") el.classList.add("male"); |
| WEB seats.js | 954 | if(gender === "bayan") el.classList.add("female"); |
| WEB seats.js | 955 | if(serviceMap[key]) el.classList.add("has-service"); |
| WEB seats.js | 957 | const label = $("#label-" + seatNo); |
| WEB seats.js | 991 | standingCount > 0 ? standingCard.classList.add("pulse") : standingCard.classList.remove("pulse"); |
| WEB seats.js | 1063 | target.classList.add("route-focus-flash"); |
| WEB seats.js | 1064 | setTimeout(() => target.classList.remove("route-focus-flash"), 1200); |
| WEB seats.js | 1190 | item.addEventListener("click", () => { |
| WEB seats.js | 1377 | function openModal(backdropSel, modalSel){ |
| WEB seats.js | 1378 | show($(backdropSel)); |
| WEB seats.js | 1379 | show($(modalSel)); |
| WEB seats.js | 1382 | function closeModal(backdropSel, modalSel){ |
| WEB seats.js | 1383 | hide($(backdropSel)); |
| WEB seats.js | 1384 | hide($(modalSel)); |
| WEB seats.js | 1387 | function openSeat(seatNo){ |
| WEB seats.js | 1388 | currentSeat = seatNo; |
| WEB seats.js | 1389 | $$(".seat.selected").forEach(x => x.classList.remove("selected")); |
| WEB seats.js | 1391 | const seatEl = $("#seat-" + seatNo); |
| WEB seats.js | 1392 | if(seatEl) seatEl.classList.add("selected"); |
| WEB seats.js | 1394 | setText("#seatTitle", "Koltuk " + seatNo); |
| WEB seats.js | 1395 | setValue("#pickup", boardsMap[String(seatNo)] \|\| getSelectedStopName() \|\| ""); |
| WEB seats.js | 1396 | setValue("#dropoff", stopsMap[String(seatNo)] \|\| ""); |
| WEB seats.js | 1406 | const prevGender = genders[String(seatNo)] \|\| ""; |
| WEB seats.js | 1412 | if($("#service")) $("#service").checked = !!serviceMap[String(seatNo)]; |
| WEB seats.js | 1413 | setValue("#service_note", serviceNotes[String(seatNo)] \|\| ""); |
| WEB seats.js | 1416 | openModal("#seatBackdrop", "#seatModal"); |
| WEB seats.js | 1420 | currentSeat = null; |
| WEB seats.js | 1421 | closeModal("#seatBackdrop", "#seatModal"); |
| WEB seats.js | 1422 | $$(".seat.selected").forEach(x => x.classList.remove("selected")); |
| WEB seats.js | 1425 | async function saveSeat(){ |
| WEB seats.js | 1426 | if(!currentSeat) return; |
| WEB seats.js | 1428 | const wasAlreadyAssigned = !!assigned[String(currentSeat)]; |
| WEB seats.js | 1441 | const j = await safeJsonFetch("/api/seat", { |
| WEB seats.js | 1445 | seat_no: currentSeat, |
| WEB seats.js | 1460 | assigned[String(currentSeat)] = true; |
| WEB seats.js | 1461 | stopsMap[String(currentSeat)] = stop; |
| WEB seats.js | 1462 | genders[String(currentSeat)] = gender; |
| WEB seats.js | 1463 | serviceMap[String(currentSeat)] = !!service; |
| WEB seats.js | 1464 | serviceNotes[String(currentSeat)] = service_note; |
| WEB seats.js | 1465 | boardsMap[String(currentSeat)] = from; |
| WEB seats.js | 1472 | setSeatVisual(currentSeat); |
| WEB seats.js | 1482 | toast(e.message \|\| "Kaydetme hatası"); |
| WEB seats.js | 1486 | function clearSeatUI(seatNo){ |
| WEB seats.js | 1489 | window.clearBiletsizSeatBadges([seatNo]); |
| WEB seats.js | 1493 | delete assigned[String(seatNo)]; |
| WEB seats.js | 1494 | delete stopsMap[String(seatNo)]; |
| WEB seats.js | 1495 | delete genders[String(seatNo)]; |
| WEB seats.js | 1496 | delete serviceMap[String(seatNo)]; |
| WEB seats.js | 1497 | delete serviceNotes[String(seatNo)]; |
| WEB seats.js | 1498 | delete boardsMap[String(seatNo)]; |
| WEB seats.js | 1501 | setSeatVisual(seatNo); |
| WEB seats.js | 1503 | const el = $("#seat-" + seatNo); |
| WEB seats.js | 1505 | el.classList.remove("has-stop","multi-picked","blink-yellow","has-bag"); |
| WEB seats.js | 1514 | if(!currentSeat) return; |
| WEB seats.js | 1516 | const offStop = stopsMap[String(currentSeat)] \|\| getSelectedStopName() \|\| ""; |
| WEB seats.js | 1519 | const j = await safeJsonFetch("/api/seat?seat_no=" + currentSeat, { |
| WEB seats.js | 1530 | await clearBagsForSeat(currentSeat); |
| WEB seats.js | 1531 | clearSeatUI(currentSeat); |
| WEB seats.js | 1547 | el.classList.remove("multi-picked"); |
| WEB seats.js | 1553 | if(el.classList.contains("isAssigned")) return; |
| WEB seats.js | 1557 | el.classList.remove("multi-picked"); |
| WEB seats.js | 1560 | el.classList.add("multi-picked"); |
| WEB seats.js | 1593 | async function saveBulk(){ |
| WEB seats.js | 1633 | const j = await safeJsonFetch("/api/seats/bulk", { |
| WEB seats.js | 1649 | await safeJsonFetch("/api/seat", { |
| WEB seats.js | 1698 | if(el) el.classList.add("blink-yellow"); |
| WEB seats.js | 1706 | if(el) el.classList.remove("blink-yellow"); |
| WEB seats.js | 1784 | const j = await safeJsonFetch("/api/seats/offload", { |
| WEB seats.js | 1794 | const j = await safeJsonFetch("/api/seat?seat_no=" + n, { |
| WEB seats.js | 1938 | async function saveCoord(){ |
| WEB seats.js | 1954 | const j = await safeJsonFetch("/api/coords", { |
| WEB seats.js | 2177 | row.addEventListener("click", () => setSelectedStop(item.stop, { silent:true, voiceReply:false })); |
| WEB seats.js | 2188 | const selectedSeatCount = stop ? (seatCounts[stop] \|\| 0) : 0; |
| WEB seats.js | 2206 | const totalOps = selectedSeatCount + selectedStanding + selectedParcel; |
| WEB seats.js | 2211 | ? `${stop} için ${selectedSeatCount} koltuk, ${selectedStanding} ayakta, ${selectedParcel} emanet görünüyor.` |
| WEB seats.js | 2443 | btn.addEventListener("click", () => { |
| WEB seats.js | 2445 | $$(".tab-btn").forEach(b => b.classList.toggle("active", b === btn)); |
| WEB seats.js | 2446 | $$(".tab-pane").forEach(p => p.classList.toggle("active", p.dataset.pane === tab)); |
| WEB seats.js | 2480 | ttsEnabled ? ttsBtn.classList.remove("muted") : ttsBtn.classList.add("muted"); |
| WEB seats.js | 2490 | ttsBtn.addEventListener("click", () => { |
| WEB seats.js | 2562 | speedBox.classList.remove("limit-ok","limit-warn","limit-bad"); |
| WEB seats.js | 2563 | if(cls) speedBox.classList.add(cls); |
| WEB seats.js | 2586 | const r = await fetch(`/api/speedlimit?lat=${lat}&lng=${lng}`); |
| WEB seats.js | 2672 | document.addEventListener("click", (e) => { |
| WEB seats.js | 2675 | e.preventDefault(); |
| WEB seats.js | 2691 | e.preventDefault(); |
| WEB seats.js | 2700 | onClick("#btnSeatSave", saveSeat); |
| WEB seats.js | 2704 | const seat = currentSeat; |
| WEB seats.js | 2713 | const seat = currentSeat; |
| WEB seats.js | 2724 | onClick("#bulkSave", saveBulk); |
| WEB seats.js | 2731 | onClick("#cashSave", saveCash); |
| WEB seats.js | 2740 | const j = await safeJsonFetch("/api/standing?all=1", { |
| WEB seats.js | 2767 | onClick("#btnSaveCoord", saveCoord); |
| WEB seats.js | 2808 | window.addEventListener("keydown", (e) => { |
| WEB seats.js | 2821 | livePill.addEventListener("click", () => { |
| WEB seats.js | 2833 | nextPill.addEventListener("click", () => { |
| WEB seats.js | 2862 | for(const seatNo of Object.keys(seatPositions \|\| {})){ |
| WEB seats.js | 2863 | setSeatVisual(seatNo); |
| WEB seats.js | 2899 | const tripId = window.SEATS_BOOT?.tripId; |
| WEB seats.js | 2900 | if(!tripId) return; |
| WEB seats.js | 2934 | `/api/live-runtime-state?write=1` + |
| WEB seats.js | 2935 | `&trip_id=${encodeURIComponent(tripId)}` + |
| WEB seats.js | 2942 | fetch(url, { |
| WEB seats.js | 2955 | window.addEventListener("beforeunload", function(){ |
| WEB standing.js | 23 | async function saveCash(){ |
| WEB standing.js | 37 | const j = await safeJsonFetch("/api/standing", { |
| WEB standing.js | 69 | const j = await safeJsonFetch("/api/standing"); |
| WEB standing.js | 90 | const j = await safeJsonFetch("/api/standing/list"); |
| WEB standing.js | 108 | const j = await safeJsonFetch("/api/parcels?status=bekliyor"); |
| WEB standing.js | 165 | btn.addEventListener("click", () => removeStandingById(parseInt(btn.dataset.id, 10))); |
| WEB standing.js | 182 | const j = await safeJsonFetch(`/api/standing?id=${encodeURIComponent(itemId)}`, { |
| WEB standing.js | 208 | const j = await safeJsonFetch("/api/standing?to=" + encodeURIComponent(stopName), { |
| WEB standing.js | 236 | saveCash, |
| WEB manual-ticket-system.js | 35 | function saveMap(obj){ |
| WEB manual-ticket-system.js | 69 | el.classList.contains("isAssigned") \|\| |
| WEB manual-ticket-system.js | 70 | el.classList.contains("male") \|\| |
| WEB manual-ticket-system.js | 71 | el.classList.contains("female") |
| WEB manual-ticket-system.js | 100 | const savedSig = map[no] \|\| ""; |
| WEB manual-ticket-system.js | 103 | el.classList.remove("has-manual-ticket-badge"); |
| WEB manual-ticket-system.js | 104 | el.classList.remove("has-manual-ticket-badge-sig"); |
| WEB manual-ticket-system.js | 106 | if(savedSig && seatAssigned(no) && curSig && savedSig === curSig){ |
| WEB manual-ticket-system.js | 107 | el.classList.add("has-manual-ticket-badge-sig"); |
| WEB manual-ticket-system.js | 115 | if(savedSig && seatAssigned(no) && curSig && savedSig !== curSig){ |
| WEB manual-ticket-system.js | 122 | saveMap(map); |
| WEB manual-ticket-system.js | 153 | el.classList.add("has-manual-ticket-badge-sig"); |
| WEB manual-ticket-system.js | 154 | el.classList.remove("has-manual-ticket-badge"); |
| WEB manual-ticket-system.js | 158 | saveMap(map); |
| WEB manual-ticket-system.js | 180 | el.classList.remove("has-manual-ticket-badge"); |
| WEB manual-ticket-system.js | 181 | el.classList.remove("has-manual-ticket-badge-sig"); |
| WEB manual-ticket-system.js | 185 | saveMap(map); |
| WEB manual-ticket-system.js | 202 | document.addEventListener("DOMContentLoaded", schedule); |
| WEB manual-ticket-system.js | 207 | window.addEventListener("load", schedule); |
| WEB manual-ticket-system.js | 209 | document.addEventListener("click", function(){ |
| WEB manual-ticket-system.js | 215 | document.addEventListener("change", schedule, true); |
| WEB seat-simple-ui-pack.js | 34 | document.documentElement.classList.toggle("seat-simple-mode", simple); |
| WEB seat-simple-ui-pack.js | 35 | document.body.classList.toggle("seat-simple-mode", simple); |
| WEB seat-simple-ui-pack.js | 61 | btn.addEventListener("click", function(){ |
| WEB seat-simple-ui-pack.js | 80 | document.addEventListener("DOMContentLoaded", boot); |
| WEB seat-simple-ui-pack.js | 193 | document.addEventListener("DOMContentLoaded", boot); |
| WEB seat-simple-ui-pack.js | 202 | /* ===== seat-hide-bottom-menu-on-modal-script ===== */ |
| WEB seat-simple-ui-pack.js | 225 | const seatModal = q("#seatModal"); |
| WEB seat-simple-ui-pack.js | 228 | const open = isVisible(seatModal) \|\| isVisible(seatBackdrop); |
| WEB seat-simple-ui-pack.js | 230 | document.documentElement.classList.toggle("seat-modal-open", open); |
| WEB seat-simple-ui-pack.js | 231 | document.body.classList.toggle("seat-modal-open", open); |
| WEB seat-simple-ui-pack.js | 238 | "#seatModal", |
| WEB seat-simple-ui-pack.js | 241 | "#btnSeatSave", |
| WEB seat-simple-ui-pack.js | 259 | document.addEventListener("click", function(){ |
| WEB seat-simple-ui-pack.js | 265 | window.addEventListener("resize", sync); |
| WEB seat-simple-ui-pack.js | 266 | window.addEventListener("orientationchange", function(){ |
| WEB seat-simple-ui-pack.js | 274 | document.addEventListener("DOMContentLoaded", boot); |
| WEB modal-bottom-nav-autohide.js | 2 | if(window.__muavinModalBottomNavAutohideV3) return; |
| WEB modal-bottom-nav-autohide.js | 3 | window.__muavinModalBottomNavAutohideV3 = true; |
| WEB modal-bottom-nav-autohide.js | 45 | "[role='dialog'], .modal, .modal-content, .sheet, .sheet-panel, .drawer, " + |
| WEB modal-bottom-nav-autohide.js | 46 | "[class*='modal'], [class*='sheet'], [class*='drawer'], [class*='panel'], form, section, div" |
| WEB modal-bottom-nav-autohide.js | 100 | document.body.classList.toggle("muavin-work-modal-open", open); |
| WEB modal-bottom-nav-autohide.js | 106 | nav.classList.add("muavin-hidden-bottom-nav-by-modal"); |
| WEB modal-bottom-nav-autohide.js | 109 | document.querySelectorAll(".muavin-hidden-bottom-nav-by-modal").forEach(function(el){ |
| WEB modal-bottom-nav-autohide.js | 110 | el.classList.remove("muavin-hidden-bottom-nav-by-modal"); |
| WEB modal-bottom-nav-autohide.js | 128 | document.addEventListener("click", function(){ |
| WEB modal-bottom-nav-autohide.js | 134 | document.addEventListener("input", scheduleApply, true); |
| WEB modal-bottom-nav-autohide.js | 135 | document.addEventListener("change", scheduleApply, true); |
| WEB modal-bottom-nav-autohide.js | 136 | window.addEventListener("resize", scheduleApply); |
| WEB modal-bottom-nav-autohide.js | 137 | window.addEventListener("scroll", scheduleApply, true); |
| ANDROID seats.html | 12 | <link rel="stylesheet" href="/static/seats/patches/modal-bottom-nav-autohide.css?v=1"> |
| ANDROID seats.html | 252 | <button class="btn accent" type="button" id="btnSaveCoord">Koordinatı Kaydet</button> |
| ANDROID seats.html | 335 | {% include "seats_parts/modals.html" %} |
| ANDROID seats.html | 341 | tripId: {{ trip['id'] \| tojson \| safe }}, |
| ANDROID seats.html | 375 | <script src="/static/seats/patches/modal-bottom-nav-autohide.js?v=1"></script> |
| ANDROID seats.html | 529 | ai.addEventListener("click", function(e){ |
| ANDROID seats.html | 530 | e.preventDefault(); |
| ANDROID seats.html | 537 | end.addEventListener("click", function(){ |
| ANDROID seats.html | 585 | btn.addEventListener("click", function(){ |
| ANDROID seats.html | 604 | window.addEventListener("resize", placeDock); |
| ANDROID seats.html | 605 | window.addEventListener("orientationchange", function(){ |
| ANDROID seats.html | 620 | document.addEventListener("DOMContentLoaded", boot); |
| ANDROID seats.html | 627 | {% include "seats_parts/finish_trip_modal.html" %} |
| ANDROID seats.html | 863 | document.body.classList.toggle("drive-mode", !!on); |
| ANDROID seats.html | 864 | document.documentElement.classList.toggle("drive-mode", !!on); |
| ANDROID seats.html | 887 | document.addEventListener("click", function(e){ |
| ANDROID seats.html | 891 | e.preventDefault(); |
| ANDROID seats.html | 899 | document.addEventListener("DOMContentLoaded", sync); |
| ANDROID seats.html | 933 | fakeBtn.addEventListener("click", function(e){ |
| ANDROID seats.html | 934 | e.preventDefault(); |
| ANDROID seats.html | 964 | window.addEventListener("driveModeChanged", syncDriveVoiceStats); |
| ANDROID seats.html | 965 | window.addEventListener("resize", syncDriveVoiceStats); |
| ANDROID seats.html | 969 | document.addEventListener("DOMContentLoaded", boot); |
| ANDROID seats.html | 993 | document.documentElement.classList.remove("seat-simple-mode"); |
| ANDROID seats.html | 994 | document.body.classList.remove("seat-simple-mode"); |
| ANDROID seats.html | 1054 | durak.addEventListener("click", function(){ |
| ANDROID seats.html | 1070 | voice.addEventListener("click", function(e){ |
| ANDROID seats.html | 1071 | e.preventDefault(); |
| ANDROID seats.html | 1080 | document.addEventListener("DOMContentLoaded", boot); |
| ANDROID modals.html | 1 | <div class="modal-backdrop" id="seatBackdrop"></div> |
| ANDROID modals.html | 2 | <div class="modal glass" id="seatModal"> |
| ANDROID modals.html | 69 | <div class="modal-actions"> |
| ANDROID modals.html | 70 | <button class="btn green" type="button" id="btnSeatSave">Kaydet</button> |
| ANDROID modals.html | 76 | <div class="modal-backdrop" id="bulkBackdrop"></div> |
| ANDROID modals.html | 77 | <div class="sheet-modal glass" id="bulkModal"> |
| ANDROID modals.html | 115 | <div class="modal-actions"> |
| ANDROID modals.html | 117 | <button class="btn primary" type="button" id="bulkSave">Kaydet</button> |
| ANDROID modals.html | 121 | <div class="modal-backdrop" id="cashBackdrop"></div> |
| ANDROID modals.html | 122 | <div class="sheet-modal glass" id="cashModal"> |
| ANDROID modals.html | 164 | <div class="modal-actions"> |
| ANDROID modals.html | 166 | <button class="btn primary" type="button" id="cashSave">Ekle</button> |
| ANDROID modals.html | 170 | <div class="modal-backdrop" id="approachBackdrop"></div> |
| ANDROID modals.html | 171 | <div class="sheet-modal glass" id="approachModal"> |
| ANDROID modals.html | 176 | <div class="modal-actions"> |
| ANDROID modals.html | 183 | <div class="modal-backdrop" id="standingBackdrop"></div> |
| ANDROID modals.html | 184 | <div class="sheet-modal glass" id="standingModal"> |
| ANDROID modals.html | 189 | <div class="modal-actions"> |
| ANDROID seats.js | 95 | if(el) el.addEventListener("click", fn); |
| ANDROID seats.js | 100 | if(el) el.addEventListener("change", fn); |
| ANDROID seats.js | 113 | function show(el){ |
| ANDROID seats.js | 117 | function hide(el){ |
| ANDROID seats.js | 130 | (window.SEATS_BOOT && window.SEATS_BOOT.tripId) \|\| |
| ANDROID seats.js | 131 | (typeof BOOT !== "undefined" && BOOT && BOOT.tripId) \|\| |
| ANDROID seats.js | 144 | // Hem trip_id değişince hem de hafıza şeması değişince eski durak akışı silinsin. |
| ANDROID seats.js | 192 | let currentSeat = null; |
| ANDROID seats.js | 264 | const res = await fetch(url, opt \|\| {}); |
| ANDROID seats.js | 455 | const url = `/api/route-schedule?route=${encodeURIComponent(ROUTE_NAME)}&direction=gidis&_=${Date.now()}`; |
| ANDROID seats.js | 564 | const j = await safeJsonFetch("/api/stops"); |
| ANDROID seats.js | 570 | const c = await safeJsonFetch("/api/coords"); |
| ANDROID seats.js | 729 | Object.keys(assigned \|\| {}).forEach(seatNo => { |
| ANDROID seats.js | 730 | if(!assigned[seatNo]) return; |
| ANDROID seats.js | 731 | if(norm(boardsMap[String(seatNo)] \|\| "") === key){ |
| ANDROID seats.js | 933 | $$(".seat").forEach(el => el.classList.remove("has-stop")); |
| ANDROID seats.js | 938 | if(el) el.classList.add("has-stop"); |
| ANDROID seats.js | 942 | function setSeatVisual(seatNo){ |
| ANDROID seats.js | 943 | const key = String(seatNo); |
| ANDROID seats.js | 944 | const el = $("#seat-" + seatNo); |
| ANDROID seats.js | 947 | el.classList.remove("male","female","isAssigned","has-service"); |
| ANDROID seats.js | 952 | if(isAssigned) el.classList.add("isAssigned"); |
| ANDROID seats.js | 953 | if(gender === "bay") el.classList.add("male"); |
| ANDROID seats.js | 954 | if(gender === "bayan") el.classList.add("female"); |
| ANDROID seats.js | 955 | if(serviceMap[key]) el.classList.add("has-service"); |
| ANDROID seats.js | 957 | const label = $("#label-" + seatNo); |
| ANDROID seats.js | 991 | standingCount > 0 ? standingCard.classList.add("pulse") : standingCard.classList.remove("pulse"); |
| ANDROID seats.js | 1063 | target.classList.add("route-focus-flash"); |
| ANDROID seats.js | 1064 | setTimeout(() => target.classList.remove("route-focus-flash"), 1200); |
| ANDROID seats.js | 1190 | item.addEventListener("click", () => { |
| ANDROID seats.js | 1377 | function openModal(backdropSel, modalSel){ |
| ANDROID seats.js | 1378 | show($(backdropSel)); |
| ANDROID seats.js | 1379 | show($(modalSel)); |
| ANDROID seats.js | 1382 | function closeModal(backdropSel, modalSel){ |
| ANDROID seats.js | 1383 | hide($(backdropSel)); |
| ANDROID seats.js | 1384 | hide($(modalSel)); |
| ANDROID seats.js | 1387 | function openSeat(seatNo){ |
| ANDROID seats.js | 1388 | currentSeat = seatNo; |
| ANDROID seats.js | 1389 | $$(".seat.selected").forEach(x => x.classList.remove("selected")); |
| ANDROID seats.js | 1391 | const seatEl = $("#seat-" + seatNo); |
| ANDROID seats.js | 1392 | if(seatEl) seatEl.classList.add("selected"); |
| ANDROID seats.js | 1394 | setText("#seatTitle", "Koltuk " + seatNo); |
| ANDROID seats.js | 1395 | setValue("#pickup", boardsMap[String(seatNo)] \|\| getSelectedStopName() \|\| ""); |
| ANDROID seats.js | 1396 | setValue("#dropoff", stopsMap[String(seatNo)] \|\| ""); |
| ANDROID seats.js | 1406 | const prevGender = genders[String(seatNo)] \|\| ""; |
| ANDROID seats.js | 1412 | if($("#service")) $("#service").checked = !!serviceMap[String(seatNo)]; |
| ANDROID seats.js | 1413 | setValue("#service_note", serviceNotes[String(seatNo)] \|\| ""); |
| ANDROID seats.js | 1416 | openModal("#seatBackdrop", "#seatModal"); |
| ANDROID seats.js | 1420 | currentSeat = null; |
| ANDROID seats.js | 1421 | closeModal("#seatBackdrop", "#seatModal"); |
| ANDROID seats.js | 1422 | $$(".seat.selected").forEach(x => x.classList.remove("selected")); |
| ANDROID seats.js | 1425 | async function saveSeat(){ |
| ANDROID seats.js | 1426 | if(!currentSeat) return; |
| ANDROID seats.js | 1428 | const wasAlreadyAssigned = !!assigned[String(currentSeat)]; |
| ANDROID seats.js | 1441 | const j = await safeJsonFetch("/api/seat", { |
| ANDROID seats.js | 1445 | seat_no: currentSeat, |
| ANDROID seats.js | 1460 | assigned[String(currentSeat)] = true; |
| ANDROID seats.js | 1461 | stopsMap[String(currentSeat)] = stop; |
| ANDROID seats.js | 1462 | genders[String(currentSeat)] = gender; |
| ANDROID seats.js | 1463 | serviceMap[String(currentSeat)] = !!service; |
| ANDROID seats.js | 1464 | serviceNotes[String(currentSeat)] = service_note; |
| ANDROID seats.js | 1465 | boardsMap[String(currentSeat)] = from; |
| ANDROID seats.js | 1472 | setSeatVisual(currentSeat); |
| ANDROID seats.js | 1482 | toast(e.message \|\| "Kaydetme hatası"); |
| ANDROID seats.js | 1486 | function clearSeatUI(seatNo){ |
| ANDROID seats.js | 1489 | window.clearBiletsizSeatBadges([seatNo]); |
| ANDROID seats.js | 1493 | delete assigned[String(seatNo)]; |
| ANDROID seats.js | 1494 | delete stopsMap[String(seatNo)]; |
| ANDROID seats.js | 1495 | delete genders[String(seatNo)]; |
| ANDROID seats.js | 1496 | delete serviceMap[String(seatNo)]; |
| ANDROID seats.js | 1497 | delete serviceNotes[String(seatNo)]; |
| ANDROID seats.js | 1498 | delete boardsMap[String(seatNo)]; |
| ANDROID seats.js | 1501 | setSeatVisual(seatNo); |
| ANDROID seats.js | 1503 | const el = $("#seat-" + seatNo); |
| ANDROID seats.js | 1505 | el.classList.remove("has-stop","multi-picked","blink-yellow","has-bag"); |
| ANDROID seats.js | 1514 | if(!currentSeat) return; |
| ANDROID seats.js | 1516 | const offStop = stopsMap[String(currentSeat)] \|\| getSelectedStopName() \|\| ""; |
| ANDROID seats.js | 1519 | const j = await safeJsonFetch("/api/seat?seat_no=" + currentSeat, { |
| ANDROID seats.js | 1530 | await clearBagsForSeat(currentSeat); |
| ANDROID seats.js | 1531 | clearSeatUI(currentSeat); |
| ANDROID seats.js | 1547 | el.classList.remove("multi-picked"); |
| ANDROID seats.js | 1553 | if(el.classList.contains("isAssigned")) return; |
| ANDROID seats.js | 1557 | el.classList.remove("multi-picked"); |
| ANDROID seats.js | 1560 | el.classList.add("multi-picked"); |
| ANDROID seats.js | 1593 | async function saveBulk(){ |
| ANDROID seats.js | 1633 | const j = await safeJsonFetch("/api/seats/bulk", { |
| ANDROID seats.js | 1649 | await safeJsonFetch("/api/seat", { |
| ANDROID seats.js | 1698 | if(el) el.classList.add("blink-yellow"); |
| ANDROID seats.js | 1706 | if(el) el.classList.remove("blink-yellow"); |
| ANDROID seats.js | 1784 | const j = await safeJsonFetch("/api/seats/offload", { |
| ANDROID seats.js | 1794 | const j = await safeJsonFetch("/api/seat?seat_no=" + n, { |
| ANDROID seats.js | 1938 | async function saveCoord(){ |
| ANDROID seats.js | 1954 | const j = await safeJsonFetch("/api/coords", { |
| ANDROID seats.js | 2177 | row.addEventListener("click", () => setSelectedStop(item.stop, { silent:true, voiceReply:false })); |
| ANDROID seats.js | 2188 | const selectedSeatCount = stop ? (seatCounts[stop] \|\| 0) : 0; |
| ANDROID seats.js | 2206 | const totalOps = selectedSeatCount + selectedStanding + selectedParcel; |
| ANDROID seats.js | 2211 | ? `${stop} için ${selectedSeatCount} koltuk, ${selectedStanding} ayakta, ${selectedParcel} emanet görünüyor.` |
| ANDROID seats.js | 2443 | btn.addEventListener("click", () => { |
| ANDROID seats.js | 2445 | $$(".tab-btn").forEach(b => b.classList.toggle("active", b === btn)); |
| ANDROID seats.js | 2446 | $$(".tab-pane").forEach(p => p.classList.toggle("active", p.dataset.pane === tab)); |
| ANDROID seats.js | 2480 | ttsEnabled ? ttsBtn.classList.remove("muted") : ttsBtn.classList.add("muted"); |
| ANDROID seats.js | 2490 | ttsBtn.addEventListener("click", () => { |
| ANDROID seats.js | 2562 | speedBox.classList.remove("limit-ok","limit-warn","limit-bad"); |
| ANDROID seats.js | 2563 | if(cls) speedBox.classList.add(cls); |
| ANDROID seats.js | 2586 | const r = await fetch(`/api/speedlimit?lat=${lat}&lng=${lng}`); |
| ANDROID seats.js | 2672 | document.addEventListener("click", (e) => { |
| ANDROID seats.js | 2675 | e.preventDefault(); |
| ANDROID seats.js | 2691 | e.preventDefault(); |
| ANDROID seats.js | 2700 | onClick("#btnSeatSave", saveSeat); |
| ANDROID seats.js | 2704 | const seat = currentSeat; |
| ANDROID seats.js | 2713 | const seat = currentSeat; |
| ANDROID seats.js | 2724 | onClick("#bulkSave", saveBulk); |
| ANDROID seats.js | 2731 | onClick("#cashSave", saveCash); |
| ANDROID seats.js | 2740 | const j = await safeJsonFetch("/api/standing?all=1", { |
| ANDROID seats.js | 2767 | onClick("#btnSaveCoord", saveCoord); |
| ANDROID seats.js | 2808 | window.addEventListener("keydown", (e) => { |
| ANDROID seats.js | 2821 | livePill.addEventListener("click", () => { |
| ANDROID seats.js | 2833 | nextPill.addEventListener("click", () => { |
| ANDROID seats.js | 2862 | for(const seatNo of Object.keys(seatPositions \|\| {})){ |
| ANDROID seats.js | 2863 | setSeatVisual(seatNo); |
| ANDROID seats.js | 2899 | const tripId = window.SEATS_BOOT?.tripId; |

## 10) İlk Teşhis Notu

Bu rapordan sonra bakılacaklar:
1. Kaydet butonunun gerçek ID'si nedir?
2. Butona kaç farklı JS dosyası event bağlıyor?
3. Modal açılırken seçili koltuk değişkeni hangi isimle tutuluyor?
4. Kaydetme işlemi `/api/walkon`, `/api/standing` veya başka endpoint'e mi gidiyor?
5. İlk tıklamada endpoint çağrısı hiç gidiyor mu, yoksa çağrı gidip cevap mı hatalı?
