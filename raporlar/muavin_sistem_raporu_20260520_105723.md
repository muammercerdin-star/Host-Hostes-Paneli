# Muavin Asistanı Sistem ve Çakışma Raporu

Rapor zamanı: `2026-05-20 10:57:24`
Çalışma klasörü: `/data/data/com.termux/files/home/Host-Hostes-Paneli`

## 1) Genel kanaat

Bu rapor kodu değiştirmez; sadece dosya, JS/CSS yükleme sırası, veritabanı farkları ve muhtemel çakışma noktalarını inceler.

Bu sistemde muhtemel çakışma türleri:

- **CSS override:** Sonradan yüklenen patch CSS dosyaları ana görünümü değiştirebilir.
- **JS runtime override:** Sonradan yüklenen patch JS dosyaları ana `seats.js` davranışını değiştirebilir.
- **Veri kaynağı farkı:** Ana DB, APK seed DB ve apk_payload DB farklı olabilir.
- **Mantık çakışması:** `canlı durak`, `seçili durak`, `sıradaki durak`, `işlemli durak` aynı şey gibi ele alınırsa ekranlar farklı davranır.

## 2) Kritik dosya envanteri

| Dosya | Var | Satır | Boyut | SHA12 |
| --- | --- | --- | --- | --- |
| app.py | VAR | 4378 | 134932 | 5af7b47ec06d |
| templates/seats.html | VAR | 1088 | 33028 | 7cb77c6f5d1b |
| templates/continue_trip.html | VAR | 5428 | 133505 | 04715057b598 |
| templates/live_map.html | VAR | 2927 | 71650 | b0c335361d9c |
| templates/routes_list.html | VAR | 485 | 10157 | feb6f12310b3 |
| templates/route_edit.html | VAR | 804 | 17813 | dea06ace55d1 |
| static/seats/seats.js | VAR | 2892 | 84287 | c0234168110a |
| static/seats/route-marquee.js | VAR | 46 | 1045 | 8d06927a0722 |
| static/seats/drive-eta-chip.js | VAR | 65 | 1804 | 74e4cb065488 |
| static/seats/drive-controls.js | VAR | 287 | 7542 | e05214b3f6cf |
| static/seats/seats.css | VAR | 4872 | 102903 | 5473bcd300d0 |
| static/seats/seats-final.css | VAR | 2564 | 68499 | 6d10277852f4 |
| static/seats/patches/stop-flow-focus-patch.js | VAR | 343 | 10723 | 47e108914b94 |
| static/seats/patches/stop-flow-focus-patch.css | VAR | 178 | 3988 | 383d9d45a418 |
| static/seats/patches/stop-flow-compact-mobile.css | VAR | 107 | 2497 | 3ab54340a0cd |
| static/seats/patches/mobile-performance-fix.css | VAR | 179 | 3688 | ebb9eb4d201a |
| static/seats/patches/seat-simple-ui-pack.js | VAR | 279 | 7259 | ab923a78a462 |
| static/seats/patches/seat-simple-ui-pack.css | VAR | 398 | 9005 | 37874d3bba93 |
| static/seats/patches/seat-layout-fab-pack.js | VAR | 168 | 4474 | d15660098d60 |
| static/seats/patches/seat-layout-fab-pack.css | VAR | 409 | 11324 | 4c1589bd069a |
| android_app/app/src/main/python/app.py | VAR | 4363 | 134501 | 90f31780e4ec |
| android_app/app/src/main/python/templates/seats.html | VAR | 1088 | 33028 | 7cb77c6f5d1b |
| android_app/app/src/main/python/static/seats/seats.js | VAR | 2892 | 84287 | c0234168110a |
| android_app/app/src/main/python/seed/db.sqlite3 | VAR | 6749 | 483328 | 450f9dcc3bb1 |
| apk_payload/seed/db.sqlite3 | VAR | 6749 | 483328 | 450f9dcc3bb1 |
| db.sqlite3 | VAR | 7005 | 2523136 | 54e0ee8a1e09 |

## 3) seats.html yükleme sırası

### CSS

| Sıra | Dosya |
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

### JavaScript

