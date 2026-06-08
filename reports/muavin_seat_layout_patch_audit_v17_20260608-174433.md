# Muavin Koltuk Yerleşimi Yama Audit V17

- Tarih: `20260608-174433`
- Bu rapor sadece tespittir, dosya değiştirmez.

## 1) Aktif CSS / JS Linkleri

### `templates/seats.html`

| Satır | Link |
| ---: | --- |
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
| 16 | `<link rel="stylesheet" href="/static/seats/patches/unified-seat-deck-report-style.css?v=seat-smaller-removed-2">` |
| 17 | `<link rel="stylesheet" href="/static/seats/patches/mobile-performance-fix.css?v=2">` |
| 18 | `<link rel="stylesheet" href="/static/seats/patches/fab-sheet-solid-fix.css?v=1">` |
| 19 | `<link rel="stylesheet" href="/static/seats/patches/seat-label-ghost-clean.css?v=1">` |
| 373 | `<script src="/static/seats/patches/stop-selected-toast.js?v=1"></script>` |
| 374 | `<script src="/static/seats/patches/stop-flow-focus-patch.js?v=simple-scope-1"></script>` |
| 375 | `<script src="/static/seats/patches/seat-layout-fab-pack.js?v=1"></script>` |
| 376 | `<script src="/static/seats/patches/modal-bottom-nav-autohide.js?v=1"></script>` |
| 377 | `<script src="/static/seats/patches/manual-ticket-system.js?v=1"></script>` |
| 378 | `<script src="/static/seats/patches/top-sound-toggle.js?v=1"></script>` |
| 379 | `<script src="/static/seats/patches/seat-simple-ui-pack.js?v=1"></script>` |

### `android_app/app/src/main/python/templates/seats.html`

| Satır | Link |
| ---: | --- |
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
| 372 | `<script src="/static/seats/patches/stop-selected-toast.js?v=1"></script>` |
| 373 | `<script src="/static/seats/patches/stop-flow-focus-patch.js?v=simple-scope-1"></script>` |
| 374 | `<script src="/static/seats/patches/seat-layout-fab-pack.js?v=1"></script>` |
| 375 | `<script src="/static/seats/patches/modal-bottom-nav-autohide.js?v=1"></script>` |
| 376 | `<script src="/static/seats/patches/manual-ticket-system.js?v=1"></script>` |
| 377 | `<script src="/static/seats/patches/top-sound-toggle.js?v=1"></script>` |
| 378 | `<script src="/static/seats/patches/seat-simple-ui-pack.js?v=1"></script>` |

## 2) Fiziksel Patch Dosyaları

### `static/seats/patches`

- `bottom-row-51-54-equal-spacing.css`  ⭐
- `bottom-voice-command.css`
- `fab-sheet-solid-fix.css`
- `live-flow-v2.css.disabled_20260523_094130`
- `live-flow-v2.js.disabled_20260523_094130`
- `manual-ticket-system.css`
- `manual-ticket-system.js`
- `mobile-performance-fix.css`
- `mobile-performance-fix.css.bak_modal_readability_20260518_181100`
- `modal-bottom-nav-autohide.css`
- `modal-bottom-nav-autohide.js`
- `only-54-reapply-right-shift.css`  ⭐
- `right-seat-column-spacing-fix.css`  ⭐
- `seat-label-ghost-clean.css`  ⭐
- `seat-layout-fab-pack.css`  ⭐
- `seat-layout-fab-pack.js`  ⭐
- `seat-layout-fab-pack.js.bak-fab-overlap-v16b-20260608-173943`  ⭐
- `seat-layout-fab-pack.js.before-rollback-v16b-20260608-174157`  ⭐
- `seat-simple-ui-pack.css`  ⭐
- `seat-simple-ui-pack.js`  ⭐
- `stop-flow-compact-mobile.css`
- `stop-flow-focus-patch.css`
- `stop-flow-focus-patch.js`
- `stop-flow-focus-patch.js.bak_before_rollback_20260520_103515`
- `stop-flow-focus-patch.js.bak_live_runtime_sync_20260520_103326`
- `stop-flow-focus-patch.js.bak_scope_simple_only_20260520_105358`
- `stop-flow-focus-patch.js.bak_simple_scope_20260520_110612`
- `stop-selected-toast.css`
- `stop-selected-toast.js`
- `top-sound-toggle.css`
- `top-sound-toggle.js`
- `unified-seat-deck-report-style.css`  ⭐
- `unified-seat-deck-report-style.css.bak_before_remove_label_balance_20260521_212125`  ⭐
- `unified-seat-deck-report-style.css.bak_gap_20260521_211630`  ⭐
- `unified-seat-deck-report-style.css.bak_label_balance_20260521_212035`  ⭐
- `unified-seat-deck-report-style.css.bak_labels_20260521_211435`  ⭐
- `unified-seat-deck-report-style.css.bak_remove_smaller_20260521_212205`  ⭐
- `unified-seat-deck-report-style.css.bak_remove_smaller_20260521_212211`  ⭐
- `unified-seat-deck-report-style.css.bak_remove_smaller_20260521_212306`  ⭐
- `unified-seat-deck-report-style.css.bak_remove_smaller_20260521_212310`  ⭐
- `unified-seat-deck-report-style.css.bak_smaller_20260521_211902`  ⭐

### `android_app/app/src/main/python/static/seats/patches`

- `bottom-row-51-54-equal-spacing.css`  ⭐
- `bottom-voice-command.css`
- `fab-sheet-solid-fix.css`
- `manual-ticket-system.css`
- `manual-ticket-system.js`
- `mobile-performance-fix.css`
- `mobile-performance-fix.css.bak_modal_readability_20260518_181100`
- `modal-bottom-nav-autohide.css`
- `modal-bottom-nav-autohide.js`
- `only-54-reapply-right-shift.css`  ⭐
- `right-seat-column-spacing-fix.css`  ⭐
- `seat-label-ghost-clean.css`  ⭐
- `seat-layout-fab-pack.css`  ⭐
- `seat-layout-fab-pack.js`  ⭐
- `seat-layout-fab-pack.js.bak-fab-overlap-v16b-20260608-173943`  ⭐
- `seat-layout-fab-pack.js.before-rollback-v16b-20260608-174157`  ⭐
- `seat-simple-ui-pack.css`  ⭐
- `seat-simple-ui-pack.js`  ⭐
- `stop-flow-compact-mobile.css`
- `stop-flow-focus-patch.css`
- `stop-flow-focus-patch.js`
- `stop-flow-focus-patch.js.bak_before_rollback_20260520_103515`
- `stop-flow-focus-patch.js.bak_live_runtime_sync_20260520_103326`
- `stop-flow-focus-patch.js.bak_scope_simple_only_20260520_105358`
- `stop-flow-focus-patch.js.bak_simple_scope_20260520_110612`
- `stop-flow-focus-patch.js.bak_sync_20260520_113916`
- `stop-selected-toast.css`
- `stop-selected-toast.js`
- `top-sound-toggle.css`
- `top-sound-toggle.js`

## 3) Koltuk Yerleşimiyle İlgili Satırlar

### `templates/seats.html`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 10 | `seat-layout` | `<link rel="stylesheet" href="/static/seats/patches/seat-layout-fab-pack.css?v=1">` |
| 16 | `deck` | `<link rel="stylesheet" href="/static/seats/patches/unified-seat-deck-report-style.css?v=seat-smaller-removed-2">` |
| 19 | `label` | `<link rel="stylesheet" href="/static/seats/patches/seat-label-ghost-clean.css?v=1">` |
| 29 | `label` | `          <button id="driveModeToggle" type="button" aria-label="Sürüş modu">🚘 Sürüş</button>` |
| 59 | `deck` | `              <button class="voice-command-btn" id="btnDeckAI" type="button" title="Sesli Komut">` |
| 73 | `deck` | `  <button class="drive-voice-btn" id="btnDeckAIDrive" type="button" title="Sesli Komut">` |
| 99 | `deck` | `        {% include "seats_parts/deck.html" %}` |
| 197 | `label` | `              <label class="field">` |
| 202 | `label` | `              </label>` |
| 205 | `label` | `                <label class="field">` |
| 208 | `label` | `                </label>` |
| 210 | `label` | `                <label class="field">` |
| 213 | `label` | `                </label>` |
| 217 | `label` | `                <label><input type="checkbox" id="soundToggle" checked> Sesli yanıt</label>` |
| 218 | `label` | `                <label><input type="checkbox" id="autoAdvanceToggle" checked> Oto ilerle</label>` |
| 237 | `label` | `              <label class="field">` |
| 240 | `label` | `              </label>` |
| 243 | `label` | `                <label class="field">` |
| 246 | `label` | `                </label>` |
| 247 | `label` | `                <label class="field">` |
| 250 | `label` | `                </label>` |
| 295 | `ghost` | `              <button class="btn ghost" type="button" id="openStandingModalBtn">Ayakta Listesi</button>` |
| 375 | `seat-layout` | `<script src="/static/seats/patches/seat-layout-fab-pack.js?v=1"></script>` |
| 445 | `43` | `@media(max-width:430px){` |
| 791 | `43` | `@media(max-width:430px){` |
| 799 | `43` | `    height:43px !important;` |
| 800 | `43` | `    min-height:43px !important;` |
| 809 | `43` | `    height:43px !important;` |
| 810 | `43` | `    min-height:43px !important;` |
| 928 | `deck` | `    const fakeBtn = document.getElementById("btnDeckAIDrive");` |
| 929 | `deck` | `    const realBtn = document.getElementById("btnDeckAI");` |
| 1008 | `deck` | `      if(window.SeatsVoice && typeof window.SeatsVoice.startDeckAIVoice === "function"){` |
| 1009 | `deck` | `        window.SeatsVoice.startDeckAIVoice();` |
| 1014 | `deck` | `    const btn = q("#btnDeckAI") \|\| q("#btnDeckAIDrive");` |
| 1045 | `label` | `      <button type="button" class="seat-simple-bottom-item warn" id="seatSimpleVoiceBtn" title="Sesli Komut" aria-label="Sesli Komut">` |

