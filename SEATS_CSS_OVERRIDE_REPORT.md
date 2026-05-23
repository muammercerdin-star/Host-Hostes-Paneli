# Seats CSS Override Odak Raporu

Bu rapor sadece `templates/seats.html` içindeki CSS yükleme sırasına göre hazırlanmıştır.

## 1) CSS yükleme sırası

01. line 4 — `static/style.css`
02. line 5 — `static/seats/seats.css`
03. line 6 — `static/seats/seats-final.css`
04. line 7 — `static/seats/patches/stop-selected-toast.css`
05. line 8 — `static/seats/patches/stop-flow-focus-patch.css`
06. line 9 — `static/seats/patches/stop-flow-compact-mobile.css`
07. line 10 — `static/seats/patches/seat-layout-fab-pack.css`
08. line 11 — `static/seats/patches/bottom-voice-command.css`
09. line 12 — `static/seats/patches/modal-bottom-nav-autohide.css`
10. line 13 — `static/seats/patches/manual-ticket-system.css`
11. line 14 — `static/seats/patches/top-sound-toggle.css`
12. line 15 — `static/seats/patches/seat-simple-ui-pack.css`
13. line 16 — `static/seats/patches/unified-seat-deck-report-style.css`
14. line 17 — `static/seats/patches/mobile-performance-fix.css`
15. line 18 — `static/seats/patches/fab-sheet-solid-fix.css`
16. line 19 — `static/seats/patches/seat-label-ghost-clean.css`
17. line 380 — `INLINE:templates/seats.html#drive-mode-actions-independent-style`
18. line 630 — `INLINE:templates/seats.html#drive-dock-stability-final`

## 2) Riskli dosya özetleri

### `static/seats/seats-final.css`
- Toplam CSS bildirimi: **1443**
- Sonradan ezilen bildirim: **284**
- Ezilme oranı: **%19.7**
- Bu dosyanın sonradan ezdiği önceki bildirim: **800**

Örnek ezilmeler:
- `.label` / `font-size`
  - Bu dosya: `10.5px !important`
  - Sonradan ezen: `static/seats/patches/unified-seat-deck-report-style.css` → `10px !important`
- `.seats-shell` / `width`
  - Bu dosya: `min(100vw - 12px, 1280px) !important`
  - Sonradan ezen: `static/seats/seats-final.css` → `calc(100vw - 8px) !important`
- `.seats-shell` / `padding`
  - Bu dosya: `8px 6px 16px !important`
  - Sonradan ezen: `static/seats/seats-final.css` → `6px 4px 12px !important`
- `.route-badge` / `width`
  - Bu dosya: `52px !important`
  - Sonradan ezen: `static/seats/seats-final.css` → `46px !important`
- `.route-badge` / `height`
  - Bu dosya: `52px !important`
  - Sonradan ezen: `static/seats/seats-final.css` → `46px !important`
- `.route-badge` / `border-radius`
  - Bu dosya: `18px !important`
  - Sonradan ezen: `static/seats/seats-final.css` → `16px !important`
- `.route-badge` / `font-size`
  - Bu dosya: `24px !important`
  - Sonradan ezen: `static/seats/seats-final.css` → `22px !important`
- `.route-title` / `font-size`
  - Bu dosya: `clamp(23px,4.6vw,34px) !important`
  - Sonradan ezen: `static/seats/seats-final.css` → `23px !important`
- `.route-title` / `font-size`
  - Bu dosya: `24px !important`
  - Sonradan ezen: `static/seats/seats-final.css` → `23px !important`
- `.route-title` / `font-size`
  - Bu dosya: `clamp(22px,4.2vw,30px) !important`
  - Sonradan ezen: `static/seats/seats-final.css` → `23px !important`
- `.route-sub` / `font-size`
  - Bu dosya: `12.5px !important`
  - Sonradan ezen: `static/seats/seats-final.css` → `12px !important`
- `.route-sub` / `font-size`
  - Bu dosya: `11.5px !important`
  - Sonradan ezen: `static/seats/seats-final.css` → `12px !important`
- `.route-sub` / `margin-top`
  - Bu dosya: `5px !important`
  - Sonradan ezen: `static/seats/seats-final.css` → `4px !important`
- `.mini-chip` / `font-size`
  - Bu dosya: `11.5px !important`
  - Sonradan ezen: `static/seats/seats-final.css` → `11px !important`
