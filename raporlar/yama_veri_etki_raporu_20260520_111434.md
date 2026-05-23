# Yama / Veri Etki Raporu

Tarih: `2026-05-20 11:14:34`

## 1) Kısa açıklama

Bu rapor yamaların veriye, koordinata, km/ETA hesaplarına veya sadece görünüme etki edip etmediğini ayırmak için hazırlandı.

Genel kural:

- CSS yamaları veritabanını ve km hesabını doğrudan bozmaz; sadece görünümü/tıklamayı etkiler.
- JS yamaları canlı durak, seçili durak, localStorage, km/ETA ve backend fetch çağrılarına dokunuyorsa veri davranışını bozabilir.

## 2) Aktif seats.html yükleme sırası

### CSS
| Sıra | Aktif CSS |
| --- | --- |
| 1 | /static/style.css |
| 2 | /static/seats/seats.css?v=41 |
| 3 | /static/seats/seats-final.css?v=drive-voice-real-width-test-1 |
| 4 | /static/seats/patches/stop-selected-toast.css?v=1 |
| 5 | /static/seats/patches/stop-flow-focus-patch.css?v=1 |
| 6 | /static/seats/patches/stop-flow-compact-mobile.css?v=1 |
| 7 | /static/seats/patches/seat-layout-fab-pack.css?v=1 |
| 8 | /static/seats/patches/bottom-voice-command.css?v=1 |
| 9 | /static/seats/patches/modal-bottom-nav-autohide.css?v=1 |
| 10 | /static/seats/patches/manual-ticket-system.css?v=1 |
| 11 | /static/seats/patches/top-sound-toggle.css?v=1 |
| 12 | /static/seats/patches/seat-simple-ui-pack.css?v=1 |
| 13 | /static/seats/patches/fab-sheet-solid-fix.css?v=1 |
| 14 | /static/seats/patches/seat-label-ghost-clean.css?v=1 |

### JS
| Sıra | Aktif JS |
| --- | --- |
| 1 | /static/seats/bags.js?v=1 |
| 2 | /static/seats/voice-commands.js?v=voice-listen-guard-1 |
| 3 | /static/seats/standing.js?v=1 |
| 4 | /static/seats/seats.js?v=clear-ticket-on-offload-1 |
| 5 | /static/seats/route-marquee.js?v=route-clean-ticker-single-1 |
| 6 | /static/seats/seats-time-prayer.js?v=time-prayer-apk-1 |
| 7 | /static/seats/voice-tts.js?v=voice-owner-fix-1 |
| 8 | /static/seats/drive-eta-chip.js?v=1 |
| 9 | /static/seats/drive-controls.js?v=drive-toggle-fix-1 |
| 10 | /static/seats/patches/stop-selected-toast.js?v=1 |
| 11 | /static/seats/patches/stop-flow-focus-patch.js?v=simple-scope-1 |
| 12 | /static/seats/patches/seat-layout-fab-pack.js?v=1 |
| 13 | /static/seats/patches/modal-bottom-nav-autohide.js?v=1 |
| 14 | /static/seats/patches/manual-ticket-system.js?v=1 |
| 15 | /static/seats/patches/top-sound-toggle.js?v=1 |
| 16 | /static/seats/patches/seat-simple-ui-pack.js?v=1 |

## 3) Aktif JS dosyalarının veri bozma riski

