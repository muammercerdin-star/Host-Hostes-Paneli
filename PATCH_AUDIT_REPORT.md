# Muavin Asistanı Patch / Yama Audit Raporu

## Özet

- Toplam metin dosyası: **474**
- CSS dosyası: **69**
- JS dosyası: **58**
- HTML template: **47**
- Patch/yama gibi görünen dosya: **131**
- Gerçek yama dosyası: **131**
- Backup/eski yama dosyası: **0**
- Aktif/çağrılan yama: **121**
- Yetim/çağrılmayan yama: **10**
- Eksik static referansı: **77**
- CSS çakışma riski: **1353**
- JS syntax hatası: **kontrol edilmedi**

## 1) Aktif / çağrılan yamalar

- `SEATS_PATCH_ENVANTER_20260518_164328.txt`
- `_unused_review/static/seats/seats-redesign.css`
- `android_app/app/src/main/python/static/live_map/muavin_live_map_extra.css`
- `android_app/app/src/main/python/static/live_map/muavin_live_map_extra.js`
- `android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-final.css`
- `android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-tone.css`
- `android_app/app/src/main/python/static/seats/patches/bottom-voice-command.css`
- `android_app/app/src/main/python/static/seats/patches/fab-sheet-solid-fix.css`
- `android_app/app/src/main/python/static/seats/patches/manual-ticket-system.css`
- `android_app/app/src/main/python/static/seats/patches/manual-ticket-system.js`
- `android_app/app/src/main/python/static/seats/patches/mobile-performance-fix.css`
- `android_app/app/src/main/python/static/seats/patches/modal-bottom-nav-autohide.css`
- `android_app/app/src/main/python/static/seats/patches/modal-bottom-nav-autohide.js`
- `android_app/app/src/main/python/static/seats/patches/seat-label-ghost-clean.css`
- `android_app/app/src/main/python/static/seats/patches/seat-layout-fab-pack.css`
- `android_app/app/src/main/python/static/seats/patches/seat-layout-fab-pack.js`
- `android_app/app/src/main/python/static/seats/patches/seat-simple-ui-pack.css`
- `android_app/app/src/main/python/static/seats/patches/seat-simple-ui-pack.js`
- `android_app/app/src/main/python/static/seats/patches/stop-flow-compact-mobile.css`
- `android_app/app/src/main/python/static/seats/patches/stop-flow-focus-patch.css`
- `android_app/app/src/main/python/static/seats/patches/stop-flow-focus-patch.js`
- `android_app/app/src/main/python/static/seats/patches/stop-selected-toast.css`
- `android_app/app/src/main/python/static/seats/patches/stop-selected-toast.js`
- `android_app/app/src/main/python/static/seats/patches/top-sound-toggle.css`
- `android_app/app/src/main/python/static/seats/patches/top-sound-toggle.js`
- `android_app/app/src/main/python/static/seats/route-marquee.js`
- `android_app/app/src/main/python/static/seats/seats-final.css`
- `android_app/app/src/main/python/static/seats/seats-time-prayer.js`
- `android_app/app/src/main/python/static/seats/seats.css`
- `android_app/app/src/main/python/static/seats/seats.js`
- `android_app/app/src/main/python/templates/add_route.html`
- `android_app/app/src/main/python/templates/home.html`
- `android_app/app/src/main/python/templates/live_map.html`
- `android_app/app/src/main/python/templates/package_required.html`
- `android_app/app/src/main/python/templates/route_edit.html`
- `android_app/app/src/main/python/templates/route_schedule_edit.html`
- `android_app/app/src/main/python/templates/route_stops.html`
- `android_app/app/src/main/python/templates/routes_list.html`
- `android_app/app/src/main/python/templates/seats.html`
- `android_app/app/src/main/python/templates/seats_parts/route_flow.html`
- `android_app/app/src/main/python/templates/settings_package_requests.html`
- `apk_payload/static/live_map/muavin_live_map_extra.css`
- `apk_payload/static/live_map/muavin_live_map_extra.js`
- `apk_payload/static/seats/_archive_theme_trials/seats-dashboard-final.css`
- `apk_payload/static/seats/_archive_theme_trials/seats-dashboard-tone.css`
- `apk_payload/static/seats/patches/bottom-voice-command.css`
- `apk_payload/static/seats/patches/fab-sheet-solid-fix.css`
- `apk_payload/static/seats/patches/manual-ticket-system.css`
- `apk_payload/static/seats/patches/manual-ticket-system.js`
- `apk_payload/static/seats/patches/mobile-performance-fix.css`
- `apk_payload/static/seats/patches/modal-bottom-nav-autohide.css`
- `apk_payload/static/seats/patches/modal-bottom-nav-autohide.js`
- `apk_payload/static/seats/patches/seat-label-ghost-clean.css`
- `apk_payload/static/seats/patches/seat-layout-fab-pack.css`
- `apk_payload/static/seats/patches/seat-layout-fab-pack.js`
- `apk_payload/static/seats/patches/seat-simple-ui-pack.css`
- `apk_payload/static/seats/patches/seat-simple-ui-pack.js`
- `apk_payload/static/seats/patches/stop-flow-compact-mobile.css`
- `apk_payload/static/seats/patches/stop-flow-focus-patch.css`
- `apk_payload/static/seats/patches/stop-flow-focus-patch.js`
- `apk_payload/static/seats/patches/stop-selected-toast.css`
- `apk_payload/static/seats/patches/stop-selected-toast.js`
- `apk_payload/static/seats/patches/top-sound-toggle.css`
- `apk_payload/static/seats/patches/top-sound-toggle.js`
- `apk_payload/static/seats/route-marquee.js`
- `apk_payload/static/seats/seats-final.css`
- `apk_payload/static/seats/seats-time-prayer.js`
- `apk_payload/static/seats/seats.css`
- `apk_payload/static/seats/seats.js`
- `apk_payload/templates/add_route.html`
- `apk_payload/templates/home.html`
- `apk_payload/templates/live_map.html`
- `apk_payload/templates/package_required.html`
- `apk_payload/templates/route_edit.html`
- `apk_payload/templates/route_schedule_edit.html`
- `apk_payload/templates/route_stops.html`
- `apk_payload/templates/routes_list.html`
- `apk_payload/templates/seats.html`
- `apk_payload/templates/seats_parts/route_flow.html`
- `apk_payload/templates/settings_package_requests.html`
- `backups/apk_sync_20260520_234501/seats.html`
- `static/live_map/muavin_live_map_extra.css`
- `static/live_map/muavin_live_map_extra.js`
- `static/seats/_archive_theme_trials/seats-dashboard-final.css`
- `static/seats/_archive_theme_trials/seats-dashboard-tone.css`
- `static/seats/patches/bottom-voice-command.css`
- `static/seats/patches/fab-sheet-solid-fix.css`
- `static/seats/patches/manual-ticket-system.css`
- `static/seats/patches/manual-ticket-system.js`
- `static/seats/patches/mobile-performance-fix.css`
- `static/seats/patches/modal-bottom-nav-autohide.css`
- `static/seats/patches/modal-bottom-nav-autohide.js`
- `static/seats/patches/seat-label-ghost-clean.css`
- `static/seats/patches/seat-layout-fab-pack.css`
- `static/seats/patches/seat-layout-fab-pack.js`
- `static/seats/patches/seat-simple-ui-pack.css`
- `static/seats/patches/seat-simple-ui-pack.js`
- `static/seats/patches/stop-flow-compact-mobile.css`
- `static/seats/patches/stop-flow-focus-patch.css`
- `static/seats/patches/stop-flow-focus-patch.js`
- `static/seats/patches/stop-selected-toast.css`
- `static/seats/patches/stop-selected-toast.js`
- `static/seats/patches/top-sound-toggle.css`
- `static/seats/patches/top-sound-toggle.js`
- `static/seats/patches/unified-seat-deck-report-style.css`
- `static/seats/route-marquee.js`
- `static/seats/seats-final.css`
- `static/seats/seats-time-prayer.js`
- `static/seats/seats.css`
- `static/seats/seats.js`
- `templates/add_route.html`
- `templates/home.html`
- `templates/live_map.html`
- `templates/package_required.html`
- `templates/route_edit.html`
- `templates/route_schedule_edit.html`
- `templates/route_stops.html`
- `templates/routes_list.html`
- `templates/seats.html`
- `templates/seats_parts/route_flow.html`
- `templates/settings_package_requests.html`

## 2) Yetim / çağrılmayan yamalar

- `android_app/app/src/main/python/static/seats/patches/bottom-row-51-54-equal-spacing.css`
- `android_app/app/src/main/python/static/seats/patches/only-54-reapply-right-shift.css`
- `android_app/app/src/main/python/static/seats/patches/right-seat-column-spacing-fix.css`
- `apk_payload/static/seats/patches/bottom-row-51-54-equal-spacing.css`
- `apk_payload/static/seats/patches/only-54-reapply-right-shift.css`
- `apk_payload/static/seats/patches/right-seat-column-spacing-fix.css`
- `static/seats/patches/bottom-row-51-54-equal-spacing.css`
- `static/seats/patches/only-54-reapply-right-shift.css`
- `static/seats/patches/right-seat-column-spacing-fix.css`
- `tools/audit_patches.py`

## 3) Backup / eski yama dosyaları

- Yok

## 4) Eksik static referansları

- `static/([^` çağrılıyor ama dosya yok. Kaynak: AYARLAR_DETAY_RAPORU.txt, tools/project_tree_audit.py
- `static/...` çağrılıyor ama dosya yok. Kaynak: AYARLAR_DETAY_RAPORU.txt, tools/audit_files.py, tools/audit_patches.py, tools/project_tree_audit.py
- `static/css/style.css` çağrılıyor ama dosya yok. Kaynak: android_app/app/src/main/python/templates/base.html, apk_payload/templates/base.html, proje_flask_baglanti_raporu.txt, proje_template_haritasi.txt, templates/base.html
- `static/img/rehber-durak-akisi.png` çağrılıyor ama dosya yok. Kaynak: AYARLAR_DETAY_RAPORU.txt, android_app/app/src/main/python/templates/rehber.html, apk_payload/templates/rehber.html, templates/rehber.html
- `static/img/rehber-koltuk-yonetimi-card.png` çağrılıyor ama dosya yok. Kaynak: AYARLAR_DETAY_RAPORU.txt, android_app/app/src/main/python/templates/rehber.html, apk_payload/templates/rehber.html, templates/rehber.html
- `static/img/rehber-voice-command.png` çağrılıyor ama dosya yok. Kaynak: AYARLAR_DETAY_RAPORU.txt, android_app/app/src/main/python/templates/rehber.html, apk_payload/templates/rehber.html, templates/rehber.html
- `static/profile/{new_name}` çağrılıyor ama dosya yok. Kaynak: android_app/app/src/main/python/app.py, apk_payload/app.py, app.py, backups/apk_sync_20260520_234501/app.py
- `static/seats/bags.js?v=1` çağrılıyor ama dosya yok. Kaynak: AYARLAR_DETAY_RAPORU.txt, KOLTUK_PANEL_YAMA_RAPORU_20260516_153819.txt, SEATS_AKTIF_HARITA.txt, SEATS_DETAYLI_SISTEM_RAPORU_20260516_155924.txt, SEATS_HTML_A_DAN_Z_RAPORU_20260518_162041.txt
- `static/seats/drive-controls.js?v=1` çağrılıyor ama dosya yok. Kaynak: proje_template_haritasi.txt, seats_baglanti_haritasi.txt
- `static/seats/drive-controls.js?v=2` çağrılıyor ama dosya yok. Kaynak: SEATS_AKTIF_HARITA.txt, proje_template_haritasi.txt, seats_baglanti_haritasi.txt
- `static/seats/drive-controls.js?v=drive-toggle-fix-1` çağrılıyor ama dosya yok. Kaynak: AYARLAR_DETAY_RAPORU.txt, KOLTUK_PANEL_YAMA_RAPORU_20260516_153819.txt, SEATS_DETAYLI_SISTEM_RAPORU_20260516_155924.txt, SEATS_HTML_A_DAN_Z_RAPORU_20260518_162041.txt, SEATS_HTML_KALAN_YAMA_RAPORU_20260518_174156.txt
- `static/seats/drive-controls.js?v=voice-rollback-clean-1` çağrılıyor ama dosya yok. Kaynak: SON_YARIM_SAAT_YAMA_RAPORU_20260516_150801.txt
- `static/seats/drive-eta-chip.js?v=1` çağrılıyor ama dosya yok. Kaynak: AYARLAR_DETAY_RAPORU.txt, SEATS_DETAYLI_SISTEM_RAPORU_20260516_155924.txt, SEATS_HTML_A_DAN_Z_RAPORU_20260518_162041.txt, SEATS_HTML_KALAN_YAMA_RAPORU_20260518_174156.txt, SEATS_HTML_TEMIZLIK_RAPORU_20260518_153638.txt
- `static/seats/patches/bottom-voice-command.css?v=1` çağrılıyor ama dosya yok. Kaynak: AYARLAR_DETAY_RAPORU.txt, DURAK_AKISI_KAYNAK_RAPORU_20260518_205127.txt, SEATS_HTML_KALAN_YAMA_RAPORU_20260518_174156.txt, android_app/app/src/main/python/templates/seats.html, apk_payload/templates/seats.html
- `static/seats/patches/fab-sheet-solid-fix.css?v=1` çağrılıyor ama dosya yok. Kaynak: AYARLAR_DETAY_RAPORU.txt, android_app/app/src/main/python/templates/seats.html, apk_payload/templates/seats.html, backups/apk_sync_20260520_234501/seats.html, raporlar/asama1_durak_akisi_haritasi_20260520_110402.txt
- `static/seats/patches/manual-ticket-system.css?v=1` çağrılıyor ama dosya yok. Kaynak: AYARLAR_DETAY_RAPORU.txt, DURAK_AKISI_KAYNAK_RAPORU_20260518_205127.txt, SEATS_HTML_KALAN_YAMA_RAPORU_20260518_174156.txt, android_app/app/src/main/python/templates/seats.html, apk_payload/templates/seats.html
- `static/seats/patches/manual-ticket-system.js?v=1` çağrılıyor ama dosya yok. Kaynak: AYARLAR_DETAY_RAPORU.txt, DURAK_AKISI_KAYNAK_RAPORU_20260518_205127.txt, SEATS_HTML_KALAN_YAMA_RAPORU_20260518_174156.txt, android_app/app/src/main/python/templates/seats.html, apk_payload/templates/seats.html
- `static/seats/patches/mobile-performance-fix.css?v=2` çağrılıyor ama dosya yok. Kaynak: AYARLAR_DETAY_RAPORU.txt, DURAK_AKISI_KAYNAK_RAPORU_20260518_205127.txt, android_app/app/src/main/python/templates/seats.html, apk_payload/templates/seats.html, backups/apk_sync_20260520_234501/seats.html
- `static/seats/patches/modal-bottom-nav-autohide.css?v=1` çağrılıyor ama dosya yok. Kaynak: AYARLAR_DETAY_RAPORU.txt, DURAK_AKISI_KAYNAK_RAPORU_20260518_205127.txt, SEATS_HTML_KALAN_YAMA_RAPORU_20260518_174156.txt, android_app/app/src/main/python/templates/seats.html, apk_payload/templates/seats.html
- `static/seats/patches/modal-bottom-nav-autohide.js?v=1` çağrılıyor ama dosya yok. Kaynak: AYARLAR_DETAY_RAPORU.txt, DURAK_AKISI_KAYNAK_RAPORU_20260518_205127.txt, SEATS_HTML_KALAN_YAMA_RAPORU_20260518_174156.txt, android_app/app/src/main/python/templates/seats.html, apk_payload/templates/seats.html
- `static/seats/patches/seat-label-ghost-clean.css?v=1` çağrılıyor ama dosya yok. Kaynak: AYARLAR_DETAY_RAPORU.txt, android_app/app/src/main/python/templates/seats.html, apk_payload/templates/seats.html, backups/apk_sync_20260520_234501/seats.html, raporlar/asama1_durak_akisi_haritasi_20260520_110402.txt
- `static/seats/patches/seat-layout-fab-pack.css?v=1` çağrılıyor ama dosya yok. Kaynak: AYARLAR_DETAY_RAPORU.txt, DURAK_AKISI_KAYNAK_RAPORU_20260518_205127.txt, android_app/app/src/main/python/templates/seats.html, apk_payload/templates/seats.html, backups/apk_sync_20260520_234501/seats.html
- `static/seats/patches/seat-layout-fab-pack.js?v=1` çağrılıyor ama dosya yok. Kaynak: AYARLAR_DETAY_RAPORU.txt, DURAK_AKISI_KAYNAK_RAPORU_20260518_205127.txt, android_app/app/src/main/python/templates/seats.html, apk_payload/templates/seats.html, backups/apk_sync_20260520_234501/seats.html
- `static/seats/patches/seat-simple-ui-pack.css?v=1` çağrılıyor ama dosya yok. Kaynak: AYARLAR_DETAY_RAPORU.txt, DURAK_AKISI_KAYNAK_RAPORU_20260518_205127.txt, android_app/app/src/main/python/templates/seats.html, apk_payload/templates/seats.html, backups/apk_sync_20260520_234501/seats.html
- `static/seats/patches/seat-simple-ui-pack.js?v=1` çağrılıyor ama dosya yok. Kaynak: AYARLAR_DETAY_RAPORU.txt, DURAK_AKISI_KAYNAK_RAPORU_20260518_205127.txt, android_app/app/src/main/python/templates/seats.html, apk_payload/templates/seats.html, backups/apk_sync_20260520_234501/seats.html
- `static/seats/patches/stop-flow-compact-mobile.css?v=1` çağrılıyor ama dosya yok. Kaynak: AYARLAR_DETAY_RAPORU.txt, android_app/app/src/main/python/templates/seats.html, apk_payload/templates/seats.html, backups/apk_sync_20260520_234501/seats.html, raporlar/asama1_durak_akisi_haritasi_20260520_110402.txt
- `static/seats/patches/stop-flow-focus-patch.css?v=1` çağrılıyor ama dosya yok. Kaynak: AYARLAR_DETAY_RAPORU.txt, DURAK_AKISI_KAYNAK_RAPORU_20260518_205127.txt, android_app/app/src/main/python/templates/seats.html, apk_payload/templates/seats.html, backups/apk_sync_20260520_234501/seats.html
- `static/seats/patches/stop-flow-focus-patch.js?v=1` çağrılıyor ama dosya yok. Kaynak: DURAK_AKISI_KAYNAK_RAPORU_20260518_205127.txt, raporlar/asama1_durak_akisi_haritasi_20260520_110402.txt
- `static/seats/patches/stop-flow-focus-patch.js?v=simple-scope-1` çağrılıyor ama dosya yok. Kaynak: AYARLAR_DETAY_RAPORU.txt, android_app/app/src/main/python/templates/seats.html, apk_payload/templates/seats.html, backups/apk_sync_20260520_234501/seats.html, templates/seats.html
- `static/seats/patches/stop-selected-toast.css?v=1` çağrılıyor ama dosya yok. Kaynak: AYARLAR_DETAY_RAPORU.txt, DURAK_AKISI_KAYNAK_RAPORU_20260518_205127.txt, SEATS_HTML_KALAN_YAMA_RAPORU_20260518_174156.txt, android_app/app/src/main/python/templates/seats.html, apk_payload/templates/seats.html
- `static/seats/patches/stop-selected-toast.js?v=1` çağrılıyor ama dosya yok. Kaynak: AYARLAR_DETAY_RAPORU.txt, DURAK_AKISI_KAYNAK_RAPORU_20260518_205127.txt, SEATS_HTML_KALAN_YAMA_RAPORU_20260518_174156.txt, android_app/app/src/main/python/templates/seats.html, apk_payload/templates/seats.html
- `static/seats/patches/top-sound-toggle.css?v=1` çağrılıyor ama dosya yok. Kaynak: AYARLAR_DETAY_RAPORU.txt, DURAK_AKISI_KAYNAK_RAPORU_20260518_205127.txt, SEATS_HTML_KALAN_YAMA_RAPORU_20260518_174156.txt, android_app/app/src/main/python/templates/seats.html, apk_payload/templates/seats.html
- `static/seats/patches/top-sound-toggle.js?v=1` çağrılıyor ama dosya yok. Kaynak: AYARLAR_DETAY_RAPORU.txt, DURAK_AKISI_KAYNAK_RAPORU_20260518_205127.txt, SEATS_HTML_KALAN_YAMA_RAPORU_20260518_174156.txt, android_app/app/src/main/python/templates/seats.html, apk_payload/templates/seats.html
- `static/seats/patches/unified-seat-deck-report-style.css?v=seat-smaller-removed-2` çağrılıyor ama dosya yok. Kaynak: templates/seats.html
- `static/seats/route-marquee.js?v=route-clean-ticker-single-1` çağrılıyor ama dosya yok. Kaynak: AYARLAR_DETAY_RAPORU.txt, KOLTUK_PANEL_YAMA_RAPORU_20260516_153819.txt, SEATS_DETAYLI_SISTEM_RAPORU_20260516_155924.txt, SEATS_HTML_A_DAN_Z_RAPORU_20260518_162041.txt, SEATS_HTML_TEMIZLIK_RAPORU_20260518_153638.txt
- `static/seats/seats-dashboard-final.css?v=1` çağrılıyor ama dosya yok. Kaynak: proje_template_haritasi.txt
- `static/seats/seats-dashboard-tone.css?v=2` çağrılıyor ama dosya yok. Kaynak: proje_template_haritasi.txt
- `static/seats/seats-final.css?v=2` çağrılıyor ama dosya yok. Kaynak: SEATS_AKTIF_HARITA.txt
- `static/seats/seats-final.css?v=drive-voice-real-width-test-1` çağrılıyor ama dosya yok. Kaynak: AYARLAR_DETAY_RAPORU.txt, SEATS_DETAYLI_SISTEM_RAPORU_20260516_155924.txt, SEATS_HTML_A_DAN_Z_RAPORU_20260518_162041.txt, SEATS_HTML_KALAN_YAMA_RAPORU_20260518_174156.txt, SEATS_HTML_TEMIZLIK_RAPORU_20260518_153638.txt
- `static/seats/seats-redesign.css?v=2` çağrılıyor ama dosya yok. Kaynak: proje_template_haritasi.txt
- `static/seats/seats-redesign.css?v=3` çağrılıyor ama dosya yok. Kaynak: proje_template_haritasi.txt
- `static/seats/seats-time-prayer.js?v=time-prayer-apk-1` çağrılıyor ama dosya yok. Kaynak: AYARLAR_DETAY_RAPORU.txt, SEATS_DETAYLI_SISTEM_RAPORU_20260516_155924.txt, SEATS_HTML_A_DAN_Z_RAPORU_20260518_162041.txt, SEATS_HTML_TEMIZLIK_RAPORU_20260518_153638.txt, SON_YARIM_SAAT_YAMA_RAPORU_20260516_150801.txt
- `static/seats/seats.css?v=1` çağrılıyor ama dosya yok. Kaynak: proje_template_haritasi.txt, seats_baglanti_haritasi.txt
- `static/seats/seats.css?v=10` çağrılıyor ama dosya yok. Kaynak: proje_template_haritasi.txt, seats_baglanti_haritasi.txt
- `static/seats/seats.css?v=34` çağrılıyor ama dosya yok. Kaynak: proje_template_haritasi.txt, seats_baglanti_haritasi.txt
- `static/seats/seats.css?v=35` çağrılıyor ama dosya yok. Kaynak: proje_template_haritasi.txt, seats_baglanti_haritasi.txt
- `static/seats/seats.css?v=36` çağrılıyor ama dosya yok. Kaynak: proje_template_haritasi.txt, seats_baglanti_haritasi.txt
- `static/seats/seats.css?v=37` çağrılıyor ama dosya yok. Kaynak: proje_template_haritasi.txt, seats_baglanti_haritasi.txt
- `static/seats/seats.css?v=38` çağrılıyor ama dosya yok. Kaynak: proje_template_haritasi.txt, seats_baglanti_haritasi.txt
- `static/seats/seats.css?v=41` çağrılıyor ama dosya yok. Kaynak: AYARLAR_DETAY_RAPORU.txt, SEATS_AKTIF_HARITA.txt, SEATS_DETAYLI_SISTEM_RAPORU_20260516_155924.txt, SEATS_HTML_A_DAN_Z_RAPORU_20260518_162041.txt, SEATS_HTML_TEMIZLIK_RAPORU_20260518_153638.txt
- `static/seats/seats.js?v=1` çağrılıyor ama dosya yok. Kaynak: proje_template_haritasi.txt, seats_baglanti_haritasi.txt
- `static/seats/seats.js?v=17` çağrılıyor ama dosya yok. Kaynak: proje_template_haritasi.txt, seats_baglanti_haritasi.txt
- `static/seats/seats.js?v=19` çağrılıyor ama dosya yok. Kaynak: proje_template_haritasi.txt, seats_baglanti_haritasi.txt
- `static/seats/seats.js?v=20` çağrılıyor ama dosya yok. Kaynak: proje_template_haritasi.txt, seats_baglanti_haritasi.txt
- `static/seats/seats.js?v=20260430_100321` çağrılıyor ama dosya yok. Kaynak: proje_template_haritasi.txt, seats_baglanti_haritasi.txt
- `static/seats/seats.js?v=21` çağrılıyor ama dosya yok. Kaynak: proje_template_haritasi.txt, seats_baglanti_haritasi.txt
- `static/seats/seats.js?v=23` çağrılıyor ama dosya yok. Kaynak: proje_template_haritasi.txt, seats_baglanti_haritasi.txt
- `static/seats/seats.js?v=25` çağrılıyor ama dosya yok. Kaynak: proje_template_haritasi.txt, seats_baglanti_haritasi.txt
- `static/seats/seats.js?v=9` çağrılıyor ama dosya yok. Kaynak: proje_template_haritasi.txt, seats_baglanti_haritasi.txt
- `static/seats/seats.js?v=clear-ticket-on-offload-1` çağrılıyor ama dosya yok. Kaynak: SEATS_HTML_A_DAN_Z_RAPORU_20260518_162041.txt, SEATS_HTML_KALAN_YAMA_RAPORU_20260518_174156.txt, SEATS_HTML_TEMIZLIK_RAPORU_20260518_153638.txt, raporlar/asama1_durak_akisi_haritasi_20260520_110402.txt
- `static/seats/seats.js?v=drive-premium-rollback-1` çağrılıyor ama dosya yok. Kaynak: KOLTUK_PANEL_YAMA_RAPORU_20260516_153819.txt, SEATS_DETAYLI_SISTEM_RAPORU_20260516_155924.txt, SON_YARIM_SAAT_YAMA_RAPORU_20260516_150801.txt
- `static/seats/seats.js?v=eta20260430_082730` çağrılıyor ama dosya yok. Kaynak: proje_template_haritasi.txt, seats_baglanti_haritasi.txt
- `static/seats/seats.js?v=offload-modal-final-1` çağrılıyor ama dosya yok. Kaynak: SEATS_AKTIF_HARITA.txt
- `static/seats/seats.js?v=tripkey-by-id-1` çağrılıyor ama dosya yok. Kaynak: AYARLAR_DETAY_RAPORU.txt, android_app/app/src/main/python/templates/seats.html, apk_payload/templates/seats.html, backups/apk_sync_20260520_234501/seats.html, templates/seats.html
- `static/seats/seats.js?v=voice-rollback-clean-1` çağrılıyor ama dosya yok. Kaynak: SON_YARIM_SAAT_YAMA_RAPORU_20260516_150801.txt
- `static/seats/standing.js?v=1` çağrılıyor ama dosya yok. Kaynak: AYARLAR_DETAY_RAPORU.txt, KOLTUK_PANEL_YAMA_RAPORU_20260516_153819.txt, SEATS_AKTIF_HARITA.txt, SEATS_DETAYLI_SISTEM_RAPORU_20260516_155924.txt, SEATS_HTML_A_DAN_Z_RAPORU_20260518_162041.txt
- `static/seats/voice-commands.js?v=1` çağrılıyor ama dosya yok. Kaynak: SEATS_AKTIF_HARITA.txt, proje_template_haritasi.txt, seats_baglanti_haritasi.txt
- `static/seats/voice-commands.js?v=boarding-stop-priority-1` çağrılıyor ama dosya yok. Kaynak: SEATS_HTML_A_DAN_Z_RAPORU_20260518_162041.txt, SEATS_HTML_TEMIZLIK_RAPORU_20260518_153638.txt
- `static/seats/voice-commands.js?v=natural-total-voice-1` çağrılıyor ama dosya yok. Kaynak: KOLTUK_PANEL_YAMA_RAPORU_20260516_153819.txt, SEATS_DETAYLI_SISTEM_RAPORU_20260516_155924.txt, SON_YARIM_SAAT_YAMA_RAPORU_20260516_150801.txt
- `static/seats/voice-commands.js?v=voice-central-bridge-1` çağrılıyor ama dosya yok. Kaynak: KOLTUK_PANEL_YAMA_RAPORU_20260516_153819.txt, SEATS_DETAYLI_SISTEM_RAPORU_20260516_155924.txt, SON_YARIM_SAAT_YAMA_RAPORU_20260516_150801.txt
- `static/seats/voice-commands.js?v=voice-listen-guard-1` çağrılıyor ama dosya yok. Kaynak: AYARLAR_DETAY_RAPORU.txt, SEATS_HTML_KALAN_YAMA_RAPORU_20260518_174156.txt, android_app/app/src/main/python/templates/seats.html, apk_payload/templates/seats.html, backups/apk_sync_20260520_234501/seats.html
- `static/seats/voice-tts.js?v=voice-owner-fix-1` çağrılıyor ama dosya yok. Kaynak: AYARLAR_DETAY_RAPORU.txt, KOLTUK_PANEL_YAMA_RAPORU_20260516_153819.txt, SEATS_DETAYLI_SISTEM_RAPORU_20260516_155924.txt, SEATS_HTML_A_DAN_Z_RAPORU_20260518_162041.txt, SEATS_HTML_KALAN_YAMA_RAPORU_20260518_174156.txt
- `static/seats/voice-tts.js?v=voice-rollback-clean-1` çağrılıyor ama dosya yok. Kaynak: SON_YARIM_SAAT_YAMA_RAPORU_20260516_150801.txt
- `static/vendor/bootstrap.bundle.min.js` çağrılıyor ama dosya yok. Kaynak: proje_flask_baglanti_raporu.txt, proje_template_haritasi.txt
- `static/vendor/bootstrap.min.css` çağrılıyor ama dosya yok. Kaynak: proje_flask_baglanti_raporu.txt, proje_template_haritasi.txt
- `static/vendor/icons.css` çağrılıyor ama dosya yok. Kaynak: android_app/app/src/main/python/templates/base.html, apk_payload/templates/base.html, proje_flask_baglanti_raporu.txt, proje_template_haritasi.txt, templates/base.html
- `static/vendor/jquery.min.js` çağrılıyor ama dosya yok. Kaynak: android_app/app/src/main/python/templates/base.html, apk_payload/templates/base.html, proje_flask_baglanti_raporu.txt, proje_template_haritasi.txt, templates/base.html