### `android_app/app/src/main/python/templates/seats.html`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 10 | `seat-layout` | `<link rel="stylesheet" href="/static/seats/patches/seat-layout-fab-pack.css?v=1">` |
| 18 | `label` | `<link rel="stylesheet" href="/static/seats/patches/seat-label-ghost-clean.css?v=1">` |
| 28 | `label` | `          <button id="driveModeToggle" type="button" aria-label="Sürüş modu">🚘 Sürüş</button>` |
| 58 | `deck` | `              <button class="voice-command-btn" id="btnDeckAI" type="button" title="Sesli Komut">` |
| 72 | `deck` | `  <button class="drive-voice-btn" id="btnDeckAIDrive" type="button" title="Sesli Komut">` |
| 98 | `deck` | `        {% include "seats_parts/deck.html" %}` |
| 196 | `label` | `              <label class="field">` |
| 201 | `label` | `              </label>` |
| 204 | `label` | `                <label class="field">` |
| 207 | `label` | `                </label>` |
| 209 | `label` | `                <label class="field">` |
| 212 | `label` | `                </label>` |
| 216 | `label` | `                <label><input type="checkbox" id="soundToggle" checked> Sesli yanıt</label>` |
| 217 | `label` | `                <label><input type="checkbox" id="autoAdvanceToggle" checked> Oto ilerle</label>` |
| 236 | `label` | `              <label class="field">` |
| 239 | `label` | `              </label>` |
| 242 | `label` | `                <label class="field">` |
| 245 | `label` | `                </label>` |
| 246 | `label` | `                <label class="field">` |
| 249 | `label` | `                </label>` |
| 294 | `ghost` | `              <button class="btn ghost" type="button" id="openStandingModalBtn">Ayakta Listesi</button>` |
| 374 | `seat-layout` | `<script src="/static/seats/patches/seat-layout-fab-pack.js?v=1"></script>` |
| 444 | `43` | `@media(max-width:430px){` |
| 790 | `43` | `@media(max-width:430px){` |
| 798 | `43` | `    height:43px !important;` |
| 799 | `43` | `    min-height:43px !important;` |
| 808 | `43` | `    height:43px !important;` |
| 809 | `43` | `    min-height:43px !important;` |
| 927 | `deck` | `    const fakeBtn = document.getElementById("btnDeckAIDrive");` |
| 928 | `deck` | `    const realBtn = document.getElementById("btnDeckAI");` |
| 1007 | `deck` | `      if(window.SeatsVoice && typeof window.SeatsVoice.startDeckAIVoice === "function"){` |
| 1008 | `deck` | `        window.SeatsVoice.startDeckAIVoice();` |
| 1013 | `deck` | `    const btn = q("#btnDeckAI") \|\| q("#btnDeckAIDrive");` |
| 1044 | `label` | `      <button type="button" class="seat-simple-bottom-item warn" id="seatSimpleVoiceBtn" title="Sesli Komut" aria-label="Sesli Komut">` |

### `static/seats/seats.css`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 557 | `deck` | `  .deck-wrap{` |
| 564 | `deck` | `  .deck{` |
| 576 | `corr` | `  .corr{` |
| 577 | `grid-column` | `    grid-column:2;` |
| 578 | `grid-row` | `    grid-row:1/15;` |
| 596 | `grid-column` | `    grid-column:3/5;` |
| 597 | `grid-row` | `    grid-row:7;` |
| 601 | `51` | `    background:linear-gradient(180deg,#a16d24,#7b551b);` |
| 612 | `cell` | `  .cell{` |
| 674 | `label` | `  .label{` |
| 753 | `43` | `  .fab.green{ background:linear-gradient(180deg, #22c55e, #16843f); }` |
| 779 | `54` | `    width:54px;` |
| 1020 | `label` | `  label.field{` |
| 1065 | `label` | `  .toggle-line label{` |
| 1088 | `ghost` | `  .btn.ghost{ background:rgba(255,255,255,.05); border:1px solid var(--line); }` |
| 1245 | `translateX` | `    transform:translateX(-50%);` |
| 1264 | `label` | `  .radio-row label,` |
| 1265 | `label` | `  .check-row label{` |
| 1373 | `deck` | `    .deck-wrap{` |
| 1385 | `54` | `      width:54px;` |
| 1386 | `54` | `      height:54px;` |
| 1514 | `deck` | `    .deck{` |
| 1518 | `corr` | `    .corr{` |
| 1519 | `54` | `      width:54px;` |
| 1625 | `51` | `  border-color:rgba(251,191,36,.9) !important;` |
| 1627 | `51` | `    0 0 0 1px rgba(251,191,36,.42),` |
| 1724 | `54` | `    min-height:54px;` |
| 2210 | `deck` | `body.drive-mode .deck{` |
| 2216 | `label` | `body.drive-mode .label{` |
| 2229 | `cell` | `body.drive-mode .cell{` |
| 2321 | `label` | `  body.drive-mode .label{` |
| 2411 | `deck` | `.deck{` |
| 2436 | `deck` | `body.drive-mode .deck{` |
| 2482 | `deck` | `/* Deck biraz daha ortaya otursun */` |
| 2483 | `deck` | `body.drive-mode .deck-wrap{` |
| 2490 | `deck` | `body.drive-mode .deck{` |
| 2498 | `label` | `body.drive-mode .label{` |
| 2511 | `cell` | `body.drive-mode .cell{` |
| 2528 | `deck` | `  body.drive-mode .deck{` |
| 2537 | `label` | `  body.drive-mode .label{` |
| 2546 | `KORİDOR` | `   SÜRÜŞ MODU KORİDOR ALT HİZALAMA` |
| 2547 | `51` | `   Koridor 51-52-53-54 arka sıranın altına taşmasın` |
| 2550 | `corr` | `body.drive-mode .corr{` |
| 2551 | `grid-row` | `  grid-row:1 / 14 !important;` |
| 2557 | `corr` | `.corr{` |
| 2558 | `grid-row` | `  grid-row:1 / 14;` |
| 2569 | `deck` | `/* Deck içinde butonlara alt boşluk bırak */` |
| 2577 | `translateX` | `  transform:translateX(-50%) !important;` |
| 2622 | `51` | `/* 51-52-53-54 satırı ile çakışmasın */` |
| 2623 | `deck` | `body.drive-mode .deck{` |
| 2649 | `deck` | `  body.drive-mode .deck{` |
| 2657 | `51` | `   51-52-53-54 ile buton barı arasındaki fazla boşluğu azaltır` |
| 2665 | `deck` | `/* Deck-wrap ekstra boşluk vermesin */` |
| 2666 | `deck` | `body.drive-mode .deck-wrap{` |
| 2671 | `deck` | `body.drive-mode .deck{` |
| 2675 | `51-54` | `/* Alt hızlı işlem barını 51-54 satırına daha yakın taşı */` |
| 2699 | `deck` | `  body.drive-mode .deck{` |
| 2870 | `54` | `    min-height:54px;` |
| 3003 | `54` | `  width:154px !important;` |
| 3021 | `54` | `  width:154px !important;` |
| 3022 | `54` | `  min-width:154px !important;` |
| 3042 | `54` | `  width:154px !important;` |
| 3100 | `43` | `    min-height:43px !important;` |
| 3637 | `translateX` | `  transform:translateX(-40%) rotate(8deg);` |
| 3678 | `translateX` | `    transform:translateX(-45%) rotate(8deg);` |
| 3685 | `translateX` | `    transform:translateX(45%) rotate(8deg);` |
| 3727 | `54` | `    height:54px !important;` |
| 3772 | `54` | `  height:54px !important;` |
| 3943 | `translateX` | `  transform:translateX(-10px) !important;` |
| 3966 | `translateX` | `    transform:translateX(-14px) !important;` |
| 3983 | `translateX` | `    transform:translateX(-18px) !important;` |
| 3993 | `translateX` | `  transform:translateX(-6px) !important;` |
| 3998 | `translateX` | `    transform:translateX(-8px) !important;` |
| 4004 | `translateX` | `    transform:translateX(-10px) !important;` |
| 4014 | `translateX` | `  transform:translateX(2px) !important;` |
| 4019 | `translateX` | `    transform:translateX(0px) !important;` |
| 4025 | `translateX` | `    transform:translateX(-2px) !important;` |
| 4079 | `54` | `  min-height:54px !important;` |
| 4084 | `54` | `  height:54px !important;` |
| 4100 | `54` | `  min-height:54px !important;` |
| 4214 | `43` | `@media(max-width:430px){` |
| 4228 | `54` | `    min-height:54px !important;` |
| 4332 | `54` | `  height:54px !important;` |
| 4346 | `43` | `@media(max-width:430px){` |
| 4453 | `43` | `@media(max-width:430px){` |
| 4496 | `translateX` | `  transform:translateX(-50%) !important;` |
| 4536 | `54` | `  min-height:54px !important;` |
| 4537 | `54` | `  height:54px !important;` |
| 4549 | `label` | `#seatModal .radio-row label{` |
| 4568 | `label` | `#seatModal .check-row label{` |
| 4609 | `43` | `@media(max-width:430px){` |
| 4627 | `label` | `  #seatModal .radio-row label,` |
| 4628 | `label` | `  #seatModal .check-row label{` |
| 4732 | `51` | `/* Sadece en alt satır (51-52-53-54) altındaki iç boşluğu kapat */` |
| 4733 | `grid-row` | `.deck .cell[style*="grid-row:14;"]{` |
| 4737 | `grid-row` | `.deck .cell[style*="grid-row:14;"] .label:empty{` |
| 4748 | `51` | `/* 51-52-53-54 satırının altındaki iç boşluğu daha da daraltır */` |
| 4749 | `deck` | `.deck{` |
| 4755 | `grid-row` | `.deck .cell[style*="grid-row:14;"],` |
| 4756 | `grid-row` | `.deck .cell[style*="grid-row: 14;"]{` |
| 4761 | `grid-row` | `.deck .cell[style*="grid-row:14;"] .label:empty,` |
| 4762 | `grid-row` | `.deck .cell[style*="grid-row: 14;"] .label:empty{` |
| 4808 | `label` | `/* Koltuk altı label daha okunaklı */` |
| 4809 | `label` | `.label {` |

