# Muavin Asistanı Canlı Çekirdek Audit V3

- Tarih: `20260608-164056`
- Root: `/data/data/com.termux/files/home/Host-Hostes-Paneli`

## 1) Canlı Dosya Sayıları
| Kök | Canlı aday dosya |
| --- | --- |
| WEB | 88 |
| ANDROID | 86 |
| APK_PAYLOAD | 72 |

## 2) Asıl Kırmızı Alarm Özeti

- WEB ↔ ANDROID farklı canlı dosya: **1**
- WEB ↔ APK_PAYLOAD farklı canlı dosya: **2**
- ANDROID ↔ APK_PAYLOAD farklı canlı dosya: **2**
- WEB var ANDROID yok: **5**
- ANDROID var WEB yok: **3**
- APK_PAYLOAD tek başına var: **0**
- WEB gerçek eksik static/ref: **0**
- ANDROID gerçek eksik static/ref: **0**
- WEB aynı HTML içinde duplicate ID: **0**
- ANDROID aynı HTML içinde duplicate ID: **0**
- WEB anlamlı JS tekrar adayı: **12**
- ANDROID anlamlı JS tekrar adayı: **12**

## 3) WEB ↔ ANDROID Farklı Canlı Dosyalar
| Dosya | WEB hash | ANDROID hash | WEB satır | ANDROID satır | WEB mtime | ANDROID mtime |
| --- | --- | --- | --- | --- | --- | --- |
| app.py | 7d03ec46f6c0 | cf451e1df53e | 4513 | 4508 | 2026-05-23 12:36:58 | 2026-05-23 14:30:11 |

## 4) WEB ↔ APK_PAYLOAD Farklı Canlı Dosyalar
| Dosya | WEB hash | APK hash | WEB satır | APK satır | WEB mtime | APK mtime |
| --- | --- | --- | --- | --- | --- | --- |
| app.py | 7d03ec46f6c0 | 08ba812bdc04 | 4513 | 4409 | 2026-05-23 12:36:58 | 2026-05-21 00:07:58 |
| static/seats/seats.js | ad8f33d9d149 | ee3ed336c418 | 2960 | 2893 | 2026-05-23 13:20:33 | 2026-05-21 00:07:59 |

## 5) Sadece WEB'de Olan Canlı Dosyalar
| Dosya | Byte | Satır | Mtime |
| --- | --- | --- | --- |
| static/profile/admin_profile_4f864f2df139.jpg | 271828 |  | 2026-05-21 15:43:34 |
| static/seats/patches/_disabled/seat-bottom-fab-54-final.css.disabled_20260523_085109 | 3056 |  | 2026-05-23 08:49:38 |
| static/seats/patches/live-flow-v2.css.disabled_20260523_094130 | 12660 |  | 2026-05-23 09:38:48 |
| static/seats/patches/live-flow-v2.js.disabled_20260523_094130 | 10817 |  | 2026-05-23 09:38:48 |
| static/seats/patches/unified-seat-deck-report-style.css | 12695 | 517 | 2026-05-21 21:23:10 |

## 6) Sadece ANDROID'de Olan Canlı Dosyalar
| Dosya | Byte | Satır | Mtime |
| --- | --- | --- | --- |
| android_server.py | 3441 | 133 | 2026-05-30 10:48:42 |
| requirements.txt | 31 | 5 | 2026-05-03 16:59:51 |
| static/profile/admin_profile_dee7d0b16870.jpg | 1131200 |  | 2026-05-20 23:46:08 |

## 7) Route Karşılaştırması

### WEB route listesi
| Route | Fonksiyon | Satır |
| --- | --- | --- |
| /api/live-runtime-state | api_live_runtime_state | 907 |
| /tanitim | onboarding_page | 1284 |
| /ai-console | ai_console_page | 1334 |
| / | index | 1339 |
| /set-route | set_route | 1346 |
| /sefer-baslat | trip_start | 1360 |
| /continue-trip | continue_trip | 1416 |
| /api/live-seat-bag-detail | api_live_seat_bag_detail | 1912 |
| /api/live-stop-offload | api_live_stop_offload | 2022 |
| /api/live-seat-offload | api_live_seat_offload | 2124 |
| /api/live-seat-destination | api_live_seat_destination | 2227 |
| /api/live-consignment-detail/<int:cid> | api_live_consignment_detail | 2352 |
| /api/live-consignment-deliver/<int:cid> | api_live_consignment_deliver | 2429 |
| /api/live-stop-complete | api_live_stop_complete | 2498 |
| /api/live-stop-detail | api_live_stop_detail | 2709 |
| /canli-harita | live_map_page | 2955 |
| /api/walkon | api_walkon | 3513 |
| /api/standing | api_standing | 3661 |
| /api/standing/list | api_standing_list | 3753 |
| /api/stats | api_stats | 3787 |
| /api/stoplog | api_stoplog | 3856 |
| /sefer-raporu | trip_report_page | 3946 |
| /api/trip-report | api_trip_report | 3951 |
| /sefer-raporu/arsiv/<base> | archived_trip_report_page | 4089 |
| /api/trip-report/archive/<base> | api_archived_trip_report | 4102 |
| /api/report-archive | api_report_archive | 4122 |
| /sefer-raporu-son | latest_trip_report_redirect | 4160 |
| /rapor-arsiv | report_archive_page | 4184 |
| /rapor-dosya/<base>/<kind> | report_file_download | 4211 |
| /bags/clear | bags_clear_alias | 4305 |
| /end-trip | end_trip | 4364 |
| /end_trip | end_trip | 4365 |
| /rehber | rehber_page | 4502 |