## 5) Tekrarlanan inline style id

- Yok

## 6) Tekrarlanan inline script id

- Yok

## 7) Tekrarlanan START/END markerları

- `LAST_ROW_INNER_GAP_FIX_END` -> android_app/app/src/main/python/static/seats/seats.css, apk_payload/static/seats/seats.css, static/seats/seats.css
- `LAST_ROW_INNER_GAP_FIX_START` -> android_app/app/src/main/python/static/seats/seats.css, apk_payload/static/seats/seats.css, static/seats/seats.css
- `LAST_ROW_TIGHTER_FIX_END` -> android_app/app/src/main/python/static/seats/seats.css, apk_payload/static/seats/seats.css, static/seats/seats.css
- `LAST_ROW_TIGHTER_FIX_START` -> android_app/app/src/main/python/static/seats/seats.css, apk_payload/static/seats/seats.css, static/seats/seats.css
- `MOBILE_MODAL_READABILITY_FIX_END` -> android_app/app/src/main/python/static/seats/patches/mobile-performance-fix.css, apk_payload/static/seats/patches/mobile-performance-fix.css, static/seats/patches/mobile-performance-fix.css
- `MOBILE_MODAL_READABILITY_FIX_START` -> android_app/app/src/main/python/static/seats/patches/mobile-performance-fix.css, apk_payload/static/seats/patches/mobile-performance-fix.css, static/seats/patches/mobile-performance-fix.css
- `VOICE_DIRECT_BOARD_GENERAL_END` -> AYARLAR_DETAY_RAPORU.txt, android_app/app/src/main/python/static/seats/voice-commands.js, apk_payload/static/seats/voice-commands.js, static/seats/voice-commands.js
- `VOICE_DIRECT_BOARD_GENERAL_START` -> AYARLAR_DETAY_RAPORU.txt, android_app/app/src/main/python/static/seats/voice-commands.js, apk_payload/static/seats/voice-commands.js, static/seats/voice-commands.js
- `VOICE_SUMMARY_PATCH_END` -> AYARLAR_DETAY_RAPORU.txt, android_app/app/src/main/python/static/seats/voice-commands.js, apk_payload/static/seats/voice-commands.js, static/seats/voice-commands.js
- `VOICE_SUMMARY_PATCH_START` -> AYARLAR_DETAY_RAPORU.txt, android_app/app/src/main/python/static/seats/voice-commands.js, apk_payload/static/seats/voice-commands.js, static/seats/voice-commands.js

## 8) CSS çakışma riskleri — ilk 120

### `.voice-command-btn` / `min-width`
- `_unused_review/static/seats/seats-redesign.css` => `0 !important`
- `android_app/app/src/main/python/static/seats/seats.css` => `152px`
- `android_app/app/src/main/python/static/seats/seats.css` => `140px`
- `android_app/app/src/main/python/static/seats/seats.css` => `132px`
- `android_app/app/src/main/python/static/seats/seats.css` => `150px`
- `android_app/app/src/main/python/static/seats/seats.css` => `140px`
- `android_app/app/src/main/python/static/seats/seats.css` => `245px !important`
- `android_app/app/src/main/python/static/seats/seats.css` => `260px !important`
- `android_app/app/src/main/python/static/seats/seats.css` => `240px !important`
- `android_app/app/src/main/python/static/seats/seats.css` => `210px !important`
- `android_app/app/src/main/python/static/seats/seats.css` => `205px !important`
- `android_app/app/src/main/python/static/seats/seats.css` => `195px !important`
- ... 28 kayıt daha

### `.voice-command-btn` / `height`
- `android_app/app/src/main/python/static/seats/seats.css` => `44px`
- `android_app/app/src/main/python/static/seats/seats.css` => `40px`
- `android_app/app/src/main/python/static/seats/seats.css` => `42px`
- `android_app/app/src/main/python/static/seats/seats.css` => `56px !important`
- `android_app/app/src/main/python/static/seats/seats.css` => `54px !important`
- `android_app/app/src/main/python/static/seats/seats.css` => `52px !important`
- `android_app/app/src/main/python/static/seats/seats.css` => `54px !important`
- `android_app/app/src/main/python/static/seats/seats.css` => `52px !important`
- `android_app/app/src/main/python/static/seats/seats.css` => `50px !important`
- `android_app/app/src/main/python/static/seats/seats.css` => `68px !important`
- `android_app/app/src/main/python/static/seats/seats.css` => `62px !important`
- `android_app/app/src/main/python/static/seats/seats-final.css` => `44px !important`
- ... 24 kayıt daha

### `.board-title h2` / `font-size`
- `_unused_review/static/seats/seats-redesign.css` => `30px !important`
- `_unused_review/static/seats/seats-redesign.css` => `27px !important`
- `_unused_review/static/seats/seats-redesign.css` => `31px !important`
- `_unused_review/static/seats/seats-redesign.css` => `29px !important`
- `_unused_review/static/seats/seats-redesign.css` => `27px !important`
- `android_app/app/src/main/python/static/seats/seats.css` => `32px`
- `android_app/app/src/main/python/static/seats/seats.css` => `24px`
- `android_app/app/src/main/python/static/seats/seats.css` => `24px`
- `android_app/app/src/main/python/static/seats/seats.css` => `22px`
- `android_app/app/src/main/python/static/seats/seats-final.css` => `27px !important`
- `android_app/app/src/main/python/static/seats/seats-final.css` => `25px !important`
- `android_app/app/src/main/python/static/seats/seats-final.css` => `26px !important`
- ... 23 kayıt daha

### `.route-title` / `font-size`
- `android_app/app/src/main/python/static/seats/seats.css` => `clamp(24px, 3.5vw, 36px)`
- `android_app/app/src/main/python/static/seats/seats.css` => `clamp(20px, 7vw, 28px)`
- `android_app/app/src/main/python/static/seats/seats.css` => `28px`
- `android_app/app/src/main/python/static/seats/seats.css` => `25px`
- `android_app/app/src/main/python/static/seats/seats-final.css` => `clamp(23px,4.6vw,34px) !important`
- `android_app/app/src/main/python/static/seats/seats-final.css` => `24px !important`
- `android_app/app/src/main/python/static/seats/seats-final.css` => `clamp(22px,4.2vw,30px) !important`
- `android_app/app/src/main/python/static/seats/seats-final.css` => `23px !important`
- `android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-final.css` => `34px !important`
- `android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-final.css` => `28px !important`
- `android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-final.css` => `25px !important`
- `apk_payload/static/seats/seats.css` => `clamp(24px, 3.5vw, 36px)`
- ... 21 kayıt daha

### `.route-sub` / `font-size`
- `android_app/app/src/main/python/static/seats/seats.css` => `13px`
- `android_app/app/src/main/python/static/seats/seats.css` => `12px`
- `android_app/app/src/main/python/static/seats/seats.css` => `12px`
- `android_app/app/src/main/python/static/seats/seats.css` => `11px`
- `android_app/app/src/main/python/static/seats/seats-final.css` => `12.5px !important`
- `android_app/app/src/main/python/static/seats/seats-final.css` => `11.5px !important`
- `android_app/app/src/main/python/static/seats/seats-final.css` => `12px !important`
- `android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-final.css` => `14px !important`
- `android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-final.css` => `13px !important`
- `android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-final.css` => `12px !important`
- `apk_payload/static/seats/seats.css` => `13px`
- `apk_payload/static/seats/seats.css` => `12px`
- ... 18 kayıt daha

### `.voice-command-btn` / `border-radius`
- `_unused_review/static/seats/seats-redesign.css` => `17px !important`
- `_unused_review/static/seats/seats-redesign.css` => `18px !important`
- `android_app/app/src/main/python/static/seats/seats.css` => `15px`
- `android_app/app/src/main/python/static/seats/seats.css` => `13px`
- `android_app/app/src/main/python/static/seats/seats.css` => `22px !important`
- `android_app/app/src/main/python/static/seats/seats.css` => `21px !important`
- `android_app/app/src/main/python/static/seats/seats.css` => `21px !important`
- `android_app/app/src/main/python/static/seats/seats.css` => `26px !important`
- `android_app/app/src/main/python/static/seats/seats.css` => `24px !important`
- `android_app/app/src/main/python/static/seats/seats-final.css` => `17px !important`
- `android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-final.css` => `19px !important`
- `apk_payload/static/seats/seats.css` => `15px`
- ... 17 kayıt daha

### `.route-live-row` / `gap`
- `android_app/app/src/main/python/static/seats/seats.css` => `8px`
- `android_app/app/src/main/python/static/seats/seats.css` => `8px`
- `android_app/app/src/main/python/static/seats/seats.css` => `8px !important`
- `android_app/app/src/main/python/static/seats/seats.css` => `7px !important`
- `android_app/app/src/main/python/static/seats/seats.css` => `6px !important`
- `android_app/app/src/main/python/static/seats/seats-final.css` => `7px !important`
- `android_app/app/src/main/python/static/seats/seats-final.css` => `7px !important`
- `android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-final.css` => `10px !important`
- `android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-final.css` => `8px !important`
- `apk_payload/static/seats/seats.css` => `8px`
- `apk_payload/static/seats/seats.css` => `8px`
- `apk_payload/static/seats/seats.css` => `8px !important`
- ... 15 kayıt daha