### `android_app/app/src/main/python/static/seats/seats.css`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 557 | `deck` | `  .deck-wrap{` |
| 564 | `deck` | `  .deck{` |
| 576 | `corr` | `  .corr{` |
| 577 | `grid-column` | `    grid-column:2;` |
| 578 | `grid-row` | `    grid-row:1/15;` |
| 596 | `grid-column` | `    grid-column:3/5;` |
| 597 | `grid-row` | `    grid-row:7;` |
| 601 | `51` | `    background:linear-gradient(180deg,#a16d24,#7b551b);` |
| 612 | `cell` | `  .cell{` |
| 674 | `label` | `  .label{` |
| 753 | `43` | `  .fab.green{ background:linear-gradient(180deg, #22c55e, #16843f); }` |
| 779 | `54` | `    width:54px;` |
| 1020 | `label` | `  label.field{` |
| 1065 | `label` | `  .toggle-line label{` |
| 1088 | `ghost` | `  .btn.ghost{ background:rgba(255,255,255,.05); border:1px solid var(--line); }` |
| 1245 | `translateX` | `    transform:translateX(-50%);` |
| 1264 | `label` | `  .radio-row label,` |
| 1265 | `label` | `  .check-row label{` |
| 1373 | `deck` | `    .deck-wrap{` |
| 1385 | `54` | `      width:54px;` |
| 1386 | `54` | `      height:54px;` |
| 1514 | `deck` | `    .deck{` |
| 1518 | `corr` | `    .corr{` |
| 1519 | `54` | `      width:54px;` |
| 1625 | `51` | `  border-color:rgba(251,191,36,.9) !important;` |
| 1627 | `51` | `    0 0 0 1px rgba(251,191,36,.42),` |
| 1724 | `54` | `    min-height:54px;` |
| 2210 | `deck` | `body.drive-mode .deck{` |
| 2216 | `label` | `body.drive-mode .label{` |
| 2229 | `cell` | `body.drive-mode .cell{` |
| 2321 | `label` | `  body.drive-mode .label{` |
| 2411 | `deck` | `.deck{` |
| 2436 | `deck` | `body.drive-mode .deck{` |
| 2482 | `deck` | `/* Deck biraz daha ortaya otursun */` |
| 2483 | `deck` | `body.drive-mode .deck-wrap{` |
| 2490 | `deck` | `body.drive-mode .deck{` |
| 2498 | `label` | `body.drive-mode .label{` |
| 2511 | `cell` | `body.drive-mode .cell{` |
| 2528 | `deck` | `  body.drive-mode .deck{` |
| 2537 | `label` | `  body.drive-mode .label{` |
| 2546 | `KORİDOR` | `   SÜRÜŞ MODU KORİDOR ALT HİZALAMA` |
| 2547 | `51` | `   Koridor 51-52-53-54 arka sıranın altına taşmasın` |
| 2550 | `corr` | `body.drive-mode .corr{` |
| 2551 | `grid-row` | `  grid-row:1 / 14 !important;` |
| 2557 | `corr` | `.corr{` |
| 2558 | `grid-row` | `  grid-row:1 / 14;` |
| 2569 | `deck` | `/* Deck içinde butonlara alt boşluk bırak */` |
| 2577 | `translateX` | `  transform:translateX(-50%) !important;` |
| 2622 | `51` | `/* 51-52-53-54 satırı ile çakışmasın */` |
| 2623 | `deck` | `body.drive-mode .deck{` |
| 2649 | `deck` | `  body.drive-mode .deck{` |
| 2657 | `51` | `   51-52-53-54 ile buton barı arasındaki fazla boşluğu azaltır` |
| 2665 | `deck` | `/* Deck-wrap ekstra boşluk vermesin */` |
| 2666 | `deck` | `body.drive-mode .deck-wrap{` |
| 2671 | `deck` | `body.drive-mode .deck{` |
| 2675 | `51-54` | `/* Alt hızlı işlem barını 51-54 satırına daha yakın taşı */` |
| 2699 | `deck` | `  body.drive-mode .deck{` |
| 2870 | `54` | `    min-height:54px;` |
| 3003 | `54` | `  width:154px !important;` |
| 3021 | `54` | `  width:154px !important;` |
| 3022 | `54` | `  min-width:154px !important;` |
| 3042 | `54` | `  width:154px !important;` |
| 3100 | `43` | `    min-height:43px !important;` |
| 3637 | `translateX` | `  transform:translateX(-40%) rotate(8deg);` |
| 3678 | `translateX` | `    transform:translateX(-45%) rotate(8deg);` |
| 3685 | `translateX` | `    transform:translateX(45%) rotate(8deg);` |
| 3727 | `54` | `    height:54px !important;` |
| 3772 | `54` | `  height:54px !important;` |
| 3943 | `translateX` | `  transform:translateX(-10px) !important;` |
| 3966 | `translateX` | `    transform:translateX(-14px) !important;` |
| 3983 | `translateX` | `    transform:translateX(-18px) !important;` |
| 3993 | `translateX` | `  transform:translateX(-6px) !important;` |
| 3998 | `translateX` | `    transform:translateX(-8px) !important;` |
| 4004 | `translateX` | `    transform:translateX(-10px) !important;` |
| 4014 | `translateX` | `  transform:translateX(2px) !important;` |
| 4019 | `translateX` | `    transform:translateX(0px) !important;` |
| 4025 | `translateX` | `    transform:translateX(-2px) !important;` |
| 4079 | `54` | `  min-height:54px !important;` |
| 4084 | `54` | `  height:54px !important;` |
| 4100 | `54` | `  min-height:54px !important;` |
| 4214 | `43` | `@media(max-width:430px){` |
| 4228 | `54` | `    min-height:54px !important;` |
| 4332 | `54` | `  height:54px !important;` |
| 4346 | `43` | `@media(max-width:430px){` |
| 4453 | `43` | `@media(max-width:430px){` |
| 4496 | `translateX` | `  transform:translateX(-50%) !important;` |
| 4536 | `54` | `  min-height:54px !important;` |
| 4537 | `54` | `  height:54px !important;` |
| 4549 | `label` | `#seatModal .radio-row label{` |
| 4568 | `label` | `#seatModal .check-row label{` |
| 4609 | `43` | `@media(max-width:430px){` |
| 4627 | `label` | `  #seatModal .radio-row label,` |
| 4628 | `label` | `  #seatModal .check-row label{` |
| 4732 | `51` | `/* Sadece en alt satır (51-52-53-54) altındaki iç boşluğu kapat */` |
| 4733 | `grid-row` | `.deck .cell[style*="grid-row:14;"]{` |
| 4737 | `grid-row` | `.deck .cell[style*="grid-row:14;"] .label:empty{` |
| 4748 | `51` | `/* 51-52-53-54 satırının altındaki iç boşluğu daha da daraltır */` |
| 4749 | `deck` | `.deck{` |
| 4755 | `grid-row` | `.deck .cell[style*="grid-row:14;"],` |
| 4756 | `grid-row` | `.deck .cell[style*="grid-row: 14;"]{` |
| 4761 | `grid-row` | `.deck .cell[style*="grid-row:14;"] .label:empty,` |
| 4762 | `grid-row` | `.deck .cell[style*="grid-row: 14;"] .label:empty{` |
| 4808 | `label` | `/* Koltuk altı label daha okunaklı */` |
| 4809 | `label` | `.label {` |

### `static/seats/seats-final.css`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 11 | `43` | `  --sf-card2:#15243a;` |
| 58 | `51` | `    linear-gradient(135deg,rgba(16,31,51,.96),rgba(7,17,31,.96)) !important;` |
| 177 | `51` | `  background:linear-gradient(135deg,rgba(16,31,51,.96),rgba(7,17,31,.96)) !important;` |
| 185 | `51` | `    linear-gradient(135deg,rgba(16,31,51,.96),rgba(7,17,31,.96)) !important;` |
| 230 | `51` | `    linear-gradient(180deg,rgba(16,31,51,.94),rgba(7,17,31,.94)) !important;` |
| 594 | `deck` | `   KOLTUK DECK` |
| 608 | `deck` | `.deck-wrap{` |
| 615 | `deck` | `.deck{` |
| 627 | `label` | `.label{` |
| 822 | `54` | `    min-height:54px !important;` |
| 893 | `54` | `  min-height:54px !important;` |
| 1115 | `54` | `  border-color:rgba(96,165,250,.54) !important;` |
| 1173 | `51` | `    radial-gradient(circle at 18% 0%, rgba(251,191,36,.25), transparent 38%),` |
| 1175 | `51` | `  border-color:rgba(251,191,36,.88) !important;` |
| 1177 | `51` | `    0 0 0 1px rgba(251,191,36,.36),` |
| 1336 | `51` | `  color:rgba(248,251,255,.88) !important;` |
| 1381 | `51` | `    radial-gradient(circle at 18% 0%, rgba(251,191,36,.34), transparent 38%),` |
| 1383 | `51` | `  border-color:rgba(251,191,36,.92) !important;` |
| 1385 | `51` | `    0 0 0 1px rgba(251,191,36,.42),` |
| 1530 | `label` | `.route-mini-label{` |
| 1571 | `translateX` | `    transform:translateX(0);` |
| 1574 | `translateX` | `    transform:translateX(-50%);` |
| 1610 | `label` | `.route-strip-shell:has(.route-stop.live-danger) .route-pill-live .route-mini-label,` |
| 1633 | `51` | `    radial-gradient(circle at 18% 0%, rgba(251,191,36,.30), transparent 36%),` |
| 1635 | `51` | `  border-color:rgba(251,191,36,.72) !important;` |
| 1637 | `51` | `    0 0 0 1px rgba(251,191,36,.28),` |
| 1642 | `label` | `.route-strip-shell:has(.route-stop.next-warning) .route-pill-next .route-mini-label,` |
| 1646 | `51` | `    0 0 8px rgba(251,191,36,.70),` |
| 1673 | `translateX` | `  transform:translateX(-50%) !important;` |
| 1734 | `deck` | `body.drive-mode .deck{` |
| 1738 | `43` | `@media(max-width:430px){` |
| 1742 | `54` | `    min-height:54px !important;` |
| 1756 | `deck` | `  body.drive-mode .deck{` |
| 1786 | `translateX` | `  transform:translateX(-50%) !important;` |
| 1858 | `43` | `@media(max-width:430px){` |
| 1877 | `54` | `    margin-top:54px !important;` |
| 1979 | `43` | `@media(max-width:430px){` |
| 2147 | `43` | `@media(max-width:430px){` |
| 2157 | `54` | `    height:54px !important;` |
| 2158 | `54` | `    min-height:54px !important;` |
| 2282 | `43` | `@media(max-width:430px){` |
| 2292 | `54` | `    height:54px !important;` |
| 2293 | `54` | `    min-height:54px !important;` |
| 2297 | `54` | `    height:54px !important;` |
| 2298 | `54` | `    min-height:54px !important;` |
| 2353 | `43` | `@media(max-width:430px){` |
| 2360 | `54` | `    height:54px !important;` |
| 2361 | `54` | `    min-height:54px !important;` |
| 2514 | `43` | `@media(max-width:430px){` |
| 2522 | `54` | `    height:54px !important;` |
| 2523 | `54` | `    min-height:54px !important;` |

