# Muavin Hızlı İşlem FAB Kaynak Audit V21

- Tarih: `20260608-181859`
- Bu rapor sadece tespittir. Dosya değiştirmez.

## 1) Aktif seats.html link/include kontrolü

### `templates/seats.html`

| Satır | İçerik |
| ---: | --- |
| 10 | `<link rel="stylesheet" href="/static/seats/patches/seat-layout-fab-pack.css?v=1">` |
| 17 | `<link rel="stylesheet" href="/static/seats/patches/fab-sheet-solid-fix.css?v=1">` |
| 20 | `  {% include "seats_parts/topbar.html" %}` |
| 21 | `  {# {% include "seats_parts/stats.html" %} #}` |
| 52 | `            <small>Tek ekrandan yolcu, durak, iniş ve hızlı işlemleri yönet.</small>` |
| 97 | `        {% include "seats_parts/route_flow.html" %}` |
| 98 | `        {% include "seats_parts/deck.html" %}` |
| 110 | `        <button class="tab-btn" type="button" data-tab="quick">İşlem</button>` |
| 283 | `      <div class="tab-pane" data-pane="quick">` |
| 287 | `              <h3>Hızlı İşlemler</h3>` |
| 292 | `              <button class="btn primary" type="button" id="fabBulkPane">Toplu Giriş</button>` |
| 293 | `              <button class="btn green" type="button" id="fabCashPane">Hızlı Tahsilat</button>` |
| 302 | `              <small id="quickStandingMeta">0 kişi</small>` |
| 304 | `            <div class="standing-list" id="quickStandingList"></div>` |
| 335 | `{% include "seats_parts/modals.html" %}` |
| 374 | `<script src="/static/seats/patches/seat-layout-fab-pack.js?v=1"></script>` |
| 627 | `{% include "seats_parts/finish_trip_modal.html" %}` |
| 836 | `{% include "seats_parts/offload_confirm.html" %}` |

### `android_app/app/src/main/python/templates/seats.html`

| Satır | İçerik |
| ---: | --- |
| 10 | `<link rel="stylesheet" href="/static/seats/patches/seat-layout-fab-pack.css?v=1">` |
| 17 | `<link rel="stylesheet" href="/static/seats/patches/fab-sheet-solid-fix.css?v=1">` |
| 20 | `  {% include "seats_parts/topbar.html" %}` |
| 21 | `  {# {% include "seats_parts/stats.html" %} #}` |
| 52 | `            <small>Tek ekrandan yolcu, durak, iniş ve hızlı işlemleri yönet.</small>` |
| 97 | `        {% include "seats_parts/route_flow.html" %}` |
| 98 | `        {% include "seats_parts/deck.html" %}` |
| 110 | `        <button class="tab-btn" type="button" data-tab="quick">İşlem</button>` |
| 283 | `      <div class="tab-pane" data-pane="quick">` |
| 287 | `              <h3>Hızlı İşlemler</h3>` |
| 292 | `              <button class="btn primary" type="button" id="fabBulkPane">Toplu Giriş</button>` |
| 293 | `              <button class="btn green" type="button" id="fabCashPane">Hızlı Tahsilat</button>` |
| 302 | `              <small id="quickStandingMeta">0 kişi</small>` |
| 304 | `            <div class="standing-list" id="quickStandingList"></div>` |
| 335 | `{% include "seats_parts/modals.html" %}` |
| 374 | `<script src="/static/seats/patches/seat-layout-fab-pack.js?v=1"></script>` |
| 627 | `{% include "seats_parts/finish_trip_modal.html" %}` |
| 836 | `{% include "seats_parts/offload_confirm.html" %}` |

## 2) FAB / hızlı işlem kaynak izleri

### `templates/consignments.html`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 775 | `Hızlı` | `      Fotoğrafları “Görüntüle / Yükle” ile yönet. Durumu butonlardan hızlıca güncelleyebilirsin.` |

