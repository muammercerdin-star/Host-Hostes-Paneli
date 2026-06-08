# Muavin Asistanı Yama Envanteri V10

- Tarih: `20260608-165428`
- V9 hatası düzeltildi: `templates` klasörü artık `test` sanılıp atlanmıyor.
- Bu rapor sadece tespittir. Hiçbir dosya silinmedi/değiştirilmedi.

## 1) Genel Yama Sayıları
| Kök | Aktif çağrı satırı | Aktif benzersiz dosya | Aktif ama dosya yok | Fiziksel yama dosyası | Normal | Disabled | Backup/Eski | Orphan normal | Modal şüpheli aktif çağrı | Template patch satırı |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| WEB | 24 | 23 | 0 | 29 | 26 | 3 | 0 | 3 | 16 | 113 |
| ANDROID | 23 | 22 | 0 | 25 | 25 | 0 | 0 | 3 | 16 | 103 |
| APK_PAYLOAD | 22 | 22 | 0 | 25 | 25 | 0 | 0 | 3 | 16 | 120 |

## 2) WEB ↔ ANDROID Aktif Yama Karşılaştırması
| Yama dosyası | Durum | Risk | WEB hash | ANDROID hash | WEB satır | ANDROID satır |
| --- | --- | --- | --- | --- | --- | --- |
| static/seats/patches/bottom-voice-command.css | AYNI | ŞÜPHELİ-MODAL | 5f664bc9a1e5 | 5f664bc9a1e5 | 26 | 26 |
| static/seats/patches/fab-sheet-solid-fix.css | AYNI |  | 1f9b5f2b0b4c | 1f9b5f2b0b4c | 65 | 65 |
| static/seats/patches/manual-ticket-system.css | AYNI | ŞÜPHELİ-MODAL | 91251ec128d5 | 91251ec128d5 | 56 | 56 |
| static/seats/patches/manual-ticket-system.js | AYNI | ŞÜPHELİ-MODAL | 142da4fa8a42 | 142da4fa8a42 | 228 | 228 |
| static/seats/patches/mobile-performance-fix.css | AYNI | ŞÜPHELİ-MODAL | ebb9eb4d201a | ebb9eb4d201a | 179 | 179 |
| static/seats/patches/modal-bottom-nav-autohide.css | AYNI | ŞÜPHELİ-MODAL | a2b76d9d15a0 | a2b76d9d15a0 | 7 | 7 |
| static/seats/patches/modal-bottom-nav-autohide.js | AYNI | ŞÜPHELİ-MODAL | 5b408035d775 | 5b408035d775 | 150 | 150 |
| static/seats/patches/seat-label-ghost-clean.css | AYNI |  | 7dbec74abcf7 | 7dbec74abcf7 | 46 | 46 |
| static/seats/patches/seat-layout-fab-pack.css | AYNI | ŞÜPHELİ-MODAL | 4c1589bd069a | 4c1589bd069a | 409 | 409 |
| static/seats/patches/seat-layout-fab-pack.js | AYNI | ŞÜPHELİ-MODAL | d15660098d60 | d15660098d60 | 168 | 168 |
| static/seats/patches/seat-simple-ui-pack.css | AYNI | ŞÜPHELİ-MODAL | 37874d3bba93 | 37874d3bba93 | 398 | 398 |
| static/seats/patches/seat-simple-ui-pack.js | AYNI | ŞÜPHELİ-MODAL | ab923a78a462 | ab923a78a462 | 279 | 279 |
| static/seats/patches/stop-flow-compact-mobile.css | AYNI |  | 3ab54340a0cd | 3ab54340a0cd | 107 | 107 |
| static/seats/patches/stop-flow-focus-patch.css | AYNI | ŞÜPHELİ-MODAL | 383d9d45a418 | 383d9d45a418 | 178 | 178 |
| static/seats/patches/stop-flow-focus-patch.js | AYNI | ŞÜPHELİ-MODAL | ff6942c64edd | ff6942c64edd | 388 | 388 |
| static/seats/patches/stop-selected-toast.css | AYNI | ŞÜPHELİ-MODAL | 714896463348 | 714896463348 | 69 | 69 |
| static/seats/patches/stop-selected-toast.js | AYNI | ŞÜPHELİ-MODAL | 740905a0e0e6 | 740905a0e0e6 | 64 | 64 |
| static/seats/patches/top-sound-toggle.css | AYNI | ŞÜPHELİ-MODAL | dea40a39c380 | dea40a39c380 | 61 | 61 |
| static/seats/patches/top-sound-toggle.js | AYNI | ŞÜPHELİ-MODAL | 2851010fa38f | 2851010fa38f | 160 | 160 |
| static/seats/patches/unified-seat-deck-report-style.css | WEB VAR ANDROID YOK |  | d30bc2b71583 | - | 517 | - |
| static/seats/seats-final.css | AYNI |  | 6d10277852f4 | 6d10277852f4 | 2564 | 2564 |
| static/seats/voice-commands.js | AYNI |  | 8f12b8d0a7a2 | 8f12b8d0a7a2 | 1320 | 1320 |
| static/seats/voice-tts.js | AYNI |  | dacbfcc0d6f5 | dacbfcc0d6f5 | 160 | 160 |

