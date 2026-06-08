# Muavin Asistanı Patch Risk Matrix V11

- Tarih: `20260608-165821`
- Bu rapor sadece tespittir. Dosya değiştirmez, silmez, devre dışı bırakmaz.

## 1) Özet

| Kök | Aktif patch çağrısı | Benzersiz patch |
| --- | ---: | ---: |
| WEB | 20 | 20 |
| ANDROID | 19 | 19 |

## 2) WEB Risk Sıralaması

| Sıra | Seviye | Skor | Dosya | Satır | Hash | Mtime | SAVE | MODAL | EVENT | CSS | SEAT | STORAGE | ASYNC |
| ---: | --- | ---: | --- | ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | B-KRİTİK | 497 | `static/seats/patches/seat-simple-ui-pack.css` | 397 | 37874d3bba93 | 2026-05-18 17:59:24 | 0 | 7 | 0 | 30 | 67 | 0 | 0 |
| 2 | C-ORTA | 453 | `static/seats/patches/unified-seat-deck-report-style.css` | 516 | d30bc2b71583 | 2026-05-21 21:23:10 | 0 | 0 | 0 | 12 | 81 | 0 | 0 |
| 3 | B-KRİTİK | 358 | `static/seats/patches/mobile-performance-fix.css` | 178 | ebb9eb4d201a | 2026-05-18 18:11:00 | 0 | 36 | 0 | 8 | 22 | 0 | 0 |
| 4 | A-ÇOK KRİTİK | 294 | `static/seats/patches/seat-simple-ui-pack.js` | 278 | ab923a78a462 | 2026-05-18 17:59:24 | 1 | 10 | 7 | 2 | 23 | 2 | 20 |
| 5 | B-KRİTİK | 204 | `static/seats/patches/fab-sheet-solid-fix.css` | 64 | 1f9b5f2b0b4c | 2026-05-18 20:57:55 | 0 | 32 | 0 | 3 | 0 | 0 | 0 |
| 6 | A-ÇOK KRİTİK | 180 | `static/seats/patches/stop-flow-focus-patch.js` | 387 | ff6942c64edd | 2026-05-20 11:06:12 | 1 | 1 | 8 | 2 | 10 | 14 | 8 |
| 7 | C-ORTA | 177 | `static/seats/patches/seat-layout-fab-pack.js` | 167 | d15660098d60 | 2026-05-18 17:52:36 | 0 | 0 | 12 | 0 | 6 | 0 | 29 |
| 8 | B-KRİTİK | 160 | `static/seats/patches/seat-layout-fab-pack.css` | 408 | 4c1589bd069a | 2026-05-18 17:52:36 | 0 | 2 | 0 | 27 | 8 | 0 | 0 |
| 9 | B-KRİTİK | 143 | `static/seats/patches/modal-bottom-nav-autohide.js` | 149 | 5b408035d775 | 2026-05-18 16:57:39 | 0 | 13 | 5 | 1 | 3 | 0 | 7 |
| 10 | C-ORTA | 140 | `static/seats/patches/manual-ticket-system.js` | 227 | 142da4fa8a42 | 2026-05-18 16:59:02 | 0 | 0 | 4 | 0 | 12 | 3 | 17 |
| 11 | C-ORTA | 137 | `static/seats/patches/top-sound-toggle.js` | 159 | 2851010fa38f | 2026-05-18 17:19:03 | 0 | 0 | 8 | 0 | 11 | 3 | 11 |
| 12 | C-ORTA | 82 | `static/seats/patches/stop-flow-compact-mobile.css` | 106 | 3ab54340a0cd | 2026-05-18 20:53:14 | 0 | 0 | 0 | 7 | 0 | 18 | 0 |
| 13 | C-ORTA | 62 | `static/seats/patches/stop-flow-focus-patch.css` | 177 | 383d9d45a418 | 2026-05-18 17:44:27 | 0 | 0 | 0 | 14 | 0 | 2 | 0 |
| 14 | B-KRİTİK | 60 | `static/seats/patches/stop-selected-toast.css` | 68 | 714896463348 | 2026-05-18 16:44:37 | 0 | 2 | 0 | 12 | 0 | 0 | 0 |
| 15 | B-KRİTİK | 58 | `static/seats/patches/seat-label-ghost-clean.css` | 45 | 7dbec74abcf7 | 2026-05-18 21:04:19 | 0 | 2 | 0 | 4 | 6 | 0 | 0 |
| 16 | C-ORTA | 49 | `static/seats/patches/manual-ticket-system.css` | 55 | 91251ec128d5 | 2026-05-18 16:59:02 | 0 | 0 | 0 | 6 | 5 | 0 | 0 |
| 17 | B-KRİTİK | 22 | `static/seats/patches/modal-bottom-nav-autohide.css` | 6 | a2b76d9d15a0 | 2026-05-18 16:57:39 | 0 | 1 | 0 | 4 | 0 | 0 | 0 |
| 18 | C-ORTA | 19 | `static/seats/patches/stop-selected-toast.js` | 63 | 740905a0e0e6 | 2026-05-18 16:44:37 | 0 | 0 | 1 | 0 | 1 | 0 | 3 |
| 19 | C-ORTA | 4 | `static/seats/patches/top-sound-toggle.css` | 60 | dea40a39c380 | 2026-05-18 17:19:03 | 0 | 0 | 0 | 1 | 0 | 0 | 0 |
| 20 | D-DÜŞÜK | 0 | `static/seats/patches/bottom-voice-command.css` | 25 | 5f664bc9a1e5 | 2026-05-18 16:55:51 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

## 3) WEB ↔ ANDROID Patch Hash Kontrolü

| Dosya | WEB | ANDROID | Durum |
| --- | --- | --- | --- |
| `static/seats/patches/bottom-voice-command.css` | 5f664bc9a1e5 | 5f664bc9a1e5 | AYNI |
| `static/seats/patches/fab-sheet-solid-fix.css` | 1f9b5f2b0b4c | 1f9b5f2b0b4c | AYNI |
| `static/seats/patches/manual-ticket-system.css` | 91251ec128d5 | 91251ec128d5 | AYNI |
| `static/seats/patches/manual-ticket-system.js` | 142da4fa8a42 | 142da4fa8a42 | AYNI |
| `static/seats/patches/mobile-performance-fix.css` | ebb9eb4d201a | ebb9eb4d201a | AYNI |
| `static/seats/patches/modal-bottom-nav-autohide.css` | a2b76d9d15a0 | a2b76d9d15a0 | AYNI |
| `static/seats/patches/modal-bottom-nav-autohide.js` | 5b408035d775 | 5b408035d775 | AYNI |
| `static/seats/patches/seat-label-ghost-clean.css` | 7dbec74abcf7 | 7dbec74abcf7 | AYNI |
| `static/seats/patches/seat-layout-fab-pack.css` | 4c1589bd069a | 4c1589bd069a | AYNI |
| `static/seats/patches/seat-layout-fab-pack.js` | d15660098d60 | d15660098d60 | AYNI |
| `static/seats/patches/seat-simple-ui-pack.css` | 37874d3bba93 | 37874d3bba93 | AYNI |
| `static/seats/patches/seat-simple-ui-pack.js` | ab923a78a462 | ab923a78a462 | AYNI |
| `static/seats/patches/stop-flow-compact-mobile.css` | 3ab54340a0cd | 3ab54340a0cd | AYNI |
| `static/seats/patches/stop-flow-focus-patch.css` | 383d9d45a418 | 383d9d45a418 | AYNI |
| `static/seats/patches/stop-flow-focus-patch.js` | ff6942c64edd | ff6942c64edd | AYNI |
| `static/seats/patches/stop-selected-toast.css` | 714896463348 | 714896463348 | AYNI |
| `static/seats/patches/stop-selected-toast.js` | 740905a0e0e6 | 740905a0e0e6 | AYNI |
| `static/seats/patches/top-sound-toggle.css` | dea40a39c380 | dea40a39c380 | AYNI |
| `static/seats/patches/top-sound-toggle.js` | 2851010fa38f | 2851010fa38f | AYNI |
| `static/seats/patches/unified-seat-deck-report-style.css` | d30bc2b71583 | - | SADECE WEB |

## 4) Kritik Satır İzleri

### B-KRİTİK / Skor 497 / `static/seats/patches/seat-simple-ui-pack.css`

