# Muavin Asistanı Hedefli Dosya Karşılaştırma V4

- Tarih: `20260608-164351`

## 1) Hedef Dosya Hash Karşılaştırması
| Dosya | WEB-ANDROID | WEB hash | ANDROID hash | WEB satır | ANDROID satır | WEB-APK | APK hash | APK satır | WEB mtime | ANDROID mtime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| app.py | FARKLI | 7d03ec46f6c0 | cf451e1df53e | 4513 | 4508 | FARKLI | 08ba812bdc04 | 4409 | 2026-05-23 12:36:58 | 2026-05-23 14:30:11 |
| templates/index.html | FARKLI | e35932eeab6b | 25f6b94cbb7b | 2003 | 1779 | FARKLI | 25f6b94cbb7b | 1779 | 2026-05-23 10:35:38 | 2026-05-21 00:07:58 |
| templates/seats.html | FARKLI | ed8d71df17a4 | 144cb05b9f9e | 1091 | 1090 | FARKLI | 144cb05b9f9e | 1090 | 2026-05-23 09:43:22 | 2026-05-21 00:07:58 |
| static/seats/seats.js | AYNI | ad8f33d9d149 | ad8f33d9d149 | 2960 | 2960 | FARKLI | ee3ed336c418 | 2893 | 2026-05-23 13:20:33 | 2026-05-23 13:20:33 |
| static/seats/standing.js | AYNI | d02b404627c2 | d02b404627c2 | 246 | 246 | AYNI | d02b404627c2 | 246 | 2026-04-28 00:04:53 | 2026-05-21 00:07:58 |
| static/seats/bags.js | AYNI | fcf592ed6dd9 | fcf592ed6dd9 | 188 | 188 | AYNI | fcf592ed6dd9 | 188 | 2026-04-27 23:48:04 | 2026-05-21 00:07:58 |
| static/seats/drive-controls.js | AYNI | e05214b3f6cf | e05214b3f6cf | 287 | 287 | AYNI | e05214b3f6cf | 287 | 2026-05-16 15:41:39 | 2026-05-21 00:07:58 |
| static/seats/voice-commands.js | AYNI | 8f12b8d0a7a2 | 8f12b8d0a7a2 | 1320 | 1320 | AYNI | 8f12b8d0a7a2 | 1320 | 2026-05-18 16:50:14 | 2026-05-21 00:07:58 |
| static/seats/voice-tts.js | AYNI | dacbfcc0d6f5 | dacbfcc0d6f5 | 160 | 160 | AYNI | dacbfcc0d6f5 | 160 | 2026-05-16 15:41:39 | 2026-05-21 00:07:58 |
| templates/continue_trip.html | AYNI | 32395228ea6b | 32395228ea6b | 510 | 510 | FARKLI | 04715057b598 | 5428 | 2026-05-23 14:57:33 | 2026-05-23 14:57:33 |
| static/continue/continue_trip_core.js | AYNI | 382f895530c0 | 382f895530c0 | 2112 | 2112 | EKSİK | - | - | 2026-05-23 13:01:05 | 2026-05-23 14:27:11 |
| static/continue/continue_trip_ui.js | AYNI | 4e8f7e386c1d | 4e8f7e386c1d | 251 | 251 | EKSİK | - | - | 2026-05-23 12:54:39 | 2026-05-23 14:27:11 |
| templates/trip_report.html | FARKLI | 5a07387882e7 | d178f59a71e0 | 1484 | 1152 | FARKLI | d178f59a71e0 | 1152 | 2026-05-21 19:20:24 | 2026-05-21 00:07:58 |
| templates/report_archive.html | FARKLI | 9e36f61fa04f | 3b8702f4d24a | 497 | 102 | FARKLI | 3b8702f4d24a | 102 | 2026-05-21 15:46:02 | 2026-05-21 00:07:58 |
| templates/settings.html | FARKLI | 0556e96d2b4b | 25b8553debc6 | 586 | 205 | FARKLI | 25b8553debc6 | 205 | 2026-05-21 15:14:12 | 2026-05-21 00:07:58 |

## 2) WEB ↔ ANDROID Diff Blokları
### app.py
```diff
--- WEB/app.py
+++ ANDROID/app.py
@@ -1407,13 +1407,8 @@
         current_route=selected_route,
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
     if not tid:
```