## 3) WEB Aktif Çağrılan Yamalar
| Çağıran HTML | Satır | Ref | Dosya | Durum | Risk |
| --- | --- | --- | --- | --- | --- |
| templates/continue_trip.html | 439 | /static/seats/voice-tts.js?v=continue-tts-bridge-1 | static/seats/voice-tts.js | VAR |  |
| templates/seats.html | 6 | /static/seats/seats-final.css?v=drive-voice-real-width-test-1 | static/seats/seats-final.css | VAR |  |
| templates/seats.html | 7 | /static/seats/patches/stop-selected-toast.css?v=1 | static/seats/patches/stop-selected-toast.css | VAR | ŞÜPHELİ-MODAL |
| templates/seats.html | 8 | /static/seats/patches/stop-flow-focus-patch.css?v=1 | static/seats/patches/stop-flow-focus-patch.css | VAR | ŞÜPHELİ-MODAL |
| templates/seats.html | 9 | /static/seats/patches/stop-flow-compact-mobile.css?v=1 | static/seats/patches/stop-flow-compact-mobile.css | VAR |  |
| templates/seats.html | 10 | /static/seats/patches/seat-layout-fab-pack.css?v=1 | static/seats/patches/seat-layout-fab-pack.css | VAR | ŞÜPHELİ-MODAL |
| templates/seats.html | 11 | /static/seats/patches/bottom-voice-command.css?v=1 | static/seats/patches/bottom-voice-command.css | VAR | ŞÜPHELİ-MODAL |
| templates/seats.html | 12 | /static/seats/patches/modal-bottom-nav-autohide.css?v=1 | static/seats/patches/modal-bottom-nav-autohide.css | VAR | ŞÜPHELİ-MODAL |
| templates/seats.html | 13 | /static/seats/patches/manual-ticket-system.css?v=1 | static/seats/patches/manual-ticket-system.css | VAR | ŞÜPHELİ-MODAL |
| templates/seats.html | 14 | /static/seats/patches/top-sound-toggle.css?v=1 | static/seats/patches/top-sound-toggle.css | VAR | ŞÜPHELİ-MODAL |
| templates/seats.html | 15 | /static/seats/patches/seat-simple-ui-pack.css?v=1 | static/seats/patches/seat-simple-ui-pack.css | VAR | ŞÜPHELİ-MODAL |
| templates/seats.html | 16 | /static/seats/patches/unified-seat-deck-report-style.css?v=seat-smaller-removed-2 | static/seats/patches/unified-seat-deck-report-style.css | VAR |  |
| templates/seats.html | 17 | /static/seats/patches/mobile-performance-fix.css?v=2 | static/seats/patches/mobile-performance-fix.css | VAR | ŞÜPHELİ-MODAL |
| templates/seats.html | 18 | /static/seats/patches/fab-sheet-solid-fix.css?v=1 | static/seats/patches/fab-sheet-solid-fix.css | VAR |  |
| templates/seats.html | 19 | /static/seats/patches/seat-label-ghost-clean.css?v=1 | static/seats/patches/seat-label-ghost-clean.css | VAR |  |
| templates/seats.html | 365 | /static/seats/voice-commands.js?v=voice-listen-guard-1 | static/seats/voice-commands.js | VAR |  |
| templates/seats.html | 370 | /static/seats/voice-tts.js?v=voice-owner-fix-1 | static/seats/voice-tts.js | VAR |  |
| templates/seats.html | 373 | /static/seats/patches/stop-selected-toast.js?v=1 | static/seats/patches/stop-selected-toast.js | VAR | ŞÜPHELİ-MODAL |
| templates/seats.html | 374 | /static/seats/patches/stop-flow-focus-patch.js?v=simple-scope-1 | static/seats/patches/stop-flow-focus-patch.js | VAR | ŞÜPHELİ-MODAL |
| templates/seats.html | 375 | /static/seats/patches/seat-layout-fab-pack.js?v=1 | static/seats/patches/seat-layout-fab-pack.js | VAR | ŞÜPHELİ-MODAL |
| templates/seats.html | 376 | /static/seats/patches/modal-bottom-nav-autohide.js?v=1 | static/seats/patches/modal-bottom-nav-autohide.js | VAR | ŞÜPHELİ-MODAL |
| templates/seats.html | 377 | /static/seats/patches/manual-ticket-system.js?v=1 | static/seats/patches/manual-ticket-system.js | VAR | ŞÜPHELİ-MODAL |
| templates/seats.html | 378 | /static/seats/patches/top-sound-toggle.js?v=1 | static/seats/patches/top-sound-toggle.js | VAR | ŞÜPHELİ-MODAL |
| templates/seats.html | 379 | /static/seats/patches/seat-simple-ui-pack.js?v=1 | static/seats/patches/seat-simple-ui-pack.js | VAR | ŞÜPHELİ-MODAL |