### ANDROID route listesi
| Route | Fonksiyon | Satır |
| --- | --- | --- |
| /api/live-runtime-state | api_live_runtime_state | 907 |
| /tanitim | onboarding_page | 1284 |
| /ai-console | ai_console_page | 1334 |
| / | index | 1339 |
| /set-route | set_route | 1346 |
| /sefer-baslat | trip_start | 1360 |
| /continue-trip | continue_trip | 1411 |
| /api/live-seat-bag-detail | api_live_seat_bag_detail | 1907 |
| /api/live-stop-offload | api_live_stop_offload | 2017 |
| /api/live-seat-offload | api_live_seat_offload | 2119 |
| /api/live-seat-destination | api_live_seat_destination | 2222 |
| /api/live-consignment-detail/<int:cid> | api_live_consignment_detail | 2347 |
| /api/live-consignment-deliver/<int:cid> | api_live_consignment_deliver | 2424 |
| /api/live-stop-complete | api_live_stop_complete | 2493 |
| /api/live-stop-detail | api_live_stop_detail | 2704 |
| /canli-harita | live_map_page | 2950 |
| /api/walkon | api_walkon | 3508 |
| /api/standing | api_standing | 3656 |
| /api/standing/list | api_standing_list | 3748 |
| /api/stats | api_stats | 3782 |
| /api/stoplog | api_stoplog | 3851 |
| /sefer-raporu | trip_report_page | 3941 |
| /api/trip-report | api_trip_report | 3946 |
| /sefer-raporu/arsiv/<base> | archived_trip_report_page | 4084 |
| /api/trip-report/archive/<base> | api_archived_trip_report | 4097 |
| /api/report-archive | api_report_archive | 4117 |
| /sefer-raporu-son | latest_trip_report_redirect | 4155 |
| /rapor-arsiv | report_archive_page | 4179 |
| /rapor-dosya/<base>/<kind> | report_file_download | 4206 |
| /bags/clear | bags_clear_alias | 4300 |
| /end-trip | end_trip | 4359 |
| /end_trip | end_trip | 4360 |
| /rehber | rehber_page | 4497 |

### WEB'de var ANDROID'de yok
_Kayıt yok._

### ANDROID'de var WEB'de yok
_Kayıt yok._

## 8) render_template Karşılaştırması

### WEB render_template
| Template | Satır |
| --- | --- |
| onboarding.html | 1286 |
| ai_console.html | 1336 |
| index.html | 1343 |
| trip_report.html | 3948 |
| trip_report.html | 4099 |
| report_archive.html | 4208 |
| rehber.html | 4504 |

### ANDROID render_template
| Template | Satır |
| --- | --- |
| onboarding.html | 1286 |
| ai_console.html | 1336 |
| index.html | 1343 |
| trip_report.html | 3943 |
| trip_report.html | 4094 |
| report_archive.html | 4203 |
| rehber.html | 4499 |

### WEB render ediyor ANDROID etmiyor
_Kayıt yok._

### ANDROID render ediyor WEB etmiyor
_Kayıt yok._

## 9) Gerçek Eksik Static Referansları

### WEB
_Kayıt yok._

### ANDROID
_Kayıt yok._

## 10) Aynı HTML İçinde Duplicate ID

### WEB
_Kayıt yok._

### ANDROID
_Kayıt yok._

## 11) Anlamlı JS Fonksiyon Tekrar Adayları

### WEB
| JS | Fonksiyon | Tekrar |
| --- | --- | --- |
| static/live_map/muavin_live_map_extra.js | getMap | 4 |
| static/live_map/muavin_live_map_extra.js | boot | 4 |
| static/live_map/muavin_live_map_extra.js | getContainer | 3 |
| static/live_map/muavin_live_map_extra.js | clamp | 2 |
| static/live_map/muavin_live_map_extra.js | getPoint | 2 |
| static/live_map/muavin_live_map_extra.js | disableMapMove | 2 |
| static/live_map/muavin_live_map_extra.js | enableMapMove | 2 |
| static/live_map/muavin_live_map_extra.js | start | 2 |
| static/live_map/muavin_live_map_extra.js | move | 2 |
| static/live_map/muavin_live_map_extra.js | end | 2 |
| static/seats/patches/seat-layout-fab-pack.js | schedule | 2 |
| static/seats/patches/seat-simple-ui-pack.js | boot | 3 |

### ANDROID
| JS | Fonksiyon | Tekrar |
| --- | --- | --- |
| static/live_map/muavin_live_map_extra.js | getMap | 4 |
| static/live_map/muavin_live_map_extra.js | boot | 4 |
| static/live_map/muavin_live_map_extra.js | getContainer | 3 |
| static/live_map/muavin_live_map_extra.js | clamp | 2 |
| static/live_map/muavin_live_map_extra.js | getPoint | 2 |
| static/live_map/muavin_live_map_extra.js | disableMapMove | 2 |
| static/live_map/muavin_live_map_extra.js | enableMapMove | 2 |
| static/live_map/muavin_live_map_extra.js | start | 2 |
| static/live_map/muavin_live_map_extra.js | move | 2 |
| static/live_map/muavin_live_map_extra.js | end | 2 |
| static/seats/patches/seat-layout-fab-pack.js | schedule | 2 |
| static/seats/patches/seat-simple-ui-pack.js | boot | 3 |

## 12) Önemli Template Script/Link Sırası