### `templates/hesap.html`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 1405 | `HIZLI` | `    /* === HIZLI ISLEM PREMIUM \| START === */` |
| 1649 | `HIZLI` | `    /* === HIZLI ISLEM PREMIUM \| END === */` |
| 1963 | `Hızlı` | `        <div class="quick-action-title"><span class="spark">⚡</span> Hızlı İşlem</div>` |
| 1967 | `Hızlı` | `      <div class="tabs" role="tablist" aria-label="Hızlı işlem sekmeleri">` |
| 2067 | `Hızlı` | `        <span class="muted2">Virgülle ayır • hızlı düzenle</span>` |

### `templates/home.html`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 35 | `HIZLI` | `       <b>HIZLI KOLTUK</b><br><small>Koltuk ekranına git</small>` |

### `templates/index.html`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 1126 | `HIZLI` | `          <div class="menu-title">HIZLI KOLTUK</div>` |
| 1190 | `Hızlı` | `          <div class="menu-desc">Uygulama kullanımı / sesli komutlar / hızlı yardım</div>` |

### `templates/passenger_control.html`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 1066 | `Hızlı` | `   Amaç: Koltuk planını hızlı göstermek` |

### `templates/seats.html`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 10 | `seat-layout-fab-pack` | `<link rel="stylesheet" href="/static/seats/patches/seat-layout-fab-pack.css?v=1">` |
| 52 | `Hızlı` | `            <small>Tek ekrandan yolcu, durak, iniş ve hızlı işlemleri yönet.</small>` |
| 287 | `Hızlı` | `              <h3>Hızlı İşlemler</h3>` |
| 292 | `id="fab` | `              <button class="btn primary" type="button" id="fabBulkPane">Toplu Giriş</button>` |
| 293 | `id="fab` | `              <button class="btn green" type="button" id="fabCashPane">Hızlı Tahsilat</button>` |
| 294 | `Ayakta Listesi` | `              <button class="btn ghost" type="button" id="openStandingModalBtn">Ayakta Listesi</button>` |
| 374 | `seat-layout-fab-pack` | `<script src="/static/seats/patches/seat-layout-fab-pack.js?v=1"></script>` |
| 381 | `HIZLI` | `   SÜRÜŞ MODU ÜST HIZLI MENÜ - BAĞIMSIZ FINAL` |

### `templates/ai_console.html`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 1372 | `Hızlı` | `            <h3 class="h">⚡ Hızlı mantık</h3>` |

### `templates/trip_report.html`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 1108 | `Hızlı` | `      <p>Biten sefer raporlarına buradan hızlıca ulaş.</p>` |

### `templates/rehber.html`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 2334 | `Hızlı` | `          <p>Seçili, canlı ve sıradaki durak bilgisi sahada hızlı karar aldırır.</p>` |
| 2365 | `Hızlı` | `              Sade tasarım ve net bilgi akışı sayesinde muavin, sahada ihtiyaç duyduğu kontrolü daha hızlı sağlar.` |
| 2383 | `Hızlı` | `              <b>Hızlı</b>` |
| 2544 | `Toplu Giriş` | `              <div class="guide-line"><b>Toplu giriş</b><span>Birden fazla boş koltuğu seç, toplu giriş ekranını aç, bilgileri tek seferde işle.</span></div>` |
| 2557 | `Hızlı` | `                <div class="guide-card-sub">Sürüş modu daha sade, daha hızlı ve sahaya uygun görünüm sunar.</div>` |
| 2563 | `Hızlı` | `              <div class="guide-line"><b>Sesli komut butonu</b><span>Sürüş modunda büyük mor buton üzerinden hızlı sesli komut kullanılabilir.</span></div>` |
| 2565 | `Hızlı` | `              <div class="guide-line"><b>Canlı durak ve sıradaki durak</b><span>Durak akışı kutuları ile aktif nokta ve yaklaşan nokta hızlıca takip edilir.</span></div>` |
| 2575 | `Hızlı` | `                <div class="guide-card-sub">Sık karşılaşılan durumlar için hızlı çözüm notları.</div>` |

### `templates/seats_parts/modals.html`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 78 | `Toplu Giriş` | `  <h3>Toplu Giriş</h3>` |
| 123 | `Hızlı` | `  <h3>Hızlı Tahsilat (Ayakta)</h3>` |