### `android_app/app/src/main/python/static/seats/seats-final.css`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 11 | `43` | `  --sf-card2:#15243a;` |
| 58 | `51` | `    linear-gradient(135deg,rgba(16,31,51,.96),rgba(7,17,31,.96)) !important;` |
| 177 | `51` | `  background:linear-gradient(135deg,rgba(16,31,51,.96),rgba(7,17,31,.96)) !important;` |
| 185 | `51` | `    linear-gradient(135deg,rgba(16,31,51,.96),rgba(7,17,31,.96)) !important;` |
| 230 | `51` | `    linear-gradient(180deg,rgba(16,31,51,.94),rgba(7,17,31,.94)) !important;` |
| 594 | `deck` | `   KOLTUK DECK` |
| 608 | `deck` | `.deck-wrap{` |
| 615 | `deck` | `.deck{` |
| 627 | `label` | `.label{` |
| 822 | `54` | `    min-height:54px !important;` |
| 893 | `54` | `  min-height:54px !important;` |
| 1115 | `54` | `  border-color:rgba(96,165,250,.54) !important;` |
| 1173 | `51` | `    radial-gradient(circle at 18% 0%, rgba(251,191,36,.25), transparent 38%),` |
| 1175 | `51` | `  border-color:rgba(251,191,36,.88) !important;` |
| 1177 | `51` | `    0 0 0 1px rgba(251,191,36,.36),` |
| 1336 | `51` | `  color:rgba(248,251,255,.88) !important;` |
| 1381 | `51` | `    radial-gradient(circle at 18% 0%, rgba(251,191,36,.34), transparent 38%),` |
| 1383 | `51` | `  border-color:rgba(251,191,36,.92) !important;` |
| 1385 | `51` | `    0 0 0 1px rgba(251,191,36,.42),` |
| 1530 | `label` | `.route-mini-label{` |
| 1571 | `translateX` | `    transform:translateX(0);` |
| 1574 | `translateX` | `    transform:translateX(-50%);` |
| 1610 | `label` | `.route-strip-shell:has(.route-stop.live-danger) .route-pill-live .route-mini-label,` |
| 1633 | `51` | `    radial-gradient(circle at 18% 0%, rgba(251,191,36,.30), transparent 36%),` |
| 1635 | `51` | `  border-color:rgba(251,191,36,.72) !important;` |
| 1637 | `51` | `    0 0 0 1px rgba(251,191,36,.28),` |
| 1642 | `label` | `.route-strip-shell:has(.route-stop.next-warning) .route-pill-next .route-mini-label,` |
| 1646 | `51` | `    0 0 8px rgba(251,191,36,.70),` |
| 1673 | `translateX` | `  transform:translateX(-50%) !important;` |
| 1734 | `deck` | `body.drive-mode .deck{` |
| 1738 | `43` | `@media(max-width:430px){` |
| 1742 | `54` | `    min-height:54px !important;` |
| 1756 | `deck` | `  body.drive-mode .deck{` |
| 1786 | `translateX` | `  transform:translateX(-50%) !important;` |
| 1858 | `43` | `@media(max-width:430px){` |
| 1877 | `54` | `    margin-top:54px !important;` |
| 1979 | `43` | `@media(max-width:430px){` |
| 2147 | `43` | `@media(max-width:430px){` |
| 2157 | `54` | `    height:54px !important;` |
| 2158 | `54` | `    min-height:54px !important;` |
| 2282 | `43` | `@media(max-width:430px){` |
| 2292 | `54` | `    height:54px !important;` |
| 2293 | `54` | `    min-height:54px !important;` |
| 2297 | `54` | `    height:54px !important;` |
| 2298 | `54` | `    min-height:54px !important;` |
| 2353 | `43` | `@media(max-width:430px){` |
| 2360 | `54` | `    height:54px !important;` |
| 2361 | `54` | `    min-height:54px !important;` |
| 2514 | `43` | `@media(max-width:430px){` |
| 2522 | `54` | `    height:54px !important;` |
| 2523 | `54` | `    min-height:54px !important;` |

### `static/seats/patches/bottom-row-51-54-equal-spacing.css`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 2 | `51` | `    En alt sıra 51-52-53-54 eşit aralık düzeltmesi.` |
| 3 | `54` | `    Sağ kolon kaydırma 54'ü de etkilediği için bu satırda` |
| 4 | `51` | `    kaydırmayı sıfırlıyoruz. Böylece 51-52-53-54 kendi grid` |
| 8 | `grid-row` | `  .deck .cell[style*="grid-row:14"],` |
| 9 | `grid-row` | `  .deck .cell[style*="grid-row: 14"]{` |
| 13 | `grid-row` | `  body.drive-mode .deck .cell[style*="grid-row:14"],` |
| 14 | `grid-row` | `  body.drive-mode .deck .cell[style*="grid-row: 14"]{` |

### `static/seats/patches/manual-ticket-system.js`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 76 | `label` | `    const label = document.getElementById("label-" + no);` |
| 77 | `label` | `    const text = label ? String(label.textContent \|\| "").replace(/\s+/g, " ").trim() : "";` |

### `static/seats/patches/mobile-performance-fix.css`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 43 | `deck` | `  .deck,` |
| 67 | `cell` | `  .cell,` |
| 90 | `cell` | `  .cell,` |
| 100 | `cell` | `  .cell,` |
| 112 | `deck` | `  .deck,` |

### `static/seats/patches/only-54-reapply-right-shift.css`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 3 | `51` | `    BOTTOM_ROW_51_54_EQUAL_SPACING yaması 14. satırın transformunu sıfırladığı için` |
| 4 | `54` | `    sadece 54'e sağ kolon kaymasını geri veriyoruz.` |
| 5 | `51` | `    51-52-53'e dokunmaz.` |
| 8 | `grid-row` | `  .deck .cell[style*="grid-row:14"][style*="grid-column:4"],` |
| 9 | `grid-row` | `  .deck .cell[style*="grid-row:14"][style*="grid-column: 4"],` |
| 10 | `grid-row` | `  .deck .cell[style*="grid-row: 14"][style*="grid-column:4"],` |
| 11 | `grid-row` | `  .deck .cell[style*="grid-row: 14"][style*="grid-column: 4"]{` |
| 12 | `right-seat-column` | `    transform:translateX(var(--right-seat-column-shift, 16px)) !important;` |
| 15 | `grid-row` | `  body.drive-mode .deck .cell[style*="grid-row:14"][style*="grid-column:4"],` |
| 16 | `grid-row` | `  body.drive-mode .deck .cell[style*="grid-row:14"][style*="grid-column: 4"],` |
| 17 | `grid-row` | `  body.drive-mode .deck .cell[style*="grid-row: 14"][style*="grid-column:4"],` |
| 18 | `grid-row` | `  body.drive-mode .deck .cell[style*="grid-row: 14"][style*="grid-column: 4"]{` |
| 19 | `right-seat-column` | `    transform:translateX(var(--right-seat-column-shift, 18px)) !important;` |

### `static/seats/patches/right-seat-column-spacing-fix.css`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 3 | `54` | `    4,8,12,16,20,24,28,34,38,42,46,50,54 gibi` |
| 4 | `grid-column` | `    grid-column:4 olan koltukları biraz sağa alır.` |
| 11 | `deck` | `  .deck{` |
| 12 | `right-seat-column` | `    --right-seat-column-shift:16px;` |
| 15 | `grid-column` | `  .deck .cell[style*="grid-column:4"],` |
| 16 | `grid-column` | `  .deck .cell[style*="grid-column: 4"]{` |
| 17 | `right-seat-column` | `    transform:translateX(var(--right-seat-column-shift)) !important;` |
| 24 | `deck` | `  .deck .door{` |
| 25 | `right-seat-column` | `    transform:translateX(calc(var(--right-seat-column-shift) * .35)) !important;` |
| 32 | `deck` | `    .deck{` |
| 33 | `right-seat-column` | `      --right-seat-column-shift:13px;` |
| 41 | `deck` | `  body.drive-mode .deck{` |
| 42 | `right-seat-column` | `    --right-seat-column-shift:18px;` |
| 46 | `deck` | `    body.drive-mode .deck{` |
| 47 | `right-seat-column` | `      --right-seat-column-shift:15px;` |

### `static/seats/patches/seat-label-ghost-clean.css`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 2 | `label` | `   SEAT LABEL GHOST CLEAN` |
| 3 | `label` | `   Boş koltuk altı label kutularındaki kare karartmayı kaldırır.` |
| 4 | `label` | `   Dolu label yazısını korur.` |
| 9 | `label` | `  /* Boş label tamamen yok olsun */` |
| 10 | `deck` | `  html.seat-simple-mode .deck .cell .label:empty,` |
| 11 | `deck` | `  body.seat-simple-mode .deck .cell .label:empty,` |
| 12 | `deck` | `  .deck .cell .label:empty{` |
| 26 | `label` | `  /* Dolu label varsa yazı kalsın, kare arka plan kalksın */` |
| 27 | `deck` | `  html.seat-simple-mode .deck .cell .label,` |
| 28 | `deck` | `  body.seat-simple-mode .deck .cell .label{` |
| 36 | `label` | `  /* Label içindeki yazıyı okunur tut */` |
| 37 | `deck` | `  html.seat-simple-mode .deck .cell .label:not(:empty),` |
| 38 | `deck` | `  body.seat-simple-mode .deck .cell .label:not(:empty){` |

