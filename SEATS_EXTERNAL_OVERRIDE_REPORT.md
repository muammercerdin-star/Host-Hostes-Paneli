# Seats Gerçek Dış Ezilme Raporu

Aynı dosyanın kendi içindeki tekrarları sayılmadı. Sadece başka dosyanın sonradan ezdiği kurallar listelendi.

## Özet

- `static/seats/seats-final.css` → başka dosya tarafından ezilen: **55**, başka dosyayı ezen: **571**
- `static/seats/patches/manual-ticket-system.css` → başka dosya tarafından ezilen: **0**, başka dosyayı ezen: **1**
- `static/seats/patches/mobile-performance-fix.css` → başka dosya tarafından ezilen: **4**, başka dosyayı ezen: **25**
- `static/seats/patches/seat-layout-fab-pack.css` → başka dosya tarafından ezilen: **4**, başka dosyayı ezen: **0**
- `static/seats/patches/seat-simple-ui-pack.css` → başka dosya tarafından ezilen: **2**, başka dosyayı ezen: **0**
- `static/seats/patches/stop-flow-compact-mobile.css` → başka dosya tarafından ezilen: **0**, başka dosyayı ezen: **1**
- `static/seats/patches/stop-flow-focus-patch.css` → başka dosya tarafından ezilen: **2**, başka dosyayı ezen: **0**
- `static/seats/patches/top-sound-toggle.css` → başka dosya tarafından ezilen: **0**, başka dosyayı ezen: **0**
- `static/seats/patches/unified-seat-deck-report-style.css` → başka dosya tarafından ezilen: **2**, başka dosyayı ezen: **153**

## Kritik detaylar

### `static/seats/seats-final.css`
- `.label` / `font-size`
  - Bu dosya: `10.5px !important`
  - Sonradan ezen: `static/seats/patches/unified-seat-deck-report-style.css` → `10px !important`
- `.voice-command-btn` / `box-shadow`
  - Bu dosya: `inset 0 1px 0 rgba(255,255,255,.07) !important`
  - Sonradan ezen: `static/seats/patches/mobile-performance-fix.css` → `0 4px 10px rgba(0,0,0,.18) !important`
- `.board-stage` / `padding`
  - Bu dosya: `10px 64px 10px 8px !important`
  - Sonradan ezen: `static/seats/patches/unified-seat-deck-report-style.css` → `10px 6px 12px !important`
- `.seat` / `box-shadow`
  - Bu dosya: `inset 0 -10px 18px rgba(0,0,0,.16), 0 13px 24px rgba(0,0,0,.30) !important`
  - Sonradan ezen: `static/seats/patches/mobile-performance-fix.css` → `0 4px 10px rgba(0,0,0,.18) !important`
- `.label` / `color`
  - Bu dosya: `#dbeafe !important`
  - Sonradan ezen: `static/seats/patches/unified-seat-deck-report-style.css` → `rgba(232,237,245,.82) !important`
- `#driveModeToggle` / `min-height`
  - Bu dosya: `42px !important`
  - Sonradan ezen: `INLINE:templates/seats.html#drive-dock-stability-final` → `43px !important`
- `#driveModeToggle` / `min-height`
  - Bu dosya: `44px !important`
  - Sonradan ezen: `INLINE:templates/seats.html#drive-dock-stability-final` → `43px !important`
- `#driveModeToggle` / `padding`
  - Bu dosya: `0 8px !important`
  - Sonradan ezen: `INLINE:templates/seats.html#drive-dock-stability-final` → `0 10px !important`
- `#driveModeToggle` / `border`
  - Bu dosya: `1px solid var(--sf-line) !important`
  - Sonradan ezen: `INLINE:templates/seats.html#drive-dock-stability-final` → `1px solid rgba(147,197,253,.20) !important`
- `#driveModeToggle` / `border-radius`
  - Bu dosya: `18px !important`
  - Sonradan ezen: `INLINE:templates/seats.html#drive-dock-stability-final` → `16px !important`
- `#driveModeToggle` / `background`
  - Bu dosya: `rgba(255,255,255,.065) !important`
  - Sonradan ezen: `INLINE:templates/seats.html#drive-dock-stability-final` → `linear-gradient(135deg,#2563eb,#1d4ed8) !important`
- `#driveModeToggle` / `font-size`
  - Bu dosya: `12px !important`
  - Sonradan ezen: `INLINE:templates/seats.html#drive-dock-stability-final` → `12.5px !important`
- `#driveModeToggle` / `font-size`
  - Bu dosya: `14px !important`
  - Sonradan ezen: `INLINE:templates/seats.html#drive-dock-stability-final` → `12.5px !important`
- `#driveModeToggle` / `box-shadow`
  - Bu dosya: `inset 0 1px 0 rgba(255,255,255,.07) !important`
  - Sonradan ezen: `INLINE:templates/seats.html#drive-dock-stability-final` → `0 10px 24px rgba(37,99,235,.22), inset 0 1px 0 rgba(255,255,255,.15) !important`