| Sıra | Dosya |
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
| 11 | /static/seats/patches/stop-flow-focus-patch.js?v=1 |
| 12 | /static/seats/patches/seat-layout-fab-pack.js?v=1 |
| 13 | /static/seats/patches/modal-bottom-nav-autohide.js?v=1 |
| 14 | /static/seats/patches/manual-ticket-system.js?v=1 |
| 15 | /static/seats/patches/top-sound-toggle.js?v=1 |
| 16 | /static/seats/patches/seat-simple-ui-pack.js?v=1 |

### Yükleme sırası yorumu

- Patch CSS dosyaları ana CSS dosyalarından sonra yükleniyor. Bu normal ama override riski taşır.
- Patch JS dosyaları ana `seats.js` dosyasından sonra yükleniyor. Bu da davranış override riski taşır.
- `mobile-performance-fix.css` aktif yüklenmiyor.

## 4) HTML duplicate id kontrolü

### templates/seats.html
Duplicate id görünmüyor.

### templates/continue_trip.html
Duplicate id görünmüyor.

### templates/live_map.html
Duplicate id görünmüyor.

## 5) JS çakışma taraması

| Dosya | liveStop | selectedStop | routeStrip | localStorage | innerHTML | MutationObserver | window export | fetch |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| static/seats/bags.js | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 2 |
| static/seats/voice-commands.js | 15 | 15 | 0 | 0 | 2 | 0 | 7 | 5 |
| static/seats/standing.js | 2 | 2 | 0 | 2 | 2 | 0 | 1 | 6 |
| static/seats/seats.js | 60 | 30 | 24 | 31 | 15 | 0 | 4 | 15 |
| static/seats/route-marquee.js | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 |
| static/seats/seats-time-prayer.js | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 2 |
| static/seats/voice-tts.js | 0 | 0 | 3 | 2 | 1 | 0 | 4 | 0 |
| static/seats/drive-eta-chip.js | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 |
| static/seats/drive-controls.js | 8 | 0 | 4 | 6 | 3 | 0 | 1 | 0 |
| static/seats/patches/stop-selected-toast.js | 0 | 0 | 0 | 0 | 1 | 0 | 2 | 0 |
| static/seats/patches/stop-flow-focus-patch.js | 1 | 13 | 3 | 2 | 2 | 0 | 8 | 0 |
| static/seats/patches/seat-layout-fab-pack.js | 0 | 0 | 0 | 0 | 0 | 1 | 2 | 0 |
| static/seats/patches/modal-bottom-nav-autohide.js | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 |
| static/seats/patches/manual-ticket-system.js | 0 | 0 | 0 | 3 | 0 | 1 | 4 | 0 |
| static/seats/patches/top-sound-toggle.js | 0 | 0 | 0 | 3 | 1 | 1 | 1 | 0 |
| static/seats/patches/seat-simple-ui-pack.js | 0 | 1 | 2 | 2 | 2 | 1 | 3 | 0 |

### JS risk yorumu

- `seats.js` canlı durak, seçili durak, rota şeridi ve backend runtime yazma işlerini taşıyan ana dosya gibi görünüyor.
- Patch JS dosyaları `seats.js` sonrasında yüklenirse, aynı DOM alanlarına müdahale ettiğinde çakışma olabilir.
- `MutationObserver` ve `innerHTML` yoğun kullanılan yerlerde sonsuz tetikleme / ekrana tekrar basma riski vardır.
- `selectedStopBadge`, `topLiveStop`, `routeStrip`, `liveStop` aynı anda birden fazla dosyada değiştiriliyorsa runtime çakışması mümkündür.

## 6) CSS çakışma taraması

| CSS dosyası | kritik eşleşme sayısı |
| --- | --- |
| static/style.css | 6 |
| static/seats/seats.css | 236 |
| static/seats/seats-final.css | 112 |
| static/seats/patches/stop-selected-toast.css | 9 |
| static/seats/patches/stop-flow-focus-patch.css | 12 |
| static/seats/patches/stop-flow-compact-mobile.css | 4 |
| static/seats/patches/seat-layout-fab-pack.css | 18 |
| static/seats/patches/bottom-voice-command.css | 4 |
| static/seats/patches/modal-bottom-nav-autohide.css | 3 |
| static/seats/patches/manual-ticket-system.css | 3 |
| static/seats/patches/top-sound-toggle.css | 9 |
| static/seats/patches/seat-simple-ui-pack.css | 27 |
| static/seats/patches/fab-sheet-solid-fix.css | 1 |
| static/seats/patches/seat-label-ghost-clean.css | 2 |