### `templates/seats_parts/deck.html`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 23 | `fab-column` | `            <div class="fab-column" aria-label="Hızlı işlemler">` |
| 24 | `class="fab` | `              <button class="fab primary" id="fabBulk" type="button" title="Toplu Giriş">＋</button>` |
| 25 | `class="fab` | `              <button class="fab green" id="fabCash" type="button" title="Hızlı Tahsilat">₺</button>` |
| 26 | `class="fab` | `              <button class="fab orange" id="btnOffloadNow" type="button" title="İndir">⇩</button>` |

### `static/seats/seats.css`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 730 | `fab-column` | `  .fab-column{` |
| 1377 | `fab-column` | `    .fab-column{` |
| 1523 | `fab-column` | `    .fab-column{` |
| 2250 | `Hızlı` | `/* Sağdaki hızlı butonlar koltukların üstüne fazla binmesin */` |
| 2251 | `fab-column` | `body.drive-mode .fab-column{` |
| 2563 | `HIZLI` | `   SÜRÜŞ MODU ALT HIZLI İŞLEM BARI` |
| 2572 | `fab-column` | `body.drive-mode .fab-column{` |
| 2629 | `fab-column` | `  body.drive-mode .fab-column{` |
| 2675 | `Hızlı` | `/* Alt hızlı işlem barını 51-54 satırına daha yakın taşı */` |
| 2676 | `fab-column` | `body.drive-mode .fab-column{` |
| 2703 | `fab-column` | `  body.drive-mode .fab-column{` |

### `static/seats/seats.js`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 1690 | `Toplu Giriş` | `      toast(e.message \|\| "Toplu giriş hatası");` |
| 2720 | `fabBulk` | `  onClick("#fabBulk", openBulk);` |
| 2721 | `fabBulk` | `  onClick("#fabBulkPane", openBulk);` |
| 2727 | `fabCash` | `  onClick("#fabCash", openCash);` |
| 2728 | `fabCash` | `  onClick("#fabCashPane", openCash);` |
| 2734 | `openStandingModalBtn` | `  onClick("#openStandingModalBtn", openStandingModal);` |

### `static/seats/drive-controls.js`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 3 | `HIZLI` | `   HIZLI KOLTUK → OTOMATİK SÜRÜŞ MODU` |
| 33 | `Hızlı` | `    console.warn("Hızlı koltuk sürüş modu açılamadı:", e);` |

### `static/seats/voice-commands.js`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 848 | `Toplu Giriş` | `  toast("Toplu giriş formu hazırlandı");` |
| 849 | `Toplu Giriş` | `  speak("Toplu giriş formu açıldı.");` |

### `static/seats/standing.js`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 3 | `Hızlı` | `   Ayakta yolcu + hızlı tahsilat + ayakta liste` |

### `static/seats/seats-final.css`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 632 | `fab-column` | `.fab-column{` |

### `static/live_map/muavin_live_map_extra.js`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 1055 | `class="fab` | `      toolsFab.innerHTML = '<span class="fab-icon">⚙️</span><span class="fab-text">Araçlar</span>';` |

### `static/seats/patches/modal-bottom-nav-autohide.js`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 26 | `Toplu Giriş` | `      (t.includes("toplu giriş") \|\| t.includes("toplu giris")) &&` |
| 33 | `HIZLI` | `      (t.includes("hızlı tahsilat") \|\| t.includes("hizli tahsilat")) &&` |