| Kategori | Satır | İçerik |
| --- | ---: | --- |
| MODAL_DIRECT | 302 | `backdrop-filter:blur(18px) saturate(1.1);` |
| MODAL_DIRECT | 303 | `-webkit-backdrop-filter:blur(18px) saturate(1.1);` |
| MODAL_DIRECT | 388 | `/* ===== seat-hide-bottom-menu-on-modal-style ===== */` |
| MODAL_DIRECT | 390 | `KOLTUK MODAL AÇILINCA ALT MENÜYÜ GİZLE` |
| MODAL_DIRECT | 391 | `Modala dokunmaz; sadece sade mod alt barını saklar.` |
| MODAL_DIRECT | 394 | `html.seat-modal-open .seat-simple-bottom-bar,` |
| MODAL_DIRECT | 395 | `body.seat-modal-open .seat-simple-bottom-bar{` |
| CSS_BLOCK_RISK | 9 | `top:8px;` |
| CSS_BLOCK_RISK | 10 | `z-index:9999;` |
| CSS_BLOCK_RISK | 35 | `display:none !important;` |
| CSS_BLOCK_RISK | 44 | `display:none !important;` |
| CSS_BLOCK_RISK | 54 | `padding-top:10px !important;` |
| CSS_BLOCK_RISK | 60 | `display:none !important;` |
| CSS_BLOCK_RISK | 68 | `display:none !important;` |
| CSS_BLOCK_RISK | 83 | `display:none !important;` |
| CSS_BLOCK_RISK | 110 | `display:none !important;` |
| CSS_BLOCK_RISK | 117 | `margin-top:8px !important;` |
| CSS_BLOCK_RISK | 126 | `margin-bottom:8px;` |
| CSS_BLOCK_RISK | 145 | `display:none;` |
| CSS_BLOCK_RISK | 168 | `margin-bottom:10px;` |
| CSS_BLOCK_RISK | 178 | `overflow:hidden;` |
| CSS_BLOCK_RISK | 179 | `text-overflow:ellipsis;` |
| CSS_BLOCK_RISK | 213 | `overflow:hidden;` |
| CSS_BLOCK_RISK | 218 | `margin-bottom:5px;` |
| CSS_BLOCK_RISK | 222 | `text-transform:uppercase;` |
| CSS_BLOCK_RISK | 233 | `overflow:hidden;` |
| CSS_BLOCK_RISK | 234 | `text-overflow:ellipsis;` |
| CSS_BLOCK_RISK | 247 | `margin-bottom:10px !important;` |
| CSS_BLOCK_RISK | 254 | `margin-bottom:10px;` |
| CSS_BLOCK_RISK | 288 | `display:none;` |
| CSS_BLOCK_RISK | 289 | `position:fixed;` |
| CSS_BLOCK_RISK | 292 | `bottom:10px;` |
| CSS_BLOCK_RISK | 293 | `z-index:99999;` |
| CSS_BLOCK_RISK | 313 | `padding-bottom:92px !important;` |
| CSS_BLOCK_RISK | 364 | `transform:scale(.96);` |
| CSS_BLOCK_RISK | 371 | `bottom:8px;` |
| CSS_BLOCK_RISK | 396 | `display:none !important;` |
| SEAT_STATE | 1 | `/* ===== seat-simple-open-mode-style ===== */` |
| SEAT_STATE | 7 | `.seat-simple-toggle{` |
| SEAT_STATE | 28 | `html.seat-simple-mode .seats-shell{` |
| SEAT_STATE | 34 | `html.seat-simple-mode .seats-shell > :not(.layout){` |
| SEAT_STATE | 38 | `html.seat-simple-mode .layout{` |
| SEAT_STATE | 43 | `html.seat-simple-mode .panel-card{` |
| SEAT_STATE | 47 | `html.seat-simple-mode .board-card{` |
| SEAT_STATE | 53 | `html.seat-simple-mode .board-inner{` |
| SEAT_STATE | 58 | `html.seat-simple-mode #driveInlineDock,` |
| SEAT_STATE | 59 | `html.seat-simple-mode #driveModeActionsDock{` |
| SEAT_STATE | 64 | `html.seat-simple-mode .board-head-right,` |
| SEAT_STATE | 65 | `html.seat-simple-mode .voice-row,` |
| SEAT_STATE | 66 | `html.seat-simple-mode .drive-voice-row,` |
| SEAT_STATE | 67 | `html.seat-simple-mode .legend{` |
| SEAT_STATE | 72 | `html.seat-simple-mode .board-head{` |
| SEAT_STATE | 77 | `html.seat-simple-mode .board-title{` |
| SEAT_STATE | 81 | `html.seat-simple-mode .board-kicker,` |
| SEAT_STATE | 82 | `html.seat-simple-mode .board-title small{` |
| SEAT_STATE | 86 | `html.seat-simple-mode .board-title h2{` |
| SEAT_STATE | 93 | `html.seat-simple-mode .selected-stop-chip{` |
| SEAT_STATE | 104 | `html.seat-simple-mode .route-strip-shell,` |
| SEAT_STATE | 105 | `html.seat-simple-mode .route-flow-shell,` |
| SEAT_STATE | 106 | `html.seat-simple-mode .route-flow,` |
| SEAT_STATE | 107 | `html.seat-simple-mode #routeStrip,` |
| SEAT_STATE | 108 | `html.seat-simple-mode .route-mini,` |
| SEAT_STATE | 109 | `html.seat-simple-mode .route-pill{` |
| SEAT_STATE | 114 | `html.seat-simple-mode .deck-card,` |
| SEAT_STATE | 115 | `html.seat-simple-mode .seat-deck,` |
| SEAT_STATE | 116 | `html.seat-simple-mode .deck-shell{` |
| SEAT_STATE | 122 | `.seat-simple-toggle{` |
| SEAT_STATE | 129 | `html.seat-simple-mode .board-inner{` |
| SEAT_STATE | 133 | `html.seat-simple-mode .board-title h2{` |
| SEAT_STATE | 138 | `/* ===== seat-simple-summary-polish-style ===== */` |
| SEAT_STATE | 144 | `.seat-simple-summary{` |
| SEAT_STATE | 159 | `html.seat-simple-mode .seat-simple-summary{` |
| SEAT_STATE | 163 | `.seat-simple-summary-top{` |
| SEAT_STATE | 171 | `.seat-simple-route{` |
| SEAT_STATE | 183 | `.seat-simple-status{` |
| SEAT_STATE | 200 | `.seat-simple-summary-grid{` |
| SEAT_STATE | 206 | `.seat-simple-mini{` |
| SEAT_STATE | 216 | `.seat-simple-mini small{` |
| SEAT_STATE | 227 | `.seat-simple-mini b{` |
| SEAT_STATE | 238 | `.seat-simple-mini .ok{` |

### C-ORTA / Skor 453 / `static/seats/patches/unified-seat-deck-report-style.css`