### `static/seats/patches/seat-layout-fab-pack.css`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 4 | `54` | `    4,8,12,16,20,24,28,34,38,42,46,50,54 gibi` |
| 5 | `grid-column` | `    grid-column:4 olan koltukları biraz sağa alır.` |
| 12 | `deck` | `  .deck{` |
| 13 | `right-seat-column` | `    --right-seat-column-shift:16px;` |
| 16 | `grid-column` | `  .deck .cell[style*="grid-column:4"],` |
| 17 | `grid-column` | `  .deck .cell[style*="grid-column: 4"]{` |
| 18 | `right-seat-column` | `    transform:translateX(var(--right-seat-column-shift)) !important;` |
| 25 | `deck` | `  .deck .door{` |
| 26 | `right-seat-column` | `    transform:translateX(calc(var(--right-seat-column-shift) * .35)) !important;` |
| 33 | `deck` | `    .deck{` |
| 34 | `right-seat-column` | `      --right-seat-column-shift:13px;` |
| 42 | `deck` | `  body.drive-mode .deck{` |
| 43 | `right-seat-column` | `    --right-seat-column-shift:18px;` |
| 47 | `deck` | `    body.drive-mode .deck{` |
| 48 | `right-seat-column` | `      --right-seat-column-shift:15px;` |
| 52 | `51` | `/* ===== BOTTOM_ROW_51_54_EQUAL_SPACING ===== */` |
| 54 | `51` | `    En alt sıra 51-52-53-54 eşit aralık düzeltmesi.` |
| 55 | `54` | `    Sağ kolon kaydırma 54'ü de etkilediği için bu satırda` |
| 56 | `51` | `    kaydırmayı sıfırlıyoruz. Böylece 51-52-53-54 kendi grid` |
| 60 | `grid-row` | `  .deck .cell[style*="grid-row:14"],` |
| 61 | `grid-row` | `  .deck .cell[style*="grid-row: 14"]{` |
| 65 | `grid-row` | `  body.drive-mode .deck .cell[style*="grid-row:14"],` |
| 66 | `grid-row` | `  body.drive-mode .deck .cell[style*="grid-row: 14"]{` |
| 70 | `54` | `/* ===== ONLY_54_REAPPLY_RIGHT_SHIFT ===== */` |
| 73 | `51` | `    BOTTOM_ROW_51_54_EQUAL_SPACING yaması 14. satırın transformunu sıfırladığı için` |
| 74 | `54` | `    sadece 54'e sağ kolon kaymasını geri veriyoruz.` |
| 75 | `51` | `    51-52-53'e dokunmaz.` |
| 78 | `grid-row` | `  .deck .cell[style*="grid-row:14"][style*="grid-column:4"],` |
| 79 | `grid-row` | `  .deck .cell[style*="grid-row:14"][style*="grid-column: 4"],` |
| 80 | `grid-row` | `  .deck .cell[style*="grid-row: 14"][style*="grid-column:4"],` |
| 81 | `grid-row` | `  .deck .cell[style*="grid-row: 14"][style*="grid-column: 4"]{` |
| 82 | `right-seat-column` | `    transform:translateX(var(--right-seat-column-shift, 16px)) !important;` |
| 85 | `grid-row` | `  body.drive-mode .deck .cell[style*="grid-row:14"][style*="grid-column:4"],` |
| 86 | `grid-row` | `  body.drive-mode .deck .cell[style*="grid-row:14"][style*="grid-column: 4"],` |
| 87 | `grid-row` | `  body.drive-mode .deck .cell[style*="grid-row: 14"][style*="grid-column:4"],` |
| 88 | `grid-row` | `  body.drive-mode .deck .cell[style*="grid-row: 14"][style*="grid-column: 4"]{` |
| 89 | `right-seat-column` | `    transform:translateX(var(--right-seat-column-shift, 18px)) !important;` |
| 95 | `51` | `    43 ile 51 arasındaki boş sol alana yerleştirir.` |
| 170 | `translateX` | `    transform:translateX(-50%);` |
| 175 | `54` | `    color:rgba(191,219,254,.92);` |
| 242 | `51` | `    Hızlı işlem paneli 43 ile 51 arasına tam otursun diye` |
| 300 | `51` | `    paneli tekrar 43-51 arasındaki dikey mini panel yap.` |
| 350 | `translateX` | `    transform:translateX(-50%) !important;` |
| 356 | `54` | `    color:rgba(191,219,254,.92) !important;` |

### `static/seats/patches/seat-layout-fab-pack.js`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 12 | `deck` | `    var wrap = q(".deck-wrap");` |
| 13 | `43` | `    var seat43 = q("#seat-43");` |
| 14 | `51` | `    var seat51 = q("#seat-51");` |
| 16 | `51` | `    if(!col \|\| !wrap \|\| !seat43 \|\| !seat51) return;` |
| 22 | `43` | `    var r43 = seat43.getBoundingClientRect();` |
| 23 | `51` | `    var r51 = seat51.getBoundingClientRect();` |
| 29 | `43` | `    var centerX43 = r43.left + (r43.width / 2);` |
| 30 | `51` | `    var centerX51 = r51.left + (r51.width / 2);` |
| 31 | `51` | `    var centerX = (centerX43 + centerX51) / 2;` |
| 33 | `43` | `    var gapTop = r43.bottom + 12;` |
| 34 | `51` | `    var gapBottom = r51.top - 12;` |
| 111 | `deck` | `    var wrap = q(".deck-wrap");` |
| 112 | `43` | `    var seat43 = q("#seat-43");` |
| 113 | `51` | `    var seat51 = q("#seat-51");` |
| 115 | `51` | `    if(!col \|\| !wrap \|\| !seat43 \|\| !seat51) return;` |
| 120 | `43` | `    var r43 = seat43.getBoundingClientRect();` |
| 121 | `51` | `    var r51 = seat51.getBoundingClientRect();` |
| 127 | `43` | `    var centerX43 = r43.left + (r43.width / 2);` |
| 128 | `51` | `    var centerX51 = r51.left + (r51.width / 2);` |
| 129 | `51` | `    var centerX = (centerX43 + centerX51) / 2;` |
| 131 | `43` | `    var gapTop = r43.bottom + 12;` |
| 132 | `51` | `    var gapBottom = r51.top - 12;` |

### `static/seats/patches/seat-simple-ui-pack.css`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 113 | `deck` | `/* koltuk deck yukarı gelsin */` |
| 114 | `deck` | `html.seat-simple-mode .deck-card,` |
| 115 | `deck` | `html.seat-simple-mode .seat-deck,` |
| 116 | `deck` | `html.seat-simple-mode .deck-shell{` |
| 121 | `43` | `@media(max-width:430px){` |
| 250 | `43` | `@media(max-width:430px){` |
| 267 | `49` | `    min-height:49px;` |
| 367 | `43` | `@media(max-width:430px){` |

### `static/seats/patches/stop-flow-compact-mobile.css`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 89 | `43` | `@media (max-width: 430px){` |

### `static/seats/patches/stop-flow-focus-patch.css`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 29 | `54` | `    border:1px solid rgba(110,154,255,.23);` |
| 105 | `51` | `    border:1px solid rgba(105,151,255,.24);` |

### `static/seats/patches/stop-flow-focus-patch.js`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 160 | `label` | `      '<div class="stop-focus-panel" role="dialog" aria-modal="true" aria-label="Durak Akışı">' +` |
| 259 | `deck` | `        var target = qs("#deck") \|\| qs(".deck") \|\| qs(".board-card") \|\| qs(".seats-shell");` |
| 310 | `label` | `    var text = (btn.innerText \|\| btn.textContent \|\| btn.getAttribute("aria-label") \|\| "").replace(/\s+/g, " ").trim();` |

### `static/seats/patches/stop-selected-toast.css`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 5 | `translateX` | `    transform:translateX(-50%) translateY(22px) scale(.96);` |
| 16 | `translateX` | `    transform:translateX(-50%) translateY(0) scale(1);` |

### `static/seats/patches/unified-seat-deck-report-style.css`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 2 | `deck` | `   UNIFIED SEAT DECK REPORT STYLE` |
| 8 | `unified-seat` | `  --unified-seat-w:82px;` |
| 9 | `unified-seat` | `  --unified-seat-h:58px;` |
| 10 | `corr` | `  --unified-corr-w:68px;` |
| 26 | `deck` | `/* Deck ortalansın, sağ boşluk/fab baskısı koltuk planını bozmasın */` |
| 27 | `deck` | `.deck-wrap,` |
| 28 | `deck` | `body.drive-mode .deck-wrap,` |
| 29 | `deck` | `html.seat-simple-mode .deck-wrap{` |
| 39 | `deck` | `.deck,` |
| 40 | `deck` | `body.drive-mode .deck,` |
| 41 | `deck` | `html.seat-simple-mode .deck{` |
| 47 | `unified-seat` | `    var(--unified-seat-w)` |
| 48 | `corr` | `    var(--unified-corr-w)` |
| 49 | `unified-seat` | `    var(--unified-seat-w)` |
| 50 | `unified-seat` | `    var(--unified-seat-w) !important;` |
| 69 | `label` | `/* Eski sağ kolon kaydırmalarını iptal et: artık label gizli, kaydırmaya gerek yok */` |
| 70 | `grid-column` | `.deck .cell[style*="grid-column:4"],` |
| 71 | `grid-column` | `.deck .cell[style*="grid-column: 4"],` |
| 72 | `grid-column` | `body.drive-mode .deck .cell[style*="grid-column:4"],` |
| 73 | `grid-column` | `body.drive-mode .deck .cell[style*="grid-column: 4"],` |
| 74 | `grid-column` | `html.seat-simple-mode .deck .cell[style*="grid-column:4"],` |
| 75 | `grid-column` | `html.seat-simple-mode .deck .cell[style*="grid-column: 4"],` |
| 76 | `grid-row` | `.deck .cell[style*="grid-row:14"],` |
| 77 | `grid-row` | `.deck .cell[style*="grid-row: 14"],` |
| 78 | `grid-row` | `body.drive-mode .deck .cell[style*="grid-row:14"],` |
| 79 | `grid-row` | `body.drive-mode .deck .cell[style*="grid-row: 14"]{` |
| 84 | `cell` | `.cell,` |
| 85 | `cell` | `body.drive-mode .cell,` |
| 86 | `cell` | `html.seat-simple-mode .cell{` |
| 87 | `unified-seat` | `  width:var(--unified-seat-w) !important;` |
| 88 | `unified-seat` | `  min-width:var(--unified-seat-w) !important;` |
| 89 | `unified-seat` | `  max-width:var(--unified-seat-w) !important;` |
| 96 | `label` | `.label,` |
| 97 | `label` | `body.drive-mode .label,` |
| 98 | `label` | `html.seat-simple-mode .label{` |
| 114 | `unified-seat` | `  height:var(--unified-seat-h) !important;` |
| 115 | `unified-seat` | `  min-height:var(--unified-seat-h) !important;` |
| 184 | `koridor` | `/* Koridor: rapor ekranındaki kırmızı blok */` |
| 185 | `corr` | `.corr,` |
| 186 | `corr` | `body.drive-mode .corr,` |
| 187 | `corr` | `html.seat-simple-mode .corr{` |
| 188 | `grid-column` | `  grid-column:2 !important;` |
| 189 | `grid-row` | `  grid-row:1 / 14 !important;` |
| 191 | `corr` | `  width:var(--unified-corr-w) !important;` |
| 192 | `corr` | `  min-width:var(--unified-corr-w) !important;` |
| 193 | `corr` | `  max-width:var(--unified-corr-w) !important;` |
| 223 | `grid-column` | `  grid-column:3 / 5 !important;` |
| 224 | `grid-row` | `  grid-row:7 !important;` |
| 290 | `43` | `@media(max-width:430px){` |
| 292 | `unified-seat` | `    --unified-seat-w:76px;` |
| 293 | `unified-seat` | `    --unified-seat-h:56px;` |
| 294 | `corr` | `    --unified-corr-w:62px;` |
| 306 | `deck` | `  .deck,` |
| 307 | `deck` | `  body.drive-mode .deck,` |
| 308 | `deck` | `  html.seat-simple-mode .deck{` |
| 320 | `corr` | `  .corr,` |
| 321 | `corr` | `  body.drive-mode .corr,` |
| 322 | `corr` | `  html.seat-simple-mode .corr{` |
| 338 | `unified-seat` | `    --unified-seat-w:70px;` |
| 339 | `54` | `    --unified-seat-h:54px;` |
| 340 | `corr` | `    --unified-corr-w:56px;` |
| 354 | `label` | `/* ===== UNIFIED_LABELS_BACK_START ===== */` |
| 358 | `label` | `  --unified-label-h:32px;` |
| 363 | `cell` | `.cell,` |
| 364 | `cell` | `body.drive-mode .cell,` |
| 365 | `cell` | `html.seat-simple-mode .cell{` |
| 372 | `label` | `.label,` |
| 373 | `label` | `body.drive-mode .label,` |
| 374 | `label` | `html.seat-simple-mode .label{` |
| 376 | `unified-seat` | `  width:var(--unified-seat-w) !important;` |
| 377 | `unified-seat` | `  max-width:var(--unified-seat-w) !important;` |
| 378 | `label` | `  min-height:var(--unified-label-h) !important;` |
| 379 | `label` | `  height:var(--unified-label-h) !important;` |
| 380 | `label` | `  max-height:var(--unified-label-h) !important;` |
| 400 | `label` | `.label:empty,` |
| 401 | `label` | `body.drive-mode .label:empty,` |
| 402 | `label` | `html.seat-simple-mode .label:empty{` |
| 414 | `label` | `html.seat-simple-mode .label{` |
| 420 | `43` | `@media(max-width:430px){` |
| 422 | `label` | `    --unified-label-h:31px;` |
| 426 | `label` | `  .label,` |
| 427 | `label` | `  body.drive-mode .label,` |
| 428 | `label` | `  html.seat-simple-mode .label{` |
| 434 | `label` | `  .label:empty,` |
| 435 | `label` | `  body.drive-mode .label:empty,` |
| 436 | `label` | `  html.seat-simple-mode .label:empty{` |
| 445 | `label` | `    --unified-label-h:30px;` |
| 449 | `label` | `  .label,` |
| 450 | `label` | `  body.drive-mode .label,` |
| 451 | `label` | `  html.seat-simple-mode .label{` |
| 455 | `label` | `/* ===== UNIFIED_LABELS_BACK_END ===== */` |
| 469 | `deck` | `.deck,` |
| 470 | `deck` | `body.drive-mode .deck,` |
| 471 | `deck` | `html.seat-simple-mode .deck{` |
| 477 | `koridor` | `/* Koridorla koltuk arasındaki mesafe daha dengeli */` |
| 478 | `corr` | `.corr,` |
| 479 | `corr` | `body.drive-mode .corr,` |
| 480 | `corr` | `html.seat-simple-mode .corr{` |
| 486 | `43` | `@media(max-width:430px){` |
| 488 | `unified-seat` | `    --unified-seat-w:74px;` |
| 489 | `unified-seat` | `    --unified-seat-h:56px;` |
| 490 | `corr` | `    --unified-corr-w:60px;` |
| 496 | `deck` | `  .deck,` |
| 497 | `deck` | `  body.drive-mode .deck,` |
| 498 | `deck` | `  html.seat-simple-mode .deck{` |
| 506 | `unified-seat` | `    --unified-seat-w:68px;` |
| 507 | `54` | `    --unified-seat-h:54px;` |
| 508 | `54` | `    --unified-corr-w:54px;` |