## 4) ANDROID Aktif Çağrılan Yamalar
| Çağıran HTML | Satır | Ref | Dosya | Durum | Risk |
| --- | --- | --- | --- | --- | --- |
| templates/continue_trip.html | 439 | /static/seats/voice-tts.js?v=continue-tts-bridge-1 | static/seats/voice-tts.js | VAR |  |
| templates/seats.html | 6 | /static/seats/seats-final.css?v=drive-voice-real-width-test-1 | static/seats/seats-final.css | VAR |  |
| templates/seats.html | 7 | /static/seats/patches/stop-selected-toast.css?v=1 | static/seats/patches/stop-selected-toast.css | VAR | ŞÜPHELİ-MODAL |
| templates/seats.html | 8 | /static/seats/patches/stop-flow-focus-patch.css?v=1 | static/seats/patches/stop-flow-focus-patch.css | VAR | ŞÜPHELİ-MODAL |
| templates/seats.html | 9 | /static/seats/patches/stop-flow-compact-mobile.css?v=1 | static/seats/patches/stop-flow-compact-mobile.css | VAR |  |
| templates/seats.html | 10 | /static/seats/patches/seat-layout-fab-pack.css?v=1 | static/seats/patches/seat-layout-fab-pack.css | VAR | ŞÜPHELİ-MODAL |
| templates/seats.html | 11 | /static/seats/patches/bottom-voice-command.css?v=1 | static/seats/patches/bottom-voice-command.css | VAR | ŞÜPHELİ-MODAL |
| templates/seats.html | 12 | /static/seats/patches/modal-bottom-nav-autohide.css?v=1 | static/seats/patches/modal-bottom-nav-autohide.css | VAR | ŞÜPHELİ-MODAL |
| templates/seats.html | 13 | /static/seats/patches/manual-ticket-system.css?v=1 | static/seats/patches/manual-ticket-system.css | VAR | ŞÜPHELİ-MODAL |
| templates/seats.html | 14 | /static/seats/patches/top-sound-toggle.css?v=1 | static/seats/patches/top-sound-toggle.css | VAR | ŞÜPHELİ-MODAL |
| templates/seats.html | 15 | /static/seats/patches/seat-simple-ui-pack.css?v=1 | static/seats/patches/seat-simple-ui-pack.css | VAR | ŞÜPHELİ-MODAL |
| templates/seats.html | 16 | /static/seats/patches/mobile-performance-fix.css?v=2 | static/seats/patches/mobile-performance-fix.css | VAR | ŞÜPHELİ-MODAL |
| templates/seats.html | 17 | /static/seats/patches/fab-sheet-solid-fix.css?v=1 | static/seats/patches/fab-sheet-solid-fix.css | VAR |  |
| templates/seats.html | 18 | /static/seats/patches/seat-label-ghost-clean.css?v=1 | static/seats/patches/seat-label-ghost-clean.css | VAR |  |
| templates/seats.html | 364 | /static/seats/voice-commands.js?v=voice-listen-guard-1 | static/seats/voice-commands.js | VAR |  |
| templates/seats.html | 369 | /static/seats/voice-tts.js?v=voice-owner-fix-1 | static/seats/voice-tts.js | VAR |  |
| templates/seats.html | 372 | /static/seats/patches/stop-selected-toast.js?v=1 | static/seats/patches/stop-selected-toast.js | VAR | ŞÜPHELİ-MODAL |
| templates/seats.html | 373 | /static/seats/patches/stop-flow-focus-patch.js?v=simple-scope-1 | static/seats/patches/stop-flow-focus-patch.js | VAR | ŞÜPHELİ-MODAL |
| templates/seats.html | 374 | /static/seats/patches/seat-layout-fab-pack.js?v=1 | static/seats/patches/seat-layout-fab-pack.js | VAR | ŞÜPHELİ-MODAL |
| templates/seats.html | 375 | /static/seats/patches/modal-bottom-nav-autohide.js?v=1 | static/seats/patches/modal-bottom-nav-autohide.js | VAR | ŞÜPHELİ-MODAL |
| templates/seats.html | 376 | /static/seats/patches/manual-ticket-system.js?v=1 | static/seats/patches/manual-ticket-system.js | VAR | ŞÜPHELİ-MODAL |
| templates/seats.html | 377 | /static/seats/patches/top-sound-toggle.js?v=1 | static/seats/patches/top-sound-toggle.js | VAR | ŞÜPHELİ-MODAL |
| templates/seats.html | 378 | /static/seats/patches/seat-simple-ui-pack.js?v=1 | static/seats/patches/seat-simple-ui-pack.js | VAR | ŞÜPHELİ-MODAL |