| Kategori | Satır | İçerik |
| --- | ---: | --- |
| CSS_BLOCK_RISK | 22 | `overflow-x:auto !important;` |
| CSS_BLOCK_RISK | 23 | `overflow-y:visible !important;` |
| CSS_BLOCK_RISK | 80 | `transform:none !important;` |
| CSS_BLOCK_RISK | 99 | `display:none !important;` |
| CSS_BLOCK_RISK | 106 | `overflow:hidden !important;` |
| CSS_BLOCK_RISK | 202 | `opacity:.92 !important;` |
| CSS_BLOCK_RISK | 241 | `transform:none !important;` |
| CSS_BLOCK_RISK | 253 | `top:-12px !important;` |
| CSS_BLOCK_RISK | 257 | `transform:none !important;` |
| CSS_BLOCK_RISK | 268 | `top:-10px !important;` |
| CSS_BLOCK_RISK | 278 | `bottom:-10px !important;` |
| CSS_BLOCK_RISK | 385 | `overflow:hidden !important;` |
| SEAT_STATE | 8 | `--unified-seat-w:82px;` |
| SEAT_STATE | 9 | `--unified-seat-h:58px;` |
| SEAT_STATE | 19 | `html.seat-simple-mode .board-stage{` |
| SEAT_STATE | 29 | `html.seat-simple-mode .deck-wrap{` |
| SEAT_STATE | 41 | `html.seat-simple-mode .deck{` |
| SEAT_STATE | 47 | `var(--unified-seat-w)` |
| SEAT_STATE | 49 | `var(--unified-seat-w)` |
| SEAT_STATE | 50 | `var(--unified-seat-w) !important;` |
| SEAT_STATE | 74 | `html.seat-simple-mode .deck .cell[style*="grid-column:4"],` |
| SEAT_STATE | 75 | `html.seat-simple-mode .deck .cell[style*="grid-column: 4"],` |
| SEAT_STATE | 86 | `html.seat-simple-mode .cell{` |
| SEAT_STATE | 87 | `width:var(--unified-seat-w) !important;` |
| SEAT_STATE | 88 | `min-width:var(--unified-seat-w) !important;` |
| SEAT_STATE | 89 | `max-width:var(--unified-seat-w) !important;` |
| SEAT_STATE | 98 | `html.seat-simple-mode .label{` |
| SEAT_STATE | 110 | `.seat,` |
| SEAT_STATE | 111 | `body.drive-mode .seat,` |
| SEAT_STATE | 112 | `html.seat-simple-mode .seat{` |
| SEAT_STATE | 114 | `height:var(--unified-seat-h) !important;` |
| SEAT_STATE | 115 | `min-height:var(--unified-seat-h) !important;` |
| SEAT_STATE | 139 | `.seat:not(.isAssigned):not(.male):not(.female),` |
| SEAT_STATE | 140 | `body.drive-mode .seat:not(.isAssigned):not(.male):not(.female),` |
| SEAT_STATE | 141 | `html.seat-simple-mode .seat:not(.isAssigned):not(.male):not(.female){` |
| SEAT_STATE | 145 | `.seat.male,` |
| SEAT_STATE | 146 | `body.drive-mode .seat.male,` |
| SEAT_STATE | 147 | `html.seat-simple-mode .seat.male{` |
| SEAT_STATE | 151 | `.seat.female,` |
| SEAT_STATE | 152 | `body.drive-mode .seat.female,` |
| SEAT_STATE | 153 | `html.seat-simple-mode .seat.female{` |
| SEAT_STATE | 157 | `.seat.isAssigned:not(.male):not(.female),` |
| SEAT_STATE | 158 | `body.drive-mode .seat.isAssigned:not(.male):not(.female),` |
| SEAT_STATE | 159 | `html.seat-simple-mode .seat.isAssigned:not(.male):not(.female){` |
| SEAT_STATE | 164 | `.seat.selected,` |
| SEAT_STATE | 165 | `body.drive-mode .seat.selected,` |
| SEAT_STATE | 166 | `html.seat-simple-mode .seat.selected{` |
| SEAT_STATE | 176 | `.seat.has-stop,` |
| SEAT_STATE | 177 | `body.drive-mode .seat.has-stop,` |
| SEAT_STATE | 178 | `html.seat-simple-mode .seat.has-stop{` |
| SEAT_STATE | 187 | `html.seat-simple-mode .corr{` |
| SEAT_STATE | 222 | `html.seat-simple-mode .door{` |
| SEAT_STATE | 249 | `.seat .bag-badge,` |
| SEAT_STATE | 250 | `body.drive-mode .seat .bag-badge,` |
| SEAT_STATE | 251 | `html.seat-simple-mode .seat .bag-badge{` |
| SEAT_STATE | 264 | `.seat .svc-badge,` |
| SEAT_STATE | 265 | `body.drive-mode .seat .svc-badge,` |
| SEAT_STATE | 266 | `html.seat-simple-mode .seat .svc-badge{` |
| SEAT_STATE | 274 | `.seat .stop-badge,` |
| SEAT_STATE | 275 | `body.drive-mode .seat .stop-badge,` |
| SEAT_STATE | 276 | `html.seat-simple-mode .seat .stop-badge{` |
| SEAT_STATE | 285 | `--seat-gap-x:var(--unified-gap-x) !important;` |
| SEAT_STATE | 286 | `--seat-gap-y:var(--unified-gap-y) !important;` |
| SEAT_STATE | 292 | `--unified-seat-w:76px;` |
| SEAT_STATE | 293 | `--unified-seat-h:56px;` |
| SEAT_STATE | 302 | `html.seat-simple-mode .board-stage{` |
| SEAT_STATE | 308 | `html.seat-simple-mode .deck{` |
| SEAT_STATE | 313 | `.seat,` |
| SEAT_STATE | 314 | `body.drive-mode .seat,` |
| SEAT_STATE | 315 | `html.seat-simple-mode .seat{` |
| SEAT_STATE | 322 | `html.seat-simple-mode .corr{` |
| SEAT_STATE | 329 | `html.seat-simple-mode .door{` |
| SEAT_STATE | 338 | `--unified-seat-w:70px;` |
| SEAT_STATE | 339 | `--unified-seat-h:54px;` |
| SEAT_STATE | 346 | `.seat,` |
| SEAT_STATE | 347 | `body.drive-mode .seat,` |
| SEAT_STATE | 348 | `html.seat-simple-mode .seat{` |
| SEAT_STATE | 365 | `html.seat-simple-mode .cell{` |
| SEAT_STATE | 374 | `html.seat-simple-mode .label{` |
| SEAT_STATE | 376 | `width:var(--unified-seat-w) !important;` |

### B-KRİTİK / Skor 358 / `static/seats/patches/mobile-performance-fix.css`

| Kategori | Satır | İçerik |
| --- | ---: | --- |
| MODAL_DIRECT | 35 | `-webkit-backdrop-filter:none !important;` |
| MODAL_DIRECT | 36 | `backdrop-filter:none !important;` |
| MODAL_DIRECT | 52 | `.modal,` |
| MODAL_DIRECT | 53 | `.modal-card,` |
| MODAL_DIRECT | 54 | `.modal-content,` |
| MODAL_DIRECT | 125 | `/* MOBILE_MODAL_READABILITY_FIX_START */` |
| MODAL_DIRECT | 126 | `/* Performans yaması modalı fazla şeffaflaştırmasın diye modal koruması */` |
| MODAL_DIRECT | 129 | `#seatBackdrop,` |
| MODAL_DIRECT | 130 | `.seat-backdrop,` |
| MODAL_DIRECT | 131 | `.modal-backdrop,` |
| MODAL_DIRECT | 132 | `.backdrop{` |
| MODAL_DIRECT | 137 | `#seatModal,` |
| MODAL_DIRECT | 138 | `.seat-modal,` |
| MODAL_DIRECT | 139 | `.modal,` |
| MODAL_DIRECT | 140 | `.modal-card,` |
| MODAL_DIRECT | 141 | `.modal-content,` |
| MODAL_DIRECT | 144 | `.seat-edit-modal{` |
| MODAL_DIRECT | 145 | `-webkit-backdrop-filter:none !important;` |
| MODAL_DIRECT | 146 | `backdrop-filter:none !important;` |
| MODAL_DIRECT | 149 | `#seatModal,` |
| MODAL_DIRECT | 150 | `.seat-modal{` |
| MODAL_DIRECT | 154 | `#seatModal .modal-card,` |
| MODAL_DIRECT | 155 | `#seatModal .modal-content,` |
| MODAL_DIRECT | 156 | `#seatModal .sheet,` |
| MODAL_DIRECT | 157 | `#seatModal form,` |
| MODAL_DIRECT | 158 | `.seat-modal .modal-card,` |
| MODAL_DIRECT | 159 | `.seat-modal .modal-content,` |
| MODAL_DIRECT | 160 | `.seat-modal .sheet,` |
| MODAL_DIRECT | 161 | `.seat-modal form{` |
| MODAL_DIRECT | 167 | `#seatModal input,` |
| MODAL_DIRECT | 168 | `#seatModal select,` |
| MODAL_DIRECT | 169 | `#seatModal textarea,` |
| MODAL_DIRECT | 170 | `.seat-modal input,` |
| MODAL_DIRECT | 171 | `.seat-modal select,` |
| MODAL_DIRECT | 172 | `.seat-modal textarea{` |
| MODAL_DIRECT | 178 | `/* MOBILE_MODAL_READABILITY_FIX_END */` |
| CSS_BLOCK_RISK | 24 | `position:fixed;` |
| CSS_BLOCK_RISK | 25 | `inset:0;` |
| CSS_BLOCK_RISK | 26 | `z-index:-1;` |
| CSS_BLOCK_RISK | 27 | `pointer-events:none;` |
| CSS_BLOCK_RISK | 108 | `transition:transform .06s linear, opacity .06s linear !important;` |
| CSS_BLOCK_RISK | 119 | `transform:translateZ(0);` |
| CSS_BLOCK_RISK | 120 | `backface-visibility:hidden;` |
| CSS_BLOCK_RISK | 134 | `opacity:1 !important;` |
| SEAT_STATE | 45 | `.seat-card,` |
| SEAT_STATE | 56 | `.seat-simple-bottom-bar,` |
| SEAT_STATE | 66 | `.seat,` |
| SEAT_STATE | 74 | `.seat-simple-bottom-item,` |
| SEAT_STATE | 89 | `.seat,` |
| SEAT_STATE | 99 | `.seat,` |
| SEAT_STATE | 105 | `.seat-simple-bottom-item,` |
| SEAT_STATE | 113 | `.seat-grid,` |
| SEAT_STATE | 114 | `.seat-board,` |
| SEAT_STATE | 115 | `.seat-map,` |
| SEAT_STATE | 116 | `.seat-simple-bottom-bar,` |
| SEAT_STATE | 130 | `.seat-backdrop,` |
| SEAT_STATE | 138 | `.seat-modal,` |
| SEAT_STATE | 144 | `.seat-edit-modal{` |
| SEAT_STATE | 150 | `.seat-modal{` |
| SEAT_STATE | 158 | `.seat-modal .modal-card,` |
| SEAT_STATE | 159 | `.seat-modal .modal-content,` |
| SEAT_STATE | 160 | `.seat-modal .sheet,` |
| SEAT_STATE | 161 | `.seat-modal form{` |
| SEAT_STATE | 170 | `.seat-modal input,` |
| SEAT_STATE | 171 | `.seat-modal select,` |
| SEAT_STATE | 172 | `.seat-modal textarea{` |