### `.status-pill` / `min-height`
- `android_app/app/src/main/python/static/seats/seats.css` => `64px`
- `android_app/app/src/main/python/static/seats/seats.css` => `54px`
- `android_app/app/src/main/python/static/seats/seats.css` => `50px`
- `android_app/app/src/main/python/static/seats/seats-final.css` => `58px !important`
- `android_app/app/src/main/python/static/seats/seats-final.css` => `54px !important`
- `android_app/app/src/main/python/static/seats/seats-final.css` => `54px !important`
- `android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-final.css` => `96px !important`
- `android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-final.css` => `74px !important`
- `android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-final.css` => `68px !important`
- `apk_payload/static/seats/seats.css` => `64px`
- `apk_payload/static/seats/seats.css` => `54px`
- `apk_payload/static/seats/seats.css` => `50px`
- ... 15 kayıt daha

### `.status-pill .v` / `font-size`
- `android_app/app/src/main/python/static/seats/seats.css` => `24px`
- `android_app/app/src/main/python/static/seats/seats.css` => `25px`
- `android_app/app/src/main/python/static/seats/seats.css` => `23px`
- `android_app/app/src/main/python/static/seats/seats-final.css` => `26px !important`
- `android_app/app/src/main/python/static/seats/seats-final.css` => `24px !important`
- `android_app/app/src/main/python/static/seats/seats-final.css` => `25px !important`
- `android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-final.css` => `38px !important`
- `android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-final.css` => `31px !important`
- `android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-final.css` => `29px !important`
- `apk_payload/static/seats/seats.css` => `24px`
- `apk_payload/static/seats/seats.css` => `25px`
- `apk_payload/static/seats/seats.css` => `23px`
- ... 15 kayıt daha

### `.voice-command-btn` / `padding`
- `android_app/app/src/main/python/static/seats/seats.css` => `0 14px`
- `android_app/app/src/main/python/static/seats/seats.css` => `0 12px`
- `android_app/app/src/main/python/static/seats/seats.css` => `0 22px 0 16px !important`
- `android_app/app/src/main/python/static/seats/seats.css` => `0 18px 0 14px !important`
- `android_app/app/src/main/python/static/seats/seats.css` => `0 16px !important`
- `android_app/app/src/main/python/static/seats/seats.css` => `0 15px !important`
- `android_app/app/src/main/python/static/seats/seats.css` => `0 14px !important`
- `android_app/app/src/main/python/static/seats/seats.css` => `0 18px !important`
- `android_app/app/src/main/python/static/seats/seats-final.css` => `0 10px !important`
- `apk_payload/static/seats/seats.css` => `0 14px`
- `apk_payload/static/seats/seats.css` => `0 12px`
- `apk_payload/static/seats/seats.css` => `0 22px 0 16px !important`
- ... 15 kayıt daha

### `.night-voice-toggle` / `transform`
- `android_app/app/src/main/python/static/seats/seats.css` => `translateX(-10px) !important`
- `android_app/app/src/main/python/static/seats/seats.css` => `translateX(-14px) !important`
- `android_app/app/src/main/python/static/seats/seats.css` => `translateX(-18px) !important`
- `android_app/app/src/main/python/static/seats/seats.css` => `translateX(-6px) !important`
- `android_app/app/src/main/python/static/seats/seats.css` => `translateX(-8px) !important`
- `android_app/app/src/main/python/static/seats/seats.css` => `translateX(-10px) !important`
- `android_app/app/src/main/python/static/seats/seats.css` => `translateX(2px) !important`
- `android_app/app/src/main/python/static/seats/seats.css` => `translateX(0px) !important`
- `android_app/app/src/main/python/static/seats/seats.css` => `translateX(-2px) !important`
- `apk_payload/static/seats/seats.css` => `translateX(-10px) !important`
- `apk_payload/static/seats/seats.css` => `translateX(-14px) !important`
- `apk_payload/static/seats/seats.css` => `translateX(-18px) !important`
- ... 15 kayıt daha

### `.selected-stop-chip` / `font-size`
- `_unused_review/static/seats/seats-redesign.css` => `13px !important`
- `_unused_review/static/seats/seats-redesign.css` => `12px !important`
- `_unused_review/static/seats/seats-redesign.css` => `13px !important`
- `_unused_review/static/seats/seats-redesign.css` => `12.5px !important`
- `_unused_review/static/seats/seats-redesign.css` => `12px !important`
- `android_app/app/src/main/python/static/seats/seats.css` => `13px`
- `android_app/app/src/main/python/static/seats/seats.css` => `13px`
- `android_app/app/src/main/python/static/seats/seats.css` => `18px !important`
- `android_app/app/src/main/python/static/seats/seats.css` => `16px !important`
- `android_app/app/src/main/python/static/seats/seats-final.css` => `12.5px !important`
- `android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-final.css` => `14px !important`
- `android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-final.css` => `12.5px !important`
- ... 14 kayıt daha

### `#driveModeToggle` / `font-size`
- `_unused_review/static/seats/seats-redesign.css` => `14px !important`
- `android_app/app/src/main/python/static/seats/seats.css` => `13px`
- `android_app/app/src/main/python/static/seats/seats.css` => `12px`
- `android_app/app/src/main/python/static/seats/seats.css` => `17px !important`
- `android_app/app/src/main/python/static/seats/seats.css` => `15px !important`
- `android_app/app/src/main/python/static/seats/seats-final.css` => `12.5px !important`
- `android_app/app/src/main/python/static/seats/seats-final.css` => `12px !important`
- `android_app/app/src/main/python/static/seats/seats-final.css` => `14px !important`
- `android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-final.css` => `15px !important`
- `apk_payload/static/seats/seats.css` => `13px`
- `apk_payload/static/seats/seats.css` => `12px`
- `apk_payload/static/seats/seats.css` => `17px !important`
- ... 13 kayıt daha

### `.voice-row` / `grid-template-columns`
- `_unused_review/static/seats/seats-redesign.css` => `1fr 96px !important`
- `_unused_review/static/seats/seats-redesign.css` => `1fr 78px !important`
- `_unused_review/static/seats/seats-redesign.css` => `1fr 92px !important`
- `_unused_review/static/seats/seats-redesign.css` => `1fr 78px !important`
- `android_app/app/src/main/python/static/seats/seats.css` => `minmax(0, 1fr) 128px !important`
- `android_app/app/src/main/python/static/seats/seats.css` => `minmax(0, 1fr) 104px !important`
- `android_app/app/src/main/python/static/seats/seats.css` => `1fr !important`
- `android_app/app/src/main/python/static/seats/seats-final.css` => `minmax(0,1fr) 84px !important`
- `android_app/app/src/main/python/static/seats/seats-final.css` => `minmax(0,1fr) 74px !important`
- `android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-final.css` => `1fr 110px !important`
- `android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-final.css` => `1fr 84px !important`
- `apk_payload/static/seats/seats.css` => `minmax(0, 1fr) 128px !important`
- ... 13 kayıt daha

### `.voice-command-btn` / `font-size`
- `_unused_review/static/seats/seats-redesign.css` => `14px !important`
- `android_app/app/src/main/python/static/seats/seats.css` => `13px`
- `android_app/app/src/main/python/static/seats/seats.css` => `12px`
- `android_app/app/src/main/python/static/seats/seats.css` => `11px`
- `android_app/app/src/main/python/static/seats/seats.css` => `0 !important`
- `android_app/app/src/main/python/static/seats/seats.css` => `22px !important`
- `android_app/app/src/main/python/static/seats/seats.css` => `18px !important`
- `android_app/app/src/main/python/static/seats/seats-final.css` => `13px !important`
- `android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-final.css` => `15px !important`
- `apk_payload/static/seats/seats.css` => `13px`
- `apk_payload/static/seats/seats.css` => `12px`
- `apk_payload/static/seats/seats.css` => `11px`
- ... 13 kayıt daha

### `.voice-state` / `font-size`
- `_unused_review/static/seats/seats-redesign.css` => `13px !important`
- `android_app/app/src/main/python/static/seats/seats.css` => `12px`
- `android_app/app/src/main/python/static/seats/seats.css` => `11px`
- `android_app/app/src/main/python/static/seats/seats.css` => `10px`
- `android_app/app/src/main/python/static/seats/seats.css` => `14px !important`
- `android_app/app/src/main/python/static/seats/seats.css` => `19px !important`
- `android_app/app/src/main/python/static/seats/seats.css` => `17px !important`
- `android_app/app/src/main/python/static/seats/seats-final.css` => `12px !important`
- `android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-final.css` => `14px !important`
- `apk_payload/static/seats/seats.css` => `12px`
- `apk_payload/static/seats/seats.css` => `11px`
- `apk_payload/static/seats/seats.css` => `10px`
- ... 13 kayıt daha

### `.legend` / `grid-template-columns`
- `_unused_review/static/seats/seats-redesign.css` => `repeat(3, minmax(0, 1fr)) !important`
- `_unused_review/static/seats/seats-redesign.css` => `repeat(3, minmax(0, 1fr)) !important`
- `_unused_review/static/seats/seats-redesign.css` => `repeat(3, minmax(0,1fr)) !important`
- `_unused_review/static/seats/seats-redesign.css` => `repeat(3, minmax(0,1fr)) !important`
- `android_app/app/src/main/python/static/seats/seats.css` => `repeat(3, minmax(0, 1fr)) !important`
- `android_app/app/src/main/python/static/seats/seats.css` => `repeat(3, minmax(0, 1fr)) !important`
- `android_app/app/src/main/python/static/seats/seats.css` => `repeat(2, minmax(0, 1fr)) !important`
- `android_app/app/src/main/python/static/seats/seats-final.css` => `repeat(3,minmax(0,1fr)) !important`
- `android_app/app/src/main/python/static/seats/seats-final.css` => `repeat(3,minmax(0,1fr)) !important`
- `android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-final.css` => `repeat(6,minmax(0,1fr)) !important`
- `android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-final.css` => `repeat(3,minmax(0,1fr)) !important`
- `apk_payload/static/seats/seats.css` => `repeat(3, minmax(0, 1fr)) !important`
- ... 13 kayıt daha

### `.route-live-row` / `grid-template-columns`
- `android_app/app/src/main/python/static/seats/seats.css` => `1fr 1fr`
- `android_app/app/src/main/python/static/seats/seats.css` => `minmax(96px, .85fr) minmax(0, 1.45fr) auto !important`
- `android_app/app/src/main/python/static/seats/seats.css` => `minmax(92px, .75fr) minmax(0, 1.35fr) auto !important`
- `android_app/app/src/main/python/static/seats/seats.css` => `minmax(84px, .7fr) minmax(0, 1.25fr) auto !important`
- `android_app/app/src/main/python/static/seats/seats-final.css` => `repeat(4,minmax(0,1fr)) !important`
- `android_app/app/src/main/python/static/seats/seats-final.css` => `1fr 1fr !important`
- `android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-final.css` => `repeat(4,minmax(0,1fr)) !important`
- `android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-final.css` => `repeat(2,minmax(0,1fr)) !important`
- `apk_payload/static/seats/seats.css` => `1fr 1fr`
- `apk_payload/static/seats/seats.css` => `minmax(96px, .85fr) minmax(0, 1.45fr) auto !important`
- `apk_payload/static/seats/seats.css` => `minmax(92px, .75fr) minmax(0, 1.35fr) auto !important`
- `apk_payload/static/seats/seats.css` => `minmax(84px, .7fr) minmax(0, 1.25fr) auto !important`
- ... 12 kayıt daha

### `.fab-column.fab-left-gap-moved .fab` / `width`
- `android_app/app/src/main/python/static/seats/patches/seat-layout-fab-pack.css` => `46px !important`
- `android_app/app/src/main/python/static/seats/patches/seat-layout-fab-pack.css` => `44px !important`
- `android_app/app/src/main/python/static/seats/patches/seat-layout-fab-pack.css` => `48px !important`
- `android_app/app/src/main/python/static/seats/patches/seat-layout-fab-pack.css` => `46px !important`
- `android_app/app/src/main/python/static/seats/patches/seat-layout-fab-pack.css` => `41px !important`
- `android_app/app/src/main/python/static/seats/patches/seat-layout-fab-pack.css` => `39px !important`
- `android_app/app/src/main/python/static/seats/patches/seat-layout-fab-pack.css` => `41px !important`
- `android_app/app/src/main/python/static/seats/patches/seat-layout-fab-pack.css` => `39px !important`
- `apk_payload/static/seats/patches/seat-layout-fab-pack.css` => `46px !important`
- `apk_payload/static/seats/patches/seat-layout-fab-pack.css` => `44px !important`
- `apk_payload/static/seats/patches/seat-layout-fab-pack.css` => `48px !important`
- `apk_payload/static/seats/patches/seat-layout-fab-pack.css` => `46px !important`
- ... 12 kayıt daha

### `.fab-column.fab-left-gap-moved .fab` / `height`
- `android_app/app/src/main/python/static/seats/patches/seat-layout-fab-pack.css` => `46px !important`
- `android_app/app/src/main/python/static/seats/patches/seat-layout-fab-pack.css` => `44px !important`
- `android_app/app/src/main/python/static/seats/patches/seat-layout-fab-pack.css` => `48px !important`
- `android_app/app/src/main/python/static/seats/patches/seat-layout-fab-pack.css` => `46px !important`
- `android_app/app/src/main/python/static/seats/patches/seat-layout-fab-pack.css` => `41px !important`
- `android_app/app/src/main/python/static/seats/patches/seat-layout-fab-pack.css` => `39px !important`
- `android_app/app/src/main/python/static/seats/patches/seat-layout-fab-pack.css` => `41px !important`
- `android_app/app/src/main/python/static/seats/patches/seat-layout-fab-pack.css` => `39px !important`
- `apk_payload/static/seats/patches/seat-layout-fab-pack.css` => `46px !important`
- `apk_payload/static/seats/patches/seat-layout-fab-pack.css` => `44px !important`
- `apk_payload/static/seats/patches/seat-layout-fab-pack.css` => `48px !important`
- `apk_payload/static/seats/patches/seat-layout-fab-pack.css` => `46px !important`
- ... 12 kayıt daha

### `.fab-column.fab-left-gap-moved .fab` / `border-radius`
- `android_app/app/src/main/python/static/seats/patches/seat-layout-fab-pack.css` => `16px !important`
- `android_app/app/src/main/python/static/seats/patches/seat-layout-fab-pack.css` => `15px !important`
- `android_app/app/src/main/python/static/seats/patches/seat-layout-fab-pack.css` => `18px !important`
- `android_app/app/src/main/python/static/seats/patches/seat-layout-fab-pack.css` => `17px !important`
- `android_app/app/src/main/python/static/seats/patches/seat-layout-fab-pack.css` => `15px !important`
- `android_app/app/src/main/python/static/seats/patches/seat-layout-fab-pack.css` => `14px !important`
- `android_app/app/src/main/python/static/seats/patches/seat-layout-fab-pack.css` => `15px !important`
- `android_app/app/src/main/python/static/seats/patches/seat-layout-fab-pack.css` => `14px !important`
- `apk_payload/static/seats/patches/seat-layout-fab-pack.css` => `16px !important`
- `apk_payload/static/seats/patches/seat-layout-fab-pack.css` => `15px !important`
- `apk_payload/static/seats/patches/seat-layout-fab-pack.css` => `18px !important`
- `apk_payload/static/seats/patches/seat-layout-fab-pack.css` => `17px !important`
- ... 12 kayıt daha

### `.voice-row` / `gap`
- `_unused_review/static/seats/seats-redesign.css` => `8px !important`
- `_unused_review/static/seats/seats-redesign.css` => `8px !important`
- `android_app/app/src/main/python/static/seats/seats.css` => `10px`
- `android_app/app/src/main/python/static/seats/seats.css` => `8px`
- `android_app/app/src/main/python/static/seats/seats.css` => `12px !important`
- `android_app/app/src/main/python/static/seats/seats.css` => `12px !important`
- `android_app/app/src/main/python/static/seats/seats.css` => `10px !important`
- `android_app/app/src/main/python/static/seats/seats-final.css` => `8px !important`
- `android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-final.css` => `10px !important`
- `apk_payload/static/seats/seats.css` => `10px`
- `apk_payload/static/seats/seats.css` => `8px`
- `apk_payload/static/seats/seats.css` => `12px !important`
- ... 11 kayıt daha

### `.voice-state` / `min-height`
- `_unused_review/static/seats/seats-redesign.css` => `44px !important`
- `_unused_review/static/seats/seats-redesign.css` => `46px !important`
- `android_app/app/src/main/python/static/seats/seats.css` => `40px`
- `android_app/app/src/main/python/static/seats/seats.css` => `36px`
- `android_app/app/src/main/python/static/seats/seats.css` => `42px`
- `android_app/app/src/main/python/static/seats/seats.css` => `48px !important`
- `android_app/app/src/main/python/static/seats/seats.css` => `48px !important`
- `android_app/app/src/main/python/static/seats/seats-final.css` => `44px !important`
- `android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-final.css` => `48px !important`
- `apk_payload/static/seats/seats.css` => `40px`
- `apk_payload/static/seats/seats.css` => `36px`
- `apk_payload/static/seats/seats.css` => `42px`
- ... 11 kayıt daha

### `.mini-chip` / `font-size`
- `_unused_review/static/seats/seats-redesign.css` => `13px !important`
- `_unused_review/static/seats/seats-redesign.css` => `12px !important`
- `_unused_review/static/seats/seats-redesign.css` => `11.5px !important`
- `_unused_review/static/seats/seats-redesign.css` => `12px !important`
- `_unused_review/static/seats/seats-redesign.css` => `11.5px !important`
- `android_app/app/src/main/python/static/seats/seats.css` => `13px`
- `android_app/app/src/main/python/static/seats/seats.css` => `12px`
- `android_app/app/src/main/python/static/seats/seats.css` => `16px !important`
- `android_app/app/src/main/python/static/seats/seats.css` => `14px !important`
- `android_app/app/src/main/python/static/seats/seats-final.css` => `11.5px !important`
- `android_app/app/src/main/python/static/seats/seats-final.css` => `11px !important`
- `apk_payload/static/seats/seats.css` => `13px`
- ... 11 kayıt daha

### `.selected-stop-chip` / `min-height`
- `_unused_review/static/seats/seats-redesign.css` => `42px !important`
- `_unused_review/static/seats/seats-redesign.css` => `40px !important`
- `android_app/app/src/main/python/static/seats/seats.css` => `40px`
- `android_app/app/src/main/python/static/seats/seats.css` => `36px`
- `android_app/app/src/main/python/static/seats/seats.css` => `58px !important`
- `android_app/app/src/main/python/static/seats/seats.css` => `54px !important`
- `android_app/app/src/main/python/static/seats/seats-final.css` => `40px !important`
- `android_app/app/src/main/python/static/seats/seats-final.css` => `38px !important`
- `android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-final.css` => `44px !important`
- `apk_payload/static/seats/seats.css` => `40px`
- `apk_payload/static/seats/seats.css` => `36px`
- `apk_payload/static/seats/seats.css` => `58px !important`
- ... 11 kayıt daha

### `#driveModeToggle` / `background`
- `_unused_review/static/seats/seats-redesign.css` => `rgba(255,255,255,.07) !important`
- `android_app/app/src/main/python/static/seats/seats.css` => `linear-gradient(180deg, rgba(37,99,235,.96), rgba(29,78,216,.96))`
- `android_app/app/src/main/python/static/seats/seats-final.css` => `rgba(255,255,255,.065) !important`
- `android_app/app/src/main/python/static/seats/seats-final.css` => `linear-gradient(135deg,#2563eb,#1d4ed8) !important`
- `android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-final.css` => `linear-gradient(180deg,#fff,#f8fbff) !important`
- `android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-final.css` => `linear-gradient(135deg,#2563eb,#0ea5e9) !important`
- `android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-tone.css` => `rgba(255,255,255,.08) !important`
- `android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-tone.css` => `linear-gradient(135deg,#2563eb,#1d4ed8) !important`
- `apk_payload/static/seats/seats.css` => `linear-gradient(180deg, rgba(37,99,235,.96), rgba(29,78,216,.96))`
- `apk_payload/static/seats/seats-final.css` => `rgba(255,255,255,.065) !important`
- `apk_payload/static/seats/seats-final.css` => `linear-gradient(135deg,#2563eb,#1d4ed8) !important`
- `apk_payload/static/seats/_archive_theme_trials/seats-dashboard-final.css` => `linear-gradient(180deg,#fff,#f8fbff) !important`
- ... 10 kayıt daha