### `android_app/app/src/main/python/static/seats/patches/bottom-row-51-54-equal-spacing.css`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 2 | `51` | `    En alt sıra 51-52-53-54 eşit aralık düzeltmesi.` |
| 3 | `54` | `    Sağ kolon kaydırma 54'ü de etkilediği için bu satırda` |
| 4 | `51` | `    kaydırmayı sıfırlıyoruz. Böylece 51-52-53-54 kendi grid` |
| 8 | `grid-row` | `  .deck .cell[style*="grid-row:14"],` |
| 9 | `grid-row` | `  .deck .cell[style*="grid-row: 14"]{` |
| 13 | `grid-row` | `  body.drive-mode .deck .cell[style*="grid-row:14"],` |
| 14 | `grid-row` | `  body.drive-mode .deck .cell[style*="grid-row: 14"]{` |

### `android_app/app/src/main/python/static/seats/patches/manual-ticket-system.js`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 76 | `label` | `    const label = document.getElementById("label-" + no);` |
| 77 | `label` | `    const text = label ? String(label.textContent \|\| "").replace(/\s+/g, " ").trim() : "";` |

### `android_app/app/src/main/python/static/seats/patches/mobile-performance-fix.css`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 43 | `deck` | `  .deck,` |
| 67 | `cell` | `  .cell,` |
| 90 | `cell` | `  .cell,` |
| 100 | `cell` | `  .cell,` |
| 112 | `deck` | `  .deck,` |

### `android_app/app/src/main/python/static/seats/patches/only-54-reapply-right-shift.css`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 3 | `51` | `    BOTTOM_ROW_51_54_EQUAL_SPACING yaması 14. satırın transformunu sıfırladığı için` |
| 4 | `54` | `    sadece 54'e sağ kolon kaymasını geri veriyoruz.` |
| 5 | `51` | `    51-52-53'e dokunmaz.` |
| 8 | `grid-row` | `  .deck .cell[style*="grid-row:14"][style*="grid-column:4"],` |
| 9 | `grid-row` | `  .deck .cell[style*="grid-row:14"][style*="grid-column: 4"],` |
| 10 | `grid-row` | `  .deck .cell[style*="grid-row: 14"][style*="grid-column:4"],` |
| 11 | `grid-row` | `  .deck .cell[style*="grid-row: 14"][style*="grid-column: 4"]{` |
| 12 | `right-seat-column` | `    transform:translateX(var(--right-seat-column-shift, 16px)) !important;` |
| 15 | `grid-row` | `  body.drive-mode .deck .cell[style*="grid-row:14"][style*="grid-column:4"],` |
| 16 | `grid-row` | `  body.drive-mode .deck .cell[style*="grid-row:14"][style*="grid-column: 4"],` |
| 17 | `grid-row` | `  body.drive-mode .deck .cell[style*="grid-row: 14"][style*="grid-column:4"],` |
| 18 | `grid-row` | `  body.drive-mode .deck .cell[style*="grid-row: 14"][style*="grid-column: 4"]{` |
| 19 | `right-seat-column` | `    transform:translateX(var(--right-seat-column-shift, 18px)) !important;` |

### `android_app/app/src/main/python/static/seats/patches/right-seat-column-spacing-fix.css`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 3 | `54` | `    4,8,12,16,20,24,28,34,38,42,46,50,54 gibi` |
| 4 | `grid-column` | `    grid-column:4 olan koltukları biraz sağa alır.` |
| 11 | `deck` | `  .deck{` |
| 12 | `right-seat-column` | `    --right-seat-column-shift:16px;` |
| 15 | `grid-column` | `  .deck .cell[style*="grid-column:4"],` |
| 16 | `grid-column` | `  .deck .cell[style*="grid-column: 4"]{` |
| 17 | `right-seat-column` | `    transform:translateX(var(--right-seat-column-shift)) !important;` |
| 24 | `deck` | `  .deck .door{` |
| 25 | `right-seat-column` | `    transform:translateX(calc(var(--right-seat-column-shift) * .35)) !important;` |
| 32 | `deck` | `    .deck{` |
| 33 | `right-seat-column` | `      --right-seat-column-shift:13px;` |
| 41 | `deck` | `  body.drive-mode .deck{` |
| 42 | `right-seat-column` | `    --right-seat-column-shift:18px;` |
| 46 | `deck` | `    body.drive-mode .deck{` |
| 47 | `right-seat-column` | `      --right-seat-column-shift:15px;` |

### `android_app/app/src/main/python/static/seats/patches/seat-label-ghost-clean.css`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 2 | `label` | `   SEAT LABEL GHOST CLEAN` |
| 3 | `label` | `   Boş koltuk altı label kutularındaki kare karartmayı kaldırır.` |
| 4 | `label` | `   Dolu label yazısını korur.` |
| 9 | `label` | `  /* Boş label tamamen yok olsun */` |
| 10 | `deck` | `  html.seat-simple-mode .deck .cell .label:empty,` |
| 11 | `deck` | `  body.seat-simple-mode .deck .cell .label:empty,` |
| 12 | `deck` | `  .deck .cell .label:empty{` |
| 26 | `label` | `  /* Dolu label varsa yazı kalsın, kare arka plan kalksın */` |
| 27 | `deck` | `  html.seat-simple-mode .deck .cell .label,` |
| 28 | `deck` | `  body.seat-simple-mode .deck .cell .label{` |
| 36 | `label` | `  /* Label içindeki yazıyı okunur tut */` |
| 37 | `deck` | `  html.seat-simple-mode .deck .cell .label:not(:empty),` |
| 38 | `deck` | `  body.seat-simple-mode .deck .cell .label:not(:empty){` |