## 5) WEB Fiziksel Yama Dosyaları
| Dosya | Durum | Risk | Uzantı | Byte | Satır | Hash | Mtime |
| --- | --- | --- | --- | --- | --- | --- | --- |
| static/seats/patches/_disabled/seat-bottom-fab-54-final.css.disabled_20260523_085109 | DISABLED |  | .disabled_20260523_085109 | 3056 |  | b25c9bf38389 | 2026-05-23 08:49:38 |
| static/seats/patches/bottom-row-51-54-equal-spacing.css | NORMAL |  | .css | 489 | 17 | 3bd1c2baffe1 | 2026-05-18 17:47:01 |
| static/seats/patches/bottom-voice-command.css | NORMAL | ŞÜPHELİ-MODAL | .css | 739 | 26 | 5f664bc9a1e5 | 2026-05-18 16:55:51 |
| static/seats/patches/fab-sheet-solid-fix.css | NORMAL |  | .css | 1930 | 65 | 1f9b5f2b0b4c | 2026-05-18 20:57:55 |
| static/seats/patches/live-flow-v2.css.disabled_20260523_094130 | DISABLED |  | .disabled_20260523_094130 | 12660 |  | 2351ddd827c2 | 2026-05-23 09:38:48 |
| static/seats/patches/live-flow-v2.js.disabled_20260523_094130 | DISABLED |  | .disabled_20260523_094130 | 10817 |  | 8aa579bac4e5 | 2026-05-23 09:38:48 |
| static/seats/patches/manual-ticket-system.css | NORMAL | ŞÜPHELİ-MODAL | .css | 1092 | 56 | 91251ec128d5 | 2026-05-18 16:59:02 |
| static/seats/patches/manual-ticket-system.js | NORMAL | ŞÜPHELİ-MODAL | .js | 5038 | 228 | 142da4fa8a42 | 2026-05-18 16:59:02 |
| static/seats/patches/mobile-performance-fix.css | NORMAL | ŞÜPHELİ-MODAL | .css | 3688 | 179 | ebb9eb4d201a | 2026-05-18 18:11:00 |
| static/seats/patches/modal-bottom-nav-autohide.css | NORMAL | ŞÜPHELİ-MODAL | .css | 193 | 7 | a2b76d9d15a0 | 2026-05-18 16:57:39 |
| static/seats/patches/modal-bottom-nav-autohide.js | NORMAL | ŞÜPHELİ-MODAL | .js | 4115 | 150 | 5b408035d775 | 2026-05-18 16:57:39 |
| static/seats/patches/only-54-reapply-right-shift.css | NORMAL |  | .css | 955 | 21 | dd1207d8cb80 | 2026-05-18 17:47:01 |
| static/seats/patches/right-seat-column-spacing-fix.css | NORMAL |  | .css | 1100 | 50 | 478f51a8d7ef | 2026-05-18 17:47:01 |
| static/seats/patches/seat-label-ghost-clean.css | NORMAL |  | .css | 1425 | 46 | 7dbec74abcf7 | 2026-05-18 21:04:19 |
| static/seats/patches/seat-layout-fab-pack.css | NORMAL | ŞÜPHELİ-MODAL | .css | 11324 | 409 | 4c1589bd069a | 2026-05-18 17:52:36 |
| static/seats/patches/seat-layout-fab-pack.js | NORMAL | ŞÜPHELİ-MODAL | .js | 4474 | 168 | d15660098d60 | 2026-05-18 17:52:36 |
| static/seats/patches/seat-simple-ui-pack.css | NORMAL | ŞÜPHELİ-MODAL | .css | 9005 | 398 | 37874d3bba93 | 2026-05-18 17:59:24 |
| static/seats/patches/seat-simple-ui-pack.js | NORMAL | ŞÜPHELİ-MODAL | .js | 7259 | 279 | ab923a78a462 | 2026-05-18 17:59:24 |
| static/seats/patches/stop-flow-compact-mobile.css | NORMAL |  | .css | 2497 | 107 | 3ab54340a0cd | 2026-05-18 20:53:14 |
| static/seats/patches/stop-flow-focus-patch.css | NORMAL | ŞÜPHELİ-MODAL | .css | 3988 | 178 | 383d9d45a418 | 2026-05-18 17:44:27 |
| static/seats/patches/stop-flow-focus-patch.js | NORMAL | ŞÜPHELİ-MODAL | .js | 12254 | 388 | ff6942c64edd | 2026-05-20 11:06:12 |
| static/seats/patches/stop-selected-toast.css | NORMAL | ŞÜPHELİ-MODAL | .css | 1575 | 69 | 714896463348 | 2026-05-18 16:44:37 |
| static/seats/patches/stop-selected-toast.js | NORMAL | ŞÜPHELİ-MODAL | .js | 1659 | 64 | 740905a0e0e6 | 2026-05-18 16:44:37 |
| static/seats/patches/top-sound-toggle.css | NORMAL | ŞÜPHELİ-MODAL | .css | 1439 | 61 | dea40a39c380 | 2026-05-18 17:19:03 |
| static/seats/patches/top-sound-toggle.js | NORMAL | ŞÜPHELİ-MODAL | .js | 3839 | 160 | 2851010fa38f | 2026-05-18 17:19:03 |
| static/seats/patches/unified-seat-deck-report-style.css | NORMAL |  | .css | 12695 | 517 | d30bc2b71583 | 2026-05-21 21:23:10 |
| static/seats/seats-final.css | NORMAL |  | .css | 68499 | 2564 | 6d10277852f4 | 2026-05-07 09:02:03 |
| static/seats/voice-commands.js | NORMAL |  | .js | 34320 | 1320 | 8f12b8d0a7a2 | 2026-05-18 16:50:14 |
| static/seats/voice-tts.js | NORMAL |  | .js | 3944 | 160 | dacbfcc0d6f5 | 2026-05-16 15:41:39 |

