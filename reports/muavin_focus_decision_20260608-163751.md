# Muavin Asistanı Odak Karar Raporu

- Kaynak rapor: `/data/data/com.termux/files/home/Host-Hostes-Paneli/reports/muavin_full_audit_20260608-163602.md`
- Yeni karar raporu: `/data/data/com.termux/files/home/Host-Hostes-Paneli/reports/muavin_focus_decision_20260608-163751.md`

## 1) Kritik Sayılar

- Aynı isimli çakışma adayı: **40**
- Android/Web senkron çakışması: **58**
- Eksik static/ref: **200**
- Referans verilmeyen static adayı: **200**
- Backup/eski/test adayı: **200**
- Aynı HTML içinde duplicate ID: **4**
- Farklı dosyalarda aynı ID: **200**
- Aynı dosyada tekrar JS fonksiyonu: **200**
- Farklı dosyalarda aynı JS fonksiyonu: **200**
- Aynı dosyada tekrar Python fonksiyonu: **16**
- Farklı dosyalarda aynı Python fonksiyonu: **200**
- CSS selector tekrar adayı: **200**
- Patch/yama token satırı: **200**
- Debug/TODO/alert satırı: **238**

## 2) İlk Karar

Şu aşamada silme yapılmayacak. Önce şu sırayla ilerlenmeli:

1. Android/Web farklı kopyalar incelenecek.
2. Aynı isimli ama farklı içerikli dosyalar sınıflandırılacak.
3. Eksik static referansları düzeltilecek veya referans kaldırma adayı yapılacak.
4. Backup/eski/test dosyaları aktif çağrılıyor mu kontrol edilecek.
5. Duplicate ID ve JS fonksiyon tekrarları uygulama hatası çıkarıyor mu incelenecek.
6. Son aşamada temizlik paketi hazırlanacak.

## 3) Android/Web Senkron Çakışmaları
| Alt yol | Durum | Ana kopya | Android kopya |
| --- | --- | --- | --- |
| android_server.py | ANA KOPYA YOK | - | android_app/app/src/main/python/android_server.py |
| android_server.py.bak_port_guard_20260530_104842 | ANA KOPYA YOK | - | android_app/app/src/main/python/android_server.py.bak_port_guard_20260530_104842 |
| app.py | FARKLI / SENKRON ÇAKIŞMASI | app.py | android_app/app/src/main/python/app.py |
| app.py.bak_continue_route_sync_20260523_143011 | ANA KOPYA YOK | - | android_app/app/src/main/python/app.py.bak_continue_route_sync_20260523_143011 |
| app.py.bak_sync_20260520_113916 | ANA KOPYA YOK | - | android_app/app/src/main/python/app.py.bak_sync_20260520_113916 |
| requirements.txt | ANA KOPYA YOK | - | android_app/app/src/main/python/requirements.txt |
| seed/db.sqlite3 | ANA KOPYA YOK | - | android_app/app/src/main/python/seed/db.sqlite3 |
| seed/db.sqlite3.bak_coords_sync_20260518_184401 | ANA KOPYA YOK | - | android_app/app/src/main/python/seed/db.sqlite3.bak_coords_sync_20260518_184401 |
| seed/db.sqlite3.bak_route_full_sync_20260518_191613 | ANA KOPYA YOK | - | android_app/app/src/main/python/seed/db.sqlite3.bak_route_full_sync_20260518_191613 |
| static/continue/continue_bag_emanet.js.bak_sync_continue_20260523_142710 | ANA KOPYA YOK | - | android_app/app/src/main/python/static/continue/continue_bag_emanet.js.bak_sync_continue_20260523_142710 |
| static/continue/continue_flow_refresh.js.bak_sync_continue_20260523_142710 | ANA KOPYA YOK | - | android_app/app/src/main/python/static/continue/continue_flow_refresh.js.bak_sync_continue_20260523_142710 |
| static/continue/continue_live_diagnostics.js.bak_sync_continue_20260523_142710 | ANA KOPYA YOK | - | android_app/app/src/main/python/static/continue/continue_live_diagnostics.js.bak_sync_continue_20260523_142710 |
| static/continue/continue_trip.css.bak_diag_collapsible_20260523_133213 | FARKLI / SENKRON ÇAKIŞMASI | static/continue/continue_trip.css.bak_diag_collapsible_20260523_133213 | android_app/app/src/main/python/static/continue/continue_trip.css.bak_diag_collapsible_20260523_133213 |
| static/continue/continue_trip.css.bak_live_diag_20260523_132945 | FARKLI / SENKRON ÇAKIŞMASI | static/continue/continue_trip.css.bak_live_diag_20260523_132945 | android_app/app/src/main/python/static/continue/continue_trip.css.bak_live_diag_20260523_132945 |
| static/continue/continue_trip.css.bak_map_overlay_20260523_140732 | FARKLI / SENKRON ÇAKIŞMASI | static/continue/continue_trip.css.bak_map_overlay_20260523_140732 | android_app/app/src/main/python/static/continue/continue_trip.css.bak_map_overlay_20260523_140732 |
| static/continue/continue_trip.css.bak_sync_continue_20260523_142710 | ANA KOPYA YOK | - | android_app/app/src/main/python/static/continue/continue_trip.css.bak_sync_continue_20260523_142710 |
| static/continue/continue_trip_core.js.bak_bag_emanet_clean_20260523_130105 | FARKLI / SENKRON ÇAKIŞMASI | static/continue/continue_trip_core.js.bak_bag_emanet_clean_20260523_130105 | android_app/app/src/main/python/static/continue/continue_trip_core.js.bak_bag_emanet_clean_20260523_130105 |
| static/continue/continue_trip_core.js.bak_sync_continue_20260523_142710 | ANA KOPYA YOK | - | android_app/app/src/main/python/static/continue/continue_trip_core.js.bak_sync_continue_20260523_142710 |
| static/continue/continue_trip_ui.js.bak_sync_continue_20260523_142710 | ANA KOPYA YOK | - | android_app/app/src/main/python/static/continue/continue_trip_ui.js.bak_sync_continue_20260523_142710 |
| static/data/route_segments.json.bak_geom_sync_20260518_192438 | ANA KOPYA YOK | - | android_app/app/src/main/python/static/data/route_segments.json.bak_geom_sync_20260518_192438 |
| static/live_map/muavin_live_map_extra.css.bak_final_apk_20260513_192149 | ANA KOPYA YOK | - | android_app/app/src/main/python/static/live_map/muavin_live_map_extra.css.bak_final_apk_20260513_192149 |
| static/live_map/muavin_live_map_extra.js.bak_final_apk_20260513_192149 | ANA KOPYA YOK | - | android_app/app/src/main/python/static/live_map/muavin_live_map_extra.js.bak_final_apk_20260513_192149 |
| static/profile/admin_profile_dee7d0b16870.jpg | ANA KOPYA YOK | - | android_app/app/src/main/python/static/profile/admin_profile_dee7d0b16870.jpg |
| static/seats/patches/stop-flow-focus-patch.js.bak_sync_20260520_113916 | ANA KOPYA YOK | - | android_app/app/src/main/python/static/seats/patches/stop-flow-focus-patch.js.bak_sync_20260520_113916 |
| static/seats/seats.js.bak_sync_20260520_113916 | ANA KOPYA YOK | - | android_app/app/src/main/python/static/seats/seats.js.bak_sync_20260520_113916 |
| templates/continue_trip.html.bak_bag_emanet_clean_20260523_130105 | FARKLI / SENKRON ÇAKIŞMASI | templates/continue_trip.html.bak_bag_emanet_clean_20260523_130105 | android_app/app/src/main/python/templates/continue_trip.html.bak_bag_emanet_clean_20260523_130105 |
| templates/continue_trip.html.bak_bag_emanet_split_20260523_114832 | FARKLI / SENKRON ÇAKIŞMASI | templates/continue_trip.html.bak_bag_emanet_split_20260523_114832 | android_app/app/src/main/python/templates/continue_trip.html.bak_bag_emanet_split_20260523_114832 |
| templates/continue_trip.html.bak_continue_live_flow_refresh_20260523_123118 | FARKLI / SENKRON ÇAKIŞMASI | templates/continue_trip.html.bak_continue_live_flow_refresh_20260523_123118 | android_app/app/src/main/python/templates/continue_trip.html.bak_continue_live_flow_refresh_20260523_123118 |
| templates/continue_trip.html.bak_css_split_20260523_125057 | FARKLI / SENKRON ÇAKIŞMASI | templates/continue_trip.html.bak_css_split_20260523_125057 | android_app/app/src/main/python/templates/continue_trip.html.bak_css_split_20260523_125057 |
| templates/continue_trip.html.bak_fix_live_bag_emanet_counter_20260523_115747 | FARKLI / SENKRON ÇAKIŞMASI | templates/continue_trip.html.bak_fix_live_bag_emanet_counter_20260523_115747 | android_app/app/src/main/python/templates/continue_trip.html.bak_fix_live_bag_emanet_counter_20260523_115747 |
| templates/continue_trip.html.bak_fix_live_bag_emanet_counter_20260523_115758 | FARKLI / SENKRON ÇAKIŞMASI | templates/continue_trip.html.bak_fix_live_bag_emanet_counter_20260523_115758 | android_app/app/src/main/python/templates/continue_trip.html.bak_fix_live_bag_emanet_counter_20260523_115758 |
| templates/continue_trip.html.bak_flow_refresh_20260523_130314 | FARKLI / SENKRON ÇAKIŞMASI | templates/continue_trip.html.bak_flow_refresh_20260523_130314 | android_app/app/src/main/python/templates/continue_trip.html.bak_flow_refresh_20260523_130314 |
| templates/continue_trip.html.bak_js_core_split_20260523_125851 | FARKLI / SENKRON ÇAKIŞMASI | templates/continue_trip.html.bak_js_core_split_20260523_125851 | android_app/app/src/main/python/templates/continue_trip.html.bak_js_core_split_20260523_125851 |
| templates/continue_trip.html.bak_js_safe_split_20260523_125438 | FARKLI / SENKRON ÇAKIŞMASI | templates/continue_trip.html.bak_js_safe_split_20260523_125438 | android_app/app/src/main/python/templates/continue_trip.html.bak_js_safe_split_20260523_125438 |
| templates/continue_trip.html.bak_live_diag_20260523_132945 | FARKLI / SENKRON ÇAKIŞMASI | templates/continue_trip.html.bak_live_diag_20260523_132945 | android_app/app/src/main/python/templates/continue_trip.html.bak_live_diag_20260523_132945 |
| templates/continue_trip.html.bak_map_overlay_20260523_140732 | FARKLI / SENKRON ÇAKIŞMASI | templates/continue_trip.html.bak_map_overlay_20260523_140732 | android_app/app/src/main/python/templates/continue_trip.html.bak_map_overlay_20260523_140732 |
| templates/continue_trip.html.bak_next_stop_border_20260523_114325 | FARKLI / SENKRON ÇAKIŞMASI | templates/continue_trip.html.bak_next_stop_border_20260523_114325 | android_app/app/src/main/python/templates/continue_trip.html.bak_next_stop_border_20260523_114325 |
| templates/continue_trip.html.bak_next_stop_glow_20260523_113649 | FARKLI / SENKRON ÇAKIŞMASI | templates/continue_trip.html.bak_next_stop_glow_20260523_113649 | android_app/app/src/main/python/templates/continue_trip.html.bak_next_stop_glow_20260523_113649 |
| templates/continue_trip.html.bak_real_bag_emanet_fix_20260523_120629 | FARKLI / SENKRON ÇAKIŞMASI | templates/continue_trip.html.bak_real_bag_emanet_fix_20260523_120629 | android_app/app/src/main/python/templates/continue_trip.html.bak_real_bag_emanet_fix_20260523_120629 |
| templates/continue_trip.html.bak_remove_newline_announce_20260523_122341 | FARKLI / SENKRON ÇAKIŞMASI | templates/continue_trip.html.bak_remove_newline_announce_20260523_122341 | android_app/app/src/main/python/templates/continue_trip.html.bak_remove_newline_announce_20260523_122341 |
| templates/continue_trip.html.bak_revert_continue_live_flow_20260523_123657 | FARKLI / SENKRON ÇAKIŞMASI | templates/continue_trip.html.bak_revert_continue_live_flow_20260523_123657 | android_app/app/src/main/python/templates/continue_trip.html.bak_revert_continue_live_flow_20260523_123657 |
| templates/continue_trip.html.bak_rollback_bag_emanet_split_20260523_114955 | FARKLI / SENKRON ÇAKIŞMASI | templates/continue_trip.html.bak_rollback_bag_emanet_split_20260523_114955 | android_app/app/src/main/python/templates/continue_trip.html.bak_rollback_bag_emanet_split_20260523_114955 |
| templates/continue_trip.html.bak_sync_continue_20260523_142710 | ANA KOPYA YOK | - | android_app/app/src/main/python/templates/continue_trip.html.bak_sync_continue_20260523_142710 |
| templates/continue_trip.html.bak_tts_bridge_{TS} | FARKLI / SENKRON ÇAKIŞMASI | templates/continue_trip.html.bak_tts_bridge_{TS} | android_app/app/src/main/python/templates/continue_trip.html.bak_tts_bridge_{TS} |
| templates/index.html | FARKLI / SENKRON ÇAKIŞMASI | templates/index.html | android_app/app/src/main/python/templates/index.html |
| templates/live_map.html.bak_final_apk_20260513_192149 | ANA KOPYA YOK | - | android_app/app/src/main/python/templates/live_map.html.bak_final_apk_20260513_192149 |
| templates/report_archive.html | FARKLI / SENKRON ÇAKIŞMASI | templates/report_archive.html | android_app/app/src/main/python/templates/report_archive.html |
| templates/seats.html | FARKLI / SENKRON ÇAKIŞMASI | templates/seats.html | android_app/app/src/main/python/templates/seats.html |
| templates/seats.html.bak_before_apk_sync_20260518_182148 | ANA KOPYA YOK | - | android_app/app/src/main/python/templates/seats.html.bak_before_apk_sync_20260518_182148 |
| templates/seats.html.bak_sync_20260520_113916 | ANA KOPYA YOK | - | android_app/app/src/main/python/templates/seats.html.bak_sync_20260520_113916 |
| templates/seats.html.bak_voice_bottom_final_20260516_111252 | ANA KOPYA YOK | - | android_app/app/src/main/python/templates/seats.html.bak_voice_bottom_final_20260516_111252 |
| templates/settings.html | FARKLI / SENKRON ÇAKIŞMASI | templates/settings.html | android_app/app/src/main/python/templates/settings.html |
| templates/settings_backup.html | FARKLI / SENKRON ÇAKIŞMASI | templates/settings_backup.html | android_app/app/src/main/python/templates/settings_backup.html |
| templates/settings_password.html | FARKLI / SENKRON ÇAKIŞMASI | templates/settings_password.html | android_app/app/src/main/python/templates/settings_password.html |
| templates/settings_profile.html | FARKLI / SENKRON ÇAKIŞMASI | templates/settings_profile.html | android_app/app/src/main/python/templates/settings_profile.html |
| templates/settings_recovery.html | FARKLI / SENKRON ÇAKIŞMASI | templates/settings_recovery.html | android_app/app/src/main/python/templates/settings_recovery.html |
| templates/settings_subscription.html | FARKLI / SENKRON ÇAKIŞMASI | templates/settings_subscription.html | android_app/app/src/main/python/templates/settings_subscription.html |
| templates/trip_report.html | FARKLI / SENKRON ÇAKIŞMASI | templates/trip_report.html | android_app/app/src/main/python/templates/trip_report.html |

## 4) Aynı İsimli Ama Farklı İçerikli Dosyalar
| Dosya adı | Adet | Durum | Konumlar |
| --- | --- | --- | --- |
| ic_launcher.png | 10 | FARKLI / ÇAKIŞMA ADAYI | tmp_muavin_icon/app/src/main/res/mipmap-mdpi/ic_launcher.png, tmp_muavin_icon/app/src/main/res/mipmap-hdpi/ic_launcher.png, tmp_muavin_icon/app/src/main/res/mipmap-xhdpi/ic_launcher.png, tmp_muavin_icon/app/src/main/res/mipmap-xxhdpi/ic_launcher.png, tmp_muavin_icon/app/src/main/res/mipmap-xxxhdpi/ic_launcher.png, android_app/app/src/main/res/mipmap-hdpi/ic_launcher.png, android_app/app/src/main/res/mipmap-mdpi/ic_launcher.png, android_app/app/src/main/res/mipmap-xhdpi/ic_launcher.png, android_app/app/src/main/res/mipmap-xxhdpi/ic_launcher.png, android_app/app/src/main/res/mipmap-xxxhdpi/ic_launcher.png |
| ic_launcher_round.png | 10 | FARKLI / ÇAKIŞMA ADAYI | tmp_muavin_icon/app/src/main/res/mipmap-mdpi/ic_launcher_round.png, tmp_muavin_icon/app/src/main/res/mipmap-hdpi/ic_launcher_round.png, tmp_muavin_icon/app/src/main/res/mipmap-xhdpi/ic_launcher_round.png, tmp_muavin_icon/app/src/main/res/mipmap-xxhdpi/ic_launcher_round.png, tmp_muavin_icon/app/src/main/res/mipmap-xxxhdpi/ic_launcher_round.png, android_app/app/src/main/res/mipmap-hdpi/ic_launcher_round.png, android_app/app/src/main/res/mipmap-mdpi/ic_launcher_round.png, android_app/app/src/main/res/mipmap-xhdpi/ic_launcher_round.png, android_app/app/src/main/res/mipmap-xxhdpi/ic_launcher_round.png, android_app/app/src/main/res/mipmap-xxxhdpi/ic_launcher_round.png |
| README.txt | 4 | FARKLI / ÇAKIŞMA ADAYI | tmp_muavin_icon/README.txt, android_app/app/src/main/python/static/img/onboarding/README.txt, apk_payload/static/img/onboarding/README.txt, static/img/onboarding/README.txt |
| app.py | 4 | FARKLI / ÇAKIŞMA ADAYI | app.py, apk_payload/app.py, backups/apk_sync_20260520_234501/app.py, android_app/app/src/main/python/app.py |
| seats.html | 4 | FARKLI / ÇAKIŞMA ADAYI | templates/seats.html, backups/apk_sync_20260520_234501/seats.html, android_app/app/src/main/python/templates/seats.html, apk_payload/templates/seats.html |
| trip_report.html | 4 | FARKLI / ÇAKIŞMA ADAYI | templates/trip_report.html, backups/apk_sync_20260520_234501/trip_report.html, android_app/app/src/main/python/templates/trip_report.html, apk_payload/templates/trip_report.html |
| continue_trip.html | 3 | FARKLI / ÇAKIŞMA ADAYI | templates/continue_trip.html, android_app/app/src/main/python/templates/continue_trip.html, apk_payload/templates/continue_trip.html |
| db.sqlite3 | 3 | FARKLI / ÇAKIŞMA ADAYI | db.sqlite3, android_app/app/src/main/python/seed/db.sqlite3, apk_payload/seed/db.sqlite3 |
| index.html | 3 | FARKLI / ÇAKIŞMA ADAYI | templates/index.html, android_app/app/src/main/python/templates/index.html, apk_payload/templates/index.html |
| report_archive.html | 3 | FARKLI / ÇAKIŞMA ADAYI | templates/report_archive.html, android_app/app/src/main/python/templates/report_archive.html, apk_payload/templates/report_archive.html |
| seats.js | 3 | FARKLI / ÇAKIŞMA ADAYI | android_app/app/src/main/python/static/seats/seats.js, apk_payload/static/seats/seats.js, static/seats/seats.js |
| settings.html | 3 | FARKLI / ÇAKIŞMA ADAYI | templates/settings.html, android_app/app/src/main/python/templates/settings.html, apk_payload/templates/settings.html |
| settings_backup.html | 3 | FARKLI / ÇAKIŞMA ADAYI | templates/settings_backup.html, android_app/app/src/main/python/templates/settings_backup.html, apk_payload/templates/settings_backup.html |
| settings_password.html | 3 | FARKLI / ÇAKIŞMA ADAYI | templates/settings_password.html, android_app/app/src/main/python/templates/settings_password.html, apk_payload/templates/settings_password.html |
| settings_profile.html | 3 | FARKLI / ÇAKIŞMA ADAYI | templates/settings_profile.html, android_app/app/src/main/python/templates/settings_profile.html, apk_payload/templates/settings_profile.html |
| settings_recovery.html | 3 | FARKLI / ÇAKIŞMA ADAYI | templates/settings_recovery.html, android_app/app/src/main/python/templates/settings_recovery.html, apk_payload/templates/settings_recovery.html |
| settings_subscription.html | 3 | FARKLI / ÇAKIŞMA ADAYI | templates/settings_subscription.html, android_app/app/src/main/python/templates/settings_subscription.html, apk_payload/templates/settings_subscription.html |
| build.gradle | 2 | FARKLI / ÇAKIŞMA ADAYI | android_app/build.gradle, android_app/app/build.gradle |
| continue_trip.css.bak_diag_collapsible_20260523_133213 | 2 | FARKLI / ÇAKIŞMA ADAYI | android_app/app/src/main/python/static/continue/continue_trip.css.bak_diag_collapsible_20260523_133213, static/continue/continue_trip.css.bak_diag_collapsible_20260523_133213 |
| continue_trip.css.bak_live_diag_20260523_132945 | 2 | FARKLI / ÇAKIŞMA ADAYI | android_app/app/src/main/python/static/continue/continue_trip.css.bak_live_diag_20260523_132945, static/continue/continue_trip.css.bak_live_diag_20260523_132945 |
| continue_trip.css.bak_map_overlay_20260523_140732 | 2 | FARKLI / ÇAKIŞMA ADAYI | android_app/app/src/main/python/static/continue/continue_trip.css.bak_map_overlay_20260523_140732, static/continue/continue_trip.css.bak_map_overlay_20260523_140732 |
| continue_trip.html.bak_bag_emanet_clean_20260523_130105 | 2 | FARKLI / ÇAKIŞMA ADAYI | templates/continue_trip.html.bak_bag_emanet_clean_20260523_130105, android_app/app/src/main/python/templates/continue_trip.html.bak_bag_emanet_clean_20260523_130105 |
| continue_trip.html.bak_bag_emanet_split_20260523_114832 | 2 | FARKLI / ÇAKIŞMA ADAYI | templates/continue_trip.html.bak_bag_emanet_split_20260523_114832, android_app/app/src/main/python/templates/continue_trip.html.bak_bag_emanet_split_20260523_114832 |
| continue_trip.html.bak_continue_live_flow_refresh_20260523_123118 | 2 | FARKLI / ÇAKIŞMA ADAYI | templates/continue_trip.html.bak_continue_live_flow_refresh_20260523_123118, android_app/app/src/main/python/templates/continue_trip.html.bak_continue_live_flow_refresh_20260523_123118 |
| continue_trip.html.bak_css_split_20260523_125057 | 2 | FARKLI / ÇAKIŞMA ADAYI | templates/continue_trip.html.bak_css_split_20260523_125057, android_app/app/src/main/python/templates/continue_trip.html.bak_css_split_20260523_125057 |
| continue_trip.html.bak_fix_live_bag_emanet_counter_20260523_115747 | 2 | FARKLI / ÇAKIŞMA ADAYI | templates/continue_trip.html.bak_fix_live_bag_emanet_counter_20260523_115747, android_app/app/src/main/python/templates/continue_trip.html.bak_fix_live_bag_emanet_counter_20260523_115747 |
| continue_trip.html.bak_fix_live_bag_emanet_counter_20260523_115758 | 2 | FARKLI / ÇAKIŞMA ADAYI | templates/continue_trip.html.bak_fix_live_bag_emanet_counter_20260523_115758, android_app/app/src/main/python/templates/continue_trip.html.bak_fix_live_bag_emanet_counter_20260523_115758 |
| continue_trip.html.bak_flow_refresh_20260523_130314 | 2 | FARKLI / ÇAKIŞMA ADAYI | templates/continue_trip.html.bak_flow_refresh_20260523_130314, android_app/app/src/main/python/templates/continue_trip.html.bak_flow_refresh_20260523_130314 |
| continue_trip.html.bak_js_core_split_20260523_125851 | 2 | FARKLI / ÇAKIŞMA ADAYI | templates/continue_trip.html.bak_js_core_split_20260523_125851, android_app/app/src/main/python/templates/continue_trip.html.bak_js_core_split_20260523_125851 |
| continue_trip.html.bak_js_safe_split_20260523_125438 | 2 | FARKLI / ÇAKIŞMA ADAYI | templates/continue_trip.html.bak_js_safe_split_20260523_125438, android_app/app/src/main/python/templates/continue_trip.html.bak_js_safe_split_20260523_125438 |
| continue_trip.html.bak_live_diag_20260523_132945 | 2 | FARKLI / ÇAKIŞMA ADAYI | templates/continue_trip.html.bak_live_diag_20260523_132945, android_app/app/src/main/python/templates/continue_trip.html.bak_live_diag_20260523_132945 |
| continue_trip.html.bak_map_overlay_20260523_140732 | 2 | FARKLI / ÇAKIŞMA ADAYI | templates/continue_trip.html.bak_map_overlay_20260523_140732, android_app/app/src/main/python/templates/continue_trip.html.bak_map_overlay_20260523_140732 |
| continue_trip.html.bak_next_stop_border_20260523_114325 | 2 | FARKLI / ÇAKIŞMA ADAYI | templates/continue_trip.html.bak_next_stop_border_20260523_114325, android_app/app/src/main/python/templates/continue_trip.html.bak_next_stop_border_20260523_114325 |
| continue_trip.html.bak_next_stop_glow_20260523_113649 | 2 | FARKLI / ÇAKIŞMA ADAYI | templates/continue_trip.html.bak_next_stop_glow_20260523_113649, android_app/app/src/main/python/templates/continue_trip.html.bak_next_stop_glow_20260523_113649 |
| continue_trip.html.bak_real_bag_emanet_fix_20260523_120629 | 2 | FARKLI / ÇAKIŞMA ADAYI | templates/continue_trip.html.bak_real_bag_emanet_fix_20260523_120629, android_app/app/src/main/python/templates/continue_trip.html.bak_real_bag_emanet_fix_20260523_120629 |
| continue_trip.html.bak_remove_newline_announce_20260523_122341 | 2 | FARKLI / ÇAKIŞMA ADAYI | templates/continue_trip.html.bak_remove_newline_announce_20260523_122341, android_app/app/src/main/python/templates/continue_trip.html.bak_remove_newline_announce_20260523_122341 |
| continue_trip.html.bak_revert_continue_live_flow_20260523_123657 | 2 | FARKLI / ÇAKIŞMA ADAYI | templates/continue_trip.html.bak_revert_continue_live_flow_20260523_123657, android_app/app/src/main/python/templates/continue_trip.html.bak_revert_continue_live_flow_20260523_123657 |
| continue_trip.html.bak_rollback_bag_emanet_split_20260523_114955 | 2 | FARKLI / ÇAKIŞMA ADAYI | templates/continue_trip.html.bak_rollback_bag_emanet_split_20260523_114955, android_app/app/src/main/python/templates/continue_trip.html.bak_rollback_bag_emanet_split_20260523_114955 |
| continue_trip.html.bak_tts_bridge_{TS} | 2 | FARKLI / ÇAKIŞMA ADAYI | templates/continue_trip.html.bak_tts_bridge_{TS}, android_app/app/src/main/python/templates/continue_trip.html.bak_tts_bridge_{TS} |
| continue_trip_core.js.bak_bag_emanet_clean_20260523_130105 | 2 | FARKLI / ÇAKIŞMA ADAYI | android_app/app/src/main/python/static/continue/continue_trip_core.js.bak_bag_emanet_clean_20260523_130105, static/continue/continue_trip_core.js.bak_bag_emanet_clean_20260523_130105 |

## 5) Eksik Static/Local Referanslar - Çağıran Dosyaya Göre
| Çağıran dosya | Eksik ref sayısı |
| --- | --- |
| templates/rehber.html | 15 |
| templates/index.html | 13 |
| android_app/app/src/main/python/templates/index.html | 13 |
| templates/continue_trip.html | 11 |
| templates/base.html | 9 |
| templates/seats.html | 9 |
| backups/apk_sync_20260520_234501/seats.html | 9 |
| android_app/app/src/main/python/templates/base.html | 9 |
| templates/live_map.html | 7 |
| templates/settings.html | 6 |
| templates/route_schedule_edit.html | 5 |
| templates/trip_report.html | 5 |
| templates/report_archive.html | 5 |
| backups/apk_sync_20260520_234501/trip_report.html | 5 |
| templates/consignments.html | 4 |
| templates/hesap.html | 4 |
| templates/home.html | 4 |
| templates/login.html | 4 |
| templates/routes_list.html | 4 |
| android_app/app/src/main/python/templates/consignments.html | 4 |
| android_app/app/src/main/python/templates/hesap.html | 4 |
| android_app/app/src/main/python/templates/home.html | 4 |
| templates/events.html | 3 |
| templates/settings_recovery.html | 3 |
| templates/settings_profile.html | 3 |
| android_app/app/src/main/python/templates/events.html | 3 |
| android_app/app/src/main/python/templates/login.html | 3 |
| templates/fare_admin.html | 2 |
| templates/fare_query.html | 2 |
| templates/passenger_control.html | 2 |
| templates/route_edit.html | 2 |
| templates/ai_console.html | 2 |
| templates/settings_password.html | 2 |
| templates/settings_backup.html | 2 |
| templates/settings_subscription.html | 2 |
| templates/no_active_trip.html | 2 |
| android_app/app/src/main/python/templates/fare_admin.html | 2 |
| android_app/app/src/main/python/templates/fare_query.html | 2 |
| templates/reports.html | 1 |
| templates/route_stops.html | 1 |
| templates/start_trip.html | 1 |
| templates/forgot_password.html | 1 |
| templates/setup_done.html | 1 |
| templates/subscription_required.html | 1 |
| templates/package_required.html | 1 |
| templates/onboarding.html | 1 |
| templates/settings_package_requests.html | 1 |
| templates/user_reset.html | 1 |

### Eksik referansların uzantı dağılımı
| Uzantı | Adet |
| --- | --- |
| [uzantısız] | 173 |
| .css | 4 |
| .url} | 4 |
| .photo_path }} | 3 |
| .png | 3 |
| .js | 2 |
| .view} | 2 |
| .txt} | 2 |
| .csv} | 2 |
| .view }} | 1 |
| .txt }} | 1 |
| .csv }} | 1 |
| .json }} | 1 |
| .name }} | 1 |

### Eksik referanslardan ilk 160 kayıt
| Çağıran HTML | Referans | Beklenen yol |
| --- | --- | --- |
| templates/base.html | {{ url_for( | templates/{{ url_for( |
| templates/base.html | {{ url_for( | templates/{{ url_for( |
| templates/base.html | {{ url_for( | templates/{{ url_for( |
| templates/base.html | {{ url_for( | templates/{{ url_for( |
| templates/base.html | {{ url_for( | templates/{{ url_for( |
| templates/base.html | {{ url_for( | templates/{{ url_for( |
| templates/base.html | url_for static: vendor/icons.css | static/vendor/icons.css |
| templates/base.html | url_for static: css/style.css | static/css/style.css |
| templates/base.html | url_for static: vendor/jquery.min.js | static/vendor/jquery.min.js |
| templates/consignments.html | {{ url_for( | templates/{{ url_for( |
| templates/consignments.html | {{ url_for( | templates/{{ url_for( |
| templates/consignments.html | ${p.url} | templates/${p.url} |
| templates/consignments.html | ${p.url} | templates/${p.url} |
| templates/events.html | {{ url_for( | templates/{{ url_for( |
| templates/events.html | {{ url_for( | templates/{{ url_for( |
| templates/events.html | {{ url_for( | templates/{{ url_for( |
| templates/fare_admin.html | {{ url_for( | templates/{{ url_for( |
| templates/fare_admin.html | {{ url_for( | templates/{{ url_for( |
| templates/fare_query.html | {{ url_for( | templates/{{ url_for( |
| templates/fare_query.html | {{ url_for( | templates/{{ url_for( |
| templates/hesap.html | {{ url_for( | templates/{{ url_for( |
| templates/hesap.html | {{ url_for( | templates/{{ url_for( |
| templates/hesap.html | {{ url_for( | templates/{{ url_for( |
| templates/hesap.html | {{ url_for( | templates/{{ url_for( |
| templates/home.html | {{ url_for( | templates/{{ url_for( |
| templates/home.html | {{ url_for( | templates/{{ url_for( |
| templates/home.html | {{ url_for( | templates/{{ url_for( |
| templates/home.html | {{ url_for( | templates/{{ url_for( |
| templates/index.html | {{ url_for( | templates/{{ url_for( |
| templates/index.html | {{ url_for( | templates/{{ url_for( |
| templates/index.html | {{ url_for( | templates/{{ url_for( |
| templates/index.html | {{ url_for( | templates/{{ url_for( |
| templates/index.html | {{ url_for( | templates/{{ url_for( |
| templates/index.html | {{ url_for( | templates/{{ url_for( |
| templates/index.html | {{ url_for( | templates/{{ url_for( |
| templates/index.html | {{ url_for( | templates/{{ url_for( |
| templates/index.html | {{ url_for( | templates/{{ url_for( |
| templates/index.html | {{ url_for( | templates/{{ url_for( |
| templates/index.html | /sefer-raporu-son | sefer-raporu-son |
| templates/index.html | {{ url_for( | templates/{{ url_for( |
| templates/index.html | /ayarlar | ayarlar |
| templates/login.html | {{ url_for( | templates/{{ url_for( |
| templates/login.html | {{ admin_profile.photo_path }} | templates/{{ admin_profile.photo_path }} |
| templates/login.html | /sifre-unuttum | sifre-unuttum |
| templates/login.html | /kullanici-sifirla | kullanici-sifirla |
| templates/passenger_control.html | {{ url_for( | templates/{{ url_for( |
| templates/passenger_control.html | {{ url_for( | templates/{{ url_for( |
| templates/reports.html | {{ url_for( | templates/{{ url_for( |
| templates/route_edit.html | {{ url_for( | templates/{{ url_for( |
| templates/route_edit.html | {{ url_for( | templates/{{ url_for( |
| templates/route_stops.html | {{ url_for( | templates/{{ url_for( |
| templates/routes_list.html | {{ url_for( | templates/{{ url_for( |
| templates/routes_list.html | {{ url_for( | templates/{{ url_for( |
| templates/routes_list.html | {{ url_for( | templates/{{ url_for( |
| templates/routes_list.html | {{ url_for( | templates/{{ url_for( |
| templates/seats.html | {{ url_for( | templates/{{ url_for( |
| templates/seats.html | {{ url_for( | templates/{{ url_for( |
| templates/seats.html | {{ url_for( | templates/{{ url_for( |
| templates/seats.html | /ai-console | ai-console |
| templates/seats.html | /ai-console | ai-console |
| templates/seats.html | /end_trip | end_trip |
| templates/seats.html | {{ url_for( | templates/{{ url_for( |
| templates/seats.html | {{ url_for( | templates/{{ url_for( |
| templates/seats.html | {{ url_for( | templates/{{ url_for( |
| templates/settings.html | /ayarlar/abonelik | ayarlar/abonelik |
| templates/settings.html | /ayarlar/profil | ayarlar/profil |
| templates/settings.html | /ayarlar/sifre | ayarlar/sifre |
| templates/settings.html | /ayarlar/kurtarma-kodu | ayarlar/kurtarma-kodu |
| templates/settings.html | /rapor-arsiv | rapor-arsiv |
| templates/settings.html | /ayarlar/yedekleme | ayarlar/yedekleme |
| templates/start_trip.html | {{ url_for( | templates/{{ url_for( |
| templates/ai_console.html | {{ url_for( | templates/{{ url_for( |
| templates/ai_console.html | {{ url_for( | templates/{{ url_for( |
| templates/route_schedule_edit.html | {{ url_for( | templates/{{ url_for( |
| templates/route_schedule_edit.html | {{ url_for( | templates/{{ url_for( |
| templates/route_schedule_edit.html | {{ url_for( | templates/{{ url_for( |
| templates/route_schedule_edit.html | {{ url_for( | templates/{{ url_for( |
| templates/route_schedule_edit.html | {{ url_for( | templates/{{ url_for( |
| templates/trip_report.html | /seats | seats |
| templates/trip_report.html | /rapor-arsiv | rapor-arsiv |
| templates/trip_report.html | ${it.view} | templates/${it.view} |
| templates/trip_report.html | ${it.txt} | templates/${it.txt} |
| templates/trip_report.html | ${it.csv} | templates/${it.csv} |
| templates/report_archive.html | {{ it.view }} | templates/{{ it.view }} |
| templates/report_archive.html | {{ it.txt }} | templates/{{ it.txt }} |
| templates/report_archive.html | {{ it.csv }} | templates/{{ it.csv }} |
| templates/report_archive.html | {{ it.json }} | templates/{{ it.json }} |
| templates/report_archive.html | /ayarlar | ayarlar |
| templates/rehber.html | {{ url_for( | templates/{{ url_for( |
| templates/rehber.html | {{ url_for( | templates/{{ url_for( |
| templates/rehber.html | {{ url_for( | templates/{{ url_for( |
| templates/rehber.html | {{ url_for( | templates/{{ url_for( |
| templates/rehber.html | {{ url_for( | templates/{{ url_for( |
| templates/rehber.html | {{ url_for( | templates/{{ url_for( |
| templates/rehber.html | {{ url_for( | templates/{{ url_for( |
| templates/rehber.html | {{ url_for( | templates/{{ url_for( |
| templates/rehber.html | {{ url_for( | templates/{{ url_for( |
| templates/rehber.html | {{ url_for( | templates/{{ url_for( |
| templates/rehber.html | {{ url_for( | templates/{{ url_for( |
| templates/rehber.html | {{ url_for( | templates/{{ url_for( |
| templates/rehber.html | url_for static: img/rehber-koltuk-yonetimi-card.png | static/img/rehber-koltuk-yonetimi-card.png |
| templates/rehber.html | url_for static: img/rehber-durak-akisi.png | static/img/rehber-durak-akisi.png |
| templates/rehber.html | url_for static: img/rehber-voice-command.png | static/img/rehber-voice-command.png |
| templates/settings_password.html | /ayarlar | ayarlar |
| templates/settings_password.html | /ayarlar | ayarlar |
| templates/live_map.html | {{ url_for( | templates/{{ url_for( |
| templates/live_map.html | {{ url_for( | templates/{{ url_for( |
| templates/live_map.html | {{ url_for( | templates/{{ url_for( |
| templates/live_map.html | {{ url_for( | templates/{{ url_for( |
| templates/live_map.html | {{ url_for( | templates/{{ url_for( |
| templates/live_map.html | {{ url_for( | templates/{{ url_for( |
| templates/live_map.html | /seats | seats |
| templates/settings_recovery.html | /ayarlar | ayarlar |
| templates/settings_recovery.html | /ayarlar | ayarlar |
| templates/settings_recovery.html | /ayarlar | ayarlar |
| templates/forgot_password.html | /login | login |
| templates/setup_done.html | /login | login |
| templates/settings_profile.html | {{ profile.photo_path }} | templates/{{ profile.photo_path }} |
| templates/settings_profile.html | /ayarlar | ayarlar |
| templates/settings_profile.html | /ayarlar | ayarlar |
| templates/settings_backup.html | /ayarlar/yedekleme/indir/{{ it.name }} | ayarlar/yedekleme/indir/{{ it.name }} |
| templates/settings_backup.html | /ayarlar | ayarlar |
| templates/settings_subscription.html | /ayarlar/paket-talepleri | ayarlar/paket-talepleri |
| templates/settings_subscription.html | /ayarlar | ayarlar |
| templates/subscription_required.html | /ayarlar/abonelik | ayarlar/abonelik |
| templates/package_required.html | /ayarlar/abonelik | ayarlar/abonelik |
| templates/onboarding.html | /kurulum | kurulum |
| templates/continue_trip.html | {{ url_for( | templates/{{ url_for( |
| templates/continue_trip.html | {{ url_for( | templates/{{ url_for( |
| templates/continue_trip.html | {{ url_for( | templates/{{ url_for( |
| templates/continue_trip.html | {{ url_for( | templates/{{ url_for( |
| templates/continue_trip.html | {{ url_for( | templates/{{ url_for( |
| templates/continue_trip.html | {{ url_for( | templates/{{ url_for( |
| templates/continue_trip.html | {{ url_for( | templates/{{ url_for( |
| templates/continue_trip.html | {{ url_for( | templates/{{ url_for( |
| templates/continue_trip.html | {{ url_for( | templates/{{ url_for( |
| templates/continue_trip.html | {{ url_for( | templates/{{ url_for( |
| templates/continue_trip.html | {{ url_for( | templates/{{ url_for( |
| templates/settings_package_requests.html | /ayarlar | ayarlar |
| templates/no_active_trip.html | {{ action_url }} | templates/{{ action_url }} |
| templates/no_active_trip.html | {{ home_url }} | templates/{{ home_url }} |
| templates/user_reset.html | /login | login |
| backups/apk_sync_20260520_234501/seats.html | {{ url_for( | backups/apk_sync_20260520_234501/{{ url_for( |
| backups/apk_sync_20260520_234501/seats.html | {{ url_for( | backups/apk_sync_20260520_234501/{{ url_for( |
| backups/apk_sync_20260520_234501/seats.html | {{ url_for( | backups/apk_sync_20260520_234501/{{ url_for( |
| backups/apk_sync_20260520_234501/seats.html | /ai-console | ai-console |
| backups/apk_sync_20260520_234501/seats.html | /ai-console | ai-console |
| backups/apk_sync_20260520_234501/seats.html | /end_trip | end_trip |
| backups/apk_sync_20260520_234501/seats.html | {{ url_for( | backups/apk_sync_20260520_234501/{{ url_for( |
| backups/apk_sync_20260520_234501/seats.html | {{ url_for( | backups/apk_sync_20260520_234501/{{ url_for( |
| backups/apk_sync_20260520_234501/seats.html | {{ url_for( | backups/apk_sync_20260520_234501/{{ url_for( |
| backups/apk_sync_20260520_234501/trip_report.html | /seats | seats |
| backups/apk_sync_20260520_234501/trip_report.html | /rapor-arsiv | rapor-arsiv |
| backups/apk_sync_20260520_234501/trip_report.html | ${it.view} | backups/apk_sync_20260520_234501/${it.view} |
| backups/apk_sync_20260520_234501/trip_report.html | ${it.txt} | backups/apk_sync_20260520_234501/${it.txt} |
| backups/apk_sync_20260520_234501/trip_report.html | ${it.csv} | backups/apk_sync_20260520_234501/${it.csv} |
| android_app/app/src/main/python/templates/base.html | {{ url_for( | android_app/app/src/main/python/templates/{{ url_for( |
| android_app/app/src/main/python/templates/base.html | {{ url_for( | android_app/app/src/main/python/templates/{{ url_for( |
| android_app/app/src/main/python/templates/base.html | {{ url_for( | android_app/app/src/main/python/templates/{{ url_for( |
| android_app/app/src/main/python/templates/base.html | {{ url_for( | android_app/app/src/main/python/templates/{{ url_for( |

## 6) Referans Verilmeyen Static Dosyalar

Bu liste tehlikelidir: JS dinamik çağırıyor olabilir. Direkt silinmez.

### Uzantı dağılımı
| Uzantı | Adet |
| --- | --- |
| .css | 12 |
| .jpg | 5 |
| .json | 2 |
| .png | 2 |
| .bak_bottom_final_20260513_164512 | 2 |
| .bak_clean_start_20260513_185013 | 2 |
| .bak_map_ui_final_20260513_165054 | 2 |
| .bak_next_ops_drag_20260513_174215 | 2 |
| .bak_next_ops_final_20260513_172822 | 2 |
| .bak_remove_compass_20260513_165759 | 2 |
| .bak_before_clean_speed_split_leftover_20260516_151647 | 2 |
| .bak_before_corrective_restore_20260516_151536 | 2 |
| .bak_before_exact_113619_restore_20260516_153946 | 2 |
| .disabled_20260523_094130 | 2 |
| .bak_force_always | 2 |
| .bak_full_scroll_fix | 2 |
| .bak_marquee_clean_final | 2 |
| .bak_marquee_readable | 2 |
| .bak_marquee_single_clean | 2 |
| .bak_marquee_total_cleanup | 2 |
| .bak_ticker_fix | 2 |
| .bak_tv_marquee_real | 2 |
| .bak_km_distance_20260523_134050 | 1 |
| .bak_no_flicker_20260523_130647 | 1 |
| .bak_collapsible_20260523_133213 | 1 |
| .bak_name_km_20260523_134050 | 1 |
| .bak_diag_collapsible_20260523_133213 | 1 |
| .bak_live_diag_20260523_132945 | 1 |
| .bak_map_overlay_20260523_140732 | 1 |
| .bak_parts_20260523_144047 | 1 |
| .bak_bag_emanet_clean_20260523_130105 | 1 |
| .bak_accept_alibeykoy_gebze_yss_20260518_000238 | 1 |
| .bak_akhisar_balikesir_d565_20260517_103807 | 1 |
| .bak_ant_ist_20260517_094613 | 1 |
| .bak_before_rollback_accept_alibeykoy_gebze_yss_20260518_001320 | 1 |
| .bak_before_rollback_salihli_akhisar_via_20260517_100817 | 1 |
| .bak_before_rollback_salihli_correct_turn_20260517_102155 | 1 |
| .bak_before_rollback_salihli_pin_d555_20260517_101430 | 1 |
| .bak_before_rollback_tuzla_segments_20260517_111533 | 1 |
| .bak_build_denizli_istanbul_20260520_122020 | 1 |

### İlk 160 kayıt
| Static dosya | Byte | Uzantı |
| --- | --- | --- |
| static/continue/continue_flow_refresh.js.bak_km_distance_20260523_134050 | 8724 | .bak_km_distance_20260523_134050 |
| static/continue/continue_flow_refresh.js.bak_no_flicker_20260523_130647 | 7655 | .bak_no_flicker_20260523_130647 |
| static/continue/continue_live_diagnostics.js.bak_collapsible_20260523_133213 | 6169 | .bak_collapsible_20260523_133213 |
| static/continue/continue_live_diagnostics.js.bak_name_km_20260523_134050 | 7941 | .bak_name_km_20260523_134050 |
| static/continue/continue_trip.css.bak_diag_collapsible_20260523_133213 | 83914 | .bak_diag_collapsible_20260523_133213 |
| static/continue/continue_trip.css.bak_live_diag_20260523_132945 | 81776 | .bak_live_diag_20260523_132945 |
| static/continue/continue_trip.css.bak_map_overlay_20260523_140732 | 84753 | .bak_map_overlay_20260523_140732 |
| static/continue/continue_trip.css.bak_parts_20260523_144047 | 84753 | .bak_parts_20260523_144047 |
| static/continue/continue_trip_core.js.bak_bag_emanet_clean_20260523_130105 | 66766 | .bak_bag_emanet_clean_20260523_130105 |
| static/continue/css_parts/00-base-legacy.css | 19974 | .css |
| static/continue/css_parts/10-compact-timeline-hero.css | 16409 | .css |
| static/continue/css_parts/20-live-stop-sheet-base.css | 6576 | .css |
| static/continue/css_parts/30-sheet-bag-photo.css | 13474 | .css |
| static/continue/css_parts/40-cargo-gender-summary.css | 9930 | .css |
| static/continue/css_parts/50-live-v2-top-glow.css | 15130 | .css |
| static/continue/css_parts/60-live-diagnostics.css | 2976 | .css |
| static/data/route_profile_segments.json | 258317 | .json |
| static/data/route_segments.json | 2138381 | .json |
| static/data/route_segments.json.bak_accept_alibeykoy_gebze_yss_20260518_000238 | 3544583 | .bak_accept_alibeykoy_gebze_yss_20260518_000238 |
| static/data/route_segments.json.bak_akhisar_balikesir_d565_20260517_103807 | 1771202 | .bak_akhisar_balikesir_d565_20260517_103807 |
| static/data/route_segments.json.bak_ant_ist_20260517_094613 | 481930 | .bak_ant_ist_20260517_094613 |
| static/data/route_segments.json.bak_before_rollback_accept_alibeykoy_gebze_yss_20260518_001320 | 3132577 | .bak_before_rollback_accept_alibeykoy_gebze_yss_20260518_001320 |
| static/data/route_segments.json.bak_before_rollback_salihli_akhisar_via_20260517_100817 | 1771210 | .bak_before_rollback_salihli_akhisar_via_20260517_100817 |
| static/data/route_segments.json.bak_before_rollback_salihli_correct_turn_20260517_102155 | 1767779 | .bak_before_rollback_salihli_correct_turn_20260517_102155 |
| static/data/route_segments.json.bak_before_rollback_salihli_pin_d555_20260517_101430 | 1767776 | .bak_before_rollback_salihli_pin_d555_20260517_101430 |
| static/data/route_segments.json.bak_before_rollback_tuzla_segments_20260517_111533 | 790747 | .bak_before_rollback_tuzla_segments_20260517_111533 |
| static/data/route_segments.json.bak_build_denizli_istanbul_20260520_122020 | 3544583 | .bak_build_denizli_istanbul_20260520_122020 |
| static/data/route_segments.json.bak_denizli_korkuteli_segments_20260517_144319 | 2368645 | .bak_denizli_korkuteli_segments_20260517_144319 |
| static/data/route_segments.json.bak_fix_alibeykoy_gebze_short_yss_20260517_235959 | 3544583 | .bak_fix_alibeykoy_gebze_short_yss_20260517_235959 |
| static/data/route_segments.json.bak_force_ist_ant_yss_route_20260517_234658 | 2362611 | .bak_force_ist_ant_yss_route_20260517_234658 |
| static/data/route_segments.json.bak_ist_ant_alibeykoy_gebze_yss_extra2_20260517_235604 | 3537181 | .bak_ist_ant_alibeykoy_gebze_yss_extra2_20260517_235604 |
| static/data/route_segments.json.bak_ist_ant_alibeykoy_gebze_yss_extra_20260517_235252 | 3463743 | .bak_ist_ant_alibeykoy_gebze_yss_extra_20260517_235252 |
| static/data/route_segments.json.bak_ist_ant_manisa_route_20260517_233207 | 2480965 | .bak_ist_ant_manisa_route_20260517_233207 |
| static/data/route_segments.json.bak_ist_ant_refresh_segments_20260517_144738 | 2368645 | .bak_ist_ant_refresh_segments_20260517_144738 |
| static/data/route_segments.json.bak_istanbul_antalya_yss_20260517_141115 | 2441086 | .bak_istanbul_antalya_yss_20260517_141115 |
| static/data/route_segments.json.bak_korkuteli_elmali_segments_20260517_143312 | 2368645 | .bak_korkuteli_elmali_segments_20260517_143312 |
| static/data/route_segments.json.bak_rebuild_denizli_istanbul_20260520_122635 | 1860939 | .bak_rebuild_denizli_istanbul_20260520_122635 |
| static/data/route_segments.json.bak_refresh_new_coords_segments_20260517_143857 | 2368645 | .bak_refresh_new_coords_segments_20260517_143857 |
| static/data/route_segments.json.bak_restore_denizli_istanbul_from_reverse_20260521_000121 | 2135441 | .bak_restore_denizli_istanbul_from_reverse_20260521_000121 |
| static/data/route_segments.json.bak_reverse_ist_ant_20260517_140145 | 1756223 | .bak_reverse_ist_ant_20260517_140145 |
| static/data/route_segments.json.bak_reverse_to_istanbul_denizli_20260520_123746 | 1859812 | .bak_reverse_to_istanbul_denizli_20260520_123746 |
| static/data/route_segments.json.bak_salihli_akhisar_via_d555_20260517_100121 | 1767215 | .bak_salihli_akhisar_via_d555_20260517_100121 |
| static/data/route_segments.json.bak_salihli_akhisar_via_points_20260517_100608 | 1771202 | .bak_salihli_akhisar_via_points_20260517_100608 |
| static/data/route_segments.json.bak_salihli_correct_turn_20260517_101854 | 1771202 | .bak_salihli_correct_turn_20260517_101854 |
| static/data/route_segments.json.bak_salihli_pin_d555_fix_20260517_101253 | 1771202 | .bak_salihli_pin_d555_fix_20260517_101253 |
| static/data/route_segments.json.bak_tuzla_refresh_20260517_112331 | 1767425 | .bak_tuzla_refresh_20260517_112331 |
| static/data/route_segments.json.bak_tuzla_segments_redraw_fix_20260517_112456 | 1767425 | .bak_tuzla_segments_redraw_fix_20260517_112456 |
| static/img/drive-mode-card.png | 1737741 | .png |
| static/img/home-bus-card.jpg | 282490 | .jpg |
| static/img/home-seat-card.jpg | 269291 | .jpg |
| static/img/menu-seat-card.png | 579671 | .png |
| static/img/onboarding/README.txt | 514 | .txt |
| static/img/seat-card.jpg | 240314 | .jpg |
| static/live_map/muavin_live_map_extra.css.bak_bottom_final_20260513_164512 | 37340 | .bak_bottom_final_20260513_164512 |
| static/live_map/muavin_live_map_extra.css.bak_clean_dock_visible_20260513_185554 | 37653 | .bak_clean_dock_visible_20260513_185554 |
| static/live_map/muavin_live_map_extra.css.bak_clean_fullscreen_20260513_185236 | 35789 | .bak_clean_fullscreen_20260513_185236 |
| static/live_map/muavin_live_map_extra.css.bak_clean_hide_km_20260513_190426 | 39080 | .bak_clean_hide_km_20260513_190426 |
| static/live_map/muavin_live_map_extra.css.bak_clean_location_visible_20260513_190610 | 40242 | .bak_clean_location_visible_20260513_190610 |
| static/live_map/muavin_live_map_extra.css.bak_clean_speed_visible_20260513_190933 | 42042 | .bak_clean_speed_visible_20260513_190933 |
| static/live_map/muavin_live_map_extra.css.bak_clean_start_20260513_185013 | 33506 | .bak_clean_start_20260513_185013 |
| static/live_map/muavin_live_map_extra.css.bak_map_ui_final_20260513_165054 | 32648 | .bak_map_ui_final_20260513_165054 |
| static/live_map/muavin_live_map_extra.css.bak_next_ops_bubble_20260513_174004 | 24071 | .bak_next_ops_bubble_20260513_174004 |
| static/live_map/muavin_live_map_extra.css.bak_next_ops_drag_20260513_174215 | 28388 | .bak_next_ops_drag_20260513_174215 |
| static/live_map/muavin_live_map_extra.css.bak_next_ops_final_20260513_172822 | 17372 | .bak_next_ops_final_20260513_172822 |
| static/live_map/muavin_live_map_extra.css.bak_next_ops_polish_20260513_173333 | 21527 | .bak_next_ops_polish_20260513_173333 |
| static/live_map/muavin_live_map_extra.css.bak_remove_compass_20260513_165759 | 16945 | .bak_remove_compass_20260513_165759 |
| static/live_map/muavin_live_map_extra.css.bak_remove_old_blue_v1_20260513_191843 | 44326 | .bak_remove_old_blue_v1_20260513_191843 |
| static/live_map/muavin_live_map_extra.css.bak_small_buttons_20260513_174403 | 29079 | .bak_small_buttons_20260513_174403 |
| static/live_map/muavin_live_map_extra.js.bak_bottom_final_20260513_164512 | 77370 | .bak_bottom_final_20260513_164512 |
| static/live_map/muavin_live_map_extra.js.bak_button_bridge_20260523_141312 | 57832 | .bak_button_bridge_20260523_141312 |
| static/live_map/muavin_live_map_extra.js.bak_clean_start_20260513_185013 | 54832 | .bak_clean_start_20260513_185013 |
| static/live_map/muavin_live_map_extra.js.bak_map_ui_final_20260513_165054 | 63896 | .bak_map_ui_final_20260513_165054 |
| static/live_map/muavin_live_map_extra.js.bak_next_ops_drag_20260513_174215 | 48818 | .bak_next_ops_drag_20260513_174215 |
| static/live_map/muavin_live_map_extra.js.bak_next_ops_final_20260513_172822 | 41383 | .bak_next_ops_final_20260513_172822 |
| static/live_map/muavin_live_map_extra.js.bak_remove_compass_20260513_165759 | 40400 | .bak_remove_compass_20260513_165759 |
| static/profile/admin_profile_4f864f2df139.jpg | 271828 | .jpg |
| static/profile/admin_profile_6a6400ae12c1.jpg | 775993 | .jpg |
| static/seats/_archive_theme_trials/seats-dashboard-final.css | 18430 | .css |
| static/seats/_archive_theme_trials/seats-dashboard-tone.css | 5303 | .css |
| static/seats/drive-controls.js.bak_before_clean_speed_split_leftover_20260516_151647 | 7542 | .bak_before_clean_speed_split_leftover_20260516_151647 |
| static/seats/drive-controls.js.bak_before_corrective_restore_20260516_151536 | 7959 | .bak_before_corrective_restore_20260516_151536 |
| static/seats/drive-controls.js.bak_before_exact_113619_restore_20260516_153946 | 7542 | .bak_before_exact_113619_restore_20260516_153946 |
| static/seats/drive-controls.js.bak_before_fix_bad_voice_rollback_20260516_150609 | 7542 | .bak_before_fix_bad_voice_rollback_20260516_150609 |
| static/seats/drive-controls.js.bak_before_restore_12_checkpoint_20260516_153518 | 7542 | .bak_before_restore_12_checkpoint_20260516_153518 |
| static/seats/drive-controls.js.bak_before_restore_from_20260516_145319_20260516_151331 | 7543 | .bak_before_restore_from_20260516_145319_20260516_151331 |
| static/seats/drive-controls.js.bak_before_restore_natural_total_checkpoint_20260516_152438 | 7542 | .bak_before_restore_natural_total_checkpoint_20260516_152438 |
| static/seats/drive-controls.js.bak_before_restore_previous_20260516_150549 | 7959 | .bak_before_restore_previous_20260516_150549 |
| static/seats/drive-controls.js.bak_before_rollback_exact_113619_20260516_154139 | 7542 | .bak_before_rollback_exact_113619_20260516_154139 |
| static/seats/drive-controls.js.bak_before_voice_mass_rollback_20260516_150355 | 7542 | .bak_before_voice_mass_rollback_20260516_150355 |
| static/seats/drive-controls.js.bak_drive_toggle_fix | 7564 | .bak_drive_toggle_fix |
| static/seats/drive-controls.js.bak_force_repair_20260516_145319 | 7959 | .bak_force_repair_20260516_145319 |
| static/seats/drive-controls.js.bak_hard_line_repair_20260516_145608 | 7959 | .bak_hard_line_repair_20260516_145608 |
| static/seats/drive-controls.js.bak_hard_repair_voice_block_20260516_145427 | 7959 | .bak_hard_repair_voice_block_20260516_145427 |
| static/seats/drive-controls.js.bak_repair_voice_block_20260516_133452 | 7959 | .bak_repair_voice_block_20260516_133452 |
| static/seats/drive-controls.js.bak_voice_owner_fix | 6642 | .bak_voice_owner_fix |
| static/seats/patches/_disabled/seat-bottom-fab-54-final.css.disabled_20260523_085109 | 3056 | .disabled_20260523_085109 |
| static/seats/patches/bottom-row-51-54-equal-spacing.css | 489 | .css |
| static/seats/patches/live-flow-v2.css.disabled_20260523_094130 | 12660 | .disabled_20260523_094130 |
| static/seats/patches/live-flow-v2.js.disabled_20260523_094130 | 10817 | .disabled_20260523_094130 |
| static/seats/patches/mobile-performance-fix.css.bak_modal_readability_20260518_181100 | 2498 | .bak_modal_readability_20260518_181100 |
| static/seats/patches/only-54-reapply-right-shift.css | 955 | .css |
| static/seats/patches/right-seat-column-spacing-fix.css | 1100 | .css |
| static/seats/patches/stop-flow-focus-patch.js.bak_before_rollback_20260520_103515 | 18400 | .bak_before_rollback_20260520_103515 |
| static/seats/patches/stop-flow-focus-patch.js.bak_live_runtime_sync_20260520_103326 | 10723 | .bak_live_runtime_sync_20260520_103326 |
| static/seats/patches/stop-flow-focus-patch.js.bak_scope_simple_only_20260520_105358 | 10723 | .bak_scope_simple_only_20260520_105358 |
| static/seats/patches/stop-flow-focus-patch.js.bak_simple_scope_20260520_110612 | 10723 | .bak_simple_scope_20260520_110612 |
| static/seats/patches/unified-seat-deck-report-style.css.bak_before_remove_label_balance_20260521_212125 | 16978 | .bak_before_remove_label_balance_20260521_212125 |
| static/seats/patches/unified-seat-deck-report-style.css.bak_gap_20260521_211630 | 11421 | .bak_gap_20260521_211630 |
| static/seats/patches/unified-seat-deck-report-style.css.bak_label_balance_20260521_212035 | 15244 | .bak_label_balance_20260521_212035 |
| static/seats/patches/unified-seat-deck-report-style.css.bak_labels_20260521_211435 | 9049 | .bak_labels_20260521_211435 |
| static/seats/patches/unified-seat-deck-report-style.css.bak_remove_smaller_20260521_212205 | 15246 | .bak_remove_smaller_20260521_212205 |
| static/seats/patches/unified-seat-deck-report-style.css.bak_remove_smaller_20260521_212211 | 12695 | .bak_remove_smaller_20260521_212211 |
| static/seats/patches/unified-seat-deck-report-style.css.bak_remove_smaller_20260521_212306 | 12695 | .bak_remove_smaller_20260521_212306 |
| static/seats/patches/unified-seat-deck-report-style.css.bak_remove_smaller_20260521_212310 | 12695 | .bak_remove_smaller_20260521_212310 |
| static/seats/patches/unified-seat-deck-report-style.css.bak_smaller_20260521_211902 | 12693 | .bak_smaller_20260521_211902 |
| static/seats/route-marquee.js.bak_force_always | 2928 | .bak_force_always |
| static/seats/route-marquee.js.bak_full_scroll_fix | 1848 | .bak_full_scroll_fix |
| static/seats/route-marquee.js.bak_marquee_clean_final | 2798 | .bak_marquee_clean_final |
| static/seats/route-marquee.js.bak_marquee_readable | 2231 | .bak_marquee_readable |
| static/seats/route-marquee.js.bak_marquee_single_clean | 2276 | .bak_marquee_single_clean |
| static/seats/route-marquee.js.bak_marquee_total_cleanup | 2009 | .bak_marquee_total_cleanup |
| static/seats/route-marquee.js.bak_ticker_fix | 2090 | .bak_ticker_fix |
| static/seats/route-marquee.js.bak_tv_marquee_real | 1444 | .bak_tv_marquee_real |
| static/seats/seats-dashboard-final.css.bak_tone | 18430 | .bak_tone |
| static/seats/seats-final.css.bak_bottom_legend_fixed_final | 59871 | .bak_bottom_legend_fixed_final |
| static/seats/seats-final.css.bak_clean_marquee_final | 45650 | .bak_clean_marquee_final |
| static/seats/seats-final.css.bak_drive_actions_route_top | 62888 | .bak_drive_actions_route_top |
| static/seats/seats-final.css.bak_drive_actions_top | 59765 | .bak_drive_actions_top |
| static/seats/seats-final.css.bak_drive_fab_final | 25105 | .bak_drive_fab_final |
| static/seats/seats-final.css.bak_drive_premium_screen_v1 | 25107 | .bak_drive_premium_screen_v1 |
| static/seats/seats-final.css.bak_drive_top_clean_final | 28419 | .bak_drive_top_clean_final |
| static/seats/seats-final.css.bak_drive_voice_clean_single | 61899 | .bak_drive_voice_clean_single |
| static/seats/seats-final.css.bak_drive_voice_clone_row | 63589 | .bak_drive_voice_clone_row |
| static/seats/seats-final.css.bak_drive_voice_equal_clean | 63589 | .bak_drive_voice_equal_clean |
| static/seats/seats-final.css.bak_drive_voice_id | 61900 | .bak_drive_voice_id |
| static/seats/seats-final.css.bak_drive_voice_only_final | 65516 | .bak_drive_voice_only_final |
| static/seats/seats-final.css.bak_drive_voice_only_rollback | 64652 | .bak_drive_voice_only_rollback |
| static/seats/seats-final.css.bak_drive_voice_separat | 61899 | .bak_drive_voice_separat |
| static/seats/seats-final.css.bak_drive_voice_width_only | 61899 | .bak_drive_voice_width_only |
| static/seats/seats-final.css.bak_fixed_bottom_legend | 57082 | .bak_fixed_bottom_legend |
| static/seats/seats-final.css.bak_force_always | 46405 | .bak_force_always |
| static/seats/seats-final.css.bak_full_scroll_fix | 46499 | .bak_full_scroll_fix |
| static/seats/seats-final.css.bak_hide_legend_row | 56798 | .bak_hide_legend_row |
| static/seats/seats-final.css.bak_legend_conflict_clean | 62916 | .bak_legend_conflict_clean |
| static/seats/seats-final.css.bak_legend_lift_fix | 59766 | .bak_legend_lift_fix |
| static/seats/seats-final.css.bak_live_danger_restore | 30966 | .bak_live_danger_restore |
| static/seats/seats-final.css.bak_live_dot_position_fix | 42657 | .bak_live_dot_position_fix |
| static/seats/seats-final.css.bak_live_pill_dot | 41879 | .bak_live_pill_dot |
| static/seats/seats-final.css.bak_live_pill_red_text | 45946 | .bak_live_pill_red_text |
| static/seats/seats-final.css.bak_marquee_clean_final | 54312 | .bak_marquee_clean_final |
| static/seats/seats-final.css.bak_marquee_cleanup | 56807 | .bak_marquee_cleanup |
| static/seats/seats-final.css.bak_marquee_conflict_cleanup | 49959 | .bak_marquee_conflict_cleanup |
| static/seats/seats-final.css.bak_marquee_final | 52046 | .bak_marquee_final |
| static/seats/seats-final.css.bak_marquee_readable | 47658 | .bak_marquee_readable |
| static/seats/seats-final.css.bak_marquee_single_clean | 47185 | .bak_marquee_single_clean |
| static/seats/seats-final.css.bak_marquee_total_cleanup | 50400 | .bak_marquee_total_cleanup |
| static/seats/seats-final.css.bak_next_pill_orange | 47326 | .bak_next_pill_orange |
| static/seats/seats-final.css.bak_normal_pin_bright | 35117 | .bak_normal_pin_bright |
| static/seats/seats-final.css.bak_normal_route_pin | 33224 | .bak_normal_route_pin |
| static/seats/seats-final.css.bak_rollback_drive_fab_top | 28331 | .bak_rollback_drive_fab_top |

## 7) Backup / Eski / Test Adayları

### Ana klasöre göre dağılım
| Klasör | Adet |
| --- | --- |
| android_app | 200 |

### Uzantıya göre dağılım
| Uzantı | Adet |
| --- | --- |
| .bak_sync_continue_20260523_142710 | 6 |
| .bak_port_guard_20260530_104842 | 2 |
| .bak_sync_20260520_113916 | 2 |
| .bak_bottom_final_20260513_164512 | 2 |
| .bak_clean_start_20260513_185013 | 2 |
| .bak_final_apk_20260513_192149 | 2 |
| .bak_map_ui_final_20260513_165054 | 2 |
| .bak_next_ops_drag_20260513_174215 | 2 |
| .bak_next_ops_final_20260513_172822 | 2 |
| .bak_remove_compass_20260513_165759 | 2 |
| .bak_before_clean_speed_split_leftover_20260516_151647 | 2 |
| .bak_before_corrective_restore_20260516_151536 | 2 |
| .bak_before_exact_113619_restore_20260516_153946 | 2 |
| .bak_before_fix_bad_voice_rollback_20260516_150609 | 2 |
| .bak_before_restore_12_checkpoint_20260516_153518 | 2 |
| .bak_before_restore_from_20260516_145319_20260516_151331 | 2 |
| .bak_before_restore_natural_total_checkpoint_20260516_152438 | 2 |
| .bak_before_restore_previous_20260516_150549 | 2 |
| .bak_before_rollback_exact_113619_20260516_154139 | 2 |
| .bak_force_always | 2 |
| .bak_full_scroll_fix | 2 |
| .bak_marquee_clean_final | 2 |
| .bak_marquee_readable | 2 |
| .bak_marquee_single_clean | 2 |
| .bak_marquee_total_cleanup | 2 |
| .bak_ticker_fix | 2 |
| .bak_tv_marquee_real | 2 |
| .bak_bind_printbridge_real | 1 |
| .bak_geolocation_patch | 1 |
| .bak_print_bridge | 1 |
| .bak_print_debug | 1 |
| .bak_tts_bridge | 1 |
| .bak_webview_scheme_fix | 1 |
| .bak_continue_route_sync_20260523_143011 | 1 |
| .py | 1 |
| .bak_events_sums_fix | 1 |
| .bak_seat_destination_change_20260520_231815 | 1 |
| .bak_report_change_payload_20260520_233720 | 1 |
| .bak_report_destination_change_20260520_232729 | 1 |
| .bak_coords_sync_20260518_184401 | 1 |

### En büyük 120 backup/eski/test adayı
| Dosya | Byte | Satır |
| --- | --- | --- |
| android_app/app/src/main/python/static/data/route_segments.json.bak_accept_alibeykoy_gebze_yss_20260518_000238 | 3544583 | None |
| android_app/app/src/main/python/static/data/route_segments.json.bak_build_denizli_istanbul_20260520_122020 | 3544583 | None |
| android_app/app/src/main/python/static/data/route_segments.json.bak_fix_alibeykoy_gebze_short_yss_20260517_235959 | 3544583 | None |
| android_app/app/src/main/python/static/data/route_segments.json.bak_ist_ant_alibeykoy_gebze_yss_extra2_20260517_235604 | 3537181 | None |
| android_app/app/src/main/python/static/data/route_segments.json.bak_ist_ant_alibeykoy_gebze_yss_extra_20260517_235252 | 3463743 | None |
| android_app/app/src/main/python/static/data/route_segments.json.bak_before_rollback_accept_alibeykoy_gebze_yss_20260518_001320 | 3132577 | None |
| android_app/app/src/main/python/static/data/route_segments.json.bak_ist_ant_manisa_route_20260517_233207 | 2480965 | None |
| android_app/app/src/main/python/static/data/route_segments.json.bak_istanbul_antalya_yss_20260517_141115 | 2441086 | None |
| android_app/app/src/main/python/static/data/route_segments.json.bak_denizli_korkuteli_segments_20260517_144319 | 2368645 | None |
| android_app/app/src/main/python/static/data/route_segments.json.bak_ist_ant_refresh_segments_20260517_144738 | 2368645 | None |
| android_app/app/src/main/python/static/data/route_segments.json.bak_korkuteli_elmali_segments_20260517_143312 | 2368645 | None |
| android_app/app/src/main/python/static/data/route_segments.json.bak_refresh_new_coords_segments_20260517_143857 | 2368645 | None |
| android_app/app/src/main/python/static/data/route_segments.json.bak_force_ist_ant_yss_route_20260517_234658 | 2362611 | None |
| android_app/app/src/main/python/static/data/route_segments.json.bak_restore_denizli_istanbul_from_reverse_20260521_000121 | 2135441 | None |
| android_app/app/src/main/python/static/data/route_segments.json.bak_rebuild_denizli_istanbul_20260520_122635 | 1860939 | None |
| android_app/app/src/main/python/static/data/route_segments.json.bak_reverse_to_istanbul_denizli_20260520_123746 | 1859812 | None |
| android_app/app/src/main/python/static/data/route_segments.json.bak_before_rollback_salihli_akhisar_via_20260517_100817 | 1771210 | None |
| android_app/app/src/main/python/static/data/route_segments.json.bak_akhisar_balikesir_d565_20260517_103807 | 1771202 | None |
| android_app/app/src/main/python/static/data/route_segments.json.bak_salihli_akhisar_via_points_20260517_100608 | 1771202 | None |
| android_app/app/src/main/python/static/data/route_segments.json.bak_salihli_correct_turn_20260517_101854 | 1771202 | None |
| android_app/app/src/main/python/static/data/route_segments.json.bak_salihli_pin_d555_fix_20260517_101253 | 1771202 | None |
| android_app/app/src/main/python/static/data/route_segments.json.bak_before_rollback_salihli_correct_turn_20260517_102155 | 1767779 | None |
| android_app/app/src/main/python/static/data/route_segments.json.bak_before_rollback_salihli_pin_d555_20260517_101430 | 1767776 | None |
| android_app/app/src/main/python/static/data/route_segments.json.bak_tuzla_refresh_20260517_112331 | 1767425 | None |
| android_app/app/src/main/python/static/data/route_segments.json.bak_tuzla_segments_redraw_fix_20260517_112456 | 1767425 | None |
| android_app/app/src/main/python/static/data/route_segments.json.bak_salihli_akhisar_via_d555_20260517_100121 | 1767215 | None |
| android_app/app/src/main/python/static/data/route_segments.json.bak_reverse_ist_ant_20260517_140145 | 1756223 | None |
| android_app/app/src/main/python/static/data/route_segments.json.bak_before_rollback_tuzla_segments_20260517_111533 | 790747 | None |
| android_app/app/src/main/python/seed/db.sqlite3.bak_coords_sync_20260518_184401 | 483328 | None |
| android_app/app/src/main/python/seed/db.sqlite3.bak_route_full_sync_20260518_191613 | 483328 | None |
| android_app/app/src/main/python/static/data/route_segments.json.bak_ant_ist_20260517_094613 | 481930 | None |
| android_app/app/src/main/python/static/data/route_segments.json.bak_geom_sync_20260518_192438 | 257477 | None |
| android_app/app/src/main/python/app.py.bak_continue_route_sync_20260523_143011 | 136113 | None |
| android_app/app/src/main/python/app.py.bak_sync_20260520_113916 | 134501 | None |
| android_app/app/src/main/python/static/seats/seats.css.bak_before_label_rollback | 103706 | None |
| android_app/app/src/main/python/static/seats/seats.css.bak_last_row_tighter_20260516_065700 | 103257 | None |
| android_app/app/src/main/python/static/seats/seats.css.bak_before_seats_final | 102877 | None |
| android_app/app/src/main/python/static/seats/seats.css.bak_last_row_inner_gap_fix_20260516_065535 | 102877 | None |
| android_app/app/src/main/python/static/seats/seats.js.bak_before_rollback_selected_stop_memory_20260518_153528 | 84819 | None |
| android_app/app/src/main/python/static/continue/continue_trip.css.bak_parts_20260523_144047 | 84753 | None |
| android_app/app/src/main/python/static/seats/seats.js.bak_before_rollback_live_stop_core_20260520_104302 | 84662 | None |
| android_app/app/src/main/python/static/seats/seats.js.bak_before_rollback_live_stop_core_20260520_104314 | 84287 | None |
| android_app/app/src/main/python/static/seats/seats.js.bak_before_restore_natural_total_checkpoint_20260516_152438 | 84179 | None |
| android_app/app/src/main/python/static/seats/seats.js.bak_before_clean_speed_split_leftover_20260516_151647 | 84151 | None |
| android_app/app/src/main/python/static/seats/seats.js.bak_before_fix_bad_voice_rollback_20260516_150609 | 84151 | None |
| android_app/app/src/main/python/static/seats/seats.js.bak_before_corrective_restore_20260516_151536 | 84139 | None |
| android_app/app/src/main/python/static/seats/seats.js.bak_before_exact_113619_restore_20260516_153946 | 84139 | None |
| android_app/app/src/main/python/static/seats/seats.js.bak_before_restore_12_checkpoint_20260516_153518 | 84139 | None |
| android_app/app/src/main/python/static/seats/seats.js.bak_before_restore_from_20260516_145319_20260516_151331 | 84139 | None |
| android_app/app/src/main/python/static/seats/seats.js.bak_before_rollback_exact_113619_20260516_154139 | 84139 | None |
| android_app/app/src/main/python/static/seats/seats.js.bak_before_restore_previous_20260516_150549 | 84111 | None |
| android_app/app/src/main/python/static/live_map/muavin_live_map_extra.js.bak_bottom_final_20260513_164512 | 77370 | None |
| android_app/app/src/main/python/static/seats/seats.js.bak_android_tts | 74818 | None |
| android_app/app/src/main/python/static/seats/seats.js.bak_add_continue_trip_coords_helper_final | 74559 | None |
| android_app/app/src/main/python/static/seats/seats.js.bak_add_missing_coords_helper_fix | 74559 | None |
| android_app/app/src/main/python/static/seats/seats.js.bak_append_missing_coords_helper | 74559 | None |
| android_app/app/src/main/python/static/continue/continue_trip.css.bak_map_overlay_20260523_140732 | 73054 | None |
| android_app/app/src/main/python/static/continue/continue_trip.css.bak_sync_continue_20260523_142710 | 73054 | None |
| android_app/app/src/main/python/static/continue/continue_trip.css.bak_diag_collapsible_20260523_133213 | 72215 | None |
| android_app/app/src/main/python/static/continue/continue_trip.css.bak_live_diag_20260523_132945 | 70077 | None |
| android_app/app/src/main/python/static/seats/seats-final.css.bak_voice_conflict_clean | 68186 | None |
| android_app/app/src/main/python/static/seats/seats-final.css.bak_voice_row_spacing_final | 65939 | None |
| android_app/app/src/main/python/static/seats/seats-final.css.bak_drive_voice_only_final | 65516 | None |
| android_app/app/src/main/python/static/seats/seats-final.css.bak_drive_voice_only_rollback | 64652 | None |
| android_app/app/src/main/python/static/live_map/muavin_live_map_extra.js.bak_map_ui_final_20260513_165054 | 63896 | None |
| android_app/app/src/main/python/static/seats/seats-final.css.bak_drive_voice_clone_row | 63589 | None |
| android_app/app/src/main/python/static/seats/seats-final.css.bak_drive_voice_equal_clean | 63589 | None |
| android_app/app/src/main/python/static/seats/seats-final.css.bak_legend_conflict_clean | 62916 | None |
| android_app/app/src/main/python/static/seats/seats-final.css.bak_drive_actions_route_top | 62888 | None |
| android_app/app/src/main/python/static/seats/seats-final.css.bak_drive_voice_id | 61900 | None |
| android_app/app/src/main/python/static/seats/seats-final.css.bak_drive_voice_clean_single | 61899 | None |
| android_app/app/src/main/python/static/seats/seats-final.css.bak_drive_voice_separat | 61899 | None |
| android_app/app/src/main/python/static/seats/seats-final.css.bak_drive_voice_width_only | 61899 | None |
| android_app/app/src/main/python/static/seats/seats-final.css.bak_bottom_legend_fixed_final | 59871 | None |
| android_app/app/src/main/python/static/seats/seats-final.css.bak_legend_lift_fix | 59766 | None |
| android_app/app/src/main/python/static/seats/seats-final.css.bak_drive_actions_top | 59765 | None |
| android_app/app/src/main/python/static/live_map/muavin_live_map_extra.js.bak_button_bridge_20260523_141312 | 57832 | None |
| android_app/app/src/main/python/static/live_map/muavin_live_map_extra.js.bak_final_apk_20260513_192149 | 57832 | None |
| android_app/app/src/main/python/static/seats/seats-final.css.bak_fixed_bottom_legend | 57082 | None |
| android_app/app/src/main/python/static/seats/seats-final.css.bak_marquee_cleanup | 56807 | None |
| android_app/app/src/main/python/static/seats/seats-final.css.bak_hide_legend_row | 56798 | None |
| android_app/app/src/main/python/static/continue/continue_trip_core.js.bak_bag_emanet_clean_20260523_130105 | 56647 | None |
| android_app/app/src/main/python/static/seats/seats-final.css.bak_voice_seat_emoji | 55654 | None |
| android_app/app/src/main/python/static/continue/continue_trip_core.js.bak_sync_continue_20260523_142710 | 55364 | None |
| android_app/app/src/main/python/static/seats/seats-final.css.bak_voice_row_clean_final | 55100 | None |
| android_app/app/src/main/python/static/live_map/muavin_live_map_extra.js.bak_clean_start_20260513_185013 | 54832 | None |
| android_app/app/src/main/python/static/seats/seats-final.css.bak_marquee_clean_final | 54312 | None |
| android_app/app/src/main/python/static/seats/seats-final.css.bak_voice_row_equal_rollback | 53034 | None |
| android_app/app/src/main/python/static/seats/seats-final.css.bak_voice_seat_icon_match | 52943 | None |
| android_app/app/src/main/python/static/seats/seats-final.css.bak_marquee_final | 52046 | None |
| android_app/app/src/main/python/static/seats/seats-final.css.bak_voice_clean_one_final | 51182 | None |
| android_app/app/src/main/python/static/seats/seats-final.css.bak_marquee_total_cleanup | 50400 | None |
| android_app/app/src/main/python/static/seats/seats-final.css.bak_voice_seat_icon_final | 50342 | None |
| android_app/app/src/main/python/static/seats/seats-final.css.bak_marquee_conflict_cleanup | 49959 | None |
| android_app/app/src/main/python/static/seats/seats-final.css.bak_ticker_fix | 49781 | None |
| android_app/app/src/main/python/static/seats/seats-final.css.bak_voice_row_fix_rollback | 49473 | None |
| android_app/app/src/main/python/static/live_map/muavin_live_map_extra.js.bak_next_ops_drag_20260513_174215 | 48818 | None |
| android_app/app/src/main/python/static/seats/seats-final.css.bak_voice_row_equal_counter | 48292 | None |
| android_app/app/src/main/python/static/seats/seats-final.css.bak_voice_row_final_clean | 48292 | None |
| android_app/app/src/main/python/static/seats/seats-final.css.bak_tv_marquee_real | 48087 | None |
| android_app/app/src/main/python/static/seats/seats-final.css.bak_voice_row_equal_final | 47721 | None |
| android_app/app/src/main/python/static/seats/seats-final.css.bak_marquee_readable | 47658 | None |
| android_app/app/src/main/python/static/seats/seats-final.css.bak_next_pill_orange | 47326 | None |
| android_app/app/src/main/python/static/seats/seats-final.css.bak_marquee_single_clean | 47185 | None |
| android_app/app/src/main/python/static/seats/seats-final.css.bak_tv_marquee_fix | 46637 | None |
| android_app/app/src/main/python/static/seats/seats-final.css.bak_full_scroll_fix | 46499 | None |
| android_app/app/src/main/python/static/seats/seats-final.css.bak_force_always | 46405 | None |
| android_app/app/src/main/python/static/seats/seats-final.css.bak_live_pill_red_text | 45946 | None |
| android_app/app/src/main/python/static/seats/seats-final.css.bak_clean_marquee_final | 45650 | None |
| android_app/app/src/main/python/static/seats/seats-final.css.bak_route_marquee | 45123 | None |
| android_app/app/src/main/python/static/live_map/muavin_live_map_extra.css.bak_remove_old_blue_v1_20260513_191843 | 44326 | None |
| android_app/app/src/main/python/static/seats/seats-final.css.bak_route_pill_bg_boost | 43545 | None |
| android_app/app/src/main/python/static/seats/seats-final.css.bak_live_dot_position_fix | 42657 | None |
| android_app/app/src/main/python/static/live_map/muavin_live_map_extra.css.bak_final_apk_20260513_192149 | 42465 | None |
| android_app/app/src/main/python/static/live_map/muavin_live_map_extra.css.bak_clean_speed_visible_20260513_190933 | 42042 | None |
| android_app/app/src/main/python/static/seats/seats-final.css.bak_live_pill_dot | 41879 | None |
| android_app/app/src/main/python/static/live_map/muavin_live_map_extra.js.bak_next_ops_final_20260513_172822 | 41383 | None |
| android_app/app/src/main/python/static/live_map/muavin_live_map_extra.js.bak_remove_compass_20260513_165759 | 40400 | None |
| android_app/app/src/main/python/static/live_map/muavin_live_map_extra.css.bak_clean_location_visible_20260513_190610 | 40242 | None |
| android_app/app/src/main/python/static/live_map/muavin_live_map_extra.css.bak_clean_hide_km_20260513_190426 | 39080 | None |

## 8) Duplicate ID

### Aynı HTML içinde
| ID | Tekrar | Dosya |
| --- | --- | --- |
| tripGuardBackdrop | 2 | templates/index.html |
| tripGuardModal | 2 | templates/index.html |
| tripGuardGo | 2 | templates/index.html |
| tripGuardOk | 2 | templates/index.html |

### Farklı dosyalarda
| ID | Dosya sayısı | Dosyalar |
| --- | --- | --- |
| toast | 8 | android_app/app/src/main/python/templates/reports.html, android_app/app/src/main/python/templates/seats_parts/modals.html, apk_payload/templates/reports.html, apk_payload/templates/seats_parts/modals.html, templates/reports.html, templates/seats_parts/modals.html, templates/settings_recovery.html, templates/settings_subscription.html |
| n | 7 | templates/report_archive.html, templates/settings.html, templates/settings_backup.html, templates/settings_password.html, templates/settings_profile.html, templates/settings_recovery.html, templates/settings_subscription.html |
| seatModal | 7 | android_app/app/src/main/python/templates/seats_parts/modals.html, android_app/app/src/main/python/templates/trip_report.html, apk_payload/templates/seats_parts/modals.html, apk_payload/templates/trip_report.html, backups/apk_sync_20260520_234501/trip_report.html, templates/seats_parts/modals.html, templates/trip_report.html |
| btnReset | 6 | android_app/app/src/main/python/templates/passenger_control.html, android_app/app/src/main/python/templates/reports.html, apk_payload/templates/passenger_control.html, apk_payload/templates/reports.html, templates/passenger_control.html, templates/reports.html |
| deck | 6 | android_app/app/src/main/python/templates/passenger_control.html, android_app/app/src/main/python/templates/seats_parts/deck.html, apk_payload/templates/passenger_control.html, apk_payload/templates/seats_parts/deck.html, templates/passenger_control.html, templates/seats_parts/deck.html |
| endTripForm | 6 | android_app/app/src/main/python/templates/continue_trip.html, android_app/app/src/main/python/templates/hesap.html, apk_payload/templates/continue_trip.html, apk_payload/templates/hesap.html, templates/continue_trip.html, templates/hesap.html |
| fromSel | 6 | android_app/app/src/main/python/templates/fare_admin.html, android_app/app/src/main/python/templates/fare_query.html, apk_payload/templates/fare_admin.html, apk_payload/templates/fare_query.html, templates/fare_admin.html, templates/fare_query.html |
| label-{{ n }} | 6 | android_app/app/src/main/python/templates/passenger_control.html, android_app/app/src/main/python/templates/seats_parts/deck.html, apk_payload/templates/passenger_control.html, apk_payload/templates/seats_parts/deck.html, templates/passenger_control.html, templates/seats_parts/deck.html |
| routeSel | 6 | android_app/app/src/main/python/templates/fare_admin.html, android_app/app/src/main/python/templates/fare_query.html, apk_payload/templates/fare_admin.html, apk_payload/templates/fare_query.html, templates/fare_admin.html, templates/fare_query.html |
| seat-{{ n }} | 6 | android_app/app/src/main/python/templates/passenger_control.html, android_app/app/src/main/python/templates/seats_parts/deck.html, apk_payload/templates/passenger_control.html, apk_payload/templates/seats_parts/deck.html, templates/passenger_control.html, templates/seats_parts/deck.html |
| toSel | 6 | android_app/app/src/main/python/templates/fare_admin.html, android_app/app/src/main/python/templates/fare_query.html, apk_payload/templates/fare_admin.html, apk_payload/templates/fare_query.html, templates/fare_admin.html, templates/fare_query.html |
| aiDelay | 4 | android_app/app/src/main/python/templates/seats.html, apk_payload/templates/seats.html, backups/apk_sync_20260520_234501/seats.html, templates/seats.html |
| aiDensity | 4 | android_app/app/src/main/python/templates/seats.html, apk_payload/templates/seats.html, backups/apk_sync_20260520_234501/seats.html, templates/seats.html |
| aiLiveStop | 4 | android_app/app/src/main/python/templates/seats.html, apk_payload/templates/seats.html, backups/apk_sync_20260520_234501/seats.html, templates/seats.html |
| aiMain | 4 | android_app/app/src/main/python/templates/seats.html, apk_payload/templates/seats.html, backups/apk_sync_20260520_234501/seats.html, templates/seats.html |
| aiNextAction | 4 | android_app/app/src/main/python/templates/seats.html, apk_payload/templates/seats.html, backups/apk_sync_20260520_234501/seats.html, templates/seats.html |
| aiNextActionMirror | 4 | android_app/app/src/main/python/templates/seats.html, apk_payload/templates/seats.html, backups/apk_sync_20260520_234501/seats.html, templates/seats.html |
| aiParcel | 4 | android_app/app/src/main/python/templates/seats.html, apk_payload/templates/seats.html, backups/apk_sync_20260520_234501/seats.html, templates/seats.html |
| aiService | 4 | android_app/app/src/main/python/templates/seats.html, apk_payload/templates/seats.html, backups/apk_sync_20260520_234501/seats.html, templates/seats.html |
| aiSub | 4 | android_app/app/src/main/python/templates/seats.html, apk_payload/templates/seats.html, backups/apk_sync_20260520_234501/seats.html, templates/seats.html |
| alertRadius | 4 | android_app/app/src/main/python/templates/seats.html, apk_payload/templates/seats.html, backups/apk_sync_20260520_234501/seats.html, templates/seats.html |
| alertStop | 4 | android_app/app/src/main/python/templates/seats.html, apk_payload/templates/seats.html, backups/apk_sync_20260520_234501/seats.html, templates/seats.html |
| autoAdvanceToggle | 4 | android_app/app/src/main/python/templates/seats.html, apk_payload/templates/seats.html, backups/apk_sync_20260520_234501/seats.html, templates/seats.html |
| avatarPreview | 4 | android_app/app/src/main/python/templates/setup.html, apk_payload/templates/setup.html, templates/settings_profile.html, templates/setup.html |
| btnDeckAI | 4 | android_app/app/src/main/python/templates/seats.html, apk_payload/templates/seats.html, backups/apk_sync_20260520_234501/seats.html, templates/seats.html |
| btnDeckAIDrive | 4 | android_app/app/src/main/python/templates/seats.html, apk_payload/templates/seats.html, backups/apk_sync_20260520_234501/seats.html, templates/seats.html |
| btnGeoWatch | 4 | android_app/app/src/main/python/templates/seats.html, apk_payload/templates/seats.html, backups/apk_sync_20260520_234501/seats.html, templates/seats.html |
| btnOffloadNowPane | 4 | android_app/app/src/main/python/templates/seats.html, apk_payload/templates/seats.html, backups/apk_sync_20260520_234501/seats.html, templates/seats.html |
| btnOpenRouteTab | 4 | android_app/app/src/main/python/templates/seats.html, apk_payload/templates/seats.html, backups/apk_sync_20260520_234501/seats.html, templates/seats.html |
| btnSaveCoord | 4 | android_app/app/src/main/python/templates/seats.html, apk_payload/templates/seats.html, backups/apk_sync_20260520_234501/seats.html, templates/seats.html |
| btnTriggerNow | 4 | android_app/app/src/main/python/templates/seats.html, apk_payload/templates/seats.html, backups/apk_sync_20260520_234501/seats.html, templates/seats.html |
| clockDate | 4 | android_app/app/src/main/python/templates/seats.html, apk_payload/templates/seats.html, backups/apk_sync_20260520_234501/seats.html, templates/seats.html |
| clockMain | 4 | android_app/app/src/main/python/templates/seats.html, apk_payload/templates/seats.html, backups/apk_sync_20260520_234501/seats.html, templates/seats.html |
| clockSub | 4 | android_app/app/src/main/python/templates/seats.html, apk_payload/templates/seats.html, backups/apk_sync_20260520_234501/seats.html, templates/seats.html |
| coordLat | 4 | android_app/app/src/main/python/templates/seats.html, apk_payload/templates/seats.html, backups/apk_sync_20260520_234501/seats.html, templates/seats.html |
| coordLng | 4 | android_app/app/src/main/python/templates/seats.html, apk_payload/templates/seats.html, backups/apk_sync_20260520_234501/seats.html, templates/seats.html |
| coordStopName | 4 | android_app/app/src/main/python/templates/seats.html, apk_payload/templates/seats.html, backups/apk_sync_20260520_234501/seats.html, templates/seats.html |
| csvBtn | 4 | android_app/app/src/main/python/templates/trip_report.html, apk_payload/templates/trip_report.html, backups/apk_sync_20260520_234501/trip_report.html, templates/trip_report.html |
| delayMain | 4 | android_app/app/src/main/python/templates/seats.html, apk_payload/templates/seats.html, backups/apk_sync_20260520_234501/seats.html, templates/seats.html |
| delaySub | 4 | android_app/app/src/main/python/templates/seats.html, apk_payload/templates/seats.html, backups/apk_sync_20260520_234501/seats.html, templates/seats.html |
| dmaAiBtn | 4 | android_app/app/src/main/python/templates/seats.html, apk_payload/templates/seats.html, backups/apk_sync_20260520_234501/seats.html, templates/seats.html |
| dmaEndBtn | 4 | android_app/app/src/main/python/templates/seats.html, apk_payload/templates/seats.html, backups/apk_sync_20260520_234501/seats.html, templates/seats.html |
| drive-dock-stability-final | 4 | android_app/app/src/main/python/templates/seats.html, apk_payload/templates/seats.html, backups/apk_sync_20260520_234501/seats.html, templates/seats.html |
| drive-mode-actions-independent-js | 4 | android_app/app/src/main/python/templates/seats.html, apk_payload/templates/seats.html, backups/apk_sync_20260520_234501/seats.html, templates/seats.html |
| drive-mode-actions-independent-style | 4 | android_app/app/src/main/python/templates/seats.html, apk_payload/templates/seats.html, backups/apk_sync_20260520_234501/seats.html, templates/seats.html |
| drive-mode-force-toggle-js | 4 | android_app/app/src/main/python/templates/seats.html, apk_payload/templates/seats.html, backups/apk_sync_20260520_234501/seats.html, templates/seats.html |
| drive-voice-mirror-script | 4 | android_app/app/src/main/python/templates/seats.html, apk_payload/templates/seats.html, backups/apk_sync_20260520_234501/seats.html, templates/seats.html |
| driveEtaChip | 4 | android_app/app/src/main/python/templates/seats.html, apk_payload/templates/seats.html, backups/apk_sync_20260520_234501/seats.html, templates/seats.html |
| driveEtaMain | 4 | android_app/app/src/main/python/templates/seats.html, apk_payload/templates/seats.html, backups/apk_sync_20260520_234501/seats.html, templates/seats.html |
| driveEtaSub | 4 | android_app/app/src/main/python/templates/seats.html, apk_payload/templates/seats.html, backups/apk_sync_20260520_234501/seats.html, templates/seats.html |
| driveInlineDock | 4 | android_app/app/src/main/python/templates/seats.html, apk_payload/templates/seats.html, backups/apk_sync_20260520_234501/seats.html, templates/seats.html |
| driveModeActionsDock | 4 | android_app/app/src/main/python/templates/seats.html, apk_payload/templates/seats.html, backups/apk_sync_20260520_234501/seats.html, templates/seats.html |
| driveModeToggle | 4 | android_app/app/src/main/python/templates/seats.html, apk_payload/templates/seats.html, backups/apk_sync_20260520_234501/seats.html, templates/seats.html |
| driveSpeedChip | 4 | android_app/app/src/main/python/templates/seats.html, apk_payload/templates/seats.html, backups/apk_sync_20260520_234501/seats.html, templates/seats.html |
| driveVoiceEmpty | 4 | android_app/app/src/main/python/templates/seats.html, apk_payload/templates/seats.html, backups/apk_sync_20260520_234501/seats.html, templates/seats.html |
| driveVoiceFilled | 4 | android_app/app/src/main/python/templates/seats.html, apk_payload/templates/seats.html, backups/apk_sync_20260520_234501/seats.html, templates/seats.html |
| driveVoiceRow | 4 | android_app/app/src/main/python/templates/seats.html, apk_payload/templates/seats.html, backups/apk_sync_20260520_234501/seats.html, templates/seats.html |
| driveVoiceSeatCard | 4 | android_app/app/src/main/python/templates/seats.html, apk_payload/templates/seats.html, backups/apk_sync_20260520_234501/seats.html, templates/seats.html |
| embeddedArchiveBox | 4 | android_app/app/src/main/python/templates/trip_report.html, apk_payload/templates/trip_report.html, backups/apk_sync_20260520_234501/trip_report.html, templates/trip_report.html |
| embeddedArchiveList | 4 | android_app/app/src/main/python/templates/trip_report.html, apk_payload/templates/trip_report.html, backups/apk_sync_20260520_234501/trip_report.html, templates/trip_report.html |
| etaTimeline | 4 | android_app/app/src/main/python/templates/seats.html, apk_payload/templates/seats.html, backups/apk_sync_20260520_234501/seats.html, templates/seats.html |
| fabBulkPane | 4 | android_app/app/src/main/python/templates/seats.html, apk_payload/templates/seats.html, backups/apk_sync_20260520_234501/seats.html, templates/seats.html |
| fabCashPane | 4 | android_app/app/src/main/python/templates/seats.html, apk_payload/templates/seats.html, backups/apk_sync_20260520_234501/seats.html, templates/seats.html |
| geoHint | 4 | android_app/app/src/main/python/templates/seats.html, apk_payload/templates/seats.html, backups/apk_sync_20260520_234501/seats.html, templates/seats.html |
| miniLiveState | 4 | android_app/app/src/main/python/templates/seats.html, apk_payload/templates/seats.html, backups/apk_sync_20260520_234501/seats.html, templates/seats.html |
| miniStop | 4 | android_app/app/src/main/python/templates/seats.html, apk_payload/templates/seats.html, backups/apk_sync_20260520_234501/seats.html, templates/seats.html |
| openStandingModalBtn | 4 | android_app/app/src/main/python/templates/seats.html, apk_payload/templates/seats.html, backups/apk_sync_20260520_234501/seats.html, templates/seats.html |
| prLine | 4 | android_app/app/src/main/python/templates/seats.html, apk_payload/templates/seats.html, backups/apk_sync_20260520_234501/seats.html, templates/seats.html |
| profilePhotoInput | 4 | android_app/app/src/main/python/templates/setup.html, apk_payload/templates/setup.html, templates/settings_profile.html, templates/setup.html |
| quickStandingList | 4 | android_app/app/src/main/python/templates/seats.html, apk_payload/templates/seats.html, backups/apk_sync_20260520_234501/seats.html, templates/seats.html |
| quickStandingMeta | 4 | android_app/app/src/main/python/templates/seats.html, apk_payload/templates/seats.html, backups/apk_sync_20260520_234501/seats.html, templates/seats.html |
| resoldSeats | 4 | android_app/app/src/main/python/templates/trip_report.html, apk_payload/templates/trip_report.html, backups/apk_sync_20260520_234501/trip_report.html, templates/trip_report.html |
| routeLiveStop | 4 | android_app/app/src/main/python/templates/seats.html, apk_payload/templates/seats.html, backups/apk_sync_20260520_234501/seats.html, templates/seats.html |
| routeLiveStopCard | 4 | android_app/app/src/main/python/templates/seats.html, apk_payload/templates/seats.html, backups/apk_sync_20260520_234501/seats.html, templates/seats.html |
| routeNextTimed | 4 | android_app/app/src/main/python/templates/seats.html, apk_payload/templates/seats.html, backups/apk_sync_20260520_234501/seats.html, templates/seats.html |
| seat-simple-bottom-bar-script | 4 | android_app/app/src/main/python/templates/seats.html, apk_payload/templates/seats.html, backups/apk_sync_20260520_234501/seats.html, templates/seats.html |
| seatModalBackdrop | 4 | android_app/app/src/main/python/templates/trip_report.html, apk_payload/templates/trip_report.html, backups/apk_sync_20260520_234501/trip_report.html, templates/trip_report.html |
| seatModalBody | 4 | android_app/app/src/main/python/templates/trip_report.html, apk_payload/templates/trip_report.html, backups/apk_sync_20260520_234501/trip_report.html, templates/trip_report.html |
| seatModalClose | 4 | android_app/app/src/main/python/templates/trip_report.html, apk_payload/templates/trip_report.html, backups/apk_sync_20260520_234501/trip_report.html, templates/trip_report.html |
| seatModalSub | 4 | android_app/app/src/main/python/templates/trip_report.html, apk_payload/templates/trip_report.html, backups/apk_sync_20260520_234501/trip_report.html, templates/trip_report.html |
| seatModalTitle | 4 | android_app/app/src/main/python/templates/trip_report.html, apk_payload/templates/trip_report.html, backups/apk_sync_20260520_234501/trip_report.html, templates/trip_report.html |
| seatReportDeck | 4 | android_app/app/src/main/python/templates/trip_report.html, apk_payload/templates/trip_report.html, backups/apk_sync_20260520_234501/trip_report.html, templates/trip_report.html |
| seatSimpleBottomBar | 4 | android_app/app/src/main/python/templates/seats.html, apk_payload/templates/seats.html, backups/apk_sync_20260520_234501/seats.html, templates/seats.html |
| seatSimpleOpenDurak | 4 | android_app/app/src/main/python/templates/seats.html, apk_payload/templates/seats.html, backups/apk_sync_20260520_234501/seats.html, templates/seats.html |
| seatSimpleVoiceBtn | 4 | android_app/app/src/main/python/templates/seats.html, apk_payload/templates/seats.html, backups/apk_sync_20260520_234501/seats.html, templates/seats.html |
| selectedStopBadge | 4 | android_app/app/src/main/python/templates/seats.html, apk_payload/templates/seats.html, backups/apk_sync_20260520_234501/seats.html, templates/seats.html |
| shareBtn | 4 | android_app/app/src/main/python/templates/trip_report.html, apk_payload/templates/trip_report.html, backups/apk_sync_20260520_234501/trip_report.html, templates/trip_report.html |
| soundToggle | 4 | android_app/app/src/main/python/templates/seats.html, apk_payload/templates/seats.html, backups/apk_sync_20260520_234501/seats.html, templates/seats.html |
| spLimit | 4 | android_app/app/src/main/python/templates/seats.html, apk_payload/templates/seats.html, backups/apk_sync_20260520_234501/seats.html, templates/seats.html |
| spVal | 4 | android_app/app/src/main/python/templates/seats.html, apk_payload/templates/seats.html, backups/apk_sync_20260520_234501/seats.html, templates/seats.html |
| speedBox | 4 | android_app/app/src/main/python/templates/seats.html, apk_payload/templates/seats.html, backups/apk_sync_20260520_234501/seats.html, templates/seats.html |
| stEtaHint | 4 | android_app/app/src/main/python/templates/seats.html, apk_payload/templates/seats.html, backups/apk_sync_20260520_234501/seats.html, templates/seats.html |
| stEtaTarget | 4 | android_app/app/src/main/python/templates/seats.html, apk_payload/templates/seats.html, backups/apk_sync_20260520_234501/seats.html, templates/seats.html |
| stopReportList | 4 | android_app/app/src/main/python/templates/trip_report.html, apk_payload/templates/trip_report.html, backups/apk_sync_20260520_234501/trip_report.html, templates/trip_report.html |
| totalBoard | 4 | android_app/app/src/main/python/templates/trip_report.html, apk_payload/templates/trip_report.html, backups/apk_sync_20260520_234501/trip_report.html, templates/trip_report.html |
| totalMoney | 4 | android_app/app/src/main/python/templates/trip_report.html, apk_payload/templates/trip_report.html, backups/apk_sync_20260520_234501/trip_report.html, templates/trip_report.html |
| totalOff | 4 | android_app/app/src/main/python/templates/trip_report.html, apk_payload/templates/trip_report.html, backups/apk_sync_20260520_234501/trip_report.html, templates/trip_report.html |
| tripInfo | 4 | android_app/app/src/main/python/templates/trip_report.html, apk_payload/templates/trip_report.html, backups/apk_sync_20260520_234501/trip_report.html, templates/trip_report.html |
| ttsToggle | 4 | android_app/app/src/main/python/templates/seats.html, apk_payload/templates/seats.html, backups/apk_sync_20260520_234501/seats.html, templates/seats.html |
| voiceSeatEmpty | 4 | android_app/app/src/main/python/templates/seats.html, apk_payload/templates/seats.html, backups/apk_sync_20260520_234501/seats.html, templates/seats.html |
| voiceSeatFilled | 4 | android_app/app/src/main/python/templates/seats.html, apk_payload/templates/seats.html, backups/apk_sync_20260520_234501/seats.html, templates/seats.html |
| voiceSeatMiniStats | 4 | android_app/app/src/main/python/templates/seats.html, apk_payload/templates/seats.html, backups/apk_sync_20260520_234501/seats.html, templates/seats.html |
| voiceStateBadge | 4 | android_app/app/src/main/python/templates/seats.html, apk_payload/templates/seats.html, backups/apk_sync_20260520_234501/seats.html, templates/seats.html |
| acAmount | 3 | android_app/app/src/main/python/templates/ai_console.html, apk_payload/templates/ai_console.html, templates/ai_console.html |
| acFrom | 3 | android_app/app/src/main/python/templates/ai_console.html, apk_payload/templates/ai_console.html, templates/ai_console.html |
| acGender | 3 | android_app/app/src/main/python/templates/ai_console.html, apk_payload/templates/ai_console.html, templates/ai_console.html |
| acNote | 3 | android_app/app/src/main/python/templates/ai_console.html, apk_payload/templates/ai_console.html, templates/ai_console.html |
| acPairOk | 3 | android_app/app/src/main/python/templates/ai_console.html, apk_payload/templates/ai_console.html, templates/ai_console.html |
| acPayment | 3 | android_app/app/src/main/python/templates/ai_console.html, apk_payload/templates/ai_console.html, templates/ai_console.html |
| acSeats | 3 | android_app/app/src/main/python/templates/ai_console.html, apk_payload/templates/ai_console.html, templates/ai_console.html |
| acService | 3 | android_app/app/src/main/python/templates/ai_console.html, apk_payload/templates/ai_console.html, templates/ai_console.html |
| acTicketType | 3 | android_app/app/src/main/python/templates/ai_console.html, apk_payload/templates/ai_console.html, templates/ai_console.html |
| acTo | 3 | android_app/app/src/main/python/templates/ai_console.html, apk_payload/templates/ai_console.html, templates/ai_console.html |
| actionCard | 3 | android_app/app/src/main/python/templates/ai_console.html, apk_payload/templates/ai_console.html, templates/ai_console.html |
| actionIntentBadge | 3 | android_app/app/src/main/python/templates/ai_console.html, apk_payload/templates/ai_console.html, templates/ai_console.html |
| actionSub | 3 | android_app/app/src/main/python/templates/ai_console.html, apk_payload/templates/ai_console.html, templates/ai_console.html |
| actionTitle | 3 | android_app/app/src/main/python/templates/ai_console.html, apk_payload/templates/ai_console.html, templates/ai_console.html |
| active-trip-guard-script | 3 | android_app/app/src/main/python/templates/index.html, apk_payload/templates/index.html, templates/index.html |
| active-trip-guard-style | 3 | android_app/app/src/main/python/templates/index.html, apk_payload/templates/index.html, templates/index.html |
| approach-alert-banner-compact-style | 3 | android_app/app/src/main/python/templates/live_map.html, apk_payload/templates/live_map.html, templates/live_map.html |

## 9) JS Fonksiyon Tekrarları

### Aynı dosya içinde
| Fonksiyon | Tekrar | Dosya |
| --- | --- | --- |
| e | 83 | android_app/app/src/main/python/static/vendor/bootstrap/bootstrap.bundle.min.js |
| e | 83 | apk_payload/static/vendor/bootstrap/bootstrap.bundle.min.js |
| e | 83 | static/vendor/bootstrap/bootstrap.bundle.min.js |
| i | 40 | android_app/app/src/main/python/static/vendor/bootstrap/bootstrap.bundle.min.js |
| i | 40 | apk_payload/static/vendor/bootstrap/bootstrap.bundle.min.js |
| i | 40 | static/vendor/bootstrap/bootstrap.bundle.min.js |
| t | 39 | android_app/app/src/main/python/static/vendor/bootstrap/bootstrap.bundle.min.js |
| t | 39 | apk_payload/static/vendor/bootstrap/bootstrap.bundle.min.js |
| t | 39 | static/vendor/bootstrap/bootstrap.bundle.min.js |
| t | 38 | _unused_review/static/vendor/jquery/jquery-3.7.1.min.js |
| n | 33 | _unused_review/static/vendor/jquery/jquery-3.7.1.min.js |
| n | 23 | android_app/app/src/main/python/static/vendor/bootstrap/bootstrap.bundle.min.js |
| n | 23 | apk_payload/static/vendor/bootstrap/bootstrap.bundle.min.js |
| n | 23 | static/vendor/bootstrap/bootstrap.bundle.min.js |
| e | 22 | _unused_review/static/vendor/jquery/jquery-3.7.1.min.js |
| msg | 21 | android_app/app/src/main/python/static/seats/voice-commands.js |
| msg | 21 | apk_payload/static/seats/voice-commands.js |
| msg | 21 | static/seats/voice-commands.js |
| map | 17 | android_app/app/src/main/python/static/live_map/muavin_live_map_extra.js |
| map | 17 | apk_payload/static/live_map/muavin_live_map_extra.js |
| map | 17 | static/live_map/muavin_live_map_extra.js |
| s | 15 | android_app/app/src/main/python/static/vendor/bootstrap/bootstrap.bundle.min.js |
| s | 15 | apk_payload/static/vendor/bootstrap/bootstrap.bundle.min.js |
| s | 15 | static/vendor/bootstrap/bootstrap.bundle.min.js |
| r | 13 | _unused_review/static/vendor/jquery/jquery-3.7.1.min.js |
| container | 12 | android_app/app/src/main/python/static/live_map/muavin_live_map_extra.js |
| container | 12 | apk_payload/static/live_map/muavin_live_map_extra.js |
| container | 12 | static/live_map/muavin_live_map_extra.js |
| j | 11 | android_app/app/src/main/python/static/seats/seats.js |
| j | 11 | apk_payload/static/seats/seats.js |
| j | 11 | static/seats/seats.js |
| stop | 11 | android_app/app/src/main/python/static/seats/voice-commands.js |
| stop | 11 | apk_payload/static/seats/voice-commands.js |
| stop | 11 | static/seats/voice-commands.js |
| el | 10 | android_app/app/src/main/python/static/seats/seats.js |
| el | 10 | apk_payload/static/seats/seats.js |
| el | 10 | static/seats/seats.js |
| list | 10 | android_app/app/src/main/python/static/seats/seats.js |
| list | 10 | apk_payload/static/seats/seats.js |
| list | 10 | static/seats/seats.js |
| stop | 10 | android_app/app/src/main/python/static/seats/seats.js |
| stop | 10 | apk_payload/static/seats/seats.js |
| stop | 10 | static/seats/seats.js |
| el | 9 | templates/passenger_control.html |
| el | 9 | android_app/app/src/main/python/templates/passenger_control.html |
| el | 9 | apk_payload/templates/passenger_control.html |
| res | 9 | android_app/app/src/main/python/static/continue/continue_trip_core.js |
| res | 9 | static/continue/continue_trip_core.js |
| res | 9 | apk_payload/templates/continue_trip.html |
| data | 8 | android_app/app/src/main/python/static/continue/continue_trip_core.js |
| data | 8 | static/continue/continue_trip_core.js |
| data | 8 | apk_payload/templates/continue_trip.html |
| key | 8 | android_app/app/src/main/python/static/seats/seats.js |
| key | 8 | apk_payload/static/seats/seats.js |
| key | 8 | static/seats/seats.js |
| next | 8 | android_app/app/src/main/python/static/seats/seats.js |
| next | 8 | apk_payload/static/seats/seats.js |
| next | 8 | static/seats/seats.js |
| o | 8 | android_app/app/src/main/python/static/vendor/bootstrap/bootstrap.bundle.min.js |
| o | 8 | apk_payload/static/vendor/bootstrap/bootstrap.bundle.min.js |
| o | 8 | static/vendor/bootstrap/bootstrap.bundle.min.js |
| seats | 8 | templates/ai_console.html |
| seats | 8 | android_app/app/src/main/python/templates/ai_console.html |
| seats | 8 | apk_payload/templates/ai_console.html |
| btn | 7 | templates/live_map.html |
| btn | 7 | android_app/app/src/main/python/templates/live_map.html |
| btn | 7 | apk_payload/templates/live_map.html |
| live | 7 | android_app/app/src/main/python/static/seats/seats.js |
| live | 7 | apk_payload/static/seats/seats.js |
| live | 7 | static/seats/seats.js |
| passengers | 7 | android_app/app/src/main/python/static/continue/continue_trip_core.js |
| passengers | 7 | static/continue/continue_trip_core.js |
| passengers | 7 | apk_payload/templates/continue_trip.html |
| btn | 6 | templates/seats.html |
| btn | 6 | backups/apk_sync_20260520_234501/seats.html |
| btn | 6 | android_app/app/src/main/python/templates/seats.html |
| btn | 6 | apk_payload/templates/seats.html |
| cRect | 6 | android_app/app/src/main/python/static/live_map/muavin_live_map_extra.js |
| cRect | 6 | apk_payload/static/live_map/muavin_live_map_extra.js |
| cRect | 6 | static/live_map/muavin_live_map_extra.js |
| data | 6 | templates/ai_console.html |
| data | 6 | android_app/app/src/main/python/templates/ai_console.html |
| data | 6 | apk_payload/templates/ai_console.html |
| j | 6 | android_app/app/src/main/python/static/seats/standing.js |
| j | 6 | apk_payload/static/seats/standing.js |
| j | 6 | static/seats/standing.js |
| km | 6 | android_app/app/src/main/python/static/seats/seats.js |
| km | 6 | apk_payload/static/seats/seats.js |
| km | 6 | static/seats/seats.js |
| n | 6 | android_app/app/src/main/python/static/continue/continue_trip_core.js |
| n | 6 | static/continue/continue_trip_core.js |
| boot | 5 | templates/seats.html |
| boot | 5 | backups/apk_sync_20260520_234501/seats.html |
| boot | 5 | android_app/app/src/main/python/templates/seats.html |
| boot | 5 | apk_payload/templates/seats.html |
| canonical | 5 | android_app/app/src/main/python/static/seats/seats.js |
| canonical | 5 | apk_payload/static/seats/seats.js |
| canonical | 5 | static/seats/seats.js |
| g | 5 | android_app/app/src/main/python/static/continue/continue_trip_core.js |
| g | 5 | static/continue/continue_trip_core.js |
| g | 5 | apk_payload/templates/continue_trip.html |
| headers | 5 | android_app/app/src/main/python/static/continue/continue_trip_core.js |
| headers | 5 | static/continue/continue_trip_core.js |
| headers | 5 | apk_payload/templates/continue_trip.html |
| i | 5 | android_app/app/src/main/python/static/live_map/muavin_live_map_extra.js |
| i | 5 | apk_payload/static/live_map/muavin_live_map_extra.js |
| i | 5 | static/live_map/muavin_live_map_extra.js |
| j | 5 | templates/consignments.html |
| j | 5 | android_app/app/src/main/python/templates/consignments.html |
| j | 5 | apk_payload/templates/consignments.html |
| m | 5 | templates/trip_report.html |
| m | 5 | backups/apk_sync_20260520_234501/trip_report.html |
| m | 5 | android_app/app/src/main/python/templates/trip_report.html |
| m | 5 | apk_payload/templates/trip_report.html |
| now | 5 | android_app/app/src/main/python/static/seats/seats.js |
| now | 5 | apk_payload/static/seats/seats.js |
| now | 5 | static/seats/seats.js |
| res | 5 | templates/consignments.html |
| res | 5 | android_app/app/src/main/python/templates/consignments.html |
| res | 5 | apk_payload/templates/consignments.html |

### Farklı dosyalarda
| Fonksiyon | Dosya sayısı | Dosyalar |
| --- | --- | --- |
| btn | 58 | android_app/app/src/main/python/static/continue/continue_trip_core.js, android_app/app/src/main/python/static/live_map/muavin_live_map_extra.js, android_app/app/src/main/python/static/seats/drive-controls.js, android_app/app/src/main/python/static/seats/patches/seat-simple-ui-pack.js, android_app/app/src/main/python/static/seats/patches/stop-flow-focus-patch.js, android_app/app/src/main/python/static/seats/patches/top-sound-toggle.js, android_app/app/src/main/python/static/seats/seats.js, android_app/app/src/main/python/static/seats/voice-commands.js, android_app/app/src/main/python/static/seats/voice-tts.js, android_app/app/src/main/python/templates/ai_console.html |
| el | 58 | android_app/app/src/main/python/static/continue/continue_flow_refresh.js, android_app/app/src/main/python/static/continue/continue_live_diagnostics.js, android_app/app/src/main/python/static/continue/continue_trip_core.js, android_app/app/src/main/python/static/continue/continue_trip_ui.js, android_app/app/src/main/python/static/live_map/muavin_live_map_extra.js, android_app/app/src/main/python/static/seats/bags.js, android_app/app/src/main/python/static/seats/drive-controls.js, android_app/app/src/main/python/static/seats/patches/manual-ticket-system.js, android_app/app/src/main/python/static/seats/patches/seat-simple-ui-pack.js, android_app/app/src/main/python/static/seats/patches/stop-flow-focus-patch.js |
| text | 42 | android_app/app/src/main/python/static/continue/continue_flow_refresh.js, android_app/app/src/main/python/static/continue/continue_live_diagnostics.js, android_app/app/src/main/python/static/continue/continue_trip_core.js, android_app/app/src/main/python/static/live_map/muavin_live_map_extra.js, android_app/app/src/main/python/static/seats/patches/manual-ticket-system.js, android_app/app/src/main/python/static/seats/patches/stop-flow-focus-patch.js, android_app/app/src/main/python/static/seats/route-marquee.js, android_app/app/src/main/python/static/seats/voice-commands.js, android_app/app/src/main/python/templates/ai_console.html, android_app/app/src/main/python/templates/hesap.html |
| j | 41 | android_app/app/src/main/python/static/continue/continue_live_diagnostics.js, android_app/app/src/main/python/static/continue/continue_trip_core.js, android_app/app/src/main/python/static/seats/bags.js, android_app/app/src/main/python/static/seats/seats-time-prayer.js, android_app/app/src/main/python/static/seats/seats.js, android_app/app/src/main/python/static/seats/standing.js, android_app/app/src/main/python/static/seats/voice-commands.js, android_app/app/src/main/python/static/vendor/bootstrap/bootstrap.bundle.min.js, android_app/app/src/main/python/templates/consignments.html, android_app/app/src/main/python/templates/passenger_control.html |
| n | 37 | _unused_review/static/vendor/jquery/jquery-3.7.1.min.js, android_app/app/src/main/python/static/continue/continue_bag_emanet.js, android_app/app/src/main/python/static/continue/continue_flow_refresh.js, android_app/app/src/main/python/static/continue/continue_trip_core.js, android_app/app/src/main/python/static/seats/seats-time-prayer.js, android_app/app/src/main/python/static/seats/seats.js, android_app/app/src/main/python/static/seats/voice-commands.js, android_app/app/src/main/python/static/seats/voice-tts.js, android_app/app/src/main/python/static/vendor/bootstrap/bootstrap.bundle.min.js, android_app/app/src/main/python/templates/live_map.html |
| t | 36 | _unused_review/static/vendor/jquery/jquery-3.7.1.min.js, android_app/app/src/main/python/static/continue/continue_live_diagnostics.js, android_app/app/src/main/python/static/continue/continue_trip_ui.js, android_app/app/src/main/python/static/seats/drive-eta-chip.js, android_app/app/src/main/python/static/seats/patches/modal-bottom-nav-autohide.js, android_app/app/src/main/python/static/seats/patches/stop-flow-focus-patch.js, android_app/app/src/main/python/static/seats/seats.js, android_app/app/src/main/python/static/seats/voice-commands.js, android_app/app/src/main/python/static/vendor/bootstrap/bootstrap.bundle.min.js, android_app/app/src/main/python/templates/live_map.html |
| q | 34 | _unused_review/static/vendor/jquery/jquery-3.7.1.min.js, android_app/app/src/main/python/static/continue/continue_trip_core.js, android_app/app/src/main/python/static/continue/continue_trip_ui.js, android_app/app/src/main/python/static/seats/drive-eta-chip.js, android_app/app/src/main/python/static/seats/patches/seat-layout-fab-pack.js, android_app/app/src/main/python/static/seats/patches/seat-simple-ui-pack.js, android_app/app/src/main/python/static/seats/patches/top-sound-toggle.js, android_app/app/src/main/python/templates/ai_console.html, android_app/app/src/main/python/templates/fare_admin.html, android_app/app/src/main/python/templates/hesap.html |
| r | 34 | _unused_review/static/vendor/jquery/jquery-3.7.1.min.js, android_app/app/src/main/python/static/app.js, android_app/app/src/main/python/static/continue/continue_trip_core.js, android_app/app/src/main/python/static/live_map/muavin_live_map_extra.js, android_app/app/src/main/python/static/seats/patches/modal-bottom-nav-autohide.js, android_app/app/src/main/python/static/seats/seats-time-prayer.js, android_app/app/src/main/python/static/seats/seats.js, android_app/app/src/main/python/static/seats/voice-commands.js, android_app/app/src/main/python/static/vendor/bootstrap/bootstrap.bundle.min.js, android_app/app/src/main/python/templates/passenger_control.html |
| list | 30 | android_app/app/src/main/python/static/seats/bags.js, android_app/app/src/main/python/static/seats/patches/manual-ticket-system.js, android_app/app/src/main/python/static/seats/patches/stop-flow-focus-patch.js, android_app/app/src/main/python/static/seats/seats-time-prayer.js, android_app/app/src/main/python/static/seats/seats.js, android_app/app/src/main/python/static/seats/standing.js, android_app/app/src/main/python/static/seats/voice-commands.js, android_app/app/src/main/python/templates/hesap.html, android_app/app/src/main/python/templates/passenger_control.html, android_app/app/src/main/python/templates/route_edit.html |
| res | 30 | android_app/app/src/main/python/static/continue/continue_flow_refresh.js, android_app/app/src/main/python/static/continue/continue_live_diagnostics.js, android_app/app/src/main/python/static/continue/continue_trip_core.js, android_app/app/src/main/python/static/seats/seats.js, android_app/app/src/main/python/static/seats/voice-commands.js, android_app/app/src/main/python/templates/ai_console.html, android_app/app/src/main/python/templates/consignments.html, android_app/app/src/main/python/templates/route_edit.html, android_app/app/src/main/python/templates/route_stops.html, android_app/app/src/main/python/templates/routes_list.html |
| d | 28 | _unused_review/static/vendor/jquery/jquery-3.7.1.min.js, android_app/app/src/main/python/static/continue/continue_trip_core.js, android_app/app/src/main/python/static/live_map/muavin_live_map_extra.js, android_app/app/src/main/python/static/seats/seats-time-prayer.js, android_app/app/src/main/python/static/seats/seats.js, android_app/app/src/main/python/static/seats/standing.js, android_app/app/src/main/python/static/vendor/bootstrap/bootstrap.bundle.min.js, android_app/app/src/main/python/templates/consignments.html, android_app/app/src/main/python/templates/onboarding.html, android_app/app/src/main/python/templates/trip_report.html |
| boot | 27 | android_app/app/src/main/python/static/continue/continue_bag_emanet.js, android_app/app/src/main/python/static/live_map/muavin_live_map_extra.js, android_app/app/src/main/python/static/seats/drive-controls.js, android_app/app/src/main/python/static/seats/drive-eta-chip.js, android_app/app/src/main/python/static/seats/patches/seat-simple-ui-pack.js, android_app/app/src/main/python/static/seats/route-marquee.js, android_app/app/src/main/python/static/seats/seats-time-prayer.js, android_app/app/src/main/python/static/seats/voice-tts.js, android_app/app/src/main/python/templates/seats.html, apk_payload/static/live_map/muavin_live_map_extra.js |
| next | 27 | android_app/app/src/main/python/static/live_map/muavin_live_map_extra.js, android_app/app/src/main/python/static/seats/drive-controls.js, android_app/app/src/main/python/static/seats/patches/seat-simple-ui-pack.js, android_app/app/src/main/python/static/seats/patches/top-sound-toggle.js, android_app/app/src/main/python/static/seats/seats-time-prayer.js, android_app/app/src/main/python/static/seats/seats.js, android_app/app/src/main/python/static/seats/voice-commands.js, android_app/app/src/main/python/static/seats/voice-tts.js, android_app/app/src/main/python/templates/live_map.html, apk_payload/static/live_map/muavin_live_map_extra.js |
| stop | 27 | android_app/app/src/main/python/static/app.js, android_app/app/src/main/python/static/continue/continue_trip_core.js, android_app/app/src/main/python/static/live_map/muavin_live_map_extra.js, android_app/app/src/main/python/static/seats/patches/seat-simple-ui-pack.js, android_app/app/src/main/python/static/seats/seats.js, android_app/app/src/main/python/static/seats/voice-commands.js, android_app/app/src/main/python/static/seats/voice-tts.js, android_app/app/src/main/python/templates/live_map.html, android_app/app/src/main/python/templates/route_edit.html, apk_payload/static/app.js |
| total | 27 | android_app/app/src/main/python/static/live_map/muavin_live_map_extra.js, android_app/app/src/main/python/static/seats/bags.js, android_app/app/src/main/python/static/seats/patches/seat-simple-ui-pack.js, android_app/app/src/main/python/static/seats/seats.js, android_app/app/src/main/python/static/seats/standing.js, android_app/app/src/main/python/static/seats/voice-commands.js, android_app/app/src/main/python/templates/ai_console.html, android_app/app/src/main/python/templates/live_map.html, android_app/app/src/main/python/templates/passenger_control.html, apk_payload/static/live_map/muavin_live_map_extra.js |
| h | 26 | android_app/app/src/main/python/static/continue/continue_flow_refresh.js, android_app/app/src/main/python/static/continue/continue_trip_core.js, android_app/app/src/main/python/static/live_map/muavin_live_map_extra.js, android_app/app/src/main/python/static/seats/seats-time-prayer.js, android_app/app/src/main/python/static/seats/seats.js, android_app/app/src/main/python/static/vendor/bootstrap/bootstrap.bundle.min.js, android_app/app/src/main/python/templates/hesap.html, android_app/app/src/main/python/templates/reports.html, android_app/app/src/main/python/templates/trip_report.html, apk_payload/static/live_map/muavin_live_map_extra.js |
| s | 25 | _unused_review/static/vendor/jquery/jquery-3.7.1.min.js, android_app/app/src/main/python/static/app.js, android_app/app/src/main/python/static/continue/continue_live_diagnostics.js, android_app/app/src/main/python/static/continue/continue_trip_core.js, android_app/app/src/main/python/static/live_map/muavin_live_map_extra.js, android_app/app/src/main/python/static/seats/seats.js, android_app/app/src/main/python/static/vendor/bootstrap/bootstrap.bundle.min.js, android_app/app/src/main/python/templates/reports.html, android_app/app/src/main/python/templates/trip_report.html, apk_payload/static/app.js |
| box | 24 | android_app/app/src/main/python/static/continue/continue_live_diagnostics.js, android_app/app/src/main/python/static/seats/patches/seat-simple-ui-pack.js, android_app/app/src/main/python/static/seats/seats.js, android_app/app/src/main/python/templates/ai_console.html, android_app/app/src/main/python/templates/live_map.html, android_app/app/src/main/python/templates/rehber.html, android_app/app/src/main/python/templates/route_edit.html, android_app/app/src/main/python/templates/trip_report.html, apk_payload/static/seats/patches/seat-simple-ui-pack.js, apk_payload/static/seats/seats.js |
| m | 24 | _unused_review/static/vendor/jquery/jquery-3.7.1.min.js, android_app/app/src/main/python/static/continue/continue_trip_core.js, android_app/app/src/main/python/static/continue/continue_trip_ui.js, android_app/app/src/main/python/static/live_map/muavin_live_map_extra.js, android_app/app/src/main/python/static/seats/seats-time-prayer.js, android_app/app/src/main/python/static/seats/seats.js, android_app/app/src/main/python/static/seats/voice-commands.js, android_app/app/src/main/python/templates/live_map.html, android_app/app/src/main/python/templates/trip_report.html, apk_payload/static/live_map/muavin_live_map_extra.js |
| txt | 24 | android_app/app/src/main/python/static/continue/continue_bag_emanet.js, android_app/app/src/main/python/static/live_map/muavin_live_map_extra.js, android_app/app/src/main/python/static/seats/patches/stop-flow-focus-patch.js, android_app/app/src/main/python/static/seats/seats.js, android_app/app/src/main/python/static/seats/voice-commands.js, android_app/app/src/main/python/templates/ai_console.html, android_app/app/src/main/python/templates/fare_admin.html, android_app/app/src/main/python/templates/seats.html, apk_payload/static/live_map/muavin_live_map_extra.js, apk_payload/static/seats/patches/stop-flow-focus-patch.js |
| note | 23 | android_app/app/src/main/python/static/continue/continue_live_diagnostics.js, android_app/app/src/main/python/static/live_map/muavin_live_map_extra.js, android_app/app/src/main/python/static/seats/seats.js, android_app/app/src/main/python/static/seats/standing.js, android_app/app/src/main/python/static/seats/voice-commands.js, android_app/app/src/main/python/templates/ai_console.html, android_app/app/src/main/python/templates/hesap.html, android_app/app/src/main/python/templates/live_map.html, apk_payload/static/live_map/muavin_live_map_extra.js, apk_payload/static/seats/seats.js |
| modal | 22 | android_app/app/src/main/python/templates/consignments.html, android_app/app/src/main/python/templates/hesap.html, android_app/app/src/main/python/templates/index.html, android_app/app/src/main/python/templates/passenger_control.html, android_app/app/src/main/python/templates/seats_parts/finish_trip_modal.html, android_app/app/src/main/python/templates/seats_parts/offload_confirm.html, android_app/app/src/main/python/templates/settings_subscription.html, apk_payload/templates/consignments.html, apk_payload/templates/hesap.html, apk_payload/templates/index.html |
| u | 22 | _unused_review/static/vendor/jquery/jquery-3.7.1.min.js, android_app/app/src/main/python/static/continue/continue_trip_core.js, android_app/app/src/main/python/static/live_map/muavin_live_map_extra.js, android_app/app/src/main/python/static/seats/bags.js, android_app/app/src/main/python/static/seats/seats.js, android_app/app/src/main/python/static/seats/voice-commands.js, android_app/app/src/main/python/static/seats/voice-tts.js, android_app/app/src/main/python/templates/live_map.html, apk_payload/static/live_map/muavin_live_map_extra.js, apk_payload/static/seats/bags.js |
| a | 21 | _unused_review/static/vendor/jquery/jquery-3.7.1.min.js, android_app/app/src/main/python/static/live_map/muavin_live_map_extra.js, android_app/app/src/main/python/static/seats/seats-time-prayer.js, android_app/app/src/main/python/static/seats/seats.js, android_app/app/src/main/python/static/vendor/bootstrap/bootstrap.bundle.min.js, android_app/app/src/main/python/templates/reports.html, android_app/app/src/main/python/templates/trip_report.html, apk_payload/static/live_map/muavin_live_map_extra.js, apk_payload/static/seats/seats-time-prayer.js, apk_payload/static/seats/seats.js |
| data | 21 | android_app/app/src/main/python/static/app.js, android_app/app/src/main/python/static/continue/continue_flow_refresh.js, android_app/app/src/main/python/static/continue/continue_live_diagnostics.js, android_app/app/src/main/python/static/continue/continue_trip_core.js, android_app/app/src/main/python/static/continue/continue_trip_ui.js, android_app/app/src/main/python/templates/ai_console.html, android_app/app/src/main/python/templates/settings_subscription.html, android_app/app/src/main/python/templates/trip_report.html, apk_payload/static/app.js, apk_payload/templates/ai_console.html |
| i | 21 | _unused_review/static/vendor/jquery/jquery-3.7.1.min.js, android_app/app/src/main/python/static/continue/continue_flow_refresh.js, android_app/app/src/main/python/static/live_map/muavin_live_map_extra.js, android_app/app/src/main/python/static/seats/seats-time-prayer.js, android_app/app/src/main/python/static/seats/seats.js, android_app/app/src/main/python/static/vendor/bootstrap/bootstrap.bundle.min.js, android_app/app/src/main/python/templates/live_map.html, android_app/app/src/main/python/templates/onboarding.html, apk_payload/static/live_map/muavin_live_map_extra.js, apk_payload/static/seats/seats-time-prayer.js |
| target | 21 | android_app/app/src/main/python/static/continue/continue_flow_refresh.js, android_app/app/src/main/python/static/continue/continue_trip_core.js, android_app/app/src/main/python/static/seats/drive-eta-chip.js, android_app/app/src/main/python/static/seats/patches/stop-flow-focus-patch.js, android_app/app/src/main/python/static/seats/seats.js, android_app/app/src/main/python/templates/live_map.html, android_app/app/src/main/python/templates/settings_subscription.html, android_app/app/src/main/python/templates/setup.html, apk_payload/static/seats/drive-eta-chip.js, apk_payload/static/seats/patches/stop-flow-focus-patch.js |
| url | 21 | android_app/app/src/main/python/static/continue/continue_trip_core.js, android_app/app/src/main/python/static/seats/seats-time-prayer.js, android_app/app/src/main/python/static/seats/seats.js, android_app/app/src/main/python/templates/ai_console.html, android_app/app/src/main/python/templates/reports.html, android_app/app/src/main/python/templates/setup.html, android_app/app/src/main/python/templates/trip_report.html, apk_payload/static/seats/seats-time-prayer.js, apk_payload/static/seats/seats.js, apk_payload/templates/ai_console.html |
| item | 20 | android_app/app/src/main/python/static/continue/continue_flow_refresh.js, android_app/app/src/main/python/static/continue/continue_trip_core.js, android_app/app/src/main/python/static/live_map/muavin_live_map_extra.js, android_app/app/src/main/python/static/seats/seats.js, android_app/app/src/main/python/templates/ai_console.html, android_app/app/src/main/python/templates/hesap.html, android_app/app/src/main/python/templates/live_map.html, apk_payload/static/live_map/muavin_live_map_extra.js, apk_payload/static/seats/seats.js, apk_payload/templates/ai_console.html |
| key | 20 | android_app/app/src/main/python/static/continue/continue_flow_refresh.js, android_app/app/src/main/python/static/seats/bags.js, android_app/app/src/main/python/static/seats/drive-controls.js, android_app/app/src/main/python/static/seats/patches/seat-simple-ui-pack.js, android_app/app/src/main/python/static/seats/seats.js, android_app/app/src/main/python/static/seats/voice-commands.js, android_app/app/src/main/python/templates/ai_console.html, apk_payload/static/seats/bags.js, apk_payload/static/seats/drive-controls.js, apk_payload/static/seats/patches/seat-simple-ui-pack.js |
| msg | 20 | android_app/app/src/main/python/static/continue/continue_trip_core.js, android_app/app/src/main/python/static/live_map/muavin_live_map_extra.js, android_app/app/src/main/python/static/seats/seats.js, android_app/app/src/main/python/static/seats/voice-commands.js, android_app/app/src/main/python/static/seats/voice-tts.js, android_app/app/src/main/python/templates/live_map.html, android_app/app/src/main/python/templates/settings_subscription.html, apk_payload/static/live_map/muavin_live_map_extra.js, apk_payload/static/seats/seats.js, apk_payload/static/seats/voice-commands.js |
| closeBtn | 19 | android_app/app/src/main/python/static/continue/continue_trip_core.js, android_app/app/src/main/python/static/continue/continue_trip_ui.js, android_app/app/src/main/python/static/seats/patches/stop-flow-focus-patch.js, android_app/app/src/main/python/templates/hesap.html, android_app/app/src/main/python/templates/index.html, android_app/app/src/main/python/templates/route_schedule_edit.html, android_app/app/src/main/python/templates/settings_subscription.html, apk_payload/static/seats/patches/stop-flow-focus-patch.js, apk_payload/templates/continue_trip.html, apk_payload/templates/hesap.html |
| from | 19 | android_app/app/src/main/python/static/seats/seats.js, android_app/app/src/main/python/static/seats/standing.js, android_app/app/src/main/python/templates/ai_console.html, android_app/app/src/main/python/templates/fare_admin.html, android_app/app/src/main/python/templates/passenger_control.html, android_app/app/src/main/python/templates/trip_report.html, apk_payload/static/seats/seats.js, apk_payload/static/seats/standing.js, apk_payload/templates/ai_console.html, apk_payload/templates/fare_admin.html |
| name | 19 | android_app/app/src/main/python/static/continue/continue_trip_core.js, android_app/app/src/main/python/static/live_map/muavin_live_map_extra.js, android_app/app/src/main/python/static/seats/patches/stop-flow-focus-patch.js, android_app/app/src/main/python/static/seats/seats.js, android_app/app/src/main/python/templates/add_route.html, android_app/app/src/main/python/templates/live_map.html, apk_payload/static/live_map/muavin_live_map_extra.js, apk_payload/static/seats/patches/stop-flow-focus-patch.js, apk_payload/static/seats/seats.js, apk_payload/templates/add_route.html |
| now | 19 | android_app/app/src/main/python/static/continue/continue_flow_refresh.js, android_app/app/src/main/python/static/continue/continue_trip_core.js, android_app/app/src/main/python/static/continue/continue_trip_ui.js, android_app/app/src/main/python/static/live_map/muavin_live_map_extra.js, android_app/app/src/main/python/static/seats/seats-time-prayer.js, android_app/app/src/main/python/static/seats/seats.js, android_app/app/src/main/python/templates/live_map.html, apk_payload/static/live_map/muavin_live_map_extra.js, apk_payload/static/seats/seats-time-prayer.js, apk_payload/static/seats/seats.js |
| title | 19 | android_app/app/src/main/python/static/continue/continue_flow_refresh.js, android_app/app/src/main/python/static/continue/continue_trip_ui.js, android_app/app/src/main/python/static/seats/patches/stop-selected-toast.js, android_app/app/src/main/python/templates/hesap.html, android_app/app/src/main/python/templates/live_map.html, android_app/app/src/main/python/templates/trip_report.html, apk_payload/static/seats/patches/stop-selected-toast.js, apk_payload/templates/continue_trip.html, apk_payload/templates/hesap.html, apk_payload/templates/live_map.html |
| to | 19 | android_app/app/src/main/python/static/seats/seats.js, android_app/app/src/main/python/static/seats/standing.js, android_app/app/src/main/python/templates/ai_console.html, android_app/app/src/main/python/templates/fare_admin.html, android_app/app/src/main/python/templates/passenger_control.html, android_app/app/src/main/python/templates/trip_report.html, apk_payload/static/seats/seats.js, apk_payload/static/seats/standing.js, apk_payload/templates/ai_console.html, apk_payload/templates/fare_admin.html |
| x | 19 | _unused_review/static/vendor/jquery/jquery-3.7.1.min.js, android_app/app/src/main/python/static/live_map/muavin_live_map_extra.js, android_app/app/src/main/python/static/seats/standing.js, android_app/app/src/main/python/static/seats/voice-commands.js, android_app/app/src/main/python/static/vendor/bootstrap/bootstrap.bundle.min.js, android_app/app/src/main/python/templates/live_map.html, android_app/app/src/main/python/templates/reports.html, apk_payload/static/live_map/muavin_live_map_extra.js, apk_payload/static/seats/standing.js, apk_payload/static/seats/voice-commands.js |
| best | 18 | android_app/app/src/main/python/static/live_map/muavin_live_map_extra.js, android_app/app/src/main/python/static/seats/patches/modal-bottom-nav-autohide.js, android_app/app/src/main/python/static/seats/seats.js, android_app/app/src/main/python/static/seats/voice-commands.js, android_app/app/src/main/python/templates/ai_console.html, android_app/app/src/main/python/templates/live_map.html, apk_payload/static/live_map/muavin_live_map_extra.js, apk_payload/static/seats/patches/modal-bottom-nav-autohide.js, apk_payload/static/seats/seats.js, apk_payload/static/seats/voice-commands.js |
| count | 18 | android_app/app/src/main/python/static/seats/patches/modal-bottom-nav-autohide.js, android_app/app/src/main/python/static/seats/seats.js, android_app/app/src/main/python/templates/ai_console.html, android_app/app/src/main/python/templates/hesap.html, android_app/app/src/main/python/templates/route_edit.html, android_app/app/src/main/python/templates/seats_parts/offload_confirm.html, apk_payload/static/seats/patches/modal-bottom-nav-autohide.js, apk_payload/static/seats/seats.js, apk_payload/templates/ai_console.html, apk_payload/templates/hesap.html |
| input | 18 | android_app/app/src/main/python/templates/consignments.html, android_app/app/src/main/python/templates/forgot_password.html, android_app/app/src/main/python/templates/login.html, android_app/app/src/main/python/templates/rehber.html, android_app/app/src/main/python/templates/settings_password.html, android_app/app/src/main/python/templates/settings_subscription.html, apk_payload/templates/consignments.html, apk_payload/templates/forgot_password.html, apk_payload/templates/login.html, apk_payload/templates/rehber.html |
| parts | 18 | android_app/app/src/main/python/static/continue/continue_trip_core.js, android_app/app/src/main/python/static/seats/bags.js, android_app/app/src/main/python/static/seats/seats.js, android_app/app/src/main/python/static/seats/voice-commands.js, android_app/app/src/main/python/templates/add_route.html, android_app/app/src/main/python/templates/live_map.html, apk_payload/static/seats/bags.js, apk_payload/static/seats/seats.js, apk_payload/static/seats/voice-commands.js, apk_payload/templates/add_route.html |
| row | 18 | android_app/app/src/main/python/static/live_map/muavin_live_map_extra.js, android_app/app/src/main/python/static/seats/patches/top-sound-toggle.js, android_app/app/src/main/python/static/seats/seats.js, android_app/app/src/main/python/templates/ai_console.html, android_app/app/src/main/python/templates/fare_admin.html, android_app/app/src/main/python/templates/passenger_control.html, apk_payload/static/live_map/muavin_live_map_extra.js, apk_payload/static/seats/patches/top-sound-toggle.js, apk_payload/static/seats/seats.js, apk_payload/templates/ai_console.html |
| saved | 18 | android_app/app/src/main/python/static/live_map/muavin_live_map_extra.js, android_app/app/src/main/python/static/seats/drive-controls.js, android_app/app/src/main/python/static/seats/voice-commands.js, android_app/app/src/main/python/templates/hesap.html, android_app/app/src/main/python/templates/index.html, android_app/app/src/main/python/templates/reports.html, apk_payload/static/live_map/muavin_live_map_extra.js, apk_payload/static/seats/drive-controls.js, apk_payload/static/seats/voice-commands.js, apk_payload/templates/hesap.html |
| stops | 18 | android_app/app/src/main/python/static/live_map/muavin_live_map_extra.js, android_app/app/src/main/python/static/seats/patches/stop-flow-focus-patch.js, android_app/app/src/main/python/static/seats/seats.js, android_app/app/src/main/python/templates/add_route.html, android_app/app/src/main/python/templates/live_map.html, android_app/app/src/main/python/templates/route_edit.html, apk_payload/static/live_map/muavin_live_map_extra.js, apk_payload/static/seats/patches/stop-flow-focus-patch.js, apk_payload/static/seats/seats.js, apk_payload/templates/add_route.html |
| $ | 16 | _unused_review/static/vendor/jquery/jquery-3.7.1.min.js, android_app/app/src/main/python/static/seats/seats-time-prayer.js, android_app/app/src/main/python/static/seats/seats.js, android_app/app/src/main/python/static/vendor/bootstrap/bootstrap.bundle.min.js, android_app/app/src/main/python/templates/ai_console.html, android_app/app/src/main/python/templates/reports.html, apk_payload/static/seats/seats-time-prayer.js, apk_payload/static/seats/seats.js, apk_payload/static/vendor/bootstrap/bootstrap.bundle.min.js, apk_payload/templates/ai_console.html |
| active | 16 | android_app/app/src/main/python/static/seats/patches/stop-flow-focus-patch.js, android_app/app/src/main/python/static/seats/seats.js, android_app/app/src/main/python/templates/live_map.html, android_app/app/src/main/python/templates/route_schedule_edit.html, android_app/app/src/main/python/templates/seats.html, apk_payload/static/seats/patches/stop-flow-focus-patch.js, apk_payload/static/seats/seats.js, apk_payload/templates/live_map.html, apk_payload/templates/route_schedule_edit.html, apk_payload/templates/seats.html |
| board | 16 | android_app/app/src/main/python/static/live_map/muavin_live_map_extra.js, android_app/app/src/main/python/static/seats/patches/seat-simple-ui-pack.js, android_app/app/src/main/python/static/seats/seats.js, android_app/app/src/main/python/templates/live_map.html, android_app/app/src/main/python/templates/seats.html, apk_payload/static/live_map/muavin_live_map_extra.js, apk_payload/static/seats/patches/seat-simple-ui-pack.js, apk_payload/static/seats/seats.js, apk_payload/templates/live_map.html, apk_payload/templates/seats.html |
| cls | 16 | android_app/app/src/main/python/static/live_map/muavin_live_map_extra.js, android_app/app/src/main/python/static/seats/drive-controls.js, android_app/app/src/main/python/templates/live_map.html, android_app/app/src/main/python/templates/route_edit.html, android_app/app/src/main/python/templates/trip_report.html, apk_payload/static/live_map/muavin_live_map_extra.js, apk_payload/static/seats/drive-controls.js, apk_payload/templates/live_map.html, apk_payload/templates/route_edit.html, apk_payload/templates/trip_report.html |
| current | 16 | android_app/app/src/main/python/static/continue/continue_bag_emanet.js, android_app/app/src/main/python/static/continue/continue_flow_refresh.js, android_app/app/src/main/python/static/continue/continue_trip_core.js, android_app/app/src/main/python/static/seats/patches/seat-simple-ui-pack.js, android_app/app/src/main/python/static/seats/patches/stop-flow-focus-patch.js, android_app/app/src/main/python/static/seats/seats.js, apk_payload/static/seats/patches/seat-simple-ui-pack.js, apk_payload/static/seats/patches/stop-flow-focus-patch.js, apk_payload/static/seats/seats.js, apk_payload/templates/continue_trip.html |
| lat | 16 | android_app/app/src/main/python/static/continue/continue_flow_refresh.js, android_app/app/src/main/python/static/continue/continue_trip_core.js, android_app/app/src/main/python/static/seats/seats.js, android_app/app/src/main/python/templates/live_map.html, android_app/app/src/main/python/templates/route_edit.html, android_app/app/src/main/python/templates/route_stops.html, apk_payload/static/seats/seats.js, apk_payload/templates/live_map.html, apk_payload/templates/route_edit.html, apk_payload/templates/route_stops.html |
| lng | 16 | android_app/app/src/main/python/static/continue/continue_flow_refresh.js, android_app/app/src/main/python/static/continue/continue_trip_core.js, android_app/app/src/main/python/static/seats/seats.js, android_app/app/src/main/python/templates/live_map.html, android_app/app/src/main/python/templates/route_edit.html, android_app/app/src/main/python/templates/route_stops.html, apk_payload/static/seats/seats.js, apk_payload/templates/live_map.html, apk_payload/templates/route_edit.html, apk_payload/templates/route_stops.html |
| route | 16 | android_app/app/src/main/python/static/continue/continue_trip_core.js, android_app/app/src/main/python/static/seats/patches/seat-simple-ui-pack.js, android_app/app/src/main/python/templates/hesap.html, android_app/app/src/main/python/templates/index.html, android_app/app/src/main/python/templates/trip_report.html, apk_payload/static/seats/patches/seat-simple-ui-pack.js, apk_payload/templates/continue_trip.html, apk_payload/templates/hesap.html, apk_payload/templates/index.html, apk_payload/templates/trip_report.html |
| speed | 16 | android_app/app/src/main/python/static/continue/continue_live_diagnostics.js, android_app/app/src/main/python/static/continue/continue_trip_core.js, android_app/app/src/main/python/static/live_map/muavin_live_map_extra.js, android_app/app/src/main/python/static/seats/drive-controls.js, android_app/app/src/main/python/static/seats/patches/seat-simple-ui-pack.js, android_app/app/src/main/python/static/seats/seats.js, apk_payload/static/live_map/muavin_live_map_extra.js, apk_payload/static/seats/drive-controls.js, apk_payload/static/seats/patches/seat-simple-ui-pack.js, apk_payload/static/seats/seats.js |
| tripKey | 16 | android_app/app/src/main/python/static/seats/drive-controls.js, android_app/app/src/main/python/static/seats/patches/manual-ticket-system.js, android_app/app/src/main/python/static/seats/patches/stop-flow-focus-patch.js, android_app/app/src/main/python/templates/continue_trip.html, android_app/app/src/main/python/templates/seats.html, apk_payload/static/seats/drive-controls.js, apk_payload/static/seats/patches/manual-ticket-system.js, apk_payload/static/seats/patches/stop-flow-focus-patch.js, apk_payload/templates/continue_trip.html, apk_payload/templates/seats.html |
| badge | 15 | android_app/app/src/main/python/static/continue/continue_trip_ui.js, android_app/app/src/main/python/static/seats/bags.js, android_app/app/src/main/python/static/seats/patches/stop-flow-focus-patch.js, android_app/app/src/main/python/static/seats/voice-commands.js, android_app/app/src/main/python/templates/live_map.html, apk_payload/static/seats/bags.js, apk_payload/static/seats/patches/stop-flow-focus-patch.js, apk_payload/static/seats/voice-commands.js, apk_payload/templates/continue_trip.html, apk_payload/templates/live_map.html |
| map | 15 | android_app/app/src/main/python/static/live_map/muavin_live_map_extra.js, android_app/app/src/main/python/static/seats/patches/manual-ticket-system.js, android_app/app/src/main/python/static/seats/voice-commands.js, android_app/app/src/main/python/templates/ai_console.html, android_app/app/src/main/python/templates/live_map.html, apk_payload/static/live_map/muavin_live_map_extra.js, apk_payload/static/seats/patches/manual-ticket-system.js, apk_payload/static/seats/voice-commands.js, apk_payload/templates/ai_console.html, apk_payload/templates/live_map.html |
| opt | 15 | android_app/app/src/main/python/static/seats/patches/stop-flow-focus-patch.js, android_app/app/src/main/python/templates/ai_console.html, android_app/app/src/main/python/templates/hesap.html, android_app/app/src/main/python/templates/index.html, android_app/app/src/main/python/templates/route_schedule_edit.html, apk_payload/static/seats/patches/stop-flow-focus-patch.js, apk_payload/templates/ai_console.html, apk_payload/templates/hesap.html, apk_payload/templates/index.html, apk_payload/templates/route_schedule_edit.html |
| p | 15 | _unused_review/static/vendor/jquery/jquery-3.7.1.min.js, android_app/app/src/main/python/static/continue/continue_trip_core.js, android_app/app/src/main/python/static/continue/continue_trip_ui.js, android_app/app/src/main/python/static/live_map/muavin_live_map_extra.js, android_app/app/src/main/python/static/seats/seats.js, android_app/app/src/main/python/templates/reports.html, apk_payload/static/live_map/muavin_live_map_extra.js, apk_payload/static/seats/seats.js, apk_payload/templates/continue_trip.html, apk_payload/templates/reports.html |
| seats | 15 | android_app/app/src/main/python/static/continue/continue_trip_core.js, android_app/app/src/main/python/static/seats/bags.js, android_app/app/src/main/python/static/seats/seats.js, android_app/app/src/main/python/static/seats/voice-commands.js, android_app/app/src/main/python/templates/ai_console.html, apk_payload/static/seats/bags.js, apk_payload/static/seats/seats.js, apk_payload/static/seats/voice-commands.js, apk_payload/templates/ai_console.html, apk_payload/templates/continue_trip.html |
| select | 15 | android_app/app/src/main/python/static/continue/continue_trip_core.js, android_app/app/src/main/python/static/seats/patches/stop-flow-focus-patch.js, android_app/app/src/main/python/templates/hesap.html, android_app/app/src/main/python/templates/index.html, android_app/app/src/main/python/templates/route_schedule_edit.html, apk_payload/static/seats/patches/stop-flow-focus-patch.js, apk_payload/templates/continue_trip.html, apk_payload/templates/hesap.html, apk_payload/templates/index.html, apk_payload/templates/route_schedule_edit.html |
| timer | 15 | android_app/app/src/main/python/static/seats/patches/manual-ticket-system.js, android_app/app/src/main/python/static/seats/patches/seat-layout-fab-pack.js, android_app/app/src/main/python/static/seats/patches/stop-selected-toast.js, android_app/app/src/main/python/static/seats/patches/top-sound-toggle.js, android_app/app/src/main/python/static/seats/voice-tts.js, apk_payload/static/seats/patches/manual-ticket-system.js, apk_payload/static/seats/patches/seat-layout-fab-pack.js, apk_payload/static/seats/patches/stop-selected-toast.js, apk_payload/static/seats/patches/top-sound-toggle.js, apk_payload/static/seats/voice-tts.js |
| bag | 14 | android_app/app/src/main/python/static/continue/continue_bag_emanet.js, android_app/app/src/main/python/static/continue/continue_trip_core.js, android_app/app/src/main/python/static/live_map/muavin_live_map_extra.js, android_app/app/src/main/python/static/seats/seats.js, android_app/app/src/main/python/templates/live_map.html, apk_payload/static/live_map/muavin_live_map_extra.js, apk_payload/static/seats/seats.js, apk_payload/templates/continue_trip.html, apk_payload/templates/live_map.html, static/continue/continue_bag_emanet.js |
| c | 14 | _unused_review/static/vendor/jquery/jquery-3.7.1.min.js, android_app/app/src/main/python/static/continue/continue_flow_refresh.js, android_app/app/src/main/python/static/continue/continue_trip_core.js, android_app/app/src/main/python/static/live_map/muavin_live_map_extra.js, android_app/app/src/main/python/static/seats/seats.js, android_app/app/src/main/python/static/vendor/bootstrap/bootstrap.bundle.min.js, apk_payload/static/live_map/muavin_live_map_extra.js, apk_payload/static/seats/seats.js, apk_payload/static/vendor/bootstrap/bootstrap.bundle.min.js, static/continue/continue_flow_refresh.js |
| km | 14 | android_app/app/src/main/python/static/continue/continue_flow_refresh.js, android_app/app/src/main/python/static/continue/continue_trip_core.js, android_app/app/src/main/python/static/live_map/muavin_live_map_extra.js, android_app/app/src/main/python/static/seats/seats.js, android_app/app/src/main/python/templates/live_map.html, apk_payload/static/live_map/muavin_live_map_extra.js, apk_payload/static/seats/seats.js, apk_payload/templates/continue_trip.html, apk_payload/templates/live_map.html, static/continue/continue_flow_refresh.js |
| label | 14 | android_app/app/src/main/python/static/continue/continue_trip_core.js, android_app/app/src/main/python/static/continue/continue_trip_ui.js, android_app/app/src/main/python/static/seats/patches/manual-ticket-system.js, android_app/app/src/main/python/static/seats/seats.js, android_app/app/src/main/python/templates/route_schedule_edit.html, apk_payload/static/seats/patches/manual-ticket-system.js, apk_payload/static/seats/seats.js, apk_payload/templates/continue_trip.html, apk_payload/templates/route_schedule_edit.html, static/continue/continue_trip_core.js |
| form | 13 | android_app/app/src/main/python/templates/continue_trip.html, android_app/app/src/main/python/templates/hesap.html, android_app/app/src/main/python/templates/route_edit.html, android_app/app/src/main/python/templates/start_trip.html, apk_payload/templates/continue_trip.html, apk_payload/templates/hesap.html, apk_payload/templates/route_edit.html, apk_payload/templates/start_trip.html, templates/continue_trip.html, templates/hesap.html |
| gender | 13 | android_app/app/src/main/python/static/seats/seats.js, android_app/app/src/main/python/static/seats/voice-commands.js, android_app/app/src/main/python/templates/ai_console.html, android_app/app/src/main/python/templates/trip_report.html, apk_payload/static/seats/seats.js, apk_payload/static/seats/voice-commands.js, apk_payload/templates/ai_console.html, apk_payload/templates/trip_report.html, backups/apk_sync_20260520_234501/trip_report.html, static/seats/seats.js |
| items | 13 | android_app/app/src/main/python/static/live_map/muavin_live_map_extra.js, android_app/app/src/main/python/static/seats/seats.js, android_app/app/src/main/python/templates/live_map.html, android_app/app/src/main/python/templates/trip_report.html, apk_payload/static/live_map/muavin_live_map_extra.js, apk_payload/static/seats/seats.js, apk_payload/templates/live_map.html, apk_payload/templates/trip_report.html, backups/apk_sync_20260520_234501/trip_report.html, static/live_map/muavin_live_map_extra.js |
| norm | 13 | android_app/app/src/main/python/static/continue/continue_flow_refresh.js, android_app/app/src/main/python/static/continue/continue_trip_core.js, android_app/app/src/main/python/static/live_map/muavin_live_map_extra.js, android_app/app/src/main/python/static/seats/seats.js, android_app/app/src/main/python/templates/ai_console.html, apk_payload/static/live_map/muavin_live_map_extra.js, apk_payload/static/seats/seats.js, apk_payload/templates/ai_console.html, static/continue/continue_flow_refresh.js, static/continue/continue_trip_core.js |
| pay | 13 | android_app/app/src/main/python/static/app.js, android_app/app/src/main/python/static/seats/seats.js, android_app/app/src/main/python/static/seats/standing.js, android_app/app/src/main/python/templates/trip_report.html, apk_payload/static/app.js, apk_payload/static/seats/seats.js, apk_payload/static/seats/standing.js, apk_payload/templates/trip_report.html, backups/apk_sync_20260520_234501/trip_report.html, static/app.js |
| rows | 13 | android_app/app/src/main/python/templates/ai_console.html, android_app/app/src/main/python/templates/hesap.html, android_app/app/src/main/python/templates/reports.html, android_app/app/src/main/python/templates/trip_report.html, apk_payload/templates/ai_console.html, apk_payload/templates/hesap.html, apk_payload/templates/reports.html, apk_payload/templates/trip_report.html, backups/apk_sync_20260520_234501/trip_report.html, templates/ai_console.html |
| sync | 13 | android_app/app/src/main/python/static/continue/continue_trip_core.js, android_app/app/src/main/python/static/seats/patches/seat-simple-ui-pack.js, android_app/app/src/main/python/templates/hesap.html, android_app/app/src/main/python/templates/seats.html, apk_payload/static/seats/patches/seat-simple-ui-pack.js, apk_payload/templates/continue_trip.html, apk_payload/templates/hesap.html, apk_payload/templates/seats.html, backups/apk_sync_20260520_234501/seats.html, static/continue/continue_trip_core.js |
| v | 13 | _unused_review/static/vendor/jquery/jquery-3.7.1.min.js, android_app/app/src/main/python/static/live_map/muavin_live_map_extra.js, android_app/app/src/main/python/static/seats/patches/stop-flow-focus-patch.js, android_app/app/src/main/python/templates/hesap.html, android_app/app/src/main/python/templates/reports.html, apk_payload/static/live_map/muavin_live_map_extra.js, apk_payload/static/seats/patches/stop-flow-focus-patch.js, apk_payload/templates/hesap.html, apk_payload/templates/reports.html, static/live_map/muavin_live_map_extra.js |
| BOOT | 12 | android_app/app/src/main/python/static/continue/continue_flow_refresh.js, android_app/app/src/main/python/static/continue/continue_live_diagnostics.js, android_app/app/src/main/python/static/continue/continue_trip_core.js, android_app/app/src/main/python/static/seats/seats.js, android_app/app/src/main/python/templates/live_map.html, apk_payload/static/seats/seats.js, apk_payload/templates/live_map.html, static/continue/continue_flow_refresh.js, static/continue/continue_live_diagnostics.js, static/continue/continue_trip_core.js |
| arr | 12 | android_app/app/src/main/python/static/live_map/muavin_live_map_extra.js, android_app/app/src/main/python/static/seats/patches/stop-flow-focus-patch.js, android_app/app/src/main/python/static/seats/seats.js, android_app/app/src/main/python/templates/passenger_control.html, apk_payload/static/live_map/muavin_live_map_extra.js, apk_payload/static/seats/patches/stop-flow-focus-patch.js, apk_payload/static/seats/seats.js, apk_payload/templates/passenger_control.html, static/live_map/muavin_live_map_extra.js, static/seats/patches/stop-flow-focus-patch.js |
| csrf | 12 | android_app/app/src/main/python/static/seats/seats.js, android_app/app/src/main/python/templates/consignments.html, android_app/app/src/main/python/templates/route_stops.html, android_app/app/src/main/python/templates/routes_list.html, apk_payload/static/seats/seats.js, apk_payload/templates/consignments.html, apk_payload/templates/route_stops.html, apk_payload/templates/routes_list.html, static/seats/seats.js, templates/consignments.html |
| done | 12 | android_app/app/src/main/python/static/live_map/muavin_live_map_extra.js, android_app/app/src/main/python/static/seats/patches/manual-ticket-system.js, android_app/app/src/main/python/static/seats/voice-commands.js, android_app/app/src/main/python/templates/passenger_control.html, apk_payload/static/live_map/muavin_live_map_extra.js, apk_payload/static/seats/patches/manual-ticket-system.js, apk_payload/static/seats/voice-commands.js, apk_payload/templates/passenger_control.html, static/live_map/muavin_live_map_extra.js, static/seats/patches/manual-ticket-system.js |
| esc | 12 | android_app/app/src/main/python/static/continue/continue_trip_ui.js, android_app/app/src/main/python/static/live_map/muavin_live_map_extra.js, android_app/app/src/main/python/templates/route_edit.html, android_app/app/src/main/python/templates/trip_report.html, apk_payload/static/live_map/muavin_live_map_extra.js, apk_payload/templates/route_edit.html, apk_payload/templates/trip_report.html, backups/apk_sync_20260520_234501/trip_report.html, static/continue/continue_trip_ui.js, static/live_map/muavin_live_map_extra.js |
| escapeHtml | 12 | android_app/app/src/main/python/static/continue/continue_trip_core.js, android_app/app/src/main/python/templates/ai_console.html, android_app/app/src/main/python/templates/route_edit.html, android_app/app/src/main/python/templates/route_schedule_edit.html, apk_payload/templates/ai_console.html, apk_payload/templates/continue_trip.html, apk_payload/templates/route_edit.html, apk_payload/templates/route_schedule_edit.html, static/continue/continue_trip_core.js, templates/ai_console.html |
| html | 12 | android_app/app/src/main/python/static/continue/continue_trip_ui.js, android_app/app/src/main/python/static/live_map/muavin_live_map_extra.js, android_app/app/src/main/python/templates/live_map.html, android_app/app/src/main/python/templates/trip_report.html, apk_payload/static/live_map/muavin_live_map_extra.js, apk_payload/templates/live_map.html, apk_payload/templates/trip_report.html, backups/apk_sync_20260520_234501/trip_report.html, static/continue/continue_trip_ui.js, static/live_map/muavin_live_map_extra.js |
| obs | 12 | android_app/app/src/main/python/static/seats/patches/manual-ticket-system.js, android_app/app/src/main/python/static/seats/patches/modal-bottom-nav-autohide.js, android_app/app/src/main/python/static/seats/patches/seat-layout-fab-pack.js, android_app/app/src/main/python/static/seats/patches/top-sound-toggle.js, apk_payload/static/seats/patches/manual-ticket-system.js, apk_payload/static/seats/patches/modal-bottom-nav-autohide.js, apk_payload/static/seats/patches/seat-layout-fab-pack.js, apk_payload/static/seats/patches/top-sound-toggle.js, static/seats/patches/manual-ticket-system.js, static/seats/patches/modal-bottom-nav-autohide.js |
| ok | 12 | android_app/app/src/main/python/static/seats/seats.js, android_app/app/src/main/python/static/seats/voice-commands.js, android_app/app/src/main/python/templates/continue_trip.html, android_app/app/src/main/python/templates/hesap.html, apk_payload/static/seats/seats.js, apk_payload/static/seats/voice-commands.js, apk_payload/templates/continue_trip.html, apk_payload/templates/hesap.html, static/seats/seats.js, static/seats/voice-commands.js |
| on | 12 | android_app/app/src/main/python/static/seats/drive-controls.js, android_app/app/src/main/python/static/seats/patches/top-sound-toggle.js, android_app/app/src/main/python/static/seats/voice-tts.js, android_app/app/src/main/python/static/vendor/bootstrap/bootstrap.bundle.min.js, apk_payload/static/seats/drive-controls.js, apk_payload/static/seats/patches/top-sound-toggle.js, apk_payload/static/seats/voice-tts.js, apk_payload/static/vendor/bootstrap/bootstrap.bundle.min.js, static/seats/drive-controls.js, static/seats/patches/top-sound-toggle.js |
| parcel | 12 | android_app/app/src/main/python/static/live_map/muavin_live_map_extra.js, android_app/app/src/main/python/static/seats/seats.js, android_app/app/src/main/python/templates/ai_console.html, android_app/app/src/main/python/templates/live_map.html, apk_payload/static/live_map/muavin_live_map_extra.js, apk_payload/static/seats/seats.js, apk_payload/templates/ai_console.html, apk_payload/templates/live_map.html, static/live_map/muavin_live_map_extra.js, static/seats/seats.js |
| raw | 12 | android_app/app/src/main/python/static/continue/continue_trip_core.js, android_app/app/src/main/python/static/seats/patches/manual-ticket-system.js, android_app/app/src/main/python/static/seats/seats.js, android_app/app/src/main/python/templates/start_trip.html, apk_payload/static/seats/patches/manual-ticket-system.js, apk_payload/static/seats/seats.js, apk_payload/templates/continue_trip.html, apk_payload/templates/start_trip.html, static/continue/continue_trip_core.js, static/seats/patches/manual-ticket-system.js |
| selected | 12 | android_app/app/src/main/python/static/continue/continue_trip_core.js, android_app/app/src/main/python/static/seats/seats.js, android_app/app/src/main/python/static/seats/standing.js, android_app/app/src/main/python/static/seats/voice-commands.js, apk_payload/static/seats/seats.js, apk_payload/static/seats/standing.js, apk_payload/static/seats/voice-commands.js, apk_payload/templates/continue_trip.html, static/continue/continue_trip_core.js, static/seats/seats.js |
| show | 12 | android_app/app/src/main/python/static/seats/seats.js, android_app/app/src/main/python/templates/forgot_password.html, android_app/app/src/main/python/templates/login.html, android_app/app/src/main/python/templates/settings_password.html, apk_payload/static/seats/seats.js, apk_payload/templates/forgot_password.html, apk_payload/templates/login.html, apk_payload/templates/settings_password.html, static/seats/seats.js, templates/forgot_password.html |
| closeModal | 11 | android_app/app/src/main/python/static/seats/seats.js, android_app/app/src/main/python/templates/continue_trip.html, android_app/app/src/main/python/templates/reports.html, android_app/app/src/main/python/templates/settings_subscription.html, apk_payload/static/seats/seats.js, apk_payload/templates/continue_trip.html, apk_payload/templates/reports.html, apk_payload/templates/settings_subscription.html, static/seats/seats.js, templates/continue_trip.html |
| live | 11 | android_app/app/src/main/python/static/continue/continue_trip_core.js, android_app/app/src/main/python/static/seats/seats.js, android_app/app/src/main/python/static/seats/standing.js, android_app/app/src/main/python/static/seats/voice-commands.js, apk_payload/static/seats/seats.js, apk_payload/static/seats/standing.js, apk_payload/static/seats/voice-commands.js, static/continue/continue_trip_core.js, static/seats/seats.js, static/seats/standing.js |
| liveStop | 11 | android_app/app/src/main/python/static/continue/continue_live_diagnostics.js, android_app/app/src/main/python/static/seats/drive-controls.js, android_app/app/src/main/python/static/seats/seats.js, android_app/app/src/main/python/templates/live_map.html, apk_payload/static/seats/drive-controls.js, apk_payload/static/seats/seats.js, apk_payload/templates/live_map.html, static/continue/continue_live_diagnostics.js, static/seats/drive-controls.js, static/seats/seats.js |
| openModal | 11 | android_app/app/src/main/python/static/seats/seats.js, android_app/app/src/main/python/templates/continue_trip.html, android_app/app/src/main/python/templates/reports.html, android_app/app/src/main/python/templates/settings_subscription.html, apk_payload/static/seats/seats.js, apk_payload/templates/continue_trip.html, apk_payload/templates/reports.html, apk_payload/templates/settings_subscription.html, static/seats/seats.js, templates/continue_trip.html |
| render | 11 | android_app/app/src/main/python/static/continue/continue_trip_ui.js, android_app/app/src/main/python/static/live_map/muavin_live_map_extra.js, android_app/app/src/main/python/static/seats/seats-time-prayer.js, android_app/app/src/main/python/templates/onboarding.html, apk_payload/static/live_map/muavin_live_map_extra.js, apk_payload/static/seats/seats-time-prayer.js, apk_payload/templates/onboarding.html, static/continue/continue_trip_ui.js, static/live_map/muavin_live_map_extra.js, static/seats/seats-time-prayer.js |
| schedule | 11 | android_app/app/src/main/python/static/continue/continue_trip_core.js, android_app/app/src/main/python/static/seats/patches/manual-ticket-system.js, android_app/app/src/main/python/static/seats/patches/seat-layout-fab-pack.js, android_app/app/src/main/python/static/seats/patches/top-sound-toggle.js, apk_payload/static/seats/patches/manual-ticket-system.js, apk_payload/static/seats/patches/seat-layout-fab-pack.js, apk_payload/static/seats/patches/top-sound-toggle.js, static/continue/continue_trip_core.js, static/seats/patches/manual-ticket-system.js, static/seats/patches/seat-layout-fab-pack.js |
| trVoice | 11 | android_app/app/src/main/python/static/continue/continue_trip_core.js, android_app/app/src/main/python/static/seats/seats.js, android_app/app/src/main/python/static/seats/voice-commands.js, android_app/app/src/main/python/static/seats/voice-tts.js, apk_payload/static/seats/seats.js, apk_payload/static/seats/voice-commands.js, apk_payload/static/seats/voice-tts.js, static/continue/continue_trip_core.js, static/seats/seats.js, static/seats/voice-commands.js |
| voices | 11 | android_app/app/src/main/python/static/continue/continue_trip_core.js, android_app/app/src/main/python/static/seats/seats.js, android_app/app/src/main/python/static/seats/voice-commands.js, android_app/app/src/main/python/static/seats/voice-tts.js, apk_payload/static/seats/seats.js, apk_payload/static/seats/voice-commands.js, apk_payload/static/seats/voice-tts.js, static/continue/continue_trip_core.js, static/seats/seats.js, static/seats/voice-commands.js |
| R | 10 | android_app/app/src/main/python/static/continue/continue_flow_refresh.js, android_app/app/src/main/python/static/continue/continue_trip_core.js, android_app/app/src/main/python/static/live_map/muavin_live_map_extra.js, android_app/app/src/main/python/static/seats/seats.js, apk_payload/static/live_map/muavin_live_map_extra.js, apk_payload/static/seats/seats.js, static/continue/continue_flow_refresh.js, static/continue/continue_trip_core.js, static/live_map/muavin_live_map_extra.js, static/seats/seats.js |
| ai | 10 | android_app/app/src/main/python/static/seats/seats.js, android_app/app/src/main/python/static/vendor/bootstrap/bootstrap.bundle.min.js, android_app/app/src/main/python/templates/seats.html, apk_payload/static/seats/seats.js, apk_payload/static/vendor/bootstrap/bootstrap.bundle.min.js, apk_payload/templates/seats.html, backups/apk_sync_20260520_234501/seats.html, static/seats/seats.js, static/vendor/bootstrap/bootstrap.bundle.min.js, templates/seats.html |
| amount | 10 | android_app/app/src/main/python/static/seats/seats.js, android_app/app/src/main/python/templates/ai_console.html, android_app/app/src/main/python/templates/trip_report.html, apk_payload/static/seats/seats.js, apk_payload/templates/ai_console.html, apk_payload/templates/trip_report.html, backups/apk_sync_20260520_234501/trip_report.html, static/seats/seats.js, templates/ai_console.html, templates/trip_report.html |
| dLat | 10 | android_app/app/src/main/python/static/continue/continue_flow_refresh.js, android_app/app/src/main/python/static/continue/continue_trip_core.js, android_app/app/src/main/python/static/live_map/muavin_live_map_extra.js, android_app/app/src/main/python/static/seats/seats.js, apk_payload/static/live_map/muavin_live_map_extra.js, apk_payload/static/seats/seats.js, static/continue/continue_flow_refresh.js, static/continue/continue_trip_core.js, static/live_map/muavin_live_map_extra.js, static/seats/seats.js |
| dLng | 10 | android_app/app/src/main/python/static/continue/continue_flow_refresh.js, android_app/app/src/main/python/static/continue/continue_trip_core.js, android_app/app/src/main/python/static/live_map/muavin_live_map_extra.js, android_app/app/src/main/python/static/seats/seats.js, apk_payload/static/live_map/muavin_live_map_extra.js, apk_payload/static/seats/seats.js, static/continue/continue_flow_refresh.js, static/continue/continue_trip_core.js, static/live_map/muavin_live_map_extra.js, static/seats/seats.js |
| f | 10 | _unused_review/static/vendor/jquery/jquery-3.7.1.min.js, android_app/app/src/main/python/static/vendor/bootstrap/bootstrap.bundle.min.js, android_app/app/src/main/python/templates/consignments.html, android_app/app/src/main/python/templates/fare_query.html, apk_payload/static/vendor/bootstrap/bootstrap.bundle.min.js, apk_payload/templates/consignments.html, apk_payload/templates/fare_query.html, static/vendor/bootstrap/bootstrap.bundle.min.js, templates/consignments.html, templates/fare_query.html |
| l | 10 | _unused_review/static/vendor/jquery/jquery-3.7.1.min.js, android_app/app/src/main/python/static/seats/seats.js, android_app/app/src/main/python/static/vendor/bootstrap/bootstrap.bundle.min.js, android_app/app/src/main/python/templates/reports.html, apk_payload/static/seats/seats.js, apk_payload/static/vendor/bootstrap/bootstrap.bundle.min.js, apk_payload/templates/reports.html, static/seats/seats.js, static/vendor/bootstrap/bootstrap.bundle.min.js, templates/reports.html |
| no | 10 | android_app/app/src/main/python/static/seats/patches/manual-ticket-system.js, android_app/app/src/main/python/static/seats/seats.js, android_app/app/src/main/python/templates/trip_report.html, apk_payload/static/seats/patches/manual-ticket-system.js, apk_payload/static/seats/seats.js, apk_payload/templates/trip_report.html, backups/apk_sync_20260520_234501/trip_report.html, static/seats/patches/manual-ticket-system.js, static/seats/seats.js, templates/trip_report.html |
| b | 9 | android_app/app/src/main/python/static/continue/continue_bag_emanet.js, android_app/app/src/main/python/static/live_map/muavin_live_map_extra.js, android_app/app/src/main/python/static/seats/patches/manual-ticket-system.js, apk_payload/static/live_map/muavin_live_map_extra.js, apk_payload/static/seats/patches/manual-ticket-system.js, static/continue/continue_bag_emanet.js, static/live_map/muavin_live_map_extra.js, static/seats/patches/manual-ticket-system.js, templates/settings_password.html |
| backdrop | 9 | android_app/app/src/main/python/templates/hesap.html, android_app/app/src/main/python/templates/index.html, android_app/app/src/main/python/templates/passenger_control.html, apk_payload/templates/hesap.html, apk_payload/templates/index.html, apk_payload/templates/passenger_control.html, templates/hesap.html, templates/index.html, templates/passenger_control.html |
| base | 9 | android_app/app/src/main/python/static/seats/seats.js, android_app/app/src/main/python/templates/ai_console.html, android_app/app/src/main/python/templates/index.html, apk_payload/static/seats/seats.js, apk_payload/templates/ai_console.html, apk_payload/templates/index.html, static/seats/seats.js, templates/ai_console.html, templates/index.html |
| cards | 9 | android_app/app/src/main/python/static/continue/continue_flow_refresh.js, android_app/app/src/main/python/templates/hesap.html, android_app/app/src/main/python/templates/rehber.html, apk_payload/templates/hesap.html, apk_payload/templates/rehber.html, static/continue/continue_flow_refresh.js, templates/hesap.html, templates/rehber.html, templates/report_archive.html |
| cnt | 9 | android_app/app/src/main/python/static/seats/bags.js, android_app/app/src/main/python/static/seats/seats.js, android_app/app/src/main/python/static/seats/standing.js, apk_payload/static/seats/bags.js, apk_payload/static/seats/seats.js, apk_payload/static/seats/standing.js, static/seats/bags.js, static/seats/seats.js, static/seats/standing.js |
| dir | 9 | android_app/app/src/main/python/static/seats/bags.js, android_app/app/src/main/python/static/seats/seats.js, android_app/app/src/main/python/templates/hesap.html, apk_payload/static/seats/bags.js, apk_payload/static/seats/seats.js, apk_payload/templates/hesap.html, static/seats/bags.js, static/seats/seats.js, templates/hesap.html |
| empty | 9 | android_app/app/src/main/python/static/seats/patches/seat-simple-ui-pack.js, android_app/app/src/main/python/static/seats/seats.js, android_app/app/src/main/python/templates/ai_console.html, apk_payload/static/seats/patches/seat-simple-ui-pack.js, apk_payload/static/seats/seats.js, apk_payload/templates/ai_console.html, static/seats/patches/seat-simple-ui-pack.js, static/seats/seats.js, templates/ai_console.html |
| ensureButton | 9 | android_app/app/src/main/python/static/live_map/muavin_live_map_extra.js, android_app/app/src/main/python/static/seats/patches/seat-simple-ui-pack.js, android_app/app/src/main/python/static/seats/patches/top-sound-toggle.js, apk_payload/static/live_map/muavin_live_map_extra.js, apk_payload/static/seats/patches/seat-simple-ui-pack.js, apk_payload/static/seats/patches/top-sound-toggle.js, static/live_map/muavin_live_map_extra.js, static/seats/patches/seat-simple-ui-pack.js, static/seats/patches/top-sound-toggle.js |
| filled | 9 | android_app/app/src/main/python/static/seats/patches/seat-simple-ui-pack.js, android_app/app/src/main/python/static/seats/seats.js, android_app/app/src/main/python/templates/passenger_control.html, apk_payload/static/seats/patches/seat-simple-ui-pack.js, apk_payload/static/seats/seats.js, apk_payload/templates/passenger_control.html, static/seats/patches/seat-simple-ui-pack.js, static/seats/seats.js, templates/passenger_control.html |
| fmtTL | 9 | android_app/app/src/main/python/static/seats/seats.js, android_app/app/src/main/python/templates/ai_console.html, android_app/app/src/main/python/templates/reports.html, apk_payload/static/seats/seats.js, apk_payload/templates/ai_console.html, apk_payload/templates/reports.html, static/seats/seats.js, templates/ai_console.html, templates/reports.html |
| hist | 9 | android_app/app/src/main/python/static/continue/continue_trip_core.js, android_app/app/src/main/python/static/seats/seats.js, android_app/app/src/main/python/templates/trip_report.html, apk_payload/static/seats/seats.js, apk_payload/templates/trip_report.html, backups/apk_sync_20260520_234501/trip_report.html, static/continue/continue_trip_core.js, static/seats/seats.js, templates/trip_report.html |
| last | 9 | android_app/app/src/main/python/static/live_map/muavin_live_map_extra.js, android_app/app/src/main/python/static/seats/bags.js, android_app/app/src/main/python/templates/live_map.html, apk_payload/static/live_map/muavin_live_map_extra.js, apk_payload/static/seats/bags.js, apk_payload/templates/live_map.html, static/live_map/muavin_live_map_extra.js, static/seats/bags.js, templates/live_map.html |
| left | 9 | android_app/app/src/main/python/static/seats/patches/seat-layout-fab-pack.js, android_app/app/src/main/python/static/seats/seats.js, android_app/app/src/main/python/templates/passenger_control.html, apk_payload/static/seats/patches/seat-layout-fab-pack.js, apk_payload/static/seats/seats.js, apk_payload/templates/passenger_control.html, static/seats/patches/seat-layout-fab-pack.js, static/seats/seats.js, templates/passenger_control.html |
| listEl | 9 | android_app/app/src/main/python/static/live_map/muavin_live_map_extra.js, android_app/app/src/main/python/templates/live_map.html, android_app/app/src/main/python/templates/route_schedule_edit.html, apk_payload/static/live_map/muavin_live_map_extra.js, apk_payload/templates/live_map.html, apk_payload/templates/route_schedule_edit.html, static/live_map/muavin_live_map_extra.js, templates/live_map.html, templates/route_schedule_edit.html |
| main | 9 | android_app/app/src/main/python/static/seats/drive-eta-chip.js, android_app/app/src/main/python/static/seats/patches/stop-flow-focus-patch.js, android_app/app/src/main/python/static/seats/seats-time-prayer.js, apk_payload/static/seats/drive-eta-chip.js, apk_payload/static/seats/patches/stop-flow-focus-patch.js, apk_payload/static/seats/seats-time-prayer.js, static/seats/drive-eta-chip.js, static/seats/patches/stop-flow-focus-patch.js, static/seats/seats-time-prayer.js |
| meta | 9 | android_app/app/src/main/python/static/seats/bags.js, android_app/app/src/main/python/static/seats/patches/stop-flow-focus-patch.js, android_app/app/src/main/python/templates/passenger_control.html, apk_payload/static/seats/bags.js, apk_payload/static/seats/patches/stop-flow-focus-patch.js, apk_payload/templates/passenger_control.html, static/seats/bags.js, static/seats/patches/stop-flow-focus-patch.js, templates/passenger_control.html |

## 10) Python Fonksiyon Tekrarları

### Aynı dosya içinde
| Fonksiyon | Tekrar | Dosya |
| --- | --- | --- |
| norm_stop | 5 | app.py |
| norm_stop | 5 | apk_payload/app.py |
| norm_stop | 5 | backups/apk_sync_20260520_234501/app.py |
| norm_stop | 5 | android_app/app/src/main/python/app.py |
| _bag_count_from_meta | 3 | app.py |
| _bag_count_from_meta | 3 | apk_payload/app.py |
| _bag_count_from_meta | 3 | backups/apk_sync_20260520_234501/app.py |
| _bag_count_from_meta | 3 | android_app/app/src/main/python/app.py |
| find_route_stop | 3 | app.py |
| find_route_stop | 3 | apk_payload/app.py |
| find_route_stop | 3 | backups/apk_sync_20260520_234501/app.py |
| find_route_stop | 3 | android_app/app/src/main/python/app.py |
| stop_key | 3 | app.py |
| stop_key | 3 | apk_payload/app.py |
| stop_key | 3 | backups/apk_sync_20260520_234501/app.py |
| stop_key | 3 | android_app/app/src/main/python/app.py |

### Farklı dosyalarda
| Fonksiyon | Dosya sayısı | Dosyalar |
| --- | --- | --- |
| rel | 16 | tools/audit_auto_live_stop.py, tools/audit_live_patches.py, tools/audit_patches.py, tools/live_flow_target_audit.py, tools/live_flow_v2_audit.py, tools/muavin_audit_step1.py, tools/muavin_audit_step2.py, tools/muavin_audit_step3_flask_routes.py, tools/muavin_audit_step4_suspicious_context.py, tools/muavin_audit_step5_active_bug_context.py |
| read | 13 | tools/audit_auto_live_stop.py, tools/audit_live_patches.py, tools/live_flow_target_audit.py, tools/live_flow_v2_audit.py, tools/muavin_audit_step2.py, tools/muavin_audit_step3_flask_routes.py, tools/muavin_audit_step4_suspicious_context.py, tools/muavin_audit_step5_active_bug_context.py, tools/muavin_audit_step7_global_appjs.py, tools/muavin_audit_step8_appjs_impact.py |
| section | 9 | tools/muavin_audit_step2.py, tools/muavin_audit_step3_flask_routes.py, tools/muavin_audit_step4_suspicious_context.py, tools/muavin_audit_step5_active_bug_context.py, tools/muavin_audit_step6_runtime_smoke.py, tools/muavin_audit_step6b_runtime_smoke_fixed.py, tools/muavin_audit_step7_global_appjs.py, tools/muavin_audit_step8_appjs_impact.py, tools/muavin_audit_step9_sync_plan.py |
| group_for | 8 | android_app/app/src/main/python/app.py, android_app/app/src/main/python/modules/trip_report_builder.py, apk_payload/app.py, apk_payload/modules/trip_report_builder.py, app.py, backups/apk_sync_20260520_234501/app.py, backups/apk_sync_20260520_234501/trip_report_builder.py, modules/trip_report_builder.py |
| norm_stop | 8 | android_app/app/src/main/python/app.py, android_app/app/src/main/python/modules/coords_panel.py, apk_payload/app.py, apk_payload/modules/coords_panel.py, app.py, backups/apk_sync_20260520_234501/app.py, modules/coords_panel.py, tools/build_route_segments.py |
| _trip_key_from_row | 7 | android_app/app/src/main/python/app.py, android_app/app/src/main/python/modules/ai_panel.py, apk_payload/app.py, apk_payload/modules/ai_panel.py, app.py, backups/apk_sync_20260520_234501/app.py, modules/ai_panel.py |
| add | 7 | android_app/app/src/main/python/modules/coords_panel.py, android_app/app/src/main/python/modules/trip_report_builder.py, apk_payload/modules/coords_panel.py, apk_payload/modules/trip_report_builder.py, backups/apk_sync_20260520_234501/trip_report_builder.py, modules/coords_panel.py, modules/trip_report_builder.py |
| clear_bags_for_seat | 7 | android_app/app/src/main/python/app.py, android_app/app/src/main/python/modules/ai_panel.py, apk_payload/app.py, apk_payload/modules/ai_panel.py, app.py, backups/apk_sync_20260520_234501/app.py, modules/ai_panel.py |
| stop_key | 7 | android_app/app/src/main/python/app.py, android_app/app/src/main/python/modules/ai_panel.py, apk_payload/app.py, apk_payload/modules/ai_panel.py, app.py, backups/apk_sync_20260520_234501/app.py, modules/ai_panel.py |
| _bag_count_from_meta | 4 | android_app/app/src/main/python/app.py, apk_payload/app.py, app.py, backups/apk_sync_20260520_234501/app.py |
| _report_slug | 4 | android_app/app/src/main/python/modules/trip_report_builder.py, apk_payload/modules/trip_report_builder.py, backups/apk_sync_20260520_234501/trip_report_builder.py, modules/trip_report_builder.py |
| _row_dict | 4 | android_app/app/src/main/python/app.py, apk_payload/app.py, app.py, backups/apk_sync_20260520_234501/app.py |
| _rv | 4 | android_app/app/src/main/python/app.py, apk_payload/app.py, app.py, backups/apk_sync_20260520_234501/app.py |
| _seat_event_meta | 4 | android_app/app/src/main/python/app.py, apk_payload/app.py, app.py, backups/apk_sync_20260520_234501/app.py |
| _walkon_event_meta | 4 | android_app/app/src/main/python/app.py, apk_payload/app.py, app.py, backups/apk_sync_20260520_234501/app.py |
| admin_profile_exists | 4 | android_app/app/src/main/python/app.py, apk_payload/app.py, app.py, backups/apk_sync_20260520_234501/app.py |
| ai_console_page | 4 | android_app/app/src/main/python/app.py, apk_payload/app.py, app.py, backups/apk_sync_20260520_234501/app.py |
| ai_extract_seat_list | 4 | android_app/app/src/main/python/app.py, apk_payload/app.py, app.py, backups/apk_sync_20260520_234501/app.py |
| ai_find_learned_match | 4 | android_app/app/src/main/python/app.py, apk_payload/app.py, app.py, backups/apk_sync_20260520_234501/app.py |
| ai_make_skeleton | 4 | android_app/app/src/main/python/app.py, apk_payload/app.py, app.py, backups/apk_sync_20260520_234501/app.py |
| all_files | 4 | tools/audit_live_patches.py, tools/muavin_audit_step2.py, tools/muavin_audit_step3_flask_routes.py, tools/muavin_audit_step4_suspicious_context.py |
| all_route_names | 4 | android_app/app/src/main/python/app.py, apk_payload/app.py, app.py, backups/apk_sync_20260520_234501/app.py |
| allowed_file | 4 | android_app/app/src/main/python/app.py, apk_payload/app.py, app.py, backups/apk_sync_20260520_234501/app.py |
| api_archived_trip_report | 4 | android_app/app/src/main/python/app.py, apk_payload/app.py, app.py, backups/apk_sync_20260520_234501/app.py |
| api_bags_meta | 4 | android_app/app/src/main/python/app.py, apk_payload/app.py, app.py, backups/apk_sync_20260520_234501/app.py |
| api_live_consignment_deliver | 4 | android_app/app/src/main/python/app.py, apk_payload/app.py, app.py, backups/apk_sync_20260520_234501/app.py |
| api_live_consignment_detail | 4 | android_app/app/src/main/python/app.py, apk_payload/app.py, app.py, backups/apk_sync_20260520_234501/app.py |
| api_live_runtime_state | 4 | android_app/app/src/main/python/app.py, apk_payload/app.py, app.py, backups/apk_sync_20260520_234501/app.py |
| api_live_seat_bag_detail | 4 | android_app/app/src/main/python/app.py, apk_payload/app.py, app.py, backups/apk_sync_20260520_234501/app.py |
| api_live_seat_destination | 4 | android_app/app/src/main/python/app.py, apk_payload/app.py, app.py, backups/apk_sync_20260520_234501/app.py |
| api_live_seat_offload | 4 | android_app/app/src/main/python/app.py, apk_payload/app.py, app.py, backups/apk_sync_20260520_234501/app.py |
| api_live_stop_complete | 4 | android_app/app/src/main/python/app.py, apk_payload/app.py, app.py, backups/apk_sync_20260520_234501/app.py |
| api_live_stop_detail | 4 | android_app/app/src/main/python/app.py, apk_payload/app.py, app.py, backups/apk_sync_20260520_234501/app.py |
| api_live_stop_offload | 4 | android_app/app/src/main/python/app.py, apk_payload/app.py, app.py, backups/apk_sync_20260520_234501/app.py |
| api_report_archive | 4 | android_app/app/src/main/python/app.py, apk_payload/app.py, app.py, backups/apk_sync_20260520_234501/app.py |
| api_seat | 4 | android_app/app/src/main/python/modules/seats_panel.py, apk_payload/modules/seats_panel.py, backups/apk_sync_20260520_234501/seats_panel.py, modules/seats_panel.py |
| api_seats_bulk | 4 | android_app/app/src/main/python/modules/seats_panel.py, apk_payload/modules/seats_panel.py, backups/apk_sync_20260520_234501/seats_panel.py, modules/seats_panel.py |
| api_seats_gender | 4 | android_app/app/src/main/python/modules/seats_panel.py, apk_payload/modules/seats_panel.py, backups/apk_sync_20260520_234501/seats_panel.py, modules/seats_panel.py |
| api_seats_list | 4 | android_app/app/src/main/python/modules/seats_panel.py, apk_payload/modules/seats_panel.py, backups/apk_sync_20260520_234501/seats_panel.py, modules/seats_panel.py |
| api_seats_offload | 4 | android_app/app/src/main/python/modules/seats_panel.py, apk_payload/modules/seats_panel.py, backups/apk_sync_20260520_234501/seats_panel.py, modules/seats_panel.py |
| api_seats_service | 4 | android_app/app/src/main/python/modules/seats_panel.py, apk_payload/modules/seats_panel.py, backups/apk_sync_20260520_234501/seats_panel.py, modules/seats_panel.py |
| api_standing | 4 | android_app/app/src/main/python/app.py, apk_payload/app.py, app.py, backups/apk_sync_20260520_234501/app.py |
| api_standing_list | 4 | android_app/app/src/main/python/app.py, apk_payload/app.py, app.py, backups/apk_sync_20260520_234501/app.py |
| api_stats | 4 | android_app/app/src/main/python/app.py, apk_payload/app.py, app.py, backups/apk_sync_20260520_234501/app.py |
| api_stoplog | 4 | android_app/app/src/main/python/app.py, apk_payload/app.py, app.py, backups/apk_sync_20260520_234501/app.py |
| api_trip_report | 4 | android_app/app/src/main/python/app.py, apk_payload/app.py, app.py, backups/apk_sync_20260520_234501/app.py |
| api_walkon | 4 | android_app/app/src/main/python/app.py, apk_payload/app.py, app.py, backups/apk_sync_20260520_234501/app.py |
| archived_trip_report_page | 4 | android_app/app/src/main/python/app.py, apk_payload/app.py, app.py, backups/apk_sync_20260520_234501/app.py |
| bags_clear_alias | 4 | android_app/app/src/main/python/app.py, apk_payload/app.py, app.py, backups/apk_sync_20260520_234501/app.py |
| bootstrap_and_guard | 4 | android_app/app/src/main/python/app.py, apk_payload/app.py, app.py, backups/apk_sync_20260520_234501/app.py |
| build_trip_report_payload_for_trip | 4 | android_app/app/src/main/python/modules/trip_report_builder.py, apk_payload/modules/trip_report_builder.py, backups/apk_sync_20260520_234501/trip_report_builder.py, modules/trip_report_builder.py |
| check_csrf | 4 | android_app/app/src/main/python/app.py, apk_payload/app.py, app.py, backups/apk_sync_20260520_234501/app.py |
| close_db | 4 | android_app/app/src/main/python/app.py, apk_payload/app.py, app.py, backups/apk_sync_20260520_234501/app.py |
| continue_trip | 4 | android_app/app/src/main/python/app.py, apk_payload/app.py, app.py, backups/apk_sync_20260520_234501/app.py |
| css_rules | 4 | tools/audit_live_patches.py, tools/audit_patches.py, tools/seats_css_override_audit.py, tools/seats_external_override_audit.py |
| delete_walkon_rows | 4 | android_app/app/src/main/python/app.py, apk_payload/app.py, app.py, backups/apk_sync_20260520_234501/app.py |
| dev_no_cache_headers | 4 | android_app/app/src/main/python/app.py, apk_payload/app.py, app.py, backups/apk_sync_20260520_234501/app.py |
| end_trip | 4 | android_app/app/src/main/python/app.py, apk_payload/app.py, app.py, backups/apk_sync_20260520_234501/app.py |
| ensure_admin_profile_table | 4 | android_app/app/src/main/python/app.py, apk_payload/app.py, app.py, backups/apk_sync_20260520_234501/app.py |
| ensure_list | 4 | android_app/app/src/main/python/app.py, apk_payload/app.py, app.py, backups/apk_sync_20260520_234501/app.py |
| ensure_live_runtime_state_table | 4 | android_app/app/src/main/python/app.py, apk_payload/app.py, app.py, backups/apk_sync_20260520_234501/app.py |
| ensure_schema | 4 | android_app/app/src/main/python/app.py, apk_payload/app.py, app.py, backups/apk_sync_20260520_234501/app.py |
| ensure_security_table | 4 | android_app/app/src/main/python/app.py, apk_payload/app.py, app.py, backups/apk_sync_20260520_234501/app.py |
| ensure_upload_dir | 4 | android_app/app/src/main/python/app.py, apk_payload/app.py, app.py, backups/apk_sync_20260520_234501/app.py |
| env_bool | 4 | android_app/app/src/main/python/app.py, apk_payload/app.py, app.py, backups/apk_sync_20260520_234501/app.py |
| fetch_live_runtime_state | 4 | android_app/app/src/main/python/app.py, apk_payload/app.py, app.py, backups/apk_sync_20260520_234501/app.py |
| finalize_remaining_trip_events | 4 | android_app/app/src/main/python/modules/trip_report_builder.py, apk_payload/modules/trip_report_builder.py, backups/apk_sync_20260520_234501/trip_report_builder.py, modules/trip_report_builder.py |
| find_route_stop | 4 | android_app/app/src/main/python/app.py, apk_payload/app.py, app.py, backups/apk_sync_20260520_234501/app.py |
| format_tl | 4 | android_app/app/src/main/python/app.py, apk_payload/app.py, app.py, backups/apk_sync_20260520_234501/app.py |
| get_active_trip | 4 | android_app/app/src/main/python/app.py, apk_payload/app.py, app.py, backups/apk_sync_20260520_234501/app.py |
| get_active_trip_row | 4 | android_app/app/src/main/python/app.py, apk_payload/app.py, app.py, backups/apk_sync_20260520_234501/app.py |
| get_admin_password_hash | 4 | android_app/app/src/main/python/app.py, apk_payload/app.py, app.py, backups/apk_sync_20260520_234501/app.py |
| get_admin_profile | 4 | android_app/app/src/main/python/app.py, apk_payload/app.py, app.py, backups/apk_sync_20260520_234501/app.py |
| get_cash_categories | 4 | android_app/app/src/main/python/app.py, apk_payload/app.py, app.py, backups/apk_sync_20260520_234501/app.py |
| get_csrf | 4 | android_app/app/src/main/python/app.py, apk_payload/app.py, app.py, backups/apk_sync_20260520_234501/app.py |
| get_db | 4 | android_app/app/src/main/python/app.py, apk_payload/app.py, app.py, backups/apk_sync_20260520_234501/app.py |
| get_recovery_code_hash | 4 | android_app/app/src/main/python/app.py, apk_payload/app.py, app.py, backups/apk_sync_20260520_234501/app.py |
| get_stops | 4 | android_app/app/src/main/python/app.py, apk_payload/app.py, app.py, backups/apk_sync_20260520_234501/app.py |
| index | 4 | android_app/app/src/main/python/app.py, apk_payload/app.py, app.py, backups/apk_sync_20260520_234501/app.py |
| inject_admin_profile | 4 | android_app/app/src/main/python/app.py, apk_payload/app.py, app.py, backups/apk_sync_20260520_234501/app.py |
| inject_globals | 4 | android_app/app/src/main/python/app.py, apk_payload/app.py, app.py, backups/apk_sync_20260520_234501/app.py |
| is_excluded_path | 4 | android_app/app/src/main/python/app.py, apk_payload/app.py, app.py, backups/apk_sync_20260520_234501/app.py |
| issue_csrf | 4 | android_app/app/src/main/python/app.py, apk_payload/app.py, app.py, backups/apk_sync_20260520_234501/app.py |
| latest_trip_report_redirect | 4 | android_app/app/src/main/python/app.py, apk_payload/app.py, app.py, backups/apk_sync_20260520_234501/app.py |
| live_map_page | 4 | android_app/app/src/main/python/app.py, apk_payload/app.py, app.py, backups/apk_sync_20260520_234501/app.py |
| log_trip_stop_event | 4 | android_app/app/src/main/python/app.py, apk_payload/app.py, app.py, backups/apk_sync_20260520_234501/app.py |
| main | 4 | tools/add_route_via.py, tools/build_route_segments.py, tools/geo_pipeline.py, tools/make_soy_agaci_satirli.py |
| make_recovery_code | 4 | android_app/app/src/main/python/app.py, apk_payload/app.py, app.py, backups/apk_sync_20260520_234501/app.py |
| make_stop_payload | 4 | android_app/app/src/main/python/app.py, apk_payload/app.py, app.py, backups/apk_sync_20260520_234501/app.py |
| neighbor_rule_ok | 4 | android_app/app/src/main/python/app.py, apk_payload/app.py, app.py, backups/apk_sync_20260520_234501/app.py |
| norm_bool | 4 | android_app/app/src/main/python/app.py, apk_payload/app.py, app.py, backups/apk_sync_20260520_234501/app.py |
| norm_gender | 4 | android_app/app/src/main/python/app.py, apk_payload/app.py, app.py, backups/apk_sync_20260520_234501/app.py |
| norm_payment | 4 | android_app/app/src/main/python/app.py, apk_payload/app.py, app.py, backups/apk_sync_20260520_234501/app.py |
| norm_ticket_type | 4 | android_app/app/src/main/python/app.py, apk_payload/app.py, app.py, backups/apk_sync_20260520_234501/app.py |
| normalize_ai_text | 4 | android_app/app/src/main/python/app.py, apk_payload/app.py, app.py, backups/apk_sync_20260520_234501/app.py |
| normalize_hhmm | 4 | android_app/app/src/main/python/app.py, apk_payload/app.py, app.py, backups/apk_sync_20260520_234501/app.py |
| normalize_recovery_code | 4 | android_app/app/src/main/python/app.py, apk_payload/app.py, app.py, backups/apk_sync_20260520_234501/app.py |
| onboarding_page | 4 | android_app/app/src/main/python/app.py, apk_payload/app.py, app.py, backups/apk_sync_20260520_234501/app.py |
| parse_float | 4 | android_app/app/src/main/python/app.py, apk_payload/app.py, app.py, backups/apk_sync_20260520_234501/app.py |
| parse_int | 4 | android_app/app/src/main/python/app.py, apk_payload/app.py, app.py, backups/apk_sync_20260520_234501/app.py |
| parse_int_list | 4 | android_app/app/src/main/python/app.py, apk_payload/app.py, app.py, backups/apk_sync_20260520_234501/app.py |
| parse_lines | 4 | android_app/app/src/main/python/app.py, apk_payload/app.py, app.py, backups/apk_sync_20260520_234501/app.py |
| parse_stops | 4 | android_app/app/src/main/python/app.py, apk_payload/app.py, app.py, backups/apk_sync_20260520_234501/app.py |
| passenger_control | 4 | android_app/app/src/main/python/modules/seats_panel.py, apk_payload/modules/seats_panel.py, backups/apk_sync_20260520_234501/seats_panel.py, modules/seats_panel.py |
| read_text | 4 | tools/audit_files.py, tools/audit_patches.py, tools/muavin_full_audit_v1.py, tools/project_tree_audit.py |
| register_seats_routes | 4 | android_app/app/src/main/python/modules/seats_panel.py, apk_payload/modules/seats_panel.py, backups/apk_sync_20260520_234501/seats_panel.py, modules/seats_panel.py |
| register_trip_report_builder | 4 | android_app/app/src/main/python/modules/trip_report_builder.py, apk_payload/modules/trip_report_builder.py, backups/apk_sync_20260520_234501/trip_report_builder.py, modules/trip_report_builder.py |
| rehber_page | 4 | android_app/app/src/main/python/app.py, apk_payload/app.py, app.py, backups/apk_sync_20260520_234501/app.py |
| report_archive_page | 4 | android_app/app/src/main/python/app.py, apk_payload/app.py, app.py, backups/apk_sync_20260520_234501/app.py |
| report_file_download | 4 | android_app/app/src/main/python/app.py, apk_payload/app.py, app.py, backups/apk_sync_20260520_234501/app.py |
| reports_dir_path | 4 | android_app/app/src/main/python/app.py, apk_payload/app.py, app.py, backups/apk_sync_20260520_234501/app.py |
| reset_admin_owner | 4 | android_app/app/src/main/python/app.py, apk_payload/app.py, app.py, backups/apk_sync_20260520_234501/app.py |
| safe | 4 | android_app/app/src/main/python/modules/bags/__init__.py, apk_payload/modules/bags/__init__.py, modules/bags/__init__.py, tools/seat_count_audit.py |
| safe_report_base | 4 | android_app/app/src/main/python/app.py, apk_payload/app.py, app.py, backups/apk_sync_20260520_234501/app.py |
| save_admin_profile | 4 | android_app/app/src/main/python/app.py, apk_payload/app.py, app.py, backups/apk_sync_20260520_234501/app.py |
| save_cash_categories | 4 | android_app/app/src/main/python/app.py, apk_payload/app.py, app.py, backups/apk_sync_20260520_234501/app.py |
| save_finished_trip_report | 4 | android_app/app/src/main/python/modules/trip_report_builder.py, apk_payload/modules/trip_report_builder.py, backups/apk_sync_20260520_234501/trip_report_builder.py, modules/trip_report_builder.py |
| save_profile_photo | 4 | android_app/app/src/main/python/app.py, apk_payload/app.py, app.py, backups/apk_sync_20260520_234501/app.py |
| schedule_default_profile_for_route | 4 | android_app/app/src/main/python/app.py, apk_payload/app.py, app.py, backups/apk_sync_20260520_234501/app.py |
| schedule_editor_rows | 4 | android_app/app/src/main/python/app.py, apk_payload/app.py, app.py, backups/apk_sync_20260520_234501/app.py |

## 11) CSS Selector Tekrarları
| Selector | Tekrar | Dosyalar |
| --- | --- | --- |
| .btn | 180 | _unused_review/static/seats/seats-redesign.css, _unused_review/trafik_isigi/trafik.html, android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-final.css, android_app/app/src/main/python/static/seats/seats-final.css, android_app/app/src/main/python/static/seats/seats.css, android_app/app/src/main/python/static/vendor/bootstrap/bootstrap.min.css, android_app/app/src/main/python/templates/add_route.html, android_app/app/src/main/python/templates/ai_console.html |
| .active | 159 | _unused_review/static/seats/seats-redesign.css, android_app/app/src/main/python/static/continue/css_parts/30-sheet-bag-photo.css, android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-final.css, android_app/app/src/main/python/static/seats/seats-final.css, android_app/app/src/main/python/static/seats/seats.css, android_app/app/src/main/python/static/vendor/bootstrap/bootstrap.min.css, android_app/app/src/main/python/templates/ai_console.html, android_app/app/src/main/python/templates/hesap.html |
| #driveModeToggle | 92 | _unused_review/static/seats/seats-redesign.css, android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-final.css, android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-tone.css, android_app/app/src/main/python/static/seats/seats-final.css, android_app/app/src/main/python/static/seats/seats.css, android_app/app/src/main/python/templates/seats.html, apk_payload/static/seats/_archive_theme_trials/seats-dashboard-final.css, apk_payload/static/seats/_archive_theme_trials/seats-dashboard-tone.css |
| .card | 90 | android_app/app/src/main/python/static/continue/css_parts/00-base-legacy.css, android_app/app/src/main/python/static/continue/css_parts/10-compact-timeline-hero.css, android_app/app/src/main/python/static/vendor/bootstrap/bootstrap.min.css, android_app/app/src/main/python/templates/add_route.html, android_app/app/src/main/python/templates/events.html, android_app/app/src/main/python/templates/fare_admin.html, android_app/app/src/main/python/templates/fare_query.html, android_app/app/src/main/python/templates/forgot_password.html |
| .hero | 89 | android_app/app/src/main/python/static/continue/css_parts/00-base-legacy.css, android_app/app/src/main/python/static/continue/css_parts/10-compact-timeline-hero.css, android_app/app/src/main/python/templates/ai_console.html, android_app/app/src/main/python/templates/forgot_password.html, android_app/app/src/main/python/templates/report_archive.html, android_app/app/src/main/python/templates/route_schedule_edit.html, android_app/app/src/main/python/templates/settings_backup.html, android_app/app/src/main/python/templates/settings_package_requests.html |
| .primary | 87 | _unused_review/static/seats/seats-redesign.css, android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-final.css, android_app/app/src/main/python/static/seats/patches/seat-layout-fab-pack.css, android_app/app/src/main/python/static/seats/patches/seat-simple-ui-pack.css, android_app/app/src/main/python/static/seats/seats.css, android_app/app/src/main/python/templates/add_route.html, android_app/app/src/main/python/templates/events.html, android_app/app/src/main/python/templates/fare_admin.html |
| .deck | 82 | android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-final.css, android_app/app/src/main/python/static/seats/patches/right-seat-column-spacing-fix.css, android_app/app/src/main/python/static/seats/patches/seat-layout-fab-pack.css, android_app/app/src/main/python/static/seats/seats-final.css, android_app/app/src/main/python/static/seats/seats.css, android_app/app/src/main/python/templates/passenger_control.html, apk_payload/static/seats/_archive_theme_trials/seats-dashboard-final.css, apk_payload/static/seats/patches/right-seat-column-spacing-fix.css |
| .voice-command-btn | 80 | _unused_review/static/seats/seats-redesign.css, android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-final.css, android_app/app/src/main/python/static/seats/seats-final.css, android_app/app/src/main/python/static/seats/seats.css, apk_payload/static/seats/_archive_theme_trials/seats-dashboard-final.css, apk_payload/static/seats/seats-final.css, apk_payload/static/seats/seats.css, static/seats/_archive_theme_trials/seats-dashboard-final.css |
| .mini-chip | 77 | _unused_review/static/seats/seats-redesign.css, android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-final.css, android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-tone.css, android_app/app/src/main/python/static/seats/seats-final.css, android_app/app/src/main/python/static/seats/seats.css, apk_payload/static/seats/_archive_theme_trials/seats-dashboard-final.css, apk_payload/static/seats/_archive_theme_trials/seats-dashboard-tone.css, apk_payload/static/seats/seats-final.css |
| .v | 77 | _unused_review/static/seats/seats-redesign.css, android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-final.css, android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-tone.css, android_app/app/src/main/python/static/seats/seats-final.css, android_app/app/src/main/python/static/seats/seats.css, android_app/app/src/main/python/templates/ai_console.html, android_app/app/src/main/python/templates/passenger_control.html, android_app/app/src/main/python/templates/reports.html |
| #driveInlineDock | 74 | _unused_review/static/seats/seats-redesign.css, android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-final.css, android_app/app/src/main/python/static/seats/patches/mobile-performance-fix.css, android_app/app/src/main/python/static/seats/seats-final.css, android_app/app/src/main/python/static/seats/seats.css, android_app/app/src/main/python/templates/seats.html, apk_payload/static/seats/_archive_theme_trials/seats-dashboard-final.css, apk_payload/static/seats/patches/mobile-performance-fix.css |
| .board-head | 74 | _unused_review/static/seats/seats-redesign.css, android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-final.css, android_app/app/src/main/python/static/seats/patches/seat-simple-ui-pack.css, android_app/app/src/main/python/static/seats/seats-final.css, android_app/app/src/main/python/static/seats/seats.css, android_app/app/src/main/python/templates/seats.html, apk_payload/static/seats/_archive_theme_trials/seats-dashboard-final.css, apk_payload/static/seats/patches/seat-simple-ui-pack.css |
| .voice-row | 73 | _unused_review/static/seats/seats-redesign.css, android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-final.css, android_app/app/src/main/python/static/seats/seats-final.css, android_app/app/src/main/python/static/seats/seats.css, apk_payload/static/seats/_archive_theme_trials/seats-dashboard-final.css, apk_payload/static/seats/seats-final.css, apk_payload/static/seats/seats.css, static/seats/_archive_theme_trials/seats-dashboard-final.css |
| .legend | 64 | _unused_review/static/seats/seats-redesign.css, android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-final.css, android_app/app/src/main/python/static/seats/patches/seat-simple-ui-pack.css, android_app/app/src/main/python/static/seats/seats-final.css, android_app/app/src/main/python/static/seats/seats.css, android_app/app/src/main/python/templates/live_map.html, android_app/app/src/main/python/templates/reports.html, android_app/app/src/main/python/templates/trip_report.html |
| .board-stage | 63 | _unused_review/static/seats/seats-redesign.css, android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-final.css, android_app/app/src/main/python/static/seats/seats-final.css, android_app/app/src/main/python/static/seats/seats.css, apk_payload/static/seats/_archive_theme_trials/seats-dashboard-final.css, apk_payload/static/seats/seats-final.css, apk_payload/static/seats/seats.css, static/seats/_archive_theme_trials/seats-dashboard-final.css |
| .fab | 59 | _unused_review/static/vendor/fa/all.min.css, android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-final.css, android_app/app/src/main/python/static/seats/patches/seat-layout-fab-pack.css, android_app/app/src/main/python/static/seats/seats-final.css, android_app/app/src/main/python/static/seats/seats.css, apk_payload/static/seats/_archive_theme_trials/seats-dashboard-final.css, apk_payload/static/seats/patches/seat-layout-fab-pack.css, apk_payload/static/seats/seats-final.css |
| .k | 59 | _unused_review/static/seats/seats-redesign.css, android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-final.css, android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-tone.css, android_app/app/src/main/python/static/seats/seats-final.css, android_app/app/src/main/python/static/seats/seats.css, android_app/app/src/main/python/templates/ai_console.html, android_app/app/src/main/python/templates/passenger_control.html, android_app/app/src/main/python/templates/reports.html |
| .show | 59 | android_app/app/src/main/python/static/continue/css_parts/00-base-legacy.css, android_app/app/src/main/python/static/seats/patches/stop-selected-toast.css, android_app/app/src/main/python/static/vendor/bootstrap/bootstrap.min.css, android_app/app/src/main/python/templates/index.html, android_app/app/src/main/python/templates/live_map.html, android_app/app/src/main/python/templates/route_schedule_edit.html, android_app/app/src/main/python/templates/seats_parts/finish_trip_modal.html, android_app/app/src/main/python/templates/seats_parts/offload_confirm.html |
| .warn | 59 | _unused_review/static/seats/seats-redesign.css, android_app/app/src/main/python/static/continue/css_parts/20-live-stop-sheet-base.css, android_app/app/src/main/python/static/live_map/muavin_live_map_extra.css, android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-final.css, android_app/app/src/main/python/static/seats/patches/seat-simple-ui-pack.css, android_app/app/src/main/python/static/seats/seats.css, android_app/app/src/main/python/templates/ai_console.html, android_app/app/src/main/python/templates/hesap.html |
| .label | 57 | _unused_review/trafik_isigi/trafik.html, android_app/app/src/main/python/static/seats/patches/seat-label-ghost-clean.css, android_app/app/src/main/python/static/seats/seats-final.css, android_app/app/src/main/python/static/seats/seats.css, android_app/app/src/main/python/static/style.css, android_app/app/src/main/python/templates/fare_admin.html, android_app/app/src/main/python/templates/fare_query.html, android_app/app/src/main/python/templates/hesap.html |
| .shell | 57 | android_app/app/src/main/python/static/continue/css_parts/00-base-legacy.css, android_app/app/src/main/python/static/continue/css_parts/10-compact-timeline-hero.css, android_app/app/src/main/python/static/continue/css_parts/50-live-v2-top-glow.css, android_app/app/src/main/python/templates/forgot_password.html, android_app/app/src/main/python/templates/live_map.html, android_app/app/src/main/python/templates/settings_backup.html, android_app/app/src/main/python/templates/settings_package_requests.html, android_app/app/src/main/python/templates/settings_password.html |
| .live | 55 | android_app/app/src/main/python/static/continue/css_parts/00-base-legacy.css, android_app/app/src/main/python/static/continue/css_parts/10-compact-timeline-hero.css, android_app/app/src/main/python/static/continue/css_parts/50-live-v2-top-glow.css, android_app/app/src/main/python/templates/live_map.html, apk_payload/templates/continue_trip.html, apk_payload/templates/live_map.html, static/continue/css_parts/00-base-legacy.css, static/continue/css_parts/10-compact-timeline-hero.css |
| .map-speed-badge | 54 | android_app/app/src/main/python/static/live_map/muavin_live_map_extra.css, android_app/app/src/main/python/templates/live_map.html, apk_payload/static/live_map/muavin_live_map_extra.css, apk_payload/templates/live_map.html, static/live_map/muavin_live_map_extra.css, templates/live_map.html |
| .voice-state | 54 | _unused_review/static/seats/seats-redesign.css, android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-final.css, android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-tone.css, android_app/app/src/main/python/static/seats/seats-final.css, android_app/app/src/main/python/static/seats/seats.css, apk_payload/static/seats/_archive_theme_trials/seats-dashboard-final.css, apk_payload/static/seats/_archive_theme_trials/seats-dashboard-tone.css, apk_payload/static/seats/seats-final.css |
| .green | 52 | _unused_review/static/seats/seats-redesign.css, android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-final.css, android_app/app/src/main/python/static/seats/patches/seat-layout-fab-pack.css, android_app/app/src/main/python/static/seats/seats.css, android_app/app/src/main/python/templates/consignments.html, android_app/app/src/main/python/templates/fare_admin.html, android_app/app/src/main/python/templates/fare_query.html, android_app/app/src/main/python/templates/passenger_control.html |
| .selected-stop-chip | 50 | _unused_review/static/seats/seats-redesign.css, android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-final.css, android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-tone.css, android_app/app/src/main/python/static/seats/patches/seat-simple-ui-pack.css, android_app/app/src/main/python/static/seats/seats-final.css, android_app/app/src/main/python/static/seats/seats.css, apk_payload/static/seats/_archive_theme_trials/seats-dashboard-final.css, apk_payload/static/seats/_archive_theme_trials/seats-dashboard-tone.css |
| #driveSpeedChip | 48 | android_app/app/src/main/python/static/seats/seats-final.css, android_app/app/src/main/python/static/seats/seats.css, apk_payload/static/seats/seats-final.css, apk_payload/static/seats/seats.css, static/seats/seats-final.css, static/seats/seats.css |
| .glass | 48 | android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-final.css, android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-tone.css, android_app/app/src/main/python/static/seats/patches/fab-sheet-solid-fix.css, android_app/app/src/main/python/static/seats/seats-final.css, android_app/app/src/main/python/static/seats/seats.css, android_app/app/src/main/python/templates/ai_console.html, android_app/app/src/main/python/templates/route_schedule_edit.html, apk_payload/static/seats/_archive_theme_trials/seats-dashboard-final.css |
| .nav-link | 48 | android_app/app/src/main/python/static/vendor/bootstrap/bootstrap.min.css, apk_payload/static/vendor/bootstrap/bootstrap.min.css, static/vendor/bootstrap/bootstrap.min.css |
| .actions | 46 | android_app/app/src/main/python/templates/consignments.html, android_app/app/src/main/python/templates/forgot_password.html, android_app/app/src/main/python/templates/no_active_trip.html, android_app/app/src/main/python/templates/onboarding.html, android_app/app/src/main/python/templates/report_archive.html, android_app/app/src/main/python/templates/settings_password.html, android_app/app/src/main/python/templates/settings_profile.html, android_app/app/src/main/python/templates/settings_recovery.html |
| .drive-eta-chip | 44 | _unused_review/static/seats/seats-redesign.css, android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-final.css, android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-tone.css, android_app/app/src/main/python/static/seats/patches/mobile-performance-fix.css, android_app/app/src/main/python/static/seats/seats-final.css, android_app/app/src/main/python/static/seats/seats.css, android_app/app/src/main/python/templates/seats.html, apk_payload/static/seats/_archive_theme_trials/seats-dashboard-final.css |
| .layout | 44 | _unused_review/static/seats/seats-redesign.css, android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-final.css, android_app/app/src/main/python/static/seats/patches/seat-simple-ui-pack.css, android_app/app/src/main/python/static/seats/seats-final.css, android_app/app/src/main/python/static/seats/seats.css, android_app/app/src/main/python/templates/ai_console.html, android_app/app/src/main/python/templates/route_schedule_edit.html, apk_payload/static/seats/_archive_theme_trials/seats-dashboard-final.css |
| .ok | 43 | android_app/app/src/main/python/static/continue/css_parts/10-compact-timeline-hero.css, android_app/app/src/main/python/static/seats/patches/seat-simple-ui-pack.css, android_app/app/src/main/python/static/seats/seats.css, android_app/app/src/main/python/templates/ai_console.html, android_app/app/src/main/python/templates/forgot_password.html, android_app/app/src/main/python/templates/live_map.html, android_app/app/src/main/python/templates/passenger_control.html, android_app/app/src/main/python/templates/route_stops.html |
| .status-pill | 42 | android_app/app/src/main/python/static/continue/css_parts/00-base-legacy.css, android_app/app/src/main/python/static/continue/css_parts/10-compact-timeline-hero.css, android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-final.css, android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-tone.css, android_app/app/src/main/python/static/seats/seats-final.css, android_app/app/src/main/python/static/seats/seats.css, android_app/app/src/main/python/templates/passenger_control.html, apk_payload/static/seats/_archive_theme_trials/seats-dashboard-final.css |
| .empty | 41 | android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-final.css, android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-tone.css, android_app/app/src/main/python/static/seats/seats-final.css, android_app/app/src/main/python/static/seats/seats.css, android_app/app/src/main/python/static/style.css, android_app/app/src/main/python/templates/report_archive.html, android_app/app/src/main/python/templates/route_schedule_edit.html, android_app/app/src/main/python/templates/settings_backup.html |
| .muted | 40 | _unused_review/static/seats/seats-redesign.css, android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-final.css, android_app/app/src/main/python/static/seats/patches/fab-sheet-solid-fix.css, android_app/app/src/main/python/static/seats/seats-final.css, android_app/app/src/main/python/static/seats/seats.css, android_app/app/src/main/python/templates/add_route.html, android_app/app/src/main/python/templates/fare_admin.html, android_app/app/src/main/python/templates/fare_query.html |
| .danger | 39 | _unused_review/static/seats/seats-redesign.css, android_app/app/src/main/python/static/continue/css_parts/20-live-stop-sheet-base.css, android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-final.css, android_app/app/src/main/python/static/seats/patches/seat-simple-ui-pack.css, android_app/app/src/main/python/static/seats/seats-final.css, android_app/app/src/main/python/static/seats/seats.css, android_app/app/src/main/python/templates/ai_console.html, android_app/app/src/main/python/templates/events.html |
| .route-stop | 39 | android_app/app/src/main/python/static/seats/seats-final.css, android_app/app/src/main/python/static/seats/seats.css, apk_payload/static/seats/seats-final.css, apk_payload/static/seats/seats.css, static/seats/seats-final.css, static/seats/seats.css |
| .showing | 39 | android_app/app/src/main/python/static/vendor/bootstrap/bootstrap.min.css, apk_payload/static/vendor/bootstrap/bootstrap.min.css, static/vendor/bootstrap/bootstrap.min.css |
| .board-head-right | 38 | _unused_review/static/seats/seats-redesign.css, android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-final.css, android_app/app/src/main/python/static/seats/seats-final.css, android_app/app/src/main/python/static/seats/seats.css, apk_payload/static/seats/_archive_theme_trials/seats-dashboard-final.css, apk_payload/static/seats/seats-final.css, apk_payload/static/seats/seats.css, static/seats/_archive_theme_trials/seats-dashboard-final.css |
| .box | 38 | android_app/app/src/main/python/templates/add_route.html, android_app/app/src/main/python/templates/events.html, android_app/app/src/main/python/templates/hesap.html, android_app/app/src/main/python/templates/no_active_trip.html, android_app/app/src/main/python/templates/package_required.html, android_app/app/src/main/python/templates/reports.html, android_app/app/src/main/python/templates/trip_report.html, apk_payload/templates/add_route.html |
| .card-title | 38 | android_app/app/src/main/python/static/continue/css_parts/00-base-legacy.css, android_app/app/src/main/python/static/continue/css_parts/10-compact-timeline-hero.css, android_app/app/src/main/python/static/continue/css_parts/50-live-v2-top-glow.css, android_app/app/src/main/python/static/vendor/bootstrap/bootstrap.min.css, android_app/app/src/main/python/templates/consignments.html, android_app/app/src/main/python/templates/route_schedule_edit.html, apk_payload/static/vendor/bootstrap/bootstrap.min.css, apk_payload/templates/consignments.html |
| .seats-shell | 38 | _unused_review/static/seats/seats-redesign.css, android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-final.css, android_app/app/src/main/python/static/seats/patches/seat-simple-ui-pack.css, android_app/app/src/main/python/static/seats/seats-final.css, android_app/app/src/main/python/static/seats/seats.css, apk_payload/static/seats/_archive_theme_trials/seats-dashboard-final.css, apk_payload/static/seats/patches/seat-simple-ui-pack.css, apk_payload/static/seats/seats-final.css |
| .chip | 36 | android_app/app/src/main/python/templates/ai_console.html, android_app/app/src/main/python/templates/hesap.html, android_app/app/src/main/python/templates/passenger_control.html, android_app/app/src/main/python/templates/route_schedule_edit.html, apk_payload/templates/ai_console.html, apk_payload/templates/hesap.html, apk_payload/templates/passenger_control.html, apk_payload/templates/route_schedule_edit.html |
| .night-voice-toggle | 36 | android_app/app/src/main/python/static/seats/seats.css, apk_payload/static/seats/seats.css, static/seats/seats.css |
| .offcanvas-body | 36 | android_app/app/src/main/python/static/vendor/bootstrap/bootstrap.min.css, apk_payload/static/vendor/bootstrap/bootstrap.min.css, static/vendor/bootstrap/bootstrap.min.css |
| .offcanvas-header | 36 | android_app/app/src/main/python/static/vendor/bootstrap/bootstrap.min.css, apk_payload/static/vendor/bootstrap/bootstrap.min.css, static/vendor/bootstrap/bootstrap.min.css |
| .right | 36 | android_app/app/src/main/python/static/style.css, android_app/app/src/main/python/templates/add_route.html, android_app/app/src/main/python/templates/hesap.html, android_app/app/src/main/python/templates/rehber.html, android_app/app/src/main/python/templates/reports.html, apk_payload/static/style.css, apk_payload/templates/add_route.html, apk_payload/templates/hesap.html |
| .route-pill | 36 | android_app/app/src/main/python/static/seats/patches/seat-simple-ui-pack.css, android_app/app/src/main/python/static/seats/seats-final.css, android_app/app/src/main/python/static/seats/seats.css, android_app/app/src/main/python/templates/route_edit.html, apk_payload/static/seats/patches/seat-simple-ui-pack.css, apk_payload/static/seats/seats-final.css, apk_payload/static/seats/seats.css, apk_payload/templates/route_edit.html |
| .route-sub | 36 | android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-final.css, android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-tone.css, android_app/app/src/main/python/static/seats/seats-final.css, android_app/app/src/main/python/static/seats/seats.css, android_app/app/src/main/python/templates/routes_list.html, apk_payload/static/seats/_archive_theme_trials/seats-dashboard-final.css, apk_payload/static/seats/_archive_theme_trials/seats-dashboard-tone.css, apk_payload/static/seats/seats-final.css |
| .route-title | 36 | android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-final.css, android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-tone.css, android_app/app/src/main/python/static/seats/seats-final.css, android_app/app/src/main/python/static/seats/seats.css, apk_payload/static/seats/_archive_theme_trials/seats-dashboard-final.css, apk_payload/static/seats/_archive_theme_trials/seats-dashboard-tone.css, apk_payload/static/seats/seats-final.css, apk_payload/static/seats/seats.css |
| .board-inner | 35 | _unused_review/static/seats/seats-redesign.css, android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-final.css, android_app/app/src/main/python/static/seats/patches/seat-simple-ui-pack.css, android_app/app/src/main/python/static/seats/seats-final.css, android_app/app/src/main/python/static/seats/seats.css, android_app/app/src/main/python/templates/seats.html, apk_payload/static/seats/_archive_theme_trials/seats-dashboard-final.css, apk_payload/static/seats/patches/seat-simple-ui-pack.css |
| .next | 34 | android_app/app/src/main/python/static/continue/css_parts/00-base-legacy.css, android_app/app/src/main/python/static/continue/css_parts/10-compact-timeline-hero.css, android_app/app/src/main/python/static/continue/css_parts/50-live-v2-top-glow.css, android_app/app/src/main/python/templates/live_map.html, android_app/app/src/main/python/templates/onboarding.html, apk_payload/templates/continue_trip.html, apk_payload/templates/live_map.html, apk_payload/templates/onboarding.html |
| .fab-column | 33 | android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-final.css, android_app/app/src/main/python/static/seats/patches/fab-sheet-solid-fix.css, android_app/app/src/main/python/static/seats/seats-final.css, android_app/app/src/main/python/static/seats/seats.css, apk_payload/static/seats/_archive_theme_trials/seats-dashboard-final.css, apk_payload/static/seats/patches/fab-sheet-solid-fix.css, apk_payload/static/seats/seats-final.css, apk_payload/static/seats/seats.css |
| .map-fullscreen-btn | 33 | android_app/app/src/main/python/static/live_map/muavin_live_map_extra.css, android_app/app/src/main/python/templates/live_map.html, apk_payload/static/live_map/muavin_live_map_extra.css, apk_payload/templates/live_map.html, static/live_map/muavin_live_map_extra.css, templates/live_map.html |
| .map-route-status | 33 | android_app/app/src/main/python/templates/live_map.html, apk_payload/templates/live_map.html, templates/live_map.html |
| .seat | 33 | android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-final.css, android_app/app/src/main/python/static/seats/patches/manual-ticket-system.css, android_app/app/src/main/python/static/seats/seats-final.css, android_app/app/src/main/python/static/seats/seats.css, android_app/app/src/main/python/static/style.css, android_app/app/src/main/python/templates/passenger_control.html, android_app/app/src/main/python/templates/reports.html, apk_payload/static/seats/_archive_theme_trials/seats-dashboard-final.css |
| .summary-grid | 33 | _unused_review/static/seats/seats-redesign.css, android_app/app/src/main/python/static/live_map/muavin_live_map_extra.css, android_app/app/src/main/python/templates/ai_console.html, android_app/app/src/main/python/templates/routes_list.html, android_app/app/src/main/python/templates/trip_report.html, apk_payload/static/live_map/muavin_live_map_extra.css, apk_payload/templates/ai_console.html, apk_payload/templates/routes_list.html |
| .field | 31 | _unused_review/static/seats/seats-redesign.css, android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-final.css, android_app/app/src/main/python/static/seats/seats.css, android_app/app/src/main/python/templates/ai_console.html, android_app/app/src/main/python/templates/forgot_password.html, android_app/app/src/main/python/templates/login.html, android_app/app/src/main/python/templates/route_schedule_edit.html, android_app/app/src/main/python/templates/settings_password.html |
| .ghost | 31 | _unused_review/static/seats/seats-redesign.css, android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-final.css, android_app/app/src/main/python/static/seats/seats.css, android_app/app/src/main/python/templates/ai_console.html, android_app/app/src/main/python/templates/hesap.html, android_app/app/src/main/python/templates/no_active_trip.html, android_app/app/src/main/python/templates/rehber.html, android_app/app/src/main/python/templates/route_schedule_edit.html |
| .ico | 30 | android_app/app/src/main/python/static/seats/patches/bottom-voice-command.css, android_app/app/src/main/python/static/seats/patches/seat-simple-ui-pack.css, android_app/app/src/main/python/templates/index.html, apk_payload/static/seats/patches/bottom-voice-command.css, apk_payload/static/seats/patches/seat-simple-ui-pack.css, apk_payload/templates/index.html, static/seats/patches/bottom-voice-command.css, static/seats/patches/seat-simple-ui-pack.css |
| .muavin-locate-control | 30 | android_app/app/src/main/python/static/live_map/muavin_live_map_extra.css, apk_payload/static/live_map/muavin_live_map_extra.css, static/live_map/muavin_live_map_extra.css |
| .name | 30 | android_app/app/src/main/python/static/seats/seats-final.css, android_app/app/src/main/python/static/seats/seats.css, apk_payload/static/seats/seats-final.css, apk_payload/static/seats/seats.css, static/seats/seats-final.css, static/seats/seats.css |
| .route-live-row | 30 | android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-final.css, android_app/app/src/main/python/static/seats/seats-final.css, android_app/app/src/main/python/static/seats/seats.css, apk_payload/static/seats/_archive_theme_trials/seats-dashboard-final.css, apk_payload/static/seats/seats-final.css, apk_payload/static/seats/seats.css, static/seats/_archive_theme_trials/seats-dashboard-final.css, static/seats/seats-final.css |
| .route-strip-shell | 30 | android_app/app/src/main/python/static/seats/seats-final.css, android_app/app/src/main/python/static/seats/seats.css, apk_payload/static/seats/seats-final.css, apk_payload/static/seats/seats.css, static/seats/seats-final.css, static/seats/seats.css |
| .timeline | 30 | android_app/app/src/main/python/static/continue/css_parts/00-base-legacy.css, android_app/app/src/main/python/static/continue/css_parts/10-compact-timeline-hero.css, android_app/app/src/main/python/static/continue/css_parts/50-live-v2-top-glow.css, android_app/app/src/main/python/templates/trip_report.html, apk_payload/templates/continue_trip.html, apk_payload/templates/trip_report.html, backups/apk_sync_20260520_234501/trip_report.html, static/continue/css_parts/00-base-legacy.css |
| #driveModeActionsDock | 29 | android_app/app/src/main/python/static/seats/patches/seat-simple-ui-pack.css, android_app/app/src/main/python/static/seats/seats-final.css, android_app/app/src/main/python/templates/seats.html, apk_payload/static/seats/patches/seat-simple-ui-pack.css, apk_payload/static/seats/seats-final.css, apk_payload/templates/seats.html, backups/apk_sync_20260520_234501/seats.html, static/seats/patches/seat-simple-ui-pack.css |
| .badge | 29 | android_app/app/src/main/python/static/vendor/bootstrap/bootstrap.min.css, android_app/app/src/main/python/templates/add_route.html, android_app/app/src/main/python/templates/ai_console.html, android_app/app/src/main/python/templates/events.html, android_app/app/src/main/python/templates/route_schedule_edit.html, android_app/app/src/main/python/templates/routes_list.html, android_app/app/src/main/python/templates/settings_package_requests.html, android_app/app/src/main/python/templates/trip_report.html |
| .upcoming | 29 | android_app/app/src/main/python/static/continue/css_parts/00-base-legacy.css, android_app/app/src/main/python/static/continue/css_parts/10-compact-timeline-hero.css, android_app/app/src/main/python/static/continue/css_parts/50-live-v2-top-glow.css, apk_payload/templates/continue_trip.html, static/continue/css_parts/00-base-legacy.css, static/continue/css_parts/10-compact-timeline-hero.css, static/continue/css_parts/50-live-v2-top-glow.css |
| .board-card | 28 | _unused_review/static/seats/seats-redesign.css, android_app/app/src/main/python/static/seats/patches/seat-simple-ui-pack.css, android_app/app/src/main/python/static/seats/seats-final.css, android_app/app/src/main/python/static/seats/seats.css, apk_payload/static/seats/patches/seat-simple-ui-pack.css, apk_payload/static/seats/seats-final.css, apk_payload/static/seats/seats.css, static/seats/patches/seat-simple-ui-pack.css |
| .modal-body | 28 | android_app/app/src/main/python/static/vendor/bootstrap/bootstrap.min.css, android_app/app/src/main/python/templates/trip_report.html, apk_payload/static/vendor/bootstrap/bootstrap.min.css, apk_payload/templates/trip_report.html, backups/apk_sync_20260520_234501/trip_report.html, static/vendor/bootstrap/bootstrap.min.css, templates/trip_report.html |
| .panel-card | 28 | _unused_review/static/seats/seats-redesign.css, android_app/app/src/main/python/static/seats/patches/seat-simple-ui-pack.css, android_app/app/src/main/python/static/seats/seats-final.css, android_app/app/src/main/python/static/seats/seats.css, apk_payload/static/seats/patches/seat-simple-ui-pack.css, apk_payload/static/seats/seats-final.css, apk_payload/static/seats/seats.css, static/seats/patches/seat-simple-ui-pack.css |
| .section-head | 28 | _unused_review/static/seats/seats-redesign.css, android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-final.css, android_app/app/src/main/python/static/seats/seats.css, android_app/app/src/main/python/templates/ai_console.html, android_app/app/src/main/python/templates/rehber.html, android_app/app/src/main/python/templates/route_schedule_edit.html, android_app/app/src/main/python/templates/routes_list.html, android_app/app/src/main/python/templates/trip_report.html |
| .approach-alert | 27 | android_app/app/src/main/python/templates/live_map.html, apk_payload/templates/live_map.html, templates/live_map.html |
| .dropdown-menu | 27 | android_app/app/src/main/python/static/vendor/bootstrap/bootstrap.min.css, apk_payload/static/vendor/bootstrap/bootstrap.min.css, static/vendor/bootstrap/bootstrap.min.css |
| .icon-btn | 27 | android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-final.css, android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-tone.css, android_app/app/src/main/python/static/seats/seats-final.css, android_app/app/src/main/python/static/seats/seats.css, android_app/app/src/main/python/templates/ai_console.html, android_app/app/src/main/python/templates/route_schedule_edit.html, apk_payload/static/seats/_archive_theme_trials/seats-dashboard-final.css, apk_payload/static/seats/_archive_theme_trials/seats-dashboard-tone.css |
| .list-group-item | 27 | android_app/app/src/main/python/static/vendor/bootstrap/bootstrap.min.css, apk_payload/static/vendor/bootstrap/bootstrap.min.css, static/vendor/bootstrap/bootstrap.min.css |
| .muavin-bottom-dock-final-v5 | 27 | android_app/app/src/main/python/static/live_map/muavin_live_map_extra.css, apk_payload/static/live_map/muavin_live_map_extra.css, static/live_map/muavin_live_map_extra.css |
| .muavin-clean-toggle-v10 | 27 | android_app/app/src/main/python/static/live_map/muavin_live_map_extra.css, apk_payload/static/live_map/muavin_live_map_extra.css, static/live_map/muavin_live_map_extra.css |
| .num | 27 | android_app/app/src/main/python/templates/events.html, android_app/app/src/main/python/templates/hesap.html, apk_payload/templates/events.html, apk_payload/templates/hesap.html, templates/events.html, templates/hesap.html |
| .passed | 27 | android_app/app/src/main/python/static/continue/css_parts/00-base-legacy.css, android_app/app/src/main/python/static/continue/css_parts/10-compact-timeline-hero.css, android_app/app/src/main/python/static/seats/seats.css, apk_payload/static/seats/seats.css, apk_payload/templates/continue_trip.html, static/continue/css_parts/00-base-legacy.css, static/continue/css_parts/10-compact-timeline-hero.css, static/seats/seats.css |
| .route-name | 27 | android_app/app/src/main/python/templates/index.html, android_app/app/src/main/python/templates/routes_list.html, apk_payload/templates/index.html, apk_payload/templates/routes_list.html, templates/index.html, templates/routes_list.html |
| .route-strip-meta | 27 | android_app/app/src/main/python/static/seats/seats-final.css, android_app/app/src/main/python/static/seats/seats.css, apk_payload/static/seats/seats-final.css, apk_payload/static/seats/seats.css, static/seats/seats-final.css, static/seats/seats.css |
| .secondary | 27 | android_app/app/src/main/python/templates/add_route.html, android_app/app/src/main/python/templates/forgot_password.html, android_app/app/src/main/python/templates/package_required.html, android_app/app/src/main/python/templates/settings_package_requests.html, android_app/app/src/main/python/templates/settings_password.html, android_app/app/src/main/python/templates/settings_profile.html, android_app/app/src/main/python/templates/settings_recovery.html, android_app/app/src/main/python/templates/settings_subscription.html |
| .status-row | 27 | android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-final.css, android_app/app/src/main/python/static/seats/seats-final.css, android_app/app/src/main/python/static/seats/seats.css, apk_payload/static/seats/_archive_theme_trials/seats-dashboard-final.css, apk_payload/static/seats/seats-final.css, apk_payload/static/seats/seats.css, static/seats/_archive_theme_trials/seats-dashboard-final.css, static/seats/seats-final.css |
| .topbar | 27 | android_app/app/src/main/python/static/seats/seats.css, android_app/app/src/main/python/templates/hesap.html, android_app/app/src/main/python/templates/live_map.html, android_app/app/src/main/python/templates/onboarding.html, android_app/app/src/main/python/templates/reports.html, apk_payload/static/seats/seats.css, apk_payload/templates/hesap.html, apk_payload/templates/live_map.html |
| .voice-seat-mini | 27 | android_app/app/src/main/python/static/seats/seats-final.css, apk_payload/static/seats/seats-final.css, static/seats/seats-final.css |
| .deck-wrap | 25 | android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-final.css, android_app/app/src/main/python/static/seats/seats-final.css, android_app/app/src/main/python/static/seats/seats.css, android_app/app/src/main/python/templates/passenger_control.html, apk_payload/static/seats/_archive_theme_trials/seats-dashboard-final.css, apk_payload/static/seats/seats-final.css, apk_payload/static/seats/seats.css, apk_payload/templates/passenger_control.html |
| .alert | 24 | android_app/app/src/main/python/static/vendor/bootstrap/bootstrap.min.css, android_app/app/src/main/python/templates/forgot_password.html, android_app/app/src/main/python/templates/settings_backup.html, android_app/app/src/main/python/templates/settings_password.html, android_app/app/src/main/python/templates/settings_profile.html, android_app/app/src/main/python/templates/settings_recovery.html, android_app/app/src/main/python/templates/settings_subscription.html, android_app/app/src/main/python/templates/setup.html |
| .collapsed | 24 | android_app/app/src/main/python/static/live_map/muavin_live_map_extra.css, android_app/app/src/main/python/static/vendor/bootstrap/bootstrap.min.css, apk_payload/static/live_map/muavin_live_map_extra.css, apk_payload/static/vendor/bootstrap/bootstrap.min.css, static/live_map/muavin_live_map_extra.css, static/vendor/bootstrap/bootstrap.min.css |
| .done | 24 | android_app/app/src/main/python/static/continue/css_parts/40-cargo-gender-summary.css, android_app/app/src/main/python/static/live_map/muavin_live_map_extra.css, android_app/app/src/main/python/static/seats/seats-final.css, android_app/app/src/main/python/static/seats/seats.css, android_app/app/src/main/python/templates/ai_console.html, android_app/app/src/main/python/templates/seats_parts/finish_trip_modal.html, android_app/app/src/main/python/templates/settings_package_requests.html, apk_payload/static/live_map/muavin_live_map_extra.css |
| .drive-eta-sub | 24 | _unused_review/static/seats/seats-redesign.css, android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-final.css, android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-tone.css, android_app/app/src/main/python/static/seats/seats-final.css, android_app/app/src/main/python/static/seats/seats.css, android_app/app/src/main/python/templates/seats.html, apk_payload/static/seats/_archive_theme_trials/seats-dashboard-final.css, apk_payload/static/seats/_archive_theme_trials/seats-dashboard-tone.css |
| .drive-speed-sub | 24 | android_app/app/src/main/python/static/seats/seats.css, apk_payload/static/seats/seats.css, static/seats/seats.css |
| .extra-v | 24 | android_app/app/src/main/python/static/seats/seats-final.css, android_app/app/src/main/python/static/seats/seats.css, apk_payload/static/seats/seats-final.css, apk_payload/static/seats/seats.css, static/seats/seats-final.css, static/seats/seats.css |
| .fab-left-gap-moved | 24 | android_app/app/src/main/python/static/seats/patches/seat-layout-fab-pack.css, apk_payload/static/seats/patches/seat-layout-fab-pack.css, static/seats/patches/seat-layout-fab-pack.css |
| .form-select | 24 | android_app/app/src/main/python/static/vendor/bootstrap/bootstrap.min.css, apk_payload/static/vendor/bootstrap/bootstrap.min.css, static/vendor/bootstrap/bootstrap.min.css |
| .guide-card-header | 24 | android_app/app/src/main/python/templates/rehber.html, apk_payload/templates/rehber.html, templates/rehber.html |
| .hero-link | 24 | android_app/app/src/main/python/templates/index.html, apk_payload/templates/index.html, templates/index.html |
| .menu-desc | 24 | android_app/app/src/main/python/templates/index.html, apk_payload/templates/index.html, templates/index.html |
| .menu-item | 24 | android_app/app/src/main/python/templates/index.html, apk_payload/templates/index.html, templates/index.html |
| .menu-title | 24 | android_app/app/src/main/python/templates/index.html, apk_payload/templates/index.html, templates/index.html |
| .modal-content | 24 | android_app/app/src/main/python/static/vendor/bootstrap/bootstrap.min.css, apk_payload/static/vendor/bootstrap/bootstrap.min.css, static/vendor/bootstrap/bootstrap.min.css |
| .navbar-toggler | 24 | android_app/app/src/main/python/static/vendor/bootstrap/bootstrap.min.css, apk_payload/static/vendor/bootstrap/bootstrap.min.css, static/vendor/bootstrap/bootstrap.min.css |
| .offcanvas | 24 | android_app/app/src/main/python/static/vendor/bootstrap/bootstrap.min.css, apk_payload/static/vendor/bootstrap/bootstrap.min.css, static/vendor/bootstrap/bootstrap.min.css |
| .open | 24 | android_app/app/src/main/python/static/continue/css_parts/20-live-stop-sheet-base.css, android_app/app/src/main/python/static/continue/css_parts/30-sheet-bag-photo.css, android_app/app/src/main/python/static/style.css, android_app/app/src/main/python/templates/ai_console.html, android_app/app/src/main/python/templates/live_map.html, android_app/app/src/main/python/templates/settings_package_requests.html, apk_payload/static/style.css, apk_payload/templates/ai_console.html |
| .route-badge | 24 | android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-final.css, android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-tone.css, android_app/app/src/main/python/static/seats/seats-final.css, android_app/app/src/main/python/static/seats/seats.css, apk_payload/static/seats/_archive_theme_trials/seats-dashboard-final.css, apk_payload/static/seats/_archive_theme_trials/seats-dashboard-tone.css, apk_payload/static/seats/seats-final.css, apk_payload/static/seats/seats.css |
| .stat-box | 24 | android_app/app/src/main/python/static/continue/css_parts/00-base-legacy.css, android_app/app/src/main/python/static/continue/css_parts/10-compact-timeline-hero.css, apk_payload/templates/continue_trip.html, static/continue/css_parts/00-base-legacy.css, static/continue/css_parts/10-compact-timeline-hero.css |
| .timeline-line | 24 | android_app/app/src/main/python/static/continue/css_parts/00-base-legacy.css, android_app/app/src/main/python/static/continue/css_parts/10-compact-timeline-hero.css, apk_payload/templates/continue_trip.html, static/continue/css_parts/00-base-legacy.css, static/continue/css_parts/10-compact-timeline-hero.css |
| .top-actions | 24 | android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-final.css, android_app/app/src/main/python/static/seats/seats-final.css, android_app/app/src/main/python/static/seats/seats.css, apk_payload/static/seats/_archive_theme_trials/seats-dashboard-final.css, apk_payload/static/seats/seats-final.css, apk_payload/static/seats/seats.css, static/seats/_archive_theme_trials/seats-dashboard-final.css, static/seats/seats-final.css |
| .blue | 23 | android_app/app/src/main/python/templates/consignments.html, android_app/app/src/main/python/templates/report_archive.html, android_app/app/src/main/python/templates/route_schedule_edit.html, android_app/app/src/main/python/templates/settings_subscription.html, android_app/app/src/main/python/templates/trip_report.html, apk_payload/templates/consignments.html, apk_payload/templates/report_archive.html, apk_payload/templates/route_schedule_edit.html |
| .drive-eta-top | 23 | android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-final.css, android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-tone.css, android_app/app/src/main/python/static/seats/seats-final.css, android_app/app/src/main/python/static/seats/seats.css, android_app/app/src/main/python/templates/seats.html, apk_payload/static/seats/_archive_theme_trials/seats-dashboard-final.css, apk_payload/static/seats/_archive_theme_trials/seats-dashboard-tone.css, apk_payload/static/seats/seats-final.css |
| .bag-badge | 22 | android_app/app/src/main/python/static/seats/seats.css, apk_payload/static/seats/seats.css, static/seats/patches/unified-seat-deck-report-style.css, static/seats/seats.css |
| .page | 22 | android_app/app/src/main/python/static/style.css, android_app/app/src/main/python/templates/route_schedule_edit.html, apk_payload/static/style.css, apk_payload/templates/route_schedule_edit.html, static/style.css, templates/report_archive.html, templates/route_schedule_edit.html, templates/settings.html |
| .row | 22 | android_app/app/src/main/python/static/style.css, android_app/app/src/main/python/static/vendor/bootstrap/bootstrap.min.css, android_app/app/src/main/python/templates/add_route.html, android_app/app/src/main/python/templates/hesap.html, android_app/app/src/main/python/templates/reports.html, android_app/app/src/main/python/templates/trip_report.html, apk_payload/static/style.css, apk_payload/static/vendor/bootstrap/bootstrap.min.css |
| #nightVoiceToggle | 21 | android_app/app/src/main/python/static/seats/seats-final.css, android_app/app/src/main/python/static/seats/seats.css, apk_payload/static/seats/seats-final.css, apk_payload/static/seats/seats.css, static/seats/seats-final.css, static/seats/seats.css |
| .corr | 21 | android_app/app/src/main/python/static/seats/seats.css, android_app/app/src/main/python/templates/passenger_control.html, apk_payload/static/seats/seats.css, apk_payload/templates/passenger_control.html, static/seats/patches/unified-seat-deck-report-style.css, static/seats/seats.css, templates/passenger_control.html |
| .err | 21 | android_app/app/src/main/python/templates/ai_console.html, android_app/app/src/main/python/templates/forgot_password.html, android_app/app/src/main/python/templates/settings_backup.html, android_app/app/src/main/python/templates/settings_password.html, android_app/app/src/main/python/templates/settings_profile.html, android_app/app/src/main/python/templates/settings_subscription.html, apk_payload/templates/ai_console.html, apk_payload/templates/forgot_password.html |
| .gray | 21 | android_app/app/src/main/python/templates/consignments.html, android_app/app/src/main/python/templates/fare_admin.html, android_app/app/src/main/python/templates/fare_query.html, android_app/app/src/main/python/templates/passenger_control.html, android_app/app/src/main/python/templates/route_schedule_edit.html, android_app/app/src/main/python/templates/route_stops.html, apk_payload/templates/consignments.html, apk_payload/templates/fare_admin.html |
| .guide-card | 21 | android_app/app/src/main/python/templates/rehber.html, apk_payload/templates/rehber.html, templates/rehber.html |
| .guide-grid | 21 | android_app/app/src/main/python/templates/rehber.html, apk_payload/templates/rehber.html, templates/rehber.html |
| .hero-meta | 21 | android_app/app/src/main/python/static/continue/css_parts/00-base-legacy.css, android_app/app/src/main/python/static/continue/css_parts/10-compact-timeline-hero.css, android_app/app/src/main/python/templates/route_schedule_edit.html, apk_payload/templates/continue_trip.html, apk_payload/templates/route_schedule_edit.html, static/continue/css_parts/00-base-legacy.css, static/continue/css_parts/10-compact-timeline-hero.css, templates/route_schedule_edit.html |
| .hero-title | 21 | android_app/app/src/main/python/templates/ai_console.html, android_app/app/src/main/python/templates/route_schedule_edit.html, apk_payload/templates/ai_console.html, apk_payload/templates/route_schedule_edit.html, templates/ai_console.html, templates/route_schedule_edit.html |
| .home-shell | 21 | android_app/app/src/main/python/templates/index.html, apk_payload/templates/index.html, templates/index.html |
| .modal-header | 21 | android_app/app/src/main/python/static/vendor/bootstrap/bootstrap.min.css, apk_payload/static/vendor/bootstrap/bootstrap.min.css, static/vendor/bootstrap/bootstrap.min.css |
| .navbar-collapse | 21 | android_app/app/src/main/python/static/vendor/bootstrap/bootstrap.min.css, apk_payload/static/vendor/bootstrap/bootstrap.min.css, static/vendor/bootstrap/bootstrap.min.css |
| .navbar-nav | 21 | android_app/app/src/main/python/static/vendor/bootstrap/bootstrap.min.css, apk_payload/static/vendor/bootstrap/bootstrap.min.css, static/vendor/bootstrap/bootstrap.min.css |
| .navbar-nav-scroll | 21 | android_app/app/src/main/python/static/vendor/bootstrap/bootstrap.min.css, apk_payload/static/vendor/bootstrap/bootstrap.min.css, static/vendor/bootstrap/bootstrap.min.css |
| .next-ops-panel | 21 | android_app/app/src/main/python/static/live_map/muavin_live_map_extra.css, android_app/app/src/main/python/templates/live_map.html, apk_payload/static/live_map/muavin_live_map_extra.css, apk_payload/templates/live_map.html, static/live_map/muavin_live_map_extra.css, templates/live_map.html |
| .route-picker-premium | 21 | android_app/app/src/main/python/templates/index.html, apk_payload/templates/index.html, templates/index.html |
| .dma-btn | 20 | android_app/app/src/main/python/static/seats/seats-final.css, android_app/app/src/main/python/templates/seats.html, apk_payload/static/seats/seats-final.css, apk_payload/templates/seats.html, backups/apk_sync_20260520_234501/seats.html, static/seats/seats-final.css, templates/seats.html |
| .modal | 20 | android_app/app/src/main/python/static/vendor/bootstrap/bootstrap.min.css, android_app/app/src/main/python/templates/consignments.html, android_app/app/src/main/python/templates/reports.html, apk_payload/static/vendor/bootstrap/bootstrap.min.css, apk_payload/templates/consignments.html, apk_payload/templates/reports.html, static/vendor/bootstrap/bootstrap.min.css, templates/consignments.html |
| .bad | 19 | android_app/app/src/main/python/static/seats/seats.css, android_app/app/src/main/python/templates/live_map.html, android_app/app/src/main/python/templates/passenger_control.html, apk_payload/static/seats/seats.css, apk_payload/templates/live_map.html, apk_payload/templates/passenger_control.html, static/seats/seats.css, templates/live_map.html |
| .metric-hint | 19 | android_app/app/src/main/python/static/continue/css_parts/20-live-stop-sheet-base.css, android_app/app/src/main/python/static/continue/css_parts/30-sheet-bag-photo.css, android_app/app/src/main/python/static/continue/css_parts/50-live-v2-top-glow.css, apk_payload/templates/continue_trip.html, static/continue/css_parts/20-live-stop-sheet-base.css, static/continue/css_parts/30-sheet-bag-photo.css, static/continue/css_parts/50-live-v2-top-glow.css |
| .account-hero-top | 18 | android_app/app/src/main/python/templates/hesap.html, apk_payload/templates/hesap.html, templates/hesap.html |
| .arrow | 18 | android_app/app/src/main/python/templates/index.html, apk_payload/templates/index.html, templates/index.html |
| .back-btn | 18 | android_app/app/src/main/python/templates/route_edit.html, android_app/app/src/main/python/templates/settings.html, android_app/app/src/main/python/templates/settings_backup.html, apk_payload/templates/route_edit.html, apk_payload/templates/settings.html, apk_payload/templates/settings_backup.html, templates/index.html, templates/report_archive.html |
| .board-kicker | 18 | _unused_review/static/seats/seats-redesign.css, android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-final.css, android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-tone.css, android_app/app/src/main/python/static/seats/seats-final.css, android_app/app/src/main/python/static/seats/seats.css, apk_payload/static/seats/_archive_theme_trials/seats-dashboard-final.css, apk_payload/static/seats/_archive_theme_trials/seats-dashboard-tone.css, apk_payload/static/seats/seats-final.css |
| .board-title | 18 | _unused_review/static/seats/seats-redesign.css, android_app/app/src/main/python/static/seats/patches/seat-simple-ui-pack.css, android_app/app/src/main/python/static/seats/seats-final.css, android_app/app/src/main/python/static/seats/seats.css, android_app/app/src/main/python/templates/seats.html, apk_payload/static/seats/patches/seat-simple-ui-pack.css, apk_payload/static/seats/seats-final.css, apk_payload/static/seats/seats.css |
| .btn-close | 18 | android_app/app/src/main/python/static/vendor/bootstrap/bootstrap.min.css, apk_payload/static/vendor/bootstrap/bootstrap.min.css, static/vendor/bootstrap/bootstrap.min.css |
| .door | 18 | android_app/app/src/main/python/static/seats/patches/right-seat-column-spacing-fix.css, android_app/app/src/main/python/static/seats/patches/seat-layout-fab-pack.css, android_app/app/src/main/python/static/seats/seats.css, android_app/app/src/main/python/templates/passenger_control.html, android_app/app/src/main/python/templates/trip_report.html, apk_payload/static/seats/patches/right-seat-column-spacing-fix.css, apk_payload/static/seats/patches/seat-layout-fab-pack.css, apk_payload/static/seats/seats.css |
| .form-check-input | 18 | android_app/app/src/main/python/static/vendor/bootstrap/bootstrap.min.css, apk_payload/static/vendor/bootstrap/bootstrap.min.css, static/vendor/bootstrap/bootstrap.min.css |
| .hero-actions | 18 | android_app/app/src/main/python/templates/ai_console.html, android_app/app/src/main/python/templates/route_schedule_edit.html, apk_payload/templates/ai_console.html, apk_payload/templates/route_schedule_edit.html, templates/ai_console.html, templates/route_schedule_edit.html |
| .info | 18 | android_app/app/src/main/python/static/seats/seats.css, android_app/app/src/main/python/templates/ai_console.html, android_app/app/src/main/python/templates/settings_backup.html, android_app/app/src/main/python/templates/settings_subscription.html, apk_payload/static/seats/seats.css, apk_payload/templates/ai_console.html, apk_payload/templates/settings_backup.html, apk_payload/templates/settings_subscription.html |
| .main | 18 | android_app/app/src/main/python/templates/rehber.html, apk_payload/templates/rehber.html, templates/rehber.html |
| .modal-dialog | 18 | android_app/app/src/main/python/static/vendor/bootstrap/bootstrap.min.css, apk_payload/static/vendor/bootstrap/bootstrap.min.css, static/vendor/bootstrap/bootstrap.min.css |
| .next-ops-head | 18 | android_app/app/src/main/python/static/live_map/muavin_live_map_extra.css, android_app/app/src/main/python/templates/live_map.html, apk_payload/static/live_map/muavin_live_map_extra.css, apk_payload/templates/live_map.html, static/live_map/muavin_live_map_extra.css, templates/live_map.html |
| .next-ops-list | 18 | android_app/app/src/main/python/static/live_map/muavin_live_map_extra.css, android_app/app/src/main/python/templates/live_map.html, apk_payload/static/live_map/muavin_live_map_extra.css, apk_payload/templates/live_map.html, static/live_map/muavin_live_map_extra.css, templates/live_map.html |
| .offcanvas-bottom | 18 | android_app/app/src/main/python/static/vendor/bootstrap/bootstrap.min.css, apk_payload/static/vendor/bootstrap/bootstrap.min.css, static/vendor/bootstrap/bootstrap.min.css |
| .offcanvas-end | 18 | android_app/app/src/main/python/static/vendor/bootstrap/bootstrap.min.css, apk_payload/static/vendor/bootstrap/bootstrap.min.css, static/vendor/bootstrap/bootstrap.min.css |
| .offcanvas-start | 18 | android_app/app/src/main/python/static/vendor/bootstrap/bootstrap.min.css, apk_payload/static/vendor/bootstrap/bootstrap.min.css, static/vendor/bootstrap/bootstrap.min.css |
| .offcanvas-top | 18 | android_app/app/src/main/python/static/vendor/bootstrap/bootstrap.min.css, apk_payload/static/vendor/bootstrap/bootstrap.min.css, static/vendor/bootstrap/bootstrap.min.css |
| .route-strip-title | 18 | android_app/app/src/main/python/static/seats/seats-final.css, android_app/app/src/main/python/static/seats/seats.css, apk_payload/static/seats/seats-final.css, apk_payload/static/seats/seats.css, static/seats/seats-final.css, static/seats/seats.css |
| .route-title-row | 18 | android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-final.css, android_app/app/src/main/python/static/seats/seats-final.css, android_app/app/src/main/python/static/seats/seats.css, apk_payload/static/seats/_archive_theme_trials/seats-dashboard-final.css, apk_payload/static/seats/seats-final.css, apk_payload/static/seats/seats.css, static/seats/_archive_theme_trials/seats-dashboard-final.css, static/seats/seats-final.css |
| .visual-caption | 18 | android_app/app/src/main/python/templates/rehber.html, apk_payload/templates/rehber.html, templates/rehber.html |
| .content | 17 | android_app/app/src/main/python/templates/live_map.html, apk_payload/templates/live_map.html, templates/live_map.html, templates/report_archive.html, templates/settings.html, templates/settings_backup.html, templates/settings_password.html, templates/settings_profile.html |
| .dark | 17 | android_app/app/src/main/python/static/seats/seats.css, android_app/app/src/main/python/templates/ai_console.html, android_app/app/src/main/python/templates/consignments.html, android_app/app/src/main/python/templates/live_map.html, android_app/app/src/main/python/templates/settings_subscription.html, apk_payload/static/seats/seats.css, apk_payload/templates/ai_console.html, apk_payload/templates/consignments.html |
| .drive-mode | 17 | android_app/app/src/main/python/static/seats/seats.css, apk_payload/static/seats/seats.css, static/seats/patches/unified-seat-deck-report-style.css, static/seats/seats.css |
| .field-row | 16 | _unused_review/static/seats/seats-redesign.css, android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-final.css, android_app/app/src/main/python/static/seats/seats.css, android_app/app/src/main/python/templates/consignments.html, apk_payload/static/seats/_archive_theme_trials/seats-dashboard-final.css, apk_payload/static/seats/seats.css, apk_payload/templates/consignments.html, static/seats/_archive_theme_trials/seats-dashboard-final.css |
| .metric | 16 | android_app/app/src/main/python/static/continue/css_parts/00-base-legacy.css, android_app/app/src/main/python/static/continue/css_parts/10-compact-timeline-hero.css, android_app/app/src/main/python/static/continue/css_parts/50-live-v2-top-glow.css, apk_payload/templates/continue_trip.html, static/continue/css_parts/00-base-legacy.css, static/continue/css_parts/10-compact-timeline-hero.css, static/continue/css_parts/50-live-v2-top-glow.css |
| .tab-btn | 16 | _unused_review/static/seats/seats-redesign.css, android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-final.css, android_app/app/src/main/python/static/seats/seats-final.css, android_app/app/src/main/python/static/seats/seats.css, apk_payload/static/seats/_archive_theme_trials/seats-dashboard-final.css, apk_payload/static/seats/seats-final.css, apk_payload/static/seats/seats.css, static/seats/_archive_theme_trials/seats-dashboard-final.css |

## 12) Inline Script/Style Şişkinliği
| HTML | Inline style | Inline script |
| --- | --- | --- |
| templates/add_route.html | 2 | 1 |
| templates/base.html | 0 | 0 |
| templates/consignments.html | 2 | 1 |
| templates/events.html | 1 | 0 |
| templates/fare_admin.html | 1 | 1 |
| templates/fare_query.html | 1 | 1 |
| templates/hesap.html | 1 | 2 |
| templates/home.html | 0 | 0 |
| templates/index.html | 10 | 4 |
| templates/login.html | 1 | 1 |
| templates/passenger_control.html | 2 | 1 |
| templates/reports.html | 1 | 1 |
| templates/route_edit.html | 2 | 2 |
| templates/route_stops.html | 1 | 1 |
| templates/routes_list.html | 1 | 1 |
| templates/seats.html | 2 | 5 |
| templates/settings.html | 1 | 1 |
| templates/start_trip.html | 1 | 1 |
| templates/trip_new.html | 0 | 0 |
| templates/ai_console.html | 2 | 2 |
| templates/route_schedule_edit.html | 2 | 1 |
| templates/trip_report.html | 4 | 3 |
| templates/report_archive.html | 1 | 1 |
| templates/rehber.html | 1 | 1 |
| templates/settings_password.html | 1 | 1 |
| templates/live_map.html | 19 | 2 |
| templates/settings_recovery.html | 1 | 1 |
| templates/forgot_password.html | 1 | 1 |
| templates/setup.html | 1 | 2 |
| templates/setup_done.html | 1 | 0 |
| templates/settings_profile.html | 1 | 1 |
| templates/settings_backup.html | 1 | 1 |
| templates/settings_subscription.html | 1 | 1 |
| templates/subscription_required.html | 1 | 0 |
| templates/package_required.html | 1 | 0 |
| templates/onboarding.html | 1 | 1 |
| templates/continue_trip.html | 0 | 2 |
| templates/settings_package_requests.html | 1 | 0 |
| templates/no_active_trip.html | 1 | 0 |
| templates/user_reset.html | 1 | 0 |
| backups/apk_sync_20260520_234501/seats.html | 2 | 5 |
| backups/apk_sync_20260520_234501/trip_report.html | 2 | 3 |
| _unused_review/trafik_isigi/trafik.html | 1 | 1 |
| android_app/app/src/main/python/templates/add_route.html | 2 | 1 |
| android_app/app/src/main/python/templates/base.html | 0 | 0 |
| android_app/app/src/main/python/templates/consignments.html | 2 | 1 |
| android_app/app/src/main/python/templates/events.html | 1 | 0 |
| android_app/app/src/main/python/templates/fare_admin.html | 1 | 1 |
| android_app/app/src/main/python/templates/fare_query.html | 1 | 1 |
| android_app/app/src/main/python/templates/hesap.html | 1 | 2 |
| android_app/app/src/main/python/templates/home.html | 0 | 0 |
| android_app/app/src/main/python/templates/index.html | 8 | 3 |
| android_app/app/src/main/python/templates/login.html | 1 | 1 |
| android_app/app/src/main/python/templates/passenger_control.html | 2 | 1 |
| android_app/app/src/main/python/templates/reports.html | 1 | 1 |
| android_app/app/src/main/python/templates/route_edit.html | 2 | 2 |
| android_app/app/src/main/python/templates/route_stops.html | 1 | 1 |
| android_app/app/src/main/python/templates/routes_list.html | 1 | 1 |
| android_app/app/src/main/python/templates/seats.html | 2 | 5 |
| android_app/app/src/main/python/templates/settings.html | 1 | 0 |
| android_app/app/src/main/python/templates/start_trip.html | 1 | 1 |
| android_app/app/src/main/python/templates/trip_new.html | 0 | 0 |
| android_app/app/src/main/python/templates/ai_console.html | 2 | 2 |
| android_app/app/src/main/python/templates/route_schedule_edit.html | 2 | 1 |
| android_app/app/src/main/python/templates/trip_report.html | 2 | 3 |
| android_app/app/src/main/python/templates/report_archive.html | 1 | 0 |
| android_app/app/src/main/python/templates/rehber.html | 1 | 1 |
| android_app/app/src/main/python/templates/settings_password.html | 1 | 1 |
| android_app/app/src/main/python/templates/live_map.html | 19 | 2 |
| android_app/app/src/main/python/templates/settings_recovery.html | 1 | 1 |
| android_app/app/src/main/python/templates/forgot_password.html | 1 | 1 |
| android_app/app/src/main/python/templates/setup.html | 1 | 2 |
| android_app/app/src/main/python/templates/setup_done.html | 1 | 0 |
| android_app/app/src/main/python/templates/settings_profile.html | 1 | 0 |
| android_app/app/src/main/python/templates/settings_backup.html | 1 | 0 |
| android_app/app/src/main/python/templates/settings_subscription.html | 1 | 5 |
| android_app/app/src/main/python/templates/subscription_required.html | 1 | 0 |
| android_app/app/src/main/python/templates/package_required.html | 1 | 0 |
| android_app/app/src/main/python/templates/onboarding.html | 1 | 1 |
| android_app/app/src/main/python/templates/continue_trip.html | 0 | 2 |

## 13) Patch/Yama Tokenları
| Yama token | Geçiş | Dosyalar |
| --- | --- | --- |
| stop-flow-focus-patch | 340 | AUTO_LIVE_STOP_AUDIT.txt, AYARLAR_DETAY_RAPORU.txt, DURAK_AKISI_KAYNAK_RAPORU_20260518_205127.txt, LIVE_FLOW_TARGET_AUDIT.txt, LIVE_FLOW_V2_AUDIT.txt, PATCH_AUDIT_REPORT.md, PATCH_LIVE_AUDIT_REPORT.md, SEATS_CSS_OVERRIDE_REPORT.md |
| muavin-bottom-dock-final-v5 | 99 | AUTO_LIVE_STOP_AUDIT.txt, android_app/app/src/main/python/static/live_map/muavin_live_map_extra.css, android_app/app/src/main/python/static/live_map/muavin_live_map_extra.js, apk_payload/static/live_map/muavin_live_map_extra.css, apk_payload/static/live_map/muavin_live_map_extra.js, static/live_map/muavin_live_map_extra.css, static/live_map/muavin_live_map_extra.js |
| mobile-performance-fix | 98 | AUTO_LIVE_STOP_AUDIT.txt, AYARLAR_DETAY_RAPORU.txt, DURAK_AKISI_KAYNAK_RAPORU_20260518_205127.txt, LIVE_FLOW_TARGET_AUDIT.txt, LIVE_FLOW_V2_AUDIT.txt, PATCH_AUDIT_REPORT.md, PATCH_LIVE_AUDIT_REPORT.md, SEATS_CSS_OVERRIDE_REPORT.md |
| bak_bottom_voice_clickfix_20260516_111618 | 92 | AYARLAR_DETAY_RAPORU.txt, DURAK_AKISI_KAYNAK_RAPORU_20260518_205127.txt, KOLTUK_PANEL_YAMA_RAPORU_20260516_153819.txt, SEATS_DETAYLI_SISTEM_RAPORU_20260516_155924.txt, SON_YARIM_SAAT_YAMA_RAPORU_20260516_150801.txt |
| bak-fixed-dock | 90 | proje_dosya_listesi.txt, seats_baglanti_haritasi.txt, tracked_junk.txt, tracked_junk_safe.txt |
| bak_before_fix_bad_voice_rollback_20260516_150609 | 83 | AYARLAR_DETAY_RAPORU.txt, DURAK_AKISI_KAYNAK_RAPORU_20260518_205127.txt, KOLTUK_PANEL_YAMA_RAPORU_20260516_153819.txt, SEATS_DETAYLI_SISTEM_RAPORU_20260516_155924.txt, SON_YARIM_SAAT_YAMA_RAPORU_20260516_150801.txt, raporlar/asama1_durak_akisi_haritasi_20260520_110402.txt |
| continue-live-v2 | 82 | android_app/app/src/main/python/static/continue/continue_trip_ui.js, android_app/app/src/main/python/static/continue/css_parts/50-live-v2-top-glow.css, static/continue/continue_trip_ui.js, static/continue/css_parts/50-live-v2-top-glow.css |
| seats_ses_fix_yedek_20260427_165038 | 79 | proje_dosya_listesi.txt, seats_baglanti_haritasi.txt, tracked_junk.txt, tracked_junk_safe.txt |
| bak_before_cleanup_step1_20260518_153910 | 78 | DURAK_AKISI_KAYNAK_RAPORU_20260518_205127.txt |
| bak_before_fab_drive_override_fix_20260516_164916 | 78 | DURAK_AKISI_KAYNAK_RAPORU_20260518_205127.txt |
| bak_extract_fab_patches_20260518_172257 | 78 | DURAK_AKISI_KAYNAK_RAPORU_20260518_205127.txt |
| bak_manual_ticket_persist_fix_20260518_135715 | 78 | DURAK_AKISI_KAYNAK_RAPORU_20260518_205127.txt |
| bak_selected_stop_memory_fix_version_20260518_153404 | 78 | DURAK_AKISI_KAYNAK_RAPORU_20260518_205127.txt |
| seats_voice_summary_fix_20260427_165419 | 78 | aktif_dosya_listesi.txt, proje_dosya_listesi.txt, seats_baglanti_haritasi.txt |
| bak_general_seat_label_fix_20260516_062235 | 63 | DURAK_AKISI_KAYNAK_RAPORU_20260518_205127.txt, SEATS_DETAYLI_SISTEM_RAPORU_20260516_155924.txt, SON_YARIM_SAAT_YAMA_RAPORU_20260516_150801.txt, raporlar/asama1_durak_akisi_haritasi_20260520_110402.txt |
| bak_rollback_general_label_fix_20260516_062504 | 63 | DURAK_AKISI_KAYNAK_RAPORU_20260518_205127.txt, SEATS_DETAYLI_SISTEM_RAPORU_20260516_155924.txt, SON_YARIM_SAAT_YAMA_RAPORU_20260516_150801.txt, raporlar/asama1_durak_akisi_haritasi_20260520_110402.txt |
| hero-device-v2 | 63 | AYARLAR_DETAY_RAPORU.txt, android_app/app/src/main/python/templates/rehber.html, apk_payload/templates/rehber.html, templates/rehber.html |
| driveFixedDock | 60 | LIVE_FLOW_TARGET_AUDIT.txt, SEATS_AKTIF_HARITA.txt, SURUS_MODU_GORUNUM_RAPORU_20260516_171742.txt, android_app/app/src/main/python/static/seats/seats.css, apk_payload/static/seats/seats.css, static/seats/seats.css |
| EXCLUDE_PREFIXES | 50 | android_app/app/src/main/python/app.py, apk_payload/app.py, app.py, audit_reports/muavin_step3_flask_routes.txt, audit_reports/muavin_step4_suspicious_context.txt, audit_reports/muavin_step6_runtime_smoke.txt, backups/apk_sync_20260520_234501/app.py, tools/muavin_audit_step3_flask_routes.py |
| fab-sheet-solid-fix | 47 | AUTO_LIVE_STOP_AUDIT.txt, AYARLAR_DETAY_RAPORU.txt, LIVE_FLOW_V2_AUDIT.txt, PATCH_AUDIT_REPORT.md, PATCH_LIVE_AUDIT_REPORT.md, SEATS_CSS_OVERRIDE_REPORT.md, android_app/app/src/main/python/templates/seats.html, apk_payload/templates/seats.html |
| PROTECTED_PREFIXES | 45 | AYARLAR_DETAY_RAPORU.txt, android_app/app/src/main/python/app.py, apk_payload/app.py, app.py, audit_reports/muavin_step3_flask_routes.txt, audit_reports/muavin_step4_suspicious_context.txt, audit_reports/muavin_step6_runtime_smoke.txt, backups/apk_sync_20260520_234501/app.py |
| bak_only54_shift_fix_20260516_105927 | 42 | DURAK_AKISI_KAYNAK_RAPORU_20260518_205127.txt, KOLTUK_PANEL_YAMA_RAPORU_20260516_153819.txt, SEATS_DETAYLI_SISTEM_RAPORU_20260516_155924.txt, SON_YARIM_SAAT_YAMA_RAPORU_20260516_150801.txt |
| bak_bulk_nav_hide_v2_20260515_173615 | 41 | DURAK_AKISI_KAYNAK_RAPORU_20260518_205127.txt, SEATS_DETAYLI_SISTEM_RAPORU_20260516_155924.txt, SON_YARIM_SAAT_YAMA_RAPORU_20260516_150801.txt |
| bak_modal_bottom_nav_hide_v3_20260515_173940 | 41 | DURAK_AKISI_KAYNAK_RAPORU_20260518_205127.txt, SEATS_DETAYLI_SISTEM_RAPORU_20260516_155924.txt, SON_YARIM_SAAT_YAMA_RAPORU_20260516_150801.txt |
| bak_rollback_seat_label_overlap_fix_20260515_210127 | 41 | DURAK_AKISI_KAYNAK_RAPORU_20260518_205127.txt, SEATS_DETAYLI_SISTEM_RAPORU_20260516_155924.txt, SON_YARIM_SAAT_YAMA_RAPORU_20260516_150801.txt |
| bak_seat_label_overlap_fix_20260515_210033 | 41 | DURAK_AKISI_KAYNAK_RAPORU_20260518_205127.txt, SEATS_DETAYLI_SISTEM_RAPORU_20260516_155924.txt, SON_YARIM_SAAT_YAMA_RAPORU_20260516_150801.txt |
| bak_before_full_cleanup_audit_20260518_153638 | 39 | DURAK_AKISI_KAYNAK_RAPORU_20260518_205127.txt |
| voice-owner-fix-1 | 39 | AYARLAR_DETAY_RAPORU.txt, KOLTUK_PANEL_YAMA_RAPORU_20260516_153819.txt, LIVE_FLOW_V2_AUDIT.txt, PATCH_AUDIT_REPORT.md, SEATS_DETAYLI_SISTEM_RAPORU_20260516_155924.txt, SEATS_HTML_A_DAN_Z_RAPORU_20260518_162041.txt, SEATS_HTML_KALAN_YAMA_RAPORU_20260518_174156.txt, SEATS_HTML_TEMIZLIK_RAPORU_20260518_153638.txt |
| bak-ai-button-fix | 38 | proje_dosya_listesi.txt, proje_flask_baglanti_raporu.txt, proje_template_haritasi.txt, seats_baglanti_haritasi.txt, tracked_junk.txt, tracked_junk_safe.txt |
| drive-toggle-fix-1 | 38 | AYARLAR_DETAY_RAPORU.txt, KOLTUK_PANEL_YAMA_RAPORU_20260516_153819.txt, LIVE_FLOW_V2_AUDIT.txt, PATCH_AUDIT_REPORT.md, SEATS_DETAYLI_SISTEM_RAPORU_20260516_155924.txt, SEATS_HTML_A_DAN_Z_RAPORU_20260518_162041.txt, SEATS_HTML_KALAN_YAMA_RAPORU_20260518_174156.txt, SEATS_HTML_TEMIZLIK_RAPORU_20260518_153638.txt |
| bak_drive_dock_fix | 37 | proje_dosya_listesi.txt, proje_flask_baglanti_raporu.txt, proje_template_haritasi.txt, seats_baglanti_haritasi.txt |
| bak_selected_stop_memory_fix_20260518_153404 | 37 | DURAK_AKISI_KAYNAK_RAPORU_20260518_205127.txt, raporlar/asama1_durak_akisi_haritasi_20260520_110402.txt |
| bak_design_v1 | 36 | proje_dosya_listesi.txt, proje_flask_baglanti_raporu.txt, proje_template_haritasi.txt, seats_baglanti_haritasi.txt |
| muavin-clean-toggle-v10 | 36 | android_app/app/src/main/python/static/live_map/muavin_live_map_extra.css, android_app/app/src/main/python/static/live_map/muavin_live_map_extra.js, apk_payload/static/live_map/muavin_live_map_extra.css, apk_payload/static/live_map/muavin_live_map_extra.js, static/live_map/muavin_live_map_extra.css, static/live_map/muavin_live_map_extra.js |
| continue-trip-compact-final-fix | 34 | PATCH_LIVE_AUDIT_REPORT.md, android_app/app/src/main/python/static/continue/css_parts/10-compact-timeline-hero.css, apk_payload/templates/continue_trip.html, static/continue/css_parts/10-compact-timeline-hero.css |
| bak-drive-quick-menu-size-fix | 32 | proje_dosya_listesi.txt, proje_flask_baglanti_raporu.txt, proje_template_haritasi.txt, seats_baglanti_haritasi.txt, tracked_junk.txt, tracked_junk_safe.txt |
| bak_ticker_fix | 26 | DURAK_AKISI_KAYNAK_RAPORU_20260518_205127.txt, raporlar/asama1_durak_akisi_haritasi_20260520_110402.txt |
| bak-route-lock-fix | 25 | proje_dosya_listesi.txt, proje_flask_baglanti_raporu.txt, proje_template_haritasi.txt, tracked_junk.txt, tracked_junk_safe.txt |
| bak_live_dot_position_fix | 25 | DURAK_AKISI_KAYNAK_RAPORU_20260518_205127.txt, raporlar/asama1_durak_akisi_haritasi_20260520_110402.txt |
| bak_tv_marquee_fix | 25 | DURAK_AKISI_KAYNAK_RAPORU_20260518_205127.txt, raporlar/asama1_durak_akisi_haritasi_20260520_110402.txt |
| stopFlowFocusPatchLoaded | 25 | DURAK_AKISI_KAYNAK_RAPORU_20260518_205127.txt, LIVE_FLOW_V2_AUDIT.txt, SEATS_HTML_KALAN_YAMA_RAPORU_20260518_174156.txt, SEATS_HTML_TEMIZLIK_RAPORU_20260518_153638.txt, android_app/app/src/main/python/static/seats/patches/stop-flow-focus-patch.js, apk_payload/static/seats/patches/stop-flow-focus-patch.js, raporlar/asama1_durak_akisi_haritasi_20260520_110402.txt, raporlar/muavin_sistem_raw_20260520_105723.txt |
| bak_voice_mini_drive_fix | 22 | AYARLAR_DETAY_RAPORU.txt, DURAK_AKISI_KAYNAK_RAPORU_20260518_205127.txt, raporlar/asama1_durak_akisi_haritasi_20260520_110402.txt |
| live-hero-title-size-fix | 22 | PATCH_LIVE_AUDIT_REPORT.md, android_app/app/src/main/python/static/continue/css_parts/10-compact-timeline-hero.css, apk_payload/templates/continue_trip.html, static/continue/css_parts/10-compact-timeline-hero.css |
| bak_live_candidate_selected_fix_20260512_2346 | 21 | DURAK_AKISI_KAYNAK_RAPORU_20260518_205127.txt, raporlar/asama1_durak_akisi_haritasi_20260520_110402.txt |
| bak_live_stop_fix_final_20260512_2349 | 21 | DURAK_AKISI_KAYNAK_RAPORU_20260518_205127.txt, raporlar/asama1_durak_akisi_haritasi_20260520_110402.txt |
| bak_live_stale_fix_20260512_2354 | 20 | DURAK_AKISI_KAYNAK_RAPORU_20260518_205127.txt, raporlar/asama1_durak_akisi_haritasi_20260520_110402.txt |
| bak_fix_drive_css | 19 | proje_dosya_listesi.txt, proje_flask_baglanti_raporu.txt, proje_template_haritasi.txt, tracked_junk.txt, tracked_junk_safe.txt |
| bak_voice_row_fix_rollback | 19 | AYARLAR_DETAY_RAPORU.txt, DURAK_AKISI_KAYNAK_RAPORU_20260518_205127.txt, raporlar/asama1_durak_akisi_haritasi_20260520_110402.txt |
| bak_legend_lift_fix | 17 | DURAK_AKISI_KAYNAK_RAPORU_20260518_205127.txt, raporlar/asama1_durak_akisi_haritasi_20260520_110402.txt |
| fabDriveModeOverrideFixReady | 17 | SEATS_HTML_KALAN_YAMA_RAPORU_20260518_174156.txt, SEATS_HTML_TEMIZLIK_RAPORU_20260518_153638.txt, SURUS_MODU_GORUNUM_RAPORU_20260516_171742.txt, android_app/app/src/main/python/static/seats/patches/seat-layout-fab-pack.js, apk_payload/static/seats/patches/seat-layout-fab-pack.js, raporlar/muavin_sistem_raw_20260520_105723.txt, raporlar/yama_veri_etki_raw_20260520_111434.txt, static/seats/patches/seat-layout-fab-pack.js |
| muavin_audit_step2 | 17 | audit_reports/muavin_step2_report.txt, audit_reports/muavin_step3_flask_routes.txt |
| bak_fix_apk_voice_counts | 16 | AYARLAR_DETAY_RAPORU.txt, DURAK_AKISI_KAYNAK_RAPORU_20260518_205127.txt, raporlar/asama1_durak_akisi_haritasi_20260520_110402.txt |
| bak_fix_voice_seat_counts | 16 | AYARLAR_DETAY_RAPORU.txt, DURAK_AKISI_KAYNAK_RAPORU_20260518_205127.txt, raporlar/asama1_durak_akisi_haritasi_20260520_110402.txt |
| bak_fixed_bottom_legend | 16 | DURAK_AKISI_KAYNAK_RAPORU_20260518_205127.txt, raporlar/asama1_durak_akisi_haritasi_20260520_110402.txt |
| bak_full_scroll_fix | 16 | DURAK_AKISI_KAYNAK_RAPORU_20260518_205127.txt, raporlar/asama1_durak_akisi_haritasi_20260520_110402.txt |
| bak_raw_gpskm_format_fix | 16 | DURAK_AKISI_KAYNAK_RAPORU_20260518_205127.txt, raporlar/asama1_durak_akisi_haritasi_20260520_110402.txt |
| bak_route_direct_tts_summary_fix | 16 | DURAK_AKISI_KAYNAK_RAPORU_20260518_205127.txt, raporlar/asama1_durak_akisi_haritasi_20260520_110402.txt |
| bak_route_voice_fix | 16 | AYARLAR_DETAY_RAPORU.txt, DURAK_AKISI_KAYNAK_RAPORU_20260518_205127.txt, raporlar/asama1_durak_akisi_haritasi_20260520_110402.txt |
| intent-legend-mobile-fix | 16 | AYARLAR_DETAY_RAPORU.txt, PATCH_LIVE_AUDIT_REPORT.md, android_app/app/src/main/python/templates/ai_console.html, apk_payload/templates/ai_console.html, templates/ai_console.html |
| bak-clean-local-coords-ui-v2 | 15 | proje_dosya_listesi.txt, proje_flask_baglanti_raporu.txt, proje_template_haritasi.txt, tracked_junk.txt, tracked_junk_safe.txt |
| hero-device-stage-v2 | 15 | AYARLAR_DETAY_RAPORU.txt, android_app/app/src/main/python/templates/rehber.html, apk_payload/templates/rehber.html, templates/rehber.html |
| jsonv2 | 14 | android_app/app/src/main/python/static/seats/seats-time-prayer.js, apk_payload/static/seats/seats-time-prayer.js, audit_reports/muavin_step2_report.txt, audit_reports/muavin_step3_flask_routes.txt, audit_reports/muavin_step4_suspicious_context.txt, raporlar/muavin_sistem_raw_20260520_105723.txt, raporlar/yama_veri_etki_raw_20260520_111434.txt, static/seats/seats-time-prayer.js |
| arc_prefix | 13 | AYARLAR_DETAY_RAPORU.txt, AYARLAR_NET_RAPORU.txt, android_app/app/src/main/python/modules/backup_panel.py, apk_payload/modules/backup_panel.py, modules/backup_panel.py |
| bak-ai-url-fix | 13 | proje_dosya_listesi.txt, proje_flask_baglanti_raporu.txt, proje_template_haritasi.txt, tracked_junk.txt, tracked_junk_safe.txt |
| bak_add_missing_coords_helper_fix | 13 | DURAK_AKISI_KAYNAK_RAPORU_20260518_205127.txt, raporlar/asama1_durak_akisi_haritasi_20260520_110402.txt |
| bak_boarding_stop_fix_final | 13 | DURAK_AKISI_KAYNAK_RAPORU_20260518_205127.txt, raporlar/asama1_durak_akisi_haritasi_20260520_110402.txt |
| bak_fix_cachedStops_object_usage_final | 13 | DURAK_AKISI_KAYNAK_RAPORU_20260518_205127.txt, raporlar/asama1_durak_akisi_haritasi_20260520_110402.txt |
| bak_fix_object_object_route_strip | 13 | DURAK_AKISI_KAYNAK_RAPORU_20260518_205127.txt, raporlar/asama1_durak_akisi_haritasi_20260520_110402.txt |
| bak_fix_object_object_route_strip_v2 | 13 | DURAK_AKISI_KAYNAK_RAPORU_20260518_205127.txt, raporlar/asama1_durak_akisi_haritasi_20260520_110402.txt |
| bak_fix_stop_flow_after_api_stops_object | 13 | DURAK_AKISI_KAYNAK_RAPORU_20260518_205127.txt, raporlar/asama1_durak_akisi_haritasi_20260520_110402.txt |
| bak_gpskm_raw_write_fix | 13 | DURAK_AKISI_KAYNAK_RAPORU_20260518_205127.txt, raporlar/asama1_durak_akisi_haritasi_20260520_110402.txt |
| bak_pickup_live_full_fix | 13 | DURAK_AKISI_KAYNAK_RAPORU_20260518_205127.txt, raporlar/asama1_durak_akisi_haritasi_20260520_110402.txt |
| bak_tts_button_sync_fix | 13 | DURAK_AKISI_KAYNAK_RAPORU_20260518_205127.txt, raporlar/asama1_durak_akisi_haritasi_20260520_110402.txt |
| bak_tts_sync_fix | 13 | DURAK_AKISI_KAYNAK_RAPORU_20260518_205127.txt, raporlar/asama1_durak_akisi_haritasi_20260520_110402.txt |
| muavin-bottom-dock-v2 | 13 | AUTO_LIVE_STOP_AUDIT.txt, android_app/app/src/main/python/static/live_map/muavin_live_map_extra.css, android_app/app/src/main/python/static/live_map/muavin_live_map_extra.js, apk_payload/static/live_map/muavin_live_map_extra.css, apk_payload/static/live_map/muavin_live_map_extra.js, static/live_map/muavin_live_map_extra.css, static/live_map/muavin_live_map_extra.js |
| muavin_audit_step4_suspicious_context | 13 | audit_reports/muavin_step4_suspicious_context.txt, audit_reports/muavin_step7_global_appjs.txt |
| bak_bottom_legend_fixed_final | 12 | DURAK_AKISI_KAYNAK_RAPORU_20260518_205127.txt |
| muavin_audit_step1 | 12 | audit_reports/muavin_step2_report.txt |
| FAB_DRIVE_MODE_OVERRIDE_FIX | 11 | SEATS_HTML_A_DAN_Z_RAPORU_20260518_162041.txt, SEATS_HTML_KALAN_YAMA_RAPORU_20260518_174156.txt, SEATS_HTML_TEMIZLIK_RAPORU_20260518_153638.txt, SEATS_PATCH_ENVANTER_20260518_164328.txt, android_app/app/src/main/python/static/seats/patches/seat-layout-fab-pack.css, android_app/app/src/main/python/static/seats/patches/seat-layout-fab-pack.js, apk_payload/static/seats/patches/seat-layout-fab-pack.css, apk_payload/static/seats/patches/seat-layout-fab-pack.js |
| bak-bottom-buttons-fix | 11 | proje_dosya_listesi.txt, proje_flask_baglanti_raporu.txt, proje_template_haritasi.txt, tracked_junk.txt, tracked_junk_safe.txt |
| bak-save-button-final-fix | 11 | proje_dosya_listesi.txt, proje_flask_baglanti_raporu.txt, proje_template_haritasi.txt, tracked_junk.txt, tracked_junk_safe.txt |
| bak-title-fix | 11 | proje_dosya_listesi.txt, proje_flask_baglanti_raporu.txt, proje_template_haritasi.txt, tracked_junk.txt, tracked_junk_safe.txt |
| bottom-voice-listening-state-fix-style | 11 | KOLTUK_PANEL_YAMA_RAPORU_20260516_153819.txt, SEATS_DETAYLI_SISTEM_RAPORU_20260516_155924.txt, SEATS_HTML_A_DAN_Z_RAPORU_20260518_162041.txt, SEATS_HTML_TEMIZLIK_RAPORU_20260518_153638.txt, SEATS_PATCH_ENVANTER_20260518_164328.txt, SURUS_MODU_GORUNUM_RAPORU_20260516_171742.txt |
| live-hero-bus-brightness-fix | 11 | PATCH_LIVE_AUDIT_REPORT.md, android_app/app/src/main/python/static/continue/css_parts/10-compact-timeline-hero.css, apk_payload/templates/continue_trip.html, static/continue/css_parts/10-compact-timeline-hero.css |
| right-seat-column-spacing-fix-style | 11 | KOLTUK_PANEL_YAMA_RAPORU_20260516_153819.txt, SEATS_DETAYLI_SISTEM_RAPORU_20260516_155924.txt, SEATS_HTML_A_DAN_Z_RAPORU_20260518_162041.txt, SEATS_HTML_KALAN_YAMA_RAPORU_20260518_174156.txt, SEATS_HTML_TEMIZLIK_RAPORU_20260518_153638.txt, SEATS_PATCH_ENVANTER_20260518_164328.txt |
| stopSelectedToastPatchLoaded | 11 | SEATS_HTML_TEMIZLIK_RAPORU_20260518_153638.txt, android_app/app/src/main/python/static/seats/patches/stop-selected-toast.js, apk_payload/static/seats/patches/stop-selected-toast.js, raporlar/muavin_sistem_raw_20260520_105723.txt, raporlar/yama_veri_etki_raw_20260520_111434.txt, static/seats/patches/stop-selected-toast.js |
| VOICE_SUMMARY_PATCH_END | 10 | AYARLAR_DETAY_RAPORU.txt, PATCH_AUDIT_REPORT.md, android_app/app/src/main/python/static/seats/voice-commands.js, apk_payload/static/seats/voice-commands.js, static/seats/voice-commands.js |
| VOICE_SUMMARY_PATCH_START | 10 | AYARLAR_DETAY_RAPORU.txt, PATCH_AUDIT_REPORT.md, android_app/app/src/main/python/static/seats/voice-commands.js, apk_payload/static/seats/voice-commands.js, static/seats/voice-commands.js |
| ensureV2 | 10 | android_app/app/src/main/python/static/continue/continue_trip_ui.js, static/continue/continue_trip_ui.js |
| fab-drive-mode-override-fix-script | 10 | SEATS_HTML_A_DAN_Z_RAPORU_20260518_162041.txt, SEATS_HTML_KALAN_YAMA_RAPORU_20260518_174156.txt, SEATS_HTML_TEMIZLIK_RAPORU_20260518_153638.txt, SEATS_PATCH_ENVANTER_20260518_164328.txt, SURUS_MODU_GORUNUM_RAPORU_20260516_171742.txt |
| fab-drive-mode-override-fix-style | 10 | SEATS_HTML_A_DAN_Z_RAPORU_20260518_162041.txt, SEATS_HTML_KALAN_YAMA_RAPORU_20260518_174156.txt, SEATS_HTML_TEMIZLIK_RAPORU_20260518_153638.txt, SEATS_PATCH_ENVANTER_20260518_164328.txt, SURUS_MODU_GORUNUM_RAPORU_20260516_171742.txt |
| stop-flow-focus-patch-script | 10 | SEATS_DETAYLI_SISTEM_RAPORU_20260516_155924.txt, SEATS_HTML_A_DAN_Z_RAPORU_20260518_162041.txt, SEATS_HTML_KALAN_YAMA_RAPORU_20260518_174156.txt, SEATS_HTML_TEMIZLIK_RAPORU_20260518_153638.txt, SEATS_PATCH_ENVANTER_20260518_164328.txt |
| stop-flow-focus-patch-style | 10 | SEATS_DETAYLI_SISTEM_RAPORU_20260516_155924.txt, SEATS_HTML_A_DAN_Z_RAPORU_20260518_162041.txt, SEATS_HTML_KALAN_YAMA_RAPORU_20260518_174156.txt, SEATS_HTML_TEMIZLIK_RAPORU_20260518_153638.txt, SEATS_PATCH_ENVANTER_20260518_164328.txt |
| BOTTOM_VOICE_LISTENING_STATE_FIX_END | 9 | KOLTUK_PANEL_YAMA_RAPORU_20260516_153819.txt, SEATS_DETAYLI_SISTEM_RAPORU_20260516_155924.txt, SEATS_HTML_A_DAN_Z_RAPORU_20260518_162041.txt, SEATS_HTML_TEMIZLIK_RAPORU_20260518_153638.txt, SON_YARIM_SAAT_YAMA_RAPORU_20260516_150801.txt |
| BOTTOM_VOICE_LISTENING_STATE_FIX_START | 9 | KOLTUK_PANEL_YAMA_RAPORU_20260516_153819.txt, SEATS_DETAYLI_SISTEM_RAPORU_20260516_155924.txt, SEATS_HTML_A_DAN_Z_RAPORU_20260518_162041.txt, SEATS_HTML_TEMIZLIK_RAPORU_20260518_153638.txt, SON_YARIM_SAAT_YAMA_RAPORU_20260516_150801.txt, SURUS_MODU_GORUNUM_RAPORU_20260516_171742.txt |
| MUAVIN_BOTTOM_DOCK_FINAL_V5 | 9 | android_app/app/src/main/python/static/live_map/muavin_live_map_extra.css, android_app/app/src/main/python/static/live_map/muavin_live_map_extra.js, apk_payload/static/live_map/muavin_live_map_extra.css, apk_payload/static/live_map/muavin_live_map_extra.js, static/live_map/muavin_live_map_extra.css, static/live_map/muavin_live_map_extra.js |
| MUAVIN_CLEAN_START_MODE_V10 | 9 | android_app/app/src/main/python/static/live_map/muavin_live_map_extra.css, android_app/app/src/main/python/static/live_map/muavin_live_map_extra.js, apk_payload/static/live_map/muavin_live_map_extra.css, apk_payload/static/live_map/muavin_live_map_extra.js, static/live_map/muavin_live_map_extra.css, static/live_map/muavin_live_map_extra.js |
| MUAVIN_MAP_UI_FINAL_V6 | 9 | android_app/app/src/main/python/static/live_map/muavin_live_map_extra.css, android_app/app/src/main/python/static/live_map/muavin_live_map_extra.js, apk_payload/static/live_map/muavin_live_map_extra.css, apk_payload/static/live_map/muavin_live_map_extra.js, static/live_map/muavin_live_map_extra.css, static/live_map/muavin_live_map_extra.js |
| MUAVIN_NEXT_OPS_BUBBLE_DRAG_V4 | 9 | android_app/app/src/main/python/static/live_map/muavin_live_map_extra.css, android_app/app/src/main/python/static/live_map/muavin_live_map_extra.js, apk_payload/static/live_map/muavin_live_map_extra.css, apk_payload/static/live_map/muavin_live_map_extra.js, static/live_map/muavin_live_map_extra.css, static/live_map/muavin_live_map_extra.js |
| MUAVIN_NEXT_OPS_FINAL_V1 | 9 | android_app/app/src/main/python/static/live_map/muavin_live_map_extra.css, android_app/app/src/main/python/static/live_map/muavin_live_map_extra.js, apk_payload/static/live_map/muavin_live_map_extra.css, apk_payload/static/live_map/muavin_live_map_extra.js, static/live_map/muavin_live_map_extra.css, static/live_map/muavin_live_map_extra.js |
| MUAVIN_REMOVE_COMPASS_V7 | 9 | android_app/app/src/main/python/static/live_map/muavin_live_map_extra.css, android_app/app/src/main/python/static/live_map/muavin_live_map_extra.js, apk_payload/static/live_map/muavin_live_map_extra.css, apk_payload/static/live_map/muavin_live_map_extra.js, static/live_map/muavin_live_map_extra.css, static/live_map/muavin_live_map_extra.js |
| active_patches | 9 | tools/audit_patches.py |
| bak-overflow-fix-20260502_011712 | 9 | proje_dosya_listesi.txt, proje_flask_baglanti_raporu.txt, proje_template_haritasi.txt, tracked_junk.txt, tracked_junk_safe.txt |
| bak-route-input-fix | 9 | proje_dosya_listesi.txt, proje_flask_baglanti_raporu.txt, proje_template_haritasi.txt, tracked_junk.txt, tracked_junk_safe.txt |
| consignment-photo-modal-fix | 9 | android_app/app/src/main/python/templates/consignments.html, apk_payload/templates/consignments.html, audit_reports/muavin_step5_active_bug_context.txt, templates/consignments.html |
| muavinModalBottomNavAutohideV3 | 9 | android_app/app/src/main/python/static/seats/patches/modal-bottom-nav-autohide.js, apk_payload/static/seats/patches/modal-bottom-nav-autohide.js, raporlar/muavin_sistem_raw_20260520_105723.txt, raporlar/yama_veri_etki_raw_20260520_111434.txt, static/seats/patches/modal-bottom-nav-autohide.js |
| project_tree_audit | 9 | AYARLAR_DETAY_RAPORU.txt, HOST_HOSTES_SOY_AGACI.md, HOST_HOSTES_SOY_AGACI_SATIRLI.md, PATCH_AUDIT_REPORT.md, PROJE_AGAC_RAPORU.md, TOOL_PATHS.txt, TOOL_TREE.txt |
| setNav3d | 9 | android_app/app/src/main/python/static/live_map/muavin_live_map_extra.js, apk_payload/static/live_map/muavin_live_map_extra.js, static/live_map/muavin_live_map_extra.js |
| 11h2v9h6v-6h2v6h6v-9h2z | 8 | AYARLAR_DETAY_RAPORU.txt, AYARLAR_NET_RAPORU.txt, android_app/app/src/main/python/templates/reports.html, apk_payload/templates/reports.html, templates/reports.html |
| RIGHT_SEAT_COLUMN_SPACING_FIX | 8 | SEATS_DETAYLI_SISTEM_RAPORU_20260516_155924.txt, SEATS_HTML_A_DAN_Z_RAPORU_20260518_162041.txt, SEATS_HTML_KALAN_YAMA_RAPORU_20260518_174156.txt, SEATS_HTML_TEMIZLIK_RAPORU_20260518_153638.txt, SEATS_PATCH_ENVANTER_20260518_164328.txt, android_app/app/src/main/python/static/seats/patches/seat-layout-fab-pack.css, apk_payload/static/seats/patches/seat-layout-fab-pack.css, static/seats/patches/seat-layout-fab-pack.css |
| RIGHT_SEAT_COLUMN_SPACING_FIX_END | 8 | KOLTUK_PANEL_YAMA_RAPORU_20260516_153819.txt, SEATS_HTML_A_DAN_Z_RAPORU_20260518_162041.txt, SEATS_HTML_KALAN_YAMA_RAPORU_20260518_174156.txt, SEATS_HTML_TEMIZLIK_RAPORU_20260518_153638.txt, SON_YARIM_SAAT_YAMA_RAPORU_20260516_150801.txt, SURUS_MODU_GORUNUM_RAPORU_20260516_171742.txt |
| bak-drive-speed-fixed | 8 | proje_dosya_listesi.txt, seats_baglanti_haritasi.txt, tracked_junk.txt, tracked_junk_safe.txt |
| bak-route-flow-real-fix | 8 | proje_dosya_listesi.txt, seats_baglanti_haritasi.txt, tracked_junk.txt, tracked_junk_safe.txt |
| continue-v2-distance-line | 8 | android_app/app/src/main/python/static/continue/continue_trip_ui.js, android_app/app/src/main/python/static/continue/css_parts/50-live-v2-top-glow.css, static/continue/continue_trip_ui.js, static/continue/css_parts/50-live-v2-top-glow.css |
| propFix | 8 | AYARLAR_DETAY_RAPORU.txt, _unused_review/static/vendor/jquery/jquery-3.7.1.min.js |
| 13h3v-2H1v2zm10-9h2V1h-2v3zm7 | 7 | AYARLAR_NET_RAPORU.txt, android_app/app/src/main/python/templates/reports.html, apk_payload/templates/reports.html, templates/reports.html |
| 13h3v-2h-3v2zm-7 | 7 | AYARLAR_NET_RAPORU.txt, android_app/app/src/main/python/templates/reports.html, apk_payload/templates/reports.html, templates/reports.html |
| 7h2v-3h-2v3zM6 | 7 | AYARLAR_NET_RAPORU.txt, android_app/app/src/main/python/templates/reports.html, apk_payload/templates/reports.html, templates/reports.html |
| RIGHT_SEAT_COLUMN_SPACING_FIX_START | 7 | KOLTUK_PANEL_YAMA_RAPORU_20260516_153819.txt, SEATS_HTML_A_DAN_Z_RAPORU_20260518_162041.txt, SEATS_HTML_KALAN_YAMA_RAPORU_20260518_174156.txt, SEATS_HTML_TEMIZLIK_RAPORU_20260518_153638.txt, SON_YARIM_SAAT_YAMA_RAPORU_20260516_150801.txt |
| modal-bottom-nav-autohide-v3-script | 7 | SEATS_DETAYLI_SISTEM_RAPORU_20260516_155924.txt, SEATS_HTML_A_DAN_Z_RAPORU_20260518_162041.txt, SEATS_HTML_TEMIZLIK_RAPORU_20260518_153638.txt, SEATS_PATCH_ENVANTER_20260518_164328.txt |
| modal-bottom-nav-autohide-v3-style | 7 | SEATS_DETAYLI_SISTEM_RAPORU_20260516_155924.txt, SEATS_HTML_A_DAN_Z_RAPORU_20260518_162041.txt, SEATS_HTML_TEMIZLIK_RAPORU_20260518_153638.txt, SEATS_PATCH_ENVANTER_20260518_164328.txt |
| END_MUAVIN_LIVE_MAP_EXTRA_CSS_LINK_V1 | 6 | AYARLAR_DETAY_RAPORU.txt, android_app/app/src/main/python/templates/live_map.html, apk_payload/templates/live_map.html, templates/live_map.html |
| END_MUAVIN_LIVE_MAP_EXTRA_JS_LINK_V1 | 6 | AYARLAR_DETAY_RAPORU.txt, android_app/app/src/main/python/templates/live_map.html, apk_payload/templates/live_map.html, templates/live_map.html |
| MUAVIN_GOOGLE_LOCATION_V2 | 6 | android_app/app/src/main/python/static/live_map/muavin_live_map_extra.js, apk_payload/static/live_map/muavin_live_map_extra.js, static/live_map/muavin_live_map_extra.js |
| MUAVIN_LIVE_MAP_EXTRA_CSS_LINK_V1 | 6 | AYARLAR_DETAY_RAPORU.txt, android_app/app/src/main/python/templates/live_map.html, apk_payload/templates/live_map.html, templates/live_map.html |
| MUAVIN_LIVE_MAP_EXTRA_JS_LINK_V1 | 6 | AYARLAR_DETAY_RAPORU.txt, android_app/app/src/main/python/templates/live_map.html, apk_payload/templates/live_map.html, templates/live_map.html |
| STOP_FLOW_FOCUS_PATCH | 6 | SEATS_DETAYLI_SISTEM_RAPORU_20260516_155924.txt, SEATS_HTML_A_DAN_Z_RAPORU_20260518_162041.txt, SEATS_HTML_KALAN_YAMA_RAPORU_20260518_174156.txt, SEATS_HTML_TEMIZLIK_RAPORU_20260518_153638.txt, SEATS_PATCH_ENVANTER_20260518_164328.txt |
| VOICE_MAP_FULLSCREEN_PATCH_START | 6 | AYARLAR_DETAY_RAPORU.txt, android_app/app/src/main/python/templates/live_map.html, apk_payload/templates/live_map.html, templates/live_map.html |
| allowed_prefixes | 6 | android_app/app/src/main/python/modules/backup_panel.py, apk_payload/modules/backup_panel.py, modules/backup_panel.py |
| bak_drive_voice_abort_fix | 6 | AYARLAR_DETAY_RAPORU.txt |
| bak_patch2_runtime_reader_only | 6 | DURAK_AKISI_KAYNAK_RAPORU_20260518_205127.txt |
| bak_voice_button_fix | 6 | AYARLAR_DETAY_RAPORU.txt |
| bak_voice_button_state_fix | 6 | AYARLAR_DETAY_RAPORU.txt |
| bak_voice_stop_ops_patch | 6 | AYARLAR_DETAY_RAPORU.txt |
| clearfix | 6 | AYARLAR_DETAY_RAPORU.txt, android_app/app/src/main/python/static/vendor/bootstrap/bootstrap.min.css, apk_payload/static/vendor/bootstrap/bootstrap.min.css, static/vendor/bootstrap/bootstrap.min.css |
| continue-v2-dot | 6 | android_app/app/src/main/python/static/continue/continue_trip_ui.js, android_app/app/src/main/python/static/continue/css_parts/50-live-v2-top-glow.css, static/continue/continue_trip_ui.js, static/continue/css_parts/50-live-v2-top-glow.css |
| continueLiveV2Distance | 6 | android_app/app/src/main/python/static/continue/continue_trip_ui.js, static/continue/continue_trip_ui.js |
| dragAwareV4 | 6 | android_app/app/src/main/python/static/live_map/muavin_live_map_extra.js, apk_payload/static/live_map/muavin_live_map_extra.js, static/live_map/muavin_live_map_extra.js |
| home-route-link-fix | 6 | AYARLAR_DETAY_RAPORU.txt, android_app/app/src/main/python/templates/index.html, apk_payload/templates/index.html, templates/index.html |
| live-metric-hint-compact-fix | 6 | PATCH_LIVE_AUDIT_REPORT.md, android_app/app/src/main/python/static/continue/css_parts/30-sheet-bag-photo.css, apk_payload/templates/continue_trip.html, static/continue/css_parts/30-sheet-bag-photo.css |
| muavinNav3dModeFinal | 6 | android_app/app/src/main/python/static/live_map/muavin_live_map_extra.js, apk_payload/static/live_map/muavin_live_map_extra.js, static/live_map/muavin_live_map_extra.js |
| nextOpsDragV4 | 6 | android_app/app/src/main/python/static/live_map/muavin_live_map_extra.js, apk_payload/static/live_map/muavin_live_map_extra.js, static/live_map/muavin_live_map_extra.js |
| orphan_patches | 6 | tools/audit_patches.py |
| position-fixed | 6 | AYARLAR_DETAY_RAPORU.txt, android_app/app/src/main/python/static/vendor/bootstrap/bootstrap.min.css, apk_payload/static/vendor/bootstrap/bootstrap.min.css, static/vendor/bootstrap/bootstrap.min.css |
| postDispatch | 6 | AYARLAR_DETAY_RAPORU.txt, _unused_review/static/vendor/jquery/jquery-3.7.1.min.js |
| right-seat-column-spacing-fix | 6 | AUTO_LIVE_STOP_AUDIT.txt, PATCH_AUDIT_REPORT.md, PATCH_LIVE_AUDIT_REPORT.md |
| syncV2Texts | 6 | android_app/app/src/main/python/static/continue/continue_trip_ui.js, static/continue/continue_trip_ui.js |
| BOTTOM_VOICE_LISTENING_STATE_FIX | 5 | SEATS_DETAYLI_SISTEM_RAPORU_20260516_155924.txt, SEATS_HTML_A_DAN_Z_RAPORU_20260518_162041.txt, SEATS_HTML_TEMIZLIK_RAPORU_20260518_153638.txt, SEATS_PATCH_ENVANTER_20260518_164328.txt |
| FAB_DRIVE_MODE_OVERRIDE_FIX_START | 5 | SEATS_HTML_A_DAN_Z_RAPORU_20260518_162041.txt, SEATS_HTML_KALAN_YAMA_RAPORU_20260518_174156.txt, SEATS_HTML_TEMIZLIK_RAPORU_20260518_153638.txt, SURUS_MODU_GORUNUM_RAPORU_20260516_171742.txt |
| MODAL_BOTTOM_NAV_AUTOHIDE_V3 | 5 | SEATS_DETAYLI_SISTEM_RAPORU_20260516_155924.txt, SEATS_HTML_A_DAN_Z_RAPORU_20260518_162041.txt, SEATS_HTML_TEMIZLIK_RAPORU_20260518_153638.txt, SEATS_PATCH_ENVANTER_20260518_164328.txt |
| STOP_SELECTED_TOAST_PATCH | 5 | SEATS_DETAYLI_SISTEM_RAPORU_20260516_155924.txt, SEATS_HTML_A_DAN_Z_RAPORU_20260518_162041.txt, SEATS_HTML_TEMIZLIK_RAPORU_20260518_153638.txt, SEATS_PATCH_ENVANTER_20260518_164328.txt |
| bak_voice_owner_fix | 5 | AYARLAR_DETAY_RAPORU.txt, raporlar/asama1_durak_akisi_haritasi_20260520_110402.txt |
| cargo-photo-badge-position-fix | 5 | android_app/app/src/main/python/static/continue/css_parts/40-cargo-gender-summary.css, apk_payload/templates/continue_trip.html, static/continue/css_parts/40-cargo-gender-summary.css |
| live-metric-compact-final-fix | 5 | android_app/app/src/main/python/static/continue/css_parts/30-sheet-bag-photo.css, apk_payload/templates/continue_trip.html, static/continue/css_parts/30-sheet-bag-photo.css |
| muavin_audit_step7_global_appjs | 5 | audit_reports/muavin_step7_global_appjs.txt |
| route-sheet-no-flash-fix | 5 | audit_reports/muavin_step5_active_bug_context.txt, audit_reports/muavin_step9_sync_plan.txt, templates/index.html, tools/muavin_audit_step9_sync_plan.py |
| sheet-offload-button-text-fix | 5 | android_app/app/src/main/python/static/continue/css_parts/30-sheet-bag-photo.css, apk_payload/templates/continue_trip.html, static/continue/css_parts/30-sheet-bag-photo.css |
| sheet-seat-number-spacing-fix | 5 | android_app/app/src/main/python/static/continue/css_parts/30-sheet-bag-photo.css, apk_payload/templates/continue_trip.html, static/continue/css_parts/30-sheet-bag-photo.css |
| url_prefix | 5 | android_app/app/src/main/python/modules/bags/__init__.py, apk_payload/modules/bags/__init__.py, modules/bags/__init__.py, proje_flask_baglanti_raporu.txt |
| 13h14v-2H5v2z | 4 | AYARLAR_NET_RAPORU.txt, android_app/app/src/main/python/templates/reports.html, apk_payload/templates/reports.html, templates/reports.html |

## 14) Debug/TODO/Alert İzleri
| Dosya | Satır | Satır içeriği |
| --- | --- | --- |
| proje_dosya_listesi.txt | 1440 | ./.venv/lib/python3.12/site-packages/werkzeug/debug/shared/debugger.js |
| proje_dosya_listesi.txt | 3058 | ./.venv/lib/python3.13/site-packages/werkzeug/debug/shared/debugger.js |
| AYARLAR_DETAY_RAPORU.txt | 8468 | 444:       alert('Hata: ' + (j.msg \ |
| AYARLAR_DETAY_RAPORU.txt | 9352 | 661:                 !function(n,t){"object"==typeof exports&&"object"==typeof module?module.exports=t():"function"==typeof define&&define.amd?define([],t):"object"==typeof exports... |
| AYARLAR_DETAY_RAPORU.txt | 9357 | 661:                 !function(n,t){"object"==typeof exports&&"object"==typeof module?module.exports=t():"function"==typeof define&&define.amd?define([],t):"object"==typeof exports... |
| AYARLAR_DETAY_RAPORU.txt | 10982 | 444:       alert('Hata: ' + (j.msg \ |
| AYARLAR_DETAY_RAPORU.txt | 13839 | 444:       alert('Hata: ' + (j.msg \ |
| AYARLAR_DETAY_RAPORU.txt | 14844 | 9: .fa-sr-only,.fa-sr-only-focusable:not(:focus),.sr-only,.sr-only-focusable:not(:focus){position:absolute;width:1px;height:1px;padding:0;margin:-1px;overflow:hidden;clip:rect(0,0,... |
| AYARLAR_DETAY_RAPORU.txt | 17100 | 474:       console.log("Saat profili API'den yüklendi:", apiSchedule); |
| AYARLAR_DETAY_RAPORU.txt | 20614 | 474:       console.log("Saat profili API'den yüklendi:", apiSchedule); |
| AYARLAR_DETAY_RAPORU.txt | 24128 | 474:       console.log("Saat profili API'den yüklendi:", apiSchedule); |
| SEFER_RAPORU_KAYNAK_RAPORU.txt | 527 | 503:           alert("PrintBridge bulunamadı. Tarayıcı yazdırma deneniyor."); |
| SEFER_RAPORU_KAYNAK_RAPORU.txt | 530 | 506:         alert("PrintBridge hatası: " + err); |
| SEFER_RAPORU_KAYNAK_RAPORU.txt | 544 | 503:           alert("PrintBridge bulunamadı. Tarayıcı yazdırma deneniyor."); |
| SEFER_RAPORU_KAYNAK_RAPORU.txt | 547 | 506:         alert("PrintBridge hatası: " + err); |
| SEFER_RAPORU_KAYNAK_RAPORU.txt | 548 | 507:         console.log("PrintBridge error:", err); |
| SEFER_RAPORU_KAYNAK_RAPORU.txt | 561 | 503:           alert("PrintBridge bulunamadı. Tarayıcı yazdırma deneniyor."); |
| SEFER_RAPORU_KAYNAK_RAPORU.txt | 564 | 506:         alert("PrintBridge hatası: " + err); |
| SEFER_RAPORU_KAYNAK_RAPORU.txt | 565 | 507:         console.log("PrintBridge error:", err); |
| SEFER_RAPORU_KAYNAK_RAPORU.txt | 578 | 503:           alert("PrintBridge bulunamadı. Tarayıcı yazdırma deneniyor."); |
| SEFER_RAPORU_KAYNAK_RAPORU.txt | 581 | 506:         alert("PrintBridge hatası: " + err); |
| SEFER_RAPORU_KAYNAK_RAPORU.txt | 582 | 507:         console.log("PrintBridge error:", err); |
| SEFER_RAPORU_KAYNAK_RAPORU.txt | 594 | 503:           alert("PrintBridge bulunamadı. Tarayıcı yazdırma deneniyor."); |
| SEFER_RAPORU_KAYNAK_RAPORU.txt | 597 | 506:         alert("PrintBridge hatası: " + err); |
| SEFER_RAPORU_KAYNAK_RAPORU.txt | 598 | 507:         console.log("PrintBridge error:", err); |
| SEFER_RAPORU_KAYNAK_RAPORU.txt | 604 | 513:         alert("Yazdırma ekranı açılamadı."); |
| SEFER_RAPORU_KAYNAK_RAPORU.txt | 610 | 503:           alert("PrintBridge bulunamadı. Tarayıcı yazdırma deneniyor."); |
| SEFER_RAPORU_KAYNAK_RAPORU.txt | 613 | 506:         alert("PrintBridge hatası: " + err); |
| SEFER_RAPORU_KAYNAK_RAPORU.txt | 614 | 507:         console.log("PrintBridge error:", err); |
| SEFER_RAPORU_KAYNAK_RAPORU.txt | 620 | 513:         alert("Yazdırma ekranı açılamadı."); |
| SEFER_RAPORU_KAYNAK_RAPORU.txt | 628 | 503:           alert("PrintBridge bulunamadı. Tarayıcı yazdırma deneniyor."); |
| SEFER_RAPORU_KAYNAK_RAPORU.txt | 631 | 506:         alert("PrintBridge hatası: " + err); |
| SEFER_RAPORU_KAYNAK_RAPORU.txt | 632 | 507:         console.log("PrintBridge error:", err); |
| SEFER_RAPORU_KAYNAK_RAPORU.txt | 638 | 513:         alert("Yazdırma ekranı açılamadı."); |
| SEFER_RAPORU_KAYNAK_RAPORU.txt | 647 | 507:         console.log("PrintBridge error:", err); |
| SEFER_RAPORU_KAYNAK_RAPORU.txt | 653 | 513:         alert("Yazdırma ekranı açılamadı."); |
| SEFER_RAPORU_KAYNAK_RAPORU.txt | 1791 | 503:           alert("PrintBridge bulunamadı. Tarayıcı yazdırma deneniyor."); |
| SEFER_RAPORU_KAYNAK_RAPORU.txt | 1796 | 503:           alert("PrintBridge bulunamadı. Tarayıcı yazdırma deneniyor."); |
| SEFER_RAPORU_KAYNAK_RAPORU.txt | 1799 | 506:         alert("PrintBridge hatası: " + err); |
| SEFER_RAPORU_KAYNAK_RAPORU.txt | 1800 | 507:         console.log("PrintBridge error:", err); |
| SEFER_RAPORU_KAYNAK_RAPORU.txt | 1804 | 506:         alert("PrintBridge hatası: " + err); |
| SEFER_RAPORU_KAYNAK_RAPORU.txt | 1805 | 507:         console.log("PrintBridge error:", err); |
| SEFER_RAPORU_KAYNAK_RAPORU.txt | 1811 | 506:         alert("PrintBridge hatası: " + err); |
| SEFER_RAPORU_KAYNAK_RAPORU.txt | 1812 | 507:         console.log("PrintBridge error:", err); |
| SEFER_RAPORU_KAYNAK_RAPORU.txt | 1822 | 513:         alert("Yazdırma ekranı açılamadı."); |
| LIVE_FLOW_V2_AUDIT.txt | 526 | 806: [stopFlow] console.log("recordStopFlowEvent error", err); |
| LIVE_FLOW_V2_AUDIT.txt | 2172 | 2543:         console.log("approach speak error", err); |
| tools/muavin_audit_step1.py | 273 | # 7) TODO / FIXME / HACK / ERROR İZLERİ |
| tools/muavin_audit_step1.py | 278 | suspicious = re.compile(r"\b(TODO\ |
| tools/muavin_audit_step1.py | 300 | print("✅ Şüpheli TODO/FIXME/HACK/BUG/debugger izi yok") |
| tools/muavin_audit_step2.py | 537 | "alert(", |
| tools/muavin_audit_step2.py | 538 | "debugger", |
| tools/muavin_audit_step2.py | 539 | "TODO", |
| tools/muavin_audit_step2.py | 540 | "FIXME", |
| tools/muavin_full_audit_v1.py | 413 | PATCH_LINE_RE = re.compile(r"(patch\ |
| tools/muavin_full_audit_v1.py | 420 | DEBUG_RE = re.compile(r"(console\.log\ |
| tools/muavin_full_audit_v1.py | 576 | md.append("\n## 25) Debug / TODO / Alert İzleri") |
| templates/add_route.html | 376 | alert('Hat adı ve en az bir durak gerekli.'); |
| templates/consignments.html | 970 | if(j.ok) location.reload(); else alert(j.msg \ |
| templates/consignments.html | 981 | if(j.ok) location.reload(); else alert(j.msg \ |
| templates/consignments.html | 993 | if(j.ok) location.reload(); else alert(j.msg \ |
| templates/hesap.html | 1910 | alert("PrintBridge bulunamadı. Tarayıcı yazdırma deneniyor."); |
| templates/hesap.html | 1913 | alert("PrintBridge hatası: " + err); |
| templates/hesap.html | 1914 | console.log("PrintBridge error:", err); |
| templates/hesap.html | 1920 | alert("Yazdırma ekranı açılamadı."); |
| templates/hesap.html | 2386 | alert("Paylaşılacak hareket yok."); |
| templates/route_edit.html | 699 | alert("Önce hat adını yaz."); |
| templates/route_edit.html | 704 | alert("Durak listesi boş."); |
| templates/route_edit.html | 760 | alert("Lat ve Lng gir."); |
| templates/route_edit.html | 782 | alert(j.msg \ |
| templates/route_edit.html | 790 | alert("Bağlantı hatası: " + e.message); |
| templates/route_stops.html | 46 | if(!j.ok){ alert(j.msg \ |
| templates/route_stops.html | 55 | if(lat.value==='' \ |
| templates/route_stops.html | 69 | else { alert(jj.msg \ |
| templates/route_stops.html | 70 | }catch(e){ alert('Bağlantı hatası'); } |
| templates/routes_list.html | 444 | alert('Hata: ' + (j.msg \ |
| templates/routes_list.html | 447 | alert('Bağlantı hatası'); |
| templates/trip_report.html | 503 | alert("PrintBridge bulunamadı. Tarayıcı yazdırma deneniyor."); |
| templates/trip_report.html | 506 | alert("PrintBridge hatası: " + err); |
| templates/trip_report.html | 507 | console.log("PrintBridge error:", err); |
| templates/trip_report.html | 513 | alert("Yazdırma ekranı açılamadı."); |
| templates/live_map.html | 2543 | console.log("approach speak error", err); |
| templates/live_map.html | 2547 | function hideApproachAlert(){ |
| templates/live_map.html | 2555 | function showApproachAlert(stop, km, level){ |
| templates/live_map.html | 2584 | function checkApproachAlert(){ |
| templates/live_map.html | 2591 | hideApproachAlert(); |
| templates/live_map.html | 2599 | hideApproachAlert(); |
| templates/live_map.html | 2609 | showApproachAlert(target, km, level); |
| templates/live_map.html | 2632 | checkApproachAlert(); |
| templates/live_map.html | 2643 | console.log("Konum alınamadı", err); |
| templates/live_map.html | 2718 | hideApproachAlert(); |
| templates/live_map.html | 2723 | hideApproachAlert(); |
| templates/live_map.html | 2746 | hideApproachAlert(); |
| templates/settings_backup.html | 738 | alert("Önce bir .zip yedek dosyası seç."); |
| raporlar/yama_veri_etki_raw_20260520_111434.txt | 322 | 473:       console.log("Saat profili API'den yüklendi:", apiSchedule); |
| audit_reports/muavin_step2_report.txt | 337 | ⚠️ 'alert(' izi: 57 |
| audit_reports/muavin_step2_report.txt | 378 | ⚠️ 'debugger' izi: 3 |
| audit_reports/muavin_step2_report.txt | 382 | ⚠️ 'TODO' izi: 4 |
| audit_reports/muavin_step2_report.txt | 387 | ⚠️ 'FIXME' izi: 4 |
| audit_reports/muavin_step4_suspicious_context.txt | 88 | 970:   if(j.ok) location.reload(); else alert(j.msg \ |
| audit_reports/muavin_step4_suspicious_context.txt | 99 | 981:   if(j.ok) location.reload(); else alert(j.msg \ |
| audit_reports/muavin_step4_suspicious_context.txt | 152 | 55:       if(lat.value==='' \ |
| audit_reports/muavin_step4_suspicious_context.txt | 166 | 69:         else { alert(jj.msg \ |
| audit_reports/muavin_step4_suspicious_context.txt | 167 | 70:       }catch(e){ alert('Bağlantı hatası'); } |
| audit_reports/muavin_step4_suspicious_context.txt | 274 | 970:   if(j.ok) location.reload(); else alert(j.msg \ |
| audit_reports/muavin_step4_suspicious_context.txt | 285 | 981:   if(j.ok) location.reload(); else alert(j.msg \ |
| audit_reports/muavin_step4_suspicious_context.txt | 326 | 55:       if(lat.value==='' \ |
| audit_reports/muavin_step4_suspicious_context.txt | 340 | 69:         else { alert(jj.msg \ |
| audit_reports/muavin_step4_suspicious_context.txt | 2249 | 370:       alert("Koltuk bilgisi bulunamadı."); |
| audit_reports/muavin_step4_suspicious_context.txt | 2409 | 285:         alert(data.error \ |
| audit_reports/muavin_step4_suspicious_context.txt | 2441 | 285:         alert(data.error \ |
| audit_reports/muavin_step4_suspicious_context.txt | 2775 | 285:         alert(data.error \ |
| audit_reports/muavin_step4_suspicious_context.txt | 2807 | 285:         alert(data.error \ |
| audit_reports/muavin_step4_suspicious_context.txt | 2839 | 285:         alert(data.error \ |
| audit_reports/muavin_step4_suspicious_context.txt | 3278 | 370:       alert("Koltuk bilgisi bulunamadı."); |
| audit_reports/muavin_step4_suspicious_context.txt | 3438 | 285:         alert(data.error \ |
| audit_reports/muavin_step4_suspicious_context.txt | 3470 | 285:         alert(data.error \ |
| audit_reports/muavin_step4_suspicious_context.txt | 3804 | 285:         alert(data.error \ |
| audit_reports/muavin_step4_suspicious_context.txt | 3836 | 285:         alert(data.error \ |
| audit_reports/muavin_step4_suspicious_context.txt | 3868 | 285:         alert(data.error \ |
| audit_reports/muavin_step5_active_bug_context.txt | 896 | 970:   if(j.ok) location.reload(); else alert(j.msg \ |
| audit_reports/muavin_step5_active_bug_context.txt | 907 | 981:   if(j.ok) location.reload(); else alert(j.msg \ |
| audit_reports/muavin_step5_active_bug_context.txt | 919 | 993:   if(j.ok) location.reload(); else alert(j.msg \ |
| audit_reports/muavin_step5_active_bug_context.txt | 1099 | 970:   if(j.ok) location.reload(); else alert(j.msg \ |
| audit_reports/muavin_step5_active_bug_context.txt | 1110 | 981:   if(j.ok) location.reload(); else alert(j.msg \ |
| audit_reports/muavin_step5_active_bug_context.txt | 1122 | 993:   if(j.ok) location.reload(); else alert(j.msg \ |
| audit_reports/muavin_step5_active_bug_context.txt | 1293 | 970:   if(j.ok) location.reload(); else alert(j.msg \ |
| audit_reports/muavin_step5_active_bug_context.txt | 1304 | 981:   if(j.ok) location.reload(); else alert(j.msg \ |
| audit_reports/muavin_step5_active_bug_context.txt | 1309 | 970:   if(j.ok) location.reload(); else alert(j.msg \ |
| audit_reports/muavin_step5_active_bug_context.txt | 1320 | 981:   if(j.ok) location.reload(); else alert(j.msg \ |
| audit_reports/muavin_step5_active_bug_context.txt | 1334 | 981:   if(j.ok) location.reload(); else alert(j.msg \ |
| audit_reports/muavin_step5_active_bug_context.txt | 1357 | 970:   if(j.ok) location.reload(); else alert(j.msg \ |
| audit_reports/muavin_step5_active_bug_context.txt | 1368 | 981:   if(j.ok) location.reload(); else alert(j.msg \ |
| audit_reports/muavin_step5_active_bug_context.txt | 1380 | 993:   if(j.ok) location.reload(); else alert(j.msg \ |
| audit_reports/muavin_step5_active_bug_context.txt | 1560 | 970:   if(j.ok) location.reload(); else alert(j.msg \ |
| audit_reports/muavin_step5_active_bug_context.txt | 1571 | 981:   if(j.ok) location.reload(); else alert(j.msg \ |
| audit_reports/muavin_step5_active_bug_context.txt | 1583 | 993:   if(j.ok) location.reload(); else alert(j.msg \ |
| audit_reports/muavin_step5_active_bug_context.txt | 1754 | 970:   if(j.ok) location.reload(); else alert(j.msg \ |
| audit_reports/muavin_step5_active_bug_context.txt | 1765 | 981:   if(j.ok) location.reload(); else alert(j.msg \ |
| audit_reports/muavin_step5_active_bug_context.txt | 1770 | 970:   if(j.ok) location.reload(); else alert(j.msg \ |
| audit_reports/muavin_step5_active_bug_context.txt | 1781 | 981:   if(j.ok) location.reload(); else alert(j.msg \ |
| audit_reports/muavin_step5_active_bug_context.txt | 1795 | 981:   if(j.ok) location.reload(); else alert(j.msg \ |
| backups/apk_sync_20260520_234501/trip_report.html | 503 | alert("PrintBridge bulunamadı. Tarayıcı yazdırma deneniyor."); |
| backups/apk_sync_20260520_234501/trip_report.html | 506 | alert("PrintBridge hatası: " + err); |
| backups/apk_sync_20260520_234501/trip_report.html | 507 | console.log("PrintBridge error:", err); |
| backups/apk_sync_20260520_234501/trip_report.html | 513 | alert("Yazdırma ekranı açılamadı."); |
| _unused_review/static/vendor/fa/all.min.css | 9 | .fa-sr-only,.fa-sr-only-focusable:not(:focus),.sr-only,.sr-only-focusable:not(:focus){position:absolute;width:1px;height:1px;padding:0;margin:-1px;overflow:hidden;clip:rect(0,0,0,0... |
| android_app/app/src/main/python/templates/add_route.html | 376 | alert('Hat adı ve en az bir durak gerekli.'); |
| android_app/app/src/main/python/templates/consignments.html | 970 | if(j.ok) location.reload(); else alert(j.msg \ |
| android_app/app/src/main/python/templates/consignments.html | 981 | if(j.ok) location.reload(); else alert(j.msg \ |
| android_app/app/src/main/python/templates/consignments.html | 993 | if(j.ok) location.reload(); else alert(j.msg \ |
| android_app/app/src/main/python/templates/hesap.html | 1910 | alert("PrintBridge bulunamadı. Tarayıcı yazdırma deneniyor."); |
| android_app/app/src/main/python/templates/hesap.html | 1913 | alert("PrintBridge hatası: " + err); |
| android_app/app/src/main/python/templates/hesap.html | 1914 | console.log("PrintBridge error:", err); |
| android_app/app/src/main/python/templates/hesap.html | 1920 | alert("Yazdırma ekranı açılamadı."); |
| android_app/app/src/main/python/templates/hesap.html | 2386 | alert("Paylaşılacak hareket yok."); |
| android_app/app/src/main/python/templates/route_edit.html | 699 | alert("Önce hat adını yaz."); |
| android_app/app/src/main/python/templates/route_edit.html | 704 | alert("Durak listesi boş."); |
| android_app/app/src/main/python/templates/route_edit.html | 760 | alert("Lat ve Lng gir."); |
| android_app/app/src/main/python/templates/route_edit.html | 782 | alert(j.msg \ |

## 15) Temizlik İçin Güven Sınıfları

### A - Şimdilik dokunulmayacak
- `app.py`, `templates/*.html`, aktif `static/*.js`, aktif `static/*.css`
- Android içindeki aktif çalışan kopyalar
- Route/render_template içinde görünen dosyalar

### B - İncelenecek
- Android/Web farklı kopyalar
- Aynı isimli ama farklı içerikli dosyalar
- Duplicate ID olan template dosyaları
- Aynı dosya içinde tekrar eden JS fonksiyonları

### C - Silme adayı olabilir ama önce aktif çağrı kontrolü şart
- `.bak`, `backup`, `old`, `eski`, `copy`, `tmp`, `deneme`, `test`, `step`, `audit` geçen dosyalar
- Referans verilmeyen static dosyalar

### D - Asla direkt silinmeyecek
- `android_app/app/src/main/python` altındaki dosyalar
- `templates` içindeki ana ekranlar
- `static/seats`, `static/js`, `static/css` gibi canlı bağlı klasörler
- Veritabanı veya kullanıcı kayıt dosyaları