- `.top-actions` / `display`
  - Bu dosya: `grid !important`
  - Sonradan ezen: `static/seats/seats-final.css` → `flex !important`
- `.status-row` / `grid-template-columns`
  - Bu dosya: `repeat(2,minmax(0,1fr)) !important`
  - Sonradan ezen: `static/seats/seats-final.css` → `1fr 1fr !important`
- `.status-row` / `margin`
  - Bu dosya: `9px 0 10px !important`
  - Sonradan ezen: `static/seats/seats-final.css` → `8px 0 9px !important`
- `.status-pill` / `min-height`
  - Bu dosya: `58px !important`
  - Sonradan ezen: `static/seats/seats-final.css` → `54px !important`
- `.status-pill` / `border-radius`
  - Bu dosya: `19px !important`
  - Sonradan ezen: `static/seats/seats-final.css` → `18px !important`
- `.status-pill .v` / `font-size`
  - Bu dosya: `26px !important`
  - Sonradan ezen: `static/seats/seats-final.css` → `25px !important`
- `.status-pill .v` / `font-size`
  - Bu dosya: `24px !important`
  - Sonradan ezen: `static/seats/seats-final.css` → `25px !important`
- `.board-card` / `padding`
  - Bu dosya: `10px !important`
  - Sonradan ezen: `static/seats/seats-final.css` → `8px !important`
- `.board-title h2` / `font-size`
  - Bu dosya: `27px !important`
  - Sonradan ezen: `static/seats/seats-final.css` → `26px !important`
- `.board-title h2` / `font-size`
  - Bu dosya: `25px !important`
  - Sonradan ezen: `static/seats/seats-final.css` → `26px !important`
- `.voice-command-btn` / `box-shadow`
  - Bu dosya: `inset 0 1px 0 rgba(255,255,255,.07) !important`
  - Sonradan ezen: `static/seats/patches/mobile-performance-fix.css` → `0 4px 10px rgba(0,0,0,.18) !important`

### `static/seats/patches/manual-ticket-system.css`
- Toplam CSS bildirimi: **29**
- Sonradan ezilen bildirim: **5**
- Ezilme oranı: **%17.2**
- Bu dosyanın sonradan ezdiği önceki bildirim: **6**

Örnek ezilmeler:
- `.seat .manual-ticket-badge` / `right`
  - Bu dosya: `-8px`
  - Sonradan ezen: `static/seats/patches/manual-ticket-system.css` → `-7px`
- `.seat .manual-ticket-badge` / `bottom`
  - Bu dosya: `-8px`
  - Sonradan ezen: `static/seats/patches/manual-ticket-system.css` → `-7px`
- `.seat .manual-ticket-badge` / `width`
  - Bu dosya: `24px`
  - Sonradan ezen: `static/seats/patches/manual-ticket-system.css` → `22px`
- `.seat .manual-ticket-badge` / `height`
  - Bu dosya: `24px`
  - Sonradan ezen: `static/seats/patches/manual-ticket-system.css` → `22px`
- `.seat .manual-ticket-badge` / `font-size`
  - Bu dosya: `13px`
  - Sonradan ezen: `static/seats/patches/manual-ticket-system.css` → `12px`

### `static/seats/patches/mobile-performance-fix.css`
- Toplam CSS bildirimi: **164**
- Sonradan ezilen bildirim: **4**
- Ezilme oranı: **%2.4**
- Bu dosyanın sonradan ezdiği önceki bildirim: **25**

Örnek ezilmeler:
- `.drive-eta-chip` / `box-shadow`
  - Bu dosya: `0 4px 10px rgba(0,0,0,.18) !important`
  - Sonradan ezen: `INLINE:templates/seats.html#drive-dock-stability-final` → `inset 0 1px 0 rgba(255,255,255,.08) !important`
- `#driveInlineDock` / `transform`
  - Bu dosya: `translateZ(0)`
  - Sonradan ezen: `INLINE:templates/seats.html#drive-dock-stability-final` → `none !important`
- `.drive-speed-chip` / `box-shadow`
  - Bu dosya: `0 4px 10px rgba(0,0,0,.18) !important`
  - Sonradan ezen: `INLINE:templates/seats.html#drive-dock-stability-final` → `inset 0 1px 0 rgba(255,255,255,.08) !important`