### `static/seats/patches/seat-layout-fab-pack.css`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 92 | `FAB_LEFT_GAP_MOVE` | `/* ===== FAB_LEFT_GAP_MOVE ===== */` |
| 94 | `Hızlı` | `    Hızlı işlem butonlarını sağ alttan alıp` |
| 99 | `fab-column` | `  .fab-column.fab-left-gap-moved{` |
| 112 | `fab-column` | `  .fab-column.fab-left-gap-moved .fab{` |
| 120 | `fab-column` | `  body.drive-mode .fab-column.fab-left-gap-moved .fab{` |
| 128 | `fab-column` | `    .fab-column.fab-left-gap-moved{` |
| 132 | `fab-column` | `    .fab-column.fab-left-gap-moved .fab,` |
| 133 | `fab-column` | `    body.drive-mode .fab-column.fab-left-gap-moved .fab{` |
| 143 | `Hızlı` | `    Sol boş alana taşınan hızlı işlem butonlarını` |
| 147 | `fab-column` | `  .fab-column.fab-left-gap-moved{` |
| 165 | `fab-column` | `  .fab-column.fab-left-gap-moved::before{` |
| 166 | `HIZLI` | `    content:"HIZLI";` |
| 180 | `fab-column` | `  .fab-column.fab-left-gap-moved .fab{` |
| 196 | `fab-column` | `  .fab-column.fab-left-gap-moved .fab::after{` |
| 205 | `fab-column` | `  .fab-column.fab-left-gap-moved .fab.primary{` |
| 211 | `fab-column` | `  .fab-column.fab-left-gap-moved .fab.green{` |
| 217 | `fab-column` | `  .fab-column.fab-left-gap-moved .fab.orange{` |
| 223 | `fab-column` | `  .fab-column.fab-left-gap-moved .fab:active{` |
| 228 | `fab-column` | `    .fab-column.fab-left-gap-moved{` |
| 233 | `fab-column` | `    .fab-column.fab-left-gap-moved .fab{` |
| 242 | `Hızlı` | `    Hızlı işlem paneli 43 ile 51 arasına tam otursun diye` |
| 246 | `fab-column` | `  .fab-column.fab-left-gap-moved{` |
| 252 | `fab-column` | `  .fab-column.fab-left-gap-moved::before{` |
| 258 | `fab-column` | `  .fab-column.fab-left-gap-moved .fab,` |
| 259 | `fab-column` | `  body.drive-mode .fab-column.fab-left-gap-moved .fab{` |
| 269 | `fab-column` | `  .fab-column.fab-left-gap-moved .fab::after{` |
| 275 | `fab-column` | `    .fab-column.fab-left-gap-moved{` |
| 281 | `fab-column` | `    .fab-column.fab-left-gap-moved .fab,` |
| 282 | `fab-column` | `    body.drive-mode .fab-column.fab-left-gap-moved .fab{` |
| 295 | `fab-column` | `    static/seats/seats.css içindeki body.drive-mode .fab-column kuralı` |
| 296 | `Hızlı` | `    hızlı işlem panelini yatay alt bar gibi zorluyordu.` |
| 299 | `fab-left-gap-moved` | `    .fab-left-gap-moved sınıfı varsa, drive-mode kurallarını ezip` |
| 303 | `fab-column` | `  .fab-column.fab-left-gap-moved,` |
| 304 | `fab-column` | `  body.drive-mode .fab-column.fab-left-gap-moved{` |
| 344 | `fab-column` | `  .fab-column.fab-left-gap-moved::before,` |
| 345 | `fab-column` | `  body.drive-mode .fab-column.fab-left-gap-moved::before{` |
| 346 | `HIZLI` | `    content:"HIZLI" !important;` |
| 361 | `fab-column` | `  .fab-column.fab-left-gap-moved .fab,` |
| 362 | `fab-column` | `  body.drive-mode .fab-column.fab-left-gap-moved .fab{` |
| 381 | `fab-column` | `  .fab-column.fab-left-gap-moved .fab::after,` |
| 382 | `fab-column` | `  body.drive-mode .fab-column.fab-left-gap-moved .fab::after{` |
| 388 | `fab-column` | `    .fab-column.fab-left-gap-moved,` |
| 389 | `fab-column` | `    body.drive-mode .fab-column.fab-left-gap-moved{` |
| 399 | `fab-column` | `    .fab-column.fab-left-gap-moved .fab,` |
| 400 | `fab-column` | `    body.drive-mode .fab-column.fab-left-gap-moved .fab{` |

### `static/seats/patches/seat-layout-fab-pack.js`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 1 | `FAB_LEFT_GAP_MOVE` | `/* ===== FAB_LEFT_GAP_MOVE ===== */` |
| 11 | `fab-column` | `    var col = q(".fab-column");` |
| 18 | `fab-left-gap-moved` | `    col.classList.add("fab-left-gap-moved");` |
| 110 | `fab-column` | `    var col = q(".fab-column");` |
| 117 | `fab-left-gap-moved` | `    col.classList.add("fab-left-gap-moved");` |

### `static/seats/patches/seat-simple-ui-pack.css`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 283 | `HIZLI` | `   SADE MOD ALT HIZLI BAR` |