### A-ÇOK KRİTİK / Skor 294 / `static/seats/patches/seat-simple-ui-pack.js`

| Kategori | Satır | İçerik |
| --- | ---: | --- |
| SAVE_DIRECT | 241 | `"#btnSeatSave",` |
| MODAL_DIRECT | 202 | `/* ===== seat-hide-bottom-menu-on-modal-script ===== */` |
| MODAL_DIRECT | 204 | `if(window.__seatHideBottomMenuOnModalReady) return;` |
| MODAL_DIRECT | 205 | `window.__seatHideBottomMenuOnModalReady = true;` |
| MODAL_DIRECT | 225 | `const seatModal = q("#seatModal");` |
| MODAL_DIRECT | 226 | `const seatBackdrop = q("#seatBackdrop");` |
| MODAL_DIRECT | 228 | `const open = isVisible(seatModal) \|\| isVisible(seatBackdrop);` |
| MODAL_DIRECT | 230 | `document.documentElement.classList.toggle("seat-modal-open", open);` |
| MODAL_DIRECT | 231 | `document.body.classList.toggle("seat-modal-open", open);` |
| MODAL_DIRECT | 238 | `"#seatModal",` |
| MODAL_DIRECT | 239 | `"#seatBackdrop",` |
| EVENT_RISK | 61 | `btn.addEventListener("click", function(){` |
| EVENT_RISK | 80 | `document.addEventListener("DOMContentLoaded", boot);` |
| EVENT_RISK | 193 | `document.addEventListener("DOMContentLoaded", boot);` |
| EVENT_RISK | 259 | `document.addEventListener("click", function(){` |
| EVENT_RISK | 265 | `window.addEventListener("resize", sync);` |
| EVENT_RISK | 266 | `window.addEventListener("orientationchange", function(){` |
| EVENT_RISK | 274 | `document.addEventListener("DOMContentLoaded", boot);` |
| CSS_BLOCK_RISK | 217 | `if(cs.visibility === "hidden") return false;` |
| CSS_BLOCK_RISK | 218 | `if(cs.opacity === "0") return false;` |
| SEAT_STATE | 1 | `/* ===== seat-simple-open-mode-script ===== */` |
| SEAT_STATE | 8 | `return (window.SEATS_BOOT && window.SEATS_BOOT.tripKey) \|\| window.BAG_TRIP \|\| "default";` |
| SEAT_STATE | 34 | `document.documentElement.classList.toggle("seat-simple-mode", simple);` |
| SEAT_STATE | 35 | `document.body.classList.toggle("seat-simple-mode", simple);` |
| SEAT_STATE | 54 | `const host = document.querySelector(".board-inner") \|\| document.querySelector(".seats-shell");` |
| SEAT_STATE | 60 | `btn.className = "seat-simple-toggle";` |
| SEAT_STATE | 86 | `/* ===== seat-simple-summary-polish-script ===== */` |
| SEAT_STATE | 92 | `return document.querySelector(sel);` |
| SEAT_STATE | 103 | `box.className = "seat-simple-summary";` |
| SEAT_STATE | 105 | `<div class="seat-simple-summary-top">` |
| SEAT_STATE | 106 | `<div class="seat-simple-route" id="seatSimpleRoute">—</div>` |
| SEAT_STATE | 107 | `<div class="seat-simple-status"><span>●</span><span>Sade Mod</span></div>` |
| SEAT_STATE | 110 | `<div class="seat-simple-summary-grid">` |
| SEAT_STATE | 111 | `<div class="seat-simple-mini">` |
| SEAT_STATE | 115 | `<div class="seat-simple-mini">` |
| SEAT_STATE | 119 | `<div class="seat-simple-mini">` |
| SEAT_STATE | 144 | `const bootData = window.SEATS_BOOT \|\| {};` |
| SEAT_STATE | 161 | `filled = String(Object.values(bootData.assigned \|\| {}).filter(Boolean).length);` |
| SEAT_STATE | 169 | `const total = Object.keys(bootData.seatPositions \|\| {}).length;` |
| SEAT_STATE | 202 | `/* ===== seat-hide-bottom-menu-on-modal-script ===== */` |
| SEAT_STATE | 208 | `return document.querySelector(sel);` |
| SEAT_STATE | 230 | `document.documentElement.classList.toggle("seat-modal-open", open);` |
| SEAT_STATE | 231 | `document.body.classList.toggle("seat-modal-open", open);` |
| STORAGE_STATE | 20 | `return localStorage.getItem(key()) \|\| "simple";` |
| STORAGE_STATE | 28 | `localStorage.setItem(key(), mode);` |
| ASYNC_TIMING | 75 | `setTimeout(function(){ applyMode(readMode()); }, 250);` |
| ASYNC_TIMING | 76 | `setTimeout(function(){ applyMode(readMode()); }, 900);` |
| ASYNC_TIMING | 79 | `if(document.readyState === "loading"){` |
| ASYNC_TIMING | 80 | `document.addEventListener("DOMContentLoaded", boot);` |
| ASYNC_TIMING | 135 | `setInterval(update, 1000);` |
| ASYNC_TIMING | 192 | `if(document.readyState === "loading"){` |
| ASYNC_TIMING | 193 | `document.addEventListener("DOMContentLoaded", boot);` |
| ASYNC_TIMING | 198 | `setTimeout(boot, 300);` |
| ASYNC_TIMING | 199 | `setTimeout(update, 900);` |
| ASYNC_TIMING | 242 | `"#btnSeatOffload"` |
| ASYNC_TIMING | 245 | `const observer = new MutationObserver(sync);` |
| ASYNC_TIMING | 260 | `setTimeout(sync, 20);` |
| ASYNC_TIMING | 261 | `setTimeout(sync, 120);` |
| ASYNC_TIMING | 262 | `setTimeout(sync, 300);` |
| ASYNC_TIMING | 265 | `window.addEventListener("resize", sync);` |
| ASYNC_TIMING | 266 | `window.addEventListener("orientationchange", function(){` |
| ASYNC_TIMING | 267 | `setTimeout(sync, 250);` |
| ASYNC_TIMING | 270 | `setInterval(sync, 500);` |
| ASYNC_TIMING | 273 | `if(document.readyState === "loading"){` |
| ASYNC_TIMING | 274 | `document.addEventListener("DOMContentLoaded", boot);` |

### B-KRİTİK / Skor 204 / `static/seats/patches/fab-sheet-solid-fix.css`