### WEB
| HTML | Satır | Tür | Referans |
| --- | --- | --- | --- |
| templates/index.html | 951 | link | https://fonts.googleapis.com/css2 |
| templates/seats.html | 4 | link | /static/style.css |
| templates/seats.html | 5 | link | /static/seats/seats.css |
| templates/seats.html | 6 | link | /static/seats/seats-final.css |
| templates/seats.html | 7 | link | /static/seats/patches/stop-selected-toast.css |
| templates/seats.html | 8 | link | /static/seats/patches/stop-flow-focus-patch.css |
| templates/seats.html | 9 | link | /static/seats/patches/stop-flow-compact-mobile.css |
| templates/seats.html | 10 | link | /static/seats/patches/seat-layout-fab-pack.css |
| templates/seats.html | 11 | link | /static/seats/patches/bottom-voice-command.css |
| templates/seats.html | 12 | link | /static/seats/patches/modal-bottom-nav-autohide.css |
| templates/seats.html | 13 | link | /static/seats/patches/manual-ticket-system.css |
| templates/seats.html | 14 | link | /static/seats/patches/top-sound-toggle.css |
| templates/seats.html | 15 | link | /static/seats/patches/seat-simple-ui-pack.css |
| templates/seats.html | 16 | link | /static/seats/patches/unified-seat-deck-report-style.css |
| templates/seats.html | 17 | link | /static/seats/patches/mobile-performance-fix.css |
| templates/seats.html | 18 | link | /static/seats/patches/fab-sheet-solid-fix.css |
| templates/seats.html | 19 | link | /static/seats/patches/seat-label-ghost-clean.css |
| templates/seats.html | 364 | script | /static/seats/bags.js |
| templates/seats.html | 365 | script | /static/seats/voice-commands.js |
| templates/seats.html | 366 | script | /static/seats/standing.js |
| templates/seats.html | 367 | script | /static/seats/seats.js |
| templates/seats.html | 368 | script | /static/seats/route-marquee.js |
| templates/seats.html | 369 | script | /static/seats/seats-time-prayer.js |
| templates/seats.html | 370 | script | /static/seats/voice-tts.js |
| templates/seats.html | 371 | script | /static/seats/drive-eta-chip.js |
| templates/seats.html | 372 | script | /static/seats/drive-controls.js |
| templates/seats.html | 373 | script | /static/seats/patches/stop-selected-toast.js |
| templates/seats.html | 374 | script | /static/seats/patches/stop-flow-focus-patch.js |
| templates/seats.html | 375 | script | /static/seats/patches/seat-layout-fab-pack.js |
| templates/seats.html | 376 | script | /static/seats/patches/modal-bottom-nav-autohide.js |
| templates/seats.html | 377 | script | /static/seats/patches/manual-ticket-system.js |
| templates/seats.html | 378 | script | /static/seats/patches/top-sound-toggle.js |
| templates/seats.html | 379 | script | /static/seats/patches/seat-simple-ui-pack.js |
| templates/continue_trip.html | 84 | link | {{ url_for( |
| templates/continue_trip.html | 439 | script | /static/seats/voice-tts.js |
| templates/continue_trip.html | 503 | script | {{ url_for( |
| templates/continue_trip.html | 504 | script | {{ url_for( |
| templates/continue_trip.html | 505 | script | {{ url_for( |
| templates/continue_trip.html | 506 | script | {{ url_for( |
| templates/continue_trip.html | 507 | script | {{ url_for( |
| templates/report_archive.html | 8 | link | https://fonts.googleapis.com/css2 |

### ANDROID
| HTML | Satır | Tür | Referans |
| --- | --- | --- | --- |
| templates/seats.html | 4 | link | /static/style.css |
| templates/seats.html | 5 | link | /static/seats/seats.css |
| templates/seats.html | 6 | link | /static/seats/seats-final.css |
| templates/seats.html | 7 | link | /static/seats/patches/stop-selected-toast.css |
| templates/seats.html | 8 | link | /static/seats/patches/stop-flow-focus-patch.css |
| templates/seats.html | 9 | link | /static/seats/patches/stop-flow-compact-mobile.css |
| templates/seats.html | 10 | link | /static/seats/patches/seat-layout-fab-pack.css |
| templates/seats.html | 11 | link | /static/seats/patches/bottom-voice-command.css |
| templates/seats.html | 12 | link | /static/seats/patches/modal-bottom-nav-autohide.css |
| templates/seats.html | 13 | link | /static/seats/patches/manual-ticket-system.css |
| templates/seats.html | 14 | link | /static/seats/patches/top-sound-toggle.css |
| templates/seats.html | 15 | link | /static/seats/patches/seat-simple-ui-pack.css |
| templates/seats.html | 16 | link | /static/seats/patches/mobile-performance-fix.css |
| templates/seats.html | 17 | link | /static/seats/patches/fab-sheet-solid-fix.css |
| templates/seats.html | 18 | link | /static/seats/patches/seat-label-ghost-clean.css |
| templates/seats.html | 363 | script | /static/seats/bags.js |
| templates/seats.html | 364 | script | /static/seats/voice-commands.js |
| templates/seats.html | 365 | script | /static/seats/standing.js |
| templates/seats.html | 366 | script | /static/seats/seats.js |
| templates/seats.html | 367 | script | /static/seats/route-marquee.js |
| templates/seats.html | 368 | script | /static/seats/seats-time-prayer.js |
| templates/seats.html | 369 | script | /static/seats/voice-tts.js |
| templates/seats.html | 370 | script | /static/seats/drive-eta-chip.js |
| templates/seats.html | 371 | script | /static/seats/drive-controls.js |
| templates/seats.html | 372 | script | /static/seats/patches/stop-selected-toast.js |
| templates/seats.html | 373 | script | /static/seats/patches/stop-flow-focus-patch.js |
| templates/seats.html | 374 | script | /static/seats/patches/seat-layout-fab-pack.js |
| templates/seats.html | 375 | script | /static/seats/patches/modal-bottom-nav-autohide.js |
| templates/seats.html | 376 | script | /static/seats/patches/manual-ticket-system.js |
| templates/seats.html | 377 | script | /static/seats/patches/top-sound-toggle.js |
| templates/seats.html | 378 | script | /static/seats/patches/seat-simple-ui-pack.js |
| templates/continue_trip.html | 84 | link | {{ url_for( |
| templates/continue_trip.html | 439 | script | /static/seats/voice-tts.js |
| templates/continue_trip.html | 503 | script | {{ url_for( |
| templates/continue_trip.html | 504 | script | {{ url_for( |
| templates/continue_trip.html | 505 | script | {{ url_for( |
| templates/continue_trip.html | 506 | script | {{ url_for( |
| templates/continue_trip.html | 507 | script | {{ url_for( |

## 13) Öncelikli Diff Önizlemeleri

### app.py
```diff
--- WEB/app.py
+++ ANDROID/app.py
@@ -1408,11 +1408,6 @@
         all_routes=routes,
     )
 
-
-
-# ===== CONTINUE_LIVE_FLOW_STATE_API_START =====
-
-
 @app.route("/continue-trip")
 def continue_trip():
     tid = get_active_trip()
```

### templates/index.html
```diff
--- WEB/templates/index.html
+++ ANDROID/templates/index.html
@@ -948,100 +948,6 @@
 </style>
 
 
-<link id="home-font-barlow-settings" href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@400;600;700;800&family=Barlow:wght@400;500;600;700&display=swap" rel="stylesheet">
-
-<style id="home-font-match-settings">
-  :root{
-    --font-display:'Barlow Condensed',system-ui,-apple-system,"Segoe UI",Arial,sans-serif;
-    --font-body:'Barlow',system-ui,-apple-system,"Segoe UI",Arial,sans-serif;
-  }
-
-  html,
-  body{
-    font-family:var(--font-body) !important;
-    -webkit-font-smoothing:antialiased;
-    text-rendering:geometricPrecision;
-  }
-
-  body,
-  button,
-  input,
-  select,
-  textarea,
-  a{
-    font-family:var(--font-body) !important;
-  }
-
-  h1,
-  h2,
-  h3,
-  h4,
-  .hero-title,
-  .brand-title,
-  .app-title,
-  .page-title,
-  .section-title,
-  .menu-title,
-  .quick-title,
-  .quick-card-title,
-  .card-title,
-  .tile-title,
-  .status-title,
-  .route-title,
-  .action-title,
-  .panel-title,
-  .title,
-  .big-title{
-    font-family:var(--font-display) !important;
-    font-weight:800;
-    letter-spacing:.01em;
-  }
-
-  .menu-item,
-  .quick-card,
-  .quick-item,
-  .btn,
-  .button,
-  .primary-btn,
-  .secondary-btn,
-  .back-btn{
-    font-family:var(--font-display) !important;
-    font-weight:800;
-    letter-spacing:.02em;
-  }
-
-  p,
-  .muted,
-  .sub,
-  .desc,
-  .menu-desc,
-  .quick-desc,
-  .card-desc,
-  .tile-desc,
-  .status-desc,
-  .small,
-  .label,
-  .meta,
-  .hint{
-    font-family:var(--font-body) !important;
-  }
-</style>
-
-
-<style id="route-sheet-no-flash-fix">
-  /* Route picker ilk render parlamasını engeller */
-  #routeSheet[hidden],
-  #routeSheetBackdrop[hidden]{
-    display:none !important;
-  }
-
-  #routeSheet:not(.show),
-  #routeSheetBackdrop:not(.show){
-    display:none !important;
-  }
-</style>
-
-
... diff kesildi, toplam satır: 252
```

### templates/seats.html
```diff
--- WEB/templates/seats.html
+++ ANDROID/templates/seats.html
@@ -13,7 +13,6 @@
 <link rel="stylesheet" href="/static/seats/patches/manual-ticket-system.css?v=1">
 <link rel="stylesheet" href="/static/seats/patches/top-sound-toggle.css?v=1">
 <link rel="stylesheet" href="/static/seats/patches/seat-simple-ui-pack.css?v=1">
-<link rel="stylesheet" href="/static/seats/patches/unified-seat-deck-report-style.css?v=seat-smaller-removed-2">
 <link rel="stylesheet" href="/static/seats/patches/mobile-performance-fix.css?v=2">
 <link rel="stylesheet" href="/static/seats/patches/fab-sheet-solid-fix.css?v=1">
 <link rel="stylesheet" href="/static/seats/patches/seat-label-ghost-clean.css?v=1">
```

### templates/trip_report.html
```diff
--- WEB/templates/trip_report.html
+++ ANDROID/templates/trip_report.html
@@ -1148,336 +1148,4 @@
 </script>
 
 
-
-
-<style id="trip-report-top-premium-v1">
-  @import url("https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@400;600;700;800&family=Barlow:wght@400;500;600;700&display=swap");
-
-  .report-wrap{
-    max-width:1040px;
-    padding-top:18px;
-    font-family:'Barlow',system-ui,-apple-system,"Segoe UI",Arial,sans-serif;
-  }
-
-  .report-wrap > .hero{
-    position:relative;
-    overflow:hidden;
-    border-radius:28px;
-    padding:26px 22px;
-    background:linear-gradient(160deg,#0e1624 0%,#0d0f14 62%) !important;
-    border:1px solid rgba(255,255,255,.08);
-    box-shadow:0 24px 70px rgba(0,0,0,.42);
-  }
-
-  .report-wrap > .hero::before{
-    content:"";
-    position:absolute;
-    top:-70px;
-    right:-55px;
-    width:260px;
-    height:260px;
-    border-radius:50%;
-    background:radial-gradient(circle,rgba(59,139,255,.22),transparent 70%);
-    pointer-events:none;
-  }
-
-  .report-wrap > .hero::after{
-    content:"";
-    position:absolute;
-    left:0;
-    right:0;
-    bottom:0;
-    height:1px;
-    background:linear-gradient(90deg,transparent,#3b8bff,transparent);
-    opacity:.45;
-  }
-
-  .report-wrap > .hero h1{
-    position:relative;
-    margin:0 0 8px;
-    font-family:'Barlow Condensed',system-ui,-apple-system,"Segoe UI",Arial,sans-serif;
-    font-size:54px;
-    line-height:.95;
-    font-weight:800;
-    letter-spacing:-.02em;
-    color:#e8edf5;
-  }
-
-  .report-wrap > .hero h1::before{
-    content:"RAPORLAR";
-    display:flex;
-    align-items:center;
-    gap:7px;
-    margin-bottom:10px;
-    font-family:'Barlow Condensed',system-ui,-apple-system,"Segoe UI",Arial,sans-serif;
-    font-size:11px;
-    line-height:1;
-    font-weight:800;
-    letter-spacing:.18em;
-    color:#3b8bff;
-  }
-
-  .report-wrap > .hero .muted{
-    position:relative;
-    max-width:760px;
-    color:rgba(232,237,245,.56);
-    font-size:17px;
-    font-weight:650;
-    line-height:1.35;
-  }
-
-  .report-wrap > .hero .actions{
-    position:relative;
-    display:grid;
-    grid-template-columns:repeat(4,1fr);
-    gap:10px;
-    margin-top:18px;
-  }
-
-  .report-wrap > .hero .btn{
-    min-height:56px;
-    border-radius:18px;
-    padding:0 12px;
-    border:1px solid rgba(255,255,255,.08);
-    background:rgba(255,255,255,.035);
-    color:#e8edf5;
-    display:flex;
... diff kesildi, toplam satır: 339
```

### templates/report_archive.html
```diff
--- WEB/templates/report_archive.html
+++ ANDROID/templates/report_archive.html
@@ -1,496 +1,101 @@
-<!doctype html>
-<html lang="tr">
-<head>
-<meta charset="utf-8">
-<meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
-<title>Sefer Rapor Arşivi</title>
-
-<link href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@400;600;700;800&family=Barlow:wght@400;500;600;700&display=swap" rel="stylesheet">
+{% extends "base.html" %}
+{% block content %}
 
 <style>
-  :root{
-    --bg:#0d0f14;
-    --bg-row:#181c27;
-    --bg-hover:#1e2333;
-    --border:rgba(255,255,255,.07);
-    --border-act:rgba(255,255,255,.14);
-    --text:#e8edf5;
-    --text-sub:rgba(232,237,245,.54);
-    --text-dim:rgba(232,237,245,.32);
-    --accent:#3b8bff;
-    --amber:#f5a623;
-    --green:#30d988;
-    --red:#ff4f4f;
-    --font-display:'Barlow Condensed',system-ui,-apple-system,"Segoe UI",Arial,sans-serif;
-    --font-body:'Barlow',system-ui,-apple-system,"Segoe UI",Arial,sans-serif;
-    --r-card:20px;
+  body{
+    background:#06101c;
+    color:#eaf2ff;
+    font-family:system-ui,-apple-system,Segoe UI,Roboto,Arial,sans-serif;
   }
 
-  *,*::before,*::after{
-    box-sizing:border-box;
-    margin:0;
-    padding:0;
-  }
-
-  html,body{
-    min-height:100%;
-    background:var(--bg);
-    color:var(--text);
-    font-family:var(--font-body);
-    -webkit-font-smoothing:antialiased;
-  }
-
-  body::before{
-    content:"";
-    position:fixed;
-    inset:0;
-    background-image:url("data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)' opacity='0.04'/%3E%3C/svg%3E");
-    pointer-events:none;
-    z-index:0;
-  }
-
-  .page{
-    position:relative;
-    z-index:1;
-    max-width:480px;
-    min-height:100vh;
+  .wrap{
+    max-width:900px;
     margin:0 auto;
-    padding:0 0 40px;
+    padding:18px 12px 42px;
   }
 
   .hero{
-    position:relative;
-    overflow:hidden;
-    padding:52px 24px 32px;
-    background:linear-gradient(160deg,#0e1624 0%,#0d0f14 62%);
-    border-bottom:1px solid var(--border);
+    background:linear-gradient(145deg,rgba(37,99,235,.24),rgba(15,23,42,.96));
+    border:1px solid rgba(148,163,184,.22);
+    border-radius:26px;
+    padding:18px;
+    box-shadow:0 18px 55px rgba(0,0,0,.42);
+    margin-bottom:14px;
   }
 
-  .hero::before{
-    content:"";
-    position:absolute;
-    top:-60px;
-    right:-40px;
-    width:260px;
-    height:260px;
-    border-radius:50%;
-    background:radial-gradient(circle,rgba(59,139,255,.18) 0%,transparent 70%);
-    pointer-events:none;
+  h1{
+    margin:0 0 8px;
+    font-size:32px;
   }
... diff kesildi, toplam satır: 559
```

### templates/settings.html
```diff
--- WEB/templates/settings.html
+++ ANDROID/templates/settings.html
@@ -1,585 +1,204 @@
-<!DOCTYPE html>
+<!doctype html>
 <html lang="tr">
 <head>
-<meta charset="UTF-8">
-<meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
-<title>Ayarlar</title>
-
-<link href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@400;600;700;800&family=Barlow:wght@400;500;600;700&display=swap" rel="stylesheet">
-
-<style>
-  :root {
-    --bg:#0d0f14;
-    --bg-card:#13161e;
-    --bg-row:#181c27;
-    --bg-hover:#1e2333;
-    --border:rgba(255,255,255,.07);
-    --border-act:rgba(255,255,255,.14);
-    --text:#e8edf5;
-    --text-sub:rgba(232,237,245,.52);
-    --text-dim:rgba(232,237,245,.30);
-    --accent:#3b8bff;
-    --accent-glow:rgba(59,139,255,.22);
-    --amber:#f5a623;
-    --green:#30d988;
-    --red:#ff4f4f;
-    --purple:#a769ff;
-    --slate:#94a3b8;
-
-    --font-display:'Barlow Condensed',system-ui,-apple-system,"Segoe UI",Arial,sans-serif;
-    --font-body:'Barlow',system-ui,-apple-system,"Segoe UI",Arial,sans-serif;
-
-    --r-card:20px;
-    --r-row:14px;
-  }
-
-  *,*::before,*::after{
-    box-sizing:border-box;
-    margin:0;
-    padding:0;
-  }
-
-  html,body{
-    min-height:100%;
-    background:var(--bg);
-    color:var(--text);
-    font-family:var(--font-body);
-    -webkit-font-smoothing:antialiased;
-  }
-
-  body::before{
-    content:"";
-    position:fixed;
-    inset:0;
-    background-image:url("data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)' opacity='0.04'/%3E%3C/svg%3E");
-    pointer-events:none;
-    z-index:0;
-  }
-
-  .page{
-    position:relative;
-    z-index:1;
-    max-width:480px;
-    min-height:100vh;
-    margin:0 auto;
-    padding:0 0 40px;
-  }
-
-  .hero{
-    position:relative;
-    overflow:hidden;
-    padding:52px 24px 32px;
-    background:linear-gradient(160deg,#0e1624 0%,#0d0f14 62%);
-    border-bottom:1px solid var(--border);
-  }
-
-  .hero::before{
-    content:"";
-    position:absolute;
-    top:-60px;
-    right:-40px;
-    width:260px;
-    height:260px;
-    border-radius:50%;
-    background:radial-gradient(circle,rgba(59,139,255,.18) 0%,transparent 70%);
-    pointer-events:none;
-  }
-
-  .hero::after{
-    content:"";
-    position:absolute;
-    left:0;
-    right:0;
-    bottom:0;
-    height:1px;
-    background:linear-gradient(90deg,transparent,var(--accent),transparent);
-    opacity:.45;
... diff kesildi, toplam satır: 782
```

## 14) Tüm Canlı Dosya Hash Tablosu
| Dosya | WEB | WEB hash | WEB satır | ANDROID | ANDROID hash | ANDROID satır | APK | APK hash | APK satır |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| android_server.py | - | - | - | VAR | c7bb754ce70c | 133 | - | - | - |
| app.py | VAR | 7d03ec46f6c0 | 4513 | VAR | cf451e1df53e | 4508 | VAR | 08ba812bdc04 | 4409 |
| requirements.txt | - | - | - | VAR | a0c7a60fe3a1 | 5 | VAR | a0c7a60fe3a1 | 5 |
| static/app.js | VAR | d144f846ebc3 | 98 | VAR | d144f846ebc3 | 98 | VAR | d144f846ebc3 | 98 |
| static/continue/continue_bag_emanet.js | VAR | 0ff3a3abf6a9 | 129 | VAR | 0ff3a3abf6a9 | 129 | - | - | - |
| static/continue/continue_flow_refresh.js | VAR | f41dbb50eee2 | 419 | VAR | f41dbb50eee2 | 419 | - | - | - |
| static/continue/continue_live_diagnostics.js | VAR | 19431371b579 | 305 | VAR | 19431371b579 | 305 | - | - | - |
| static/continue/continue_trip.css | VAR | d83a890cfc4f | 14 | VAR | d83a890cfc4f | 14 | - | - | - |
| static/continue/continue_trip_core.js | VAR | 382f895530c0 | 2112 | VAR | 382f895530c0 | 2112 | - | - | - |
| static/continue/continue_trip_ui.js | VAR | 4e8f7e386c1d | 251 | VAR | 4e8f7e386c1d | 251 | - | - | - |
| static/continue/css_parts/00-base-legacy.css | VAR | bba69ddc0b09 | 945 | VAR | bba69ddc0b09 | 945 | - | - | - |
| static/continue/css_parts/10-compact-timeline-hero.css | VAR | bb9b29abd26d | 804 | VAR | bb9b29abd26d | 804 | - | - | - |
| static/continue/css_parts/20-live-stop-sheet-base.css | VAR | 78d603e766e1 | 374 | VAR | 78d603e766e1 | 374 | - | - | - |
| static/continue/css_parts/30-sheet-bag-photo.css | VAR | 06ca788e1ee0 | 680 | VAR | 06ca788e1ee0 | 680 | - | - | - |
| static/continue/css_parts/40-cargo-gender-summary.css | VAR | 29bec4ec6099 | 493 | VAR | 29bec4ec6099 | 493 | - | - | - |
| static/continue/css_parts/50-live-v2-top-glow.css | VAR | c61cb85ef163 | 574 | VAR | c61cb85ef163 | 574 | - | - | - |
| static/continue/css_parts/60-live-diagnostics.css | VAR | c418aa372e5a | 144 | VAR | c418aa372e5a | 144 | - | - | - |
| static/data/route_profile_segments.json | VAR | 6c9ca71aac32 | 1 | VAR | 6c9ca71aac32 | 1 | VAR | 6c9ca71aac32 | 1 |
| static/data/route_segments.json | VAR | 8c594d8cdd58 | 1 | VAR | 8c594d8cdd58 | 1 | VAR | 8c594d8cdd58 | 1 |
| static/img/drive-mode-card.png | VAR | c468e07b616c |  | VAR | c468e07b616c |  | VAR | c468e07b616c |  |
| static/img/home-bus-card-final.png | VAR | 9f37bebb1c9e |  | VAR | 9f37bebb1c9e |  | VAR | 9f37bebb1c9e |  |
| static/img/home-bus-card.jpg | VAR | ae0fc6521392 |  | VAR | ae0fc6521392 |  | VAR | ae0fc6521392 |  |
| static/img/home-seat-card.jpg | VAR | 6cb339ad058b |  | VAR | 6cb339ad058b |  | VAR | 6cb339ad058b |  |
| static/img/live-hero-bus.png | VAR | 811eaff42e80 |  | VAR | 811eaff42e80 |  | VAR | 811eaff42e80 |  |
| static/img/menu-bus-card.png | VAR | 9f37bebb1c9e |  | VAR | 9f37bebb1c9e |  | VAR | 9f37bebb1c9e |  |
| static/img/menu-seat-card.png | VAR | 5dc9529909d2 |  | VAR | 5dc9529909d2 |  | VAR | 5dc9529909d2 |  |
| static/img/onboarding/README.txt | VAR | fdb27f4c3548 | 15 | VAR | fdb27f4c3548 | 15 | VAR | fdb27f4c3548 | 15 |
| static/img/onboarding/slides/onboarding_1.png | VAR | 7a4e8f716dfb |  | VAR | 7a4e8f716dfb |  | VAR | 7a4e8f716dfb |  |
| static/img/onboarding/slides/onboarding_2.png | VAR | 7c3f1bebf6ea |  | VAR | 7c3f1bebf6ea |  | VAR | 7c3f1bebf6ea |  |
| static/img/onboarding/slides/onboarding_3.png | VAR | 168083fe08d3 |  | VAR | 168083fe08d3 |  | VAR | 168083fe08d3 |  |
| static/img/onboarding/slides/onboarding_4.png | VAR | 11c9c853153f |  | VAR | 11c9c853153f |  | VAR | 11c9c853153f |  |
| static/img/onboarding/slides/onboarding_5.png | VAR | daf5da8c3cf8 |  | VAR | daf5da8c3cf8 |  | VAR | daf5da8c3cf8 |  |
| static/img/onboarding/slides/onboarding_6.png | VAR | d216733564e2 |  | VAR | d216733564e2 |  | VAR | d216733564e2 |  |
| static/img/onboarding/slides/onboarding_7.png | VAR | 7e28443817dd |  | VAR | 7e28443817dd |  | VAR | 7e28443817dd |  |
| static/img/rehber-cinema-main.png | VAR | d119a66923aa |  | VAR | d119a66923aa |  | VAR | d119a66923aa |  |
| static/img/rehber-durak-akisi-card.png | VAR | de756dddcd74 |  | VAR | de756dddcd74 |  | VAR | de756dddcd74 |  |
| static/img/rehber-hesap-card.png | VAR | 089086214a22 |  | VAR | 089086214a22 |  | VAR | 089086214a22 |  |
| static/img/rehber-promo-main.png | VAR | b8f20b817fe3 |  | VAR | b8f20b817fe3 |  | VAR | b8f20b817fe3 |  |
| static/img/rehber-seat-plan-card.png | VAR | f22e90d5ab8e |  | VAR | f22e90d5ab8e |  | VAR | f22e90d5ab8e |  |
| static/img/rehber-voice-command-card.png | VAR | 128252867424 |  | VAR | 128252867424 |  | VAR | 128252867424 |  |
| static/img/seat-card-final.png | VAR | 5dc9529909d2 |  | VAR | 5dc9529909d2 |  | VAR | 5dc9529909d2 |  |
| static/img/seat-card.jpg | VAR | 26b1e118df00 |  | VAR | 26b1e118df00 |  | VAR | 26b1e118df00 |  |
| static/live_map/muavin_live_map_extra.css | VAR | e52332da4603 | 1831 | VAR | e52332da4603 | 1831 | VAR | e52332da4603 | 1831 |
| static/live_map/muavin_live_map_extra.js | VAR | ec78a9528cb6 | 2101 | VAR | ec78a9528cb6 | 2101 | VAR | ec78a9528cb6 | 2101 |
| static/profile/admin_profile_4f864f2df139.jpg | VAR | a79c06f2b41d |  | - | - | - | - | - | - |
| static/profile/admin_profile_6a6400ae12c1.jpg | VAR | 965fa33adf0e |  | VAR | 965fa33adf0e |  | VAR | 965fa33adf0e |  |
| static/profile/admin_profile_dee7d0b16870.jpg | - | - | - | VAR | e9ddcf589446 |  | VAR | e9ddcf589446 |  |
| static/seats/_archive_theme_trials/seats-dashboard-final.css | VAR | bb790e80850c | 828 | VAR | bb790e80850c | 828 | VAR | bb790e80850c | 828 |
| static/seats/_archive_theme_trials/seats-dashboard-tone.css | VAR | e3471d8357ce | 197 | VAR | e3471d8357ce | 197 | VAR | e3471d8357ce | 197 |
| static/seats/bags.js | VAR | fcf592ed6dd9 | 188 | VAR | fcf592ed6dd9 | 188 | VAR | fcf592ed6dd9 | 188 |
| static/seats/drive-controls.js | VAR | e05214b3f6cf | 287 | VAR | e05214b3f6cf | 287 | VAR | e05214b3f6cf | 287 |
| static/seats/drive-eta-chip.js | VAR | 74e4cb065488 | 65 | VAR | 74e4cb065488 | 65 | VAR | 74e4cb065488 | 65 |
| static/seats/patches/_disabled/seat-bottom-fab-54-final.css.disabled_20260523_085109 | VAR | b25c9bf38389 |  | - | - | - | - | - | - |
| static/seats/patches/bottom-row-51-54-equal-spacing.css | VAR | 3bd1c2baffe1 | 17 | VAR | 3bd1c2baffe1 | 17 | VAR | 3bd1c2baffe1 | 17 |
| static/seats/patches/bottom-voice-command.css | VAR | 5f664bc9a1e5 | 26 | VAR | 5f664bc9a1e5 | 26 | VAR | 5f664bc9a1e5 | 26 |
| static/seats/patches/fab-sheet-solid-fix.css | VAR | 1f9b5f2b0b4c | 65 | VAR | 1f9b5f2b0b4c | 65 | VAR | 1f9b5f2b0b4c | 65 |
| static/seats/patches/live-flow-v2.css.disabled_20260523_094130 | VAR | 2351ddd827c2 |  | - | - | - | - | - | - |
| static/seats/patches/live-flow-v2.js.disabled_20260523_094130 | VAR | 8aa579bac4e5 |  | - | - | - | - | - | - |
| static/seats/patches/manual-ticket-system.css | VAR | 91251ec128d5 | 56 | VAR | 91251ec128d5 | 56 | VAR | 91251ec128d5 | 56 |
| static/seats/patches/manual-ticket-system.js | VAR | 142da4fa8a42 | 228 | VAR | 142da4fa8a42 | 228 | VAR | 142da4fa8a42 | 228 |
| static/seats/patches/mobile-performance-fix.css | VAR | ebb9eb4d201a | 179 | VAR | ebb9eb4d201a | 179 | VAR | ebb9eb4d201a | 179 |
| static/seats/patches/modal-bottom-nav-autohide.css | VAR | a2b76d9d15a0 | 7 | VAR | a2b76d9d15a0 | 7 | VAR | a2b76d9d15a0 | 7 |
| static/seats/patches/modal-bottom-nav-autohide.js | VAR | 5b408035d775 | 150 | VAR | 5b408035d775 | 150 | VAR | 5b408035d775 | 150 |
| static/seats/patches/only-54-reapply-right-shift.css | VAR | dd1207d8cb80 | 21 | VAR | dd1207d8cb80 | 21 | VAR | dd1207d8cb80 | 21 |
| static/seats/patches/right-seat-column-spacing-fix.css | VAR | 478f51a8d7ef | 50 | VAR | 478f51a8d7ef | 50 | VAR | 478f51a8d7ef | 50 |
| static/seats/patches/seat-label-ghost-clean.css | VAR | 7dbec74abcf7 | 46 | VAR | 7dbec74abcf7 | 46 | VAR | 7dbec74abcf7 | 46 |
| static/seats/patches/seat-layout-fab-pack.css | VAR | 4c1589bd069a | 409 | VAR | 4c1589bd069a | 409 | VAR | 4c1589bd069a | 409 |
| static/seats/patches/seat-layout-fab-pack.js | VAR | d15660098d60 | 168 | VAR | d15660098d60 | 168 | VAR | d15660098d60 | 168 |
| static/seats/patches/seat-simple-ui-pack.css | VAR | 37874d3bba93 | 398 | VAR | 37874d3bba93 | 398 | VAR | 37874d3bba93 | 398 |
| static/seats/patches/seat-simple-ui-pack.js | VAR | ab923a78a462 | 279 | VAR | ab923a78a462 | 279 | VAR | ab923a78a462 | 279 |
| static/seats/patches/stop-flow-compact-mobile.css | VAR | 3ab54340a0cd | 107 | VAR | 3ab54340a0cd | 107 | VAR | 3ab54340a0cd | 107 |
| static/seats/patches/stop-flow-focus-patch.css | VAR | 383d9d45a418 | 178 | VAR | 383d9d45a418 | 178 | VAR | 383d9d45a418 | 178 |
| static/seats/patches/stop-flow-focus-patch.js | VAR | ff6942c64edd | 388 | VAR | ff6942c64edd | 388 | VAR | ff6942c64edd | 388 |
| static/seats/patches/stop-selected-toast.css | VAR | 714896463348 | 69 | VAR | 714896463348 | 69 | VAR | 714896463348 | 69 |
| static/seats/patches/stop-selected-toast.js | VAR | 740905a0e0e6 | 64 | VAR | 740905a0e0e6 | 64 | VAR | 740905a0e0e6 | 64 |
| static/seats/patches/top-sound-toggle.css | VAR | dea40a39c380 | 61 | VAR | dea40a39c380 | 61 | VAR | dea40a39c380 | 61 |
| static/seats/patches/top-sound-toggle.js | VAR | 2851010fa38f | 160 | VAR | 2851010fa38f | 160 | VAR | 2851010fa38f | 160 |
| static/seats/patches/unified-seat-deck-report-style.css | VAR | d30bc2b71583 | 517 | - | - | - | - | - | - |
| static/seats/route-marquee.js | VAR | 8d06927a0722 | 46 | VAR | 8d06927a0722 | 46 | VAR | 8d06927a0722 | 46 |
| static/seats/seats-final.css | VAR | 6d10277852f4 | 2564 | VAR | 6d10277852f4 | 2564 | VAR | 6d10277852f4 | 2564 |
| static/seats/seats-time-prayer.js | VAR | 283fabce3c19 | 194 | VAR | 283fabce3c19 | 194 | VAR | 283fabce3c19 | 194 |
| static/seats/seats.css | VAR | 5473bcd300d0 | 4872 | VAR | 5473bcd300d0 | 4872 | VAR | 5473bcd300d0 | 4872 |
| static/seats/seats.css.ba | VAR | 9a2310f2139a |  | VAR | 9a2310f2139a |  | VAR | 9a2310f2139a |  |
| static/seats/seats.js | VAR | ad8f33d9d149 | 2960 | VAR | ad8f33d9d149 | 2960 | VAR | ee3ed336c418 | 2893 |
| static/seats/seats.js.before_revert_route_strip_bug | VAR | 4e5f4bb80bbe |  | VAR | 4e5f4bb80bbe |  | VAR | 4e5f4bb80bbe |  |
| static/seats/standing.js | VAR | d02b404627c2 | 246 | VAR | d02b404627c2 | 246 | VAR | d02b404627c2 | 246 |
| static/seats/voice-commands.js | VAR | 8f12b8d0a7a2 | 1320 | VAR | 8f12b8d0a7a2 | 1320 | VAR | 8f12b8d0a7a2 | 1320 |
| static/seats/voice-tts.js | VAR | dacbfcc0d6f5 | 160 | VAR | dacbfcc0d6f5 | 160 | VAR | dacbfcc0d6f5 | 160 |
| static/style.css | VAR | f2cfa10ef72b | 42 | VAR | f2cfa10ef72b | 42 | VAR | f2cfa10ef72b | 42 |
| static/vendor/bootstrap/bootstrap.bundle.min.js | VAR | 0833b2e9c3a2 | 7 | VAR | 0833b2e9c3a2 | 7 | VAR | 0833b2e9c3a2 | 7 |
| static/vendor/bootstrap/bootstrap.min.css | VAR | 3c8f27e6009c | 6 | VAR | 3c8f27e6009c | 6 | VAR | 3c8f27e6009c | 6 |

## 15) Karar Notu

Bu rapor da sadece tespit içindir. Hiçbir dosya silinmedi.

Bundan sonra doğru sıra:

1. `app.py` WEB/ANDROID farkı incelenecek.
2. `templates/seats.html` ve `static/seats/seats.js` WEB/ANDROID/APK farkı incelenecek.
3. `templates/index.html` içindeki `tripGuard*` duplicate ID sorunu düzeltilecek.
4. Android APK hangi dosyadan çalışıyorsa o ana kaynak kabul edilmeden kopyalama yapılmayacak.
5. `apk_payload` aktif build kaynağı mı, eski paket kalıntısı mı ayrıca belirlenecek.
6. Temizlik ancak bu çekirdek farklar sınıflandırıldıktan sonra yapılacak.