### CSS risk yorumu

- CSS dosyaları veriyi değiştirmez; fakat kartların görünmemesi, üst üste binme, tıklanamama, kırpılma ve mod geçiş hissi CSS kaynaklı olabilir.
- Veri yanlışsa asıl şüphe JS veya DB tarafıdır; görünüm yanlışsa CSS tarafıdır.

## 7) Veritabanı karşılaştırması

| DB | Var | Tablo sayısı | Aktif sefer | Runtime live_stop |
| --- | --- | --- | --- | --- |
| db.sqlite3 | True | 27 | 292 | Antalya – İstanbul | Ortahan |
| android_app/app/src/main/python/seed/db.sqlite3 | True | 21 | 276 | Denizli – İstanbul | - |
| apk_payload/seed/db.sqlite3 | True | 21 | 276 | Denizli – İstanbul | - |

### Rota id / durak sayısı karşılaştırması

| Hat | Ana DB | Android seed | APK payload |
| --- | --- | --- | --- |
| Antalya – İstanbul | id=19, durak=42 | id=14, durak=42 | id=14, durak=42 |
| Denizli – İstanbul | id=4, durak=56 | id=4, durak=56 | id=4, durak=56 |
| Denizli – İzmir | id=7, durak=32 | id=7, durak=32 | id=7, durak=32 |
| Denizli-İstanbul (Vardön) | id=16, durak=41 | id=16, durak=41 | id=16, durak=41 |
| Sarıgöl-Çanakkale | id=15, durak=3 | id=15, durak=3 | id=15, durak=3 |
| İstanbul - Antalya | id=18, durak=33 | id=18, durak=33 | id=18, durak=33 |
| İstanbul – Antalya | id=6, durak=33 | id=6, durak=33 | id=6, durak=33 |
| İstanbul – Denizli | id=10, durak=43 | id=10, durak=43 | id=10, durak=43 |
| İstanbul-Denizli(Vardön) | id=17, durak=40 | id=17, durak=40 | id=17, durak=40 |
| İzmir – Denizli | id=8, durak=35 | id=8, durak=35 | id=8, durak=35 |

### Kritik hat detayları

#### İstanbul – Antalya
- `db.sqlite3`: id=6, durak=33, koordinat=47, eksik_koordinat=0, hata=None
  - Saat profili: id=5 | İstanbul 14:30 → Antalya | item=33 | default=1
- `android_app/app/src/main/python/seed/db.sqlite3`: id=6, durak=33, koordinat=47, eksik_koordinat=0, hata=None
  - Saat profili: id=5 | İstanbul 14:30 → Antalya | item=33 | default=1
- `apk_payload/seed/db.sqlite3`: id=6, durak=33, koordinat=47, eksik_koordinat=0, hata=None
  - Saat profili: id=5 | İstanbul 14:30 → Antalya | item=33 | default=1

#### Antalya – İstanbul
- `db.sqlite3`: id=19, durak=42, koordinat=36, eksik_koordinat=7, hata=None
  - Eksikler: Çavdır, Acıpayam Kavşağı, Gölmarmara, 70 Evler, Zümrütevler (Huzur Evi), Arabalı Vapur / Harem İskele, Sirkeci
  - Saat profili: id=4 | Antalya 17:00 → Esenler | item=42 | default=1
- `android_app/app/src/main/python/seed/db.sqlite3`: id=14, durak=42, koordinat=36, eksik_koordinat=7, hata=None
  - Eksikler: Çavdır, Acıpayam Kavşağı, Gölmarmara, 70 Evler, Zümrütevler (Huzur Evi), Arabalı Vapur / Harem İskele, Sirkeci
  - Saat profili: id=4 | Antalya 17:00 → Esenler | item=42 | default=1