### `.board-head` / `gap`
- `_unused_review/static/seats/seats-redesign.css` => `9px !important`
- `_unused_review/static/seats/seats-redesign.css` => `12px !important`
- `_unused_review/static/seats/seats-redesign.css` => `10px !important`
- `android_app/app/src/main/python/static/seats/seats.css` => `14px`
- `android_app/app/src/main/python/static/seats/seats.css` => `10px`
- `android_app/app/src/main/python/static/seats/seats.css` => `8px`
- `android_app/app/src/main/python/static/seats/seats.css` => `16px !important`
- `android_app/app/src/main/python/static/seats/seats-final.css` => `10px !important`
- `android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-final.css` => `13px !important`
- `apk_payload/static/seats/seats.css` => `14px`
- `apk_payload/static/seats/seats.css` => `10px`
- `apk_payload/static/seats/seats.css` => `8px`
- ... 9 kayıt daha

### `.route-badge` / `width`
- `android_app/app/src/main/python/static/seats/seats.css` => `52px`
- `android_app/app/src/main/python/static/seats/seats.css` => `46px`
- `android_app/app/src/main/python/static/seats/seats.css` => `42px`
- `android_app/app/src/main/python/static/seats/seats-final.css` => `52px !important`
- `android_app/app/src/main/python/static/seats/seats-final.css` => `46px !important`
- `android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-final.css` => `74px !important`
- `android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-final.css` => `58px !important`
- `apk_payload/static/seats/seats.css` => `52px`
- `apk_payload/static/seats/seats.css` => `46px`
- `apk_payload/static/seats/seats.css` => `42px`
- `apk_payload/static/seats/seats-final.css` => `52px !important`
- `apk_payload/static/seats/seats-final.css` => `46px !important`
- ... 9 kayıt daha

### `.route-badge` / `height`
- `android_app/app/src/main/python/static/seats/seats.css` => `52px`
- `android_app/app/src/main/python/static/seats/seats.css` => `46px`
- `android_app/app/src/main/python/static/seats/seats.css` => `42px`
- `android_app/app/src/main/python/static/seats/seats-final.css` => `52px !important`
- `android_app/app/src/main/python/static/seats/seats-final.css` => `46px !important`
- `android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-final.css` => `74px !important`
- `android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-final.css` => `58px !important`
- `apk_payload/static/seats/seats.css` => `52px`
- `apk_payload/static/seats/seats.css` => `46px`
- `apk_payload/static/seats/seats.css` => `42px`
- `apk_payload/static/seats/seats-final.css` => `52px !important`
- `apk_payload/static/seats/seats-final.css` => `46px !important`
- ... 9 kayıt daha

### `.route-badge` / `border-radius`
- `android_app/app/src/main/python/static/seats/seats.css` => `18px`
- `android_app/app/src/main/python/static/seats/seats.css` => `16px`
- `android_app/app/src/main/python/static/seats/seats.css` => `15px`
- `android_app/app/src/main/python/static/seats/seats-final.css` => `18px !important`
- `android_app/app/src/main/python/static/seats/seats-final.css` => `16px !important`
- `android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-final.css` => `24px !important`
- `android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-final.css` => `20px !important`
- `apk_payload/static/seats/seats.css` => `18px`
- `apk_payload/static/seats/seats.css` => `16px`
- `apk_payload/static/seats/seats.css` => `15px`
- `apk_payload/static/seats/seats-final.css` => `18px !important`
- `apk_payload/static/seats/seats-final.css` => `16px !important`
- ... 9 kayıt daha

### `.route-badge` / `font-size`
- `android_app/app/src/main/python/static/seats/seats.css` => `24px`
- `android_app/app/src/main/python/static/seats/seats.css` => `21px`
- `android_app/app/src/main/python/static/seats/seats.css` => `21px`
- `android_app/app/src/main/python/static/seats/seats-final.css` => `24px !important`
- `android_app/app/src/main/python/static/seats/seats-final.css` => `22px !important`
- `android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-final.css` => `34px !important`
- `android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-final.css` => `28px !important`
- `apk_payload/static/seats/seats.css` => `24px`
- `apk_payload/static/seats/seats.css` => `21px`
- `apk_payload/static/seats/seats.css` => `21px`
- `apk_payload/static/seats/seats-final.css` => `24px !important`
- `apk_payload/static/seats/seats-final.css` => `22px !important`
- ... 9 kayıt daha

### `.status-row` / `grid-template-columns`
- `android_app/app/src/main/python/static/seats/seats.css` => `repeat(6, minmax(0,1fr))`
- `android_app/app/src/main/python/static/seats/seats.css` => `repeat(3, minmax(0,1fr))`
- `android_app/app/src/main/python/static/seats/seats.css` => `unset`
- `android_app/app/src/main/python/static/seats/seats.css` => `1fr 1fr`
- `android_app/app/src/main/python/static/seats/seats-final.css` => `repeat(2,minmax(0,1fr)) !important`
- `android_app/app/src/main/python/static/seats/seats-final.css` => `1fr 1fr !important`
- `android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-final.css` => `repeat(2,minmax(0,1fr)) !important`
- `apk_payload/static/seats/seats.css` => `repeat(6, minmax(0,1fr))`
- `apk_payload/static/seats/seats.css` => `repeat(3, minmax(0,1fr))`
- `apk_payload/static/seats/seats.css` => `unset`
- `apk_payload/static/seats/seats.css` => `1fr 1fr`
- `apk_payload/static/seats/seats-final.css` => `repeat(2,minmax(0,1fr)) !important`
- ... 9 kayıt daha

### `.route-strip-meta` / `gap`
- `android_app/app/src/main/python/static/seats/seats.css` => `8px`
- `android_app/app/src/main/python/static/seats/seats.css` => `8px`
- `android_app/app/src/main/python/static/seats/seats.css` => `7px !important`
- `android_app/app/src/main/python/static/seats/seats.css` => `10px !important`
- `android_app/app/src/main/python/static/seats/seats.css` => `8px !important`
- `android_app/app/src/main/python/static/seats/seats-final.css` => `7px !important`
- `android_app/app/src/main/python/static/seats/seats-final.css` => `8px !important`
- `apk_payload/static/seats/seats.css` => `8px`
- `apk_payload/static/seats/seats.css` => `8px`
- `apk_payload/static/seats/seats.css` => `7px !important`
- `apk_payload/static/seats/seats.css` => `10px !important`
- `apk_payload/static/seats/seats.css` => `8px !important`
- ... 9 kayıt daha

### `.voice-command-btn span` / `font-size`
- `android_app/app/src/main/python/static/seats/seats.css` => `18px !important`
- `android_app/app/src/main/python/static/seats/seats.css` => `17px !important`
- `android_app/app/src/main/python/static/seats/seats.css` => `16px !important`
- `android_app/app/src/main/python/static/seats/seats.css` => `17px !important`
- `android_app/app/src/main/python/static/seats/seats.css` => `16px !important`
- `android_app/app/src/main/python/static/seats/seats.css` => `15.5px !important`
- `android_app/app/src/main/python/static/seats/seats-final.css` => `13px !important`
- `apk_payload/static/seats/seats.css` => `18px !important`
- `apk_payload/static/seats/seats.css` => `17px !important`
- `apk_payload/static/seats/seats.css` => `16px !important`
- `apk_payload/static/seats/seats.css` => `17px !important`
- `apk_payload/static/seats/seats.css` => `16px !important`
- ... 9 kayıt daha

### `#nightVoiceToggle` / `min-width`
- `android_app/app/src/main/python/static/seats/seats.css` => `100px !important`
- `android_app/app/src/main/python/static/seats/seats.css` => `92px !important`
- `android_app/app/src/main/python/static/seats/seats.css` => `86px !important`
- `android_app/app/src/main/python/static/seats/seats.css` => `96px !important`
- `android_app/app/src/main/python/static/seats/seats.css` => `50px !important`
- `android_app/app/src/main/python/static/seats/seats-final.css` => `46px !important`
- `android_app/app/src/main/python/static/seats/seats-final.css` => `42px !important`
- `apk_payload/static/seats/seats.css` => `100px !important`
- `apk_payload/static/seats/seats.css` => `92px !important`
- `apk_payload/static/seats/seats.css` => `86px !important`
- `apk_payload/static/seats/seats.css` => `96px !important`
- `apk_payload/static/seats/seats.css` => `50px !important`
- ... 9 kayıt daha

### `body.drive-mode .board-head-right .voice-row` / `gap`
- `android_app/app/src/main/python/static/seats/seats-final.css` => `14px !important`
- `android_app/app/src/main/python/static/seats/seats-final.css` => `12px !important`
- `android_app/app/src/main/python/static/seats/seats-final.css` => `14px !important`
- `android_app/app/src/main/python/static/seats/seats-final.css` => `12px !important`
- `android_app/app/src/main/python/static/seats/seats-final.css` => `10px !important`
- `android_app/app/src/main/python/static/seats/seats-final.css` => `12px !important`
- `android_app/app/src/main/python/static/seats/seats-final.css` => `10px !important`
- `apk_payload/static/seats/seats-final.css` => `14px !important`
- `apk_payload/static/seats/seats-final.css` => `12px !important`
- `apk_payload/static/seats/seats-final.css` => `14px !important`
- `apk_payload/static/seats/seats-final.css` => `12px !important`
- `apk_payload/static/seats/seats-final.css` => `10px !important`
- ... 9 kayıt daha

### `.muavin-locate-control` / `bottom`
- `android_app/app/src/main/python/static/live_map/muavin_live_map_extra.css` => `calc(env(safe-area-inset-bottom, 0px) + 132px)`
- `android_app/app/src/main/python/static/live_map/muavin_live_map_extra.css` => `calc(env(safe-area-inset-bottom, 0px) + 245px) !important`
- `android_app/app/src/main/python/static/live_map/muavin_live_map_extra.css` => `calc(env(safe-area-inset-bottom, 0px) + 218px) !important`
- `android_app/app/src/main/python/static/live_map/muavin_live_map_extra.css` => `calc(env(safe-area-inset-bottom, 0px) + 250px) !important`
- `android_app/app/src/main/python/static/live_map/muavin_live_map_extra.css` => `calc(env(safe-area-inset-bottom, 0px) + 242px) !important`
- `android_app/app/src/main/python/static/live_map/muavin_live_map_extra.css` => `calc(env(safe-area-inset-bottom, 0px) + 220px) !important`
- `android_app/app/src/main/python/static/live_map/muavin_live_map_extra.css` => `calc(env(safe-area-inset-bottom, 0px) + 218px) !important`
- `apk_payload/static/live_map/muavin_live_map_extra.css` => `calc(env(safe-area-inset-bottom, 0px) + 132px)`
- `apk_payload/static/live_map/muavin_live_map_extra.css` => `calc(env(safe-area-inset-bottom, 0px) + 245px) !important`
- `apk_payload/static/live_map/muavin_live_map_extra.css` => `calc(env(safe-area-inset-bottom, 0px) + 218px) !important`
- `apk_payload/static/live_map/muavin_live_map_extra.css` => `calc(env(safe-area-inset-bottom, 0px) + 250px) !important`
- `apk_payload/static/live_map/muavin_live_map_extra.css` => `calc(env(safe-area-inset-bottom, 0px) + 242px) !important`
- ... 9 kayıt daha

### `.seats-shell` / `padding`
- `_unused_review/static/seats/seats-redesign.css` => `8px 6px 16px !important`
- `_unused_review/static/seats/seats-redesign.css` => `6px 4px 12px !important`
- `android_app/app/src/main/python/static/seats/seats.css` => `12px 12px 18px`
- `android_app/app/src/main/python/static/seats/seats.css` => `8px 8px 16px`
- `android_app/app/src/main/python/static/seats/seats.css` => `8px 8px 14px`
- `android_app/app/src/main/python/static/seats/seats-final.css` => `8px 6px 16px !important`
- `android_app/app/src/main/python/static/seats/seats-final.css` => `6px 4px 12px !important`
- `android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-final.css` => `0 !important`
- `apk_payload/static/seats/seats.css` => `12px 12px 18px`
- `apk_payload/static/seats/seats.css` => `8px 8px 16px`
- `apk_payload/static/seats/seats.css` => `8px 8px 14px`
- `apk_payload/static/seats/seats-final.css` => `8px 6px 16px !important`
- ... 8 kayıt daha

### `#driveInlineDock` / `gap`
- `_unused_review/static/seats/seats-redesign.css` => `8px !important`
- `_unused_review/static/seats/seats-redesign.css` => `8px !important`
- `android_app/app/src/main/python/static/seats/seats.css` => `10px !important`
- `android_app/app/src/main/python/static/seats/seats.css` => `10px`
- `android_app/app/src/main/python/static/seats/seats-final.css` => `7px !important`
- `android_app/app/src/main/python/static/seats/seats-final.css` => `6px !important`
- `android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-final.css` => `10px !important`
- `android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-final.css` => `7px !important`
- `apk_payload/static/seats/seats.css` => `10px !important`
- `apk_payload/static/seats/seats.css` => `10px`
- `apk_payload/static/seats/seats-final.css` => `7px !important`
- `apk_payload/static/seats/seats-final.css` => `6px !important`
- ... 8 kayıt daha

### `.selected-stop-chip` / `padding`
- `_unused_review/static/seats/seats-redesign.css` => `9px 11px !important`
- `_unused_review/static/seats/seats-redesign.css` => `9px 12px !important`
- `android_app/app/src/main/python/static/seats/seats.css` => `9px 13px`
- `android_app/app/src/main/python/static/seats/seats.css` => `8px 12px`
- `android_app/app/src/main/python/static/seats/seats.css` => `12px 18px !important`
- `android_app/app/src/main/python/static/seats/seats.css` => `11px 14px !important`
- `android_app/app/src/main/python/static/seats/seats-final.css` => `9px 11px !important`
- `android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-final.css` => `10px 13px !important`
- `apk_payload/static/seats/seats.css` => `9px 13px`
- `apk_payload/static/seats/seats.css` => `8px 12px`
- `apk_payload/static/seats/seats.css` => `12px 18px !important`
- `apk_payload/static/seats/seats.css` => `11px 14px !important`
- ... 8 kayıt daha

### `.voice-state` / `border-radius`
- `_unused_review/static/seats/seats-redesign.css` => `17px !important`
- `_unused_review/static/seats/seats-redesign.css` => `18px !important`
- `android_app/app/src/main/python/static/seats/seats.css` => `999px`
- `android_app/app/src/main/python/static/seats/seats.css` => `999px !important`
- `android_app/app/src/main/python/static/seats/seats.css` => `26px !important`
- `android_app/app/src/main/python/static/seats/seats.css` => `24px !important`
- `android_app/app/src/main/python/static/seats/seats-final.css` => `17px !important`
- `android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-final.css` => `19px !important`
- `apk_payload/static/seats/seats.css` => `999px`
- `apk_payload/static/seats/seats.css` => `999px !important`
- `apk_payload/static/seats/seats.css` => `26px !important`
- `apk_payload/static/seats/seats.css` => `24px !important`
- ... 8 kayıt daha

### `.legend` / `gap`
- `_unused_review/static/seats/seats-redesign.css` => `7px !important`
- `_unused_review/static/seats/seats-redesign.css` => `7px !important`
- `android_app/app/src/main/python/static/seats/seats.css` => `8px`
- `android_app/app/src/main/python/static/seats/seats.css` => `7px`
- `android_app/app/src/main/python/static/seats/seats.css` => `10px !important`
- `android_app/app/src/main/python/static/seats/seats.css` => `9px !important`
- `android_app/app/src/main/python/static/seats/seats-final.css` => `7px !important`
- `android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-final.css` => `8px !important`
- `apk_payload/static/seats/seats.css` => `8px`
- `apk_payload/static/seats/seats.css` => `7px`
- `apk_payload/static/seats/seats.css` => `10px !important`
- `apk_payload/static/seats/seats.css` => `9px !important`
- ... 8 kayıt daha

### `.seat` / `box-shadow`
- `_unused_review/static/seats/seats-redesign.css` => `0 8px 20px rgba(0,0,0,.20), inset 0 1px 0 rgba(255,255,255,.10) !important`
- `android_app/app/src/main/python/static/seats/seats.css` => `inset 0 -10px 18px rgba(0,0,0,.14), 0 14px 28px rgba(0,0,0,.34)`
- `android_app/app/src/main/python/static/seats/seats.css` => `inset 0 -10px 18px rgba(0,0,0,.14), 0 14px 28px rgba(0,0,0,.34) !important`
- `android_app/app/src/main/python/static/seats/seats.css` => `inset 0 1px 0 rgba(255,255,255,.22), inset 0 -10px 18px rgba(0,0,0,.18), 0 14px 28px rgba(0,0,0,.38) !important`
- `android_app/app/src/main/python/static/seats/seats-final.css` => `inset 0 -10px 18px rgba(0,0,0,.16), 0 13px 24px rgba(0,0,0,.30) !important`
- `android_app/app/src/main/python/static/seats/patches/mobile-performance-fix.css` => `0 4px 10px rgba(0,0,0,.18) !important`
- `android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-final.css` => `0 8px 18px rgba(0,0,0,.22), inset 0 1px 0 rgba(255,255,255,.15) !important`
- `apk_payload/static/seats/seats.css` => `inset 0 -10px 18px rgba(0,0,0,.14), 0 14px 28px rgba(0,0,0,.34)`
- `apk_payload/static/seats/seats.css` => `inset 0 -10px 18px rgba(0,0,0,.14), 0 14px 28px rgba(0,0,0,.34) !important`
- `apk_payload/static/seats/seats.css` => `inset 0 1px 0 rgba(255,255,255,.22), inset 0 -10px 18px rgba(0,0,0,.18), 0 14px 28px rgba(0,0,0,.38) !important`
- `apk_payload/static/seats/seats-final.css` => `inset 0 -10px 18px rgba(0,0,0,.16), 0 13px 24px rgba(0,0,0,.30) !important`
- `apk_payload/static/seats/patches/mobile-performance-fix.css` => `0 4px 10px rgba(0,0,0,.18) !important`
- ... 8 kayıt daha

### `.top-actions` / `gap`
- `_unused_review/static/seats/seats-redesign.css` => `8px !important`
- `android_app/app/src/main/python/static/seats/seats.css` => `10px`
- `android_app/app/src/main/python/static/seats/seats.css` => `8px`
- `android_app/app/src/main/python/static/seats/seats.css` => `6px`
- `android_app/app/src/main/python/static/seats/seats.css` => `7px`
- `android_app/app/src/main/python/static/seats/seats-final.css` => `7px !important`
- `android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-final.css` => `9px !important`
- `apk_payload/static/seats/seats.css` => `10px`
- `apk_payload/static/seats/seats.css` => `8px`
- `apk_payload/static/seats/seats.css` => `6px`
- `apk_payload/static/seats/seats.css` => `7px`
- `apk_payload/static/seats/seats-final.css` => `7px !important`
- ... 7 kayıt daha

### `#driveModeToggle` / `min-height`
- `_unused_review/static/seats/seats-redesign.css` => `44px !important`
- `android_app/app/src/main/python/static/seats/seats.css` => `42px`
- `android_app/app/src/main/python/static/seats/seats.css` => `40px`
- `android_app/app/src/main/python/static/seats/seats-final.css` => `42px !important`
- `android_app/app/src/main/python/static/seats/seats-final.css` => `44px !important`
- `android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-final.css` => `52px !important`
- `android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-final.css` => `44px !important`
- `apk_payload/static/seats/seats.css` => `42px`
- `apk_payload/static/seats/seats.css` => `40px`
- `apk_payload/static/seats/seats-final.css` => `42px !important`
- `apk_payload/static/seats/seats-final.css` => `44px !important`
- `apk_payload/static/seats/_archive_theme_trials/seats-dashboard-final.css` => `52px !important`
- ... 7 kayıt daha

### `#driveModeToggle` / `border-radius`
- `_unused_review/static/seats/seats-redesign.css` => `17px !important`
- `android_app/app/src/main/python/static/seats/seats.css` => `999px`
- `android_app/app/src/main/python/static/seats/seats.css` => `999px !important`
- `android_app/app/src/main/python/static/seats/seats-final.css` => `16px !important`
- `android_app/app/src/main/python/static/seats/seats-final.css` => `18px !important`
- `android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-final.css` => `19px !important`
- `android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-final.css` => `16px !important`
- `apk_payload/static/seats/seats.css` => `999px`
- `apk_payload/static/seats/seats.css` => `999px !important`
- `apk_payload/static/seats/seats-final.css` => `16px !important`
- `apk_payload/static/seats/seats-final.css` => `18px !important`
- `apk_payload/static/seats/_archive_theme_trials/seats-dashboard-final.css` => `19px !important`
- ... 7 kayıt daha