- `.drive-speed-top` / `gap`
  - Bu dosya: `4px !important`
  - Sonradan ezen: `INLINE:templates/seats.html#drive-dock-stability-final` → `5px !important`
- `.drive-speed-sub` / `color`
  - Bu dosya: `var(--sf-muted) !important`
  - Sonradan ezen: `INLINE:templates/seats.html#drive-dock-stability-final` → `rgba(226,232,240,.62) !important`
- `#driveInlineDock` / `display`
  - Bu dosya: `grid !important`
  - Sonradan ezen: `INLINE:templates/seats.html#drive-dock-stability-final` → `flex !important`
- `#driveInlineDock` / `gap`
  - Bu dosya: `7px !important`
  - Sonradan ezen: `INLINE:templates/seats.html#drive-dock-stability-final` → `6px !important`
- `#driveInlineDock` / `margin`
  - Bu dosya: `0 0 10px 0 !important`
  - Sonradan ezen: `INLINE:templates/seats.html#drive-dock-stability-final` → `0 0 12px 0 !important`
- `#driveInlineDock` / `min-height`
  - Bu dosya: `42px !important`
  - Sonradan ezen: `INLINE:templates/seats.html#drive-dock-stability-final` → `46px !important`
- `#driveModeToggle` / `height`
  - Bu dosya: `42px !important`
  - Sonradan ezen: `INLINE:templates/seats.html#drive-dock-stability-final` → `43px !important`
- `#driveModeToggle` / `height`
  - Bu dosya: `44px !important`
  - Sonradan ezen: `INLINE:templates/seats.html#drive-dock-stability-final` → `43px !important`
- `#driveSpeedChip` / `min-height`
  - Bu dosya: `42px !important`
  - Sonradan ezen: `INLINE:templates/seats.html#drive-dock-stability-final` → `43px !important`
- `#driveInlineDock` / `margin-bottom`
  - Bu dosya: `12px !important`
  - Sonradan ezen: `INLINE:templates/seats.html#drive-dock-stability-final` → `10px !important`
- `.drive-eta-chip` / `padding`
  - Bu dosya: `7px 10px !important`
  - Sonradan ezen: `INLINE:templates/seats.html#drive-dock-stability-final` → `6px 8px !important`
- `.drive-eta-chip` / `border-radius`
  - Bu dosya: `18px !important`
  - Sonradan ezen: `INLINE:templates/seats.html#drive-dock-stability-final` → `16px !important`
- `.drive-eta-chip` / `border`
  - Bu dosya: `1px solid var(--sf-line) !important`
  - Sonradan ezen: `INLINE:templates/seats.html#drive-dock-stability-final` → `1px solid rgba(148,163,184,.16) !important`
- `.drive-eta-chip` / `background`
  - Bu dosya: `rgba(255,255,255,.065) !important`
  - Sonradan ezen: `INLINE:templates/seats.html#drive-dock-stability-final` → `rgba(255,255,255,.07) !important`
- `.drive-eta-chip` / `box-shadow`
  - Bu dosya: `inset 0 1px 0 rgba(255,255,255,.07) !important`
  - Sonradan ezen: `INLINE:templates/seats.html#drive-dock-stability-final` → `inset 0 1px 0 rgba(255,255,255,.08) !important`
- `.drive-eta-top` / `gap`
  - Bu dosya: `4px !important`
  - Sonradan ezen: `INLINE:templates/seats.html#drive-dock-stability-final` → `5px !important`
- `.drive-eta-sub` / `color`
  - Bu dosya: `var(--sf-muted) !important`
  - Sonradan ezen: `INLINE:templates/seats.html#drive-dock-stability-final` → `rgba(226,232,240,.62) !important`
- `#driveInlineDock` / `position`
  - Bu dosya: `static !important`
  - Sonradan ezen: `INLINE:templates/seats.html#drive-dock-stability-final` → `relative !important`
- `#driveInlineDock` / `z-index`
  - Bu dosya: `1 !important`
  - Sonradan ezen: `INLINE:templates/seats.html#drive-dock-stability-final` → `4 !important`
- `#driveSpeedChip` / `height`
  - Bu dosya: `42px !important`
  - Sonradan ezen: `INLINE:templates/seats.html#drive-dock-stability-final` → `43px !important`
- `#driveEtaChip` / `height`
  - Bu dosya: `42px !important`
  - Sonradan ezen: `INLINE:templates/seats.html#drive-dock-stability-final` → `43px !important`
- `#driveEtaChip` / `height`
  - Bu dosya: `44px !important`
  - Sonradan ezen: `INLINE:templates/seats.html#drive-dock-stability-final` → `43px !important`
- `.drive-speed-chip` / `height`
  - Bu dosya: `42px !important`
  - Sonradan ezen: `INLINE:templates/seats.html#drive-dock-stability-final` → `43px !important`
- `.drive-eta-chip` / `height`
  - Bu dosya: `42px !important`
  - Sonradan ezen: `INLINE:templates/seats.html#drive-dock-stability-final` → `43px !important`