## 6) WEB Orphan Normal Yama Dosyaları
Dosyada var ama aktif HTML çağrısı bulunmadı. Direkt silinmez; önce dinamik kullanım kontrolü gerekir.
| Dosya | Uzantı | Byte | Satır | Hash | Mtime |
| --- | --- | --- | --- | --- | --- |
| static/seats/patches/bottom-row-51-54-equal-spacing.css | .css | 489 | 17 | 3bd1c2baffe1 | 2026-05-18 17:47:01 |
| static/seats/patches/only-54-reapply-right-shift.css | .css | 955 | 21 | dd1207d8cb80 | 2026-05-18 17:47:01 |
| static/seats/patches/right-seat-column-spacing-fix.css | .css | 1100 | 50 | 478f51a8d7ef | 2026-05-18 17:47:01 |

## 7) WEB Son Değişen Yama Dosyaları
| Mtime | Dosya | Durum | Risk | Uzantı | Satır | Hash |
| --- | --- | --- | --- | --- | --- | --- |
| 2026-05-23 09:38:48 | static/seats/patches/live-flow-v2.js.disabled_20260523_094130 | DISABLED |  | .disabled_20260523_094130 |  | 8aa579bac4e5 |
| 2026-05-23 09:38:48 | static/seats/patches/live-flow-v2.css.disabled_20260523_094130 | DISABLED |  | .disabled_20260523_094130 |  | 2351ddd827c2 |
| 2026-05-23 08:49:38 | static/seats/patches/_disabled/seat-bottom-fab-54-final.css.disabled_20260523_085109 | DISABLED |  | .disabled_20260523_085109 |  | b25c9bf38389 |
| 2026-05-21 21:23:10 | static/seats/patches/unified-seat-deck-report-style.css | NORMAL |  | .css | 517 | d30bc2b71583 |
| 2026-05-20 11:06:12 | static/seats/patches/stop-flow-focus-patch.js | NORMAL | ŞÜPHELİ-MODAL | .js | 388 | ff6942c64edd |
| 2026-05-18 21:04:19 | static/seats/patches/seat-label-ghost-clean.css | NORMAL |  | .css | 46 | 7dbec74abcf7 |
| 2026-05-18 20:57:55 | static/seats/patches/fab-sheet-solid-fix.css | NORMAL |  | .css | 65 | 1f9b5f2b0b4c |
| 2026-05-18 20:53:14 | static/seats/patches/stop-flow-compact-mobile.css | NORMAL |  | .css | 107 | 3ab54340a0cd |
| 2026-05-18 18:11:00 | static/seats/patches/mobile-performance-fix.css | NORMAL | ŞÜPHELİ-MODAL | .css | 179 | ebb9eb4d201a |
| 2026-05-18 17:59:24 | static/seats/patches/seat-simple-ui-pack.js | NORMAL | ŞÜPHELİ-MODAL | .js | 279 | ab923a78a462 |
| 2026-05-18 17:59:24 | static/seats/patches/seat-simple-ui-pack.css | NORMAL | ŞÜPHELİ-MODAL | .css | 398 | 37874d3bba93 |
| 2026-05-18 17:52:36 | static/seats/patches/seat-layout-fab-pack.js | NORMAL | ŞÜPHELİ-MODAL | .js | 168 | d15660098d60 |
| 2026-05-18 17:52:36 | static/seats/patches/seat-layout-fab-pack.css | NORMAL | ŞÜPHELİ-MODAL | .css | 409 | 4c1589bd069a |
| 2026-05-18 17:47:01 | static/seats/patches/right-seat-column-spacing-fix.css | NORMAL |  | .css | 50 | 478f51a8d7ef |
| 2026-05-18 17:47:01 | static/seats/patches/only-54-reapply-right-shift.css | NORMAL |  | .css | 21 | dd1207d8cb80 |
| 2026-05-18 17:47:01 | static/seats/patches/bottom-row-51-54-equal-spacing.css | NORMAL |  | .css | 17 | 3bd1c2baffe1 |
| 2026-05-18 17:44:27 | static/seats/patches/stop-flow-focus-patch.css | NORMAL | ŞÜPHELİ-MODAL | .css | 178 | 383d9d45a418 |
| 2026-05-18 17:19:03 | static/seats/patches/top-sound-toggle.js | NORMAL | ŞÜPHELİ-MODAL | .js | 160 | 2851010fa38f |
| 2026-05-18 17:19:03 | static/seats/patches/top-sound-toggle.css | NORMAL | ŞÜPHELİ-MODAL | .css | 61 | dea40a39c380 |
| 2026-05-18 16:59:02 | static/seats/patches/manual-ticket-system.js | NORMAL | ŞÜPHELİ-MODAL | .js | 228 | 142da4fa8a42 |
| 2026-05-18 16:59:02 | static/seats/patches/manual-ticket-system.css | NORMAL | ŞÜPHELİ-MODAL | .css | 56 | 91251ec128d5 |
| 2026-05-18 16:57:39 | static/seats/patches/modal-bottom-nav-autohide.js | NORMAL | ŞÜPHELİ-MODAL | .js | 150 | 5b408035d775 |
| 2026-05-18 16:57:39 | static/seats/patches/modal-bottom-nav-autohide.css | NORMAL | ŞÜPHELİ-MODAL | .css | 7 | a2b76d9d15a0 |
| 2026-05-18 16:55:51 | static/seats/patches/bottom-voice-command.css | NORMAL | ŞÜPHELİ-MODAL | .css | 26 | 5f664bc9a1e5 |
| 2026-05-18 16:50:14 | static/seats/voice-commands.js | NORMAL |  | .js | 1320 | 8f12b8d0a7a2 |
| 2026-05-18 16:44:37 | static/seats/patches/stop-selected-toast.js | NORMAL | ŞÜPHELİ-MODAL | .js | 64 | 740905a0e0e6 |
| 2026-05-18 16:44:37 | static/seats/patches/stop-selected-toast.css | NORMAL | ŞÜPHELİ-MODAL | .css | 69 | 714896463348 |
| 2026-05-16 15:41:39 | static/seats/voice-tts.js | NORMAL |  | .js | 160 | dacbfcc0d6f5 |
| 2026-05-07 09:02:03 | static/seats/seats-final.css | NORMAL |  | .css | 2564 | 6d10277852f4 |