### `android_app/app/src/main/python/static/seats/patches/seat-layout-fab-pack.css`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 4 | `54` | `    4,8,12,16,20,24,28,34,38,42,46,50,54 gibi` |
| 5 | `grid-column` | `    grid-column:4 olan koltukları biraz sağa alır.` |
| 12 | `deck` | `  .deck{` |
| 13 | `right-seat-column` | `    --right-seat-column-shift:16px;` |
| 16 | `grid-column` | `  .deck .cell[style*="grid-column:4"],` |
| 17 | `grid-column` | `  .deck .cell[style*="grid-column: 4"]{` |
| 18 | `right-seat-column` | `    transform:translateX(var(--right-seat-column-shift)) !important;` |
| 25 | `deck` | `  .deck .door{` |
| 26 | `right-seat-column` | `    transform:translateX(calc(var(--right-seat-column-shift) * .35)) !important;` |
| 33 | `deck` | `    .deck{` |
| 34 | `right-seat-column` | `      --right-seat-column-shift:13px;` |
| 42 | `deck` | `  body.drive-mode .deck{` |
| 43 | `right-seat-column` | `    --right-seat-column-shift:18px;` |
| 47 | `deck` | `    body.drive-mode .deck{` |
| 48 | `right-seat-column` | `      --right-seat-column-shift:15px;` |
| 52 | `51` | `/* ===== BOTTOM_ROW_51_54_EQUAL_SPACING ===== */` |
| 54 | `51` | `    En alt sıra 51-52-53-54 eşit aralık düzeltmesi.` |
| 55 | `54` | `    Sağ kolon kaydırma 54'ü de etkilediği için bu satırda` |
| 56 | `51` | `    kaydırmayı sıfırlıyoruz. Böylece 51-52-53-54 kendi grid` |
| 60 | `grid-row` | `  .deck .cell[style*="grid-row:14"],` |
| 61 | `grid-row` | `  .deck .cell[style*="grid-row: 14"]{` |
| 65 | `grid-row` | `  body.drive-mode .deck .cell[style*="grid-row:14"],` |
| 66 | `grid-row` | `  body.drive-mode .deck .cell[style*="grid-row: 14"]{` |
| 70 | `54` | `/* ===== ONLY_54_REAPPLY_RIGHT_SHIFT ===== */` |
| 73 | `51` | `    BOTTOM_ROW_51_54_EQUAL_SPACING yaması 14. satırın transformunu sıfırladığı için` |
| 74 | `54` | `    sadece 54'e sağ kolon kaymasını geri veriyoruz.` |
| 75 | `51` | `    51-52-53'e dokunmaz.` |
| 78 | `grid-row` | `  .deck .cell[style*="grid-row:14"][style*="grid-column:4"],` |
| 79 | `grid-row` | `  .deck .cell[style*="grid-row:14"][style*="grid-column: 4"],` |
| 80 | `grid-row` | `  .deck .cell[style*="grid-row: 14"][style*="grid-column:4"],` |
| 81 | `grid-row` | `  .deck .cell[style*="grid-row: 14"][style*="grid-column: 4"]{` |
| 82 | `right-seat-column` | `    transform:translateX(var(--right-seat-column-shift, 16px)) !important;` |
| 85 | `grid-row` | `  body.drive-mode .deck .cell[style*="grid-row:14"][style*="grid-column:4"],` |
| 86 | `grid-row` | `  body.drive-mode .deck .cell[style*="grid-row:14"][style*="grid-column: 4"],` |
| 87 | `grid-row` | `  body.drive-mode .deck .cell[style*="grid-row: 14"][style*="grid-column:4"],` |
| 88 | `grid-row` | `  body.drive-mode .deck .cell[style*="grid-row: 14"][style*="grid-column: 4"]{` |
| 89 | `right-seat-column` | `    transform:translateX(var(--right-seat-column-shift, 18px)) !important;` |
| 95 | `51` | `    43 ile 51 arasındaki boş sol alana yerleştirir.` |
| 170 | `translateX` | `    transform:translateX(-50%);` |
| 175 | `54` | `    color:rgba(191,219,254,.92);` |
| 242 | `51` | `    Hızlı işlem paneli 43 ile 51 arasına tam otursun diye` |
| 300 | `51` | `    paneli tekrar 43-51 arasındaki dikey mini panel yap.` |
| 350 | `translateX` | `    transform:translateX(-50%) !important;` |
| 356 | `54` | `    color:rgba(191,219,254,.92) !important;` |

### `android_app/app/src/main/python/static/seats/patches/seat-layout-fab-pack.js`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 12 | `deck` | `    var wrap = q(".deck-wrap");` |
| 13 | `43` | `    var seat43 = q("#seat-43");` |
| 14 | `51` | `    var seat51 = q("#seat-51");` |
| 16 | `51` | `    if(!col \|\| !wrap \|\| !seat43 \|\| !seat51) return;` |
| 22 | `43` | `    var r43 = seat43.getBoundingClientRect();` |
| 23 | `51` | `    var r51 = seat51.getBoundingClientRect();` |
| 29 | `43` | `    var centerX43 = r43.left + (r43.width / 2);` |
| 30 | `51` | `    var centerX51 = r51.left + (r51.width / 2);` |
| 31 | `51` | `    var centerX = (centerX43 + centerX51) / 2;` |
| 33 | `43` | `    var gapTop = r43.bottom + 12;` |
| 34 | `51` | `    var gapBottom = r51.top - 12;` |
| 111 | `deck` | `    var wrap = q(".deck-wrap");` |
| 112 | `43` | `    var seat43 = q("#seat-43");` |
| 113 | `51` | `    var seat51 = q("#seat-51");` |
| 115 | `51` | `    if(!col \|\| !wrap \|\| !seat43 \|\| !seat51) return;` |
| 120 | `43` | `    var r43 = seat43.getBoundingClientRect();` |
| 121 | `51` | `    var r51 = seat51.getBoundingClientRect();` |
| 127 | `43` | `    var centerX43 = r43.left + (r43.width / 2);` |
| 128 | `51` | `    var centerX51 = r51.left + (r51.width / 2);` |
| 129 | `51` | `    var centerX = (centerX43 + centerX51) / 2;` |
| 131 | `43` | `    var gapTop = r43.bottom + 12;` |
| 132 | `51` | `    var gapBottom = r51.top - 12;` |

### `android_app/app/src/main/python/static/seats/patches/seat-simple-ui-pack.css`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 113 | `deck` | `/* koltuk deck yukarı gelsin */` |
| 114 | `deck` | `html.seat-simple-mode .deck-card,` |
| 115 | `deck` | `html.seat-simple-mode .seat-deck,` |
| 116 | `deck` | `html.seat-simple-mode .deck-shell{` |
| 121 | `43` | `@media(max-width:430px){` |
| 250 | `43` | `@media(max-width:430px){` |
| 267 | `49` | `    min-height:49px;` |
| 367 | `43` | `@media(max-width:430px){` |

### `android_app/app/src/main/python/static/seats/patches/stop-flow-compact-mobile.css`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 89 | `43` | `@media (max-width: 430px){` |

### `android_app/app/src/main/python/static/seats/patches/stop-flow-focus-patch.css`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 29 | `54` | `    border:1px solid rgba(110,154,255,.23);` |
| 105 | `51` | `    border:1px solid rgba(105,151,255,.24);` |

### `android_app/app/src/main/python/static/seats/patches/stop-flow-focus-patch.js`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 160 | `label` | `      '<div class="stop-focus-panel" role="dialog" aria-modal="true" aria-label="Durak Akışı">' +` |
| 259 | `deck` | `        var target = qs("#deck") \|\| qs(".deck") \|\| qs(".board-card") \|\| qs(".seats-shell");` |
| 310 | `label` | `    var text = (btn.innerText \|\| btn.textContent \|\| btn.getAttribute("aria-label") \|\| "").replace(/\s+/g, " ").trim();` |

### `android_app/app/src/main/python/static/seats/patches/stop-selected-toast.css`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 5 | `translateX` | `    transform:translateX(-50%) translateY(22px) scale(.96);` |
| 16 | `translateX` | `    transform:translateX(-50%) translateY(0) scale(1);` |

## 4) seat-layout-fab-pack kritik bölge

| Satır | İçerik |
| ---: | --- |
| 1 | `/* ===== RIGHT_SEAT_COLUMN_SPACING_FIX ===== */` |
| 2 | `/*` |
| 3 | `    Sağ koltuk kolonunu ferahlatma:` |
| 4 | `    4,8,12,16,20,24,28,34,38,42,46,50,54 gibi` |
| 5 | `    grid-column:4 olan koltukları biraz sağa alır.` |
| 6 | `` |
| 7 | `    Amaç:` |
| 8 | `    23-24 / 27-28 gibi yan yana koltuklarda alt yazıların` |
| 9 | `    birbirine girmesini azaltmak.` |
| 10 | `  */` |
| 11 | `` |
| 12 | `  .deck{` |
| 13 | `    --right-seat-column-shift:16px;` |
| 14 | `  }` |
| 15 | `` |
| 16 | `  .deck .cell[style*="grid-column:4"],` |
| 17 | `  .deck .cell[style*="grid-column: 4"]{` |
| 18 | `    transform:translateX(var(--right-seat-column-shift)) !important;` |
| 19 | `  }` |
| 20 | `` |
| 21 | `  /*` |
| 22 | `    Kapı sağ çift koltukların arasında durduğu için` |
| 23 | `    çok az sağa alınır; görüntü dengeli kalır.` |
| 24 | `  */` |
| 25 | `  .deck .door{` |
| 26 | `    transform:translateX(calc(var(--right-seat-column-shift) * .35)) !important;` |
| 27 | `  }` |
| 28 | `` |
| 29 | `  /*` |
| 30 | `    Çok dar ekranda fazla kaçmasın.` |
| 31 | `  */` |
| 32 | `  @media(max-width:380px){` |
| 33 | `    .deck{` |
| 34 | `      --right-seat-column-shift:13px;` |
| 35 | `    }` |
| 36 | `  }` |

## 4) 51-54 / alt sıra bölgesi

| Satır | İçerik |
| ---: | --- |
| 40 | `    sağ kolonu bir tık daha açıyoruz.` |
| 41 | `  */` |
| 42 | `  body.drive-mode .deck{` |
| 43 | `    --right-seat-column-shift:18px;` |
| 44 | `  }` |
| 45 | `` |
| 46 | `  @media(max-width:380px){` |
| 47 | `    body.drive-mode .deck{` |
| 48 | `      --right-seat-column-shift:15px;` |
| 49 | `    }` |
| 50 | `  }` |
| 51 | `` |
| 52 | `/* ===== BOTTOM_ROW_51_54_EQUAL_SPACING ===== */` |
| 53 | `/*` |
| 54 | `    En alt sıra 51-52-53-54 eşit aralık düzeltmesi.` |
| 55 | `    Sağ kolon kaydırma 54'ü de etkilediği için bu satırda` |
| 56 | `    kaydırmayı sıfırlıyoruz. Böylece 51-52-53-54 kendi grid` |
| 57 | `    kolonlarında eşit aralıkla durur.` |
| 58 | `  */` |
| 59 | `` |
| 60 | `  .deck .cell[style*="grid-row:14"],` |
| 61 | `  .deck .cell[style*="grid-row: 14"]{` |
| 62 | `    transform:none !important;` |
| 63 | `  }` |
| 64 | `` |
| 65 | `  body.drive-mode .deck .cell[style*="grid-row:14"],` |
| 66 | `  body.drive-mode .deck .cell[style*="grid-row: 14"]{` |
| 67 | `    transform:none !important;` |
| 68 | `  }` |
| 69 | `` |
| 70 | `/* ===== ONLY_54_REAPPLY_RIGHT_SHIFT ===== */` |
| 71 | `/*` |
| 72 | `    50 zaten sağ kolon kaydırmasından etkileniyor.` |
| 73 | `    BOTTOM_ROW_51_54_EQUAL_SPACING yaması 14. satırın transformunu sıfırladığı için` |
| 74 | `    sadece 54'e sağ kolon kaymasını geri veriyoruz.` |
| 75 | `    51-52-53'e dokunmaz.` |
| 76 | `  */` |
| 77 | `` |
| 78 | `  .deck .cell[style*="grid-row:14"][style*="grid-column:4"],` |
| 79 | `  .deck .cell[style*="grid-row:14"][style*="grid-column: 4"],` |
| 80 | `  .deck .cell[style*="grid-row: 14"][style*="grid-column:4"],` |
| 81 | `  .deck .cell[style*="grid-row: 14"][style*="grid-column: 4"]{` |
| 82 | `    transform:translateX(var(--right-seat-column-shift, 16px)) !important;` |
| 83 | `  }` |
| 84 | `` |
| 85 | `  body.drive-mode .deck .cell[style*="grid-row:14"][style*="grid-column:4"],` |
| 86 | `  body.drive-mode .deck .cell[style*="grid-row:14"][style*="grid-column: 4"],` |
| 87 | `  body.drive-mode .deck .cell[style*="grid-row: 14"][style*="grid-column:4"],` |