| Kategori | Satır | İçerik |
| --- | ---: | --- |
| MODAL_DIRECT | 3 | `Toplu Giriş / Hızlı Tahsilat / Ayakta Listesi modallarının` |
| MODAL_DIRECT | 9 | `#bulkBackdrop,` |
| MODAL_DIRECT | 10 | `#cashBackdrop,` |
| MODAL_DIRECT | 11 | `#standingBackdrop,` |
| MODAL_DIRECT | 12 | `#approachBackdrop{` |
| MODAL_DIRECT | 17 | `#bulkModal.sheet-modal.glass,` |
| MODAL_DIRECT | 18 | `#cashModal.sheet-modal.glass,` |
| MODAL_DIRECT | 19 | `#standingModal.sheet-modal.glass,` |
| MODAL_DIRECT | 20 | `#approachModal.sheet-modal.glass{` |
| MODAL_DIRECT | 24 | `-webkit-backdrop-filter:none !important;` |
| MODAL_DIRECT | 25 | `backdrop-filter:none !important;` |
| MODAL_DIRECT | 28 | `#bulkModal.sheet-modal.glass *,` |
| MODAL_DIRECT | 29 | `#cashModal.sheet-modal.glass *,` |
| MODAL_DIRECT | 30 | `#standingModal.sheet-modal.glass *,` |
| MODAL_DIRECT | 31 | `#approachModal.sheet-modal.glass *{` |
| MODAL_DIRECT | 35 | `#bulkModal input,` |
| MODAL_DIRECT | 36 | `#bulkModal select,` |
| MODAL_DIRECT | 37 | `#cashModal input,` |
| MODAL_DIRECT | 38 | `#cashModal select,` |
| MODAL_DIRECT | 39 | `#standingModal input,` |
| MODAL_DIRECT | 40 | `#standingModal select,` |
| MODAL_DIRECT | 41 | `#approachModal input,` |
| MODAL_DIRECT | 42 | `#approachModal select{` |
| MODAL_DIRECT | 48 | `#bulkModal .muted,` |
| MODAL_DIRECT | 49 | `#cashModal .muted,` |
| MODAL_DIRECT | 50 | `#standingModal .muted,` |
| MODAL_DIRECT | 51 | `#approachModal .muted{` |
| MODAL_DIRECT | 55 | `/* Modal açıkken sol hızlı butonlar arkada çok bağırmasın */` |
| MODAL_DIRECT | 56 | `body:has(#bulkModal[style*="display: block"]) .fab-column,` |
| MODAL_DIRECT | 57 | `body:has(#cashModal[style*="display: block"]) .fab-column,` |
| MODAL_DIRECT | 58 | `body:has(#standingModal[style*="display: block"]) .fab-column,` |
| MODAL_DIRECT | 59 | `body:has(#approachModal[style*="display: block"]) .fab-column{` |
| CSS_BLOCK_RISK | 14 | `opacity:1 !important;` |
| CSS_BLOCK_RISK | 60 | `opacity:.18 !important;` |
| CSS_BLOCK_RISK | 61 | `pointer-events:none !important;` |

### A-ÇOK KRİTİK / Skor 180 / `static/seats/patches/stop-flow-focus-patch.js`

| Kategori | Satır | İçerik |
| --- | ---: | --- |
| SAVE_DIRECT | 361 | `["openSeat", "openFormWithSeat"].forEach(function(fn){` |
| MODAL_DIRECT | 160 | `'<div class="stop-focus-panel" role="dialog" aria-modal="true" aria-label="Durak Akışı">' +` |
| EVENT_RISK | 174 | `ov.addEventListener("click", function(e){` |
| EVENT_RISK | 177 | `e.preventDefault();` |
| EVENT_RISK | 184 | `e.preventDefault();` |
| EVENT_RISK | 324 | `document.addEventListener("click", function(e){` |
| EVENT_RISK | 335 | `e.preventDefault();` |
| EVENT_RISK | 336 | `e.stopPropagation();` |
| EVENT_RISK | 337 | `e.stopImmediatePropagation();` |
| EVENT_RISK | 384 | `document.addEventListener("DOMContentLoaded", installHooks);` |
| CSS_BLOCK_RISK | 6 | `var memoryKey = "muavin:selectedStop:" + String(window.TRIP_KEY \|\| window.BAG_TRIP \|\| location.pathname);` |
| CSS_BLOCK_RISK | 149 | `document.dispatchEvent(new CustomEvent("muavin:selected-stop-change", {detail:{stop:name}}));` |
| SEAT_STATE | 8 | `function qs(s, root){ return (root \|\| document).querySelector(s); }` |
| SEAT_STATE | 9 | `function qsa(s, root){ return Array.prototype.slice.call((root \|\| document).querySelectorAll(s)); }` |
| SEAT_STATE | 75 | `if(window.SEATS_BOOT && Array.isArray(window.SEATS_BOOT.stops)) window.SEATS_BOOT.stops.forEach(add);` |
| SEAT_STATE | 82 | `add(el.getAttribute("data-stop-name") \|\| el.getAttribute("data-stop") \|\| (el.querySelector(".stop-name, .name, strong") \|\| el).textContent);` |
| SEAT_STATE | 259 | `var target = qs("#deck") \|\| qs(".deck") \|\| qs(".board-card") \|\| qs(".seats-shell");` |
| SEAT_STATE | 272 | `if(document.documentElement.classList.contains("seat-simple-mode")) return true;` |
| SEAT_STATE | 273 | `if(document.body.classList.contains("seat-simple-mode")) return true;` |
| SEAT_STATE | 277 | `var tripKey = String((window.SEATS_BOOT && window.SEATS_BOOT.tripKey) \|\| window.BAG_TRIP \|\| "default");` |
| SEAT_STATE | 291 | `if(btn.classList && btn.classList.contains("seat-simple-bottom-item")){` |
| SEAT_STATE | 296 | `var parent = btn.closest(".seat-simple-bottom-bar, .seat-simple-dock, .seat-simple-nav");` |
| STORAGE_STATE | 2 | `if(window.__stopFlowFocusPatchLoaded) return;` |
| STORAGE_STATE | 3 | `window.__stopFlowFocusPatchLoaded = true;` |
| STORAGE_STATE | 5 | `var overlayId = "stopFlowFocusOverlay";` |
| STORAGE_STATE | 6 | `var memoryKey = "muavin:selectedStop:" + String(window.TRIP_KEY \|\| window.BAG_TRIP \|\| location.pathname);` |
| STORAGE_STATE | 51 | `return cleanStopName(localStorage.getItem(memoryKey) \|\| "");` |
| STORAGE_STATE | 58 | `try{ localStorage.setItem(memoryKey, name); }catch(e){}` |
| STORAGE_STATE | 107 | `["#seatSimpleStop", "#topLiveStop"].forEach(function(sel){` |
| STORAGE_STATE | 265 | `window.openStopFlowFocus = openStopFocus;` |
| STORAGE_STATE | 266 | `window.closeStopFlowFocus = closeStopFocus;` |
| STORAGE_STATE | 278 | `var v = localStorage.getItem("seatUiMode:" + tripKey);` |
| STORAGE_STATE | 343 | `if(window.setSelectedStop.__stopFlowFocusHooked) return;` |
| STORAGE_STATE | 356 | `wrapped.__stopFlowFocusHooked = true;` |
| STORAGE_STATE | 363 | `if(window[fn].__stopFlowFocusHooked) return;` |
| STORAGE_STATE | 373 | `wrapped.__stopFlowFocusHooked = true;` |
| ASYNC_TIMING | 2 | `if(window.__stopFlowFocusPatchLoaded) return;` |
| ASYNC_TIMING | 3 | `window.__stopFlowFocusPatchLoaded = true;` |
| ASYNC_TIMING | 236 | `setTimeout(function(){` |
| ASYNC_TIMING | 258 | `setTimeout(function(){` |
| ASYNC_TIMING | 368 | `setTimeout(function(){` |
| ASYNC_TIMING | 384 | `document.addEventListener("DOMContentLoaded", installHooks);` |
| ASYNC_TIMING | 385 | `setTimeout(installHooks, 300);` |
| ASYNC_TIMING | 386 | `setTimeout(installHooks, 1000);` |

### C-ORTA / Skor 177 / `static/seats/patches/seat-layout-fab-pack.js`

