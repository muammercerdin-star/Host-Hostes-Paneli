# Muavin iOS Tarzı Sürüş Paneli Kaynak Audit V22

- Tarih: `20260608-183058`
- Bu rapor sadece tespittir. Dosya değiştirmez.
- Amaç: Üst sürüş paneli, sesli komut, durak akışı ve alt legend hangi dosyadan geliyor bulmak.

## 1) Aktif seats.html yapı haritası

### `templates/seats.html`

| Satır | İçerik |
| ---: | --- |
| 4 | `<link rel="stylesheet" href="/static/style.css">` |
| 5 | `<link rel="stylesheet" href="/static/seats/seats.css?v=41">` |
| 6 | `<link rel="stylesheet" href="/static/seats/seats-final.css?v=drive-voice-real-width-test-1">` |
| 7 | `<link rel="stylesheet" href="/static/seats/patches/stop-selected-toast.css?v=1">` |
| 8 | `<link rel="stylesheet" href="/static/seats/patches/stop-flow-focus-patch.css?v=1">` |
| 9 | `<link rel="stylesheet" href="/static/seats/patches/stop-flow-compact-mobile.css?v=1">` |
| 10 | `<link rel="stylesheet" href="/static/seats/patches/seat-layout-fab-pack.css?v=1">` |
| 11 | `<link rel="stylesheet" href="/static/seats/patches/bottom-voice-command.css?v=1">` |
| 12 | `<link rel="stylesheet" href="/static/seats/patches/modal-bottom-nav-autohide.css?v=1">` |
| 13 | `<link rel="stylesheet" href="/static/seats/patches/manual-ticket-system.css?v=1">` |
| 14 | `<link rel="stylesheet" href="/static/seats/patches/top-sound-toggle.css?v=1">` |
| 15 | `<link rel="stylesheet" href="/static/seats/patches/seat-simple-ui-pack.css?v=1">` |
| 16 | `<link rel="stylesheet" href="/static/seats/patches/mobile-performance-fix.css?v=2">` |
| 17 | `<link rel="stylesheet" href="/static/seats/patches/fab-sheet-solid-fix.css?v=1">` |
| 18 | `<link rel="stylesheet" href="/static/seats/patches/seat-label-ghost-clean.css?v=1">` |
| 19 | `<link rel="stylesheet" href="/static/seats/patches/hide-quick-fab-v22.css?v=1">` |
| 21 | `{% include "seats_parts/topbar.html" %}` |
| 22 | `{# {% include "seats_parts/stats.html" %} #}` |
| 29 | `<button id="driveModeToggle" type="button" aria-label="Sürüş modu">🚘 Sürüş</button>` |
| 54 | `<div class="selected-stop-chip">🎯 Seçili durak: <b id="selectedStopBadge">—</b></div>` |
| 59 | `<button class="voice-command-btn" id="btnDeckAI" type="button" title="Sesli Komut">` |
| 60 | `🎤 <span>Sesli Komut</span>` |
| 73 | `<button class="drive-voice-btn" id="btnDeckAIDrive" type="button" title="Sesli Komut">` |
| 74 | `🎤 <span>Sesli Komut</span>` |
| 87 | `<div class="legend">` |
| 88 | `<div class="mini-chip">🟢 Boş</div>` |
| 89 | `<div class="mini-chip">🔵 Bay</div>` |
| 90 | `<div class="mini-chip">🩷 Bayan</div>` |
| 91 | `<div class="mini-chip">🧳 Bagaj</div>` |
| 92 | `<div class="mini-chip">🔔 İniş</div>` |
| 93 | `<div class="mini-chip">🚌 Servis</div>` |
| 98 | `{% include "seats_parts/route_flow.html" %}` |
| 99 | `{% include "seats_parts/deck.html" %}` |
| 336 | `{% include "seats_parts/modals.html" %}` |
| 338 | `<script>` |
| 364 | `<script src="/static/seats/bags.js?v=1"></script>` |
| 365 | `<script src="/static/seats/voice-commands.js?v=voice-listen-guard-1"></script>` |
| 366 | `<script src="/static/seats/standing.js?v=1"></script>` |
| 367 | `<script src="/static/seats/seats.js?v=tripkey-by-id-1"></script>` |
| 368 | `<script src="/static/seats/route-marquee.js?v=route-clean-ticker-single-1"></script>` |
| 369 | `<script src="/static/seats/seats-time-prayer.js?v=time-prayer-apk-1"></script>` |
| 370 | `<script src="/static/seats/voice-tts.js?v=voice-owner-fix-1"></script>` |
| 371 | `<script src="/static/seats/drive-eta-chip.js?v=1"></script>` |
| 372 | `<script src="/static/seats/drive-controls.js?v=drive-toggle-fix-1"></script>` |
| 373 | `<script src="/static/seats/patches/stop-selected-toast.js?v=1"></script>` |
| 374 | `<script src="/static/seats/patches/stop-flow-focus-patch.js?v=simple-scope-1"></script>` |
| 375 | `<script src="/static/seats/patches/seat-layout-fab-pack.js?v=1"></script>` |
| 376 | `<script src="/static/seats/patches/modal-bottom-nav-autohide.js?v=1"></script>` |
| 377 | `<script src="/static/seats/patches/manual-ticket-system.js?v=1"></script>` |
| 378 | `<script src="/static/seats/patches/top-sound-toggle.js?v=1"></script>` |
| 379 | `<script src="/static/seats/patches/seat-simple-ui-pack.js?v=1"></script>` |
| 380 | `<style id="drive-mode-actions-independent-style">` |
| 390 | `#driveModeActionsDock{` |
| 411 | `#driveModeActionsDock .dma-btn{` |
| 436 | `#driveModeActionsDock .dma-btn.danger{` |
| 441 | `#driveModeActionsDock .dma-btn:active{` |
| 446 | `#driveModeActionsDock{` |
| 454 | `#driveModeActionsDock .dma-btn{` |
| 465 | `<script id="drive-mode-actions-independent-js">` |
| 468 | `const btn = document.getElementById("driveModeToggle");` |
| 486 | `let dock = document.getElementById("driveModeActionsDock");` |
| 490 | `dock.id = "driveModeActionsDock";` |
| 584 | `const btn = document.getElementById("driveModeToggle");` |
| 628 | `{% include "seats_parts/finish_trip_modal.html" %}` |
| 678 | `#driveModeToggle{` |
| 797 | `#driveModeToggle{` |
| 837 | `{% include "seats_parts/offload_confirm.html" %}` |
| 840 | `<script id="drive-mode-force-toggle-js">` |
| 842 | `if(window.__driveModeForceToggleReady) return;` |
| 843 | `window.__driveModeForceToggleReady = true;` |
| 848 | `return "driveMode:" + tripKey;` |
| 864 | `document.body.classList.toggle("drive-mode", !!on);` |
| 865 | `document.documentElement.classList.toggle("drive-mode", !!on);` |
| 867 | `const btn = document.getElementById("driveModeToggle");` |
| 879 | `window.dispatchEvent(new CustomEvent("driveModeChanged", { detail:{ on:!!on } }));` |
| 889 | `const btn = e.target.closest && e.target.closest("#driveModeToggle");` |
| 911 | `<script id="drive-mode-manual-normal-guard-v20">` |
| 916 | `const MANUAL_KEY = "driveModeManualNormalGuard:v20";` |
| 921 | `return document.getElementById("driveModeToggle");` |
| 927 | `return document.body.classList.contains("drive-mode") \|\|` |
| 928 | `document.documentElement.classList.contains("drive-mode") \|\|` |
| 937 | `if(k && k.indexOf("driveMode:") === 0) out.push(k);` |
| 971 | `document.body.classList.remove("drive-mode");` |
| 972 | `document.documentElement.classList.remove("drive-mode");` |
| 983 | `window.dispatchEvent(new CustomEvent("driveModeChanged", {` |
| 990 | `const hit = e.target && e.target.closest && e.target.closest("#driveModeToggle");` |
| 1044 | `<script id="drive-voice-mirror-script">` |
| 1098 | `window.addEventListener("driveModeChanged", syncDriveVoiceStats);` |
| 1111 | `<script id="seat-simple-bottom-bar-script">` |
| 1178 | `<button type="button" class="seat-simple-bottom-item warn" id="seatSimpleVoiceBtn" title="Sesli Komut" aria-label="Sesli Komut">` |

### `android_app/app/src/main/python/templates/seats.html`

| Satır | İçerik |
| ---: | --- |
| 4 | `<link rel="stylesheet" href="/static/style.css">` |
| 5 | `<link rel="stylesheet" href="/static/seats/seats.css?v=41">` |
| 6 | `<link rel="stylesheet" href="/static/seats/seats-final.css?v=drive-voice-real-width-test-1">` |
| 7 | `<link rel="stylesheet" href="/static/seats/patches/stop-selected-toast.css?v=1">` |
| 8 | `<link rel="stylesheet" href="/static/seats/patches/stop-flow-focus-patch.css?v=1">` |
| 9 | `<link rel="stylesheet" href="/static/seats/patches/stop-flow-compact-mobile.css?v=1">` |
| 10 | `<link rel="stylesheet" href="/static/seats/patches/seat-layout-fab-pack.css?v=1">` |
| 11 | `<link rel="stylesheet" href="/static/seats/patches/bottom-voice-command.css?v=1">` |
| 12 | `<link rel="stylesheet" href="/static/seats/patches/modal-bottom-nav-autohide.css?v=1">` |
| 13 | `<link rel="stylesheet" href="/static/seats/patches/manual-ticket-system.css?v=1">` |
| 14 | `<link rel="stylesheet" href="/static/seats/patches/top-sound-toggle.css?v=1">` |
| 15 | `<link rel="stylesheet" href="/static/seats/patches/seat-simple-ui-pack.css?v=1">` |
| 16 | `<link rel="stylesheet" href="/static/seats/patches/mobile-performance-fix.css?v=2">` |
| 17 | `<link rel="stylesheet" href="/static/seats/patches/fab-sheet-solid-fix.css?v=1">` |
| 18 | `<link rel="stylesheet" href="/static/seats/patches/seat-label-ghost-clean.css?v=1">` |
| 19 | `<link rel="stylesheet" href="/static/seats/patches/hide-quick-fab-v22.css?v=1">` |
| 21 | `{% include "seats_parts/topbar.html" %}` |
| 22 | `{# {% include "seats_parts/stats.html" %} #}` |
| 29 | `<button id="driveModeToggle" type="button" aria-label="Sürüş modu">🚘 Sürüş</button>` |
| 54 | `<div class="selected-stop-chip">🎯 Seçili durak: <b id="selectedStopBadge">—</b></div>` |
| 59 | `<button class="voice-command-btn" id="btnDeckAI" type="button" title="Sesli Komut">` |
| 60 | `🎤 <span>Sesli Komut</span>` |
| 73 | `<button class="drive-voice-btn" id="btnDeckAIDrive" type="button" title="Sesli Komut">` |
| 74 | `🎤 <span>Sesli Komut</span>` |
| 87 | `<div class="legend">` |
| 88 | `<div class="mini-chip">🟢 Boş</div>` |
| 89 | `<div class="mini-chip">🔵 Bay</div>` |
| 90 | `<div class="mini-chip">🩷 Bayan</div>` |
| 91 | `<div class="mini-chip">🧳 Bagaj</div>` |
| 92 | `<div class="mini-chip">🔔 İniş</div>` |
| 93 | `<div class="mini-chip">🚌 Servis</div>` |
| 98 | `{% include "seats_parts/route_flow.html" %}` |
| 99 | `{% include "seats_parts/deck.html" %}` |
| 336 | `{% include "seats_parts/modals.html" %}` |
| 338 | `<script>` |
| 364 | `<script src="/static/seats/bags.js?v=1"></script>` |
| 365 | `<script src="/static/seats/voice-commands.js?v=voice-listen-guard-1"></script>` |
| 366 | `<script src="/static/seats/standing.js?v=1"></script>` |
| 367 | `<script src="/static/seats/seats.js?v=tripkey-by-id-1"></script>` |
| 368 | `<script src="/static/seats/route-marquee.js?v=route-clean-ticker-single-1"></script>` |
| 369 | `<script src="/static/seats/seats-time-prayer.js?v=time-prayer-apk-1"></script>` |
| 370 | `<script src="/static/seats/voice-tts.js?v=voice-owner-fix-1"></script>` |
| 371 | `<script src="/static/seats/drive-eta-chip.js?v=1"></script>` |
| 372 | `<script src="/static/seats/drive-controls.js?v=drive-toggle-fix-1"></script>` |
| 373 | `<script src="/static/seats/patches/stop-selected-toast.js?v=1"></script>` |
| 374 | `<script src="/static/seats/patches/stop-flow-focus-patch.js?v=simple-scope-1"></script>` |
| 375 | `<script src="/static/seats/patches/seat-layout-fab-pack.js?v=1"></script>` |
| 376 | `<script src="/static/seats/patches/modal-bottom-nav-autohide.js?v=1"></script>` |
| 377 | `<script src="/static/seats/patches/manual-ticket-system.js?v=1"></script>` |
| 378 | `<script src="/static/seats/patches/top-sound-toggle.js?v=1"></script>` |
| 379 | `<script src="/static/seats/patches/seat-simple-ui-pack.js?v=1"></script>` |
| 380 | `<style id="drive-mode-actions-independent-style">` |
| 390 | `#driveModeActionsDock{` |
| 411 | `#driveModeActionsDock .dma-btn{` |
| 436 | `#driveModeActionsDock .dma-btn.danger{` |
| 441 | `#driveModeActionsDock .dma-btn:active{` |
| 446 | `#driveModeActionsDock{` |
| 454 | `#driveModeActionsDock .dma-btn{` |
| 465 | `<script id="drive-mode-actions-independent-js">` |
| 468 | `const btn = document.getElementById("driveModeToggle");` |
| 486 | `let dock = document.getElementById("driveModeActionsDock");` |
| 490 | `dock.id = "driveModeActionsDock";` |
| 584 | `const btn = document.getElementById("driveModeToggle");` |
| 628 | `{% include "seats_parts/finish_trip_modal.html" %}` |
| 678 | `#driveModeToggle{` |
| 797 | `#driveModeToggle{` |
| 837 | `{% include "seats_parts/offload_confirm.html" %}` |
| 840 | `<script id="drive-mode-force-toggle-js">` |
| 842 | `if(window.__driveModeForceToggleReady) return;` |
| 843 | `window.__driveModeForceToggleReady = true;` |
| 848 | `return "driveMode:" + tripKey;` |
| 864 | `document.body.classList.toggle("drive-mode", !!on);` |
| 865 | `document.documentElement.classList.toggle("drive-mode", !!on);` |
| 867 | `const btn = document.getElementById("driveModeToggle");` |
| 879 | `window.dispatchEvent(new CustomEvent("driveModeChanged", { detail:{ on:!!on } }));` |
| 889 | `const btn = e.target.closest && e.target.closest("#driveModeToggle");` |
| 911 | `<script id="drive-mode-manual-normal-guard-v20">` |
| 916 | `const MANUAL_KEY = "driveModeManualNormalGuard:v20";` |
| 921 | `return document.getElementById("driveModeToggle");` |
| 927 | `return document.body.classList.contains("drive-mode") \|\|` |
| 928 | `document.documentElement.classList.contains("drive-mode") \|\|` |
| 937 | `if(k && k.indexOf("driveMode:") === 0) out.push(k);` |
| 971 | `document.body.classList.remove("drive-mode");` |
| 972 | `document.documentElement.classList.remove("drive-mode");` |
| 983 | `window.dispatchEvent(new CustomEvent("driveModeChanged", {` |
| 990 | `const hit = e.target && e.target.closest && e.target.closest("#driveModeToggle");` |
| 1044 | `<script id="drive-voice-mirror-script">` |
| 1098 | `window.addEventListener("driveModeChanged", syncDriveVoiceStats);` |
| 1111 | `<script id="seat-simple-bottom-bar-script">` |
| 1178 | `<button type="button" class="seat-simple-bottom-item warn" id="seatSimpleVoiceBtn" title="Sesli Komut" aria-label="Sesli Komut">` |

## 2) Görünen ekran elemanlarının kaynak izleri

### `templates/add_route.html`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 208 | `Boş` | `/* Sayfa dış boşluk */` |
| 304 | `Boş` | `      <div class="hint">Virgül (,) ve/veya yeni satır ile ayırabilirsiniz. Boşlukları otomatik temizler.</div>` |
| 334 | `Boş` | `    // satır ve virgül bazlı parçala, kırp, boşları at` |
| 370 | `Normal` | `  // Gönderimden önce metni normalize et (server tarafına temiz liste gitsin)` |
| 379 | `Normal` | `    // Sunucu "virgülle ayrılmış" bekliyorsa normalize et:` |

### `templates/events.html`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 123 | `Boş` | `      <span class="small" style="margin-left:8px">Boş bırakırsan varsayılana döner.</span>` |

### `templates/fare_admin.html`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 54 | `İniş` | `        <div class="label">İniş</div>` |
| 69 | `İniş` | `        <button class="btn gray" type="button" onclick="swap()">Biniş ↔ İniş</button>` |
| 127 | `Canlı` | `  // Canlı filtre` |
| 131 | `Boş` | `      if(!el.dataset.from){ return; } // boş satır için` |

### `templates/fare_query.html`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 54 | `İniş` | `        <div class="label">İniş</div>` |
| 67 | `İniş` | `      <button class="btn gray" type="button" onclick="swapStops()">Biniş ↔ İniş</button>` |

### `templates/hesap.html`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 1887 | `Durak Akışı` | `        Bu işlem aktif seferi kapatır. Koltuklar, ayakta yolcular ve durak akışı temizlenir.` |
| 2340 | `Normal` | `    function normalize(s){` |
| 2345 | `Normal` | `      const term = normalize(q?.value \|\| "");` |
| 2352 | `Normal` | `        const ok = !term \|\| normalize(r.innerText).includes(term);` |
| 2358 | `Normal` | `        const ok = !term \|\| normalize(c.innerText).includes(term);` |

### `templates/index.html`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 1190 | `Sesli Komut` | `          <div class="menu-desc">Uygulama kullanımı / sesli komutlar / hızlı yardım</div>` |
| 1879 | `Normal` | `       Aktif sefer yoksa premium route picker normal açılır.` |

### `templates/passenger_control.html`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 240 | `legend` | `.legend-box{` |
| 252 | `legend` | `.legend-line{` |
| 259 | `legend` | `.legend-dot{` |
| 266 | `legend` | `.legend-dot.wait{ background:#f59e0b; box-shadow:0 0 16px rgba(245,158,11,.55); }` |
| 267 | `legend` | `.legend-dot.ok{ background:#22c55e; box-shadow:0 0 16px rgba(34,197,94,.50); }` |
| 268 | `legend` | `.legend-dot.bad{ background:#ef4444; box-shadow:0 0 16px rgba(239,68,68,.50); }` |
| 710 | `Boş` | `    <div class="stat"><div class="k">Boş Koltuk</div><div class="v" id="st_empty">0</div></div>` |
| 715 | `legend` | `  <section class="legend-box">` |
| 716 | `legend` | `    <div class="legend-line"><span class="legend-dot wait"></span> Sarı yanıp sönüyor: kontrol bekliyor</div>` |
| 717 | `legend` | `    <div class="legend-line"><span class="legend-dot ok"></span> Yeşil: yolcu yerinde</div>` |
| 718 | `legend` | `    <div class="legend-line"><span class="legend-dot bad"></span> Kırmızı: eksik yolcu</div>` |
| 724 | `Canlı` | `      <span class="deck-badge">Canlı kontrol</span>` |
| 754 | `Bay` | `  if(gender === 'bay'){` |
| 756 | `Bay` | `  }else if(gender === 'bayan'){` |
| 1218 | `legend` | `.legend-box{` |
| 1226 | `legend` | `.legend-line{` |
| 1230 | `legend` | `.legend-dot{` |

### `templates/reports.html`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 125 | `legend` | `  .legend{display:flex;gap:8px;align-items:center;margin-top:8px;color:var(--sub)}` |
| 250 | `legend` | `      <div class="legend">` |

### `templates/route_edit.html`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 704 | `Boş` | `      alert("Durak listesi boş.");` |

### `templates/route_stops.html`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 57 | `route-stop` | `        const res = await fetch('/api/route-stop', {` |

### `templates/seats.html`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 6 | `voice` | `<link rel="stylesheet" href="/static/seats/seats-final.css?v=drive-voice-real-width-test-1">` |
| 11 | `voice` | `<link rel="stylesheet" href="/static/seats/patches/bottom-voice-command.css?v=1">` |
| 15 | `seat-simple` | `<link rel="stylesheet" href="/static/seats/patches/seat-simple-ui-pack.css?v=1">` |
| 29 | `Sürüş` | `          <button id="driveModeToggle" type="button" aria-label="Sürüş modu">🚘 Sürüş</button>` |
| 31 | `driveSpeedChip` | `          <div id="driveSpeedChip" class="drive-speed-chip neutral">` |
| 40 | `driveEtaChip` | `          <div id="driveEtaChip" class="drive-eta-chip neutral">` |
| 43 | `driveEtaMain` | `              <b id="driveEtaMain">Rötar</b>` |
| 45 | `driveEtaSub` | `            <div class="drive-eta-sub" id="driveEtaSub">ETA bekleniyor</div>` |
| 49 | `board-head` | `        <div class="board-head">` |
| 50 | `board-title` | `          <div class="board-title">` |
| 51 | `Canlı` | `            <div class="board-kicker">Canlı Operasyon Paneli</div>` |
| 54 | `Seçili durak` | `            <div class="selected-stop-chip">🎯 Seçili durak: <b id="selectedStopBadge">—</b></div>` |
| 57 | `board-head` | `          <div class="board-head-right">` |
| 58 | `voice` | `            <div class="voice-row">` |
| 59 | `Sesli Komut` | `              <button class="voice-command-btn" id="btnDeckAI" type="button" title="Sesli Komut">` |
| 60 | `Sesli Komut` | `                🎤 <span>Sesli Komut</span>` |
| 63 | `voice` | `              <div class="voice-seat-mini" id="voiceSeatMiniStats" title="Koltuk özeti">` |
| 64 | `voice` | `                <span>Dolu <b id="voiceSeatFilled">0</b></span>` |
| 65 | `voice` | `                <span>Boş <b id="voiceSeatEmpty">0</b></span>` |
| 68 | `voice` | `              <div class="voice-state" id="voiceStateBadge">Hazır</div>` |
| 71 | `voice` | `<!-- DRIVE VOICE ROW START -->` |
| 72 | `voice` | `<div class="drive-voice-row" id="driveVoiceRow">` |
| 73 | `Sesli Komut` | `  <button class="drive-voice-btn" id="btnDeckAIDrive" type="button" title="Sesli Komut">` |
| 74 | `Sesli Komut` | `    🎤 <span>Sesli Komut</span>` |
| 77 | `voice` | `  <div class="drive-voice-seat" id="driveVoiceSeatCard" title="Koltuk özeti">` |
| 78 | `voice` | `    <span class="drive-voice-seat-ico">💺</span>` |
| 79 | `voice` | `    <span class="drive-voice-seat-values">` |
| 80 | `voice` | `      <b id="driveVoiceFilled">0</b>` |
| 82 | `voice` | `      <b id="driveVoiceEmpty">0</b>` |
| 86 | `voice` | `<!-- DRIVE VOICE ROW END -->` |
| 87 | `legend` | `<div class="legend">` |
| 88 | `mini-chip` | `              <div class="mini-chip">🟢 Boş</div>` |
| 89 | `mini-chip` | `              <div class="mini-chip">🔵 Bay</div>` |
| 90 | `mini-chip` | `              <div class="mini-chip">🩷 Bayan</div>` |
| 91 | `mini-chip` | `              <div class="mini-chip">🧳 Bagaj</div>` |
| 92 | `mini-chip` | `              <div class="mini-chip">🔔 İniş</div>` |
| 93 | `mini-chip` | `              <div class="mini-chip">🚌 Servis</div>` |
| 125 | `Canlı` | `                <div class="k">Canlı Durak</div>` |
| 149 | `Canlı` | `              <small>Canlı</small>` |
| 192 | `Canlı` | `              <h3>Canlı Durak Yönetimi</h3>` |
| 198 | `Sıradaki` | `                <span>Sıradaki Durak</span>` |
| 238 | `Seçili durak` | `                <span>Seçili Durak</span>` |
| 270 | `Canlı` | `                <div class="k">Canlı Durak</div>` |
| 315 | `Canlı` | `              <small>Canlı analiz</small>` |
| 319 | `Canlı` | `            <div class="ai-sub" id="aiSub">Sistem canlı rota, durak ve rötar özetini hazırlıyor.</div>` |
| 322 | `Sıradaki` | `              <div class="ai-item"><b>Sıradaki İşlem</b><span id="aiNextActionMirror">—</span></div>` |
| 323 | `Canlı` | `              <div class="ai-item"><b>Canlı Durak</b><span id="aiLiveStop">—</span></div>` |
| 326 | `Servis` | `              <div class="ai-item"><b>Servis</b><span id="aiService">—</span></div>` |
| 365 | `voice` | `<script src="/static/seats/voice-commands.js?v=voice-listen-guard-1"></script>` |
| 370 | `voice` | `<script src="/static/seats/voice-tts.js?v=voice-owner-fix-1"></script>` |
| 379 | `seat-simple` | `<script src="/static/seats/patches/seat-simple-ui-pack.js?v=1"></script>` |
| 380 | `drive-mode` | `<style id="drive-mode-actions-independent-style">` |
| 382 | `Sürüş` | `   SÜRÜŞ MODU ÜST HIZLI MENÜ - BAĞIMSIZ FINAL` |
| 465 | `drive-mode` | `<script id="drive-mode-actions-independent-js">` |
| 468 | `driveModeToggle` | `    const btn = document.getElementById("driveModeToggle");` |
| 471 | `Normal` | `    // Sürüş modunda buton "Normal" oluyor` |
| 472 | `Normal` | `    if(txt.includes("normal")) return true;` |
| 501 | `route-strip` | `      const routeShell = board.querySelector(".route-strip-shell");` |
| 568 | `Normal` | `       Normal HTML akışındaki yerinde sabit duracak. */` |
| 584 | `driveModeToggle` | `    const btn = document.getElementById("driveModeToggle");` |
| 632 | `Sürüş` | `   SÜRÜŞ / HIZ / RÖTAR SATIRI SABİTLEME` |
| 677 | `Sürüş` | `/* Sürüş butonu */` |
| 678 | `driveModeToggle` | `#driveModeToggle{` |
| 703 | `driveSpeedChip` | `#driveSpeedChip,` |
| 704 | `driveEtaChip` | `#driveEtaChip,` |
| 724 | `driveSpeedChip` | `#driveSpeedChip,` |
| 729 | `driveEtaChip` | `#driveEtaChip,` |
| 768 | `board-head` | `.board-head{` |
| 775 | `board-title` | `.board-title{` |
| 780 | `board-title` | `.board-title h2{` |
| 785 | `driveEtaChip` | `#driveEtaChip *,` |
| 797 | `driveModeToggle` | `  #driveModeToggle{` |
| 805 | `driveSpeedChip` | `  #driveSpeedChip,` |
| 806 | `driveEtaChip` | `  #driveEtaChip,` |
| 815 | `driveSpeedChip` | `  #driveSpeedChip,` |
| 820 | `driveEtaChip` | `  #driveEtaChip,` |
| 840 | `drive-mode` | `<script id="drive-mode-force-toggle-js">` |
| 864 | `drive-mode` | `    document.body.classList.toggle("drive-mode", !!on);` |
| 865 | `drive-mode` | `    document.documentElement.classList.toggle("drive-mode", !!on);` |
| 867 | `driveModeToggle` | `    const btn = document.getElementById("driveModeToggle");` |
| 869 | `Normal` | `      btn.innerHTML = on ? "↩ Normal" : "🚘 Sürüş";` |
| 870 | `Normal` | `      btn.title = on ? "Normal moda geç" : "Sürüş moduna geç";` |
| 876 | `driveEtaChip` | `    try{ if(typeof syncDriveEtaChip === "function") syncDriveEtaChip(); }catch(e){}` |
| 889 | `driveModeToggle` | `    const btn = e.target.closest && e.target.closest("#driveModeToggle");` |
| 910 | `Normal` | `<!-- DRIVE_MODE_MANUAL_NORMAL_GUARD_V20_START -->` |
| 911 | `Normal` | `<script id="drive-mode-manual-normal-guard-v20">` |
| 913 | `Normal` | `  if(window.__DRIVE_MODE_MANUAL_NORMAL_GUARD_V20__) return;` |
| 914 | `Normal` | `  window.__DRIVE_MODE_MANUAL_NORMAL_GUARD_V20__ = true;` |
| 916 | `Normal` | `  const MANUAL_KEY = "driveModeManualNormalGuard:v20";` |
| 921 | `driveModeToggle` | `    return document.getElementById("driveModeToggle");` |
| 927 | `drive-mode` | `    return document.body.classList.contains("drive-mode") \|\|` |
| 928 | `drive-mode` | `           document.documentElement.classList.contains("drive-mode") \|\|` |
| 929 | `Normal` | `           txt.includes("normal");` |
| 970 | `Normal` | `  function forceNormal(){` |
| 971 | `drive-mode` | `    document.body.classList.remove("drive-mode");` |
| 972 | `drive-mode` | `    document.documentElement.classList.remove("drive-mode");` |
| 976 | `Sürüş` | `      b.innerHTML = "🚘 Sürüş";` |
| 977 | `Sürüş` | `      b.title = "Sürüş moduna geç";` |
| 984 | `Normal` | `        detail:{ on:false, source:"manual-normal-guard-v20" }` |
| 990 | `driveModeToggle` | `    const hit = e.target && e.target.closest && e.target.closest("#driveModeToggle");` |
| 1030 | `Normal` | `      forceNormal();` |
| 1040 | `Normal` | `<!-- DRIVE_MODE_MANUAL_NORMAL_GUARD_V20_END -->` |
| 1043 | `voice` | `<!-- DRIVE VOICE MIRROR SCRIPT START -->` |
| 1044 | `voice` | `<script id="drive-voice-mirror-script">` |
| 1046 | `voice` | `  function syncDriveVoiceStats(){` |
| 1047 | `voice` | `    const oldFilled = document.getElementById("voiceSeatFilled");` |
| 1048 | `voice` | `    const oldEmpty  = document.getElementById("voiceSeatEmpty");` |
| 1049 | `voice` | `    const newFilled = document.getElementById("driveVoiceFilled");` |
| 1050 | `voice` | `    const newEmpty  = document.getElementById("driveVoiceEmpty");` |
| 1060 | `voice` | `  function bindDriveVoiceButton(){` |
| 1061 | `btnDeckAI` | `    const fakeBtn = document.getElementById("btnDeckAIDrive");` |
| 1062 | `btnDeckAI` | `    const realBtn = document.getElementById("btnDeckAI");` |
| 1081 | `voice` | `    new MutationObserver(syncDriveVoiceStats).observe(el, {` |
| 1089 | `voice` | `    bindDriveVoiceButton();` |
| 1090 | `voice` | `    syncDriveVoiceStats();` |
| 1091 | `voice` | `    watchNode("voiceSeatFilled");` |
| 1092 | `voice` | `    watchNode("voiceSeatEmpty");` |
| 1094 | `voice` | `    setTimeout(syncDriveVoiceStats, 150);` |
| 1095 | `voice` | `    setTimeout(syncDriveVoiceStats, 600);` |
| 1096 | `voice` | `    setTimeout(syncDriveVoiceStats, 1400);` |
| 1098 | `voice` | `    window.addEventListener("driveModeChanged", syncDriveVoiceStats);` |
| 1099 | `voice` | `    window.addEventListener("resize", syncDriveVoiceStats);` |
| 1109 | `voice` | `<!-- DRIVE VOICE MIRROR SCRIPT END -->` |
| 1111 | `seat-simple` | `<script id="seat-simple-bottom-bar-script">` |
| 1127 | `seat-simple` | `    document.documentElement.classList.remove("seat-simple-mode");` |
| 1128 | `seat-simple` | `    document.body.classList.remove("seat-simple-mode");` |
| 1132 | `sade koltuk moduna dön` | `      if(btn) btn.innerHTML = "💺 Sade koltuk moduna dön";` |
| 1139 | `voice` | `  function openVoice(){` |
| 1141 | `voice` | `      if(window.SeatsVoice && typeof window.SeatsVoice.startDeckAIVoice === "function"){` |
| 1142 | `voice` | `        window.SeatsVoice.startDeckAIVoice();` |
| 1147 | `btnDeckAI` | `    const btn = q("#btnDeckAI") \|\| q("#btnDeckAIDrive");` |
| 1156 | `seat-simple` | `    bar.className = "seat-simple-bottom-bar";` |
| 1158 | `seat-simple` | `      <button type="button" class="seat-simple-bottom-item primary" id="seatSimpleOpenDurak">` |
| 1163 | `seat-simple` | `      <a class="seat-simple-bottom-item" href="{{ url_for('hesap_page') }}">` |
| 1168 | `seat-simple` | `      <a class="seat-simple-bottom-item" href="{{ url_for('consignments_page') }}">` |
| 1173 | `seat-simple` | `      <a class="seat-simple-bottom-item" href="{{ url_for('live_map_page') }}">` |
| 1178 | `Sesli Komut` | `      <button type="button" class="seat-simple-bottom-item warn" id="seatSimpleVoiceBtn" title="Sesli Komut" aria-label="Sesli Komut">` |
| 1180 | `voice` | `        <span class="voice-bottom-text">Sesli<br>Komut</span>` |
| 1194 | `route-flow` | `          const flow = q("#routeStrip") \|\| q(".route-strip-shell") \|\| q(".route-flow-shell");` |
| 1202 | `voice` | `    const voice = q("#seatSimpleVoiceBtn");` |
| 1203 | `voice` | `    if(voice){` |
| 1204 | `voice` | `      voice.addEventListener("click", function(e){` |
| 1208 | `voice` | `        openVoice();` |

### `templates/start_trip.html`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 312 | `Durak Akışı` | `      Sefer başlatıldığında koltuk, hesap, emanet ve durak akışı bu hatta göre açılır.` |

### `templates/ai_console.html`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 7 | `legend` | `<style id="intent-legend-mobile-fix">` |
| 10 | `legend` | `   Sadece #intentLegend alanını etkiler.` |
| 13 | `legend` | `#intentLegend{` |
| 21 | `legend` | `#intentLegend .legend-item{` |
| 34 | `legend` | `#intentLegend .legend-item b{` |
| 45 | `legend` | `#intentLegend .legend-item span{` |
| 51 | `Normal` | `  white-space:normal !important;` |
| 63 | `legend` | `  #intentLegend .legend-item{` |
| 68 | `legend` | `  #intentLegend .legend-item b{` |
| 72 | `legend` | `  #intentLegend .legend-item span{` |
| 477 | `route-strip` | `  .route-strip{` |
| 850 | `legend` | `  .legend-list{` |
| 855 | `legend` | `  .legend-item{` |
| 867 | `legend` | `  .legend-item b{` |
| 1029 | `Normal` | `      <div class="v" id="statMode">Normal</div>` |
| 1030 | `Normal` | `      <div class="s">Normal / Öğretme</div>` |
| 1074 | `Normal` | `            <button type="button" class="mode-btn active" data-mode="normal">Normal kullanım</button>` |
| 1082 | `Boş` | `              <button type="button" class="chip" data-fill="7-8 numarayı boşalt">7-8 numarayı boşalt</button>` |
| 1084 | `Servis` | `              <button type="button" class="chip" data-fill="arka dörtlü servis tamam">arka dörtlü servis tamam</button>` |
| 1086 | `Boş` | `              <button type="button" class="chip" data-fill="kaç boş koltuk var">kaç boş koltuk var</button>` |
| 1091 | `Boş` | `                <textarea id="commandInput" class="cmd-input" placeholder="Komut yaz... örn: 7 ile 8 numarayı boşalt"></textarea>` |
| 1092 | `Sesli Komut` | `                <button type="button" id="micBtn" class="mic-btn" title="Sesli komut">🎤</button>` |
| 1106 | `route-strip` | `              <div class="route-strip">` |
| 1113 | `voice` | `              <div class="flow-card" id="voicePreview">` |
| 1114 | `Sesli Komut` | `                <h3 class="mini-title">Sesli komut önizleme</h3>` |
| 1116 | `voice` | `                <div class="preview-text" id="voicePreviewText">-</div>` |
| 1118 | `voice` | `                  <button type="button" class="btn brand" id="btnVoiceUseRun">Kullan ve çalıştır</button>` |
| 1119 | `voice` | `                  <button type="button" class="btn dark" id="btnVoiceUseOnly">Sadece alana yaz</button>` |
| 1120 | `voice` | `                  <button type="button" class="btn warn" id="btnVoiceRetry">Tekrar dinle</button>` |
| 1121 | `voice` | `                  <button type="button" class="btn ghost" id="btnVoiceCancel">İptal</button>` |
| 1237 | `İniş` | `                <label for="acTo">İniş durağı</label>` |
| 1262 | `Servis` | `                <label for="acService">Servis</label>` |
| 1274 | `Boş` | `                  <option value="">boş</option>` |
| 1275 | `Bay` | `                  <option value="bay">bay</option>` |
| 1276 | `Bay` | `                  <option value="bayan">bayan</option>` |
| 1332 | `Canlı` | `                <p class="section-sub">Canlı akış ve sistem notları</p>` |
| 1346 | `Canlı` | `            <p class="section-sub">AI Console’un aktif seferden aldığı canlı veriler.</p>` |
| 1349 | `Normal` | `            <span class="badge info" id="sideModeBadge">Mod: Normal</span>` |
| 1356 | `Canlı` | `            <h3 class="h">📡 Canlı metrikler</h3>` |
| 1357 | `legend` | `            <div class="legend-list" id="liveStatsList">` |
| 1358 | `legend` | `              <div class="legend-item"><b>Dolu koltuk</b><span id="liveSeatCount">0</span></div>` |
| 1359 | `legend` | `              <div class="legend-item"><b>Ayakta</b><span id="liveStandingCount">0</span></div>` |
| 1360 | `legend` | `              <div class="legend-item"><b>Emanet</b><span id="liveParcelCount">0</span></div>` |
| 1361 | `legend` | `              <div class="legend-item"><b>Toplam yolcu</b><span id="liveTotalPax">0</span></div>` |
| 1362 | `legend` | `              <div class="legend-item"><b>Boş koltuk</b><span id="liveEmptySeats">0</span></div>` |
| 1368 | `legend` | `            <div class="legend-list" id="intentLegend"></div>` |
| 1373 | `legend` | `            <div class="legend-list">` |
| 1374 | `legend` | `              <div class="legend-item"><b>1</b><span>Learned map ara</span></div>` |
| 1375 | `legend` | `              <div class="legend-item"><b>2</b><span>Parser ile intent bul</span></div>` |
| 1376 | `legend` | `              <div class="legend-item"><b>3</b><span>Güven düşükse suggestion ver</span></div>` |
| 1377 | `legend` | `              <div class="legend-item"><b>4</b><span>Riskliyse preview aç</span></div>` |
| 1378 | `legend` | `              <div class="legend-item"><b>5</b><span>Eksikse action form aç</span></div>` |
| 1412 | `Normal` | `    mode: 'normal',` |
| 1425 | `voice` | `    voiceText: '',` |
| 1473 | `voice` | `    voicePreview: $('#voicePreview'),` |
| 1474 | `voice` | `    voicePreviewText: $('#voicePreviewText'),` |
| 1475 | `voice` | `    btnVoiceUseRun: $('#btnVoiceUseRun'),` |
| 1476 | `voice` | `    btnVoiceUseOnly: $('#btnVoiceUseOnly'),` |
| 1477 | `voice` | `    btnVoiceRetry: $('#btnVoiceRetry'),` |
| 1478 | `voice` | `    btnVoiceCancel: $('#btnVoiceCancel'),` |
| 1530 | `legend` | `    intentLegend: $('#intentLegend'),` |
| 1549 | `voice` | `    initVoiceInput();` |
| 1628 | `voice` | `    els.btnVoiceUseRun.addEventListener('click', async () => {` |
| 1629 | `voice` | `      const text = state.voiceText \|\| '';` |
| 1630 | `voice` | `      closeVoicePreview();` |
| 1636 | `voice` | `    els.btnVoiceUseOnly.addEventListener('click', () => {` |
| 1637 | `voice` | `      const text = state.voiceText \|\| '';` |
| 1638 | `voice` | `      closeVoicePreview();` |
| 1644 | `voice` | `    els.btnVoiceRetry.addEventListener('click', () => {` |
| 1645 | `voice` | `      closeVoicePreview();` |
| 1646 | `voice` | `      startVoiceRecognition();` |
| 1649 | `voice` | `    els.btnVoiceCancel.addEventListener('click', closeVoicePreview);` |
| 1656 | `Normal` | `    state.mode = mode === 'teach' ? 'teach' : 'normal';` |
| 1661 | `Normal` | `    addMessage('sys', 'Mod değişti: ${state.mode === 'teach' ? 'Öğretme modu' : 'Normal kullanım'}');` |
| 1701 | `legend` | `    renderIntentLegend();` |
| 1765 | `legend` | `  function renderIntentLegend(){` |
| 1766 | `legend` | `    els.intentLegend.innerHTML = '';` |
| 1769 | `legend` | `      row.className = 'legend-item';` |
| 1774 | `legend` | `      els.intentLegend.appendChild(row);` |
| 1983 | `Boş` | `      els.previewTitle.textContent = 'Boşaltma önizlemesi';` |
| 1991 | `Boş` | `        row.innerHTML = '<span>Kayıt bulunamadı</span><span>Boş koltuk olabilir</span>';` |
| 2009 | `Servis` | `      els.previewTitle.textContent = 'Servis işaretleme önizlemesi';` |
| 2010 | `Servis` | `      els.previewSub.textContent = 'Bu koltuklarda servis alanı aktif olacak.';` |
| 2011 | `Servis` | `      addBadge('Servis mark', 'info');` |
| 2019 | `Servis` | `          <div>${seatRows.find(x => Number(x.seat_no) === Number(no))?.service ? 'Zaten servisli' : 'Servis işaretlenecek'}</div>` |
| 2160 | `Boş` | `        if (!seats.length) throw new Error('Boşaltılacak koltuk bulunamadı.');` |
| 2173 | `Boş` | `          label:'Koltuk boşaltma geri alma',` |
| 2178 | `Boş` | `        addMessage('ok', 'Boşaltma uygulandı.\nSilinen koltuklar: ${(data.deleted \|\| seats).join(', ')}');` |
| 2187 | `Servis` | `        if (!seats.length) throw new Error('Servis işaretlenecek koltuk bulunamadı.');` |
| 2198 | `Servis` | `        addMessage('ok', 'Servis işlendi.\nKoltuklar: ${(data.updated \|\| seats).join(', ')}');` |
| 2314 | `Boş` | `    if (/(bos koltuk\|boş koltuk)/.test(text)) {` |
| 2315 | `Boş` | `      addMessage('info', 'Şu an ${emptySeats} boş koltuk var.');` |
| 2348 | `Servis` | `    if (/(servis)/.test(text) && /(kac\|kaç)/.test(text)) {` |
| 2350 | `Servis` | `      addMessage('info', 'Servis işaretli ${serviceCt} koltuk var.');` |
| 2377 | `Bay` | `    if (/(bayan\|kadin\|kadın)/.test(text) && /(hangi koltuk\|koltuklar)/.test(text)) {` |
| 2378 | `Bay` | `      const rows = seats.filter(x => norm(x.gender \|\| '') === 'bayan').map(x => x.seat_no);` |
| 2379 | `Bay` | `      addMessage('info', rows.length ? 'Bayan görünen koltuklar: ${rows.join(', ')}' : 'Bayan işaretli koltuk yok.');` |
| 2383 | `Bay` | `    if (/(erkek\|bay)/.test(text) && /(hangi koltuk\|koltuklar)/.test(text)) {` |
| 2384 | `Bay` | `      const rows = seats.filter(x => norm(x.gender \|\| '') === 'bay').map(x => x.seat_no);` |
| 2385 | `Bay` | `      addMessage('info', rows.length ? 'Bay görünen koltuklar: ${rows.join(', ')}' : 'Bay işaretli koltuk yok.');` |
| 2454 | `Boş` | `        addMessage('ok', 'Son boşaltma işlemi geri alındı.');` |
| 2467 | `Normal` | `    els.statMode.textContent = state.mode === 'teach' ? 'Öğretme' : 'Normal';` |
| 2468 | `Normal` | `    els.sideModeBadge.textContent = 'Mod: ${state.mode === 'teach' ? 'Öğretme' : 'Normal'}';` |
| 2485 | `voice` | `    closeVoicePreview();` |
| 2580 | `Normal` | `      .normalize('NFKD')` |
| 2599 | `voice` | `  function closeVoicePreview(){` |
| 2600 | `voice` | `    state.voiceText = '';` |
| 2601 | `voice` | `    els.voicePreview.classList.remove('open');` |
| 2602 | `voice` | `    els.voicePreviewText.textContent = '-';` |
| 2616 | `voice` | `  function initVoiceInput(){` |
| 2622 | `Sesli Komut` | `      addMessage('warn', 'Bu cihazda/tarayıcıda sesli komut desteklenmiyor.');` |
| 2646 | `Sesli Komut` | `      addMessage('err', 'Sesli komut hatası: ' + (event.error \|\| 'bilinmiyor'));` |
| 2656 | `voice` | `      state.voiceText = text;` |
| 2657 | `voice` | `      els.voicePreviewText.textContent = text;` |
| 2658 | `voice` | `      els.voicePreview.classList.add('open');` |
| 2659 | `Sesli Komut` | `      addMessage('info', 'Sesli komut algılandı. Önizlemeden onaylayabilirsin.');` |
| 2668 | `voice` | `      startVoiceRecognition();` |
| 2672 | `voice` | `  function startVoiceRecognition(){` |
| 2674 | `voice` | `      closeVoicePreview();` |

### `templates/route_schedule_edit.html`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 1234 | `Boş` | `          İlk durakta segment km boş kalabilir.` |
| 1306 | `Durak Akışı` | `            <br>• Durak Akışı kutusunda plan saat olarak` |

### `templates/trip_report.html`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 104 | `legend` | `  .legend{` |
| 546 | `legend` | `      <div class="legend">` |
| 617 | `Bay` | `  if(g === "bay") return "Bay";` |
| 618 | `Bay` | `  if(g === "bayan") return "Bayan";` |
| 756 | `Boş` | `  return h.active ? "Son durum: koltuk seferde dolu görünüyor." : "Son durum: koltuk boş / yolcu inmiş görünüyor.";` |
| 799 | `İniş` | `        title = "🟣 İniş durağı değişti";` |
| 817 | `İniş` | `      <div class="seat-stat"><div class="k">İniş</div><div class="v">${h.offload_count \|\| 0}</div></div>` |
| 1422 | `legend` | `  .report-wrap .legend{` |
| 1477 | `legend` | `    .report-wrap .legend{` |

### `templates/report_archive.html`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 471 | `Boş` | `        <div class="empty-title">Arşiv boş</div>` |

### `templates/rehber.html`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 743 | `voice` | `  .guide-voice-list{` |
| 749 | `voice` | `  .guide-voice-item{` |
| 764 | `voice` | `  .guide-voice-item p{` |
| 1384 | `voice` | `.guide-voice-list{` |
| 1392 | `voice` | `.guide-voice-item{` |
| 1399 | `voice` | `.guide-voice-item .cmd{` |
| 1413 | `voice` | `.guide-voice-item p{` |
| 1542 | `voice` | `  .guide-voice-item p,` |
| 1547 | `voice` | `  .guide-voice-item{` |
| 1786 | `voice` | `.guide-voice-list{` |
| 1790 | `voice` | `.guide-voice-item{` |
| 1794 | `voice` | `.guide-voice-item:hover{` |
| 1857 | `voice` | `  .guide-voice-list{` |
| 2185 | `voice` | `.guide-voice-item p{` |
| 2290 | `Sesli Komut` | `          Koltuk, durak, bagaj, emanet, hesap ve sesli komutlar. Hepsi tek, sade ve güçlü bir ekranda.` |
| 2311 | `Bagaj` | `          <div class="hero-floating f3">🧳 Bagaj kontrolü</div>` |
| 2326 | `Bagaj` | `          <p>Yolcu, cinsiyet, iniş durağı, servis ve bagaj bilgisi aynı akışta görünür.</p>` |
| 2333 | `Canlı` | `          <h3>Canlı durak. İnişleri kaçırma.</h3>` |
| 2334 | `Canlı` | `          <p>Seçili, canlı ve sıradaki durak bilgisi sahada hızlı karar aldırır.</p>` |
| 2336 | `Canlı` | `            <img src="{{ url_for('static', filename='img/rehber-durak-akisi-card.png') }}" alt="Canlı durak">` |
| 2341 | `Sesli Komut` | `          <h3>Sesli komut. Ekrana daha az bak.</h3>` |
| 2342 | `Bagaj` | `          <p>“Kaç yolcu var”, “Rötar kaç”, “Bu durakta bagaj var mı” gibi kısa komutlarla bilgi al.</p>` |
| 2344 | `Sesli Komut` | `            <img src="{{ url_for('static', filename='img/rehber-voice-command-card.png') }}" alt="Sesli komut">` |
| 2372 | `Bagaj` | `              <span>Koltuk, durak, bagaj, servis ve hesap takibi.</span>` |
| 2376 | `Sesli Komut` | `              <span>Sahada kullanılabilecek kısa sesli komut.</span>` |
| 2379 | `Canlı` | `              <b>Canlı</b>` |
| 2380 | `Sıradaki` | `              <span>Durak, sıradaki nokta ve rötar bilgisi.</span>` |
| 2410 | `Bagaj` | `            <p>Koltuk planı üzerinden biniş, iniş, cinsiyet, ödeme, servis ve bagaj bilgileri düzenli tutulur.</p>` |
| 2414 | `Servis` | `              <span>Servis işle</span>` |
| 2415 | `Bagaj` | `              <span>Bagaj gör</span>` |
| 2425 | `Canlı` | `            <small>Canlı Durak</small>` |
| 2426 | `Sıradaki` | `            <h3>Sıradaki nokta hep belli.</h3>` |
| 2427 | `Canlı` | `            <p>Canlı durak, yaklaşan durak, rötar ve iniş yoğunluğu daha görünür olur.</p>` |
| 2429 | `Canlı` | `              <span>Canlı durak</span>` |
| 2430 | `Sıradaki` | `              <span>Sıradaki durak</span>` |
| 2432 | `İniş` | `              <span>İniş özeti</span>` |
| 2436 | `Canlı` | `            <img src="{{ url_for('static', filename='img/rehber-durak-akisi.png') }}" alt="Canlı durak takibi">` |
| 2442 | `Sesli Komut` | `            <small>Sesli Komut</small>` |
| 2448 | `Bagaj` | `              <span>Bagaj var mı</span>` |
| 2453 | `Sesli Komut` | `            <img src="{{ url_for('static', filename='img/rehber-voice-command.png') }}" alt="Sesli komut">` |
| 2498 | `Bagaj` | `              <div class="guide-line"><b>Koltuk ekranını kullan</b><span>Koltuk planı ekranında yolcu ekleme, indirme, ayakta yolcu, servis, durak ve bagaj işlemleri aynı ekrandan yapılır.</span></div>` |
| 2503 | `voice` | `          <article class="guide-card guide-searchable" id="guideVoiceSection" data-guide-cat="sesli">` |
| 2507 | `Sesli Komut` | `                <h3>Sesli Komutlar</h3>` |
| 2514 | `voice` | `            <div class="guide-voice-list">` |
| 2515 | `voice` | `              <div class="guide-voice-item"><div class="cmd">Kaç yolcu var</div><p>Toplam yolcu sayısını, oturan ve ayakta durumuyla birlikte söyler.</p></div>` |
| 2516 | `voice` | `              <div class="guide-voice-item"><div class="cmd">Ayakta kaç kişi var</div><p>Ayakta yolcu sayısını ve ayakta tahsilatı söyler.</p></div>` |
| 2517 | `Seçili durak` | `              <div class="guide-voice-item"><div class="cmd">Hangi duraktayız</div><p>Canlı veya seçili durak bilgisini verir.</p></div>` |
| 2518 | `voice` | `              <div class="guide-voice-item"><div class="cmd">Rötar kaç</div><p>Bir sonraki saatli durağın gecikmesini söyler.</p></div>` |
| 2519 | `voice` | `              <div class="guide-voice-item"><div class="cmd">Bir sonraki durak</div><p>Sıradaki saatli noktayı sesli söyler.</p></div>` |
| 2523 | `voice` | `            <div class="guide-voice-list">` |
| 2524 | `voice` | `              <div class="guide-voice-item"><div class="cmd">Alaşehir kaç yolcu var</div><p>Belirtilen durakta inecek yolcu özetini söyler.</p></div>` |
| 2525 | `Seçili durak` | `              <div class="guide-voice-item"><div class="cmd">Bu durakta işlem var mı</div><p>Seçili durakta yolcu, bagaj, emanet ve servis durumunu özetler.</p></div>` |
| 2526 | `Seçili durak` | `              <div class="guide-voice-item"><div class="cmd">Bu durakta kimler inecek</div><p>Seçili duraktaki iniş durumunu sesli anlatır.</p></div>` |
| 2527 | `Seçili durak` | `              <div class="guide-voice-item"><div class="cmd">Bu durakta bagaj var mı</div><p>Seçili durak için bagaj bilgisini söyler.</p></div>` |
| 2528 | `voice` | `              <div class="guide-voice-item"><div class="cmd">Durak seç Alaşehir</div><p>Seçili durağı değiştirir.</p></div>` |
| 2529 | `Seçili durak` | `              <div class="guide-voice-item"><div class="cmd">İnecekleri indir</div><p>Seçili duraktaki indirme akışını başlatır.</p></div>` |
| 2544 | `Boş` | `              <div class="guide-line"><b>Toplu giriş</b><span>Birden fazla boş koltuğu seç, toplu giriş ekranını aç, bilgileri tek seferde işle.</span></div>` |
| 2546 | `Sesli Komut` | `              <div class="guide-line"><b>Servis işaretleme</b><span>Koltuk seçerek ya da sesli komutla servis bilgisini işaretle.</span></div>` |
| 2548 | `Bagaj` | `              <div class="guide-line"><b>Bagaj ve emanet kontrolü</b><span>İniş durağında yolcu özetine ek olarak bagaj ve emanet bilgisini kontrol et.</span></div>` |
| 2556 | `Sürüş` | `                <h3>Sürüşte Kullanım</h3>` |
| 2557 | `Sürüş` | `                <div class="guide-card-sub">Sürüş modu daha sade, daha hızlı ve sahaya uygun görünüm sunar.</div>` |
| 2562 | `Sürüş` | `              <div class="guide-line"><b>Sürüş modu ne işe yarar</b><span>Ekranı sadeleştirir. En gerekli alanları öne çıkarır. Sesli komut kullanımı daha rahat olur.</span></div>` |
| 2563 | `Sürüş` | `              <div class="guide-line"><b>Sesli komut butonu</b><span>Sürüş modunda büyük mor buton üzerinden hızlı sesli komut kullanılabilir.</span></div>` |
| 2564 | `Sürüş` | `              <div class="guide-line"><b>Hız ve rötar kutusu</b><span>Üst alanda anlık hız ve zaman durumu özetlenir. Sürüşte takip kolaylaşır.</span></div>` |
| 2565 | `Durak Akışı` | `              <div class="guide-line"><b>Canlı durak ve sıradaki durak</b><span>Durak akışı kutuları ile aktif nokta ve yaklaşan nokta hızlıca takip edilir.</span></div>` |
| 2566 | `Sürüş` | `              <div class="guide-line"><b>Öneri</b><span>Sürüşte komutları kısa ver: “Kaç yolcu var”, “Hangi duraktayız”, “Rötar kaç” gibi.</span></div>` |
| 2581 | `Sesli Komut` | `              <div class="guide-line"><b>Sesli komut dinliyor ama işlem yapmıyorsa</b><span>Komutu daha kısa söyle. Durak adını ve koltuk numarasını net telaffuz et.</span></div>` |
| 2583 | `Seçili durak` | `              <div class="guide-line"><b>Durak yanlış görünüyorsa</b><span>Seçili durak ile canlı durak durumunu karşılaştır. Gerekirse manuel durak seç.</span></div>` |
| 2584 | `Canlı` | `              <div class="guide-line"><b>GPS çalışmıyorsa</b><span>Konum izni, internet bağlantısı ve canlı takip açık mı kontrol et.</span></div>` |
| 2607 | `Bagaj` | `              <div class="guide-chip">9. Bu durakta bagaj var mı</div>` |
| 2613 | `Bagaj` | `              <p>Mikrofona bastıktan sonra kısa ve tek komut ver. Uzun cümle yerine net ifade kullan: “Rötar kaç”, “Durak seç Alaşehir”, “Bu durakta bagaj var mı”.</p>` |

### `templates/live_map.html`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 6 | `Canlı` | `  <title>Canlı Harita</title>` |
| 226 | `legend` | `    .legend{` |
| 233 | `legend` | `    .legend span{` |
| 960 | `legend` | `body.map-fullscreen-mode .legend{` |
| 1024 | `Canlı` | `/* Canlı harita popup kompakt görünüm */` |
| 1613 | `Normal` | `/* Normal mod */` |
| 1727 | `Canlı` | `      <a class="back" href="{{ url_for('continue_trip') }}">← Canlı Akış</a>` |
| 1729 | `Canlı` | `        <h1>Canlı Harita</h1>` |
| 1736 | `Canlı` | `        <small>Canlı durak</small>` |
| 1741 | `Sıradaki` | `        <small>Sıradaki işlem</small>` |
| 1746 | `legend` | `    <div class="legend">` |
| 1747 | `Canlı` | `      <span>🔴 Canlı</span>` |
| 1748 | `Sıradaki` | `      <span>🟡 Sıradaki işlem</span>` |
| 1797 | `Sıradaki` | `          <div class="next-ops-title">Sıradaki İşlemler</div>` |
| 1871 | `Canlı` | `            <svg viewBox="0 0 300 150" xmlns="http://www.w3.org/2000/svg" aria-label="Canlı otobüs">` |
| 2032 | `Canlı` | `      if(kind === "live") stateText = "Canlı Durak";` |
| 2033 | `Sıradaki` | `      else if(kind === "next") stateText = "Sıradaki İşlem";` |
| 2048 | `Bagaj` | `        if(bag) parts.push('${bag} bagaj');` |
| 2072 | `Bagaj` | `              <small>Bagaj</small>` |
| 2089 | `Bagaj` | `            <a class="bag" href="{{ url_for('continue_trip') }}?stop=${encodeURIComponent(stop.name)}">Bagaj</a>` |
| 2402 | `Bagaj` | `      if(bag) parts.push('${bag} bagaj');` |
| 2518 | `Bagaj` | `      if(bag) parts.push('${bag} bagaj');` |
| 2796 | `voice` | `<!-- VOICE_MAP_FULLSCREEN_PATCH_START -->` |
| 2797 | `voice` | `<style id="voice-map-fullscreen-style">` |
| 2798 | `voice` | `  html.voice-map-fullscreen,` |
| 2799 | `voice` | `  body.voice-map-fullscreen{` |
| 2808 | `voice` | `  body.voice-map-fullscreen #map{` |
| 2820 | `voice` | `  body.voice-map-fullscreen .leaflet-control-container{` |
| 2825 | `voice` | `  body.voice-map-fullscreen .topbar,` |
| 2826 | `voice` | `  body.voice-map-fullscreen .page-header,` |
| 2827 | `voice` | `  body.voice-map-fullscreen .map-header,` |
| 2828 | `voice` | `  body.voice-map-fullscreen .live-map-header,` |
| 2829 | `voice` | `  body.voice-map-fullscreen .map-hero,` |
| 2830 | `voice` | `  body.voice-map-fullscreen .map-summary,` |
| 2831 | `voice` | `  body.voice-map-fullscreen .bottom-nav,` |
| 2832 | `voice` | `  body.voice-map-fullscreen .bottom-bar{` |
| 2836 | `voice` | `  body.voice-map-fullscreen main,` |
| 2837 | `voice` | `  body.voice-map-fullscreen .map-shell,` |
| 2838 | `voice` | `  body.voice-map-fullscreen .live-map-shell,` |
| 2839 | `voice` | `  body.voice-map-fullscreen .content{` |
| 2848 | `voice` | `  #voiceMapFullscreenExit{` |
| 2869 | `voice` | `  #voiceMapFullscreenExit:active{` |
| 2874 | `voice` | `<script id="voice-map-fullscreen-script">` |
| 2884 | `voice` | `  document.documentElement.classList.add("voice-map-fullscreen");` |
| 2885 | `voice` | `  document.body.classList.add("voice-map-fullscreen");` |
| 2888 | `voice` | `    if(document.getElementById("voiceMapFullscreenExit")) return;` |
| 2891 | `voice` | `    btn.id = "voiceMapFullscreenExit";` |
| 2923 | `voice` | `<!-- VOICE_MAP_FULLSCREEN_PATCH_END -->` |

### `templates/onboarding.html`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 200 | `Canlı` | `        <div class="slide"><img src="/static/img/onboarding/slides/onboarding_4.png" alt="Canlı Konum Takibi"></div>` |
| 203 | `Sesli Komut` | `        <div class="slide"><img src="/static/img/onboarding/slides/onboarding_7.png" alt="Sesli Komut Desteği"></div>` |

### `templates/continue_trip.html`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 6 | `Durak Akışı` | `  <title>Canlı Durak Akışı</title>` |
| 99 | `Sesli Komut` | `      <a class="brand-action" href="{{ url_for('seats_page') }}?drive=1" aria-label="Sesli komut">` |
| 105 | `Canlı` | `      <img class="hero-bus-img" src="{{ url_for('static', filename='img/live-hero-bus.png', v='1') }}" alt="Canlı durak otobüs görseli">` |
| 108 | `Durak Akışı` | `      <h1 class="hero-title">Canlı Durak Akışı</h1>` |
| 137 | `Bay` | `          <span class="male">Bay {{ live_summary.male_count or 0 }}</span>` |
| 138 | `Bay` | `          <span class="female">Bayan {{ live_summary.female_count or 0 }}</span>` |
| 157 | `Canlı` | `        <div class="card live live-summary-trigger" id="liveCurrentCard" role="button" tabindex="0" aria-label="Canlı durak özetini aç">` |
| 164 | `Canlı` | `            <span class="status-pill live">{{ live_current.status or "Canlı" }}</span>` |
| 184 | `Bagaj` | `            <button class="metric metric-action" type="button" id="liveBagajMetric" data-kind="bagaj" aria-label="Bu durakta indirilecek bagajları göster">` |
| 185 | `Bagaj` | `              <small>Bagaj</small>` |
| 186 | `Bagaj` | `              <b id="liveBagajCount">{{ live_current.bagaj_count or 0 }}</b>` |
| 232 | `Bagaj` | `              <small>Bagaj</small>` |
| 233 | `Bagaj` | `              <b>{{ stop.bagaj_label }}</b>` |
| 249 | `Canlı` | `          <div class="sheet-kicker" id="liveStopSheetKicker">Canlı durak</div>` |
| 439 | `voice` | `<script src="/static/seats/voice-tts.js?v=continue-tts-bridge-1"></script>` |
| 447 | `Bagaj` | `      <div class="bag-viewer-kicker">Bagaj fotoğrafı</div>` |
| 456 | `Bagaj` | `      <img class="bag-viewer-img" id="bagViewerImg" src="" alt="Bagaj fotoğrafı">` |
| 499 | `Bagaj` | `    liveBagajCount: {{ (live_current.bagaj_count if live_current and live_current.bagaj_count is defined else 0) \| tojson \| safe }},` |

### `templates/seats_parts/modals.html`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 12 | `İniş` | `        <span>İniş Yeri</span>` |
| 29 | `Bay` | `        <label><input type="radio" name="gender" value="bay"> Bay</label>` |
| 30 | `Bay` | `        <label><input type="radio" name="gender" value="bayan"> Bayan</label>` |
| 31 | `Boş` | `        <label><input type="radio" name="gender" value=""> Boş</label>` |
| 37 | `Servis` | `      <label><input type="checkbox" id="service"> Servis kullanacak</label>` |
| 41 | `Bagaj` | `      <button class="btn primary" type="button" id="btnBagAdd">🧳 Bagaj Ekle</button>` |
| 42 | `Bagaj` | `      <button class="btn dark" type="button" id="btnBagView">📸 Bagaj Gör</button>` |
| 51 | `Servis` | `        <span>Servis Notu</span>` |
| 71 | `Boş` | `    <button class="btn danger" type="button" id="btnSeatOffload">İniş (Boşalt)</button>` |
| 109 | `Servis` | `      <label><input type="checkbox" id="bulkService"> Servis</label>` |
| 112 | `Boş` | `    <div class="muted">Çoklu seçim açıksa koltukları elle seçersin. Kapalıysa sistem boş koltuklardan yerleştirir.</div>` |

### `templates/seats_parts/topbar.html`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 22 | `mini-chip` | `        <div class="mini-chip">📍 <span>Durak</span> <b id="topLiveStop">—</b></div>` |
| 23 | `mini-chip` | `        <div class="mini-chip">🚦 <span>Hız</span> <b id="topSpeed">0 km/h</b></div>` |
| 24 | `mini-chip` | `        <div class="mini-chip">🕒 <span>Saat</span> <b id="topClock">--:--</b></div>` |
| 25 | `mini-chip` | `        <div class="mini-chip">🎯 <span>Doluluk</span> <b id="topOcc">0%</b></div>` |

### `templates/seats_parts/stats.html`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 7 | `Boş` | `      <div class="k">Boş Koltuk</div>` |
| 19 | `Servis` | `      <div class="k">Servis</div>` |

### `templates/seats_parts/route_flow.html`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 1 | `route-strip` | `<div class="route-strip-shell">` |
| 2 | `route-strip` | `  <div class="route-strip-head">` |
| 3 | `Durak Akışı` | `    <div class="route-strip-title">Durak Akışı</div>` |
| 5 | `route-strip` | `    <div class="route-strip-meta">` |
| 8 | `Canlı` | `        <span class="route-mini-label">Canlı:</span>` |
| 15 | `Sıradaki` | `        <span class="route-mini-label">Sıradaki:</span>` |
| 21 | `voice` | `      <button id="nightVoiceToggle" class="night-voice-toggle" type="button" title="Sesli robot">🔊 Ses Açık</button>` |
| 25 | `route-strip` | `  <div class="route-strip" id="routeStrip">` |
| 26 | `route-stop` | `    <div class="route-stop active">` |

### `templates/seats_parts/deck.html`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 1 | `board-stage` | `<div class="board-stage">` |
| 14 | `Servis` | `                    <span class="svc-badge" title="Servis">🚌</span>` |
| 15 | `Bagaj` | `                    <span class="bag-badge" title="Bagaj"><span class="bag-dir"></span><span class="bag-count">0</span></span>` |

### `templates/seats_parts/offload_confirm.html`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 177 | `Seçili durak` | `        <p class="offload-small">Seçili durak işlemi yapılacak.</p>` |
| 226 | `Seçili durak` | `    stopEl.textContent = stop \|\| "seçili durak";` |

### `static/seats/seats.css`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 133 | `mini-chip` | `  .mini-chip{` |
| 150 | `mini-chip` | `  .mini-chip b{` |
| 182 | `voice` | `  .voice-command-btn:hover{` |
| 286 | `board-head` | `  .board-head{` |
| 294 | `board-title` | `  .board-title{` |
| 317 | `board-title` | `  .board-title h2{` |
| 325 | `board-title` | `  .board-title small{` |
| 331 | `board-head` | `  .board-head-right{` |
| 339 | `voice` | `  .voice-row{` |
| 347 | `voice` | `  .voice-command-btn{` |
| 370 | `voice` | `  .voice-command-btn.listening{` |
| 375 | `voice` | `  .voice-state{` |
| 389 | `legend` | `  .legend{` |
| 396 | `legend` | `  .legend .mini-chip{` |
| 402 | `selected-stop` | `  .selected-stop-chip{` |
| 419 | `route-strip` | `  .route-strip-shell{` |
| 428 | `route-strip` | `  .route-strip-head{` |
| 437 | `route-strip` | `  .route-strip-title{` |
| 443 | `route-strip` | `  .route-strip-meta{` |
| 464 | `route-strip` | `  .route-strip{` |
| 472 | `route-strip` | `  .route-strip::-webkit-scrollbar{ display:none; }` |
| 474 | `route-stop` | `  .route-stop{` |
| 490 | `route-stop` | `  .route-stop .name{` |
| 497 | `route-stop` | `  .route-stop .meta{` |
| 503 | `route-stop` | `  .route-stop .extra{` |
| 509 | `route-stop` | `  .route-stop .extra-line{` |
| 518 | `route-stop` | `  .route-stop .extra-k{` |
| 524 | `route-stop` | `  .route-stop .extra-v{` |
| 531 | `route-stop` | `  .route-stop.active{` |
| 539 | `route-stop` | `  .route-stop.done{` |
| 543 | `board-stage` | `  .board-stage{` |
| 1368 | `board-stage` | `    .board-stage{` |
| 1435 | `mini-chip` | `    .mini-chip{` |
| 1458 | `board-head` | `    .board-head{` |
| 1463 | `board-title` | `    .board-title h2{` |
| 1467 | `board-head` | `    .board-head-right{` |
| 1473 | `voice` | `    .voice-row{` |
| 1478 | `voice` | `    .voice-command-btn{` |
| 1487 | `voice` | `    .voice-state{` |
| 1493 | `legend` | `    .legend{` |
| 1498 | `route-strip` | `    .route-strip-shell{` |
| 1503 | `route-stop` | `    .route-stop{` |
| 1509 | `board-stage` | `    .board-stage{` |
| 1571 | `voice` | `    .voice-command-btn{` |
| 1577 | `voice` | `    .voice-state{` |
| 1582 | `board-stage` | `    .board-stage{` |
| 1586 | `route-stop` | `    .route-stop{` |
| 1595 | `route-stop` | `.route-stop.live-danger{` |
| 1605 | `route-stop` | `.route-stop.live-danger .name,` |
| 1606 | `route-stop` | `.route-stop.live-danger .meta,` |
| 1607 | `route-stop` | `.route-stop.live-danger .extra-k,` |
| 1608 | `route-stop` | `.route-stop.live-danger .extra-v{` |
| 1623 | `route-stop` | `.route-stop.next-warning{` |
| 1632 | `route-stop` | `.route-stop.next-warning .name,` |
| 1633 | `route-stop` | `.route-stop.next-warning .meta,` |
| 1634 | `route-stop` | `.route-stop.next-warning .extra-k,` |
| 1635 | `route-stop` | `.route-stop.next-warning .extra-v{` |
| 1639 | `route-stop` | `.route-stop.flow-green{` |
| 1687 | `Canlı` | `  /* Üst canlı bilgiler 2 sütun küçük chip */` |
| 1694 | `mini-chip` | `  .route-live-row .mini-chip{` |
| 1745 | `Boş` | `  /* Koltuk kartının üst boşluğunu azalt */` |
| 1751 | `board-head` | `  .board-head{` |
| 1761 | `board-title` | `  .board-title h2{` |
| 1765 | `board-title` | `  .board-title small{` |
| 1769 | `selected-stop` | `  .selected-stop-chip{` |
| 1775 | `Sesli Komut` | `  /* Sesli komut ve legend kısmı daha kompakt */` |
| 1776 | `board-head` | `  .board-head-right{` |
| 1780 | `voice` | `  .voice-row{` |
| 1784 | `voice` | `  .voice-command-btn{` |
| 1789 | `voice` | `  .voice-state{` |
| 1794 | `legend` | `  .legend{` |
| 1798 | `legend` | `  .legend .mini-chip{` |
| 1804 | `Durak Akışı` | `  /* Durak akışı daha yukarı ve daha kompakt */` |
| 1805 | `route-strip` | `  .route-strip-shell{` |
| 1812 | `route-strip` | `  .route-strip-head{` |
| 1816 | `route-strip` | `  .route-strip-title{` |
| 1825 | `route-stop` | `  .route-stop{` |
| 1832 | `board-stage` | `  .board-stage{` |
| 1856 | `board-title` | `  .board-title h2{` |
| 1860 | `voice` | `  .voice-command-btn{` |
| 1864 | `route-stop` | `  .route-stop{` |
| 1871 | `Sürüş` | `   SÜRÜŞ MODU` |
| 1875 | `driveModeToggle` | `#driveModeToggle{` |
| 1892 | `driveModeToggle` | `body.drive-mode #driveModeToggle{` |
| 1896 | `drive-mode` | `body.drive-mode .topbar,` |
| 1897 | `drive-mode` | `body.drive-mode .status-row,` |
| 1898 | `drive-mode` | `body.drive-mode .panel-card{` |
| 1902 | `drive-mode` | `body.drive-mode .seats-shell{` |
| 1908 | `drive-mode` | `body.drive-mode .layout{` |
| 1912 | `drive-mode` | `body.drive-mode .board-card{` |
| 1918 | `drive-mode` | `body.drive-mode .board-head{` |
| 1926 | `drive-mode` | `body.drive-mode .board-kicker,` |
| 1927 | `drive-mode` | `body.drive-mode .board-title h2,` |
| 1928 | `drive-mode` | `body.drive-mode .board-title small,` |
| 1929 | `legend` | `body.drive-mode .legend{` |
| 1933 | `selected-stop` | `body.drive-mode .selected-stop-chip{` |
| 1939 | `drive-mode` | `body.drive-mode .board-head-right{` |
| 1944 | `voice` | `body.drive-mode .voice-row{` |
| 1949 | `voice` | `body.drive-mode .voice-command-btn{` |
| 1957 | `voice` | `body.drive-mode .voice-state{` |
| 1961 | `route-strip` | `body.drive-mode .route-strip-shell{` |
| 1968 | `route-strip` | `body.drive-mode .route-strip-head{` |
| 1972 | `route-strip` | `body.drive-mode .route-strip-title{` |
| 1976 | `drive-mode` | `body.drive-mode .route-pill{` |
| 1982 | `route-stop` | `body.drive-mode .route-stop{` |
| 1989 | `drive-mode` | `body.drive-mode .board-stage{` |
| 1995 | `driveModeToggle` | `  #driveModeToggle{` |
| 2003 | `drive-mode` | `  body.drive-mode .seats-shell{` |
| 2007 | `drive-mode` | `  body.drive-mode .board-card{` |
| 2012 | `drive-mode` | `  body.drive-mode .board-head{` |
| 2017 | `drive-mode` | `  body.drive-mode .board-head-right{` |
| 2021 | `voice` | `  body.drive-mode .voice-row{` |
| 2026 | `selected-stop` | `  body.drive-mode .selected-stop-chip{` |
| 2033 | `voice` | `  body.drive-mode .voice-command-btn{` |
| 2038 | `route-strip` | `  body.drive-mode .route-strip-shell{` |
| 2043 | `route-stop` | `  body.drive-mode .route-stop{` |
| 2048 | `drive-mode` | `  body.drive-mode .board-stage{` |
| 2055 | `Sürüş` | `   SÜRÜŞ MODU İNCE AYAR v2` |
| 2056 | `Durak Akışı` | `   Daha temiz üst alan + düzgün durak akışı + okunaklı koltuk yazıları` |
| 2059 | `Sürüş` | `/* Sürüş modu ana ekranı daha sıkı */` |
| 2060 | `drive-mode` | `body.drive-mode{` |
| 2064 | `Normal` | `/* Normal butonu tarayıcı üst çubuğuna çok yapışmasın */` |
| 2065 | `driveModeToggle` | `body.drive-mode #driveModeToggle{` |
| 2075 | `Sürüş` | `/* Sürüş modunda ana kart ekrana tam otursun */` |
| 2076 | `drive-mode` | `body.drive-mode .seats-shell{` |
| 2080 | `drive-mode` | `body.drive-mode .board-card{` |
| 2086 | `Seçili durak` | `/* Üst başlık alanı: seçili durak + sesli komut */` |
| 2087 | `drive-mode` | `body.drive-mode .board-head{` |
| 2094 | `Seçili durak` | `/* Seçili durak rozeti daha net */` |
| 2095 | `selected-stop` | `body.drive-mode .selected-stop-chip{` |
| 2108 | `Sürüş` | `/* Sesli komut butonu sürüş modunda daha kullanışlı */` |
| 2109 | `voice` | `body.drive-mode .voice-row{` |
| 2113 | `voice` | `body.drive-mode .voice-command-btn{` |
| 2123 | `Durak Akışı` | `/* Durak akışı kutusu daha profesyonel */` |
| 2124 | `route-strip` | `body.drive-mode .route-strip-shell{` |
| 2134 | `route-strip` | `body.drive-mode .route-strip-head{` |
| 2142 | `route-strip` | `body.drive-mode .route-strip-title{` |
| 2148 | `route-strip` | `body.drive-mode .route-strip-meta{` |
| 2153 | `drive-mode` | `body.drive-mode .route-pill{` |
| 2161 | `route-strip` | `body.drive-mode .route-strip{` |
| 2169 | `Sürüş` | `/* Sürüş modunda durak kartları daha okunaklı */` |
| 2170 | `route-stop` | `body.drive-mode .route-stop{` |
| 2177 | `route-stop` | `body.drive-mode .route-stop .name{` |
| 2186 | `route-stop` | `body.drive-mode .route-stop .meta{` |
| 2194 | `route-stop` | `body.drive-mode .route-stop .extra-line{` |
| 2198 | `route-stop` | `body.drive-mode .route-stop.active{` |
| 2203 | `drive-mode` | `body.drive-mode .board-stage{` |
| 2209 | `Boş` | `/* Koltuk çevresindeki dış boşluğu azalt */` |
| 2210 | `drive-mode` | `body.drive-mode .deck{` |
| 2216 | `drive-mode` | `body.drive-mode .label{` |
| 2229 | `drive-mode` | `body.drive-mode .cell{` |
| 2233 | `Bagaj` | `/* Bagaj/iniş rozetleri koltuk üstünde daha düzgün dursun */` |
| 2234 | `drive-mode` | `body.drive-mode .bag-badge{` |
| 2242 | `drive-mode` | `body.drive-mode .stop-badge{` |
| 2251 | `drive-mode` | `body.drive-mode .fab-column{` |
| 2257 | `drive-mode` | `body.drive-mode .fab{` |
| 2266 | `driveModeToggle` | `  body.drive-mode #driveModeToggle{` |
| 2274 | `drive-mode` | `  body.drive-mode .board-head{` |
| 2278 | `selected-stop` | `  body.drive-mode .selected-stop-chip{` |
| 2285 | `voice` | `  body.drive-mode .voice-command-btn{` |
| 2292 | `route-strip` | `  body.drive-mode .route-strip-title{` |
| 2296 | `drive-mode` | `  body.drive-mode .route-pill{` |
| 2302 | `route-stop` | `  body.drive-mode .route-stop{` |
| 2308 | `route-stop` | `  body.drive-mode .route-stop .name{` |
| 2312 | `route-stop` | `  body.drive-mode .route-stop .meta,` |
| 2313 | `route-stop` | `  body.drive-mode .route-stop .extra-line{` |
| 2317 | `drive-mode` | `  body.drive-mode .board-stage{` |
| 2321 | `drive-mode` | `  body.drive-mode .label{` |
| 2330 | `driveModeToggle` | `  body.drive-mode #driveModeToggle{` |
| 2337 | `selected-stop` | `  body.drive-mode .selected-stop-chip{` |
| 2342 | `voice` | `  body.drive-mode .voice-command-btn{` |
| 2348 | `route-stop` | `  body.drive-mode .route-stop{` |
| 2352 | `drive-mode` | `  body.drive-mode .board-stage{` |
| 2359 | `Sürüş` | `   BAGAJ BALONU + SÜRÜŞ MODU KOLTUK SIKIŞTIRMA` |
| 2394 | `Bagaj` | `/* Bagaj yön ikonları fazla büyüyüp numarayı kapatmasın */` |
| 2410 | `Boş` | `/* Bagaj rozetinin çıkacağı yer için üst boşluk */` |
| 2415 | `Sürüş` | `/* Sürüş modunda çiftli koltuklar biraz yaklaşsın */` |
| 2416 | `drive-mode` | `body.drive-mode{` |
| 2421 | `Sürüş` | `/* Sürüş modunda bagaj balonu daha kontrollü */` |
| 2422 | `drive-mode` | `body.drive-mode .seat .bag-badge{` |

### `static/seats/voice-tts.js`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 2 | `voice` | `   SEATS UNIFIED VOICE MODULE` |
| 8 | `voice` | `  if(window.__SeatsVoiceUnifiedReady) return;` |
| 9 | `voice` | `  window.__SeatsVoiceUnifiedReady = true;` |
| 70 | `voice` | `      const voices = speechSynthesis.getVoices ? speechSynthesis.getVoices() : [];` |
| 71 | `voice` | `      const trVoice = voices.find(v =>` |
| 76 | `voice` | `      if(trVoice) u.voice = trVoice;` |
| 87 | `voice` | `    const nightBtn = document.getElementById("nightVoiceToggle");` |
| 90 | `voice` | `      nightBtn.dataset.voiceOn = on ? "1" : "0";` |
| 91 | `Durak Akışı` | `      nightBtn.title = on ? "Durak akışı sesi açık" : "Durak akışı sesi kapalı";` |
| 94 | `Sessiz` | `        : '<span class="nv-ico">🔇</span><span>Sessiz</span>';` |
| 112 | `voice` | `  window.SeatsStopVoice = stop;` |
| 114 | `voice` | `  // voice-commands.js daha önce window.SeatsVoice içine komut fonksiyonları koymuş olabilir.` |
| 116 | `voice` | `  window.SeatsVoice = Object.assign(window.SeatsVoice \|\| {}, {` |
| 125 | `Sessiz` | `  // Yeşil Ses Açık / Sessiz butonu` |
| 127 | `voice` | `    const btn = e.target.closest && e.target.closest("#nightVoiceToggle");` |
| 137 | `Durak Akışı` | `      speak("Durak akışı sesi açık.", { force:true });` |

### `static/seats/seats.js`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 124 | `Canlı` | `   Aynı rota/plaka ile yeni sefer açılınca eski canlı durak,` |
| 125 | `Durak Akışı` | `   geçildi bilgisi ve durak akışı özeti taşınmasın.` |
| 144 | `Durak Akışı` | `    // Hem trip_id değişince hem de hafıza şeması değişince eski durak akışı silinsin.` |
| 204 | `voice` | `  let lastApproachVoiceStop = "";` |
| 252 | `Normal` | `      .normalize("NFKD")` |
| 277 | `voice` | `  function persistVoiceState(){` |
| 282 | `voice` | `  function loadVoiceState(){` |
| 376 | `Canlı` | `  // Çok uzaktaysa canlı durak göstermesin` |
| 386 | `Canlı` | `  // İşlem olmayan durak canlı gösterilmez.` |
| 401 | `Canlı` | `  // Canlı durak sadece gerçekten yakındaki doğrulanmış durak olsun.` |
| 545 | `selectedStop` | `  function getSelectedStopName(){` |
| 681 | `Durak Akışı` | `      // Yeni sefer açılmış ve koltuk yoksa eski durak akışı özetini taşıma.` |
| 880 | `Bagaj` | `    if(bag > 0) parts.push('${bag} bagaj');` |
| 902 | `voice` | `function setVoiceBadge(text){` |
| 903 | `voice` | `    setText("#voiceStateBadge", text \|\| "Hazır");` |
| 932 | `selectedStop` | `    const stop = getSelectedStopName();` |
| 953 | `Bay` | `    if(gender === "bay") el.classList.add("male");` |
| 954 | `Bay` | `    if(gender === "bayan") el.classList.add("female");` |
| 967 | `Servis` | `      svc.title = note ? 'Servis: ${note}' : "Servis";` |
| 979 | `voice` | `    setText("#voiceSeatFilled", String(filled));` |
| 980 | `voice` | `    setText("#voiceSeatEmpty", String(empty));` |
| 981 | `voice` | `    setText("#driveVoiceFilled", String(filled));` |
| 982 | `voice` | `    setText("#driveVoiceEmpty", String(empty));` |
| 1038 | `voice` | `function focusRouteStripStop(stopName, { select=false, voice=false } = {}){` |
| 1048 | `selectedStop` | `    setSelectedStop(canonical, { silent:!voice, voiceReply:voice });` |
| 1058 | `route-stop` | `      const target = Array.from(wrap.querySelectorAll(".route-stop"))` |
| 1081 | `route-stop` | `      <div class="route-stop active">` |
| 1089 | `selectedStop` | `  const selected = getSelectedStopName();` |
| 1139 | `Canlı` | `    if(isLive) metaLine1 = "Canlı";` |
| 1163 | `route-stop` | `    item.className = 'route-stop ${isActive \|\| isLive ? "active" : ""} ${isDone ? "done has-flow-summary" : ""} ${liveDangerOn && isLive ? "live-danger" : ""} ${isNextWarn ? "next-warning" : ""} ${isFlowGreen ? "flow-green" : ""}';` |
| 1191 | `selectedStop` | `  setSelectedStop(stop, { silent:false, voiceReply:true });` |
| 1195 | `voice` | `    const msg = stopHumanVoiceSummary(stop);` |
| 1218 | `selectedStop` | `    const selected = getSelectedStopName();` |
| 1224 | `selectedStop` | `    setText("#selectedStopBadge", selected \|\| "—");` |
| 1274 | `selectedStop` | `  function setSelectedStop(name, { silent=false, voiceReply=true } = {}){` |
| 1303 | `voice` | `    if(!silent && voiceReply){` |
| 1304 | `voice` | `      const msg = stopHumanVoiceSummary(canonical);` |
| 1326 | `voice` | `    persistVoiceState();` |
| 1335 | `voice` | `    persistVoiceState();` |
| 1346 | `selectedStop` | `    const cur = getSelectedStopName();` |
| 1351 | `selectedStop` | `      setSelectedStop("", { silent:true, voiceReply:false });` |
| 1355 | `selectedStop` | `    setSelectedStop(next, { silent, voiceReply: !silent });` |
| 1362 | `selectedStop` | `    const stopName = getSelectedStopName();` |
| 1395 | `selectedStop` | `    setValue("#pickup", boardsMap[String(seatNo)] \|\| getSelectedStopName() \|\| "");` |
| 1430 | `selectedStop` | `    const from = $("#pickup")?.value \|\| getSelectedStopName() \|\| "";` |
| 1516 | `selectedStop` | `    const offStop = stopsMap[String(currentSeat)] \|\| getSelectedStopName() \|\| "";` |
| 1539 | `Boş` | `      toast("Koltuk boşaltıldı");` |
| 1541 | `İniş` | `      toast(e.message \|\| "İniş hatası");` |
| 1579 | `selectedStop` | `      const selected = getSelectedStopName() \|\| "";` |
| 1594 | `selectedStop` | `    const from = $("#bulkFrom")?.value \|\| speedState.liveStop \|\| getSelectedStopName() \|\| "";` |
| 1622 | `Boş` | `        toast("Boş koltuk yok");` |
| 1759 | `voice` | `      const msg = stopHumanVoiceSummary(stop);` |
| 1774 | `selectedStop` | `      const st = stopsMap[String(n)] \|\| getSelectedStopName() \|\| "";` |
| 1798 | `Boş` | `          if(!j.ok) throw new Error(j.msg \|\| ("Koltuk " + n + " boşaltılamadı"));` |
| 1819 | `Boş` | `      toast('${seatNums.length} koltuk boşaltıldı');` |
| 1821 | `Boş` | `      toast(e.message \|\| "Toplu boşaltma hatası");` |
| 1826 | `selectedStop` | `    const stop = getSelectedStopName();` |
| 1843 | `selectedStop` | `  async function offloadSelectedStop(){` |
| 1844 | `selectedStop` | `    const stop = getSelectedStopName();` |
| 1894 | `selectedStop` | `    const stopName = getSelectedStopName();` |
| 1940 | `selectedStop` | `      const stop = (getSelectedStopName() \|\| $("#coordStopName")?.value \|\| "").trim();` |
| 1994 | `selectedStop` | `    const selectedIdx = indexOfStopByName(getSelectedStopName());` |
| 2054 | `selectedStop` | `      const activeName = getSelectedStopName() \|\| liveName;` |
| 2080 | `Sıradaki` | `    // Asıl akıllı hesap: sıradaki saatli durağa kalan km + efektif hız.` |
| 2177 | `selectedStop` | `      row.addEventListener("click", () => setSelectedStop(item.stop, { silent:true, voiceReply:false }));` |
| 2183 | `selectedStop` | `    const stop = getSelectedStopName();` |
| 2212 | `Canlı` | `      : '${live} civarındasın. Sistem canlı durak ve rötarı izliyor.'` |
| 2215 | `Normal` | `    let aiSub = "Şu an sistem normal akışta.";` |
| 2232 | `Servis` | `    setText("#aiService", unserved > 0 ? '${unserved} yolcu servis bekliyor' : "Servis tarafı temiz");` |
| 2236 | `Canlı` | `  const LIVE_DETECT_KM = 5;        // Muavin hazırlık/canlı durak eşiği` |
| 2237 | `Canlı` | `  const LIVE_FORCE_KM = 1.2;       // Çok yakına girerse beklemeden canlı yap` |
| 2239 | `Canlı` | `  const LIVE_LOOKAHEAD_STOPS = 4;  // Mevcut canlı duraktan sonra kaç durağa bakılsın` |
| 2251 | `Canlı` | `    // Canlı durak GPS + rota sırasına göre belirlenecek.` |
| 2252 | `Seçili durak` | `    // Seçili durak veya eski canlı durak aday listesini kısıtlamaz.` |
| 2321 | `Canlı` | `          Canlı durak zaten belliyse:` |
| 2331 | `Canlı` | `          Geçilmiş durak tekrar canlı aday olmasın.` |
| 2332 | `Canlı` | `          Mevcut canlı durak buna istisna; çünkü markPassedStopsUntil()` |
| 2333 | `Canlı` | `          canlı durağı da passed listesine dahil ediyor.` |
| 2339 | `Canlı` | `        // İşlem yoksa canlı durak yapma.` |
| 2363 | `Canlı` | `        // Mevcut canlı durakta artık işlem yoksa canlıyı boşalt.` |
| 2382 | `Canlı` | `        - canlı durak varsa rota sırasına göre ilerle` |
| 2383 | `Canlı` | `        - canlı durak yoksa en yakındaki işlemli durağı yakala` |
| 2431 | `Canlı` | `        Aynı aday 2 kez görülürse canlı yap.` |
| 2432 | `Canlı` | `        Çok yakına girdiyse beklemeden canlı yap.` |
| 2483 | `voice` | `      if(window.SeatsVoice && typeof window.SeatsVoice.syncButtons === "function"){` |
| 2484 | `voice` | `        window.SeatsVoice.syncButtons();` |
| 2493 | `voice` | `      if(window.SeatsVoice && typeof window.SeatsVoice.setEnabled === "function"){` |
| 2494 | `voice` | `        window.SeatsVoice.setEnabled(next);` |
| 2509 | `voice` | `        if(window.SeatsStopVoice){` |
| 2510 | `voice` | `          window.SeatsStopVoice();` |
| 2515 | `voice` | `    let trVoice = null;` |
| 2516 | `voice` | `    function loadVoices(){` |
| 2517 | `voice` | `      const voices = speechSynthesis.getVoices();` |
| 2518 | `voice` | `      trVoice = voices.find(v => (v.lang \|\| "").toLowerCase().startsWith("tr")) \|\| null;` |
| 2522 | `voice` | `      loadVoices();` |
| 2523 | `voice` | `      speechSynthesis.onvoiceschanged = loadVoices;` |
| 2547 | `voice` | `        const voices = speechSynthesis.getVoices ? speechSynthesis.getVoices() : [];` |
| 2548 | `voice` | `        const trVoice = voices.find(v =>` |
| 2553 | `voice` | `        if(trVoice) u.voice = trVoice;` |
| 2574 | `Servis` | `        service:"servis"` |
| 2765 | `selectedStop` | `  onClick("#btnOffloadNow", offloadSelectedStop);` |
| 2766 | `selectedStop` | `  onClick("#btnOffloadNowPane", offloadSelectedStop);` |
| 2803 | `selectedStop` | `    const a = getSelectedStopName() \|\| "";` |
| 2824 | `Canlı` | `        toast("Canlı durak henüz yok");` |
| 2827 | `voice` | `      focusRouteStripStop(live, { select:true, voice:true });` |
| 2835 | `selectedStop` | `      const selected = getSelectedStopName();` |
| 2838 | `Sıradaki` | `        toast("Sıradaki durak bulunamadı");` |
| 2841 | `voice` | `      focusRouteStripStop(next, { select:true, voice:true });` |
| 2846 | `btnDeckAI` | `  onClick("#btnDeckAI", startDeckAIVoice);` |
| 2851 | `voice` | `      loadVoiceState();` |
| 2853 | `voice` | `      setVoiceBadge("Hazır");` |
| 2880 | `selectedStop` | `      if(next) setSelectedStop(next, { silent:true, voiceReply:false });` |
| 2881 | `selectedStop` | `      else if(serverStops?.length) setSelectedStop(serverStops[0], { silent:true, voiceReply:false });` |
| 2895 | `Canlı` | `   Seats ekranındaki canlı veriyi backend'e yazar` |
| 2902 | `Canlı` | `    // Backend'e sadece gerçekten set edilmiş canlı durağı yaz.` |
| 2908 | `Canlı` | `    // Uzakta kalmış eski canlı durak backend'e yazılmasın.` |

### `static/seats/drive-eta-chip.js`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 3 | `Sürüş` | `   Paneldeki Rötar / ETA bilgisini üst sürüş kutusuna taşır.` |
| 27 | `driveEtaChip` | `  function syncDriveEtaChip(){` |
| 28 | `driveEtaChip` | `    const chip = q("#driveEtaChip");` |
| 29 | `driveEtaMain` | `    const main = q("#driveEtaMain");` |
| 30 | `driveEtaSub` | `    const sub = q("#driveEtaSub");` |
| 52 | `driveEtaChip` | `  window.syncDriveEtaChip = syncDriveEtaChip;` |
| 55 | `driveEtaChip` | `    syncDriveEtaChip();` |
| 56 | `driveEtaChip` | `    setInterval(syncDriveEtaChip, 1500);` |

### `static/seats/bags.js`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 3 | `Bagaj` | `   Bagaj rozetleri + bagaj ses özeti + bagaj temizleme` |
| 6 | `Bagaj` | `// Bagaj göz bilgisi sesli uyarıda kullanılacak.` |
| 30 | `voice` | `function formatSeatListForVoice(seats){` |
| 40 | `voice` | `function bagEyeVoicePartsForSeat(seatNo){` |
| 50 | `Bagaj` | `    if(count === 1) parts.push('${label} gözde bagaj');` |
| 51 | `Bagaj` | `    else parts.push('${label} gözde ${count} bagaj');` |
| 59 | `Bagaj` | `    if(meta.eyes.includes("R")) parts.push("sağ gözde bagaj");` |
| 60 | `Bagaj` | `    if(meta.eyes.includes("LF")) parts.push("sol ön gözde bagaj");` |
| 61 | `Bagaj` | `    if(meta.eyes.includes("LB")) parts.push("sol arka gözde bagaj");` |
| 67 | `voice` | `function bagVoiceSummaryForStop(stopName){` |
| 72 | `voice` | `    const parts = bagEyeVoicePartsForSeat(seatNo);` |
| 78 | `Bagaj` | `    return '${seatNo} numarada bagaj';` |
| 81 | `Bagaj` | `  return 'Bagaj uyarısı: ${chunks.join(". ")} var.';` |
| 145 | `Bagaj` | `  if(badge) badge.title = cnt ? 'Bagaj: ${cnt} adet' : "Bagaj yok";` |
| 179 | `voice` | `  formatSeatListForVoice,` |
| 180 | `voice` | `  bagEyeVoicePartsForSeat,` |
| 181 | `voice` | `  bagVoiceSummaryForStop,` |

### `static/seats/drive-controls.js`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 3 | `Sürüş` | `   HIZLI KOLTUK → OTOMATİK SÜRÜŞ MODU` |
| 4 | `Sürüş` | `   /seats?drive=1 ile gelirse sürüş modunu açar` |
| 18 | `drive-mode` | `    document.body.classList.add("drive-mode");` |
| 33 | `Sürüş` | `    console.warn("Hızlı koltuk sürüş modu açılamadı:", e);` |
| 39 | `Sessiz` | `   Sürüş modu + hız kutusu + ses açık/sessiz` |
| 96 | `driveModeToggle` | `    const btn = document.getElementById("driveModeToggle");` |
| 99 | `drive-mode` | `    document.body.classList.toggle("drive-mode", on);` |
| 100 | `drive-mode` | `    document.documentElement.classList.toggle("drive-mode", on);` |
| 103 | `Normal` | `      btn.innerHTML = on ? "↩ Normal" : "🚘 Sürüş";` |
| 104 | `Normal` | `      btn.title = on ? "Normal moda geç" : "Sürüş moduna geç";` |
| 111 | `driveEtaChip` | `      if(typeof syncDriveEtaChip === "function") syncDriveEtaChip();` |
| 122 | `driveModeToggle` | `    const btn = document.getElementById("driveModeToggle");` |
| 147 | `driveSpeedChip` | `  function updateDriveSpeedChip(){` |
| 148 | `driveSpeedChip` | `    const el = document.getElementById("driveSpeedChip");` |
| 176 | `voice` | `  function getVoiceEnabled(){` |
| 178 | `voice` | `      if(window.SeatsVoice && typeof window.SeatsVoice.isEnabled === "function"){` |
| 179 | `voice` | `        return window.SeatsVoice.isEnabled();` |
| 192 | `voice` | `  function updateNightVoiceToggle(){` |
| 194 | `voice` | `      if(window.SeatsVoice && typeof window.SeatsVoice.syncButtons === "function"){` |
| 195 | `voice` | `        window.SeatsVoice.syncButtons();` |
| 200 | `voice` | `    const btn = document.getElementById("nightVoiceToggle");` |
| 203 | `voice` | `    const on = getVoiceEnabled();` |
| 208 | `Sessiz` | `      : '<span class="nv-ico">🔇</span><span>Sessiz</span>';` |
| 214 | `voice` | `    function setVoiceEnabled(on, opts={}){` |
| 218 | `voice` | `        if(window.SeatsVoice && typeof window.SeatsVoice.setEnabled === "function"){` |
| 219 | `voice` | `          window.SeatsVoice.setEnabled(enabled);` |
| 232 | `voice` | `      updateNightVoiceToggle();` |
| 244 | `voice` | `  function bindNightVoiceToggle(){` |
| 248 | `voice` | `      cb.checked = getVoiceEnabled();` |
| 250 | `voice` | `      if(cb.dataset.voiceBound !== "1"){` |
| 251 | `voice` | `        cb.dataset.voiceBound = "1";` |
| 253 | `voice` | `          setVoiceEnabled(cb.checked, { silent:true });` |
| 259 | `voice` | `      #nightVoiceToggle butonunun tek sahibi voice-tts.js.` |
| 262 | `voice` | `    updateNightVoiceToggle();` |
| 267 | `voice` | `    bindNightVoiceToggle();` |
| 268 | `driveSpeedChip` | `    updateDriveSpeedChip();` |
| 279 | `driveSpeedChip` | `  setInterval(updateDriveSpeedChip, 1000);` |
| 283 | `driveSpeedChip` | `    updateSpeed: updateDriveSpeedChip,` |
| 284 | `voice` | `    setVoiceEnabled` |

### `static/seats/voice-commands.js`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 2 | `voice` | `   VOICE COMMANDS MODULE` |
| 3 | `Sesli Komut` | `   Sesli komut + konuşma + insancıl durak özeti` |
| 6 | `voice` | `const VOICE_HELP = [` |
| 12 | `Sıradaki` | `  "sıradaki durak [durak adı]",` |
| 16 | `Bay` | `  "5 numara bayan [durak]",` |
| 25 | `Bagaj` | `  "bu durakta bagaj var mı",` |
| 32 | `voice` | `/* VOICE_SUMMARY_PATCH_START */` |
| 33 | `voice` | `function buildTripVoiceSummary(){` |
| 61 | `selectedStop` | `    if(typeof getSelectedStopName === "function"){` |
| 62 | `selectedStop` | `      selected = getSelectedStopName() \|\| "";` |
| 75 | `Seçili durak` | `    parts.push('Seçili durak ${selected}.');` |
| 101 | `voice` | `      bagMsg = String(bagVoiceSummaryForStop(selected) \|\| "").trim();` |
| 146 | `Sıradaki` | `    parts.push('Sıradaki işlem ${next}.');` |
| 151 | `voice` | `/* VOICE_SUMMARY_PATCH_END */` |
| 153 | `voice` | `function stopHumanVoiceSummary(stopName){` |
| 179 | `Bay` | `  let bay = 0;` |
| 180 | `Bay` | `  let bayan = 0;` |
| 185 | `Bay` | `    if(g === "bay") bay++;` |
| 186 | `Bay` | `    else if(g === "bayan") bayan++;` |
| 190 | `Normal` | `  // Ayakta yolcuyu "ayakta" diye söyleme; normal yolcu gibi ekle.` |
| 194 | `Bay` | `  if(bay > 0) parts.push('${bay} bay');` |
| 195 | `Bay` | `  if(bayan > 0) parts.push('${bayan} bayan');` |
| 211 | `voice` | `    const bagMsg = bagVoiceSummaryForStop(stop);` |
| 220 | `voice` | `/* --- voice stop ops helpers start --- */` |
| 221 | `voice` | `function stopOperationVoiceSummary(stopName){` |
| 256 | `voice` | `    bagMsg = bagVoiceSummaryForStop(stop) \|\| "";` |
| 273 | `voice` | `    msg += stopHumanVoiceSummary(stop);` |
| 279 | `Servis` | `    msg += ' Ayrıca ${serviceCt} servisli koltuk var.';` |
| 285 | `voice` | `function stopBagVoiceOnly(stopName){` |
| 290 | `voice` | `    const bagMsg = String(bagVoiceSummaryForStop(stop) \|\| "").trim();` |
| 294 | `Bagaj` | `  return '${stop} durağı için bagaj görünmüyor.';` |
| 297 | `selectedStop` | `async function offloadSelectedStopByVoice(){` |
| 298 | `selectedStop` | `  const stop = getSelectedStopName() \|\| speedState.liveStop \|\| "";` |
| 344 | `voice` | `/* --- voice stop ops helpers end --- */` |
| 352 | `voice` | `  if(lastApproachVoiceStop === key) return;` |
| 354 | `voice` | `  lastApproachVoiceStop = key;` |
| 355 | `voice` | `  speak('${stopName} durağına yaklaşılıyor. ${stopHumanVoiceSummary(stopName)}');` |
| 370 | `voice` | `      window.SeatsVoice &&` |
| 371 | `voice` | `      typeof window.SeatsVoice.speak === "function" &&` |
| 372 | `voice` | `      window.SeatsVoice.speak !== speak` |
| 374 | `voice` | `      window.SeatsVoice.speak(msg);` |
| 379 | `voice` | `      const voices = speechSynthesis.getVoices ? speechSynthesis.getVoices() : [];` |
| 380 | `voice` | `      const trVoice = voices.find(v => (v.lang \|\| "").toLowerCase().startsWith("tr"));` |
| 382 | `voice` | `      if(trVoice) u.voice = trVoice;` |
| 383 | `voice` | `      u.lang = trVoice ? trVoice.lang : "tr-TR";` |
| 400 | `voice` | `  speak(stopHumanVoiceSummary(name));` |
| 438 | `Bay` | `  if(/\b(erkek\|bay\|adam)\b/.test(t)) return "bay";` |
| 439 | `Bay` | `  if(/\b(kadin\|kadın\|bayan\|kiz\|kız)\b/.test(t)) return "bayan";` |
| 440 | `Boş` | `  if(/\b(bos yap\|boş yap\|cinsiyeti kaldir\|cinsiyeti kaldır\|temizle\|sil\|sifirla\|sıfırla)\b/.test(t)) return "";` |
| 485 | `Bay` | `    gender === "bay" ? "bay" :` |
| 486 | `Boş` | `    gender === "bayan" ? "bayan" : "boş";` |
| 490 | `Boş` | `    msg += '. Boş olduğu için atlanan: ${emptySeats.join(", ")}';` |
| 498 | `voice` | `function parseVoiceCommand(text){` |
| 506 | `Canlı` | `  if(/^(harita ac\|harita aç\|haritayi ac\|haritayı aç\|canli harita ac\|canlı harita aç\|yol haritasi ac\|yol haritası aç)$/.test(t)) return { type:"open_map" };` |
| 513 | `Sıradaki` | `  if(/(bir sonraki durak\|siradaki saatli\|sıradaki saatli)/.test(t)) return { type:"ask_next_timed" };` |
| 531 | `Sıradaki` | `  if((/(siradaki durak\|sıradaki durak\|durak sec\|durak seç)/.test(t)) && mentionedStop){` |
| 540 | `Seçili durak` | `  if(/(bu durakta islem var mi\|bu durakta işlem var mı\|secili durakta islem var mi\|seçili durakta işlem var mı\|bu durakta ne var)/.test(t)){` |
| 544 | `Seçili durak` | `  if(/(bu durakta kimler inecek\|secili durakta kim inecek\|seçili durakta kim inecek\|inecekleri soyle\|inecekleri söyle)/.test(t)){` |
| 548 | `Bagaj` | `  if(mentionedStop && /(bagaj var mi\|bagaj var mı)/.test(t)){` |
| 552 | `Seçili durak` | `  if(/(bu durakta bagaj var mi\|bu durakta bagaj var mı\|secili durakta bagaj var mi\|seçili durakta bagaj var mı\|bagajli var mi\|bagajlı var mı)/.test(t)){` |
| 556 | `Seçili durak` | `  if(/(inecekleri indir\|bu durakta indir\|secili duraktakileri indir\|seçili duraktakileri indir)/.test(t)){` |
| 567 | `Boş` | `    seat_remove_single: "Tek koltuk boşaltma",` |
| 568 | `Boş` | `    seat_remove_group: "Çoklu koltuk boşaltma",` |
| 570 | `Servis` | `    service_mark: "Servis işaretleme",` |
| 577 | `voice` | `async function resolveVoiceWithBackendAI(text){` |
| 598 | `voice` | `/* VOICE_DIRECT_BOARD_GENERAL_START */` |
| 599 | `voice` | `function voiceCleanStopValue(v){` |
| 607 | `voice` | `function voiceCurrentBoardingStop(){` |
| 611 | `Seçili durak` | `    Öncelik seçili durakta olmalı.` |
| 618 | `voice` | `      stop = voiceCleanStopValue(alertStop.value);` |
| 623 | `selectedStop` | `    if(!stop && typeof getSelectedStopName === "function"){` |
| 624 | `selectedStop` | `      stop = voiceCleanStopValue(getSelectedStopName());` |
| 630 | `selectedStop` | `      const badge = document.querySelector("#selectedStopBadge");` |
| 631 | `voice` | `      if(badge) stop = voiceCleanStopValue(badge.textContent);` |
| 638 | `voice` | `      if(simpleStop) stop = voiceCleanStopValue(simpleStop.textContent);` |
| 643 | `Canlı` | `    Canlı durak en son fallback.` |
| 648 | `voice` | `      stop = voiceCleanStopValue(getDisplayLiveStop());` |
| 654 | `voice` | `      stop = voiceCleanStopValue(speedState.liveStop);` |
| 668 | `voice` | `async function voiceDirectBoardSeats(seats, toStop, genderValue=""){` |
| 679 | `voice` | `  let fromStop = voiceCurrentBoardingStop();` |
| 680 | `voice` | `  toStop = voiceCleanStopValue(toStop);` |
| 685 | `Bay` | `    genderValue = "bay";` |
| 687 | `Bay` | `    genderValue = "bayan";` |
| 690 | `Bay` | `  if(genderValue !== "bay" && genderValue !== "bayan"){` |
| 707 | `Seçili durak` | `    toast("Canlı durak veya seçili durak yok");` |
| 708 | `Seçili durak` | `    speak("Önce canlı durak ya da seçili durak belirlenmeli.");` |
| 713 | `İniş` | `    toast("İniş durağı bulunamadı");` |
| 714 | `İniş` | `    speak("İniş durağı bulunamadı.");` |
| 801 | `Bay` | `      genderValue === "bay" ? " Erkek." :` |
| 802 | `Bay` | `      genderValue === "bayan" ? " Bayan." : "";` |
| 804 | `İniş` | `    const msg = '${seatText} yolcu alındı. Biniş ${fromStop}. İniş ${toStop}.${genderText}';` |
| 815 | `voice` | `/* VOICE_DIRECT_BOARD_GENERAL_END */` |
| 821 | `selectedStop` | `  const selectedStop = getSelectedStopName() \|\| "";` |
| 822 | `selectedStop` | `  if(selectedStop && $("#pickup")) $("#pickup").value = selectedStop;` |
| 833 | `selectedStop` | `  const selectedStop = getSelectedStopName() \|\| "";` |
| 834 | `selectedStop` | `  if(selectedStop && $("#bulkTo")) $("#bulkTo").value = selectedStop;` |
| 857 | `selectedStop` | `  const selectedStop = getSelectedStopName() \|\| "";` |
| 858 | `selectedStop` | `  if(selectedStop && $("#cashTo")) $("#cashTo").value = selectedStop;` |
| 873 | `Servis` | `    toast("Servis için koltuk bulunamadı");` |
| 874 | `Servis` | `    speak("Servis için koltuk bulunamadı.");` |
| 878 | `Sesli Komut` | `  const note = "Sesli komut";` |
| 893 | `Servis` | `  if(!j.ok) throw new Error(j.msg \|\| "Servis işaretleme başarısız");` |
| 906 | `Servis` | `  toast('Servis işlendi: ${seats.join(", ")}');` |
| 907 | `Servis` | `  speak('Servis işlendi. Koltuklar ${seats.join(", ")}');` |
| 928 | `Boş` | `      toast("Boşaltılacak koltuk bulunamadı");` |
| 929 | `Boş` | `      speak("Boşaltılacak koltuk bulunamadı.");` |
| 934 | `Boş` | `    speak('${seats.join(" ve ")} numaralı koltuk boşaltıldı.');` |
| 977 | `voice` | `async function handleLocalVoiceCommand(text){` |
| 978 | `voice` | `  const cmd = parseVoiceCommand(text);` |
| 981 | `voice` | `    const help = "Temel komutlar: " + VOICE_HELP.join(", ");` |
| 988 | `voice` | `    const msg = buildTripVoiceSummary();` |
| 1007 | `Canlı` | `    speak("Canlı harita tam ekran açılıyor.");` |
| 1018 | `voice` | `    await voiceDirectBoardSeats(cmd.seats, cmd.stop, cmd.gender);` |
| 1067 | `selectedStop` | `    const stop = getSelectedStopName() \|\| speedState.liveStop \|\| "";` |
| 1068 | `voice` | `    const msg = stopOperationVoiceSummary(stop);` |
| 1076 | `selectedStop` | `    const stop = getSelectedStopName() \|\| speedState.liveStop \|\| "";` |
| 1077 | `voice` | `    const msg = stopHumanVoiceSummary(stop);` |
| 1085 | `selectedStop` | `    const stop = cmd.stop \|\| getSelectedStopName() \|\| speedState.liveStop \|\| "";` |
| 1086 | `voice` | `    const msg = stopBagVoiceOnly(stop);` |
| 1094 | `selectedStop` | `    return await offloadSelectedStopByVoice();` |
| 1099 | `voice` | `    const msg = stopHumanVoiceSummary(stop);` |
| 1107 | `selectedStop` | `    const live = speedState.liveStop \|\| getSelectedStopName() \|\| "henüz belli değil";` |
| 1132 | `Sıradaki` | `      const msg = "Sıradaki saatli durak bulunamadı.";` |
| 1138 | `Sıradaki` | `    const msg = 'Sıradaki saatli nokta ${nextTimed.stop}. Plan ${nextTimed.plan}, tahmini ${fmtHour(nextTimed.etaDate)}.';` |
| 1145 | `selectedStop` | `    const ok = setSelectedStop(cmd.stop, { silent:true, voiceReply:false });` |
| 1152 | `selectedStop` | `    const stop = getSelectedStopName();` |
| 1153 | `voice` | `    const msg = stopHumanVoiceSummary(stop);` |
| 1162 | `voice` | `async function handleBasicVoiceCommand(text){` |
| 1163 | `voice` | `  const localHandled = await handleLocalVoiceCommand(text);` |
| 1167 | `voice` | `    const resolved = await resolveVoiceWithBackendAI(text);` |
| 1173 | `voice` | `      const cmd = parseVoiceCommand(text);` |
| 1177 | `voice` | `        const msg = stopHumanVoiceSummary(stop);` |
| 1206 | `voice` | `    console.error("AI voice resolve error:", e);` |
| 1207 | `Sesli Komut` | `    toast("AI sesli komut hatası");` |
| 1208 | `Sesli Komut` | `    speak("AI sesli komut tarafında bir hata oluştu.");` |
| 1212 | `voice` | `function getVoiceCommandButtons(){` |
| 1214 | `btnDeckAI` | `  const mainBtn = $("#btnDeckAI");` |
| 1215 | `btnDeckAI` | `  const driveBtn = document.getElementById("btnDeckAIDrive");` |
| 1216 | `voice` | `  const bottomBtn = document.getElementById("seatSimpleVoiceBtn");` |
| 1225 | `voice` | `function setVoiceCommandButtonsListening(buttons, on){` |
| 1229 | `voice` | `    if(btn.id === "seatSimpleVoiceBtn"){` |
| 1231 | `voice` | `        ? '<span class="ico">🔴</span><span class="voice-bottom-text">Dinliyor</span>'` |
| 1232 | `voice` | `        : '<span class="ico">🎙️</span><span class="voice-bottom-text">Sesli<br>Komut</span>';` |
| 1233 | `Sesli Komut` | `      btn.setAttribute("title", on ? "Dinliyor" : "Sesli Komut");` |
| 1234 | `Sesli Komut` | `      btn.setAttribute("aria-label", on ? "Dinliyor" : "Sesli Komut");` |
| 1240 | `Sesli Komut` | `      : '🎤 <span>Sesli Komut</span>';` |
| 1244 | `voice` | `function startDeckAIVoice(){` |
| 1247 | `voice` | `    try{ setVoiceBadge("Dinleniyor"); }catch(_){}` |
| 1253 | `voice` | `  const buttons = getVoiceCommandButtons();` |
| 1258 | `Sesli Komut` | `    toast("Bu tarayıcı sesli komutu desteklemiyor");` |
| 1259 | `voice` | `    setVoiceBadge("Destek yok");` |
| 1269 | `voice` | `  setVoiceCommandButtonsListening(buttons, true);` |
| 1271 | `voice` | `  setVoiceBadge("Dinleniyor");` |
| 1278 | `voice` | `      setVoiceBadge("Tekrar dene");` |
| 1283 | `voice` | `    setVoiceBadge(text.length > 18 ? text.slice(0, 18) + "…" : text);` |
| 1284 | `voice` | `    await handleBasicVoiceCommand(text);` |
| 1289 | `Sesli Komut` | `    toast("Sesli komut hatası: " + (e.error \|\| "bilinmiyor"));` |
| 1290 | `voice` | `    setVoiceBadge("Hata");` |
| 1295 | `voice` | `    setVoiceCommandButtonsListening(buttons, false);` |
| 1297 | `voice` | `    setTimeout(() => setVoiceBadge("Hazır"), 900);` |
| 1304 | `voice` | `    setVoiceCommandButtonsListening(buttons, false);` |
| 1306 | `voice` | `    setVoiceBadge("Başlatılamadı");` |
| 1311 | `voice` | `window.SeatsVoice = {` |
| 1312 | `voice` | `  stopHumanVoiceSummary,` |
| 1316 | `voice` | `  parseVoiceCommand,` |
| 1317 | `voice` | `  handleBasicVoiceCommand,` |
| 1318 | `voice` | `  startDeckAIVoice` |

### `static/seats/standing.js`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 8 | `selectedStop` | `    const selected = getSelectedStopName() \|\| "";` |
| 27 | `selectedStop` | `  const from = $("#cashFrom")?.value \|\| speedState.liveStop \|\| getSelectedStopName() \|\| serverStops?.[0] \|\| "";` |

### `static/seats/seats-final.css`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 109 | `mini-chip` | `.route-live-row .mini-chip{` |
| 125 | `mini-chip` | `.route-live-row .mini-chip span{` |
| 129 | `mini-chip` | `.route-live-row .mini-chip b{` |
| 246 | `Sürüş` | `   SÜRÜŞ / HIZ / RÖTAR SATIRI` |
| 250 | `drive-mode` | `body.drive-mode #driveInlineDock,` |
| 251 | `drive-mode` | `body:not(.drive-mode) #driveInlineDock{` |
| 276 | `driveModeToggle` | `#driveModeToggle,` |
| 277 | `driveSpeedChip` | `#driveSpeedChip,` |
| 278 | `driveEtaChip` | `#driveEtaChip,` |
| 302 | `driveModeToggle` | `#driveModeToggle{` |
| 313 | `driveSpeedChip` | `#driveSpeedChip,` |
| 314 | `driveEtaChip` | `#driveEtaChip{` |
| 359 | `board-head` | `.board-head{` |
| 367 | `board-title` | `.board-title{` |
| 386 | `board-title` | `.board-title h2{` |
| 395 | `board-title` | `.board-title small{` |
| 399 | `selected-stop` | `.selected-stop-chip{` |
| 412 | `board-head` | `.board-head-right{` |
| 417 | `voice` | `.voice-row{` |
| 424 | `voice` | `.voice-command-btn,` |
| 425 | `voice` | `.voice-state{` |
| 433 | `voice` | `.voice-command-btn{` |
| 447 | `voice` | `.voice-command-btn::before,` |
| 448 | `voice` | `.voice-command-btn::after{` |
| 452 | `voice` | `.voice-command-btn span{` |
| 459 | `voice` | `.voice-state{` |
| 469 | `legend` | `.legend{` |
| 476 | `legend` | `.legend .mini-chip,` |
| 477 | `mini-chip` | `.mini-chip{` |
| 497 | `route-strip` | `.route-strip-shell{` |
| 506 | `route-strip` | `.route-strip-head{` |
| 512 | `route-strip` | `.route-strip-title{` |
| 518 | `route-strip` | `.route-strip-meta{` |
| 551 | `voice` | `#nightVoiceToggle{` |
| 562 | `voice` | `#nightVoiceToggle::first-letter{` |
| 566 | `route-strip` | `.route-strip{` |
| 574 | `route-strip` | `.route-strip::-webkit-scrollbar{` |
| 578 | `route-stop` | `.route-stop{` |
| 585 | `route-stop` | `.route-stop .name{` |
| 589 | `route-stop` | `.route-stop .meta{` |
| 597 | `board-stage` | `.board-stage{` |
| 784 | `drive-mode` | `  body.drive-mode #driveInlineDock,` |
| 785 | `drive-mode` | `  body:not(.drive-mode) #driveInlineDock{` |
| 790 | `driveModeToggle` | `  #driveModeToggle{` |
| 794 | `board-title` | `  .board-title h2{` |
| 798 | `route-strip` | `  .route-strip-meta{` |
| 802 | `voice` | `  #nightVoiceToggle{` |
| 807 | `board-stage` | `  .board-stage{` |
| 829 | `voice` | `  .voice-row{` |
| 833 | `voice` | `  .voice-command-btn span{` |
| 837 | `legend` | `  .legend{` |
| 841 | `mini-chip` | `  .mini-chip{` |
| 881 | `mini-chip` | `.route-live-row .mini-chip{` |
| 901 | `Sürüş` | `/* Sürüş + rötar satırı daha düzgün dursun */` |
| 903 | `drive-mode` | `body.drive-mode #driveInlineDock,` |
| 904 | `drive-mode` | `body:not(.drive-mode) #driveInlineDock{` |
| 910 | `driveSpeedChip` | `#driveInlineDock #driveSpeedChip{` |
| 914 | `driveModeToggle` | `#driveModeToggle{` |
| 921 | `driveEtaChip` | `#driveEtaChip,` |
| 934 | `board-title` | `.board-title h2{` |
| 938 | `selected-stop` | `.selected-stop-chip{` |
| 945 | `drive-mode` | `  body.drive-mode #driveInlineDock,` |
| 946 | `drive-mode` | `  body:not(.drive-mode) #driveInlineDock{` |
| 954 | `mini-chip` | `  .route-live-row .mini-chip{` |
| 964 | `Sürüş` | `   Sürüş modunda Durak Akışı kartlarında durak başına konum işareti` |
| 967 | `route-stop` | `body.drive-mode .route-stop .name{` |
| 973 | `route-stop` | `body.drive-mode .route-stop .name::before{` |
| 987 | `route-stop` | `body.drive-mode .route-stop.active .name::before,` |
| 988 | `route-stop` | `body.drive-mode .route-stop.live-danger .name::before,` |
| 989 | `route-stop` | `body.drive-mode .route-stop.next-warning .name::before,` |
| 990 | `route-stop` | `body.drive-mode .route-stop.flow-green .name::before{` |
| 994 | `route-stop` | `body.drive-mode .route-stop.done .name::before{` |
| 1004 | `route-stop` | `body.drive-mode .route-stop .name{` |
| 1010 | `route-stop` | `body.drive-mode .route-stop .name::before{` |
| 1030 | `route-stop` | `body.drive-mode .route-stop.active .name::before,` |
| 1031 | `route-stop` | `body.drive-mode .route-stop.live-danger .name::before,` |
| 1032 | `route-stop` | `body.drive-mode .route-stop.next-warning .name::before,` |
| 1033 | `route-stop` | `body.drive-mode .route-stop.flow-green .name::before{` |
| 1040 | `route-stop` | `body.drive-mode .route-stop.done .name::before{` |
| 1050 | `route-stop` | `body.drive-mode .route-stop .name::before{` |
| 1058 | `route-stop` | `body.drive-mode .route-stop.done .name::before{` |
| 1063 | `route-stop` | `body.drive-mode .route-stop.active .name::before,` |
| 1064 | `route-stop` | `body.drive-mode .route-stop.live-danger .name::before,` |
| 1065 | `route-stop` | `body.drive-mode .route-stop.next-warning .name::before,` |
| 1066 | `route-stop` | `body.drive-mode .route-stop.flow-green .name::before{` |
| 1076 | `Sürüş` | `   Sürüş modunda Durak Akışı kartlarını daha canlı yapar.` |
| 1079 | `route-stop` | `body.drive-mode .route-stop{` |
| 1090 | `route-stop` | `body.drive-mode .route-stop.done{` |
| 1098 | `route-stop` | `body.drive-mode .route-stop.done .name{` |
| 1103 | `route-stop` | `body.drive-mode .route-stop.done .meta,` |
| 1104 | `route-stop` | `body.drive-mode .route-stop.done .extra-k,` |
| 1105 | `route-stop` | `body.drive-mode .route-stop.done .extra-v{` |
| 1109 | `Canlı` | `/* Seçili / canlı kart daha güçlü dursun */` |
| 1110 | `route-stop` | `body.drive-mode .route-stop.active{` |
| 1122 | `route-stop` | `body.drive-mode .route-stop.active .name,` |
| 1123 | `route-stop` | `body.drive-mode .route-stop.active .meta,` |
| 1124 | `route-stop` | `body.drive-mode .route-stop.active .extra-k,` |
| 1125 | `route-stop` | `body.drive-mode .route-stop.active .extra-v{` |
| 1129 | `Normal` | `/* Normal bekleyen kartlar da çok sönük kalmasın */` |
| 1130 | `route-stop` | `body.drive-mode .route-stop:not(.active):not(.live-danger):not(.next-warning):not(.flow-green){` |
| 1137 | `Canlı` | `   Canlı durak eşik km altına düşünce kırmızı uyarı geri gelsin.` |
| 1140 | `route-stop` | `body.drive-mode .route-stop.live-danger{` |
| 1155 | `route-stop` | `body.drive-mode .route-stop.live-danger .name,` |
| 1156 | `route-stop` | `body.drive-mode .route-stop.live-danger .meta,` |
| 1157 | `route-stop` | `body.drive-mode .route-stop.live-danger .extra-k,` |
| 1158 | `route-stop` | `body.drive-mode .route-stop.live-danger .extra-v{` |
| 1163 | `route-stop` | `body.drive-mode .route-stop.live-danger .name::before{` |
| 1170 | `Sıradaki` | `/* Sıradaki uyarı sarı kalsın */` |
| 1171 | `route-stop` | `body.drive-mode .route-stop.next-warning:not(.live-danger){` |
| 1183 | `route-stop` | `body.drive-mode .route-stop.flow-green:not(.live-danger):not(.next-warning){` |
| 1196 | `Normal` | `   NORMAL ROUTE STOP PIN ICON` |
| 1197 | `Normal` | `   Normal modda Durak Akışı kartlarının başına mavi konum ikonu ekler.` |
| 1200 | `route-stop` | `body:not(.drive-mode) .route-stop .name{` |
| 1206 | `route-stop` | `body:not(.drive-mode) .route-stop .name::before{` |
| 1228 | `route-stop` | `body:not(.drive-mode) .route-stop.done .name::before{` |
| 1232 | `route-stop` | `body:not(.drive-mode) .route-stop.active .name::before,` |
| 1233 | `route-stop` | `body:not(.drive-mode) .route-stop.live-danger .name::before,` |
| 1234 | `route-stop` | `body:not(.drive-mode) .route-stop.next-warning .name::before,` |
| 1235 | `route-stop` | `body:not(.drive-mode) .route-stop.flow-green .name::before{` |
| 1244 | `Normal` | `   NORMAL ROUTE PIN BRIGHT FINAL` |
| 1245 | `Normal` | `   Normal mod Durak Akışı konum ikonlarını daha canlı/parlak yapar.` |
| 1248 | `route-stop` | `body:not(.drive-mode) .route-stop .name::before{` |
| 1268 | `route-stop` | `body:not(.drive-mode) .route-stop.done .name::before{` |
| 1285 | `Canlı` | `/* Seçili / canlı / uyarı kartında ikon daha güçlü parlasın */` |
| 1286 | `route-stop` | `body:not(.drive-mode) .route-stop.active .name::before,` |
| 1287 | `route-stop` | `body:not(.drive-mode) .route-stop.live-danger .name::before,` |
| 1288 | `route-stop` | `body:not(.drive-mode) .route-stop.next-warning .name::before,` |
| 1289 | `route-stop` | `body:not(.drive-mode) .route-stop.flow-green .name::before{` |
| 1308 | `Normal` | `   NORMAL ROUTE CARD BACKGROUND BOOST` |
| 1309 | `Normal` | `   Normal modda Durak Akışı kartlarının arka planını canlı yapar.` |
| 1312 | `route-stop` | `body:not(.drive-mode) .route-stop{` |
| 1325 | `route-stop` | `body:not(.drive-mode) .route-stop.done{` |
| 1335 | `route-stop` | `body:not(.drive-mode) .route-stop.done .name{` |
| 1340 | `route-stop` | `body:not(.drive-mode) .route-stop.done .meta,` |
| 1341 | `route-stop` | `body:not(.drive-mode) .route-stop.done .extra-k,` |
| 1342 | `route-stop` | `body:not(.drive-mode) .route-stop.done .extra-v{` |
| 1346 | `Canlı` | `/* Seçili/canlı kırmızı kart kendi rengini korusun */` |
| 1347 | `route-stop` | `body:not(.drive-mode) .route-stop.live-danger{` |
| 1357 | `Normal` | `   NORMAL ROUTE WARNING COLORS RESTORE` |
| 1358 | `Durak Akışı` | `   Durak Akışı: kırmızı / turuncu / yeşil akış renklerini geri getirir.` |
| 1361 | `Canlı` | `/* Canlı / tehlike: kırmızı */` |
| 1362 | `route-stop` | `body:not(.drive-mode) .route-stop.live-danger{` |
| 1377 | `Sıradaki` | `/* Sıradaki uyarı: turuncu */` |
| 1378 | `route-stop` | `body:not(.drive-mode) .route-stop.next-warning:not(.live-danger){` |
| 1393 | `route-stop` | `body:not(.drive-mode) .route-stop.flow-green:not(.live-danger):not(.next-warning){` |
| 1408 | `route-stop` | `body:not(.drive-mode) .route-stop.live-danger .name,` |
| 1409 | `route-stop` | `body:not(.drive-mode) .route-stop.live-danger .meta,` |
| 1410 | `route-stop` | `body:not(.drive-mode) .route-stop.live-danger .extra-k,` |
| 1411 | `route-stop` | `body:not(.drive-mode) .route-stop.live-danger .extra-v,` |
| 1412 | `route-stop` | `body:not(.drive-mode) .route-stop.next-warning .name,` |
| 1413 | `route-stop` | `body:not(.drive-mode) .route-stop.next-warning .meta,` |
| 1414 | `route-stop` | `body:not(.drive-mode) .route-stop.next-warning .extra-k,` |
| 1415 | `route-stop` | `body:not(.drive-mode) .route-stop.next-warning .extra-v,` |
| 1416 | `route-stop` | `body:not(.drive-mode) .route-stop.flow-green .name,` |
| 1417 | `route-stop` | `body:not(.drive-mode) .route-stop.flow-green .meta,` |
| 1418 | `route-stop` | `body:not(.drive-mode) .route-stop.flow-green .extra-k,` |
| 1419 | `route-stop` | `body:not(.drive-mode) .route-stop.flow-green .extra-v{` |
| 1425 | `route-stop` | `body:not(.drive-mode) .route-stop.live-danger .name::before{` |
| 1429 | `route-stop` | `body:not(.drive-mode) .route-stop.next-warning .name::before{` |
| 1433 | `route-stop` | `body:not(.drive-mode) .route-stop.flow-green .name::before{` |
| 1440 | `Canlı` | `   Canlı ve Sıradaki durak kutularını daha canlı yapar.` |
| 1456 | `Canlı` | `/* Canlı kutusu biraz yeşil vurgu alsın */` |
| 1464 | `Sıradaki` | `/* Sıradaki kutusu mavi vurgu */` |
| 1487 | `Canlı` | `   Tek sistem: Canlı/Sıradaki sabit, durak adı TV altyazısı gibi akar.` |
| 1490 | `route-strip` | `.route-strip-meta{` |
| 1547 | `route-strip` | `.route-strip-meta .route-pill b{` |
| 1562 | `Boş` | `/* İkinci kopya: boşluk olmadan akış sağlar */` |
| 1591 | `Canlı` | `   Canlı durak kırmızı uyarıdayken üst Canlı yazısını da kırmızı yapar.` |
| 1594 | `route-strip` | `body.drive-mode .route-strip:has(.route-stop.live-danger) ~ *,` |
| 1595 | `route-strip` | `body:not(.drive-mode) .route-strip:has(.route-stop.live-danger) ~ *{` |
| 1599 | `route-strip` | `.route-strip-shell:has(.route-stop.live-danger) .route-pill-live{` |
| 1610 | `route-strip` | `.route-strip-shell:has(.route-stop.live-danger) .route-pill-live .route-mini-label,` |
| 1611 | `route-strip` | `.route-strip-shell:has(.route-stop.live-danger) .route-pill-live #routeMiniLive{` |
| 1618 | `route-strip` | `.route-strip-shell:has(.route-stop.live-danger) .route-mini-dot{` |
| 1628 | `Sıradaki` | `   Sıradaki durak uyarı/turuncu kart olduğunda üst Sıradaki kutusu da turuncu olur.` |
| 1631 | `route-strip` | `.route-strip-shell:has(.route-stop.next-warning) .route-pill-next{` |
| 1642 | `route-strip` | `.route-strip-shell:has(.route-stop.next-warning) .route-pill-next .route-mini-label,` |
| 1643 | `route-strip` | `.route-strip-shell:has(.route-stop.next-warning) .route-pill-next #routeMiniNext{` |
| 1656 | `legend` | `   DRIVE MODE LEGEND FIXED SINGLE FINAL` |
| 1657 | `Sürüş` | `   Sürüş modunda Boş/Bay/Bayan/Bagaj/İniş/Servis barı` |

### `static/seats/patches/stop-selected-toast.js`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 59 | `selected-stop` | `  document.addEventListener("muavin:selected-stop-change", function(e){` |

### `static/seats/patches/bottom-voice-command.css`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 1 | `voice` | `#seatSimpleVoiceBtn{` |
| 8 | `voice` | `  #seatSimpleVoiceBtn .ico{` |
| 12 | `voice` | `  #seatSimpleVoiceBtn .voice-bottom-text{` |
| 20 | `voice` | `#seatSimpleVoiceBtn.listening{` |

### `static/seats/patches/manual-ticket-system.css`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 4 | `Sesli Komut` | `    Sadece sesli komutla işaretlenen mevcut yolcuya 🎫 verir.` |
| 39 | `drive-mode` | `  body.drive-mode .seat .manual-ticket-badge{` |

### `static/seats/patches/top-sound-toggle.js`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 21 | `voice` | `      if(window.SeatsVoice && typeof window.SeatsVoice.isEnabled === "function"){` |
| 22 | `voice` | `        return !!window.SeatsVoice.isEnabled();` |
| 32 | `voice` | `      if(window.SeatsVoice && typeof window.SeatsVoice.setEnabled === "function"){` |
| 33 | `voice` | `        window.SeatsVoice.setEnabled(on);` |
| 55 | `voice` | `        if(window.SeatsVoice && typeof window.SeatsVoice.stop === "function"){` |
| 56 | `voice` | `          window.SeatsVoice.stop();` |
| 57 | `voice` | `        }else if(window.SeatsStopVoice){` |
| 58 | `voice` | `          window.SeatsStopVoice();` |
| 83 | `Sessiz` | `      : '<span>🔇</span><span>Sessiz</span>';` |

### `static/seats/patches/stop-flow-focus-patch.js`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 6 | `selectedStop` | `  var memoryKey = "muavin:selectedStop:" + String(window.TRIP_KEY \|\| window.BAG_TRIP \|\| location.pathname);` |
| 15 | `Sıradaki` | `    v = v.replace(/^Sıradaki\s*:\s*/i, "");` |
| 39 | `selectedStop` | `    var fromWindow = cleanStopName(window.__muavinSelectedStop \|\| "");` |
| 48 | `selectedStop` | `    var badge = qs("#selectedStopBadge");` |
| 57 | `selectedStop` | `    window.__muavinSelectedStop = name;` |
| 81 | `route-stop` | `    qsa(".route-stop, [data-stop-name], [data-stop]").forEach(function(el){` |
| 112 | `selectedStop` | `    var badge = qs("#selectedStopBadge");` |
| 114 | `Seçili durak` | `      if((badge.textContent \|\| "").toLocaleLowerCase("tr-TR").includes("seçili durak")){` |
| 115 | `Seçili durak` | `        badge.textContent = "🎯 Seçili durak: " + name;` |
| 122 | `selectedStop` | `  function applySelectedStop(name){` |
| 135 | `selectedStop` | `    if(typeof window.setSelectedStop === "function" && !window.__stopFocusCallingSetSelected){` |
| 138 | `selectedStop` | `        window.setSelectedStop(name, true);` |
| 140 | `selectedStop` | `        console.warn("setSelectedStop çağrısı geçildi:", e);` |
| 149 | `selected-stop` | `    document.dispatchEvent(new CustomEvent("muavin:selected-stop-change", {detail:{stop:name}}));` |
| 160 | `Durak Akışı` | `      '<div class="stop-focus-panel" role="dialog" aria-modal="true" aria-label="Durak Akışı">' +` |
| 164 | `Durak Akışı` | `            '<div class="stop-focus-badge">Sadece Durak Akışı</div>' +` |
| 166 | `Durak Akışı` | `          '<h2 class="stop-focus-title">Durak Akışı</h2>' +` |
| 167 | `Seçili durak` | `          '<p class="stop-focus-sub">Seçili durak: <b data-current-stop>—</b></p>' +` |
| 186 | `selectedStop` | `        applySelectedStop(name);` |
| 222 | `Seçili durak` | `      meta.textContent = sameStop(stop, current) ? "Şu an seçili durak" : "Dokun, seç ve koltuk planına dön";` |
| 272 | `seat-simple` | `      if(document.documentElement.classList.contains("seat-simple-mode")) return true;` |
| 273 | `seat-simple` | `      if(document.body.classList.contains("seat-simple-mode")) return true;` |
| 291 | `seat-simple` | `      if(btn.classList && btn.classList.contains("seat-simple-bottom-item")){` |
| 296 | `seat-simple` | `      var parent = btn.closest(".seat-simple-bottom-bar, .seat-simple-dock, .seat-simple-nav");` |
| 314 | `Seçili durak` | `    if(low.includes("seçili durak")) return null;` |
| 329 | `Normal` | `    // Normal moddaki alt Durak butonunu engelleme.` |
| 330 | `Durak Akışı` | `    // Sadece Sade Koltuk modundaki Durak butonu özel "Sadece Durak Akışı" ekranını açsın.` |
| 341 | `selectedStop` | `  function hookSetSelectedStop(){` |
| 342 | `selectedStop` | `    if(typeof window.setSelectedStop !== "function") return;` |
| 343 | `selectedStop` | `    if(window.setSelectedStop.__stopFlowFocusHooked) return;` |
| 345 | `selectedStop` | `    var old = window.setSelectedStop;` |
| 357 | `selectedStop` | `    window.setSelectedStop = wrapped;` |
| 379 | `selectedStop` | `    hookSetSelectedStop();` |

### `static/seats/patches/right-seat-column-spacing-fix.css`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 38 | `Sürüş` | `    Sürüş modunda koltuklar biraz daha sıkıştığı için` |
| 41 | `drive-mode` | `  body.drive-mode .deck{` |
| 46 | `drive-mode` | `    body.drive-mode .deck{` |

### `static/seats/patches/bottom-row-51-54-equal-spacing.css`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 13 | `drive-mode` | `  body.drive-mode .deck .cell[style*="grid-row:14"],` |
| 14 | `drive-mode` | `  body.drive-mode .deck .cell[style*="grid-row: 14"]{` |

### `static/seats/patches/only-54-reapply-right-shift.css`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 15 | `drive-mode` | `  body.drive-mode .deck .cell[style*="grid-row:14"][style*="grid-column:4"],` |
| 16 | `drive-mode` | `  body.drive-mode .deck .cell[style*="grid-row:14"][style*="grid-column: 4"],` |
| 17 | `drive-mode` | `  body.drive-mode .deck .cell[style*="grid-row: 14"][style*="grid-column:4"],` |
| 18 | `drive-mode` | `  body.drive-mode .deck .cell[style*="grid-row: 14"][style*="grid-column: 4"]{` |

### `static/seats/patches/seat-layout-fab-pack.css`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 39 | `Sürüş` | `    Sürüş modunda koltuklar biraz daha sıkıştığı için` |
| 42 | `drive-mode` | `  body.drive-mode .deck{` |
| 47 | `drive-mode` | `    body.drive-mode .deck{` |
| 65 | `drive-mode` | `  body.drive-mode .deck .cell[style*="grid-row:14"],` |
| 66 | `drive-mode` | `  body.drive-mode .deck .cell[style*="grid-row: 14"]{` |
| 85 | `drive-mode` | `  body.drive-mode .deck .cell[style*="grid-row:14"][style*="grid-column:4"],` |
| 86 | `drive-mode` | `  body.drive-mode .deck .cell[style*="grid-row:14"][style*="grid-column: 4"],` |
| 87 | `drive-mode` | `  body.drive-mode .deck .cell[style*="grid-row: 14"][style*="grid-column:4"],` |
| 88 | `drive-mode` | `  body.drive-mode .deck .cell[style*="grid-row: 14"][style*="grid-column: 4"]{` |
| 95 | `Boş` | `    43 ile 51 arasındaki boş sol alana yerleştirir.` |
| 120 | `drive-mode` | `  body.drive-mode .fab-column.fab-left-gap-moved .fab{` |
| 133 | `drive-mode` | `    body.drive-mode .fab-column.fab-left-gap-moved .fab{` |
| 143 | `Boş` | `    Sol boş alana taşınan hızlı işlem butonlarını` |
| 259 | `drive-mode` | `  body.drive-mode .fab-column.fab-left-gap-moved .fab{` |
| 282 | `drive-mode` | `    body.drive-mode .fab-column.fab-left-gap-moved .fab{` |
| 295 | `drive-mode` | `    static/seats/seats.css içindeki body.drive-mode .fab-column kuralı` |
| 299 | `drive-mode` | `    .fab-left-gap-moved sınıfı varsa, drive-mode kurallarını ezip` |
| 304 | `drive-mode` | `  body.drive-mode .fab-column.fab-left-gap-moved{` |
| 345 | `drive-mode` | `  body.drive-mode .fab-column.fab-left-gap-moved::before{` |
| 362 | `drive-mode` | `  body.drive-mode .fab-column.fab-left-gap-moved .fab{` |
| 382 | `drive-mode` | `  body.drive-mode .fab-column.fab-left-gap-moved .fab::after{` |
| 389 | `drive-mode` | `    body.drive-mode .fab-column.fab-left-gap-moved{` |
| 400 | `drive-mode` | `    body.drive-mode .fab-column.fab-left-gap-moved .fab{` |

### `static/seats/patches/seat-simple-ui-pack.css`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 1 | `seat-simple` | `/* ===== seat-simple-open-mode-style ===== */` |
| 7 | `seat-simple` | `.seat-simple-toggle{` |
| 28 | `seat-simple` | `html.seat-simple-mode .seats-shell{` |
| 34 | `seat-simple` | `html.seat-simple-mode .seats-shell > :not(.layout){` |
| 38 | `seat-simple` | `html.seat-simple-mode .layout{` |
| 43 | `seat-simple` | `html.seat-simple-mode .panel-card{` |
| 47 | `seat-simple` | `html.seat-simple-mode .board-card{` |
| 53 | `seat-simple` | `html.seat-simple-mode .board-inner{` |
| 57 | `Sürüş` | `/* üst sürüş/eta dock sade modda gizli */` |
| 58 | `seat-simple` | `html.seat-simple-mode #driveInlineDock,` |
| 59 | `seat-simple` | `html.seat-simple-mode #driveModeActionsDock{` |
| 63 | `legend` | `/* sağdaki ses/legend/kalabalık kontroller gizli */` |
| 64 | `seat-simple` | `html.seat-simple-mode .board-head-right,` |
| 65 | `voice` | `html.seat-simple-mode .voice-row,` |
| 66 | `voice` | `html.seat-simple-mode .drive-voice-row,` |
| 67 | `legend` | `html.seat-simple-mode .legend{` |
| 72 | `seat-simple` | `html.seat-simple-mode .board-head{` |
| 77 | `seat-simple` | `html.seat-simple-mode .board-title{` |
| 81 | `seat-simple` | `html.seat-simple-mode .board-kicker,` |
| 82 | `seat-simple` | `html.seat-simple-mode .board-title small{` |
| 86 | `seat-simple` | `html.seat-simple-mode .board-title h2{` |
| 93 | `selected-stop` | `html.seat-simple-mode .selected-stop-chip{` |
| 103 | `Durak Akışı` | `/* rota/durak akışı ilk açılışta gizli */` |
| 104 | `route-strip` | `html.seat-simple-mode .route-strip-shell,` |
| 105 | `route-flow` | `html.seat-simple-mode .route-flow-shell,` |
| 106 | `route-flow` | `html.seat-simple-mode .route-flow,` |
| 107 | `seat-simple` | `html.seat-simple-mode #routeStrip,` |
| 108 | `seat-simple` | `html.seat-simple-mode .route-mini,` |
| 109 | `seat-simple` | `html.seat-simple-mode .route-pill{` |
| 114 | `seat-simple` | `html.seat-simple-mode .deck-card,` |
| 115 | `seat-simple` | `html.seat-simple-mode .seat-deck,` |
| 116 | `seat-simple` | `html.seat-simple-mode .deck-shell{` |
| 122 | `seat-simple` | `  .seat-simple-toggle{` |
| 129 | `seat-simple` | `  html.seat-simple-mode .board-inner{` |
| 133 | `seat-simple` | `  html.seat-simple-mode .board-title h2{` |
| 138 | `seat-simple` | `/* ===== seat-simple-summary-polish-style ===== */` |
| 144 | `seat-simple` | `.seat-simple-summary{` |
| 159 | `seat-simple` | `html.seat-simple-mode .seat-simple-summary{` |
| 163 | `seat-simple` | `.seat-simple-summary-top{` |
| 171 | `seat-simple` | `.seat-simple-route{` |
| 183 | `seat-simple` | `.seat-simple-status{` |
| 200 | `seat-simple` | `.seat-simple-summary-grid{` |
| 206 | `seat-simple` | `.seat-simple-mini{` |
| 216 | `seat-simple` | `.seat-simple-mini small{` |
| 227 | `seat-simple` | `.seat-simple-mini b{` |
| 238 | `seat-simple` | `.seat-simple-mini .ok{` |
| 242 | `seat-simple` | `.seat-simple-mini .speed{` |
| 246 | `seat-simple` | `html.seat-simple-mode .seat-simple-toggle{` |
| 251 | `seat-simple` | `  .seat-simple-summary{` |
| 257 | `seat-simple` | `  .seat-simple-route{` |
| 261 | `seat-simple` | `  .seat-simple-summary-grid{` |
| 266 | `seat-simple` | `  .seat-simple-mini{` |
| 272 | `seat-simple` | `  .seat-simple-mini small{` |
| 276 | `seat-simple` | `  .seat-simple-mini b{` |
| 281 | `seat-simple` | `/* ===== seat-simple-bottom-bar-style ===== */` |
| 287 | `seat-simple` | `.seat-simple-bottom-bar{` |
| 308 | `seat-simple` | `html.seat-simple-mode .seat-simple-bottom-bar{` |
| 312 | `seat-simple` | `html.seat-simple-mode body{` |
| 316 | `seat-simple` | `.seat-simple-bottom-item{` |
| 339 | `seat-simple` | `.seat-simple-bottom-item .ico{` |
| 344 | `seat-simple` | `.seat-simple-bottom-item.primary{` |
| 351 | `seat-simple` | `.seat-simple-bottom-item.warn{` |
| 357 | `seat-simple` | `.seat-simple-bottom-item.danger{` |
| 363 | `seat-simple` | `.seat-simple-bottom-item:active{` |
| 368 | `seat-simple` | `  .seat-simple-bottom-bar{` |
| 377 | `seat-simple` | `  .seat-simple-bottom-item{` |
| 383 | `seat-simple` | `  .seat-simple-bottom-item .ico{` |
| 394 | `seat-simple` | `html.seat-modal-open .seat-simple-bottom-bar,` |
| 395 | `seat-simple` | `body.seat-modal-open .seat-simple-bottom-bar{` |

### `static/seats/patches/seat-simple-ui-pack.js`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 1 | `seat-simple` | `/* ===== seat-simple-open-mode-script ===== */` |
| 34 | `seat-simple` | `    document.documentElement.classList.toggle("seat-simple-mode", simple);` |
| 35 | `seat-simple` | `    document.body.classList.toggle("seat-simple-mode", simple);` |
| 41 | `sade koltuk moduna dön` | `        : "💺 Sade koltuk moduna dön";` |
| 60 | `seat-simple` | `    btn.className = "seat-simple-toggle";` |
| 86 | `seat-simple` | `/* ===== seat-simple-summary-polish-script ===== */` |
| 103 | `seat-simple` | `      box.className = "seat-simple-summary";` |
| 105 | `seat-simple` | `        <div class="seat-simple-summary-top">` |
| 106 | `seat-simple` | `          <div class="seat-simple-route" id="seatSimpleRoute">—</div>` |
| 107 | `seat-simple` | `          <div class="seat-simple-status"><span>●</span><span>Sade Mod</span></div>` |
| 110 | `seat-simple` | `        <div class="seat-simple-summary-grid">` |
| 111 | `seat-simple` | `          <div class="seat-simple-mini">` |
| 115 | `seat-simple` | `          <div class="seat-simple-mini">` |
| 119 | `seat-simple` | `          <div class="seat-simple-mini">` |
| 150 | `selectedStop` | `    let stop = readText("#selectedStopBadge") \|\| "—";` |
| 156 | `voice` | `    let filled = readText("#voiceSeatFilled") \|\| readText("#driveVoiceFilled") \|\| "";` |
| 157 | `voice` | `    let empty  = readText("#voiceSeatEmpty")  \|\| readText("#driveVoiceEmpty")  \|\| "";` |

### `static/seats/patches/mobile-performance-fix.css`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 21 | `Boş` | `  /* Beyaz flash/boşluk görünmesin diye kök alanı koyulaştır */` |
| 56 | `seat-simple` | `  .seat-simple-bottom-bar,` |
| 71 | `route-stop` | `  .route-stop,` |
| 72 | `voice` | `  .voice-command-btn,` |
| 73 | `voice` | `  .drive-voice-btn,` |
| 74 | `seat-simple` | `  .seat-simple-bottom-item,` |
| 82 | `route-stop` | `  .route-stop,` |
| 83 | `route-stop` | `  .route-stop *,` |
| 84 | `voice` | `  .voice-command-btn,` |
| 85 | `voice` | `  .drive-voice-btn,` |
| 104 | `route-stop` | `  .route-stop,` |
| 105 | `seat-simple` | `  .seat-simple-bottom-item,` |
| 106 | `voice` | `  .voice-command-btn,` |
| 107 | `voice` | `  .drive-voice-btn{` |
| 116 | `seat-simple` | `  .seat-simple-bottom-bar,` |

### `static/seats/patches/stop-flow-compact-mobile.css`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 1 | `Durak Akışı` | `/* Durak Akışı mobil kompakt görünüm */` |

### `static/seats/patches/seat-label-ghost-clean.css`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 3 | `Boş` | `   Boş koltuk altı label kutularındaki kare karartmayı kaldırır.` |
| 9 | `Boş` | `  /* Boş label tamamen yok olsun */` |
| 10 | `seat-simple` | `  html.seat-simple-mode .deck .cell .label:empty,` |
| 11 | `seat-simple` | `  body.seat-simple-mode .deck .cell .label:empty,` |
| 27 | `seat-simple` | `  html.seat-simple-mode .deck .cell .label,` |
| 28 | `seat-simple` | `  body.seat-simple-mode .deck .cell .label{` |
| 37 | `seat-simple` | `  html.seat-simple-mode .deck .cell .label:not(:empty),` |
| 38 | `seat-simple` | `  body.seat-simple-mode .deck .cell .label:not(:empty){` |

### `static/seats/patches/unified-seat-deck-report-style.css`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 3 | `Normal` | `   Normal mod + Sürüş modu + Sade mod aynı koltuk planını kullanır.` |
| 17 | `board-stage` | `.board-stage,` |
| 18 | `drive-mode` | `body.drive-mode .board-stage,` |
| 19 | `seat-simple` | `html.seat-simple-mode .board-stage{` |
| 26 | `Boş` | `/* Deck ortalansın, sağ boşluk/fab baskısı koltuk planını bozmasın */` |
| 28 | `drive-mode` | `body.drive-mode .deck-wrap,` |
| 29 | `seat-simple` | `html.seat-simple-mode .deck-wrap{` |
| 40 | `drive-mode` | `body.drive-mode .deck,` |
| 41 | `seat-simple` | `html.seat-simple-mode .deck{` |
| 72 | `drive-mode` | `body.drive-mode .deck .cell[style*="grid-column:4"],` |
| 73 | `drive-mode` | `body.drive-mode .deck .cell[style*="grid-column: 4"],` |
| 74 | `seat-simple` | `html.seat-simple-mode .deck .cell[style*="grid-column:4"],` |
| 75 | `seat-simple` | `html.seat-simple-mode .deck .cell[style*="grid-column: 4"],` |
| 78 | `drive-mode` | `body.drive-mode .deck .cell[style*="grid-row:14"],` |
| 79 | `drive-mode` | `body.drive-mode .deck .cell[style*="grid-row: 14"]{` |
| 85 | `drive-mode` | `body.drive-mode .cell,` |
| 86 | `seat-simple` | `html.seat-simple-mode .cell{` |
| 97 | `drive-mode` | `body.drive-mode .label,` |
| 98 | `seat-simple` | `html.seat-simple-mode .label{` |
| 111 | `drive-mode` | `body.drive-mode .seat,` |
| 112 | `seat-simple` | `html.seat-simple-mode .seat{` |
| 138 | `Boş` | `/* Boş / erkek / kadın / atanmış renkleri */` |
| 140 | `drive-mode` | `body.drive-mode .seat:not(.isAssigned):not(.male):not(.female),` |
| 141 | `seat-simple` | `html.seat-simple-mode .seat:not(.isAssigned):not(.male):not(.female){` |
| 146 | `drive-mode` | `body.drive-mode .seat.male,` |
| 147 | `seat-simple` | `html.seat-simple-mode .seat.male{` |
| 152 | `drive-mode` | `body.drive-mode .seat.female,` |
| 153 | `seat-simple` | `html.seat-simple-mode .seat.female{` |
| 158 | `drive-mode` | `body.drive-mode .seat.isAssigned:not(.male):not(.female),` |
| 159 | `seat-simple` | `html.seat-simple-mode .seat.isAssigned:not(.male):not(.female){` |
| 165 | `drive-mode` | `body.drive-mode .seat.selected,` |
| 166 | `seat-simple` | `html.seat-simple-mode .seat.selected{` |
| 177 | `drive-mode` | `body.drive-mode .seat.has-stop,` |
| 178 | `seat-simple` | `html.seat-simple-mode .seat.has-stop{` |
| 186 | `drive-mode` | `body.drive-mode .corr,` |
| 187 | `seat-simple` | `html.seat-simple-mode .corr{` |
| 221 | `drive-mode` | `body.drive-mode .door,` |
| 222 | `seat-simple` | `html.seat-simple-mode .door{` |
| 248 | `Bagaj` | `/* Bagaj / servis / inecek rozetleri koltuğun üstünde kalsın */` |
| 250 | `drive-mode` | `body.drive-mode .seat .bag-badge,` |
| 251 | `seat-simple` | `html.seat-simple-mode .seat .bag-badge{` |
| 265 | `drive-mode` | `body.drive-mode .seat .svc-badge,` |
| 266 | `seat-simple` | `html.seat-simple-mode .seat .svc-badge{` |
| 275 | `drive-mode` | `body.drive-mode .seat .stop-badge,` |
| 276 | `seat-simple` | `html.seat-simple-mode .seat .stop-badge{` |
| 283 | `Sürüş` | `/* Sürüş modunda koltuk planı artık ayrı küçülmesin/büyümesin */` |
| 284 | `drive-mode` | `body.drive-mode{` |
| 300 | `board-stage` | `  .board-stage,` |
| 301 | `drive-mode` | `  body.drive-mode .board-stage,` |
| 302 | `seat-simple` | `  html.seat-simple-mode .board-stage{` |
| 307 | `drive-mode` | `  body.drive-mode .deck,` |
| 308 | `seat-simple` | `  html.seat-simple-mode .deck{` |
| 314 | `drive-mode` | `  body.drive-mode .seat,` |
| 315 | `seat-simple` | `  html.seat-simple-mode .seat{` |
| 321 | `drive-mode` | `  body.drive-mode .corr,` |
| 322 | `seat-simple` | `  html.seat-simple-mode .corr{` |
| 328 | `drive-mode` | `  body.drive-mode .door,` |
| 329 | `seat-simple` | `  html.seat-simple-mode .door{` |
| 347 | `drive-mode` | `  body.drive-mode .seat,` |
| 348 | `seat-simple` | `  html.seat-simple-mode .seat{` |
| 355 | `Normal` | `/* Etiketler geri geldi: normal + sürüş + sade mod aynı kompakt etiket düzeni */` |
| 364 | `drive-mode` | `body.drive-mode .cell,` |
| 365 | `seat-simple` | `html.seat-simple-mode .cell{` |
| 373 | `drive-mode` | `body.drive-mode .label,` |
| 374 | `seat-simple` | `html.seat-simple-mode .label{` |
| 399 | `Boş` | `/* Boş etikette alanı biraz azalt ama düzen bozulmasın */` |
| 401 | `drive-mode` | `body.drive-mode .label:empty,` |
| 402 | `seat-simple` | `html.seat-simple-mode .label:empty{` |
| 408 | `Sürüş` | `/* Sürüş modunda da aynı düzen kalsın */` |
| 409 | `drive-mode` | `body.drive-mode{` |
| 414 | `seat-simple` | `html.seat-simple-mode .label{` |
| 427 | `drive-mode` | `  body.drive-mode .label,` |
| 428 | `seat-simple` | `  html.seat-simple-mode .label{` |
| 435 | `drive-mode` | `  body.drive-mode .label:empty,` |
| 436 | `seat-simple` | `  html.seat-simple-mode .label:empty{` |
| 450 | `drive-mode` | `  body.drive-mode .label,` |
| 451 | `seat-simple` | `  html.seat-simple-mode .label{` |
| 460 | `Normal` | `/* Koltuk aralarını biraz açar; normal + sürüş + sade mod aynı kalır */` |
| 470 | `drive-mode` | `body.drive-mode .deck,` |
| 471 | `seat-simple` | `html.seat-simple-mode .deck{` |
| 479 | `drive-mode` | `body.drive-mode .corr,` |
| 480 | `seat-simple` | `html.seat-simple-mode .corr{` |
| 497 | `drive-mode` | `  body.drive-mode .deck,` |
| 498 | `seat-simple` | `  html.seat-simple-mode .deck{` |

### `static/seats/patches/hide-quick-fab-v22.css`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 4 | `Normal` | `   İşlem sekmesindeki normal Hızlı İşlemler ekranına dokunmaz.` |
| 9 | `drive-mode` | `body.drive-mode .fab-column,` |
| 10 | `drive-mode` | `body.drive-mode .fab-column.fab-left-gap-moved,` |
| 11 | `seat-simple` | `html.seat-simple-mode .fab-column,` |
| 12 | `seat-simple` | `html.seat-simple-mode .fab-column.fab-left-gap-moved{` |

### `static/seats/_archive_theme_trials/seats-dashboard-final.css`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 105 | `Canlı` | `/* canlı chip satırı */` |
| 113 | `mini-chip` | `.route-live-row .mini-chip{` |
| 128 | `mini-chip` | `.route-live-row .mini-chip span{` |
| 135 | `mini-chip` | `.route-live-row .mini-chip b{` |
| 251 | `Sürüş` | `   SÜRÜŞ / HIZ / RÖTAR SATIRI` |
| 277 | `driveModeToggle` | `#driveModeToggle,` |
| 278 | `driveSpeedChip` | `#driveSpeedChip,` |
| 279 | `driveEtaChip` | `#driveEtaChip,` |
| 291 | `driveModeToggle` | `#driveModeToggle{` |
| 320 | `board-head` | `.board-head{` |
| 340 | `board-title` | `.board-title h2{` |
| 349 | `board-title` | `.board-title small{` |
| 353 | `selected-stop` | `.selected-stop-chip{` |
| 366 | `board-head` | `.board-head-right{` |
| 371 | `voice` | `.voice-row{` |
| 377 | `voice` | `.voice-command-btn,` |
| 378 | `voice` | `.voice-state{` |
| 385 | `voice` | `.voice-command-btn{` |
| 392 | `voice` | `.voice-state{` |
| 401 | `legend` | `.legend{` |
| 407 | `legend` | `.legend .mini-chip{` |
| 422 | `route-flow` | `.route-flow,` |
| 425 | `route-flow` | `.route-flow-card{` |
| 439 | `board-stage` | `.board-stage{` |
| 715 | `mini-chip` | `  .route-live-row .mini-chip{` |
| 752 | `driveModeToggle` | `  #driveModeToggle,` |
| 753 | `driveSpeedChip` | `  #driveSpeedChip,` |
| 754 | `driveEtaChip` | `  #driveEtaChip,` |
| 761 | `board-title` | `  .board-title h2{` |
| 765 | `voice` | `  .voice-row{` |
| 769 | `legend` | `  .legend{` |
| 773 | `legend` | `  .legend .mini-chip{` |
| 778 | `board-stage` | `  .board-stage{` |
| 803 | `mini-chip` | `  .route-live-row .mini-chip b{` |
| 815 | `board-title` | `  .board-title h2{` |
| 819 | `selected-stop` | `  .selected-stop-chip{` |

### `static/seats/_archive_theme_trials/seats-dashboard-tone.css`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 40 | `Canlı` | `/* Üstteki canlı chipler: beyaz değil koyu cam */` |
| 41 | `mini-chip` | `.route-live-row .mini-chip{` |
| 48 | `mini-chip` | `.route-live-row .mini-chip span{` |
| 52 | `mini-chip` | `.route-live-row .mini-chip b{` |
| 103 | `board-title` | `.board-title h2{` |
| 107 | `selected-stop` | `.selected-stop-chip{` |
| 114 | `Sürüş` | `/* Sürüş / rötar satırı koyu cam */` |
| 115 | `driveModeToggle` | `#driveModeToggle,` |
| 116 | `driveSpeedChip` | `#driveSpeedChip,` |
| 117 | `driveEtaChip` | `#driveEtaChip,` |
| 126 | `driveModeToggle` | `#driveModeToggle{` |
| 140 | `Sesli Komut` | `/* Sesli komut ve legend */` |
| 141 | `voice` | `.voice-state{` |
| 147 | `legend` | `.legend .mini-chip{` |
| 153 | `Durak Akışı` | `/* Durak akışı koyu cam */` |
| 154 | `route-flow` | `.route-flow,` |
| 157 | `route-flow` | `.route-flow-card{` |

### `android_app/app/src/main/python/templates/add_route.html`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 208 | `Boş` | `/* Sayfa dış boşluk */` |
| 304 | `Boş` | `      <div class="hint">Virgül (,) ve/veya yeni satır ile ayırabilirsiniz. Boşlukları otomatik temizler.</div>` |
| 334 | `Boş` | `    // satır ve virgül bazlı parçala, kırp, boşları at` |
| 370 | `Normal` | `  // Gönderimden önce metni normalize et (server tarafına temiz liste gitsin)` |
| 379 | `Normal` | `    // Sunucu "virgülle ayrılmış" bekliyorsa normalize et:` |

### `android_app/app/src/main/python/templates/events.html`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 123 | `Boş` | `      <span class="small" style="margin-left:8px">Boş bırakırsan varsayılana döner.</span>` |

### `android_app/app/src/main/python/templates/fare_admin.html`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 54 | `İniş` | `        <div class="label">İniş</div>` |
| 69 | `İniş` | `        <button class="btn gray" type="button" onclick="swap()">Biniş ↔ İniş</button>` |
| 127 | `Canlı` | `  // Canlı filtre` |
| 131 | `Boş` | `      if(!el.dataset.from){ return; } // boş satır için` |

### `android_app/app/src/main/python/templates/fare_query.html`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 54 | `İniş` | `        <div class="label">İniş</div>` |
| 67 | `İniş` | `      <button class="btn gray" type="button" onclick="swapStops()">Biniş ↔ İniş</button>` |

### `android_app/app/src/main/python/templates/hesap.html`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 1887 | `Durak Akışı` | `        Bu işlem aktif seferi kapatır. Koltuklar, ayakta yolcular ve durak akışı temizlenir.` |
| 2340 | `Normal` | `    function normalize(s){` |
| 2345 | `Normal` | `      const term = normalize(q?.value \|\| "");` |
| 2352 | `Normal` | `        const ok = !term \|\| normalize(r.innerText).includes(term);` |
| 2358 | `Normal` | `        const ok = !term \|\| normalize(c.innerText).includes(term);` |

### `android_app/app/src/main/python/templates/index.html`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 1096 | `Sesli Komut` | `          <div class="menu-desc">Uygulama kullanımı / sesli komutlar / hızlı yardım</div>` |
| 1785 | `Normal` | `       Aktif sefer yoksa premium route picker normal açılır.` |

### `android_app/app/src/main/python/templates/passenger_control.html`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 240 | `legend` | `.legend-box{` |
| 252 | `legend` | `.legend-line{` |
| 259 | `legend` | `.legend-dot{` |
| 266 | `legend` | `.legend-dot.wait{ background:#f59e0b; box-shadow:0 0 16px rgba(245,158,11,.55); }` |
| 267 | `legend` | `.legend-dot.ok{ background:#22c55e; box-shadow:0 0 16px rgba(34,197,94,.50); }` |
| 268 | `legend` | `.legend-dot.bad{ background:#ef4444; box-shadow:0 0 16px rgba(239,68,68,.50); }` |
| 710 | `Boş` | `    <div class="stat"><div class="k">Boş Koltuk</div><div class="v" id="st_empty">0</div></div>` |
| 715 | `legend` | `  <section class="legend-box">` |
| 716 | `legend` | `    <div class="legend-line"><span class="legend-dot wait"></span> Sarı yanıp sönüyor: kontrol bekliyor</div>` |
| 717 | `legend` | `    <div class="legend-line"><span class="legend-dot ok"></span> Yeşil: yolcu yerinde</div>` |
| 718 | `legend` | `    <div class="legend-line"><span class="legend-dot bad"></span> Kırmızı: eksik yolcu</div>` |
| 724 | `Canlı` | `      <span class="deck-badge">Canlı kontrol</span>` |
| 754 | `Bay` | `  if(gender === 'bay'){` |
| 756 | `Bay` | `  }else if(gender === 'bayan'){` |
| 1218 | `legend` | `.legend-box{` |
| 1226 | `legend` | `.legend-line{` |
| 1230 | `legend` | `.legend-dot{` |

### `android_app/app/src/main/python/templates/reports.html`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 125 | `legend` | `  .legend{display:flex;gap:8px;align-items:center;margin-top:8px;color:var(--sub)}` |
| 250 | `legend` | `      <div class="legend">` |

### `android_app/app/src/main/python/templates/route_edit.html`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 704 | `Boş` | `      alert("Durak listesi boş.");` |

### `android_app/app/src/main/python/templates/route_stops.html`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 57 | `route-stop` | `        const res = await fetch('/api/route-stop', {` |

### `android_app/app/src/main/python/templates/seats.html`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 6 | `voice` | `<link rel="stylesheet" href="/static/seats/seats-final.css?v=drive-voice-real-width-test-1">` |
| 11 | `voice` | `<link rel="stylesheet" href="/static/seats/patches/bottom-voice-command.css?v=1">` |
| 15 | `seat-simple` | `<link rel="stylesheet" href="/static/seats/patches/seat-simple-ui-pack.css?v=1">` |
| 29 | `Sürüş` | `          <button id="driveModeToggle" type="button" aria-label="Sürüş modu">🚘 Sürüş</button>` |
| 31 | `driveSpeedChip` | `          <div id="driveSpeedChip" class="drive-speed-chip neutral">` |
| 40 | `driveEtaChip` | `          <div id="driveEtaChip" class="drive-eta-chip neutral">` |
| 43 | `driveEtaMain` | `              <b id="driveEtaMain">Rötar</b>` |
| 45 | `driveEtaSub` | `            <div class="drive-eta-sub" id="driveEtaSub">ETA bekleniyor</div>` |
| 49 | `board-head` | `        <div class="board-head">` |
| 50 | `board-title` | `          <div class="board-title">` |
| 51 | `Canlı` | `            <div class="board-kicker">Canlı Operasyon Paneli</div>` |
| 54 | `Seçili durak` | `            <div class="selected-stop-chip">🎯 Seçili durak: <b id="selectedStopBadge">—</b></div>` |
| 57 | `board-head` | `          <div class="board-head-right">` |
| 58 | `voice` | `            <div class="voice-row">` |
| 59 | `Sesli Komut` | `              <button class="voice-command-btn" id="btnDeckAI" type="button" title="Sesli Komut">` |
| 60 | `Sesli Komut` | `                🎤 <span>Sesli Komut</span>` |
| 63 | `voice` | `              <div class="voice-seat-mini" id="voiceSeatMiniStats" title="Koltuk özeti">` |
| 64 | `voice` | `                <span>Dolu <b id="voiceSeatFilled">0</b></span>` |
| 65 | `voice` | `                <span>Boş <b id="voiceSeatEmpty">0</b></span>` |
| 68 | `voice` | `              <div class="voice-state" id="voiceStateBadge">Hazır</div>` |
| 71 | `voice` | `<!-- DRIVE VOICE ROW START -->` |
| 72 | `voice` | `<div class="drive-voice-row" id="driveVoiceRow">` |
| 73 | `Sesli Komut` | `  <button class="drive-voice-btn" id="btnDeckAIDrive" type="button" title="Sesli Komut">` |
| 74 | `Sesli Komut` | `    🎤 <span>Sesli Komut</span>` |
| 77 | `voice` | `  <div class="drive-voice-seat" id="driveVoiceSeatCard" title="Koltuk özeti">` |
| 78 | `voice` | `    <span class="drive-voice-seat-ico">💺</span>` |
| 79 | `voice` | `    <span class="drive-voice-seat-values">` |
| 80 | `voice` | `      <b id="driveVoiceFilled">0</b>` |
| 82 | `voice` | `      <b id="driveVoiceEmpty">0</b>` |
| 86 | `voice` | `<!-- DRIVE VOICE ROW END -->` |
| 87 | `legend` | `<div class="legend">` |
| 88 | `mini-chip` | `              <div class="mini-chip">🟢 Boş</div>` |
| 89 | `mini-chip` | `              <div class="mini-chip">🔵 Bay</div>` |
| 90 | `mini-chip` | `              <div class="mini-chip">🩷 Bayan</div>` |
| 91 | `mini-chip` | `              <div class="mini-chip">🧳 Bagaj</div>` |
| 92 | `mini-chip` | `              <div class="mini-chip">🔔 İniş</div>` |
| 93 | `mini-chip` | `              <div class="mini-chip">🚌 Servis</div>` |
| 125 | `Canlı` | `                <div class="k">Canlı Durak</div>` |
| 149 | `Canlı` | `              <small>Canlı</small>` |
| 192 | `Canlı` | `              <h3>Canlı Durak Yönetimi</h3>` |
| 198 | `Sıradaki` | `                <span>Sıradaki Durak</span>` |
| 238 | `Seçili durak` | `                <span>Seçili Durak</span>` |
| 270 | `Canlı` | `                <div class="k">Canlı Durak</div>` |
| 315 | `Canlı` | `              <small>Canlı analiz</small>` |
| 319 | `Canlı` | `            <div class="ai-sub" id="aiSub">Sistem canlı rota, durak ve rötar özetini hazırlıyor.</div>` |
| 322 | `Sıradaki` | `              <div class="ai-item"><b>Sıradaki İşlem</b><span id="aiNextActionMirror">—</span></div>` |
| 323 | `Canlı` | `              <div class="ai-item"><b>Canlı Durak</b><span id="aiLiveStop">—</span></div>` |
| 326 | `Servis` | `              <div class="ai-item"><b>Servis</b><span id="aiService">—</span></div>` |
| 365 | `voice` | `<script src="/static/seats/voice-commands.js?v=voice-listen-guard-1"></script>` |
| 370 | `voice` | `<script src="/static/seats/voice-tts.js?v=voice-owner-fix-1"></script>` |
| 379 | `seat-simple` | `<script src="/static/seats/patches/seat-simple-ui-pack.js?v=1"></script>` |
| 380 | `drive-mode` | `<style id="drive-mode-actions-independent-style">` |
| 382 | `Sürüş` | `   SÜRÜŞ MODU ÜST HIZLI MENÜ - BAĞIMSIZ FINAL` |
| 465 | `drive-mode` | `<script id="drive-mode-actions-independent-js">` |
| 468 | `driveModeToggle` | `    const btn = document.getElementById("driveModeToggle");` |
| 471 | `Normal` | `    // Sürüş modunda buton "Normal" oluyor` |
| 472 | `Normal` | `    if(txt.includes("normal")) return true;` |
| 501 | `route-strip` | `      const routeShell = board.querySelector(".route-strip-shell");` |
| 568 | `Normal` | `       Normal HTML akışındaki yerinde sabit duracak. */` |
| 584 | `driveModeToggle` | `    const btn = document.getElementById("driveModeToggle");` |
| 632 | `Sürüş` | `   SÜRÜŞ / HIZ / RÖTAR SATIRI SABİTLEME` |
| 677 | `Sürüş` | `/* Sürüş butonu */` |
| 678 | `driveModeToggle` | `#driveModeToggle{` |
| 703 | `driveSpeedChip` | `#driveSpeedChip,` |
| 704 | `driveEtaChip` | `#driveEtaChip,` |
| 724 | `driveSpeedChip` | `#driveSpeedChip,` |
| 729 | `driveEtaChip` | `#driveEtaChip,` |
| 768 | `board-head` | `.board-head{` |
| 775 | `board-title` | `.board-title{` |
| 780 | `board-title` | `.board-title h2{` |
| 785 | `driveEtaChip` | `#driveEtaChip *,` |
| 797 | `driveModeToggle` | `  #driveModeToggle{` |
| 805 | `driveSpeedChip` | `  #driveSpeedChip,` |
| 806 | `driveEtaChip` | `  #driveEtaChip,` |
| 815 | `driveSpeedChip` | `  #driveSpeedChip,` |
| 820 | `driveEtaChip` | `  #driveEtaChip,` |
| 840 | `drive-mode` | `<script id="drive-mode-force-toggle-js">` |
| 864 | `drive-mode` | `    document.body.classList.toggle("drive-mode", !!on);` |
| 865 | `drive-mode` | `    document.documentElement.classList.toggle("drive-mode", !!on);` |
| 867 | `driveModeToggle` | `    const btn = document.getElementById("driveModeToggle");` |
| 869 | `Normal` | `      btn.innerHTML = on ? "↩ Normal" : "🚘 Sürüş";` |
| 870 | `Normal` | `      btn.title = on ? "Normal moda geç" : "Sürüş moduna geç";` |
| 876 | `driveEtaChip` | `    try{ if(typeof syncDriveEtaChip === "function") syncDriveEtaChip(); }catch(e){}` |
| 889 | `driveModeToggle` | `    const btn = e.target.closest && e.target.closest("#driveModeToggle");` |
| 910 | `Normal` | `<!-- DRIVE_MODE_MANUAL_NORMAL_GUARD_V20_START -->` |
| 911 | `Normal` | `<script id="drive-mode-manual-normal-guard-v20">` |
| 913 | `Normal` | `  if(window.__DRIVE_MODE_MANUAL_NORMAL_GUARD_V20__) return;` |
| 914 | `Normal` | `  window.__DRIVE_MODE_MANUAL_NORMAL_GUARD_V20__ = true;` |
| 916 | `Normal` | `  const MANUAL_KEY = "driveModeManualNormalGuard:v20";` |
| 921 | `driveModeToggle` | `    return document.getElementById("driveModeToggle");` |
| 927 | `drive-mode` | `    return document.body.classList.contains("drive-mode") \|\|` |
| 928 | `drive-mode` | `           document.documentElement.classList.contains("drive-mode") \|\|` |
| 929 | `Normal` | `           txt.includes("normal");` |
| 970 | `Normal` | `  function forceNormal(){` |
| 971 | `drive-mode` | `    document.body.classList.remove("drive-mode");` |
| 972 | `drive-mode` | `    document.documentElement.classList.remove("drive-mode");` |
| 976 | `Sürüş` | `      b.innerHTML = "🚘 Sürüş";` |
| 977 | `Sürüş` | `      b.title = "Sürüş moduna geç";` |
| 984 | `Normal` | `        detail:{ on:false, source:"manual-normal-guard-v20" }` |
| 990 | `driveModeToggle` | `    const hit = e.target && e.target.closest && e.target.closest("#driveModeToggle");` |
| 1030 | `Normal` | `      forceNormal();` |
| 1040 | `Normal` | `<!-- DRIVE_MODE_MANUAL_NORMAL_GUARD_V20_END -->` |
| 1043 | `voice` | `<!-- DRIVE VOICE MIRROR SCRIPT START -->` |
| 1044 | `voice` | `<script id="drive-voice-mirror-script">` |
| 1046 | `voice` | `  function syncDriveVoiceStats(){` |
| 1047 | `voice` | `    const oldFilled = document.getElementById("voiceSeatFilled");` |
| 1048 | `voice` | `    const oldEmpty  = document.getElementById("voiceSeatEmpty");` |
| 1049 | `voice` | `    const newFilled = document.getElementById("driveVoiceFilled");` |
| 1050 | `voice` | `    const newEmpty  = document.getElementById("driveVoiceEmpty");` |
| 1060 | `voice` | `  function bindDriveVoiceButton(){` |
| 1061 | `btnDeckAI` | `    const fakeBtn = document.getElementById("btnDeckAIDrive");` |
| 1062 | `btnDeckAI` | `    const realBtn = document.getElementById("btnDeckAI");` |
| 1081 | `voice` | `    new MutationObserver(syncDriveVoiceStats).observe(el, {` |
| 1089 | `voice` | `    bindDriveVoiceButton();` |
| 1090 | `voice` | `    syncDriveVoiceStats();` |
| 1091 | `voice` | `    watchNode("voiceSeatFilled");` |
| 1092 | `voice` | `    watchNode("voiceSeatEmpty");` |
| 1094 | `voice` | `    setTimeout(syncDriveVoiceStats, 150);` |
| 1095 | `voice` | `    setTimeout(syncDriveVoiceStats, 600);` |
| 1096 | `voice` | `    setTimeout(syncDriveVoiceStats, 1400);` |
| 1098 | `voice` | `    window.addEventListener("driveModeChanged", syncDriveVoiceStats);` |
| 1099 | `voice` | `    window.addEventListener("resize", syncDriveVoiceStats);` |
| 1109 | `voice` | `<!-- DRIVE VOICE MIRROR SCRIPT END -->` |
| 1111 | `seat-simple` | `<script id="seat-simple-bottom-bar-script">` |
| 1127 | `seat-simple` | `    document.documentElement.classList.remove("seat-simple-mode");` |
| 1128 | `seat-simple` | `    document.body.classList.remove("seat-simple-mode");` |
| 1132 | `sade koltuk moduna dön` | `      if(btn) btn.innerHTML = "💺 Sade koltuk moduna dön";` |
| 1139 | `voice` | `  function openVoice(){` |
| 1141 | `voice` | `      if(window.SeatsVoice && typeof window.SeatsVoice.startDeckAIVoice === "function"){` |
| 1142 | `voice` | `        window.SeatsVoice.startDeckAIVoice();` |
| 1147 | `btnDeckAI` | `    const btn = q("#btnDeckAI") \|\| q("#btnDeckAIDrive");` |
| 1156 | `seat-simple` | `    bar.className = "seat-simple-bottom-bar";` |
| 1158 | `seat-simple` | `      <button type="button" class="seat-simple-bottom-item primary" id="seatSimpleOpenDurak">` |
| 1163 | `seat-simple` | `      <a class="seat-simple-bottom-item" href="{{ url_for('hesap_page') }}">` |
| 1168 | `seat-simple` | `      <a class="seat-simple-bottom-item" href="{{ url_for('consignments_page') }}">` |
| 1173 | `seat-simple` | `      <a class="seat-simple-bottom-item" href="{{ url_for('live_map_page') }}">` |
| 1178 | `Sesli Komut` | `      <button type="button" class="seat-simple-bottom-item warn" id="seatSimpleVoiceBtn" title="Sesli Komut" aria-label="Sesli Komut">` |
| 1180 | `voice` | `        <span class="voice-bottom-text">Sesli<br>Komut</span>` |
| 1194 | `route-flow` | `          const flow = q("#routeStrip") \|\| q(".route-strip-shell") \|\| q(".route-flow-shell");` |
| 1202 | `voice` | `    const voice = q("#seatSimpleVoiceBtn");` |
| 1203 | `voice` | `    if(voice){` |
| 1204 | `voice` | `      voice.addEventListener("click", function(e){` |
| 1208 | `voice` | `        openVoice();` |

### `android_app/app/src/main/python/templates/start_trip.html`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 312 | `Durak Akışı` | `      Sefer başlatıldığında koltuk, hesap, emanet ve durak akışı bu hatta göre açılır.` |

### `android_app/app/src/main/python/templates/ai_console.html`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 7 | `legend` | `<style id="intent-legend-mobile-fix">` |
| 10 | `legend` | `   Sadece #intentLegend alanını etkiler.` |
| 13 | `legend` | `#intentLegend{` |
| 21 | `legend` | `#intentLegend .legend-item{` |
| 34 | `legend` | `#intentLegend .legend-item b{` |
| 45 | `legend` | `#intentLegend .legend-item span{` |
| 51 | `Normal` | `  white-space:normal !important;` |
| 63 | `legend` | `  #intentLegend .legend-item{` |
| 68 | `legend` | `  #intentLegend .legend-item b{` |
| 72 | `legend` | `  #intentLegend .legend-item span{` |
| 477 | `route-strip` | `  .route-strip{` |
| 850 | `legend` | `  .legend-list{` |
| 855 | `legend` | `  .legend-item{` |
| 867 | `legend` | `  .legend-item b{` |
| 1029 | `Normal` | `      <div class="v" id="statMode">Normal</div>` |
| 1030 | `Normal` | `      <div class="s">Normal / Öğretme</div>` |
| 1074 | `Normal` | `            <button type="button" class="mode-btn active" data-mode="normal">Normal kullanım</button>` |
| 1082 | `Boş` | `              <button type="button" class="chip" data-fill="7-8 numarayı boşalt">7-8 numarayı boşalt</button>` |
| 1084 | `Servis` | `              <button type="button" class="chip" data-fill="arka dörtlü servis tamam">arka dörtlü servis tamam</button>` |
| 1086 | `Boş` | `              <button type="button" class="chip" data-fill="kaç boş koltuk var">kaç boş koltuk var</button>` |
| 1091 | `Boş` | `                <textarea id="commandInput" class="cmd-input" placeholder="Komut yaz... örn: 7 ile 8 numarayı boşalt"></textarea>` |
| 1092 | `Sesli Komut` | `                <button type="button" id="micBtn" class="mic-btn" title="Sesli komut">🎤</button>` |
| 1106 | `route-strip` | `              <div class="route-strip">` |
| 1113 | `voice` | `              <div class="flow-card" id="voicePreview">` |
| 1114 | `Sesli Komut` | `                <h3 class="mini-title">Sesli komut önizleme</h3>` |
| 1116 | `voice` | `                <div class="preview-text" id="voicePreviewText">-</div>` |
| 1118 | `voice` | `                  <button type="button" class="btn brand" id="btnVoiceUseRun">Kullan ve çalıştır</button>` |
| 1119 | `voice` | `                  <button type="button" class="btn dark" id="btnVoiceUseOnly">Sadece alana yaz</button>` |
| 1120 | `voice` | `                  <button type="button" class="btn warn" id="btnVoiceRetry">Tekrar dinle</button>` |
| 1121 | `voice` | `                  <button type="button" class="btn ghost" id="btnVoiceCancel">İptal</button>` |
| 1237 | `İniş` | `                <label for="acTo">İniş durağı</label>` |
| 1262 | `Servis` | `                <label for="acService">Servis</label>` |
| 1274 | `Boş` | `                  <option value="">boş</option>` |
| 1275 | `Bay` | `                  <option value="bay">bay</option>` |
| 1276 | `Bay` | `                  <option value="bayan">bayan</option>` |
| 1332 | `Canlı` | `                <p class="section-sub">Canlı akış ve sistem notları</p>` |
| 1346 | `Canlı` | `            <p class="section-sub">AI Console’un aktif seferden aldığı canlı veriler.</p>` |
| 1349 | `Normal` | `            <span class="badge info" id="sideModeBadge">Mod: Normal</span>` |
| 1356 | `Canlı` | `            <h3 class="h">📡 Canlı metrikler</h3>` |
| 1357 | `legend` | `            <div class="legend-list" id="liveStatsList">` |
| 1358 | `legend` | `              <div class="legend-item"><b>Dolu koltuk</b><span id="liveSeatCount">0</span></div>` |
| 1359 | `legend` | `              <div class="legend-item"><b>Ayakta</b><span id="liveStandingCount">0</span></div>` |
| 1360 | `legend` | `              <div class="legend-item"><b>Emanet</b><span id="liveParcelCount">0</span></div>` |
| 1361 | `legend` | `              <div class="legend-item"><b>Toplam yolcu</b><span id="liveTotalPax">0</span></div>` |
| 1362 | `legend` | `              <div class="legend-item"><b>Boş koltuk</b><span id="liveEmptySeats">0</span></div>` |
| 1368 | `legend` | `            <div class="legend-list" id="intentLegend"></div>` |
| 1373 | `legend` | `            <div class="legend-list">` |
| 1374 | `legend` | `              <div class="legend-item"><b>1</b><span>Learned map ara</span></div>` |
| 1375 | `legend` | `              <div class="legend-item"><b>2</b><span>Parser ile intent bul</span></div>` |
| 1376 | `legend` | `              <div class="legend-item"><b>3</b><span>Güven düşükse suggestion ver</span></div>` |
| 1377 | `legend` | `              <div class="legend-item"><b>4</b><span>Riskliyse preview aç</span></div>` |
| 1378 | `legend` | `              <div class="legend-item"><b>5</b><span>Eksikse action form aç</span></div>` |
| 1412 | `Normal` | `    mode: 'normal',` |
| 1425 | `voice` | `    voiceText: '',` |
| 1473 | `voice` | `    voicePreview: $('#voicePreview'),` |
| 1474 | `voice` | `    voicePreviewText: $('#voicePreviewText'),` |
| 1475 | `voice` | `    btnVoiceUseRun: $('#btnVoiceUseRun'),` |
| 1476 | `voice` | `    btnVoiceUseOnly: $('#btnVoiceUseOnly'),` |
| 1477 | `voice` | `    btnVoiceRetry: $('#btnVoiceRetry'),` |
| 1478 | `voice` | `    btnVoiceCancel: $('#btnVoiceCancel'),` |
| 1530 | `legend` | `    intentLegend: $('#intentLegend'),` |
| 1549 | `voice` | `    initVoiceInput();` |
| 1628 | `voice` | `    els.btnVoiceUseRun.addEventListener('click', async () => {` |
| 1629 | `voice` | `      const text = state.voiceText \|\| '';` |
| 1630 | `voice` | `      closeVoicePreview();` |
| 1636 | `voice` | `    els.btnVoiceUseOnly.addEventListener('click', () => {` |
| 1637 | `voice` | `      const text = state.voiceText \|\| '';` |
| 1638 | `voice` | `      closeVoicePreview();` |
| 1644 | `voice` | `    els.btnVoiceRetry.addEventListener('click', () => {` |
| 1645 | `voice` | `      closeVoicePreview();` |
| 1646 | `voice` | `      startVoiceRecognition();` |
| 1649 | `voice` | `    els.btnVoiceCancel.addEventListener('click', closeVoicePreview);` |
| 1656 | `Normal` | `    state.mode = mode === 'teach' ? 'teach' : 'normal';` |
| 1661 | `Normal` | `    addMessage('sys', 'Mod değişti: ${state.mode === 'teach' ? 'Öğretme modu' : 'Normal kullanım'}');` |
| 1701 | `legend` | `    renderIntentLegend();` |
| 1765 | `legend` | `  function renderIntentLegend(){` |
| 1766 | `legend` | `    els.intentLegend.innerHTML = '';` |
| 1769 | `legend` | `      row.className = 'legend-item';` |
| 1774 | `legend` | `      els.intentLegend.appendChild(row);` |
| 1983 | `Boş` | `      els.previewTitle.textContent = 'Boşaltma önizlemesi';` |
| 1991 | `Boş` | `        row.innerHTML = '<span>Kayıt bulunamadı</span><span>Boş koltuk olabilir</span>';` |
| 2009 | `Servis` | `      els.previewTitle.textContent = 'Servis işaretleme önizlemesi';` |
| 2010 | `Servis` | `      els.previewSub.textContent = 'Bu koltuklarda servis alanı aktif olacak.';` |
| 2011 | `Servis` | `      addBadge('Servis mark', 'info');` |
| 2019 | `Servis` | `          <div>${seatRows.find(x => Number(x.seat_no) === Number(no))?.service ? 'Zaten servisli' : 'Servis işaretlenecek'}</div>` |
| 2160 | `Boş` | `        if (!seats.length) throw new Error('Boşaltılacak koltuk bulunamadı.');` |
| 2173 | `Boş` | `          label:'Koltuk boşaltma geri alma',` |
| 2178 | `Boş` | `        addMessage('ok', 'Boşaltma uygulandı.\nSilinen koltuklar: ${(data.deleted \|\| seats).join(', ')}');` |
| 2187 | `Servis` | `        if (!seats.length) throw new Error('Servis işaretlenecek koltuk bulunamadı.');` |
| 2198 | `Servis` | `        addMessage('ok', 'Servis işlendi.\nKoltuklar: ${(data.updated \|\| seats).join(', ')}');` |
| 2314 | `Boş` | `    if (/(bos koltuk\|boş koltuk)/.test(text)) {` |
| 2315 | `Boş` | `      addMessage('info', 'Şu an ${emptySeats} boş koltuk var.');` |
| 2348 | `Servis` | `    if (/(servis)/.test(text) && /(kac\|kaç)/.test(text)) {` |
| 2350 | `Servis` | `      addMessage('info', 'Servis işaretli ${serviceCt} koltuk var.');` |
| 2377 | `Bay` | `    if (/(bayan\|kadin\|kadın)/.test(text) && /(hangi koltuk\|koltuklar)/.test(text)) {` |
| 2378 | `Bay` | `      const rows = seats.filter(x => norm(x.gender \|\| '') === 'bayan').map(x => x.seat_no);` |
| 2379 | `Bay` | `      addMessage('info', rows.length ? 'Bayan görünen koltuklar: ${rows.join(', ')}' : 'Bayan işaretli koltuk yok.');` |
| 2383 | `Bay` | `    if (/(erkek\|bay)/.test(text) && /(hangi koltuk\|koltuklar)/.test(text)) {` |
| 2384 | `Bay` | `      const rows = seats.filter(x => norm(x.gender \|\| '') === 'bay').map(x => x.seat_no);` |
| 2385 | `Bay` | `      addMessage('info', rows.length ? 'Bay görünen koltuklar: ${rows.join(', ')}' : 'Bay işaretli koltuk yok.');` |
| 2454 | `Boş` | `        addMessage('ok', 'Son boşaltma işlemi geri alındı.');` |
| 2467 | `Normal` | `    els.statMode.textContent = state.mode === 'teach' ? 'Öğretme' : 'Normal';` |
| 2468 | `Normal` | `    els.sideModeBadge.textContent = 'Mod: ${state.mode === 'teach' ? 'Öğretme' : 'Normal'}';` |
| 2485 | `voice` | `    closeVoicePreview();` |
| 2580 | `Normal` | `      .normalize('NFKD')` |
| 2599 | `voice` | `  function closeVoicePreview(){` |
| 2600 | `voice` | `    state.voiceText = '';` |
| 2601 | `voice` | `    els.voicePreview.classList.remove('open');` |
| 2602 | `voice` | `    els.voicePreviewText.textContent = '-';` |
| 2616 | `voice` | `  function initVoiceInput(){` |
| 2622 | `Sesli Komut` | `      addMessage('warn', 'Bu cihazda/tarayıcıda sesli komut desteklenmiyor.');` |
| 2646 | `Sesli Komut` | `      addMessage('err', 'Sesli komut hatası: ' + (event.error \|\| 'bilinmiyor'));` |
| 2656 | `voice` | `      state.voiceText = text;` |
| 2657 | `voice` | `      els.voicePreviewText.textContent = text;` |
| 2658 | `voice` | `      els.voicePreview.classList.add('open');` |
| 2659 | `Sesli Komut` | `      addMessage('info', 'Sesli komut algılandı. Önizlemeden onaylayabilirsin.');` |
| 2668 | `voice` | `      startVoiceRecognition();` |
| 2672 | `voice` | `  function startVoiceRecognition(){` |
| 2674 | `voice` | `      closeVoicePreview();` |

### `android_app/app/src/main/python/templates/route_schedule_edit.html`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 1234 | `Boş` | `          İlk durakta segment km boş kalabilir.` |
| 1306 | `Durak Akışı` | `            <br>• Durak Akışı kutusunda plan saat olarak` |

### `android_app/app/src/main/python/templates/trip_report.html`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 104 | `legend` | `  .legend{` |
| 546 | `legend` | `      <div class="legend">` |
| 617 | `Bay` | `  if(g === "bay") return "Bay";` |
| 618 | `Bay` | `  if(g === "bayan") return "Bayan";` |
| 756 | `Boş` | `  return h.active ? "Son durum: koltuk seferde dolu görünüyor." : "Son durum: koltuk boş / yolcu inmiş görünüyor.";` |
| 799 | `İniş` | `        title = "🟣 İniş durağı değişti";` |
| 817 | `İniş` | `      <div class="seat-stat"><div class="k">İniş</div><div class="v">${h.offload_count \|\| 0}</div></div>` |

### `android_app/app/src/main/python/templates/rehber.html`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 743 | `voice` | `  .guide-voice-list{` |
| 749 | `voice` | `  .guide-voice-item{` |
| 764 | `voice` | `  .guide-voice-item p{` |
| 1384 | `voice` | `.guide-voice-list{` |
| 1392 | `voice` | `.guide-voice-item{` |
| 1399 | `voice` | `.guide-voice-item .cmd{` |
| 1413 | `voice` | `.guide-voice-item p{` |
| 1542 | `voice` | `  .guide-voice-item p,` |
| 1547 | `voice` | `  .guide-voice-item{` |
| 1786 | `voice` | `.guide-voice-list{` |
| 1790 | `voice` | `.guide-voice-item{` |
| 1794 | `voice` | `.guide-voice-item:hover{` |
| 1857 | `voice` | `  .guide-voice-list{` |
| 2185 | `voice` | `.guide-voice-item p{` |
| 2290 | `Sesli Komut` | `          Koltuk, durak, bagaj, emanet, hesap ve sesli komutlar. Hepsi tek, sade ve güçlü bir ekranda.` |
| 2311 | `Bagaj` | `          <div class="hero-floating f3">🧳 Bagaj kontrolü</div>` |
| 2326 | `Bagaj` | `          <p>Yolcu, cinsiyet, iniş durağı, servis ve bagaj bilgisi aynı akışta görünür.</p>` |
| 2333 | `Canlı` | `          <h3>Canlı durak. İnişleri kaçırma.</h3>` |
| 2334 | `Canlı` | `          <p>Seçili, canlı ve sıradaki durak bilgisi sahada hızlı karar aldırır.</p>` |
| 2336 | `Canlı` | `            <img src="{{ url_for('static', filename='img/rehber-durak-akisi-card.png') }}" alt="Canlı durak">` |
| 2341 | `Sesli Komut` | `          <h3>Sesli komut. Ekrana daha az bak.</h3>` |
| 2342 | `Bagaj` | `          <p>“Kaç yolcu var”, “Rötar kaç”, “Bu durakta bagaj var mı” gibi kısa komutlarla bilgi al.</p>` |
| 2344 | `Sesli Komut` | `            <img src="{{ url_for('static', filename='img/rehber-voice-command-card.png') }}" alt="Sesli komut">` |
| 2372 | `Bagaj` | `              <span>Koltuk, durak, bagaj, servis ve hesap takibi.</span>` |
| 2376 | `Sesli Komut` | `              <span>Sahada kullanılabilecek kısa sesli komut.</span>` |
| 2379 | `Canlı` | `              <b>Canlı</b>` |
| 2380 | `Sıradaki` | `              <span>Durak, sıradaki nokta ve rötar bilgisi.</span>` |
| 2410 | `Bagaj` | `            <p>Koltuk planı üzerinden biniş, iniş, cinsiyet, ödeme, servis ve bagaj bilgileri düzenli tutulur.</p>` |
| 2414 | `Servis` | `              <span>Servis işle</span>` |
| 2415 | `Bagaj` | `              <span>Bagaj gör</span>` |
| 2425 | `Canlı` | `            <small>Canlı Durak</small>` |
| 2426 | `Sıradaki` | `            <h3>Sıradaki nokta hep belli.</h3>` |
| 2427 | `Canlı` | `            <p>Canlı durak, yaklaşan durak, rötar ve iniş yoğunluğu daha görünür olur.</p>` |
| 2429 | `Canlı` | `              <span>Canlı durak</span>` |
| 2430 | `Sıradaki` | `              <span>Sıradaki durak</span>` |
| 2432 | `İniş` | `              <span>İniş özeti</span>` |
| 2436 | `Canlı` | `            <img src="{{ url_for('static', filename='img/rehber-durak-akisi.png') }}" alt="Canlı durak takibi">` |
| 2442 | `Sesli Komut` | `            <small>Sesli Komut</small>` |
| 2448 | `Bagaj` | `              <span>Bagaj var mı</span>` |
| 2453 | `Sesli Komut` | `            <img src="{{ url_for('static', filename='img/rehber-voice-command.png') }}" alt="Sesli komut">` |
| 2498 | `Bagaj` | `              <div class="guide-line"><b>Koltuk ekranını kullan</b><span>Koltuk planı ekranında yolcu ekleme, indirme, ayakta yolcu, servis, durak ve bagaj işlemleri aynı ekrandan yapılır.</span></div>` |
| 2503 | `voice` | `          <article class="guide-card guide-searchable" id="guideVoiceSection" data-guide-cat="sesli">` |
| 2507 | `Sesli Komut` | `                <h3>Sesli Komutlar</h3>` |
| 2514 | `voice` | `            <div class="guide-voice-list">` |
| 2515 | `voice` | `              <div class="guide-voice-item"><div class="cmd">Kaç yolcu var</div><p>Toplam yolcu sayısını, oturan ve ayakta durumuyla birlikte söyler.</p></div>` |
| 2516 | `voice` | `              <div class="guide-voice-item"><div class="cmd">Ayakta kaç kişi var</div><p>Ayakta yolcu sayısını ve ayakta tahsilatı söyler.</p></div>` |
| 2517 | `Seçili durak` | `              <div class="guide-voice-item"><div class="cmd">Hangi duraktayız</div><p>Canlı veya seçili durak bilgisini verir.</p></div>` |
| 2518 | `voice` | `              <div class="guide-voice-item"><div class="cmd">Rötar kaç</div><p>Bir sonraki saatli durağın gecikmesini söyler.</p></div>` |
| 2519 | `voice` | `              <div class="guide-voice-item"><div class="cmd">Bir sonraki durak</div><p>Sıradaki saatli noktayı sesli söyler.</p></div>` |
| 2523 | `voice` | `            <div class="guide-voice-list">` |
| 2524 | `voice` | `              <div class="guide-voice-item"><div class="cmd">Alaşehir kaç yolcu var</div><p>Belirtilen durakta inecek yolcu özetini söyler.</p></div>` |
| 2525 | `Seçili durak` | `              <div class="guide-voice-item"><div class="cmd">Bu durakta işlem var mı</div><p>Seçili durakta yolcu, bagaj, emanet ve servis durumunu özetler.</p></div>` |
| 2526 | `Seçili durak` | `              <div class="guide-voice-item"><div class="cmd">Bu durakta kimler inecek</div><p>Seçili duraktaki iniş durumunu sesli anlatır.</p></div>` |
| 2527 | `Seçili durak` | `              <div class="guide-voice-item"><div class="cmd">Bu durakta bagaj var mı</div><p>Seçili durak için bagaj bilgisini söyler.</p></div>` |
| 2528 | `voice` | `              <div class="guide-voice-item"><div class="cmd">Durak seç Alaşehir</div><p>Seçili durağı değiştirir.</p></div>` |
| 2529 | `Seçili durak` | `              <div class="guide-voice-item"><div class="cmd">İnecekleri indir</div><p>Seçili duraktaki indirme akışını başlatır.</p></div>` |
| 2544 | `Boş` | `              <div class="guide-line"><b>Toplu giriş</b><span>Birden fazla boş koltuğu seç, toplu giriş ekranını aç, bilgileri tek seferde işle.</span></div>` |
| 2546 | `Sesli Komut` | `              <div class="guide-line"><b>Servis işaretleme</b><span>Koltuk seçerek ya da sesli komutla servis bilgisini işaretle.</span></div>` |
| 2548 | `Bagaj` | `              <div class="guide-line"><b>Bagaj ve emanet kontrolü</b><span>İniş durağında yolcu özetine ek olarak bagaj ve emanet bilgisini kontrol et.</span></div>` |
| 2556 | `Sürüş` | `                <h3>Sürüşte Kullanım</h3>` |
| 2557 | `Sürüş` | `                <div class="guide-card-sub">Sürüş modu daha sade, daha hızlı ve sahaya uygun görünüm sunar.</div>` |
| 2562 | `Sürüş` | `              <div class="guide-line"><b>Sürüş modu ne işe yarar</b><span>Ekranı sadeleştirir. En gerekli alanları öne çıkarır. Sesli komut kullanımı daha rahat olur.</span></div>` |
| 2563 | `Sürüş` | `              <div class="guide-line"><b>Sesli komut butonu</b><span>Sürüş modunda büyük mor buton üzerinden hızlı sesli komut kullanılabilir.</span></div>` |
| 2564 | `Sürüş` | `              <div class="guide-line"><b>Hız ve rötar kutusu</b><span>Üst alanda anlık hız ve zaman durumu özetlenir. Sürüşte takip kolaylaşır.</span></div>` |
| 2565 | `Durak Akışı` | `              <div class="guide-line"><b>Canlı durak ve sıradaki durak</b><span>Durak akışı kutuları ile aktif nokta ve yaklaşan nokta hızlıca takip edilir.</span></div>` |
| 2566 | `Sürüş` | `              <div class="guide-line"><b>Öneri</b><span>Sürüşte komutları kısa ver: “Kaç yolcu var”, “Hangi duraktayız”, “Rötar kaç” gibi.</span></div>` |
| 2581 | `Sesli Komut` | `              <div class="guide-line"><b>Sesli komut dinliyor ama işlem yapmıyorsa</b><span>Komutu daha kısa söyle. Durak adını ve koltuk numarasını net telaffuz et.</span></div>` |
| 2583 | `Seçili durak` | `              <div class="guide-line"><b>Durak yanlış görünüyorsa</b><span>Seçili durak ile canlı durak durumunu karşılaştır. Gerekirse manuel durak seç.</span></div>` |
| 2584 | `Canlı` | `              <div class="guide-line"><b>GPS çalışmıyorsa</b><span>Konum izni, internet bağlantısı ve canlı takip açık mı kontrol et.</span></div>` |
| 2607 | `Bagaj` | `              <div class="guide-chip">9. Bu durakta bagaj var mı</div>` |
| 2613 | `Bagaj` | `              <p>Mikrofona bastıktan sonra kısa ve tek komut ver. Uzun cümle yerine net ifade kullan: “Rötar kaç”, “Durak seç Alaşehir”, “Bu durakta bagaj var mı”.</p>` |

### `android_app/app/src/main/python/templates/live_map.html`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 6 | `Canlı` | `  <title>Canlı Harita</title>` |
| 226 | `legend` | `    .legend{` |
| 233 | `legend` | `    .legend span{` |
| 960 | `legend` | `body.map-fullscreen-mode .legend{` |
| 1024 | `Canlı` | `/* Canlı harita popup kompakt görünüm */` |
| 1613 | `Normal` | `/* Normal mod */` |
| 1727 | `Canlı` | `      <a class="back" href="{{ url_for('continue_trip') }}">← Canlı Akış</a>` |
| 1729 | `Canlı` | `        <h1>Canlı Harita</h1>` |
| 1736 | `Canlı` | `        <small>Canlı durak</small>` |
| 1741 | `Sıradaki` | `        <small>Sıradaki işlem</small>` |
| 1746 | `legend` | `    <div class="legend">` |
| 1747 | `Canlı` | `      <span>🔴 Canlı</span>` |
| 1748 | `Sıradaki` | `      <span>🟡 Sıradaki işlem</span>` |
| 1797 | `Sıradaki` | `          <div class="next-ops-title">Sıradaki İşlemler</div>` |
| 1871 | `Canlı` | `            <svg viewBox="0 0 300 150" xmlns="http://www.w3.org/2000/svg" aria-label="Canlı otobüs">` |
| 2032 | `Canlı` | `      if(kind === "live") stateText = "Canlı Durak";` |
| 2033 | `Sıradaki` | `      else if(kind === "next") stateText = "Sıradaki İşlem";` |
| 2048 | `Bagaj` | `        if(bag) parts.push('${bag} bagaj');` |
| 2072 | `Bagaj` | `              <small>Bagaj</small>` |
| 2089 | `Bagaj` | `            <a class="bag" href="{{ url_for('continue_trip') }}?stop=${encodeURIComponent(stop.name)}">Bagaj</a>` |
| 2402 | `Bagaj` | `      if(bag) parts.push('${bag} bagaj');` |
| 2518 | `Bagaj` | `      if(bag) parts.push('${bag} bagaj');` |
| 2796 | `voice` | `<!-- VOICE_MAP_FULLSCREEN_PATCH_START -->` |
| 2797 | `voice` | `<style id="voice-map-fullscreen-style">` |
| 2798 | `voice` | `  html.voice-map-fullscreen,` |
| 2799 | `voice` | `  body.voice-map-fullscreen{` |
| 2808 | `voice` | `  body.voice-map-fullscreen #map{` |
| 2820 | `voice` | `  body.voice-map-fullscreen .leaflet-control-container{` |
| 2825 | `voice` | `  body.voice-map-fullscreen .topbar,` |
| 2826 | `voice` | `  body.voice-map-fullscreen .page-header,` |
| 2827 | `voice` | `  body.voice-map-fullscreen .map-header,` |
| 2828 | `voice` | `  body.voice-map-fullscreen .live-map-header,` |
| 2829 | `voice` | `  body.voice-map-fullscreen .map-hero,` |
| 2830 | `voice` | `  body.voice-map-fullscreen .map-summary,` |
| 2831 | `voice` | `  body.voice-map-fullscreen .bottom-nav,` |
| 2832 | `voice` | `  body.voice-map-fullscreen .bottom-bar{` |
| 2836 | `voice` | `  body.voice-map-fullscreen main,` |
| 2837 | `voice` | `  body.voice-map-fullscreen .map-shell,` |
| 2838 | `voice` | `  body.voice-map-fullscreen .live-map-shell,` |
| 2839 | `voice` | `  body.voice-map-fullscreen .content{` |
| 2848 | `voice` | `  #voiceMapFullscreenExit{` |
| 2869 | `voice` | `  #voiceMapFullscreenExit:active{` |
| 2874 | `voice` | `<script id="voice-map-fullscreen-script">` |
| 2884 | `voice` | `  document.documentElement.classList.add("voice-map-fullscreen");` |
| 2885 | `voice` | `  document.body.classList.add("voice-map-fullscreen");` |
| 2888 | `voice` | `    if(document.getElementById("voiceMapFullscreenExit")) return;` |
| 2891 | `voice` | `    btn.id = "voiceMapFullscreenExit";` |
| 2923 | `voice` | `<!-- VOICE_MAP_FULLSCREEN_PATCH_END -->` |

### `android_app/app/src/main/python/templates/settings_subscription.html`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 340 | `Normal` | `      font-style:normal;` |
| 1122 | `Boş` | `            <div class="feature"><i>✓</i><span>Koltuk satış / boşaltma işlemleri</span></div>` |

### `android_app/app/src/main/python/templates/onboarding.html`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 200 | `Canlı` | `        <div class="slide"><img src="/static/img/onboarding/slides/onboarding_4.png" alt="Canlı Konum Takibi"></div>` |
| 203 | `Sesli Komut` | `        <div class="slide"><img src="/static/img/onboarding/slides/onboarding_7.png" alt="Sesli Komut Desteği"></div>` |

### `android_app/app/src/main/python/templates/continue_trip.html`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 6 | `Durak Akışı` | `  <title>Canlı Durak Akışı</title>` |
| 99 | `Sesli Komut` | `      <a class="brand-action" href="{{ url_for('seats_page') }}?drive=1" aria-label="Sesli komut">` |
| 105 | `Canlı` | `      <img class="hero-bus-img" src="{{ url_for('static', filename='img/live-hero-bus.png', v='1') }}" alt="Canlı durak otobüs görseli">` |
| 108 | `Durak Akışı` | `      <h1 class="hero-title">Canlı Durak Akışı</h1>` |
| 137 | `Bay` | `          <span class="male">Bay {{ live_summary.male_count or 0 }}</span>` |
| 138 | `Bay` | `          <span class="female">Bayan {{ live_summary.female_count or 0 }}</span>` |
| 157 | `Canlı` | `        <div class="card live live-summary-trigger" id="liveCurrentCard" role="button" tabindex="0" aria-label="Canlı durak özetini aç">` |
| 164 | `Canlı` | `            <span class="status-pill live">{{ live_current.status or "Canlı" }}</span>` |
| 184 | `Bagaj` | `            <button class="metric metric-action" type="button" id="liveBagajMetric" data-kind="bagaj" aria-label="Bu durakta indirilecek bagajları göster">` |
| 185 | `Bagaj` | `              <small>Bagaj</small>` |
| 186 | `Bagaj` | `              <b id="liveBagajCount">{{ live_current.bagaj_count or 0 }}</b>` |
| 232 | `Bagaj` | `              <small>Bagaj</small>` |
| 233 | `Bagaj` | `              <b>{{ stop.bagaj_label }}</b>` |
| 249 | `Canlı` | `          <div class="sheet-kicker" id="liveStopSheetKicker">Canlı durak</div>` |
| 439 | `voice` | `<script src="/static/seats/voice-tts.js?v=continue-tts-bridge-1"></script>` |
| 447 | `Bagaj` | `      <div class="bag-viewer-kicker">Bagaj fotoğrafı</div>` |
| 456 | `Bagaj` | `      <img class="bag-viewer-img" id="bagViewerImg" src="" alt="Bagaj fotoğrafı">` |
| 499 | `Bagaj` | `    liveBagajCount: {{ (live_current.bagaj_count if live_current and live_current.bagaj_count is defined else 0) \| tojson \| safe }},` |

### `android_app/app/src/main/python/templates/seats_parts/modals.html`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 12 | `İniş` | `        <span>İniş Yeri</span>` |
| 29 | `Bay` | `        <label><input type="radio" name="gender" value="bay"> Bay</label>` |
| 30 | `Bay` | `        <label><input type="radio" name="gender" value="bayan"> Bayan</label>` |
| 31 | `Boş` | `        <label><input type="radio" name="gender" value=""> Boş</label>` |
| 37 | `Servis` | `      <label><input type="checkbox" id="service"> Servis kullanacak</label>` |
| 41 | `Bagaj` | `      <button class="btn primary" type="button" id="btnBagAdd">🧳 Bagaj Ekle</button>` |
| 42 | `Bagaj` | `      <button class="btn dark" type="button" id="btnBagView">📸 Bagaj Gör</button>` |
| 51 | `Servis` | `        <span>Servis Notu</span>` |
| 71 | `Boş` | `    <button class="btn danger" type="button" id="btnSeatOffload">İniş (Boşalt)</button>` |
| 109 | `Servis` | `      <label><input type="checkbox" id="bulkService"> Servis</label>` |
| 112 | `Boş` | `    <div class="muted">Çoklu seçim açıksa koltukları elle seçersin. Kapalıysa sistem boş koltuklardan yerleştirir.</div>` |

### `android_app/app/src/main/python/templates/seats_parts/topbar.html`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 22 | `mini-chip` | `        <div class="mini-chip">📍 <span>Durak</span> <b id="topLiveStop">—</b></div>` |
| 23 | `mini-chip` | `        <div class="mini-chip">🚦 <span>Hız</span> <b id="topSpeed">0 km/h</b></div>` |
| 24 | `mini-chip` | `        <div class="mini-chip">🕒 <span>Saat</span> <b id="topClock">--:--</b></div>` |
| 25 | `mini-chip` | `        <div class="mini-chip">🎯 <span>Doluluk</span> <b id="topOcc">0%</b></div>` |

### `android_app/app/src/main/python/templates/seats_parts/stats.html`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 7 | `Boş` | `      <div class="k">Boş Koltuk</div>` |
| 19 | `Servis` | `      <div class="k">Servis</div>` |

### `android_app/app/src/main/python/templates/seats_parts/route_flow.html`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 1 | `route-strip` | `<div class="route-strip-shell">` |
| 2 | `route-strip` | `  <div class="route-strip-head">` |
| 3 | `Durak Akışı` | `    <div class="route-strip-title">Durak Akışı</div>` |
| 5 | `route-strip` | `    <div class="route-strip-meta">` |
| 8 | `Canlı` | `        <span class="route-mini-label">Canlı:</span>` |
| 15 | `Sıradaki` | `        <span class="route-mini-label">Sıradaki:</span>` |
| 21 | `voice` | `      <button id="nightVoiceToggle" class="night-voice-toggle" type="button" title="Sesli robot">🔊 Ses Açık</button>` |
| 25 | `route-strip` | `  <div class="route-strip" id="routeStrip">` |
| 26 | `route-stop` | `    <div class="route-stop active">` |

### `android_app/app/src/main/python/templates/seats_parts/deck.html`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 1 | `board-stage` | `<div class="board-stage">` |
| 14 | `Servis` | `                    <span class="svc-badge" title="Servis">🚌</span>` |
| 15 | `Bagaj` | `                    <span class="bag-badge" title="Bagaj"><span class="bag-dir"></span><span class="bag-count">0</span></span>` |

### `android_app/app/src/main/python/templates/seats_parts/offload_confirm.html`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 177 | `Seçili durak` | `        <p class="offload-small">Seçili durak işlemi yapılacak.</p>` |
| 226 | `Seçili durak` | `    stopEl.textContent = stop \|\| "seçili durak";` |

### `android_app/app/src/main/python/static/seats/seats.css`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 133 | `mini-chip` | `  .mini-chip{` |
| 150 | `mini-chip` | `  .mini-chip b{` |
| 182 | `voice` | `  .voice-command-btn:hover{` |
| 286 | `board-head` | `  .board-head{` |
| 294 | `board-title` | `  .board-title{` |
| 317 | `board-title` | `  .board-title h2{` |
| 325 | `board-title` | `  .board-title small{` |
| 331 | `board-head` | `  .board-head-right{` |
| 339 | `voice` | `  .voice-row{` |
| 347 | `voice` | `  .voice-command-btn{` |
| 370 | `voice` | `  .voice-command-btn.listening{` |
| 375 | `voice` | `  .voice-state{` |
| 389 | `legend` | `  .legend{` |
| 396 | `legend` | `  .legend .mini-chip{` |
| 402 | `selected-stop` | `  .selected-stop-chip{` |
| 419 | `route-strip` | `  .route-strip-shell{` |
| 428 | `route-strip` | `  .route-strip-head{` |
| 437 | `route-strip` | `  .route-strip-title{` |
| 443 | `route-strip` | `  .route-strip-meta{` |
| 464 | `route-strip` | `  .route-strip{` |
| 472 | `route-strip` | `  .route-strip::-webkit-scrollbar{ display:none; }` |
| 474 | `route-stop` | `  .route-stop{` |
| 490 | `route-stop` | `  .route-stop .name{` |
| 497 | `route-stop` | `  .route-stop .meta{` |
| 503 | `route-stop` | `  .route-stop .extra{` |
| 509 | `route-stop` | `  .route-stop .extra-line{` |
| 518 | `route-stop` | `  .route-stop .extra-k{` |
| 524 | `route-stop` | `  .route-stop .extra-v{` |
| 531 | `route-stop` | `  .route-stop.active{` |
| 539 | `route-stop` | `  .route-stop.done{` |
| 543 | `board-stage` | `  .board-stage{` |
| 1368 | `board-stage` | `    .board-stage{` |
| 1435 | `mini-chip` | `    .mini-chip{` |
| 1458 | `board-head` | `    .board-head{` |
| 1463 | `board-title` | `    .board-title h2{` |
| 1467 | `board-head` | `    .board-head-right{` |
| 1473 | `voice` | `    .voice-row{` |
| 1478 | `voice` | `    .voice-command-btn{` |
| 1487 | `voice` | `    .voice-state{` |
| 1493 | `legend` | `    .legend{` |
| 1498 | `route-strip` | `    .route-strip-shell{` |
| 1503 | `route-stop` | `    .route-stop{` |
| 1509 | `board-stage` | `    .board-stage{` |
| 1571 | `voice` | `    .voice-command-btn{` |
| 1577 | `voice` | `    .voice-state{` |
| 1582 | `board-stage` | `    .board-stage{` |
| 1586 | `route-stop` | `    .route-stop{` |
| 1595 | `route-stop` | `.route-stop.live-danger{` |
| 1605 | `route-stop` | `.route-stop.live-danger .name,` |
| 1606 | `route-stop` | `.route-stop.live-danger .meta,` |
| 1607 | `route-stop` | `.route-stop.live-danger .extra-k,` |
| 1608 | `route-stop` | `.route-stop.live-danger .extra-v{` |
| 1623 | `route-stop` | `.route-stop.next-warning{` |
| 1632 | `route-stop` | `.route-stop.next-warning .name,` |
| 1633 | `route-stop` | `.route-stop.next-warning .meta,` |
| 1634 | `route-stop` | `.route-stop.next-warning .extra-k,` |
| 1635 | `route-stop` | `.route-stop.next-warning .extra-v{` |
| 1639 | `route-stop` | `.route-stop.flow-green{` |
| 1687 | `Canlı` | `  /* Üst canlı bilgiler 2 sütun küçük chip */` |
| 1694 | `mini-chip` | `  .route-live-row .mini-chip{` |
| 1745 | `Boş` | `  /* Koltuk kartının üst boşluğunu azalt */` |
| 1751 | `board-head` | `  .board-head{` |
| 1761 | `board-title` | `  .board-title h2{` |
| 1765 | `board-title` | `  .board-title small{` |
| 1769 | `selected-stop` | `  .selected-stop-chip{` |
| 1775 | `Sesli Komut` | `  /* Sesli komut ve legend kısmı daha kompakt */` |
| 1776 | `board-head` | `  .board-head-right{` |
| 1780 | `voice` | `  .voice-row{` |
| 1784 | `voice` | `  .voice-command-btn{` |
| 1789 | `voice` | `  .voice-state{` |
| 1794 | `legend` | `  .legend{` |
| 1798 | `legend` | `  .legend .mini-chip{` |
| 1804 | `Durak Akışı` | `  /* Durak akışı daha yukarı ve daha kompakt */` |
| 1805 | `route-strip` | `  .route-strip-shell{` |
| 1812 | `route-strip` | `  .route-strip-head{` |
| 1816 | `route-strip` | `  .route-strip-title{` |
| 1825 | `route-stop` | `  .route-stop{` |
| 1832 | `board-stage` | `  .board-stage{` |
| 1856 | `board-title` | `  .board-title h2{` |
| 1860 | `voice` | `  .voice-command-btn{` |
| 1864 | `route-stop` | `  .route-stop{` |
| 1871 | `Sürüş` | `   SÜRÜŞ MODU` |
| 1875 | `driveModeToggle` | `#driveModeToggle{` |
| 1892 | `driveModeToggle` | `body.drive-mode #driveModeToggle{` |
| 1896 | `drive-mode` | `body.drive-mode .topbar,` |
| 1897 | `drive-mode` | `body.drive-mode .status-row,` |
| 1898 | `drive-mode` | `body.drive-mode .panel-card{` |
| 1902 | `drive-mode` | `body.drive-mode .seats-shell{` |
| 1908 | `drive-mode` | `body.drive-mode .layout{` |
| 1912 | `drive-mode` | `body.drive-mode .board-card{` |
| 1918 | `drive-mode` | `body.drive-mode .board-head{` |
| 1926 | `drive-mode` | `body.drive-mode .board-kicker,` |
| 1927 | `drive-mode` | `body.drive-mode .board-title h2,` |
| 1928 | `drive-mode` | `body.drive-mode .board-title small,` |
| 1929 | `legend` | `body.drive-mode .legend{` |
| 1933 | `selected-stop` | `body.drive-mode .selected-stop-chip{` |
| 1939 | `drive-mode` | `body.drive-mode .board-head-right{` |
| 1944 | `voice` | `body.drive-mode .voice-row{` |
| 1949 | `voice` | `body.drive-mode .voice-command-btn{` |
| 1957 | `voice` | `body.drive-mode .voice-state{` |
| 1961 | `route-strip` | `body.drive-mode .route-strip-shell{` |
| 1968 | `route-strip` | `body.drive-mode .route-strip-head{` |
| 1972 | `route-strip` | `body.drive-mode .route-strip-title{` |
| 1976 | `drive-mode` | `body.drive-mode .route-pill{` |
| 1982 | `route-stop` | `body.drive-mode .route-stop{` |
| 1989 | `drive-mode` | `body.drive-mode .board-stage{` |
| 1995 | `driveModeToggle` | `  #driveModeToggle{` |
| 2003 | `drive-mode` | `  body.drive-mode .seats-shell{` |
| 2007 | `drive-mode` | `  body.drive-mode .board-card{` |
| 2012 | `drive-mode` | `  body.drive-mode .board-head{` |
| 2017 | `drive-mode` | `  body.drive-mode .board-head-right{` |
| 2021 | `voice` | `  body.drive-mode .voice-row{` |
| 2026 | `selected-stop` | `  body.drive-mode .selected-stop-chip{` |
| 2033 | `voice` | `  body.drive-mode .voice-command-btn{` |
| 2038 | `route-strip` | `  body.drive-mode .route-strip-shell{` |
| 2043 | `route-stop` | `  body.drive-mode .route-stop{` |
| 2048 | `drive-mode` | `  body.drive-mode .board-stage{` |
| 2055 | `Sürüş` | `   SÜRÜŞ MODU İNCE AYAR v2` |
| 2056 | `Durak Akışı` | `   Daha temiz üst alan + düzgün durak akışı + okunaklı koltuk yazıları` |
| 2059 | `Sürüş` | `/* Sürüş modu ana ekranı daha sıkı */` |
| 2060 | `drive-mode` | `body.drive-mode{` |
| 2064 | `Normal` | `/* Normal butonu tarayıcı üst çubuğuna çok yapışmasın */` |
| 2065 | `driveModeToggle` | `body.drive-mode #driveModeToggle{` |
| 2075 | `Sürüş` | `/* Sürüş modunda ana kart ekrana tam otursun */` |
| 2076 | `drive-mode` | `body.drive-mode .seats-shell{` |
| 2080 | `drive-mode` | `body.drive-mode .board-card{` |
| 2086 | `Seçili durak` | `/* Üst başlık alanı: seçili durak + sesli komut */` |
| 2087 | `drive-mode` | `body.drive-mode .board-head{` |
| 2094 | `Seçili durak` | `/* Seçili durak rozeti daha net */` |
| 2095 | `selected-stop` | `body.drive-mode .selected-stop-chip{` |
| 2108 | `Sürüş` | `/* Sesli komut butonu sürüş modunda daha kullanışlı */` |
| 2109 | `voice` | `body.drive-mode .voice-row{` |
| 2113 | `voice` | `body.drive-mode .voice-command-btn{` |
| 2123 | `Durak Akışı` | `/* Durak akışı kutusu daha profesyonel */` |
| 2124 | `route-strip` | `body.drive-mode .route-strip-shell{` |
| 2134 | `route-strip` | `body.drive-mode .route-strip-head{` |
| 2142 | `route-strip` | `body.drive-mode .route-strip-title{` |
| 2148 | `route-strip` | `body.drive-mode .route-strip-meta{` |
| 2153 | `drive-mode` | `body.drive-mode .route-pill{` |
| 2161 | `route-strip` | `body.drive-mode .route-strip{` |
| 2169 | `Sürüş` | `/* Sürüş modunda durak kartları daha okunaklı */` |
| 2170 | `route-stop` | `body.drive-mode .route-stop{` |
| 2177 | `route-stop` | `body.drive-mode .route-stop .name{` |
| 2186 | `route-stop` | `body.drive-mode .route-stop .meta{` |
| 2194 | `route-stop` | `body.drive-mode .route-stop .extra-line{` |
| 2198 | `route-stop` | `body.drive-mode .route-stop.active{` |
| 2203 | `drive-mode` | `body.drive-mode .board-stage{` |
| 2209 | `Boş` | `/* Koltuk çevresindeki dış boşluğu azalt */` |
| 2210 | `drive-mode` | `body.drive-mode .deck{` |
| 2216 | `drive-mode` | `body.drive-mode .label{` |
| 2229 | `drive-mode` | `body.drive-mode .cell{` |
| 2233 | `Bagaj` | `/* Bagaj/iniş rozetleri koltuk üstünde daha düzgün dursun */` |
| 2234 | `drive-mode` | `body.drive-mode .bag-badge{` |
| 2242 | `drive-mode` | `body.drive-mode .stop-badge{` |
| 2251 | `drive-mode` | `body.drive-mode .fab-column{` |
| 2257 | `drive-mode` | `body.drive-mode .fab{` |
| 2266 | `driveModeToggle` | `  body.drive-mode #driveModeToggle{` |
| 2274 | `drive-mode` | `  body.drive-mode .board-head{` |
| 2278 | `selected-stop` | `  body.drive-mode .selected-stop-chip{` |
| 2285 | `voice` | `  body.drive-mode .voice-command-btn{` |
| 2292 | `route-strip` | `  body.drive-mode .route-strip-title{` |
| 2296 | `drive-mode` | `  body.drive-mode .route-pill{` |
| 2302 | `route-stop` | `  body.drive-mode .route-stop{` |
| 2308 | `route-stop` | `  body.drive-mode .route-stop .name{` |
| 2312 | `route-stop` | `  body.drive-mode .route-stop .meta,` |
| 2313 | `route-stop` | `  body.drive-mode .route-stop .extra-line{` |
| 2317 | `drive-mode` | `  body.drive-mode .board-stage{` |
| 2321 | `drive-mode` | `  body.drive-mode .label{` |
| 2330 | `driveModeToggle` | `  body.drive-mode #driveModeToggle{` |
| 2337 | `selected-stop` | `  body.drive-mode .selected-stop-chip{` |
| 2342 | `voice` | `  body.drive-mode .voice-command-btn{` |
| 2348 | `route-stop` | `  body.drive-mode .route-stop{` |
| 2352 | `drive-mode` | `  body.drive-mode .board-stage{` |
| 2359 | `Sürüş` | `   BAGAJ BALONU + SÜRÜŞ MODU KOLTUK SIKIŞTIRMA` |
| 2394 | `Bagaj` | `/* Bagaj yön ikonları fazla büyüyüp numarayı kapatmasın */` |
| 2410 | `Boş` | `/* Bagaj rozetinin çıkacağı yer için üst boşluk */` |
| 2415 | `Sürüş` | `/* Sürüş modunda çiftli koltuklar biraz yaklaşsın */` |
| 2416 | `drive-mode` | `body.drive-mode{` |
| 2421 | `Sürüş` | `/* Sürüş modunda bagaj balonu daha kontrollü */` |
| 2422 | `drive-mode` | `body.drive-mode .seat .bag-badge{` |

### `android_app/app/src/main/python/static/seats/voice-tts.js`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 2 | `voice` | `   SEATS UNIFIED VOICE MODULE` |
| 8 | `voice` | `  if(window.__SeatsVoiceUnifiedReady) return;` |
| 9 | `voice` | `  window.__SeatsVoiceUnifiedReady = true;` |
| 70 | `voice` | `      const voices = speechSynthesis.getVoices ? speechSynthesis.getVoices() : [];` |
| 71 | `voice` | `      const trVoice = voices.find(v =>` |
| 76 | `voice` | `      if(trVoice) u.voice = trVoice;` |
| 87 | `voice` | `    const nightBtn = document.getElementById("nightVoiceToggle");` |
| 90 | `voice` | `      nightBtn.dataset.voiceOn = on ? "1" : "0";` |
| 91 | `Durak Akışı` | `      nightBtn.title = on ? "Durak akışı sesi açık" : "Durak akışı sesi kapalı";` |
| 94 | `Sessiz` | `        : '<span class="nv-ico">🔇</span><span>Sessiz</span>';` |
| 112 | `voice` | `  window.SeatsStopVoice = stop;` |
| 114 | `voice` | `  // voice-commands.js daha önce window.SeatsVoice içine komut fonksiyonları koymuş olabilir.` |
| 116 | `voice` | `  window.SeatsVoice = Object.assign(window.SeatsVoice \|\| {}, {` |
| 125 | `Sessiz` | `  // Yeşil Ses Açık / Sessiz butonu` |
| 127 | `voice` | `    const btn = e.target.closest && e.target.closest("#nightVoiceToggle");` |
| 137 | `Durak Akışı` | `      speak("Durak akışı sesi açık.", { force:true });` |

### `android_app/app/src/main/python/static/seats/seats.js`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 124 | `Canlı` | `   Aynı rota/plaka ile yeni sefer açılınca eski canlı durak,` |
| 125 | `Durak Akışı` | `   geçildi bilgisi ve durak akışı özeti taşınmasın.` |
| 144 | `Durak Akışı` | `    // Hem trip_id değişince hem de hafıza şeması değişince eski durak akışı silinsin.` |
| 204 | `voice` | `  let lastApproachVoiceStop = "";` |
| 252 | `Normal` | `      .normalize("NFKD")` |
| 277 | `voice` | `  function persistVoiceState(){` |
| 282 | `voice` | `  function loadVoiceState(){` |
| 376 | `Canlı` | `  // Çok uzaktaysa canlı durak göstermesin` |
| 386 | `Canlı` | `  // İşlem olmayan durak canlı gösterilmez.` |
| 401 | `Canlı` | `  // Canlı durak sadece gerçekten yakındaki doğrulanmış durak olsun.` |
| 545 | `selectedStop` | `  function getSelectedStopName(){` |
| 681 | `Durak Akışı` | `      // Yeni sefer açılmış ve koltuk yoksa eski durak akışı özetini taşıma.` |
| 880 | `Bagaj` | `    if(bag > 0) parts.push('${bag} bagaj');` |
| 902 | `voice` | `function setVoiceBadge(text){` |
| 903 | `voice` | `    setText("#voiceStateBadge", text \|\| "Hazır");` |
| 932 | `selectedStop` | `    const stop = getSelectedStopName();` |
| 953 | `Bay` | `    if(gender === "bay") el.classList.add("male");` |
| 954 | `Bay` | `    if(gender === "bayan") el.classList.add("female");` |
| 967 | `Servis` | `      svc.title = note ? 'Servis: ${note}' : "Servis";` |
| 979 | `voice` | `    setText("#voiceSeatFilled", String(filled));` |
| 980 | `voice` | `    setText("#voiceSeatEmpty", String(empty));` |
| 981 | `voice` | `    setText("#driveVoiceFilled", String(filled));` |
| 982 | `voice` | `    setText("#driveVoiceEmpty", String(empty));` |
| 1038 | `voice` | `function focusRouteStripStop(stopName, { select=false, voice=false } = {}){` |
| 1048 | `selectedStop` | `    setSelectedStop(canonical, { silent:!voice, voiceReply:voice });` |
| 1058 | `route-stop` | `      const target = Array.from(wrap.querySelectorAll(".route-stop"))` |
| 1081 | `route-stop` | `      <div class="route-stop active">` |
| 1089 | `selectedStop` | `  const selected = getSelectedStopName();` |
| 1139 | `Canlı` | `    if(isLive) metaLine1 = "Canlı";` |
| 1163 | `route-stop` | `    item.className = 'route-stop ${isActive \|\| isLive ? "active" : ""} ${isDone ? "done has-flow-summary" : ""} ${liveDangerOn && isLive ? "live-danger" : ""} ${isNextWarn ? "next-warning" : ""} ${isFlowGreen ? "flow-green" : ""}';` |
| 1191 | `selectedStop` | `  setSelectedStop(stop, { silent:false, voiceReply:true });` |
| 1195 | `voice` | `    const msg = stopHumanVoiceSummary(stop);` |
| 1218 | `selectedStop` | `    const selected = getSelectedStopName();` |
| 1224 | `selectedStop` | `    setText("#selectedStopBadge", selected \|\| "—");` |
| 1274 | `selectedStop` | `  function setSelectedStop(name, { silent=false, voiceReply=true } = {}){` |
| 1303 | `voice` | `    if(!silent && voiceReply){` |
| 1304 | `voice` | `      const msg = stopHumanVoiceSummary(canonical);` |
| 1326 | `voice` | `    persistVoiceState();` |
| 1335 | `voice` | `    persistVoiceState();` |
| 1346 | `selectedStop` | `    const cur = getSelectedStopName();` |
| 1351 | `selectedStop` | `      setSelectedStop("", { silent:true, voiceReply:false });` |
| 1355 | `selectedStop` | `    setSelectedStop(next, { silent, voiceReply: !silent });` |
| 1362 | `selectedStop` | `    const stopName = getSelectedStopName();` |
| 1395 | `selectedStop` | `    setValue("#pickup", boardsMap[String(seatNo)] \|\| getSelectedStopName() \|\| "");` |
| 1430 | `selectedStop` | `    const from = $("#pickup")?.value \|\| getSelectedStopName() \|\| "";` |
| 1516 | `selectedStop` | `    const offStop = stopsMap[String(currentSeat)] \|\| getSelectedStopName() \|\| "";` |
| 1539 | `Boş` | `      toast("Koltuk boşaltıldı");` |
| 1541 | `İniş` | `      toast(e.message \|\| "İniş hatası");` |
| 1579 | `selectedStop` | `      const selected = getSelectedStopName() \|\| "";` |
| 1594 | `selectedStop` | `    const from = $("#bulkFrom")?.value \|\| speedState.liveStop \|\| getSelectedStopName() \|\| "";` |
| 1622 | `Boş` | `        toast("Boş koltuk yok");` |
| 1759 | `voice` | `      const msg = stopHumanVoiceSummary(stop);` |
| 1774 | `selectedStop` | `      const st = stopsMap[String(n)] \|\| getSelectedStopName() \|\| "";` |
| 1798 | `Boş` | `          if(!j.ok) throw new Error(j.msg \|\| ("Koltuk " + n + " boşaltılamadı"));` |
| 1819 | `Boş` | `      toast('${seatNums.length} koltuk boşaltıldı');` |
| 1821 | `Boş` | `      toast(e.message \|\| "Toplu boşaltma hatası");` |
| 1826 | `selectedStop` | `    const stop = getSelectedStopName();` |
| 1843 | `selectedStop` | `  async function offloadSelectedStop(){` |
| 1844 | `selectedStop` | `    const stop = getSelectedStopName();` |
| 1894 | `selectedStop` | `    const stopName = getSelectedStopName();` |
| 1940 | `selectedStop` | `      const stop = (getSelectedStopName() \|\| $("#coordStopName")?.value \|\| "").trim();` |
| 1994 | `selectedStop` | `    const selectedIdx = indexOfStopByName(getSelectedStopName());` |
| 2054 | `selectedStop` | `      const activeName = getSelectedStopName() \|\| liveName;` |
| 2080 | `Sıradaki` | `    // Asıl akıllı hesap: sıradaki saatli durağa kalan km + efektif hız.` |
| 2177 | `selectedStop` | `      row.addEventListener("click", () => setSelectedStop(item.stop, { silent:true, voiceReply:false }));` |
| 2183 | `selectedStop` | `    const stop = getSelectedStopName();` |
| 2212 | `Canlı` | `      : '${live} civarındasın. Sistem canlı durak ve rötarı izliyor.'` |
| 2215 | `Normal` | `    let aiSub = "Şu an sistem normal akışta.";` |
| 2232 | `Servis` | `    setText("#aiService", unserved > 0 ? '${unserved} yolcu servis bekliyor' : "Servis tarafı temiz");` |
| 2236 | `Canlı` | `  const LIVE_DETECT_KM = 5;        // Muavin hazırlık/canlı durak eşiği` |
| 2237 | `Canlı` | `  const LIVE_FORCE_KM = 1.2;       // Çok yakına girerse beklemeden canlı yap` |
| 2239 | `Canlı` | `  const LIVE_LOOKAHEAD_STOPS = 4;  // Mevcut canlı duraktan sonra kaç durağa bakılsın` |
| 2251 | `Canlı` | `    // Canlı durak GPS + rota sırasına göre belirlenecek.` |
| 2252 | `Seçili durak` | `    // Seçili durak veya eski canlı durak aday listesini kısıtlamaz.` |
| 2321 | `Canlı` | `          Canlı durak zaten belliyse:` |
| 2331 | `Canlı` | `          Geçilmiş durak tekrar canlı aday olmasın.` |
| 2332 | `Canlı` | `          Mevcut canlı durak buna istisna; çünkü markPassedStopsUntil()` |
| 2333 | `Canlı` | `          canlı durağı da passed listesine dahil ediyor.` |
| 2339 | `Canlı` | `        // İşlem yoksa canlı durak yapma.` |
| 2363 | `Canlı` | `        // Mevcut canlı durakta artık işlem yoksa canlıyı boşalt.` |
| 2382 | `Canlı` | `        - canlı durak varsa rota sırasına göre ilerle` |
| 2383 | `Canlı` | `        - canlı durak yoksa en yakındaki işlemli durağı yakala` |
| 2431 | `Canlı` | `        Aynı aday 2 kez görülürse canlı yap.` |
| 2432 | `Canlı` | `        Çok yakına girdiyse beklemeden canlı yap.` |
| 2483 | `voice` | `      if(window.SeatsVoice && typeof window.SeatsVoice.syncButtons === "function"){` |
| 2484 | `voice` | `        window.SeatsVoice.syncButtons();` |
| 2493 | `voice` | `      if(window.SeatsVoice && typeof window.SeatsVoice.setEnabled === "function"){` |
| 2494 | `voice` | `        window.SeatsVoice.setEnabled(next);` |
| 2509 | `voice` | `        if(window.SeatsStopVoice){` |
| 2510 | `voice` | `          window.SeatsStopVoice();` |
| 2515 | `voice` | `    let trVoice = null;` |
| 2516 | `voice` | `    function loadVoices(){` |
| 2517 | `voice` | `      const voices = speechSynthesis.getVoices();` |
| 2518 | `voice` | `      trVoice = voices.find(v => (v.lang \|\| "").toLowerCase().startsWith("tr")) \|\| null;` |
| 2522 | `voice` | `      loadVoices();` |
| 2523 | `voice` | `      speechSynthesis.onvoiceschanged = loadVoices;` |
| 2547 | `voice` | `        const voices = speechSynthesis.getVoices ? speechSynthesis.getVoices() : [];` |
| 2548 | `voice` | `        const trVoice = voices.find(v =>` |
| 2553 | `voice` | `        if(trVoice) u.voice = trVoice;` |
| 2574 | `Servis` | `        service:"servis"` |
| 2765 | `selectedStop` | `  onClick("#btnOffloadNow", offloadSelectedStop);` |
| 2766 | `selectedStop` | `  onClick("#btnOffloadNowPane", offloadSelectedStop);` |
| 2803 | `selectedStop` | `    const a = getSelectedStopName() \|\| "";` |
| 2824 | `Canlı` | `        toast("Canlı durak henüz yok");` |
| 2827 | `voice` | `      focusRouteStripStop(live, { select:true, voice:true });` |
| 2835 | `selectedStop` | `      const selected = getSelectedStopName();` |
| 2838 | `Sıradaki` | `        toast("Sıradaki durak bulunamadı");` |
| 2841 | `voice` | `      focusRouteStripStop(next, { select:true, voice:true });` |
| 2846 | `btnDeckAI` | `  onClick("#btnDeckAI", startDeckAIVoice);` |
| 2851 | `voice` | `      loadVoiceState();` |
| 2853 | `voice` | `      setVoiceBadge("Hazır");` |
| 2880 | `selectedStop` | `      if(next) setSelectedStop(next, { silent:true, voiceReply:false });` |
| 2881 | `selectedStop` | `      else if(serverStops?.length) setSelectedStop(serverStops[0], { silent:true, voiceReply:false });` |
| 2895 | `Canlı` | `   Seats ekranındaki canlı veriyi backend'e yazar` |
| 2902 | `Canlı` | `    // Backend'e sadece gerçekten set edilmiş canlı durağı yaz.` |
| 2908 | `Canlı` | `    // Uzakta kalmış eski canlı durak backend'e yazılmasın.` |

### `android_app/app/src/main/python/static/seats/drive-eta-chip.js`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 3 | `Sürüş` | `   Paneldeki Rötar / ETA bilgisini üst sürüş kutusuna taşır.` |
| 27 | `driveEtaChip` | `  function syncDriveEtaChip(){` |
| 28 | `driveEtaChip` | `    const chip = q("#driveEtaChip");` |
| 29 | `driveEtaMain` | `    const main = q("#driveEtaMain");` |
| 30 | `driveEtaSub` | `    const sub = q("#driveEtaSub");` |
| 52 | `driveEtaChip` | `  window.syncDriveEtaChip = syncDriveEtaChip;` |
| 55 | `driveEtaChip` | `    syncDriveEtaChip();` |
| 56 | `driveEtaChip` | `    setInterval(syncDriveEtaChip, 1500);` |

### `android_app/app/src/main/python/static/seats/bags.js`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 3 | `Bagaj` | `   Bagaj rozetleri + bagaj ses özeti + bagaj temizleme` |
| 6 | `Bagaj` | `// Bagaj göz bilgisi sesli uyarıda kullanılacak.` |
| 30 | `voice` | `function formatSeatListForVoice(seats){` |
| 40 | `voice` | `function bagEyeVoicePartsForSeat(seatNo){` |
| 50 | `Bagaj` | `    if(count === 1) parts.push('${label} gözde bagaj');` |
| 51 | `Bagaj` | `    else parts.push('${label} gözde ${count} bagaj');` |
| 59 | `Bagaj` | `    if(meta.eyes.includes("R")) parts.push("sağ gözde bagaj");` |
| 60 | `Bagaj` | `    if(meta.eyes.includes("LF")) parts.push("sol ön gözde bagaj");` |
| 61 | `Bagaj` | `    if(meta.eyes.includes("LB")) parts.push("sol arka gözde bagaj");` |
| 67 | `voice` | `function bagVoiceSummaryForStop(stopName){` |
| 72 | `voice` | `    const parts = bagEyeVoicePartsForSeat(seatNo);` |
| 78 | `Bagaj` | `    return '${seatNo} numarada bagaj';` |
| 81 | `Bagaj` | `  return 'Bagaj uyarısı: ${chunks.join(". ")} var.';` |
| 145 | `Bagaj` | `  if(badge) badge.title = cnt ? 'Bagaj: ${cnt} adet' : "Bagaj yok";` |
| 179 | `voice` | `  formatSeatListForVoice,` |
| 180 | `voice` | `  bagEyeVoicePartsForSeat,` |
| 181 | `voice` | `  bagVoiceSummaryForStop,` |

### `android_app/app/src/main/python/static/seats/drive-controls.js`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 3 | `Sürüş` | `   HIZLI KOLTUK → OTOMATİK SÜRÜŞ MODU` |
| 4 | `Sürüş` | `   /seats?drive=1 ile gelirse sürüş modunu açar` |
| 18 | `drive-mode` | `    document.body.classList.add("drive-mode");` |
| 33 | `Sürüş` | `    console.warn("Hızlı koltuk sürüş modu açılamadı:", e);` |
| 39 | `Sessiz` | `   Sürüş modu + hız kutusu + ses açık/sessiz` |
| 96 | `driveModeToggle` | `    const btn = document.getElementById("driveModeToggle");` |
| 99 | `drive-mode` | `    document.body.classList.toggle("drive-mode", on);` |
| 100 | `drive-mode` | `    document.documentElement.classList.toggle("drive-mode", on);` |
| 103 | `Normal` | `      btn.innerHTML = on ? "↩ Normal" : "🚘 Sürüş";` |
| 104 | `Normal` | `      btn.title = on ? "Normal moda geç" : "Sürüş moduna geç";` |
| 111 | `driveEtaChip` | `      if(typeof syncDriveEtaChip === "function") syncDriveEtaChip();` |
| 122 | `driveModeToggle` | `    const btn = document.getElementById("driveModeToggle");` |
| 147 | `driveSpeedChip` | `  function updateDriveSpeedChip(){` |
| 148 | `driveSpeedChip` | `    const el = document.getElementById("driveSpeedChip");` |
| 176 | `voice` | `  function getVoiceEnabled(){` |
| 178 | `voice` | `      if(window.SeatsVoice && typeof window.SeatsVoice.isEnabled === "function"){` |
| 179 | `voice` | `        return window.SeatsVoice.isEnabled();` |
| 192 | `voice` | `  function updateNightVoiceToggle(){` |
| 194 | `voice` | `      if(window.SeatsVoice && typeof window.SeatsVoice.syncButtons === "function"){` |
| 195 | `voice` | `        window.SeatsVoice.syncButtons();` |
| 200 | `voice` | `    const btn = document.getElementById("nightVoiceToggle");` |
| 203 | `voice` | `    const on = getVoiceEnabled();` |
| 208 | `Sessiz` | `      : '<span class="nv-ico">🔇</span><span>Sessiz</span>';` |
| 214 | `voice` | `    function setVoiceEnabled(on, opts={}){` |
| 218 | `voice` | `        if(window.SeatsVoice && typeof window.SeatsVoice.setEnabled === "function"){` |
| 219 | `voice` | `          window.SeatsVoice.setEnabled(enabled);` |
| 232 | `voice` | `      updateNightVoiceToggle();` |
| 244 | `voice` | `  function bindNightVoiceToggle(){` |
| 248 | `voice` | `      cb.checked = getVoiceEnabled();` |
| 250 | `voice` | `      if(cb.dataset.voiceBound !== "1"){` |
| 251 | `voice` | `        cb.dataset.voiceBound = "1";` |
| 253 | `voice` | `          setVoiceEnabled(cb.checked, { silent:true });` |
| 259 | `voice` | `      #nightVoiceToggle butonunun tek sahibi voice-tts.js.` |
| 262 | `voice` | `    updateNightVoiceToggle();` |
| 267 | `voice` | `    bindNightVoiceToggle();` |
| 268 | `driveSpeedChip` | `    updateDriveSpeedChip();` |
| 279 | `driveSpeedChip` | `  setInterval(updateDriveSpeedChip, 1000);` |
| 283 | `driveSpeedChip` | `    updateSpeed: updateDriveSpeedChip,` |
| 284 | `voice` | `    setVoiceEnabled` |

### `android_app/app/src/main/python/static/seats/voice-commands.js`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 2 | `voice` | `   VOICE COMMANDS MODULE` |
| 3 | `Sesli Komut` | `   Sesli komut + konuşma + insancıl durak özeti` |
| 6 | `voice` | `const VOICE_HELP = [` |
| 12 | `Sıradaki` | `  "sıradaki durak [durak adı]",` |
| 16 | `Bay` | `  "5 numara bayan [durak]",` |
| 25 | `Bagaj` | `  "bu durakta bagaj var mı",` |
| 32 | `voice` | `/* VOICE_SUMMARY_PATCH_START */` |
| 33 | `voice` | `function buildTripVoiceSummary(){` |
| 61 | `selectedStop` | `    if(typeof getSelectedStopName === "function"){` |
| 62 | `selectedStop` | `      selected = getSelectedStopName() \|\| "";` |
| 75 | `Seçili durak` | `    parts.push('Seçili durak ${selected}.');` |
| 101 | `voice` | `      bagMsg = String(bagVoiceSummaryForStop(selected) \|\| "").trim();` |
| 146 | `Sıradaki` | `    parts.push('Sıradaki işlem ${next}.');` |
| 151 | `voice` | `/* VOICE_SUMMARY_PATCH_END */` |
| 153 | `voice` | `function stopHumanVoiceSummary(stopName){` |
| 179 | `Bay` | `  let bay = 0;` |
| 180 | `Bay` | `  let bayan = 0;` |
| 185 | `Bay` | `    if(g === "bay") bay++;` |
| 186 | `Bay` | `    else if(g === "bayan") bayan++;` |
| 190 | `Normal` | `  // Ayakta yolcuyu "ayakta" diye söyleme; normal yolcu gibi ekle.` |
| 194 | `Bay` | `  if(bay > 0) parts.push('${bay} bay');` |
| 195 | `Bay` | `  if(bayan > 0) parts.push('${bayan} bayan');` |
| 211 | `voice` | `    const bagMsg = bagVoiceSummaryForStop(stop);` |
| 220 | `voice` | `/* --- voice stop ops helpers start --- */` |
| 221 | `voice` | `function stopOperationVoiceSummary(stopName){` |
| 256 | `voice` | `    bagMsg = bagVoiceSummaryForStop(stop) \|\| "";` |
| 273 | `voice` | `    msg += stopHumanVoiceSummary(stop);` |
| 279 | `Servis` | `    msg += ' Ayrıca ${serviceCt} servisli koltuk var.';` |
| 285 | `voice` | `function stopBagVoiceOnly(stopName){` |
| 290 | `voice` | `    const bagMsg = String(bagVoiceSummaryForStop(stop) \|\| "").trim();` |
| 294 | `Bagaj` | `  return '${stop} durağı için bagaj görünmüyor.';` |
| 297 | `selectedStop` | `async function offloadSelectedStopByVoice(){` |
| 298 | `selectedStop` | `  const stop = getSelectedStopName() \|\| speedState.liveStop \|\| "";` |
| 344 | `voice` | `/* --- voice stop ops helpers end --- */` |
| 352 | `voice` | `  if(lastApproachVoiceStop === key) return;` |
| 354 | `voice` | `  lastApproachVoiceStop = key;` |
| 355 | `voice` | `  speak('${stopName} durağına yaklaşılıyor. ${stopHumanVoiceSummary(stopName)}');` |
| 370 | `voice` | `      window.SeatsVoice &&` |
| 371 | `voice` | `      typeof window.SeatsVoice.speak === "function" &&` |
| 372 | `voice` | `      window.SeatsVoice.speak !== speak` |
| 374 | `voice` | `      window.SeatsVoice.speak(msg);` |
| 379 | `voice` | `      const voices = speechSynthesis.getVoices ? speechSynthesis.getVoices() : [];` |
| 380 | `voice` | `      const trVoice = voices.find(v => (v.lang \|\| "").toLowerCase().startsWith("tr"));` |
| 382 | `voice` | `      if(trVoice) u.voice = trVoice;` |
| 383 | `voice` | `      u.lang = trVoice ? trVoice.lang : "tr-TR";` |
| 400 | `voice` | `  speak(stopHumanVoiceSummary(name));` |
| 438 | `Bay` | `  if(/\b(erkek\|bay\|adam)\b/.test(t)) return "bay";` |
| 439 | `Bay` | `  if(/\b(kadin\|kadın\|bayan\|kiz\|kız)\b/.test(t)) return "bayan";` |
| 440 | `Boş` | `  if(/\b(bos yap\|boş yap\|cinsiyeti kaldir\|cinsiyeti kaldır\|temizle\|sil\|sifirla\|sıfırla)\b/.test(t)) return "";` |
| 485 | `Bay` | `    gender === "bay" ? "bay" :` |
| 486 | `Boş` | `    gender === "bayan" ? "bayan" : "boş";` |
| 490 | `Boş` | `    msg += '. Boş olduğu için atlanan: ${emptySeats.join(", ")}';` |
| 498 | `voice` | `function parseVoiceCommand(text){` |
| 506 | `Canlı` | `  if(/^(harita ac\|harita aç\|haritayi ac\|haritayı aç\|canli harita ac\|canlı harita aç\|yol haritasi ac\|yol haritası aç)$/.test(t)) return { type:"open_map" };` |
| 513 | `Sıradaki` | `  if(/(bir sonraki durak\|siradaki saatli\|sıradaki saatli)/.test(t)) return { type:"ask_next_timed" };` |
| 531 | `Sıradaki` | `  if((/(siradaki durak\|sıradaki durak\|durak sec\|durak seç)/.test(t)) && mentionedStop){` |
| 540 | `Seçili durak` | `  if(/(bu durakta islem var mi\|bu durakta işlem var mı\|secili durakta islem var mi\|seçili durakta işlem var mı\|bu durakta ne var)/.test(t)){` |
| 544 | `Seçili durak` | `  if(/(bu durakta kimler inecek\|secili durakta kim inecek\|seçili durakta kim inecek\|inecekleri soyle\|inecekleri söyle)/.test(t)){` |
| 548 | `Bagaj` | `  if(mentionedStop && /(bagaj var mi\|bagaj var mı)/.test(t)){` |
| 552 | `Seçili durak` | `  if(/(bu durakta bagaj var mi\|bu durakta bagaj var mı\|secili durakta bagaj var mi\|seçili durakta bagaj var mı\|bagajli var mi\|bagajlı var mı)/.test(t)){` |
| 556 | `Seçili durak` | `  if(/(inecekleri indir\|bu durakta indir\|secili duraktakileri indir\|seçili duraktakileri indir)/.test(t)){` |
| 567 | `Boş` | `    seat_remove_single: "Tek koltuk boşaltma",` |
| 568 | `Boş` | `    seat_remove_group: "Çoklu koltuk boşaltma",` |
| 570 | `Servis` | `    service_mark: "Servis işaretleme",` |
| 577 | `voice` | `async function resolveVoiceWithBackendAI(text){` |
| 598 | `voice` | `/* VOICE_DIRECT_BOARD_GENERAL_START */` |
| 599 | `voice` | `function voiceCleanStopValue(v){` |
| 607 | `voice` | `function voiceCurrentBoardingStop(){` |
| 611 | `Seçili durak` | `    Öncelik seçili durakta olmalı.` |
| 618 | `voice` | `      stop = voiceCleanStopValue(alertStop.value);` |
| 623 | `selectedStop` | `    if(!stop && typeof getSelectedStopName === "function"){` |
| 624 | `selectedStop` | `      stop = voiceCleanStopValue(getSelectedStopName());` |
| 630 | `selectedStop` | `      const badge = document.querySelector("#selectedStopBadge");` |
| 631 | `voice` | `      if(badge) stop = voiceCleanStopValue(badge.textContent);` |
| 638 | `voice` | `      if(simpleStop) stop = voiceCleanStopValue(simpleStop.textContent);` |
| 643 | `Canlı` | `    Canlı durak en son fallback.` |
| 648 | `voice` | `      stop = voiceCleanStopValue(getDisplayLiveStop());` |
| 654 | `voice` | `      stop = voiceCleanStopValue(speedState.liveStop);` |
| 668 | `voice` | `async function voiceDirectBoardSeats(seats, toStop, genderValue=""){` |
| 679 | `voice` | `  let fromStop = voiceCurrentBoardingStop();` |
| 680 | `voice` | `  toStop = voiceCleanStopValue(toStop);` |
| 685 | `Bay` | `    genderValue = "bay";` |
| 687 | `Bay` | `    genderValue = "bayan";` |
| 690 | `Bay` | `  if(genderValue !== "bay" && genderValue !== "bayan"){` |
| 707 | `Seçili durak` | `    toast("Canlı durak veya seçili durak yok");` |
| 708 | `Seçili durak` | `    speak("Önce canlı durak ya da seçili durak belirlenmeli.");` |
| 713 | `İniş` | `    toast("İniş durağı bulunamadı");` |
| 714 | `İniş` | `    speak("İniş durağı bulunamadı.");` |
| 801 | `Bay` | `      genderValue === "bay" ? " Erkek." :` |
| 802 | `Bay` | `      genderValue === "bayan" ? " Bayan." : "";` |
| 804 | `İniş` | `    const msg = '${seatText} yolcu alındı. Biniş ${fromStop}. İniş ${toStop}.${genderText}';` |
| 815 | `voice` | `/* VOICE_DIRECT_BOARD_GENERAL_END */` |
| 821 | `selectedStop` | `  const selectedStop = getSelectedStopName() \|\| "";` |
| 822 | `selectedStop` | `  if(selectedStop && $("#pickup")) $("#pickup").value = selectedStop;` |
| 833 | `selectedStop` | `  const selectedStop = getSelectedStopName() \|\| "";` |
| 834 | `selectedStop` | `  if(selectedStop && $("#bulkTo")) $("#bulkTo").value = selectedStop;` |
| 857 | `selectedStop` | `  const selectedStop = getSelectedStopName() \|\| "";` |
| 858 | `selectedStop` | `  if(selectedStop && $("#cashTo")) $("#cashTo").value = selectedStop;` |
| 873 | `Servis` | `    toast("Servis için koltuk bulunamadı");` |
| 874 | `Servis` | `    speak("Servis için koltuk bulunamadı.");` |
| 878 | `Sesli Komut` | `  const note = "Sesli komut";` |
| 893 | `Servis` | `  if(!j.ok) throw new Error(j.msg \|\| "Servis işaretleme başarısız");` |
| 906 | `Servis` | `  toast('Servis işlendi: ${seats.join(", ")}');` |
| 907 | `Servis` | `  speak('Servis işlendi. Koltuklar ${seats.join(", ")}');` |
| 928 | `Boş` | `      toast("Boşaltılacak koltuk bulunamadı");` |
| 929 | `Boş` | `      speak("Boşaltılacak koltuk bulunamadı.");` |
| 934 | `Boş` | `    speak('${seats.join(" ve ")} numaralı koltuk boşaltıldı.');` |
| 977 | `voice` | `async function handleLocalVoiceCommand(text){` |
| 978 | `voice` | `  const cmd = parseVoiceCommand(text);` |
| 981 | `voice` | `    const help = "Temel komutlar: " + VOICE_HELP.join(", ");` |
| 988 | `voice` | `    const msg = buildTripVoiceSummary();` |
| 1007 | `Canlı` | `    speak("Canlı harita tam ekran açılıyor.");` |
| 1018 | `voice` | `    await voiceDirectBoardSeats(cmd.seats, cmd.stop, cmd.gender);` |
| 1067 | `selectedStop` | `    const stop = getSelectedStopName() \|\| speedState.liveStop \|\| "";` |
| 1068 | `voice` | `    const msg = stopOperationVoiceSummary(stop);` |
| 1076 | `selectedStop` | `    const stop = getSelectedStopName() \|\| speedState.liveStop \|\| "";` |
| 1077 | `voice` | `    const msg = stopHumanVoiceSummary(stop);` |
| 1085 | `selectedStop` | `    const stop = cmd.stop \|\| getSelectedStopName() \|\| speedState.liveStop \|\| "";` |
| 1086 | `voice` | `    const msg = stopBagVoiceOnly(stop);` |
| 1094 | `selectedStop` | `    return await offloadSelectedStopByVoice();` |
| 1099 | `voice` | `    const msg = stopHumanVoiceSummary(stop);` |
| 1107 | `selectedStop` | `    const live = speedState.liveStop \|\| getSelectedStopName() \|\| "henüz belli değil";` |
| 1132 | `Sıradaki` | `      const msg = "Sıradaki saatli durak bulunamadı.";` |
| 1138 | `Sıradaki` | `    const msg = 'Sıradaki saatli nokta ${nextTimed.stop}. Plan ${nextTimed.plan}, tahmini ${fmtHour(nextTimed.etaDate)}.';` |
| 1145 | `selectedStop` | `    const ok = setSelectedStop(cmd.stop, { silent:true, voiceReply:false });` |
| 1152 | `selectedStop` | `    const stop = getSelectedStopName();` |
| 1153 | `voice` | `    const msg = stopHumanVoiceSummary(stop);` |
| 1162 | `voice` | `async function handleBasicVoiceCommand(text){` |
| 1163 | `voice` | `  const localHandled = await handleLocalVoiceCommand(text);` |
| 1167 | `voice` | `    const resolved = await resolveVoiceWithBackendAI(text);` |
| 1173 | `voice` | `      const cmd = parseVoiceCommand(text);` |
| 1177 | `voice` | `        const msg = stopHumanVoiceSummary(stop);` |
| 1206 | `voice` | `    console.error("AI voice resolve error:", e);` |
| 1207 | `Sesli Komut` | `    toast("AI sesli komut hatası");` |
| 1208 | `Sesli Komut` | `    speak("AI sesli komut tarafında bir hata oluştu.");` |
| 1212 | `voice` | `function getVoiceCommandButtons(){` |
| 1214 | `btnDeckAI` | `  const mainBtn = $("#btnDeckAI");` |
| 1215 | `btnDeckAI` | `  const driveBtn = document.getElementById("btnDeckAIDrive");` |
| 1216 | `voice` | `  const bottomBtn = document.getElementById("seatSimpleVoiceBtn");` |
| 1225 | `voice` | `function setVoiceCommandButtonsListening(buttons, on){` |
| 1229 | `voice` | `    if(btn.id === "seatSimpleVoiceBtn"){` |
| 1231 | `voice` | `        ? '<span class="ico">🔴</span><span class="voice-bottom-text">Dinliyor</span>'` |
| 1232 | `voice` | `        : '<span class="ico">🎙️</span><span class="voice-bottom-text">Sesli<br>Komut</span>';` |
| 1233 | `Sesli Komut` | `      btn.setAttribute("title", on ? "Dinliyor" : "Sesli Komut");` |
| 1234 | `Sesli Komut` | `      btn.setAttribute("aria-label", on ? "Dinliyor" : "Sesli Komut");` |
| 1240 | `Sesli Komut` | `      : '🎤 <span>Sesli Komut</span>';` |
| 1244 | `voice` | `function startDeckAIVoice(){` |
| 1247 | `voice` | `    try{ setVoiceBadge("Dinleniyor"); }catch(_){}` |
| 1253 | `voice` | `  const buttons = getVoiceCommandButtons();` |
| 1258 | `Sesli Komut` | `    toast("Bu tarayıcı sesli komutu desteklemiyor");` |
| 1259 | `voice` | `    setVoiceBadge("Destek yok");` |
| 1269 | `voice` | `  setVoiceCommandButtonsListening(buttons, true);` |
| 1271 | `voice` | `  setVoiceBadge("Dinleniyor");` |
| 1278 | `voice` | `      setVoiceBadge("Tekrar dene");` |
| 1283 | `voice` | `    setVoiceBadge(text.length > 18 ? text.slice(0, 18) + "…" : text);` |
| 1284 | `voice` | `    await handleBasicVoiceCommand(text);` |
| 1289 | `Sesli Komut` | `    toast("Sesli komut hatası: " + (e.error \|\| "bilinmiyor"));` |
| 1290 | `voice` | `    setVoiceBadge("Hata");` |
| 1295 | `voice` | `    setVoiceCommandButtonsListening(buttons, false);` |
| 1297 | `voice` | `    setTimeout(() => setVoiceBadge("Hazır"), 900);` |
| 1304 | `voice` | `    setVoiceCommandButtonsListening(buttons, false);` |
| 1306 | `voice` | `    setVoiceBadge("Başlatılamadı");` |
| 1311 | `voice` | `window.SeatsVoice = {` |
| 1312 | `voice` | `  stopHumanVoiceSummary,` |
| 1316 | `voice` | `  parseVoiceCommand,` |
| 1317 | `voice` | `  handleBasicVoiceCommand,` |
| 1318 | `voice` | `  startDeckAIVoice` |

### `android_app/app/src/main/python/static/seats/standing.js`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 8 | `selectedStop` | `    const selected = getSelectedStopName() \|\| "";` |
| 27 | `selectedStop` | `  const from = $("#cashFrom")?.value \|\| speedState.liveStop \|\| getSelectedStopName() \|\| serverStops?.[0] \|\| "";` |

### `android_app/app/src/main/python/static/seats/seats-final.css`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 109 | `mini-chip` | `.route-live-row .mini-chip{` |
| 125 | `mini-chip` | `.route-live-row .mini-chip span{` |
| 129 | `mini-chip` | `.route-live-row .mini-chip b{` |
| 246 | `Sürüş` | `   SÜRÜŞ / HIZ / RÖTAR SATIRI` |
| 250 | `drive-mode` | `body.drive-mode #driveInlineDock,` |
| 251 | `drive-mode` | `body:not(.drive-mode) #driveInlineDock{` |
| 276 | `driveModeToggle` | `#driveModeToggle,` |
| 277 | `driveSpeedChip` | `#driveSpeedChip,` |
| 278 | `driveEtaChip` | `#driveEtaChip,` |
| 302 | `driveModeToggle` | `#driveModeToggle{` |
| 313 | `driveSpeedChip` | `#driveSpeedChip,` |
| 314 | `driveEtaChip` | `#driveEtaChip{` |
| 359 | `board-head` | `.board-head{` |
| 367 | `board-title` | `.board-title{` |
| 386 | `board-title` | `.board-title h2{` |
| 395 | `board-title` | `.board-title small{` |
| 399 | `selected-stop` | `.selected-stop-chip{` |
| 412 | `board-head` | `.board-head-right{` |
| 417 | `voice` | `.voice-row{` |
| 424 | `voice` | `.voice-command-btn,` |
| 425 | `voice` | `.voice-state{` |
| 433 | `voice` | `.voice-command-btn{` |
| 447 | `voice` | `.voice-command-btn::before,` |
| 448 | `voice` | `.voice-command-btn::after{` |
| 452 | `voice` | `.voice-command-btn span{` |
| 459 | `voice` | `.voice-state{` |
| 469 | `legend` | `.legend{` |
| 476 | `legend` | `.legend .mini-chip,` |
| 477 | `mini-chip` | `.mini-chip{` |
| 497 | `route-strip` | `.route-strip-shell{` |
| 506 | `route-strip` | `.route-strip-head{` |
| 512 | `route-strip` | `.route-strip-title{` |
| 518 | `route-strip` | `.route-strip-meta{` |
| 551 | `voice` | `#nightVoiceToggle{` |
| 562 | `voice` | `#nightVoiceToggle::first-letter{` |
| 566 | `route-strip` | `.route-strip{` |
| 574 | `route-strip` | `.route-strip::-webkit-scrollbar{` |
| 578 | `route-stop` | `.route-stop{` |
| 585 | `route-stop` | `.route-stop .name{` |
| 589 | `route-stop` | `.route-stop .meta{` |
| 597 | `board-stage` | `.board-stage{` |
| 784 | `drive-mode` | `  body.drive-mode #driveInlineDock,` |
| 785 | `drive-mode` | `  body:not(.drive-mode) #driveInlineDock{` |
| 790 | `driveModeToggle` | `  #driveModeToggle{` |
| 794 | `board-title` | `  .board-title h2{` |
| 798 | `route-strip` | `  .route-strip-meta{` |
| 802 | `voice` | `  #nightVoiceToggle{` |
| 807 | `board-stage` | `  .board-stage{` |
| 829 | `voice` | `  .voice-row{` |
| 833 | `voice` | `  .voice-command-btn span{` |
| 837 | `legend` | `  .legend{` |
| 841 | `mini-chip` | `  .mini-chip{` |
| 881 | `mini-chip` | `.route-live-row .mini-chip{` |
| 901 | `Sürüş` | `/* Sürüş + rötar satırı daha düzgün dursun */` |
| 903 | `drive-mode` | `body.drive-mode #driveInlineDock,` |
| 904 | `drive-mode` | `body:not(.drive-mode) #driveInlineDock{` |
| 910 | `driveSpeedChip` | `#driveInlineDock #driveSpeedChip{` |
| 914 | `driveModeToggle` | `#driveModeToggle{` |
| 921 | `driveEtaChip` | `#driveEtaChip,` |
| 934 | `board-title` | `.board-title h2{` |
| 938 | `selected-stop` | `.selected-stop-chip{` |
| 945 | `drive-mode` | `  body.drive-mode #driveInlineDock,` |
| 946 | `drive-mode` | `  body:not(.drive-mode) #driveInlineDock{` |
| 954 | `mini-chip` | `  .route-live-row .mini-chip{` |
| 964 | `Sürüş` | `   Sürüş modunda Durak Akışı kartlarında durak başına konum işareti` |
| 967 | `route-stop` | `body.drive-mode .route-stop .name{` |
| 973 | `route-stop` | `body.drive-mode .route-stop .name::before{` |
| 987 | `route-stop` | `body.drive-mode .route-stop.active .name::before,` |
| 988 | `route-stop` | `body.drive-mode .route-stop.live-danger .name::before,` |
| 989 | `route-stop` | `body.drive-mode .route-stop.next-warning .name::before,` |
| 990 | `route-stop` | `body.drive-mode .route-stop.flow-green .name::before{` |
| 994 | `route-stop` | `body.drive-mode .route-stop.done .name::before{` |
| 1004 | `route-stop` | `body.drive-mode .route-stop .name{` |
| 1010 | `route-stop` | `body.drive-mode .route-stop .name::before{` |
| 1030 | `route-stop` | `body.drive-mode .route-stop.active .name::before,` |
| 1031 | `route-stop` | `body.drive-mode .route-stop.live-danger .name::before,` |
| 1032 | `route-stop` | `body.drive-mode .route-stop.next-warning .name::before,` |
| 1033 | `route-stop` | `body.drive-mode .route-stop.flow-green .name::before{` |
| 1040 | `route-stop` | `body.drive-mode .route-stop.done .name::before{` |
| 1050 | `route-stop` | `body.drive-mode .route-stop .name::before{` |
| 1058 | `route-stop` | `body.drive-mode .route-stop.done .name::before{` |
| 1063 | `route-stop` | `body.drive-mode .route-stop.active .name::before,` |
| 1064 | `route-stop` | `body.drive-mode .route-stop.live-danger .name::before,` |
| 1065 | `route-stop` | `body.drive-mode .route-stop.next-warning .name::before,` |
| 1066 | `route-stop` | `body.drive-mode .route-stop.flow-green .name::before{` |
| 1076 | `Sürüş` | `   Sürüş modunda Durak Akışı kartlarını daha canlı yapar.` |
| 1079 | `route-stop` | `body.drive-mode .route-stop{` |
| 1090 | `route-stop` | `body.drive-mode .route-stop.done{` |
| 1098 | `route-stop` | `body.drive-mode .route-stop.done .name{` |
| 1103 | `route-stop` | `body.drive-mode .route-stop.done .meta,` |
| 1104 | `route-stop` | `body.drive-mode .route-stop.done .extra-k,` |
| 1105 | `route-stop` | `body.drive-mode .route-stop.done .extra-v{` |
| 1109 | `Canlı` | `/* Seçili / canlı kart daha güçlü dursun */` |
| 1110 | `route-stop` | `body.drive-mode .route-stop.active{` |
| 1122 | `route-stop` | `body.drive-mode .route-stop.active .name,` |
| 1123 | `route-stop` | `body.drive-mode .route-stop.active .meta,` |
| 1124 | `route-stop` | `body.drive-mode .route-stop.active .extra-k,` |
| 1125 | `route-stop` | `body.drive-mode .route-stop.active .extra-v{` |
| 1129 | `Normal` | `/* Normal bekleyen kartlar da çok sönük kalmasın */` |
| 1130 | `route-stop` | `body.drive-mode .route-stop:not(.active):not(.live-danger):not(.next-warning):not(.flow-green){` |
| 1137 | `Canlı` | `   Canlı durak eşik km altına düşünce kırmızı uyarı geri gelsin.` |
| 1140 | `route-stop` | `body.drive-mode .route-stop.live-danger{` |
| 1155 | `route-stop` | `body.drive-mode .route-stop.live-danger .name,` |
| 1156 | `route-stop` | `body.drive-mode .route-stop.live-danger .meta,` |
| 1157 | `route-stop` | `body.drive-mode .route-stop.live-danger .extra-k,` |
| 1158 | `route-stop` | `body.drive-mode .route-stop.live-danger .extra-v{` |
| 1163 | `route-stop` | `body.drive-mode .route-stop.live-danger .name::before{` |
| 1170 | `Sıradaki` | `/* Sıradaki uyarı sarı kalsın */` |
| 1171 | `route-stop` | `body.drive-mode .route-stop.next-warning:not(.live-danger){` |
| 1183 | `route-stop` | `body.drive-mode .route-stop.flow-green:not(.live-danger):not(.next-warning){` |
| 1196 | `Normal` | `   NORMAL ROUTE STOP PIN ICON` |
| 1197 | `Normal` | `   Normal modda Durak Akışı kartlarının başına mavi konum ikonu ekler.` |
| 1200 | `route-stop` | `body:not(.drive-mode) .route-stop .name{` |
| 1206 | `route-stop` | `body:not(.drive-mode) .route-stop .name::before{` |
| 1228 | `route-stop` | `body:not(.drive-mode) .route-stop.done .name::before{` |
| 1232 | `route-stop` | `body:not(.drive-mode) .route-stop.active .name::before,` |
| 1233 | `route-stop` | `body:not(.drive-mode) .route-stop.live-danger .name::before,` |
| 1234 | `route-stop` | `body:not(.drive-mode) .route-stop.next-warning .name::before,` |
| 1235 | `route-stop` | `body:not(.drive-mode) .route-stop.flow-green .name::before{` |
| 1244 | `Normal` | `   NORMAL ROUTE PIN BRIGHT FINAL` |
| 1245 | `Normal` | `   Normal mod Durak Akışı konum ikonlarını daha canlı/parlak yapar.` |
| 1248 | `route-stop` | `body:not(.drive-mode) .route-stop .name::before{` |
| 1268 | `route-stop` | `body:not(.drive-mode) .route-stop.done .name::before{` |
| 1285 | `Canlı` | `/* Seçili / canlı / uyarı kartında ikon daha güçlü parlasın */` |
| 1286 | `route-stop` | `body:not(.drive-mode) .route-stop.active .name::before,` |
| 1287 | `route-stop` | `body:not(.drive-mode) .route-stop.live-danger .name::before,` |
| 1288 | `route-stop` | `body:not(.drive-mode) .route-stop.next-warning .name::before,` |
| 1289 | `route-stop` | `body:not(.drive-mode) .route-stop.flow-green .name::before{` |
| 1308 | `Normal` | `   NORMAL ROUTE CARD BACKGROUND BOOST` |
| 1309 | `Normal` | `   Normal modda Durak Akışı kartlarının arka planını canlı yapar.` |
| 1312 | `route-stop` | `body:not(.drive-mode) .route-stop{` |
| 1325 | `route-stop` | `body:not(.drive-mode) .route-stop.done{` |
| 1335 | `route-stop` | `body:not(.drive-mode) .route-stop.done .name{` |
| 1340 | `route-stop` | `body:not(.drive-mode) .route-stop.done .meta,` |
| 1341 | `route-stop` | `body:not(.drive-mode) .route-stop.done .extra-k,` |
| 1342 | `route-stop` | `body:not(.drive-mode) .route-stop.done .extra-v{` |
| 1346 | `Canlı` | `/* Seçili/canlı kırmızı kart kendi rengini korusun */` |
| 1347 | `route-stop` | `body:not(.drive-mode) .route-stop.live-danger{` |
| 1357 | `Normal` | `   NORMAL ROUTE WARNING COLORS RESTORE` |
| 1358 | `Durak Akışı` | `   Durak Akışı: kırmızı / turuncu / yeşil akış renklerini geri getirir.` |
| 1361 | `Canlı` | `/* Canlı / tehlike: kırmızı */` |
| 1362 | `route-stop` | `body:not(.drive-mode) .route-stop.live-danger{` |
| 1377 | `Sıradaki` | `/* Sıradaki uyarı: turuncu */` |
| 1378 | `route-stop` | `body:not(.drive-mode) .route-stop.next-warning:not(.live-danger){` |
| 1393 | `route-stop` | `body:not(.drive-mode) .route-stop.flow-green:not(.live-danger):not(.next-warning){` |
| 1408 | `route-stop` | `body:not(.drive-mode) .route-stop.live-danger .name,` |
| 1409 | `route-stop` | `body:not(.drive-mode) .route-stop.live-danger .meta,` |
| 1410 | `route-stop` | `body:not(.drive-mode) .route-stop.live-danger .extra-k,` |
| 1411 | `route-stop` | `body:not(.drive-mode) .route-stop.live-danger .extra-v,` |
| 1412 | `route-stop` | `body:not(.drive-mode) .route-stop.next-warning .name,` |
| 1413 | `route-stop` | `body:not(.drive-mode) .route-stop.next-warning .meta,` |
| 1414 | `route-stop` | `body:not(.drive-mode) .route-stop.next-warning .extra-k,` |
| 1415 | `route-stop` | `body:not(.drive-mode) .route-stop.next-warning .extra-v,` |
| 1416 | `route-stop` | `body:not(.drive-mode) .route-stop.flow-green .name,` |
| 1417 | `route-stop` | `body:not(.drive-mode) .route-stop.flow-green .meta,` |
| 1418 | `route-stop` | `body:not(.drive-mode) .route-stop.flow-green .extra-k,` |
| 1419 | `route-stop` | `body:not(.drive-mode) .route-stop.flow-green .extra-v{` |
| 1425 | `route-stop` | `body:not(.drive-mode) .route-stop.live-danger .name::before{` |
| 1429 | `route-stop` | `body:not(.drive-mode) .route-stop.next-warning .name::before{` |
| 1433 | `route-stop` | `body:not(.drive-mode) .route-stop.flow-green .name::before{` |
| 1440 | `Canlı` | `   Canlı ve Sıradaki durak kutularını daha canlı yapar.` |
| 1456 | `Canlı` | `/* Canlı kutusu biraz yeşil vurgu alsın */` |
| 1464 | `Sıradaki` | `/* Sıradaki kutusu mavi vurgu */` |
| 1487 | `Canlı` | `   Tek sistem: Canlı/Sıradaki sabit, durak adı TV altyazısı gibi akar.` |
| 1490 | `route-strip` | `.route-strip-meta{` |
| 1547 | `route-strip` | `.route-strip-meta .route-pill b{` |
| 1562 | `Boş` | `/* İkinci kopya: boşluk olmadan akış sağlar */` |
| 1591 | `Canlı` | `   Canlı durak kırmızı uyarıdayken üst Canlı yazısını da kırmızı yapar.` |
| 1594 | `route-strip` | `body.drive-mode .route-strip:has(.route-stop.live-danger) ~ *,` |
| 1595 | `route-strip` | `body:not(.drive-mode) .route-strip:has(.route-stop.live-danger) ~ *{` |
| 1599 | `route-strip` | `.route-strip-shell:has(.route-stop.live-danger) .route-pill-live{` |
| 1610 | `route-strip` | `.route-strip-shell:has(.route-stop.live-danger) .route-pill-live .route-mini-label,` |
| 1611 | `route-strip` | `.route-strip-shell:has(.route-stop.live-danger) .route-pill-live #routeMiniLive{` |
| 1618 | `route-strip` | `.route-strip-shell:has(.route-stop.live-danger) .route-mini-dot{` |
| 1628 | `Sıradaki` | `   Sıradaki durak uyarı/turuncu kart olduğunda üst Sıradaki kutusu da turuncu olur.` |
| 1631 | `route-strip` | `.route-strip-shell:has(.route-stop.next-warning) .route-pill-next{` |
| 1642 | `route-strip` | `.route-strip-shell:has(.route-stop.next-warning) .route-pill-next .route-mini-label,` |
| 1643 | `route-strip` | `.route-strip-shell:has(.route-stop.next-warning) .route-pill-next #routeMiniNext{` |
| 1656 | `legend` | `   DRIVE MODE LEGEND FIXED SINGLE FINAL` |
| 1657 | `Sürüş` | `   Sürüş modunda Boş/Bay/Bayan/Bagaj/İniş/Servis barı` |

### `android_app/app/src/main/python/static/seats/patches/stop-selected-toast.js`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 59 | `selected-stop` | `  document.addEventListener("muavin:selected-stop-change", function(e){` |

### `android_app/app/src/main/python/static/seats/patches/bottom-voice-command.css`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 1 | `voice` | `#seatSimpleVoiceBtn{` |
| 8 | `voice` | `  #seatSimpleVoiceBtn .ico{` |
| 12 | `voice` | `  #seatSimpleVoiceBtn .voice-bottom-text{` |
| 20 | `voice` | `#seatSimpleVoiceBtn.listening{` |

### `android_app/app/src/main/python/static/seats/patches/manual-ticket-system.css`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 4 | `Sesli Komut` | `    Sadece sesli komutla işaretlenen mevcut yolcuya 🎫 verir.` |
| 39 | `drive-mode` | `  body.drive-mode .seat .manual-ticket-badge{` |

### `android_app/app/src/main/python/static/seats/patches/top-sound-toggle.js`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 21 | `voice` | `      if(window.SeatsVoice && typeof window.SeatsVoice.isEnabled === "function"){` |
| 22 | `voice` | `        return !!window.SeatsVoice.isEnabled();` |
| 32 | `voice` | `      if(window.SeatsVoice && typeof window.SeatsVoice.setEnabled === "function"){` |
| 33 | `voice` | `        window.SeatsVoice.setEnabled(on);` |
| 55 | `voice` | `        if(window.SeatsVoice && typeof window.SeatsVoice.stop === "function"){` |
| 56 | `voice` | `          window.SeatsVoice.stop();` |
| 57 | `voice` | `        }else if(window.SeatsStopVoice){` |
| 58 | `voice` | `          window.SeatsStopVoice();` |
| 83 | `Sessiz` | `      : '<span>🔇</span><span>Sessiz</span>';` |

### `android_app/app/src/main/python/static/seats/patches/stop-flow-focus-patch.js`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 6 | `selectedStop` | `  var memoryKey = "muavin:selectedStop:" + String(window.TRIP_KEY \|\| window.BAG_TRIP \|\| location.pathname);` |
| 15 | `Sıradaki` | `    v = v.replace(/^Sıradaki\s*:\s*/i, "");` |
| 39 | `selectedStop` | `    var fromWindow = cleanStopName(window.__muavinSelectedStop \|\| "");` |
| 48 | `selectedStop` | `    var badge = qs("#selectedStopBadge");` |
| 57 | `selectedStop` | `    window.__muavinSelectedStop = name;` |
| 81 | `route-stop` | `    qsa(".route-stop, [data-stop-name], [data-stop]").forEach(function(el){` |
| 112 | `selectedStop` | `    var badge = qs("#selectedStopBadge");` |
| 114 | `Seçili durak` | `      if((badge.textContent \|\| "").toLocaleLowerCase("tr-TR").includes("seçili durak")){` |
| 115 | `Seçili durak` | `        badge.textContent = "🎯 Seçili durak: " + name;` |
| 122 | `selectedStop` | `  function applySelectedStop(name){` |
| 135 | `selectedStop` | `    if(typeof window.setSelectedStop === "function" && !window.__stopFocusCallingSetSelected){` |
| 138 | `selectedStop` | `        window.setSelectedStop(name, true);` |
| 140 | `selectedStop` | `        console.warn("setSelectedStop çağrısı geçildi:", e);` |
| 149 | `selected-stop` | `    document.dispatchEvent(new CustomEvent("muavin:selected-stop-change", {detail:{stop:name}}));` |
| 160 | `Durak Akışı` | `      '<div class="stop-focus-panel" role="dialog" aria-modal="true" aria-label="Durak Akışı">' +` |
| 164 | `Durak Akışı` | `            '<div class="stop-focus-badge">Sadece Durak Akışı</div>' +` |
| 166 | `Durak Akışı` | `          '<h2 class="stop-focus-title">Durak Akışı</h2>' +` |
| 167 | `Seçili durak` | `          '<p class="stop-focus-sub">Seçili durak: <b data-current-stop>—</b></p>' +` |
| 186 | `selectedStop` | `        applySelectedStop(name);` |
| 222 | `Seçili durak` | `      meta.textContent = sameStop(stop, current) ? "Şu an seçili durak" : "Dokun, seç ve koltuk planına dön";` |
| 272 | `seat-simple` | `      if(document.documentElement.classList.contains("seat-simple-mode")) return true;` |
| 273 | `seat-simple` | `      if(document.body.classList.contains("seat-simple-mode")) return true;` |
| 291 | `seat-simple` | `      if(btn.classList && btn.classList.contains("seat-simple-bottom-item")){` |
| 296 | `seat-simple` | `      var parent = btn.closest(".seat-simple-bottom-bar, .seat-simple-dock, .seat-simple-nav");` |
| 314 | `Seçili durak` | `    if(low.includes("seçili durak")) return null;` |
| 329 | `Normal` | `    // Normal moddaki alt Durak butonunu engelleme.` |
| 330 | `Durak Akışı` | `    // Sadece Sade Koltuk modundaki Durak butonu özel "Sadece Durak Akışı" ekranını açsın.` |
| 341 | `selectedStop` | `  function hookSetSelectedStop(){` |
| 342 | `selectedStop` | `    if(typeof window.setSelectedStop !== "function") return;` |
| 343 | `selectedStop` | `    if(window.setSelectedStop.__stopFlowFocusHooked) return;` |
| 345 | `selectedStop` | `    var old = window.setSelectedStop;` |
| 357 | `selectedStop` | `    window.setSelectedStop = wrapped;` |
| 379 | `selectedStop` | `    hookSetSelectedStop();` |

### `android_app/app/src/main/python/static/seats/patches/right-seat-column-spacing-fix.css`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 38 | `Sürüş` | `    Sürüş modunda koltuklar biraz daha sıkıştığı için` |
| 41 | `drive-mode` | `  body.drive-mode .deck{` |
| 46 | `drive-mode` | `    body.drive-mode .deck{` |

### `android_app/app/src/main/python/static/seats/patches/bottom-row-51-54-equal-spacing.css`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 13 | `drive-mode` | `  body.drive-mode .deck .cell[style*="grid-row:14"],` |
| 14 | `drive-mode` | `  body.drive-mode .deck .cell[style*="grid-row: 14"]{` |

### `android_app/app/src/main/python/static/seats/patches/only-54-reapply-right-shift.css`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 15 | `drive-mode` | `  body.drive-mode .deck .cell[style*="grid-row:14"][style*="grid-column:4"],` |
| 16 | `drive-mode` | `  body.drive-mode .deck .cell[style*="grid-row:14"][style*="grid-column: 4"],` |
| 17 | `drive-mode` | `  body.drive-mode .deck .cell[style*="grid-row: 14"][style*="grid-column:4"],` |
| 18 | `drive-mode` | `  body.drive-mode .deck .cell[style*="grid-row: 14"][style*="grid-column: 4"]{` |

### `android_app/app/src/main/python/static/seats/patches/seat-layout-fab-pack.css`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 39 | `Sürüş` | `    Sürüş modunda koltuklar biraz daha sıkıştığı için` |
| 42 | `drive-mode` | `  body.drive-mode .deck{` |
| 47 | `drive-mode` | `    body.drive-mode .deck{` |
| 65 | `drive-mode` | `  body.drive-mode .deck .cell[style*="grid-row:14"],` |
| 66 | `drive-mode` | `  body.drive-mode .deck .cell[style*="grid-row: 14"]{` |
| 85 | `drive-mode` | `  body.drive-mode .deck .cell[style*="grid-row:14"][style*="grid-column:4"],` |
| 86 | `drive-mode` | `  body.drive-mode .deck .cell[style*="grid-row:14"][style*="grid-column: 4"],` |
| 87 | `drive-mode` | `  body.drive-mode .deck .cell[style*="grid-row: 14"][style*="grid-column:4"],` |
| 88 | `drive-mode` | `  body.drive-mode .deck .cell[style*="grid-row: 14"][style*="grid-column: 4"]{` |
| 95 | `Boş` | `    43 ile 51 arasındaki boş sol alana yerleştirir.` |
| 120 | `drive-mode` | `  body.drive-mode .fab-column.fab-left-gap-moved .fab{` |
| 133 | `drive-mode` | `    body.drive-mode .fab-column.fab-left-gap-moved .fab{` |
| 143 | `Boş` | `    Sol boş alana taşınan hızlı işlem butonlarını` |
| 259 | `drive-mode` | `  body.drive-mode .fab-column.fab-left-gap-moved .fab{` |
| 282 | `drive-mode` | `    body.drive-mode .fab-column.fab-left-gap-moved .fab{` |
| 295 | `drive-mode` | `    static/seats/seats.css içindeki body.drive-mode .fab-column kuralı` |
| 299 | `drive-mode` | `    .fab-left-gap-moved sınıfı varsa, drive-mode kurallarını ezip` |
| 304 | `drive-mode` | `  body.drive-mode .fab-column.fab-left-gap-moved{` |
| 345 | `drive-mode` | `  body.drive-mode .fab-column.fab-left-gap-moved::before{` |
| 362 | `drive-mode` | `  body.drive-mode .fab-column.fab-left-gap-moved .fab{` |
| 382 | `drive-mode` | `  body.drive-mode .fab-column.fab-left-gap-moved .fab::after{` |
| 389 | `drive-mode` | `    body.drive-mode .fab-column.fab-left-gap-moved{` |
| 400 | `drive-mode` | `    body.drive-mode .fab-column.fab-left-gap-moved .fab{` |

### `android_app/app/src/main/python/static/seats/patches/seat-simple-ui-pack.css`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 1 | `seat-simple` | `/* ===== seat-simple-open-mode-style ===== */` |
| 7 | `seat-simple` | `.seat-simple-toggle{` |
| 28 | `seat-simple` | `html.seat-simple-mode .seats-shell{` |
| 34 | `seat-simple` | `html.seat-simple-mode .seats-shell > :not(.layout){` |
| 38 | `seat-simple` | `html.seat-simple-mode .layout{` |
| 43 | `seat-simple` | `html.seat-simple-mode .panel-card{` |
| 47 | `seat-simple` | `html.seat-simple-mode .board-card{` |
| 53 | `seat-simple` | `html.seat-simple-mode .board-inner{` |
| 57 | `Sürüş` | `/* üst sürüş/eta dock sade modda gizli */` |
| 58 | `seat-simple` | `html.seat-simple-mode #driveInlineDock,` |
| 59 | `seat-simple` | `html.seat-simple-mode #driveModeActionsDock{` |
| 63 | `legend` | `/* sağdaki ses/legend/kalabalık kontroller gizli */` |
| 64 | `seat-simple` | `html.seat-simple-mode .board-head-right,` |
| 65 | `voice` | `html.seat-simple-mode .voice-row,` |
| 66 | `voice` | `html.seat-simple-mode .drive-voice-row,` |
| 67 | `legend` | `html.seat-simple-mode .legend{` |
| 72 | `seat-simple` | `html.seat-simple-mode .board-head{` |
| 77 | `seat-simple` | `html.seat-simple-mode .board-title{` |
| 81 | `seat-simple` | `html.seat-simple-mode .board-kicker,` |
| 82 | `seat-simple` | `html.seat-simple-mode .board-title small{` |
| 86 | `seat-simple` | `html.seat-simple-mode .board-title h2{` |
| 93 | `selected-stop` | `html.seat-simple-mode .selected-stop-chip{` |
| 103 | `Durak Akışı` | `/* rota/durak akışı ilk açılışta gizli */` |
| 104 | `route-strip` | `html.seat-simple-mode .route-strip-shell,` |
| 105 | `route-flow` | `html.seat-simple-mode .route-flow-shell,` |
| 106 | `route-flow` | `html.seat-simple-mode .route-flow,` |
| 107 | `seat-simple` | `html.seat-simple-mode #routeStrip,` |
| 108 | `seat-simple` | `html.seat-simple-mode .route-mini,` |
| 109 | `seat-simple` | `html.seat-simple-mode .route-pill{` |
| 114 | `seat-simple` | `html.seat-simple-mode .deck-card,` |
| 115 | `seat-simple` | `html.seat-simple-mode .seat-deck,` |
| 116 | `seat-simple` | `html.seat-simple-mode .deck-shell{` |
| 122 | `seat-simple` | `  .seat-simple-toggle{` |
| 129 | `seat-simple` | `  html.seat-simple-mode .board-inner{` |
| 133 | `seat-simple` | `  html.seat-simple-mode .board-title h2{` |
| 138 | `seat-simple` | `/* ===== seat-simple-summary-polish-style ===== */` |
| 144 | `seat-simple` | `.seat-simple-summary{` |
| 159 | `seat-simple` | `html.seat-simple-mode .seat-simple-summary{` |
| 163 | `seat-simple` | `.seat-simple-summary-top{` |
| 171 | `seat-simple` | `.seat-simple-route{` |
| 183 | `seat-simple` | `.seat-simple-status{` |
| 200 | `seat-simple` | `.seat-simple-summary-grid{` |
| 206 | `seat-simple` | `.seat-simple-mini{` |
| 216 | `seat-simple` | `.seat-simple-mini small{` |
| 227 | `seat-simple` | `.seat-simple-mini b{` |
| 238 | `seat-simple` | `.seat-simple-mini .ok{` |
| 242 | `seat-simple` | `.seat-simple-mini .speed{` |
| 246 | `seat-simple` | `html.seat-simple-mode .seat-simple-toggle{` |
| 251 | `seat-simple` | `  .seat-simple-summary{` |
| 257 | `seat-simple` | `  .seat-simple-route{` |
| 261 | `seat-simple` | `  .seat-simple-summary-grid{` |
| 266 | `seat-simple` | `  .seat-simple-mini{` |
| 272 | `seat-simple` | `  .seat-simple-mini small{` |
| 276 | `seat-simple` | `  .seat-simple-mini b{` |
| 281 | `seat-simple` | `/* ===== seat-simple-bottom-bar-style ===== */` |
| 287 | `seat-simple` | `.seat-simple-bottom-bar{` |
| 308 | `seat-simple` | `html.seat-simple-mode .seat-simple-bottom-bar{` |
| 312 | `seat-simple` | `html.seat-simple-mode body{` |
| 316 | `seat-simple` | `.seat-simple-bottom-item{` |
| 339 | `seat-simple` | `.seat-simple-bottom-item .ico{` |
| 344 | `seat-simple` | `.seat-simple-bottom-item.primary{` |
| 351 | `seat-simple` | `.seat-simple-bottom-item.warn{` |
| 357 | `seat-simple` | `.seat-simple-bottom-item.danger{` |
| 363 | `seat-simple` | `.seat-simple-bottom-item:active{` |
| 368 | `seat-simple` | `  .seat-simple-bottom-bar{` |
| 377 | `seat-simple` | `  .seat-simple-bottom-item{` |
| 383 | `seat-simple` | `  .seat-simple-bottom-item .ico{` |
| 394 | `seat-simple` | `html.seat-modal-open .seat-simple-bottom-bar,` |
| 395 | `seat-simple` | `body.seat-modal-open .seat-simple-bottom-bar{` |

### `android_app/app/src/main/python/static/seats/patches/seat-simple-ui-pack.js`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 1 | `seat-simple` | `/* ===== seat-simple-open-mode-script ===== */` |
| 34 | `seat-simple` | `    document.documentElement.classList.toggle("seat-simple-mode", simple);` |
| 35 | `seat-simple` | `    document.body.classList.toggle("seat-simple-mode", simple);` |
| 41 | `sade koltuk moduna dön` | `        : "💺 Sade koltuk moduna dön";` |
| 60 | `seat-simple` | `    btn.className = "seat-simple-toggle";` |
| 86 | `seat-simple` | `/* ===== seat-simple-summary-polish-script ===== */` |
| 103 | `seat-simple` | `      box.className = "seat-simple-summary";` |
| 105 | `seat-simple` | `        <div class="seat-simple-summary-top">` |
| 106 | `seat-simple` | `          <div class="seat-simple-route" id="seatSimpleRoute">—</div>` |
| 107 | `seat-simple` | `          <div class="seat-simple-status"><span>●</span><span>Sade Mod</span></div>` |
| 110 | `seat-simple` | `        <div class="seat-simple-summary-grid">` |
| 111 | `seat-simple` | `          <div class="seat-simple-mini">` |
| 115 | `seat-simple` | `          <div class="seat-simple-mini">` |
| 119 | `seat-simple` | `          <div class="seat-simple-mini">` |
| 150 | `selectedStop` | `    let stop = readText("#selectedStopBadge") \|\| "—";` |
| 156 | `voice` | `    let filled = readText("#voiceSeatFilled") \|\| readText("#driveVoiceFilled") \|\| "";` |
| 157 | `voice` | `    let empty  = readText("#voiceSeatEmpty")  \|\| readText("#driveVoiceEmpty")  \|\| "";` |

### `android_app/app/src/main/python/static/seats/patches/mobile-performance-fix.css`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 21 | `Boş` | `  /* Beyaz flash/boşluk görünmesin diye kök alanı koyulaştır */` |
| 56 | `seat-simple` | `  .seat-simple-bottom-bar,` |
| 71 | `route-stop` | `  .route-stop,` |
| 72 | `voice` | `  .voice-command-btn,` |
| 73 | `voice` | `  .drive-voice-btn,` |
| 74 | `seat-simple` | `  .seat-simple-bottom-item,` |
| 82 | `route-stop` | `  .route-stop,` |
| 83 | `route-stop` | `  .route-stop *,` |
| 84 | `voice` | `  .voice-command-btn,` |
| 85 | `voice` | `  .drive-voice-btn,` |
| 104 | `route-stop` | `  .route-stop,` |
| 105 | `seat-simple` | `  .seat-simple-bottom-item,` |
| 106 | `voice` | `  .voice-command-btn,` |
| 107 | `voice` | `  .drive-voice-btn{` |
| 116 | `seat-simple` | `  .seat-simple-bottom-bar,` |

### `android_app/app/src/main/python/static/seats/patches/stop-flow-compact-mobile.css`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 1 | `Durak Akışı` | `/* Durak Akışı mobil kompakt görünüm */` |

### `android_app/app/src/main/python/static/seats/patches/seat-label-ghost-clean.css`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 3 | `Boş` | `   Boş koltuk altı label kutularındaki kare karartmayı kaldırır.` |
| 9 | `Boş` | `  /* Boş label tamamen yok olsun */` |
| 10 | `seat-simple` | `  html.seat-simple-mode .deck .cell .label:empty,` |
| 11 | `seat-simple` | `  body.seat-simple-mode .deck .cell .label:empty,` |
| 27 | `seat-simple` | `  html.seat-simple-mode .deck .cell .label,` |
| 28 | `seat-simple` | `  body.seat-simple-mode .deck .cell .label{` |
| 37 | `seat-simple` | `  html.seat-simple-mode .deck .cell .label:not(:empty),` |
| 38 | `seat-simple` | `  body.seat-simple-mode .deck .cell .label:not(:empty){` |

### `android_app/app/src/main/python/static/seats/patches/hide-quick-fab-v22.css`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 4 | `Normal` | `   İşlem sekmesindeki normal Hızlı İşlemler ekranına dokunmaz.` |
| 9 | `drive-mode` | `body.drive-mode .fab-column,` |
| 10 | `drive-mode` | `body.drive-mode .fab-column.fab-left-gap-moved,` |
| 11 | `seat-simple` | `html.seat-simple-mode .fab-column,` |
| 12 | `seat-simple` | `html.seat-simple-mode .fab-column.fab-left-gap-moved{` |

### `android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-final.css`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 105 | `Canlı` | `/* canlı chip satırı */` |
| 113 | `mini-chip` | `.route-live-row .mini-chip{` |
| 128 | `mini-chip` | `.route-live-row .mini-chip span{` |
| 135 | `mini-chip` | `.route-live-row .mini-chip b{` |
| 251 | `Sürüş` | `   SÜRÜŞ / HIZ / RÖTAR SATIRI` |
| 277 | `driveModeToggle` | `#driveModeToggle,` |
| 278 | `driveSpeedChip` | `#driveSpeedChip,` |
| 279 | `driveEtaChip` | `#driveEtaChip,` |
| 291 | `driveModeToggle` | `#driveModeToggle{` |
| 320 | `board-head` | `.board-head{` |
| 340 | `board-title` | `.board-title h2{` |
| 349 | `board-title` | `.board-title small{` |
| 353 | `selected-stop` | `.selected-stop-chip{` |
| 366 | `board-head` | `.board-head-right{` |
| 371 | `voice` | `.voice-row{` |
| 377 | `voice` | `.voice-command-btn,` |
| 378 | `voice` | `.voice-state{` |
| 385 | `voice` | `.voice-command-btn{` |
| 392 | `voice` | `.voice-state{` |
| 401 | `legend` | `.legend{` |
| 407 | `legend` | `.legend .mini-chip{` |
| 422 | `route-flow` | `.route-flow,` |
| 425 | `route-flow` | `.route-flow-card{` |
| 439 | `board-stage` | `.board-stage{` |
| 715 | `mini-chip` | `  .route-live-row .mini-chip{` |
| 752 | `driveModeToggle` | `  #driveModeToggle,` |
| 753 | `driveSpeedChip` | `  #driveSpeedChip,` |
| 754 | `driveEtaChip` | `  #driveEtaChip,` |
| 761 | `board-title` | `  .board-title h2{` |
| 765 | `voice` | `  .voice-row{` |
| 769 | `legend` | `  .legend{` |
| 773 | `legend` | `  .legend .mini-chip{` |
| 778 | `board-stage` | `  .board-stage{` |
| 803 | `mini-chip` | `  .route-live-row .mini-chip b{` |
| 815 | `board-title` | `  .board-title h2{` |
| 819 | `selected-stop` | `  .selected-stop-chip{` |

### `android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-tone.css`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 40 | `Canlı` | `/* Üstteki canlı chipler: beyaz değil koyu cam */` |
| 41 | `mini-chip` | `.route-live-row .mini-chip{` |
| 48 | `mini-chip` | `.route-live-row .mini-chip span{` |
| 52 | `mini-chip` | `.route-live-row .mini-chip b{` |
| 103 | `board-title` | `.board-title h2{` |
| 107 | `selected-stop` | `.selected-stop-chip{` |
| 114 | `Sürüş` | `/* Sürüş / rötar satırı koyu cam */` |
| 115 | `driveModeToggle` | `#driveModeToggle,` |
| 116 | `driveSpeedChip` | `#driveSpeedChip,` |
| 117 | `driveEtaChip` | `#driveEtaChip,` |
| 126 | `driveModeToggle` | `#driveModeToggle{` |
| 140 | `Sesli Komut` | `/* Sesli komut ve legend */` |
| 141 | `voice` | `.voice-state{` |
| 147 | `legend` | `.legend .mini-chip{` |
| 153 | `Durak Akışı` | `/* Durak akışı koyu cam */` |
| 154 | `route-flow` | `.route-flow,` |
| 157 | `route-flow` | `.route-flow-card{` |

## 3) Tasarımı etkileyen CSS/JS izleri

### `templates/seats.html`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 6 | `drive-voice` | `<link rel="stylesheet" href="/static/seats/seats-final.css?v=drive-voice-real-width-test-1">` |
| 31 | `drive-speed` | `          <div id="driveSpeedChip" class="drive-speed-chip neutral">` |
| 32 | `drive-speed` | `            <div class="drive-speed-top">` |
| 33 | `drive-speed` | `              <span class="drive-speed-ico">🚦</span>` |
| 37 | `drive-speed` | `            <div class="drive-speed-sub">Limit: —</div>` |
| 40 | `drive-eta` | `          <div id="driveEtaChip" class="drive-eta-chip neutral">` |
| 41 | `drive-eta` | `            <div class="drive-eta-top">` |
| 45 | `drive-eta` | `            <div class="drive-eta-sub" id="driveEtaSub">ETA bekleniyor</div>` |
| 49 | `board-head` | `        <div class="board-head">` |
| 54 | `selected-stop-chip` | `            <div class="selected-stop-chip">🎯 Seçili durak: <b id="selectedStopBadge">—</b></div>` |
| 57 | `board-head` | `          <div class="board-head-right">` |
| 59 | `voice-command-btn` | `              <button class="voice-command-btn" id="btnDeckAI" type="button" title="Sesli Komut">` |
| 72 | `drive-voice` | `<div class="drive-voice-row" id="driveVoiceRow">` |
| 73 | `drive-voice` | `  <button class="drive-voice-btn" id="btnDeckAIDrive" type="button" title="Sesli Komut">` |
| 77 | `drive-voice` | `  <div class="drive-voice-seat" id="driveVoiceSeatCard" title="Koltuk özeti">` |
| 78 | `drive-voice` | `    <span class="drive-voice-seat-ico">💺</span>` |
| 79 | `drive-voice` | `    <span class="drive-voice-seat-values">` |
| 87 | `legend` | `<div class="legend">` |
| 88 | `mini-chip` | `              <div class="mini-chip">🟢 Boş</div>` |
| 89 | `mini-chip` | `              <div class="mini-chip">🔵 Bay</div>` |
| 90 | `mini-chip` | `              <div class="mini-chip">🩷 Bayan</div>` |
| 91 | `mini-chip` | `              <div class="mini-chip">🧳 Bagaj</div>` |
| 92 | `mini-chip` | `              <div class="mini-chip">🔔 İniş</div>` |
| 93 | `mini-chip` | `              <div class="mini-chip">🚌 Servis</div>` |
| 371 | `drive-eta` | `<script src="/static/seats/drive-eta-chip.js?v=1"></script>` |
| 380 | `drive-mode-actions-independent` | `<style id="drive-mode-actions-independent-style">` |
| 393 | `z-index` | `  z-index:9999;` |
| 399 | `border-radius` | `  border-radius:22px;` |
| 402 | `box-shadow` | `  box-shadow:` |
| 417 | `border-radius` | `  border-radius:15px;` |
| 420 | `box-shadow` | `  box-shadow:` |
| 451 | `border-radius` | `    border-radius:20px;` |
| 459 | `border-radius` | `    border-radius:13px;` |
| 465 | `drive-mode-actions-independent` | `<script id="drive-mode-actions-independent-js">` |
| 501 | `route-strip` | `      const routeShell = board.querySelector(".route-strip-shell");` |
| 642 | `bottom:` | `  bottom:auto !important;` |
| 655 | `z-index` | `  z-index:4 !important;` |
| 671 | `bottom:` | `  bottom:auto !important;` |
| 682 | `border-radius` | `  border-radius:17px !important;` |
| 699 | `box-shadow` | `  box-shadow:0 10px 24px rgba(37,99,235,.22), inset 0 1px 0 rgba(255,255,255,.15) !important;` |
| 705 | `drive-speed` | `.drive-speed-chip,` |
| 706 | `drive-eta` | `.drive-eta-chip{` |
| 710 | `border-radius` | `  border-radius:17px !important;` |
| 719 | `box-shadow` | `  box-shadow:inset 0 1px 0 rgba(255,255,255,.08) !important;` |
| 725 | `drive-speed` | `.drive-speed-chip{` |
| 730 | `drive-eta` | `.drive-eta-chip{` |
| 735 | `drive-speed` | `.drive-speed-top,` |
| 736 | `drive-eta` | `.drive-eta-top{` |
| 747 | `drive-speed` | `.drive-speed-top b,` |
| 748 | `drive-eta` | `.drive-eta-top b{` |
| 755 | `drive-speed` | `.drive-speed-sub,` |
| 756 | `drive-eta` | `.drive-eta-sub{` |
| 768 | `board-head` | `.board-head{` |
| 770 | `z-index` | `  z-index:3 !important;` |
| 777 | `z-index` | `  z-index:3 !important;` |
| 786 | `drive-eta` | `.drive-eta-chip *{` |
| 794 | `bottom:` | `    margin-bottom:10px !important;` |
| 802 | `border-radius` | `    border-radius:16px !important;` |
| 807 | `drive-speed` | `  .drive-speed-chip,` |
| 808 | `drive-eta` | `  .drive-eta-chip{` |
| 811 | `border-radius` | `    border-radius:16px !important;` |
| 816 | `drive-speed` | `  .drive-speed-chip{` |
| 821 | `drive-eta` | `  .drive-eta-chip{` |
| 825 | `drive-speed` | `  .drive-speed-top,` |
| 826 | `drive-eta` | `  .drive-eta-top{` |
| 830 | `drive-speed` | `  .drive-speed-sub,` |
| 831 | `drive-eta` | `  .drive-eta-sub{` |
| 840 | `drive-mode-force-toggle` | `<script id="drive-mode-force-toggle-js">` |
| 1044 | `drive-voice` | `<script id="drive-voice-mirror-script">` |
| 1111 | `seat-simple-bottom-bar` | `<script id="seat-simple-bottom-bar-script">` |
| 1156 | `seat-simple-bottom-bar` | `    bar.className = "seat-simple-bottom-bar";` |
| 1194 | `route-strip` | `          const flow = q("#routeStrip") \|\| q(".route-strip-shell") \|\| q(".route-flow-shell");` |

### `static/seats/seats.css`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 36 | `bottom:` | `    --mobile-safe-bottom:112px;` |
| 57 | `box-shadow` | `    box-shadow:var(--shadow);` |
| 58 | `backdrop-filter` | `    backdrop-filter:blur(12px);` |
| 70 | `z-index` | `    z-index:1200;` |
| 72 | `grid-template` | `    grid-template-columns:minmax(0,1fr) auto;` |
| 77 | `border-radius` | `    border-radius:28px;` |
| 98 | `border-radius` | `    border-radius:18px;` |
| 105 | `box-shadow` | `    box-shadow:0 12px 24px rgba(0,0,0,.22);` |
| 127 | `route-live` | `  .route-live-row{` |
| 133 | `mini-chip` | `  .mini-chip{` |
| 139 | `border-radius` | `    border-radius:999px;` |
| 147 | `box-shadow` | `    box-shadow:0 10px 20px rgba(0,0,0,.16);` |
| 150 | `mini-chip` | `  .mini-chip b{` |
| 157 | `grid-template` | `    grid-template-columns:repeat(5, 50px);` |
| 182 | `voice-command-btn` | `  .voice-command-btn:hover{` |
| 193 | `border-radius` | `    border-radius:18px;` |
| 197 | `box-shadow` | `    box-shadow:0 12px 26px rgba(0,0,0,.24);` |
| 202 | `grid-template` | `    grid-template-columns:repeat(6, minmax(0,1fr));` |
| 214 | `border-radius` | `    border-radius:20px;` |
| 217 | `box-shadow` | `    box-shadow:var(--shadow-soft);` |
| 262 | `border-radius` | `    border-radius:28px;` |
| 283 | `z-index` | `    z-index:1;` |
| 286 | `board-head` | `  .board-head{` |
| 288 | `grid-template` | `    grid-template-columns:minmax(0,1fr) auto;` |
| 291 | `bottom:` | `    margin-bottom:12px;` |
| 307 | `border-radius` | `    border-radius:999px;` |
| 331 | `board-head` | `  .board-head-right{` |
| 347 | `voice-command-btn` | `  .voice-command-btn{` |
| 356 | `border-radius` | `    border-radius:15px;` |
| 364 | `box-shadow` | `    box-shadow:` |
| 370 | `voice-command-btn` | `  .voice-command-btn.listening{` |
| 381 | `border-radius` | `    border-radius:999px;` |
| 389 | `legend` | `  .legend{` |
| 396 | `legend` | `  .legend .mini-chip{` |
| 402 | `selected-stop-chip` | `  .selected-stop-chip{` |
| 408 | `border-radius` | `    border-radius:999px;` |
| 416 | `box-shadow` | `    box-shadow:0 10px 22px rgba(0,0,0,.18);` |
| 419 | `route-strip` | `  .route-strip-shell{` |
| 420 | `bottom:` | `    margin-bottom:12px;` |
| 422 | `border-radius` | `    border-radius:22px;` |
| 425 | `box-shadow` | `    box-shadow:var(--shadow-soft);` |
| 428 | `route-strip` | `  .route-strip-head{` |
| 434 | `bottom:` | `    margin-bottom:10px;` |
| 437 | `route-strip` | `  .route-strip-title{` |
| 443 | `route-strip` | `  .route-strip-meta{` |
| 456 | `border-radius` | `    border-radius:999px;` |
| 464 | `route-strip` | `  .route-strip{` |
| 468 | `bottom:` | `    padding-bottom:2px;` |
| 472 | `route-strip` | `  .route-strip::-webkit-scrollbar{ display:none; }` |
| 479 | `border-radius` | `    border-radius:18px;` |
| 486 | `box-shadow` | `    box-shadow:0 10px 20px rgba(0,0,0,.16);` |
| 534 | `box-shadow` | `    box-shadow:` |
| 545 | `border-radius` | `    border-radius:26px;` |
| 567 | `grid-template` | `    grid-template-columns:var(--seat-w) var(--seat-w) var(--seat-w) var(--seat-w);` |
| 581 | `border-radius` | `    border-radius:20px;` |
| 583 | `box-shadow` | `    box-shadow:0 20px 40px rgba(0,0,0,.25);` |
| 600 | `border-radius` | `    border-radius:12px;` |
| 609 | `box-shadow` | `    box-shadow:0 10px 22px rgba(0,0,0,.22);` |
| 614 | `z-index` | `    z-index:1;` |
| 623 | `z-index` | `    z-index:1;` |
| 626 | `border-radius` | `    border-radius:22px;` |
| 638 | `box-shadow` | `    box-shadow:` |
| 649 | `box-shadow` | `    box-shadow:` |
| 661 | `box-shadow` | `      box-shadow:` |
| 667 | `box-shadow` | `      box-shadow:` |
| 691 | `border-radius` | `    border-radius:999px;` |
| 695 | `box-shadow` | `    box-shadow:0 8px 18px rgba(0,0,0,.26);` |
| 719 | `bottom:` | `    bottom:-7px;` |
| 733 | `bottom:` | `    bottom:14px;` |
| 734 | `z-index` | `    z-index:40;` |
| 744 | `border-radius` | `    border-radius:50%;` |
| 749 | `box-shadow` | `    box-shadow:0 16px 32px rgba(0,0,0,.32);` |
| 764 | `box-shadow` | `      box-shadow:0 0 0 0 rgba(239,68,68,0), 0 14px 30px rgba(0,0,0,.3);` |
| 767 | `box-shadow` | `      box-shadow:0 0 0 11px rgba(239,68,68,.20), 0 14px 30px rgba(0,0,0,.3);` |
| 781 | `border-radius` | `    border-radius:999px;` |
| 788 | `grid-template` | `    grid-template-columns:repeat(5, minmax(0,1fr));` |
| 790 | `bottom:` | `    margin-bottom:12px;` |
| 796 | `border-radius` | `    border-radius:16px;` |
| 811 | `box-shadow` | `    box-shadow:0 10px 20px rgba(0,0,0,.14);` |
| 823 | `border-radius` | `    border-radius:22px;` |
| 827 | `box-shadow` | `    box-shadow:0 12px 24px rgba(0,0,0,.10);` |
| 835 | `bottom:` | `    margin-bottom:12px;` |
| 853 | `grid-template` | `    grid-template-columns:1fr 1fr;` |
| 859 | `border-radius` | `    border-radius:18px;` |
| 869 | `bottom:` | `    margin-bottom:6px;` |
| 920 | `border-radius` | `    border-radius:18px;` |
| 955 | `border-radius` | `    border-radius:14px;` |
| 969 | `box-shadow` | `    box-shadow:0 0 0 2px rgba(34,197,94,.26) inset;` |
| 974 | `box-shadow` | `    box-shadow:0 0 0 2px rgba(245,158,11,.24) inset;` |
| 979 | `box-shadow` | `    box-shadow:0 0 0 2px rgba(239,68,68,.25) inset;` |
| 1011 | `border-radius` | `    border-radius:16px;` |
| 1018 | `grid-template` | `  .field-row{ display:grid; grid-template-columns:1fr 1fr; gap:10px; }` |
| 1040 | `border-radius` | `    border-radius:14px;` |
| 1060 | `border-radius` | `    border-radius:16px;` |
| 1076 | `border-radius` | `    border-radius:16px;` |
| 1078 | `box-shadow` | `    box-shadow:0 14px 28px rgba(0,0,0,.20);` |
| 1092 | `grid-template` | `    grid-template-columns:repeat(2, minmax(0,1fr));` |
| 1120 | `border-radius` | `    border-radius:14px;` |
| 1145 | `grid-template` | `    grid-template-columns:1fr auto;` |
| 1149 | `border-radius` | `    border-radius:18px;` |
| 1156 | `box-shadow` | `    box-shadow:0 0 0 2px rgba(59,130,246,.32) inset;` |
| 1186 | `border-radius` | `    border-radius:999px;` |
| 1208 | `border-radius` | `    border-radius:14px;` |
| 1222 | `position:fixed` | `    position:fixed;` |
| 1225 | `z-index` | `    z-index:3000;` |
| 1231 | `position:fixed` | `    position:fixed;` |
| 1238 | `z-index` | `    z-index:3010;` |
| 1244 | `bottom:` | `    bottom:12px;` |
| 1294 | `border-radius` | `    border-radius:14px;` |
| 1301 | `position:fixed` | `    position:fixed;` |
| 1304 | `z-index` | `    z-index:5000;` |
| 1307 | `border-radius` | `    border-radius:14px;` |
| 1310 | `box-shadow` | `    box-shadow:0 16px 32px rgba(0,0,0,.3);` |
| 1317 | `grid-template` | `      grid-template-columns:minmax(0, 1.16fr) 420px;` |
| 1334 | `z-index` | `      z-index:20;` |
| 1335 | `grid-template` | `      grid-template-columns:1fr;` |
| 1337 | `border-radius` | `      border-radius:24px;` |
| 1341 | `grid-template` | `      grid-template-columns:repeat(5, 44px);` |
| 1350 | `border-radius` | `      border-radius:16px;` |
| 1355 | `grid-template` | `      grid-template-columns:repeat(3, minmax(0,1fr));` |
| 1359 | `grid-template` | `      grid-template-columns:1fr;` |
| 1365 | `grid-template` | `      grid-template-columns:1fr;` |
| 1370 | `bottom:` | `      padding-bottom:12px;` |
| 1378 | `position:fixed` | `      position:fixed;` |
| 1380 | `bottom:` | `      bottom:16px;` |
| 1381 | `z-index` | `      z-index:1300;` |
| 1392 | `border-radius` | `      border-radius:28px;` |
| 1415 | `border-radius` | `      border-radius:22px;` |
| 1421 | `border-radius` | `      border-radius:16px;` |
| 1435 | `mini-chip` | `    .mini-chip{` |
| 1444 | `grid-template` | `      grid-template-columns:unset;` |
| 1446 | `bottom:` | `      padding-bottom:4px;` |
| 1455 | `border-radius` | `      border-radius:24px;` |
| 1458 | `board-head` | `    .board-head{` |
| 1459 | `grid-template` | `      grid-template-columns:1fr;` |
| 1467 | `board-head` | `    .board-head-right{` |
| 1478 | `voice-command-btn` | `    .voice-command-btn{` |
| 1484 | `border-radius` | `      border-radius:13px;` |
| 1493 | `legend` | `    .legend{` |
| 1498 | `route-strip` | `    .route-strip-shell{` |
| 1500 | `border-radius` | `      border-radius:20px;` |
| 1511 | `border-radius` | `      border-radius:22px;` |
| 1520 | `border-radius` | `      border-radius:18px;` |
| 1525 | `bottom:` | `      bottom:12px;` |
| 1535 | `grid-template` | `      grid-template-columns:repeat(5, minmax(0,1fr));` |
| 1543 | `border-radius` | `      border-radius:14px;` |
| 1554 | `border-radius` | `      border-radius:22px;` |
| 1560 | `grid-template` | `      grid-template-columns:repeat(5, 40px);` |
| 1568 | `border-radius` | `      border-radius:14px;` |
| 1571 | `voice-command-btn` | `    .voice-command-btn{` |
| 1598 | `box-shadow` | `  box-shadow:` |
| 1626 | `box-shadow` | `  box-shadow:` |
| 1642 | `box-shadow` | `  box-shadow:` |
| 1660 | `border-radius` | `    border-radius:22px;` |
| 1672 | `border-radius` | `    border-radius:15px;` |
| 1688 | `route-live` | `  .route-live-row{` |
| 1690 | `grid-template` | `    grid-template-columns:1fr 1fr;` |
| 1694 | `route-live` | `  .route-live-row .mini-chip{` |
| 1703 | `grid-template` | `    grid-template-columns:repeat(5, 42px);` |
| 1710 | `border-radius` | `    border-radius:15px;` |
| 1717 | `grid-template` | `    grid-template-columns:1fr 1fr;` |
| 1726 | `border-radius` | `    border-radius:18px;` |
| 1748 | `border-radius` | `    border-radius:24px;` |
| 1751 | `board-head` | `  .board-head{` |
| 1752 | `bottom:` | `    margin-bottom:8px;` |
| 1769 | `selected-stop-chip` | `  .selected-stop-chip{` |
| 1775 | `legend` | `  /* Sesli komut ve legend kısmı daha kompakt */` |
| 1776 | `board-head` | `  .board-head-right{` |
| 1784 | `voice-command-btn` | `  .voice-command-btn{` |
| 1794 | `legend` | `  .legend{` |
| 1798 | `legend` | `  .legend .mini-chip{` |
| 1805 | `route-strip` | `  .route-strip-shell{` |
| 1807 | `bottom:` | `    margin-bottom:10px;` |
| 1809 | `border-radius` | `    border-radius:22px;` |
| 1812 | `route-strip` | `  .route-strip-head{` |
| 1813 | `bottom:` | `    margin-bottom:8px;` |
| 1816 | `route-strip` | `  .route-strip-title{` |
| 1828 | `border-radius` | `    border-radius:18px;` |
| 1860 | `voice-command-btn` | `  .voice-command-btn{` |
| 1876 | `position:fixed` | `  position:fixed;` |
| 1879 | `z-index` | `  z-index:7000;` |
| 1883 | `border-radius` | `  border-radius:999px;` |
| 1888 | `box-shadow` | `  box-shadow:0 14px 30px rgba(0,0,0,.35);` |
| 1889 | `backdrop-filter` | `  backdrop-filter:blur(12px);` |
| 1915 | `border-radius` | `  border-radius:22px;` |
| 1918 | `board-head` | `body.drive-mode .board-head{` |
| 1920 | `grid-template` | `  grid-template-columns:minmax(0,1fr) auto;` |
| 1923 | `bottom:` | `  margin-bottom:8px;` |
| 1929 | `legend` | `body.drive-mode .legend{` |
| 1933 | `selected-stop-chip` | `body.drive-mode .selected-stop-chip{` |
| 1939 | `board-head` | `body.drive-mode .board-head-right{` |
| 1949 | `voice-command-btn` | `body.drive-mode .voice-command-btn{` |
| 1953 | `border-radius` | `  border-radius:14px;` |
| 1961 | `route-strip` | `body.drive-mode .route-strip-shell{` |
| 1963 | `bottom:` | `  margin-bottom:8px;` |
| 1965 | `border-radius` | `  border-radius:20px;` |
| 1968 | `route-strip` | `body.drive-mode .route-strip-head{` |
| 1969 | `bottom:` | `  margin-bottom:7px;` |
| 1972 | `route-strip` | `body.drive-mode .route-strip-title{` |
| 1986 | `border-radius` | `  border-radius:17px;` |
| 2008 | `border-radius` | `    border-radius:18px;` |
| 2012 | `board-head` | `  body.drive-mode .board-head{` |
| 2013 | `grid-template` | `    grid-template-columns:1fr;` |
| 2017 | `board-head` | `  body.drive-mode .board-head-right{` |
| 2026 | `selected-stop-chip` | `  body.drive-mode .selected-stop-chip{` |
| 2033 | `voice-command-btn` | `  body.drive-mode .voice-command-btn{` |
| 2038 | `route-strip` | `  body.drive-mode .route-strip-shell{` |
| 2040 | `bottom:` | `    margin-bottom:8px;` |
| 2072 | `border-radius` | `  border-radius:999px;` |
| 2082 | `border-radius` | `  border-radius:22px !important;` |
| 2087 | `board-head` | `body.drive-mode .board-head{` |
| 2088 | `grid-template` | `  grid-template-columns:minmax(0,1fr) auto !important;` |
| 2091 | `bottom:` | `  margin-bottom:8px !important;` |
| 2095 | `selected-stop-chip` | `body.drive-mode .selected-stop-chip{` |
| 2099 | `border-radius` | `  border-radius:18px;` |
| 2113 | `voice-command-btn` | `body.drive-mode .voice-command-btn{` |
| 2118 | `border-radius` | `  border-radius:17px;` |
| 2120 | `box-shadow` | `  box-shadow:0 12px 24px rgba(0,0,0,.28);` |
| 2124 | `route-strip` | `body.drive-mode .route-strip-shell{` |
| 2127 | `border-radius` | `  border-radius:22px !important;` |

### `static/seats/drive-controls.js`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 161 | `drive-speed` | `    el.className = "drive-speed-chip " + cls;` |
| 167 | `drive-speed` | `      <div class="drive-speed-top">` |
| 168 | `drive-speed` | `        <span class="drive-speed-ico">🚦</span>` |
| 172 | `drive-speed` | `      <div class="drive-speed-sub">${limitText}${stopText}</div>` |

### `static/seats/seats-final.css`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 45 | `z-index` | `  z-index:20 !important;` |
| 48 | `grid-template` | `  grid-template-columns:minmax(0,1fr) auto !important;` |
| 54 | `border-radius` | `  border-radius:26px !important;` |
| 60 | `box-shadow` | `  box-shadow:0 22px 55px rgba(0,0,0,.28) !important;` |
| 65 | `grid-template` | `  grid-template-columns:52px 1fr !important;` |
| 73 | `border-radius` | `  border-radius:18px !important;` |
| 79 | `box-shadow` | `  box-shadow:inset 0 1px 0 rgba(255,255,255,.08) !important;` |
| 102 | `route-live` | `.route-live-row{` |
| 104 | `grid-template` | `  grid-template-columns:repeat(4,minmax(0,1fr)) !important;` |
| 109 | `route-live` | `.route-live-row .mini-chip{` |
| 113 | `border-radius` | `  border-radius:16px !important;` |
| 125 | `route-live` | `.route-live-row .mini-chip span{` |
| 129 | `route-live` | `.route-live-row .mini-chip b{` |
| 137 | `grid-template` | `  grid-template-columns:repeat(5,42px) !important;` |
| 148 | `border-radius` | `  border-radius:15px !important;` |
| 154 | `box-shadow` | `  box-shadow:0 10px 22px rgba(0,0,0,.22) !important;` |
| 164 | `grid-template` | `  grid-template-columns:repeat(2,minmax(0,1fr)) !important;` |
| 173 | `border-radius` | `  border-radius:19px !important;` |
| 179 | `box-shadow` | `  box-shadow:0 14px 30px rgba(0,0,0,.22) !important;` |
| 220 | `grid-template` | `  grid-template-columns:minmax(0,1fr) 380px !important;` |
| 227 | `border-radius` | `  border-radius:26px !important;` |
| 232 | `box-shadow` | `  box-shadow:0 22px 55px rgba(0,0,0,.28) !important;` |
| 257 | `bottom:` | `  bottom:auto !important;` |
| 264 | `grid-template` | `  grid-template-columns:92px minmax(0,1fr) minmax(0,1.2fr) !important;` |
| 271 | `z-index` | `  z-index:1 !important;` |
| 279 | `drive-speed` | `.drive-speed-chip,` |
| 280 | `drive-eta` | `.drive-eta-chip{` |
| 286 | `bottom:` | `  bottom:auto !important;` |
| 294 | `border-radius` | `  border-radius:16px !important;` |
| 298 | `box-shadow` | `  box-shadow:inset 0 1px 0 rgba(255,255,255,.07) !important;` |
| 321 | `drive-speed` | `.drive-speed-top,` |
| 322 | `drive-eta` | `.drive-eta-top{` |
| 336 | `drive-speed` | `.drive-speed-top b,` |
| 337 | `drive-eta` | `.drive-eta-top b{` |
| 344 | `drive-speed` | `.drive-speed-sub,` |
| 345 | `drive-eta` | `.drive-eta-sub{` |
| 359 | `board-head` | `.board-head{` |
| 361 | `grid-template` | `  grid-template-columns:1fr !important;` |
| 377 | `border-radius` | `  border-radius:999px !important;` |
| 399 | `selected-stop-chip` | `.selected-stop-chip{` |
| 403 | `border-radius` | `  border-radius:17px !important;` |
| 407 | `box-shadow` | `  box-shadow:inset 0 1px 0 rgba(255,255,255,.06) !important;` |
| 412 | `board-head` | `.board-head-right{` |
| 419 | `grid-template` | `  grid-template-columns:minmax(0,1fr) 84px !important;` |
| 424 | `voice-command-btn` | `.voice-command-btn,` |
| 428 | `border-radius` | `  border-radius:17px !important;` |
| 430 | `box-shadow` | `  box-shadow:inset 0 1px 0 rgba(255,255,255,.07) !important;` |
| 433 | `voice-command-btn` | `.voice-command-btn{` |
| 447 | `voice-command-btn` | `.voice-command-btn::before,` |
| 448 | `voice-command-btn` | `.voice-command-btn::after{` |
| 452 | `voice-command-btn` | `.voice-command-btn span{` |
| 469 | `legend` | `.legend{` |
| 471 | `grid-template` | `  grid-template-columns:repeat(3,minmax(0,1fr)) !important;` |
| 476 | `legend` | `.legend .mini-chip,` |
| 477 | `mini-chip` | `.mini-chip{` |
| 481 | `border-radius` | `  border-radius:14px !important;` |
| 497 | `route-strip` | `.route-strip-shell{` |
| 500 | `border-radius` | `  border-radius:21px !important;` |
| 503 | `box-shadow` | `  box-shadow:0 12px 26px rgba(0,0,0,.16) !important;` |
| 506 | `route-strip` | `.route-strip-head{` |
| 509 | `bottom:` | `  margin-bottom:8px !important;` |
| 512 | `route-strip` | `.route-strip-title{` |
| 518 | `route-strip` | `.route-strip-meta{` |
| 520 | `grid-template` | `  grid-template-columns:minmax(0,.9fr) minmax(0,1.25fr) 46px !important;` |
| 530 | `border-radius` | `  border-radius:15px !important;` |
| 556 | `border-radius` | `  border-radius:15px !important;` |
| 566 | `route-strip` | `.route-strip{` |
| 570 | `bottom:` | `  padding-bottom:2px !important;` |
| 574 | `route-strip` | `.route-strip::-webkit-scrollbar{` |
| 582 | `border-radius` | `  border-radius:17px !important;` |
| 598 | `border-radius` | `  border-radius:24px !important;` |
| 621 | `border-radius` | `  border-radius:20px !important;` |
| 622 | `box-shadow` | `  box-shadow:` |
| 634 | `bottom:` | `  bottom:10px !important;` |
| 641 | `border-radius` | `  border-radius:17px !important;` |
| 661 | `bottom:` | `  margin-bottom:9px !important;` |
| 662 | `bottom:` | `  padding-bottom:3px !important;` |
| 673 | `border-radius` | `  border-radius:14px !important;` |
| 687 | `border-radius` | `  border-radius:20px !important;` |
| 691 | `box-shadow` | `  box-shadow:0 10px 22px rgba(0,0,0,.12) !important;` |
| 735 | `border-radius` | `  border-radius:15px !important;` |
| 744 | `grid-template` | `    grid-template-columns:1fr !important;` |
| 759 | `grid-template` | `    grid-template-columns:1fr !important;` |
| 760 | `border-radius` | `    border-radius:23px !important;` |
| 770 | `route-live` | `  .route-live-row{` |
| 771 | `grid-template` | `    grid-template-columns:1fr 1fr !important;` |
| 775 | `grid-template` | `    grid-template-columns:1fr 1fr !important;` |
| 779 | `border-radius` | `    border-radius:22px !important;` |
| 786 | `grid-template` | `    grid-template-columns:82px minmax(0,1fr) minmax(0,1.05fr) !important;` |
| 798 | `route-strip` | `  .route-strip-meta{` |
| 799 | `grid-template` | `    grid-template-columns:minmax(0,.85fr) minmax(0,1.15fr) 42px !important;` |
| 830 | `grid-template` | `    grid-template-columns:minmax(0,1fr) 74px !important;` |
| 833 | `voice-command-btn` | `  .voice-command-btn span{` |
| 837 | `legend` | `  .legend{` |
| 838 | `grid-template` | `    grid-template-columns:repeat(3,minmax(0,1fr)) !important;` |
| 841 | `mini-chip` | `  .mini-chip{` |
| 853 | `border-radius` | `  border-radius:24px !important;` |
| 859 | `border-radius` | `  border-radius:16px !important;` |
| 864 | `grid-template` | `  grid-template-columns:46px 1fr !important;` |
| 876 | `route-live` | `.route-live-row{` |
| 881 | `route-live` | `.route-live-row .mini-chip{` |
| 883 | `border-radius` | `  border-radius:15px !important;` |
| 894 | `border-radius` | `  border-radius:18px !important;` |
| 905 | `grid-template` | `  grid-template-columns:180px minmax(0,1fr) !important;` |
| 906 | `bottom:` | `  margin-bottom:12px !important;` |
| 917 | `border-radius` | `  border-radius:18px !important;` |
| 922 | `drive-eta` | `.drive-eta-chip{` |
| 925 | `border-radius` | `  border-radius:18px !important;` |
| 938 | `selected-stop-chip` | `.selected-stop-chip{` |
| 947 | `grid-template` | `    grid-template-columns:180px minmax(0,1fr) !important;` |
| 954 | `route-live` | `  .route-live-row .mini-chip{` |
| 981 | `border-radius` | `  border-radius:999px;` |
| 1085 | `box-shadow` | `  box-shadow:` |
| 1116 | `box-shadow` | `  box-shadow:` |
| 1146 | `box-shadow` | `  box-shadow:` |
| 1176 | `box-shadow` | `  box-shadow:` |
| 1188 | `box-shadow` | `  box-shadow:` |
| 1318 | `box-shadow` | `  box-shadow:` |
| 1368 | `box-shadow` | `  box-shadow:` |
| 1384 | `box-shadow` | `  box-shadow:` |
| 1399 | `box-shadow` | `  box-shadow:` |
| 1449 | `box-shadow` | `  box-shadow:` |
| 1490 | `route-strip` | `.route-strip-meta{` |
| 1493 | `grid-template` | `  grid-template-columns:minmax(0,.9fr) minmax(0,1.25fr) 50px !important;` |
| 1509 | `grid-template` | `  grid-template-columns:10px auto minmax(0,1fr) !important;` |
| 1514 | `grid-template` | `  grid-template-columns:auto minmax(0,1fr) !important;` |
| 1522 | `border-radius` | `  border-radius:999px !important;` |
| 1525 | `box-shadow` | `  box-shadow:` |
| 1547 | `route-strip` | `.route-strip-meta .route-pill b{` |
| 1594 | `route-strip` | `body.drive-mode .route-strip:has(.route-stop.live-danger) ~ *,` |
| 1595 | `route-strip` | `body:not(.drive-mode) .route-strip:has(.route-stop.live-danger) ~ *{` |
| 1599 | `route-strip` | `.route-strip-shell:has(.route-stop.live-danger) .route-pill-live{` |
| 1604 | `box-shadow` | `  box-shadow:` |
| 1610 | `route-strip` | `.route-strip-shell:has(.route-stop.live-danger) .route-pill-live .route-mini-label,` |
| 1611 | `route-strip` | `.route-strip-shell:has(.route-stop.live-danger) .route-pill-live #routeMiniLive{` |
| 1618 | `route-strip` | `.route-strip-shell:has(.route-stop.live-danger) .route-mini-dot{` |
| 1620 | `box-shadow` | `  box-shadow:` |
| 1631 | `route-strip` | `.route-strip-shell:has(.route-stop.next-warning) .route-pill-next{` |
| 1636 | `box-shadow` | `  box-shadow:` |
| 1642 | `route-strip` | `.route-strip-shell:has(.route-stop.next-warning) .route-pill-next .route-mini-label,` |
| 1643 | `route-strip` | `.route-strip-shell:has(.route-stop.next-warning) .route-pill-next #routeMiniNext{` |
| 1656 | `legend` | `   DRIVE MODE LEGEND FIXED SINGLE FINAL` |
| 1661 | `legend` | `/* Normal modda legend gizli */` |
| 1662 | `legend` | `body:not(.drive-mode) .board-head-right .legend{` |
| 1666 | `legend` | `/* Sürüş modunda legend sabit alt bar */` |
| 1667 | `legend` | `body.drive-mode .board-head-right .legend{` |
| 1668 | `position:fixed` | `  position:fixed !important;` |
| 1672 | `bottom:` | `  bottom:calc(env(safe-area-inset-bottom, 0px) + 8px) !important;` |
| 1679 | `z-index` | `  z-index:99999 !important;` |
| 1682 | `grid-template` | `  grid-template-columns:repeat(6, minmax(0,1fr)) !important;` |
| 1689 | `border-radius` | `  border-radius:22px !important;` |
| 1694 | `box-shadow` | `  box-shadow:` |
| 1698 | `backdrop-filter` | `  backdrop-filter:blur(14px) !important;` |
| 1699 | `backdrop-filter` | `  -webkit-backdrop-filter:blur(14px) !important;` |
| 1702 | `legend` | `body.drive-mode .board-head-right .legend .mini-chip{` |
| 1709 | `border-radius` | `  border-radius:15px !important;` |
| 1717 | `box-shadow` | `  box-shadow:none !important;` |
| 1731 | `bottom:` | `  padding-bottom:82px !important;` |
| 1735 | `bottom:` | `  padding-bottom:82px !important;` |
| 1739 | `legend` | `  body.drive-mode .board-head-right .legend{` |
| 1741 | `bottom:` | `    bottom:calc(env(safe-area-inset-bottom, 0px) + 6px) !important;` |
| 1745 | `border-radius` | `    border-radius:20px !important;` |
| 1748 | `legend` | `  body.drive-mode .board-head-right .legend .mini-chip{` |
| 1757 | `bottom:` | `    padding-bottom:78px !important;` |
| 1762 | `legend` | `  body.drive-mode .board-head-right .legend .mini-chip{` |
| 1781 | `position:fixed` | `  position:fixed !important;` |
| 1785 | `bottom:` | `  bottom:auto !important;` |
| 1788 | `z-index` | `  z-index:99998 !important;` |
| 1796 | `border-radius` | `  border-radius:24px !important;` |
| 1809 | `box-shadow` | `  box-shadow:` |
| 1813 | `backdrop-filter` | `  backdrop-filter:blur(14px) !important;` |
| 1814 | `backdrop-filter` | `  -webkit-backdrop-filter:blur(14px) !important;` |
| 1824 | `border-radius` | `  border-radius:15px !important;` |
| 1842 | `box-shadow` | `  box-shadow:` |
| 1854 | `route-strip` | `body.drive-mode .route-strip-shell{` |
| 1864 | `border-radius` | `    border-radius:22px !important;` |
| 1872 | `border-radius` | `    border-radius:14px !important;` |
| 1876 | `route-strip` | `  body.drive-mode .route-strip-shell{` |
| 1899 | `bottom:` | `  bottom:auto !important;` |
| 1911 | `grid-template` | `  grid-template-columns:repeat(5, minmax(0, 1fr)) !important;` |
| 1916 | `border-radius` | `  border-radius:24px !important;` |
| 1922 | `box-shadow` | `  box-shadow:` |
| 1926 | `backdrop-filter` | `  backdrop-filter:blur(12px) !important;` |
| 1927 | `backdrop-filter` | `  -webkit-backdrop-filter:blur(12px) !important;` |
| 1929 | `z-index` | `  z-index:20 !important;` |
| 1939 | `border-radius` | `  border-radius:17px !important;` |
| 1957 | `box-shadow` | `  box-shadow:` |
| 1974 | `route-strip` | `body.drive-mode .route-strip-shell{` |
| 1984 | `border-radius` | `    border-radius:22px !important;` |
| 1990 | `border-radius` | `    border-radius:16px !important;` |
| 2001 | `board-head` | `.board-head-right .voice-row,` |
| 2002 | `board-head` | `body.drive-mode .board-head-right .voice-row,` |
| 2003 | `board-head` | `body:not(.drive-mode) .board-head-right .voice-row{` |
| 2007 | `grid-template` | `  grid-template-columns:minmax(0,1fr) minmax(120px,.78fr) !important;` |
| 2012 | `board-head` | `.board-head-right .voice-state{` |
| 2017 | `voice-command-btn` | `.board-head-right .voice-command-btn{` |
| 2023 | `border-radius` | `  border-radius:22px !important;` |
| 2037 | `box-shadow` | `  box-shadow:` |
| 2044 | `voice-command-btn` | `.board-head-right .voice-command-btn::before,` |
| 2045 | `voice-command-btn` | `.board-head-right .voice-command-btn::after{` |
| 2050 | `voice-command-btn` | `.board-head-right .voice-command-btn span{` |
| 2062 | `board-head` | `.board-head-right .voice-seat-mini{` |
| 2068 | `border-radius` | `  border-radius:22px !important;` |
| 2080 | `box-shadow` | `  box-shadow:` |
| 2088 | `board-head` | `.board-head-right .voice-seat-mini::before{` |
| 2094 | `border-radius` | `  border-radius:13px !important;` |
| 2101 | `box-shadow` | `  box-shadow:` |
| 2109 | `board-head` | `.board-head-right .voice-seat-mini::after{` |
| 2115 | `board-head` | `.board-head-right .voice-seat-mini span{` |
| 2123 | `board-head` | `.board-head-right .voice-seat-mini span:first-child::after{` |
| 2131 | `board-head` | `.board-head-right .voice-seat-mini b{` |
| 2139 | `board-head` | `.board-head-right .voice-seat-mini span:first-child b{` |
| 2143 | `board-head` | `.board-head-right .voice-seat-mini span:last-child b{` |
| 2148 | `board-head` | `  .board-head-right .voice-row,` |
| 2149 | `board-head` | `  body.drive-mode .board-head-right .voice-row,` |
| 2150 | `board-head` | `  body:not(.drive-mode) .board-head-right .voice-row{` |
| 2151 | `grid-template` | `    grid-template-columns:minmax(0,1fr) 116px !important;` |
| 2155 | `voice-command-btn` | `  .board-head-right .voice-command-btn,` |
| 2156 | `board-head` | `  .board-head-right .voice-seat-mini{` |
| 2159 | `border-radius` | `    border-radius:20px !important;` |

### `static/seats/patches/stop-selected-toast.css`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 2 | `position:fixed` | `    position:fixed;` |
| 4 | `bottom:` | `    bottom:calc(env(safe-area-inset-bottom, 0px) + 92px);` |
| 6 | `z-index` | `    z-index:2147483600;` |
| 23 | `border-radius` | `    border-radius:22px;` |
| 30 | `box-shadow` | `    box-shadow:0 18px 44px rgba(0,0,0,.42), inset 0 1px 0 rgba(255,255,255,.12);` |
| 31 | `backdrop-filter` | `    backdrop-filter:blur(16px);` |
| 32 | `backdrop-filter` | `    -webkit-backdrop-filter:blur(16px);` |
| 39 | `border-radius` | `    border-radius:16px;` |

### `static/seats/patches/bottom-voice-command.css`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 24 | `box-shadow` | `    box-shadow:0 14px 34px rgba(220,38,38,.30), inset 0 1px 0 rgba(255,255,255,.14) !important;` |

### `static/seats/patches/manual-ticket-system.css`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 14 | `bottom:` | `    bottom:-8px;` |
| 17 | `border-radius` | `    border-radius:999px;` |
| 28 | `box-shadow` | `    box-shadow:` |
| 31 | `z-index` | `    z-index:12;` |
| 41 | `bottom:` | `    bottom:-9px;` |
| 50 | `bottom:` | `      bottom:-7px;` |

### `static/seats/patches/top-sound-toggle.css`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 4 | `grid-template` | `    grid-template-columns:1fr auto;` |
| 19 | `border-radius` | `    border-radius:22px;` |
| 32 | `box-shadow` | `    box-shadow:0 14px 34px rgba(22,163,74,.22), inset 0 1px 0 rgba(255,255,255,.14);` |
| 40 | `box-shadow` | `    box-shadow:0 14px 34px rgba(15,23,42,.25), inset 0 1px 0 rgba(255,255,255,.10);` |
| 56 | `border-radius` | `      border-radius:19px;` |

### `static/seats/patches/stop-flow-focus-patch.css`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 8 | `position:fixed` | `    position:fixed;` |
| 10 | `z-index` | `    z-index:2147483000;` |
| 30 | `border-radius` | `    border-radius:28px;` |
| 32 | `box-shadow` | `    box-shadow:0 28px 80px rgba(0,0,0,.55), inset 0 1px 0 rgba(255,255,255,.08);` |
| 40 | `bottom:` | `    border-bottom:1px solid rgba(120,160,255,.18);` |
| 49 | `bottom:` | `    margin-bottom:14px;` |
| 54 | `border-radius` | `    border-radius:18px;` |
| 60 | `box-shadow` | `    box-shadow:0 12px 28px rgba(37,92,255,.28);` |
| 67 | `border-radius` | `    border-radius:999px;` |
| 106 | `border-radius` | `    border-radius:24px;` |
| 112 | `box-shadow` | `    box-shadow:0 16px 34px rgba(0,0,0,.26), inset 0 1px 0 rgba(255,255,255,.06);` |
| 125 | `box-shadow` | `    box-shadow:0 16px 38px rgba(18,214,96,.18), inset 0 1px 0 rgba(255,255,255,.10);` |
| 132 | `border-radius` | `    border-radius:17px;` |
| 165 | `border-radius` | `    border-radius:999px;` |

### `static/seats/patches/stop-flow-focus-patch.js`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 296 | `seat-simple-bottom-bar` | `      var parent = btn.closest(".seat-simple-bottom-bar, .seat-simple-dock, .seat-simple-nav");` |

### `static/seats/patches/seat-layout-fab-pack.css`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 102 | `bottom:` | `    bottom:auto !important;` |
| 103 | `z-index` | `    z-index:45 !important;` |
| 115 | `border-radius` | `    border-radius:16px !important;` |
| 117 | `box-shadow` | `    box-shadow:0 14px 28px rgba(0,0,0,.34) !important;` |
| 123 | `border-radius` | `    border-radius:16px !important;` |
| 136 | `border-radius` | `      border-radius:15px !important;` |
| 149 | `border-radius` | `    border-radius:24px !important;` |
| 156 | `box-shadow` | `    box-shadow:` |
| 161 | `backdrop-filter` | `    backdrop-filter:blur(14px) !important;` |
| 162 | `backdrop-filter` | `    -webkit-backdrop-filter:blur(14px) !important;` |
| 184 | `border-radius` | `    border-radius:18px !important;` |
| 190 | `box-shadow` | `    box-shadow:` |
| 200 | `border-radius` | `    border-radius:22px;` |
| 230 | `border-radius` | `      border-radius:22px !important;` |
| 236 | `border-radius` | `      border-radius:17px !important;` |
| 249 | `border-radius` | `    border-radius:21px !important;` |
| 264 | `border-radius` | `    border-radius:15px !important;` |
| 271 | `border-radius` | `    border-radius:18px !important;` |
| 278 | `border-radius` | `      border-radius:19px !important;` |
| 287 | `border-radius` | `      border-radius:14px !important;` |
| 310 | `bottom:` | `    bottom:auto !important;` |
| 328 | `border-radius` | `    border-radius:21px !important;` |
| 335 | `box-shadow` | `    box-shadow:` |
| 341 | `z-index` | `    z-index:90 !important;` |
| 368 | `border-radius` | `    border-radius:15px !important;` |
| 384 | `border-radius` | `    border-radius:18px !important;` |
| 396 | `border-radius` | `      border-radius:19px !important;` |
| 405 | `border-radius` | `      border-radius:14px !important;` |

### `static/seats/patches/seat-simple-ui-pack.css`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 10 | `z-index` | `  z-index:9999;` |
| 15 | `border-radius` | `  border-radius:18px;` |
| 18 | `box-shadow` | `  box-shadow:0 12px 28px rgba(37,99,235,.24), inset 0 1px 0 rgba(255,255,255,.16);` |
| 40 | `grid-template` | `  grid-template-columns:1fr !important;` |
| 63 | `legend` | `/* sağdaki ses/legend/kalabalık kontroller gizli */` |
| 64 | `board-head` | `html.seat-simple-mode .board-head-right,` |
| 66 | `drive-voice` | `html.seat-simple-mode .drive-voice-row,` |
| 67 | `legend` | `html.seat-simple-mode .legend{` |
| 72 | `board-head` | `html.seat-simple-mode .board-head{` |
| 93 | `selected-stop-chip` | `html.seat-simple-mode .selected-stop-chip{` |
| 98 | `border-radius` | `  border-radius:18px !important;` |
| 104 | `route-strip` | `html.seat-simple-mode .route-strip-shell,` |
| 124 | `border-radius` | `    border-radius:16px;` |
| 126 | `bottom:` | `    margin-bottom:8px;` |
| 149 | `border-radius` | `  border-radius:22px;` |
| 154 | `box-shadow` | `  box-shadow:` |
| 168 | `bottom:` | `  margin-bottom:10px;` |
| 187 | `border-radius` | `  border-radius:999px;` |
| 202 | `grid-template` | `  grid-template-columns:1.25fr .75fr .75fr;` |
| 209 | `border-radius` | `  border-radius:17px;` |
| 212 | `box-shadow` | `  box-shadow:inset 0 1px 0 rgba(255,255,255,.04);` |
| 218 | `bottom:` | `  margin-bottom:5px;` |
| 247 | `bottom:` | `  margin-bottom:10px !important;` |
| 253 | `border-radius` | `    border-radius:20px;` |
| 254 | `bottom:` | `    margin-bottom:10px;` |
| 262 | `grid-template` | `    grid-template-columns:1.15fr .85fr .85fr;` |
| 269 | `border-radius` | `    border-radius:15px;` |
| 281 | `seat-simple-bottom-bar` | `/* ===== seat-simple-bottom-bar-style ===== */` |
| 287 | `seat-simple-bottom-bar` | `.seat-simple-bottom-bar{` |
| 289 | `position:fixed` | `  position:fixed;` |
| 292 | `bottom:` | `  bottom:10px;` |
| 293 | `z-index` | `  z-index:99999;` |
| 295 | `border-radius` | `  border-radius:26px;` |
| 299 | `box-shadow` | `  box-shadow:` |
| 302 | `backdrop-filter` | `  backdrop-filter:blur(18px) saturate(1.1);` |
| 303 | `backdrop-filter` | `  -webkit-backdrop-filter:blur(18px) saturate(1.1);` |
| 304 | `grid-template` | `  grid-template-columns:repeat(5,1fr);` |
| 308 | `seat-simple-bottom-bar` | `html.seat-simple-mode .seat-simple-bottom-bar{` |
| 313 | `bottom:` | `  padding-bottom:92px !important;` |
| 318 | `border-radius` | `  border-radius:20px;` |
| 336 | `box-shadow` | `  box-shadow:inset 0 1px 0 rgba(255,255,255,.06);` |
| 368 | `seat-simple-bottom-bar` | `  .seat-simple-bottom-bar{` |
| 371 | `bottom:` | `    bottom:8px;` |
| 372 | `border-radius` | `    border-radius:24px;` |
| 379 | `border-radius` | `    border-radius:18px;` |
| 394 | `seat-simple-bottom-bar` | `html.seat-modal-open .seat-simple-bottom-bar,` |
| 395 | `seat-simple-bottom-bar` | `body.seat-modal-open .seat-simple-bottom-bar{` |

### `static/seats/patches/mobile-performance-fix.css`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 24 | `position:fixed` | `    position:fixed;` |
| 26 | `z-index` | `    z-index:-1;` |
| 35 | `backdrop-filter` | `    -webkit-backdrop-filter:none !important;` |
| 36 | `backdrop-filter` | `    backdrop-filter:none !important;` |
| 56 | `seat-simple-bottom-bar` | `  .seat-simple-bottom-bar,` |
| 62 | `box-shadow` | `    box-shadow:0 8px 18px rgba(0,0,0,.22) !important;` |
| 72 | `voice-command-btn` | `  .voice-command-btn,` |
| 73 | `drive-voice` | `  .drive-voice-btn,` |
| 75 | `drive-speed` | `  .drive-speed-chip,` |
| 76 | `drive-eta` | `  .drive-eta-chip{` |
| 77 | `box-shadow` | `    box-shadow:0 4px 10px rgba(0,0,0,.18) !important;` |
| 84 | `voice-command-btn` | `  .voice-command-btn,` |
| 85 | `drive-voice` | `  .drive-voice-btn,` |
| 86 | `drive-speed` | `  .drive-speed-chip,` |
| 87 | `drive-eta` | `  .drive-eta-chip,` |
| 106 | `voice-command-btn` | `  .voice-command-btn,` |
| 107 | `drive-voice` | `  .drive-voice-btn{` |
| 116 | `seat-simple-bottom-bar` | `  .seat-simple-bottom-bar,` |
| 145 | `backdrop-filter` | `    -webkit-backdrop-filter:none !important;` |
| 146 | `backdrop-filter` | `    backdrop-filter:none !important;` |
| 164 | `box-shadow` | `    box-shadow:0 18px 38px rgba(0,0,0,.42) !important;` |

### `static/seats/patches/stop-flow-compact-mobile.css`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 11 | `border-radius` | `    border-radius:22px !important;` |
| 19 | `bottom:` | `    margin-bottom:8px !important;` |
| 25 | `border-radius` | `    border-radius:15px !important;` |
| 58 | `border-radius` | `    border-radius:18px !important;` |
| 65 | `border-radius` | `    border-radius:14px !important;` |

### `static/seats/patches/fab-sheet-solid-fix.css`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 23 | `box-shadow` | `    box-shadow:0 22px 58px rgba(0,0,0,.58), inset 0 1px 0 rgba(255,255,255,.06) !important;` |
| 24 | `backdrop-filter` | `    -webkit-backdrop-filter:none !important;` |
| 25 | `backdrop-filter` | `    backdrop-filter:none !important;` |

### `static/seats/patches/seat-label-ghost-clean.css`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 21 | `box-shadow` | `    box-shadow:none !important;` |
| 30 | `box-shadow` | `    box-shadow:none !important;` |
| 32 | `backdrop-filter` | `    backdrop-filter:none !important;` |
| 33 | `backdrop-filter` | `    -webkit-backdrop-filter:none !important;` |

### `static/seats/patches/unified-seat-deck-report-style.css`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 21 | `border-radius` | `  border-radius:24px !important;` |
| 46 | `grid-template` | `  grid-template-columns:` |
| 66 | `border-radius` | `  border-radius:24px !important;` |
| 117 | `border-radius` | `  border-radius:22px !important;` |
| 130 | `box-shadow` | `  box-shadow:` |
| 169 | `box-shadow` | `  box-shadow:` |
| 179 | `box-shadow` | `  box-shadow:` |
| 199 | `border-radius` | `  border-radius:28px !important;` |
| 204 | `box-shadow` | `  box-shadow:` |
| 229 | `border-radius` | `  border-radius:18px !important;` |
| 243 | `box-shadow` | `  box-shadow:` |
| 256 | `border-radius` | `  border-radius:999px !important;` |
| 278 | `bottom:` | `  bottom:-10px !important;` |
| 310 | `border-radius` | `    border-radius:22px !important;` |
| 317 | `border-radius` | `    border-radius:20px !important;` |
| 323 | `border-radius` | `    border-radius:25px !important;` |

### `android_app/app/src/main/python/templates/seats.html`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 6 | `drive-voice` | `<link rel="stylesheet" href="/static/seats/seats-final.css?v=drive-voice-real-width-test-1">` |
| 31 | `drive-speed` | `          <div id="driveSpeedChip" class="drive-speed-chip neutral">` |
| 32 | `drive-speed` | `            <div class="drive-speed-top">` |
| 33 | `drive-speed` | `              <span class="drive-speed-ico">🚦</span>` |
| 37 | `drive-speed` | `            <div class="drive-speed-sub">Limit: —</div>` |
| 40 | `drive-eta` | `          <div id="driveEtaChip" class="drive-eta-chip neutral">` |
| 41 | `drive-eta` | `            <div class="drive-eta-top">` |
| 45 | `drive-eta` | `            <div class="drive-eta-sub" id="driveEtaSub">ETA bekleniyor</div>` |
| 49 | `board-head` | `        <div class="board-head">` |
| 54 | `selected-stop-chip` | `            <div class="selected-stop-chip">🎯 Seçili durak: <b id="selectedStopBadge">—</b></div>` |
| 57 | `board-head` | `          <div class="board-head-right">` |
| 59 | `voice-command-btn` | `              <button class="voice-command-btn" id="btnDeckAI" type="button" title="Sesli Komut">` |
| 72 | `drive-voice` | `<div class="drive-voice-row" id="driveVoiceRow">` |
| 73 | `drive-voice` | `  <button class="drive-voice-btn" id="btnDeckAIDrive" type="button" title="Sesli Komut">` |
| 77 | `drive-voice` | `  <div class="drive-voice-seat" id="driveVoiceSeatCard" title="Koltuk özeti">` |
| 78 | `drive-voice` | `    <span class="drive-voice-seat-ico">💺</span>` |
| 79 | `drive-voice` | `    <span class="drive-voice-seat-values">` |
| 87 | `legend` | `<div class="legend">` |
| 88 | `mini-chip` | `              <div class="mini-chip">🟢 Boş</div>` |
| 89 | `mini-chip` | `              <div class="mini-chip">🔵 Bay</div>` |
| 90 | `mini-chip` | `              <div class="mini-chip">🩷 Bayan</div>` |
| 91 | `mini-chip` | `              <div class="mini-chip">🧳 Bagaj</div>` |
| 92 | `mini-chip` | `              <div class="mini-chip">🔔 İniş</div>` |
| 93 | `mini-chip` | `              <div class="mini-chip">🚌 Servis</div>` |
| 371 | `drive-eta` | `<script src="/static/seats/drive-eta-chip.js?v=1"></script>` |
| 380 | `drive-mode-actions-independent` | `<style id="drive-mode-actions-independent-style">` |
| 393 | `z-index` | `  z-index:9999;` |
| 399 | `border-radius` | `  border-radius:22px;` |
| 402 | `box-shadow` | `  box-shadow:` |
| 417 | `border-radius` | `  border-radius:15px;` |
| 420 | `box-shadow` | `  box-shadow:` |
| 451 | `border-radius` | `    border-radius:20px;` |
| 459 | `border-radius` | `    border-radius:13px;` |
| 465 | `drive-mode-actions-independent` | `<script id="drive-mode-actions-independent-js">` |
| 501 | `route-strip` | `      const routeShell = board.querySelector(".route-strip-shell");` |
| 642 | `bottom:` | `  bottom:auto !important;` |
| 655 | `z-index` | `  z-index:4 !important;` |
| 671 | `bottom:` | `  bottom:auto !important;` |
| 682 | `border-radius` | `  border-radius:17px !important;` |
| 699 | `box-shadow` | `  box-shadow:0 10px 24px rgba(37,99,235,.22), inset 0 1px 0 rgba(255,255,255,.15) !important;` |
| 705 | `drive-speed` | `.drive-speed-chip,` |
| 706 | `drive-eta` | `.drive-eta-chip{` |
| 710 | `border-radius` | `  border-radius:17px !important;` |
| 719 | `box-shadow` | `  box-shadow:inset 0 1px 0 rgba(255,255,255,.08) !important;` |
| 725 | `drive-speed` | `.drive-speed-chip{` |
| 730 | `drive-eta` | `.drive-eta-chip{` |
| 735 | `drive-speed` | `.drive-speed-top,` |
| 736 | `drive-eta` | `.drive-eta-top{` |
| 747 | `drive-speed` | `.drive-speed-top b,` |
| 748 | `drive-eta` | `.drive-eta-top b{` |
| 755 | `drive-speed` | `.drive-speed-sub,` |
| 756 | `drive-eta` | `.drive-eta-sub{` |
| 768 | `board-head` | `.board-head{` |
| 770 | `z-index` | `  z-index:3 !important;` |
| 777 | `z-index` | `  z-index:3 !important;` |
| 786 | `drive-eta` | `.drive-eta-chip *{` |
| 794 | `bottom:` | `    margin-bottom:10px !important;` |
| 802 | `border-radius` | `    border-radius:16px !important;` |
| 807 | `drive-speed` | `  .drive-speed-chip,` |
| 808 | `drive-eta` | `  .drive-eta-chip{` |
| 811 | `border-radius` | `    border-radius:16px !important;` |
| 816 | `drive-speed` | `  .drive-speed-chip{` |
| 821 | `drive-eta` | `  .drive-eta-chip{` |
| 825 | `drive-speed` | `  .drive-speed-top,` |
| 826 | `drive-eta` | `  .drive-eta-top{` |
| 830 | `drive-speed` | `  .drive-speed-sub,` |
| 831 | `drive-eta` | `  .drive-eta-sub{` |
| 840 | `drive-mode-force-toggle` | `<script id="drive-mode-force-toggle-js">` |
| 1044 | `drive-voice` | `<script id="drive-voice-mirror-script">` |
| 1111 | `seat-simple-bottom-bar` | `<script id="seat-simple-bottom-bar-script">` |
| 1156 | `seat-simple-bottom-bar` | `    bar.className = "seat-simple-bottom-bar";` |
| 1194 | `route-strip` | `          const flow = q("#routeStrip") \|\| q(".route-strip-shell") \|\| q(".route-flow-shell");` |

### `android_app/app/src/main/python/static/seats/seats.css`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 36 | `bottom:` | `    --mobile-safe-bottom:112px;` |
| 57 | `box-shadow` | `    box-shadow:var(--shadow);` |
| 58 | `backdrop-filter` | `    backdrop-filter:blur(12px);` |
| 70 | `z-index` | `    z-index:1200;` |
| 72 | `grid-template` | `    grid-template-columns:minmax(0,1fr) auto;` |
| 77 | `border-radius` | `    border-radius:28px;` |
| 98 | `border-radius` | `    border-radius:18px;` |
| 105 | `box-shadow` | `    box-shadow:0 12px 24px rgba(0,0,0,.22);` |
| 127 | `route-live` | `  .route-live-row{` |
| 133 | `mini-chip` | `  .mini-chip{` |
| 139 | `border-radius` | `    border-radius:999px;` |
| 147 | `box-shadow` | `    box-shadow:0 10px 20px rgba(0,0,0,.16);` |
| 150 | `mini-chip` | `  .mini-chip b{` |
| 157 | `grid-template` | `    grid-template-columns:repeat(5, 50px);` |
| 182 | `voice-command-btn` | `  .voice-command-btn:hover{` |
| 193 | `border-radius` | `    border-radius:18px;` |
| 197 | `box-shadow` | `    box-shadow:0 12px 26px rgba(0,0,0,.24);` |
| 202 | `grid-template` | `    grid-template-columns:repeat(6, minmax(0,1fr));` |
| 214 | `border-radius` | `    border-radius:20px;` |
| 217 | `box-shadow` | `    box-shadow:var(--shadow-soft);` |
| 262 | `border-radius` | `    border-radius:28px;` |
| 283 | `z-index` | `    z-index:1;` |
| 286 | `board-head` | `  .board-head{` |
| 288 | `grid-template` | `    grid-template-columns:minmax(0,1fr) auto;` |
| 291 | `bottom:` | `    margin-bottom:12px;` |
| 307 | `border-radius` | `    border-radius:999px;` |
| 331 | `board-head` | `  .board-head-right{` |
| 347 | `voice-command-btn` | `  .voice-command-btn{` |
| 356 | `border-radius` | `    border-radius:15px;` |
| 364 | `box-shadow` | `    box-shadow:` |
| 370 | `voice-command-btn` | `  .voice-command-btn.listening{` |
| 381 | `border-radius` | `    border-radius:999px;` |
| 389 | `legend` | `  .legend{` |
| 396 | `legend` | `  .legend .mini-chip{` |
| 402 | `selected-stop-chip` | `  .selected-stop-chip{` |
| 408 | `border-radius` | `    border-radius:999px;` |
| 416 | `box-shadow` | `    box-shadow:0 10px 22px rgba(0,0,0,.18);` |
| 419 | `route-strip` | `  .route-strip-shell{` |
| 420 | `bottom:` | `    margin-bottom:12px;` |
| 422 | `border-radius` | `    border-radius:22px;` |
| 425 | `box-shadow` | `    box-shadow:var(--shadow-soft);` |
| 428 | `route-strip` | `  .route-strip-head{` |
| 434 | `bottom:` | `    margin-bottom:10px;` |
| 437 | `route-strip` | `  .route-strip-title{` |
| 443 | `route-strip` | `  .route-strip-meta{` |
| 456 | `border-radius` | `    border-radius:999px;` |
| 464 | `route-strip` | `  .route-strip{` |
| 468 | `bottom:` | `    padding-bottom:2px;` |
| 472 | `route-strip` | `  .route-strip::-webkit-scrollbar{ display:none; }` |
| 479 | `border-radius` | `    border-radius:18px;` |
| 486 | `box-shadow` | `    box-shadow:0 10px 20px rgba(0,0,0,.16);` |
| 534 | `box-shadow` | `    box-shadow:` |
| 545 | `border-radius` | `    border-radius:26px;` |
| 567 | `grid-template` | `    grid-template-columns:var(--seat-w) var(--seat-w) var(--seat-w) var(--seat-w);` |
| 581 | `border-radius` | `    border-radius:20px;` |
| 583 | `box-shadow` | `    box-shadow:0 20px 40px rgba(0,0,0,.25);` |
| 600 | `border-radius` | `    border-radius:12px;` |
| 609 | `box-shadow` | `    box-shadow:0 10px 22px rgba(0,0,0,.22);` |
| 614 | `z-index` | `    z-index:1;` |
| 623 | `z-index` | `    z-index:1;` |
| 626 | `border-radius` | `    border-radius:22px;` |
| 638 | `box-shadow` | `    box-shadow:` |
| 649 | `box-shadow` | `    box-shadow:` |
| 661 | `box-shadow` | `      box-shadow:` |
| 667 | `box-shadow` | `      box-shadow:` |
| 691 | `border-radius` | `    border-radius:999px;` |
| 695 | `box-shadow` | `    box-shadow:0 8px 18px rgba(0,0,0,.26);` |
| 719 | `bottom:` | `    bottom:-7px;` |
| 733 | `bottom:` | `    bottom:14px;` |
| 734 | `z-index` | `    z-index:40;` |
| 744 | `border-radius` | `    border-radius:50%;` |
| 749 | `box-shadow` | `    box-shadow:0 16px 32px rgba(0,0,0,.32);` |
| 764 | `box-shadow` | `      box-shadow:0 0 0 0 rgba(239,68,68,0), 0 14px 30px rgba(0,0,0,.3);` |
| 767 | `box-shadow` | `      box-shadow:0 0 0 11px rgba(239,68,68,.20), 0 14px 30px rgba(0,0,0,.3);` |
| 781 | `border-radius` | `    border-radius:999px;` |
| 788 | `grid-template` | `    grid-template-columns:repeat(5, minmax(0,1fr));` |
| 790 | `bottom:` | `    margin-bottom:12px;` |
| 796 | `border-radius` | `    border-radius:16px;` |
| 811 | `box-shadow` | `    box-shadow:0 10px 20px rgba(0,0,0,.14);` |
| 823 | `border-radius` | `    border-radius:22px;` |
| 827 | `box-shadow` | `    box-shadow:0 12px 24px rgba(0,0,0,.10);` |
| 835 | `bottom:` | `    margin-bottom:12px;` |
| 853 | `grid-template` | `    grid-template-columns:1fr 1fr;` |
| 859 | `border-radius` | `    border-radius:18px;` |
| 869 | `bottom:` | `    margin-bottom:6px;` |
| 920 | `border-radius` | `    border-radius:18px;` |
| 955 | `border-radius` | `    border-radius:14px;` |
| 969 | `box-shadow` | `    box-shadow:0 0 0 2px rgba(34,197,94,.26) inset;` |
| 974 | `box-shadow` | `    box-shadow:0 0 0 2px rgba(245,158,11,.24) inset;` |
| 979 | `box-shadow` | `    box-shadow:0 0 0 2px rgba(239,68,68,.25) inset;` |
| 1011 | `border-radius` | `    border-radius:16px;` |
| 1018 | `grid-template` | `  .field-row{ display:grid; grid-template-columns:1fr 1fr; gap:10px; }` |
| 1040 | `border-radius` | `    border-radius:14px;` |
| 1060 | `border-radius` | `    border-radius:16px;` |
| 1076 | `border-radius` | `    border-radius:16px;` |
| 1078 | `box-shadow` | `    box-shadow:0 14px 28px rgba(0,0,0,.20);` |
| 1092 | `grid-template` | `    grid-template-columns:repeat(2, minmax(0,1fr));` |
| 1120 | `border-radius` | `    border-radius:14px;` |
| 1145 | `grid-template` | `    grid-template-columns:1fr auto;` |
| 1149 | `border-radius` | `    border-radius:18px;` |
| 1156 | `box-shadow` | `    box-shadow:0 0 0 2px rgba(59,130,246,.32) inset;` |
| 1186 | `border-radius` | `    border-radius:999px;` |
| 1208 | `border-radius` | `    border-radius:14px;` |
| 1222 | `position:fixed` | `    position:fixed;` |
| 1225 | `z-index` | `    z-index:3000;` |
| 1231 | `position:fixed` | `    position:fixed;` |
| 1238 | `z-index` | `    z-index:3010;` |
| 1244 | `bottom:` | `    bottom:12px;` |
| 1294 | `border-radius` | `    border-radius:14px;` |
| 1301 | `position:fixed` | `    position:fixed;` |
| 1304 | `z-index` | `    z-index:5000;` |
| 1307 | `border-radius` | `    border-radius:14px;` |
| 1310 | `box-shadow` | `    box-shadow:0 16px 32px rgba(0,0,0,.3);` |
| 1317 | `grid-template` | `      grid-template-columns:minmax(0, 1.16fr) 420px;` |
| 1334 | `z-index` | `      z-index:20;` |
| 1335 | `grid-template` | `      grid-template-columns:1fr;` |
| 1337 | `border-radius` | `      border-radius:24px;` |
| 1341 | `grid-template` | `      grid-template-columns:repeat(5, 44px);` |
| 1350 | `border-radius` | `      border-radius:16px;` |
| 1355 | `grid-template` | `      grid-template-columns:repeat(3, minmax(0,1fr));` |
| 1359 | `grid-template` | `      grid-template-columns:1fr;` |
| 1365 | `grid-template` | `      grid-template-columns:1fr;` |
| 1370 | `bottom:` | `      padding-bottom:12px;` |
| 1378 | `position:fixed` | `      position:fixed;` |
| 1380 | `bottom:` | `      bottom:16px;` |
| 1381 | `z-index` | `      z-index:1300;` |
| 1392 | `border-radius` | `      border-radius:28px;` |
| 1415 | `border-radius` | `      border-radius:22px;` |
| 1421 | `border-radius` | `      border-radius:16px;` |
| 1435 | `mini-chip` | `    .mini-chip{` |
| 1444 | `grid-template` | `      grid-template-columns:unset;` |
| 1446 | `bottom:` | `      padding-bottom:4px;` |
| 1455 | `border-radius` | `      border-radius:24px;` |
| 1458 | `board-head` | `    .board-head{` |
| 1459 | `grid-template` | `      grid-template-columns:1fr;` |
| 1467 | `board-head` | `    .board-head-right{` |
| 1478 | `voice-command-btn` | `    .voice-command-btn{` |
| 1484 | `border-radius` | `      border-radius:13px;` |
| 1493 | `legend` | `    .legend{` |
| 1498 | `route-strip` | `    .route-strip-shell{` |
| 1500 | `border-radius` | `      border-radius:20px;` |
| 1511 | `border-radius` | `      border-radius:22px;` |
| 1520 | `border-radius` | `      border-radius:18px;` |
| 1525 | `bottom:` | `      bottom:12px;` |
| 1535 | `grid-template` | `      grid-template-columns:repeat(5, minmax(0,1fr));` |
| 1543 | `border-radius` | `      border-radius:14px;` |
| 1554 | `border-radius` | `      border-radius:22px;` |
| 1560 | `grid-template` | `      grid-template-columns:repeat(5, 40px);` |
| 1568 | `border-radius` | `      border-radius:14px;` |
| 1571 | `voice-command-btn` | `    .voice-command-btn{` |
| 1598 | `box-shadow` | `  box-shadow:` |
| 1626 | `box-shadow` | `  box-shadow:` |
| 1642 | `box-shadow` | `  box-shadow:` |
| 1660 | `border-radius` | `    border-radius:22px;` |
| 1672 | `border-radius` | `    border-radius:15px;` |
| 1688 | `route-live` | `  .route-live-row{` |
| 1690 | `grid-template` | `    grid-template-columns:1fr 1fr;` |
| 1694 | `route-live` | `  .route-live-row .mini-chip{` |
| 1703 | `grid-template` | `    grid-template-columns:repeat(5, 42px);` |
| 1710 | `border-radius` | `    border-radius:15px;` |
| 1717 | `grid-template` | `    grid-template-columns:1fr 1fr;` |
| 1726 | `border-radius` | `    border-radius:18px;` |
| 1748 | `border-radius` | `    border-radius:24px;` |
| 1751 | `board-head` | `  .board-head{` |
| 1752 | `bottom:` | `    margin-bottom:8px;` |
| 1769 | `selected-stop-chip` | `  .selected-stop-chip{` |
| 1775 | `legend` | `  /* Sesli komut ve legend kısmı daha kompakt */` |
| 1776 | `board-head` | `  .board-head-right{` |
| 1784 | `voice-command-btn` | `  .voice-command-btn{` |
| 1794 | `legend` | `  .legend{` |
| 1798 | `legend` | `  .legend .mini-chip{` |
| 1805 | `route-strip` | `  .route-strip-shell{` |
| 1807 | `bottom:` | `    margin-bottom:10px;` |
| 1809 | `border-radius` | `    border-radius:22px;` |
| 1812 | `route-strip` | `  .route-strip-head{` |
| 1813 | `bottom:` | `    margin-bottom:8px;` |
| 1816 | `route-strip` | `  .route-strip-title{` |
| 1828 | `border-radius` | `    border-radius:18px;` |
| 1860 | `voice-command-btn` | `  .voice-command-btn{` |
| 1876 | `position:fixed` | `  position:fixed;` |
| 1879 | `z-index` | `  z-index:7000;` |
| 1883 | `border-radius` | `  border-radius:999px;` |
| 1888 | `box-shadow` | `  box-shadow:0 14px 30px rgba(0,0,0,.35);` |
| 1889 | `backdrop-filter` | `  backdrop-filter:blur(12px);` |
| 1915 | `border-radius` | `  border-radius:22px;` |
| 1918 | `board-head` | `body.drive-mode .board-head{` |
| 1920 | `grid-template` | `  grid-template-columns:minmax(0,1fr) auto;` |
| 1923 | `bottom:` | `  margin-bottom:8px;` |
| 1929 | `legend` | `body.drive-mode .legend{` |
| 1933 | `selected-stop-chip` | `body.drive-mode .selected-stop-chip{` |
| 1939 | `board-head` | `body.drive-mode .board-head-right{` |
| 1949 | `voice-command-btn` | `body.drive-mode .voice-command-btn{` |
| 1953 | `border-radius` | `  border-radius:14px;` |
| 1961 | `route-strip` | `body.drive-mode .route-strip-shell{` |
| 1963 | `bottom:` | `  margin-bottom:8px;` |
| 1965 | `border-radius` | `  border-radius:20px;` |
| 1968 | `route-strip` | `body.drive-mode .route-strip-head{` |
| 1969 | `bottom:` | `  margin-bottom:7px;` |
| 1972 | `route-strip` | `body.drive-mode .route-strip-title{` |
| 1986 | `border-radius` | `  border-radius:17px;` |
| 2008 | `border-radius` | `    border-radius:18px;` |
| 2012 | `board-head` | `  body.drive-mode .board-head{` |
| 2013 | `grid-template` | `    grid-template-columns:1fr;` |
| 2017 | `board-head` | `  body.drive-mode .board-head-right{` |
| 2026 | `selected-stop-chip` | `  body.drive-mode .selected-stop-chip{` |
| 2033 | `voice-command-btn` | `  body.drive-mode .voice-command-btn{` |
| 2038 | `route-strip` | `  body.drive-mode .route-strip-shell{` |
| 2040 | `bottom:` | `    margin-bottom:8px;` |
| 2072 | `border-radius` | `  border-radius:999px;` |
| 2082 | `border-radius` | `  border-radius:22px !important;` |
| 2087 | `board-head` | `body.drive-mode .board-head{` |
| 2088 | `grid-template` | `  grid-template-columns:minmax(0,1fr) auto !important;` |
| 2091 | `bottom:` | `  margin-bottom:8px !important;` |
| 2095 | `selected-stop-chip` | `body.drive-mode .selected-stop-chip{` |
| 2099 | `border-radius` | `  border-radius:18px;` |
| 2113 | `voice-command-btn` | `body.drive-mode .voice-command-btn{` |
| 2118 | `border-radius` | `  border-radius:17px;` |
| 2120 | `box-shadow` | `  box-shadow:0 12px 24px rgba(0,0,0,.28);` |
| 2124 | `route-strip` | `body.drive-mode .route-strip-shell{` |
| 2127 | `border-radius` | `  border-radius:22px !important;` |

### `android_app/app/src/main/python/static/seats/drive-controls.js`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 161 | `drive-speed` | `    el.className = "drive-speed-chip " + cls;` |
| 167 | `drive-speed` | `      <div class="drive-speed-top">` |
| 168 | `drive-speed` | `        <span class="drive-speed-ico">🚦</span>` |
| 172 | `drive-speed` | `      <div class="drive-speed-sub">${limitText}${stopText}</div>` |

### `android_app/app/src/main/python/static/seats/seats-final.css`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 45 | `z-index` | `  z-index:20 !important;` |
| 48 | `grid-template` | `  grid-template-columns:minmax(0,1fr) auto !important;` |
| 54 | `border-radius` | `  border-radius:26px !important;` |
| 60 | `box-shadow` | `  box-shadow:0 22px 55px rgba(0,0,0,.28) !important;` |
| 65 | `grid-template` | `  grid-template-columns:52px 1fr !important;` |
| 73 | `border-radius` | `  border-radius:18px !important;` |
| 79 | `box-shadow` | `  box-shadow:inset 0 1px 0 rgba(255,255,255,.08) !important;` |
| 102 | `route-live` | `.route-live-row{` |
| 104 | `grid-template` | `  grid-template-columns:repeat(4,minmax(0,1fr)) !important;` |
| 109 | `route-live` | `.route-live-row .mini-chip{` |
| 113 | `border-radius` | `  border-radius:16px !important;` |
| 125 | `route-live` | `.route-live-row .mini-chip span{` |
| 129 | `route-live` | `.route-live-row .mini-chip b{` |
| 137 | `grid-template` | `  grid-template-columns:repeat(5,42px) !important;` |
| 148 | `border-radius` | `  border-radius:15px !important;` |
| 154 | `box-shadow` | `  box-shadow:0 10px 22px rgba(0,0,0,.22) !important;` |
| 164 | `grid-template` | `  grid-template-columns:repeat(2,minmax(0,1fr)) !important;` |
| 173 | `border-radius` | `  border-radius:19px !important;` |
| 179 | `box-shadow` | `  box-shadow:0 14px 30px rgba(0,0,0,.22) !important;` |
| 220 | `grid-template` | `  grid-template-columns:minmax(0,1fr) 380px !important;` |
| 227 | `border-radius` | `  border-radius:26px !important;` |
| 232 | `box-shadow` | `  box-shadow:0 22px 55px rgba(0,0,0,.28) !important;` |
| 257 | `bottom:` | `  bottom:auto !important;` |
| 264 | `grid-template` | `  grid-template-columns:92px minmax(0,1fr) minmax(0,1.2fr) !important;` |
| 271 | `z-index` | `  z-index:1 !important;` |
| 279 | `drive-speed` | `.drive-speed-chip,` |
| 280 | `drive-eta` | `.drive-eta-chip{` |
| 286 | `bottom:` | `  bottom:auto !important;` |
| 294 | `border-radius` | `  border-radius:16px !important;` |
| 298 | `box-shadow` | `  box-shadow:inset 0 1px 0 rgba(255,255,255,.07) !important;` |
| 321 | `drive-speed` | `.drive-speed-top,` |
| 322 | `drive-eta` | `.drive-eta-top{` |
| 336 | `drive-speed` | `.drive-speed-top b,` |
| 337 | `drive-eta` | `.drive-eta-top b{` |
| 344 | `drive-speed` | `.drive-speed-sub,` |
| 345 | `drive-eta` | `.drive-eta-sub{` |
| 359 | `board-head` | `.board-head{` |
| 361 | `grid-template` | `  grid-template-columns:1fr !important;` |
| 377 | `border-radius` | `  border-radius:999px !important;` |
| 399 | `selected-stop-chip` | `.selected-stop-chip{` |
| 403 | `border-radius` | `  border-radius:17px !important;` |
| 407 | `box-shadow` | `  box-shadow:inset 0 1px 0 rgba(255,255,255,.06) !important;` |
| 412 | `board-head` | `.board-head-right{` |
| 419 | `grid-template` | `  grid-template-columns:minmax(0,1fr) 84px !important;` |
| 424 | `voice-command-btn` | `.voice-command-btn,` |
| 428 | `border-radius` | `  border-radius:17px !important;` |
| 430 | `box-shadow` | `  box-shadow:inset 0 1px 0 rgba(255,255,255,.07) !important;` |
| 433 | `voice-command-btn` | `.voice-command-btn{` |
| 447 | `voice-command-btn` | `.voice-command-btn::before,` |
| 448 | `voice-command-btn` | `.voice-command-btn::after{` |
| 452 | `voice-command-btn` | `.voice-command-btn span{` |
| 469 | `legend` | `.legend{` |
| 471 | `grid-template` | `  grid-template-columns:repeat(3,minmax(0,1fr)) !important;` |
| 476 | `legend` | `.legend .mini-chip,` |
| 477 | `mini-chip` | `.mini-chip{` |
| 481 | `border-radius` | `  border-radius:14px !important;` |
| 497 | `route-strip` | `.route-strip-shell{` |
| 500 | `border-radius` | `  border-radius:21px !important;` |
| 503 | `box-shadow` | `  box-shadow:0 12px 26px rgba(0,0,0,.16) !important;` |
| 506 | `route-strip` | `.route-strip-head{` |
| 509 | `bottom:` | `  margin-bottom:8px !important;` |
| 512 | `route-strip` | `.route-strip-title{` |
| 518 | `route-strip` | `.route-strip-meta{` |
| 520 | `grid-template` | `  grid-template-columns:minmax(0,.9fr) minmax(0,1.25fr) 46px !important;` |
| 530 | `border-radius` | `  border-radius:15px !important;` |
| 556 | `border-radius` | `  border-radius:15px !important;` |
| 566 | `route-strip` | `.route-strip{` |
| 570 | `bottom:` | `  padding-bottom:2px !important;` |
| 574 | `route-strip` | `.route-strip::-webkit-scrollbar{` |
| 582 | `border-radius` | `  border-radius:17px !important;` |
| 598 | `border-radius` | `  border-radius:24px !important;` |
| 621 | `border-radius` | `  border-radius:20px !important;` |
| 622 | `box-shadow` | `  box-shadow:` |
| 634 | `bottom:` | `  bottom:10px !important;` |
| 641 | `border-radius` | `  border-radius:17px !important;` |
| 661 | `bottom:` | `  margin-bottom:9px !important;` |
| 662 | `bottom:` | `  padding-bottom:3px !important;` |
| 673 | `border-radius` | `  border-radius:14px !important;` |
| 687 | `border-radius` | `  border-radius:20px !important;` |
| 691 | `box-shadow` | `  box-shadow:0 10px 22px rgba(0,0,0,.12) !important;` |
| 735 | `border-radius` | `  border-radius:15px !important;` |
| 744 | `grid-template` | `    grid-template-columns:1fr !important;` |
| 759 | `grid-template` | `    grid-template-columns:1fr !important;` |
| 760 | `border-radius` | `    border-radius:23px !important;` |
| 770 | `route-live` | `  .route-live-row{` |
| 771 | `grid-template` | `    grid-template-columns:1fr 1fr !important;` |
| 775 | `grid-template` | `    grid-template-columns:1fr 1fr !important;` |
| 779 | `border-radius` | `    border-radius:22px !important;` |
| 786 | `grid-template` | `    grid-template-columns:82px minmax(0,1fr) minmax(0,1.05fr) !important;` |
| 798 | `route-strip` | `  .route-strip-meta{` |
| 799 | `grid-template` | `    grid-template-columns:minmax(0,.85fr) minmax(0,1.15fr) 42px !important;` |
| 830 | `grid-template` | `    grid-template-columns:minmax(0,1fr) 74px !important;` |
| 833 | `voice-command-btn` | `  .voice-command-btn span{` |
| 837 | `legend` | `  .legend{` |
| 838 | `grid-template` | `    grid-template-columns:repeat(3,minmax(0,1fr)) !important;` |
| 841 | `mini-chip` | `  .mini-chip{` |
| 853 | `border-radius` | `  border-radius:24px !important;` |
| 859 | `border-radius` | `  border-radius:16px !important;` |
| 864 | `grid-template` | `  grid-template-columns:46px 1fr !important;` |
| 876 | `route-live` | `.route-live-row{` |
| 881 | `route-live` | `.route-live-row .mini-chip{` |
| 883 | `border-radius` | `  border-radius:15px !important;` |
| 894 | `border-radius` | `  border-radius:18px !important;` |
| 905 | `grid-template` | `  grid-template-columns:180px minmax(0,1fr) !important;` |
| 906 | `bottom:` | `  margin-bottom:12px !important;` |
| 917 | `border-radius` | `  border-radius:18px !important;` |
| 922 | `drive-eta` | `.drive-eta-chip{` |
| 925 | `border-radius` | `  border-radius:18px !important;` |
| 938 | `selected-stop-chip` | `.selected-stop-chip{` |
| 947 | `grid-template` | `    grid-template-columns:180px minmax(0,1fr) !important;` |
| 954 | `route-live` | `  .route-live-row .mini-chip{` |
| 981 | `border-radius` | `  border-radius:999px;` |
| 1085 | `box-shadow` | `  box-shadow:` |
| 1116 | `box-shadow` | `  box-shadow:` |
| 1146 | `box-shadow` | `  box-shadow:` |
| 1176 | `box-shadow` | `  box-shadow:` |
| 1188 | `box-shadow` | `  box-shadow:` |
| 1318 | `box-shadow` | `  box-shadow:` |
| 1368 | `box-shadow` | `  box-shadow:` |
| 1384 | `box-shadow` | `  box-shadow:` |
| 1399 | `box-shadow` | `  box-shadow:` |
| 1449 | `box-shadow` | `  box-shadow:` |
| 1490 | `route-strip` | `.route-strip-meta{` |
| 1493 | `grid-template` | `  grid-template-columns:minmax(0,.9fr) minmax(0,1.25fr) 50px !important;` |
| 1509 | `grid-template` | `  grid-template-columns:10px auto minmax(0,1fr) !important;` |
| 1514 | `grid-template` | `  grid-template-columns:auto minmax(0,1fr) !important;` |
| 1522 | `border-radius` | `  border-radius:999px !important;` |
| 1525 | `box-shadow` | `  box-shadow:` |
| 1547 | `route-strip` | `.route-strip-meta .route-pill b{` |
| 1594 | `route-strip` | `body.drive-mode .route-strip:has(.route-stop.live-danger) ~ *,` |
| 1595 | `route-strip` | `body:not(.drive-mode) .route-strip:has(.route-stop.live-danger) ~ *{` |
| 1599 | `route-strip` | `.route-strip-shell:has(.route-stop.live-danger) .route-pill-live{` |
| 1604 | `box-shadow` | `  box-shadow:` |
| 1610 | `route-strip` | `.route-strip-shell:has(.route-stop.live-danger) .route-pill-live .route-mini-label,` |
| 1611 | `route-strip` | `.route-strip-shell:has(.route-stop.live-danger) .route-pill-live #routeMiniLive{` |
| 1618 | `route-strip` | `.route-strip-shell:has(.route-stop.live-danger) .route-mini-dot{` |
| 1620 | `box-shadow` | `  box-shadow:` |
| 1631 | `route-strip` | `.route-strip-shell:has(.route-stop.next-warning) .route-pill-next{` |
| 1636 | `box-shadow` | `  box-shadow:` |
| 1642 | `route-strip` | `.route-strip-shell:has(.route-stop.next-warning) .route-pill-next .route-mini-label,` |
| 1643 | `route-strip` | `.route-strip-shell:has(.route-stop.next-warning) .route-pill-next #routeMiniNext{` |
| 1656 | `legend` | `   DRIVE MODE LEGEND FIXED SINGLE FINAL` |
| 1661 | `legend` | `/* Normal modda legend gizli */` |
| 1662 | `legend` | `body:not(.drive-mode) .board-head-right .legend{` |
| 1666 | `legend` | `/* Sürüş modunda legend sabit alt bar */` |
| 1667 | `legend` | `body.drive-mode .board-head-right .legend{` |
| 1668 | `position:fixed` | `  position:fixed !important;` |
| 1672 | `bottom:` | `  bottom:calc(env(safe-area-inset-bottom, 0px) + 8px) !important;` |
| 1679 | `z-index` | `  z-index:99999 !important;` |
| 1682 | `grid-template` | `  grid-template-columns:repeat(6, minmax(0,1fr)) !important;` |
| 1689 | `border-radius` | `  border-radius:22px !important;` |
| 1694 | `box-shadow` | `  box-shadow:` |
| 1698 | `backdrop-filter` | `  backdrop-filter:blur(14px) !important;` |
| 1699 | `backdrop-filter` | `  -webkit-backdrop-filter:blur(14px) !important;` |
| 1702 | `legend` | `body.drive-mode .board-head-right .legend .mini-chip{` |
| 1709 | `border-radius` | `  border-radius:15px !important;` |
| 1717 | `box-shadow` | `  box-shadow:none !important;` |
| 1731 | `bottom:` | `  padding-bottom:82px !important;` |
| 1735 | `bottom:` | `  padding-bottom:82px !important;` |
| 1739 | `legend` | `  body.drive-mode .board-head-right .legend{` |
| 1741 | `bottom:` | `    bottom:calc(env(safe-area-inset-bottom, 0px) + 6px) !important;` |
| 1745 | `border-radius` | `    border-radius:20px !important;` |
| 1748 | `legend` | `  body.drive-mode .board-head-right .legend .mini-chip{` |
| 1757 | `bottom:` | `    padding-bottom:78px !important;` |
| 1762 | `legend` | `  body.drive-mode .board-head-right .legend .mini-chip{` |
| 1781 | `position:fixed` | `  position:fixed !important;` |
| 1785 | `bottom:` | `  bottom:auto !important;` |
| 1788 | `z-index` | `  z-index:99998 !important;` |
| 1796 | `border-radius` | `  border-radius:24px !important;` |
| 1809 | `box-shadow` | `  box-shadow:` |
| 1813 | `backdrop-filter` | `  backdrop-filter:blur(14px) !important;` |
| 1814 | `backdrop-filter` | `  -webkit-backdrop-filter:blur(14px) !important;` |
| 1824 | `border-radius` | `  border-radius:15px !important;` |
| 1842 | `box-shadow` | `  box-shadow:` |
| 1854 | `route-strip` | `body.drive-mode .route-strip-shell{` |
| 1864 | `border-radius` | `    border-radius:22px !important;` |
| 1872 | `border-radius` | `    border-radius:14px !important;` |
| 1876 | `route-strip` | `  body.drive-mode .route-strip-shell{` |
| 1899 | `bottom:` | `  bottom:auto !important;` |
| 1911 | `grid-template` | `  grid-template-columns:repeat(5, minmax(0, 1fr)) !important;` |
| 1916 | `border-radius` | `  border-radius:24px !important;` |
| 1922 | `box-shadow` | `  box-shadow:` |
| 1926 | `backdrop-filter` | `  backdrop-filter:blur(12px) !important;` |
| 1927 | `backdrop-filter` | `  -webkit-backdrop-filter:blur(12px) !important;` |
| 1929 | `z-index` | `  z-index:20 !important;` |
| 1939 | `border-radius` | `  border-radius:17px !important;` |
| 1957 | `box-shadow` | `  box-shadow:` |
| 1974 | `route-strip` | `body.drive-mode .route-strip-shell{` |
| 1984 | `border-radius` | `    border-radius:22px !important;` |
| 1990 | `border-radius` | `    border-radius:16px !important;` |
| 2001 | `board-head` | `.board-head-right .voice-row,` |
| 2002 | `board-head` | `body.drive-mode .board-head-right .voice-row,` |
| 2003 | `board-head` | `body:not(.drive-mode) .board-head-right .voice-row{` |
| 2007 | `grid-template` | `  grid-template-columns:minmax(0,1fr) minmax(120px,.78fr) !important;` |
| 2012 | `board-head` | `.board-head-right .voice-state{` |
| 2017 | `voice-command-btn` | `.board-head-right .voice-command-btn{` |
| 2023 | `border-radius` | `  border-radius:22px !important;` |
| 2037 | `box-shadow` | `  box-shadow:` |
| 2044 | `voice-command-btn` | `.board-head-right .voice-command-btn::before,` |
| 2045 | `voice-command-btn` | `.board-head-right .voice-command-btn::after{` |
| 2050 | `voice-command-btn` | `.board-head-right .voice-command-btn span{` |
| 2062 | `board-head` | `.board-head-right .voice-seat-mini{` |
| 2068 | `border-radius` | `  border-radius:22px !important;` |
| 2080 | `box-shadow` | `  box-shadow:` |
| 2088 | `board-head` | `.board-head-right .voice-seat-mini::before{` |
| 2094 | `border-radius` | `  border-radius:13px !important;` |
| 2101 | `box-shadow` | `  box-shadow:` |
| 2109 | `board-head` | `.board-head-right .voice-seat-mini::after{` |
| 2115 | `board-head` | `.board-head-right .voice-seat-mini span{` |
| 2123 | `board-head` | `.board-head-right .voice-seat-mini span:first-child::after{` |
| 2131 | `board-head` | `.board-head-right .voice-seat-mini b{` |
| 2139 | `board-head` | `.board-head-right .voice-seat-mini span:first-child b{` |
| 2143 | `board-head` | `.board-head-right .voice-seat-mini span:last-child b{` |
| 2148 | `board-head` | `  .board-head-right .voice-row,` |
| 2149 | `board-head` | `  body.drive-mode .board-head-right .voice-row,` |
| 2150 | `board-head` | `  body:not(.drive-mode) .board-head-right .voice-row{` |
| 2151 | `grid-template` | `    grid-template-columns:minmax(0,1fr) 116px !important;` |
| 2155 | `voice-command-btn` | `  .board-head-right .voice-command-btn,` |
| 2156 | `board-head` | `  .board-head-right .voice-seat-mini{` |
| 2159 | `border-radius` | `    border-radius:20px !important;` |

### `android_app/app/src/main/python/static/seats/patches/stop-selected-toast.css`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 2 | `position:fixed` | `    position:fixed;` |
| 4 | `bottom:` | `    bottom:calc(env(safe-area-inset-bottom, 0px) + 92px);` |
| 6 | `z-index` | `    z-index:2147483600;` |
| 23 | `border-radius` | `    border-radius:22px;` |
| 30 | `box-shadow` | `    box-shadow:0 18px 44px rgba(0,0,0,.42), inset 0 1px 0 rgba(255,255,255,.12);` |
| 31 | `backdrop-filter` | `    backdrop-filter:blur(16px);` |
| 32 | `backdrop-filter` | `    -webkit-backdrop-filter:blur(16px);` |
| 39 | `border-radius` | `    border-radius:16px;` |

### `android_app/app/src/main/python/static/seats/patches/bottom-voice-command.css`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 24 | `box-shadow` | `    box-shadow:0 14px 34px rgba(220,38,38,.30), inset 0 1px 0 rgba(255,255,255,.14) !important;` |

### `android_app/app/src/main/python/static/seats/patches/manual-ticket-system.css`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 14 | `bottom:` | `    bottom:-8px;` |
| 17 | `border-radius` | `    border-radius:999px;` |
| 28 | `box-shadow` | `    box-shadow:` |
| 31 | `z-index` | `    z-index:12;` |
| 41 | `bottom:` | `    bottom:-9px;` |
| 50 | `bottom:` | `      bottom:-7px;` |

### `android_app/app/src/main/python/static/seats/patches/top-sound-toggle.css`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 4 | `grid-template` | `    grid-template-columns:1fr auto;` |
| 19 | `border-radius` | `    border-radius:22px;` |
| 32 | `box-shadow` | `    box-shadow:0 14px 34px rgba(22,163,74,.22), inset 0 1px 0 rgba(255,255,255,.14);` |
| 40 | `box-shadow` | `    box-shadow:0 14px 34px rgba(15,23,42,.25), inset 0 1px 0 rgba(255,255,255,.10);` |
| 56 | `border-radius` | `      border-radius:19px;` |

### `android_app/app/src/main/python/static/seats/patches/stop-flow-focus-patch.css`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 8 | `position:fixed` | `    position:fixed;` |
| 10 | `z-index` | `    z-index:2147483000;` |
| 30 | `border-radius` | `    border-radius:28px;` |
| 32 | `box-shadow` | `    box-shadow:0 28px 80px rgba(0,0,0,.55), inset 0 1px 0 rgba(255,255,255,.08);` |
| 40 | `bottom:` | `    border-bottom:1px solid rgba(120,160,255,.18);` |
| 49 | `bottom:` | `    margin-bottom:14px;` |
| 54 | `border-radius` | `    border-radius:18px;` |
| 60 | `box-shadow` | `    box-shadow:0 12px 28px rgba(37,92,255,.28);` |
| 67 | `border-radius` | `    border-radius:999px;` |
| 106 | `border-radius` | `    border-radius:24px;` |
| 112 | `box-shadow` | `    box-shadow:0 16px 34px rgba(0,0,0,.26), inset 0 1px 0 rgba(255,255,255,.06);` |
| 125 | `box-shadow` | `    box-shadow:0 16px 38px rgba(18,214,96,.18), inset 0 1px 0 rgba(255,255,255,.10);` |
| 132 | `border-radius` | `    border-radius:17px;` |
| 165 | `border-radius` | `    border-radius:999px;` |

### `android_app/app/src/main/python/static/seats/patches/stop-flow-focus-patch.js`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 296 | `seat-simple-bottom-bar` | `      var parent = btn.closest(".seat-simple-bottom-bar, .seat-simple-dock, .seat-simple-nav");` |

### `android_app/app/src/main/python/static/seats/patches/seat-layout-fab-pack.css`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 102 | `bottom:` | `    bottom:auto !important;` |
| 103 | `z-index` | `    z-index:45 !important;` |
| 115 | `border-radius` | `    border-radius:16px !important;` |
| 117 | `box-shadow` | `    box-shadow:0 14px 28px rgba(0,0,0,.34) !important;` |
| 123 | `border-radius` | `    border-radius:16px !important;` |
| 136 | `border-radius` | `      border-radius:15px !important;` |
| 149 | `border-radius` | `    border-radius:24px !important;` |
| 156 | `box-shadow` | `    box-shadow:` |
| 161 | `backdrop-filter` | `    backdrop-filter:blur(14px) !important;` |
| 162 | `backdrop-filter` | `    -webkit-backdrop-filter:blur(14px) !important;` |
| 184 | `border-radius` | `    border-radius:18px !important;` |
| 190 | `box-shadow` | `    box-shadow:` |
| 200 | `border-radius` | `    border-radius:22px;` |
| 230 | `border-radius` | `      border-radius:22px !important;` |
| 236 | `border-radius` | `      border-radius:17px !important;` |
| 249 | `border-radius` | `    border-radius:21px !important;` |
| 264 | `border-radius` | `    border-radius:15px !important;` |
| 271 | `border-radius` | `    border-radius:18px !important;` |
| 278 | `border-radius` | `      border-radius:19px !important;` |
| 287 | `border-radius` | `      border-radius:14px !important;` |
| 310 | `bottom:` | `    bottom:auto !important;` |
| 328 | `border-radius` | `    border-radius:21px !important;` |
| 335 | `box-shadow` | `    box-shadow:` |
| 341 | `z-index` | `    z-index:90 !important;` |
| 368 | `border-radius` | `    border-radius:15px !important;` |
| 384 | `border-radius` | `    border-radius:18px !important;` |
| 396 | `border-radius` | `      border-radius:19px !important;` |
| 405 | `border-radius` | `      border-radius:14px !important;` |

### `android_app/app/src/main/python/static/seats/patches/seat-simple-ui-pack.css`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 10 | `z-index` | `  z-index:9999;` |
| 15 | `border-radius` | `  border-radius:18px;` |
| 18 | `box-shadow` | `  box-shadow:0 12px 28px rgba(37,99,235,.24), inset 0 1px 0 rgba(255,255,255,.16);` |
| 40 | `grid-template` | `  grid-template-columns:1fr !important;` |
| 63 | `legend` | `/* sağdaki ses/legend/kalabalık kontroller gizli */` |
| 64 | `board-head` | `html.seat-simple-mode .board-head-right,` |
| 66 | `drive-voice` | `html.seat-simple-mode .drive-voice-row,` |
| 67 | `legend` | `html.seat-simple-mode .legend{` |
| 72 | `board-head` | `html.seat-simple-mode .board-head{` |
| 93 | `selected-stop-chip` | `html.seat-simple-mode .selected-stop-chip{` |
| 98 | `border-radius` | `  border-radius:18px !important;` |
| 104 | `route-strip` | `html.seat-simple-mode .route-strip-shell,` |
| 124 | `border-radius` | `    border-radius:16px;` |
| 126 | `bottom:` | `    margin-bottom:8px;` |
| 149 | `border-radius` | `  border-radius:22px;` |
| 154 | `box-shadow` | `  box-shadow:` |
| 168 | `bottom:` | `  margin-bottom:10px;` |
| 187 | `border-radius` | `  border-radius:999px;` |
| 202 | `grid-template` | `  grid-template-columns:1.25fr .75fr .75fr;` |
| 209 | `border-radius` | `  border-radius:17px;` |
| 212 | `box-shadow` | `  box-shadow:inset 0 1px 0 rgba(255,255,255,.04);` |
| 218 | `bottom:` | `  margin-bottom:5px;` |
| 247 | `bottom:` | `  margin-bottom:10px !important;` |
| 253 | `border-radius` | `    border-radius:20px;` |
| 254 | `bottom:` | `    margin-bottom:10px;` |
| 262 | `grid-template` | `    grid-template-columns:1.15fr .85fr .85fr;` |
| 269 | `border-radius` | `    border-radius:15px;` |
| 281 | `seat-simple-bottom-bar` | `/* ===== seat-simple-bottom-bar-style ===== */` |
| 287 | `seat-simple-bottom-bar` | `.seat-simple-bottom-bar{` |
| 289 | `position:fixed` | `  position:fixed;` |
| 292 | `bottom:` | `  bottom:10px;` |
| 293 | `z-index` | `  z-index:99999;` |
| 295 | `border-radius` | `  border-radius:26px;` |
| 299 | `box-shadow` | `  box-shadow:` |
| 302 | `backdrop-filter` | `  backdrop-filter:blur(18px) saturate(1.1);` |
| 303 | `backdrop-filter` | `  -webkit-backdrop-filter:blur(18px) saturate(1.1);` |
| 304 | `grid-template` | `  grid-template-columns:repeat(5,1fr);` |
| 308 | `seat-simple-bottom-bar` | `html.seat-simple-mode .seat-simple-bottom-bar{` |
| 313 | `bottom:` | `  padding-bottom:92px !important;` |
| 318 | `border-radius` | `  border-radius:20px;` |
| 336 | `box-shadow` | `  box-shadow:inset 0 1px 0 rgba(255,255,255,.06);` |
| 368 | `seat-simple-bottom-bar` | `  .seat-simple-bottom-bar{` |
| 371 | `bottom:` | `    bottom:8px;` |
| 372 | `border-radius` | `    border-radius:24px;` |
| 379 | `border-radius` | `    border-radius:18px;` |
| 394 | `seat-simple-bottom-bar` | `html.seat-modal-open .seat-simple-bottom-bar,` |
| 395 | `seat-simple-bottom-bar` | `body.seat-modal-open .seat-simple-bottom-bar{` |

### `android_app/app/src/main/python/static/seats/patches/mobile-performance-fix.css`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 24 | `position:fixed` | `    position:fixed;` |
| 26 | `z-index` | `    z-index:-1;` |
| 35 | `backdrop-filter` | `    -webkit-backdrop-filter:none !important;` |
| 36 | `backdrop-filter` | `    backdrop-filter:none !important;` |
| 56 | `seat-simple-bottom-bar` | `  .seat-simple-bottom-bar,` |
| 62 | `box-shadow` | `    box-shadow:0 8px 18px rgba(0,0,0,.22) !important;` |
| 72 | `voice-command-btn` | `  .voice-command-btn,` |
| 73 | `drive-voice` | `  .drive-voice-btn,` |
| 75 | `drive-speed` | `  .drive-speed-chip,` |
| 76 | `drive-eta` | `  .drive-eta-chip{` |
| 77 | `box-shadow` | `    box-shadow:0 4px 10px rgba(0,0,0,.18) !important;` |
| 84 | `voice-command-btn` | `  .voice-command-btn,` |
| 85 | `drive-voice` | `  .drive-voice-btn,` |
| 86 | `drive-speed` | `  .drive-speed-chip,` |
| 87 | `drive-eta` | `  .drive-eta-chip,` |
| 106 | `voice-command-btn` | `  .voice-command-btn,` |
| 107 | `drive-voice` | `  .drive-voice-btn{` |
| 116 | `seat-simple-bottom-bar` | `  .seat-simple-bottom-bar,` |
| 145 | `backdrop-filter` | `    -webkit-backdrop-filter:none !important;` |
| 146 | `backdrop-filter` | `    backdrop-filter:none !important;` |
| 164 | `box-shadow` | `    box-shadow:0 18px 38px rgba(0,0,0,.42) !important;` |

### `android_app/app/src/main/python/static/seats/patches/stop-flow-compact-mobile.css`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 11 | `border-radius` | `    border-radius:22px !important;` |
| 19 | `bottom:` | `    margin-bottom:8px !important;` |
| 25 | `border-radius` | `    border-radius:15px !important;` |
| 58 | `border-radius` | `    border-radius:18px !important;` |
| 65 | `border-radius` | `    border-radius:14px !important;` |

### `android_app/app/src/main/python/static/seats/patches/fab-sheet-solid-fix.css`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 23 | `box-shadow` | `    box-shadow:0 22px 58px rgba(0,0,0,.58), inset 0 1px 0 rgba(255,255,255,.06) !important;` |
| 24 | `backdrop-filter` | `    -webkit-backdrop-filter:none !important;` |
| 25 | `backdrop-filter` | `    backdrop-filter:none !important;` |

### `android_app/app/src/main/python/static/seats/patches/seat-label-ghost-clean.css`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 21 | `box-shadow` | `    box-shadow:none !important;` |
| 30 | `box-shadow` | `    box-shadow:none !important;` |
| 32 | `backdrop-filter` | `    backdrop-filter:none !important;` |
| 33 | `backdrop-filter` | `    -webkit-backdrop-filter:none !important;` |

## 4) Kritik blok çevreleri

### `templates/seats.html` / `drive-mode-actions-independent-style`

| Satır | İçerik |
| ---: | --- |
| 370 | `<script src="/static/seats/voice-tts.js?v=voice-owner-fix-1"></script>` |
| 371 | `<script src="/static/seats/drive-eta-chip.js?v=1"></script>` |
| 372 | `<script src="/static/seats/drive-controls.js?v=drive-toggle-fix-1"></script>` |
| 373 | `<script src="/static/seats/patches/stop-selected-toast.js?v=1"></script>` |
| 374 | `<script src="/static/seats/patches/stop-flow-focus-patch.js?v=simple-scope-1"></script>` |
| 375 | `<script src="/static/seats/patches/seat-layout-fab-pack.js?v=1"></script>` |
| 376 | `<script src="/static/seats/patches/modal-bottom-nav-autohide.js?v=1"></script>` |
| 377 | `<script src="/static/seats/patches/manual-ticket-system.js?v=1"></script>` |
| 378 | `<script src="/static/seats/patches/top-sound-toggle.js?v=1"></script>` |
| 379 | `<script src="/static/seats/patches/seat-simple-ui-pack.js?v=1"></script>` |
| 380 | `<style id="drive-mode-actions-independent-style">` |
| 381 | `/* =========================================================` |
| 382 | `   SÜRÜŞ MODU ÜST HIZLI MENÜ - BAĞIMSIZ FINAL` |
| 383 | `   driveInlineDock içine girmez, kendi kendine görünür.` |
| 384 | `========================================================= */` |
| 385 | `` |
| 386 | `.board-inner{` |
| 387 | `  position:relative !important;` |
| 388 | `}` |
| 389 | `` |
| 390 | `#driveModeActionsDock{` |
| 391 | `  display:none;` |
| 392 | `  position:absolute;` |
| 393 | `  z-index:9999;` |
| 394 | `` |
| 395 | `  width:238px;` |
| 396 | `  height:50px;` |
| 397 | `  padding:7px;` |
| 398 | `` |
| 399 | `  border-radius:22px;` |
| 400 | `  background:rgba(5,15,28,.95);` |
| 401 | `  border:1px solid rgba(96,165,250,.28);` |
| 402 | `  box-shadow:` |
| 403 | `    inset 0 0 0 1px rgba(255,255,255,.05),` |
| 404 | `    0 16px 34px rgba(0,0,0,.38);` |
| 405 | `` |
| 406 | `  align-items:center;` |
| 407 | `  justify-content:center;` |
| 408 | `  gap:7px;` |

### `templates/seats.html` / `drive-mode-actions-independent-js`

| Satır | İçerik |
| ---: | --- |
| 455 | `    width:34px;` |
| 456 | `    height:34px;` |
| 457 | `    min-width:34px;` |
| 458 | `    min-height:34px;` |
| 459 | `    border-radius:13px;` |
| 460 | `    font-size:20px;` |
| 461 | `  }` |
| 462 | `}` |
| 463 | `</style>` |
| 464 | `` |
| 465 | `<script id="drive-mode-actions-independent-js">` |
| 466 | `(function(){` |
| 467 | `  function isDriveMode(){` |
| 468 | `    const btn = document.getElementById("driveModeToggle");` |
| 469 | `    const txt = (btn ? btn.textContent : "").toLowerCase();` |
| 470 | `` |
| 471 | `    // Sürüş modunda buton "Normal" oluyor` |
| 472 | `    if(txt.includes("normal")) return true;` |
| 473 | `` |
| 474 | `    const bodyCls = document.body.className.toLowerCase();` |
| 475 | `    const htmlCls = document.documentElement.className.toLowerCase();` |
| 476 | `` |
| 477 | `    return (` |
| 478 | `      bodyCls.includes("drive") \|\|` |
| 479 | `      bodyCls.includes("surus") \|\|` |
| 480 | `      htmlCls.includes("drive") \|\|` |
| 481 | `      htmlCls.includes("surus")` |
| 482 | `    );` |
| 483 | `  }` |
| 484 | `` |
| 485 | `  function ensureDock(){` |
| 486 | `    let dock = document.getElementById("driveModeActionsDock");` |
| 487 | `    if(dock) return dock;` |
| 488 | `` |
| 489 | `    dock = document.createElement("div");` |
| 490 | `    dock.id = "driveModeActionsDock";` |
| 491 | `    dock.innerHTML = '` |
| 492 | `      <a class="dma-btn" href="{{ url_for('index') }}" title="Ana Sayfa">🏠</a>` |
| 493 | `      <a class="dma-btn" href="{{ url_for('hesap_page') }}" title="Hesap">💵</a>` |

### `templates/seats.html` / `drive-mode-force-toggle-js`

| Satır | İçerik |
| ---: | --- |
| 830 | `  .drive-speed-sub,` |
| 831 | `  .drive-eta-sub{` |
| 832 | `    font-size:10px !important;` |
| 833 | `  }` |
| 834 | `}` |
| 835 | `</style>` |
| 836 | `` |
| 837 | `{% include "seats_parts/offload_confirm.html" %}` |
| 838 | `` |
| 839 | `<!-- DRIVE MODE FORCE TOGGLE START -->` |
| 840 | `<script id="drive-mode-force-toggle-js">` |
| 841 | `(function(){` |
| 842 | `  if(window.__driveModeForceToggleReady) return;` |
| 843 | `  window.__driveModeForceToggleReady = true;` |
| 844 | `` |
| 845 | `  function driveKey(){` |
| 846 | `    const boot = window.SEATS_BOOT \|\| {};` |
| 847 | `    const tripKey = boot.tripKey \|\| window.TRIP_KEY \|\| window.BAG_TRIP \|\| "default";` |
| 848 | `    return "driveMode:" + tripKey;` |
| 849 | `  }` |
| 850 | `` |
| 851 | `  function isDriveOn(){` |
| 852 | `    try{` |
| 853 | `      return localStorage.getItem(driveKey()) === "1";` |
| 854 | `    }catch(e){` |
| 855 | `      return false;` |
| 856 | `    }` |
| 857 | `  }` |
| 858 | `` |
| 859 | `  function setDrive(on){` |
| 860 | `    try{` |
| 861 | `      localStorage.setItem(driveKey(), on ? "1" : "0");` |
| 862 | `    }catch(e){}` |
| 863 | `` |
| 864 | `    document.body.classList.toggle("drive-mode", !!on);` |
| 865 | `    document.documentElement.classList.toggle("drive-mode", !!on);` |
| 866 | `` |
| 867 | `    const btn = document.getElementById("driveModeToggle");` |
| 868 | `    if(btn){` |

### `templates/seats.html` / `seat-simple-bottom-bar-script`

| Satır | İçerik |
| ---: | --- |
| 1101 | `` |
| 1102 | `  if(document.readyState === "loading"){` |
| 1103 | `    document.addEventListener("DOMContentLoaded", boot);` |
| 1104 | `  }else{` |
| 1105 | `    boot();` |
| 1106 | `  }` |
| 1107 | `})();` |
| 1108 | `</script>` |
| 1109 | `<!-- DRIVE VOICE MIRROR SCRIPT END -->` |
| 1110 | `` |
| 1111 | `<script id="seat-simple-bottom-bar-script">` |
| 1112 | `(function(){` |
| 1113 | `  if(window.__seatSimpleBottomBarReady) return;` |
| 1114 | `  window.__seatSimpleBottomBarReady = true;` |
| 1115 | `` |
| 1116 | `  function q(sel){` |
| 1117 | `    return document.querySelector(sel);` |
| 1118 | `  }` |
| 1119 | `` |
| 1120 | `  function setAdvanced(){` |
| 1121 | `    try{` |
| 1122 | `      const boot = window.SEATS_BOOT \|\| {};` |
| 1123 | `      const tripKey = boot.tripKey \|\| window.TRIP_KEY \|\| window.BAG_TRIP \|\| "default";` |
| 1124 | `      localStorage.setItem("seatUiMode:" + tripKey, "advanced");` |
| 1125 | `    }catch(_){}` |
| 1126 | `` |
| 1127 | `    document.documentElement.classList.remove("seat-simple-mode");` |
| 1128 | `    document.body.classList.remove("seat-simple-mode");` |
| 1129 | `` |
| 1130 | `    try{` |
| 1131 | `      const btn = document.getElementById("seatSimpleModeToggle");` |
| 1132 | `      if(btn) btn.innerHTML = "💺 Sade koltuk moduna dön";` |
| 1133 | `    }catch(_){}` |
| 1134 | `` |
| 1135 | `    try{ if(typeof renderRouteStrip === "function") renderRouteStrip(); }catch(_){}` |
| 1136 | `    try{ if(typeof updateCompactHeader === "function") updateCompactHeader(); }catch(_){}` |
| 1137 | `  }` |
| 1138 | `` |
| 1139 | `  function openVoice(){` |

### `templates/seats_parts/route_flow.html` / `Durak`

| Satır | İçerik |
| ---: | --- |
| 1 | `<div class="route-strip-shell">` |
| 2 | `  <div class="route-strip-head">` |
| 3 | `    <div class="route-strip-title">Durak Akışı</div>` |
| 4 | `` |
| 5 | `    <div class="route-strip-meta">` |
| 6 | `      <div class="route-pill route-pill-live">` |
| 7 | `        <span class="route-mini-dot"></span>` |
| 8 | `        <span class="route-mini-label">Canlı:</span>` |
| 9 | `        <span class="route-name-window">` |
| 10 | `          <b id="routeMiniLive">—</b>` |
| 11 | `        </span>` |
| 12 | `      </div>` |
| 13 | `` |
| 14 | `      <div class="route-pill route-pill-next">` |
| 15 | `        <span class="route-mini-label">Sıradaki:</span>` |
| 16 | `        <span class="route-name-window">` |
| 17 | `          <b id="routeMiniNext">—</b>` |
| 18 | `        </span>` |
| 19 | `      </div>` |
| 20 | `` |
| 21 | `      <button id="nightVoiceToggle" class="night-voice-toggle" type="button" title="Sesli robot">🔊 Ses Açık</button>` |
| 22 | `    </div>` |
| 23 | `  </div>` |
| 24 | `` |
| 25 | `  <div class="route-strip" id="routeStrip">` |
| 26 | `    <div class="route-stop active">` |
| 27 | `      <div class="name">Rota hazırlanıyor</div>` |
| 28 | `      <div class="meta">Duraklar yüklenecek</div>` |
| 29 | `    </div>` |
| 30 | `  </div>` |
| 31 | `</div>` |

### `templates/seats_parts/topbar.html` / `driveModeToggle`

_Bulunamadı._

### `templates/seats_parts/deck.html` / `legend`

_Bulunamadı._

### `static/seats/seats-final.css` / `DRIVE MODE LEGEND`

| Satır | İçerik |
| ---: | --- |
| 1646 | `    0 0 8px rgba(251,191,36,.70),` |
| 1647 | `    0 0 18px rgba(245,158,11,.38) !important;` |
| 1648 | `}` |
| 1649 | `` |
| 1650 | `` |
| 1651 | `` |
| 1652 | `` |
| 1653 | `` |
| 1654 | `` |
| 1655 | `/* =========================================================` |
| 1656 | `   DRIVE MODE LEGEND FIXED SINGLE FINAL` |
| 1657 | `   Sürüş modunda Boş/Bay/Bayan/Bagaj/İniş/Servis barı` |
| 1658 | `   ekranın en altında sabit kalır.` |
| 1659 | `========================================================= */` |
| 1660 | `` |
| 1661 | `/* Normal modda legend gizli */` |
| 1662 | `body:not(.drive-mode) .board-head-right .legend{` |
| 1663 | `  display:none !important;` |
| 1664 | `}` |
| 1665 | `` |
| 1666 | `/* Sürüş modunda legend sabit alt bar */` |
| 1667 | `body.drive-mode .board-head-right .legend{` |
| 1668 | `  position:fixed !important;` |
| 1669 | `  left:50% !important;` |
| 1670 | `  right:auto !important;` |
| 1671 | `  top:auto !important;` |
| 1672 | `  bottom:calc(env(safe-area-inset-bottom, 0px) + 8px) !important;` |
| 1673 | `  transform:translateX(-50%) !important;` |
| 1674 | `` |
| 1675 | `  width:calc(100vw - 22px) !important;` |
| 1676 | `  max-width:720px !important;` |
| 1677 | `  min-height:58px !important;` |
| 1678 | `` |
| 1679 | `  z-index:99999 !important;` |
| 1680 | `` |
| 1681 | `  display:grid !important;` |
| 1682 | `  grid-template-columns:repeat(6, minmax(0,1fr)) !important;` |
| 1683 | `  align-items:center !important;` |
| 1684 | `  gap:7px !important;` |

### `static/seats/seats.css` / `SÜRÜŞ / HIZ`

_Bulunamadı._

### `static/seats/seats.css` / `SÜRÜŞ MODU ALT`

| Satır | İçerik |
| ---: | --- |
| 2553 | `  margin-bottom:18px !important;` |
| 2554 | `}` |
| 2555 | `` |
| 2556 | `/* Normal modda da aynı düzgünlük istenirse */` |
| 2557 | `.corr{` |
| 2558 | `  grid-row:1 / 14;` |
| 2559 | `}` |
| 2560 | `` |
| 2561 | `` |
| 2562 | `/* =========================================================` |
| 2563 | `   SÜRÜŞ MODU ALT HIZLI İŞLEM BARI` |
| 2564 | `   Sağ alttaki + ₺ ⇩ butonlarını alta yatay dizer` |
| 2565 | `========================================================= */` |
| 2566 | `` |
| 2567 | `/* Alt bar için koltuk planının altında yer aç */` |
| 2568 | `` |
| 2569 | `/* Deck içinde butonlara alt boşluk bırak */` |
| 2570 | `` |
| 2571 | `/* Sağdaki dikey FAB kolonunu sürüş modunda yatay alt bara çevir */` |
| 2572 | `body.drive-mode .fab-column{` |
| 2573 | `  position:absolute !important;` |
| 2574 | `  left:50% !important;` |
| 2575 | `  right:auto !important;` |
| 2576 | `  bottom:14px !important;` |
| 2577 | `  transform:translateX(-50%) !important;` |
| 2578 | `` |
| 2579 | `  display:flex !important;` |
| 2580 | `  flex-direction:row !important;` |
| 2581 | `  align-items:center !important;` |
| 2582 | `  justify-content:center !important;` |
| 2583 | `  gap:14px !important;` |
| 2584 | `` |
| 2585 | `  width:auto !important;` |
| 2586 | `  padding:10px 14px !important;` |
| 2587 | `  border-radius:26px !important;` |
| 2588 | `` |
| 2589 | `  background:linear-gradient(180deg, rgba(15,23,42,.88), rgba(2,6,23,.88));` |
| 2590 | `  border:1px solid rgba(255,255,255,.12);` |
| 2591 | `  box-shadow:` |

## 5) Patron ilk karar notu

- Bu ekran iOS tarzına çevrilecekse çekirdek mantığa dokunmadan, sadece görünüm ve yerleşim katmanı yapılmalı.
- Öncelik: üstte tek cam sefer kapsülü, ortada tek sesli komut aksiyonu, durak akışında sade timeline, altta temiz legend/toolbar.
- Mevcut fonksiyonlar korunmalı: sürüş/normal geçişi, sessiz/sesli durum, hız/ETA, seçili durak, sesli komut, durak akışı.
- Uygulama aşamasında öneri: `ios-drive-panel-v1.css` ve gerekirse küçük `ios-drive-panel-v1.js` yaması. Ana dosyaları parça parça bozmayacağız.