- `#driveModeActionsDock` / `box-shadow`
  - Bu dosya: `0 8px 18px rgba(0,0,0,.22) !important`
  - Sonradan ezen: `INLINE:templates/seats.html#drive-mode-actions-independent-style` → `inset 0 0 0 1px rgba(255,255,255,.05), 0 16px 34px rgba(0,0,0,.38)`

### `static/seats/patches/seat-layout-fab-pack.css`
- Toplam CSS bildirimi: **248**
- Sonradan ezilen bildirim: **91**
- Ezilme oranı: **%36.7**
- Bu dosyanın sonradan ezdiği önceki bildirim: **87**

Örnek ezilmeler:
- `.deck` / `--right-seat-column-shift`
  - Bu dosya: `16px`
  - Sonradan ezen: `static/seats/patches/seat-layout-fab-pack.css` → `13px`
- `.deck .cell[style*="grid-column:4"]` / `transform`
  - Bu dosya: `translateX(var(--right-seat-column-shift)) !important`
  - Sonradan ezen: `static/seats/patches/unified-seat-deck-report-style.css` → `none !important`
- `.deck .cell[style*="grid-column: 4"]` / `transform`
  - Bu dosya: `translateX(var(--right-seat-column-shift)) !important`
  - Sonradan ezen: `static/seats/patches/unified-seat-deck-report-style.css` → `none !important`
- `body.drive-mode .deck` / `--right-seat-column-shift`
  - Bu dosya: `18px`
  - Sonradan ezen: `static/seats/patches/seat-layout-fab-pack.css` → `15px`
- `.fab-column.fab-left-gap-moved` / `z-index`
  - Bu dosya: `45 !important`
  - Sonradan ezen: `static/seats/patches/seat-layout-fab-pack.css` → `90 !important`
- `.fab-column.fab-left-gap-moved` / `gap`
  - Bu dosya: `7px !important`
  - Sonradan ezen: `static/seats/patches/seat-layout-fab-pack.css` → `4px !important`
- `.fab-column.fab-left-gap-moved` / `gap`
  - Bu dosya: `6px !important`
  - Sonradan ezen: `static/seats/patches/seat-layout-fab-pack.css` → `4px !important`
- `.fab-column.fab-left-gap-moved` / `gap`
  - Bu dosya: `5px !important`
  - Sonradan ezen: `static/seats/patches/seat-layout-fab-pack.css` → `4px !important`
- `.fab-column.fab-left-gap-moved` / `gap`
  - Bu dosya: `5px !important`
  - Sonradan ezen: `static/seats/patches/seat-layout-fab-pack.css` → `4px !important`
- `.fab-column.fab-left-gap-moved .fab` / `width`
  - Bu dosya: `46px !important`
  - Sonradan ezen: `static/seats/patches/seat-layout-fab-pack.css` → `39px !important`
- `.fab-column.fab-left-gap-moved .fab` / `width`
  - Bu dosya: `44px !important`
  - Sonradan ezen: `static/seats/patches/seat-layout-fab-pack.css` → `39px !important`
- `.fab-column.fab-left-gap-moved .fab` / `width`
  - Bu dosya: `48px !important`
  - Sonradan ezen: `static/seats/patches/seat-layout-fab-pack.css` → `39px !important`
- `.fab-column.fab-left-gap-moved .fab` / `width`
  - Bu dosya: `46px !important`
  - Sonradan ezen: `static/seats/patches/seat-layout-fab-pack.css` → `39px !important`
- `.fab-column.fab-left-gap-moved .fab` / `width`
  - Bu dosya: `41px !important`
  - Sonradan ezen: `static/seats/patches/seat-layout-fab-pack.css` → `39px !important`
- `.fab-column.fab-left-gap-moved .fab` / `width`
  - Bu dosya: `41px !important`
  - Sonradan ezen: `static/seats/patches/seat-layout-fab-pack.css` → `39px !important`
- `.fab-column.fab-left-gap-moved .fab` / `height`
  - Bu dosya: `46px !important`
  - Sonradan ezen: `static/seats/patches/seat-layout-fab-pack.css` → `39px !important`
- `.fab-column.fab-left-gap-moved .fab` / `height`
  - Bu dosya: `44px !important`
  - Sonradan ezen: `static/seats/patches/seat-layout-fab-pack.css` → `39px !important`
- `.fab-column.fab-left-gap-moved .fab` / `height`
  - Bu dosya: `48px !important`
  - Sonradan ezen: `static/seats/patches/seat-layout-fab-pack.css` → `39px !important`