## 8) WEB Template İçinde Patch/Yama Satırları
| Template | Satır | İçerik |
| --- | --- | --- |
| templates/ai_console.html | 7 | <style id="intent-legend-mobile-fix"> |
| templates/ai_console.html | 2587 | return '₺' + Number(v \|\| 0).toFixed(2); |
| templates/consignments.html | 412 | position:fixed; |
| templates/consignments.html | 852 | <style id="consignment-photo-modal-fix"> |
| templates/consignments.html | 855 | position:fixed !important; |
| templates/continue_trip.html | 439 | <script src="/static/seats/voice-tts.js?v=continue-tts-bridge-1"></script> |
| templates/hesap.html | 63 | position:fixed; |
| templates/hesap.html | 671 | position:fixed; |
| templates/hesap.html | 739 | position:fixed; |
| templates/hesap.html | 900 | position:fixed; |
| templates/hesap.html | 1121 | /* === ACCOUNT HERO TOP FIX \| START === */ |
| templates/hesap.html | 1252 | /* === ACCOUNT HERO TOP FIX \| END === */ |
| templates/hesap.html | 1255 | /* === HERO HOME BUTTON FIX \| START === */ |
| templates/hesap.html | 1294 | /* === HERO HOME BUTTON FIX \| END === */ |
| templates/hesap.html | 1358 | /* === HERO HOME MICRO FIX \| START === */ |
| templates/hesap.html | 1402 | /* === HERO HOME MICRO FIX \| END === */ |
| templates/hesap.html | 2311 | select.dispatchEvent(new Event("change", { bubbles:true })); |
| templates/hesap.html | 2445 | function fixFooterGap(){ |
| templates/hesap.html | 2453 | window.addEventListener("load", fixFooterGap, {once:true}); |
| templates/hesap.html | 2454 | window.addEventListener("resize", fixFooterGap); |
| templates/hesap.html | 2455 | window.addEventListener("orientationchange", fixFooterGap); |
| templates/hesap.html | 2456 | setTimeout(fixFooterGap, 300); |
| templates/hesap.html | 2457 | setTimeout(fixFooterGap, 1200); |
| templates/index.html | 272 | position:fixed; |
| templates/index.html | 1031 | <style id="route-sheet-no-flash-fix"> |
| templates/index.html | 1210 | <style id="home-route-lock-fix"> |
| templates/index.html | 1261 | <script id="home-route-link-fix"> |
| templates/index.html | 1359 | position:fixed; |
| templates/index.html | 1373 | position:fixed; |
| templates/index.html | 1649 | position:fixed; |
| templates/index.html | 1663 | position:fixed; |
| templates/live_map.html | 965 | position:fixed !important; |
| templates/live_map.html | 1236 | <style id="route-status-right-top-fix"> |
| templates/live_map.html | 2314 | return `${(m / 1000).toFixed(1)} km`; |
| templates/live_map.html | 2419 | return `${km.toFixed(1)} km`; |
| templates/live_map.html | 2522 | const kmText = km < 1 ? `${Math.round(km * 1000)} m` : `${km.toFixed(1)} km`; |
| templates/live_map.html | 2796 | <!-- VOICE_MAP_FULLSCREEN_PATCH_START --> |
| templates/live_map.html | 2809 | position:fixed !important; |
| templates/live_map.html | 2849 | position:fixed; |
| templates/live_map.html | 2923 | <!-- VOICE_MAP_FULLSCREEN_PATCH_END --> |
| templates/passenger_control.html | 457 | position:fixed; |
| templates/passenger_control.html | 466 | position:fixed; |
| templates/rehber.html | 1096 | HERO V2 IMAGE FIX |
| templates/report_archive.html | 45 | position:fixed; |
| templates/reports.html | 144 | .backdrop{display:none;position:fixed;inset:0;background:var(--backdrop);z-index:2400} |
| templates/reports.html | 146 | display:none;position:fixed;left:50%;top:50%;transform:translate(-50%,-50%); |
| templates/reports.html | 157 | #busy{display:none;position:fixed;right:12px;bottom:12px;z-index:2600;background:var(--busy-bg);color:var(--busy-text);border:1px solid rgba(0,0,0,.2);padding:8px 12px;border-radius:10px;font-weight:800;box-shadow:var(--... |
| templates/reports.html | 158 | #toast{display:none;position:fixed;left:50%;bottom:18px;transform:translateX(-50%);z-index:2700;background:var(--toast-bg);color:var(--toast-text);border:1px solid var(--toast-border);padding:10px 14px;border-radius:10px... |
| templates/reports.html | 287 | const fmtTL = n => '₺' + (Number(n\|\|0).toFixed(2)); |
| templates/reports.html | 514 | L.push(`Toplam Gelir;${Number(t.overall_revenue\|\|0).toFixed(2)}`); |
| templates/reports.html | 515 | L.push(`Ortalama Gelir;${pax? (Number(t.overall_revenue\|\|0)/pax).toFixed(2):'0.00'}`); |
| templates/reports.html | 518 | L.push(...(j.per_seat\|\|[]).map(r=>`${r.seat_no};${r.times};${Number(r.revenue\|\|0).toFixed(2)}`)); |
| templates/route_schedule_edit.html | 988 | ROUTE SCHEDULE HERO COMPACT FIX |
| templates/route_schedule_edit.html | 1371 | position:fixed; |
| templates/route_schedule_edit.html | 1660 | activeSelect.dispatchEvent(new Event("input", { bubbles:true })); |
| templates/route_schedule_edit.html | 1661 | activeSelect.dispatchEvent(new Event("change", { bubbles:true })); |
| templates/routes_list.html | 209 | .badge.fixed{ |
| templates/routes_list.html | 230 | .route-actions.fixed-actions{ |
| templates/routes_list.html | 393 | <span class="badge fixed">Düzenlenebilir</span> |
| templates/seats.html | 6 | <link rel="stylesheet" href="/static/seats/seats-final.css?v=drive-voice-real-width-test-1"> |
| templates/seats.html | 7 | <link rel="stylesheet" href="/static/seats/patches/stop-selected-toast.css?v=1"> |
| templates/seats.html | 8 | <link rel="stylesheet" href="/static/seats/patches/stop-flow-focus-patch.css?v=1"> |
| templates/seats.html | 9 | <link rel="stylesheet" href="/static/seats/patches/stop-flow-compact-mobile.css?v=1"> |
| templates/seats.html | 10 | <link rel="stylesheet" href="/static/seats/patches/seat-layout-fab-pack.css?v=1"> |
| templates/seats.html | 11 | <link rel="stylesheet" href="/static/seats/patches/bottom-voice-command.css?v=1"> |
| templates/seats.html | 12 | <link rel="stylesheet" href="/static/seats/patches/modal-bottom-nav-autohide.css?v=1"> |
| templates/seats.html | 13 | <link rel="stylesheet" href="/static/seats/patches/manual-ticket-system.css?v=1"> |
| templates/seats.html | 14 | <link rel="stylesheet" href="/static/seats/patches/top-sound-toggle.css?v=1"> |
| templates/seats.html | 15 | <link rel="stylesheet" href="/static/seats/patches/seat-simple-ui-pack.css?v=1"> |
| templates/seats.html | 16 | <link rel="stylesheet" href="/static/seats/patches/unified-seat-deck-report-style.css?v=seat-smaller-removed-2"> |
| templates/seats.html | 17 | <link rel="stylesheet" href="/static/seats/patches/mobile-performance-fix.css?v=2"> |
| templates/seats.html | 18 | <link rel="stylesheet" href="/static/seats/patches/fab-sheet-solid-fix.css?v=1"> |
| templates/seats.html | 19 | <link rel="stylesheet" href="/static/seats/patches/seat-label-ghost-clean.css?v=1"> |
| templates/seats.html | 293 | <button class="btn primary" type="button" id="fabBulkPane">Toplu Giriş</button> |
| templates/seats.html | 294 | <button class="btn green" type="button" id="fabCashPane">Hızlı Tahsilat</button> |
| templates/seats.html | 365 | <script src="/static/seats/voice-commands.js?v=voice-listen-guard-1"></script> |
| templates/seats.html | 370 | <script src="/static/seats/voice-tts.js?v=voice-owner-fix-1"></script> |
| templates/seats.html | 372 | <script src="/static/seats/drive-controls.js?v=drive-toggle-fix-1"></script> |
| templates/seats.html | 373 | <script src="/static/seats/patches/stop-selected-toast.js?v=1"></script> |
| templates/seats.html | 374 | <script src="/static/seats/patches/stop-flow-focus-patch.js?v=simple-scope-1"></script> |
| templates/seats.html | 375 | <script src="/static/seats/patches/seat-layout-fab-pack.js?v=1"></script> |
| templates/seats.html | 376 | <script src="/static/seats/patches/modal-bottom-nav-autohide.js?v=1"></script> |
| templates/seats.html | 377 | <script src="/static/seats/patches/manual-ticket-system.js?v=1"></script> |
| templates/seats.html | 378 | <script src="/static/seats/patches/top-sound-toggle.js?v=1"></script> |
| templates/seats.html | 379 | <script src="/static/seats/patches/seat-simple-ui-pack.js?v=1"></script> |
| templates/seats.html | 879 | window.dispatchEvent(new CustomEvent("driveModeChanged", { detail:{ on:!!on } })); |
| templates/seats.html | 978 | <script id="seat-simple-bottom-bar-script"> |
| templates/seats.html | 994 | document.documentElement.classList.remove("seat-simple-mode"); |
| templates/seats.html | 995 | document.body.classList.remove("seat-simple-mode"); |
| templates/seats.html | 1023 | bar.className = "seat-simple-bottom-bar"; |
| templates/seats.html | 1025 | <button type="button" class="seat-simple-bottom-item primary" id="seatSimpleOpenDurak"> |
| templates/seats.html | 1030 | <a class="seat-simple-bottom-item" href="{{ url_for('hesap_page') }}"> |
| templates/seats.html | 1035 | <a class="seat-simple-bottom-item" href="{{ url_for('consignments_page') }}"> |
| templates/seats.html | 1040 | <a class="seat-simple-bottom-item" href="{{ url_for('live_map_page') }}"> |
| templates/seats.html | 1045 | <button type="button" class="seat-simple-bottom-item warn" id="seatSimpleVoiceBtn" title="Sesli Komut" aria-label="Sesli Komut"> |
| templates/seats_parts/deck.html | 23 | <div class="fab-column" aria-label="Hızlı işlemler"> |
| templates/seats_parts/deck.html | 24 | <button class="fab primary" id="fabBulk" type="button" title="Toplu Giriş">＋</button> |
| templates/seats_parts/deck.html | 25 | <button class="fab green" id="fabCash" type="button" title="Hızlı Tahsilat">₺</button> |
| templates/seats_parts/deck.html | 26 | <button class="fab orange" id="btnOffloadNow" type="button" title="İndir">⇩</button> |
| templates/seats_parts/finish_trip_modal.html | 40 | position:fixed; |
| templates/seats_parts/offload_confirm.html | 4 | position:fixed; |
| templates/settings.html | 52 | position:fixed; |
| templates/settings.html | 364 | position:fixed; |
| templates/settings_password.html | 45 | position:fixed; |
| templates/settings_profile.html | 44 | position:fixed; |
| templates/settings_recovery.html | 45 | position:fixed; |
| templates/settings_recovery.html | 340 | position:fixed; |
| templates/settings_recovery.html | 367 | position:fixed; |
| templates/settings_subscription.html | 42 | position:fixed; |
| templates/settings_subscription.html | 449 | position:fixed; |
| templates/trip_report.html | 330 | position:fixed; |
| templates/trip_report.html | 338 | position:fixed; |
| templates/trip_report.html | 613 | return "₺" + n.toFixed(0); |

## 9) İlk Karar Notu

Bu rapordan sonra:
1. Aktif çalışan yama sayısı kesinleşecek.
2. Koltuk modalını etkileyen aktif yamalar ayrılacak.
3. Sonradan eklenen ama aktif olan dosyalar incelenecek.
4. Orphan/disabled/backuplar temizlik adayı olarak sınıflandırılacak.
5. Silme hâlâ yok; önce rapor, sonra kontrollü arşivleme.