### templates/index.html
```diff
--- WEB/templates/index.html
+++ ANDROID/templates/index.html
@@ -947,102 +947,8 @@
 }
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
 </head>
 
 <body>
   <main class="home-shell">
@@ -1068,11 +974,11 @@
         {% endif %}
       </select>
     </div>
 
-    <div class="route-sheet-backdrop" id="routeSheetBackdrop" hidden aria-hidden="true"></div>
-
-    <section class="route-sheet" id="routeSheet" hidden aria-hidden="true">
+    <div class="route-sheet-backdrop" id="routeSheetBackdrop"></div>
+
+    <section class="route-sheet" id="routeSheet" aria-hidden="true">
       <div class="route-sheet-handle"></div>
 
       <div class="route-sheet-head">
         <div>
@@ -1867,136 +1773,6 @@
   }
 })();
 </script>
 
-
-
-<!-- ACTIVE_ROUTE_LOCK_FINAL_START -->
-<script id="active-route-lock-final">
-(function(){
-  const HAS_ACTIVE_TRIP = {% if active_trip is defined and active_trip %}true{% else %}false{% endif %};
-  const ACTIVE_TRIP_ROUTE = {% if active_trip is defined and active_trip %}{{ active_trip.route|tojson }}{% else %}""{% endif %};
-
-  if(!HAS_ACTIVE_TRIP) return;
-
-  const routeBtn = document.getElementById("routePickerBtn");
-  const routeText = document.getElementById("routePickerText");
-  const routeSelect = document.getElementById("homeRouteSelect");
-  const startLink = document.getElementById("homeTripStart");
-
-  const continueLink =
-    Array.from(document.querySelectorAll(".hero-link"))[1] ||
-    document.querySelector('a[href*="continue"]') ||
-    document.querySelector('a[href*="seats"]');
-
-  const sheet = document.getElementById("routeSheet");
-  const backdrop = document.getElementById("routeSheetBackdrop");
-
-  function hardCloseRouteSheet(){
-    if(sheet){
-      sheet.classList.remove("show");
-      sheet.hidden = true;
-      sheet.setAttribute("aria-hidden", "true");
-    }
-    if(backdrop){
-      backdrop.classList.remove("show");
-      backdrop.hidden = true;
-      backdrop.setAttribute("aria-hidden", "true");
-    }
-  }
-
-  function forceActiveRouteText(){
-    if(!ACTIVE_TRIP_ROUTE) return;
-
-    if(routeText) routeText.textContent = ACTIVE_TRIP_ROUTE;
-
-    if(routeSelect){
-      const opt = Array.from(routeSelect.options || []).find(o => o.value === ACTIVE_TRIP_ROUTE);
-      if(opt) routeSelect.value = ACTIVE_TRIP_ROUTE;
-    }
-
-    try{
-      localStorage.setItem("homeSelectedRoute", ACTIVE_TRIP_ROUTE);
-    }catch(_){}
-  }
-
-  function ensureModal(){
-    let bd = document.getElementById("tripGuardBackdrop");
-    let modal = document.getElementById("tripGuardModal");
-
-    if(bd && modal) return {bd, modal};
-
-    bd = document.createElement("div");
-    bd.id = "tripGuardBackdrop";
-    bd.className = "trip-guard-backdrop";
-
-    modal = document.createElement("section");
-    modal.id = "tripGuardModal";
-    modal.className = "trip-guard-modal";
-    modal.innerHTML = `
-      <div class="trip-guard-icon">⚠️</div>
-      <h2>Aktif sefer var</h2>
-      <p>Yeni sefer başlatmadan önce mevcut seferi devam ettirmen veya seferi sonlandırman gerekir.</p>
-      <div class="trip-guard-actions">
-        <a class="trip-guard-go" id="tripGuardGo" href="#">Devam eden sefere git</a>
-        <button class="trip-guard-ok" id="tripGuardOk" type="button">Tamam</button>
-      </div>
-    `;
-
-    document.body.appendChild(bd);
-    document.body.appendChild(modal);
-
-    function close(){
-      bd.classList.remove("show");
-      modal.classList.remove("show");
-    }
-
-    bd.addEventListener("click", close);
-    modal.querySelector("#tripGuardOk")?.addEventListener("click", close);
-
-    const go = modal.querySelector("#tripGuardGo");
-    if(go && continueLink){
-      go.href = continueLink.getAttribute("href") || "/continue-trip";
-    }
-
-    return {bd, modal};
-  }
-
-  function showGuard(){
-    hardCloseRouteSheet();
... DIFF KESİLDİ toplam diff satırı: 257
```