## 4) right-seat-column dosyası

| Satır | İçerik |
| ---: | --- |
| 1 | `/*` |
| 2 | `    Sağ koltuk kolonunu ferahlatma:` |
| 3 | `    4,8,12,16,20,24,28,34,38,42,46,50,54 gibi` |
| 4 | `    grid-column:4 olan koltukları biraz sağa alır.` |
| 5 | `` |
| 6 | `    Amaç:` |
| 7 | `    23-24 / 27-28 gibi yan yana koltuklarda alt yazıların` |
| 8 | `    birbirine girmesini azaltmak.` |
| 9 | `  */` |
| 10 | `` |
| 11 | `  .deck{` |
| 12 | `    --right-seat-column-shift:16px;` |
| 13 | `  }` |
| 14 | `` |
| 15 | `  .deck .cell[style*="grid-column:4"],` |
| 16 | `  .deck .cell[style*="grid-column: 4"]{` |
| 17 | `    transform:translateX(var(--right-seat-column-shift)) !important;` |
| 18 | `  }` |
| 19 | `` |
| 20 | `  /*` |
| 21 | `    Kapı sağ çift koltukların arasında durduğu için` |
| 22 | `    çok az sağa alınır; görüntü dengeli kalır.` |
| 23 | `  */` |
| 24 | `  .deck .door{` |
| 25 | `    transform:translateX(calc(var(--right-seat-column-shift) * .35)) !important;` |
| 26 | `  }` |
| 27 | `` |
| 28 | `  /*` |
| 29 | `    Çok dar ekranda fazla kaçmasın.` |
| 30 | `  */` |
| 31 | `  @media(max-width:380px){` |
| 32 | `    .deck{` |
| 33 | `      --right-seat-column-shift:13px;` |
| 34 | `    }` |
| 35 | `  }` |
| 36 | `` |
| 37 | `  /*` |
| 38 | `    Sürüş modunda koltuklar biraz daha sıkıştığı için` |
| 39 | `    sağ kolonu bir tık daha açıyoruz.` |
| 40 | `  */` |
| 41 | `  body.drive-mode .deck{` |
| 42 | `    --right-seat-column-shift:18px;` |
| 43 | `  }` |
| 44 | `` |
| 45 | `  @media(max-width:380px){` |
| 46 | `    body.drive-mode .deck{` |
| 47 | `      --right-seat-column-shift:15px;` |

## 4) bottom-row dosyası

| Satır | İçerik |
| ---: | --- |
| 1 | `/*` |
| 2 | `    En alt sıra 51-52-53-54 eşit aralık düzeltmesi.` |
| 3 | `    Sağ kolon kaydırma 54'ü de etkilediği için bu satırda` |
| 4 | `    kaydırmayı sıfırlıyoruz. Böylece 51-52-53-54 kendi grid` |
| 5 | `    kolonlarında eşit aralıkla durur.` |
| 6 | `  */` |
| 7 | `` |
| 8 | `  .deck .cell[style*="grid-row:14"],` |
| 9 | `  .deck .cell[style*="grid-row: 14"]{` |
| 10 | `    transform:none !important;` |
| 11 | `  }` |
| 12 | `` |
| 13 | `  body.drive-mode .deck .cell[style*="grid-row:14"],` |
| 14 | `  body.drive-mode .deck .cell[style*="grid-row: 14"]{` |
| 15 | `    transform:none !important;` |
| 16 | `  }` |

## 4) only-54 dosyası

| Satır | İçerik |
| ---: | --- |
| 1 | `/*` |
| 2 | `    50 zaten sağ kolon kaydırmasından etkileniyor.` |
| 3 | `    BOTTOM_ROW_51_54_EQUAL_SPACING yaması 14. satırın transformunu sıfırladığı için` |
| 4 | `    sadece 54'e sağ kolon kaymasını geri veriyoruz.` |
| 5 | `    51-52-53'e dokunmaz.` |
| 6 | `  */` |
| 7 | `` |
| 8 | `  .deck .cell[style*="grid-row:14"][style*="grid-column:4"],` |
| 9 | `  .deck .cell[style*="grid-row:14"][style*="grid-column: 4"],` |
| 10 | `  .deck .cell[style*="grid-row: 14"][style*="grid-column:4"],` |
| 11 | `  .deck .cell[style*="grid-row: 14"][style*="grid-column: 4"]{` |
| 12 | `    transform:translateX(var(--right-seat-column-shift, 16px)) !important;` |
| 13 | `  }` |
| 14 | `` |
| 15 | `  body.drive-mode .deck .cell[style*="grid-row:14"][style*="grid-column:4"],` |
| 16 | `  body.drive-mode .deck .cell[style*="grid-row:14"][style*="grid-column: 4"],` |
| 17 | `  body.drive-mode .deck .cell[style*="grid-row: 14"][style*="grid-column:4"],` |
| 18 | `  body.drive-mode .deck .cell[style*="grid-row: 14"][style*="grid-column: 4"]{` |
| 19 | `    transform:translateX(var(--right-seat-column-shift, 18px)) !important;` |
| 20 | `  }` |

## 4) unified seat deck

| Satır | İçerik |
| ---: | --- |
| 1 | `/* =========================================================` |
| 2 | `   UNIFIED SEAT DECK REPORT STYLE` |
| 3 | `   Normal mod + Sürüş modu + Sade mod aynı koltuk planını kullanır.` |
| 4 | `   JS / HTML mantığına dokunmaz.` |
| 5 | `========================================================= */` |
| 6 | `` |
| 7 | `:root{` |
| 8 | `  --unified-seat-w:82px;` |
| 9 | `  --unified-seat-h:58px;` |
| 10 | `  --unified-corr-w:68px;` |
| 11 | `  --unified-gap-x:12px;` |
| 12 | `  --unified-gap-y:12px;` |
| 13 | `  --unified-row-h:70px;` |
| 14 | `}` |
| 15 | `` |
| 16 | `/* Tüm modlarda board alanı aynı davranır */` |
| 17 | `.board-stage,` |
| 18 | `body.drive-mode .board-stage,` |
| 19 | `html.seat-simple-mode .board-stage{` |
| 20 | `  padding:12px 10px 14px !important;` |
| 21 | `  border-radius:24px !important;` |
| 22 | `  overflow-x:auto !important;` |
| 23 | `  overflow-y:visible !important;` |
| 24 | `}` |
| 25 | `` |
| 26 | `/* Deck ortalansın, sağ boşluk/fab baskısı koltuk planını bozmasın */` |
| 27 | `.deck-wrap,` |
| 28 | `body.drive-mode .deck-wrap,` |
| 29 | `html.seat-simple-mode .deck-wrap{` |
| 30 | `  width:100% !important;` |
| 31 | `  min-width:100% !important;` |
| 32 | `  padding-right:0 !important;` |
| 33 | `  margin:0 auto !important;` |
| 34 | `  display:flex !important;` |
| 35 | `  justify-content:center !important;` |
| 36 | `}` |
| 37 | `` |

## 4) seat label ghost

| Satır | İçerik |
| ---: | --- |
| 1 | `/* =========================================================` |
| 2 | `   SEAT LABEL GHOST CLEAN` |
| 3 | `   Boş koltuk altı label kutularındaki kare karartmayı kaldırır.` |
| 4 | `   Dolu label yazısını korur.` |
| 5 | `   ========================================================= */` |
| 6 | `` |
| 7 | `@media (max-width: 900px){` |
| 8 | `` |
| 9 | `  /* Boş label tamamen yok olsun */` |
| 10 | `  html.seat-simple-mode .deck .cell .label:empty,` |
| 11 | `  body.seat-simple-mode .deck .cell .label:empty,` |
| 12 | `  .deck .cell .label:empty{` |
| 13 | `    display:none !important;` |
| 14 | `    height:0 !important;` |
| 15 | `    min-height:0 !important;` |
| 16 | `    max-height:0 !important;` |
| 17 | `    margin:0 !important;` |
| 18 | `    padding:0 !important;` |
| 19 | `    border:0 !important;` |
| 20 | `    background:transparent !important;` |
| 21 | `    box-shadow:none !important;` |
| 22 | `    opacity:0 !important;` |
| 23 | `    overflow:hidden !important;` |
| 24 | `  }` |
| 25 | `` |
| 26 | `  /* Dolu label varsa yazı kalsın, kare arka plan kalksın */` |
| 27 | `  html.seat-simple-mode .deck .cell .label,` |
| 28 | `  body.seat-simple-mode .deck .cell .label{` |
| 29 | `    background:transparent !important;` |
| 30 | `    box-shadow:none !important;` |
| 31 | `    border:0 !important;` |
| 32 | `    backdrop-filter:none !important;` |
| 33 | `    -webkit-backdrop-filter:none !important;` |
| 34 | `  }` |
| 35 | `` |
| 36 | `  /* Label içindeki yazıyı okunur tut */` |
| 37 | `  html.seat-simple-mode .deck .cell .label:not(:empty),` |

## 5) İlk Yorum

- Koltuk aralığı, koridor, 51-54 hizası, sağ sütun kayması gibi işler büyük ihtimalle `seat-layout-fab-pack.css` ve eski yetim patch dosyaları içinde.
- Aktif linkte olmayan dosya varsa, fiziksel dosya duruyor ama sayfaya uygulanmıyor demektir.
- Özellikle `right-seat-column-spacing-fix.css`, `bottom-row-51-54-equal-spacing.css`, `only-54-reapply-right-shift.css` daha önce yetim görünmüştü; tekrar kontrol edilmeli.