- `.drive-eta-chip` / `height`
  - Bu dosya: `44px !important`
  - Sonradan ezen: `INLINE:templates/seats.html#drive-dock-stability-final` → `43px !important`
- `#driveEtaChip` / `min-height`
  - Bu dosya: `42px !important`
  - Sonradan ezen: `INLINE:templates/seats.html#drive-dock-stability-final` → `43px !important`

### `static/seats/patches/manual-ticket-system.css`
- Dış ezilme yok.

### `static/seats/patches/mobile-performance-fix.css`
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
- `.deck .cell[style*="grid-column:4"]` / `transform`
  - Bu dosya: `translateX(var(--right-seat-column-shift)) !important`
  - Sonradan ezen: `static/seats/patches/unified-seat-deck-report-style.css` → `none !important`
- `.deck .cell[style*="grid-column: 4"]` / `transform`
  - Bu dosya: `translateX(var(--right-seat-column-shift)) !important`
  - Sonradan ezen: `static/seats/patches/unified-seat-deck-report-style.css` → `none !important`
- `.fab-column.fab-left-gap-moved` / `box-shadow`
  - Bu dosya: `0 0 0 1px rgba(255,255,255,.05) inset, 0 18px 42px rgba(0,0,0,.42), 0 0 28px rgba(37,99,235,.20) !important`
  - Sonradan ezen: `static/seats/patches/mobile-performance-fix.css` → `0 8px 18px rgba(0,0,0,.22) !important`
- `.fab-column.fab-left-gap-moved` / `box-shadow`
  - Bu dosya: `inset 0 1px 0 rgba(255,255,255,.08), 0 14px 28px rgba(0,0,0,.36), 0 0 22px rgba(37,99,235,.16) !important`
  - Sonradan ezen: `static/seats/patches/mobile-performance-fix.css` → `0 8px 18px rgba(0,0,0,.22) !important`

### `static/seats/patches/seat-simple-ui-pack.css`
- `.seat-simple-bottom-bar` / `box-shadow`
  - Bu dosya: `0 18px 46px rgba(0,0,0,.42), inset 0 1px 0 rgba(255,255,255,.07)`
  - Sonradan ezen: `static/seats/patches/mobile-performance-fix.css` → `0 8px 18px rgba(0,0,0,.22) !important`
- `.seat-simple-bottom-item` / `box-shadow`
  - Bu dosya: `inset 0 1px 0 rgba(255,255,255,.06)`
  - Sonradan ezen: `static/seats/patches/mobile-performance-fix.css` → `0 4px 10px rgba(0,0,0,.18) !important`

### `static/seats/patches/stop-flow-compact-mobile.css`
- Dış ezilme yok.

### `static/seats/patches/stop-flow-focus-patch.css`
- `#stopFlowFocusOverlay` / `padding`
  - Bu dosya: `calc(env(safe-area-inset-top, 0px) + 14px) 14px calc(env(safe-area-inset-bottom, 0px) + 16px)`
  - Sonradan ezen: `static/seats/patches/stop-flow-compact-mobile.css` → `calc(env(safe-area-inset-top, 0px) + 8px) 8px calc(env(safe-area-inset-bottom, 0px) + 8px) !important`
- `.stop-focus-panel` / `box-shadow`
  - Bu dosya: `0 28px 80px rgba(0,0,0,.55), inset 0 1px 0 rgba(255,255,255,.08)`
  - Sonradan ezen: `static/seats/patches/mobile-performance-fix.css` → `0 8px 18px rgba(0,0,0,.22) !important`

### `static/seats/patches/top-sound-toggle.css`
- Dış ezilme yok.

### `static/seats/patches/unified-seat-deck-report-style.css`
- `.seat` / `box-shadow`
  - Bu dosya: `inset 0 2px 0 rgba(255,255,255,.20), inset 0 -2px 0 rgba(0,0,0,.18), 0 12px 20px rgba(0,0,0,.30) !important`
  - Sonradan ezen: `static/seats/patches/mobile-performance-fix.css` → `0 4px 10px rgba(0,0,0,.18) !important`
- `.seat` / `text-shadow`
  - Bu dosya: `0 1px 0 rgba(0,0,0,.18) !important`
  - Sonradan ezen: `static/seats/patches/mobile-performance-fix.css` → `none !important`

## En çok sonradan ezenler

- `static/seats/seats-final.css` → **571** dış kural eziyor
- `static/seats/patches/unified-seat-deck-report-style.css` → **153** dış kural eziyor
- `INLINE:templates/seats.html#drive-dock-stability-final` → **119** dış kural eziyor
- `static/seats/patches/mobile-performance-fix.css` → **25** dış kural eziyor
- `INLINE:templates/seats.html#drive-mode-actions-independent-style` → **2** dış kural eziyor
- `static/seats/seats.css` → **1** dış kural eziyor
- `static/seats/patches/manual-ticket-system.css` → **1** dış kural eziyor
- `static/seats/patches/stop-flow-compact-mobile.css` → **1** dış kural eziyor