### templates/seats.html
```diff
--- WEB/templates/seats.html
+++ ANDROID/templates/seats.html
@@ -12,9 +12,8 @@
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

### templates/trip_report.html
```diff
--- WEB/templates/trip_report.html
+++ ANDROID/templates/trip_report.html
@@ -1147,337 +1147,5 @@
 })();
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
-    align-items:center;
-    justify-content:center;
-    text-align:center;
-    font-family:'Barlow Condensed',system-ui,-apple-system,"Segoe UI",Arial,sans-serif;
-    font-size:18px;
-    font-weight:800;
-    letter-spacing:.02em;
-    box-shadow:none;
-  }
-
-  .report-wrap > .hero .btn.blue{
-    background:linear-gradient(145deg,#38bdf8,#2563eb);
-    border-color:rgba(59,139,255,.35);
-    box-shadow:0 16px 34px rgba(37,99,235,.24);
-  }
-
-  .report-wrap > .hero .btn.green{
-    background:linear-gradient(145deg,#22c55e,#15803d);
-    border-color:rgba(48,217,136,.32);
-    box-shadow:0 16px 34px rgba(22,163,74,.20);
-  }
-
-  .report-wrap > .summary-grid{
-    display:grid;
-    grid-template-columns:repeat(4,1fr);
-    gap:12px;
-    margin:14px 0;
-  }
-
-  .report-wrap > .summary-grid > .sum-card{
-    position:relative;
-    overflow:hidden;
-    min-height:112px;
-    border-radius:22px;
-    padding:16px;
-    background:#181c27;
-    border:1px solid rgba(255,255,255,.075);
-    box-shadow:0 18px 55px rgba(0,0,0,.24);
-  }
-
-  .report-wrap > .summary-grid > .sum-card::before{
-    content:"";
-    position:absolute;
-    top:-36px;
-    right:-36px;
-    width:96px;
-    height:96px;
-    border-radius:50%;
-    background:radial-gradient(circle,rgba(59,139,255,.16),transparent 70%);
-  }
-
-  .report-wrap > .summary-grid > .sum-card .k{
-    position:relative;
-    font-size:13px;
-    color:rgba(232,237,245,.52);
-    font-weight:750;
-    line-height:1.25;
-  }
-
-  .report-wrap > .summary-grid > .sum-card .v{
-    position:relative;
-    margin-top:10px;
-    font-family:'Barlow Condensed',system-ui,-apple-system,"Segoe UI",Arial,sans-serif;
-    font-size:46px;
-    line-height:.9;
-    font-weight:800;
-    color:#e8edf5;
-    letter-spacing:-.01em;
-  }
-
-  .report-wrap > .summary-grid > .sum-card:nth-child(1) .v{ color:#9af2c8; }
-  .report-wrap > .summary-grid > .sum-card:nth-child(2) .v{ color:#ffb1b1; }
-  .report-wrap > .summary-grid > .sum-card:nth-child(3) .v{ color:#d9b3ff; }
-  .report-wrap > .summary-grid > .sum-card:nth-child(4) .v{ color:#a9ccff; }
-
-  @media(max-width:720px){
-    .report-wrap > .hero h1{
-      font-size:48px;
-    }
-
-    .report-wrap > .hero .actions{
-      grid-template-columns:1fr 1fr;
-    }
-
-    .report-wrap > .summary-grid{
-      grid-template-columns:1fr 1fr;
-    }
-  }
-
-  @media(max-width:390px){
-    .report-wrap{
-      padding-left:12px;
-      padding-right:12px;
-    }
-
-    .report-wrap > .hero{
-      padding:24px 18px;
-    }
-
-    .report-wrap > .hero h1{
-      font-size:44px;
-    }
-
-    .report-wrap > .hero .btn{
-      min-height:54px;
-      font-size:17px;
-    }
-
-    .report-wrap > .summary-grid > .sum-card{
-      min-height:104px;
-      padding:15px;
-    }
-
-    .report-wrap > .summary-grid > .sum-card .v{
-      font-size:40px;
-    }
-  }
-</style>
-
... DIFF KESİLDİ toplam diff satırı: 340
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
 
-  .hero::after{
-    content:"";
-    position:absolute;
-    left:0;
-    right:0;
-    bottom:0;
-    height:1px;
-    background:linear-gradient(90deg,transparent,var(--accent),transparent);
-    opacity:.45;
+  .muted{
+    color:rgba(226,232,240,.65);
   }
 
-  .hero-tag{
-    position:relative;
-    display:inline-flex;
-    align-items:center;
-    gap:7px;
-    font-family:var(--font-display);
-    font-size:11px;
-    font-weight:800;
-    letter-spacing:.18em;
-    text-transform:uppercase;
-    color:var(--accent);
+  .item{
+    background:rgba(15,23,42,.78);
+    border:1px solid rgba(148,163,184,.18);
+    border-radius:20px;
+    padding:14px;
     margin-bottom:10px;
-    opacity:0;
-    animation:fadeUp .5s .05s forwards;
   }
 
-  .hero-tag::before{
-    content:"";
-    width:24px;
-    height:1px;
-    background:var(--accent);
-    display:block;
-  }
-
-  .hero h1{
-    position:relative;
-    font-family:var(--font-display);
-    font-size:54px;
-    font-weight:800;
-    letter-spacing:-.02em;
-    line-height:.95;
-    color:var(--text);
-    opacity:0;
-    animation:fadeUp .5s .12s forwards;
-  }
-
-  .hero h1 span{
-    display:block;
-    max-width:370px;
+  .title{
     font-size:20px;
-    font-weight:600;
-    color:var(--text-sub);
-    margin-top:8px;
-    line-height:1.32;
-  }
-
-  .content{
-    padding:24px 16px 0;
-    display:grid;
-    gap:12px;
-  }
-
-  .summary{
-    display:grid;
-    grid-template-columns:1fr auto;
-    align-items:center;
-    gap:14px;
-    background:var(--bg-row);
-    border:1px solid var(--border);
-    border-radius:var(--r-card);
-    padding:18px;
-    box-shadow:0 20px 60px rgba(0,0,0,.22);
-    opacity:0;
-    animation:fadeUp .4s .16s forwards;
-  }
-
-  .summary-title{
-    font-family:var(--font-display);
-    font-size:28px;
-    font-weight:800;
-    line-height:1;
-  }
-
-  .summary-sub{
-    margin-top:5px;
-    color:var(--text-sub);
-    font-size:14px;
-    font-weight:600;
-    line-height:1.35;
-  }
-
-  .summary-count{
-    min-width:64px;
-    height:56px;
-    border-radius:17px;
-    display:grid;
-    place-items:center;
-    background:rgba(59,139,255,.12);
-    color:#a9ccff;
-    border:1px solid rgba(59,139,255,.24);
-    font-family:var(--font-display);
-    font-size:30px;
-    font-weight:800;
-  }
-
-  .search-card{
-    background:var(--bg-row);
-    border:1px solid var(--border);
-    border-radius:var(--r-card);
-    padding:14px;
... DIFF KESİLDİ toplam diff satırı: 559
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
-  }
-
-  .hero-tag{
-    position:relative;
-    display:inline-flex;
-    align-items:center;
-    gap:7px;
-    font-family:var(--font-display);
-    font-size:11px;
-    font-weight:800;
-    letter-spacing:.18em;
-    text-transform:uppercase;
-    color:var(--accent);
-    margin-bottom:10px;
-    opacity:0;
-    animation:fadeUp .5s .05s forwards;
-  }
-
-  .hero-tag::before{
-    content:"";
-    width:24px;
-    height:1px;
-    background:var(--accent);
-    display:block;
-  }
-
-  .hero h1{
-    position:relative;
-    font-family:var(--font-display);
-    font-size:54px;
-    font-weight:800;
-    letter-spacing:-.02em;
-    line-height:.95;
-    color:var(--text);
-    opacity:0;
-    animation:fadeUp .5s .12s forwards;
-  }
-
-  .hero h1 span{
-    display:block;
-    max-width:340px;
-    font-size:20px;
-    font-weight:600;
-    letter-spacing:.01em;
-    color:var(--text-sub);
-    margin-top:8px;
-    line-height:1.32;
-  }
-
-  .content{
-    padding:24px 16px 0;
-    display:flex;
-    flex-direction:column;
-    gap:8px;
-  }
-
-  .group-label{
-    font-family:var(--font-display);
-    font-size:11px;
-    font-weight:800;
-    letter-spacing:.16em;
-    text-transform:uppercase;
-    color:var(--text-dim);
-    padding:16px 4px 6px;
-    opacity:0;
-    animation:fadeUp .4s forwards;
-  }
-
-  .card-group{
-    background:var(--bg-row);
-    border:1px solid var(--border);
-    border-radius:var(--r-card);
-    overflow:hidden;
-    opacity:0;
-    animation:fadeUp .4s forwards;
-  }
-
-  .setting-row{
-    position:relative;
-    display:flex;
-    align-items:center;
-    gap:14px;
-    min-height:76px;
-    padding:14px 16px;
-    background:transparent;
-    border:none;
-    border-bottom:1px solid var(--border);
-    cursor:pointer;
-    text-decoration:none;
-    color:inherit;
-    transition:background .15s,border-color .15s,transform .1s;
-  }
-
-  .setting-row:last-child{
-    border-bottom:none;
-  }
-
-  .setting-row:active{
-    transform:scale(.985);
-    background:var(--bg-hover);
-  }
-
-  @media(hover:hover){
-    .setting-row:hover{
-      background:var(--bg-hover);
-    }
-  }
-
-  .setting-row::before{
-    content:"";
-    position:absolute;
-    left:0;
-    top:22%;
-    bottom:22%;
-    width:2px;
-    border-radius:2px;
-    opacity:0;
-    transition:opacity .2s;
-  }
-
... DIFF KESİLDİ toplam diff satırı: 782
```


## 3) Kritik Kelime Taraması
### WEB/app.py
| Satır | İçerik |
| --- | --- |
| 100 | def save_admin_profile(full_name, phone, photo_path=""): |
| 125 | def save_profile_photo(file_storage): |
| 141 | file_storage.save(str(target)) |
| 178 | saved_hash = get_admin_password_hash(db) |
| 181 | if saved_hash: |
| 183 | return check_password_hash(saved_hash, password) |
| 304 | "standing_add": {"title": "Ayakta ekleme", "pattern": "standing + add"}, |
| 375 | def delete_walkon_rows( |
| 508 | CREATE INDEX IF NOT EXISTS idx_walkon_trip ON walk_on_sales(trip_id); |
| 747 | saved_hash = get_recovery_code_hash() |
| 748 | if not saved_hash: |
| 752 | return check_password_hash(saved_hash, code) |
| 778 | def save_cash_categories(text_in: str, text_out: str) -> None: |
| 1413 | # ===== CONTINUE_LIVE_FLOW_STATE_API_START ===== |
| 1472 | walkon_total = 0 |
| 1474 | walkon_total = db.execute( |
| 1479 | walkon_total = 0 |
| 1481 | total_revenue = seat_total + walkon_total |
| 1623 | stop_walkon_counts = {} |
| 1639 | stop_walkon_counts[norm_stop(ts)] = int(r["c"] or 0) |
| 1763 | operation_keys.update(k for k, v in stop_walkon_counts.items() if v) |
| 1783 | walkon_count = int(stop_walkon_counts.get(key, 0) or 0) |
| 1820 | "board_count": board_count + walkon_count, |
| 1891 | "walkon_total": walkon_total, |
| 2608 | standing_count = 0 |
| 2620 | standing_count = int(row["c"] or 0) if row else 0 |
| 2622 | standing_count = 0 |
| 2662 | "standing_count": standing_count, |
| 2670 | + pending["standing_count"] |
| 3300 | "save_cash_categories": save_cash_categories, |
| 3323 | "delete_walkon_rows": delete_walkon_rows, |
| 3390 | def _walkon_event_meta(row, extra=None): |
| 3393 | "walkon_id": d.get("id"), |
| 3401 | "source": "standing", |
| 3412 | board, offload, standing_add, standing_off, parcel_deliver, pass_stop |
| 3513 | @app.route("/api/walkon", methods=["GET", "POST", "DELETE"]) |
| 3514 | def api_walkon(): |
| 3586 | "standing_add", |
| 3587 | _walkon_event_meta(row_for_log, {"action": "standing_board"}), |
| 3634 | deleted_ids = delete_walkon_rows( |
| 3649 | "standing_off", |
| 3650 | _walkon_event_meta(r, {"action": "standing_offload"}), |
| 3661 | @app.route("/api/standing", methods=["GET", "POST", "DELETE"]) |
| 3662 | def api_standing(): |
| 3737 | deleted_ids = delete_walkon_rows( |
| 3753 | @app.route("/api/standing/list") |
| 3754 | def api_standing_list(): |
| 3787 | @app.route("/api/stats") |
| 3830 | walkon_revenue = float(walk_row["tot"] or 0) |
| 3836 | "walkon_pax": int(walk_row["pax"] or 0), |
| 3837 | "walkon_revenue": walkon_revenue, |
| 3838 | "total_revenue": seats_revenue + walkon_revenue, |
| 3906 | "standing_add", "standing_off", |
| 3983 | "standing_add": [], |
| 3984 | "standing_off": [], |
| 3992 | "standing_board_count": 0, |
| 3993 | "standing_off_count": 0, |
| 4028 | elif event == "standing_add": |
| 4029 | g["standing_add"].append(item) |
| 4030 | g["summary"]["standing_board_count"] += int(meta.get("pax") or 0) |
| 4032 | elif event == "standing_off": |
| 4033 | g["standing_off"].append(item) |
| 4034 | g["summary"]["standing_off_count"] += int(meta.get("pax") or 0) |
| 4353 | "_walkon_event_meta": _walkon_event_meta, |
| 4361 | save_finished_trip_report = _trip_report_exports["save_finished_trip_report"] |
| 4374 | report_files = save_finished_trip_report(tid) |
| 4491 | "save_admin_profile": save_admin_profile, |
| 4492 | "save_profile_photo": save_profile_photo, |

### ANDROID/app.py
| Satır | İçerik |
| --- | --- |
| 100 | def save_admin_profile(full_name, phone, photo_path=""): |
| 125 | def save_profile_photo(file_storage): |
| 141 | file_storage.save(str(target)) |
| 178 | saved_hash = get_admin_password_hash(db) |
| 181 | if saved_hash: |
| 183 | return check_password_hash(saved_hash, password) |
| 304 | "standing_add": {"title": "Ayakta ekleme", "pattern": "standing + add"}, |
| 375 | def delete_walkon_rows( |
| 508 | CREATE INDEX IF NOT EXISTS idx_walkon_trip ON walk_on_sales(trip_id); |
| 747 | saved_hash = get_recovery_code_hash() |
| 748 | if not saved_hash: |
| 752 | return check_password_hash(saved_hash, code) |
| 778 | def save_cash_categories(text_in: str, text_out: str) -> None: |
| 1467 | walkon_total = 0 |
| 1469 | walkon_total = db.execute( |
| 1474 | walkon_total = 0 |
| 1476 | total_revenue = seat_total + walkon_total |
| 1618 | stop_walkon_counts = {} |
| 1634 | stop_walkon_counts[norm_stop(ts)] = int(r["c"] or 0) |
| 1758 | operation_keys.update(k for k, v in stop_walkon_counts.items() if v) |
| 1778 | walkon_count = int(stop_walkon_counts.get(key, 0) or 0) |
| 1815 | "board_count": board_count + walkon_count, |
| 1886 | "walkon_total": walkon_total, |
| 2603 | standing_count = 0 |
| 2615 | standing_count = int(row["c"] or 0) if row else 0 |
| 2617 | standing_count = 0 |
| 2657 | "standing_count": standing_count, |
| 2665 | + pending["standing_count"] |
| 3295 | "save_cash_categories": save_cash_categories, |
| 3318 | "delete_walkon_rows": delete_walkon_rows, |
| 3385 | def _walkon_event_meta(row, extra=None): |
| 3388 | "walkon_id": d.get("id"), |
| 3396 | "source": "standing", |
| 3407 | board, offload, standing_add, standing_off, parcel_deliver, pass_stop |
| 3508 | @app.route("/api/walkon", methods=["GET", "POST", "DELETE"]) |
| 3509 | def api_walkon(): |
| 3581 | "standing_add", |
| 3582 | _walkon_event_meta(row_for_log, {"action": "standing_board"}), |
| 3629 | deleted_ids = delete_walkon_rows( |
| 3644 | "standing_off", |
| 3645 | _walkon_event_meta(r, {"action": "standing_offload"}), |
| 3656 | @app.route("/api/standing", methods=["GET", "POST", "DELETE"]) |
| 3657 | def api_standing(): |
| 3732 | deleted_ids = delete_walkon_rows( |
| 3748 | @app.route("/api/standing/list") |
| 3749 | def api_standing_list(): |
| 3782 | @app.route("/api/stats") |
| 3825 | walkon_revenue = float(walk_row["tot"] or 0) |
| 3831 | "walkon_pax": int(walk_row["pax"] or 0), |
| 3832 | "walkon_revenue": walkon_revenue, |
| 3833 | "total_revenue": seats_revenue + walkon_revenue, |
| 3901 | "standing_add", "standing_off", |
| 3978 | "standing_add": [], |
| 3979 | "standing_off": [], |
| 3987 | "standing_board_count": 0, |
| 3988 | "standing_off_count": 0, |
| 4023 | elif event == "standing_add": |
| 4024 | g["standing_add"].append(item) |
| 4025 | g["summary"]["standing_board_count"] += int(meta.get("pax") or 0) |
| 4027 | elif event == "standing_off": |
| 4028 | g["standing_off"].append(item) |
| 4029 | g["summary"]["standing_off_count"] += int(meta.get("pax") or 0) |
| 4348 | "_walkon_event_meta": _walkon_event_meta, |
| 4356 | save_finished_trip_report = _trip_report_exports["save_finished_trip_report"] |
| 4369 | report_files = save_finished_trip_report(tid) |
| 4486 | "save_admin_profile": save_admin_profile, |
| 4487 | "save_profile_photo": save_profile_photo, |

### WEB/templates/index.html
| Satır | İçerik |
| --- | --- |
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
| 1683 | animation:tripGuardIn .16s ease forwards; |
| 1686 | @keyframes tripGuardIn{ |
| 1800 | let backdrop = document.getElementById("tripGuardBackdrop"); |
| 1801 | let modal = document.getElementById("tripGuardModal"); |
| 1806 | backdrop.id = "tripGuardBackdrop"; |
| 1810 | modal.id = "tripGuardModal"; |
| 1817 | <a class="trip-guard-go" id="tripGuardGo" href="#">Devam eden sefere git</a> |
| 1818 | <button class="trip-guard-ok" id="tripGuardOk" type="button">Tamam</button> |
| 1831 | modal.querySelector("#tripGuardOk").addEventListener("click", close); |
| 1833 | const go = modal.querySelector("#tripGuardGo"); |
| 1891 | const sheet = document.getElementById("routeSheet"); |
| 1892 | const backdrop = document.getElementById("routeSheetBackdrop"); |
| 1923 | let bd = document.getElementById("tripGuardBackdrop"); |
| 1924 | let modal = document.getElementById("tripGuardModal"); |
| 1929 | bd.id = "tripGuardBackdrop"; |
| 1933 | modal.id = "tripGuardModal"; |
| 1940 | <a class="trip-guard-go" id="tripGuardGo" href="#">Devam eden sefere git</a> |
| 1941 | <button class="trip-guard-ok" id="tripGuardOk" type="button">Tamam</button> |
| 1954 | modal.querySelector("#tripGuardOk")?.addEventListener("click", close); |
| 1956 | const go = modal.querySelector("#tripGuardGo"); |

### ANDROID/templates/index.html
| Satır | İçerik |
| --- | --- |
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
| 1589 | animation:tripGuardIn .16s ease forwards; |
| 1592 | @keyframes tripGuardIn{ |
| 1706 | let backdrop = document.getElementById("tripGuardBackdrop"); |
| 1707 | let modal = document.getElementById("tripGuardModal"); |
| 1712 | backdrop.id = "tripGuardBackdrop"; |
| 1716 | modal.id = "tripGuardModal"; |
| 1723 | <a class="trip-guard-go" id="tripGuardGo" href="#">Devam eden sefere git</a> |
| 1724 | <button class="trip-guard-ok" id="tripGuardOk" type="button">Tamam</button> |
| 1737 | modal.querySelector("#tripGuardOk").addEventListener("click", close); |
| 1739 | const go = modal.querySelector("#tripGuardGo"); |

### WEB/templates/seats.html
| Satır | İçerik |
| --- | --- |
| 16 | <link rel="stylesheet" href="/static/seats/patches/unified-seat-deck-report-style.css?v=seat-smaller-removed-2"> |
| 253 | <button class="btn accent" type="button" id="btnSaveCoord">Koordinatı Kaydet</button> |
| 305 | <div class="standing-list" id="quickStandingList"></div> |
| 366 | <script src="/static/seats/standing.js?v=1"></script> |

### ANDROID/templates/seats.html
| Satır | İçerik |
| --- | --- |
| 252 | <button class="btn accent" type="button" id="btnSaveCoord">Koordinatı Kaydet</button> |
| 304 | <div class="standing-list" id="quickStandingList"></div> |
| 365 | <script src="/static/seats/standing.js?v=1"></script> |

### WEB/static/seats/seats.js
| Satır | İçerik |
| --- | --- |
| 158 | "standingTotals:", |
| 159 | "standingItems:", |
| 194 | let standingCount = 0; |
| 195 | let standingRevenue = 0; |
| 196 | let standingItems = []; |
| 264 | const res = await fetch(url, opt \|\| {}); |
| 292 | localStorage.setItem("standingTotals:" + TRIP_KEY, JSON.stringify({ |
| 293 | count: standingCount, |
| 294 | revenue: standingRevenue |
| 299 | localStorage.setItem("standingItems:" + TRIP_KEY, JSON.stringify(standingItems \|\| [])); |
| 621 | (standingItems \|\| []).forEach(it => { |
| 689 | "standingTotals:" + TRIP_KEY, |
| 690 | "standingItems:" + TRIP_KEY, |
| 736 | (standingItems \|\| []).forEach(it => { |
| 783 | standing_board: Number(old.standing_board \|\| 0) + Number(delta.standing_board \|\| 0), |
| 784 | standing_offload: Number(old.standing_offload \|\| 0) + Number(delta.standing_offload \|\| 0), |
| 856 | const standingBoard = Math.max( |
| 857 | Number(rec.standing_board \|\| rec.standingBoard \|\| 0), |
| 858 | Number(liveRec.standing_board \|\| 0) |
| 861 | const standingOffload = Math.max( |
| 862 | Number(rec.standing_offload \|\| rec.standingOffload \|\| 0), |
| 863 | Number(liveRec.standing_offload \|\| 0) |
| 878 | if(standingBoard > 0) parts.push(`${standingBoard} ayakta bindi`); |
| 879 | if(standingOffload > 0) parts.push(`${standingOffload} ayakta indi`); |
| 911 | const standingCounts = computeStandingCountsByStop(); |
| 924 | const standTxt = standingCounts[base] ? ` + Ayakta ${standingCounts[base]}` : ""; |
| 977 | setText("#pillTotal", String(filled + standingCount)); |
| 983 | setText("#pillStanding", String(standingCount)); |
| 984 | setText("#pillCash", fmtTL(standingRevenue)); |
| 989 | const standingCard = $("#standingCard"); |
| 990 | if(standingCard){ |
| 991 | standingCount > 0 ? standingCard.classList.add("pulse") : standingCard.classList.remove("pulse"); |
| 994 | setText("#quickStandingMeta", `${standingCount} kişi · ${fmtTL(standingRevenue)}`); |
| 1002 | if(!standingItems.length){ |
| 1007 | standingItems.slice(0, 6).forEach(it => { |
| 1013 | d.className = "standing-item"; |
| 1103 | const standingCounts = computeStandingCountsByStop(); |
| 1117 | const standingCt = standingCounts[stop] \|\| 0; |
| 1149 | }else if(seatCt \|\| standingCt \|\| parcelCt){ |
| 1150 | metaLine2 = `${seatCt}K ${standingCt}A ${parcelCt}E`; |
| 1235 | const standingCt = selected ? (computeStandingCountsByStop()[selected] \|\| 0) : 0; |
| 1237 | const totalOps = seatCt + standingCt + parcelCt; |
| 1416 | openModal("#seatBackdrop", "#seatModal"); |
| 1421 | closeModal("#seatBackdrop", "#seatModal"); |
| 1425 | async function saveSeat(){ |
| 1593 | async function saveBulk(){ |
| 1719 | const standingMap = computeStandingCountsByStop(); |
| 1723 | setText("#approachInfo", `${seats.length} koltuk · ${standingMap[stop] \|\| 0} ayakta · ${parcelMap[stop] \|\| 0} emanet`); |
| 1729 | if(!seats.length && !(standingMap[stop] \|\| 0) && !(parcelMap[stop] \|\| 0)){ |
| 1740 | if(standingMap[stop]){ |
| 1743 | row.innerHTML = `<b>Ayakta</b><span>${standingMap[stop]} kişi inecek</span>`; |
| 1938 | async function saveCoord(){ |
| 2185 | const standingCounts = computeStandingCountsByStop(); |
| 2189 | const selectedStanding = stop ? (standingCounts[stop] \|\| 0) : 0; |
| 2275 | const standingMap = computeStandingCountsByStop(); |
| 2276 | total += Number(standingMap[canonical] \|\| 0); |
| 2586 | const r = await fetch(`/api/speedlimit?lat=${lat}&lng=${lng}`); |
| 2700 | onClick("#btnSeatSave", saveSeat); |
| 2724 | onClick("#bulkSave", saveBulk); |
| 2731 | onClick("#cashSave", saveCash); |
| 2733 | onClick("#standingCard", openStandingModal); |
| 2735 | onClick("#standingClose", closeStandingModal); |
| 2736 | onClick("#standingBackdrop", closeStandingModal); |
| 2738 | onClick("#standingBulkOff", async () => { |
| 2740 | const j = await safeJsonFetch("/api/standing?all=1", { |
| 2767 | onClick("#btnSaveCoord", saveCoord); |
| 2942 | fetch(url, { |

### ANDROID/static/seats/seats.js
| Satır | İçerik |
| --- | --- |
| 158 | "standingTotals:", |
| 159 | "standingItems:", |
| 194 | let standingCount = 0; |
| 195 | let standingRevenue = 0; |
| 196 | let standingItems = []; |
| 264 | const res = await fetch(url, opt \|\| {}); |
| 292 | localStorage.setItem("standingTotals:" + TRIP_KEY, JSON.stringify({ |
| 293 | count: standingCount, |
| 294 | revenue: standingRevenue |
| 299 | localStorage.setItem("standingItems:" + TRIP_KEY, JSON.stringify(standingItems \|\| [])); |
| 621 | (standingItems \|\| []).forEach(it => { |
| 689 | "standingTotals:" + TRIP_KEY, |
| 690 | "standingItems:" + TRIP_KEY, |
| 736 | (standingItems \|\| []).forEach(it => { |
| 783 | standing_board: Number(old.standing_board \|\| 0) + Number(delta.standing_board \|\| 0), |
| 784 | standing_offload: Number(old.standing_offload \|\| 0) + Number(delta.standing_offload \|\| 0), |
| 856 | const standingBoard = Math.max( |
| 857 | Number(rec.standing_board \|\| rec.standingBoard \|\| 0), |
| 858 | Number(liveRec.standing_board \|\| 0) |
| 861 | const standingOffload = Math.max( |
| 862 | Number(rec.standing_offload \|\| rec.standingOffload \|\| 0), |
| 863 | Number(liveRec.standing_offload \|\| 0) |
| 878 | if(standingBoard > 0) parts.push(`${standingBoard} ayakta bindi`); |
| 879 | if(standingOffload > 0) parts.push(`${standingOffload} ayakta indi`); |
| 911 | const standingCounts = computeStandingCountsByStop(); |
| 924 | const standTxt = standingCounts[base] ? ` + Ayakta ${standingCounts[base]}` : ""; |
| 977 | setText("#pillTotal", String(filled + standingCount)); |
| 983 | setText("#pillStanding", String(standingCount)); |
| 984 | setText("#pillCash", fmtTL(standingRevenue)); |
| 989 | const standingCard = $("#standingCard"); |
| 990 | if(standingCard){ |
| 991 | standingCount > 0 ? standingCard.classList.add("pulse") : standingCard.classList.remove("pulse"); |
| 994 | setText("#quickStandingMeta", `${standingCount} kişi · ${fmtTL(standingRevenue)}`); |
| 1002 | if(!standingItems.length){ |
| 1007 | standingItems.slice(0, 6).forEach(it => { |
| 1013 | d.className = "standing-item"; |
| 1103 | const standingCounts = computeStandingCountsByStop(); |
| 1117 | const standingCt = standingCounts[stop] \|\| 0; |
| 1149 | }else if(seatCt \|\| standingCt \|\| parcelCt){ |
| 1150 | metaLine2 = `${seatCt}K ${standingCt}A ${parcelCt}E`; |
| 1235 | const standingCt = selected ? (computeStandingCountsByStop()[selected] \|\| 0) : 0; |
| 1237 | const totalOps = seatCt + standingCt + parcelCt; |
| 1416 | openModal("#seatBackdrop", "#seatModal"); |
| 1421 | closeModal("#seatBackdrop", "#seatModal"); |
| 1425 | async function saveSeat(){ |
| 1593 | async function saveBulk(){ |
| 1719 | const standingMap = computeStandingCountsByStop(); |
| 1723 | setText("#approachInfo", `${seats.length} koltuk · ${standingMap[stop] \|\| 0} ayakta · ${parcelMap[stop] \|\| 0} emanet`); |
| 1729 | if(!seats.length && !(standingMap[stop] \|\| 0) && !(parcelMap[stop] \|\| 0)){ |
| 1740 | if(standingMap[stop]){ |
| 1743 | row.innerHTML = `<b>Ayakta</b><span>${standingMap[stop]} kişi inecek</span>`; |
| 1938 | async function saveCoord(){ |
| 2185 | const standingCounts = computeStandingCountsByStop(); |
| 2189 | const selectedStanding = stop ? (standingCounts[stop] \|\| 0) : 0; |
| 2275 | const standingMap = computeStandingCountsByStop(); |
| 2276 | total += Number(standingMap[canonical] \|\| 0); |
| 2586 | const r = await fetch(`/api/speedlimit?lat=${lat}&lng=${lng}`); |
| 2700 | onClick("#btnSeatSave", saveSeat); |
| 2724 | onClick("#bulkSave", saveBulk); |
| 2731 | onClick("#cashSave", saveCash); |
| 2733 | onClick("#standingCard", openStandingModal); |
| 2735 | onClick("#standingClose", closeStandingModal); |
| 2736 | onClick("#standingBackdrop", closeStandingModal); |
| 2738 | onClick("#standingBulkOff", async () => { |
| 2740 | const j = await safeJsonFetch("/api/standing?all=1", { |
| 2767 | onClick("#btnSaveCoord", saveCoord); |
| 2942 | fetch(url, { |

## 4) Karar

Bu rapor da sadece tespit içindir. Silme/kopyalama yapmadı.

Öncelik:
1. WEB-ANDROID farkı olan dosyalar gerçekten fonksiyonel mi görsel mi ayrılacak.
2. Koltuk modal kaydetme sorunu için `templates/seats.html`, `static/seats/seats.js`, `/api/standing`, `/api/walkon`, `/api/stats` akışı ayrıca incelenecek.
3. APK_PAYLOAD ana kaynak kabul edilmeyecek; eski paket çıktısı gibi duruyor.
