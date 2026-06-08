# Muavin Asistanı Full Audit Raporu

- Tarih: `20260608-163602`
- Root: `/data/data/com.termux/files/home/Host-Hostes-Paneli`
- Toplam dosya: **3004**
- Text dosya: **464**
- Python: **78**
- HTML template/dosya: **144**
- CSS: **85**
- JS: **68**

## 1) Git Durumu
Branch: `main`
```
M android_app/app/src/main/java/com/muavinasistani/app/MainActivity.java
 M android_app/app/src/main/python/android_server.py
 M db.sqlite3
?? audit_reports/
?? tools/muavin_audit_step1.py
?? tools/muavin_audit_step2.py
?? tools/muavin_audit_step3_flask_routes.py
?? tools/muavin_audit_step4_suspicious_context.py
?? tools/muavin_audit_step5_active_bug_context.py
?? tools/muavin_audit_step6_runtime_smoke.py
?? tools/muavin_audit_step6b_runtime_smoke_fixed.py
?? tools/muavin_audit_step7_global_appjs.py
?? tools/muavin_audit_step8_appjs_impact.py
?? tools/muavin_audit_step9_sync_plan.py
?? tools/muavin_full_audit_v1.py
?? tools/seat_count_audit.py
```
Son commitler:
```
6842e10 Refactor continue trip flow and sync Android source
6892e64 güncelleme
f073522 güncelleme
0d43ada güncelleme
4ace4ed seats css yamalar
```

## 2) Ana Klasörlere Göre Dosya Sayısı
| Klasör | Dosya sayısı |
| --- | --- |
| android_app | 920 |
| apk_payload | 832 |
| templates | 535 |
| static | 382 |
| uploads | 49 |
| tools | 32 |
| modules | 16 |
| tmp_muavin_icon | 14 |
| audit_reports | 9 |
| checkpoints | 7 |
| backups | 6 |
| _unused_review | 5 |
| raporlar | 5 |
| rollback_backup_now | 3 |
| .github | 1 |
| .gitignore | 1 |
| ACTIVE_FILES.txt | 1 |
| ACTIVE_PATHS.txt | 1 |
| ACTIVE_TREE.txt | 1 |
| AUTO_LIVE_STOP_AUDIT.txt | 1 |
| AYARLAR_DETAY_RAPORU.txt | 1 |
| AYARLAR_NET_RAPORU.txt | 1 |
| BACKUP_PATHS.txt | 1 |
| BACKUP_TREE.txt | 1 |
| CHECK_PATHS.txt | 1 |
| CHECK_TREE.txt | 1 |
| DEPLOY_COPY_PATHS.txt | 1 |
| DEPLOY_COPY_TREE.txt | 1 |
| DURAK_AKISI_KAYNAK_RAPORU_20260518_205127.txt | 1 |
| FAB_DETAYLI_ARASTIRMA_20260516_164549.txt | 1 |
| HOST_HOSTES_SOY_AGACI.md | 1 |
| HOST_HOSTES_SOY_AGACI_SATIRLI.md | 1 |
| KARANTINA_ONERILEN.txt | 1 |
| KOLTUK_PANEL_YAMA_RAPORU_20260516_153819.txt | 1 |
| LIVE_FLOW_TARGET_AUDIT.txt | 1 |
| LIVE_FLOW_V2_AUDIT.txt | 1 |
| PATCH_AUDIT_REPORT.md | 1 |
| PATCH_LIVE_AUDIT_REPORT.md | 1 |
| PROJE_AGAC_RAPORU.md | 1 |
| SEATS_AKTIF_HARITA.txt | 1 |
| SEATS_CSS_OVERRIDE_REPORT.md | 1 |
| SEATS_DETAYLI_SISTEM_RAPORU_20260516_155924.txt | 1 |
| SEATS_EXTERNAL_OVERRIDE_REPORT.md | 1 |
| SEATS_HTML_A_DAN_Z_RAPORU_20260518_162041.txt | 1 |
| SEATS_HTML_KALAN_YAMA_RAPORU_20260518_174156.txt | 1 |
| SEATS_HTML_TEMIZLIK_RAPORU_20260518_153638.txt | 1 |
| SEATS_PATCH_ENVANTER_20260518_164328.txt | 1 |
| SEFER_RAPORU_KAYNAK_RAPORU.txt | 1 |
| SESLI_KOMUT_RAPORU_20260518_123328.txt | 1 |
| SON_YARIM_SAAT_YAMA_RAPORU_20260516_150801.txt | 1 |
| SURUS_MODU_GORUNUM_RAPORU_20260516_171742.txt | 1 |
| SUSPECT_BACKUP_FILES.txt | 1 |
| TOOL_PATHS.txt | 1 |
| TOOL_TREE.txt | 1 |
| UNKNOWN_FILES.txt | 1 |
| aktif_dosya_listesi.txt | 1 |
| antalya_istanbul_eksik_koordinatlar.txt | 1 |
| antalya_istanbul_koordinat_adaylari.txt | 1 |
| antalya_istanbul_koordinat_adaylari_2.txt | 1 |
| antalya_istanbul_son_4_koordinat_adaylari.txt | 1 |
| apk_payload_files.txt | 1 |
| app.py | 1 |
| app.py.bak_ai_duplicate_clean | 1 |
| app.py.bak_ai_duplicate_clean_2 | 1 |
| app.py.bak_ai_learned_route_fix | 1 |
| app.py.bak_ai_learned_route_fix_correct | 1 |
| app.py.bak_ai_remove_bag_cleanup | 1 |
| app.py.bak_ai_runtime_answers_only | 1 |
| app.py.bak_api_seats_offload_bag_clear | 1 |
| app.py.bak_api_stops_contract_patch1 | 1 |
| app.py.bak_api_stops_coords_final_fix | 1 |
| app.py.bak_api_stops_route_coords_fix | 1 |
| app.py.bak_bag_clear_on_seat_delete | 1 |
| app.py.bak_bag_clear_on_seat_delete_v2 | 1 |
| app.py.bak_bag_photo_gallery_20260512_1322 | 1 |
| app.py.bak_before_rollback_continue_real_data | 1 |
| app.py.bak_cargo_detail_deliver_20260512_1938 | 1 |
| app.py.bak_change_destination_20260512_1238 | 1 |
| app.py.bak_consignment_trip_filter_fix | 1 |
| app.py.bak_continue_live_eta_engine_20260523_105409 | 1 |
| app.py.bak_continue_live_flow_api_20260523_123118 | 1 |
| app.py.bak_continue_stop_bridge | 1 |
| app.py.bak_continue_stop_logic | 1 |
| app.py.bak_continue_trip_bag_exact_patch | 1 |
| app.py.bak_continue_trip_bag_fix_fresh | 1 |
| app.py.bak_continue_trip_bag_tuple_fix | 1 |
| app.py.bak_continue_trip_live_data | 1 |
| app.py.bak_continue_trip_real_bags | 1 |
| app.py.bak_continue_trip_real_data_final | 1 |
| app.py.bak_delivered_consignment_filter_20260512_1943 | 1 |
| app.py.bak_end_trip_cleanup_real_20260512_2300 | 1 |
| app.py.bak_existing_bag_gallery_20260512_1325 | 1 |
| app.py.bak_fix_api_stops_object_leak | 1 |
| app.py.bak_fix_api_stops_string_list | 1 |
| app.py.bak_fix_api_stops_string_list_v2 | 1 |
| app.py.bak_fix_route_stop_coords_recursion | 1 |
| app.py.bak_live_bag_detail_20260512_1313 | 1 |
| app.py.bak_live_consignment_photo_url_20260512_1954 | 1 |
| app.py.bak_live_gender_color_20260512_2030 | 1 |
| app.py.bak_live_gender_counts_20260523_111341 | 1 |
| app.py.bak_live_map_20260513_0058 | 1 |
| app.py.bak_live_runtime_sync | 1 |
| app.py.bak_live_seat_offload_20260512_1256 | 1 |
| app.py.bak_live_stop_bulk_offload_20260512_1309 | 1 |
| app.py.bak_live_stop_sheet_20260512_1231 | 1 |
| app.py.bak_no_cache_dev_20260520_101438 | 1 |
| app.py.bak_onboarding_route | 1 |
| app.py.bak_onboarding_server_fix | 1 |
| app.py.bak_raw_gpskm_format_fix | 1 |
| app.py.bak_real_bag_emanet_fix_20260523_120629 | 1 |
| app.py.bak_rehber_menu_patch | 1 |
| app.py.bak_remove_dead_api_seat_code | 1 |
| app.py.bak_remove_dead_api_seat_code_v2 | 1 |
| app.py.bak_report_change_payload_20260520_233720 | 1 |
| app.py.bak_report_destination_change_20260520_232729 | 1 |
| app.py.bak_reports_deps_events_sums_fix | 1 |
| app.py.bak_revert_continue_live_flow_20260523_123657 | 1 |
| app.py.bak_route_coords_refactor | 1 |
| app.py.bak_route_order_fix_final | 1 |
| app.py.bak_route_profile_system_20260513_1446 | 1 |
| app.py.bak_route_segments_json_fallback_20260513_0308 | 1 |
| app.py.bak_route_segments_map_20260513_0254 | 1 |
| app.py.bak_seat_destination_change_20260520_231815 | 1 |
| app.py.bak_small_fixes_runtime_bag | 1 |
| app.py.bak_split_ai_module | 1 |
| app.py.bak_split_backup_module | 1 |
| app.py.bak_split_bag_emanet_20260523_120318 | 1 |
| app.py.bak_split_cash_module | 1 |
| app.py.bak_split_consignments_module | 1 |
| app.py.bak_split_coords_module | 1 |
| app.py.bak_split_live_ops_module | 1 |
| app.py.bak_split_reports_light_module | 1 |
| app.py.bak_split_routes_module | 1 |
| app.py.bak_split_seats_module | 1 |
| app.py.bak_split_settings_module | 1 |
| app.py.bak_split_subscription_module | 1 |
| app.py.bak_split_trip_report_builder | 1 |
| app.py.bak_stop_complete_20260513_0151 | 1 |
| app.py.bak_stop_fuzzy_match | 1 |
| app.py.bak_tanitim_redirect_fix | 1 |
| app.py.bak_user_reset | 1 |
| app.py.before_coords_order_manual_fix | 1 |
| db.sqlite3 | 1 |
| db.sqlite3.bak_accept_alibeykoy_gebze_yss_20260518_000238 | 1 |
| db.sqlite3.bak_add_icmeler_denizli_istanbul_20260520_120742 | 1 |
| db.sqlite3.bak_add_missing_ant_ist_coords_20260517_143011 | 1 |
| db.sqlite3.bak_akhisar_balikesir_d565_20260517_103807 | 1 |
| db.sqlite3.bak_ant_ist_coord_copy_20260517_092120 | 1 |
| db.sqlite3.bak_ant_ist_coord_copy_fix_20260517_092218 | 1 |
| db.sqlite3.bak_ant_ist_route_segments_20260517_094613 | 1 |
| db.sqlite3.bak_ant_ist_safe_coords_20260517_093127 | 1 |
| db.sqlite3.bak_ant_ist_schedule_20260516_180115 | 1 |
| db.sqlite3.bak_before_rollback_accept_alibeykoy_gebze_yss_20260518_001320 | 1 |
| db.sqlite3.bak_before_rollback_missing_coords_20260517_143054 | 1 |
| db.sqlite3.bak_before_rollback_salihli_akhisar_via_20260517_100817 | 1 |
| db.sqlite3.bak_before_rollback_salihli_correct_turn_20260517_102155 | 1 |
| db.sqlite3.bak_before_rollback_salihli_pin_d555_20260517_101430 | 1 |
| db.sqlite3.bak_before_rollback_tuzla_segments_20260517_111533 | 1 |
| db.sqlite3.bak_build_denizli_istanbul_segments_20260520_122020 | 1 |
| db.sqlite3.bak_copy_elmali_to_ant_ist_20260517_144513 | 1 |
| db.sqlite3.bak_copy_elmali_to_ant_ist_20260517_144542 | 1 |
| db.sqlite3.bak_denizli_istanbul_alias_coords_20260520_115135 | 1 |
| db.sqlite3.bak_denizli_istanbul_coords_mix_20260520_114947 | 1 |
| db.sqlite3.bak_denizli_korkuteli_segments_20260517_144319 | 1 |
| db.sqlite3.bak_fix_alibeykoy_gebze_short_yss_20260517_235959 | 1 |
| db.sqlite3.bak_force_ist_ant_yss_route_20260517_234658 | 1 |
| db.sqlite3.bak_ist_ant_alibeykoy_gebze_yss_extra2_20260517_235604 | 1 |
| db.sqlite3.bak_ist_ant_alibeykoy_gebze_yss_extra_20260517_235252 | 1 |
| db.sqlite3.bak_ist_ant_copy_missing_coords_20260517_144701 | 1 |
| db.sqlite3.bak_ist_ant_manisa_route_20260517_233207 | 1 |
| db.sqlite3.bak_ist_ant_refresh_segments_20260517_144738 | 1 |
| db.sqlite3.bak_ist_ant_schedule_20260518_122400 | 1 |
| db.sqlite3.bak_istanbul_antalya_yss_20260517_141115 | 1 |
| db.sqlite3.bak_istanbul_denizli_schedule_20260520_133113 | 1 |
| db.sqlite3.bak_korkuteli_elmali_segments_20260517_143312 | 1 |
| db.sqlite3.bak_ortahan_km_fix_20260516_181153 | 1 |
| db.sqlite3.bak_rebuild_denizli_istanbul_segments_20260520_122635 | 1 |
| db.sqlite3.bak_refresh_new_coords_segments_20260517_143857 | 1 |
| db.sqlite3.bak_reorder_denizli_istanbul_from_antalya_20260520_115837 | 1 |
| db.sqlite3.bak_restore_antalya_istanbul_stops_20260520_102308 | 1 |
| db.sqlite3.bak_restore_denizli_istanbul_from_reverse_20260521_000121 | 1 |
| db.sqlite3.bak_reverse_ist_ant_20260517_140145 | 1 |
| db.sqlite3.bak_reverse_to_istanbul_denizli_20260520_123746 | 1 |
| db.sqlite3.bak_salihli_akhisar_via_d555_20260517_100121 | 1 |
| db.sqlite3.bak_salihli_akhisar_via_points_20260517_100608 | 1 |
| db.sqlite3.bak_salihli_correct_turn_20260517_101854 | 1 |
| db.sqlite3.bak_salihli_pin_d555_fix_20260517_101253 | 1 |
| db.sqlite3.bak_tuzla_refresh_20260517_112331 | 1 |
| db.sqlite3.bak_tuzla_segments_redraw_20260517_111153 | 1 |
| db.sqlite3.bak_tuzla_segments_redraw_fix_20260517_112456 | 1 |
| db.sqlite3.local_backup_20260512_2009 | 1 |
| nano | 1 |
| proje_dosya_listesi.txt | 1 |
| proje_flask_baglanti_raporu.txt | 1 |
| proje_template_haritasi.txt | 1 |
| schema.sql | 1 |
| seats_baglanti_haritasi.txt | 1 |
| speedlimit.py | 1 |
| storage | 1 |
| tmp | 1 |
| tracked_junk.txt | 1 |
| tracked_junk_safe.txt | 1 |
| update.sh | 1 |

## 3) Uzantıya Göre Dosya Sayısı
| Uzantı | Dosya sayısı |
| --- | --- |
| .html | 144 |
| .css | 85 |
| .png | 80 |
| .py | 78 |
| .js | 68 |
| .jpg | 64 |
| .txt | 62 |
| .bak_before_exact_113619_restore_20260516_153946 | 15 |
| .bak_before_restore_12_checkpoint_20260516_153518 | 15 |
| .bak_before_restore_natural_total_checkpoint_20260516_152438 | 15 |
| .bak_before_rollback_exact_113619_20260516_154139 | 15 |
| .bak_before_clean_speed_split_leftover_20260516_151647 | 12 |
| .bak_before_corrective_restore_20260516_151536 | 12 |
| .bak_before_fix_bad_voice_rollback_20260516_150609 | 12 |
| .bak_before_restore_from_20260516_145319_20260516_151331 | 12 |
| .bak_before_restore_previous_20260516_150549 | 12 |
| .bak_before_voice_mass_rollback_20260516_150355 | 12 |
| .bak_live_runtime_sync | 10 |
| .bak_bottom_final_20260513_164512 | 9 |
| .bak_clean_speed_voice_split_20260516_114304 | 9 |
| .bak_clean_start_20260513_185013 | 9 |
| .bak_final_voice_split_20260516_133629 | 9 |
| .bak_fix_menu_images | 9 |
| .bak_map_ui_final_20260513_165054 | 9 |
| .bak_marquee_cleanup | 9 |
| .bak_marquee_total_cleanup | 9 |
| .bak_next_ops_drag_20260513_174215 | 9 |
| .bak_next_ops_final_20260513_172822 | 9 |
| .bak_remove_compass_20260513_165759 | 9 |
| .bak_speed_voice_click_final_20260516_145945 | 9 |
| .bak_split_assistant_speed_voice_20260516_113619 | 9 |
| .bak_stop_flow_cleanup_20260512_2304 | 9 |
| .bak_voice_mini_counter_final | 9 |
| .bak_voice_mini_drive_fix | 9 |
| .bak_voice_seat_mini | 9 |
| .bak_voice_split_final2_20260516_145734 | 9 |
| .md | 9 |
| .bak_print_bridge | 7 |
| .bak_print_debug | 7 |
| .bak_raw_gpskm_format_fix | 7 |
| .bak_report_destination_change_20260520_232729 | 7 |
| .bak_sync_continue_20260523_142710 | 7 |
| .before_refactor_20260520_110402 | 7 |
| .bak_android_tts_fix | 6 |
| .bak_before_rollback_live_stop_core_20260520_104302 | 6 |
| .bak_before_rollback_live_stop_core_20260520_104314 | 6 |
| .bak_before_rollback_selected_stop_memory_20260518_153528 | 6 |
| .bak_before_rollback_voice_direct_board_20260518_125402 | 6 |
| .bak_before_rollback_voice_direct_board_general_20260518_125649 | 6 |
| .bak_before_seats_final | 6 |
| .bak_bottom_voice_clickfix_20260516_111618 | 6 |
| .bak_clean_dock_visible_20260513_185554 | 6 |
| .bak_clean_fullscreen_20260513_185236 | 6 |
| .bak_clean_hide_km_20260513_190426 | 6 |
| .bak_clean_location_visible_20260513_190610 | 6 |
| .bak_clean_marquee_final | 6 |
| .bak_clean_speed_visible_20260513_190933 | 6 |
| .bak_drive_voice_abort_fix | 6 |
| .bak_drive_voice_clean_single | 6 |
| .bak_drive_voice_clone_row | 6 |
| .bak_drive_voice_direct_guard | 6 |
| .bak_drive_voice_equal_clean | 6 |
| .bak_drive_voice_id | 6 |
| .bak_end_trip_local_cleanup_20260512_2300 | 6 |
| .bak_fix_tripkey_exact_20260520_204851 | 6 |
| .bak_force_always | 6 |
| .bak_full_scroll_fix | 6 |
| .bak_general_seat_label_fix_20260516_062235 | 6 |
| .bak_light_design | 6 |
| .bak_live_stop_core_fix_20260520_104112 | 6 |
| .bak_manual_ticket_badge_20260518_135457 | 6 |
| .bak_marquee_clean_final | 6 |
| .bak_marquee_final | 6 |
| .bak_marquee_readable | 6 |
| .bak_marquee_single_clean | 6 |
| .bak_modal_readability_20260518_181100 | 6 |
| .bak_next_ops_bubble_20260513_174004 | 6 |
| .bak_next_ops_polish_20260513_173333 | 6 |
| .bak_offload_modal_clean | 6 |
| .bak_only54_20260516_105535 | 6 |
| .bak_remove_all_visible_slash_n_20260513_153624 | 6 |
| .bak_rollback_general_label_fix_20260516_062504 | 6 |
| .bak_rollback_only54_20260516_105639 | 6 |
| .bak_scope_simple_only_20260520_105358 | 6 |
| .bak_simple_scope_20260520_110612 | 6 |
| .bak_small_buttons_20260513_174403 | 6 |
| .bak_ticker_fix | 6 |
| .bak_tripkey_by_id_20260520_204710 | 6 |
| .bak_tts_toggle_speed_sync_20260516_150032 | 6 |
| .bak_tv_marquee_real | 6 |
| .bak_unified_voice | 6 |
| .bak_voice_button_fix | 6 |
| .bak_voice_button_state_fix | 6 |
| .bak_voice_central_bridge | 6 |
| .bak_voice_listen_guard_20260518_165014 | 6 |
| .bak_voice_map_fullscreen_20260518_124532 | 6 |
| .bak_voice_stop_ops_patch | 6 |
| .bak_wa_scheme_fix | 6 |
| .htm | 6 |
| .json | 6 |
| .sqlite3 | 5 |
| .bak_accept_alibeykoy_gebze_yss_20260518_000238 | 4 |
| .bak_akhisar_balikesir_d565_20260517_103807 | 4 |
| .bak_bag_emanet_clean_20260523_130105 | 4 |
| .bak_bag_photo_gallery_20260512_1322 | 4 |
| .bak_before_rollback_accept_alibeykoy_gebze_yss_20260518_001320 | 4 |
| .bak_before_rollback_salihli_akhisar_via_20260517_100817 | 4 |
| .bak_before_rollback_salihli_correct_turn_20260517_102155 | 4 |
| .bak_before_rollback_salihli_pin_d555_20260517_101430 | 4 |
| .bak_before_rollback_tuzla_segments_20260517_111533 | 4 |
| .bak_cargo_detail_deliver_20260512_1938 | 4 |
| .bak_change_destination_20260512_1238 | 4 |
| .bak_continue_stop_bridge | 4 |
| .bak_denizli_korkuteli_segments_20260517_144319 | 4 |
| .bak_existing_bag_gallery_20260512_1325 | 4 |
| .bak_fix_alibeykoy_gebze_short_yss_20260517_235959 | 4 |
| .bak_force_ist_ant_yss_route_20260517_234658 | 4 |
| .bak_ist_ant_alibeykoy_gebze_yss_extra2_20260517_235604 | 4 |
| .bak_ist_ant_alibeykoy_gebze_yss_extra_20260517_235252 | 4 |
| .bak_ist_ant_manisa_route_20260517_233207 | 4 |
| .bak_ist_ant_refresh_segments_20260517_144738 | 4 |
| .bak_istanbul_antalya_yss_20260517_141115 | 4 |
| .bak_korkuteli_elmali_segments_20260517_143312 | 4 |
| .bak_live_bag_detail_20260512_1313 | 4 |
| .bak_live_diag_20260523_132945 | 4 |
| .bak_live_gender_color_20260512_2030 | 4 |
| .bak_live_seat_offload_20260512_1256 | 4 |
| .bak_live_stop_bulk_offload_20260512_1309 | 4 |
| .bak_live_stop_sheet_20260512_1231 | 4 |
| .bak_map_overlay_20260523_140732 | 4 |
| .bak_refresh_new_coords_segments_20260517_143857 | 4 |
| .bak_rehber_menu_patch | 4 |
| .bak_report_change_payload_20260520_233720 | 4 |
| .bak_restore_denizli_istanbul_from_reverse_20260521_000121 | 4 |
| .bak_reverse_ist_ant_20260517_140145 | 4 |
| .bak_reverse_to_istanbul_denizli_20260520_123746 | 4 |
| .bak_route_profile_system_20260513_1446 | 4 |
| .bak_salihli_akhisar_via_d555_20260517_100121 | 4 |
| .bak_salihli_akhisar_via_points_20260517_100608 | 4 |
| .bak_salihli_correct_turn_20260517_101854 | 4 |
| .bak_salihli_pin_d555_fix_20260517_101253 | 4 |
| .bak_seat_destination_change_20260520_231815 | 4 |
| .bak_stop_complete_20260513_0151 | 4 |
| .bak_sync_20260520_113916 | 4 |
| .bak_tuzla_refresh_20260517_112331 | 4 |
| .bak_tuzla_segments_redraw_fix_20260517_112456 | 4 |
| .xml | 4 |
| .ba | 3 |
| .bak_account_hero_top_fix | 3 |
| .bak_add_continue_trip_coords_helper_final | 3 |
| .bak_add_missing_coords_helper_fix | 3 |
| .bak_add_speed_box | 3 |
| .bak_android_tts | 3 |
| .bak_ant_ist_20260517_094613 | 3 |
| .bak_append_missing_coords_helper | 3 |
| .bak_apple_landing_final | 3 |
| .bak_approach_alert_20260513_0223 | 3 |
| .bak_approach_banner_20260513_0228 | 3 |
| .bak_approach_test_20260513_0225 | 3 |
| .bak_approach_test_20260513_0229 | 3 |
| .bak_bag_cargo_sections_20260512_1934 | 3 |
| .bak_bag_centered_fix_20260512_1406 | 3 |
| .bak_bag_photo_viewer_20260512_1329 | 3 |
| .bak_before_cleanup_step1_20260518_153910 | 3 |
| .bak_before_design | 3 |
| .bak_before_fab_drive_override_fix_20260516_164916 | 3 |
| .bak_before_fab_drive_style_all_20260516_172024 | 3 |
| .bak_before_fab_mini_restore_20260516_155226 | 3 |
| .bak_before_fab_vertical_override_20260516_160256 | 3 |
| .bak_before_full_cleanup_audit_20260518_153638 | 3 |
| .bak_before_label_rollback | 3 |
| .bak_before_remove_fab_compact_fit_20260516_154836 | 3 |
| .bak_before_remove_modal_retouch_20260518_204549 | 3 |
| .bak_before_remove_tilt_20260513_152523 | 3 |
| .bak_before_restore_fab_2_3_20260516_164351 | 3 |
| .bak_before_restore_good_fab_20260516_155627 | 3 |
| .bak_before_restore_good_fab_20260516_161034 | 3 |
| .bak_before_restore_good_fab_20260516_162430 | 3 |
| .bak_before_restore_only_fab_compact_20260516_160058 | 3 |
| .bak_before_restore_visual_blocks_20260516_153134 | 3 |
| .bak_before_rollback_20260520_103515 | 3 |
| .bak_before_rollback_appledark | 3 |
| .bak_before_rollback_fab_drive_style_all_20260516_172140 | 3 |
| .bak_before_rollback_fab_extract_20260518_173110 | 3 |
| .bak_before_rollback_fab_mini_20260516_155332 | 3 |
| .bak_before_rollback_fab_vertical_override_20260516_160418 | 3 |
| .bak_before_rollback_good_fab_20260516_155731 | 3 |
| .bak_before_rollback_hide_static_20260520_140340 | 3 |
| .bak_before_rollback_last_live_ui | 3 |
| .bak_before_rollback_live_sync_20260520_103515 | 3 |
| .bak_before_rollback_only_fab_compact_20260516_160156 | 3 |
| .bak_before_rollback_rear_bottom_gap_20260516_165210 | 3 |
| .bak_before_rollback_stop_memory_clear_once_20260518_141131 | 3 |
| .bak_before_voice_tts_split | 3 |
| .bak_blue_location_20260513_150229 | 3 |
| .bak_blue_location_fixed_20260513_150348 | 3 |
| .bak_blue_marker_polish_20260513_150746 | 3 |
| .bak_board_fix | 3 |
| .bak_boarding_stop_fix_final | 3 |
| .bak_boarding_stop_logic | 3 |
| .bak_boarding_stop_priority_20260518_142016 | 3 |
| .bak_bottom_actions_minimal_20260513_162347 | 3 |
| .bak_bottom_actions_minimal_fixed_20260513_162448 | 3 |
| .bak_bottom_deck_space_trim_20260516_064820 | 3 |
| .bak_bottom_dock_click_fix_20260513_163228 | 3 |
| .bak_bottom_dock_fix_20260513_162709 | 3 |
| .bak_bottom_dock_smart_more_20260513_162927 | 3 |
| .bak_bottom_legend_fixed_final | 3 |
| .bak_bottom_row_align_20260516_075348 | 3 |
| .bak_bottom_row_equal_20260516_063703 | 3 |
| .bak_brand_chip_only | 3 |
| .bak_build_denizli_istanbul_20260520_122020 | 3 |
| .bak_bulk_modal_hide_bottom_nav_20260515_152410 | 3 |
| .bak_bulk_nav_hide_v2_20260515_173615 | 3 |
| .bak_bus_marker_size_fix_20260513_0126 | 3 |
| .bak_caption_down_final | 3 |
| .bak_cargo_photo_badge_fix_20260512_1958 | 3 |
| .bak_cargo_photo_viewer_20260512_1956 | 3 |
| .bak_cinema_text_update | 3 |
| .bak_cinematic_bus_marker_20260513_0123 | 3 |
| .bak_clean_manual_ticket_system_20260518_143846 | 3 |
| .bak_clean_rewrite | 3 |
| .bak_cleanup_bad_speed_gps | 3 |
| .bak_clear_ticket_on_offload_20260518_145103 | 3 |
| .bak_compact_neon_20260511_134504 | 3 |
| .bak_compact_popup_20260513_0144 | 3 |
| .bak_compact_visual_fix | 3 |
| .bak_confirm_offload_disable | 3 |
| .bak_continue_stop_local_fix_20260512_2332 | 3 |
| .bak_continue_stop_store | 3 |
| .bak_continue_trip_all_cards_from_cached_coords | 3 |
| .bak_continue_trip_bridge | 3 |
| .bak_continue_trip_sync_from_seats | 3 |
| .bak_counter_remove | 3 |
| .bak_custom_select_final | 3 |
| .bak_custom_select_picker | 3 |
| .bak_dark_apple_home_final | 3 |
| .bak_dark_font_balance | 3 |
| .bak_dark_guide_detail | 3 |
| .bak_dark_premium_override | 3 |
| .bak_debug_stop_memory_20260518_142714 | 3 |
| .bak_deck_wide_angle_fit_20260516_070229 | 3 |
| .bak_design_v1 | 3 |
| .bak_destination_label_20260520_233448 | 3 |
| .bak_direct_final_banner | 3 |
| .bak_disable_deck_horizontal_scroll_20260516_065903 | 3 |
| .bak_draggable_route_bubble_20260513_160034 | 3 |
| .bak_drive_actions_above_route | 3 |
| .bak_drive_actions_route_top | 3 |
| .bak_drive_actions_top | 3 |
| .bak_drive_controls_repair_version_20260516_133452 | 3 |
| .bak_drive_dock_fix | 3 |
| .bak_drive_eta_split | 3 |
| .bak_drive_fab_final | 3 |
| .bak_drive_force_repair_version_20260516_145319 | 3 |
| .bak_drive_force_toggle | 3 |
| .bak_drive_premium_screen_v1 | 3 |
| .bak_drive_toggle_fix | 3 |
| .bak_drive_top_clean_final | 3 |
| .bak_drive_voice_only_final | 3 |
| .bak_drive_voice_only_rollback | 3 |
| .bak_drive_voice_relay_fix | 3 |
| .bak_drive_voice_separat | 3 |
| .bak_drive_voice_separate | 3 |
| .bak_drive_voice_width_only | 3 |
| .bak_events_sums_fix | 3 |
| .bak_external_assets_20260513_163848 | 3 |
| .bak_extract_bottom_voice_css_20260518_165551 | 3 |
| .bak_extract_drive_mode_pack_20260518_175558 | 3 |
| .bak_extract_fab_patches_20260518_172257 | 3 |
| .bak_extract_manual_ticket_system_20260518_165902 | 3 |
| .bak_extract_modal_bottom_nav_20260518_165739 | 3 |
| .bak_extract_seat_layout_fab_pack_20260518_175236 | 3 |
| .bak_extract_seat_simple_pack_20260518_175924 | 3 |
| .bak_extract_seat_spacing_patches_20260518_174701 | 3 |
| .bak_extract_stop_flow_focus_20260518_174427 | 3 |
| .bak_extract_stop_selected_toast_20260518_165333 | 3 |
| .bak_extract_stop_toast_20260518_164437 | 3 |
| .bak_extract_top_sound_toggle_20260518_171903 | 3 |
| .bak_fab_compact_fit_20260516_064606 | 3 |
| .bak_fab_distinct_panel_20260516_064444 | 3 |
| .bak_fab_left_gap_move_20260516_064207 | 3 |
| .bak_fab_left_gap_move_20260516_163849 | 3 |
| .bak_fab_sheet_solid_20260518_205755 | 3 |
| .bak_final_apk_20260513_192149 | 3 |
| .bak_final_polish_phase | 3 |
| .bak_final_stabilizer | 3 |
| .bak_final_stop_normalize_cleanup | 3 |
| .bak_finish_modal_split | 3 |
| .bak_fix_apk_voice_counts | 3 |
| .bak_fix_cachedstops_object_usage_final | 3 |
| .bak_fix_change_event_render_20260520_233609 | 3 |
| .bak_fix_continue_hero | 3 |
| .bak_fix_duplicate_hero_cards | 3 |
| .bak_fix_duplicate_start_card | 3 |
| .bak_fix_live_km_jump | 3 |
| .bak_fix_object_object_route_strip | 3 |
| .bak_fix_object_object_route_strip_v2 | 3 |
| .bak_fix_rehber_image_split | 3 |
| .bak_fix_stop_flow_after_api_stops_object | 3 |
| .bak_fix_voice_seat_counts | 3 |
| .bak_fixed_bottom_legend | 3 |
| .bak_force_change_render_20260520_233819 | 3 |
| .bak_force_repair_20260516_145319 | 3 |
| .bak_force_same_hero | 3 |
| .bak_force_single_gps_format | 3 |
| .bak_force_tts_toggle_speed_sync_20260516_150133 | 3 |
| .bak_fullscreen_map_20260513_0141 | 3 |
| .bak_future_stop_gps_distance | 3 |
| .bak_future_stops_distance_bind | 3 |
| .bak_ghost_icons_soften | 3 |
| .bak_google_location_v2_20260513_151340 | 3 |
| .bak_gpskm_raw_write_fix | 3 |
| .bak_guide_accordion | 3 |
| .bak_guide_detail_polish | 3 |
| .bak_guide_filter_bar | 3 |
| .bak_guide_mini_nav | 3 |
| .bak_hard_line_repair_20260516_145608 | 3 |
| .bak_hard_repair_voice_block_20260516_145427 | 3 |
| .bak_hatlar_theme | 3 |
| .bak_head_n_fix_20260512_2043 | 3 |
| .bak_headline_text_fix | 3 |
| .bak_hero_home_button_fix | 3 |
| .bak_hero_home_micro_fix | 3 |
| .bak_hero_image_fit | 3 |
| .bak_hero_title_class | 3 |
| .bak_hero_v2_fix | 3 |
| .bak_hesap_card_image | 3 |
| .bak_hesap_final_touch | 3 |
| .bak_hide_bottom_menu_on_seat_modal | 3 |
| .bak_hide_initial_runtime_jump | 3 |
| .bak_hide_legend_row | 3 |
| .bak_hide_static_routes_20260520_140228 | 3 |
| .bak_hizli_islem_premium | 3 |
| .bak_insert_coords_helper_after_currentcoords | 3 |
| .bak_intent_legend_fix | 3 |
| .bak_ios_select_picker | 3 |
| .bak_ios_select_rollback | 3 |
| .bak_ios_wheel_picker | 3 |
| .bak_km_labels_20260513_154243 | 3 |
| .bak_koltuk_yonetimi_card | 3 |
| .bak_label_title_regex_20260516_062350 | 3 |
| .bak_last_coords_cache | 3 |
| .bak_last_row_inner_gap_fix_20260516_065535 | 3 |
| .bak_last_row_tighter_20260516_065700 | 3 |
| .bak_legend_conflict_clean | 3 |
| .bak_legend_lift_fix | 3 |
| .bak_light_select_picker | 3 |
| .bak_literal_n_cleanup_20260512_2001 | 3 |
| .bak_literal_n_cleanup_20260513_0242 | 3 |
| .bak_literal_n_fix_20260513_1451 | 3 |
| .bak_literal_newline_fix_20260512_1409 | 3 |
| .bak_live_candidate_selected_fix_20260512_2346 | 3 |
| .bak_live_clock_fix | 3 |
| .bak_live_clock_seconds | 3 |
| .bak_live_danger_restore | 3 |
| .bak_live_display_no_fallback_20260512_2341 | 3 |
| .bak_live_dot_position_fix | 3 |
| .bak_live_event_memory_20260512_2330 | 3 |
| .bak_live_final_visual_match | 3 |
| .bak_live_gps_speed | 3 |
| .bak_live_hero_brightness | 3 |
| .bak_live_hero_bus_html_insert | 3 |
| .bak_live_hero_bus_img | 3 |
| .bak_live_hero_bus_insert | 3 |
| .bak_live_hero_title_size | 3 |
| .bak_live_hero_title_smaller | 3 |
| .bak_live_label_fix | 3 |
| .bak_live_map_link_20260513_0100 | 3 |
| .bak_live_only_operation_stops_20260513_0027 | 3 |
| .bak_live_operation_panel | 3 |
| .bak_live_pill_dot | 3 |
| .bak_live_pill_red_text | 3 |
| .bak_live_runtime_sync_20260520_103326 | 3 |
| .bak_live_stale_fix_20260512_2354 | 3 |
| .bak_live_stop_card_image | 3 |
| .bak_live_stop_fix_final_20260512_2349 | 3 |
| .bak_live_stop_flow_events_20260512_2324 | 3 |
| .bak_live_stop_pro_20260512_2248 | 3 |
| .bak_live_stop_summary_20260512_2224 | 3 |
| .bak_live_ui_final | 3 |
| .bak_livestop_bridge_fix | 3 |
| .bak_locate_btn_fix_20260513_151533 | 3 |
| .bak_manual_rehber_update | 3 |
| .bak_manual_ticket_persist_fix_20260518_135715 | 3 |
| .bak_map_controls_stack_20260513_0244 | 3 |
| .bak_map_speed_badge_20260513_0131 | 3 |
| .bak_marquee | 3 |
| .bak_marquee_conflict_cleanup | 3 |
| .bak_metric_hint_polish_20260512_1353 | 3 |
| .bak_minimal_sadelestirme_20260513_162118 | 3 |
| .bak_mobile_final | 3 |
| .bak_mobile_perf_fix_20260518_180706 | 3 |
| .bak_mockup_to_code | 3 |
| .bak_modal_bottom_nav_hide_v3_20260515_173940 | 3 |
| .bak_modal_premium_v2 | 3 |
| .bak_natural_total_voice_20260516_112923 | 3 |
| .bak_nav3d_feel_20260513_152147 | 3 |
| .bak_neon_hesap | 3 |
| .bak_next_ops_compact_20260513_0145 | 3 |
| .bak_next_ops_panel_20260513_0138 | 3 |
| .bak_next_pill_orange | 3 |
| .bak_night_voice_rollback | 3 |
| .bak_night_voice_safe_bind | 3 |
| .bak_night_voice_toggle_bind | 3 |
| .bak_no_auto_popup_20260513_0239 | 3 |
| .bak_normal_pin_bright | 3 |
| .bak_normal_route_pin | 3 |
| .bak_offload_custom_modal | 3 |
| .bak_offload_split | 3 |
| .bak_onboarding_redirect | 3 |
| .bak_one_screen_compact | 3 |
| .bak_only54_shift_fix_20260516_105927 | 3 |
| .bak_patch2_runtime_reader_only | 3 |
| .bak_phase1_premium_top | 3 |
| .bak_phase2_premium_upgrade | 3 |
| .bak_phase3_final_premium | 3 |
| .bak_phase3_mobile_fallback_hotfix | 3 |
| .bak_photo_modal_fix_20260512_1950 | 3 |
| .bak_pickup_live_default | 3 |
| .bak_pickup_live_full_fix | 3 |
| .bak_placedock_static | 3 |
| .bak_planinda_fix | 3 |
| .bak_popup_focus_mode_20260513_0235 | 3 |
| .bak_premium_setup_final | 3 |
| .bak_print_clean_pdf | 3 |
| .bak_quick_guide_hub | 3 |
| .bak_real_bag_emanet_fix_20260523_120629 | 3 |
| .bak_real_bus_marker_20260513_0120 | 3 |
| .bak_real_route_geometry_20260513_0255 | 3 |
| .bak_rear_bottom_gap_soft_20260516_165121 | 3 |
| .bak_rear_bottom_gap_soft_20260516_165243 | 3 |
| .bak_rebuild_denizli_istanbul_20260520_122635 | 3 |
| .bak_remove_dash_jump | 3 |
| .bak_remove_dash_jump_exact | 3 |
| .bak_remove_debug_stop_memory_20260518_145103 | 3 |
| .bak_remove_debug_stop_memory_20260518_145203 | 3 |
| .bak_remove_direct_route_listener | 3 |
| .bak_remove_light_select_picker | 3 |
| .bak_remove_mobile_performance_fix_20260520_104823 | 3 |
| .bak_remove_old_blue_v1_20260513_191843 | 3 |
| .bak_remove_old_sync_conflict | 3 |
| .bak_remove_static_routes_real_20260520_140503 | 3 |
| .bak_remove_visible_slash_n_20260513_153508 | 3 |
| .bak_repair_top_split_shift_20260516_060003 | 3 |
| .bak_repair_voice_block_20260516_133452 | 3 |
| .bak_report_change_render_20260520_233720 | 3 |
| .bak_restore_continue_hero | 3 |
| .bak_restore_mobile_performance_fix_20260520_112145 | 3 |
| .bak_restore_mobile_performance_fix_20260520_112152 | 3 |
| .bak_restore_runtime_bridge_final | 3 |
| .bak_revert_cinema_text | 3 |
| .bak_revert_continue_live_flow_20260523_123657 | 3 |
| .bak_revert_next_ops_compact_20260513_0147 | 3 |
| .bak_revert_start_neon | 3 |
| .bak_right_column_spacing_20260516_063100 | 3 |
| .bak_rollback_bottom_deck_space_trim_20260516_064933 | 3 |
| .bak_rollback_bottom_row_align_20260516_075433 | 3 |
| .bak_rollback_bulk_modal_hide_bottom_nav_20260515_152530 | 3 |
| .bak_rollback_disable_deck_horizontal_scroll_20260516_070001 | 3 |
| .bak_rollback_drive_fab_top | 3 |
| .bak_rollback_safe_top_voice_overlay_20260516_060324 | 3 |
| .bak_rollback_seat_label_overlap_fix_20260515_210127 | 3 |
| .bak_rollback_top_voice_split_20260516_055839 | 3 |
| .bak_rollback_voice_to_bottom_20260516_110701 | 3 |
| .bak_rollback_wide_angle_scroll_20260516_071027 | 3 |
| .bak_rollback_wide_angle_scroll_20260516_171115 | 3 |
| .bak_rotate_gesture_20260513_153001 | 3 |
| .bak_route_bubble_drag_v2_20260513_160257 | 3 |
| .bak_route_card_bg_boost | 3 |
| .bak_route_card_color_boost | 3 |
| .bak_route_deviation_20260513_0217 | 3 |
| .bak_route_direct_tts | 3 |
| .bak_route_direct_tts_summary_fix | 3 |
| .bak_route_line_solid_20260513_0114 | 3 |
| .bak_route_marquee | 3 |
| .bak_route_memory_schema_reset_20260512_2317 | 3 |
| .bak_route_order_live_final_20260513_0023 | 3 |
| .bak_route_order_live_stop_20260513_0020 | 3 |
| .bak_route_pill_bg_boost | 3 |
| .bak_route_pin_blue_icon | 3 |
| .bak_route_pin_icon | 3 |
| .bak_route_red_green_20260513_0134 | 3 |
| .bak_route_status_right_20260513_0219 | 3 |
| .bak_route_summary_20260513_154928 | 3 |
| .bak_route_summary_bubble_20260513_155614 | 3 |
| .bak_route_summary_compact_20260513_155318 | 3 |
| .bak_route_toggle_20260513_0109 | 3 |
| .bak_route_voice_fix | 3 |
| .bak_route_warning_colors_restore | 3 |
| .bak_runtime_bridge | 3 |
| .bak_safe_select_picker | 3 |
| .bak_safe_select_rollback | 3 |
| .bak_safe_top_voice_overlay_20260516_060214 | 3 |
| .bak_search_fit_fix | 3 |
| .bak_seat_label_ghost_clean_20260518_210419 | 3 |
| .bak_seat_label_overlap_fix_20260515_210033 | 3 |
| .bak_seat_modal_simple_fix | 3 |
| .bak_seat_plan_card_image | 3 |
| .bak_seat_simple_bottom_bar | 3 |
| .bak_seat_simple_open_mode | 3 |
| .bak_seat_simple_summary_polish | 3 |
| .bak_seed_cache_before_gps | 3 |
| .bak_seed_cache_before_gps_fix2 | 3 |
| .bak_select_disappear_guard | 3 |
| .bak_select_keyboard_fix | 3 |
| .bak_select_picker_clickfix | 3 |
| .bak_select_picker_rollback | 3 |
| .bak_selected_stop_memory_fix_20260518_153404 | 3 |
| .bak_selected_stop_memory_fix_version_20260518_153404 | 3 |
| .bak_simple_top_voice_safe_20260516_061522 | 3 |
| .bak_smaller_hero_text | 3 |
| .bak_space_cleanup_20260518_163641 | 3 |
| .bak_speed_gps_km_patch | 3 |
| .bak_speed_render_throttle | 3 |
| .bak_speed_text_cleanup | 3 |
| .bak_speed_unit_fix | 3 |
| .bak_split_menu_images | 3 |
| .bak_split_rehber_images | 3 |
| .bak_stage2_20260513_0105 | 3 |
| .bak_stage3_popup_20260513_0128 | 3 |
| .bak_stats_row_hide | 3 |
| .bak_status_four_col_polish | 3 |
| .bak_stop_complete_text_20260513_0157 | 3 |
| .bak_stop_flow_compact_20260518_205314 | 3 |
| .bak_stop_flow_focus_20260515_151416 | 3 |
| .bak_stop_flow_live_runtime_sync_20260520_103326 | 3 |
| .bak_stop_memory_clear_once_20260518_141013 | 3 |
| .bak_stop_summary_bag_location_20260512_2232 | 3 |
| .bak_stop_toast_20260515_151720 | 3 |
| .bak_summary_box_ghost_icons | 3 |
| .bak_summary_bubble_polish_20260513_155843 | 3 |
| .bak_theme_rollback | 3 |
| .bak_tilt_3d_view_20260513_152416 | 3 |
| .bak_time_prayer_remove_final | 3 |
| .bak_time_prayer_split | 3 |
| .bak_timeline_balance_final | 3 |
| .bak_timeline_neon_final | 3 |
| .bak_tone | 3 |
| .bak_top_sound_toggle_20260516_112357 | 3 |
| .bak_top_voice_split_20260516_055736 | 3 |
| .bak_travego_marker_20260513_0118 | 3 |
| .bak_trip_id_memory_guard_20260512_2312 | 3 |
| .bak_tts_button_sync_fix | 3 |
| .bak_tts_sync_event | 3 |
| .bak_tts_sync_fix | 3 |
| .bak_tv_marquee_fix | 3 |
| .bak_vendor_path_fix_20260512_1139 | 3 |
| .bak_viewport_apple_fix | 3 |
| .bak_viewport_fix | 3 |
| .bak_viewport_fix_clean | 3 |
| .bak_visual_caption_tune | 3 |
| .bak_voice_bottom_final_20260516_111251 | 3 |
| .bak_voice_card_image | 3 |
| .bak_voice_clean_one_final | 3 |
| .bak_voice_conflict_clean | 3 |
| .bak_voice_direct_board_20260518_125204 | 3 |
| .bak_voice_direct_board_gender_20260518_132303 | 3 |
| .bak_voice_direct_board_gender_version_20260518_132303 | 3 |
| .bak_voice_direct_board_general_20260518_125607 | 3 |
| .bak_voice_direct_board_general_20260518_125826 | 3 |
| .bak_voice_direct_board_general_version_20260518_125607 | 3 |
| .bak_voice_direct_board_general_version_20260518_125826 | 3 |
| .bak_voice_direct_board_version_20260518_125204 | 3 |
| .bak_voice_map_fullscreen_version_20260518_124532 | 3 |
| .bak_voice_merge_fix | 3 |
| .bak_voice_owner_fix | 3 |
| .bak_voice_row_clean_final | 3 |
| .bak_voice_row_equal_counter | 3 |
| .bak_voice_row_equal_final | 3 |
| .bak_voice_row_equal_rollback | 3 |
| .bak_voice_row_final_clean | 3 |
| .bak_voice_row_fix_rollback | 3 |
| .bak_voice_row_spacing_final | 3 |
| .bak_voice_seat_emoji | 3 |
| .bak_voice_seat_icon_final | 3 |
| .bak_voice_seat_icon_match | 3 |
| .bak_voice_summary_20260518_124001 | 3 |
| .bak_voice_summary_version_20260518_124001 | 3 |
| .bak_voice_to_bottom_20260516_110540 | 3 |
| .bak_wide_angle_final_nudge_20260516_070540 | 3 |
| .before_next_revert_test | 3 |
| .before_revert_route_strip_bug | 3 |
| .current_bad | 3 |
| .gradle | 3 |
| .html | 3 |
| .sql | 3 |
| .bak_bag_emanet_split_20260523_114832 | 2 |
| .bak_before_apk_sync_20260518_182148 | 2 |
| .bak_button_bridge_20260523_141312 | 2 |
| .bak_clean_wrong_live_flow_v2_20260523_094322 | 2 |
| .bak_collapsible_20260523_133213 | 2 |
| .bak_continue_live_eta_engine_20260523_105409 | 2 |
| .bak_continue_live_flow_refresh_20260523_123118 | 2 |
| .bak_coords_sync_20260518_184401 | 2 |
| .bak_css_parts_20260523_144047 | 2 |
| .bak_css_split_20260523_125057 | 2 |
| .bak_diag_collapsible_20260523_133213 | 2 |
| .bak_fix_live_bag_emanet_counter_20260523_115747 | 2 |
| .bak_fix_live_bag_emanet_counter_20260523_115758 | 2 |
| .bak_flow_refresh_20260523_130314 | 2 |
| .bak_gap_20260521_211630 | 2 |
| .bak_geom_sync_20260518_192438 | 2 |
| .bak_js_core_split_20260523_125851 | 2 |
| .bak_js_safe_split_20260523_125438 | 2 |
| .bak_km_distance_20260523_134050 | 2 |
| .bak_label_balance_20260521_212035 | 2 |
| .bak_labels_20260521_211435 | 2 |
| .bak_live_auto_stable_20260523_132033 | 2 |
| .bak_live_flow_v2_20260523_093847 | 2 |
| .bak_live_gender_counts_20260523_111341 | 2 |
| .bak_name_km_20260523_134050 | 2 |
| .bak_next_stop_border_20260523_114325 | 2 |
| .bak_next_stop_glow_20260523_113649 | 2 |
| .bak_no_flicker_20260523_130647 | 2 |
| .bak_parts_20260523_144047 | 2 |
| .bak_port_guard_20260530_104842 | 2 |
| .bak_remove_newline_announce_20260523_122341 | 2 |
| .bak_remove_smaller_20260521_212205 | 2 |
| .bak_remove_smaller_20260521_212211 | 2 |
| .bak_remove_smaller_20260521_212306 | 2 |
| .bak_remove_smaller_20260521_212310 | 2 |
| .bak_rollback_bag_emanet_split_20260523_114955 | 2 |
| .bak_route_full_sync_20260518_191613 | 2 |
| .bak_smaller_20260521_211902 | 2 |
| .bak_tts_bridge_{ts} | 2 |
| .bak_unified_deck_20260521_210744 | 2 |
| .before_rollback_live_flow_v2_20260523_094130 | 2 |
| .disabled_20260523_094130 | 2 |
| .properties | 2 |
| [uzantısız] | 2 |
| .bak_active_route_lock_20260523_103538 | 1 |
| .bak_add_icmeler_denizli_istanbul_20260520_120742 | 1 |
| .bak_add_missing_ant_ist_coords_20260517_143011 | 1 |
| .bak_ai_duplicate_clean | 1 |
| .bak_ai_duplicate_clean_2 | 1 |
| .bak_ai_learned_route_fix | 1 |
| .bak_ai_learned_route_fix_correct | 1 |
| .bak_ai_remove_bag_cleanup | 1 |
| .bak_ai_runtime_answers_only | 1 |
| .bak_ant_ist_coord_copy_20260517_092120 | 1 |
| .bak_ant_ist_coord_copy_fix_20260517_092218 | 1 |
| .bak_ant_ist_route_segments_20260517_094613 | 1 |
| .bak_ant_ist_safe_coords_20260517_093127 | 1 |
| .bak_ant_ist_schedule_20260516_180115 | 1 |
| .bak_api_seats_offload_bag_clear | 1 |
| .bak_api_stops_contract_patch1 | 1 |
| .bak_api_stops_coords_final_fix | 1 |
| .bak_api_stops_route_coords_fix | 1 |
| .bak_bag_clear_on_seat_delete | 1 |
| .bak_bag_clear_on_seat_delete_v2 | 1 |
| .bak_before_remove_label_balance_20260521_212125 | 1 |
| .bak_before_restore_home_route_fix_20260523_102159 | 1 |
| .bak_before_restore_route_unlock_20260523_101748 | 1 |
| .bak_before_rollback_continue_real_data | 1 |
| .bak_before_rollback_missing_coords_20260517_143054 | 1 |
| .bak_bind_printbridge_real | 1 |
| .bak_bottom_fab54_20260523_084938 | 1 |
| .bak_build_denizli_istanbul_segments_20260520_122020 | 1 |
| .bak_consignment_trip_filter_fix | 1 |
| .bak_continue_live_flow_api_20260523_123118 | 1 |
| .bak_continue_live_v2_20260523_094525 | 1 |
| .bak_continue_route_sync_20260523_143011 | 1 |
| .bak_continue_stop_logic | 1 |
| .bak_continue_trip_bag_exact_patch | 1 |
| .bak_continue_trip_bag_fix_fresh | 1 |
| .bak_continue_trip_bag_tuple_fix | 1 |
| .bak_continue_trip_live_data | 1 |
| .bak_continue_trip_real_bags | 1 |
| .bak_continue_trip_real_data_final | 1 |
| .bak_copy_elmali_to_ant_ist_20260517_144513 | 1 |
| .bak_copy_elmali_to_ant_ist_20260517_144542 | 1 |
| .bak_dark_archive_20260521_154602 | 1 |
| .bak_dark_backup_20260521_155022 | 1 |
| .bak_dark_password_20260521_153534 | 1 |
| .bak_dark_profile_20260521_154308 | 1 |
| .bak_dark_recovery_20260521_152700 | 1 |
| .bak_dark_report_20260521_182646 | 1 |
| .bak_dark_settings_20260521_151412 | 1 |
| .bak_dark_subscription_20260521_153946 | 1 |
| .bak_delivered_consignment_filter_20260512_1943 | 1 |
| .bak_denizli_istanbul_alias_coords_20260520_115135 | 1 |
| .bak_denizli_istanbul_coords_mix_20260520_114947 | 1 |
| .bak_dot_blink_20260523_095527 | 1 |
| .bak_end_trip_cleanup_real_20260512_2300 | 1 |
| .bak_fix_api_stops_object_leak | 1 |
| .bak_fix_api_stops_string_list | 1 |
| .bak_fix_api_stops_string_list_v2 | 1 |
| .bak_fix_route_stop_coords_recursion | 1 |
| .bak_font_settings_20260521_151743 | 1 |
| .bak_geolocation_patch | 1 |
| .bak_home_route_fix_20260523_102028 | 1 |
| .bak_ios_status_premium_20260523_100429 | 1 |
| .bak_ist_ant_copy_missing_coords_20260517_144701 | 1 |
| .bak_ist_ant_schedule_20260518_122400 | 1 |
| .bak_istanbul_denizli_schedule_20260520_133113 | 1 |
| .bak_live_consignment_photo_url_20260512_1954 | 1 |
| .bak_live_map_20260513_0058 | 1 |
| .bak_live_speed_fix_20260523_110052 | 1 |
| .bak_no_cache_dev_20260520_101438 | 1 |
| .bak_onboarding_route | 1 |
| .bak_onboarding_server_fix | 1 |
| .bak_ortahan_km_fix_20260516_181153 | 1 |
| .bak_planinda_blink_20260523_100844 | 1 |
| .bak_planinda_green_20260523_095915 | 1 |
| .bak_rebuild_denizli_istanbul_segments_20260520_122635 | 1 |
| .bak_remove_dead_api_seat_code | 1 |
| .bak_remove_dead_api_seat_code_v2 | 1 |
| .bak_remove_ios_status_20260523_100619 | 1 |
| .bak_remove_planinda_green_20260523_100041 | 1 |
| .bak_remove_status_premium_small_20260523_100339 | 1 |
| .bak_reorder_denizli_istanbul_from_antalya_20260520_115837 | 1 |
| .bak_reports_deps_events_sums_fix | 1 |
| .bak_restore_antalya_istanbul_stops_20260520_102308 | 1 |
| .bak_revert_bottom_fab54_20260523_085109 | 1 |
| .bak_route_coords_refactor | 1 |
| .bak_route_flash_20260523_013005 | 1 |
| .bak_route_order_fix_final | 1 |
| .bak_route_referee_20260523_102348 | 1 |
| .bak_route_segments_json_fallback_20260513_0308 | 1 |
| .bak_route_segments_map_20260513_0254 | 1 |
| .bak_route_unlock_20260523_101631 | 1 |
| .bak_section_compact_20260521_191808 | 1 |
| .bak_section_report_style_20260521_191618 | 1 |
| .bak_section_tiny_20260521_192024 | 1 |
| .bak_sheet_speak_fix_20260523_112005 | 1 |
| .bak_small_fixes_runtime_bag | 1 |
| .bak_split_ai_module | 1 |
| .bak_split_backup_module | 1 |
| .bak_split_bag_emanet_20260523_120318 | 1 |
| .bak_split_cash_module | 1 |
| .bak_split_consignments_module | 1 |
| .bak_split_coords_module | 1 |
| .bak_split_live_ops_module | 1 |
| .bak_split_reports_light_module | 1 |
| .bak_split_routes_module | 1 |
| .bak_split_seats_module | 1 |
| .bak_split_settings_module | 1 |
| .bak_split_subscription_module | 1 |
| .bak_split_trip_report_builder | 1 |
| .bak_status_flicker_fix_20260523_104413 | 1 |
| .bak_status_premium_small_20260523_100232 | 1 |
| .bak_stop_fuzzy_match | 1 |
| .bak_tanitim_redirect_fix | 1 |
| .bak_top_report_style_20260521_183712 | 1 |
| .bak_top_status_compact_20260523_104212 | 1 |
| .bak_top_status_sync_20260523_103945 | 1 |
| .bak_tts_bridge | 1 |
| .bak_tuzla_segments_redraw_20260517_111153 | 1 |
| .bak_user_reset | 1 |
| .bak_via_20260513_0809 | 1 |
| .bak_voice_bottom_final_20260516_111252 | 1 |
| .bak_webview_scheme_fix | 1 |
| .before_coords_order_manual_fix | 1 |
| .disabled_20260523_085109 | 1 |
| .java | 1 |
| .local_backup_20260512_2009 | 1 |
| .sh | 1 |
| .yml | 1 |
| .zip | 1 |

## 4) En Büyük 40 Dosya
| Dosya | Byte | Satır |
| --- | --- | --- |
| storage/backups/yedek_20260502_235928.zip | 138465303 | None |
| uploads/consignments/c4_1757766898.jpg | 6772585 | None |
| uploads/consignments/c164_1779640343_811edb.jpg | 5364099 | None |
| uploads/consignments/c102_1768648725_446d39.jpg | 5224213 | None |
| uploads/consignments/c165_1779640391_830b13.jpg | 5015232 | None |
| uploads/consignments/c104_1768838688_f9c3d9.jpg | 4759401 | None |
| uploads/consignments/c136_1772130822_7d2b91.jpg | 4680858 | None |
| uploads/consignments/c148_1772716119_008d9f.jpg | 4456995 | None |
| uploads/consignments/c109_1770126060_5d114e.jpg | 4447235 | None |
| uploads/consignments/c144_1772131088_8dab69.jpg | 4446974 | None |
| uploads/consignments/c147_1772711100_4769a2.jpg | 4369585 | None |
| uploads/consignments/c142_1772131009_f69ec7.jpg | 4195645 | None |
| uploads/consignments/c154_1777406277_ce7469.jpg | 4017676 | None |
| uploads/consignments/c3_1757595850.jpg | 3838389 | None |
| uploads/consignments/c128_1771778140_212b85.jpg | 3812470 | None |
| uploads/consignments/c6_1758018950.jpg | 3798382 | None |
| uploads/consignments/c121_1771433789_4af594.jpg | 3773612 | None |
| android_app/app/src/main/python/static/data/route_segments.json.bak_build_denizli_istanbul_20260520_122020 | 3544583 | None |
| android_app/app/src/main/python/static/data/route_segments.json.bak_fix_alibeykoy_gebze_short_yss_20260517_235959 | 3544583 | None |
| android_app/app/src/main/python/static/data/route_segments.json.bak_accept_alibeykoy_gebze_yss_20260518_000238 | 3544583 | None |
| apk_payload/static/data/route_segments.json.bak_build_denizli_istanbul_20260520_122020 | 3544583 | None |
| apk_payload/static/data/route_segments.json.bak_fix_alibeykoy_gebze_short_yss_20260517_235959 | 3544583 | None |
| apk_payload/static/data/route_segments.json.bak_accept_alibeykoy_gebze_yss_20260518_000238 | 3544583 | None |
| static/data/route_segments.json.bak_build_denizli_istanbul_20260520_122020 | 3544583 | None |
| static/data/route_segments.json.bak_fix_alibeykoy_gebze_short_yss_20260517_235959 | 3544583 | None |
| static/data/route_segments.json.bak_accept_alibeykoy_gebze_yss_20260518_000238 | 3544583 | None |
| android_app/app/src/main/python/static/data/route_segments.json.bak_ist_ant_alibeykoy_gebze_yss_extra2_20260517_235604 | 3537181 | None |
| apk_payload/static/data/route_segments.json.bak_ist_ant_alibeykoy_gebze_yss_extra2_20260517_235604 | 3537181 | None |
| static/data/route_segments.json.bak_ist_ant_alibeykoy_gebze_yss_extra2_20260517_235604 | 3537181 | None |
| uploads/consignments/c149_1775061337_880202.jpg | 3524334 | None |
| android_app/app/src/main/python/static/data/route_segments.json.bak_ist_ant_alibeykoy_gebze_yss_extra_20260517_235252 | 3463743 | None |
| apk_payload/static/data/route_segments.json.bak_ist_ant_alibeykoy_gebze_yss_extra_20260517_235252 | 3463743 | None |
| static/data/route_segments.json.bak_ist_ant_alibeykoy_gebze_yss_extra_20260517_235252 | 3463743 | None |
| uploads/consignments/c131_1771778380_2246ec.jpg | 3287468 | None |
| uploads/consignments/c110_1770222831_63b3c3.jpg | 3264882 | None |
| uploads/consignments/c141_1772130989_d06045.jpg | 3240093 | None |
| db.sqlite3 | 3198976 | None |
| uploads/consignments/c143_1772131047_f124fa.jpg | 3159074 | None |
| db.sqlite3.bak_restore_denizli_istanbul_from_reverse_20260521_000121 | 3137536 | None |
| android_app/app/src/main/python/static/data/route_segments.json.bak_before_rollback_accept_alibeykoy_gebze_yss_20260518_001320 | 3132577 | None |

## 5) En Uzun 40 Text Dosya
| Dosya | Satır | Byte |
| --- | --- | --- |
| AYARLAR_DETAY_RAPORU.txt | 27181 | 2058344 |
| DURAK_AKISI_KAYNAK_RAPORU_20260518_205127.txt | 9323 | 1089535 |
| apk_payload/templates/continue_trip.html | 5428 | 133505 |
| android_app/app/src/main/python/static/seats/seats.css | 4872 | 102903 |
| apk_payload/static/seats/seats.css | 4872 | 102903 |
| static/seats/seats.css | 4872 | 102903 |
| audit_reports/muavin_step5_active_bug_context.txt | 4727 | 186546 |
| audit_reports/muavin_step4_suspicious_context.txt | 4666 | 183319 |
| LIVE_FLOW_TARGET_AUDIT.txt | 4636 | 134594 |
| app.py | 4513 | 139372 |
| android_app/app/src/main/python/app.py | 4508 | 139319 |
| apk_payload/app.py | 4409 | 136113 |
| backups/apk_sync_20260520_234501/app.py | 4409 | 136113 |
| AYARLAR_NET_RAPORU.txt | 3971 | 144110 |
| proje_dosya_listesi.txt | 3526 | 260296 |
| SURUS_MODU_GORUNUM_RAPORU_20260516_171742.txt | 3303 | 125553 |
| LIVE_FLOW_V2_AUDIT.txt | 3127 | 131691 |
| seats_baglanti_haritasi.txt | 3048 | 313674 |
| android_app/app/src/main/python/static/seats/seats.js | 2960 | 86274 |
| static/seats/seats.js | 2960 | 86274 |
| templates/live_map.html | 2927 | 71650 |
| android_app/app/src/main/python/templates/live_map.html | 2927 | 71650 |
| apk_payload/templates/live_map.html | 2927 | 71650 |
| apk_payload/static/seats/seats.js | 2893 | 84331 |
| templates/rehber.html | 2688 | 61151 |
| android_app/app/src/main/python/templates/rehber.html | 2688 | 61151 |
| apk_payload/templates/rehber.html | 2688 | 61151 |
| templates/ai_console.html | 2683 | 77979 |
| android_app/app/src/main/python/templates/ai_console.html | 2683 | 77979 |
| apk_payload/templates/ai_console.html | 2683 | 77979 |
| android_app/app/src/main/python/static/seats/seats-final.css | 2564 | 68499 |
| apk_payload/static/seats/seats-final.css | 2564 | 68499 |
| static/seats/seats-final.css | 2564 | 68499 |
| templates/hesap.html | 2461 | 62477 |
| android_app/app/src/main/python/templates/hesap.html | 2461 | 62477 |
| apk_payload/templates/hesap.html | 2461 | 62477 |
| android_app/app/src/main/python/static/continue/continue_trip_core.js | 2112 | 65483 |
| static/continue/continue_trip_core.js | 2112 | 65483 |
| android_app/app/src/main/python/static/live_map/muavin_live_map_extra.js | 2101 | 57832 |
| apk_payload/static/live_map/muavin_live_map_extra.js | 2101 | 57832 |

## 6) Aynı İçeriğe Sahip Dosyalar
Bunlar birebir aynı dosyalar. Silme adayı olabilir ama şimdilik sadece rapor.
| Hash | Adet | Dosyalar |
| --- | --- | --- |
| dacbfcc0d6f5 | 54 | android_app/app/src/main/python/static/seats/voice-tts.js, android_app/app/src/main/python/static/seats/voice-tts.js.bak_split_assistant_speed_voice_20260516_113619, android_app/app/src/main/python/static/seats/voice-tts.js.bak_clean_speed_voice_split_20260516_114304, android_app/app/src/main/python/static/seats/voice-tts.js.bak_final_voice_split_20260516_133629, android_app/app/src/main/python/static/seats/voice-tts.js.bak_voice_split_final2_20260516_145734, android_app/app/src/main/python/static/seats/voice-tts.js.bak_speed_voice_click_final_20260516_145945, android_app/app/src/main/python/static/seats/voice-tts.js.bak_tts_toggle_speed_sync_20260516_150032, android_app/app/src/main/python/static/seats/voice-tts.js.bak_force_tts_toggle_speed_sync_20260516_150133 |
| 169014289f8c | 27 | android_app/app/src/main/python/static/seats/seats.js.bak_split_assistant_speed_voice_20260516_113619, android_app/app/src/main/python/static/seats/seats.js.bak_clean_speed_voice_split_20260516_114304, android_app/app/src/main/python/static/seats/seats.js.bak_final_voice_split_20260516_133629, android_app/app/src/main/python/static/seats/seats.js.bak_before_corrective_restore_20260516_151536, android_app/app/src/main/python/static/seats/seats.js.bak_before_exact_113619_restore_20260516_153946, android_app/app/src/main/python/static/seats/seats.js.bak_before_restore_12_checkpoint_20260516_153518, android_app/app/src/main/python/static/seats/seats.js.bak_before_restore_from_20260516_145319_20260516_151331, android_app/app/src/main/python/static/seats/seats.js.bak_clear_ticket_on_offload_20260518_145103 |
| e05214b3f6cf | 24 | android_app/app/src/main/python/static/seats/drive-controls.js, android_app/app/src/main/python/static/seats/drive-controls.js.bak_before_clean_speed_split_leftover_20260516_151647, android_app/app/src/main/python/static/seats/drive-controls.js.bak_before_exact_113619_restore_20260516_153946, android_app/app/src/main/python/static/seats/drive-controls.js.bak_before_fix_bad_voice_rollback_20260516_150609, android_app/app/src/main/python/static/seats/drive-controls.js.bak_before_restore_12_checkpoint_20260516_153518, android_app/app/src/main/python/static/seats/drive-controls.js.bak_before_restore_natural_total_checkpoint_20260516_152438, android_app/app/src/main/python/static/seats/drive-controls.js.bak_before_rollback_exact_113619_20260516_154139, android_app/app/src/main/python/static/seats/drive-controls.js.bak_before_voice_mass_rollback_20260516_150355 |
| 219a681c6506 | 21 | templates/seats.html.bak_split_assistant_speed_voice_20260516_113619, templates/seats.html.bak_before_exact_113619_restore_20260516_153946, templates/seats.html.bak_before_rollback_exact_113619_20260516_154139, templates/seats.html.bak_before_restore_visual_blocks_20260516_153134, templates/seats.html.bak_before_remove_fab_compact_fit_20260516_154836, templates/seats.html.bak_drive_controls_repair_version_20260516_133452, templates/seats.html.bak_clean_speed_voice_split_20260516_114304, android_app/app/src/main/python/templates/seats.html.bak_split_assistant_speed_voice_20260516_113619 |
| 6f9c62253c55 | 18 | android_app/app/src/main/python/static/seats/drive-controls.js.bak_repair_voice_block_20260516_133452, android_app/app/src/main/python/static/seats/drive-controls.js.bak_force_repair_20260516_145319, android_app/app/src/main/python/static/seats/drive-controls.js.bak_hard_repair_voice_block_20260516_145427, android_app/app/src/main/python/static/seats/drive-controls.js.bak_hard_line_repair_20260516_145608, android_app/app/src/main/python/static/seats/drive-controls.js.bak_before_corrective_restore_20260516_151536, android_app/app/src/main/python/static/seats/drive-controls.js.bak_before_restore_previous_20260516_150549, apk_payload/static/seats/drive-controls.js.bak_before_corrective_restore_20260516_151536, apk_payload/static/seats/drive-controls.js.bak_before_restore_previous_20260516_150549 |
| 814acef4271b | 15 | android_app/app/src/main/python/static/seats/voice-commands.js.bak_voice_summary_20260518_124001, android_app/app/src/main/python/static/seats/voice-commands.js.bak_before_restore_12_checkpoint_20260516_153518, android_app/app/src/main/python/static/seats/voice-commands.js.bak_before_restore_natural_total_checkpoint_20260516_152438, android_app/app/src/main/python/static/seats/voice-commands.js.bak_before_rollback_exact_113619_20260516_154139, android_app/app/src/main/python/static/seats/voice-commands.js.bak_before_exact_113619_restore_20260516_153946, apk_payload/static/seats/voice-commands.js.bak_voice_summary_20260518_124001, apk_payload/static/seats/voice-commands.js.bak_before_restore_natural_total_checkpoint_20260516_152438, apk_payload/static/seats/voice-commands.js.bak_before_exact_113619_restore_20260516_153946 |
| c0234168110a | 14 | checkpoints/seats.js.before_refactor_20260520_110402, android_app/app/src/main/python/static/seats/seats.js.bak_selected_stop_memory_fix_20260518_153404, android_app/app/src/main/python/static/seats/seats.js.bak_sync_20260520_113916, android_app/app/src/main/python/static/seats/seats.js.bak_before_rollback_live_stop_core_20260520_104314, android_app/app/src/main/python/static/seats/seats.js.bak_live_stop_core_fix_20260520_104112, android_app/app/src/main/python/static/seats/seats.js.bak_tripkey_by_id_20260520_204710, apk_payload/static/seats/seats.js.bak_selected_stop_memory_fix_20260518_153404, apk_payload/static/seats/seats.js.bak_before_rollback_live_stop_core_20260520_104314 |
| 1c2e4c4be71b | 12 | templates/seats.html.bak_selected_stop_memory_fix_version_20260518_153404, templates/seats.html.bak_before_full_cleanup_audit_20260518_153638, templates/seats.html.bak_remove_debug_stop_memory_20260518_145203, templates/seats.html.bak_before_cleanup_step1_20260518_153910, android_app/app/src/main/python/templates/seats.html.bak_remove_debug_stop_memory_20260518_145203, android_app/app/src/main/python/templates/seats.html.bak_selected_stop_memory_fix_version_20260518_153404, android_app/app/src/main/python/templates/seats.html.bak_before_cleanup_step1_20260518_153910, android_app/app/src/main/python/templates/seats.html.bak_before_full_cleanup_audit_20260518_153638 |
| fea641f7925e | 12 | templates/seats.html.bak_stop_flow_live_runtime_sync_20260520_103326, templates/seats.html.bak_live_stop_core_fix_20260520_104112, templates/seats.html.bak_remove_mobile_performance_fix_20260520_104823, templates/seats.html.bak_before_rollback_live_stop_core_20260520_104314, android_app/app/src/main/python/templates/seats.html.bak_remove_mobile_performance_fix_20260520_104823, android_app/app/src/main/python/templates/seats.html.bak_before_rollback_live_stop_core_20260520_104314, android_app/app/src/main/python/templates/seats.html.bak_live_stop_core_fix_20260520_104112, android_app/app/src/main/python/templates/seats.html.bak_stop_flow_live_runtime_sync_20260520_103326 |
| 23cd5cf75a6a | 12 | templates/seats.html.bak_before_restore_only_fab_compact_20260516_160058, templates/seats.html.bak_before_fab_mini_restore_20260516_155226, templates/seats.html.bak_before_restore_good_fab_20260516_155627, templates/seats.html.bak_before_fab_vertical_override_20260516_160256, android_app/app/src/main/python/templates/seats.html.bak_before_fab_mini_restore_20260516_155226, android_app/app/src/main/python/templates/seats.html.bak_before_restore_good_fab_20260516_155627, android_app/app/src/main/python/templates/seats.html.bak_before_restore_only_fab_compact_20260516_160058, android_app/app/src/main/python/templates/seats.html.bak_before_fab_vertical_override_20260516_160256 |
| 8fda10ba5f5d | 12 | android_app/app/src/main/python/static/seats/seats.js.bak_add_continue_trip_coords_helper_final, android_app/app/src/main/python/static/seats/seats.js.bak_add_missing_coords_helper_fix, android_app/app/src/main/python/static/seats/seats.js.bak_append_missing_coords_helper, android_app/app/src/main/python/static/seats/seats.js.bak_insert_coords_helper_after_currentCoords, apk_payload/static/seats/seats.js.bak_add_continue_trip_coords_helper_final, apk_payload/static/seats/seats.js.bak_add_missing_coords_helper_fix, apk_payload/static/seats/seats.js.bak_append_missing_coords_helper, apk_payload/static/seats/seats.js.bak_insert_coords_helper_after_currentCoords |
| f2c9f51bee2b | 12 | android_app/app/src/main/python/static/data/route_segments.json.bak_salihli_akhisar_via_points_20260517_100608, android_app/app/src/main/python/static/data/route_segments.json.bak_salihli_pin_d555_fix_20260517_101253, android_app/app/src/main/python/static/data/route_segments.json.bak_salihli_correct_turn_20260517_101854, android_app/app/src/main/python/static/data/route_segments.json.bak_akhisar_balikesir_d565_20260517_103807, apk_payload/static/data/route_segments.json.bak_salihli_akhisar_via_points_20260517_100608, apk_payload/static/data/route_segments.json.bak_salihli_pin_d555_fix_20260517_101253, apk_payload/static/data/route_segments.json.bak_salihli_correct_turn_20260517_101854, apk_payload/static/data/route_segments.json.bak_akhisar_balikesir_d565_20260517_103807 |
| cdd9b0ca6173 | 12 | android_app/app/src/main/python/static/data/route_segments.json.bak_korkuteli_elmali_segments_20260517_143312, android_app/app/src/main/python/static/data/route_segments.json.bak_refresh_new_coords_segments_20260517_143857, android_app/app/src/main/python/static/data/route_segments.json.bak_denizli_korkuteli_segments_20260517_144319, android_app/app/src/main/python/static/data/route_segments.json.bak_ist_ant_refresh_segments_20260517_144738, apk_payload/static/data/route_segments.json.bak_korkuteli_elmali_segments_20260517_143312, apk_payload/static/data/route_segments.json.bak_refresh_new_coords_segments_20260517_143857, apk_payload/static/data/route_segments.json.bak_denizli_korkuteli_segments_20260517_144319, apk_payload/static/data/route_segments.json.bak_ist_ant_refresh_segments_20260517_144738 |
| a7547b1db953 | 10 | templates/seats.html.bak_tripkey_by_id_20260520_204710, templates/seats.html.bak_fix_tripkey_exact_20260520_204851, templates/seats.html.bak_restore_mobile_performance_fix_20260520_112152, android_app/app/src/main/python/templates/seats.html.bak_restore_mobile_performance_fix_20260520_112152, android_app/app/src/main/python/templates/seats.html.bak_sync_20260520_113916, android_app/app/src/main/python/templates/seats.html.bak_fix_tripkey_exact_20260520_204851, android_app/app/src/main/python/templates/seats.html.bak_tripkey_by_id_20260520_204710, apk_payload/templates/seats.html.bak_restore_mobile_performance_fix_20260520_112152 |
| 47e108914b94 | 10 | checkpoints/stop-flow-focus-patch.js.before_refactor_20260520_110402, android_app/app/src/main/python/static/seats/patches/stop-flow-focus-patch.js.bak_live_runtime_sync_20260520_103326, android_app/app/src/main/python/static/seats/patches/stop-flow-focus-patch.js.bak_scope_simple_only_20260520_105358, android_app/app/src/main/python/static/seats/patches/stop-flow-focus-patch.js.bak_simple_scope_20260520_110612, apk_payload/static/seats/patches/stop-flow-focus-patch.js.bak_live_runtime_sync_20260520_103326, apk_payload/static/seats/patches/stop-flow-focus-patch.js.bak_scope_simple_only_20260520_105358, apk_payload/static/seats/patches/stop-flow-focus-patch.js.bak_simple_scope_20260520_110612, static/seats/patches/stop-flow-focus-patch.js.bak_live_runtime_sync_20260520_103326 |
| 1100474790a1 | 9 | templates/seats.html.bak_end_trip_local_cleanup_20260512_2300, templates/seats.html.bak_seat_simple_open_mode, templates/seats.html.bak_stop_flow_cleanup_20260512_2304, android_app/app/src/main/python/templates/seats.html.bak_seat_simple_open_mode, android_app/app/src/main/python/templates/seats.html.bak_end_trip_local_cleanup_20260512_2300, android_app/app/src/main/python/templates/seats.html.bak_stop_flow_cleanup_20260512_2304, apk_payload/templates/seats.html.bak_end_trip_local_cleanup_20260512_2300, apk_payload/templates/seats.html.bak_stop_flow_cleanup_20260512_2304 |
| 5e9db76a71d3 | 9 | templates/live_map.html.bak_route_profile_system_20260513_1446, templates/live_map.html.bak_blue_location_20260513_150229, templates/live_map.html.bak_blue_location_fixed_20260513_150348, android_app/app/src/main/python/templates/live_map.html.bak_blue_location_fixed_20260513_150348, android_app/app/src/main/python/templates/live_map.html.bak_blue_location_20260513_150229, android_app/app/src/main/python/templates/live_map.html.bak_route_profile_system_20260513_1446, apk_payload/templates/live_map.html.bak_blue_location_20260513_150229, apk_payload/templates/live_map.html.bak_route_profile_system_20260513_1446 |
| 5a0e58a3d4c6 | 9 | templates/seats.html.bak_drive_force_repair_version_20260516_145319, templates/seats.html.bak_before_corrective_restore_20260516_151536, templates/seats.html.bak_before_restore_previous_20260516_150549, android_app/app/src/main/python/templates/seats.html.bak_drive_force_repair_version_20260516_145319, android_app/app/src/main/python/templates/seats.html.bak_before_corrective_restore_20260516_151536, android_app/app/src/main/python/templates/seats.html.bak_before_restore_previous_20260516_150549, apk_payload/templates/seats.html.bak_before_corrective_restore_20260516_151536, apk_payload/templates/seats.html.bak_before_restore_previous_20260516_150549 |
| b3d2d9fda551 | 9 | templates/seats.html.bak_before_voice_mass_rollback_20260516_150355, templates/seats.html.bak_before_fix_bad_voice_rollback_20260516_150609, templates/seats.html.bak_before_clean_speed_split_leftover_20260516_151647, android_app/app/src/main/python/templates/seats.html.bak_before_clean_speed_split_leftover_20260516_151647, android_app/app/src/main/python/templates/seats.html.bak_before_voice_mass_rollback_20260516_150355, android_app/app/src/main/python/templates/seats.html.bak_before_fix_bad_voice_rollback_20260516_150609, apk_payload/templates/seats.html.bak_before_clean_speed_split_leftover_20260516_151647, apk_payload/templates/seats.html.bak_before_voice_mass_rollback_20260516_150355 |
| 367dc0d3f53a | 9 | templates/seats.html.bak_voice_summary_version_20260518_124001, templates/seats.html.bak_before_fab_drive_style_all_20260516_172024, templates/seats.html.bak_rollback_wide_angle_scroll_20260516_171115, android_app/app/src/main/python/templates/seats.html.bak_before_fab_drive_style_all_20260516_172024, android_app/app/src/main/python/templates/seats.html.bak_voice_summary_version_20260518_124001, android_app/app/src/main/python/templates/seats.html.bak_rollback_wide_angle_scroll_20260516_171115, apk_payload/templates/seats.html.bak_before_fab_drive_style_all_20260516_172024, apk_payload/templates/seats.html.bak_voice_summary_version_20260518_124001 |
| 3957b22ab94e | 9 | templates/seats.html.bak_voice_direct_board_version_20260518_125204, templates/seats.html.bak_voice_direct_board_general_version_20260518_125826, templates/seats.html.bak_voice_direct_board_general_version_20260518_125607, android_app/app/src/main/python/templates/seats.html.bak_voice_direct_board_version_20260518_125204, android_app/app/src/main/python/templates/seats.html.bak_voice_direct_board_general_version_20260518_125607, android_app/app/src/main/python/templates/seats.html.bak_voice_direct_board_general_version_20260518_125826, apk_payload/templates/seats.html.bak_voice_direct_board_version_20260518_125204, apk_payload/templates/seats.html.bak_voice_direct_board_general_version_20260518_125607 |
| 6fe4a7f66074 | 9 | templates/trip_report.html.bak_fix_change_event_render_20260520_233609, templates/trip_report.html.bak_report_change_render_20260520_233720, templates/trip_report.html.bak_force_change_render_20260520_233819, android_app/app/src/main/python/templates/trip_report.html.bak_report_change_render_20260520_233720, android_app/app/src/main/python/templates/trip_report.html.bak_fix_change_event_render_20260520_233609, android_app/app/src/main/python/templates/trip_report.html.bak_force_change_render_20260520_233819, apk_payload/templates/trip_report.html.bak_report_change_render_20260520_233720, apk_payload/templates/trip_report.html.bak_fix_change_event_render_20260520_233609 |
| 20f8adc9a873 | 9 | android_app/app/src/main/python/static/seats/seats.js.bak_voice_split_final2_20260516_145734, android_app/app/src/main/python/static/seats/seats.js.bak_speed_voice_click_final_20260516_145945, android_app/app/src/main/python/static/seats/seats.js.bak_before_restore_previous_20260516_150549, apk_payload/static/seats/seats.js.bak_before_restore_previous_20260516_150549, apk_payload/static/seats/seats.js.bak_speed_voice_click_final_20260516_145945, apk_payload/static/seats/seats.js.bak_voice_split_final2_20260516_145734, static/seats/seats.js.bak_speed_voice_click_final_20260516_145945, static/seats/seats.js.bak_voice_split_final2_20260516_145734 |
| 0348985b4c84 | 9 | android_app/app/src/main/python/static/seats/voice-commands.js.bak_voice_direct_board_20260518_125204, android_app/app/src/main/python/static/seats/voice-commands.js.bak_voice_direct_board_general_20260518_125607, android_app/app/src/main/python/static/seats/voice-commands.js.bak_voice_direct_board_general_20260518_125826, apk_payload/static/seats/voice-commands.js.bak_voice_direct_board_20260518_125204, apk_payload/static/seats/voice-commands.js.bak_voice_direct_board_general_20260518_125607, apk_payload/static/seats/voice-commands.js.bak_voice_direct_board_general_20260518_125826, static/seats/voice-commands.js.bak_voice_direct_board_20260518_125204, static/seats/voice-commands.js.bak_voice_direct_board_general_20260518_125607 |
| 454d8ea5363b | 9 | android_app/app/src/main/python/static/seats/seats-final.css.bak_drive_voice_separat, android_app/app/src/main/python/static/seats/seats-final.css.bak_drive_voice_clean_single, android_app/app/src/main/python/static/seats/seats-final.css.bak_drive_voice_width_only, apk_payload/static/seats/seats-final.css.bak_drive_voice_clean_single, apk_payload/static/seats/seats-final.css.bak_drive_voice_separat, apk_payload/static/seats/seats-final.css.bak_drive_voice_width_only, static/seats/seats-final.css.bak_drive_voice_width_only, static/seats/seats-final.css.bak_drive_voice_separat |
| dfa7442a0f63 | 9 | android_app/app/src/main/python/static/seats/seats.js.bak_before_fix_bad_voice_rollback_20260516_150609, android_app/app/src/main/python/static/seats/seats.js.bak_before_clean_speed_split_leftover_20260516_151647, android_app/app/src/main/python/static/seats/seats.js.bak_before_voice_mass_rollback_20260516_150355, apk_payload/static/seats/seats.js.bak_before_fix_bad_voice_rollback_20260516_150609, apk_payload/static/seats/seats.js.bak_before_voice_mass_rollback_20260516_150355, apk_payload/static/seats/seats.js.bak_before_clean_speed_split_leftover_20260516_151647, static/seats/seats.js.bak_before_voice_mass_rollback_20260516_150355, static/seats/seats.js.bak_before_clean_speed_split_leftover_20260516_151647 |
| fd2abc101e94 | 9 | android_app/app/src/main/python/static/seats/voice-commands.js.bak_drive_voice_direct_guard, android_app/app/src/main/python/static/seats/voice-commands.js.bak_voice_button_fix, android_app/app/src/main/python/static/seats/voice-commands.js.bak_voice_button_state_fix, apk_payload/static/seats/voice-commands.js.bak_drive_voice_direct_guard, apk_payload/static/seats/voice-commands.js.bak_voice_button_fix, apk_payload/static/seats/voice-commands.js.bak_voice_button_state_fix, static/seats/voice-commands.js.bak_voice_button_state_fix, static/seats/voice-commands.js.bak_voice_button_fix |
| f3dbbc211ea5 | 9 | android_app/app/src/main/python/static/data/route_segments.json.bak_build_denizli_istanbul_20260520_122020, android_app/app/src/main/python/static/data/route_segments.json.bak_fix_alibeykoy_gebze_short_yss_20260517_235959, android_app/app/src/main/python/static/data/route_segments.json.bak_accept_alibeykoy_gebze_yss_20260518_000238, apk_payload/static/data/route_segments.json.bak_build_denizli_istanbul_20260520_122020, apk_payload/static/data/route_segments.json.bak_fix_alibeykoy_gebze_short_yss_20260517_235959, apk_payload/static/data/route_segments.json.bak_accept_alibeykoy_gebze_yss_20260518_000238, static/data/route_segments.json.bak_build_denizli_istanbul_20260520_122020, static/data/route_segments.json.bak_fix_alibeykoy_gebze_short_yss_20260517_235959 |
| a8c4f280dcf2 | 8 | android_app/app/src/main/python/templates/seats_parts/route_flow.html, android_app/app/src/main/python/templates/seats_parts/route_flow.html.bak_marquee_total_cleanup, apk_payload/templates/seats_parts/route_flow.html, apk_payload/templates/seats_parts/route_flow.html.bak_marquee_total_cleanup, templates/seats_parts/route_flow.html, templates/seats_parts/route_flow.html.bak_marquee_total_cleanup, templates/seats_parts/route_flow.html.bak_live_flow_v2_20260523_093847, templates/seats_parts/route_flow.html.bak_clean_wrong_live_flow_v2_20260523_094322 |
| 563c54543547 | 7 | rollback_backup_now/index.html.current_bad, templates/index.html.bak_split_menu_images, templates/index.html.bak_direct_final_banner, android_app/app/src/main/python/templates/index.html.bak_direct_final_banner, android_app/app/src/main/python/templates/index.html.bak_split_menu_images, apk_payload/templates/index.html.bak_direct_final_banner, apk_payload/templates/index.html.bak_split_menu_images |
| 3c9c8d0b830d | 7 | rollback_backup_now/base.html.current_bad, templates/base.html.bak_viewport_fix_clean, templates/base.html.bak_vendor_path_fix_20260512_1139, android_app/app/src/main/python/templates/base.html.bak_vendor_path_fix_20260512_1139, android_app/app/src/main/python/templates/base.html.bak_viewport_fix_clean, apk_payload/templates/base.html.bak_vendor_path_fix_20260512_1139, apk_payload/templates/base.html.bak_viewport_fix_clean |
| 7cb77c6f5d1b | 7 | templates/seats.html.bak_scope_simple_only_20260520_105358, templates/seats.html.bak_simple_scope_20260520_110612, checkpoints/seats.html.before_refactor_20260520_110402, android_app/app/src/main/python/templates/seats.html.bak_scope_simple_only_20260520_105358, android_app/app/src/main/python/templates/seats.html.bak_simple_scope_20260520_110612, apk_payload/templates/seats.html.bak_scope_simple_only_20260520_105358, apk_payload/templates/seats.html.bak_simple_scope_20260520_110612 |
| 26893ab528b8 | 7 | modules/trip_report_builder.py, modules/trip_report_builder.py.bak_report_change_payload_20260520_233720, backups/apk_sync_20260520_234501/trip_report_builder.py, android_app/app/src/main/python/modules/trip_report_builder.py, android_app/app/src/main/python/modules/trip_report_builder.py.bak_report_change_payload_20260520_233720, apk_payload/modules/trip_report_builder.py, apk_payload/modules/trip_report_builder.py.bak_report_change_payload_20260520_233720 |
| 365763fd400b | 6 | templates/base.html, templates/base.html.bak_remove_all_visible_slash_n_20260513_153624, android_app/app/src/main/python/templates/base.html, android_app/app/src/main/python/templates/base.html.bak_remove_all_visible_slash_n_20260513_153624, apk_payload/templates/base.html, apk_payload/templates/base.html.bak_remove_all_visible_slash_n_20260513_153624 |
| 62df8aad6f23 | 6 | templates/seats.html.bak_voice_seat_mini, templates/seats.html.bak_voice_mini_counter_final, android_app/app/src/main/python/templates/seats.html.bak_voice_seat_mini, android_app/app/src/main/python/templates/seats.html.bak_voice_mini_counter_final, apk_payload/templates/seats.html.bak_voice_seat_mini, apk_payload/templates/seats.html.bak_voice_mini_counter_final |
| 73601031a6a8 | 6 | templates/hesap.html, templates/hesap.html.bak_print_clean_pdf, android_app/app/src/main/python/templates/hesap.html, android_app/app/src/main/python/templates/hesap.html.bak_print_clean_pdf, apk_payload/templates/hesap.html, apk_payload/templates/hesap.html.bak_print_clean_pdf |
| 07c508de659e | 6 | templates/seats.html.bak_drive_voice_equal_clean, templates/seats.html.bak_drive_voice_clone_row, android_app/app/src/main/python/templates/seats.html.bak_drive_voice_clone_row, android_app/app/src/main/python/templates/seats.html.bak_drive_voice_equal_clean, apk_payload/templates/seats.html.bak_drive_voice_equal_clean, apk_payload/templates/seats.html.bak_drive_voice_clone_row |
| c18d87273e6f | 6 | templates/rehber.html.bak_cinema_text_update, templates/rehber.html.bak_revert_cinema_text, android_app/app/src/main/python/templates/rehber.html.bak_cinema_text_update, android_app/app/src/main/python/templates/rehber.html.bak_revert_cinema_text, apk_payload/templates/rehber.html.bak_cinema_text_update, apk_payload/templates/rehber.html.bak_revert_cinema_text |
| b275f9216814 | 6 | templates/continue_trip.html.bak_live_operation_panel, templates/continue_trip.html.bak_fix_continue_hero, android_app/app/src/main/python/templates/continue_trip.html.bak_fix_continue_hero, android_app/app/src/main/python/templates/continue_trip.html.bak_live_operation_panel, apk_payload/templates/continue_trip.html.bak_fix_continue_hero, apk_payload/templates/continue_trip.html.bak_live_operation_panel |
| d94f6e9b1aed | 6 | templates/continue_trip.html.bak_continue_stop_bridge, templates/continue_trip.html.bak_liveStop_bridge_fix, android_app/app/src/main/python/templates/continue_trip.html.bak_continue_stop_bridge, android_app/app/src/main/python/templates/continue_trip.html.bak_liveStop_bridge_fix, apk_payload/templates/continue_trip.html.bak_continue_stop_bridge, apk_payload/templates/continue_trip.html.bak_liveStop_bridge_fix |
| 2742a9442282 | 6 | templates/continue_trip.html.bak_remove_dash_jump, templates/continue_trip.html.bak_remove_dash_jump_exact, android_app/app/src/main/python/templates/continue_trip.html.bak_remove_dash_jump, android_app/app/src/main/python/templates/continue_trip.html.bak_remove_dash_jump_exact, apk_payload/templates/continue_trip.html.bak_remove_dash_jump, apk_payload/templates/continue_trip.html.bak_remove_dash_jump_exact |
| fff775f186a5 | 6 | templates/continue_trip.html.bak_seed_cache_before_gps, templates/continue_trip.html.bak_seed_cache_before_gps_fix2, android_app/app/src/main/python/templates/continue_trip.html.bak_seed_cache_before_gps_fix2, android_app/app/src/main/python/templates/continue_trip.html.bak_seed_cache_before_gps, apk_payload/templates/continue_trip.html.bak_seed_cache_before_gps, apk_payload/templates/continue_trip.html.bak_seed_cache_before_gps_fix2 |
| e35de73dc42c | 6 | templates/continue_trip.html.bak_continue_trip_all_cards_from_cached_coords, templates/continue_trip.html.bak_future_stops_distance_bind, android_app/app/src/main/python/templates/continue_trip.html.bak_continue_trip_all_cards_from_cached_coords, android_app/app/src/main/python/templates/continue_trip.html.bak_future_stops_distance_bind, apk_payload/templates/continue_trip.html.bak_continue_trip_all_cards_from_cached_coords, apk_payload/templates/continue_trip.html.bak_future_stops_distance_bind |
| 72b5668e1fc3 | 6 | templates/continue_trip.html.bak_bag_photo_gallery_20260512_1322, templates/continue_trip.html.bak_existing_bag_gallery_20260512_1325, android_app/app/src/main/python/templates/continue_trip.html.bak_existing_bag_gallery_20260512_1325, android_app/app/src/main/python/templates/continue_trip.html.bak_bag_photo_gallery_20260512_1322, apk_payload/templates/continue_trip.html.bak_bag_photo_gallery_20260512_1322, apk_payload/templates/continue_trip.html.bak_existing_bag_gallery_20260512_1325 |
| be7ccdf7d438 | 6 | templates/seats.html.bak_before_design, templates/seats.html.bak_design_v1, android_app/app/src/main/python/templates/seats.html.bak_design_v1, android_app/app/src/main/python/templates/seats.html.bak_before_design, apk_payload/templates/seats.html.bak_design_v1, apk_payload/templates/seats.html.bak_before_design |
| 9ac0260e950e | 6 | templates/seats.html.bak_safe_select_picker, templates/seats.html.bak_select_picker_rollback, android_app/app/src/main/python/templates/seats.html.bak_safe_select_picker, android_app/app/src/main/python/templates/seats.html.bak_select_picker_rollback, apk_payload/templates/seats.html.bak_select_picker_rollback, apk_payload/templates/seats.html.bak_safe_select_picker |
| f0cbffe33696 | 6 | templates/index.html.bak_dark_apple_home_final, templates/index.html.bak_dark_premium_override, android_app/app/src/main/python/templates/index.html.bak_dark_apple_home_final, android_app/app/src/main/python/templates/index.html.bak_dark_premium_override, apk_payload/templates/index.html.bak_dark_apple_home_final, apk_payload/templates/index.html.bak_dark_premium_override |
| 4401dc1c3564 | 6 | templates/continue_trip.html.bak_before_rollback_last_live_ui, templates/continue_trip.html.bak_compact_visual_fix, android_app/app/src/main/python/templates/continue_trip.html.bak_compact_visual_fix, android_app/app/src/main/python/templates/continue_trip.html.bak_before_rollback_last_live_ui, apk_payload/templates/continue_trip.html.bak_before_rollback_last_live_ui, apk_payload/templates/continue_trip.html.bak_compact_visual_fix |
| 8f37b1d4aa36 | 6 | templates/continue_trip.html.bak_live_hero_bus_img, templates/continue_trip.html.bak_live_hero_bus_insert, android_app/app/src/main/python/templates/continue_trip.html.bak_live_hero_bus_img, android_app/app/src/main/python/templates/continue_trip.html.bak_live_hero_bus_insert, apk_payload/templates/continue_trip.html.bak_live_hero_bus_img, apk_payload/templates/continue_trip.html.bak_live_hero_bus_insert |
| 1a49cbfe04f0 | 6 | templates/seats.html.bak_live_runtime_sync, templates/seats.html.bak_continue_stop_store, android_app/app/src/main/python/templates/seats.html.bak_continue_stop_store, android_app/app/src/main/python/templates/seats.html.bak_live_runtime_sync, apk_payload/templates/seats.html.bak_continue_stop_store, apk_payload/templates/seats.html.bak_live_runtime_sync |
| 125c49102152 | 6 | templates/continue_trip.html.bak_planinda_fix, templates/continue_trip.html.bak_speed_gps_km_patch, android_app/app/src/main/python/templates/continue_trip.html.bak_speed_gps_km_patch, android_app/app/src/main/python/templates/continue_trip.html.bak_planinda_fix, apk_payload/templates/continue_trip.html.bak_planinda_fix, apk_payload/templates/continue_trip.html.bak_speed_gps_km_patch |
| 2305ff6b75e1 | 6 | templates/seats.html.bak_light_design, templates/seats.html.bak_before_seats_final, android_app/app/src/main/python/templates/seats.html.bak_light_design, android_app/app/src/main/python/templates/seats.html.bak_before_seats_final, apk_payload/templates/seats.html.bak_before_seats_final, apk_payload/templates/seats.html.bak_light_design |
| 6bd3a6c6a6bb | 6 | templates/continue_trip.html.bak_raw_gpskm_format_fix, templates/continue_trip.html.bak_hide_initial_runtime_jump, android_app/app/src/main/python/templates/continue_trip.html.bak_hide_initial_runtime_jump, android_app/app/src/main/python/templates/continue_trip.html.bak_raw_gpskm_format_fix, apk_payload/templates/continue_trip.html.bak_hide_initial_runtime_jump, apk_payload/templates/continue_trip.html.bak_raw_gpskm_format_fix |
| cbf16820a1a7 | 6 | templates/live_map.html.bak_remove_visible_slash_n_20260513_153508, templates/live_map.html.bak_remove_all_visible_slash_n_20260513_153624, android_app/app/src/main/python/templates/live_map.html.bak_remove_all_visible_slash_n_20260513_153624, android_app/app/src/main/python/templates/live_map.html.bak_remove_visible_slash_n_20260513_153508, apk_payload/templates/live_map.html.bak_remove_visible_slash_n_20260513_153508, apk_payload/templates/live_map.html.bak_remove_all_visible_slash_n_20260513_153624 |
| c8f2aabd5cdc | 6 | templates/seats.html.bak_hide_bottom_menu_on_seat_modal, templates/seats.html.bak_seat_modal_simple_fix, android_app/app/src/main/python/templates/seats.html.bak_seat_modal_simple_fix, android_app/app/src/main/python/templates/seats.html.bak_hide_bottom_menu_on_seat_modal, apk_payload/templates/seats.html.bak_seat_modal_simple_fix, apk_payload/templates/seats.html.bak_hide_bottom_menu_on_seat_modal |
| 46cd1841016d | 6 | templates/seats.html.bak_speed_voice_click_final_20260516_145945, templates/seats.html.bak_tts_toggle_speed_sync_20260516_150032, android_app/app/src/main/python/templates/seats.html.bak_speed_voice_click_final_20260516_145945, android_app/app/src/main/python/templates/seats.html.bak_tts_toggle_speed_sync_20260516_150032, apk_payload/templates/seats.html.bak_speed_voice_click_final_20260516_145945, apk_payload/templates/seats.html.bak_tts_toggle_speed_sync_20260516_150032 |
| 973c94352723 | 6 | templates/seats.html.bak_extract_stop_flow_focus_20260518_174427, templates/seats.html.bak_extract_fab_patches_20260518_172257, android_app/app/src/main/python/templates/seats.html.bak_extract_fab_patches_20260518_172257, android_app/app/src/main/python/templates/seats.html.bak_extract_stop_flow_focus_20260518_174427, apk_payload/templates/seats.html.bak_extract_fab_patches_20260518_172257, apk_payload/templates/seats.html.bak_extract_stop_flow_focus_20260518_174427 |
| acc4b2d840a3 | 6 | templates/seats.html.bak_extract_drive_mode_pack_20260518_175558, templates/seats.html.bak_extract_seat_simple_pack_20260518_175924, android_app/app/src/main/python/templates/seats.html.bak_extract_drive_mode_pack_20260518_175558, android_app/app/src/main/python/templates/seats.html.bak_extract_seat_simple_pack_20260518_175924, apk_payload/templates/seats.html.bak_extract_drive_mode_pack_20260518_175558, apk_payload/templates/seats.html.bak_extract_seat_simple_pack_20260518_175924 |
| 54c5f1bbfbdc | 6 | templates/live_map.html.bak_bottom_actions_minimal_fixed_20260513_162448, templates/live_map.html.bak_bottom_actions_minimal_20260513_162347, android_app/app/src/main/python/templates/live_map.html.bak_bottom_actions_minimal_20260513_162347, android_app/app/src/main/python/templates/live_map.html.bak_bottom_actions_minimal_fixed_20260513_162448, apk_payload/templates/live_map.html.bak_bottom_actions_minimal_fixed_20260513_162448, apk_payload/templates/live_map.html.bak_bottom_actions_minimal_20260513_162347 |
| 459fe63db925 | 6 | templates/seats.html.bak_before_rollback_voice_direct_board_general_20260518_125649, templates/seats.html.bak_voice_direct_board_gender_version_20260518_132303, android_app/app/src/main/python/templates/seats.html.bak_voice_direct_board_gender_version_20260518_132303, android_app/app/src/main/python/templates/seats.html.bak_before_rollback_voice_direct_board_general_20260518_125649, apk_payload/templates/seats.html.bak_voice_direct_board_gender_version_20260518_132303, apk_payload/templates/seats.html.bak_before_rollback_voice_direct_board_general_20260518_125649 |
| 5697f1ac1e50 | 6 | templates/seats.html.bak_extract_stop_selected_toast_20260518_165333, templates/seats.html.bak_extract_bottom_voice_css_20260518_165551, android_app/app/src/main/python/templates/seats.html.bak_extract_stop_selected_toast_20260518_165333, android_app/app/src/main/python/templates/seats.html.bak_extract_bottom_voice_css_20260518_165551, apk_payload/templates/seats.html.bak_extract_stop_selected_toast_20260518_165333, apk_payload/templates/seats.html.bak_extract_bottom_voice_css_20260518_165551 |
| e5f4321a15e7 | 6 | templates/live_map.html.bak_approach_test_20260513_0225, templates/live_map.html.bak_approach_banner_20260513_0228, android_app/app/src/main/python/templates/live_map.html.bak_approach_test_20260513_0225, android_app/app/src/main/python/templates/live_map.html.bak_approach_banner_20260513_0228, apk_payload/templates/live_map.html.bak_approach_banner_20260513_0228, apk_payload/templates/live_map.html.bak_approach_test_20260513_0225 |
| 15defdd5c11a | 6 | templates/live_map.html.bak_approach_test_20260513_0229, templates/live_map.html.bak_popup_focus_mode_20260513_0235, android_app/app/src/main/python/templates/live_map.html.bak_approach_test_20260513_0229, android_app/app/src/main/python/templates/live_map.html.bak_popup_focus_mode_20260513_0235, apk_payload/templates/live_map.html.bak_approach_test_20260513_0229, apk_payload/templates/live_map.html.bak_popup_focus_mode_20260513_0235 |
| 0d131fe3b0ef | 6 | android_app/app/src/main/python/templates/seats_parts/deck.html, android_app/app/src/main/python/templates/seats_parts/deck.html.bak_only54_20260516_105535, apk_payload/templates/seats_parts/deck.html, apk_payload/templates/seats_parts/deck.html.bak_only54_20260516_105535, templates/seats_parts/deck.html, templates/seats_parts/deck.html.bak_only54_20260516_105535 |
| 4e5f4bb80bbe | 6 | android_app/app/src/main/python/static/seats/seats.js.before_revert_route_strip_bug, android_app/app/src/main/python/static/seats/seats.js.bak_fix_stop_flow_after_api_stops_object, apk_payload/static/seats/seats.js.before_revert_route_strip_bug, apk_payload/static/seats/seats.js.bak_fix_stop_flow_after_api_stops_object, static/seats/seats.js.before_revert_route_strip_bug, static/seats/seats.js.bak_fix_stop_flow_after_api_stops_object |
| 1ec0a84e638f | 6 | android_app/app/src/main/python/static/seats/seats.js.before_next_revert_test, android_app/app/src/main/python/static/seats/seats.js.bak_last_coords_cache, apk_payload/static/seats/seats.js.before_next_revert_test, apk_payload/static/seats/seats.js.bak_last_coords_cache, static/seats/seats.js.bak_last_coords_cache, static/seats/seats.js.before_next_revert_test |
| 4d0c820cdca6 | 6 | android_app/app/src/main/python/static/seats/seats.css.bak_last_row_inner_gap_fix_20260516_065535, android_app/app/src/main/python/static/seats/seats.css.bak_before_seats_final, apk_payload/static/seats/seats.css.bak_last_row_inner_gap_fix_20260516_065535, apk_payload/static/seats/seats.css.bak_before_seats_final, static/seats/seats.css.bak_before_seats_final, static/seats/seats.css.bak_last_row_inner_gap_fix_20260516_065535 |
| 723eab58c67c | 6 | android_app/app/src/main/python/static/seats/voice-commands.js.bak_voice_direct_board_gender_20260518_132303, android_app/app/src/main/python/static/seats/voice-commands.js.bak_before_rollback_voice_direct_board_general_20260518_125649, apk_payload/static/seats/voice-commands.js.bak_voice_direct_board_gender_20260518_132303, apk_payload/static/seats/voice-commands.js.bak_before_rollback_voice_direct_board_general_20260518_125649, static/seats/voice-commands.js.bak_voice_direct_board_gender_20260518_132303, static/seats/voice-commands.js.bak_before_rollback_voice_direct_board_general_20260518_125649 |
| bb790e80850c | 6 | android_app/app/src/main/python/static/seats/seats-dashboard-final.css.bak_tone, android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-final.css, apk_payload/static/seats/seats-dashboard-final.css.bak_tone, apk_payload/static/seats/_archive_theme_trials/seats-dashboard-final.css, static/seats/seats-dashboard-final.css.bak_tone, static/seats/_archive_theme_trials/seats-dashboard-final.css |
| a66f36a61076 | 6 | android_app/app/src/main/python/static/seats/seats-final.css.bak_drive_fab_final, android_app/app/src/main/python/static/seats/seats-final.css.bak_route_pin_icon, apk_payload/static/seats/seats-final.css.bak_drive_fab_final, apk_payload/static/seats/seats-final.css.bak_route_pin_icon, static/seats/seats-final.css.bak_drive_fab_final, static/seats/seats-final.css.bak_route_pin_icon |
| 244e7d34bac6 | 6 | android_app/app/src/main/python/static/seats/seats-final.css.bak_drive_voice_clone_row, android_app/app/src/main/python/static/seats/seats-final.css.bak_drive_voice_equal_clean, apk_payload/static/seats/seats-final.css.bak_drive_voice_clone_row, apk_payload/static/seats/seats-final.css.bak_drive_voice_equal_clean, static/seats/seats-final.css.bak_drive_voice_equal_clean, static/seats/seats-final.css.bak_drive_voice_clone_row |
| dc80ae8a51da | 6 | android_app/app/src/main/python/static/seats/seats-final.css.bak_voice_mini_counter_final, android_app/app/src/main/python/static/seats/seats-final.css.bak_voice_seat_mini, apk_payload/static/seats/seats-final.css.bak_voice_mini_counter_final, apk_payload/static/seats/seats-final.css.bak_voice_seat_mini, static/seats/seats-final.css.bak_voice_seat_mini, static/seats/seats-final.css.bak_voice_mini_counter_final |
| f9e36f293a1e | 6 | android_app/app/src/main/python/static/seats/seats.js.bak_fix_apk_voice_counts, android_app/app/src/main/python/static/seats/seats.js.bak_live_stop_pro_20260512_2248, apk_payload/static/seats/seats.js.bak_fix_apk_voice_counts, apk_payload/static/seats/seats.js.bak_live_stop_pro_20260512_2248, static/seats/seats.js.bak_live_stop_pro_20260512_2248, static/seats/seats.js.bak_fix_apk_voice_counts |
| d0ca1bc9ae42 | 6 | android_app/app/src/main/python/static/seats/seats.js.bak_fix_object_object_route_strip_v2, android_app/app/src/main/python/static/seats/seats.js.bak_fix_object_object_route_strip, apk_payload/static/seats/seats.js.bak_fix_object_object_route_strip, apk_payload/static/seats/seats.js.bak_fix_object_object_route_strip_v2, static/seats/seats.js.bak_fix_object_object_route_strip, static/seats/seats.js.bak_fix_object_object_route_strip_v2 |
| d162a9560704 | 6 | android_app/app/src/main/python/static/seats/seats.js.bak_general_seat_label_fix_20260516_062235, android_app/app/src/main/python/static/seats/seats.js.bak_label_title_regex_20260516_062350, apk_payload/static/seats/seats.js.bak_general_seat_label_fix_20260516_062235, apk_payload/static/seats/seats.js.bak_label_title_regex_20260516_062350, static/seats/seats.js.bak_label_title_regex_20260516_062350, static/seats/seats.js.bak_general_seat_label_fix_20260516_062235 |
| 7445bcd4c465 | 6 | android_app/app/src/main/python/static/seats/seats.js.bak_gpskm_raw_write_fix, android_app/app/src/main/python/static/seats/seats.js.bak_raw_gpskm_format_fix, apk_payload/static/seats/seats.js.bak_gpskm_raw_write_fix, apk_payload/static/seats/seats.js.bak_raw_gpskm_format_fix, static/seats/seats.js.bak_raw_gpskm_format_fix, static/seats/seats.js.bak_gpskm_raw_write_fix |
| 80aefc142c80 | 6 | android_app/app/src/main/python/static/seats/seats.js.bak_restore_runtime_bridge_final, android_app/app/src/main/python/static/seats/seats.js.bak_runtime_bridge, apk_payload/static/seats/seats.js.bak_restore_runtime_bridge_final, apk_payload/static/seats/seats.js.bak_runtime_bridge, static/seats/seats.js.bak_runtime_bridge, static/seats/seats.js.bak_restore_runtime_bridge_final |
| ce96cc6dfc79 | 6 | android_app/app/src/main/python/static/seats/seats-final.css.bak_voice_row_equal_counter, android_app/app/src/main/python/static/seats/seats-final.css.bak_voice_row_final_clean, apk_payload/static/seats/seats-final.css.bak_voice_row_equal_counter, apk_payload/static/seats/seats-final.css.bak_voice_row_final_clean, static/seats/seats-final.css.bak_voice_row_equal_counter, static/seats/seats-final.css.bak_voice_row_final_clean |
| 8df5f437b465 | 6 | android_app/app/src/main/python/static/seats/seats.js.bak_confirm_offload_disable, android_app/app/src/main/python/static/seats/seats.js.bak_offload_modal_clean, apk_payload/static/seats/seats.js.bak_offload_modal_clean, apk_payload/static/seats/seats.js.bak_confirm_offload_disable, static/seats/seats.js.bak_offload_modal_clean, static/seats/seats.js.bak_confirm_offload_disable |
| 6fe218ccbace | 6 | android_app/app/src/main/python/static/seats/seats.js.bak_continue_trip_bridge, android_app/app/src/main/python/static/seats/seats.js.bak_voice_mini_drive_fix, apk_payload/static/seats/seats.js.bak_continue_trip_bridge, apk_payload/static/seats/seats.js.bak_voice_mini_drive_fix, static/seats/seats.js.bak_voice_mini_drive_fix, static/seats/seats.js.bak_continue_trip_bridge |

## 7) Aynı İsimli Dosyalar
Aynı isim farklı klasördeyse özellikle web/android senkron çakışması olabilir.
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
| seats_panel.py | 4 | AYNI | modules/seats_panel.py, backups/apk_sync_20260520_234501/seats_panel.py, android_app/app/src/main/python/modules/seats_panel.py, apk_payload/modules/seats_panel.py |
| trip_report_builder.py | 4 | AYNI | modules/trip_report_builder.py, backups/apk_sync_20260520_234501/trip_report_builder.py, android_app/app/src/main/python/modules/trip_report_builder.py, apk_payload/modules/trip_report_builder.py |
| __init__.py | 3 | AYNI | android_app/app/src/main/python/modules/bags/__init__.py, apk_payload/modules/bags/__init__.py, modules/bags/__init__.py |
| add_route.html | 3 | AYNI | templates/add_route.html, android_app/app/src/main/python/templates/add_route.html, apk_payload/templates/add_route.html |
| admin_profile_6a6400ae12c1.jpg | 3 | AYNI | android_app/app/src/main/python/static/profile/admin_profile_6a6400ae12c1.jpg, apk_payload/static/profile/admin_profile_6a6400ae12c1.jpg, static/profile/admin_profile_6a6400ae12c1.jpg |
| ai_console.html | 3 | AYNI | templates/ai_console.html, android_app/app/src/main/python/templates/ai_console.html, apk_payload/templates/ai_console.html |
| ai_console.html.bak_intent_legend_fix | 3 | AYNI | templates/ai_console.html.bak_intent_legend_fix, android_app/app/src/main/python/templates/ai_console.html.bak_intent_legend_fix, apk_payload/templates/ai_console.html.bak_intent_legend_fix |
| ai_panel.py | 3 | AYNI | modules/ai_panel.py, android_app/app/src/main/python/modules/ai_panel.py, apk_payload/modules/ai_panel.py |
| app.js | 3 | AYNI | static/app.js, android_app/app/src/main/python/static/app.js, apk_payload/static/app.js |
| backup_panel.py | 3 | AYNI | modules/backup_panel.py, android_app/app/src/main/python/modules/backup_panel.py, apk_payload/modules/backup_panel.py |
| bags.js | 3 | AYNI | android_app/app/src/main/python/static/seats/bags.js, apk_payload/static/seats/bags.js, static/seats/bags.js |
| base.html | 3 | AYNI | templates/base.html, android_app/app/src/main/python/templates/base.html, apk_payload/templates/base.html |
| base.html.bak_remove_all_visible_slash_n_20260513_153624 | 3 | AYNI | templates/base.html.bak_remove_all_visible_slash_n_20260513_153624, android_app/app/src/main/python/templates/base.html.bak_remove_all_visible_slash_n_20260513_153624, apk_payload/templates/base.html.bak_remove_all_visible_slash_n_20260513_153624 |
| base.html.bak_vendor_path_fix_20260512_1139 | 3 | AYNI | templates/base.html.bak_vendor_path_fix_20260512_1139, android_app/app/src/main/python/templates/base.html.bak_vendor_path_fix_20260512_1139, apk_payload/templates/base.html.bak_vendor_path_fix_20260512_1139 |
| base.html.bak_viewport_apple_fix | 3 | AYNI | templates/base.html.bak_viewport_apple_fix, android_app/app/src/main/python/templates/base.html.bak_viewport_apple_fix, apk_payload/templates/base.html.bak_viewport_apple_fix |
| base.html.bak_viewport_fix | 3 | AYNI | templates/base.html.bak_viewport_fix, android_app/app/src/main/python/templates/base.html.bak_viewport_fix, apk_payload/templates/base.html.bak_viewport_fix |
| base.html.bak_viewport_fix_clean | 3 | AYNI | templates/base.html.bak_viewport_fix_clean, android_app/app/src/main/python/templates/base.html.bak_viewport_fix_clean, apk_payload/templates/base.html.bak_viewport_fix_clean |
| bootstrap.bundle.min.js | 3 | AYNI | android_app/app/src/main/python/static/vendor/bootstrap/bootstrap.bundle.min.js, apk_payload/static/vendor/bootstrap/bootstrap.bundle.min.js, static/vendor/bootstrap/bootstrap.bundle.min.js |
| bootstrap.min.css | 3 | AYNI | android_app/app/src/main/python/static/vendor/bootstrap/bootstrap.min.css, apk_payload/static/vendor/bootstrap/bootstrap.min.css, static/vendor/bootstrap/bootstrap.min.css |
| bottom-row-51-54-equal-spacing.css | 3 | AYNI | android_app/app/src/main/python/static/seats/patches/bottom-row-51-54-equal-spacing.css, apk_payload/static/seats/patches/bottom-row-51-54-equal-spacing.css, static/seats/patches/bottom-row-51-54-equal-spacing.css |
| bottom-voice-command.css | 3 | AYNI | android_app/app/src/main/python/static/seats/patches/bottom-voice-command.css, apk_payload/static/seats/patches/bottom-voice-command.css, static/seats/patches/bottom-voice-command.css |
| cash_panel.py | 3 | AYNI | modules/cash_panel.py, android_app/app/src/main/python/modules/cash_panel.py, apk_payload/modules/cash_panel.py |
| consignments.html | 3 | AYNI | templates/consignments.html, android_app/app/src/main/python/templates/consignments.html, apk_payload/templates/consignments.html |
| consignments.html.bak_photo_modal_fix_20260512_1950 | 3 | AYNI | templates/consignments.html.bak_photo_modal_fix_20260512_1950, android_app/app/src/main/python/templates/consignments.html.bak_photo_modal_fix_20260512_1950, apk_payload/templates/consignments.html.bak_photo_modal_fix_20260512_1950 |
| consignments_panel.py | 3 | AYNI | modules/consignments_panel.py, android_app/app/src/main/python/modules/consignments_panel.py, apk_payload/modules/consignments_panel.py |
| continue_trip.html.bak_add_speed_box | 3 | AYNI | templates/continue_trip.html.bak_add_speed_box, android_app/app/src/main/python/templates/continue_trip.html.bak_add_speed_box, apk_payload/templates/continue_trip.html.bak_add_speed_box |
| continue_trip.html.bak_bag_cargo_sections_20260512_1934 | 3 | AYNI | templates/continue_trip.html.bak_bag_cargo_sections_20260512_1934, android_app/app/src/main/python/templates/continue_trip.html.bak_bag_cargo_sections_20260512_1934, apk_payload/templates/continue_trip.html.bak_bag_cargo_sections_20260512_1934 |
| continue_trip.html.bak_bag_centered_fix_20260512_1406 | 3 | AYNI | templates/continue_trip.html.bak_bag_centered_fix_20260512_1406, android_app/app/src/main/python/templates/continue_trip.html.bak_bag_centered_fix_20260512_1406, apk_payload/templates/continue_trip.html.bak_bag_centered_fix_20260512_1406 |
| continue_trip.html.bak_bag_photo_gallery_20260512_1322 | 3 | AYNI | templates/continue_trip.html.bak_bag_photo_gallery_20260512_1322, android_app/app/src/main/python/templates/continue_trip.html.bak_bag_photo_gallery_20260512_1322, apk_payload/templates/continue_trip.html.bak_bag_photo_gallery_20260512_1322 |
| continue_trip.html.bak_bag_photo_viewer_20260512_1329 | 3 | AYNI | templates/continue_trip.html.bak_bag_photo_viewer_20260512_1329, android_app/app/src/main/python/templates/continue_trip.html.bak_bag_photo_viewer_20260512_1329, apk_payload/templates/continue_trip.html.bak_bag_photo_viewer_20260512_1329 |
| continue_trip.html.bak_before_rollback_last_live_ui | 3 | AYNI | templates/continue_trip.html.bak_before_rollback_last_live_ui, android_app/app/src/main/python/templates/continue_trip.html.bak_before_rollback_last_live_ui, apk_payload/templates/continue_trip.html.bak_before_rollback_last_live_ui |
| continue_trip.html.bak_cargo_detail_deliver_20260512_1938 | 3 | AYNI | templates/continue_trip.html.bak_cargo_detail_deliver_20260512_1938, android_app/app/src/main/python/templates/continue_trip.html.bak_cargo_detail_deliver_20260512_1938, apk_payload/templates/continue_trip.html.bak_cargo_detail_deliver_20260512_1938 |
| continue_trip.html.bak_cargo_photo_badge_fix_20260512_1958 | 3 | AYNI | templates/continue_trip.html.bak_cargo_photo_badge_fix_20260512_1958, android_app/app/src/main/python/templates/continue_trip.html.bak_cargo_photo_badge_fix_20260512_1958, apk_payload/templates/continue_trip.html.bak_cargo_photo_badge_fix_20260512_1958 |
| continue_trip.html.bak_cargo_photo_viewer_20260512_1956 | 3 | AYNI | templates/continue_trip.html.bak_cargo_photo_viewer_20260512_1956, android_app/app/src/main/python/templates/continue_trip.html.bak_cargo_photo_viewer_20260512_1956, apk_payload/templates/continue_trip.html.bak_cargo_photo_viewer_20260512_1956 |
| continue_trip.html.bak_change_destination_20260512_1238 | 3 | AYNI | templates/continue_trip.html.bak_change_destination_20260512_1238, android_app/app/src/main/python/templates/continue_trip.html.bak_change_destination_20260512_1238, apk_payload/templates/continue_trip.html.bak_change_destination_20260512_1238 |
| continue_trip.html.bak_clean_rewrite | 3 | AYNI | templates/continue_trip.html.bak_clean_rewrite, android_app/app/src/main/python/templates/continue_trip.html.bak_clean_rewrite, apk_payload/templates/continue_trip.html.bak_clean_rewrite |
| continue_trip.html.bak_cleanup_bad_speed_gps | 3 | AYNI | templates/continue_trip.html.bak_cleanup_bad_speed_gps, android_app/app/src/main/python/templates/continue_trip.html.bak_cleanup_bad_speed_gps, apk_payload/templates/continue_trip.html.bak_cleanup_bad_speed_gps |
| continue_trip.html.bak_compact_neon_20260511_134504 | 3 | AYNI | templates/continue_trip.html.bak_compact_neon_20260511_134504, android_app/app/src/main/python/templates/continue_trip.html.bak_compact_neon_20260511_134504, apk_payload/templates/continue_trip.html.bak_compact_neon_20260511_134504 |
| continue_trip.html.bak_compact_visual_fix | 3 | AYNI | templates/continue_trip.html.bak_compact_visual_fix, android_app/app/src/main/python/templates/continue_trip.html.bak_compact_visual_fix, apk_payload/templates/continue_trip.html.bak_compact_visual_fix |
| continue_trip.html.bak_continue_stop_bridge | 3 | AYNI | templates/continue_trip.html.bak_continue_stop_bridge, android_app/app/src/main/python/templates/continue_trip.html.bak_continue_stop_bridge, apk_payload/templates/continue_trip.html.bak_continue_stop_bridge |
| continue_trip.html.bak_continue_trip_all_cards_from_cached_coords | 3 | AYNI | templates/continue_trip.html.bak_continue_trip_all_cards_from_cached_coords, android_app/app/src/main/python/templates/continue_trip.html.bak_continue_trip_all_cards_from_cached_coords, apk_payload/templates/continue_trip.html.bak_continue_trip_all_cards_from_cached_coords |
| continue_trip.html.bak_continue_trip_sync_from_seats | 3 | AYNI | templates/continue_trip.html.bak_continue_trip_sync_from_seats, android_app/app/src/main/python/templates/continue_trip.html.bak_continue_trip_sync_from_seats, apk_payload/templates/continue_trip.html.bak_continue_trip_sync_from_seats |
| continue_trip.html.bak_end_trip_local_cleanup_20260512_2300 | 3 | AYNI | templates/continue_trip.html.bak_end_trip_local_cleanup_20260512_2300, android_app/app/src/main/python/templates/continue_trip.html.bak_end_trip_local_cleanup_20260512_2300, apk_payload/templates/continue_trip.html.bak_end_trip_local_cleanup_20260512_2300 |
| continue_trip.html.bak_existing_bag_gallery_20260512_1325 | 3 | AYNI | templates/continue_trip.html.bak_existing_bag_gallery_20260512_1325, android_app/app/src/main/python/templates/continue_trip.html.bak_existing_bag_gallery_20260512_1325, apk_payload/templates/continue_trip.html.bak_existing_bag_gallery_20260512_1325 |
| continue_trip.html.bak_final_stabilizer | 3 | AYNI | templates/continue_trip.html.bak_final_stabilizer, android_app/app/src/main/python/templates/continue_trip.html.bak_final_stabilizer, apk_payload/templates/continue_trip.html.bak_final_stabilizer |
| continue_trip.html.bak_fix_continue_hero | 3 | AYNI | templates/continue_trip.html.bak_fix_continue_hero, android_app/app/src/main/python/templates/continue_trip.html.bak_fix_continue_hero, apk_payload/templates/continue_trip.html.bak_fix_continue_hero |
| continue_trip.html.bak_fix_live_km_jump | 3 | AYNI | templates/continue_trip.html.bak_fix_live_km_jump, android_app/app/src/main/python/templates/continue_trip.html.bak_fix_live_km_jump, apk_payload/templates/continue_trip.html.bak_fix_live_km_jump |
| continue_trip.html.bak_force_single_gps_format | 3 | AYNI | templates/continue_trip.html.bak_force_single_gps_format, android_app/app/src/main/python/templates/continue_trip.html.bak_force_single_gps_format, apk_payload/templates/continue_trip.html.bak_force_single_gps_format |
| continue_trip.html.bak_future_stop_gps_distance | 3 | AYNI | templates/continue_trip.html.bak_future_stop_gps_distance, android_app/app/src/main/python/templates/continue_trip.html.bak_future_stop_gps_distance, apk_payload/templates/continue_trip.html.bak_future_stop_gps_distance |
| continue_trip.html.bak_future_stops_distance_bind | 3 | AYNI | templates/continue_trip.html.bak_future_stops_distance_bind, android_app/app/src/main/python/templates/continue_trip.html.bak_future_stops_distance_bind, apk_payload/templates/continue_trip.html.bak_future_stops_distance_bind |
| continue_trip.html.bak_head_n_fix_20260512_2043 | 3 | AYNI | templates/continue_trip.html.bak_head_n_fix_20260512_2043, android_app/app/src/main/python/templates/continue_trip.html.bak_head_n_fix_20260512_2043, apk_payload/templates/continue_trip.html.bak_head_n_fix_20260512_2043 |
| continue_trip.html.bak_hero_title_class | 3 | AYNI | templates/continue_trip.html.bak_hero_title_class, android_app/app/src/main/python/templates/continue_trip.html.bak_hero_title_class, apk_payload/templates/continue_trip.html.bak_hero_title_class |
| continue_trip.html.bak_hide_initial_runtime_jump | 3 | AYNI | templates/continue_trip.html.bak_hide_initial_runtime_jump, android_app/app/src/main/python/templates/continue_trip.html.bak_hide_initial_runtime_jump, apk_payload/templates/continue_trip.html.bak_hide_initial_runtime_jump |
| continue_trip.html.bak_literal_n_cleanup_20260512_2001 | 3 | AYNI | templates/continue_trip.html.bak_literal_n_cleanup_20260512_2001, android_app/app/src/main/python/templates/continue_trip.html.bak_literal_n_cleanup_20260512_2001, apk_payload/templates/continue_trip.html.bak_literal_n_cleanup_20260512_2001 |
| continue_trip.html.bak_literal_newline_fix_20260512_1409 | 3 | AYNI | templates/continue_trip.html.bak_literal_newline_fix_20260512_1409, android_app/app/src/main/python/templates/continue_trip.html.bak_literal_newline_fix_20260512_1409, apk_payload/templates/continue_trip.html.bak_literal_newline_fix_20260512_1409 |
| continue_trip.html.bak_liveStop_bridge_fix | 3 | AYNI | templates/continue_trip.html.bak_liveStop_bridge_fix, android_app/app/src/main/python/templates/continue_trip.html.bak_liveStop_bridge_fix, apk_payload/templates/continue_trip.html.bak_liveStop_bridge_fix |
| continue_trip.html.bak_live_bag_detail_20260512_1313 | 3 | AYNI | templates/continue_trip.html.bak_live_bag_detail_20260512_1313, android_app/app/src/main/python/templates/continue_trip.html.bak_live_bag_detail_20260512_1313, apk_payload/templates/continue_trip.html.bak_live_bag_detail_20260512_1313 |
| continue_trip.html.bak_live_clock_fix | 3 | AYNI | templates/continue_trip.html.bak_live_clock_fix, android_app/app/src/main/python/templates/continue_trip.html.bak_live_clock_fix, apk_payload/templates/continue_trip.html.bak_live_clock_fix |
| continue_trip.html.bak_live_clock_seconds | 3 | AYNI | templates/continue_trip.html.bak_live_clock_seconds, android_app/app/src/main/python/templates/continue_trip.html.bak_live_clock_seconds, apk_payload/templates/continue_trip.html.bak_live_clock_seconds |
| continue_trip.html.bak_live_final_visual_match | 3 | AYNI | templates/continue_trip.html.bak_live_final_visual_match, android_app/app/src/main/python/templates/continue_trip.html.bak_live_final_visual_match, apk_payload/templates/continue_trip.html.bak_live_final_visual_match |
| continue_trip.html.bak_live_gender_color_20260512_2030 | 3 | AYNI | templates/continue_trip.html.bak_live_gender_color_20260512_2030, android_app/app/src/main/python/templates/continue_trip.html.bak_live_gender_color_20260512_2030, apk_payload/templates/continue_trip.html.bak_live_gender_color_20260512_2030 |
| continue_trip.html.bak_live_gps_speed | 3 | AYNI | templates/continue_trip.html.bak_live_gps_speed, android_app/app/src/main/python/templates/continue_trip.html.bak_live_gps_speed, apk_payload/templates/continue_trip.html.bak_live_gps_speed |
| continue_trip.html.bak_live_hero_brightness | 3 | AYNI | templates/continue_trip.html.bak_live_hero_brightness, android_app/app/src/main/python/templates/continue_trip.html.bak_live_hero_brightness, apk_payload/templates/continue_trip.html.bak_live_hero_brightness |
| continue_trip.html.bak_live_hero_bus_html_insert | 3 | AYNI | templates/continue_trip.html.bak_live_hero_bus_html_insert, android_app/app/src/main/python/templates/continue_trip.html.bak_live_hero_bus_html_insert, apk_payload/templates/continue_trip.html.bak_live_hero_bus_html_insert |
| continue_trip.html.bak_live_hero_bus_img | 3 | AYNI | templates/continue_trip.html.bak_live_hero_bus_img, android_app/app/src/main/python/templates/continue_trip.html.bak_live_hero_bus_img, apk_payload/templates/continue_trip.html.bak_live_hero_bus_img |
| continue_trip.html.bak_live_hero_bus_insert | 3 | AYNI | templates/continue_trip.html.bak_live_hero_bus_insert, android_app/app/src/main/python/templates/continue_trip.html.bak_live_hero_bus_insert, apk_payload/templates/continue_trip.html.bak_live_hero_bus_insert |
| continue_trip.html.bak_live_hero_title_size | 3 | AYNI | templates/continue_trip.html.bak_live_hero_title_size, android_app/app/src/main/python/templates/continue_trip.html.bak_live_hero_title_size, apk_payload/templates/continue_trip.html.bak_live_hero_title_size |
| continue_trip.html.bak_live_hero_title_smaller | 3 | AYNI | templates/continue_trip.html.bak_live_hero_title_smaller, android_app/app/src/main/python/templates/continue_trip.html.bak_live_hero_title_smaller, apk_payload/templates/continue_trip.html.bak_live_hero_title_smaller |
| continue_trip.html.bak_live_label_fix | 3 | AYNI | templates/continue_trip.html.bak_live_label_fix, android_app/app/src/main/python/templates/continue_trip.html.bak_live_label_fix, apk_payload/templates/continue_trip.html.bak_live_label_fix |
| continue_trip.html.bak_live_map_link_20260513_0100 | 3 | AYNI | templates/continue_trip.html.bak_live_map_link_20260513_0100, android_app/app/src/main/python/templates/continue_trip.html.bak_live_map_link_20260513_0100, apk_payload/templates/continue_trip.html.bak_live_map_link_20260513_0100 |
| continue_trip.html.bak_live_operation_panel | 3 | AYNI | templates/continue_trip.html.bak_live_operation_panel, android_app/app/src/main/python/templates/continue_trip.html.bak_live_operation_panel, apk_payload/templates/continue_trip.html.bak_live_operation_panel |
| continue_trip.html.bak_live_runtime_sync | 3 | AYNI | templates/continue_trip.html.bak_live_runtime_sync, android_app/app/src/main/python/templates/continue_trip.html.bak_live_runtime_sync, apk_payload/templates/continue_trip.html.bak_live_runtime_sync |
| continue_trip.html.bak_live_seat_offload_20260512_1256 | 3 | AYNI | templates/continue_trip.html.bak_live_seat_offload_20260512_1256, android_app/app/src/main/python/templates/continue_trip.html.bak_live_seat_offload_20260512_1256, apk_payload/templates/continue_trip.html.bak_live_seat_offload_20260512_1256 |
| continue_trip.html.bak_live_stop_bulk_offload_20260512_1309 | 3 | AYNI | templates/continue_trip.html.bak_live_stop_bulk_offload_20260512_1309, android_app/app/src/main/python/templates/continue_trip.html.bak_live_stop_bulk_offload_20260512_1309, apk_payload/templates/continue_trip.html.bak_live_stop_bulk_offload_20260512_1309 |
| continue_trip.html.bak_live_stop_sheet_20260512_1231 | 3 | AYNI | templates/continue_trip.html.bak_live_stop_sheet_20260512_1231, android_app/app/src/main/python/templates/continue_trip.html.bak_live_stop_sheet_20260512_1231, apk_payload/templates/continue_trip.html.bak_live_stop_sheet_20260512_1231 |
| continue_trip.html.bak_live_stop_summary_20260512_2224 | 3 | AYNI | templates/continue_trip.html.bak_live_stop_summary_20260512_2224, android_app/app/src/main/python/templates/continue_trip.html.bak_live_stop_summary_20260512_2224, apk_payload/templates/continue_trip.html.bak_live_stop_summary_20260512_2224 |
| continue_trip.html.bak_live_ui_final | 3 | AYNI | templates/continue_trip.html.bak_live_ui_final, android_app/app/src/main/python/templates/continue_trip.html.bak_live_ui_final, apk_payload/templates/continue_trip.html.bak_live_ui_final |
| continue_trip.html.bak_metric_hint_polish_20260512_1353 | 3 | AYNI | templates/continue_trip.html.bak_metric_hint_polish_20260512_1353, android_app/app/src/main/python/templates/continue_trip.html.bak_metric_hint_polish_20260512_1353, apk_payload/templates/continue_trip.html.bak_metric_hint_polish_20260512_1353 |
| continue_trip.html.bak_mockup_to_code | 3 | AYNI | templates/continue_trip.html.bak_mockup_to_code, android_app/app/src/main/python/templates/continue_trip.html.bak_mockup_to_code, apk_payload/templates/continue_trip.html.bak_mockup_to_code |
| continue_trip.html.bak_modal_premium_v2 | 3 | AYNI | templates/continue_trip.html.bak_modal_premium_v2, android_app/app/src/main/python/templates/continue_trip.html.bak_modal_premium_v2, apk_payload/templates/continue_trip.html.bak_modal_premium_v2 |

## 8) Android/Web Gölge Kopya Kontrolü
Android içindeki kopya ile ana web kopyası aynı mı farklı mı?
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
| modules/ai_panel.py | AYNI | modules/ai_panel.py | android_app/app/src/main/python/modules/ai_panel.py |
| modules/backup_panel.py | AYNI | modules/backup_panel.py | android_app/app/src/main/python/modules/backup_panel.py |
| modules/bags/__init__.py | AYNI | modules/bags/__init__.py | android_app/app/src/main/python/modules/bags/__init__.py |
| modules/cash_panel.py | AYNI | modules/cash_panel.py | android_app/app/src/main/python/modules/cash_panel.py |
| modules/consignments_panel.py | AYNI | modules/consignments_panel.py | android_app/app/src/main/python/modules/consignments_panel.py |
| modules/coords_panel.py | AYNI | modules/coords_panel.py | android_app/app/src/main/python/modules/coords_panel.py |
| modules/reports_panel.py | AYNI | modules/reports_panel.py | android_app/app/src/main/python/modules/reports_panel.py |
| modules/reports_panel.py.bak_events_sums_fix | AYNI | modules/reports_panel.py.bak_events_sums_fix | android_app/app/src/main/python/modules/reports_panel.py.bak_events_sums_fix |
| modules/routes_panel.py | AYNI | modules/routes_panel.py | android_app/app/src/main/python/modules/routes_panel.py |
| modules/seats_panel.py | AYNI | modules/seats_panel.py | android_app/app/src/main/python/modules/seats_panel.py |
| modules/seats_panel.py.bak_seat_destination_change_20260520_231815 | AYNI | modules/seats_panel.py.bak_seat_destination_change_20260520_231815 | android_app/app/src/main/python/modules/seats_panel.py.bak_seat_destination_change_20260520_231815 |
| modules/settings_panel.py | AYNI | modules/settings_panel.py | android_app/app/src/main/python/modules/settings_panel.py |
| modules/subscription_panel.py | AYNI | modules/subscription_panel.py | android_app/app/src/main/python/modules/subscription_panel.py |
| modules/trip_report_builder.py | AYNI | modules/trip_report_builder.py | android_app/app/src/main/python/modules/trip_report_builder.py |
| modules/trip_report_builder.py.bak_report_change_payload_20260520_233720 | AYNI | modules/trip_report_builder.py.bak_report_change_payload_20260520_233720 | android_app/app/src/main/python/modules/trip_report_builder.py.bak_report_change_payload_20260520_233720 |
| modules/trip_report_builder.py.bak_report_destination_change_20260520_232729 | AYNI | modules/trip_report_builder.py.bak_report_destination_change_20260520_232729 | android_app/app/src/main/python/modules/trip_report_builder.py.bak_report_destination_change_20260520_232729 |
| schema.sql | AYNI | schema.sql | android_app/app/src/main/python/schema.sql |
| speedlimit.py | AYNI | speedlimit.py | android_app/app/src/main/python/speedlimit.py |
| static/app.js | AYNI | static/app.js | android_app/app/src/main/python/static/app.js |
| static/continue/continue_bag_emanet.js | AYNI | static/continue/continue_bag_emanet.js | android_app/app/src/main/python/static/continue/continue_bag_emanet.js |
| static/continue/continue_flow_refresh.js | AYNI | static/continue/continue_flow_refresh.js | android_app/app/src/main/python/static/continue/continue_flow_refresh.js |
| static/continue/continue_flow_refresh.js.bak_km_distance_20260523_134050 | AYNI | static/continue/continue_flow_refresh.js.bak_km_distance_20260523_134050 | android_app/app/src/main/python/static/continue/continue_flow_refresh.js.bak_km_distance_20260523_134050 |
| static/continue/continue_flow_refresh.js.bak_no_flicker_20260523_130647 | AYNI | static/continue/continue_flow_refresh.js.bak_no_flicker_20260523_130647 | android_app/app/src/main/python/static/continue/continue_flow_refresh.js.bak_no_flicker_20260523_130647 |
| static/continue/continue_live_diagnostics.js | AYNI | static/continue/continue_live_diagnostics.js | android_app/app/src/main/python/static/continue/continue_live_diagnostics.js |
| static/continue/continue_live_diagnostics.js.bak_collapsible_20260523_133213 | AYNI | static/continue/continue_live_diagnostics.js.bak_collapsible_20260523_133213 | android_app/app/src/main/python/static/continue/continue_live_diagnostics.js.bak_collapsible_20260523_133213 |
| static/continue/continue_live_diagnostics.js.bak_name_km_20260523_134050 | AYNI | static/continue/continue_live_diagnostics.js.bak_name_km_20260523_134050 | android_app/app/src/main/python/static/continue/continue_live_diagnostics.js.bak_name_km_20260523_134050 |
| static/continue/continue_trip.css | AYNI | static/continue/continue_trip.css | android_app/app/src/main/python/static/continue/continue_trip.css |
| static/continue/continue_trip.css.bak_parts_20260523_144047 | AYNI | static/continue/continue_trip.css.bak_parts_20260523_144047 | android_app/app/src/main/python/static/continue/continue_trip.css.bak_parts_20260523_144047 |
| static/continue/continue_trip_core.js | AYNI | static/continue/continue_trip_core.js | android_app/app/src/main/python/static/continue/continue_trip_core.js |
| static/continue/continue_trip_ui.js | AYNI | static/continue/continue_trip_ui.js | android_app/app/src/main/python/static/continue/continue_trip_ui.js |
| static/continue/css_parts/00-base-legacy.css | AYNI | static/continue/css_parts/00-base-legacy.css | android_app/app/src/main/python/static/continue/css_parts/00-base-legacy.css |
| static/continue/css_parts/10-compact-timeline-hero.css | AYNI | static/continue/css_parts/10-compact-timeline-hero.css | android_app/app/src/main/python/static/continue/css_parts/10-compact-timeline-hero.css |
| static/continue/css_parts/20-live-stop-sheet-base.css | AYNI | static/continue/css_parts/20-live-stop-sheet-base.css | android_app/app/src/main/python/static/continue/css_parts/20-live-stop-sheet-base.css |
| static/continue/css_parts/30-sheet-bag-photo.css | AYNI | static/continue/css_parts/30-sheet-bag-photo.css | android_app/app/src/main/python/static/continue/css_parts/30-sheet-bag-photo.css |
| static/continue/css_parts/40-cargo-gender-summary.css | AYNI | static/continue/css_parts/40-cargo-gender-summary.css | android_app/app/src/main/python/static/continue/css_parts/40-cargo-gender-summary.css |
| static/continue/css_parts/50-live-v2-top-glow.css | AYNI | static/continue/css_parts/50-live-v2-top-glow.css | android_app/app/src/main/python/static/continue/css_parts/50-live-v2-top-glow.css |
| static/continue/css_parts/60-live-diagnostics.css | AYNI | static/continue/css_parts/60-live-diagnostics.css | android_app/app/src/main/python/static/continue/css_parts/60-live-diagnostics.css |
| static/data/route_profile_segments.json | AYNI | static/data/route_profile_segments.json | android_app/app/src/main/python/static/data/route_profile_segments.json |
| static/data/route_segments.json | AYNI | static/data/route_segments.json | android_app/app/src/main/python/static/data/route_segments.json |
| static/data/route_segments.json.bak_accept_alibeykoy_gebze_yss_20260518_000238 | AYNI | static/data/route_segments.json.bak_accept_alibeykoy_gebze_yss_20260518_000238 | android_app/app/src/main/python/static/data/route_segments.json.bak_accept_alibeykoy_gebze_yss_20260518_000238 |
| static/data/route_segments.json.bak_akhisar_balikesir_d565_20260517_103807 | AYNI | static/data/route_segments.json.bak_akhisar_balikesir_d565_20260517_103807 | android_app/app/src/main/python/static/data/route_segments.json.bak_akhisar_balikesir_d565_20260517_103807 |
| static/data/route_segments.json.bak_ant_ist_20260517_094613 | AYNI | static/data/route_segments.json.bak_ant_ist_20260517_094613 | android_app/app/src/main/python/static/data/route_segments.json.bak_ant_ist_20260517_094613 |
| static/data/route_segments.json.bak_before_rollback_accept_alibeykoy_gebze_yss_20260518_001320 | AYNI | static/data/route_segments.json.bak_before_rollback_accept_alibeykoy_gebze_yss_20260518_001320 | android_app/app/src/main/python/static/data/route_segments.json.bak_before_rollback_accept_alibeykoy_gebze_yss_20260518_001320 |
| static/data/route_segments.json.bak_before_rollback_salihli_akhisar_via_20260517_100817 | AYNI | static/data/route_segments.json.bak_before_rollback_salihli_akhisar_via_20260517_100817 | android_app/app/src/main/python/static/data/route_segments.json.bak_before_rollback_salihli_akhisar_via_20260517_100817 |
| static/data/route_segments.json.bak_before_rollback_salihli_correct_turn_20260517_102155 | AYNI | static/data/route_segments.json.bak_before_rollback_salihli_correct_turn_20260517_102155 | android_app/app/src/main/python/static/data/route_segments.json.bak_before_rollback_salihli_correct_turn_20260517_102155 |
| static/data/route_segments.json.bak_before_rollback_salihli_pin_d555_20260517_101430 | AYNI | static/data/route_segments.json.bak_before_rollback_salihli_pin_d555_20260517_101430 | android_app/app/src/main/python/static/data/route_segments.json.bak_before_rollback_salihli_pin_d555_20260517_101430 |
| static/data/route_segments.json.bak_before_rollback_tuzla_segments_20260517_111533 | AYNI | static/data/route_segments.json.bak_before_rollback_tuzla_segments_20260517_111533 | android_app/app/src/main/python/static/data/route_segments.json.bak_before_rollback_tuzla_segments_20260517_111533 |
| static/data/route_segments.json.bak_build_denizli_istanbul_20260520_122020 | AYNI | static/data/route_segments.json.bak_build_denizli_istanbul_20260520_122020 | android_app/app/src/main/python/static/data/route_segments.json.bak_build_denizli_istanbul_20260520_122020 |
| static/data/route_segments.json.bak_denizli_korkuteli_segments_20260517_144319 | AYNI | static/data/route_segments.json.bak_denizli_korkuteli_segments_20260517_144319 | android_app/app/src/main/python/static/data/route_segments.json.bak_denizli_korkuteli_segments_20260517_144319 |
| static/data/route_segments.json.bak_fix_alibeykoy_gebze_short_yss_20260517_235959 | AYNI | static/data/route_segments.json.bak_fix_alibeykoy_gebze_short_yss_20260517_235959 | android_app/app/src/main/python/static/data/route_segments.json.bak_fix_alibeykoy_gebze_short_yss_20260517_235959 |
| static/data/route_segments.json.bak_force_ist_ant_yss_route_20260517_234658 | AYNI | static/data/route_segments.json.bak_force_ist_ant_yss_route_20260517_234658 | android_app/app/src/main/python/static/data/route_segments.json.bak_force_ist_ant_yss_route_20260517_234658 |
| static/data/route_segments.json.bak_ist_ant_alibeykoy_gebze_yss_extra2_20260517_235604 | AYNI | static/data/route_segments.json.bak_ist_ant_alibeykoy_gebze_yss_extra2_20260517_235604 | android_app/app/src/main/python/static/data/route_segments.json.bak_ist_ant_alibeykoy_gebze_yss_extra2_20260517_235604 |
| static/data/route_segments.json.bak_ist_ant_alibeykoy_gebze_yss_extra_20260517_235252 | AYNI | static/data/route_segments.json.bak_ist_ant_alibeykoy_gebze_yss_extra_20260517_235252 | android_app/app/src/main/python/static/data/route_segments.json.bak_ist_ant_alibeykoy_gebze_yss_extra_20260517_235252 |
| static/data/route_segments.json.bak_ist_ant_manisa_route_20260517_233207 | AYNI | static/data/route_segments.json.bak_ist_ant_manisa_route_20260517_233207 | android_app/app/src/main/python/static/data/route_segments.json.bak_ist_ant_manisa_route_20260517_233207 |
| static/data/route_segments.json.bak_ist_ant_refresh_segments_20260517_144738 | AYNI | static/data/route_segments.json.bak_ist_ant_refresh_segments_20260517_144738 | android_app/app/src/main/python/static/data/route_segments.json.bak_ist_ant_refresh_segments_20260517_144738 |
| static/data/route_segments.json.bak_istanbul_antalya_yss_20260517_141115 | AYNI | static/data/route_segments.json.bak_istanbul_antalya_yss_20260517_141115 | android_app/app/src/main/python/static/data/route_segments.json.bak_istanbul_antalya_yss_20260517_141115 |
| static/data/route_segments.json.bak_korkuteli_elmali_segments_20260517_143312 | AYNI | static/data/route_segments.json.bak_korkuteli_elmali_segments_20260517_143312 | android_app/app/src/main/python/static/data/route_segments.json.bak_korkuteli_elmali_segments_20260517_143312 |
| static/data/route_segments.json.bak_rebuild_denizli_istanbul_20260520_122635 | AYNI | static/data/route_segments.json.bak_rebuild_denizli_istanbul_20260520_122635 | android_app/app/src/main/python/static/data/route_segments.json.bak_rebuild_denizli_istanbul_20260520_122635 |
| static/data/route_segments.json.bak_refresh_new_coords_segments_20260517_143857 | AYNI | static/data/route_segments.json.bak_refresh_new_coords_segments_20260517_143857 | android_app/app/src/main/python/static/data/route_segments.json.bak_refresh_new_coords_segments_20260517_143857 |
| static/data/route_segments.json.bak_restore_denizli_istanbul_from_reverse_20260521_000121 | AYNI | static/data/route_segments.json.bak_restore_denizli_istanbul_from_reverse_20260521_000121 | android_app/app/src/main/python/static/data/route_segments.json.bak_restore_denizli_istanbul_from_reverse_20260521_000121 |
| static/data/route_segments.json.bak_reverse_ist_ant_20260517_140145 | AYNI | static/data/route_segments.json.bak_reverse_ist_ant_20260517_140145 | android_app/app/src/main/python/static/data/route_segments.json.bak_reverse_ist_ant_20260517_140145 |
| static/data/route_segments.json.bak_reverse_to_istanbul_denizli_20260520_123746 | AYNI | static/data/route_segments.json.bak_reverse_to_istanbul_denizli_20260520_123746 | android_app/app/src/main/python/static/data/route_segments.json.bak_reverse_to_istanbul_denizli_20260520_123746 |
| static/data/route_segments.json.bak_salihli_akhisar_via_d555_20260517_100121 | AYNI | static/data/route_segments.json.bak_salihli_akhisar_via_d555_20260517_100121 | android_app/app/src/main/python/static/data/route_segments.json.bak_salihli_akhisar_via_d555_20260517_100121 |
| static/data/route_segments.json.bak_salihli_akhisar_via_points_20260517_100608 | AYNI | static/data/route_segments.json.bak_salihli_akhisar_via_points_20260517_100608 | android_app/app/src/main/python/static/data/route_segments.json.bak_salihli_akhisar_via_points_20260517_100608 |
| static/data/route_segments.json.bak_salihli_correct_turn_20260517_101854 | AYNI | static/data/route_segments.json.bak_salihli_correct_turn_20260517_101854 | android_app/app/src/main/python/static/data/route_segments.json.bak_salihli_correct_turn_20260517_101854 |
| static/data/route_segments.json.bak_salihli_pin_d555_fix_20260517_101253 | AYNI | static/data/route_segments.json.bak_salihli_pin_d555_fix_20260517_101253 | android_app/app/src/main/python/static/data/route_segments.json.bak_salihli_pin_d555_fix_20260517_101253 |
| static/data/route_segments.json.bak_tuzla_refresh_20260517_112331 | AYNI | static/data/route_segments.json.bak_tuzla_refresh_20260517_112331 | android_app/app/src/main/python/static/data/route_segments.json.bak_tuzla_refresh_20260517_112331 |
| static/data/route_segments.json.bak_tuzla_segments_redraw_fix_20260517_112456 | AYNI | static/data/route_segments.json.bak_tuzla_segments_redraw_fix_20260517_112456 | android_app/app/src/main/python/static/data/route_segments.json.bak_tuzla_segments_redraw_fix_20260517_112456 |
| static/img/drive-mode-card.png | AYNI | static/img/drive-mode-card.png | android_app/app/src/main/python/static/img/drive-mode-card.png |
| static/img/home-bus-card-final.png | AYNI | static/img/home-bus-card-final.png | android_app/app/src/main/python/static/img/home-bus-card-final.png |
| static/img/home-bus-card.jpg | AYNI | static/img/home-bus-card.jpg | android_app/app/src/main/python/static/img/home-bus-card.jpg |
| static/img/home-seat-card.jpg | AYNI | static/img/home-seat-card.jpg | android_app/app/src/main/python/static/img/home-seat-card.jpg |
| static/img/live-hero-bus.png | AYNI | static/img/live-hero-bus.png | android_app/app/src/main/python/static/img/live-hero-bus.png |
| static/img/menu-bus-card.png | AYNI | static/img/menu-bus-card.png | android_app/app/src/main/python/static/img/menu-bus-card.png |
| static/img/menu-seat-card.png | AYNI | static/img/menu-seat-card.png | android_app/app/src/main/python/static/img/menu-seat-card.png |
| static/img/onboarding/README.txt | AYNI | static/img/onboarding/README.txt | android_app/app/src/main/python/static/img/onboarding/README.txt |
| static/img/onboarding/slides/onboarding_1.png | AYNI | static/img/onboarding/slides/onboarding_1.png | android_app/app/src/main/python/static/img/onboarding/slides/onboarding_1.png |
| static/img/onboarding/slides/onboarding_2.png | AYNI | static/img/onboarding/slides/onboarding_2.png | android_app/app/src/main/python/static/img/onboarding/slides/onboarding_2.png |
| static/img/onboarding/slides/onboarding_3.png | AYNI | static/img/onboarding/slides/onboarding_3.png | android_app/app/src/main/python/static/img/onboarding/slides/onboarding_3.png |
| static/img/onboarding/slides/onboarding_4.png | AYNI | static/img/onboarding/slides/onboarding_4.png | android_app/app/src/main/python/static/img/onboarding/slides/onboarding_4.png |
| static/img/onboarding/slides/onboarding_5.png | AYNI | static/img/onboarding/slides/onboarding_5.png | android_app/app/src/main/python/static/img/onboarding/slides/onboarding_5.png |
| static/img/onboarding/slides/onboarding_6.png | AYNI | static/img/onboarding/slides/onboarding_6.png | android_app/app/src/main/python/static/img/onboarding/slides/onboarding_6.png |
| static/img/onboarding/slides/onboarding_7.png | AYNI | static/img/onboarding/slides/onboarding_7.png | android_app/app/src/main/python/static/img/onboarding/slides/onboarding_7.png |
| static/img/rehber-cinema-main.png | AYNI | static/img/rehber-cinema-main.png | android_app/app/src/main/python/static/img/rehber-cinema-main.png |
| static/img/rehber-durak-akisi-card.png | AYNI | static/img/rehber-durak-akisi-card.png | android_app/app/src/main/python/static/img/rehber-durak-akisi-card.png |
| static/img/rehber-hesap-card.png | AYNI | static/img/rehber-hesap-card.png | android_app/app/src/main/python/static/img/rehber-hesap-card.png |
| static/img/rehber-promo-main.png | AYNI | static/img/rehber-promo-main.png | android_app/app/src/main/python/static/img/rehber-promo-main.png |
| static/img/rehber-seat-plan-card.png | AYNI | static/img/rehber-seat-plan-card.png | android_app/app/src/main/python/static/img/rehber-seat-plan-card.png |
| static/img/rehber-voice-command-card.png | AYNI | static/img/rehber-voice-command-card.png | android_app/app/src/main/python/static/img/rehber-voice-command-card.png |
| static/img/seat-card-final.png | AYNI | static/img/seat-card-final.png | android_app/app/src/main/python/static/img/seat-card-final.png |
| static/img/seat-card.jpg | AYNI | static/img/seat-card.jpg | android_app/app/src/main/python/static/img/seat-card.jpg |
| static/live_map/muavin_live_map_extra.css | AYNI | static/live_map/muavin_live_map_extra.css | android_app/app/src/main/python/static/live_map/muavin_live_map_extra.css |
| static/live_map/muavin_live_map_extra.css.bak_bottom_final_20260513_164512 | AYNI | static/live_map/muavin_live_map_extra.css.bak_bottom_final_20260513_164512 | android_app/app/src/main/python/static/live_map/muavin_live_map_extra.css.bak_bottom_final_20260513_164512 |
| static/live_map/muavin_live_map_extra.css.bak_clean_dock_visible_20260513_185554 | AYNI | static/live_map/muavin_live_map_extra.css.bak_clean_dock_visible_20260513_185554 | android_app/app/src/main/python/static/live_map/muavin_live_map_extra.css.bak_clean_dock_visible_20260513_185554 |
| static/live_map/muavin_live_map_extra.css.bak_clean_fullscreen_20260513_185236 | AYNI | static/live_map/muavin_live_map_extra.css.bak_clean_fullscreen_20260513_185236 | android_app/app/src/main/python/static/live_map/muavin_live_map_extra.css.bak_clean_fullscreen_20260513_185236 |
| static/live_map/muavin_live_map_extra.css.bak_clean_hide_km_20260513_190426 | AYNI | static/live_map/muavin_live_map_extra.css.bak_clean_hide_km_20260513_190426 | android_app/app/src/main/python/static/live_map/muavin_live_map_extra.css.bak_clean_hide_km_20260513_190426 |
| static/live_map/muavin_live_map_extra.css.bak_clean_location_visible_20260513_190610 | AYNI | static/live_map/muavin_live_map_extra.css.bak_clean_location_visible_20260513_190610 | android_app/app/src/main/python/static/live_map/muavin_live_map_extra.css.bak_clean_location_visible_20260513_190610 |
| static/live_map/muavin_live_map_extra.css.bak_clean_speed_visible_20260513_190933 | AYNI | static/live_map/muavin_live_map_extra.css.bak_clean_speed_visible_20260513_190933 | android_app/app/src/main/python/static/live_map/muavin_live_map_extra.css.bak_clean_speed_visible_20260513_190933 |
| static/live_map/muavin_live_map_extra.css.bak_clean_start_20260513_185013 | AYNI | static/live_map/muavin_live_map_extra.css.bak_clean_start_20260513_185013 | android_app/app/src/main/python/static/live_map/muavin_live_map_extra.css.bak_clean_start_20260513_185013 |
| static/live_map/muavin_live_map_extra.css.bak_map_ui_final_20260513_165054 | AYNI | static/live_map/muavin_live_map_extra.css.bak_map_ui_final_20260513_165054 | android_app/app/src/main/python/static/live_map/muavin_live_map_extra.css.bak_map_ui_final_20260513_165054 |
| static/live_map/muavin_live_map_extra.css.bak_next_ops_bubble_20260513_174004 | AYNI | static/live_map/muavin_live_map_extra.css.bak_next_ops_bubble_20260513_174004 | android_app/app/src/main/python/static/live_map/muavin_live_map_extra.css.bak_next_ops_bubble_20260513_174004 |
| static/live_map/muavin_live_map_extra.css.bak_next_ops_drag_20260513_174215 | AYNI | static/live_map/muavin_live_map_extra.css.bak_next_ops_drag_20260513_174215 | android_app/app/src/main/python/static/live_map/muavin_live_map_extra.css.bak_next_ops_drag_20260513_174215 |

## 9) Backup / Eski / Test / Audit Dosya Adayları
Bunlar otomatik silinmeyecek. Sadece temizlik adayı olarak listeleniyor.
| Dosya | Byte | Satır |
| --- | --- | --- |
| android_app/app/src/main/java/com/muavinasistani/app/MainActivity.java.bak_bind_printbridge_real | 17612 | None |
| android_app/app/src/main/java/com/muavinasistani/app/MainActivity.java.bak_geolocation_patch | 17686 | None |
| android_app/app/src/main/java/com/muavinasistani/app/MainActivity.java.bak_port_guard_20260530_104842 | 17686 | None |
| android_app/app/src/main/java/com/muavinasistani/app/MainActivity.java.bak_print_bridge | 16274 | None |
| android_app/app/src/main/java/com/muavinasistani/app/MainActivity.java.bak_print_debug | 17468 | None |
| android_app/app/src/main/java/com/muavinasistani/app/MainActivity.java.bak_tts_bridge | 12850 | None |
| android_app/app/src/main/java/com/muavinasistani/app/MainActivity.java.bak_webview_scheme_fix | 14473 | None |
| android_app/app/src/main/python/android_server.py.bak_port_guard_20260530_104842 | 2216 | None |
| android_app/app/src/main/python/app.py.bak_continue_route_sync_20260523_143011 | 136113 | None |
| android_app/app/src/main/python/app.py.bak_sync_20260520_113916 | 134501 | None |
| android_app/app/src/main/python/modules/backup_panel.py | 11494 | 342 |
| android_app/app/src/main/python/modules/reports_panel.py.bak_events_sums_fix | 4791 | None |
| android_app/app/src/main/python/modules/seats_panel.py.bak_seat_destination_change_20260520_231815 | 21609 | None |
| android_app/app/src/main/python/modules/trip_report_builder.py.bak_report_change_payload_20260520_233720 | 11334 | None |
| android_app/app/src/main/python/modules/trip_report_builder.py.bak_report_destination_change_20260520_232729 | 10973 | None |
| android_app/app/src/main/python/seed/db.sqlite3.bak_coords_sync_20260518_184401 | 483328 | None |
| android_app/app/src/main/python/seed/db.sqlite3.bak_route_full_sync_20260518_191613 | 483328 | None |
| android_app/app/src/main/python/static/continue/continue_bag_emanet.js.bak_sync_continue_20260523_142710 | 3525 | None |
| android_app/app/src/main/python/static/continue/continue_flow_refresh.js.bak_km_distance_20260523_134050 | 8724 | None |
| android_app/app/src/main/python/static/continue/continue_flow_refresh.js.bak_no_flicker_20260523_130647 | 7655 | None |
| android_app/app/src/main/python/static/continue/continue_flow_refresh.js.bak_sync_continue_20260523_142710 | 10839 | None |
| android_app/app/src/main/python/static/continue/continue_live_diagnostics.js.bak_collapsible_20260523_133213 | 6169 | None |
| android_app/app/src/main/python/static/continue/continue_live_diagnostics.js.bak_name_km_20260523_134050 | 7941 | None |
| android_app/app/src/main/python/static/continue/continue_live_diagnostics.js.bak_sync_continue_20260523_142710 | 7939 | None |
| android_app/app/src/main/python/static/continue/continue_trip.css.bak_diag_collapsible_20260523_133213 | 72215 | None |
| android_app/app/src/main/python/static/continue/continue_trip.css.bak_live_diag_20260523_132945 | 70077 | None |
| android_app/app/src/main/python/static/continue/continue_trip.css.bak_map_overlay_20260523_140732 | 73054 | None |
| android_app/app/src/main/python/static/continue/continue_trip.css.bak_parts_20260523_144047 | 84753 | None |
| android_app/app/src/main/python/static/continue/continue_trip.css.bak_sync_continue_20260523_142710 | 73054 | None |
| android_app/app/src/main/python/static/continue/continue_trip_core.js.bak_bag_emanet_clean_20260523_130105 | 56647 | None |
| android_app/app/src/main/python/static/continue/continue_trip_core.js.bak_sync_continue_20260523_142710 | 55364 | None |
| android_app/app/src/main/python/static/continue/continue_trip_ui.js.bak_sync_continue_20260523_142710 | 4133 | None |
| android_app/app/src/main/python/static/data/route_segments.json.bak_accept_alibeykoy_gebze_yss_20260518_000238 | 3544583 | None |
| android_app/app/src/main/python/static/data/route_segments.json.bak_akhisar_balikesir_d565_20260517_103807 | 1771202 | None |
| android_app/app/src/main/python/static/data/route_segments.json.bak_ant_ist_20260517_094613 | 481930 | None |
| android_app/app/src/main/python/static/data/route_segments.json.bak_before_rollback_accept_alibeykoy_gebze_yss_20260518_001320 | 3132577 | None |
| android_app/app/src/main/python/static/data/route_segments.json.bak_before_rollback_salihli_akhisar_via_20260517_100817 | 1771210 | None |
| android_app/app/src/main/python/static/data/route_segments.json.bak_before_rollback_salihli_correct_turn_20260517_102155 | 1767779 | None |
| android_app/app/src/main/python/static/data/route_segments.json.bak_before_rollback_salihli_pin_d555_20260517_101430 | 1767776 | None |
| android_app/app/src/main/python/static/data/route_segments.json.bak_before_rollback_tuzla_segments_20260517_111533 | 790747 | None |
| android_app/app/src/main/python/static/data/route_segments.json.bak_build_denizli_istanbul_20260520_122020 | 3544583 | None |
| android_app/app/src/main/python/static/data/route_segments.json.bak_denizli_korkuteli_segments_20260517_144319 | 2368645 | None |
| android_app/app/src/main/python/static/data/route_segments.json.bak_fix_alibeykoy_gebze_short_yss_20260517_235959 | 3544583 | None |
| android_app/app/src/main/python/static/data/route_segments.json.bak_force_ist_ant_yss_route_20260517_234658 | 2362611 | None |
| android_app/app/src/main/python/static/data/route_segments.json.bak_geom_sync_20260518_192438 | 257477 | None |
| android_app/app/src/main/python/static/data/route_segments.json.bak_ist_ant_alibeykoy_gebze_yss_extra2_20260517_235604 | 3537181 | None |
| android_app/app/src/main/python/static/data/route_segments.json.bak_ist_ant_alibeykoy_gebze_yss_extra_20260517_235252 | 3463743 | None |
| android_app/app/src/main/python/static/data/route_segments.json.bak_ist_ant_manisa_route_20260517_233207 | 2480965 | None |
| android_app/app/src/main/python/static/data/route_segments.json.bak_ist_ant_refresh_segments_20260517_144738 | 2368645 | None |
| android_app/app/src/main/python/static/data/route_segments.json.bak_istanbul_antalya_yss_20260517_141115 | 2441086 | None |
| android_app/app/src/main/python/static/data/route_segments.json.bak_korkuteli_elmali_segments_20260517_143312 | 2368645 | None |
| android_app/app/src/main/python/static/data/route_segments.json.bak_rebuild_denizli_istanbul_20260520_122635 | 1860939 | None |
| android_app/app/src/main/python/static/data/route_segments.json.bak_refresh_new_coords_segments_20260517_143857 | 2368645 | None |
| android_app/app/src/main/python/static/data/route_segments.json.bak_restore_denizli_istanbul_from_reverse_20260521_000121 | 2135441 | None |
| android_app/app/src/main/python/static/data/route_segments.json.bak_reverse_ist_ant_20260517_140145 | 1756223 | None |
| android_app/app/src/main/python/static/data/route_segments.json.bak_reverse_to_istanbul_denizli_20260520_123746 | 1859812 | None |
| android_app/app/src/main/python/static/data/route_segments.json.bak_salihli_akhisar_via_d555_20260517_100121 | 1767215 | None |
| android_app/app/src/main/python/static/data/route_segments.json.bak_salihli_akhisar_via_points_20260517_100608 | 1771202 | None |
| android_app/app/src/main/python/static/data/route_segments.json.bak_salihli_correct_turn_20260517_101854 | 1771202 | None |
| android_app/app/src/main/python/static/data/route_segments.json.bak_salihli_pin_d555_fix_20260517_101253 | 1771202 | None |
| android_app/app/src/main/python/static/data/route_segments.json.bak_tuzla_refresh_20260517_112331 | 1767425 | None |
| android_app/app/src/main/python/static/data/route_segments.json.bak_tuzla_segments_redraw_fix_20260517_112456 | 1767425 | None |
| android_app/app/src/main/python/static/live_map/muavin_live_map_extra.css.bak_bottom_final_20260513_164512 | 37340 | None |
| android_app/app/src/main/python/static/live_map/muavin_live_map_extra.css.bak_clean_dock_visible_20260513_185554 | 37653 | None |
| android_app/app/src/main/python/static/live_map/muavin_live_map_extra.css.bak_clean_fullscreen_20260513_185236 | 35789 | None |
| android_app/app/src/main/python/static/live_map/muavin_live_map_extra.css.bak_clean_hide_km_20260513_190426 | 39080 | None |
| android_app/app/src/main/python/static/live_map/muavin_live_map_extra.css.bak_clean_location_visible_20260513_190610 | 40242 | None |
| android_app/app/src/main/python/static/live_map/muavin_live_map_extra.css.bak_clean_speed_visible_20260513_190933 | 42042 | None |
| android_app/app/src/main/python/static/live_map/muavin_live_map_extra.css.bak_clean_start_20260513_185013 | 33506 | None |
| android_app/app/src/main/python/static/live_map/muavin_live_map_extra.css.bak_final_apk_20260513_192149 | 42465 | None |
| android_app/app/src/main/python/static/live_map/muavin_live_map_extra.css.bak_map_ui_final_20260513_165054 | 32648 | None |
| android_app/app/src/main/python/static/live_map/muavin_live_map_extra.css.bak_next_ops_bubble_20260513_174004 | 24071 | None |
| android_app/app/src/main/python/static/live_map/muavin_live_map_extra.css.bak_next_ops_drag_20260513_174215 | 28388 | None |
| android_app/app/src/main/python/static/live_map/muavin_live_map_extra.css.bak_next_ops_final_20260513_172822 | 17372 | None |
| android_app/app/src/main/python/static/live_map/muavin_live_map_extra.css.bak_next_ops_polish_20260513_173333 | 21527 | None |
| android_app/app/src/main/python/static/live_map/muavin_live_map_extra.css.bak_remove_compass_20260513_165759 | 16945 | None |
| android_app/app/src/main/python/static/live_map/muavin_live_map_extra.css.bak_remove_old_blue_v1_20260513_191843 | 44326 | None |
| android_app/app/src/main/python/static/live_map/muavin_live_map_extra.css.bak_small_buttons_20260513_174403 | 29079 | None |
| android_app/app/src/main/python/static/live_map/muavin_live_map_extra.js.bak_bottom_final_20260513_164512 | 77370 | None |
| android_app/app/src/main/python/static/live_map/muavin_live_map_extra.js.bak_button_bridge_20260523_141312 | 57832 | None |
| android_app/app/src/main/python/static/live_map/muavin_live_map_extra.js.bak_clean_start_20260513_185013 | 54832 | None |
| android_app/app/src/main/python/static/live_map/muavin_live_map_extra.js.bak_final_apk_20260513_192149 | 57832 | None |
| android_app/app/src/main/python/static/live_map/muavin_live_map_extra.js.bak_map_ui_final_20260513_165054 | 63896 | None |
| android_app/app/src/main/python/static/live_map/muavin_live_map_extra.js.bak_next_ops_drag_20260513_174215 | 48818 | None |
| android_app/app/src/main/python/static/live_map/muavin_live_map_extra.js.bak_next_ops_final_20260513_172822 | 41383 | None |
| android_app/app/src/main/python/static/live_map/muavin_live_map_extra.js.bak_remove_compass_20260513_165759 | 40400 | None |
| android_app/app/src/main/python/static/seats/drive-controls.js.bak_before_clean_speed_split_leftover_20260516_151647 | 7542 | None |
| android_app/app/src/main/python/static/seats/drive-controls.js.bak_before_corrective_restore_20260516_151536 | 7959 | None |
| android_app/app/src/main/python/static/seats/drive-controls.js.bak_before_exact_113619_restore_20260516_153946 | 7542 | None |
| android_app/app/src/main/python/static/seats/drive-controls.js.bak_before_fix_bad_voice_rollback_20260516_150609 | 7542 | None |
| android_app/app/src/main/python/static/seats/drive-controls.js.bak_before_restore_12_checkpoint_20260516_153518 | 7542 | None |
| android_app/app/src/main/python/static/seats/drive-controls.js.bak_before_restore_from_20260516_145319_20260516_151331 | 7543 | None |
| android_app/app/src/main/python/static/seats/drive-controls.js.bak_before_restore_natural_total_checkpoint_20260516_152438 | 7542 | None |
| android_app/app/src/main/python/static/seats/drive-controls.js.bak_before_restore_previous_20260516_150549 | 7959 | None |
| android_app/app/src/main/python/static/seats/drive-controls.js.bak_before_rollback_exact_113619_20260516_154139 | 7542 | None |
| android_app/app/src/main/python/static/seats/drive-controls.js.bak_before_voice_mass_rollback_20260516_150355 | 7542 | None |
| android_app/app/src/main/python/static/seats/drive-controls.js.bak_drive_toggle_fix | 7564 | None |
| android_app/app/src/main/python/static/seats/drive-controls.js.bak_force_repair_20260516_145319 | 7959 | None |
| android_app/app/src/main/python/static/seats/drive-controls.js.bak_hard_line_repair_20260516_145608 | 7959 | None |
| android_app/app/src/main/python/static/seats/drive-controls.js.bak_hard_repair_voice_block_20260516_145427 | 7959 | None |
| android_app/app/src/main/python/static/seats/drive-controls.js.bak_repair_voice_block_20260516_133452 | 7959 | None |
| android_app/app/src/main/python/static/seats/drive-controls.js.bak_voice_owner_fix | 6642 | None |
| android_app/app/src/main/python/static/seats/patches/mobile-performance-fix.css.bak_modal_readability_20260518_181100 | 2498 | None |
| android_app/app/src/main/python/static/seats/patches/stop-flow-focus-patch.js.bak_before_rollback_20260520_103515 | 18400 | None |
| android_app/app/src/main/python/static/seats/patches/stop-flow-focus-patch.js.bak_live_runtime_sync_20260520_103326 | 10723 | None |
| android_app/app/src/main/python/static/seats/patches/stop-flow-focus-patch.js.bak_scope_simple_only_20260520_105358 | 10723 | None |
| android_app/app/src/main/python/static/seats/patches/stop-flow-focus-patch.js.bak_simple_scope_20260520_110612 | 10723 | None |
| android_app/app/src/main/python/static/seats/patches/stop-flow-focus-patch.js.bak_sync_20260520_113916 | 12254 | None |
| android_app/app/src/main/python/static/seats/route-marquee.js.bak_force_always | 2928 | None |
| android_app/app/src/main/python/static/seats/route-marquee.js.bak_full_scroll_fix | 1848 | None |
| android_app/app/src/main/python/static/seats/route-marquee.js.bak_marquee_clean_final | 2798 | None |
| android_app/app/src/main/python/static/seats/route-marquee.js.bak_marquee_readable | 2231 | None |
| android_app/app/src/main/python/static/seats/route-marquee.js.bak_marquee_single_clean | 2276 | None |
| android_app/app/src/main/python/static/seats/route-marquee.js.bak_marquee_total_cleanup | 2009 | None |
| android_app/app/src/main/python/static/seats/route-marquee.js.bak_ticker_fix | 2090 | None |
| android_app/app/src/main/python/static/seats/route-marquee.js.bak_tv_marquee_real | 1444 | None |
| android_app/app/src/main/python/static/seats/seats-dashboard-final.css.bak_tone | 18430 | None |
| android_app/app/src/main/python/static/seats/seats-final.css.bak_bottom_legend_fixed_final | 59871 | None |
| android_app/app/src/main/python/static/seats/seats-final.css.bak_clean_marquee_final | 45650 | None |
| android_app/app/src/main/python/static/seats/seats-final.css.bak_drive_actions_route_top | 62888 | None |
| android_app/app/src/main/python/static/seats/seats-final.css.bak_drive_actions_top | 59765 | None |
| android_app/app/src/main/python/static/seats/seats-final.css.bak_drive_fab_final | 25105 | None |
| android_app/app/src/main/python/static/seats/seats-final.css.bak_drive_premium_screen_v1 | 25107 | None |
| android_app/app/src/main/python/static/seats/seats-final.css.bak_drive_top_clean_final | 28419 | None |
| android_app/app/src/main/python/static/seats/seats-final.css.bak_drive_voice_clean_single | 61899 | None |
| android_app/app/src/main/python/static/seats/seats-final.css.bak_drive_voice_clone_row | 63589 | None |
| android_app/app/src/main/python/static/seats/seats-final.css.bak_drive_voice_equal_clean | 63589 | None |
| android_app/app/src/main/python/static/seats/seats-final.css.bak_drive_voice_id | 61900 | None |
| android_app/app/src/main/python/static/seats/seats-final.css.bak_drive_voice_only_final | 65516 | None |
| android_app/app/src/main/python/static/seats/seats-final.css.bak_drive_voice_only_rollback | 64652 | None |
| android_app/app/src/main/python/static/seats/seats-final.css.bak_drive_voice_separat | 61899 | None |
| android_app/app/src/main/python/static/seats/seats-final.css.bak_drive_voice_width_only | 61899 | None |
| android_app/app/src/main/python/static/seats/seats-final.css.bak_fixed_bottom_legend | 57082 | None |
| android_app/app/src/main/python/static/seats/seats-final.css.bak_force_always | 46405 | None |
| android_app/app/src/main/python/static/seats/seats-final.css.bak_full_scroll_fix | 46499 | None |
| android_app/app/src/main/python/static/seats/seats-final.css.bak_hide_legend_row | 56798 | None |
| android_app/app/src/main/python/static/seats/seats-final.css.bak_legend_conflict_clean | 62916 | None |
| android_app/app/src/main/python/static/seats/seats-final.css.bak_legend_lift_fix | 59766 | None |
| android_app/app/src/main/python/static/seats/seats-final.css.bak_live_danger_restore | 30966 | None |
| android_app/app/src/main/python/static/seats/seats-final.css.bak_live_dot_position_fix | 42657 | None |
| android_app/app/src/main/python/static/seats/seats-final.css.bak_live_pill_dot | 41879 | None |
| android_app/app/src/main/python/static/seats/seats-final.css.bak_live_pill_red_text | 45946 | None |
| android_app/app/src/main/python/static/seats/seats-final.css.bak_marquee_clean_final | 54312 | None |
| android_app/app/src/main/python/static/seats/seats-final.css.bak_marquee_cleanup | 56807 | None |
| android_app/app/src/main/python/static/seats/seats-final.css.bak_marquee_conflict_cleanup | 49959 | None |
| android_app/app/src/main/python/static/seats/seats-final.css.bak_marquee_final | 52046 | None |
| android_app/app/src/main/python/static/seats/seats-final.css.bak_marquee_readable | 47658 | None |
| android_app/app/src/main/python/static/seats/seats-final.css.bak_marquee_single_clean | 47185 | None |
| android_app/app/src/main/python/static/seats/seats-final.css.bak_marquee_total_cleanup | 50400 | None |
| android_app/app/src/main/python/static/seats/seats-final.css.bak_next_pill_orange | 47326 | None |
| android_app/app/src/main/python/static/seats/seats-final.css.bak_normal_pin_bright | 35117 | None |
| android_app/app/src/main/python/static/seats/seats-final.css.bak_normal_route_pin | 33224 | None |
| android_app/app/src/main/python/static/seats/seats-final.css.bak_rollback_drive_fab_top | 28331 | None |
| android_app/app/src/main/python/static/seats/seats-final.css.bak_route_card_bg_boost | 36814 | None |
| android_app/app/src/main/python/static/seats/seats-final.css.bak_route_card_color_boost | 28918 | None |
| android_app/app/src/main/python/static/seats/seats-final.css.bak_route_marquee | 45123 | None |
| android_app/app/src/main/python/static/seats/seats-final.css.bak_route_pill_bg_boost | 43545 | None |
| android_app/app/src/main/python/static/seats/seats-final.css.bak_route_pin_blue_icon | 26087 | None |
| android_app/app/src/main/python/static/seats/seats-final.css.bak_route_pin_icon | 25105 | None |
| android_app/app/src/main/python/static/seats/seats-final.css.bak_route_warning_colors_restore | 38616 | None |
| android_app/app/src/main/python/static/seats/seats-final.css.bak_ticker_fix | 49781 | None |
| android_app/app/src/main/python/static/seats/seats-final.css.bak_tv_marquee_fix | 46637 | None |
| android_app/app/src/main/python/static/seats/seats-final.css.bak_tv_marquee_real | 48087 | None |
| android_app/app/src/main/python/static/seats/seats-final.css.bak_voice_clean_one_final | 51182 | None |
| android_app/app/src/main/python/static/seats/seats-final.css.bak_voice_conflict_clean | 68186 | None |
| android_app/app/src/main/python/static/seats/seats-final.css.bak_voice_mini_counter_final | 21675 | None |
| android_app/app/src/main/python/static/seats/seats-final.css.bak_voice_mini_drive_fix | 23257 | None |
| android_app/app/src/main/python/static/seats/seats-final.css.bak_voice_row_clean_final | 55100 | None |
| android_app/app/src/main/python/static/seats/seats-final.css.bak_voice_row_equal_counter | 48292 | None |
| android_app/app/src/main/python/static/seats/seats-final.css.bak_voice_row_equal_final | 47721 | None |
| android_app/app/src/main/python/static/seats/seats-final.css.bak_voice_row_equal_rollback | 53034 | None |
| android_app/app/src/main/python/static/seats/seats-final.css.bak_voice_row_final_clean | 48292 | None |
| android_app/app/src/main/python/static/seats/seats-final.css.bak_voice_row_fix_rollback | 49473 | None |
| android_app/app/src/main/python/static/seats/seats-final.css.bak_voice_row_spacing_final | 65939 | None |
| android_app/app/src/main/python/static/seats/seats-final.css.bak_voice_seat_emoji | 55654 | None |
| android_app/app/src/main/python/static/seats/seats-final.css.bak_voice_seat_icon_final | 50342 | None |
| android_app/app/src/main/python/static/seats/seats-final.css.bak_voice_seat_icon_match | 52943 | None |
| android_app/app/src/main/python/static/seats/seats-final.css.bak_voice_seat_mini | 21675 | None |
| android_app/app/src/main/python/static/seats/seats-redesign.css.bak_board_fix | 15024 | None |
| android_app/app/src/main/python/static/seats/seats-redesign.css.bak_light_design | 23431 | None |
| android_app/app/src/main/python/static/seats/seats.css.bak_before_label_rollback | 103706 | None |
| android_app/app/src/main/python/static/seats/seats.css.bak_before_seats_final | 102877 | None |
| android_app/app/src/main/python/static/seats/seats.css.bak_last_row_inner_gap_fix_20260516_065535 | 102877 | None |
| android_app/app/src/main/python/static/seats/seats.css.bak_last_row_tighter_20260516_065700 | 103257 | None |
| android_app/app/src/main/python/static/seats/seats.js.bak_add_continue_trip_coords_helper_final | 74559 | None |
| android_app/app/src/main/python/static/seats/seats.js.bak_add_missing_coords_helper_fix | 74559 | None |
| android_app/app/src/main/python/static/seats/seats.js.bak_android_tts | 74818 | None |
| android_app/app/src/main/python/static/seats/seats.js.bak_append_missing_coords_helper | 74559 | None |
| android_app/app/src/main/python/static/seats/seats.js.bak_before_clean_speed_split_leftover_20260516_151647 | 84151 | None |
| android_app/app/src/main/python/static/seats/seats.js.bak_before_corrective_restore_20260516_151536 | 84139 | None |
| android_app/app/src/main/python/static/seats/seats.js.bak_before_exact_113619_restore_20260516_153946 | 84139 | None |
| android_app/app/src/main/python/static/seats/seats.js.bak_before_fix_bad_voice_rollback_20260516_150609 | 84151 | None |
| android_app/app/src/main/python/static/seats/seats.js.bak_before_restore_12_checkpoint_20260516_153518 | 84139 | None |
| android_app/app/src/main/python/static/seats/seats.js.bak_before_restore_from_20260516_145319_20260516_151331 | 84139 | None |
| android_app/app/src/main/python/static/seats/seats.js.bak_before_restore_natural_total_checkpoint_20260516_152438 | 84179 | None |
| android_app/app/src/main/python/static/seats/seats.js.bak_before_restore_previous_20260516_150549 | 84111 | None |
| android_app/app/src/main/python/static/seats/seats.js.bak_before_rollback_exact_113619_20260516_154139 | 84139 | None |
| android_app/app/src/main/python/static/seats/seats.js.bak_before_rollback_live_stop_core_20260520_104302 | 84662 | None |
| android_app/app/src/main/python/static/seats/seats.js.bak_before_rollback_live_stop_core_20260520_104314 | 84287 | None |
| android_app/app/src/main/python/static/seats/seats.js.bak_before_rollback_selected_stop_memory_20260518_153528 | 84819 | None |

## 10) Flask Route Haritası
| Route | Fonksiyon | Dosya | Satır |
| --- | --- | --- | --- |
| / | index | app.py | 1339 |
| / | index | apk_payload/app.py | 1339 |
| / | index | backups/apk_sync_20260520_234501/app.py | 1339 |
| / | index | android_app/app/src/main/python/app.py | 1339 |
| /ai-console | ai_console_page | app.py | 1334 |
| /ai-console | ai_console_page | apk_payload/app.py | 1334 |
| /ai-console | ai_console_page | backups/apk_sync_20260520_234501/app.py | 1334 |
| /ai-console | ai_console_page | android_app/app/src/main/python/app.py | 1334 |
| /api/live-consignment-deliver/<int:cid> | api_live_consignment_deliver | app.py | 2429 |
| /api/live-consignment-deliver/<int:cid> | api_live_consignment_deliver | apk_payload/app.py | 2325 |
| /api/live-consignment-deliver/<int:cid> | api_live_consignment_deliver | backups/apk_sync_20260520_234501/app.py | 2325 |
| /api/live-consignment-deliver/<int:cid> | api_live_consignment_deliver | android_app/app/src/main/python/app.py | 2424 |
| /api/live-consignment-detail/<int:cid> | api_live_consignment_detail | app.py | 2352 |
| /api/live-consignment-detail/<int:cid> | api_live_consignment_detail | apk_payload/app.py | 2248 |
| /api/live-consignment-detail/<int:cid> | api_live_consignment_detail | backups/apk_sync_20260520_234501/app.py | 2248 |
| /api/live-consignment-detail/<int:cid> | api_live_consignment_detail | android_app/app/src/main/python/app.py | 2347 |
| /api/live-runtime-state | api_live_runtime_state | app.py | 907 |
| /api/live-runtime-state | api_live_runtime_state | apk_payload/app.py | 907 |
| /api/live-runtime-state | api_live_runtime_state | backups/apk_sync_20260520_234501/app.py | 907 |
| /api/live-runtime-state | api_live_runtime_state | android_app/app/src/main/python/app.py | 907 |
| /api/live-seat-bag-detail | api_live_seat_bag_detail | app.py | 1912 |
| /api/live-seat-bag-detail | api_live_seat_bag_detail | apk_payload/app.py | 1808 |
| /api/live-seat-bag-detail | api_live_seat_bag_detail | backups/apk_sync_20260520_234501/app.py | 1808 |
| /api/live-seat-bag-detail | api_live_seat_bag_detail | android_app/app/src/main/python/app.py | 1907 |
| /api/live-seat-destination | api_live_seat_destination | app.py | 2227 |
| /api/live-seat-destination | api_live_seat_destination | apk_payload/app.py | 2123 |
| /api/live-seat-destination | api_live_seat_destination | backups/apk_sync_20260520_234501/app.py | 2123 |
| /api/live-seat-destination | api_live_seat_destination | android_app/app/src/main/python/app.py | 2222 |
| /api/live-seat-offload | api_live_seat_offload | app.py | 2124 |
| /api/live-seat-offload | api_live_seat_offload | apk_payload/app.py | 2020 |
| /api/live-seat-offload | api_live_seat_offload | backups/apk_sync_20260520_234501/app.py | 2020 |
| /api/live-seat-offload | api_live_seat_offload | android_app/app/src/main/python/app.py | 2119 |
| /api/live-stop-complete | api_live_stop_complete | app.py | 2498 |
| /api/live-stop-complete | api_live_stop_complete | apk_payload/app.py | 2394 |
| /api/live-stop-complete | api_live_stop_complete | backups/apk_sync_20260520_234501/app.py | 2394 |
| /api/live-stop-complete | api_live_stop_complete | android_app/app/src/main/python/app.py | 2493 |
| /api/live-stop-detail | api_live_stop_detail | app.py | 2709 |
| /api/live-stop-detail | api_live_stop_detail | apk_payload/app.py | 2605 |
| /api/live-stop-detail | api_live_stop_detail | backups/apk_sync_20260520_234501/app.py | 2605 |
| /api/live-stop-detail | api_live_stop_detail | android_app/app/src/main/python/app.py | 2704 |
| /api/live-stop-offload | api_live_stop_offload | app.py | 2022 |
| /api/live-stop-offload | api_live_stop_offload | apk_payload/app.py | 1918 |
| /api/live-stop-offload | api_live_stop_offload | backups/apk_sync_20260520_234501/app.py | 1918 |
| /api/live-stop-offload | api_live_stop_offload | android_app/app/src/main/python/app.py | 2017 |
| /api/report-archive | api_report_archive | app.py | 4122 |
| /api/report-archive | api_report_archive | apk_payload/app.py | 4018 |
| /api/report-archive | api_report_archive | backups/apk_sync_20260520_234501/app.py | 4018 |
| /api/report-archive | api_report_archive | android_app/app/src/main/python/app.py | 4117 |
| /api/standing | api_standing | app.py | 3661 |
| /api/standing | api_standing | apk_payload/app.py | 3557 |
| /api/standing | api_standing | backups/apk_sync_20260520_234501/app.py | 3557 |
| /api/standing | api_standing | android_app/app/src/main/python/app.py | 3656 |
| /api/standing/list | api_standing_list | app.py | 3753 |
| /api/standing/list | api_standing_list | apk_payload/app.py | 3649 |
| /api/standing/list | api_standing_list | backups/apk_sync_20260520_234501/app.py | 3649 |
| /api/standing/list | api_standing_list | android_app/app/src/main/python/app.py | 3748 |
| /api/stats | api_stats | app.py | 3787 |
| /api/stats | api_stats | apk_payload/app.py | 3683 |
| /api/stats | api_stats | backups/apk_sync_20260520_234501/app.py | 3683 |
| /api/stats | api_stats | android_app/app/src/main/python/app.py | 3782 |
| /api/stoplog | api_stoplog | app.py | 3856 |
| /api/stoplog | api_stoplog | apk_payload/app.py | 3752 |
| /api/stoplog | api_stoplog | backups/apk_sync_20260520_234501/app.py | 3752 |
| /api/stoplog | api_stoplog | android_app/app/src/main/python/app.py | 3851 |
| /api/trip-report | api_trip_report | app.py | 3951 |
| /api/trip-report | api_trip_report | apk_payload/app.py | 3847 |
| /api/trip-report | api_trip_report | backups/apk_sync_20260520_234501/app.py | 3847 |
| /api/trip-report | api_trip_report | android_app/app/src/main/python/app.py | 3946 |
| /api/trip-report/archive/<base> | api_archived_trip_report | app.py | 4102 |
| /api/trip-report/archive/<base> | api_archived_trip_report | apk_payload/app.py | 3998 |
| /api/trip-report/archive/<base> | api_archived_trip_report | backups/apk_sync_20260520_234501/app.py | 3998 |
| /api/trip-report/archive/<base> | api_archived_trip_report | android_app/app/src/main/python/app.py | 4097 |
| /api/walkon | api_walkon | app.py | 3513 |
| /api/walkon | api_walkon | apk_payload/app.py | 3409 |
| /api/walkon | api_walkon | backups/apk_sync_20260520_234501/app.py | 3409 |
| /api/walkon | api_walkon | android_app/app/src/main/python/app.py | 3508 |
| /bags/clear | bags_clear_alias | app.py | 4305 |
| /bags/clear | bags_clear_alias | apk_payload/app.py | 4201 |
| /bags/clear | bags_clear_alias | backups/apk_sync_20260520_234501/app.py | 4201 |
| /bags/clear | bags_clear_alias | android_app/app/src/main/python/app.py | 4300 |
| /canli-harita | live_map_page | app.py | 2955 |
| /canli-harita | live_map_page | apk_payload/app.py | 2851 |
| /canli-harita | live_map_page | backups/apk_sync_20260520_234501/app.py | 2851 |
| /canli-harita | live_map_page | android_app/app/src/main/python/app.py | 2950 |
| /capture | capture | android_app/app/src/main/python/modules/bags/__init__.py | 1091 |
| /capture | capture | apk_payload/modules/bags/__init__.py | 1091 |
| /capture | capture | modules/bags/__init__.py | 1091 |
| /clear | clear_bags | android_app/app/src/main/python/modules/bags/__init__.py | 1026 |
| /clear | clear_bags | apk_payload/modules/bags/__init__.py | 1026 |
| /clear | clear_bags | modules/bags/__init__.py | 1026 |
| /continue-trip | continue_trip | app.py | 1416 |
| /continue-trip | continue_trip | apk_payload/app.py | 1411 |
| /continue-trip | continue_trip | backups/apk_sync_20260520_234501/app.py | 1411 |
| /continue-trip | continue_trip | android_app/app/src/main/python/app.py | 1411 |
| /delete-one | delete_one | android_app/app/src/main/python/modules/bags/__init__.py | 1057 |
| /delete-one | delete_one | apk_payload/modules/bags/__init__.py | 1057 |
| /delete-one | delete_one | modules/bags/__init__.py | 1057 |
| /end-trip | end_trip | app.py | 4364 |
| /end-trip | end_trip | apk_payload/app.py | 4260 |
| /end-trip | end_trip | backups/apk_sync_20260520_234501/app.py | 4260 |
| /end-trip | end_trip | android_app/app/src/main/python/app.py | 4359 |
| /end_trip | end_trip | app.py | 4365 |
| /end_trip | end_trip | apk_payload/app.py | 4261 |
| /end_trip | end_trip | backups/apk_sync_20260520_234501/app.py | 4261 |
| /end_trip | end_trip | android_app/app/src/main/python/app.py | 4360 |
| /rapor-arsiv | report_archive_page | app.py | 4184 |
| /rapor-arsiv | report_archive_page | apk_payload/app.py | 4080 |
| /rapor-arsiv | report_archive_page | backups/apk_sync_20260520_234501/app.py | 4080 |
| /rapor-arsiv | report_archive_page | android_app/app/src/main/python/app.py | 4179 |
| /rapor-dosya/<base>/<kind> | report_file_download | app.py | 4211 |
| /rapor-dosya/<base>/<kind> | report_file_download | apk_payload/app.py | 4107 |
| /rapor-dosya/<base>/<kind> | report_file_download | backups/apk_sync_20260520_234501/app.py | 4107 |
| /rapor-dosya/<base>/<kind> | report_file_download | android_app/app/src/main/python/app.py | 4206 |
| /raw/<trip>/<seat>/<path:filename> | raw | android_app/app/src/main/python/modules/bags/__init__.py | 1314 |
| /raw/<trip>/<seat>/<path:filename> | raw | apk_payload/modules/bags/__init__.py | 1314 |
| /raw/<trip>/<seat>/<path:filename> | raw | modules/bags/__init__.py | 1314 |
| /rehber | rehber_page | app.py | 4502 |
| /rehber | rehber_page | apk_payload/app.py | 4398 |
| /rehber | rehber_page | backups/apk_sync_20260520_234501/app.py | 4398 |
| /rehber | rehber_page | android_app/app/src/main/python/app.py | 4497 |
| /sefer-baslat | trip_start | app.py | 1360 |
| /sefer-baslat | trip_start | apk_payload/app.py | 1360 |
| /sefer-baslat | trip_start | backups/apk_sync_20260520_234501/app.py | 1360 |
| /sefer-baslat | trip_start | android_app/app/src/main/python/app.py | 1360 |
| /sefer-raporu | trip_report_page | app.py | 3946 |
| /sefer-raporu | trip_report_page | apk_payload/app.py | 3842 |
| /sefer-raporu | trip_report_page | backups/apk_sync_20260520_234501/app.py | 3842 |
| /sefer-raporu | trip_report_page | android_app/app/src/main/python/app.py | 3941 |
| /sefer-raporu-son | latest_trip_report_redirect | app.py | 4160 |
| /sefer-raporu-son | latest_trip_report_redirect | apk_payload/app.py | 4056 |
| /sefer-raporu-son | latest_trip_report_redirect | backups/apk_sync_20260520_234501/app.py | 4056 |
| /sefer-raporu-son | latest_trip_report_redirect | android_app/app/src/main/python/app.py | 4155 |
| /sefer-raporu/arsiv/<base> | archived_trip_report_page | app.py | 4089 |
| /sefer-raporu/arsiv/<base> | archived_trip_report_page | apk_payload/app.py | 3985 |
| /sefer-raporu/arsiv/<base> | archived_trip_report_page | backups/apk_sync_20260520_234501/app.py | 3985 |
| /sefer-raporu/arsiv/<base> | archived_trip_report_page | android_app/app/src/main/python/app.py | 4084 |
| /set-route | set_route | app.py | 1346 |
| /set-route | set_route | apk_payload/app.py | 1346 |
| /set-route | set_route | backups/apk_sync_20260520_234501/app.py | 1346 |
| /set-route | set_route | android_app/app/src/main/python/app.py | 1346 |
| /tanitim | onboarding_page | app.py | 1284 |
| /tanitim | onboarding_page | apk_payload/app.py | 1284 |
| /tanitim | onboarding_page | backups/apk_sync_20260520_234501/app.py | 1284 |
| /tanitim | onboarding_page | android_app/app/src/main/python/app.py | 1284 |
| /thumb/<trip>/<seat>/<path:filename> | thumb | android_app/app/src/main/python/modules/bags/__init__.py | 1319 |
| /thumb/<trip>/<seat>/<path:filename> | thumb | apk_payload/modules/bags/__init__.py | 1319 |
| /thumb/<trip>/<seat>/<path:filename> | thumb | modules/bags/__init__.py | 1319 |
| /x |  | tools/muavin_audit_step2.py | 209 |

## 11) render_template Haritası
| Template | Çağıran Python dosyası | Satır |
| --- | --- | --- |
| add_route.html | modules/routes_panel.py | 58 |
| add_route.html | android_app/app/src/main/python/modules/routes_panel.py | 58 |
| add_route.html | apk_payload/modules/routes_panel.py | 58 |
| ai_console.html | app.py | 1336 |
| ai_console.html | apk_payload/app.py | 1336 |
| ai_console.html | backups/apk_sync_20260520_234501/app.py | 1336 |
| ai_console.html | android_app/app/src/main/python/app.py | 1336 |
| events.html | modules/reports_panel.py | 29 |
| events.html | android_app/app/src/main/python/modules/reports_panel.py | 29 |
| events.html | apk_payload/modules/reports_panel.py | 29 |
| forgot_password.html | modules/settings_panel.py | 142 |
| forgot_password.html | android_app/app/src/main/python/modules/settings_panel.py | 142 |
| forgot_password.html | apk_payload/modules/settings_panel.py | 142 |
| index.html | app.py | 1343 |
| index.html | apk_payload/app.py | 1343 |
| index.html | backups/apk_sync_20260520_234501/app.py | 1343 |
| index.html | android_app/app/src/main/python/app.py | 1343 |
| login.html | modules/settings_panel.py | 55 |
| login.html | modules/settings_panel.py | 57 |
| login.html | android_app/app/src/main/python/modules/settings_panel.py | 55 |
| login.html | android_app/app/src/main/python/modules/settings_panel.py | 57 |
| login.html | apk_payload/modules/settings_panel.py | 55 |
| login.html | apk_payload/modules/settings_panel.py | 57 |
| onboarding.html | app.py | 1286 |
| onboarding.html | apk_payload/app.py | 1286 |
| onboarding.html | backups/apk_sync_20260520_234501/app.py | 1286 |
| onboarding.html | android_app/app/src/main/python/app.py | 1286 |
| passenger_control.html | modules/seats_panel.py | 78 |
| passenger_control.html | backups/apk_sync_20260520_234501/seats_panel.py | 78 |
| passenger_control.html | android_app/app/src/main/python/modules/seats_panel.py | 78 |
| passenger_control.html | apk_payload/modules/seats_panel.py | 78 |
| rehber.html | app.py | 4504 |
| rehber.html | apk_payload/app.py | 4400 |
| rehber.html | backups/apk_sync_20260520_234501/app.py | 4400 |
| rehber.html | android_app/app/src/main/python/app.py | 4499 |
| report_archive.html | app.py | 4208 |
| report_archive.html | apk_payload/app.py | 4104 |
| report_archive.html | backups/apk_sync_20260520_234501/app.py | 4104 |
| report_archive.html | android_app/app/src/main/python/app.py | 4203 |
| reports.html | modules/reports_panel.py | 81 |
| reports.html | android_app/app/src/main/python/modules/reports_panel.py | 81 |
| reports.html | apk_payload/modules/reports_panel.py | 81 |
| route_edit.html | modules/routes_panel.py | 90 |
| route_edit.html | android_app/app/src/main/python/modules/routes_panel.py | 90 |
| route_edit.html | apk_payload/modules/routes_panel.py | 90 |
| routes_list.html | modules/routes_panel.py | 37 |
| routes_list.html | android_app/app/src/main/python/modules/routes_panel.py | 37 |
| routes_list.html | apk_payload/modules/routes_panel.py | 37 |
| settings.html | modules/subscription_panel.py | 259 |
| settings.html | android_app/app/src/main/python/modules/subscription_panel.py | 259 |
| settings.html | apk_payload/modules/subscription_panel.py | 259 |
| settings_package_requests.html | modules/subscription_panel.py | 331 |
| settings_package_requests.html | android_app/app/src/main/python/modules/subscription_panel.py | 331 |
| settings_package_requests.html | apk_payload/modules/subscription_panel.py | 331 |
| settings_password.html | modules/settings_panel.py | 85 |
| settings_password.html | android_app/app/src/main/python/modules/settings_panel.py | 85 |
| settings_password.html | apk_payload/modules/settings_panel.py | 85 |
| settings_profile.html | modules/settings_panel.py | 203 |
| settings_profile.html | android_app/app/src/main/python/modules/settings_panel.py | 203 |
| settings_profile.html | apk_payload/modules/settings_panel.py | 203 |
| setup.html | modules/settings_panel.py | 182 |
| setup.html | android_app/app/src/main/python/modules/settings_panel.py | 182 |
| setup.html | apk_payload/modules/settings_panel.py | 182 |
| setup_done.html | modules/settings_panel.py | 180 |
| setup_done.html | android_app/app/src/main/python/modules/settings_panel.py | 180 |
| setup_done.html | apk_payload/modules/settings_panel.py | 180 |
| subscription_required.html | modules/subscription_panel.py | 256 |
| subscription_required.html | android_app/app/src/main/python/modules/subscription_panel.py | 256 |
| subscription_required.html | apk_payload/modules/subscription_panel.py | 256 |
| trip_report.html | app.py | 3948 |
| trip_report.html | app.py | 4099 |
| trip_report.html | apk_payload/app.py | 3844 |
| trip_report.html | apk_payload/app.py | 3995 |
| trip_report.html | backups/apk_sync_20260520_234501/app.py | 3844 |
| trip_report.html | backups/apk_sync_20260520_234501/app.py | 3995 |
| trip_report.html | android_app/app/src/main/python/app.py | 3943 |
| trip_report.html | android_app/app/src/main/python/app.py | 4094 |
| user_reset.html | modules/settings_panel.py | 40 |
| user_reset.html | android_app/app/src/main/python/modules/settings_panel.py | 40 |
| user_reset.html | apk_payload/modules/settings_panel.py | 40 |
| x.html | tools/audit_files.py | 51 |

## 12) Template → Static / Include Haritası
| HTML | Local ref sayısı | İlk referanslar | Include/Extends |
| --- | --- | --- | --- |
| templates/add_route.html | 0 |  | base.html |
| templates/base.html | 12 | {{ url_for(, {{ url_for(, {{ url_for(, {{ url_for(, {{ url_for(, {{ url_for(, url_for static: vendor/bootstrap/bootstrap.min.css, url_for static: vendor/icons.css, url_for static: css/style.css, url_for static: vendor/jquery.min.js, url_for static: vendor/bootstrap/bootstrap.bundle.min.js, url_for static: app.js |  |
| templates/consignments.html | 5 | /static/style.css, {{ url_for(, {{ url_for(, ${p.url}, ${p.url} | base.html |
| templates/events.html | 3 | {{ url_for(, {{ url_for(, {{ url_for( |  |
| templates/fare_admin.html | 3 | /static/style.css, {{ url_for(, {{ url_for( | base.html |
| templates/fare_query.html | 3 | /static/style.css, {{ url_for(, {{ url_for( | base.html |
| templates/hesap.html | 5 | /, {{ url_for(, {{ url_for(, {{ url_for(, {{ url_for( |  |
| templates/home.html | 4 | {{ url_for(, {{ url_for(, {{ url_for(, {{ url_for( | base.html |
| templates/index.html | 15 | {{ url_for(, {{ url_for(, {{ url_for(, {{ url_for(, {{ url_for(, {{ url_for(, {{ url_for(, {{ url_for(, {{ url_for(, {{ url_for(, /sefer-raporu-son, {{ url_for( |  |
| templates/login.html | 5 | {{ url_for(, {{ admin_profile.photo_path }}, /sifre-unuttum, /kullanici-sifirla, url_for static: img/menu-bus-card.png |  |
| templates/passenger_control.html | 3 | /static/style.css, {{ url_for(, {{ url_for( | base.html |
| templates/reports.html | 1 | {{ url_for( | base.html |
| templates/route_edit.html | 3 | /static/style.css, {{ url_for(, {{ url_for( | base.html |
| templates/route_stops.html | 1 | {{ url_for( | base.html |
| templates/routes_list.html | 5 | /static/style.css, {{ url_for(, {{ url_for(, {{ url_for(, {{ url_for( | base.html |
| templates/seats.html | 41 | /static/style.css, /static/seats/seats.css, /static/seats/seats-final.css, /static/seats/patches/stop-selected-toast.css, /static/seats/patches/stop-flow-focus-patch.css, /static/seats/patches/stop-flow-compact-mobile.css, /static/seats/patches/seat-layout-fab-pack.css, /static/seats/patches/bottom-voice-command.css, /static/seats/patches/modal-bottom-nav-autohide.css, /static/seats/patches/manual-ticket-system.css, /static/seats/patches/top-sound-toggle.css, /static/seats/patches/seat-simple-ui-pack.css | base.html, seats_parts/topbar.html, seats_parts/stats.html, seats_parts/route_flow.html, seats_parts/deck.html, seats_parts/modals.html, seats_parts/finish_trip_modal.html, seats_parts/offload_confirm.html |
| templates/settings.html | 7 | /ayarlar/abonelik, /ayarlar/profil, /ayarlar/sifre, /ayarlar/kurtarma-kodu, /rapor-arsiv, /ayarlar/yedekleme, / |  |
| templates/start_trip.html | 1 | {{ url_for( | base.html |
| templates/trip_new.html | 0 |  | base.html |
| templates/ai_console.html | 3 | /static/style.css, {{ url_for(, {{ url_for( | base.html |
| templates/route_schedule_edit.html | 6 | /static/style.css, {{ url_for(, {{ url_for(, {{ url_for(, {{ url_for(, {{ url_for( | base.html |
| templates/trip_report.html | 5 | /seats, /rapor-arsiv, ${it.view}, ${it.txt}, ${it.csv} | base.html |
| templates/report_archive.html | 5 | {{ it.view }}, {{ it.txt }}, {{ it.csv }}, {{ it.json }}, /ayarlar |  |
| templates/rehber.html | 23 | {{ url_for(, {{ url_for(, {{ url_for(, {{ url_for(, {{ url_for(, {{ url_for(, {{ url_for(, {{ url_for(, {{ url_for(, {{ url_for(, {{ url_for(, {{ url_for( | base.html |
| templates/settings_password.html | 2 | /ayarlar, /ayarlar |  |
| templates/live_map.html | 9 | {{ url_for(, {{ url_for(, {{ url_for(, {{ url_for(, {{ url_for(, {{ url_for(, /seats, url_for static: live_map/muavin_live_map_extra.css, url_for static: live_map/muavin_live_map_extra.js |  |
| templates/settings_recovery.html | 3 | /ayarlar, /ayarlar, /ayarlar |  |
| templates/forgot_password.html | 1 | /login |  |
| templates/setup.html | 0 |  |  |
| templates/setup_done.html | 1 | /login |  |
| templates/settings_profile.html | 3 | {{ profile.photo_path }}, /ayarlar, /ayarlar |  |
| templates/settings_backup.html | 2 | /ayarlar/yedekleme/indir/{{ it.name }}, /ayarlar |  |
| templates/settings_subscription.html | 2 | /ayarlar/paket-talepleri, /ayarlar |  |
| templates/subscription_required.html | 1 | /ayarlar/abonelik |  |
| templates/package_required.html | 2 | /ayarlar/abonelik, / |  |
| templates/onboarding.html | 8 | /static/img/onboarding/slides/onboarding_1.png, /static/img/onboarding/slides/onboarding_2.png, /static/img/onboarding/slides/onboarding_3.png, /static/img/onboarding/slides/onboarding_4.png, /static/img/onboarding/slides/onboarding_5.png, /static/img/onboarding/slides/onboarding_6.png, /static/img/onboarding/slides/onboarding_7.png, /kurulum |  |
| templates/continue_trip.html | 20 | {{ url_for(, {{ url_for(, {{ url_for(, {{ url_for(, {{ url_for(, {{ url_for(, /, /static/seats/voice-tts.js, {{ url_for(, {{ url_for(, {{ url_for(, {{ url_for( |  |
| templates/settings_package_requests.html | 1 | /ayarlar |  |
| templates/no_active_trip.html | 2 | {{ action_url }}, {{ home_url }} |  |
| templates/user_reset.html | 1 | /login |  |
| backups/apk_sync_20260520_234501/seats.html | 40 | /static/style.css, /static/seats/seats.css, /static/seats/seats-final.css, /static/seats/patches/stop-selected-toast.css, /static/seats/patches/stop-flow-focus-patch.css, /static/seats/patches/stop-flow-compact-mobile.css, /static/seats/patches/seat-layout-fab-pack.css, /static/seats/patches/bottom-voice-command.css, /static/seats/patches/modal-bottom-nav-autohide.css, /static/seats/patches/manual-ticket-system.css, /static/seats/patches/top-sound-toggle.css, /static/seats/patches/seat-simple-ui-pack.css | base.html, seats_parts/topbar.html, seats_parts/stats.html, seats_parts/route_flow.html, seats_parts/deck.html, seats_parts/modals.html, seats_parts/finish_trip_modal.html, seats_parts/offload_confirm.html |
| backups/apk_sync_20260520_234501/trip_report.html | 5 | /seats, /rapor-arsiv, ${it.view}, ${it.txt}, ${it.csv} | base.html |
| _unused_review/trafik_isigi/trafik.html | 0 |  |  |
| android_app/app/src/main/python/templates/add_route.html | 0 |  | base.html |
| android_app/app/src/main/python/templates/base.html | 12 | {{ url_for(, {{ url_for(, {{ url_for(, {{ url_for(, {{ url_for(, {{ url_for(, url_for static: vendor/bootstrap/bootstrap.min.css, url_for static: vendor/icons.css, url_for static: css/style.css, url_for static: vendor/jquery.min.js, url_for static: vendor/bootstrap/bootstrap.bundle.min.js, url_for static: app.js |  |
| android_app/app/src/main/python/templates/consignments.html | 5 | /static/style.css, {{ url_for(, {{ url_for(, ${p.url}, ${p.url} | base.html |
| android_app/app/src/main/python/templates/events.html | 3 | {{ url_for(, {{ url_for(, {{ url_for( |  |
| android_app/app/src/main/python/templates/fare_admin.html | 3 | /static/style.css, {{ url_for(, {{ url_for( | base.html |
| android_app/app/src/main/python/templates/fare_query.html | 3 | /static/style.css, {{ url_for(, {{ url_for( | base.html |
| android_app/app/src/main/python/templates/hesap.html | 5 | /, {{ url_for(, {{ url_for(, {{ url_for(, {{ url_for( |  |
| android_app/app/src/main/python/templates/home.html | 4 | {{ url_for(, {{ url_for(, {{ url_for(, {{ url_for( | base.html |
| android_app/app/src/main/python/templates/index.html | 15 | {{ url_for(, {{ url_for(, {{ url_for(, {{ url_for(, {{ url_for(, {{ url_for(, {{ url_for(, {{ url_for(, {{ url_for(, {{ url_for(, /sefer-raporu-son, {{ url_for( |  |
| android_app/app/src/main/python/templates/login.html | 5 | {{ url_for(, {{ admin_profile.photo_path }}, /sifre-unuttum, /kullanici-sifirla, url_for static: img/menu-bus-card.png |  |
| android_app/app/src/main/python/templates/passenger_control.html | 3 | /static/style.css, {{ url_for(, {{ url_for( | base.html |
| android_app/app/src/main/python/templates/reports.html | 1 | {{ url_for( | base.html |
| android_app/app/src/main/python/templates/route_edit.html | 3 | /static/style.css, {{ url_for(, {{ url_for( | base.html |
| android_app/app/src/main/python/templates/route_stops.html | 1 | {{ url_for( | base.html |
| android_app/app/src/main/python/templates/routes_list.html | 5 | /static/style.css, {{ url_for(, {{ url_for(, {{ url_for(, {{ url_for( | base.html |
| android_app/app/src/main/python/templates/seats.html | 40 | /static/style.css, /static/seats/seats.css, /static/seats/seats-final.css, /static/seats/patches/stop-selected-toast.css, /static/seats/patches/stop-flow-focus-patch.css, /static/seats/patches/stop-flow-compact-mobile.css, /static/seats/patches/seat-layout-fab-pack.css, /static/seats/patches/bottom-voice-command.css, /static/seats/patches/modal-bottom-nav-autohide.css, /static/seats/patches/manual-ticket-system.css, /static/seats/patches/top-sound-toggle.css, /static/seats/patches/seat-simple-ui-pack.css | base.html, seats_parts/topbar.html, seats_parts/stats.html, seats_parts/route_flow.html, seats_parts/deck.html, seats_parts/modals.html, seats_parts/finish_trip_modal.html, seats_parts/offload_confirm.html |
| android_app/app/src/main/python/templates/settings.html | 7 | /ayarlar/abonelik, /ayarlar/profil, /ayarlar/sifre, /ayarlar/kurtarma-kodu, /rapor-arsiv, /ayarlar/yedekleme, / |  |
| android_app/app/src/main/python/templates/start_trip.html | 1 | {{ url_for( | base.html |
| android_app/app/src/main/python/templates/trip_new.html | 0 |  | base.html |
| android_app/app/src/main/python/templates/ai_console.html | 3 | /static/style.css, {{ url_for(, {{ url_for( | base.html |
| android_app/app/src/main/python/templates/route_schedule_edit.html | 6 | /static/style.css, {{ url_for(, {{ url_for(, {{ url_for(, {{ url_for(, {{ url_for( | base.html |
| android_app/app/src/main/python/templates/trip_report.html | 5 | /seats, /rapor-arsiv, ${it.view}, ${it.txt}, ${it.csv} | base.html |
| android_app/app/src/main/python/templates/report_archive.html | 4 | {{ it.view }}, {{ it.txt }}, {{ it.csv }}, {{ it.json }} | base.html |
| android_app/app/src/main/python/templates/rehber.html | 23 | {{ url_for(, {{ url_for(, {{ url_for(, {{ url_for(, {{ url_for(, {{ url_for(, {{ url_for(, {{ url_for(, {{ url_for(, {{ url_for(, {{ url_for(, {{ url_for( | base.html |
| android_app/app/src/main/python/templates/settings_password.html | 1 | /ayarlar |  |
| android_app/app/src/main/python/templates/live_map.html | 9 | {{ url_for(, {{ url_for(, {{ url_for(, {{ url_for(, {{ url_for(, {{ url_for(, /seats, url_for static: live_map/muavin_live_map_extra.css, url_for static: live_map/muavin_live_map_extra.js |  |
| android_app/app/src/main/python/templates/settings_recovery.html | 2 | /ayarlar, /ayarlar |  |
| android_app/app/src/main/python/templates/forgot_password.html | 1 | /login |  |
| android_app/app/src/main/python/templates/setup.html | 0 |  |  |
| android_app/app/src/main/python/templates/setup_done.html | 1 | /login |  |
| android_app/app/src/main/python/templates/settings_profile.html | 2 | {{ profile.photo_path }}, /ayarlar |  |
| android_app/app/src/main/python/templates/settings_backup.html | 2 | /ayarlar/yedekleme/indir/{{ item.name }}, /ayarlar |  |
| android_app/app/src/main/python/templates/settings_subscription.html | 2 | /ayarlar, /ayarlar/abonelik |  |
| android_app/app/src/main/python/templates/subscription_required.html | 1 | /ayarlar/abonelik |  |
| android_app/app/src/main/python/templates/package_required.html | 2 | /ayarlar/abonelik, / |  |
| android_app/app/src/main/python/templates/onboarding.html | 8 | /static/img/onboarding/slides/onboarding_1.png, /static/img/onboarding/slides/onboarding_2.png, /static/img/onboarding/slides/onboarding_3.png, /static/img/onboarding/slides/onboarding_4.png, /static/img/onboarding/slides/onboarding_5.png, /static/img/onboarding/slides/onboarding_6.png, /static/img/onboarding/slides/onboarding_7.png, /kurulum |  |
| android_app/app/src/main/python/templates/continue_trip.html | 20 | {{ url_for(, {{ url_for(, {{ url_for(, {{ url_for(, {{ url_for(, {{ url_for(, /, /static/seats/voice-tts.js, {{ url_for(, {{ url_for(, {{ url_for(, {{ url_for( |  |
| android_app/app/src/main/python/templates/settings_package_requests.html | 1 | /ayarlar |  |
| android_app/app/src/main/python/templates/no_active_trip.html | 2 | {{ action_url }}, {{ home_url }} |  |
| android_app/app/src/main/python/templates/user_reset.html | 1 | /login |  |
| android_app/app/src/main/python/templates/seats_parts/modals.html | 0 |  |  |
| android_app/app/src/main/python/templates/seats_parts/topbar.html | 4 | {{ url_for(, {{ url_for(, {{ url_for(, {{ url_for( |  |
| android_app/app/src/main/python/templates/seats_parts/stats.html | 0 |  |  |
| android_app/app/src/main/python/templates/seats_parts/route_flow.html | 0 |  |  |
| android_app/app/src/main/python/templates/seats_parts/deck.html | 0 |  |  |
| android_app/app/src/main/python/templates/seats_parts/offload_confirm.html | 0 |  |  |
| android_app/app/src/main/python/templates/seats_parts/finish_trip_modal.html | 1 | /end_trip |  |
| apk_payload/templates/add_route.html | 0 |  | base.html |
| apk_payload/templates/base.html | 12 | {{ url_for(, {{ url_for(, {{ url_for(, {{ url_for(, {{ url_for(, {{ url_for(, url_for static: vendor/bootstrap/bootstrap.min.css, url_for static: vendor/icons.css, url_for static: css/style.css, url_for static: vendor/jquery.min.js, url_for static: vendor/bootstrap/bootstrap.bundle.min.js, url_for static: app.js |  |
| apk_payload/templates/consignments.html | 5 | /static/style.css, {{ url_for(, {{ url_for(, ${p.url}, ${p.url} | base.html |
| apk_payload/templates/events.html | 3 | {{ url_for(, {{ url_for(, {{ url_for( |  |
| apk_payload/templates/fare_admin.html | 3 | /static/style.css, {{ url_for(, {{ url_for( | base.html |
| apk_payload/templates/fare_query.html | 3 | /static/style.css, {{ url_for(, {{ url_for( | base.html |
| apk_payload/templates/hesap.html | 5 | /, {{ url_for(, {{ url_for(, {{ url_for(, {{ url_for( |  |
| apk_payload/templates/home.html | 4 | {{ url_for(, {{ url_for(, {{ url_for(, {{ url_for( | base.html |
| apk_payload/templates/index.html | 15 | {{ url_for(, {{ url_for(, {{ url_for(, {{ url_for(, {{ url_for(, {{ url_for(, {{ url_for(, {{ url_for(, {{ url_for(, {{ url_for(, /sefer-raporu-son, {{ url_for( |  |
| apk_payload/templates/login.html | 5 | {{ url_for(, {{ admin_profile.photo_path }}, /sifre-unuttum, /kullanici-sifirla, url_for static: img/menu-bus-card.png |  |
| apk_payload/templates/passenger_control.html | 3 | /static/style.css, {{ url_for(, {{ url_for( | base.html |
| apk_payload/templates/reports.html | 1 | {{ url_for( | base.html |
| apk_payload/templates/route_edit.html | 3 | /static/style.css, {{ url_for(, {{ url_for( | base.html |
| apk_payload/templates/route_stops.html | 1 | {{ url_for( | base.html |
| apk_payload/templates/routes_list.html | 5 | /static/style.css, {{ url_for(, {{ url_for(, {{ url_for(, {{ url_for( | base.html |
| apk_payload/templates/seats.html | 40 | /static/style.css, /static/seats/seats.css, /static/seats/seats-final.css, /static/seats/patches/stop-selected-toast.css, /static/seats/patches/stop-flow-focus-patch.css, /static/seats/patches/stop-flow-compact-mobile.css, /static/seats/patches/seat-layout-fab-pack.css, /static/seats/patches/bottom-voice-command.css, /static/seats/patches/modal-bottom-nav-autohide.css, /static/seats/patches/manual-ticket-system.css, /static/seats/patches/top-sound-toggle.css, /static/seats/patches/seat-simple-ui-pack.css | base.html, seats_parts/topbar.html, seats_parts/stats.html, seats_parts/route_flow.html, seats_parts/deck.html, seats_parts/modals.html, seats_parts/finish_trip_modal.html, seats_parts/offload_confirm.html |
| apk_payload/templates/settings.html | 7 | /ayarlar/abonelik, /ayarlar/profil, /ayarlar/sifre, /ayarlar/kurtarma-kodu, /rapor-arsiv, /ayarlar/yedekleme, / |  |
| apk_payload/templates/start_trip.html | 1 | {{ url_for( | base.html |
| apk_payload/templates/trip_new.html | 0 |  | base.html |
| apk_payload/templates/ai_console.html | 3 | /static/style.css, {{ url_for(, {{ url_for( | base.html |
| apk_payload/templates/route_schedule_edit.html | 6 | /static/style.css, {{ url_for(, {{ url_for(, {{ url_for(, {{ url_for(, {{ url_for( | base.html |
| apk_payload/templates/trip_report.html | 5 | /seats, /rapor-arsiv, ${it.view}, ${it.txt}, ${it.csv} | base.html |
| apk_payload/templates/report_archive.html | 4 | {{ it.view }}, {{ it.txt }}, {{ it.csv }}, {{ it.json }} | base.html |
| apk_payload/templates/rehber.html | 23 | {{ url_for(, {{ url_for(, {{ url_for(, {{ url_for(, {{ url_for(, {{ url_for(, {{ url_for(, {{ url_for(, {{ url_for(, {{ url_for(, {{ url_for(, {{ url_for( | base.html |
| apk_payload/templates/settings_password.html | 1 | /ayarlar |  |
| apk_payload/templates/live_map.html | 9 | {{ url_for(, {{ url_for(, {{ url_for(, {{ url_for(, {{ url_for(, {{ url_for(, /seats, url_for static: live_map/muavin_live_map_extra.css, url_for static: live_map/muavin_live_map_extra.js |  |
| apk_payload/templates/settings_recovery.html | 2 | /ayarlar, /ayarlar |  |
| apk_payload/templates/forgot_password.html | 1 | /login |  |
| apk_payload/templates/setup.html | 0 |  |  |
| apk_payload/templates/setup_done.html | 1 | /login |  |
| apk_payload/templates/settings_profile.html | 2 | {{ profile.photo_path }}, /ayarlar |  |
| apk_payload/templates/settings_backup.html | 2 | /ayarlar/yedekleme/indir/{{ item.name }}, /ayarlar |  |
| apk_payload/templates/settings_subscription.html | 2 | /ayarlar, /ayarlar/abonelik |  |
| apk_payload/templates/subscription_required.html | 1 | /ayarlar/abonelik |  |
| apk_payload/templates/package_required.html | 2 | /ayarlar/abonelik, / |  |
| apk_payload/templates/onboarding.html | 8 | /static/img/onboarding/slides/onboarding_1.png, /static/img/onboarding/slides/onboarding_2.png, /static/img/onboarding/slides/onboarding_3.png, /static/img/onboarding/slides/onboarding_4.png, /static/img/onboarding/slides/onboarding_5.png, /static/img/onboarding/slides/onboarding_6.png, /static/img/onboarding/slides/onboarding_7.png, /kurulum |  |
| apk_payload/templates/continue_trip.html | 11 | {{ url_for(, {{ url_for(, {{ url_for(, {{ url_for(, {{ url_for(, /, ${escapeHtml(photo.url \|\| photo.thumb_url \|\|, ${escapeHtml(photo.thumb_url \|\| photo.url \|\|, ${escapeHtml(ph.url \|\|, ${escapeHtml(ph.url \|\|, url_for static: img/live-hero-bus.png |  |
| apk_payload/templates/settings_package_requests.html | 1 | /ayarlar |  |
| apk_payload/templates/no_active_trip.html | 2 | {{ action_url }}, {{ home_url }} |  |
| apk_payload/templates/user_reset.html | 1 | /login |  |
| apk_payload/templates/seats_parts/modals.html | 0 |  |  |
| apk_payload/templates/seats_parts/topbar.html | 4 | {{ url_for(, {{ url_for(, {{ url_for(, {{ url_for( |  |
| apk_payload/templates/seats_parts/stats.html | 0 |  |  |
| apk_payload/templates/seats_parts/route_flow.html | 0 |  |  |
| apk_payload/templates/seats_parts/deck.html | 0 |  |  |
| apk_payload/templates/seats_parts/offload_confirm.html | 0 |  |  |
| apk_payload/templates/seats_parts/finish_trip_modal.html | 1 | /end_trip |  |
| templates/seats_parts/modals.html | 0 |  |  |
| templates/seats_parts/topbar.html | 4 | {{ url_for(, {{ url_for(, {{ url_for(, {{ url_for( |  |
| templates/seats_parts/stats.html | 0 |  |  |
| templates/seats_parts/route_flow.html | 0 |  |  |
| templates/seats_parts/deck.html | 0 |  |  |
| templates/seats_parts/offload_confirm.html | 0 |  |  |
| templates/seats_parts/finish_trip_modal.html | 1 | /end_trip |  |

## 13) Eksik Local Static / Dosya Referansları
HTML içinde çağrılıp fiziksel olarak bulunamayan dosyalar.
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
| android_app/app/src/main/python/templates/base.html | {{ url_for( | android_app/app/src/main/python/templates/{{ url_for( |
| android_app/app/src/main/python/templates/base.html | {{ url_for( | android_app/app/src/main/python/templates/{{ url_for( |
| android_app/app/src/main/python/templates/base.html | url_for static: vendor/icons.css | static/vendor/icons.css |
| android_app/app/src/main/python/templates/base.html | url_for static: css/style.css | static/css/style.css |
| android_app/app/src/main/python/templates/base.html | url_for static: vendor/jquery.min.js | static/vendor/jquery.min.js |
| android_app/app/src/main/python/templates/consignments.html | {{ url_for( | android_app/app/src/main/python/templates/{{ url_for( |
| android_app/app/src/main/python/templates/consignments.html | {{ url_for( | android_app/app/src/main/python/templates/{{ url_for( |
| android_app/app/src/main/python/templates/consignments.html | ${p.url} | android_app/app/src/main/python/templates/${p.url} |
| android_app/app/src/main/python/templates/consignments.html | ${p.url} | android_app/app/src/main/python/templates/${p.url} |
| android_app/app/src/main/python/templates/events.html | {{ url_for( | android_app/app/src/main/python/templates/{{ url_for( |
| android_app/app/src/main/python/templates/events.html | {{ url_for( | android_app/app/src/main/python/templates/{{ url_for( |
| android_app/app/src/main/python/templates/events.html | {{ url_for( | android_app/app/src/main/python/templates/{{ url_for( |
| android_app/app/src/main/python/templates/fare_admin.html | {{ url_for( | android_app/app/src/main/python/templates/{{ url_for( |
| android_app/app/src/main/python/templates/fare_admin.html | {{ url_for( | android_app/app/src/main/python/templates/{{ url_for( |
| android_app/app/src/main/python/templates/fare_query.html | {{ url_for( | android_app/app/src/main/python/templates/{{ url_for( |
| android_app/app/src/main/python/templates/fare_query.html | {{ url_for( | android_app/app/src/main/python/templates/{{ url_for( |
| android_app/app/src/main/python/templates/hesap.html | {{ url_for( | android_app/app/src/main/python/templates/{{ url_for( |
| android_app/app/src/main/python/templates/hesap.html | {{ url_for( | android_app/app/src/main/python/templates/{{ url_for( |
| android_app/app/src/main/python/templates/hesap.html | {{ url_for( | android_app/app/src/main/python/templates/{{ url_for( |
| android_app/app/src/main/python/templates/hesap.html | {{ url_for( | android_app/app/src/main/python/templates/{{ url_for( |
| android_app/app/src/main/python/templates/home.html | {{ url_for( | android_app/app/src/main/python/templates/{{ url_for( |
| android_app/app/src/main/python/templates/home.html | {{ url_for( | android_app/app/src/main/python/templates/{{ url_for( |
| android_app/app/src/main/python/templates/home.html | {{ url_for( | android_app/app/src/main/python/templates/{{ url_for( |
| android_app/app/src/main/python/templates/home.html | {{ url_for( | android_app/app/src/main/python/templates/{{ url_for( |
| android_app/app/src/main/python/templates/index.html | {{ url_for( | android_app/app/src/main/python/templates/{{ url_for( |
| android_app/app/src/main/python/templates/index.html | {{ url_for( | android_app/app/src/main/python/templates/{{ url_for( |
| android_app/app/src/main/python/templates/index.html | {{ url_for( | android_app/app/src/main/python/templates/{{ url_for( |
| android_app/app/src/main/python/templates/index.html | {{ url_for( | android_app/app/src/main/python/templates/{{ url_for( |
| android_app/app/src/main/python/templates/index.html | {{ url_for( | android_app/app/src/main/python/templates/{{ url_for( |
| android_app/app/src/main/python/templates/index.html | {{ url_for( | android_app/app/src/main/python/templates/{{ url_for( |
| android_app/app/src/main/python/templates/index.html | {{ url_for( | android_app/app/src/main/python/templates/{{ url_for( |
| android_app/app/src/main/python/templates/index.html | {{ url_for( | android_app/app/src/main/python/templates/{{ url_for( |
| android_app/app/src/main/python/templates/index.html | {{ url_for( | android_app/app/src/main/python/templates/{{ url_for( |
| android_app/app/src/main/python/templates/index.html | {{ url_for( | android_app/app/src/main/python/templates/{{ url_for( |
| android_app/app/src/main/python/templates/index.html | /sefer-raporu-son | sefer-raporu-son |
| android_app/app/src/main/python/templates/index.html | {{ url_for( | android_app/app/src/main/python/templates/{{ url_for( |
| android_app/app/src/main/python/templates/index.html | /ayarlar | ayarlar |
| android_app/app/src/main/python/templates/login.html | {{ url_for( | android_app/app/src/main/python/templates/{{ url_for( |
| android_app/app/src/main/python/templates/login.html | {{ admin_profile.photo_path }} | android_app/app/src/main/python/templates/{{ admin_profile.photo_path }} |
| android_app/app/src/main/python/templates/login.html | /sifre-unuttum | sifre-unuttum |

## 14) Referans Verilmeyen Static Dosyalar
Bunlar gereksiz olabilir ama JS dinamik çağırıyor olabilir. Silmeden önce tek tek bakılmalı.
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
| static/seats/seats-final.css.bak_route_card_bg_boost | 36814 | .bak_route_card_bg_boost |
| static/seats/seats-final.css.bak_route_card_color_boost | 28918 | .bak_route_card_color_boost |
| static/seats/seats-final.css.bak_route_marquee | 45123 | .bak_route_marquee |
| static/seats/seats-final.css.bak_route_pill_bg_boost | 43545 | .bak_route_pill_bg_boost |
| static/seats/seats-final.css.bak_route_pin_blue_icon | 26087 | .bak_route_pin_blue_icon |
| static/seats/seats-final.css.bak_route_pin_icon | 25105 | .bak_route_pin_icon |
| static/seats/seats-final.css.bak_route_warning_colors_restore | 38616 | .bak_route_warning_colors_restore |
| static/seats/seats-final.css.bak_ticker_fix | 49781 | .bak_ticker_fix |
| static/seats/seats-final.css.bak_tv_marquee_fix | 46637 | .bak_tv_marquee_fix |
| static/seats/seats-final.css.bak_tv_marquee_real | 48087 | .bak_tv_marquee_real |
| static/seats/seats-final.css.bak_voice_clean_one_final | 51182 | .bak_voice_clean_one_final |
| static/seats/seats-final.css.bak_voice_conflict_clean | 68186 | .bak_voice_conflict_clean |
| static/seats/seats-final.css.bak_voice_mini_counter_final | 21675 | .bak_voice_mini_counter_final |
| static/seats/seats-final.css.bak_voice_mini_drive_fix | 23257 | .bak_voice_mini_drive_fix |
| static/seats/seats-final.css.bak_voice_row_clean_final | 55100 | .bak_voice_row_clean_final |
| static/seats/seats-final.css.bak_voice_row_equal_counter | 48292 | .bak_voice_row_equal_counter |
| static/seats/seats-final.css.bak_voice_row_equal_final | 47721 | .bak_voice_row_equal_final |
| static/seats/seats-final.css.bak_voice_row_equal_rollback | 53034 | .bak_voice_row_equal_rollback |
| static/seats/seats-final.css.bak_voice_row_final_clean | 48292 | .bak_voice_row_final_clean |
| static/seats/seats-final.css.bak_voice_row_fix_rollback | 49473 | .bak_voice_row_fix_rollback |
| static/seats/seats-final.css.bak_voice_row_spacing_final | 65939 | .bak_voice_row_spacing_final |
| static/seats/seats-final.css.bak_voice_seat_emoji | 55654 | .bak_voice_seat_emoji |
| static/seats/seats-final.css.bak_voice_seat_icon_final | 50342 | .bak_voice_seat_icon_final |
| static/seats/seats-final.css.bak_voice_seat_icon_match | 52943 | .bak_voice_seat_icon_match |
| static/seats/seats-final.css.bak_voice_seat_mini | 21675 | .bak_voice_seat_mini |
| static/seats/seats-redesign.css.bak_board_fix | 15024 | .bak_board_fix |
| static/seats/seats-redesign.css.bak_light_design | 23431 | .bak_light_design |
| static/seats/seats.css.ba | 106275 | .ba |
| static/seats/seats.css.bak_before_label_rollback | 103706 | .bak_before_label_rollback |
| static/seats/seats.css.bak_before_seats_final | 102877 | .bak_before_seats_final |
| static/seats/seats.css.bak_last_row_inner_gap_fix_20260516_065535 | 102877 | .bak_last_row_inner_gap_fix_20260516_065535 |
| static/seats/seats.css.bak_last_row_tighter_20260516_065700 | 103257 | .bak_last_row_tighter_20260516_065700 |
| static/seats/seats.css.bak_unified_deck_20260521_210744 | 102903 | .bak_unified_deck_20260521_210744 |
| static/seats/seats.js.bak_add_continue_trip_coords_helper_final | 74559 | .bak_add_continue_trip_coords_helper_final |
| static/seats/seats.js.bak_add_missing_coords_helper_fix | 74559 | .bak_add_missing_coords_helper_fix |
| static/seats/seats.js.bak_android_tts | 74818 | .bak_android_tts |
| static/seats/seats.js.bak_append_missing_coords_helper | 74559 | .bak_append_missing_coords_helper |
| static/seats/seats.js.bak_before_clean_speed_split_leftover_20260516_151647 | 84151 | .bak_before_clean_speed_split_leftover_20260516_151647 |
| static/seats/seats.js.bak_before_corrective_restore_20260516_151536 | 84139 | .bak_before_corrective_restore_20260516_151536 |
| static/seats/seats.js.bak_before_exact_113619_restore_20260516_153946 | 84139 | .bak_before_exact_113619_restore_20260516_153946 |

## 15) Inline Style / Script Sayısı
Büyük HTML şişkinliği ve yama üstüne yama riskini gösterir.
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
| android_app/app/src/main/python/templates/settings_package_requests.html | 1 | 0 |
| android_app/app/src/main/python/templates/no_active_trip.html | 1 | 0 |
| android_app/app/src/main/python/templates/user_reset.html | 1 | 0 |
| android_app/app/src/main/python/templates/seats_parts/modals.html | 0 | 0 |
| android_app/app/src/main/python/templates/seats_parts/topbar.html | 0 | 0 |
| android_app/app/src/main/python/templates/seats_parts/stats.html | 0 | 0 |
| android_app/app/src/main/python/templates/seats_parts/route_flow.html | 0 | 0 |
| android_app/app/src/main/python/templates/seats_parts/deck.html | 0 | 0 |
| android_app/app/src/main/python/templates/seats_parts/offload_confirm.html | 1 | 1 |
| android_app/app/src/main/python/templates/seats_parts/finish_trip_modal.html | 1 | 1 |
| apk_payload/templates/add_route.html | 2 | 1 |
| apk_payload/templates/base.html | 0 | 0 |
| apk_payload/templates/consignments.html | 2 | 1 |
| apk_payload/templates/events.html | 1 | 0 |
| apk_payload/templates/fare_admin.html | 1 | 1 |
| apk_payload/templates/fare_query.html | 1 | 1 |
| apk_payload/templates/hesap.html | 1 | 2 |
| apk_payload/templates/home.html | 0 | 0 |
| apk_payload/templates/index.html | 8 | 3 |
| apk_payload/templates/login.html | 1 | 1 |
| apk_payload/templates/passenger_control.html | 2 | 1 |
| apk_payload/templates/reports.html | 1 | 1 |
| apk_payload/templates/route_edit.html | 2 | 2 |
| apk_payload/templates/route_stops.html | 1 | 1 |
| apk_payload/templates/routes_list.html | 1 | 1 |
| apk_payload/templates/seats.html | 2 | 5 |
| apk_payload/templates/settings.html | 1 | 0 |
| apk_payload/templates/start_trip.html | 1 | 1 |
| apk_payload/templates/trip_new.html | 0 | 0 |
| apk_payload/templates/ai_console.html | 2 | 2 |
| apk_payload/templates/route_schedule_edit.html | 2 | 1 |
| apk_payload/templates/trip_report.html | 2 | 3 |
| apk_payload/templates/report_archive.html | 1 | 0 |
| apk_payload/templates/rehber.html | 1 | 1 |
| apk_payload/templates/settings_password.html | 1 | 1 |
| apk_payload/templates/live_map.html | 19 | 2 |
| apk_payload/templates/settings_recovery.html | 1 | 1 |
| apk_payload/templates/forgot_password.html | 1 | 1 |
| apk_payload/templates/setup.html | 1 | 2 |
| apk_payload/templates/setup_done.html | 1 | 0 |
| apk_payload/templates/settings_profile.html | 1 | 0 |
| apk_payload/templates/settings_backup.html | 1 | 0 |
| apk_payload/templates/settings_subscription.html | 1 | 5 |
| apk_payload/templates/subscription_required.html | 1 | 0 |
| apk_payload/templates/package_required.html | 1 | 0 |
| apk_payload/templates/onboarding.html | 1 | 1 |
| apk_payload/templates/continue_trip.html | 26 | 5 |
| apk_payload/templates/settings_package_requests.html | 1 | 0 |
| apk_payload/templates/no_active_trip.html | 1 | 0 |
| apk_payload/templates/user_reset.html | 1 | 0 |
| apk_payload/templates/seats_parts/modals.html | 0 | 0 |
| apk_payload/templates/seats_parts/topbar.html | 0 | 0 |
| apk_payload/templates/seats_parts/stats.html | 0 | 0 |
| apk_payload/templates/seats_parts/route_flow.html | 0 | 0 |
| apk_payload/templates/seats_parts/deck.html | 0 | 0 |
| apk_payload/templates/seats_parts/offload_confirm.html | 1 | 1 |
| apk_payload/templates/seats_parts/finish_trip_modal.html | 1 | 1 |
| templates/seats_parts/modals.html | 0 | 0 |
| templates/seats_parts/topbar.html | 0 | 0 |
| templates/seats_parts/stats.html | 0 | 0 |
| templates/seats_parts/route_flow.html | 0 | 0 |
| templates/seats_parts/deck.html | 0 | 0 |
| templates/seats_parts/offload_confirm.html | 1 | 1 |
| templates/seats_parts/finish_trip_modal.html | 1 | 1 |

## 16) Aynı HTML Dosyası İçinde Duplicate ID
| ID | Tekrar | Dosya |
| --- | --- | --- |
| tripGuardBackdrop | 2 | templates/index.html |
| tripGuardModal | 2 | templates/index.html |
| tripGuardGo | 2 | templates/index.html |
| tripGuardOk | 2 | templates/index.html |

## 17) Farklı Dosyalarda Aynı ID
Her zaman hata değildir ama modal/JS seçici çakışması yapabilir.
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
| approachAlert | 3 | android_app/app/src/main/python/templates/live_map.html, apk_payload/templates/live_map.html, templates/live_map.html |
| approachAlertClose | 3 | android_app/app/src/main/python/templates/live_map.html, apk_payload/templates/live_map.html, templates/live_map.html |
| approachAlertKicker | 3 | android_app/app/src/main/python/templates/live_map.html, apk_payload/templates/live_map.html, templates/live_map.html |
| approachAlertKm | 3 | android_app/app/src/main/python/templates/live_map.html, apk_payload/templates/live_map.html, templates/live_map.html |
| approachAlertOpen | 3 | android_app/app/src/main/python/templates/live_map.html, apk_payload/templates/live_map.html, templates/live_map.html |
| approachAlertSnooze | 3 | android_app/app/src/main/python/templates/live_map.html, apk_payload/templates/live_map.html, templates/live_map.html |
| approachAlertSpeak | 3 | android_app/app/src/main/python/templates/live_map.html, apk_payload/templates/live_map.html, templates/live_map.html |
| approachAlertText | 3 | android_app/app/src/main/python/templates/live_map.html, apk_payload/templates/live_map.html, templates/live_map.html |
| approachAlertTitle | 3 | android_app/app/src/main/python/templates/live_map.html, apk_payload/templates/live_map.html, templates/live_map.html |
| approachBackdrop | 3 | android_app/app/src/main/python/templates/seats_parts/modals.html, apk_payload/templates/seats_parts/modals.html, templates/seats_parts/modals.html |
| approachClose | 3 | android_app/app/src/main/python/templates/seats_parts/modals.html, apk_payload/templates/seats_parts/modals.html, templates/seats_parts/modals.html |
| approachInfo | 3 | android_app/app/src/main/python/templates/seats_parts/modals.html, apk_payload/templates/seats_parts/modals.html, templates/seats_parts/modals.html |
| approachList | 3 | android_app/app/src/main/python/templates/seats_parts/modals.html, apk_payload/templates/seats_parts/modals.html, templates/seats_parts/modals.html |
| approachModal | 3 | android_app/app/src/main/python/templates/seats_parts/modals.html, apk_payload/templates/seats_parts/modals.html, templates/seats_parts/modals.html |
| approachOffload | 3 | android_app/app/src/main/python/templates/seats_parts/modals.html, apk_payload/templates/seats_parts/modals.html, templates/seats_parts/modals.html |
| approachSnooze | 3 | android_app/app/src/main/python/templates/seats_parts/modals.html, apk_payload/templates/seats_parts/modals.html, templates/seats_parts/modals.html |
| approachTitle | 3 | android_app/app/src/main/python/templates/seats_parts/modals.html, apk_payload/templates/seats_parts/modals.html, templates/seats_parts/modals.html |
| attendant | 3 | android_app/app/src/main/python/templates/start_trip.html, apk_payload/templates/start_trip.html, templates/start_trip.html |
| avatarBox | 3 | android_app/app/src/main/python/templates/setup.html, apk_payload/templates/setup.html, templates/setup.html |
| avatarIcon | 3 | android_app/app/src/main/python/templates/setup.html, apk_payload/templates/setup.html, templates/setup.html |
| badgeBox | 3 | android_app/app/src/main/python/templates/add_route.html, apk_payload/templates/add_route.html, templates/add_route.html |
| badgeConfidence | 3 | android_app/app/src/main/python/templates/ai_console.html, apk_payload/templates/ai_console.html, templates/ai_console.html |
| badgeStatus | 3 | android_app/app/src/main/python/templates/ai_console.html, apk_payload/templates/ai_console.html, templates/ai_console.html |
| bagPhotoViewer | 3 | android_app/app/src/main/python/templates/continue_trip.html, apk_payload/templates/continue_trip.html, templates/continue_trip.html |
| bagViewerCaption | 3 | android_app/app/src/main/python/templates/continue_trip.html, apk_payload/templates/continue_trip.html, templates/continue_trip.html |
| bagViewerClose | 3 | android_app/app/src/main/python/templates/continue_trip.html, apk_payload/templates/continue_trip.html, templates/continue_trip.html |
| bagViewerImg | 3 | android_app/app/src/main/python/templates/continue_trip.html, apk_payload/templates/continue_trip.html, templates/continue_trip.html |
| bagViewerNext | 3 | android_app/app/src/main/python/templates/continue_trip.html, apk_payload/templates/continue_trip.html, templates/continue_trip.html |
| bagViewerPrev | 3 | android_app/app/src/main/python/templates/continue_trip.html, apk_payload/templates/continue_trip.html, templates/continue_trip.html |
| bagViewerTitle | 3 | android_app/app/src/main/python/templates/continue_trip.html, apk_payload/templates/continue_trip.html, templates/continue_trip.html |
| blueLight | 3 | android_app/app/src/main/python/templates/live_map.html, apk_payload/templates/live_map.html, templates/live_map.html |
| btnAcceptSuggestion | 3 | android_app/app/src/main/python/templates/ai_console.html, apk_payload/templates/ai_console.html, templates/ai_console.html |
| btnActionCancel | 3 | android_app/app/src/main/python/templates/ai_console.html, apk_payload/templates/ai_console.html, templates/ai_console.html |
| btnBagAdd | 3 | android_app/app/src/main/python/templates/seats_parts/modals.html, apk_payload/templates/seats_parts/modals.html, templates/seats_parts/modals.html |
| btnBagView | 3 | android_app/app/src/main/python/templates/seats_parts/modals.html, apk_payload/templates/seats_parts/modals.html, templates/seats_parts/modals.html |
| btnClearLog | 3 | android_app/app/src/main/python/templates/ai_console.html, apk_payload/templates/ai_console.html, templates/ai_console.html |
| btnDownload | 3 | android_app/app/src/main/python/templates/reports.html, apk_payload/templates/reports.html, templates/reports.html |
| btnEndTripCancel | 3 | android_app/app/src/main/python/templates/hesap.html, apk_payload/templates/hesap.html, templates/hesap.html |
| btnEndTripOpen | 3 | android_app/app/src/main/python/templates/hesap.html, apk_payload/templates/hesap.html, templates/hesap.html |
| btnEndTripYes | 3 | android_app/app/src/main/python/templates/hesap.html, apk_payload/templates/hesap.html, templates/hesap.html |
| btnFetch | 3 | android_app/app/src/main/python/templates/reports.html, apk_payload/templates/reports.html, templates/reports.html |
| btnFit | 3 | android_app/app/src/main/python/templates/live_map.html, apk_payload/templates/live_map.html, templates/live_map.html |
| btnLeft | 3 | android_app/app/src/main/python/templates/passenger_control.html, apk_payload/templates/passenger_control.html, templates/passenger_control.html |
| btnLocalCoordCheck | 3 | android_app/app/src/main/python/templates/route_edit.html, apk_payload/templates/route_edit.html, templates/route_edit.html |
| btnLocate | 3 | android_app/app/src/main/python/templates/live_map.html, apk_payload/templates/live_map.html, templates/live_map.html |
| btnMapFullscreen | 3 | android_app/app/src/main/python/templates/live_map.html, apk_payload/templates/live_map.html, templates/live_map.html |
| btnOffloadNow | 3 | android_app/app/src/main/python/templates/seats_parts/deck.html, apk_payload/templates/seats_parts/deck.html, templates/seats_parts/deck.html |
| btnOpenTeach | 3 | android_app/app/src/main/python/templates/ai_console.html, apk_payload/templates/ai_console.html, templates/ai_console.html |
| btnOps | 3 | android_app/app/src/main/python/templates/live_map.html, apk_payload/templates/live_map.html, templates/live_map.html |
| btnPreviewCancel | 3 | android_app/app/src/main/python/templates/ai_console.html, apk_payload/templates/ai_console.html, templates/ai_console.html |
| btnPreviewConfirm | 3 | android_app/app/src/main/python/templates/ai_console.html, apk_payload/templates/ai_console.html, templates/ai_console.html |
| btnRejectSuggestion | 3 | android_app/app/src/main/python/templates/ai_console.html, apk_payload/templates/ai_console.html, templates/ai_console.html |
| btnRoute | 3 | android_app/app/src/main/python/templates/live_map.html, apk_payload/templates/live_map.html, templates/live_map.html |
| btnRunAction | 3 | android_app/app/src/main/python/templates/ai_console.html, apk_payload/templates/ai_console.html, templates/ai_console.html |
| btnRunActionAndLearn | 3 | android_app/app/src/main/python/templates/ai_console.html, apk_payload/templates/ai_console.html, templates/ai_console.html |
| btnScrollLearned | 3 | android_app/app/src/main/python/templates/ai_console.html, apk_payload/templates/ai_console.html, templates/ai_console.html |
| btnSeatClose | 3 | android_app/app/src/main/python/templates/seats_parts/modals.html, apk_payload/templates/seats_parts/modals.html, templates/seats_parts/modals.html |
| btnSeatOffload | 3 | android_app/app/src/main/python/templates/seats_parts/modals.html, apk_payload/templates/seats_parts/modals.html, templates/seats_parts/modals.html |
| btnSeatSave | 3 | android_app/app/src/main/python/templates/seats_parts/modals.html, apk_payload/templates/seats_parts/modals.html, templates/seats_parts/modals.html |
| btnStart | 3 | android_app/app/src/main/python/templates/passenger_control.html, apk_payload/templates/passenger_control.html, templates/passenger_control.html |
| btnStop | 3 | android_app/app/src/main/python/templates/passenger_control.html, apk_payload/templates/passenger_control.html, templates/passenger_control.html |
| btnTeachAndRun | 3 | android_app/app/src/main/python/templates/ai_console.html, apk_payload/templates/ai_console.html, templates/ai_console.html |
| btnTeachCancel | 3 | android_app/app/src/main/python/templates/ai_console.html, apk_payload/templates/ai_console.html, templates/ai_console.html |
| btnTeachOnly | 3 | android_app/app/src/main/python/templates/ai_console.html, apk_payload/templates/ai_console.html, templates/ai_console.html |
| btnUndoLast | 3 | android_app/app/src/main/python/templates/ai_console.html, apk_payload/templates/ai_console.html, templates/ai_console.html |
| btnVoiceCancel | 3 | android_app/app/src/main/python/templates/ai_console.html, apk_payload/templates/ai_console.html, templates/ai_console.html |
| btnVoiceRetry | 3 | android_app/app/src/main/python/templates/ai_console.html, apk_payload/templates/ai_console.html, templates/ai_console.html |
| btnVoiceUseOnly | 3 | android_app/app/src/main/python/templates/ai_console.html, apk_payload/templates/ai_console.html, templates/ai_console.html |
| btnVoiceUseRun | 3 | android_app/app/src/main/python/templates/ai_console.html, apk_payload/templates/ai_console.html, templates/ai_console.html |
| bulkBackdrop | 3 | android_app/app/src/main/python/templates/seats_parts/modals.html, apk_payload/templates/seats_parts/modals.html, templates/seats_parts/modals.html |
| bulkClose | 3 | android_app/app/src/main/python/templates/seats_parts/modals.html, apk_payload/templates/seats_parts/modals.html, templates/seats_parts/modals.html |
| bulkCount | 3 | android_app/app/src/main/python/templates/seats_parts/modals.html, apk_payload/templates/seats_parts/modals.html, templates/seats_parts/modals.html |
| bulkFrom | 3 | android_app/app/src/main/python/templates/seats_parts/modals.html, apk_payload/templates/seats_parts/modals.html, templates/seats_parts/modals.html |
| bulkModal | 3 | android_app/app/src/main/python/templates/seats_parts/modals.html, apk_payload/templates/seats_parts/modals.html, templates/seats_parts/modals.html |
| bulkSave | 3 | android_app/app/src/main/python/templates/seats_parts/modals.html, apk_payload/templates/seats_parts/modals.html, templates/seats_parts/modals.html |
| bulkService | 3 | android_app/app/src/main/python/templates/seats_parts/modals.html, apk_payload/templates/seats_parts/modals.html, templates/seats_parts/modals.html |
| bulkTo | 3 | android_app/app/src/main/python/templates/seats_parts/modals.html, apk_payload/templates/seats_parts/modals.html, templates/seats_parts/modals.html |
| busy | 3 | android_app/app/src/main/python/templates/reports.html, apk_payload/templates/reports.html, templates/reports.html |
| captain1 | 3 | android_app/app/src/main/python/templates/start_trip.html, apk_payload/templates/start_trip.html, templates/start_trip.html |
| captain2 | 3 | android_app/app/src/main/python/templates/start_trip.html, apk_payload/templates/start_trip.html, templates/start_trip.html |

## 18) Aynı Dosya İçinde Tekrar Eden JS Fonksiyonları
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
| s | 5 | android_app/app/src/main/python/static/seats/seats.js |
| s | 5 | apk_payload/static/seats/seats.js |
| s | 5 | static/seats/seats.js |
| seatNo | 5 | android_app/app/src/main/python/static/continue/continue_trip_core.js |
| seatNo | 5 | static/continue/continue_trip_core.js |
| seatNo | 5 | apk_payload/templates/continue_trip.html |
| seats | 5 | android_app/app/src/main/python/static/seats/voice-commands.js |
| seats | 5 | apk_payload/static/seats/voice-commands.js |
| seats | 5 | static/seats/voice-commands.js |
| stop | 5 | android_app/app/src/main/python/static/continue/continue_trip_core.js |
| stop | 5 | static/continue/continue_trip_core.js |
| stop | 5 | apk_payload/templates/continue_trip.html |
| success | 5 | android_app/app/src/main/python/templates/settings_subscription.html |
| success | 5 | apk_payload/templates/settings_subscription.html |
| text | 5 | templates/ai_console.html |
| text | 5 | android_app/app/src/main/python/templates/ai_console.html |
| text | 5 | apk_payload/templates/ai_console.html |
| url | 5 | android_app/app/src/main/python/static/seats/seats.js |
| url | 5 | apk_payload/static/seats/seats.js |
| url | 5 | static/seats/seats.js |
| bagMsg | 4 | android_app/app/src/main/python/static/seats/voice-commands.js |
| bagMsg | 4 | apk_payload/static/seats/voice-commands.js |
| bagMsg | 4 | static/seats/voice-commands.js |
| bagTotal | 4 | android_app/app/src/main/python/static/continue/continue_trip_core.js |
| bagTotal | 4 | static/continue/continue_trip_core.js |
| bagTotal | 4 | apk_payload/templates/continue_trip.html |
| boot | 4 | android_app/app/src/main/python/static/live_map/muavin_live_map_extra.js |
| boot | 4 | apk_payload/static/live_map/muavin_live_map_extra.js |
| boot | 4 | static/live_map/muavin_live_map_extra.js |
| cancelBtn | 4 | android_app/app/src/main/python/static/continue/continue_trip_core.js |
| cancelBtn | 4 | static/continue/continue_trip_core.js |
| cancelBtn | 4 | apk_payload/templates/continue_trip.html |
| consignments | 4 | android_app/app/src/main/python/static/continue/continue_trip_core.js |
| consignments | 4 | static/continue/continue_trip_core.js |
| consignments | 4 | apk_payload/templates/continue_trip.html |
| d | 4 | android_app/app/src/main/python/static/live_map/muavin_live_map_extra.js |
| d | 4 | apk_payload/static/live_map/muavin_live_map_extra.js |
| d | 4 | static/live_map/muavin_live_map_extra.js |
| getMap | 4 | android_app/app/src/main/python/static/live_map/muavin_live_map_extra.js |
| getMap | 4 | apk_payload/static/live_map/muavin_live_map_extra.js |
| getMap | 4 | static/live_map/muavin_live_map_extra.js |
| intent | 4 | templates/ai_console.html |
| intent | 4 | android_app/app/src/main/python/templates/ai_console.html |
| intent | 4 | apk_payload/templates/ai_console.html |
| item | 4 | android_app/app/src/main/python/static/continue/continue_trip_core.js |
| item | 4 | static/continue/continue_trip_core.js |
| j | 4 | android_app/app/src/main/python/static/seats/voice-commands.js |
| j | 4 | apk_payload/static/seats/voice-commands.js |
| j | 4 | static/seats/voice-commands.js |
| modal | 4 | templates/settings_backup.html |
| msg | 4 | android_app/app/src/main/python/static/seats/seats.js |
| msg | 4 | apk_payload/static/seats/seats.js |
| msg | 4 | static/seats/seats.js |
| ok | 4 | android_app/app/src/main/python/static/seats/seats.js |
| ok | 4 | apk_payload/static/seats/seats.js |
| ok | 4 | static/seats/seats.js |
| out | 4 | android_app/app/src/main/python/static/seats/seats.js |
| out | 4 | apk_payload/static/seats/seats.js |
| out | 4 | static/seats/seats.js |
| ov | 4 | android_app/app/src/main/python/static/seats/patches/stop-flow-focus-patch.js |
| ov | 4 | apk_payload/static/seats/patches/stop-flow-focus-patch.js |
| ov | 4 | static/seats/patches/stop-flow-focus-patch.js |
| p | 4 | android_app/app/src/main/python/static/live_map/muavin_live_map_extra.js |
| p | 4 | apk_payload/static/live_map/muavin_live_map_extra.js |
| p | 4 | static/live_map/muavin_live_map_extra.js |
| parts | 4 | android_app/app/src/main/python/static/continue/continue_trip_core.js |
| parts | 4 | static/continue/continue_trip_core.js |
| parts | 4 | apk_payload/templates/continue_trip.html |
| raw | 4 | android_app/app/src/main/python/static/seats/seats.js |
| raw | 4 | apk_payload/static/seats/seats.js |
| raw | 4 | static/seats/seats.js |
| requestBtn | 4 | android_app/app/src/main/python/templates/settings_subscription.html |
| requestBtn | 4 | apk_payload/templates/settings_subscription.html |
| row | 4 | android_app/app/src/main/python/static/seats/seats.js |
| row | 4 | apk_payload/static/seats/seats.js |
| row | 4 | static/seats/seats.js |
| row | 4 | templates/ai_console.html |
| row | 4 | android_app/app/src/main/python/templates/ai_console.html |
| row | 4 | apk_payload/templates/ai_console.html |
| selected | 4 | android_app/app/src/main/python/static/seats/seats.js |

## 19) Farklı Dosyalarda Aynı JS Fonksiyonları
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
| obj | 9 | android_app/app/src/main/python/static/seats/patches/manual-ticket-system.js, android_app/app/src/main/python/static/seats/seats.js, android_app/app/src/main/python/templates/passenger_control.html, apk_payload/static/seats/patches/manual-ticket-system.js, apk_payload/static/seats/seats.js, apk_payload/templates/passenger_control.html, static/seats/patches/manual-ticket-system.js, static/seats/seats.js, templates/passenger_control.html |
| off | 9 | android_app/app/src/main/python/static/live_map/muavin_live_map_extra.js, android_app/app/src/main/python/static/seats/seats.js, android_app/app/src/main/python/templates/live_map.html, apk_payload/static/live_map/muavin_live_map_extra.js, apk_payload/static/seats/seats.js, apk_payload/templates/live_map.html, static/live_map/muavin_live_map_extra.js, static/seats/seats.js, templates/live_map.html |
| old | 9 | android_app/app/src/main/python/static/app.js, android_app/app/src/main/python/static/seats/patches/stop-flow-focus-patch.js, android_app/app/src/main/python/static/seats/seats.js, apk_payload/static/app.js, apk_payload/static/seats/patches/stop-flow-focus-patch.js, apk_payload/static/seats/seats.js, static/app.js, static/seats/patches/stop-flow-focus-patch.js, static/seats/seats.js |
| open | 9 | android_app/app/src/main/python/static/seats/patches/modal-bottom-nav-autohide.js, android_app/app/src/main/python/static/seats/patches/seat-simple-ui-pack.js, android_app/app/src/main/python/templates/live_map.html, apk_payload/static/seats/patches/modal-bottom-nav-autohide.js, apk_payload/static/seats/patches/seat-simple-ui-pack.js, apk_payload/templates/live_map.html, static/seats/patches/modal-bottom-nav-autohide.js, static/seats/patches/seat-simple-ui-pack.js, templates/live_map.html |
| out | 9 | android_app/app/src/main/python/static/live_map/muavin_live_map_extra.js, android_app/app/src/main/python/static/seats/seats.js, android_app/app/src/main/python/static/seats/voice-commands.js, apk_payload/static/live_map/muavin_live_map_extra.js, apk_payload/static/seats/seats.js, apk_payload/static/seats/voice-commands.js, static/live_map/muavin_live_map_extra.js, static/seats/seats.js, static/seats/voice-commands.js |
| params | 9 | android_app/app/src/main/python/static/seats/drive-controls.js, android_app/app/src/main/python/templates/live_map.html, android_app/app/src/main/python/templates/setup.html, apk_payload/static/seats/drive-controls.js, apk_payload/templates/live_map.html, apk_payload/templates/setup.html, static/seats/drive-controls.js, templates/live_map.html, templates/setup.html |
| parcelCt | 9 | android_app/app/src/main/python/static/seats/seats.js, android_app/app/src/main/python/static/seats/voice-commands.js, android_app/app/src/main/python/templates/ai_console.html, apk_payload/static/seats/seats.js, apk_payload/static/seats/voice-commands.js, apk_payload/templates/ai_console.html, static/seats/seats.js, static/seats/voice-commands.js, templates/ai_console.html |
| seatCt | 9 | android_app/app/src/main/python/static/seats/seats.js, android_app/app/src/main/python/static/seats/voice-commands.js, android_app/app/src/main/python/templates/ai_console.html, apk_payload/static/seats/seats.js, apk_payload/static/seats/voice-commands.js, apk_payload/templates/ai_console.html, static/seats/seats.js, static/seats/voice-commands.js, templates/ai_console.html |
| seatEl | 9 | android_app/app/src/main/python/static/app.js, android_app/app/src/main/python/static/seats/patches/manual-ticket-system.js, android_app/app/src/main/python/static/seats/seats.js, apk_payload/static/app.js, apk_payload/static/seats/patches/manual-ticket-system.js, apk_payload/static/seats/seats.js, static/app.js, static/seats/patches/manual-ticket-system.js, static/seats/seats.js |
| setText | 9 | android_app/app/src/main/python/static/continue/continue_flow_refresh.js, android_app/app/src/main/python/static/continue/continue_live_diagnostics.js, android_app/app/src/main/python/static/continue/continue_trip_core.js, android_app/app/src/main/python/static/seats/seats.js, apk_payload/static/seats/seats.js, static/continue/continue_flow_refresh.js, static/continue/continue_live_diagnostics.js, static/continue/continue_trip_core.js, static/seats/seats.js |
| sheet | 9 | android_app/app/src/main/python/static/continue/continue_trip_core.js, android_app/app/src/main/python/templates/hesap.html, android_app/app/src/main/python/templates/index.html, apk_payload/templates/continue_trip.html, apk_payload/templates/hesap.html, apk_payload/templates/index.html, static/continue/continue_trip_core.js, templates/hesap.html, templates/index.html |
| standingCt | 9 | android_app/app/src/main/python/static/seats/seats.js, android_app/app/src/main/python/static/seats/voice-commands.js, android_app/app/src/main/python/templates/ai_console.html, apk_payload/static/seats/seats.js, apk_payload/static/seats/voice-commands.js, apk_payload/templates/ai_console.html, static/seats/seats.js, static/seats/voice-commands.js, templates/ai_console.html |
| stopEl | 9 | android_app/app/src/main/python/static/continue/continue_trip_core.js, android_app/app/src/main/python/static/seats/patches/seat-simple-ui-pack.js, android_app/app/src/main/python/templates/seats_parts/offload_confirm.html, apk_payload/static/seats/patches/seat-simple-ui-pack.js, apk_payload/templates/continue_trip.html, apk_payload/templates/seats_parts/offload_confirm.html, static/continue/continue_trip_core.js, static/seats/patches/seat-simple-ui-pack.js, templates/seats_parts/offload_confirm.html |
| titleEl | 9 | android_app/app/src/main/python/static/continue/continue_trip_core.js, android_app/app/src/main/python/templates/hesap.html, android_app/app/src/main/python/templates/route_schedule_edit.html, apk_payload/templates/continue_trip.html, apk_payload/templates/hesap.html, apk_payload/templates/route_schedule_edit.html, static/continue/continue_trip_core.js, templates/hesap.html, templates/route_schedule_edit.html |
| tr | 9 | android_app/app/src/main/python/templates/ai_console.html, android_app/app/src/main/python/templates/reports.html, android_app/app/src/main/python/templates/route_stops.html, apk_payload/templates/ai_console.html, apk_payload/templates/reports.html, apk_payload/templates/route_stops.html, templates/ai_console.html, templates/reports.html, templates/route_stops.html |
| avg | 8 | android_app/app/src/main/python/static/continue/continue_trip_core.js, android_app/app/src/main/python/static/seats/seats.js, android_app/app/src/main/python/templates/reports.html, apk_payload/static/seats/seats.js, apk_payload/templates/reports.html, static/continue/continue_trip_core.js, static/seats/seats.js, templates/reports.html |
| idx | 8 | android_app/app/src/main/python/static/continue/continue_flow_refresh.js, android_app/app/src/main/python/static/seats/seats.js, android_app/app/src/main/python/templates/ai_console.html, apk_payload/static/seats/seats.js, apk_payload/templates/ai_console.html, static/continue/continue_flow_refresh.js, static/seats/seats.js, templates/ai_console.html |
| kmh | 8 | android_app/app/src/main/python/static/continue/continue_trip_core.js, android_app/app/src/main/python/static/seats/seats.js, android_app/app/src/main/python/templates/live_map.html, apk_payload/static/seats/seats.js, apk_payload/templates/live_map.html, static/continue/continue_trip_core.js, static/seats/seats.js, templates/live_map.html |
| overlay | 8 | android_app/app/src/main/python/static/continue/continue_trip_core.js, android_app/app/src/main/python/templates/continue_trip.html, android_app/app/src/main/python/templates/route_schedule_edit.html, apk_payload/templates/continue_trip.html, apk_payload/templates/route_schedule_edit.html, static/continue/continue_trip_core.js, templates/continue_trip.html, templates/route_schedule_edit.html |
| pad | 8 | android_app/app/src/main/python/static/continue/continue_trip_core.js, android_app/app/src/main/python/static/continue/continue_trip_ui.js, android_app/app/src/main/python/templates/start_trip.html, apk_payload/templates/continue_trip.html, apk_payload/templates/start_trip.html, static/continue/continue_trip_core.js, static/continue/continue_trip_ui.js, templates/start_trip.html |
| prev | 8 | android_app/app/src/main/python/static/continue/continue_trip_core.js, android_app/app/src/main/python/static/seats/seats-time-prayer.js, android_app/app/src/main/python/static/seats/seats.js, apk_payload/static/seats/seats-time-prayer.js, apk_payload/static/seats/seats.js, static/continue/continue_trip_core.js, static/seats/seats-time-prayer.js, static/seats/seats.js |
| selectedText | 8 | android_app/app/src/main/python/templates/hesap.html, android_app/app/src/main/python/templates/route_schedule_edit.html, android_app/app/src/main/python/templates/settings_subscription.html, apk_payload/templates/hesap.html, apk_payload/templates/route_schedule_edit.html, apk_payload/templates/settings_subscription.html, templates/hesap.html, templates/route_schedule_edit.html |
| start | 8 | android_app/app/src/main/python/static/continue/continue_trip_core.js, android_app/app/src/main/python/static/live_map/muavin_live_map_extra.js, android_app/app/src/main/python/static/seats/seats.js, apk_payload/static/live_map/muavin_live_map_extra.js, apk_payload/static/seats/seats.js, static/continue/continue_trip_core.js, static/live_map/muavin_live_map_extra.js, static/seats/seats.js |
| tripId | 8 | android_app/app/src/main/python/static/continue/continue_live_diagnostics.js, android_app/app/src/main/python/static/continue/continue_trip_core.js, android_app/app/src/main/python/static/seats/seats.js, apk_payload/static/seats/seats.js, apk_payload/templates/continue_trip.html, static/continue/continue_live_diagnostics.js, static/continue/continue_trip_core.js, static/seats/seats.js |
| L | 7 | _unused_review/static/vendor/jquery/jquery-3.7.1.min.js, android_app/app/src/main/python/static/vendor/bootstrap/bootstrap.bundle.min.js, android_app/app/src/main/python/templates/reports.html, apk_payload/static/vendor/bootstrap/bootstrap.bundle.min.js, apk_payload/templates/reports.html, static/vendor/bootstrap/bootstrap.bundle.min.js, templates/reports.html |
| P | 7 | _unused_review/static/vendor/jquery/jquery-3.7.1.min.js, android_app/app/src/main/python/static/vendor/bootstrap/bootstrap.bundle.min.js, android_app/app/src/main/python/templates/reports.html, apk_payload/static/vendor/bootstrap/bootstrap.bundle.min.js, apk_payload/templates/reports.html, static/vendor/bootstrap/bootstrap.bundle.min.js, templates/reports.html |
| blob | 7 | android_app/app/src/main/python/templates/reports.html, android_app/app/src/main/python/templates/trip_report.html, apk_payload/templates/reports.html, apk_payload/templates/trip_report.html, backups/apk_sync_20260520_234501/trip_report.html, templates/reports.html, templates/trip_report.html |
| distKm | 7 | android_app/app/src/main/python/static/continue/continue_flow_refresh.js, android_app/app/src/main/python/static/continue/continue_trip_core.js, android_app/app/src/main/python/static/seats/seats.js, apk_payload/static/seats/seats.js, static/continue/continue_flow_refresh.js, static/continue/continue_trip_core.js, static/seats/seats.js |
| dock | 7 | android_app/app/src/main/python/static/live_map/muavin_live_map_extra.js, android_app/app/src/main/python/templates/seats.html, apk_payload/static/live_map/muavin_live_map_extra.js, apk_payload/templates/seats.html, backups/apk_sync_20260520_234501/seats.html, static/live_map/muavin_live_map_extra.js, templates/seats.html |
| e | 7 | _unused_review/static/vendor/jquery/jquery-3.7.1.min.js, android_app/app/src/main/python/static/vendor/bootstrap/bootstrap.bundle.min.js, android_app/app/src/main/python/templates/route_stops.html, apk_payload/static/vendor/bootstrap/bootstrap.bundle.min.js, apk_payload/templates/route_stops.html, static/vendor/bootstrap/bootstrap.bundle.min.js, templates/route_stops.html |
| end | 7 | android_app/app/src/main/python/static/live_map/muavin_live_map_extra.js, android_app/app/src/main/python/templates/seats.html, apk_payload/static/live_map/muavin_live_map_extra.js, apk_payload/templates/seats.html, backups/apk_sync_20260520_234501/seats.html, static/live_map/muavin_live_map_extra.js, templates/seats.html |
| gpsKm | 7 | android_app/app/src/main/python/static/continue/continue_live_diagnostics.js, android_app/app/src/main/python/static/continue/continue_trip_core.js, android_app/app/src/main/python/static/seats/seats.js, apk_payload/static/seats/seats.js, static/continue/continue_live_diagnostics.js, static/continue/continue_trip_core.js, static/seats/seats.js |
| head | 7 | android_app/app/src/main/python/static/continue/continue_live_diagnostics.js, android_app/app/src/main/python/static/continue/continue_trip_ui.js, android_app/app/src/main/python/templates/hesap.html, apk_payload/templates/hesap.html, static/continue/continue_live_diagnostics.js, static/continue/continue_trip_ui.js, templates/hesap.html |
| isDriveOn | 7 | android_app/app/src/main/python/static/seats/drive-controls.js, android_app/app/src/main/python/templates/seats.html, apk_payload/static/seats/drive-controls.js, apk_payload/templates/seats.html, backups/apk_sync_20260520_234501/seats.html, static/seats/drive-controls.js, templates/seats.html |
| lines | 7 | android_app/app/src/main/python/templates/hesap.html, android_app/app/src/main/python/templates/trip_report.html, apk_payload/templates/hesap.html, apk_payload/templates/trip_report.html, backups/apk_sync_20260520_234501/trip_report.html, templates/hesap.html, templates/trip_report.html |
| o | 7 | _unused_review/static/vendor/jquery/jquery-3.7.1.min.js, android_app/app/src/main/python/static/seats/seats.js, android_app/app/src/main/python/static/vendor/bootstrap/bootstrap.bundle.min.js, apk_payload/static/seats/seats.js, apk_payload/static/vendor/bootstrap/bootstrap.bundle.min.js, static/seats/seats.js, static/vendor/bootstrap/bootstrap.bundle.min.js |
| openPrintDialog | 7 | android_app/app/src/main/python/templates/hesap.html, android_app/app/src/main/python/templates/trip_report.html, apk_payload/templates/hesap.html, apk_payload/templates/trip_report.html, backups/apk_sync_20260520_234501/trip_report.html, templates/hesap.html, templates/trip_report.html |
| pax | 7 | android_app/app/src/main/python/templates/reports.html, android_app/app/src/main/python/templates/trip_report.html, apk_payload/templates/reports.html, apk_payload/templates/trip_report.html, backups/apk_sync_20260520_234501/trip_report.html, templates/reports.html, templates/trip_report.html |
| seat | 7 | android_app/app/src/main/python/static/seats/seats.js, android_app/app/src/main/python/templates/trip_report.html, apk_payload/static/seats/seats.js, apk_payload/templates/trip_report.html, backups/apk_sync_20260520_234501/trip_report.html, static/seats/seats.js, templates/trip_report.html |
| sig | 7 | android_app/app/src/main/python/static/continue/continue_flow_refresh.js, android_app/app/src/main/python/static/continue/continue_trip_core.js, android_app/app/src/main/python/static/seats/patches/manual-ticket-system.js, apk_payload/static/seats/patches/manual-ticket-system.js, static/continue/continue_flow_refresh.js, static/continue/continue_trip_core.js, static/seats/patches/manual-ticket-system.js |
| toRad | 7 | android_app/app/src/main/python/static/continue/continue_flow_refresh.js, android_app/app/src/main/python/static/continue/continue_trip_core.js, android_app/app/src/main/python/static/seats/seats.js, apk_payload/static/seats/seats.js, static/continue/continue_flow_refresh.js, static/continue/continue_trip_core.js, static/seats/seats.js |
| value | 7 | android_app/app/src/main/python/templates/ai_console.html, android_app/app/src/main/python/templates/route_schedule_edit.html, apk_payload/templates/ai_console.html, apk_payload/templates/route_schedule_edit.html, templates/ai_console.html, templates/route_schedule_edit.html, templates/settings_password.html |
| $$ | 6 | android_app/app/src/main/python/static/seats/seats.js, android_app/app/src/main/python/templates/ai_console.html, apk_payload/static/seats/seats.js, apk_payload/templates/ai_console.html, static/seats/seats.js, templates/ai_console.html |
| KEY | 6 | android_app/app/src/main/python/static/seats/patches/top-sound-toggle.js, android_app/app/src/main/python/static/seats/voice-tts.js, apk_payload/static/seats/patches/top-sound-toggle.js, apk_payload/static/seats/voice-tts.js, static/seats/patches/top-sound-toggle.js, static/seats/voice-tts.js |
| SR | 6 | android_app/app/src/main/python/static/seats/voice-commands.js, android_app/app/src/main/python/templates/ai_console.html, apk_payload/static/seats/voice-commands.js, apk_payload/templates/ai_console.html, static/seats/voice-commands.js, templates/ai_console.html |
| add | 6 | android_app/app/src/main/python/static/seats/bags.js, android_app/app/src/main/python/static/seats/patches/stop-flow-focus-patch.js, apk_payload/static/seats/bags.js, apk_payload/static/seats/patches/stop-flow-focus-patch.js, static/seats/bags.js, static/seats/patches/stop-flow-focus-patch.js |
| alertStop | 6 | android_app/app/src/main/python/static/seats/patches/stop-flow-focus-patch.js, android_app/app/src/main/python/static/seats/voice-commands.js, apk_payload/static/seats/patches/stop-flow-focus-patch.js, apk_payload/static/seats/voice-commands.js, static/seats/patches/stop-flow-focus-patch.js, static/seats/voice-commands.js |
| assigned | 6 | android_app/app/src/main/python/static/seats/seats.js, android_app/app/src/main/python/templates/passenger_control.html, apk_payload/static/seats/seats.js, apk_payload/templates/passenger_control.html, static/seats/seats.js, templates/passenger_control.html |
| bagSeats | 6 | android_app/app/src/main/python/static/continue/continue_trip_core.js, android_app/app/src/main/python/static/seats/bags.js, apk_payload/static/seats/bags.js, apk_payload/templates/continue_trip.html, static/continue/continue_trip_core.js, static/seats/bags.js |
| cRect | 6 | android_app/app/src/main/python/static/live_map/muavin_live_map_extra.js, android_app/app/src/main/python/static/seats/patches/seat-layout-fab-pack.js, apk_payload/static/live_map/muavin_live_map_extra.js, apk_payload/static/seats/patches/seat-layout-fab-pack.js, static/live_map/muavin_live_map_extra.js, static/seats/patches/seat-layout-fab-pack.js |
| cancelBtn | 6 | android_app/app/src/main/python/static/continue/continue_trip_core.js, android_app/app/src/main/python/templates/seats_parts/offload_confirm.html, apk_payload/templates/continue_trip.html, apk_payload/templates/seats_parts/offload_confirm.html, static/continue/continue_trip_core.js, templates/seats_parts/offload_confirm.html |
| cb | 6 | android_app/app/src/main/python/static/seats/drive-controls.js, android_app/app/src/main/python/static/seats/seats.js, apk_payload/static/seats/drive-controls.js, apk_payload/static/seats/seats.js, static/seats/drive-controls.js, static/seats/seats.js |
| cleanStopName | 6 | android_app/app/src/main/python/static/seats/patches/stop-flow-focus-patch.js, android_app/app/src/main/python/static/seats/patches/stop-selected-toast.js, apk_payload/static/seats/patches/stop-flow-focus-patch.js, apk_payload/static/seats/patches/stop-selected-toast.js, static/seats/patches/stop-flow-focus-patch.js, static/seats/patches/stop-selected-toast.js |
| close | 6 | android_app/app/src/main/python/templates/index.html, android_app/app/src/main/python/templates/seats_parts/offload_confirm.html, apk_payload/templates/index.html, apk_payload/templates/seats_parts/offload_confirm.html, templates/index.html, templates/seats_parts/offload_confirm.html |
| closeSheet | 6 | android_app/app/src/main/python/static/continue/continue_trip_core.js, android_app/app/src/main/python/templates/index.html, apk_payload/templates/continue_trip.html, apk_payload/templates/index.html, static/continue/continue_trip_core.js, templates/index.html |
| code | 6 | android_app/app/src/main/python/static/continue/continue_trip_core.js, android_app/app/src/main/python/templates/settings_recovery.html, apk_payload/templates/continue_trip.html, apk_payload/templates/settings_recovery.html, static/continue/continue_trip_core.js, templates/settings_recovery.html |
| countEl | 6 | android_app/app/src/main/python/static/live_map/muavin_live_map_extra.js, android_app/app/src/main/python/templates/live_map.html, apk_payload/static/live_map/muavin_live_map_extra.js, apk_payload/templates/live_map.html, static/live_map/muavin_live_map_extra.js, templates/live_map.html |
| cs | 6 | android_app/app/src/main/python/static/seats/patches/modal-bottom-nav-autohide.js, android_app/app/src/main/python/static/seats/patches/seat-simple-ui-pack.js, apk_payload/static/seats/patches/modal-bottom-nav-autohide.js, apk_payload/static/seats/patches/seat-simple-ui-pack.js, static/seats/patches/modal-bottom-nav-autohide.js, static/seats/patches/seat-simple-ui-pack.js |
| csrfToken | 6 | android_app/app/src/main/python/static/continue/continue_trip_core.js, android_app/app/src/main/python/static/seats/voice-commands.js, apk_payload/static/seats/voice-commands.js, apk_payload/templates/continue_trip.html, static/continue/continue_trip_core.js, static/seats/voice-commands.js |
| ct | 6 | android_app/app/src/main/python/static/seats/seats.js, android_app/app/src/main/python/templates/ai_console.html, apk_payload/static/seats/seats.js, apk_payload/templates/ai_console.html, static/seats/seats.js, templates/ai_console.html |
| currentLatLng | 6 | android_app/app/src/main/python/static/live_map/muavin_live_map_extra.js, android_app/app/src/main/python/templates/live_map.html, apk_payload/static/live_map/muavin_live_map_extra.js, apk_payload/templates/live_map.html, static/live_map/muavin_live_map_extra.js, templates/live_map.html |
| date | 6 | android_app/app/src/main/python/static/seats/seats-time-prayer.js, android_app/app/src/main/python/templates/hesap.html, apk_payload/static/seats/seats-time-prayer.js, apk_payload/templates/hesap.html, static/seats/seats-time-prayer.js, templates/hesap.html |
| diff | 6 | android_app/app/src/main/python/static/seats/seats.js, android_app/app/src/main/python/templates/onboarding.html, apk_payload/static/seats/seats.js, apk_payload/templates/onboarding.html, static/seats/seats.js, templates/onboarding.html |
| dt | 6 | _unused_review/static/vendor/jquery/jquery-3.7.1.min.js, android_app/app/src/main/python/static/continue/continue_trip_core.js, android_app/app/src/main/python/templates/start_trip.html, apk_payload/templates/start_trip.html, static/continue/continue_trip_core.js, templates/start_trip.html |
| dx | 6 | android_app/app/src/main/python/static/live_map/muavin_live_map_extra.js, android_app/app/src/main/python/templates/live_map.html, apk_payload/static/live_map/muavin_live_map_extra.js, apk_payload/templates/live_map.html, static/live_map/muavin_live_map_extra.js, templates/live_map.html |
| dy | 6 | android_app/app/src/main/python/static/live_map/muavin_live_map_extra.js, android_app/app/src/main/python/templates/live_map.html, apk_payload/static/live_map/muavin_live_map_extra.js, apk_payload/templates/live_map.html, static/live_map/muavin_live_map_extra.js, templates/live_map.html |
| emptySeats | 6 | android_app/app/src/main/python/static/seats/voice-commands.js, android_app/app/src/main/python/templates/ai_console.html, apk_payload/static/seats/voice-commands.js, apk_payload/templates/ai_console.html, static/seats/voice-commands.js, templates/ai_console.html |
| failed | 6 | android_app/app/src/main/python/static/seats/patches/manual-ticket-system.js, android_app/app/src/main/python/static/seats/voice-commands.js, apk_payload/static/seats/patches/manual-ticket-system.js, apk_payload/static/seats/voice-commands.js, static/seats/patches/manual-ticket-system.js, static/seats/voice-commands.js |
| findStopMention | 6 | android_app/app/src/main/python/static/seats/voice-commands.js, android_app/app/src/main/python/templates/ai_console.html, apk_payload/static/seats/voice-commands.js, apk_payload/templates/ai_console.html, static/seats/voice-commands.js, templates/ai_console.html |
| flow | 6 | android_app/app/src/main/python/static/continue/continue_flow_refresh.js, android_app/app/src/main/python/templates/seats.html, apk_payload/templates/seats.html, backups/apk_sync_20260520_234501/seats.html, static/continue/continue_flow_refresh.js, templates/seats.html |
| found | 6 | android_app/app/src/main/python/static/seats/patches/stop-flow-focus-patch.js, android_app/app/src/main/python/templates/ai_console.html, apk_payload/static/seats/patches/stop-flow-focus-patch.js, apk_payload/templates/ai_console.html, static/seats/patches/stop-flow-focus-patch.js, templates/ai_console.html |
| fromDefault | 6 | android_app/app/src/main/python/static/seats/seats.js, android_app/app/src/main/python/static/seats/standing.js, apk_payload/static/seats/seats.js, apk_payload/static/seats/standing.js, static/seats/seats.js, static/seats/standing.js |
| fv | 6 | android_app/app/src/main/python/templates/fare_admin.html, android_app/app/src/main/python/templates/fare_query.html, apk_payload/templates/fare_admin.html, apk_payload/templates/fare_query.html, templates/fare_admin.html, templates/fare_query.html |
| g | 6 | android_app/app/src/main/python/static/continue/continue_trip_core.js, android_app/app/src/main/python/static/seats/voice-commands.js, apk_payload/static/seats/voice-commands.js, apk_payload/templates/continue_trip.html, static/continue/continue_trip_core.js, static/seats/voice-commands.js |
| headers | 6 | android_app/app/src/main/python/static/continue/continue_trip_core.js, android_app/app/src/main/python/templates/ai_console.html, apk_payload/templates/ai_console.html, apk_payload/templates/continue_trip.html, static/continue/continue_trip_core.js, templates/ai_console.html |
| iconFor | 6 | android_app/app/src/main/python/templates/live_map.html, android_app/app/src/main/python/templates/route_edit.html, apk_payload/templates/live_map.html, apk_payload/templates/route_edit.html, templates/live_map.html, templates/route_edit.html |
| index | 6 | android_app/app/src/main/python/static/continue/continue_trip_ui.js, android_app/app/src/main/python/templates/onboarding.html, apk_payload/templates/continue_trip.html, apk_payload/templates/onboarding.html, static/continue/continue_trip_ui.js, templates/onboarding.html |
| init | 6 | android_app/app/src/main/python/static/seats/seats.js, android_app/app/src/main/python/templates/ai_console.html, apk_payload/static/seats/seats.js, apk_payload/templates/ai_console.html, static/seats/seats.js, templates/ai_console.html |
| intent | 6 | android_app/app/src/main/python/static/seats/voice-commands.js, android_app/app/src/main/python/templates/ai_console.html, apk_payload/static/seats/voice-commands.js, apk_payload/templates/ai_console.html, static/seats/voice-commands.js, templates/ai_console.html |
| isDone | 6 | android_app/app/src/main/python/static/live_map/muavin_live_map_extra.js, android_app/app/src/main/python/static/seats/seats.js, apk_payload/static/live_map/muavin_live_map_extra.js, apk_payload/static/seats/seats.js, static/live_map/muavin_live_map_extra.js, static/seats/seats.js |

## 20) Aynı Dosya İçinde Tekrar Eden Python Fonksiyonları
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

## 21) Farklı Dosyalarda Aynı Python Fonksiyonları
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
| schedule_items_for_profile | 4 | android_app/app/src/main/python/app.py, apk_payload/app.py, app.py, backups/apk_sync_20260520_234501/app.py |
| schedule_profile_get | 4 | android_app/app/src/main/python/app.py, apk_payload/app.py, app.py, backups/apk_sync_20260520_234501/app.py |
| schedule_profiles_for_route | 4 | android_app/app/src/main/python/app.py, apk_payload/app.py, app.py, backups/apk_sync_20260520_234501/app.py |
| seats_count_for_stop | 4 | android_app/app/src/main/python/app.py, apk_payload/app.py, app.py, backups/apk_sync_20260520_234501/app.py |
| seats_page | 4 | android_app/app/src/main/python/modules/seats_panel.py, apk_payload/modules/seats_panel.py, backups/apk_sync_20260520_234501/seats_panel.py, modules/seats_panel.py |
| set_active_trip | 4 | android_app/app/src/main/python/app.py, apk_payload/app.py, app.py, backups/apk_sync_20260520_234501/app.py |
| set_admin_password | 4 | android_app/app/src/main/python/app.py, apk_payload/app.py, app.py, backups/apk_sync_20260520_234501/app.py |
| set_recovery_code | 4 | android_app/app/src/main/python/app.py, apk_payload/app.py, app.py, backups/apk_sync_20260520_234501/app.py |
| set_route | 4 | android_app/app/src/main/python/app.py, apk_payload/app.py, app.py, backups/apk_sync_20260520_234501/app.py |
| settings_get | 4 | android_app/app/src/main/python/app.py, apk_payload/app.py, app.py, backups/apk_sync_20260520_234501/app.py |
| settings_set | 4 | android_app/app/src/main/python/app.py, apk_payload/app.py, app.py, backups/apk_sync_20260520_234501/app.py |
| trip_report_csv | 4 | android_app/app/src/main/python/modules/trip_report_builder.py, apk_payload/modules/trip_report_builder.py, backups/apk_sync_20260520_234501/trip_report_builder.py, modules/trip_report_builder.py |
| trip_report_page | 4 | android_app/app/src/main/python/app.py, apk_payload/app.py, app.py, backups/apk_sync_20260520_234501/app.py |
| trip_report_text | 4 | android_app/app/src/main/python/modules/trip_report_builder.py, apk_payload/modules/trip_report_builder.py, backups/apk_sync_20260520_234501/trip_report_builder.py, modules/trip_report_builder.py |
| trip_start | 4 | android_app/app/src/main/python/app.py, apk_payload/app.py, app.py, backups/apk_sync_20260520_234501/app.py |
| upsert_live_runtime_state | 4 | android_app/app/src/main/python/app.py, apk_payload/app.py, app.py, backups/apk_sync_20260520_234501/app.py |
| valid_hhmm | 4 | android_app/app/src/main/python/app.py, apk_payload/app.py, app.py, backups/apk_sync_20260520_234501/app.py |
| validate_seat_no | 4 | android_app/app/src/main/python/app.py, apk_payload/app.py, app.py, backups/apk_sync_20260520_234501/app.py |
| validate_stop_for_active_trip | 4 | android_app/app/src/main/python/app.py, apk_payload/app.py, app.py, backups/apk_sync_20260520_234501/app.py |
| validate_stop_for_trip | 4 | android_app/app/src/main/python/app.py, apk_payload/app.py, app.py, backups/apk_sync_20260520_234501/app.py |
| verify_admin_password | 4 | android_app/app/src/main/python/app.py, apk_payload/app.py, app.py, backups/apk_sync_20260520_234501/app.py |
| verify_recovery_code | 4 | android_app/app/src/main/python/app.py, apk_payload/app.py, app.py, backups/apk_sync_20260520_234501/app.py |
| _back_url | 3 | android_app/app/src/main/python/modules/bags/__init__.py, apk_payload/modules/bags/__init__.py, modules/bags/__init__.py |
| _best_route_for_coords | 3 | android_app/app/src/main/python/modules/coords_panel.py, apk_payload/modules/coords_panel.py, modules/coords_panel.py |
| _check_csrf | 3 | android_app/app/src/main/python/modules/bags/__init__.py, apk_payload/modules/bags/__init__.py, modules/bags/__init__.py |
| _clamp_bag_count | 3 | android_app/app/src/main/python/modules/bags/__init__.py, apk_payload/modules/bags/__init__.py, modules/bags/__init__.py |
| _coords_items_for_route | 3 | android_app/app/src/main/python/modules/coords_panel.py, apk_payload/modules/coords_panel.py, modules/coords_panel.py |
| _coords_norm_text | 3 | android_app/app/src/main/python/modules/coords_panel.py, apk_payload/modules/coords_panel.py, modules/coords_panel.py |
| _get_csrf | 3 | android_app/app/src/main/python/modules/bags/__init__.py, apk_payload/modules/bags/__init__.py, modules/bags/__init__.py |
| _is_image | 3 | android_app/app/src/main/python/modules/bags/__init__.py, apk_payload/modules/bags/__init__.py, modules/bags/__init__.py |
| _normalize_next | 3 | android_app/app/src/main/python/modules/bags/__init__.py, apk_payload/modules/bags/__init__.py, modules/bags/__init__.py |
| _parse_stops_local | 3 | android_app/app/src/main/python/modules/coords_panel.py, apk_payload/modules/coords_panel.py, modules/coords_panel.py |
| _pick_default_side | 3 | android_app/app/src/main/python/modules/bags/__init__.py, apk_payload/modules/bags/__init__.py, modules/bags/__init__.py |
| _route_name_variants | 3 | android_app/app/src/main/python/modules/coords_panel.py, apk_payload/modules/coords_panel.py, modules/coords_panel.py |
| _save_route_stop_coord_local | 3 | android_app/app/src/main/python/modules/coords_panel.py, apk_payload/modules/coords_panel.py, modules/coords_panel.py |
| _scan_counts | 3 | android_app/app/src/main/python/modules/bags/__init__.py, apk_payload/modules/bags/__init__.py, modules/bags/__init__.py |
| _side_from_filename | 3 | android_app/app/src/main/python/modules/bags/__init__.py, apk_payload/modules/bags/__init__.py, modules/bags/__init__.py |
| _side_icon | 3 | android_app/app/src/main/python/modules/bags/__init__.py, apk_payload/modules/bags/__init__.py, modules/bags/__init__.py |
| _side_label | 3 | android_app/app/src/main/python/modules/bags/__init__.py, apk_payload/modules/bags/__init__.py, modules/bags/__init__.py |
| activate_subscription_manually | 3 | android_app/app/src/main/python/modules/subscription_panel.py, apk_payload/modules/subscription_panel.py, modules/subscription_panel.py |
| active_route_name | 3 | android_app/app/src/main/python/modules/coords_panel.py, apk_payload/modules/coords_panel.py, modules/coords_panel.py |
| add_file_to_zip | 3 | android_app/app/src/main/python/modules/backup_panel.py, apk_payload/modules/backup_panel.py, modules/backup_panel.py |
| add_folder_to_zip | 3 | android_app/app/src/main/python/modules/backup_panel.py, apk_payload/modules/backup_panel.py, modules/backup_panel.py |
| add_route | 3 | android_app/app/src/main/python/modules/routes_panel.py, apk_payload/modules/routes_panel.py, modules/routes_panel.py |
| ai_answer_query | 3 | android_app/app/src/main/python/modules/ai_panel.py, apk_payload/modules/ai_panel.py, modules/ai_panel.py |
| ai_execute_intent | 3 | android_app/app/src/main/python/modules/ai_panel.py, apk_payload/modules/ai_panel.py, modules/ai_panel.py |
| ai_extract_amount | 3 | android_app/app/src/main/python/modules/ai_panel.py, apk_payload/modules/ai_panel.py, modules/ai_panel.py |
| ai_extract_count | 3 | android_app/app/src/main/python/modules/ai_panel.py, apk_payload/modules/ai_panel.py, modules/ai_panel.py |
| ai_extract_entities | 3 | android_app/app/src/main/python/modules/ai_panel.py, apk_payload/modules/ai_panel.py, modules/ai_panel.py |
| ai_extract_gender | 3 | android_app/app/src/main/python/modules/ai_panel.py, apk_payload/modules/ai_panel.py, modules/ai_panel.py |
| ai_extract_payment | 3 | android_app/app/src/main/python/modules/ai_panel.py, apk_payload/modules/ai_panel.py, modules/ai_panel.py |
| ai_extract_stop_mentions | 3 | android_app/app/src/main/python/modules/ai_panel.py, apk_payload/modules/ai_panel.py, modules/ai_panel.py |
| ai_intent_pattern | 3 | android_app/app/src/main/python/modules/ai_panel.py, apk_payload/modules/ai_panel.py, modules/ai_panel.py |
| ai_intent_title | 3 | android_app/app/src/main/python/modules/ai_panel.py, apk_payload/modules/ai_panel.py, modules/ai_panel.py |
| ai_last_stop_info | 3 | android_app/app/src/main/python/modules/ai_panel.py, apk_payload/modules/ai_panel.py, modules/ai_panel.py |
| ai_parse_default_command | 3 | android_app/app/src/main/python/modules/ai_panel.py, apk_payload/modules/ai_panel.py, modules/ai_panel.py |
| ai_preview_text | 3 | android_app/app/src/main/python/modules/ai_panel.py, apk_payload/modules/ai_panel.py, modules/ai_panel.py |
| ai_required_fields | 3 | android_app/app/src/main/python/modules/ai_panel.py, apk_payload/modules/ai_panel.py, modules/ai_panel.py |
| ai_upsert_single_seat | 3 | android_app/app/src/main/python/modules/ai_panel.py, apk_payload/modules/ai_panel.py, modules/ai_panel.py |
| api_ai_bootstrap | 3 | android_app/app/src/main/python/modules/ai_panel.py, apk_payload/modules/ai_panel.py, modules/ai_panel.py |
| api_ai_execute | 3 | android_app/app/src/main/python/modules/ai_panel.py, apk_payload/modules/ai_panel.py, modules/ai_panel.py |
| api_ai_intents | 3 | android_app/app/src/main/python/modules/ai_panel.py, apk_payload/modules/ai_panel.py, modules/ai_panel.py |
| api_ai_learn | 3 | android_app/app/src/main/python/modules/ai_panel.py, apk_payload/modules/ai_panel.py, modules/ai_panel.py |
| api_ai_learned | 3 | android_app/app/src/main/python/modules/ai_panel.py, apk_payload/modules/ai_panel.py, modules/ai_panel.py |
| api_ai_learned_delete | 3 | android_app/app/src/main/python/modules/ai_panel.py, apk_payload/modules/ai_panel.py, modules/ai_panel.py |
| api_ai_learned_update | 3 | android_app/app/src/main/python/modules/ai_panel.py, apk_payload/modules/ai_panel.py, modules/ai_panel.py |
| api_ai_resolve | 3 | android_app/app/src/main/python/modules/ai_panel.py, apk_payload/modules/ai_panel.py, modules/ai_panel.py |
| api_consignment_delete | 3 | android_app/app/src/main/python/modules/consignments_panel.py, apk_payload/modules/consignments_panel.py, modules/consignments_panel.py |
| api_consignment_photos | 3 | android_app/app/src/main/python/modules/consignments_panel.py, apk_payload/modules/consignments_panel.py, modules/consignments_panel.py |
| api_consignments | 3 | android_app/app/src/main/python/modules/consignments_panel.py, apk_payload/modules/consignments_panel.py, modules/consignments_panel.py |
| api_coords | 3 | android_app/app/src/main/python/modules/coords_panel.py, apk_payload/modules/coords_panel.py, modules/coords_panel.py |
| api_events | 3 | android_app/app/src/main/python/modules/reports_panel.py, apk_payload/modules/reports_panel.py, modules/reports_panel.py |
| api_google_play_purchase_cancelled | 3 | android_app/app/src/main/python/modules/subscription_panel.py, apk_payload/modules/subscription_panel.py, modules/subscription_panel.py |
| api_google_play_purchase_success | 3 | android_app/app/src/main/python/modules/subscription_panel.py, apk_payload/modules/subscription_panel.py, modules/subscription_panel.py |
| api_package_request | 3 | android_app/app/src/main/python/modules/subscription_panel.py, apk_payload/modules/subscription_panel.py, modules/subscription_panel.py |
| api_parcels | 3 | android_app/app/src/main/python/modules/consignments_panel.py, apk_payload/modules/consignments_panel.py, modules/consignments_panel.py |
| api_report_seat_stats | 3 | android_app/app/src/main/python/modules/reports_panel.py, apk_payload/modules/reports_panel.py, modules/reports_panel.py |
| api_route_coord_save_manual | 3 | android_app/app/src/main/python/modules/coords_panel.py, apk_payload/modules/coords_panel.py, modules/coords_panel.py |
| api_route_coord_status | 3 | android_app/app/src/main/python/modules/coords_panel.py, apk_payload/modules/coords_panel.py, modules/coords_panel.py |
| api_route_schedule | 3 | android_app/app/src/main/python/modules/routes_panel.py, apk_payload/modules/routes_panel.py, modules/routes_panel.py |

## 22) CSS Selector Tekrarları
3 ve üzeri tekrar eden selectorlar. CSS çakışması için ilk sinyal.
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
| .account-hero-home | 15 | android_app/app/src/main/python/templates/hesap.html, apk_payload/templates/hesap.html, templates/hesap.html |
| .dock-row | 15 | android_app/app/src/main/python/static/live_map/muavin_live_map_extra.css, apk_payload/static/live_map/muavin_live_map_extra.css, static/live_map/muavin_live_map_extra.css |
| .drive-speed-top | 15 | android_app/app/src/main/python/static/seats/seats.css, apk_payload/static/seats/seats.css, static/seats/seats.css |
| .fade | 15 | android_app/app/src/main/python/static/vendor/bootstrap/bootstrap.min.css, android_app/app/src/main/python/templates/reports.html, apk_payload/static/vendor/bootstrap/bootstrap.min.css, apk_payload/templates/reports.html, static/vendor/bootstrap/bootstrap.min.css, templates/reports.html |
| .good | 15 | android_app/app/src/main/python/static/live_map/muavin_live_map_extra.css, android_app/app/src/main/python/static/seats/seats.css, android_app/app/src/main/python/templates/ai_console.html, apk_payload/static/live_map/muavin_live_map_extra.css, apk_payload/static/seats/seats.css, apk_payload/templates/ai_console.html, static/live_map/muavin_live_map_extra.css, static/seats/seats.css |
| .guide-chip | 15 | android_app/app/src/main/python/templates/rehber.html, apk_payload/templates/rehber.html, templates/rehber.html |
| .guide-line | 15 | android_app/app/src/main/python/templates/rehber.html, apk_payload/templates/rehber.html, templates/rehber.html |
| .guide-top10 | 15 | android_app/app/src/main/python/templates/rehber.html, apk_payload/templates/rehber.html, templates/rehber.html |
| .hero-sub | 15 | android_app/app/src/main/python/templates/ai_console.html, android_app/app/src/main/python/templates/route_schedule_edit.html, apk_payload/templates/ai_console.html, apk_payload/templates/route_schedule_edit.html, templates/ai_console.html, templates/route_schedule_edit.html |
| .highlight-img | 15 | android_app/app/src/main/python/templates/rehber.html, apk_payload/templates/rehber.html, templates/rehber.html |
| .kalan-pill | 15 | android_app/app/src/main/python/templates/hesap.html, apk_payload/templates/hesap.html, templates/hesap.html |
| .kasa | 15 | android_app/app/src/main/python/templates/events.html, android_app/app/src/main/python/templates/hesap.html, apk_payload/templates/events.html, apk_payload/templates/hesap.html, templates/events.html, templates/hesap.html |
| .left | 15 | android_app/app/src/main/python/templates/hesap.html, android_app/app/src/main/python/templates/rehber.html, apk_payload/templates/hesap.html, apk_payload/templates/rehber.html, templates/hesap.html, templates/rehber.html |
| .listening | 15 | android_app/app/src/main/python/static/seats/patches/bottom-voice-command.css, android_app/app/src/main/python/static/seats/seats.css, android_app/app/src/main/python/templates/ai_console.html, apk_payload/static/seats/patches/bottom-voice-command.css, apk_payload/static/seats/seats.css, apk_payload/templates/ai_console.html, static/seats/patches/bottom-voice-command.css, static/seats/seats.css |
| .lock-btn | 15 | android_app/app/src/main/python/templates/index.html, apk_payload/templates/index.html, templates/index.html |
| .map-actions | 15 | android_app/app/src/main/python/static/live_map/muavin_live_map_extra.css, android_app/app/src/main/python/templates/live_map.html, apk_payload/static/live_map/muavin_live_map_extra.css, apk_payload/templates/live_map.html, static/live_map/muavin_live_map_extra.css, templates/live_map.html |
| .muavin-locate-inner | 15 | android_app/app/src/main/python/static/live_map/muavin_live_map_extra.css, apk_payload/static/live_map/muavin_live_map_extra.css, static/live_map/muavin_live_map_extra.css |
| .muavin-summary-bubble-final | 15 | android_app/app/src/main/python/static/live_map/muavin_live_map_extra.css, apk_payload/static/live_map/muavin_live_map_extra.css, static/live_map/muavin_live_map_extra.css |
| .muavin-tools-fab-final | 15 | android_app/app/src/main/python/static/live_map/muavin_live_map_extra.css, apk_payload/static/live_map/muavin_live_map_extra.css, static/live_map/muavin_live_map_extra.css |
| .next-ops-final-wrap | 15 | android_app/app/src/main/python/static/live_map/muavin_live_map_extra.css, apk_payload/static/live_map/muavin_live_map_extra.css, static/live_map/muavin_live_map_extra.css |
| .page-link | 15 | android_app/app/src/main/python/static/vendor/bootstrap/bootstrap.min.css, apk_payload/static/vendor/bootstrap/bootstrap.min.css, static/vendor/bootstrap/bootstrap.min.css |
| .popover-arrow | 15 | android_app/app/src/main/python/static/vendor/bootstrap/bootstrap.min.css, apk_payload/static/vendor/bootstrap/bootstrap.min.css, static/vendor/bootstrap/bootstrap.min.css |
| .red | 15 | android_app/app/src/main/python/templates/consignments.html, android_app/app/src/main/python/templates/passenger_control.html, android_app/app/src/main/python/templates/route_schedule_edit.html, apk_payload/templates/consignments.html, apk_payload/templates/passenger_control.html, apk_payload/templates/route_schedule_edit.html, templates/consignments.html, templates/passenger_control.html |
| .route-card | 15 | android_app/app/src/main/python/templates/index.html, android_app/app/src/main/python/templates/route_edit.html, android_app/app/src/main/python/templates/routes_list.html, apk_payload/templates/index.html, apk_payload/templates/route_edit.html, apk_payload/templates/routes_list.html, templates/index.html, templates/route_edit.html |
| .route-strip-head | 15 | android_app/app/src/main/python/static/seats/seats-final.css, android_app/app/src/main/python/static/seats/seats.css, apk_payload/static/seats/seats-final.css, apk_payload/static/seats/seats.css, static/seats/seats-final.css, static/seats/seats.css |
| .scene-copy | 15 | android_app/app/src/main/python/templates/rehber.html, apk_payload/templates/rehber.html, templates/rehber.html |
| .sheet-seat-no | 15 | android_app/app/src/main/python/static/continue/css_parts/20-live-stop-sheet-base.css, android_app/app/src/main/python/static/continue/css_parts/30-sheet-bag-photo.css, android_app/app/src/main/python/static/continue/css_parts/40-cargo-gender-summary.css, apk_payload/templates/continue_trip.html, static/continue/css_parts/20-live-stop-sheet-base.css, static/continue/css_parts/30-sheet-bag-photo.css, static/continue/css_parts/40-cargo-gender-summary.css |
| .stats-row | 15 | android_app/app/src/main/python/static/continue/css_parts/00-base-legacy.css, android_app/app/src/main/python/static/continue/css_parts/10-compact-timeline-hero.css, apk_payload/templates/continue_trip.html, static/continue/css_parts/00-base-legacy.css, static/continue/css_parts/10-compact-timeline-hero.css |
| .table | 15 | android_app/app/src/main/python/static/vendor/bootstrap/bootstrap.min.css, android_app/app/src/main/python/templates/ai_console.html, android_app/app/src/main/python/templates/events.html, android_app/app/src/main/python/templates/hesap.html, apk_payload/static/vendor/bootstrap/bootstrap.min.css, apk_payload/templates/ai_console.html, apk_payload/templates/events.html, apk_payload/templates/hesap.html |
| .tooltip-arrow | 15 | android_app/app/src/main/python/static/vendor/bootstrap/bootstrap.min.css, apk_payload/static/vendor/bootstrap/bootstrap.min.css, static/vendor/bootstrap/bootstrap.min.css |
| .trip-field | 15 | android_app/app/src/main/python/templates/start_trip.html, apk_payload/templates/start_trip.html, templates/start_trip.html |
| .action-grid | 14 | _unused_review/static/seats/seats-redesign.css, android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-final.css, android_app/app/src/main/python/static/seats/seats.css, apk_payload/static/seats/_archive_theme_trials/seats-dashboard-final.css, apk_payload/static/seats/seats.css, static/seats/_archive_theme_trials/seats-dashboard-final.css, static/seats/seats.css |
| .cell | 14 | android_app/app/src/main/python/static/seats/seats.css, android_app/app/src/main/python/templates/passenger_control.html, apk_payload/static/seats/seats.css, apk_payload/templates/passenger_control.html, static/seats/patches/unified-seat-deck-report-style.css, static/seats/seats.css, templates/passenger_control.html |
| .panel-tabs | 14 | _unused_review/static/seats/seats-redesign.css, android_app/app/src/main/python/static/seats/_archive_theme_trials/seats-dashboard-final.css, android_app/app/src/main/python/static/seats/seats-final.css, android_app/app/src/main/python/static/seats/seats.css, apk_payload/static/seats/_archive_theme_trials/seats-dashboard-final.css, apk_payload/static/seats/seats-final.css, apk_payload/static/seats/seats.css, static/seats/_archive_theme_trials/seats-dashboard-final.css |
| .pill | 14 | android_app/app/src/main/python/templates/hesap.html, android_app/app/src/main/python/templates/reports.html, android_app/app/src/main/python/templates/settings_subscription.html, apk_payload/templates/hesap.html, apk_payload/templates/reports.html, apk_payload/templates/settings_subscription.html, templates/hesap.html, templates/reports.html |
| .section-title | 14 | android_app/app/src/main/python/templates/ai_console.html, android_app/app/src/main/python/templates/route_schedule_edit.html, apk_payload/templates/ai_console.html, apk_payload/templates/route_schedule_edit.html, templates/ai_console.html, templates/route_schedule_edit.html, templates/settings_backup.html, templates/settings_subscription.html |
| .summary-card | 14 | _unused_review/static/seats/seats-redesign.css, android_app/app/src/main/python/templates/ai_console.html, android_app/app/src/main/python/templates/live_map.html, android_app/app/src/main/python/templates/routes_list.html, apk_payload/templates/ai_console.html, apk_payload/templates/live_map.html, apk_payload/templates/routes_list.html, templates/ai_console.html |
| .wrap | 14 | android_app/app/src/main/python/templates/add_route.html, android_app/app/src/main/python/templates/fare_admin.html, android_app/app/src/main/python/templates/fare_query.html, android_app/app/src/main/python/templates/report_archive.html, android_app/app/src/main/python/templates/reports.html, apk_payload/templates/add_route.html, apk_payload/templates/fare_admin.html, apk_payload/templates/fare_query.html |
| .hint | 13 | android_app/app/src/main/python/templates/add_route.html, android_app/app/src/main/python/templates/fare_query.html, android_app/app/src/main/python/templates/login.html, android_app/app/src/main/python/templates/no_active_trip.html, apk_payload/templates/add_route.html, apk_payload/templates/fare_query.html, apk_payload/templates/login.html, apk_payload/templates/no_active_trip.html |
| .modal-actions | 13 | android_app/app/src/main/python/static/seats/seats.css, apk_payload/static/seats/seats.css, static/seats/seats.css, templates/settings_backup.html, templates/settings_recovery.html |

## 23) Yama / Patch / Fix İzleri - Özet Tokenlar
Yakalanan benzersiz yama token sayısı: **281**
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
| 20h14v-2H5v2zM11 | 4 | AYARLAR_NET_RAPORU.txt, android_app/app/src/main/python/templates/reports.html, apk_payload/templates/reports.html, templates/reports.html |
| 4-4h-3V4h-2z | 4 | AYARLAR_NET_RAPORU.txt, android_app/app/src/main/python/templates/reports.html, apk_payload/templates/reports.html, templates/reports.html |
| FAB_DRIVE_MODE_OVERRIDE_FIX_END | 4 | SEATS_HTML_A_DAN_Z_RAPORU_20260518_162041.txt, SEATS_HTML_KALAN_YAMA_RAPORU_20260518_174156.txt, SEATS_HTML_TEMIZLIK_RAPORU_20260518_153638.txt |
| LAST_ROW_INNER_GAP_FIX_END | 4 | PATCH_AUDIT_REPORT.md, android_app/app/src/main/python/static/seats/seats.css, apk_payload/static/seats/seats.css, static/seats/seats.css |
| LAST_ROW_INNER_GAP_FIX_START | 4 | PATCH_AUDIT_REPORT.md, android_app/app/src/main/python/static/seats/seats.css, apk_payload/static/seats/seats.css, static/seats/seats.css |
| LAST_ROW_TIGHTER_FIX_END | 4 | PATCH_AUDIT_REPORT.md, android_app/app/src/main/python/static/seats/seats.css, apk_payload/static/seats/seats.css, static/seats/seats.css |
| LAST_ROW_TIGHTER_FIX_START | 4 | PATCH_AUDIT_REPORT.md, android_app/app/src/main/python/static/seats/seats.css, apk_payload/static/seats/seats.css, static/seats/seats.css |
| MOBILE_MODAL_READABILITY_FIX_END | 4 | PATCH_AUDIT_REPORT.md, android_app/app/src/main/python/static/seats/patches/mobile-performance-fix.css, apk_payload/static/seats/patches/mobile-performance-fix.css, static/seats/patches/mobile-performance-fix.css |
| MOBILE_MODAL_READABILITY_FIX_START | 4 | PATCH_AUDIT_REPORT.md, android_app/app/src/main/python/static/seats/patches/mobile-performance-fix.css, apk_payload/static/seats/patches/mobile-performance-fix.css, static/seats/patches/mobile-performance-fix.css |
| STOP_FLOW_FOCUS_PATCH_END | 4 | SEATS_HTML_A_DAN_Z_RAPORU_20260518_162041.txt, SEATS_HTML_KALAN_YAMA_RAPORU_20260518_174156.txt, SEATS_HTML_TEMIZLIK_RAPORU_20260518_153638.txt |
| STOP_FLOW_FOCUS_PATCH_START | 4 | SEATS_HTML_A_DAN_Z_RAPORU_20260518_162041.txt, SEATS_HTML_KALAN_YAMA_RAPORU_20260518_174156.txt, SEATS_HTML_TEMIZLIK_RAPORU_20260518_153638.txt |
| continue-live-v2-dot-blink | 4 | android_app/app/src/main/python/static/continue/css_parts/50-live-v2-top-glow.css, static/continue/css_parts/50-live-v2-top-glow.css |
| continue-live-v2-script | 4 | android_app/app/src/main/python/static/continue/continue_trip_ui.js, static/continue/continue_trip_ui.js |
| continue-live-v2-style | 4 | android_app/app/src/main/python/static/continue/css_parts/50-live-v2-top-glow.css, static/continue/css_parts/50-live-v2-top-glow.css |
| live-bag-emanet-hard-fix-style | 4 | android_app/app/src/main/python/static/continue/css_parts/50-live-v2-top-glow.css, static/continue/css_parts/50-live-v2-top-glow.css |
| muavin_audit_step6_runtime_smoke | 4 | audit_reports/muavin_step7_global_appjs.txt |
| muavin_audit_step6b_runtime_smoke_fixed | 4 | audit_reports/muavin_step7_global_appjs.txt |
| preDispatch | 4 | AYARLAR_DETAY_RAPORU.txt, _unused_review/static/vendor/jquery/jquery-3.7.1.min.js |
| proxy_fix | 4 | proje_dosya_listesi.txt |
| with_suffix | 4 | android_app/app/src/main/python/modules/bags/__init__.py, apk_payload/modules/bags/__init__.py, modules/bags/__init__.py, tools/project_tree_audit.py |
| 20260512-v1 | 3 | android_app/app/src/main/python/static/seats/seats.js, apk_payload/static/seats/seats.js, static/seats/seats.js |
| END_MUAVIN_BOTTOM_DOCK_FINAL_V5 | 3 | android_app/app/src/main/python/static/live_map/muavin_live_map_extra.css, apk_payload/static/live_map/muavin_live_map_extra.css, static/live_map/muavin_live_map_extra.css |
| END_MUAVIN_CLEAN_MODE_DOCK_VISIBLE_V12 | 3 | android_app/app/src/main/python/static/live_map/muavin_live_map_extra.css, apk_payload/static/live_map/muavin_live_map_extra.css, static/live_map/muavin_live_map_extra.css |
| END_MUAVIN_CLEAN_MODE_FULLSCREEN_VISIBLE_V11 | 3 | android_app/app/src/main/python/static/live_map/muavin_live_map_extra.css, apk_payload/static/live_map/muavin_live_map_extra.css, static/live_map/muavin_live_map_extra.css |
| END_MUAVIN_CLEAN_MODE_HIDE_KM_LABELS_V13 | 3 | android_app/app/src/main/python/static/live_map/muavin_live_map_extra.css, apk_payload/static/live_map/muavin_live_map_extra.css, static/live_map/muavin_live_map_extra.css |
| END_MUAVIN_CLEAN_MODE_LOCATION_VISIBLE_V14 | 3 | android_app/app/src/main/python/static/live_map/muavin_live_map_extra.css, apk_payload/static/live_map/muavin_live_map_extra.css, static/live_map/muavin_live_map_extra.css |
| END_MUAVIN_CLEAN_MODE_SPEED_VISIBLE_V15 | 3 | android_app/app/src/main/python/static/live_map/muavin_live_map_extra.css, apk_payload/static/live_map/muavin_live_map_extra.css, static/live_map/muavin_live_map_extra.css |
| END_MUAVIN_CLEAN_START_MODE_V10 | 3 | android_app/app/src/main/python/static/live_map/muavin_live_map_extra.css, apk_payload/static/live_map/muavin_live_map_extra.css, static/live_map/muavin_live_map_extra.css |
| END_MUAVIN_GOOGLE_LOCATION_V2_CSS | 3 | android_app/app/src/main/python/static/live_map/muavin_live_map_extra.css, apk_payload/static/live_map/muavin_live_map_extra.css, static/live_map/muavin_live_map_extra.css |
| END_MUAVIN_LOCATE_BUTTON_POSITION_FIX_V1 | 3 | android_app/app/src/main/python/static/live_map/muavin_live_map_extra.css, apk_payload/static/live_map/muavin_live_map_extra.css, static/live_map/muavin_live_map_extra.css |
| END_MUAVIN_MAP_UI_FINAL_V6 | 3 | android_app/app/src/main/python/static/live_map/muavin_live_map_extra.css, apk_payload/static/live_map/muavin_live_map_extra.css, static/live_map/muavin_live_map_extra.css |
| END_MUAVIN_NEXT_OPS_BUBBLE_DRAG_V4 | 3 | android_app/app/src/main/python/static/live_map/muavin_live_map_extra.css, apk_payload/static/live_map/muavin_live_map_extra.css, static/live_map/muavin_live_map_extra.css |
| END_MUAVIN_NEXT_OPS_FINAL_V1 | 3 | android_app/app/src/main/python/static/live_map/muavin_live_map_extra.css, apk_payload/static/live_map/muavin_live_map_extra.css, static/live_map/muavin_live_map_extra.css |
| END_MUAVIN_NEXT_OPS_FLOAT_BUBBLE_V3 | 3 | android_app/app/src/main/python/static/live_map/muavin_live_map_extra.css, apk_payload/static/live_map/muavin_live_map_extra.css, static/live_map/muavin_live_map_extra.css |
| END_MUAVIN_NEXT_OPS_PANEL_POLISH_V2 | 3 | android_app/app/src/main/python/static/live_map/muavin_live_map_extra.css, apk_payload/static/live_map/muavin_live_map_extra.css, static/live_map/muavin_live_map_extra.css |
| END_MUAVIN_REMOVE_COMPASS_V7 | 3 | android_app/app/src/main/python/static/live_map/muavin_live_map_extra.css, apk_payload/static/live_map/muavin_live_map_extra.css, static/live_map/muavin_live_map_extra.css |
| END_MUAVIN_SMALL_ELEGANT_BUTTONS_V9 | 3 | android_app/app/src/main/python/static/live_map/muavin_live_map_extra.css, apk_payload/static/live_map/muavin_live_map_extra.css, static/live_map/muavin_live_map_extra.css |
| MUAVIN_BOTTOM_DOCK_FINAL_V5_JS | 3 | android_app/app/src/main/python/static/live_map/muavin_live_map_extra.js, apk_payload/static/live_map/muavin_live_map_extra.js, static/live_map/muavin_live_map_extra.js |
| MUAVIN_CLEAN_MODE_DOCK_VISIBLE_V12 | 3 | android_app/app/src/main/python/static/live_map/muavin_live_map_extra.css, apk_payload/static/live_map/muavin_live_map_extra.css, static/live_map/muavin_live_map_extra.css |
| MUAVIN_CLEAN_MODE_FULLSCREEN_VISIBLE_V11 | 3 | android_app/app/src/main/python/static/live_map/muavin_live_map_extra.css, apk_payload/static/live_map/muavin_live_map_extra.css, static/live_map/muavin_live_map_extra.css |

## 24) Yama / Patch / Fix Satırlarından İlk 250 Kayıt
| Dosya | Satır | Satır içeriği |
| --- | --- | --- |
| app.py | 51 | DEBUG = env_bool("FLASK_DEBUG", True) |
| app.py | 1128 | PROTECTED_PREFIXES = ("/",) |
| app.py | 1129 | EXCLUDE_PREFIXES = ("/login", "/logout", "/health", "/api/speedlimit", "/static") |
| app.py | 1133 | return any(path == x or path.startswith(x + "/") for x in EXCLUDE_PREFIXES) |
| app.py | 1197 | if any(p.startswith(pref) for pref in PROTECTED_PREFIXES) and not is_excluded_path(p): |
| app.py | 1200 | if request.method in {"POST", "PUT", "PATCH", "DELETE"}: |
| app.py | 3307 | # AI Console v2 |
| app.py | 4512 | app.run(host="0.0.0.0", port=PORT, debug=DEBUG) |
| ACTIVE_FILES.txt | 49 | tools/audit_files.py |
| update.sh | 78 | .lock-btn{position:fixed;right:12px;top:12px;z-index:9999}\ |
| update.sh | 107 | .fab-settings{position:fixed;right:16px;bottom:16px;z-index:9999}\ |
| TOOL_TREE.txt | 7 | ├── audit_files.py |
| TOOL_TREE.txt | 9 | └── project_tree_audit.py |
| proje_dosya_listesi.txt | 176 | ./.venv/lib/python3.12/site-packages/flask/__pycache__/debughelpers.cpython-312.pyc |
| proje_dosya_listesi.txt | 192 | ./.venv/lib/python3.12/site-packages/flask/debughelpers.py |
| proje_dosya_listesi.txt | 274 | ./.venv/lib/python3.12/site-packages/jinja2/__pycache__/debug.cpython-312.pyc |
| proje_dosya_listesi.txt | 298 | ./.venv/lib/python3.12/site-packages/jinja2/debug.py |
| proje_dosya_listesi.txt | 391 | ./.venv/lib/python3.12/site-packages/pip/_internal/commands/__pycache__/debug.cpython-312.pyc |
| proje_dosya_listesi.txt | 408 | ./.venv/lib/python3.12/site-packages/pip/_internal/commands/debug.py |
| proje_dosya_listesi.txt | 1431 | ./.venv/lib/python3.12/site-packages/werkzeug/debug/__init__.py |
| proje_dosya_listesi.txt | 1432 | ./.venv/lib/python3.12/site-packages/werkzeug/debug/__pycache__/__init__.cpython-312.pyc |
| proje_dosya_listesi.txt | 1433 | ./.venv/lib/python3.12/site-packages/werkzeug/debug/__pycache__/console.cpython-312.pyc |
| proje_dosya_listesi.txt | 1434 | ./.venv/lib/python3.12/site-packages/werkzeug/debug/__pycache__/repr.cpython-312.pyc |
| proje_dosya_listesi.txt | 1435 | ./.venv/lib/python3.12/site-packages/werkzeug/debug/__pycache__/tbtools.cpython-312.pyc |
| proje_dosya_listesi.txt | 1436 | ./.venv/lib/python3.12/site-packages/werkzeug/debug/console.py |
| proje_dosya_listesi.txt | 1437 | ./.venv/lib/python3.12/site-packages/werkzeug/debug/repr.py |
| proje_dosya_listesi.txt | 1438 | ./.venv/lib/python3.12/site-packages/werkzeug/debug/shared/ICON_LICENSE.md |
| proje_dosya_listesi.txt | 1439 | ./.venv/lib/python3.12/site-packages/werkzeug/debug/shared/console.png |
| proje_dosya_listesi.txt | 1440 | ./.venv/lib/python3.12/site-packages/werkzeug/debug/shared/debugger.js |
| proje_dosya_listesi.txt | 1441 | ./.venv/lib/python3.12/site-packages/werkzeug/debug/shared/less.png |
| proje_dosya_listesi.txt | 1442 | ./.venv/lib/python3.12/site-packages/werkzeug/debug/shared/more.png |
| proje_dosya_listesi.txt | 1443 | ./.venv/lib/python3.12/site-packages/werkzeug/debug/shared/style.css |
| proje_dosya_listesi.txt | 1444 | ./.venv/lib/python3.12/site-packages/werkzeug/debug/tbtools.py |
| proje_dosya_listesi.txt | 1451 | ./.venv/lib/python3.12/site-packages/werkzeug/middleware/__pycache__/dispatcher.cpython-312.pyc |
| proje_dosya_listesi.txt | 1455 | ./.venv/lib/python3.12/site-packages/werkzeug/middleware/__pycache__/proxy_fix.cpython-312.pyc |
| proje_dosya_listesi.txt | 1457 | ./.venv/lib/python3.12/site-packages/werkzeug/middleware/dispatcher.py |
| proje_dosya_listesi.txt | 1461 | ./.venv/lib/python3.12/site-packages/werkzeug/middleware/proxy_fix.py |
| proje_dosya_listesi.txt | 1841 | ./.venv/lib/python3.13/site-packages/flask/__pycache__/debughelpers.cpython-313.pyc |
| proje_dosya_listesi.txt | 1857 | ./.venv/lib/python3.13/site-packages/flask/debughelpers.py |
| proje_dosya_listesi.txt | 1939 | ./.venv/lib/python3.13/site-packages/jinja2/__pycache__/debug.cpython-313.pyc |
| proje_dosya_listesi.txt | 1963 | ./.venv/lib/python3.13/site-packages/jinja2/debug.py |
| proje_dosya_listesi.txt | 2084 | ./.venv/lib/python3.13/site-packages/pip/_internal/commands/__pycache__/debug.cpython-313.pyc |
| proje_dosya_listesi.txt | 2102 | ./.venv/lib/python3.13/site-packages/pip/_internal/commands/debug.py |
| proje_dosya_listesi.txt | 3049 | ./.venv/lib/python3.13/site-packages/werkzeug/debug/__init__.py |
| proje_dosya_listesi.txt | 3050 | ./.venv/lib/python3.13/site-packages/werkzeug/debug/__pycache__/__init__.cpython-313.pyc |
| proje_dosya_listesi.txt | 3051 | ./.venv/lib/python3.13/site-packages/werkzeug/debug/__pycache__/console.cpython-313.pyc |
| proje_dosya_listesi.txt | 3052 | ./.venv/lib/python3.13/site-packages/werkzeug/debug/__pycache__/repr.cpython-313.pyc |
| proje_dosya_listesi.txt | 3053 | ./.venv/lib/python3.13/site-packages/werkzeug/debug/__pycache__/tbtools.cpython-313.pyc |
| proje_dosya_listesi.txt | 3054 | ./.venv/lib/python3.13/site-packages/werkzeug/debug/console.py |
| proje_dosya_listesi.txt | 3055 | ./.venv/lib/python3.13/site-packages/werkzeug/debug/repr.py |
| proje_dosya_listesi.txt | 3056 | ./.venv/lib/python3.13/site-packages/werkzeug/debug/shared/ICON_LICENSE.md |
| proje_dosya_listesi.txt | 3057 | ./.venv/lib/python3.13/site-packages/werkzeug/debug/shared/console.png |
| proje_dosya_listesi.txt | 3058 | ./.venv/lib/python3.13/site-packages/werkzeug/debug/shared/debugger.js |
| proje_dosya_listesi.txt | 3059 | ./.venv/lib/python3.13/site-packages/werkzeug/debug/shared/less.png |
| proje_dosya_listesi.txt | 3060 | ./.venv/lib/python3.13/site-packages/werkzeug/debug/shared/more.png |
| proje_dosya_listesi.txt | 3061 | ./.venv/lib/python3.13/site-packages/werkzeug/debug/shared/style.css |
| proje_dosya_listesi.txt | 3062 | ./.venv/lib/python3.13/site-packages/werkzeug/debug/tbtools.py |
| proje_dosya_listesi.txt | 3069 | ./.venv/lib/python3.13/site-packages/werkzeug/middleware/__pycache__/dispatcher.cpython-313.pyc |
| proje_dosya_listesi.txt | 3073 | ./.venv/lib/python3.13/site-packages/werkzeug/middleware/__pycache__/proxy_fix.cpython-313.pyc |
| proje_dosya_listesi.txt | 3075 | ./.venv/lib/python3.13/site-packages/werkzeug/middleware/dispatcher.py |
| proje_dosya_listesi.txt | 3079 | ./.venv/lib/python3.13/site-packages/werkzeug/middleware/proxy_fix.py |
| proje_dosya_listesi.txt | 3133 | ./app.py.bak-fix-endtrip-walkon-20260429_200406 |
| proje_dosya_listesi.txt | 3135 | ./app.py.bak-trip-route-fix |
| proje_dosya_listesi.txt | 3136 | ./app.py.bak-trip-route-form-fix |
| proje_dosya_listesi.txt | 3147 | ./muavin-change-04-gender-ui.patch |
| proje_dosya_listesi.txt | 3151 | ./setup-test.patch |
| proje_dosya_listesi.txt | 3170 | ./static/seats/seats-redesign.css.bak_board_fix |
| proje_dosya_listesi.txt | 3186 | ./static/seats/seats.css.bak-drive-speed-fixed |
| proje_dosya_listesi.txt | 3189 | ./static/seats/seats.css.bak-fixed-dock |
| proje_dosya_listesi.txt | 3195 | ./static/seats/seats.css.bak-route-flow-real-fix |
| proje_dosya_listesi.txt | 3213 | ./static/seats/seats.js.bak-fixed-dock |
| proje_dosya_listesi.txt | 3225 | ./static/seats/seats_ses_fix_yedek_20260427_165038.js |
| proje_dosya_listesi.txt | 3227 | ./static/seats/seats_voice_summary_fix_20260427_165419.js |
| proje_dosya_listesi.txt | 3300 | ./templates/continue_trip.html.bak_fix_drive_css |
| proje_dosya_listesi.txt | 3335 | ./templates/index.html.bak-route-lock-fix |
| proje_dosya_listesi.txt | 3355 | ./templates/route_edit.html.bak-bottom-buttons-fix |
| proje_dosya_listesi.txt | 3356 | ./templates/route_edit.html.bak-clean-local-coords-ui-v2 |
| proje_dosya_listesi.txt | 3361 | ./templates/route_edit.html.bak-save-button-final-fix |
| proje_dosya_listesi.txt | 3364 | ./templates/route_edit.html.bak-title-fix |
| proje_dosya_listesi.txt | 3372 | ./templates/seats.html.bak-ai-button-fix |
| proje_dosya_listesi.txt | 3391 | ./templates/seats.html.bak-drive-quick-menu-size-fix |
| proje_dosya_listesi.txt | 3407 | ./templates/seats.html.bak_design_v1 |
| proje_dosya_listesi.txt | 3408 | ./templates/seats.html.bak_drive_dock_fix |
| proje_dosya_listesi.txt | 3428 | ./templates/seats_parts/topbar.html.bak-ai-url-fix |
| proje_dosya_listesi.txt | 3453 | ./templates/settings_subscription.html.bak-payment-alert-fix |
| proje_dosya_listesi.txt | 3457 | ./templates/settings_subscription.html.bak-plan-picker-text-fix |
| proje_dosya_listesi.txt | 3466 | ./templates/start_trip.html.bak-overflow-fix-20260502_011712 |
| proje_dosya_listesi.txt | 3468 | ./templates/start_trip.html.bak-route-input-fix |
| proje_dosya_listesi.txt | 3475 | ./test.patch |
| proje_dosya_listesi.txt | 3478 | ./update-ayarlar-kilitle.patch |
| proje_flask_baglanti_raporu.txt | 166 | modules/bags/__init__.py:24:bp = Blueprint("bags", __name__, url_prefix="/bags") |
| proje_flask_baglanti_raporu.txt | 189 | modules/bags/__init__.py.bak-bag-ui-20260427-174341:24:bp = Blueprint("bags", __name__, url_prefix="/bags") |
| proje_flask_baglanti_raporu.txt | 398 | templates/seats_parts/topbar.html.bak-ai-url-fix:24:      <a href="{{ url_for('index') }}" class="icon-btn" title="Ana Sayfa">🏠</a> |
| proje_flask_baglanti_raporu.txt | 399 | templates/seats_parts/topbar.html.bak-ai-url-fix:25:      <a href="{{ url_for('hesap_page') }}" class="icon-btn" title="Hesap">💵</a> |
| proje_flask_baglanti_raporu.txt | 400 | templates/seats_parts/topbar.html.bak-ai-url-fix:26:      <a href="{{ url_for('consignments_page') }}" class="icon-btn" title="Emanetler">📦</a> |
| proje_flask_baglanti_raporu.txt | 401 | templates/seats_parts/topbar.html.bak-ai-url-fix:27:      <a href="{{ url_for('ai_console_page') }}" class="icon-btn" title="AI Console">🧠</a> |
| proje_flask_baglanti_raporu.txt | 402 | templates/seats_parts/topbar.html.bak-ai-url-fix:28:      <form method="post" action="{{ url_for('end_trip') }}" onsubmit="return confirm('Sefer sonlandırılsın mı?')"> |
| proje_flask_baglanti_raporu.txt | 501 | templates/index.html.bak-route-lock-fix:222:    <a class="hero-link" href="{{ url_for('trip_start') }}" aria-label="Sefer Başlat"> |
| proje_flask_baglanti_raporu.txt | 502 | templates/index.html.bak-route-lock-fix:223:      <img src="{{ url_for('static', filename='img/home-bus-card.jpg') }}" alt="Sefer Başlat"> |
| proje_flask_baglanti_raporu.txt | 503 | templates/index.html.bak-route-lock-fix:226:    <a class="hero-link" href="{{ url_for('continue_trip') }}" aria-label="Devam Eden Sefer"> |
| proje_flask_baglanti_raporu.txt | 504 | templates/index.html.bak-route-lock-fix:227:      <img src="{{ url_for('static', filename='img/home-seat-card.jpg') }}" alt="Devam Eden Sefer"> |
| proje_flask_baglanti_raporu.txt | 505 | templates/index.html.bak-route-lock-fix:231:      <a class="menu-item" href="{{ url_for('seats_page') }}"> |
| proje_flask_baglanti_raporu.txt | 506 | templates/index.html.bak-route-lock-fix:240:      <a class="menu-item" href="{{ url_for('passenger_control') }}"> |
| proje_flask_baglanti_raporu.txt | 507 | templates/index.html.bak-route-lock-fix:249:      <a class="menu-item" href="{{ url_for('hesap_page') }}"> |
| proje_flask_baglanti_raporu.txt | 508 | templates/index.html.bak-route-lock-fix:258:      <a class="menu-item" href="{{ url_for('consignments_page') }}"> |
| proje_flask_baglanti_raporu.txt | 509 | templates/index.html.bak-route-lock-fix:267:      <a class="menu-item" href="{{ url_for('add_route') }}"> |
| proje_flask_baglanti_raporu.txt | 510 | templates/index.html.bak-route-lock-fix:276:      <a class="menu-item" href="{{ url_for('routes_list') }}"> |
| proje_flask_baglanti_raporu.txt | 511 | templates/index.html.bak-route-lock-fix:294:      <a class="menu-item" href="{{ url_for('fare_query') }}"> |
| proje_flask_baglanti_raporu.txt | 568 | templates/route_edit.html.bak-bottom-buttons-fix:454:    <a class="btn gray" href="{{ url_for('routes_list') }}">← Hatlar</a> |
| proje_flask_baglanti_raporu.txt | 569 | templates/route_edit.html.bak-bottom-buttons-fix:460:  <form method="post" action="{{ url_for('route_edit', rid=route['id']) }}"> |
| proje_flask_baglanti_raporu.txt | 570 | templates/route_edit.html.bak-bottom-buttons-fix:474:      <a class="btn gray" href="{{ url_for('routes_list') }}">Vazgeç</a> |
| proje_flask_baglanti_raporu.txt | 580 | templates/seats.html.bak-ai-button-fix:313:      hesap: {{ url_for('hesap_page') \| tojson \| safe }}, |
| proje_flask_baglanti_raporu.txt | 581 | templates/seats.html.bak-ai-button-fix:314:      consignments: {{ url_for('consignments_page') \| tojson \| safe }} |
| proje_flask_baglanti_raporu.txt | 582 | templates/seats.html.bak-ai-button-fix:449:      <a class="dma-btn" href="{{ url_for('index') }}" title="Ana Sayfa">🏠</a> |
| proje_flask_baglanti_raporu.txt | 583 | templates/seats.html.bak-ai-button-fix:450:      <a class="dma-btn" href="{{ url_for('hesap_page') }}" title="Hesap">💵</a> |
| proje_flask_baglanti_raporu.txt | 584 | templates/seats.html.bak-ai-button-fix:451:      <a class="dma-btn" href="{{ url_for('consignments_page') }}" title="Emanetler">📦</a> |
| proje_flask_baglanti_raporu.txt | 610 | templates/route_edit.html.bak-save-button-final-fix:454:    <a class="btn gray" href="{{ url_for('routes_list') }}">← Hatlar</a> |
| proje_flask_baglanti_raporu.txt | 611 | templates/route_edit.html.bak-save-button-final-fix:460:  <form method="post" action="{{ url_for('route_edit', rid=route['id']) }}"> |
| proje_flask_baglanti_raporu.txt | 612 | templates/route_edit.html.bak-save-button-final-fix:474:      <a class="btn gray" href="{{ url_for('routes_list') }}">Vazgeç</a> |
| proje_flask_baglanti_raporu.txt | 613 | templates/seats.html.bak-drive-quick-menu-size-fix:317:      hesap: {{ url_for('hesap_page') \| tojson \| safe }}, |
| proje_flask_baglanti_raporu.txt | 614 | templates/seats.html.bak-drive-quick-menu-size-fix:318:      consignments: {{ url_for('consignments_page') \| tojson \| safe }} |
| proje_flask_baglanti_raporu.txt | 633 | templates/route_edit.html.bak-title-fix:309:    <a class="btn gray" href="{{ url_for('routes_list') }}">← Hatlar</a> |
| proje_flask_baglanti_raporu.txt | 634 | templates/route_edit.html.bak-title-fix:315:  <form method="post" action="{{ url_for('route_edit', rid=route['id']) }}"> |
| proje_flask_baglanti_raporu.txt | 635 | templates/route_edit.html.bak-title-fix:329:      <a class="btn gray" href="{{ url_for('routes_list') }}">Vazgeç</a> |
| proje_flask_baglanti_raporu.txt | 640 | templates/start_trip.html.bak-route-input-fix:25:  <form id="startForm" method="post" action="{{ url_for('trip_start') }}"> |
| proje_flask_baglanti_raporu.txt | 641 | templates/start_trip.html.bak-route-input-fix:57:      <a href="{{ url_for('index') }}" class="btn btn-secondary">Vazgeç</a> |
| proje_flask_baglanti_raporu.txt | 693 | templates/start_trip.html.bak-overflow-fix-20260502_011712:217:  <form id="startForm" class="trip-form" method="post" action="{{ url_for('trip_start') }}"> |
| proje_flask_baglanti_raporu.txt | 694 | templates/start_trip.html.bak-overflow-fix-20260502_011712:255:      <a href="{{ url_for('index') }}" class="trip-btn trip-btn-secondary">Vazgeç</a> |
| proje_flask_baglanti_raporu.txt | 724 | templates/continue_trip.html.bak_fix_drive_css:712:      <a class="big-action seat-visual-card" href="{{ url_for('seats_page') }}"> |
| proje_flask_baglanti_raporu.txt | 725 | templates/continue_trip.html.bak_fix_drive_css:725:      <a class="big-action drive" href="{{ url_for('seats_page') }}?drive=1"> |
| proje_flask_baglanti_raporu.txt | 726 | templates/continue_trip.html.bak_fix_drive_css:734:      <a class="big-action cash" href="{{ url_for('hesap_page') }}"> |
| proje_flask_baglanti_raporu.txt | 727 | templates/continue_trip.html.bak_fix_drive_css:745:      <a class="quick-item" href="{{ url_for('passenger_control') }}"> |
| proje_flask_baglanti_raporu.txt | 728 | templates/continue_trip.html.bak_fix_drive_css:754:      <a class="quick-item" href="{{ url_for('consignments_page') }}"> |
| proje_flask_baglanti_raporu.txt | 729 | templates/continue_trip.html.bak_fix_drive_css:774:      <form id="endTripForm" method="post" action="{{ url_for('end_trip') }}"> |
| proje_flask_baglanti_raporu.txt | 759 | templates/seats.html.bak_design_v1:321:      hesap: {{ url_for('hesap_page') \| tojson \| safe }}, |
| proje_flask_baglanti_raporu.txt | 760 | templates/seats.html.bak_design_v1:322:      consignments: {{ url_for('consignments_page') \| tojson \| safe }} |
| proje_flask_baglanti_raporu.txt | 761 | templates/seats.html.bak_design_v1:457:      <a class="dma-btn" href="{{ url_for('index') }}" title="Ana Sayfa">🏠</a> |
| proje_flask_baglanti_raporu.txt | 762 | templates/seats.html.bak_design_v1:458:      <a class="dma-btn" href="{{ url_for('hesap_page') }}" title="Hesap">💵</a> |
| proje_flask_baglanti_raporu.txt | 763 | templates/seats.html.bak_design_v1:459:      <a class="dma-btn" href="{{ url_for('consignments_page') }}" title="Emanetler">📦</a> |
| proje_flask_baglanti_raporu.txt | 799 | templates/route_edit.html.bak-clean-local-coords-ui-v2:347:    <a class="back-btn" href="{{ url_for('routes_list') }}">← Hatlar</a> |
| proje_flask_baglanti_raporu.txt | 800 | templates/route_edit.html.bak-clean-local-coords-ui-v2:361:    <form method="post" action="{{ url_for('route_edit', rid=route['id']) }}"> |
| proje_flask_baglanti_raporu.txt | 801 | templates/route_edit.html.bak-clean-local-coords-ui-v2:397:        <a class="cancel-btn" href="{{ url_for('routes_list') }}">Vazgeç</a> |
| proje_flask_baglanti_raporu.txt | 802 | templates/route_edit.html.bak-clean-local-coords-ui-v2:716:      const res = await fetch({{ url_for('api_route_coord_status', rid=route['id']) \| tojson }}, { |
| proje_flask_baglanti_raporu.txt | 803 | templates/route_edit.html.bak-clean-local-coords-ui-v2:768:          const res = await fetch({{ url_for('api_route_coord_save_manual', rid=route['id']) \| tojson }}, { |
| proje_flask_baglanti_raporu.txt | 915 | templates/seats.html.bak_drive_dock_fix:322:      hesap: {{ url_for('hesap_page') \| tojson \| safe }}, |
| proje_flask_baglanti_raporu.txt | 916 | templates/seats.html.bak_drive_dock_fix:323:      consignments: {{ url_for('consignments_page') \| tojson \| safe }} |
| proje_flask_baglanti_raporu.txt | 917 | templates/seats.html.bak_drive_dock_fix:458:      <a class="dma-btn" href="{{ url_for('index') }}" title="Ana Sayfa">🏠</a> |
| proje_flask_baglanti_raporu.txt | 918 | templates/seats.html.bak_drive_dock_fix:459:      <a class="dma-btn" href="{{ url_for('hesap_page') }}" title="Hesap">💵</a> |
| proje_flask_baglanti_raporu.txt | 919 | templates/seats.html.bak_drive_dock_fix:460:      <a class="dma-btn" href="{{ url_for('consignments_page') }}" title="Emanetler">📦</a> |
| proje_template_haritasi.txt | 268 | templates/seats_parts/topbar.html.bak-ai-url-fix:24:      <a href="{{ url_for('index') }}" class="icon-btn" title="Ana Sayfa">🏠</a> |
| proje_template_haritasi.txt | 269 | templates/seats_parts/topbar.html.bak-ai-url-fix:25:      <a href="{{ url_for('hesap_page') }}" class="icon-btn" title="Hesap">💵</a> |
| proje_template_haritasi.txt | 270 | templates/seats_parts/topbar.html.bak-ai-url-fix:26:      <a href="{{ url_for('consignments_page') }}" class="icon-btn" title="Emanetler">📦</a> |
| proje_template_haritasi.txt | 271 | templates/seats_parts/topbar.html.bak-ai-url-fix:27:      <a href="{{ url_for('ai_console_page') }}" class="icon-btn" title="AI Console">🧠</a> |
| proje_template_haritasi.txt | 272 | templates/seats_parts/topbar.html.bak-ai-url-fix:28:      <form method="post" action="{{ url_for('end_trip') }}" onsubmit="return confirm('Sefer sonlandırılsın mı?')"> |
| proje_template_haritasi.txt | 459 | templates/index.html.bak-route-lock-fix:222:    <a class="hero-link" href="{{ url_for('trip_start') }}" aria-label="Sefer Başlat"> |
| proje_template_haritasi.txt | 460 | templates/index.html.bak-route-lock-fix:223:      <img src="{{ url_for('static', filename='img/home-bus-card.jpg') }}" alt="Sefer Başlat"> |
| proje_template_haritasi.txt | 461 | templates/index.html.bak-route-lock-fix:226:    <a class="hero-link" href="{{ url_for('continue_trip') }}" aria-label="Devam Eden Sefer"> |
| proje_template_haritasi.txt | 462 | templates/index.html.bak-route-lock-fix:227:      <img src="{{ url_for('static', filename='img/home-seat-card.jpg') }}" alt="Devam Eden Sefer"> |
| proje_template_haritasi.txt | 463 | templates/index.html.bak-route-lock-fix:231:      <a class="menu-item" href="{{ url_for('seats_page') }}"> |
| proje_template_haritasi.txt | 464 | templates/index.html.bak-route-lock-fix:240:      <a class="menu-item" href="{{ url_for('passenger_control') }}"> |
| proje_template_haritasi.txt | 465 | templates/index.html.bak-route-lock-fix:249:      <a class="menu-item" href="{{ url_for('hesap_page') }}"> |
| proje_template_haritasi.txt | 466 | templates/index.html.bak-route-lock-fix:258:      <a class="menu-item" href="{{ url_for('consignments_page') }}"> |
| proje_template_haritasi.txt | 467 | templates/index.html.bak-route-lock-fix:267:      <a class="menu-item" href="{{ url_for('add_route') }}"> |
| proje_template_haritasi.txt | 468 | templates/index.html.bak-route-lock-fix:276:      <a class="menu-item" href="{{ url_for('routes_list') }}"> |
| proje_template_haritasi.txt | 469 | templates/index.html.bak-route-lock-fix:294:      <a class="menu-item" href="{{ url_for('fare_query') }}"> |
| proje_template_haritasi.txt | 530 | templates/route_edit.html.bak-bottom-buttons-fix:1:{% extends "base.html" %} |
| proje_template_haritasi.txt | 531 | templates/route_edit.html.bak-bottom-buttons-fix:438:<link rel="stylesheet" href="/static/style.css"> |
| proje_template_haritasi.txt | 532 | templates/route_edit.html.bak-bottom-buttons-fix:454:    <a class="btn gray" href="{{ url_for('routes_list') }}">← Hatlar</a> |
| proje_template_haritasi.txt | 533 | templates/route_edit.html.bak-bottom-buttons-fix:460:  <form method="post" action="{{ url_for('route_edit', rid=route['id']) }}"> |
| proje_template_haritasi.txt | 534 | templates/route_edit.html.bak-bottom-buttons-fix:474:      <a class="btn gray" href="{{ url_for('routes_list') }}">Vazgeç</a> |
| proje_template_haritasi.txt | 572 | templates/seats.html.bak-ai-button-fix:1:{% extends "base.html" %} |
| proje_template_haritasi.txt | 573 | templates/seats.html.bak-ai-button-fix:4:<link rel="stylesheet" href="/static/style.css"> |
| proje_template_haritasi.txt | 574 | templates/seats.html.bak-ai-button-fix:5:<link rel="stylesheet" href="/static/seats/seats.css?v=38"> |
| proje_template_haritasi.txt | 575 | templates/seats.html.bak-ai-button-fix:8:  {% include "seats_parts/topbar.html" %} |
| proje_template_haritasi.txt | 576 | templates/seats.html.bak-ai-button-fix:9:  {% include "seats_parts/stats.html" %} |
| proje_template_haritasi.txt | 577 | templates/seats.html.bak-ai-button-fix:55:        {% include "seats_parts/route_flow.html" %} |
| proje_template_haritasi.txt | 578 | templates/seats.html.bak-ai-button-fix:56:        {% include "seats_parts/deck.html" %} |
| proje_template_haritasi.txt | 579 | templates/seats.html.bak-ai-button-fix:293:{% include "seats_parts/modals.html" %} |
| proje_template_haritasi.txt | 580 | templates/seats.html.bak-ai-button-fix:313:      hesap: {{ url_for('hesap_page') \| tojson \| safe }}, |
| proje_template_haritasi.txt | 581 | templates/seats.html.bak-ai-button-fix:314:      consignments: {{ url_for('consignments_page') \| tojson \| safe }} |
| proje_template_haritasi.txt | 582 | templates/seats.html.bak-ai-button-fix:319:<script src="/static/seats/bags.js?v=1"></script> |
| proje_template_haritasi.txt | 583 | templates/seats.html.bak-ai-button-fix:320:<script src="/static/seats/voice-commands.js?v=1"></script> |
| proje_template_haritasi.txt | 584 | templates/seats.html.bak-ai-button-fix:321:<script src="/static/seats/standing.js?v=1"></script> |
| proje_template_haritasi.txt | 585 | templates/seats.html.bak-ai-button-fix:322:<script src="/static/seats/seats.js?v=25"></script> |
| proje_template_haritasi.txt | 586 | templates/seats.html.bak-ai-button-fix:323:<script src="/static/seats/drive-controls.js?v=2"></script> |
| proje_template_haritasi.txt | 587 | templates/seats.html.bak-ai-button-fix:449:      <a class="dma-btn" href="{{ url_for('index') }}" title="Ana Sayfa">🏠</a> |
| proje_template_haritasi.txt | 588 | templates/seats.html.bak-ai-button-fix:450:      <a class="dma-btn" href="{{ url_for('hesap_page') }}" title="Hesap">💵</a> |
| proje_template_haritasi.txt | 589 | templates/seats.html.bak-ai-button-fix:451:      <a class="dma-btn" href="{{ url_for('consignments_page') }}" title="Emanetler">📦</a> |
| proje_template_haritasi.txt | 686 | templates/route_edit.html.bak-save-button-final-fix:1:{% extends "base.html" %} |
| proje_template_haritasi.txt | 687 | templates/route_edit.html.bak-save-button-final-fix:438:<link rel="stylesheet" href="/static/style.css"> |
| proje_template_haritasi.txt | 688 | templates/route_edit.html.bak-save-button-final-fix:454:    <a class="btn gray" href="{{ url_for('routes_list') }}">← Hatlar</a> |
| proje_template_haritasi.txt | 689 | templates/route_edit.html.bak-save-button-final-fix:460:  <form method="post" action="{{ url_for('route_edit', rid=route['id']) }}"> |
| proje_template_haritasi.txt | 690 | templates/route_edit.html.bak-save-button-final-fix:474:      <a class="btn gray" href="{{ url_for('routes_list') }}">Vazgeç</a> |
| proje_template_haritasi.txt | 691 | templates/seats.html.bak-drive-quick-menu-size-fix:1:{% extends "base.html" %} |
| proje_template_haritasi.txt | 692 | templates/seats.html.bak-drive-quick-menu-size-fix:4:<link rel="stylesheet" href="/static/style.css"> |
| proje_template_haritasi.txt | 693 | templates/seats.html.bak-drive-quick-menu-size-fix:5:<link rel="stylesheet" href="/static/seats/seats.css?v=38"> |
| proje_template_haritasi.txt | 694 | templates/seats.html.bak-drive-quick-menu-size-fix:10:  {% include "seats_parts/topbar.html" %} |
| proje_template_haritasi.txt | 695 | templates/seats.html.bak-drive-quick-menu-size-fix:12:{% include "seats_parts/stats.html" %} |
| proje_template_haritasi.txt | 696 | templates/seats.html.bak-drive-quick-menu-size-fix:57:        {% include "seats_parts/route_flow.html" %} |
| proje_template_haritasi.txt | 697 | templates/seats.html.bak-drive-quick-menu-size-fix:59:{% include "seats_parts/deck.html" %} |
| proje_template_haritasi.txt | 698 | templates/seats.html.bak-drive-quick-menu-size-fix:296:{% include "seats_parts/modals.html" %} |
| proje_template_haritasi.txt | 699 | templates/seats.html.bak-drive-quick-menu-size-fix:317:      hesap: {{ url_for('hesap_page') \| tojson \| safe }}, |
| proje_template_haritasi.txt | 700 | templates/seats.html.bak-drive-quick-menu-size-fix:318:      consignments: {{ url_for('consignments_page') \| tojson \| safe }} |
| proje_template_haritasi.txt | 701 | templates/seats.html.bak-drive-quick-menu-size-fix:323:<script src="/static/seats/bags.js?v=1"></script> |
| proje_template_haritasi.txt | 702 | templates/seats.html.bak-drive-quick-menu-size-fix:324:<script src="/static/seats/voice-commands.js?v=1"></script> |
| proje_template_haritasi.txt | 703 | templates/seats.html.bak-drive-quick-menu-size-fix:325:<script src="/static/seats/standing.js?v=1"></script> |
| proje_template_haritasi.txt | 704 | templates/seats.html.bak-drive-quick-menu-size-fix:326:<script src="/static/seats/seats.js?v=25"></script> |
| proje_template_haritasi.txt | 705 | templates/seats.html.bak-drive-quick-menu-size-fix:327:<script src="/static/seats/drive-controls.js?v=2"></script> |
| proje_template_haritasi.txt | 755 | templates/route_edit.html.bak-title-fix:1:{% extends "base.html" %} |
| proje_template_haritasi.txt | 756 | templates/route_edit.html.bak-title-fix:293:<link rel="stylesheet" href="/static/style.css"> |
| proje_template_haritasi.txt | 757 | templates/route_edit.html.bak-title-fix:309:    <a class="btn gray" href="{{ url_for('routes_list') }}">← Hatlar</a> |
| proje_template_haritasi.txt | 758 | templates/route_edit.html.bak-title-fix:315:  <form method="post" action="{{ url_for('route_edit', rid=route['id']) }}"> |
| proje_template_haritasi.txt | 759 | templates/route_edit.html.bak-title-fix:329:      <a class="btn gray" href="{{ url_for('routes_list') }}">Vazgeç</a> |
| proje_template_haritasi.txt | 790 | templates/start_trip.html.bak-route-input-fix:1:{% extends "base.html" %} |
| proje_template_haritasi.txt | 791 | templates/start_trip.html.bak-route-input-fix:25:  <form id="startForm" method="post" action="{{ url_for('trip_start') }}"> |
| proje_template_haritasi.txt | 792 | templates/start_trip.html.bak-route-input-fix:57:      <a href="{{ url_for('index') }}" class="btn btn-secondary">Vazgeç</a> |
| proje_template_haritasi.txt | 793 | templates/start_trip.html.bak-route-input-fix:135:    url("/static/img/home-bus-card.jpg") center right / cover no-repeat; |
| proje_template_haritasi.txt | 884 | templates/start_trip.html.bak-overflow-fix-20260502_011712:1:{% extends "base.html" %} |
| proje_template_haritasi.txt | 885 | templates/start_trip.html.bak-overflow-fix-20260502_011712:34:      url("/static/img/home-bus-card.jpg") center right / cover no-repeat; |
| proje_template_haritasi.txt | 886 | templates/start_trip.html.bak-overflow-fix-20260502_011712:217:  <form id="startForm" class="trip-form" method="post" action="{{ url_for('trip_start') }}"> |
| proje_template_haritasi.txt | 887 | templates/start_trip.html.bak-overflow-fix-20260502_011712:255:      <a href="{{ url_for('index') }}" class="trip-btn trip-btn-secondary">Vazgeç</a> |
| proje_template_haritasi.txt | 937 | templates/continue_trip.html.bak_fix_drive_css:43:        url("/static/img/home-bus-card.jpg") center/cover no-repeat; |
| proje_template_haritasi.txt | 938 | templates/continue_trip.html.bak_fix_drive_css:386:    url("/static/img/seat-card.jpg") center right / cover no-repeat !important; |
| proje_template_haritasi.txt | 939 | templates/continue_trip.html.bak_fix_drive_css:482:      url("/static/img/seat-card.jpg") center right / cover no-repeat !important; |
| proje_template_haritasi.txt | 940 | templates/continue_trip.html.bak_fix_drive_css:712:      <a class="big-action seat-visual-card" href="{{ url_for('seats_page') }}"> |
| proje_template_haritasi.txt | 941 | templates/continue_trip.html.bak_fix_drive_css:725:      <a class="big-action drive" href="{{ url_for('seats_page') }}?drive=1"> |
| proje_template_haritasi.txt | 942 | templates/continue_trip.html.bak_fix_drive_css:734:      <a class="big-action cash" href="{{ url_for('hesap_page') }}"> |
| proje_template_haritasi.txt | 943 | templates/continue_trip.html.bak_fix_drive_css:745:      <a class="quick-item" href="{{ url_for('passenger_control') }}"> |
| proje_template_haritasi.txt | 944 | templates/continue_trip.html.bak_fix_drive_css:754:      <a class="quick-item" href="{{ url_for('consignments_page') }}"> |
| proje_template_haritasi.txt | 945 | templates/continue_trip.html.bak_fix_drive_css:774:      <form id="endTripForm" method="post" action="{{ url_for('end_trip') }}"> |
| proje_template_haritasi.txt | 946 | templates/continue_trip.html.bak_fix_drive_css:875:    url("/static/img/drive-mode-card.png") center / cover no-repeat !important; |
| proje_template_haritasi.txt | 1008 | templates/seats.html.bak_design_v1:1:{% extends "base.html" %} |
| proje_template_haritasi.txt | 1009 | templates/seats.html.bak_design_v1:4:<link rel="stylesheet" href="/static/style.css"> |
| proje_template_haritasi.txt | 1010 | templates/seats.html.bak_design_v1:5:<link rel="stylesheet" href="/static/seats/seats.css?v=41"> |
| proje_template_haritasi.txt | 1011 | templates/seats.html.bak_design_v1:8:  {% include "seats_parts/topbar.html" %} |
| proje_template_haritasi.txt | 1012 | templates/seats.html.bak_design_v1:9:  {% include "seats_parts/stats.html" %} |
| proje_template_haritasi.txt | 1013 | templates/seats.html.bak_design_v1:63:        {% include "seats_parts/route_flow.html" %} |
| proje_template_haritasi.txt | 1014 | templates/seats.html.bak_design_v1:64:        {% include "seats_parts/deck.html" %} |
| proje_template_haritasi.txt | 1015 | templates/seats.html.bak_design_v1:301:{% include "seats_parts/modals.html" %} |
| proje_template_haritasi.txt | 1016 | templates/seats.html.bak_design_v1:321:      hesap: {{ url_for('hesap_page') \| tojson \| safe }}, |
| proje_template_haritasi.txt | 1017 | templates/seats.html.bak_design_v1:322:      consignments: {{ url_for('consignments_page') \| tojson \| safe }} |
| proje_template_haritasi.txt | 1018 | templates/seats.html.bak_design_v1:327:<script src="/static/seats/bags.js?v=1"></script> |
| proje_template_haritasi.txt | 1019 | templates/seats.html.bak_design_v1:328:<script src="/static/seats/voice-commands.js?v=1"></script> |
| proje_template_haritasi.txt | 1020 | templates/seats.html.bak_design_v1:329:<script src="/static/seats/standing.js?v=1"></script> |
| proje_template_haritasi.txt | 1021 | templates/seats.html.bak_design_v1:330:<script src="/static/seats/seats.js?v=20260430_100321"></script> |
| proje_template_haritasi.txt | 1022 | templates/seats.html.bak_design_v1:331:<script src="/static/seats/drive-controls.js?v=2"></script> |
| proje_template_haritasi.txt | 1023 | templates/seats.html.bak_design_v1:457:      <a class="dma-btn" href="{{ url_for('index') }}" title="Ana Sayfa">🏠</a> |
| proje_template_haritasi.txt | 1024 | templates/seats.html.bak_design_v1:458:      <a class="dma-btn" href="{{ url_for('hesap_page') }}" title="Hesap">💵</a> |
| proje_template_haritasi.txt | 1025 | templates/seats.html.bak_design_v1:459:      <a class="dma-btn" href="{{ url_for('consignments_page') }}" title="Emanetler">📦</a> |
| proje_template_haritasi.txt | 1137 | templates/route_edit.html.bak-clean-local-coords-ui-v2:1:{% extends "base.html" %} |

## 25) Debug / TODO / Alert İzleri
| Dosya | Satır | Satır içeriği |
| --- | --- | --- |
| proje_dosya_listesi.txt | 1440 | ./.venv/lib/python3.12/site-packages/werkzeug/debug/shared/debugger.js |
| proje_dosya_listesi.txt | 3058 | ./.venv/lib/python3.13/site-packages/werkzeug/debug/shared/debugger.js |
| AYARLAR_DETAY_RAPORU.txt | 8468 | 444:       alert('Hata: ' + (j.msg \|\| 'Bilinmeyen hata')); |
| AYARLAR_DETAY_RAPORU.txt | 9352 | 661:                 !function(n,t){"object"==typeof exports&&"object"==typeof module?module.exports=t():"function"==typeof define&&define.amd?define([],t):"object"==typeof exports... |
| AYARLAR_DETAY_RAPORU.txt | 9357 | 661:                 !function(n,t){"object"==typeof exports&&"object"==typeof module?module.exports=t():"function"==typeof define&&define.amd?define([],t):"object"==typeof exports... |
| AYARLAR_DETAY_RAPORU.txt | 10982 | 444:       alert('Hata: ' + (j.msg \|\| 'Bilinmeyen hata')); |
| AYARLAR_DETAY_RAPORU.txt | 13839 | 444:       alert('Hata: ' + (j.msg \|\| 'Bilinmeyen hata')); |
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
| tools/muavin_audit_step1.py | 278 | suspicious = re.compile(r"\b(TODO\|FIXME\|HACK\|BUG\|XXX\|console\.error\|alert\(\|debugger)\b", re.I) |
| tools/muavin_audit_step1.py | 300 | print("✅ Şüpheli TODO/FIXME/HACK/BUG/debugger izi yok") |
| tools/muavin_audit_step2.py | 537 | "alert(", |
| tools/muavin_audit_step2.py | 538 | "debugger", |
| tools/muavin_audit_step2.py | 539 | "TODO", |
| tools/muavin_audit_step2.py | 540 | "FIXME", |
| tools/muavin_full_audit_v1.py | 413 | PATCH_LINE_RE = re.compile(r"(patch\|hotfix\|fix\|step[-_ ]?\d+\|audit\|debug\|todo\|fixme\|v\d+)", re.I) |
| tools/muavin_full_audit_v1.py | 420 | DEBUG_RE = re.compile(r"(console\.log\|debugger\|alert\(\|TODO\|FIXME)", re.I) |
| tools/muavin_full_audit_v1.py | 576 | md.append("\n## 25) Debug / TODO / Alert İzleri") |
| templates/add_route.html | 376 | alert('Hat adı ve en az bir durak gerekli.'); |
| templates/consignments.html | 970 | if(j.ok) location.reload(); else alert(j.msg \|\| 'Hata'); |
| templates/consignments.html | 981 | if(j.ok) location.reload(); else alert(j.msg \|\| 'Hata'); |
| templates/consignments.html | 993 | if(j.ok) location.reload(); else alert(j.msg \|\| 'Hata'); |
| templates/hesap.html | 1910 | alert("PrintBridge bulunamadı. Tarayıcı yazdırma deneniyor."); |
| templates/hesap.html | 1913 | alert("PrintBridge hatası: " + err); |
| templates/hesap.html | 1914 | console.log("PrintBridge error:", err); |
| templates/hesap.html | 1920 | alert("Yazdırma ekranı açılamadı."); |
| templates/hesap.html | 2386 | alert("Paylaşılacak hareket yok."); |
| templates/route_edit.html | 699 | alert("Önce hat adını yaz."); |
| templates/route_edit.html | 704 | alert("Durak listesi boş."); |
| templates/route_edit.html | 760 | alert("Lat ve Lng gir."); |
| templates/route_edit.html | 782 | alert(j.msg \|\| "Kayıt hatası"); |
| templates/route_edit.html | 790 | alert("Bağlantı hatası: " + e.message); |
| templates/route_stops.html | 46 | if(!j.ok){ alert(j.msg \|\| 'Duraklar alınamadı'); return; } |
| templates/route_stops.html | 55 | if(lat.value==='' \|\| lng.value===''){ alert('Lat/Lng gir'); return; } |
| templates/route_stops.html | 69 | else { alert(jj.msg \|\| 'Hata'); } |
| templates/route_stops.html | 70 | }catch(e){ alert('Bağlantı hatası'); } |
| templates/routes_list.html | 444 | alert('Hata: ' + (j.msg \|\| 'Bilinmeyen hata')); |
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
| audit_reports/muavin_step4_suspicious_context.txt | 88 | 970:   if(j.ok) location.reload(); else alert(j.msg \|\| 'Hata'); |
| audit_reports/muavin_step4_suspicious_context.txt | 99 | 981:   if(j.ok) location.reload(); else alert(j.msg \|\| 'Hata'); |
| audit_reports/muavin_step4_suspicious_context.txt | 152 | 55:       if(lat.value==='' \|\| lng.value===''){ alert('Lat/Lng gir'); return; } |
| audit_reports/muavin_step4_suspicious_context.txt | 166 | 69:         else { alert(jj.msg \|\| 'Hata'); } |
| audit_reports/muavin_step4_suspicious_context.txt | 167 | 70:       }catch(e){ alert('Bağlantı hatası'); } |
| audit_reports/muavin_step4_suspicious_context.txt | 274 | 970:   if(j.ok) location.reload(); else alert(j.msg \|\| 'Hata'); |
| audit_reports/muavin_step4_suspicious_context.txt | 285 | 981:   if(j.ok) location.reload(); else alert(j.msg \|\| 'Hata'); |
| audit_reports/muavin_step4_suspicious_context.txt | 326 | 55:       if(lat.value==='' \|\| lng.value===''){ alert('Lat/Lng gir'); return; } |
| audit_reports/muavin_step4_suspicious_context.txt | 340 | 69:         else { alert(jj.msg \|\| 'Hata'); } |
| audit_reports/muavin_step4_suspicious_context.txt | 2249 | 370:       alert("Koltuk bilgisi bulunamadı."); |
| audit_reports/muavin_step4_suspicious_context.txt | 2409 | 285:         alert(data.error \|\| "İniş durağı değiştirilemedi."); |
| audit_reports/muavin_step4_suspicious_context.txt | 2441 | 285:         alert(data.error \|\| "İniş durağı değiştirilemedi."); |
| audit_reports/muavin_step4_suspicious_context.txt | 2775 | 285:         alert(data.error \|\| "İniş durağı değiştirilemedi."); |
| audit_reports/muavin_step4_suspicious_context.txt | 2807 | 285:         alert(data.error \|\| "İniş durağı değiştirilemedi."); |
| audit_reports/muavin_step4_suspicious_context.txt | 2839 | 285:         alert(data.error \|\| "İniş durağı değiştirilemedi."); |
| audit_reports/muavin_step4_suspicious_context.txt | 3278 | 370:       alert("Koltuk bilgisi bulunamadı."); |
| audit_reports/muavin_step4_suspicious_context.txt | 3438 | 285:         alert(data.error \|\| "İniş durağı değiştirilemedi."); |
| audit_reports/muavin_step4_suspicious_context.txt | 3470 | 285:         alert(data.error \|\| "İniş durağı değiştirilemedi."); |
| audit_reports/muavin_step4_suspicious_context.txt | 3804 | 285:         alert(data.error \|\| "İniş durağı değiştirilemedi."); |
| audit_reports/muavin_step4_suspicious_context.txt | 3836 | 285:         alert(data.error \|\| "İniş durağı değiştirilemedi."); |
| audit_reports/muavin_step4_suspicious_context.txt | 3868 | 285:         alert(data.error \|\| "İniş durağı değiştirilemedi."); |
| audit_reports/muavin_step5_active_bug_context.txt | 896 | 970:   if(j.ok) location.reload(); else alert(j.msg \|\| 'Hata'); |
| audit_reports/muavin_step5_active_bug_context.txt | 907 | 981:   if(j.ok) location.reload(); else alert(j.msg \|\| 'Hata'); |
| audit_reports/muavin_step5_active_bug_context.txt | 919 | 993:   if(j.ok) location.reload(); else alert(j.msg \|\| 'Hata'); |
| audit_reports/muavin_step5_active_bug_context.txt | 1099 | 970:   if(j.ok) location.reload(); else alert(j.msg \|\| 'Hata'); |
| audit_reports/muavin_step5_active_bug_context.txt | 1110 | 981:   if(j.ok) location.reload(); else alert(j.msg \|\| 'Hata'); |
| audit_reports/muavin_step5_active_bug_context.txt | 1122 | 993:   if(j.ok) location.reload(); else alert(j.msg \|\| 'Hata'); |
| audit_reports/muavin_step5_active_bug_context.txt | 1293 | 970:   if(j.ok) location.reload(); else alert(j.msg \|\| 'Hata'); |
| audit_reports/muavin_step5_active_bug_context.txt | 1304 | 981:   if(j.ok) location.reload(); else alert(j.msg \|\| 'Hata'); |
| audit_reports/muavin_step5_active_bug_context.txt | 1309 | 970:   if(j.ok) location.reload(); else alert(j.msg \|\| 'Hata'); |
| audit_reports/muavin_step5_active_bug_context.txt | 1320 | 981:   if(j.ok) location.reload(); else alert(j.msg \|\| 'Hata'); |
| audit_reports/muavin_step5_active_bug_context.txt | 1334 | 981:   if(j.ok) location.reload(); else alert(j.msg \|\| 'Hata'); |
| audit_reports/muavin_step5_active_bug_context.txt | 1357 | 970:   if(j.ok) location.reload(); else alert(j.msg \|\| 'Hata'); |
| audit_reports/muavin_step5_active_bug_context.txt | 1368 | 981:   if(j.ok) location.reload(); else alert(j.msg \|\| 'Hata'); |
| audit_reports/muavin_step5_active_bug_context.txt | 1380 | 993:   if(j.ok) location.reload(); else alert(j.msg \|\| 'Hata'); |
| audit_reports/muavin_step5_active_bug_context.txt | 1560 | 970:   if(j.ok) location.reload(); else alert(j.msg \|\| 'Hata'); |
| audit_reports/muavin_step5_active_bug_context.txt | 1571 | 981:   if(j.ok) location.reload(); else alert(j.msg \|\| 'Hata'); |
| audit_reports/muavin_step5_active_bug_context.txt | 1583 | 993:   if(j.ok) location.reload(); else alert(j.msg \|\| 'Hata'); |
| audit_reports/muavin_step5_active_bug_context.txt | 1754 | 970:   if(j.ok) location.reload(); else alert(j.msg \|\| 'Hata'); |
| audit_reports/muavin_step5_active_bug_context.txt | 1765 | 981:   if(j.ok) location.reload(); else alert(j.msg \|\| 'Hata'); |
| audit_reports/muavin_step5_active_bug_context.txt | 1770 | 970:   if(j.ok) location.reload(); else alert(j.msg \|\| 'Hata'); |
| audit_reports/muavin_step5_active_bug_context.txt | 1781 | 981:   if(j.ok) location.reload(); else alert(j.msg \|\| 'Hata'); |
| audit_reports/muavin_step5_active_bug_context.txt | 1795 | 981:   if(j.ok) location.reload(); else alert(j.msg \|\| 'Hata'); |
| backups/apk_sync_20260520_234501/trip_report.html | 503 | alert("PrintBridge bulunamadı. Tarayıcı yazdırma deneniyor."); |
| backups/apk_sync_20260520_234501/trip_report.html | 506 | alert("PrintBridge hatası: " + err); |
| backups/apk_sync_20260520_234501/trip_report.html | 507 | console.log("PrintBridge error:", err); |
| backups/apk_sync_20260520_234501/trip_report.html | 513 | alert("Yazdırma ekranı açılamadı."); |
| _unused_review/static/vendor/fa/all.min.css | 9 | .fa-sr-only,.fa-sr-only-focusable:not(:focus),.sr-only,.sr-only-focusable:not(:focus){position:absolute;width:1px;height:1px;padding:0;margin:-1px;overflow:hidden;clip:rect(0,0,0,0... |
| android_app/app/src/main/python/templates/add_route.html | 376 | alert('Hat adı ve en az bir durak gerekli.'); |
| android_app/app/src/main/python/templates/consignments.html | 970 | if(j.ok) location.reload(); else alert(j.msg \|\| 'Hata'); |
| android_app/app/src/main/python/templates/consignments.html | 981 | if(j.ok) location.reload(); else alert(j.msg \|\| 'Hata'); |
| android_app/app/src/main/python/templates/consignments.html | 993 | if(j.ok) location.reload(); else alert(j.msg \|\| 'Hata'); |
| android_app/app/src/main/python/templates/hesap.html | 1910 | alert("PrintBridge bulunamadı. Tarayıcı yazdırma deneniyor."); |
| android_app/app/src/main/python/templates/hesap.html | 1913 | alert("PrintBridge hatası: " + err); |
| android_app/app/src/main/python/templates/hesap.html | 1914 | console.log("PrintBridge error:", err); |
| android_app/app/src/main/python/templates/hesap.html | 1920 | alert("Yazdırma ekranı açılamadı."); |
| android_app/app/src/main/python/templates/hesap.html | 2386 | alert("Paylaşılacak hareket yok."); |
| android_app/app/src/main/python/templates/route_edit.html | 699 | alert("Önce hat adını yaz."); |
| android_app/app/src/main/python/templates/route_edit.html | 704 | alert("Durak listesi boş."); |
| android_app/app/src/main/python/templates/route_edit.html | 760 | alert("Lat ve Lng gir."); |
| android_app/app/src/main/python/templates/route_edit.html | 782 | alert(j.msg \|\| "Kayıt hatası"); |
| android_app/app/src/main/python/templates/route_edit.html | 790 | alert("Bağlantı hatası: " + e.message); |
| android_app/app/src/main/python/templates/route_stops.html | 46 | if(!j.ok){ alert(j.msg \|\| 'Duraklar alınamadı'); return; } |
| android_app/app/src/main/python/templates/route_stops.html | 55 | if(lat.value==='' \|\| lng.value===''){ alert('Lat/Lng gir'); return; } |
| android_app/app/src/main/python/templates/route_stops.html | 69 | else { alert(jj.msg \|\| 'Hata'); } |
| android_app/app/src/main/python/templates/route_stops.html | 70 | }catch(e){ alert('Bağlantı hatası'); } |
| android_app/app/src/main/python/templates/routes_list.html | 444 | alert('Hata: ' + (j.msg \|\| 'Bilinmeyen hata')); |
| android_app/app/src/main/python/templates/routes_list.html | 447 | alert('Bağlantı hatası'); |
| android_app/app/src/main/python/templates/trip_report.html | 503 | alert("PrintBridge bulunamadı. Tarayıcı yazdırma deneniyor."); |
| android_app/app/src/main/python/templates/trip_report.html | 506 | alert("PrintBridge hatası: " + err); |
| android_app/app/src/main/python/templates/trip_report.html | 507 | console.log("PrintBridge error:", err); |
| android_app/app/src/main/python/templates/trip_report.html | 513 | alert("Yazdırma ekranı açılamadı."); |
| android_app/app/src/main/python/templates/live_map.html | 2543 | console.log("approach speak error", err); |
| android_app/app/src/main/python/templates/live_map.html | 2547 | function hideApproachAlert(){ |
| android_app/app/src/main/python/templates/live_map.html | 2555 | function showApproachAlert(stop, km, level){ |
| android_app/app/src/main/python/templates/live_map.html | 2584 | function checkApproachAlert(){ |
| android_app/app/src/main/python/templates/live_map.html | 2591 | hideApproachAlert(); |
| android_app/app/src/main/python/templates/live_map.html | 2599 | hideApproachAlert(); |
| android_app/app/src/main/python/templates/live_map.html | 2609 | showApproachAlert(target, km, level); |
| android_app/app/src/main/python/templates/live_map.html | 2632 | checkApproachAlert(); |
| android_app/app/src/main/python/templates/live_map.html | 2643 | console.log("Konum alınamadı", err); |
| android_app/app/src/main/python/templates/live_map.html | 2718 | hideApproachAlert(); |
| android_app/app/src/main/python/templates/live_map.html | 2723 | hideApproachAlert(); |
| android_app/app/src/main/python/templates/live_map.html | 2746 | hideApproachAlert(); |
| android_app/app/src/main/python/templates/settings_recovery.html | 236 | navigator.clipboard.writeText(code).then(() => alert("Kurtarma kodu kopyalandı.")); |
| android_app/app/src/main/python/templates/settings_recovery.html | 238 | alert(code); |
| android_app/app/src/main/python/static/seats/seats.js | 474 | console.log("Saat profili API'den yüklendi:", apiSchedule); |
| android_app/app/src/main/python/static/seats/seats.js | 806 | console.log("recordStopFlowEvent error", err); |
| android_app/app/src/main/python/static/continue/continue_trip_core.js | 285 | alert(data.error \|\| "İniş durağı değiştirilemedi."); |
| android_app/app/src/main/python/static/continue/continue_trip_core.js | 307 | alert("Bağlantı hatası. İniş durağı değiştirilemedi."); |
| android_app/app/src/main/python/static/continue/continue_trip_core.js | 370 | alert("Koltuk bilgisi bulunamadı."); |
| apk_payload/templates/add_route.html | 376 | alert('Hat adı ve en az bir durak gerekli.'); |
| apk_payload/templates/consignments.html | 970 | if(j.ok) location.reload(); else alert(j.msg \|\| 'Hata'); |
| apk_payload/templates/consignments.html | 981 | if(j.ok) location.reload(); else alert(j.msg \|\| 'Hata'); |
| apk_payload/templates/consignments.html | 993 | if(j.ok) location.reload(); else alert(j.msg \|\| 'Hata'); |
| apk_payload/templates/hesap.html | 1910 | alert("PrintBridge bulunamadı. Tarayıcı yazdırma deneniyor."); |
| apk_payload/templates/hesap.html | 1913 | alert("PrintBridge hatası: " + err); |
| apk_payload/templates/hesap.html | 1914 | console.log("PrintBridge error:", err); |
| apk_payload/templates/hesap.html | 1920 | alert("Yazdırma ekranı açılamadı."); |
| apk_payload/templates/hesap.html | 2386 | alert("Paylaşılacak hareket yok."); |
| apk_payload/templates/route_edit.html | 699 | alert("Önce hat adını yaz."); |
| apk_payload/templates/route_edit.html | 704 | alert("Durak listesi boş."); |
| apk_payload/templates/route_edit.html | 760 | alert("Lat ve Lng gir."); |
| apk_payload/templates/route_edit.html | 782 | alert(j.msg \|\| "Kayıt hatası"); |
| apk_payload/templates/route_edit.html | 790 | alert("Bağlantı hatası: " + e.message); |
| apk_payload/templates/route_stops.html | 46 | if(!j.ok){ alert(j.msg \|\| 'Duraklar alınamadı'); return; } |
| apk_payload/templates/route_stops.html | 55 | if(lat.value==='' \|\| lng.value===''){ alert('Lat/Lng gir'); return; } |
| apk_payload/templates/route_stops.html | 69 | else { alert(jj.msg \|\| 'Hata'); } |
| apk_payload/templates/route_stops.html | 70 | }catch(e){ alert('Bağlantı hatası'); } |
| apk_payload/templates/routes_list.html | 444 | alert('Hata: ' + (j.msg \|\| 'Bilinmeyen hata')); |
| apk_payload/templates/routes_list.html | 447 | alert('Bağlantı hatası'); |
| apk_payload/templates/trip_report.html | 503 | alert("PrintBridge bulunamadı. Tarayıcı yazdırma deneniyor."); |
| apk_payload/templates/trip_report.html | 506 | alert("PrintBridge hatası: " + err); |
| apk_payload/templates/trip_report.html | 507 | console.log("PrintBridge error:", err); |
| apk_payload/templates/trip_report.html | 513 | alert("Yazdırma ekranı açılamadı."); |
| apk_payload/templates/live_map.html | 2543 | console.log("approach speak error", err); |
| apk_payload/templates/live_map.html | 2547 | function hideApproachAlert(){ |
| apk_payload/templates/live_map.html | 2555 | function showApproachAlert(stop, km, level){ |
| apk_payload/templates/live_map.html | 2584 | function checkApproachAlert(){ |
| apk_payload/templates/live_map.html | 2591 | hideApproachAlert(); |
| apk_payload/templates/live_map.html | 2599 | hideApproachAlert(); |
| apk_payload/templates/live_map.html | 2609 | showApproachAlert(target, km, level); |
| apk_payload/templates/live_map.html | 2632 | checkApproachAlert(); |
| apk_payload/templates/live_map.html | 2643 | console.log("Konum alınamadı", err); |
| apk_payload/templates/live_map.html | 2718 | hideApproachAlert(); |
| apk_payload/templates/live_map.html | 2723 | hideApproachAlert(); |
| apk_payload/templates/live_map.html | 2746 | hideApproachAlert(); |
| apk_payload/templates/settings_recovery.html | 236 | navigator.clipboard.writeText(code).then(() => alert("Kurtarma kodu kopyalandı.")); |
| apk_payload/templates/settings_recovery.html | 238 | alert(code); |
| apk_payload/templates/continue_trip.html | 3922 | alert(data.error \|\| "İniş durağı değiştirilemedi."); |
| apk_payload/templates/continue_trip.html | 3944 | alert("Bağlantı hatası. İniş durağı değiştirilemedi."); |
| apk_payload/templates/continue_trip.html | 4007 | alert("Koltuk bilgisi bulunamadı."); |
| apk_payload/static/seats/seats.js | 474 | console.log("Saat profili API'den yüklendi:", apiSchedule); |
| apk_payload/static/seats/seats.js | 806 | console.log("recordStopFlowEvent error", err); |
| static/seats/seats.js | 474 | console.log("Saat profili API'den yüklendi:", apiSchedule); |
| static/seats/seats.js | 806 | console.log("recordStopFlowEvent error", err); |
| static/continue/continue_trip_core.js | 285 | alert(data.error \|\| "İniş durağı değiştirilemedi."); |
| static/continue/continue_trip_core.js | 307 | alert("Bağlantı hatası. İniş durağı değiştirilemedi."); |
| static/continue/continue_trip_core.js | 370 | alert("Koltuk bilgisi bulunamadı."); |

## 26) İlk Karar Notu

Bu rapor sadece tespit içindir. Şu aşamada hiçbir dosya silinmedi.
Silme kararı için ayrı bir liste hazırlanmalı:

1. Birebir aynı içerikte olan backup dosyalar
2. Ana uygulama tarafından çağrılmayan eski patch dosyaları
3. Android/web kopyasında eski kalmış farklı dosyalar
4. Eksik static referansları yüzünden boşa duran bağlantılar
5. Büyük HTML içine gömülmüş tekrar eden inline script/style blokları

Önce bu rapordaki çakışmaları okuyup sınıflandıracağız. Sonra silinecekleri tek tek onaylı listeye alacağız.