| Kategori | Satır | İçerik |
| --- | ---: | --- |
| EVENT_RISK | 56 | `document.addEventListener("DOMContentLoaded", schedule);` |
| EVENT_RISK | 61 | `window.addEventListener("load", schedule);` |
| EVENT_RISK | 62 | `window.addEventListener("resize", schedule);` |
| EVENT_RISK | 63 | `window.addEventListener("orientationchange", schedule);` |
| EVENT_RISK | 64 | `window.addEventListener("scroll", schedule, true);` |
| EVENT_RISK | 88 | `document.addEventListener("DOMContentLoaded", function(){` |
| EVENT_RISK | 153 | `document.addEventListener("DOMContentLoaded", schedule);` |
| EVENT_RISK | 158 | `window.addEventListener("load", schedule);` |
| EVENT_RISK | 159 | `window.addEventListener("resize", schedule);` |
| EVENT_RISK | 160 | `window.addEventListener("orientationchange", schedule);` |
| EVENT_RISK | 161 | `window.addEventListener("scroll", schedule, true);` |
| EVENT_RISK | 162 | `window.addEventListener("driveModeChanged", schedule);` |
| SEAT_STATE | 7 | `return document.querySelector(sel);` |
| SEAT_STATE | 13 | `var seat43 = q("#seat-43");` |
| SEAT_STATE | 14 | `var seat51 = q("#seat-51");` |
| SEAT_STATE | 106 | `return document.querySelector(sel);` |
| SEAT_STATE | 112 | `var seat43 = q("#seat-43");` |
| SEAT_STATE | 113 | `var seat51 = q("#seat-51");` |
| ASYNC_TIMING | 3 | `if(window.__fabLeftGapMoveLoaded) return;` |
| ASYNC_TIMING | 4 | `window.__fabLeftGapMoveLoaded = true;` |
| ASYNC_TIMING | 52 | `timer = setTimeout(placeFabColumn, 80);` |
| ASYNC_TIMING | 55 | `if(document.readyState === "loading"){` |
| ASYNC_TIMING | 56 | `document.addEventListener("DOMContentLoaded", schedule);` |
| ASYNC_TIMING | 61 | `window.addEventListener("load", schedule);` |
| ASYNC_TIMING | 62 | `window.addEventListener("resize", schedule);` |
| ASYNC_TIMING | 63 | `window.addEventListener("orientationchange", schedule);` |
| ASYNC_TIMING | 66 | `var obs = new MutationObserver(schedule);` |
| ASYNC_TIMING | 74 | `setTimeout(placeFabColumn, 150);` |
| ASYNC_TIMING | 75 | `setTimeout(placeFabColumn, 600);` |
| ASYNC_TIMING | 76 | `setTimeout(placeFabColumn, 1400);` |
| ASYNC_TIMING | 83 | `window.dispatchEvent(new Event("resize"));` |
| ASYNC_TIMING | 87 | `if(document.readyState === "loading"){` |
| ASYNC_TIMING | 88 | `document.addEventListener("DOMContentLoaded", function(){` |
| ASYNC_TIMING | 89 | `setTimeout(refreshFabPosition, 120);` |
| ASYNC_TIMING | 90 | `setTimeout(refreshFabPosition, 600);` |
| ASYNC_TIMING | 93 | `setTimeout(refreshFabPosition, 120);` |
| ASYNC_TIMING | 94 | `setTimeout(refreshFabPosition, 600);` |
| ASYNC_TIMING | 97 | `setTimeout(refreshFabPosition, 1200);` |
| ASYNC_TIMING | 149 | `timer = setTimeout(place, 80);` |
| ASYNC_TIMING | 152 | `if(document.readyState === "loading"){` |
| ASYNC_TIMING | 153 | `document.addEventListener("DOMContentLoaded", schedule);` |
| ASYNC_TIMING | 158 | `window.addEventListener("load", schedule);` |
| ASYNC_TIMING | 159 | `window.addEventListener("resize", schedule);` |
| ASYNC_TIMING | 160 | `window.addEventListener("orientationchange", schedule);` |
| ASYNC_TIMING | 164 | `setTimeout(place, 150);` |
| ASYNC_TIMING | 165 | `setTimeout(place, 600);` |
| ASYNC_TIMING | 166 | `setTimeout(place, 1400);` |

### B-KRİTİK / Skor 160 / `static/seats/patches/seat-layout-fab-pack.css`

| Kategori | Satır | İçerik |
| --- | ---: | --- |
| MODAL_DIRECT | 161 | `backdrop-filter:blur(14px) !important;` |
| MODAL_DIRECT | 162 | `-webkit-backdrop-filter:blur(14px) !important;` |
| CSS_BLOCK_RISK | 18 | `transform:translateX(var(--right-seat-column-shift)) !important;` |
| CSS_BLOCK_RISK | 26 | `transform:translateX(calc(var(--right-seat-column-shift) * .35)) !important;` |
| CSS_BLOCK_RISK | 62 | `transform:none !important;` |
| CSS_BLOCK_RISK | 67 | `transform:none !important;` |
| CSS_BLOCK_RISK | 73 | `BOTTOM_ROW_51_54_EQUAL_SPACING yaması 14. satırın transformunu sıfırladığı için` |
| CSS_BLOCK_RISK | 82 | `transform:translateX(var(--right-seat-column-shift, 16px)) !important;` |
| CSS_BLOCK_RISK | 89 | `transform:translateX(var(--right-seat-column-shift, 18px)) !important;` |
| CSS_BLOCK_RISK | 102 | `bottom:auto !important;` |
| CSS_BLOCK_RISK | 103 | `z-index:45 !important;` |
| CSS_BLOCK_RISK | 109 | `pointer-events:auto !important;` |
| CSS_BLOCK_RISK | 168 | `top:5px;` |
| CSS_BLOCK_RISK | 170 | `transform:translateX(-50%);` |
| CSS_BLOCK_RISK | 177 | `pointer-events:none;` |
| CSS_BLOCK_RISK | 199 | `inset:-5px;` |
| CSS_BLOCK_RISK | 202 | `pointer-events:none;` |
| CSS_BLOCK_RISK | 224 | `transform:scale(.94) !important;` |
| CSS_BLOCK_RISK | 253 | `top:4px !important;` |
| CSS_BLOCK_RISK | 270 | `inset:-3px !important;` |
| CSS_BLOCK_RISK | 308 | `top:var(--fab-left-gap-top, 0px) !important;` |
| CSS_BLOCK_RISK | 310 | `bottom:auto !important;` |
| CSS_BLOCK_RISK | 311 | `transform:none !important;` |
| CSS_BLOCK_RISK | 340 | `overflow:visible !important;` |
| CSS_BLOCK_RISK | 341 | `z-index:90 !important;` |
| CSS_BLOCK_RISK | 348 | `top:4px !important;` |
| CSS_BLOCK_RISK | 350 | `transform:translateX(-50%) !important;` |
| CSS_BLOCK_RISK | 358 | `pointer-events:none !important;` |
| CSS_BLOCK_RISK | 383 | `inset:-3px !important;` |
| SEAT_STATE | 13 | `--right-seat-column-shift:16px;` |
| SEAT_STATE | 18 | `transform:translateX(var(--right-seat-column-shift)) !important;` |
| SEAT_STATE | 26 | `transform:translateX(calc(var(--right-seat-column-shift) * .35)) !important;` |
| SEAT_STATE | 34 | `--right-seat-column-shift:13px;` |
| SEAT_STATE | 43 | `--right-seat-column-shift:18px;` |
| SEAT_STATE | 48 | `--right-seat-column-shift:15px;` |
| SEAT_STATE | 82 | `transform:translateX(var(--right-seat-column-shift, 16px)) !important;` |
| SEAT_STATE | 89 | `transform:translateX(var(--right-seat-column-shift, 18px)) !important;` |

### B-KRİTİK / Skor 143 / `static/seats/patches/modal-bottom-nav-autohide.js`

| Kategori | Satır | İçerik |
| --- | ---: | --- |
| MODAL_DIRECT | 2 | `if(window.__muavinModalBottomNavAutohideV3) return;` |
| MODAL_DIRECT | 3 | `window.__muavinModalBottomNavAutohideV3 = true;` |
| MODAL_DIRECT | 24 | `function isWorkModalText(t){` |
| MODAL_DIRECT | 43 | `function workModalIsOpen(){` |
| MODAL_DIRECT | 45 | `"[role='dialog'], .modal, .modal-content, .sheet, .sheet-panel, .drawer, " +` |
| MODAL_DIRECT | 46 | `"[class*='modal'], [class*='sheet'], [class*='drawer'], [class*='panel'], form, section, div"` |
| MODAL_DIRECT | 54 | `// Modal geniş ve yüksek bir panel olmalı` |
| MODAL_DIRECT | 58 | `return isWorkModalText(textOf(el));` |
| MODAL_DIRECT | 98 | `var open = workModalIsOpen();` |
| MODAL_DIRECT | 100 | `document.body.classList.toggle("muavin-work-modal-open", open);` |
| MODAL_DIRECT | 106 | `nav.classList.add("muavin-hidden-bottom-nav-by-modal");` |
| MODAL_DIRECT | 109 | `document.querySelectorAll(".muavin-hidden-bottom-nav-by-modal").forEach(function(el){` |
| MODAL_DIRECT | 110 | `el.classList.remove("muavin-hidden-bottom-nav-by-modal");` |
| EVENT_RISK | 128 | `document.addEventListener("click", function(){` |
| EVENT_RISK | 134 | `document.addEventListener("input", scheduleApply, true);` |
| EVENT_RISK | 135 | `document.addEventListener("change", scheduleApply, true);` |
| EVENT_RISK | 136 | `window.addEventListener("resize", scheduleApply);` |
| EVENT_RISK | 137 | `window.addEventListener("scroll", scheduleApply, true);` |
| CSS_BLOCK_RISK | 18 | `if(cs.display === "none" \|\| cs.visibility === "hidden") return false;` |
| SEAT_STATE | 44 | `var nodes = Array.prototype.slice.call(document.querySelectorAll(` |
| SEAT_STATE | 63 | `var nodes = Array.prototype.slice.call(document.querySelectorAll(` |
| SEAT_STATE | 109 | `document.querySelectorAll(".muavin-hidden-bottom-nav-by-modal").forEach(function(el){` |
| ASYNC_TIMING | 122 | `requestAnimationFrame(function(){` |
| ASYNC_TIMING | 129 | `setTimeout(scheduleApply, 30);` |
| ASYNC_TIMING | 130 | `setTimeout(scheduleApply, 160);` |
| ASYNC_TIMING | 131 | `setTimeout(scheduleApply, 420);` |
| ASYNC_TIMING | 136 | `window.addEventListener("resize", scheduleApply);` |
| ASYNC_TIMING | 139 | `var obs = new MutationObserver(scheduleApply);` |
| ASYNC_TIMING | 147 | `setInterval(applyState, 700);` |

