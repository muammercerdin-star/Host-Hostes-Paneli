from pathlib import Path
from datetime import datetime
import shutil

ROOT = Path(".").resolve()
STAMP = datetime.now().strftime("%Y%m%d-%H%M%S")

MAIN = ROOT / "android_app/app/src/main/java/com/muavinasistani/app/MainActivity.java"

print("===== V86B MAINACTIVITY TEK SATIR FIX =====")

if not MAIN.exists():
    raise SystemExit("❌ MainActivity.java yok")

b = MAIN.with_name(MAIN.name + f".bak-v86b-{STAMP}")
shutil.copy2(MAIN, b)
print("📦 Yedek:", b.relative_to(ROOT))

s = MAIN.read_text(encoding="utf-8", errors="ignore")
old = s

# 1) onCreate çağrıları garanti olsun.
if "createLockAlarmChannelsV86();" not in s:
    s = s.replace(
        "super.onCreate(savedInstanceState); requestBasicPermissions();",
        "super.onCreate(savedInstanceState); createLockAlarmChannelsV86(); requestBasicPermissions(); requestNotificationPermissionV86();"
    )

if "requestNotificationPermissionV86();" not in s:
    s = s.replace(
        "createLockAlarmChannelsV86(); requestBasicPermissions();",
        "createLockAlarmChannelsV86(); requestBasicPermissions(); requestNotificationPermissionV86();"
    )

# 2) requestBasicPermissions bloğunu tek satır dosyada güvenli değiştir.
marker_start = "private void requestBasicPermissions() {"
marker_end = "@Override protected void onDestroy"

new_methods = r'''private void requestBasicPermissions() {
        if (android.os.Build.VERSION.SDK_INT >= 23) {
            requestPermissions(new String[]{
                    Manifest.permission.ACCESS_FINE_LOCATION,
                    Manifest.permission.ACCESS_COARSE_LOCATION
            }, 100);
        }
    }

    private void requestNotificationPermissionV86() {
        try {
            if (android.os.Build.VERSION.SDK_INT >= 33
                    && checkSelfPermission(Manifest.permission.POST_NOTIFICATIONS) != PackageManager.PERMISSION_GRANTED) {
                requestPermissions(new String[]{
                        Manifest.permission.POST_NOTIFICATIONS
                }, 200);
            }
        } catch (Exception ignored) {}
    }

    private void createLockAlarmChannelsV86() {
        if (android.os.Build.VERSION.SDK_INT < 26) return;

        try {
            android.app.NotificationManager nm =
                    (android.app.NotificationManager) getSystemService(NOTIFICATION_SERVICE);

            if (nm == null) return;

            android.app.NotificationChannel monitor =
                    new android.app.NotificationChannel(
                            "muavin_live_monitor_v85",
                            "Canlı durak takip",
                            android.app.NotificationManager.IMPORTANCE_LOW
                    );

            monitor.setDescription("Canlı durak arka plan takibi");
            monitor.setLockscreenVisibility(android.app.Notification.VISIBILITY_PUBLIC);

            android.app.NotificationChannel alert =
                    new android.app.NotificationChannel(
                            "muavin_live_alert_v85",
                            "Canlı durak alarmı",
                            android.app.NotificationManager.IMPORTANCE_HIGH
                    );

            alert.setDescription("2 km kala sesli ve titreşimli uyarı");
            alert.enableVibration(true);
            alert.setVibrationPattern(new long[]{0, 700, 300, 700, 300, 1000});
            alert.setLockscreenVisibility(android.app.Notification.VISIBILITY_PUBLIC);

            nm.createNotificationChannel(monitor);
            nm.createNotificationChannel(alert);
        } catch (Exception ignored) {}
    }

    '''

start = s.find(marker_start)
end = s.find(marker_end)

if start == -1:
    raise SystemExit("❌ requestBasicPermissions başlangıcı bulunamadı")

if end == -1:
    raise SystemExit("❌ onDestroy başlangıcı bulunamadı")

s = s[:start] + new_methods + s[end:]

MAIN.write_text(s, encoding="utf-8")

print()
print("===== KONTROL =====")
checks = [
    "createLockAlarmChannelsV86();",
    "requestNotificationPermissionV86();",
    "private void requestNotificationPermissionV86()",
    "private void createLockAlarmChannelsV86()",
    "Manifest.permission.CAMERA",
    "Manifest.permission.RECORD_AUDIO",
]

for c in checks:
    print(c, "=>", s.count(c))

print()
if s != old:
    print("✅ V86B düzeltme yapıldı")
else:
    print("ℹ️ Değişiklik yok")

print("✅ V86B tamam.")