- `.fab-column.fab-left-gap-moved .fab` / `height`
  - Bu dosya: `46px !important`
  - Sonradan ezen: `static/seats/patches/seat-layout-fab-pack.css` → `39px !important`
- `.fab-column.fab-left-gap-moved .fab` / `height`
  - Bu dosya: `41px !important`
  - Sonradan ezen: `static/seats/patches/seat-layout-fab-pack.css` → `39px !important`
- `.fab-column.fab-left-gap-moved .fab` / `height`
  - Bu dosya: `41px !important`
  - Sonradan ezen: `static/seats/patches/seat-layout-fab-pack.css` → `39px !important`
- `.fab-column.fab-left-gap-moved .fab` / `border-radius`
  - Bu dosya: `16px !important`
  - Sonradan ezen: `static/seats/patches/seat-layout-fab-pack.css` → `14px !important`
- `.fab-column.fab-left-gap-moved .fab` / `border-radius`
  - Bu dosya: `15px !important`
  - Sonradan ezen: `static/seats/patches/seat-layout-fab-pack.css` → `14px !important`
- `.fab-column.fab-left-gap-moved .fab` / `border-radius`
  - Bu dosya: `18px !important`
  - Sonradan ezen: `static/seats/patches/seat-layout-fab-pack.css` → `14px !important`
- `.fab-column.fab-left-gap-moved .fab` / `border-radius`
  - Bu dosya: `17px !important`
  - Sonradan ezen: `static/seats/patches/seat-layout-fab-pack.css` → `14px !important`

### `static/seats/patches/seat-simple-ui-pack.css`
- Toplam CSS bildirimi: **196**
- Sonradan ezilen bildirim: **26**
- Ezilme oranı: **%13.3**
- Bu dosyanın sonradan ezdiği önceki bildirim: **24**

Örnek ezilmeler:
- `.seat-simple-toggle` / `min-height`
  - Bu dosya: `44px`
  - Sonradan ezen: `static/seats/patches/seat-simple-ui-pack.css` → `42px`
- `.seat-simple-toggle` / `border-radius`
  - Bu dosya: `18px`
  - Sonradan ezen: `static/seats/patches/seat-simple-ui-pack.css` → `16px`
- `.seat-simple-toggle` / `font-size`
  - Bu dosya: `14px`
  - Sonradan ezen: `static/seats/patches/seat-simple-ui-pack.css` → `13px`
- `html.seat-simple-mode .board-title h2` / `font-size`
  - Bu dosya: `clamp(30px, 8vw, 44px) !important`
  - Sonradan ezen: `static/seats/patches/seat-simple-ui-pack.css` → `34px !important`
- `.seat-simple-summary` / `padding`
  - Bu dosya: `13px 14px`
  - Sonradan ezen: `static/seats/patches/seat-simple-ui-pack.css` → `12px`
- `.seat-simple-summary` / `border-radius`
  - Bu dosya: `22px`
  - Sonradan ezen: `static/seats/patches/seat-simple-ui-pack.css` → `20px`
- `.seat-simple-route` / `font-size`
  - Bu dosya: `17px`
  - Sonradan ezen: `static/seats/patches/seat-simple-ui-pack.css` → `16px`
- `.seat-simple-summary-grid` / `grid-template-columns`
  - Bu dosya: `1.25fr .75fr .75fr`
  - Sonradan ezen: `static/seats/patches/seat-simple-ui-pack.css` → `1.15fr .85fr .85fr`
- `.seat-simple-summary-grid` / `gap`
  - Bu dosya: `8px`
  - Sonradan ezen: `static/seats/patches/seat-simple-ui-pack.css` → `7px`
- `.seat-simple-mini` / `min-height`
  - Bu dosya: `52px`
  - Sonradan ezen: `static/seats/patches/seat-simple-ui-pack.css` → `49px`
- `.seat-simple-mini` / `padding`
  - Bu dosya: `9px 10px`
  - Sonradan ezen: `static/seats/patches/seat-simple-ui-pack.css` → `8px 9px`
- `.seat-simple-mini` / `border-radius`
  - Bu dosya: `17px`
  - Sonradan ezen: `static/seats/patches/seat-simple-ui-pack.css` → `15px`
- `.seat-simple-mini small` / `font-size`
  - Bu dosya: `10px`
  - Sonradan ezen: `static/seats/patches/seat-simple-ui-pack.css` → `9px`
