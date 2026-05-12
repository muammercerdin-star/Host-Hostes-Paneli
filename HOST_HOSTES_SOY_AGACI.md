# Host-Hostes Paneli Soy Ağacı

## 1. Ana Gövde

Host-Hostes Paneli
├── app.py
│   ├── Flask ana uygulama
│   ├── kullanıcı girişi / oturum
│   ├── sefer yönetimi
│   ├── koltuk kayıt sistemi
│   ├── rota / durak yönetimi
│   ├── ücret / tahsilat yönetimi
│   ├── raporlar
│   ├── ayarlar
│   ├── yedekleme / geri yükleme
│   └── API uçları
│
├── speedlimit.py
│   └── hız limiti / hız kontrol modülü
│
├── modules/
│   └── bags/
│       └── bagaj / emanet / kargo modülü
│
├── templates/
│   ├── base.html
│   │   └── ortak sayfa iskeleti
│   │
│   ├── index.html
│   │   └── ana panel
│   │
│   ├── login.html
│   │   └── giriş ekranı
│   │
│   ├── start_trip.html
│   │   └── sefer başlatma
│   │
│   ├── continue_trip.html
│   │   └── devam eden sefer ekranı
│   │
│   ├── seats.html
│   │   └── koltuk / yolcu / durak akışı ana ekranı
│   │
│   ├── seats_parts/
│   │   ├── topbar.html
│   │   ├── stats.html
│   │   ├── deck.html
│   │   ├── route_flow.html
│   │   ├── modals.html
│   │   ├── finish_trip_modal.html
│   │   └── offload_confirm.html
│   │
│   ├── route_edit.html
│   ├── route_stops.html
│   ├── routes_list.html
│   ├── route_schedule_edit.html
│   │   └── rota / durak / saat yönetimi
│   │
│   ├── fare_admin.html
│   ├── fare_query.html
│   │   └── ücret yönetimi
│   │
│   ├── consignments.html
│   │   └── bagaj / emanet yönetimi
│   │
│   ├── trip_report.html
│   ├── reports.html
│   ├── report_archive.html
│   │   └── sefer raporları
│   │
│   ├── settings.html
│   ├── settings_profile.html
│   ├── settings_password.html
│   ├── settings_backup.html
│   ├── settings_recovery.html
│   ├── settings_subscription.html
│   └── settings_package_requests.html
│       └── ayarlar / hesap / abonelik / yedekleme
│
├── static/
│   ├── style.css
│   ├── app.js
│   │   └── genel stil ve genel JS
│   │
│   ├── seats/
│   │   ├── seats.css
│   │   ├── seats-final.css
│   │   ├── seats.js
│   │   ├── bags.js
│   │   ├── standing.js
│   │   ├── voice-commands.js
│   │   ├── voice-tts.js
│   │   ├── route-marquee.js
│   │   ├── seats-time-prayer.js
│   │   ├── drive-eta-chip.js
│   │   └── drive-controls.js
│   │       └── koltuk ekranı, sesli komut, TTS, durak akışı, ETA, sürüş modu
│   │
│   └── vendor/
│       └── bootstrap/
│           ├── bootstrap.min.css
│           └── bootstrap.bundle.min.js
│
├── tools/
│   ├── audit_files.py
│   └── project_tree_audit.py
│       └── proje analiz / dosya ağacı rapor araçları
│
├── _unused_review/
│   ├── seats_aktif_harita.py
│   ├── static/seats/seats-redesign.css
│   ├── static/vendor/fa/all.min.css
│   ├── static/vendor/jquery/jquery-3.7.1.min.js
│   └── trafik_isigi/trafik.html
│       └── aktif olmayan / karantinaya alınmış dosyalar
│
├── static/seats/_archive_theme_trials/
│   ├── seats-dashboard-final.css
│   └── seats-dashboard-tone.css
│       └── eski tema denemeleri
│
├── android_app/
│   └── APK / Android proje kopyası
│
└── apk_payload/
    └── APK içine taşınan Python / template / static kopyaları

## 2. Güncel Sayısal Durum

Aktif çalışan proje: 64 dosya / 48.337 satır  
Sahipsiz dosya: 0 dosya / 0 satır  
Yedek / arşiv / karantina: 7 dosya / 2.254 satır  
APK / Android kopya: 127 dosya / 87.854 satır  
Araç / analiz scriptleri: 2 dosya / 520 satır

## 3. Ana Mantık

Host-Hostes Paneli'nin kalbi app.py dosyasıdır.  
Koltuk ve sefer ekranının ana merkezi templates/seats.html dosyasıdır.  
Koltuk ekranının parçaları templates/seats_parts altında bölünmüştür.  
Koltuk ekranının hareketli tarafı static/seats altındaki JS ve CSS dosyalarıyla çalışır.  
Bagaj / emanet sistemi modules/bags modülüne ayrılmıştır.  
APK tarafı ana proje değil, paketleme ve Android kopya alanıdır.