### `static/seats/patches/mobile-performance-fix.css`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 59 | `fab-column` | `  .fab-column,` |
| 60 | `fab-column` | `  .fab-column.fab-left-gap-moved,` |
| 98 | `Hızlı` | `  /* Geçişleri kısalt: his olarak hızlı, yük olarak hafif */` |
| 117 | `fab-column` | `  .fab-column,` |

### `static/seats/patches/fab-sheet-solid-fix.css`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 3 | `Hızlı` | `   Toplu Giriş / Hızlı Tahsilat / Ayakta Listesi modallarının` |
| 55 | `Hızlı` | `  /* Modal açıkken sol hızlı butonlar arkada çok bağırmasın */` |
| 56 | `fab-column` | `  body:has(#bulkModal[style*="display: block"]) .fab-column,` |
| 57 | `fab-column` | `  body:has(#cashModal[style*="display: block"]) .fab-column,` |
| 58 | `fab-column` | `  body:has(#standingModal[style*="display: block"]) .fab-column,` |
| 59 | `fab-column` | `  body:has(#approachModal[style*="display: block"]) .fab-column{` |

### `static/seats/_archive_theme_trials/seats-dashboard-final.css`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 470 | `fab-column` | `.fab-column{` |

### `android_app/app/src/main/python/templates/consignments.html`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 775 | `Hızlı` | `      Fotoğrafları “Görüntüle / Yükle” ile yönet. Durumu butonlardan hızlıca güncelleyebilirsin.` |

### `android_app/app/src/main/python/templates/hesap.html`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 1405 | `HIZLI` | `    /* === HIZLI ISLEM PREMIUM \| START === */` |
| 1649 | `HIZLI` | `    /* === HIZLI ISLEM PREMIUM \| END === */` |
| 1963 | `Hızlı` | `        <div class="quick-action-title"><span class="spark">⚡</span> Hızlı İşlem</div>` |
| 1967 | `Hızlı` | `      <div class="tabs" role="tablist" aria-label="Hızlı işlem sekmeleri">` |
| 2067 | `Hızlı` | `        <span class="muted2">Virgülle ayır • hızlı düzenle</span>` |

### `android_app/app/src/main/python/templates/home.html`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 35 | `HIZLI` | `       <b>HIZLI KOLTUK</b><br><small>Koltuk ekranına git</small>` |

### `android_app/app/src/main/python/templates/index.html`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 1032 | `HIZLI` | `          <div class="menu-title">HIZLI KOLTUK</div>` |
| 1096 | `Hızlı` | `          <div class="menu-desc">Uygulama kullanımı / sesli komutlar / hızlı yardım</div>` |

### `android_app/app/src/main/python/templates/passenger_control.html`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 1066 | `Hızlı` | `   Amaç: Koltuk planını hızlı göstermek` |

### `android_app/app/src/main/python/templates/seats.html`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 10 | `seat-layout-fab-pack` | `<link rel="stylesheet" href="/static/seats/patches/seat-layout-fab-pack.css?v=1">` |
| 52 | `Hızlı` | `            <small>Tek ekrandan yolcu, durak, iniş ve hızlı işlemleri yönet.</small>` |
| 287 | `Hızlı` | `              <h3>Hızlı İşlemler</h3>` |
| 292 | `id="fab` | `              <button class="btn primary" type="button" id="fabBulkPane">Toplu Giriş</button>` |
| 293 | `id="fab` | `              <button class="btn green" type="button" id="fabCashPane">Hızlı Tahsilat</button>` |
| 294 | `Ayakta Listesi` | `              <button class="btn ghost" type="button" id="openStandingModalBtn">Ayakta Listesi</button>` |
| 374 | `seat-layout-fab-pack` | `<script src="/static/seats/patches/seat-layout-fab-pack.js?v=1"></script>` |
| 381 | `HIZLI` | `   SÜRÜŞ MODU ÜST HIZLI MENÜ - BAĞIMSIZ FINAL` |

### `android_app/app/src/main/python/templates/ai_console.html`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 1372 | `Hızlı` | `            <h3 class="h">⚡ Hızlı mantık</h3>` |

### `android_app/app/src/main/python/templates/trip_report.html`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 1108 | `Hızlı` | `      <p>Biten sefer raporlarına buradan hızlıca ulaş.</p>` |