| Sıra | Dosya | Risk | Canlı | Seçili | Durak Akışı | Koordinat/km | ETA | localStorage | DOM | click | observer | fetch | window |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | static/seats/bags.js | ORTA | 0 | 0 | 0 | 0 | 24 | 0 | 7 | 0 | 0 | 2 | 1 |
| 2 | static/seats/voice-commands.js | YÜKSEK | 15 | 30 | 0 | 14 | 17 | 0 | 3 | 0 | 3 | 5 | 7 |
| 3 | static/seats/standing.js | YÜKSEK | 2 | 2 | 0 | 3 | 0 | 2 | 5 | 1 | 0 | 6 | 1 |
| 4 | static/seats/seats.js | YÜKSEK | 67 | 38 | 25 | 285 | 184 | 31 | 71 | 12 | 6 | 15 | 4 |
| 5 | static/seats/route-marquee.js | ORTA | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 3 | 0 | 1 |
| 6 | static/seats/seats-time-prayer.js | ORTA | 0 | 0 | 0 | 34 | 0 | 0 | 6 | 0 | 2 | 2 | 0 |
| 7 | static/seats/voice-tts.js | YÜKSEK | 0 | 0 | 3 | 0 | 1 | 2 | 3 | 3 | 1 | 0 | 4 |
| 8 | static/seats/drive-eta-chip.js | ORTA | 0 | 0 | 0 | 0 | 27 | 0 | 4 | 0 | 1 | 0 | 1 |
| 9 | static/seats/drive-controls.js | YÜKSEK | 8 | 0 | 4 | 1 | 6 | 6 | 7 | 2 | 7 | 0 | 1 |
| 10 | static/seats/patches/stop-selected-toast.js | ORTA | 0 | 0 | 0 | 0 | 2 | 0 | 6 | 0 | 1 | 0 | 2 |
| 11 | static/seats/patches/stop-flow-focus-patch.js | YÜKSEK | 1 | 28 | 19 | 0 | 16 | 3 | 26 | 7 | 5 | 0 | 8 |
| 12 | static/seats/patches/seat-layout-fab-pack.js | ORTA | 0 | 0 | 0 | 0 | 16 | 0 | 2 | 0 | 14 | 0 | 2 |
| 13 | static/seats/patches/modal-bottom-nav-autohide.js | YÜKSEK | 0 | 0 | 0 | 6 | 14 | 0 | 3 | 1 | 5 | 0 | 1 |
| 14 | static/seats/patches/manual-ticket-system.js | ORTA | 0 | 0 | 0 | 0 | 9 | 3 | 12 | 1 | 10 | 0 | 4 |
| 15 | static/seats/patches/top-sound-toggle.js | ORTA | 0 | 0 | 0 | 0 | 8 | 3 | 4 | 3 | 5 | 0 | 1 |
| 16 | static/seats/patches/seat-simple-ui-pack.js | YÜKSEK | 0 | 1 | 2 | 4 | 1 | 2 | 11 | 2 | 11 | 0 | 3 |

## 4) Aktif CSS dosyalarının görünüm/tıklama riski

| Sıra | Dosya | Risk | Durak görünüm | Kırpma | Gizleme | Tıklama/z-index | Performans |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | static/style.css | ORTA GÖRÜNÜM RİSKİ | 0 | 7 | 2 | 6 | 7 |
| 2 | static/seats/seats.css | YÜKSEK GÖRÜNÜM RİSKİ | 44 | 604 | 21 | 54 | 67 |
| 3 | static/seats/seats-final.css | YÜKSEK GÖRÜNÜM RİSKİ | 39 | 298 | 16 | 8 | 23 |
| 4 | static/seats/patches/stop-selected-toast.css | ORTA GÖRÜNÜM RİSKİ | 0 | 9 | 1 | 3 | 6 |
| 5 | static/seats/patches/stop-flow-focus-patch.css | YÜKSEK GÖRÜNÜM RİSKİ | 21 | 18 | 1 | 2 | 1 |
| 6 | static/seats/patches/stop-flow-compact-mobile.css | DÜŞÜK GÖRÜNÜM RİSKİ | 18 | 17 | 0 | 0 | 0 |
| 7 | static/seats/patches/seat-layout-fab-pack.css | ORTA GÖRÜNÜM RİSKİ | 0 | 44 | 0 | 11 | 13 |
| 8 | static/seats/patches/bottom-voice-command.css | DÜŞÜK GÖRÜNÜM RİSKİ | 0 | 1 | 0 | 0 | 0 |
| 9 | static/seats/patches/modal-bottom-nav-autohide.css | ORTA GÖRÜNÜM RİSKİ | 0 | 0 | 3 | 1 | 0 |
| 10 | static/seats/patches/manual-ticket-system.css | ORTA GÖRÜNÜM RİSKİ | 0 | 8 | 1 | 3 | 0 |
| 11 | static/seats/patches/top-sound-toggle.css | DÜŞÜK GÖRÜNÜM RİSKİ | 0 | 8 | 0 | 0 | 1 |
| 12 | static/seats/patches/seat-simple-ui-pack.css | YÜKSEK GÖRÜNÜM RİSKİ | 5 | 32 | 9 | 3 | 4 |
| 13 | static/seats/patches/fab-sheet-solid-fix.css | ORTA GÖRÜNÜM RİSKİ | 0 | 1 | 0 | 1 | 2 |
| 14 | static/seats/patches/seat-label-ghost-clean.css | ORTA GÖRÜNÜM RİSKİ | 0 | 5 | 2 | 0 | 2 |

## 5) DB / koordinat / runtime mevcut durum