### `.drive-eta-chip` / `border-radius`
- `_unused_review/static/seats/seats-redesign.css` => `17px !important`
- `android_app/app/src/main/python/static/seats/seats.css` => `22px`
- `android_app/app/src/main/python/static/seats/seats.css` => `18px`
- `android_app/app/src/main/python/static/seats/seats-final.css` => `16px !important`
- `android_app/app/src/main/python/static/seats/seats-final.css` => `18px !important`
- `android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-final.css` => `19px !important`
- `android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-final.css` => `16px !important`
- `apk_payload/static/seats/seats.css` => `22px`
- `apk_payload/static/seats/seats.css` => `18px`
- `apk_payload/static/seats/seats-final.css` => `16px !important`
- `apk_payload/static/seats/seats-final.css` => `18px !important`
- `apk_payload/static/seats/_archive_theme_trials/seats-dashboard-final.css` => `19px !important`
- ... 7 kayıt daha

### `.mini-chip` / `min-height`
- `_unused_review/static/seats/seats-redesign.css` => `38px !important`
- `_unused_review/static/seats/seats-redesign.css` => `35px !important`
- `_unused_review/static/seats/seats-redesign.css` => `36px !important`
- `android_app/app/src/main/python/static/seats/seats.css` => `38px`
- `android_app/app/src/main/python/static/seats/seats.css` => `34px`
- `android_app/app/src/main/python/static/seats/seats.css` => `50px !important`
- `android_app/app/src/main/python/static/seats/seats.css` => `46px !important`
- `android_app/app/src/main/python/static/seats/seats-final.css` => `34px !important`
- `apk_payload/static/seats/seats.css` => `38px`
- `apk_payload/static/seats/seats.css` => `34px`
- `apk_payload/static/seats/seats.css` => `50px !important`
- `apk_payload/static/seats/seats.css` => `46px !important`
- ... 6 kayıt daha

### `.mini-chip` / `padding`
- `_unused_review/static/seats/seats-redesign.css` => `6px 8px !important`
- `_unused_review/static/seats/seats-redesign.css` => `5px 6px !important`
- `_unused_review/static/seats/seats-redesign.css` => `6px 6px !important`
- `android_app/app/src/main/python/static/seats/seats.css` => `8px 12px`
- `android_app/app/src/main/python/static/seats/seats.css` => `7px 10px`
- `android_app/app/src/main/python/static/seats/seats.css` => `0 10px !important`
- `android_app/app/src/main/python/static/seats/seats.css` => `0 7px !important`
- `android_app/app/src/main/python/static/seats/seats-final.css` => `6px 7px !important`
- `apk_payload/static/seats/seats.css` => `8px 12px`
- `apk_payload/static/seats/seats.css` => `7px 10px`
- `apk_payload/static/seats/seats.css` => `0 10px !important`
- `apk_payload/static/seats/seats.css` => `0 7px !important`
- ... 6 kayıt daha

### `.board-stage` / `padding`
- `_unused_review/static/seats/seats-redesign.css` => `10px !important`
- `android_app/app/src/main/python/static/seats/seats.css` => `14px 12px 12px`
- `android_app/app/src/main/python/static/seats/seats.css` => `12px 76px 10px 6px`
- `android_app/app/src/main/python/static/seats/seats-final.css` => `10px 64px 10px 8px !important`
- `android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-final.css` => `14px !important`
- `android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-final.css` => `10px !important`
- `apk_payload/static/seats/seats.css` => `14px 12px 12px`
- `apk_payload/static/seats/seats.css` => `12px 76px 10px 6px`
- `apk_payload/static/seats/seats-final.css` => `10px 64px 10px 8px !important`
- `apk_payload/static/seats/_archive_theme_trials/seats-dashboard-final.css` => `14px !important`
- `apk_payload/static/seats/_archive_theme_trials/seats-dashboard-final.css` => `10px !important`
- `static/seats/seats.css` => `14px 12px 12px`
- ... 6 kayıt daha

### `.icon-btn` / `width`
- `android_app/app/src/main/python/static/seats/seats.css` => `50px`
- `android_app/app/src/main/python/static/seats/seats.css` => `44px`
- `android_app/app/src/main/python/static/seats/seats.css` => `40px`
- `android_app/app/src/main/python/static/seats/seats.css` => `42px`
- `android_app/app/src/main/python/static/seats/seats-final.css` => `42px !important`
- `android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-final.css` => `48px !important`
- `apk_payload/static/seats/seats.css` => `50px`
- `apk_payload/static/seats/seats.css` => `44px`
- `apk_payload/static/seats/seats.css` => `40px`
- `apk_payload/static/seats/seats.css` => `42px`
- `apk_payload/static/seats/seats-final.css` => `42px !important`
- `apk_payload/static/seats/_archive_theme_trials/seats-dashboard-final.css` => `48px !important`
- ... 6 kayıt daha

### `.icon-btn` / `height`
- `android_app/app/src/main/python/static/seats/seats.css` => `50px`
- `android_app/app/src/main/python/static/seats/seats.css` => `44px`
- `android_app/app/src/main/python/static/seats/seats.css` => `40px`
- `android_app/app/src/main/python/static/seats/seats.css` => `42px`
- `android_app/app/src/main/python/static/seats/seats-final.css` => `42px !important`
- `android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-final.css` => `48px !important`
- `apk_payload/static/seats/seats.css` => `50px`
- `apk_payload/static/seats/seats.css` => `44px`
- `apk_payload/static/seats/seats.css` => `40px`
- `apk_payload/static/seats/seats.css` => `42px`
- `apk_payload/static/seats/seats-final.css` => `42px !important`
- `apk_payload/static/seats/_archive_theme_trials/seats-dashboard-final.css` => `48px !important`
- ... 6 kayıt daha

### `.icon-btn` / `border-radius`
- `android_app/app/src/main/python/static/seats/seats.css` => `18px`
- `android_app/app/src/main/python/static/seats/seats.css` => `16px`
- `android_app/app/src/main/python/static/seats/seats.css` => `14px`
- `android_app/app/src/main/python/static/seats/seats.css` => `15px`
- `android_app/app/src/main/python/static/seats/seats-final.css` => `15px !important`
- `android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-final.css` => `18px !important`
- `apk_payload/static/seats/seats.css` => `18px`
- `apk_payload/static/seats/seats.css` => `16px`
- `apk_payload/static/seats/seats.css` => `14px`
- `apk_payload/static/seats/seats.css` => `15px`
- `apk_payload/static/seats/seats-final.css` => `15px !important`
- `apk_payload/static/seats/_archive_theme_trials/seats-dashboard-final.css` => `18px !important`
- ... 6 kayıt daha

### `.icon-btn` / `font-size`
- `android_app/app/src/main/python/static/seats/seats.css` => `21px`
- `android_app/app/src/main/python/static/seats/seats.css` => `18px`
- `android_app/app/src/main/python/static/seats/seats.css` => `17px`
- `android_app/app/src/main/python/static/seats/seats.css` => `18px`
- `android_app/app/src/main/python/static/seats/seats-final.css` => `18px !important`
- `android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-final.css` => `22px !important`
- `apk_payload/static/seats/seats.css` => `21px`
- `apk_payload/static/seats/seats.css` => `18px`
- `apk_payload/static/seats/seats.css` => `17px`
- `apk_payload/static/seats/seats.css` => `18px`
- `apk_payload/static/seats/seats-final.css` => `18px !important`
- `apk_payload/static/seats/_archive_theme_trials/seats-dashboard-final.css` => `22px !important`
- ... 6 kayıt daha

### `.status-pill` / `border-radius`
- `android_app/app/src/main/python/static/seats/seats.css` => `20px`
- `android_app/app/src/main/python/static/seats/seats.css` => `18px`
- `android_app/app/src/main/python/static/seats/seats-final.css` => `19px !important`
- `android_app/app/src/main/python/static/seats/seats-final.css` => `18px !important`
- `android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-final.css` => `25px !important`
- `android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-final.css` => `21px !important`
- `apk_payload/static/seats/seats.css` => `20px`
- `apk_payload/static/seats/seats.css` => `18px`
- `apk_payload/static/seats/seats-final.css` => `19px !important`
- `apk_payload/static/seats/seats-final.css` => `18px !important`
- `apk_payload/static/seats/_archive_theme_trials/seats-dashboard-final.css` => `25px !important`
- `apk_payload/static/seats/_archive_theme_trials/seats-dashboard-final.css` => `21px !important`
- ... 6 kayıt daha

### `0%` / `transform`
- `android_app/app/src/main/python/static/seats/seats.css` => `scale(1)`
- `android_app/app/src/main/python/static/seats/seats.css` => `scale(1)`
- `android_app/app/src/main/python/static/seats/seats.css` => `translateX(-45%) rotate(8deg)`
- `android_app/app/src/main/python/static/seats/seats-final.css` => `translateX(0)`
- `android_app/app/src/main/python/static/live_map/muavin_live_map_extra.css` => `translateY(0)`
- `android_app/app/src/main/python/static/live_map/muavin_live_map_extra.css` => `translateY(0)`
- `apk_payload/static/seats/seats.css` => `scale(1)`
- `apk_payload/static/seats/seats.css` => `scale(1)`
- `apk_payload/static/seats/seats.css` => `translateX(-45%) rotate(8deg)`
- `apk_payload/static/seats/seats-final.css` => `translateX(0)`
- `apk_payload/static/live_map/muavin_live_map_extra.css` => `translateY(0)`
- `apk_payload/static/live_map/muavin_live_map_extra.css` => `translateY(0)`
- ... 6 kayıt daha

### `100%` / `transform`
- `android_app/app/src/main/python/static/seats/seats.css` => `scale(1)`
- `android_app/app/src/main/python/static/seats/seats.css` => `scale(1)`
- `android_app/app/src/main/python/static/seats/seats.css` => `translateX(45%) rotate(8deg)`
- `android_app/app/src/main/python/static/seats/seats-final.css` => `translateX(-50%)`
- `android_app/app/src/main/python/static/live_map/muavin_live_map_extra.css` => `translateY(0)`
- `android_app/app/src/main/python/static/live_map/muavin_live_map_extra.css` => `translateY(0)`
- `apk_payload/static/seats/seats.css` => `scale(1)`
- `apk_payload/static/seats/seats.css` => `scale(1)`
- `apk_payload/static/seats/seats.css` => `translateX(45%) rotate(8deg)`
- `apk_payload/static/seats/seats-final.css` => `translateX(-50%)`
- `apk_payload/static/live_map/muavin_live_map_extra.css` => `translateY(0)`
- `apk_payload/static/live_map/muavin_live_map_extra.css` => `translateY(0)`
- ... 6 kayıt daha

### `.voice-state` / `padding`
- `android_app/app/src/main/python/static/seats/seats.css` => `8px 12px`
- `android_app/app/src/main/python/static/seats/seats.css` => `7px 10px`
- `android_app/app/src/main/python/static/seats/seats.css` => `6px 9px`
- `android_app/app/src/main/python/static/seats/seats.css` => `0 18px !important`
- `android_app/app/src/main/python/static/seats/seats.css` => `0 14px !important`
- `android_app/app/src/main/python/static/seats/seats-final.css` => `0 8px !important`
- `apk_payload/static/seats/seats.css` => `8px 12px`
- `apk_payload/static/seats/seats.css` => `7px 10px`
- `apk_payload/static/seats/seats.css` => `6px 9px`
- `apk_payload/static/seats/seats.css` => `0 18px !important`
- `apk_payload/static/seats/seats.css` => `0 14px !important`
- `apk_payload/static/seats/seats-final.css` => `0 8px !important`
- ... 6 kayıt daha

### `.route-stop` / `min-width`
- `android_app/app/src/main/python/static/seats/seats.css` => `138px`
- `android_app/app/src/main/python/static/seats/seats.css` => `100px`
- `android_app/app/src/main/python/static/seats/seats.css` => `92px`
- `android_app/app/src/main/python/static/seats/seats.css` => `128px`
- `android_app/app/src/main/python/static/seats/seats.css` => `118px`
- `android_app/app/src/main/python/static/seats/seats-final.css` => `118px !important`
- `apk_payload/static/seats/seats.css` => `138px`
- `apk_payload/static/seats/seats.css` => `100px`
- `apk_payload/static/seats/seats.css` => `92px`
- `apk_payload/static/seats/seats.css` => `128px`
- `apk_payload/static/seats/seats.css` => `118px`
- `apk_payload/static/seats/seats-final.css` => `118px !important`
- ... 6 kayıt daha

### `.voice-command-btn` / `max-width`
- `android_app/app/src/main/python/static/seats/seats.css` => `158px`
- `android_app/app/src/main/python/static/seats/seats.css` => `148px`
- `android_app/app/src/main/python/static/seats/seats.css` => `100% !important`
- `android_app/app/src/main/python/static/seats/seats.css` => `210px !important`
- `android_app/app/src/main/python/static/seats/seats.css` => `205px !important`
- `android_app/app/src/main/python/static/seats/seats.css` => `195px !important`
- `apk_payload/static/seats/seats.css` => `158px`
- `apk_payload/static/seats/seats.css` => `148px`
- `apk_payload/static/seats/seats.css` => `100% !important`
- `apk_payload/static/seats/seats.css` => `210px !important`
- `apk_payload/static/seats/seats.css` => `205px !important`
- `apk_payload/static/seats/seats.css` => `195px !important`
- ... 6 kayıt daha

### `.route-live-row .mini-chip` / `min-height`
- `android_app/app/src/main/python/static/seats/seats.css` => `38px`
- `android_app/app/src/main/python/static/seats/seats-final.css` => `38px !important`
- `android_app/app/src/main/python/static/seats/seats-final.css` => `36px !important`
- `android_app/app/src/main/python/static/seats/seats-final.css` => `35px !important`
- `android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-final.css` => `58px !important`
- `android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-final.css` => `52px !important`
- `apk_payload/static/seats/seats.css` => `38px`
- `apk_payload/static/seats/seats-final.css` => `38px !important`
- `apk_payload/static/seats/seats-final.css` => `36px !important`
- `apk_payload/static/seats/seats-final.css` => `35px !important`
- `apk_payload/static/seats/_archive_theme_trials/seats-dashboard-final.css` => `58px !important`
- `apk_payload/static/seats/_archive_theme_trials/seats-dashboard-final.css` => `52px !important`
- ... 6 kayıt daha

### `.route-live-row .mini-chip` / `padding`
- `android_app/app/src/main/python/static/seats/seats.css` => `8px 10px`
- `android_app/app/src/main/python/static/seats/seats.css` => `0 12px !important`
- `android_app/app/src/main/python/static/seats/seats.css` => `0 10px !important`
- `android_app/app/src/main/python/static/seats/seats.css` => `0 8px !important`
- `android_app/app/src/main/python/static/seats/seats-final.css` => `7px 9px !important`
- `android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-final.css` => `10px 12px !important`
- `apk_payload/static/seats/seats.css` => `8px 10px`
- `apk_payload/static/seats/seats.css` => `0 12px !important`
- `apk_payload/static/seats/seats.css` => `0 10px !important`
- `apk_payload/static/seats/seats.css` => `0 8px !important`
- `apk_payload/static/seats/seats-final.css` => `7px 9px !important`
- `apk_payload/static/seats/_archive_theme_trials/seats-dashboard-final.css` => `10px 12px !important`
- ... 6 kayıt daha

### `body.drive-mode .board-head` / `grid-template-columns`
- `android_app/app/src/main/python/static/seats/seats.css` => `minmax(0,1fr) auto`
- `android_app/app/src/main/python/static/seats/seats.css` => `1fr`
- `android_app/app/src/main/python/static/seats/seats.css` => `minmax(0,1fr) auto !important`
- `android_app/app/src/main/python/static/seats/seats.css` => `1fr !important`
- `android_app/app/src/main/python/static/seats/seats-final.css` => `1fr !important`
- `android_app/app/src/main/python/static/seats/seats-final.css` => `1fr !important`
- `apk_payload/static/seats/seats.css` => `minmax(0,1fr) auto`
- `apk_payload/static/seats/seats.css` => `1fr`
- `apk_payload/static/seats/seats.css` => `minmax(0,1fr) auto !important`
- `apk_payload/static/seats/seats.css` => `1fr !important`
- `apk_payload/static/seats/seats-final.css` => `1fr !important`
- `apk_payload/static/seats/seats-final.css` => `1fr !important`
- ... 6 kayıt daha

### `body.drive-mode .deck` / `padding-bottom`
- `android_app/app/src/main/python/static/seats/seats.css` => `88px !important`
- `android_app/app/src/main/python/static/seats/seats.css` => `84px !important`
- `android_app/app/src/main/python/static/seats/seats.css` => `76px !important`
- `android_app/app/src/main/python/static/seats/seats.css` => `68px !important`
- `android_app/app/src/main/python/static/seats/seats-final.css` => `82px !important`
- `android_app/app/src/main/python/static/seats/seats-final.css` => `78px !important`
- `apk_payload/static/seats/seats.css` => `88px !important`
- `apk_payload/static/seats/seats.css` => `84px !important`
- `apk_payload/static/seats/seats.css` => `76px !important`
- `apk_payload/static/seats/seats.css` => `68px !important`
- `apk_payload/static/seats/seats-final.css` => `82px !important`
- `apk_payload/static/seats/seats-final.css` => `78px !important`
- ... 6 kayıt daha

### `body.drive-mode #driveInlineDock` / `gap`
- `android_app/app/src/main/python/static/seats/seats.css` => `7px !important`
- `android_app/app/src/main/python/static/seats/seats.css` => `6px !important`
- `android_app/app/src/main/python/static/seats/seats.css` => `5px !important`
- `android_app/app/src/main/python/static/seats/seats.css` => `4px !important`
- `android_app/app/src/main/python/static/seats/seats-final.css` => `7px !important`
- `android_app/app/src/main/python/static/seats/seats-final.css` => `6px !important`
- `apk_payload/static/seats/seats.css` => `7px !important`
- `apk_payload/static/seats/seats.css` => `6px !important`
- `apk_payload/static/seats/seats.css` => `5px !important`
- `apk_payload/static/seats/seats.css` => `4px !important`
- `apk_payload/static/seats/seats-final.css` => `7px !important`
- `apk_payload/static/seats/seats-final.css` => `6px !important`
- ... 6 kayıt daha

### `body.drive-mode .board-head` / `padding-right`
- `android_app/app/src/main/python/static/seats/seats.css` => `164px !important`
- `android_app/app/src/main/python/static/seats/seats.css` => `150px !important`
- `android_app/app/src/main/python/static/seats/seats.css` => `134px !important`
- `android_app/app/src/main/python/static/seats/seats.css` => `124px !important`
- `android_app/app/src/main/python/static/seats/seats-final.css` => `0 !important`
- `android_app/app/src/main/python/static/seats/seats-final.css` => `0 !important`
- `apk_payload/static/seats/seats.css` => `164px !important`
- `apk_payload/static/seats/seats.css` => `150px !important`
- `apk_payload/static/seats/seats.css` => `134px !important`
- `apk_payload/static/seats/seats.css` => `124px !important`
- `apk_payload/static/seats/seats-final.css` => `0 !important`
- `apk_payload/static/seats/seats-final.css` => `0 !important`
- ... 6 kayıt daha

### `body:not(.drive-mode) #driveInlineDock` / `top`
- `android_app/app/src/main/python/static/seats/seats.css` => `8px !important`
- `android_app/app/src/main/python/static/seats/seats.css` => `7px !important`
- `android_app/app/src/main/python/static/seats/seats.css` => `18px !important`
- `android_app/app/src/main/python/static/seats/seats.css` => `16px !important`
- `android_app/app/src/main/python/static/seats/seats.css` => `14px !important`
- `android_app/app/src/main/python/static/seats/seats-final.css` => `auto !important`
- `apk_payload/static/seats/seats.css` => `8px !important`
- `apk_payload/static/seats/seats.css` => `7px !important`
- `apk_payload/static/seats/seats.css` => `18px !important`
- `apk_payload/static/seats/seats.css` => `16px !important`
- `apk_payload/static/seats/seats.css` => `14px !important`
- `apk_payload/static/seats/seats-final.css` => `auto !important`
- ... 6 kayıt daha