- `.seat-simple-mini b` / `font-size`
  - Bu dosya: `15px`
  - Sonradan ezen: `static/seats/patches/seat-simple-ui-pack.css` → `13.5px`
- `.seat-simple-bottom-bar` / `left`
  - Bu dosya: `10px`
  - Sonradan ezen: `static/seats/patches/seat-simple-ui-pack.css` → `8px`
- `.seat-simple-bottom-bar` / `right`
  - Bu dosya: `10px`
  - Sonradan ezen: `static/seats/patches/seat-simple-ui-pack.css` → `8px`
- `.seat-simple-bottom-bar` / `bottom`
  - Bu dosya: `10px`
  - Sonradan ezen: `static/seats/patches/seat-simple-ui-pack.css` → `8px`
- `.seat-simple-bottom-bar` / `padding`
  - Bu dosya: `8px`
  - Sonradan ezen: `static/seats/patches/seat-simple-ui-pack.css` → `7px`
- `.seat-simple-bottom-bar` / `border-radius`
  - Bu dosya: `26px`
  - Sonradan ezen: `static/seats/patches/seat-simple-ui-pack.css` → `24px`
- `.seat-simple-bottom-bar` / `box-shadow`
  - Bu dosya: `0 18px 46px rgba(0,0,0,.42), inset 0 1px 0 rgba(255,255,255,.07)`
  - Sonradan ezen: `static/seats/patches/mobile-performance-fix.css` → `0 8px 18px rgba(0,0,0,.22) !important`
- `.seat-simple-bottom-bar` / `gap`
  - Bu dosya: `7px`
  - Sonradan ezen: `static/seats/patches/seat-simple-ui-pack.css` → `6px`
- `.seat-simple-bottom-item` / `min-height`
  - Bu dosya: `62px`
  - Sonradan ezen: `static/seats/patches/seat-simple-ui-pack.css` → `58px`
- `.seat-simple-bottom-item` / `border-radius`
  - Bu dosya: `20px`
  - Sonradan ezen: `static/seats/patches/seat-simple-ui-pack.css` → `18px`
- `.seat-simple-bottom-item` / `font-size`
  - Bu dosya: `11.5px`
  - Sonradan ezen: `static/seats/patches/seat-simple-ui-pack.css` → `10.8px`
- `.seat-simple-bottom-item` / `box-shadow`
  - Bu dosya: `inset 0 1px 0 rgba(255,255,255,.06)`
  - Sonradan ezen: `static/seats/patches/mobile-performance-fix.css` → `0 4px 10px rgba(0,0,0,.18) !important`

### `static/seats/patches/stop-flow-compact-mobile.css`
- Toplam CSS bildirimi: **46**
- Sonradan ezilen bildirim: **5**
- Ezilme oranı: **%10.9**
- Bu dosyanın sonradan ezdiği önceki bildirim: **6**

Örnek ezilmeler:
- `#stopFlowFocusOverlay .stop-focus-title` / `font-size`
  - Bu dosya: `28px !important`
  - Sonradan ezen: `static/seats/patches/stop-flow-compact-mobile.css` → `26px !important`
- `#stopFlowFocusOverlay .stop-focus-card` / `min-height`
  - Bu dosya: `68px !important`
  - Sonradan ezen: `static/seats/patches/stop-flow-compact-mobile.css` → `64px !important`
- `#stopFlowFocusOverlay .stop-focus-card` / `padding`
  - Bu dosya: `10px 10px !important`
  - Sonradan ezen: `static/seats/patches/stop-flow-compact-mobile.css` → `9px 9px !important`
- `#stopFlowFocusOverlay .stop-focus-name` / `font-size`
  - Bu dosya: `18px !important`
  - Sonradan ezen: `static/seats/patches/stop-flow-compact-mobile.css` → `17px !important`
- `#stopFlowFocusOverlay .stop-focus-meta` / `font-size`
  - Bu dosya: `12px !important`
  - Sonradan ezen: `static/seats/patches/stop-flow-compact-mobile.css` → `11.5px !important`

### `static/seats/patches/stop-flow-focus-patch.css`
- Toplam CSS bildirimi: **113**
- Sonradan ezilen bildirim: **2**
- Ezilme oranı: **%1.8**
- Bu dosyanın sonradan ezdiği önceki bildirim: **0**