### C-ORTA / Skor 140 / `static/seats/patches/manual-ticket-system.js`

| Kategori | Satır | İçerik |
| --- | ---: | --- |
| EVENT_RISK | 202 | `document.addEventListener("DOMContentLoaded", schedule);` |
| EVENT_RISK | 207 | `window.addEventListener("load", schedule);` |
| EVENT_RISK | 209 | `document.addEventListener("click", function(){` |
| EVENT_RISK | 215 | `document.addEventListener("change", schedule, true);` |
| SEAT_STATE | 9 | `(window.SEATS_BOOT && window.SEATS_BOOT.tripKey) \|\|` |
| SEAT_STATE | 48 | `return document.getElementById("seat-" + no);` |
| SEAT_STATE | 54 | `let b = el.querySelector(".manual-ticket-badge");` |
| SEAT_STATE | 64 | `function seatAssigned(no){` |
| SEAT_STATE | 69 | `el.classList.contains("isAssigned") \|\|` |
| SEAT_STATE | 81 | `if(seatAssigned(no)){` |
| SEAT_STATE | 82 | `return "__assigned__";` |
| SEAT_STATE | 94 | `document.querySelectorAll(".seat[id^='seat-']").forEach(function(el){` |
| SEAT_STATE | 95 | `const no = String(el.dataset.seat \|\| (el.id \|\| "").replace(/^seat-/, "") \|\| "").trim();` |
| SEAT_STATE | 106 | `if(savedSig && seatAssigned(no) && curSig && savedSig === curSig){` |
| SEAT_STATE | 115 | `if(savedSig && seatAssigned(no) && curSig && savedSig !== curSig){` |
| SEAT_STATE | 138 | `if(!el \|\| !seatAssigned(no)){` |
| STORAGE_STATE | 27 | `const raw = localStorage.getItem(sigKey()) \|\| "{}";` |
| STORAGE_STATE | 37 | `localStorage.setItem(sigKey(), JSON.stringify(obj \|\| {}));` |
| STORAGE_STATE | 43 | `localStorage.setItem(legacyKey(), "[]");` |
| ASYNC_TIMING | 25 | `function loadMap(){` |
| ASYNC_TIMING | 91 | `const map = loadMap();` |
| ASYNC_TIMING | 131 | `const map = loadMap();` |
| ASYNC_TIMING | 161 | `setTimeout(applyBadges, 150);` |
| ASYNC_TIMING | 162 | `setTimeout(applyBadges, 600);` |
| ASYNC_TIMING | 163 | `setTimeout(applyBadges, 1200);` |
| ASYNC_TIMING | 173 | `const map = loadMap();` |
| ASYNC_TIMING | 198 | `timer = setTimeout(applyBadges, 180);` |
| ASYNC_TIMING | 201 | `if(document.readyState === "loading"){` |
| ASYNC_TIMING | 202 | `document.addEventListener("DOMContentLoaded", schedule);` |
| ASYNC_TIMING | 207 | `window.addEventListener("load", schedule);` |
| ASYNC_TIMING | 210 | `setTimeout(schedule, 250);` |
| ASYNC_TIMING | 211 | `setTimeout(schedule, 900);` |
| ASYNC_TIMING | 212 | `setTimeout(schedule, 1600);` |
| ASYNC_TIMING | 217 | `const obs = new MutationObserver(schedule);` |
| ASYNC_TIMING | 225 | `setTimeout(applyBadges, 500);` |
| ASYNC_TIMING | 226 | `setTimeout(applyBadges, 1400);` |

### C-ORTA / Skor 137 / `static/seats/patches/top-sound-toggle.js`

| Kategori | Satır | İçerik |
| --- | ---: | --- |
| EVENT_RISK | 109 | `btn.addEventListener("click", function(e){` |
| EVENT_RISK | 110 | `e.preventDefault();` |
| EVENT_RISK | 111 | `e.stopPropagation();` |
| EVENT_RISK | 135 | `document.addEventListener("DOMContentLoaded", schedule);` |
| EVENT_RISK | 140 | `window.addEventListener("load", schedule);` |
| EVENT_RISK | 141 | `window.addEventListener("resize", schedule);` |
| EVENT_RISK | 142 | `window.addEventListener("ttsEnabledChanged", syncButton);` |
| EVENT_RISK | 144 | `document.addEventListener("change", function(e){` |
| SEAT_STATE | 8 | `return document.querySelector(sel);` |
| SEAT_STATE | 21 | `if(window.SeatsVoice && typeof window.SeatsVoice.isEnabled === "function"){` |
| SEAT_STATE | 22 | `return !!window.SeatsVoice.isEnabled();` |
| SEAT_STATE | 32 | `if(window.SeatsVoice && typeof window.SeatsVoice.setEnabled === "function"){` |
| SEAT_STATE | 33 | `window.SeatsVoice.setEnabled(on);` |
| SEAT_STATE | 55 | `if(window.SeatsVoice && typeof window.SeatsVoice.stop === "function"){` |
| SEAT_STATE | 56 | `window.SeatsVoice.stop();` |
| SEAT_STATE | 57 | `}else if(window.SeatsStopVoice){` |
| SEAT_STATE | 58 | `window.SeatsStopVoice();` |
| SEAT_STATE | 116 | `if(next && window.SeatsSpeak){` |
| SEAT_STATE | 117 | `try{ window.SeatsSpeak("Sesli asistan açık.", {force:true}); }catch(_){}` |
| STORAGE_STATE | 13 | `return (localStorage.getItem(KEY) ?? "1") === "1";` |
| STORAGE_STATE | 35 | `localStorage.setItem(KEY, on ? "1" : "0");` |
| STORAGE_STATE | 38 | `try{ localStorage.setItem(KEY, on ? "1" : "0"); }catch(e){}` |
| ASYNC_TIMING | 2 | `if(window.__topSoundToggleLoaded) return;` |
| ASYNC_TIMING | 3 | `window.__topSoundToggleLoaded = true;` |
| ASYNC_TIMING | 131 | `timer = setTimeout(ensureButton, 80);` |
| ASYNC_TIMING | 134 | `if(document.readyState === "loading"){` |
| ASYNC_TIMING | 135 | `document.addEventListener("DOMContentLoaded", schedule);` |
| ASYNC_TIMING | 140 | `window.addEventListener("load", schedule);` |
| ASYNC_TIMING | 141 | `window.addEventListener("resize", schedule);` |
| ASYNC_TIMING | 150 | `var obs = new MutationObserver(schedule);` |
| ASYNC_TIMING | 156 | `setTimeout(ensureButton, 150);` |
| ASYNC_TIMING | 157 | `setTimeout(ensureButton, 600);` |
| ASYNC_TIMING | 158 | `setTimeout(ensureButton, 1400);` |

### C-ORTA / Skor 82 / `static/seats/patches/stop-flow-compact-mobile.css`

| Kategori | Satır | İçerik |
| --- | ---: | --- |
| CSS_BLOCK_RISK | 19 | `margin-bottom:8px !important;` |
| CSS_BLOCK_RISK | 33 | `overflow:hidden !important;` |
| CSS_BLOCK_RISK | 34 | `text-overflow:ellipsis !important;` |
| CSS_BLOCK_RISK | 44 | `margin-top:6px !important;` |
| CSS_BLOCK_RISK | 75 | `margin-top:4px !important;` |
| CSS_BLOCK_RISK | 84 | `overflow:hidden !important;` |
| CSS_BLOCK_RISK | 85 | `text-overflow:ellipsis !important;` |
| STORAGE_STATE | 5 | `#stopFlowFocusOverlay{` |
| STORAGE_STATE | 9 | `#stopFlowFocusOverlay .stop-focus-panel{` |
| STORAGE_STATE | 14 | `#stopFlowFocusOverlay .stop-focus-head{` |
| STORAGE_STATE | 18 | `#stopFlowFocusOverlay .stop-focus-topline{` |
| STORAGE_STATE | 23 | `#stopFlowFocusOverlay .stop-focus-back{` |
| STORAGE_STATE | 29 | `#stopFlowFocusOverlay .stop-focus-badge{` |
| STORAGE_STATE | 37 | `#stopFlowFocusOverlay .stop-focus-title{` |
| STORAGE_STATE | 43 | `#stopFlowFocusOverlay .stop-focus-sub{` |
| STORAGE_STATE | 49 | `#stopFlowFocusOverlay .stop-focus-list{` |
| STORAGE_STATE | 54 | `#stopFlowFocusOverlay .stop-focus-card{` |
| STORAGE_STATE | 61 | `#stopFlowFocusOverlay .stop-focus-pin{` |
| STORAGE_STATE | 69 | `#stopFlowFocusOverlay .stop-focus-name{` |
| STORAGE_STATE | 74 | `#stopFlowFocusOverlay .stop-focus-meta{` |
| STORAGE_STATE | 80 | `#stopFlowFocusOverlay .stop-focus-select{` |
| STORAGE_STATE | 90 | `#stopFlowFocusOverlay .stop-focus-title{` |
| STORAGE_STATE | 94 | `#stopFlowFocusOverlay .stop-focus-card{` |
| STORAGE_STATE | 99 | `#stopFlowFocusOverlay .stop-focus-name{` |
| STORAGE_STATE | 103 | `#stopFlowFocusOverlay .stop-focus-meta{` |