### `body:not(.drive-mode) #driveInlineDock` / `right`
- `android_app/app/src/main/python/static/seats/seats.css` => `8px !important`
- `android_app/app/src/main/python/static/seats/seats.css` => `7px !important`
- `android_app/app/src/main/python/static/seats/seats.css` => `18px !important`
- `android_app/app/src/main/python/static/seats/seats.css` => `16px !important`
- `android_app/app/src/main/python/static/seats/seats.css` => `14px !important`
- `android_app/app/src/main/python/static/seats/seats-final.css` => `auto !important`
- `apk_payload/static/seats/seats.css` => `8px !important`
- `apk_payload/static/seats/seats.css` => `7px !important`
- `apk_payload/static/seats/seats.css` => `18px !important`
- `apk_payload/static/seats/seats.css` => `16px !important`
- `apk_payload/static/seats/seats.css` => `14px !important`
- `apk_payload/static/seats/seats-final.css` => `auto !important`
- ... 6 kayıt daha

### `.night-voice-toggle` / `min-height`
- `android_app/app/src/main/python/static/seats/seats.css` => `38px`
- `android_app/app/src/main/python/static/seats/seats.css` => `34px`
- `android_app/app/src/main/python/static/seats/seats.css` => `32px`
- `android_app/app/src/main/python/static/seats/seats.css` => `32px !important`
- `android_app/app/src/main/python/static/seats/seats.css` => `30px !important`
- `android_app/app/src/main/python/static/seats/seats.css` => `29px !important`
- `apk_payload/static/seats/seats.css` => `38px`
- `apk_payload/static/seats/seats.css` => `34px`
- `apk_payload/static/seats/seats.css` => `32px`
- `apk_payload/static/seats/seats.css` => `32px !important`
- `apk_payload/static/seats/seats.css` => `30px !important`
- `apk_payload/static/seats/seats.css` => `29px !important`
- ... 6 kayıt daha

### `.night-voice-toggle` / `padding`
- `android_app/app/src/main/python/static/seats/seats.css` => `8px 12px`
- `android_app/app/src/main/python/static/seats/seats.css` => `7px 10px`
- `android_app/app/src/main/python/static/seats/seats.css` => `6px 9px`
- `android_app/app/src/main/python/static/seats/seats.css` => `6px 9px !important`
- `android_app/app/src/main/python/static/seats/seats.css` => `5px 8px !important`
- `android_app/app/src/main/python/static/seats/seats.css` => `5px 7px !important`
- `apk_payload/static/seats/seats.css` => `8px 12px`
- `apk_payload/static/seats/seats.css` => `7px 10px`
- `apk_payload/static/seats/seats.css` => `6px 9px`
- `apk_payload/static/seats/seats.css` => `6px 9px !important`
- `apk_payload/static/seats/seats.css` => `5px 8px !important`
- `apk_payload/static/seats/seats.css` => `5px 7px !important`
- ... 6 kayıt daha

### `.night-voice-toggle` / `font-size`
- `android_app/app/src/main/python/static/seats/seats.css` => `12px`
- `android_app/app/src/main/python/static/seats/seats.css` => `11px`
- `android_app/app/src/main/python/static/seats/seats.css` => `10.5px`
- `android_app/app/src/main/python/static/seats/seats.css` => `10.5px !important`
- `android_app/app/src/main/python/static/seats/seats.css` => `10px !important`
- `android_app/app/src/main/python/static/seats/seats.css` => `9.5px !important`
- `apk_payload/static/seats/seats.css` => `12px`
- `apk_payload/static/seats/seats.css` => `11px`
- `apk_payload/static/seats/seats.css` => `10.5px`
- `apk_payload/static/seats/seats.css` => `10.5px !important`
- `apk_payload/static/seats/seats.css` => `10px !important`
- `apk_payload/static/seats/seats.css` => `9.5px !important`
- ... 6 kayıt daha

### `#driveInlineDock` / `grid-template-columns`
- `android_app/app/src/main/python/static/seats/seats-final.css` => `92px minmax(0,1fr) minmax(0,1.2fr) !important`
- `android_app/app/src/main/python/static/seats/seats-final.css` => `82px minmax(0,1fr) minmax(0,1.05fr) !important`
- `android_app/app/src/main/python/static/seats/seats-final.css` => `180px minmax(0,1fr) !important`
- `android_app/app/src/main/python/static/seats/seats-final.css` => `180px minmax(0,1fr) !important`
- `android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-final.css` => `120px 1fr 1.2fr !important`
- `android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-final.css` => `88px 1fr 1fr !important`
- `apk_payload/static/seats/seats-final.css` => `92px minmax(0,1fr) minmax(0,1.2fr) !important`
- `apk_payload/static/seats/seats-final.css` => `82px minmax(0,1fr) minmax(0,1.05fr) !important`
- `apk_payload/static/seats/seats-final.css` => `180px minmax(0,1fr) !important`
- `apk_payload/static/seats/seats-final.css` => `180px minmax(0,1fr) !important`
- `apk_payload/static/seats/_archive_theme_trials/seats-dashboard-final.css` => `120px 1fr 1.2fr !important`
- `apk_payload/static/seats/_archive_theme_trials/seats-dashboard-final.css` => `88px 1fr 1fr !important`
- ... 6 kayıt daha

### `.fab-column.fab-left-gap-moved` / `gap`
- `android_app/app/src/main/python/static/seats/patches/seat-layout-fab-pack.css` => `7px !important`
- `android_app/app/src/main/python/static/seats/patches/seat-layout-fab-pack.css` => `6px !important`
- `android_app/app/src/main/python/static/seats/patches/seat-layout-fab-pack.css` => `5px !important`
- `android_app/app/src/main/python/static/seats/patches/seat-layout-fab-pack.css` => `4px !important`
- `android_app/app/src/main/python/static/seats/patches/seat-layout-fab-pack.css` => `5px !important`
- `android_app/app/src/main/python/static/seats/patches/seat-layout-fab-pack.css` => `4px !important`
- `apk_payload/static/seats/patches/seat-layout-fab-pack.css` => `7px !important`
- `apk_payload/static/seats/patches/seat-layout-fab-pack.css` => `6px !important`
- `apk_payload/static/seats/patches/seat-layout-fab-pack.css` => `5px !important`
- `apk_payload/static/seats/patches/seat-layout-fab-pack.css` => `4px !important`
- `apk_payload/static/seats/patches/seat-layout-fab-pack.css` => `5px !important`
- `apk_payload/static/seats/patches/seat-layout-fab-pack.css` => `4px !important`
- ... 6 kayıt daha

### `.fab-column.fab-left-gap-moved .fab` / `font-size`
- `android_app/app/src/main/python/static/seats/patches/seat-layout-fab-pack.css` => `19px !important`
- `android_app/app/src/main/python/static/seats/patches/seat-layout-fab-pack.css` => `18px !important`
- `android_app/app/src/main/python/static/seats/patches/seat-layout-fab-pack.css` => `17px !important`
- `android_app/app/src/main/python/static/seats/patches/seat-layout-fab-pack.css` => `16px !important`
- `android_app/app/src/main/python/static/seats/patches/seat-layout-fab-pack.css` => `17px !important`
- `android_app/app/src/main/python/static/seats/patches/seat-layout-fab-pack.css` => `16px !important`
- `apk_payload/static/seats/patches/seat-layout-fab-pack.css` => `19px !important`
- `apk_payload/static/seats/patches/seat-layout-fab-pack.css` => `18px !important`
- `apk_payload/static/seats/patches/seat-layout-fab-pack.css` => `17px !important`
- `apk_payload/static/seats/patches/seat-layout-fab-pack.css` => `16px !important`
- `apk_payload/static/seats/patches/seat-layout-fab-pack.css` => `17px !important`
- `apk_payload/static/seats/patches/seat-layout-fab-pack.css` => `16px !important`
- ... 6 kayıt daha

### `body.drive-mode .fab-column.fab-left-gap-moved .fab` / `width`
- `android_app/app/src/main/python/static/seats/patches/seat-layout-fab-pack.css` => `46px !important`
- `android_app/app/src/main/python/static/seats/patches/seat-layout-fab-pack.css` => `44px !important`
- `android_app/app/src/main/python/static/seats/patches/seat-layout-fab-pack.css` => `41px !important`
- `android_app/app/src/main/python/static/seats/patches/seat-layout-fab-pack.css` => `39px !important`
- `android_app/app/src/main/python/static/seats/patches/seat-layout-fab-pack.css` => `41px !important`
- `android_app/app/src/main/python/static/seats/patches/seat-layout-fab-pack.css` => `39px !important`
- `apk_payload/static/seats/patches/seat-layout-fab-pack.css` => `46px !important`
- `apk_payload/static/seats/patches/seat-layout-fab-pack.css` => `44px !important`
- `apk_payload/static/seats/patches/seat-layout-fab-pack.css` => `41px !important`
- `apk_payload/static/seats/patches/seat-layout-fab-pack.css` => `39px !important`
- `apk_payload/static/seats/patches/seat-layout-fab-pack.css` => `41px !important`
- `apk_payload/static/seats/patches/seat-layout-fab-pack.css` => `39px !important`
- ... 6 kayıt daha

### `body.drive-mode .fab-column.fab-left-gap-moved .fab` / `height`
- `android_app/app/src/main/python/static/seats/patches/seat-layout-fab-pack.css` => `46px !important`
- `android_app/app/src/main/python/static/seats/patches/seat-layout-fab-pack.css` => `44px !important`
- `android_app/app/src/main/python/static/seats/patches/seat-layout-fab-pack.css` => `41px !important`
- `android_app/app/src/main/python/static/seats/patches/seat-layout-fab-pack.css` => `39px !important`
- `android_app/app/src/main/python/static/seats/patches/seat-layout-fab-pack.css` => `41px !important`
- `android_app/app/src/main/python/static/seats/patches/seat-layout-fab-pack.css` => `39px !important`
- `apk_payload/static/seats/patches/seat-layout-fab-pack.css` => `46px !important`
- `apk_payload/static/seats/patches/seat-layout-fab-pack.css` => `44px !important`
- `apk_payload/static/seats/patches/seat-layout-fab-pack.css` => `41px !important`
- `apk_payload/static/seats/patches/seat-layout-fab-pack.css` => `39px !important`
- `apk_payload/static/seats/patches/seat-layout-fab-pack.css` => `41px !important`
- `apk_payload/static/seats/patches/seat-layout-fab-pack.css` => `39px !important`
- ... 6 kayıt daha

### `body.drive-mode .fab-column.fab-left-gap-moved .fab` / `border-radius`
- `android_app/app/src/main/python/static/seats/patches/seat-layout-fab-pack.css` => `16px !important`
- `android_app/app/src/main/python/static/seats/patches/seat-layout-fab-pack.css` => `15px !important`
- `android_app/app/src/main/python/static/seats/patches/seat-layout-fab-pack.css` => `15px !important`
- `android_app/app/src/main/python/static/seats/patches/seat-layout-fab-pack.css` => `14px !important`
- `android_app/app/src/main/python/static/seats/patches/seat-layout-fab-pack.css` => `15px !important`
- `android_app/app/src/main/python/static/seats/patches/seat-layout-fab-pack.css` => `14px !important`
- `apk_payload/static/seats/patches/seat-layout-fab-pack.css` => `16px !important`
- `apk_payload/static/seats/patches/seat-layout-fab-pack.css` => `15px !important`
- `apk_payload/static/seats/patches/seat-layout-fab-pack.css` => `15px !important`
- `apk_payload/static/seats/patches/seat-layout-fab-pack.css` => `14px !important`
- `apk_payload/static/seats/patches/seat-layout-fab-pack.css` => `15px !important`
- `apk_payload/static/seats/patches/seat-layout-fab-pack.css` => `14px !important`
- ... 6 kayıt daha

### `body.drive-mode .fab-column.fab-left-gap-moved .fab` / `font-size`
- `android_app/app/src/main/python/static/seats/patches/seat-layout-fab-pack.css` => `19px !important`
- `android_app/app/src/main/python/static/seats/patches/seat-layout-fab-pack.css` => `18px !important`
- `android_app/app/src/main/python/static/seats/patches/seat-layout-fab-pack.css` => `17px !important`
- `android_app/app/src/main/python/static/seats/patches/seat-layout-fab-pack.css` => `16px !important`
- `android_app/app/src/main/python/static/seats/patches/seat-layout-fab-pack.css` => `17px !important`
- `android_app/app/src/main/python/static/seats/patches/seat-layout-fab-pack.css` => `16px !important`
- `apk_payload/static/seats/patches/seat-layout-fab-pack.css` => `19px !important`
- `apk_payload/static/seats/patches/seat-layout-fab-pack.css` => `18px !important`
- `apk_payload/static/seats/patches/seat-layout-fab-pack.css` => `17px !important`
- `apk_payload/static/seats/patches/seat-layout-fab-pack.css` => `16px !important`
- `apk_payload/static/seats/patches/seat-layout-fab-pack.css` => `17px !important`
- `apk_payload/static/seats/patches/seat-layout-fab-pack.css` => `16px !important`
- ... 6 kayıt daha

### `.fab-column.fab-left-gap-moved` / `padding`
- `android_app/app/src/main/python/static/seats/patches/seat-layout-fab-pack.css` => `18px 8px 8px !important`
- `android_app/app/src/main/python/static/seats/patches/seat-layout-fab-pack.css` => `17px 7px 7px !important`
- `android_app/app/src/main/python/static/seats/patches/seat-layout-fab-pack.css` => `15px 6px 6px !important`
- `android_app/app/src/main/python/static/seats/patches/seat-layout-fab-pack.css` => `14px 5px 5px !important`
- `android_app/app/src/main/python/static/seats/patches/seat-layout-fab-pack.css` => `15px 6px 6px !important`
- `android_app/app/src/main/python/static/seats/patches/seat-layout-fab-pack.css` => `14px 5px 5px !important`
- `apk_payload/static/seats/patches/seat-layout-fab-pack.css` => `18px 8px 8px !important`
- `apk_payload/static/seats/patches/seat-layout-fab-pack.css` => `17px 7px 7px !important`
- `apk_payload/static/seats/patches/seat-layout-fab-pack.css` => `15px 6px 6px !important`
- `apk_payload/static/seats/patches/seat-layout-fab-pack.css` => `14px 5px 5px !important`
- `apk_payload/static/seats/patches/seat-layout-fab-pack.css` => `15px 6px 6px !important`
- `apk_payload/static/seats/patches/seat-layout-fab-pack.css` => `14px 5px 5px !important`
- ... 6 kayıt daha

### `.fab-column.fab-left-gap-moved` / `border-radius`
- `android_app/app/src/main/python/static/seats/patches/seat-layout-fab-pack.css` => `24px !important`
- `android_app/app/src/main/python/static/seats/patches/seat-layout-fab-pack.css` => `22px !important`
- `android_app/app/src/main/python/static/seats/patches/seat-layout-fab-pack.css` => `21px !important`
- `android_app/app/src/main/python/static/seats/patches/seat-layout-fab-pack.css` => `19px !important`
- `android_app/app/src/main/python/static/seats/patches/seat-layout-fab-pack.css` => `21px !important`
- `android_app/app/src/main/python/static/seats/patches/seat-layout-fab-pack.css` => `19px !important`
- `apk_payload/static/seats/patches/seat-layout-fab-pack.css` => `24px !important`
- `apk_payload/static/seats/patches/seat-layout-fab-pack.css` => `22px !important`
- `apk_payload/static/seats/patches/seat-layout-fab-pack.css` => `21px !important`
- `apk_payload/static/seats/patches/seat-layout-fab-pack.css` => `19px !important`
- `apk_payload/static/seats/patches/seat-layout-fab-pack.css` => `21px !important`
- `apk_payload/static/seats/patches/seat-layout-fab-pack.css` => `19px !important`
- ... 6 kayıt daha

### `.seats-shell` / `width`
- `_unused_review/static/seats/seats-redesign.css` => `min(100vw - 12px, 1240px) !important`
- `_unused_review/static/seats/seats-redesign.css` => `calc(100vw - 8px) !important`
- `android_app/app/src/main/python/static/seats/seats.css` => `min(1480px, 100%)`
- `android_app/app/src/main/python/static/seats/seats-final.css` => `min(100vw - 12px, 1280px) !important`
- `android_app/app/src/main/python/static/seats/seats-final.css` => `calc(100vw - 8px) !important`
- `android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-final.css` => `calc(100vw - 14px) !important`
- `android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-final.css` => `calc(100vw - 8px) !important`
- `apk_payload/static/seats/seats.css` => `min(1480px, 100%)`
- `apk_payload/static/seats/seats-final.css` => `min(100vw - 12px, 1280px) !important`
- `apk_payload/static/seats/seats-final.css` => `calc(100vw - 8px) !important`
- `apk_payload/static/seats/_archive_theme_trials/seats-dashboard-final.css` => `calc(100vw - 14px) !important`
- `apk_payload/static/seats/_archive_theme_trials/seats-dashboard-final.css` => `calc(100vw - 8px) !important`
- ... 5 kayıt daha

### `.board-head` / `grid-template-columns`
- `_unused_review/static/seats/seats-redesign.css` => `1fr !important`
- `_unused_review/static/seats/seats-redesign.css` => `1fr !important`
- `android_app/app/src/main/python/static/seats/seats.css` => `minmax(0,1fr) auto`
- `android_app/app/src/main/python/static/seats/seats.css` => `1fr`
- `android_app/app/src/main/python/static/seats/seats.css` => `1fr !important`
- `android_app/app/src/main/python/static/seats/seats-final.css` => `1fr !important`
- `android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-final.css` => `1fr !important`
- `apk_payload/static/seats/seats.css` => `minmax(0,1fr) auto`
- `apk_payload/static/seats/seats.css` => `1fr`
- `apk_payload/static/seats/seats.css` => `1fr !important`
- `apk_payload/static/seats/seats-final.css` => `1fr !important`
- `apk_payload/static/seats/_archive_theme_trials/seats-dashboard-final.css` => `1fr !important`
- ... 5 kayıt daha

### `.board-head-right` / `gap`
- `_unused_review/static/seats/seats-redesign.css` => `8px !important`
- `_unused_review/static/seats/seats-redesign.css` => `9px !important`
- `android_app/app/src/main/python/static/seats/seats.css` => `10px`
- `android_app/app/src/main/python/static/seats/seats.css` => `8px`
- `android_app/app/src/main/python/static/seats/seats.css` => `7px`
- `android_app/app/src/main/python/static/seats/seats-final.css` => `8px !important`
- `android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-final.css` => `10px !important`
- `apk_payload/static/seats/seats.css` => `10px`
- `apk_payload/static/seats/seats.css` => `8px`
- `apk_payload/static/seats/seats.css` => `7px`
- `apk_payload/static/seats/seats-final.css` => `8px !important`
- `apk_payload/static/seats/_archive_theme_trials/seats-dashboard-final.css` => `10px !important`
- ... 5 kayıt daha

### `.board-stage` / `border-radius`
- `_unused_review/static/seats/seats-redesign.css` => `24px !important`
- `android_app/app/src/main/python/static/seats/seats.css` => `26px`
- `android_app/app/src/main/python/static/seats/seats.css` => `22px`
- `android_app/app/src/main/python/static/seats/seats-final.css` => `24px !important`
- `android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-final.css` => `28px !important`
- `android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-final.css` => `24px !important`
- `apk_payload/static/seats/seats.css` => `26px`
- `apk_payload/static/seats/seats.css` => `22px`
- `apk_payload/static/seats/seats-final.css` => `24px !important`
- `apk_payload/static/seats/_archive_theme_trials/seats-dashboard-final.css` => `28px !important`
- `apk_payload/static/seats/_archive_theme_trials/seats-dashboard-final.css` => `24px !important`
- `static/seats/seats.css` => `26px`
- ... 5 kayıt daha

### `.seat` / `border-radius`
- `static/style.css` => `10px`
- `_unused_review/static/seats/seats-redesign.css` => `15px !important`
- `android_app/app/src/main/python/static/seats/seats.css` => `22px`
- `android_app/app/src/main/python/static/seats/seats.css` => `22px !important`
- `android_app/app/src/main/python/static/seats/seats-final.css` => `20px !important`
- `android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-final.css` => `15px !important`
- `apk_payload/static/seats/seats.css` => `22px`
- `apk_payload/static/seats/seats.css` => `22px !important`
- `apk_payload/static/seats/seats-final.css` => `20px !important`
- `apk_payload/static/seats/_archive_theme_trials/seats-dashboard-final.css` => `15px !important`
- `static/seats/seats.css` => `22px`
- `static/seats/seats.css` => `22px !important`
- ... 4 kayıt daha