### `android_app/app/src/main/python/templates/rehber.html`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 2334 | `Hızlı` | `          <p>Seçili, canlı ve sıradaki durak bilgisi sahada hızlı karar aldırır.</p>` |
| 2365 | `Hızlı` | `              Sade tasarım ve net bilgi akışı sayesinde muavin, sahada ihtiyaç duyduğu kontrolü daha hızlı sağlar.` |
| 2383 | `Hızlı` | `              <b>Hızlı</b>` |
| 2544 | `Toplu Giriş` | `              <div class="guide-line"><b>Toplu giriş</b><span>Birden fazla boş koltuğu seç, toplu giriş ekranını aç, bilgileri tek seferde işle.</span></div>` |
| 2557 | `Hızlı` | `                <div class="guide-card-sub">Sürüş modu daha sade, daha hızlı ve sahaya uygun görünüm sunar.</div>` |
| 2563 | `Hızlı` | `              <div class="guide-line"><b>Sesli komut butonu</b><span>Sürüş modunda büyük mor buton üzerinden hızlı sesli komut kullanılabilir.</span></div>` |
| 2565 | `Hızlı` | `              <div class="guide-line"><b>Canlı durak ve sıradaki durak</b><span>Durak akışı kutuları ile aktif nokta ve yaklaşan nokta hızlıca takip edilir.</span></div>` |
| 2575 | `Hızlı` | `                <div class="guide-card-sub">Sık karşılaşılan durumlar için hızlı çözüm notları.</div>` |

### `android_app/app/src/main/python/templates/seats_parts/modals.html`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 78 | `Toplu Giriş` | `  <h3>Toplu Giriş</h3>` |
| 123 | `Hızlı` | `  <h3>Hızlı Tahsilat (Ayakta)</h3>` |

### `android_app/app/src/main/python/templates/seats_parts/deck.html`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 23 | `fab-column` | `            <div class="fab-column" aria-label="Hızlı işlemler">` |
| 24 | `class="fab` | `              <button class="fab primary" id="fabBulk" type="button" title="Toplu Giriş">＋</button>` |
| 25 | `class="fab` | `              <button class="fab green" id="fabCash" type="button" title="Hızlı Tahsilat">₺</button>` |
| 26 | `class="fab` | `              <button class="fab orange" id="btnOffloadNow" type="button" title="İndir">⇩</button>` |

### `android_app/app/src/main/python/static/seats/seats.css`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 730 | `fab-column` | `  .fab-column{` |
| 1377 | `fab-column` | `    .fab-column{` |
| 1523 | `fab-column` | `    .fab-column{` |
| 2250 | `Hızlı` | `/* Sağdaki hızlı butonlar koltukların üstüne fazla binmesin */` |
| 2251 | `fab-column` | `body.drive-mode .fab-column{` |
| 2563 | `HIZLI` | `   SÜRÜŞ MODU ALT HIZLI İŞLEM BARI` |
| 2572 | `fab-column` | `body.drive-mode .fab-column{` |
| 2629 | `fab-column` | `  body.drive-mode .fab-column{` |
| 2675 | `Hızlı` | `/* Alt hızlı işlem barını 51-54 satırına daha yakın taşı */` |
| 2676 | `fab-column` | `body.drive-mode .fab-column{` |
| 2703 | `fab-column` | `  body.drive-mode .fab-column{` |

### `android_app/app/src/main/python/static/seats/seats.js`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 1690 | `Toplu Giriş` | `      toast(e.message \|\| "Toplu giriş hatası");` |
| 2720 | `fabBulk` | `  onClick("#fabBulk", openBulk);` |
| 2721 | `fabBulk` | `  onClick("#fabBulkPane", openBulk);` |
| 2727 | `fabCash` | `  onClick("#fabCash", openCash);` |
| 2728 | `fabCash` | `  onClick("#fabCashPane", openCash);` |
| 2734 | `openStandingModalBtn` | `  onClick("#openStandingModalBtn", openStandingModal);` |

### `android_app/app/src/main/python/static/seats/drive-controls.js`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 3 | `HIZLI` | `   HIZLI KOLTUK → OTOMATİK SÜRÜŞ MODU` |
| 33 | `Hızlı` | `    console.warn("Hızlı koltuk sürüş modu açılamadı:", e);` |