### C-ORTA / Skor 62 / `static/seats/patches/stop-flow-focus-patch.css`

| Kategori | Satır | İçerik |
| --- | ---: | --- |
| CSS_BLOCK_RISK | 3 | `overflow:hidden !important;` |
| CSS_BLOCK_RISK | 8 | `position:fixed;` |
| CSS_BLOCK_RISK | 9 | `inset:0;` |
| CSS_BLOCK_RISK | 10 | `z-index:2147483000;` |
| CSS_BLOCK_RISK | 21 | `display:none !important;` |
| CSS_BLOCK_RISK | 33 | `overflow:hidden;` |
| CSS_BLOCK_RISK | 40 | `border-bottom:1px solid rgba(120,160,255,.18);` |
| CSS_BLOCK_RISK | 49 | `margin-bottom:14px;` |
| CSS_BLOCK_RISK | 96 | `overflow:auto;` |
| CSS_BLOCK_RISK | 100 | `-webkit-overflow-scrolling:touch;` |
| CSS_BLOCK_RISK | 119 | `transform:scale(.985);` |
| CSS_BLOCK_RISK | 150 | `overflow:hidden;` |
| CSS_BLOCK_RISK | 151 | `text-overflow:ellipsis;` |
| CSS_BLOCK_RISK | 157 | `margin-top:6px;` |
| STORAGE_STATE | 7 | `#stopFlowFocusOverlay{` |
| STORAGE_STATE | 20 | `#stopFlowFocusOverlay[hidden]{` |

### B-KRİTİK / Skor 60 / `static/seats/patches/stop-selected-toast.css`

| Kategori | Satır | İçerik |
| --- | ---: | --- |
| MODAL_DIRECT | 31 | `backdrop-filter:blur(16px);` |
| MODAL_DIRECT | 32 | `-webkit-backdrop-filter:blur(16px);` |
| CSS_BLOCK_RISK | 2 | `position:fixed;` |
| CSS_BLOCK_RISK | 4 | `bottom:calc(env(safe-area-inset-bottom, 0px) + 92px);` |
| CSS_BLOCK_RISK | 5 | `transform:translateX(-50%) translateY(22px) scale(.96);` |
| CSS_BLOCK_RISK | 6 | `z-index:2147483600;` |
| CSS_BLOCK_RISK | 9 | `opacity:0;` |
| CSS_BLOCK_RISK | 10 | `pointer-events:none;` |
| CSS_BLOCK_RISK | 11 | `transition:opacity .22s ease, transform .22s ease;` |
| CSS_BLOCK_RISK | 15 | `opacity:1;` |
| CSS_BLOCK_RISK | 16 | `transform:translateX(-50%) translateY(0) scale(1);` |
| CSS_BLOCK_RISK | 58 | `overflow:hidden;` |
| CSS_BLOCK_RISK | 59 | `text-overflow:ellipsis;` |
| CSS_BLOCK_RISK | 64 | `margin-top:4px;` |

### B-KRİTİK / Skor 58 / `static/seats/patches/seat-label-ghost-clean.css`

| Kategori | Satır | İçerik |
| --- | ---: | --- |
| MODAL_DIRECT | 32 | `backdrop-filter:none !important;` |
| MODAL_DIRECT | 33 | `-webkit-backdrop-filter:none !important;` |
| CSS_BLOCK_RISK | 13 | `display:none !important;` |
| CSS_BLOCK_RISK | 22 | `opacity:0 !important;` |
| CSS_BLOCK_RISK | 23 | `overflow:hidden !important;` |
| CSS_BLOCK_RISK | 40 | `opacity:.92 !important;` |
| SEAT_STATE | 10 | `html.seat-simple-mode .deck .cell .label:empty,` |
| SEAT_STATE | 11 | `body.seat-simple-mode .deck .cell .label:empty,` |
| SEAT_STATE | 27 | `html.seat-simple-mode .deck .cell .label,` |
| SEAT_STATE | 28 | `body.seat-simple-mode .deck .cell .label{` |
| SEAT_STATE | 37 | `html.seat-simple-mode .deck .cell .label:not(:empty),` |
| SEAT_STATE | 38 | `body.seat-simple-mode .deck .cell .label:not(:empty){` |

### C-ORTA / Skor 49 / `static/seats/patches/manual-ticket-system.css`

| Kategori | Satır | İçerik |
| --- | ---: | --- |
| CSS_BLOCK_RISK | 14 | `bottom:-8px;` |
| CSS_BLOCK_RISK | 19 | `display:none;` |
| CSS_BLOCK_RISK | 31 | `z-index:12;` |
| CSS_BLOCK_RISK | 32 | `pointer-events:none;` |
| CSS_BLOCK_RISK | 41 | `bottom:-9px;` |
| CSS_BLOCK_RISK | 50 | `bottom:-7px;` |
| SEAT_STATE | 7 | `.seat{` |
| SEAT_STATE | 11 | `.seat .manual-ticket-badge{` |
| SEAT_STATE | 35 | `.seat.has-manual-ticket-badge-sig .manual-ticket-badge{` |
| SEAT_STATE | 39 | `body.drive-mode .seat .manual-ticket-badge{` |
| SEAT_STATE | 48 | `.seat .manual-ticket-badge{` |

### B-KRİTİK / Skor 22 / `static/seats/patches/modal-bottom-nav-autohide.css`

| Kategori | Satır | İçerik |
| --- | ---: | --- |
| MODAL_DIRECT | 1 | `body.muavin-work-modal-open .muavin-hidden-bottom-nav-by-modal{` |
| CSS_BLOCK_RISK | 2 | `display:none !important;` |
| CSS_BLOCK_RISK | 3 | `opacity:0 !important;` |
| CSS_BLOCK_RISK | 4 | `visibility:hidden !important;` |
| CSS_BLOCK_RISK | 5 | `pointer-events:none !important;` |

### C-ORTA / Skor 19 / `static/seats/patches/stop-selected-toast.js`

| Kategori | Satır | İçerik |
| --- | ---: | --- |
| EVENT_RISK | 59 | `document.addEventListener("muavin:selected-stop-change", function(e){` |
| SEAT_STATE | 39 | `var title = el.querySelector("[data-stop-toast-title]");` |
| ASYNC_TIMING | 2 | `if(window.__stopSelectedToastPatchLoaded) return;` |
| ASYNC_TIMING | 3 | `window.__stopSelectedToastPatchLoaded = true;` |
| ASYNC_TIMING | 52 | `timer = setTimeout(function(){` |

### C-ORTA / Skor 4 / `static/seats/patches/top-sound-toggle.css`

| Kategori | Satır | İçerik |
| --- | ---: | --- |
| CSS_BLOCK_RISK | 45 | `transform:scale(.985);` |

### D-DÜŞÜK / Skor 0 / `static/seats/patches/bottom-voice-command.css`

_Kritik iz bulunmadı._


## 5) İlk Teknik Yorum

- `A-ÇOK KRİTİK` çıkan dosyalar doğrudan koltuk kaydetme/currentSeat/openSeat/saveSeat akışına temas ediyor olabilir.
- `B-KRİTİK` çıkan dosyalar modal, backdrop, z-index, pointer-events veya click davranışıyla Kaydet butonunu dolaylı bozabilir.
- `C-ORTA` daha çok görsel veya etkileşim katmanı olabilir.
- Bu rapordan sonra devre dışı bırakma değil, önce en yüksek skorlu 2-3 dosyanın içeriği okunmalı.