### `body` / `background`
- `_unused_review/static/seats/seats-redesign.css` => `radial-gradient(circle at 10% 0%, rgba(37,99,235,.20), transparent 34%), radial-gradient(circle at 100% 30%, rgba(14,165,233,.12), transparent 30%), linear-gradient(180deg,#071423,#081827 48%,#07111d) !important`
- `android_app/app/src/main/python/static/seats/seats.css` => `radial-gradient(circle at top left, rgba(37,99,235,.15), transparent 20%), radial-gradient(circle at top right, rgba(14,165,233,.12), transparent 18%), radial-gradient(circle at bottom right, rgba(124,58,237,.10), transparent 24%), linear-gradient(180deg, #06101c 0%, #0a1422 100%)`
- `android_app/app/src/main/python/static/seats/patches/mobile-performance-fix.css` => `#06111f !important`
- `android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-final.css` => `radial-gradient(circle at 18% 0%, rgba(37,99,235,.12), transparent 34%), radial-gradient(circle at 100% 30%, rgba(14,165,233,.14), transparent 32%), linear-gradient(180deg,var(--page-bg-1),var(--page-bg-2)) !important`
- `android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-tone.css` => `radial-gradient(circle at 15% 0%, rgba(37,99,235,.22), transparent 34%), radial-gradient(circle at 100% 30%, rgba(14,165,233,.16), transparent 30%), linear-gradient(180deg,#dfeeff 0%,#d7e7f8 38%,#cddff2 100%) !important`
- `android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-tone.css` => `radial-gradient(circle at 15% 0%, rgba(37,99,235,.18), transparent 34%), linear-gradient(180deg,#e8f2ff 0%,#d7e7f8 100%) !important`
- `apk_payload/static/seats/seats.css` => `radial-gradient(circle at top left, rgba(37,99,235,.15), transparent 20%), radial-gradient(circle at top right, rgba(14,165,233,.12), transparent 18%), radial-gradient(circle at bottom right, rgba(124,58,237,.10), transparent 24%), linear-gradient(180deg, #06101c 0%, #0a1422 100%)`
- `apk_payload/static/seats/patches/mobile-performance-fix.css` => `#06111f !important`
- `apk_payload/static/seats/_archive_theme_trials/seats-dashboard-final.css` => `radial-gradient(circle at 18% 0%, rgba(37,99,235,.12), transparent 34%), radial-gradient(circle at 100% 30%, rgba(14,165,233,.14), transparent 32%), linear-gradient(180deg,var(--page-bg-1),var(--page-bg-2)) !important`
- `apk_payload/static/seats/_archive_theme_trials/seats-dashboard-tone.css` => `radial-gradient(circle at 15% 0%, rgba(37,99,235,.22), transparent 34%), radial-gradient(circle at 100% 30%, rgba(14,165,233,.16), transparent 30%), linear-gradient(180deg,#dfeeff 0%,#d7e7f8 38%,#cddff2 100%) !important`
- `apk_payload/static/seats/_archive_theme_trials/seats-dashboard-tone.css` => `radial-gradient(circle at 15% 0%, rgba(37,99,235,.18), transparent 34%), linear-gradient(180deg,#e8f2ff 0%,#d7e7f8 100%) !important`
- `static/seats/seats.css` => `radial-gradient(circle at top left, rgba(37,99,235,.15), transparent 20%), radial-gradient(circle at top right, rgba(14,165,233,.12), transparent 18%), radial-gradient(circle at bottom right, rgba(124,58,237,.10), transparent 24%), linear-gradient(180deg, #06101c 0%, #0a1422 100%)`
- ... 4 kayıt daha

### `.layout` / `grid-template-columns`
- `_unused_review/static/seats/seats-redesign.css` => `minmax(0, 1fr) 360px !important`
- `android_app/app/src/main/python/static/seats/seats.css` => `minmax(0, 1.16fr) 420px`
- `android_app/app/src/main/python/static/seats/seats.css` => `1fr`
- `android_app/app/src/main/python/static/seats/seats-final.css` => `minmax(0,1fr) 380px !important`
- `android_app/app/src/main/python/static/seats/seats-final.css` => `1fr !important`
- `android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-final.css` => `minmax(0,1fr) 360px !important`
- `apk_payload/static/seats/seats.css` => `minmax(0, 1.16fr) 420px`
- `apk_payload/static/seats/seats.css` => `1fr`
- `apk_payload/static/seats/seats-final.css` => `minmax(0,1fr) 380px !important`
- `apk_payload/static/seats/seats-final.css` => `1fr !important`
- `apk_payload/static/seats/_archive_theme_trials/seats-dashboard-final.css` => `minmax(0,1fr) 360px !important`
- `static/seats/seats.css` => `minmax(0, 1.16fr) 420px`
- ... 4 kayıt daha

### `#driveModeToggle` / `color`
- `_unused_review/static/seats/seats-redesign.css` => `#f8fafc !important`
- `android_app/app/src/main/python/static/seats/seats.css` => `#fff`
- `android_app/app/src/main/python/static/seats/seats-final.css` => `#fff !important`
- `android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-final.css` => `var(--text) !important`
- `android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-final.css` => `#fff !important`
- `android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-tone.css` => `#f8fafc !important`
- `apk_payload/static/seats/seats.css` => `#fff`
- `apk_payload/static/seats/seats-final.css` => `#fff !important`
- `apk_payload/static/seats/_archive_theme_trials/seats-dashboard-final.css` => `var(--text) !important`
- `apk_payload/static/seats/_archive_theme_trials/seats-dashboard-final.css` => `#fff !important`
- `apk_payload/static/seats/_archive_theme_trials/seats-dashboard-tone.css` => `#f8fafc !important`
- `static/seats/seats.css` => `#fff`
- ... 4 kayıt daha

### `#driveModeToggle` / `box-shadow`
- `_unused_review/static/seats/seats-redesign.css` => `inset 0 1px 0 rgba(255,255,255,.08) !important`
- `android_app/app/src/main/python/static/seats/seats.css` => `0 14px 30px rgba(0,0,0,.35)`
- `android_app/app/src/main/python/static/seats/seats.css` => `0 14px 28px rgba(37,99,235,.35) !important`
- `android_app/app/src/main/python/static/seats/seats-final.css` => `inset 0 1px 0 rgba(255,255,255,.07) !important`
- `android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-final.css` => `0 10px 24px rgba(15,23,42,.06) !important`
- `android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-tone.css` => `inset 0 1px 0 rgba(255,255,255,.08) !important`
- `apk_payload/static/seats/seats.css` => `0 14px 30px rgba(0,0,0,.35)`
- `apk_payload/static/seats/seats.css` => `0 14px 28px rgba(37,99,235,.35) !important`
- `apk_payload/static/seats/seats-final.css` => `inset 0 1px 0 rgba(255,255,255,.07) !important`
- `apk_payload/static/seats/_archive_theme_trials/seats-dashboard-final.css` => `0 10px 24px rgba(15,23,42,.06) !important`
- `apk_payload/static/seats/_archive_theme_trials/seats-dashboard-tone.css` => `inset 0 1px 0 rgba(255,255,255,.08) !important`
- `static/seats/seats.css` => `0 14px 30px rgba(0,0,0,.35)`
- ... 4 kayıt daha

### `.drive-eta-chip` / `box-shadow`
- `_unused_review/static/seats/seats-redesign.css` => `inset 0 1px 0 rgba(255,255,255,.08) !important`
- `android_app/app/src/main/python/static/seats/seats.css` => `inset 0 1px 0 rgba(255,255,255,.08), 0 10px 24px rgba(0,0,0,.28)`
- `android_app/app/src/main/python/static/seats/seats-final.css` => `inset 0 1px 0 rgba(255,255,255,.07) !important`
- `android_app/app/src/main/python/static/seats/patches/mobile-performance-fix.css` => `0 4px 10px rgba(0,0,0,.18) !important`
- `android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-final.css` => `0 10px 24px rgba(15,23,42,.06) !important`
- `android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-tone.css` => `inset 0 1px 0 rgba(255,255,255,.08) !important`
- `apk_payload/static/seats/seats.css` => `inset 0 1px 0 rgba(255,255,255,.08), 0 10px 24px rgba(0,0,0,.28)`
- `apk_payload/static/seats/seats-final.css` => `inset 0 1px 0 rgba(255,255,255,.07) !important`
- `apk_payload/static/seats/patches/mobile-performance-fix.css` => `0 4px 10px rgba(0,0,0,.18) !important`
- `apk_payload/static/seats/_archive_theme_trials/seats-dashboard-final.css` => `0 10px 24px rgba(15,23,42,.06) !important`
- `apk_payload/static/seats/_archive_theme_trials/seats-dashboard-tone.css` => `inset 0 1px 0 rgba(255,255,255,.08) !important`
- `static/seats/seats.css` => `inset 0 1px 0 rgba(255,255,255,.08), 0 10px 24px rgba(0,0,0,.28)`
- ... 4 kayıt daha

### `#driveModeToggle` / `padding`
- `_unused_review/static/seats/seats-redesign.css` => `0 14px !important`
- `android_app/app/src/main/python/static/seats/seats.css` => `9px 13px`
- `android_app/app/src/main/python/static/seats/seats.css` => `8px 12px`
- `android_app/app/src/main/python/static/seats/seats.css` => `0 20px !important`
- `android_app/app/src/main/python/static/seats/seats.css` => `0 16px !important`
- `android_app/app/src/main/python/static/seats/seats-final.css` => `0 8px !important`
- `apk_payload/static/seats/seats.css` => `9px 13px`
- `apk_payload/static/seats/seats.css` => `8px 12px`
- `apk_payload/static/seats/seats.css` => `0 20px !important`
- `apk_payload/static/seats/seats.css` => `0 16px !important`
- `apk_payload/static/seats/seats-final.css` => `0 8px !important`
- `static/seats/seats.css` => `9px 13px`
- ... 4 kayıt daha

### `.voice-command-btn` / `border`
- `_unused_review/static/seats/seats-redesign.css` => `1px solid rgba(148,163,184,.16) !important`
- `android_app/app/src/main/python/static/seats/seats.css` => `none`
- `android_app/app/src/main/python/static/seats/seats.css` => `1px solid rgba(255,255,255,.16)`
- `android_app/app/src/main/python/static/seats/seats.css` => `1px solid rgba(255,255,255,.22) !important`
- `android_app/app/src/main/python/static/seats/seats-final.css` => `1px solid var(--sf-line) !important`
- `android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-final.css` => `1px solid var(--line) !important`
- `apk_payload/static/seats/seats.css` => `none`
- `apk_payload/static/seats/seats.css` => `1px solid rgba(255,255,255,.16)`
- `apk_payload/static/seats/seats.css` => `1px solid rgba(255,255,255,.22) !important`
- `apk_payload/static/seats/seats-final.css` => `1px solid var(--sf-line) !important`
- `apk_payload/static/seats/_archive_theme_trials/seats-dashboard-final.css` => `1px solid var(--line) !important`
- `static/seats/seats.css` => `none`
- ... 4 kayıt daha

### `.voice-state` / `border`
- `_unused_review/static/seats/seats-redesign.css` => `1px solid rgba(148,163,184,.16) !important`
- `android_app/app/src/main/python/static/seats/seats.css` => `1px solid var(--line)`
- `android_app/app/src/main/python/static/seats/seats.css` => `1px solid rgba(255,255,255,.13) !important`
- `android_app/app/src/main/python/static/seats/seats-final.css` => `1px solid var(--sf-line) !important`
- `android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-final.css` => `1px solid var(--line) !important`
- `android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-tone.css` => `1px solid rgba(255,255,255,.14) !important`
- `apk_payload/static/seats/seats.css` => `1px solid var(--line)`
- `apk_payload/static/seats/seats.css` => `1px solid rgba(255,255,255,.13) !important`
- `apk_payload/static/seats/seats-final.css` => `1px solid var(--sf-line) !important`
- `apk_payload/static/seats/_archive_theme_trials/seats-dashboard-final.css` => `1px solid var(--line) !important`
- `apk_payload/static/seats/_archive_theme_trials/seats-dashboard-tone.css` => `1px solid rgba(255,255,255,.14) !important`
- `static/seats/seats.css` => `1px solid var(--line)`
- ... 4 kayıt daha

### `.voice-command-btn` / `box-shadow`
- `_unused_review/static/seats/seats-redesign.css` => `inset 0 1px 0 rgba(255,255,255,.08) !important`
- `android_app/app/src/main/python/static/seats/seats.css` => `0 12px 24px rgba(0,0,0,.24), 0 0 0 1px rgba(255,255,255,.05) inset`
- `android_app/app/src/main/python/static/seats/seats.css` => `0 18px 34px rgba(0,0,0,.34), 0 0 0 1px rgba(255,255,255,.08) inset, 0 0 26px rgba(124,58,237,.30) !important`
- `android_app/app/src/main/python/static/seats/seats-final.css` => `inset 0 1px 0 rgba(255,255,255,.07) !important`
- `android_app/app/src/main/python/static/seats/patches/mobile-performance-fix.css` => `0 4px 10px rgba(0,0,0,.18) !important`
- `android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-final.css` => `0 10px 24px rgba(15,23,42,.06) !important`
- `apk_payload/static/seats/seats.css` => `0 12px 24px rgba(0,0,0,.24), 0 0 0 1px rgba(255,255,255,.05) inset`
- `apk_payload/static/seats/seats.css` => `0 18px 34px rgba(0,0,0,.34), 0 0 0 1px rgba(255,255,255,.08) inset, 0 0 26px rgba(124,58,237,.30) !important`
- `apk_payload/static/seats/seats-final.css` => `inset 0 1px 0 rgba(255,255,255,.07) !important`
- `apk_payload/static/seats/patches/mobile-performance-fix.css` => `0 4px 10px rgba(0,0,0,.18) !important`
- `apk_payload/static/seats/_archive_theme_trials/seats-dashboard-final.css` => `0 10px 24px rgba(15,23,42,.06) !important`
- `static/seats/seats.css` => `0 12px 24px rgba(0,0,0,.24), 0 0 0 1px rgba(255,255,255,.05) inset`
- ... 4 kayıt daha

### `.voice-command-btn` / `font-weight`
- `_unused_review/static/seats/seats-redesign.css` => `950 !important`
- `android_app/app/src/main/python/static/seats/seats.css` => `900`
- `android_app/app/src/main/python/static/seats/seats.css` => `950 !important`
- `android_app/app/src/main/python/static/seats/seats.css` => `950 !important`
- `android_app/app/src/main/python/static/seats/seats-final.css` => `950 !important`
- `android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-final.css` => `1000 !important`
- `apk_payload/static/seats/seats.css` => `900`
- `apk_payload/static/seats/seats.css` => `950 !important`
- `apk_payload/static/seats/seats.css` => `950 !important`
- `apk_payload/static/seats/seats-final.css` => `950 !important`
- `apk_payload/static/seats/_archive_theme_trials/seats-dashboard-final.css` => `1000 !important`
- `static/seats/seats.css` => `900`
- ... 4 kayıt daha

### `.voice-state` / `background`
- `_unused_review/static/seats/seats-redesign.css` => `rgba(255,255,255,.07) !important`
- `android_app/app/src/main/python/static/seats/seats.css` => `rgba(255,255,255,.045)`
- `android_app/app/src/main/python/static/seats/seats.css` => `linear-gradient(180deg, rgba(255,255,255,.075), rgba(255,255,255,.035)) !important`
- `android_app/app/src/main/python/static/seats/seats-final.css` => `rgba(255,255,255,.065) !important`
- `android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-final.css` => `#fff !important`
- `android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-tone.css` => `rgba(255,255,255,.08) !important`
- `apk_payload/static/seats/seats.css` => `rgba(255,255,255,.045)`
- `apk_payload/static/seats/seats.css` => `linear-gradient(180deg, rgba(255,255,255,.075), rgba(255,255,255,.035)) !important`
- `apk_payload/static/seats/seats-final.css` => `rgba(255,255,255,.065) !important`
- `apk_payload/static/seats/_archive_theme_trials/seats-dashboard-final.css` => `#fff !important`
- `apk_payload/static/seats/_archive_theme_trials/seats-dashboard-tone.css` => `rgba(255,255,255,.08) !important`
- `static/seats/seats.css` => `rgba(255,255,255,.045)`
- ... 4 kayıt daha

### `.voice-state` / `color`
- `_unused_review/static/seats/seats-redesign.css` => `#f8fafc !important`
- `android_app/app/src/main/python/static/seats/seats.css` => `#dbe7f4`
- `android_app/app/src/main/python/static/seats/seats.css` => `#eaf2ff !important`
- `android_app/app/src/main/python/static/seats/seats-final.css` => `#fff !important`
- `android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-final.css` => `var(--text) !important`
- `android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-tone.css` => `#f8fafc !important`
- `apk_payload/static/seats/seats.css` => `#dbe7f4`
- `apk_payload/static/seats/seats.css` => `#eaf2ff !important`
- `apk_payload/static/seats/seats-final.css` => `#fff !important`
- `apk_payload/static/seats/_archive_theme_trials/seats-dashboard-final.css` => `var(--text) !important`
- `apk_payload/static/seats/_archive_theme_trials/seats-dashboard-tone.css` => `#f8fafc !important`
- `static/seats/seats.css` => `#dbe7f4`
- ... 4 kayıt daha

### `.voice-state` / `font-weight`
- `_unused_review/static/seats/seats-redesign.css` => `950 !important`
- `android_app/app/src/main/python/static/seats/seats.css` => `800`
- `android_app/app/src/main/python/static/seats/seats.css` => `900 !important`
- `android_app/app/src/main/python/static/seats/seats.css` => `950 !important`
- `android_app/app/src/main/python/static/seats/seats-final.css` => `950 !important`
- `android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-final.css` => `1000 !important`
- `apk_payload/static/seats/seats.css` => `800`
- `apk_payload/static/seats/seats.css` => `900 !important`
- `apk_payload/static/seats/seats.css` => `950 !important`
- `apk_payload/static/seats/seats-final.css` => `950 !important`
- `apk_payload/static/seats/_archive_theme_trials/seats-dashboard-final.css` => `1000 !important`
- `static/seats/seats.css` => `800`
- ... 4 kayıt daha

### `.tab-btn` / `border-radius`
- `_unused_review/static/seats/seats-redesign.css` => `14px !important`
- `android_app/app/src/main/python/static/seats/seats.css` => `16px`
- `android_app/app/src/main/python/static/seats/seats.css` => `14px`
- `android_app/app/src/main/python/static/seats/seats.css` => `16px !important`
- `android_app/app/src/main/python/static/seats/seats-final.css` => `14px !important`
- `android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-final.css` => `15px !important`
- `apk_payload/static/seats/seats.css` => `16px`
- `apk_payload/static/seats/seats.css` => `14px`
- `apk_payload/static/seats/seats.css` => `16px !important`
- `apk_payload/static/seats/seats-final.css` => `14px !important`
- `apk_payload/static/seats/_archive_theme_trials/seats-dashboard-final.css` => `15px !important`
- `static/seats/seats.css` => `16px`
- ... 4 kayıt daha

### `.voice-command-btn` / `width`
- `_unused_review/static/seats/seats-redesign.css` => `100% !important`
- `android_app/app/src/main/python/static/seats/seats.css` => `210px !important`
- `android_app/app/src/main/python/static/seats/seats.css` => `205px !important`
- `android_app/app/src/main/python/static/seats/seats.css` => `195px !important`
- `android_app/app/src/main/python/static/seats/seats.css` => `100% !important`
- `android_app/app/src/main/python/static/seats/seats-final.css` => `100% !important`
- `apk_payload/static/seats/seats.css` => `210px !important`
- `apk_payload/static/seats/seats.css` => `205px !important`
- `apk_payload/static/seats/seats.css` => `195px !important`
- `apk_payload/static/seats/seats.css` => `100% !important`
- `apk_payload/static/seats/seats-final.css` => `100% !important`
- `static/seats/seats.css` => `210px !important`
- ... 4 kayıt daha

### `.voice-command-btn` / `gap`
- `_unused_review/static/seats/seats-redesign.css` => `8px !important`
- `android_app/app/src/main/python/static/seats/seats.css` => `8px`
- `android_app/app/src/main/python/static/seats/seats.css` => `12px !important`
- `android_app/app/src/main/python/static/seats/seats.css` => `10px !important`
- `android_app/app/src/main/python/static/seats/seats.css` => `12px !important`
- `android_app/app/src/main/python/static/seats/seats-final.css` => `7px !important`
- `apk_payload/static/seats/seats.css` => `8px`
- `apk_payload/static/seats/seats.css` => `12px !important`
- `apk_payload/static/seats/seats.css` => `10px !important`
- `apk_payload/static/seats/seats.css` => `12px !important`
- `apk_payload/static/seats/seats-final.css` => `7px !important`
- `static/seats/seats.css` => `8px`
- ... 4 kayıt daha