Örnek ezilmeler:
- `#stopFlowFocusOverlay` / `padding`
  - Bu dosya: `calc(env(safe-area-inset-top, 0px) + 14px) 14px calc(env(safe-area-inset-bottom, 0px) + 16px)`
  - Sonradan ezen: `static/seats/patches/stop-flow-compact-mobile.css` → `calc(env(safe-area-inset-top, 0px) + 8px) 8px calc(env(safe-area-inset-bottom, 0px) + 8px) !important`
- `.stop-focus-panel` / `box-shadow`
  - Bu dosya: `0 28px 80px rgba(0,0,0,.55), inset 0 1px 0 rgba(255,255,255,.08)`
  - Sonradan ezen: `static/seats/patches/mobile-performance-fix.css` → `0 8px 18px rgba(0,0,0,.22) !important`

### `static/seats/patches/top-sound-toggle.css`
- Toplam CSS bildirimi: **34**
- Sonradan ezilen bildirim: **6**
- Ezilme oranı: **%17.6**
- Bu dosyanın sonradan ezdiği önceki bildirim: **6**

Örnek ezilmeler:
- `#seatSimpleTopSoundRow` / `gap`
  - Bu dosya: `10px`
  - Sonradan ezen: `static/seats/patches/top-sound-toggle.css` → `8px`
- `#seatSimpleSoundToggle` / `min-width`
  - Bu dosya: `112px`
  - Sonradan ezen: `static/seats/patches/top-sound-toggle.css` → `96px`
- `#seatSimpleSoundToggle` / `min-height`
  - Bu dosya: `56px`
  - Sonradan ezen: `static/seats/patches/top-sound-toggle.css` → `52px`
- `#seatSimpleSoundToggle` / `border-radius`
  - Bu dosya: `22px`
  - Sonradan ezen: `static/seats/patches/top-sound-toggle.css` → `19px`
- `#seatSimpleSoundToggle` / `font-size`
  - Bu dosya: `14px`
  - Sonradan ezen: `static/seats/patches/top-sound-toggle.css` → `12.5px`
- `#seatSimpleSoundToggle` / `gap`
  - Bu dosya: `7px`
  - Sonradan ezen: `static/seats/patches/top-sound-toggle.css` → `5px`

### `static/seats/patches/unified-seat-deck-report-style.css`
- Toplam CSS bildirimi: **540**
- Sonradan ezilen bildirim: **108**
- Ezilme oranı: **%20.0**
- Bu dosyanın sonradan ezdiği önceki bildirim: **259**

Örnek ezilmeler:
- `.seat` / `border-radius`
  - Bu dosya: `22px !important`
  - Sonradan ezen: `static/seats/patches/unified-seat-deck-report-style.css` → `20px !important`
- `.label` / `font-size`
  - Bu dosya: `11.5px !important`
  - Sonradan ezen: `static/seats/patches/unified-seat-deck-report-style.css` → `10px !important`
- `.label` / `font-size`
  - Bu dosya: `10.5px !important`
  - Sonradan ezen: `static/seats/patches/unified-seat-deck-report-style.css` → `10px !important`
- `.board-stage` / `padding`
  - Bu dosya: `12px 10px 14px !important`
  - Sonradan ezen: `static/seats/patches/unified-seat-deck-report-style.css` → `10px 6px 12px !important`
- `.deck` / `padding`
  - Bu dosya: `16px 8px 18px !important`
  - Sonradan ezen: `static/seats/patches/unified-seat-deck-report-style.css` → `14px 6px 16px !important`
- `.corr` / `border-radius`
  - Bu dosya: `28px !important`
  - Sonradan ezen: `static/seats/patches/unified-seat-deck-report-style.css` → `25px !important`
- `.corr` / `font-size`
  - Bu dosya: `13px !important`
  - Sonradan ezen: `static/seats/patches/unified-seat-deck-report-style.css` → `12px !important`
- `.door` / `height`
  - Bu dosya: `52px !important`
  - Sonradan ezen: `static/seats/patches/unified-seat-deck-report-style.css` → `48px !important`
- `.door` / `font-size`
  - Bu dosya: `19px !important`
  - Sonradan ezen: `static/seats/patches/unified-seat-deck-report-style.css` → `17px !important`
- `.cell` / `gap`
  - Bu dosya: `0 !important`
  - Sonradan ezen: `static/seats/patches/unified-seat-deck-report-style.css` → `7px !important`