### `android_app/app/src/main/python/static/seats/voice-commands.js`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 848 | `Toplu Giriş` | `  toast("Toplu giriş formu hazırlandı");` |
| 849 | `Toplu Giriş` | `  speak("Toplu giriş formu açıldı.");` |

### `android_app/app/src/main/python/static/seats/standing.js`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 3 | `Hızlı` | `   Ayakta yolcu + hızlı tahsilat + ayakta liste` |

### `android_app/app/src/main/python/static/seats/seats-final.css`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 632 | `fab-column` | `.fab-column{` |

### `android_app/app/src/main/python/static/live_map/muavin_live_map_extra.js`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 1055 | `class="fab` | `      toolsFab.innerHTML = '<span class="fab-icon">⚙️</span><span class="fab-text">Araçlar</span>';` |

### `android_app/app/src/main/python/static/seats/patches/modal-bottom-nav-autohide.js`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 26 | `Toplu Giriş` | `      (t.includes("toplu giriş") \|\| t.includes("toplu giris")) &&` |
| 33 | `HIZLI` | `      (t.includes("hızlı tahsilat") \|\| t.includes("hizli tahsilat")) &&` |

### `android_app/app/src/main/python/static/seats/patches/seat-layout-fab-pack.css`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 92 | `FAB_LEFT_GAP_MOVE` | `/* ===== FAB_LEFT_GAP_MOVE ===== */` |
| 94 | `Hızlı` | `    Hızlı işlem butonlarını sağ alttan alıp` |
| 99 | `fab-column` | `  .fab-column.fab-left-gap-moved{` |
| 112 | `fab-column` | `  .fab-column.fab-left-gap-moved .fab{` |
| 120 | `fab-column` | `  body.drive-mode .fab-column.fab-left-gap-moved .fab{` |
| 128 | `fab-column` | `    .fab-column.fab-left-gap-moved{` |
| 132 | `fab-column` | `    .fab-column.fab-left-gap-moved .fab,` |
| 133 | `fab-column` | `    body.drive-mode .fab-column.fab-left-gap-moved .fab{` |
| 143 | `Hızlı` | `    Sol boş alana taşınan hızlı işlem butonlarını` |
| 147 | `fab-column` | `  .fab-column.fab-left-gap-moved{` |
| 165 | `fab-column` | `  .fab-column.fab-left-gap-moved::before{` |
| 166 | `HIZLI` | `    content:"HIZLI";` |
| 180 | `fab-column` | `  .fab-column.fab-left-gap-moved .fab{` |
| 196 | `fab-column` | `  .fab-column.fab-left-gap-moved .fab::after{` |
| 205 | `fab-column` | `  .fab-column.fab-left-gap-moved .fab.primary{` |
| 211 | `fab-column` | `  .fab-column.fab-left-gap-moved .fab.green{` |
| 217 | `fab-column` | `  .fab-column.fab-left-gap-moved .fab.orange{` |
| 223 | `fab-column` | `  .fab-column.fab-left-gap-moved .fab:active{` |
| 228 | `fab-column` | `    .fab-column.fab-left-gap-moved{` |
| 233 | `fab-column` | `    .fab-column.fab-left-gap-moved .fab{` |
| 242 | `Hızlı` | `    Hızlı işlem paneli 43 ile 51 arasına tam otursun diye` |
| 246 | `fab-column` | `  .fab-column.fab-left-gap-moved{` |
| 252 | `fab-column` | `  .fab-column.fab-left-gap-moved::before{` |
| 258 | `fab-column` | `  .fab-column.fab-left-gap-moved .fab,` |
| 259 | `fab-column` | `  body.drive-mode .fab-column.fab-left-gap-moved .fab{` |
| 269 | `fab-column` | `  .fab-column.fab-left-gap-moved .fab::after{` |
| 275 | `fab-column` | `    .fab-column.fab-left-gap-moved{` |
| 281 | `fab-column` | `    .fab-column.fab-left-gap-moved .fab,` |
| 282 | `fab-column` | `    body.drive-mode .fab-column.fab-left-gap-moved .fab{` |
| 295 | `fab-column` | `    static/seats/seats.css içindeki body.drive-mode .fab-column kuralı` |
| 296 | `Hızlı` | `    hızlı işlem panelini yatay alt bar gibi zorluyordu.` |
| 299 | `fab-left-gap-moved` | `    .fab-left-gap-moved sınıfı varsa, drive-mode kurallarını ezip` |
| 303 | `fab-column` | `  .fab-column.fab-left-gap-moved,` |
| 304 | `fab-column` | `  body.drive-mode .fab-column.fab-left-gap-moved{` |
| 344 | `fab-column` | `  .fab-column.fab-left-gap-moved::before,` |
| 345 | `fab-column` | `  body.drive-mode .fab-column.fab-left-gap-moved::before{` |
| 346 | `HIZLI` | `    content:"HIZLI" !important;` |
| 361 | `fab-column` | `  .fab-column.fab-left-gap-moved .fab,` |
| 362 | `fab-column` | `  body.drive-mode .fab-column.fab-left-gap-moved .fab{` |
| 381 | `fab-column` | `  .fab-column.fab-left-gap-moved .fab::after,` |
| 382 | `fab-column` | `  body.drive-mode .fab-column.fab-left-gap-moved .fab::after{` |
| 388 | `fab-column` | `    .fab-column.fab-left-gap-moved,` |
| 389 | `fab-column` | `    body.drive-mode .fab-column.fab-left-gap-moved{` |
| 399 | `fab-column` | `    .fab-column.fab-left-gap-moved .fab,` |
| 400 | `fab-column` | `    body.drive-mode .fab-column.fab-left-gap-moved .fab{` |