| Alan | Değer |
| --- | --- |
| Aktif sefer | 292 | Antalya – İstanbul | 10:26 |
| runtime.live_stop | Ortahan |
| runtime.gps_km |  |
| runtime.eta_main | 653 dk erken |
| runtime.eta_sub | Ortahan · plan 22:10 · ETA 11:17 · Saat kaydırma |
| route id | 19 |
| route durak sayısı | 42 |
| koordinat kaydı | 36 |
| eksik koordinat | 7 |
| eksik koordinatlar | Çavdır, Acıpayam Kavşağı, Gölmarmara, 70 Evler, Zümrütevler (Huzur Evi), Arabalı Vapur / Harem İskele, Sirkeci |
| saat profili 4 | Antalya 17:00 → Esenler | item=42 |

## 6) Özellikle şüpheli aktif yamalar

| Dosya | Risk | Sebep |
| --- | --- | --- |
| static/seats/bags.js | ORTA | km/ETA/koordinat kelimeleri var, window fonksiyonlarını override ediyor |
| static/seats/voice-commands.js | YÜKSEK | km/ETA/koordinat kelimeleri var, canlı/seçili durak mantığına dokunuyor, window fonksiyonlarını override ediyor |
| static/seats/standing.js | YÜKSEK | km/ETA/koordinat kelimeleri var, canlı/seçili durak mantığına dokunuyor, click yakalıyor, window fonksiyonlarını override ediyor |
| static/seats/seats.js | YÜKSEK | km/ETA/koordinat kelimeleri var, canlı/seçili durak mantığına dokunuyor, Durak Akışı DOM’una dokunuyor, click yakalıyor, window fonksiyonlarını override ediyor |
| static/seats/route-marquee.js | ORTA | km/ETA/koordinat kelimeleri var, window fonksiyonlarını override ediyor |
| static/seats/seats-time-prayer.js | ORTA | km/ETA/koordinat kelimeleri var |
| static/seats/voice-tts.js | YÜKSEK | km/ETA/koordinat kelimeleri var, Durak Akışı DOM’una dokunuyor, click yakalıyor, window fonksiyonlarını override ediyor |
| static/seats/drive-eta-chip.js | ORTA | km/ETA/koordinat kelimeleri var, window fonksiyonlarını override ediyor |
| static/seats/drive-controls.js | YÜKSEK | km/ETA/koordinat kelimeleri var, canlı/seçili durak mantığına dokunuyor, Durak Akışı DOM’una dokunuyor, click yakalıyor, window fonksiyonlarını override ediyor |
| static/seats/patches/stop-selected-toast.js | ORTA | km/ETA/koordinat kelimeleri var, window fonksiyonlarını override ediyor |
| static/seats/patches/stop-flow-focus-patch.js | YÜKSEK | km/ETA/koordinat kelimeleri var, canlı/seçili durak mantığına dokunuyor, Durak Akışı DOM’una dokunuyor, click yakalıyor, window fonksiyonlarını override ediyor |
| static/seats/patches/seat-layout-fab-pack.js | ORTA | km/ETA/koordinat kelimeleri var, window fonksiyonlarını override ediyor |
| static/seats/patches/modal-bottom-nav-autohide.js | YÜKSEK | km/ETA/koordinat kelimeleri var, click yakalıyor, window fonksiyonlarını override ediyor |
| static/seats/patches/manual-ticket-system.js | ORTA | km/ETA/koordinat kelimeleri var, click yakalıyor, window fonksiyonlarını override ediyor |
| static/seats/patches/top-sound-toggle.js | ORTA | km/ETA/koordinat kelimeleri var, click yakalıyor, window fonksiyonlarını override ediyor |
| static/seats/patches/seat-simple-ui-pack.js | YÜKSEK | km/ETA/koordinat kelimeleri var, canlı/seçili durak mantığına dokunuyor, Durak Akışı DOM’una dokunuyor, click yakalıyor, window fonksiyonlarını override ediyor |

## 7) İlk sonuç

Bu rapora göre veri bozan yama ararken CSS dosyalarından çok JS dosyalarına bakılmalı.
Eğer km/ETA/koordinat bilgisi gelmiyorsa ana şüpheliler şunlardır:

1. `static/seats/seats.js` içindeki km/ETA/canlı durak hesap mantığı.
2. `stop-flow-focus-patch.js` gibi Durak Akışı ve seçili durak DOM’una müdahale eden patchler.
3. `drive-controls.js` gibi canlı durak/sürüş mantığına dokunan yardımcı dosyalar.
4. Eksik koordinatlar veya rota/saat profili uyuşmazlığı.

Ham risk satırları: `raporlar/yama_veri_etki_raw_20260520_111434.txt`