- `.seat` / `font-size`
  - Bu dosya: `30px !important`
  - Sonradan ezen: `static/seats/patches/unified-seat-deck-report-style.css` → `26px !important`
- `.seat` / `font-size`
  - Bu dosya: `28px !important`
  - Sonradan ezen: `static/seats/patches/unified-seat-deck-report-style.css` → `26px !important`
- `.seat` / `box-shadow`
  - Bu dosya: `inset 0 2px 0 rgba(255,255,255,.20), inset 0 -2px 0 rgba(0,0,0,.18), 0 12px 20px rgba(0,0,0,.30) !important`
  - Sonradan ezen: `static/seats/patches/mobile-performance-fix.css` → `0 4px 10px rgba(0,0,0,.18) !important`
- `.label` / `min-height`
  - Bu dosya: `0 !important`
  - Sonradan ezen: `static/seats/patches/unified-seat-deck-report-style.css` → `var(--unified-label-h) !important`
- `.label` / `width`
  - Bu dosya: `0 !important`
  - Sonradan ezen: `static/seats/patches/unified-seat-deck-report-style.css` → `var(--unified-seat-w) !important`
- `.label` / `line-height`
  - Bu dosya: `1.18 !important`
  - Sonradan ezen: `static/seats/patches/unified-seat-deck-report-style.css` → `1.15 !important`
- `body.drive-mode .board-stage` / `padding`
  - Bu dosya: `12px 10px 14px !important`
  - Sonradan ezen: `static/seats/patches/unified-seat-deck-report-style.css` → `10px 6px 12px !important`
- `body.drive-mode .label` / `width`
  - Bu dosya: `0 !important`
  - Sonradan ezen: `static/seats/patches/unified-seat-deck-report-style.css` → `var(--unified-seat-w) !important`
- `body.drive-mode .label` / `min-height`
  - Bu dosya: `0 !important`
  - Sonradan ezen: `static/seats/patches/unified-seat-deck-report-style.css` → `var(--unified-label-h) !important`
- `body.drive-mode .label` / `max-height`
  - Bu dosya: `0 !important`
  - Sonradan ezen: `static/seats/patches/unified-seat-deck-report-style.css` → `var(--unified-label-h) !important`
- `body.drive-mode .label` / `font-size`
  - Bu dosya: `11.5px !important`
  - Sonradan ezen: `static/seats/patches/unified-seat-deck-report-style.css` → `10px !important`
- `body.drive-mode .label` / `font-size`
  - Bu dosya: `10.5px !important`
  - Sonradan ezen: `static/seats/patches/unified-seat-deck-report-style.css` → `10px !important`
- `body.drive-mode .label` / `line-height`
  - Bu dosya: `1.18 !important`
  - Sonradan ezen: `static/seats/patches/unified-seat-deck-report-style.css` → `1.15 !important`
- `body.drive-mode .label` / `display`
  - Bu dosya: `none !important`
  - Sonradan ezen: `static/seats/patches/unified-seat-deck-report-style.css` → `-webkit-box !important`
- `body.drive-mode .cell` / `gap`
  - Bu dosya: `0 !important`
  - Sonradan ezen: `static/seats/patches/unified-seat-deck-report-style.css` → `7px !important`

## 3) En çok sonradan ezen dosyalar

- `static/seats/seats-final.css` → **800** kuralı sonradan eziyor
- `static/seats/seats.css` → **361** kuralı sonradan eziyor
- `static/seats/patches/unified-seat-deck-report-style.css` → **259** kuralı sonradan eziyor
- `INLINE:templates/seats.html#drive-dock-stability-final` → **147** kuralı sonradan eziyor
- `static/seats/patches/seat-layout-fab-pack.css` → **87** kuralı sonradan eziyor
- `static/seats/patches/mobile-performance-fix.css` → **25** kuralı sonradan eziyor
- `static/seats/patches/seat-simple-ui-pack.css` → **24** kuralı sonradan eziyor
- `INLINE:templates/seats.html#drive-mode-actions-independent-style` → **13** kuralı sonradan eziyor
- `static/seats/patches/manual-ticket-system.css` → **6** kuralı sonradan eziyor
- `static/seats/patches/stop-flow-compact-mobile.css` → **6** kuralı sonradan eziyor
- `static/seats/patches/top-sound-toggle.css` → **6** kuralı sonradan eziyor