### `android_app/app/src/main/python/static/seats/patches/seat-layout-fab-pack.js`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 1 | `FAB_LEFT_GAP_MOVE` | `/* ===== FAB_LEFT_GAP_MOVE ===== */` |
| 11 | `fab-column` | `    var col = q(".fab-column");` |
| 18 | `fab-left-gap-moved` | `    col.classList.add("fab-left-gap-moved");` |
| 110 | `fab-column` | `    var col = q(".fab-column");` |
| 117 | `fab-left-gap-moved` | `    col.classList.add("fab-left-gap-moved");` |

### `android_app/app/src/main/python/static/seats/patches/seat-simple-ui-pack.css`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 283 | `HIZLI` | `   SADE MOD ALT HIZLI BAR` |

### `android_app/app/src/main/python/static/seats/patches/mobile-performance-fix.css`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 59 | `fab-column` | `  .fab-column,` |
| 60 | `fab-column` | `  .fab-column.fab-left-gap-moved,` |
| 98 | `Hızlı` | `  /* Geçişleri kısalt: his olarak hızlı, yük olarak hafif */` |
| 117 | `fab-column` | `  .fab-column,` |

### `android_app/app/src/main/python/static/seats/patches/fab-sheet-solid-fix.css`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 3 | `Hızlı` | `   Toplu Giriş / Hızlı Tahsilat / Ayakta Listesi modallarının` |
| 55 | `Hızlı` | `  /* Modal açıkken sol hızlı butonlar arkada çok bağırmasın */` |
| 56 | `fab-column` | `  body:has(#bulkModal[style*="display: block"]) .fab-column,` |
| 57 | `fab-column` | `  body:has(#cashModal[style*="display: block"]) .fab-column,` |
| 58 | `fab-column` | `  body:has(#standingModal[style*="display: block"]) .fab-column,` |
| 59 | `fab-column` | `  body:has(#approachModal[style*="display: block"]) .fab-column{` |

### `android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-final.css`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 470 | `fab-column` | `.fab-column{` |

## 3) İlk teknik yorum

- `fab-column` HTML’de üretiliyorsa asıl kaynak odur.
- `seat-layout-fab-pack.js` sadece mevcut `.fab-column` elemanını bulup `fab-left-gap-moved` sınıfı ekliyorsa, butonu o üretmiyor; sadece yerini değiştiriyor demektir.
- `seat-layout-fab-pack.css` ise görünüm/konum yamasıdır.
- Gizleme veya kaldırma kararı vermeden önce asıl HTML kaynağı ile taşıyan yama ayrılmalı.