- `apk_payload/seed/db.sqlite3`: id=14, durak=42, koordinat=36, eksik_koordinat=7, hata=None
  - Eksikler: Çavdır, Acıpayam Kavşağı, Gölmarmara, 70 Evler, Zümrütevler (Huzur Evi), Arabalı Vapur / Harem İskele, Sirkeci
  - Saat profili: id=4 | Antalya 17:00 → Esenler | item=42 | default=1

#### İstanbul - Antalya
- `db.sqlite3`: id=18, durak=33, koordinat=33, eksik_koordinat=0, hata=None
  - Saat profili: id=6 | İstanbul 14:30 → Antalya | item=33 | default=1
- `android_app/app/src/main/python/seed/db.sqlite3`: id=18, durak=33, koordinat=33, eksik_koordinat=0, hata=None
  - Saat profili: id=6 | İstanbul 14:30 → Antalya | item=33 | default=1
- `apk_payload/seed/db.sqlite3`: id=18, durak=33, koordinat=33, eksik_koordinat=0, hata=None
  - Saat profili: id=6 | İstanbul 14:30 → Antalya | item=33 | default=1

## 8) Backend endpoint / runtime kontrolü

### live_runtime_state
- `808`: `def ensure_live_runtime_state_table() -> None:`
- `812`: `CREATE TABLE IF NOT EXISTS live_runtime_state(`
- `826`: `def fetch_live_runtime_state(trip_id: int) -> dict:`
- `827`: `ensure_live_runtime_state_table()`
- `831`: `FROM live_runtime_state`
- `857`: `def upsert_live_runtime_state(`
- `866`: `ensure_live_runtime_state_table()`
- `870`: `INSERT INTO live_runtime_state(trip_id, live_stop, speed, gps_km, eta_main, eta_sub, updated_at)`
- `908`: `def api_live_runtime_state():`
- `932`: `upsert_live_runtime_state(`
- `940`: `return jsonify({"ok": True, "state": fetch_live_runtime_state(tid)})`
- `942`: `return jsonify({"ok": True, "state": fetch_live_runtime_state(tid)})`
- `1456`: `live_runtime = fetch_live_runtime_state(tid)`
- `2841`: `live_runtime = fetch_live_runtime_state(tid)`
- `3195`: `"fetch_live_runtime_state": fetch_live_runtime_state,`
- `4244`: `ensure_live_runtime_state_table()`
- `4245`: `db.execute("DELETE FROM live_runtime_state WHERE trip_id=?", (tid,))`

### route_edit
Eşleşme yok.

### route_stop_coords
- `510`: `CREATE TABLE IF NOT EXISTS route_stop_coords(`
- `2856`: `FROM route_stop_coords`
- `2876`: `FROM route_stop_coords`

### get_stops
- `255`: `ROUTE_STOPS = {`
- `958`: `def get_stops(route_name: str):`
- `965`: `return ROUTE_STOPS.get(route_name, ROUTE_STOPS.get("Denizli – İstanbul", []))`
- `970`: `return list(dict.fromkeys(list(ROUTE_STOPS.keys()) + dyn))`
- `3149`: `"ROUTE_STOPS": ROUTE_STOPS,`

## 9) İlk teşhis

Bu rapora göre özellikle şu konulara bakılmalı:

1. **DB kopyaları aynı mı?** Ana DB ile APK seed/payload DB arasında id ve durak sayısı farkı varsa, APK ve Chrome farklı davranır.
2. **Durak Akışı tek kaynak mı kullanıyor?** `seats.js`, `stop-flow-focus-patch.js`, `continue_trip.html` canlı/seçili durak bilgisini ayrı kaynaklardan alıyorsa ekranlar farklı gösterir.
3. **liveStop işlemli durak gibi mi davranıyor?** Eğer canlı durak sadece işlem varsa tutuluyorsa, işlem olmayan mevcut durakta boş görünebilir.
4. **Patch JS dosyaları ana JS’ten sonra yükleniyor mu?** Evetse, aynı DOM alanlarına yazan patchler davranışı değiştirebilir.
5. **CSS mi veri mi?** Görünüm/kırpma CSS; yanlış durak/km/ETA JS veya DB mantığıdır.

## 10) Ham eşleşme dosyası

Detaylı grep eşleşmeleri ayrıca şurada: `raporlar/muavin_sistem_raw_20260520_105723.txt`