### `.route-title-row` / `gap`
- `android_app/app/src/main/python/static/seats/seats.css` => `10px`
- `android_app/app/src/main/python/static/seats/seats.css` => `10px`
- `android_app/app/src/main/python/static/seats/seats-final.css` => `10px !important`
- `android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-final.css` => `14px !important`
- `android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-final.css` => `12px !important`
- `apk_payload/static/seats/seats.css` => `10px`
- `apk_payload/static/seats/seats.css` => `10px`
- `apk_payload/static/seats/seats-final.css` => `10px !important`
- `apk_payload/static/seats/_archive_theme_trials/seats-dashboard-final.css` => `14px !important`
- `apk_payload/static/seats/_archive_theme_trials/seats-dashboard-final.css` => `12px !important`
- `static/seats/seats.css` => `10px`
- `static/seats/seats.css` => `10px`
- ... 3 kayıt daha

### `.route-title` / `line-height`
- `android_app/app/src/main/python/static/seats/seats.css` => `1.02`
- `android_app/app/src/main/python/static/seats/seats.css` => `1.04`
- `android_app/app/src/main/python/static/seats/seats.css` => `1`
- `android_app/app/src/main/python/static/seats/seats-final.css` => `1 !important`
- `android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-final.css` => `1 !important`
- `apk_payload/static/seats/seats.css` => `1.02`
- `apk_payload/static/seats/seats.css` => `1.04`
- `apk_payload/static/seats/seats.css` => `1`
- `apk_payload/static/seats/seats-final.css` => `1 !important`
- `apk_payload/static/seats/_archive_theme_trials/seats-dashboard-final.css` => `1 !important`
- `static/seats/seats.css` => `1.02`
- `static/seats/seats.css` => `1.04`
- ... 3 kayıt daha

### `.route-sub` / `line-height`
- `android_app/app/src/main/python/static/seats/seats.css` => `1.45`
- `android_app/app/src/main/python/static/seats/seats.css` => `1.45`
- `android_app/app/src/main/python/static/seats/seats.css` => `1.25`
- `android_app/app/src/main/python/static/seats/seats-final.css` => `1.35 !important`
- `android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-final.css` => `1.35 !important`
- `apk_payload/static/seats/seats.css` => `1.45`
- `apk_payload/static/seats/seats.css` => `1.45`
- `apk_payload/static/seats/seats.css` => `1.25`
- `apk_payload/static/seats/seats-final.css` => `1.35 !important`
- `apk_payload/static/seats/_archive_theme_trials/seats-dashboard-final.css` => `1.35 !important`
- `static/seats/seats.css` => `1.45`
- `static/seats/seats.css` => `1.45`
- ... 3 kayıt daha

### `.route-sub` / `margin-top`
- `android_app/app/src/main/python/static/seats/seats.css` => `4px`
- `android_app/app/src/main/python/static/seats/seats.css` => `4px`
- `android_app/app/src/main/python/static/seats/seats-final.css` => `5px !important`
- `android_app/app/src/main/python/static/seats/seats-final.css` => `4px !important`
- `android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-final.css` => `8px !important`
- `apk_payload/static/seats/seats.css` => `4px`
- `apk_payload/static/seats/seats.css` => `4px`
- `apk_payload/static/seats/seats-final.css` => `5px !important`
- `apk_payload/static/seats/seats-final.css` => `4px !important`
- `apk_payload/static/seats/_archive_theme_trials/seats-dashboard-final.css` => `8px !important`
- `static/seats/seats.css` => `4px`
- `static/seats/seats.css` => `4px`
- ... 3 kayıt daha

### `.route-live-row` / `display`
- `android_app/app/src/main/python/static/seats/seats.css` => `flex`
- `android_app/app/src/main/python/static/seats/seats.css` => `grid`
- `android_app/app/src/main/python/static/seats/seats.css` => `grid !important`
- `android_app/app/src/main/python/static/seats/seats-final.css` => `grid !important`
- `android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-final.css` => `grid !important`
- `apk_payload/static/seats/seats.css` => `flex`
- `apk_payload/static/seats/seats.css` => `grid`
- `apk_payload/static/seats/seats.css` => `grid !important`
- `apk_payload/static/seats/seats-final.css` => `grid !important`
- `apk_payload/static/seats/_archive_theme_trials/seats-dashboard-final.css` => `grid !important`
- `static/seats/seats.css` => `flex`
- `static/seats/seats.css` => `grid`
- ... 3 kayıt daha

### `.top-actions` / `grid-template-columns`
- `android_app/app/src/main/python/static/seats/seats.css` => `repeat(5, 50px)`
- `android_app/app/src/main/python/static/seats/seats.css` => `repeat(5, 44px)`
- `android_app/app/src/main/python/static/seats/seats.css` => `repeat(5, 40px)`
- `android_app/app/src/main/python/static/seats/seats.css` => `repeat(5, 42px)`
- `android_app/app/src/main/python/static/seats/seats-final.css` => `repeat(5,42px) !important`
- `apk_payload/static/seats/seats.css` => `repeat(5, 50px)`
- `apk_payload/static/seats/seats.css` => `repeat(5, 44px)`
- `apk_payload/static/seats/seats.css` => `repeat(5, 40px)`
- `apk_payload/static/seats/seats.css` => `repeat(5, 42px)`
- `apk_payload/static/seats/seats-final.css` => `repeat(5,42px) !important`
- `static/seats/seats.css` => `repeat(5, 50px)`
- `static/seats/seats.css` => `repeat(5, 44px)`
- ... 3 kayıt daha

### `.icon-btn` / `border`
- `android_app/app/src/main/python/static/seats/seats.css` => `none`
- `android_app/app/src/main/python/static/seats/seats.css` => `1px solid var(--line)`
- `android_app/app/src/main/python/static/seats/seats-final.css` => `1px solid var(--sf-line) !important`
- `android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-final.css` => `1px solid var(--line) !important`
- `android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-tone.css` => `1px solid rgba(255,255,255,.14) !important`
- `apk_payload/static/seats/seats.css` => `none`
- `apk_payload/static/seats/seats.css` => `1px solid var(--line)`
- `apk_payload/static/seats/seats-final.css` => `1px solid var(--sf-line) !important`
- `apk_payload/static/seats/_archive_theme_trials/seats-dashboard-final.css` => `1px solid var(--line) !important`
- `apk_payload/static/seats/_archive_theme_trials/seats-dashboard-tone.css` => `1px solid rgba(255,255,255,.14) !important`
- `static/seats/seats.css` => `none`
- `static/seats/seats.css` => `1px solid var(--line)`
- ... 3 kayıt daha

### `.status-row` / `gap`
- `android_app/app/src/main/python/static/seats/seats.css` => `10px`
- `android_app/app/src/main/python/static/seats/seats.css` => `8px`
- `android_app/app/src/main/python/static/seats/seats-final.css` => `8px !important`
- `android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-final.css` => `10px !important`
- `android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-final.css` => `8px !important`
- `apk_payload/static/seats/seats.css` => `10px`
- `apk_payload/static/seats/seats.css` => `8px`
- `apk_payload/static/seats/seats-final.css` => `8px !important`
- `apk_payload/static/seats/_archive_theme_trials/seats-dashboard-final.css` => `10px !important`
- `apk_payload/static/seats/_archive_theme_trials/seats-dashboard-final.css` => `8px !important`
- `static/seats/seats.css` => `10px`
- `static/seats/seats.css` => `8px`
- ... 3 kayıt daha

### `.status-row` / `margin`
- `android_app/app/src/main/python/static/seats/seats.css` => `14px 0 12px`
- `android_app/app/src/main/python/static/seats/seats.css` => `8px 0 10px`
- `android_app/app/src/main/python/static/seats/seats-final.css` => `9px 0 10px !important`
- `android_app/app/src/main/python/static/seats/seats-final.css` => `8px 0 9px !important`
- `android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-final.css` => `12px 0 !important`
- `apk_payload/static/seats/seats.css` => `14px 0 12px`
- `apk_payload/static/seats/seats.css` => `8px 0 10px`
- `apk_payload/static/seats/seats-final.css` => `9px 0 10px !important`
- `apk_payload/static/seats/seats-final.css` => `8px 0 9px !important`
- `apk_payload/static/seats/_archive_theme_trials/seats-dashboard-final.css` => `12px 0 !important`
- `static/seats/seats.css` => `14px 0 12px`
- `static/seats/seats.css` => `8px 0 10px`
- ... 3 kayıt daha

### `.status-pill` / `padding`
- `android_app/app/src/main/python/static/seats/seats.css` => `12px 14px`
- `android_app/app/src/main/python/static/seats/seats.css` => `10px 12px`
- `android_app/app/src/main/python/static/seats/seats-final.css` => `10px 12px !important`
- `android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-final.css` => `18px !important`
- `android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-final.css` => `13px !important`
- `apk_payload/static/seats/seats.css` => `12px 14px`
- `apk_payload/static/seats/seats.css` => `10px 12px`
- `apk_payload/static/seats/seats-final.css` => `10px 12px !important`
- `apk_payload/static/seats/_archive_theme_trials/seats-dashboard-final.css` => `18px !important`
- `apk_payload/static/seats/_archive_theme_trials/seats-dashboard-final.css` => `13px !important`
- `static/seats/seats.css` => `12px 14px`
- `static/seats/seats.css` => `10px 12px`
- ... 3 kayıt daha

### `.status-pill .k` / `font-size`
- `android_app/app/src/main/python/static/seats/seats.css` => `12px`
- `android_app/app/src/main/python/static/seats/seats.css` => `12px`
- `android_app/app/src/main/python/static/seats/seats-final.css` => `12px !important`
- `android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-final.css` => `15px !important`
- `android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-final.css` => `13px !important`
- `apk_payload/static/seats/seats.css` => `12px`
- `apk_payload/static/seats/seats.css` => `12px`
- `apk_payload/static/seats/seats-final.css` => `12px !important`
- `apk_payload/static/seats/_archive_theme_trials/seats-dashboard-final.css` => `15px !important`
- `apk_payload/static/seats/_archive_theme_trials/seats-dashboard-final.css` => `13px !important`
- `static/seats/seats.css` => `12px`
- `static/seats/seats.css` => `12px`
- ... 3 kayıt daha

### `.board-card` / `padding`
- `android_app/app/src/main/python/static/seats/seats.css` => `16px`
- `android_app/app/src/main/python/static/seats/seats.css` => `12px`
- `android_app/app/src/main/python/static/seats/seats.css` => `10px`
- `android_app/app/src/main/python/static/seats/seats-final.css` => `10px !important`
- `android_app/app/src/main/python/static/seats/seats-final.css` => `8px !important`
- `apk_payload/static/seats/seats.css` => `16px`
- `apk_payload/static/seats/seats.css` => `12px`
- `apk_payload/static/seats/seats.css` => `10px`
- `apk_payload/static/seats/seats-final.css` => `10px !important`
- `apk_payload/static/seats/seats-final.css` => `8px !important`
- `static/seats/seats.css` => `16px`
- `static/seats/seats.css` => `12px`
- ... 3 kayıt daha

### `.legend .mini-chip` / `min-height`
- `android_app/app/src/main/python/static/seats/seats.css` => `34px`
- `android_app/app/src/main/python/static/seats/seats.css` => `34px`
- `android_app/app/src/main/python/static/seats/seats-final.css` => `34px !important`
- `android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-final.css` => `42px !important`
- `android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-final.css` => `38px !important`
- `apk_payload/static/seats/seats.css` => `34px`
- `apk_payload/static/seats/seats.css` => `34px`
- `apk_payload/static/seats/seats-final.css` => `34px !important`
- `apk_payload/static/seats/_archive_theme_trials/seats-dashboard-final.css` => `42px !important`
- `apk_payload/static/seats/_archive_theme_trials/seats-dashboard-final.css` => `38px !important`
- `static/seats/seats.css` => `34px`
- `static/seats/seats.css` => `34px`
- ... 3 kayıt daha

### `.legend .mini-chip` / `font-size`
- `android_app/app/src/main/python/static/seats/seats.css` => `12px`
- `android_app/app/src/main/python/static/seats/seats.css` => `12px`
- `android_app/app/src/main/python/static/seats/seats-final.css` => `11.5px !important`
- `android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-final.css` => `13px !important`
- `android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-final.css` => `12px !important`
- `apk_payload/static/seats/seats.css` => `12px`
- `apk_payload/static/seats/seats.css` => `12px`
- `apk_payload/static/seats/seats-final.css` => `11.5px !important`
- `apk_payload/static/seats/_archive_theme_trials/seats-dashboard-final.css` => `13px !important`
- `apk_payload/static/seats/_archive_theme_trials/seats-dashboard-final.css` => `12px !important`
- `static/seats/seats.css` => `12px`
- `static/seats/seats.css` => `12px`
- ... 3 kayıt daha

### `.route-strip-meta` / `display`
- `android_app/app/src/main/python/static/seats/seats.css` => `flex`
- `android_app/app/src/main/python/static/seats/seats.css` => `flex !important`
- `android_app/app/src/main/python/static/seats/seats.css` => `grid !important`
- `android_app/app/src/main/python/static/seats/seats-final.css` => `grid !important`
- `android_app/app/src/main/python/static/seats/seats-final.css` => `grid !important`
- `apk_payload/static/seats/seats.css` => `flex`
- `apk_payload/static/seats/seats.css` => `flex !important`
- `apk_payload/static/seats/seats.css` => `grid !important`
- `apk_payload/static/seats/seats-final.css` => `grid !important`
- `apk_payload/static/seats/seats-final.css` => `grid !important`
- `static/seats/seats.css` => `flex`
- `static/seats/seats.css` => `flex !important`
- ... 3 kayıt daha

### `.route-strip-meta` / `align-items`
- `android_app/app/src/main/python/static/seats/seats.css` => `center`
- `android_app/app/src/main/python/static/seats/seats.css` => `center !important`
- `android_app/app/src/main/python/static/seats/seats.css` => `center !important`
- `android_app/app/src/main/python/static/seats/seats-final.css` => `center !important`
- `android_app/app/src/main/python/static/seats/seats-final.css` => `center !important`
- `apk_payload/static/seats/seats.css` => `center`
- `apk_payload/static/seats/seats.css` => `center !important`
- `apk_payload/static/seats/seats.css` => `center !important`
- `apk_payload/static/seats/seats-final.css` => `center !important`
- `apk_payload/static/seats/seats-final.css` => `center !important`
- `static/seats/seats.css` => `center`
- `static/seats/seats.css` => `center !important`
- ... 3 kayıt daha

### `0%` / `box-shadow`
- `android_app/app/src/main/python/static/seats/seats.css` => `0 0 0 0 rgba(245,158,11,0), inset 0 -10px 18px rgba(0,0,0,.14), 0 14px 28px rgba(0,0,0,.34)`
- `android_app/app/src/main/python/static/seats/seats.css` => `0 0 0 0 rgba(239,68,68,0), 0 14px 30px rgba(0,0,0,.3)`
- `android_app/app/src/main/python/static/seats/seats.css` => `0 12px 24px rgba(0,0,0,.18), 0 0 0 1px rgba(255,255,255,.08) inset`
- `android_app/app/src/main/python/static/seats/seats.css` => `0 14px 30px rgba(0,0,0,.34), 0 0 0 2px rgba(239,68,68,.25) inset`
- `android_app/app/src/main/python/static/seats/seats.css` => `0 18px 34px rgba(0,0,0,.34), 0 0 0 0 rgba(239,68,68,.0), 0 0 28px rgba(239,68,68,.34)`
- `apk_payload/static/seats/seats.css` => `0 0 0 0 rgba(245,158,11,0), inset 0 -10px 18px rgba(0,0,0,.14), 0 14px 28px rgba(0,0,0,.34)`
- `apk_payload/static/seats/seats.css` => `0 0 0 0 rgba(239,68,68,0), 0 14px 30px rgba(0,0,0,.3)`
- `apk_payload/static/seats/seats.css` => `0 12px 24px rgba(0,0,0,.18), 0 0 0 1px rgba(255,255,255,.08) inset`
- `apk_payload/static/seats/seats.css` => `0 14px 30px rgba(0,0,0,.34), 0 0 0 2px rgba(239,68,68,.25) inset`
- `apk_payload/static/seats/seats.css` => `0 18px 34px rgba(0,0,0,.34), 0 0 0 0 rgba(239,68,68,.0), 0 0 28px rgba(239,68,68,.34)`
- `static/seats/seats.css` => `0 0 0 0 rgba(245,158,11,0), inset 0 -10px 18px rgba(0,0,0,.14), 0 14px 28px rgba(0,0,0,.34)`
- `static/seats/seats.css` => `0 0 0 0 rgba(239,68,68,0), 0 14px 30px rgba(0,0,0,.3)`
- ... 3 kayıt daha

### `100%` / `box-shadow`
- `android_app/app/src/main/python/static/seats/seats.css` => `0 0 0 0 rgba(245,158,11,0), inset 0 -10px 18px rgba(0,0,0,.14), 0 14px 28px rgba(0,0,0,.34)`
- `android_app/app/src/main/python/static/seats/seats.css` => `0 0 0 0 rgba(239,68,68,0), 0 14px 30px rgba(0,0,0,.3)`
- `android_app/app/src/main/python/static/seats/seats.css` => `0 12px 24px rgba(0,0,0,.18), 0 0 0 1px rgba(255,255,255,.08) inset`
- `android_app/app/src/main/python/static/seats/seats.css` => `0 14px 30px rgba(0,0,0,.34), 0 0 0 2px rgba(239,68,68,.25) inset`
- `android_app/app/src/main/python/static/seats/seats.css` => `0 18px 34px rgba(0,0,0,.34), 0 0 0 0 rgba(239,68,68,.0), 0 0 28px rgba(239,68,68,.34)`
- `apk_payload/static/seats/seats.css` => `0 0 0 0 rgba(245,158,11,0), inset 0 -10px 18px rgba(0,0,0,.14), 0 14px 28px rgba(0,0,0,.34)`
- `apk_payload/static/seats/seats.css` => `0 0 0 0 rgba(239,68,68,0), 0 14px 30px rgba(0,0,0,.3)`
- `apk_payload/static/seats/seats.css` => `0 12px 24px rgba(0,0,0,.18), 0 0 0 1px rgba(255,255,255,.08) inset`
- `apk_payload/static/seats/seats.css` => `0 14px 30px rgba(0,0,0,.34), 0 0 0 2px rgba(239,68,68,.25) inset`
- `apk_payload/static/seats/seats.css` => `0 18px 34px rgba(0,0,0,.34), 0 0 0 0 rgba(239,68,68,.0), 0 0 28px rgba(239,68,68,.34)`
- `static/seats/seats.css` => `0 0 0 0 rgba(245,158,11,0), inset 0 -10px 18px rgba(0,0,0,.14), 0 14px 28px rgba(0,0,0,.34)`
- `static/seats/seats.css` => `0 0 0 0 rgba(239,68,68,0), 0 14px 30px rgba(0,0,0,.3)`
- ... 3 kayıt daha

### `.fab-column` / `bottom`
- `android_app/app/src/main/python/static/seats/seats.css` => `14px`
- `android_app/app/src/main/python/static/seats/seats.css` => `16px`
- `android_app/app/src/main/python/static/seats/seats.css` => `12px`
- `android_app/app/src/main/python/static/seats/seats-final.css` => `10px !important`
- `android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-final.css` => `14px !important`
- `apk_payload/static/seats/seats.css` => `14px`
- `apk_payload/static/seats/seats.css` => `16px`
- `apk_payload/static/seats/seats.css` => `12px`
- `apk_payload/static/seats/seats-final.css` => `10px !important`
- `apk_payload/static/seats/_archive_theme_trials/seats-dashboard-final.css` => `14px !important`
- `static/seats/seats.css` => `14px`
- `static/seats/seats.css` => `16px`
- ... 3 kayıt daha


## 9) JS syntax kontrolü

### `NODE_YOK`
```
node kurulu değil; JS syntax kontrolü atlandı.
```

## 10) Python compile kontrolü

- `app.py` compile OK
