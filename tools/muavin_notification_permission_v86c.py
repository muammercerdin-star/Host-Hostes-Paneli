from pathlib import Path
from datetime import datetime
import shutil

ROOT = Path(".").resolve()
STAMP = datetime.now().strftime("%Y%m%d-%H%M%S")

MAIN = ROOT / "android_app/app/src/main/java/com/muavinasistani/app/MainActivity.java"

print("===== V86C MAINACTIVITY BRACE MATCH FIX =====")

if not MAIN.exists():
    raise SystemExit("❌ MainActivity.java yok")

b = MAIN.with_name(MAIN.name + f".bak-v86c-{STAMP}")
shutil.copy2(MAIN, b)
print("📦 Yedek:", b.relative_to(ROOT))

s = MAIN.read_text(encoding="utf-8", errors="ignore")
old = s

def find_method_bounds(txt, signature):
    start = txt.find(signature)
    if start == -1:
        return -1, -1

    brace = txt.find("{", start)
    if brace == -1:
        return -1, -1

    depth = 0
    in_str = False
    esc = False

    for i in range(brace, len(txt)):
        ch = txt[i]

        if in_str:
            if esc:
                esc = False
            elif ch == "\\":
                esc = True
            elif ch == '"':
                in_str = False
            continue

        if ch == '"':
            in_str = True
            continue

        if ch == "{":
            depth += 1
        elif ch == "}":
            depth -= 1
            if depth == 0:
                return start, i + 1

    return -1, -1

# 1) onCreate çağrılarını garantiye al.
if "createLockAlarmChannelsV86();" not in s:
    s = s.replace(
        "super.onCreate(savedInstanceState);",
        "super.onCreate(savedInstanceState); createLockAlarmChannelsV86(); requestNotificationPermissionV86();",
        1
    )
    print("✅ onCreate kanal + bildirim izni çağrısı eklendi")
else:
    print("ℹ️ onCreate kanal çağrısı zaten var")

if "requestNotificationPermissionV86();" not in s:
    s = s.replace(
        "createLockAlarmChannelsV86();",
        "createLockAlarmChannelsV86(); requestNotificationPermissionV86();",
        1
    )
    print("✅ onCreate bildirim izni çağrısı eklendi")

# Eğer eski requestBasicPermissions çağrısı varsa konum izni için kalsın.
if "requestBasicPermissions();" not in s:
    s = s.replace(
        "createLockAlarmChannelsV86(); requestNotificationPermissionV86();",
        "createLockAlarmChannelsV86(); requestBasicPermissions(); requestNotificationPermissionV86();",
        1
    )
    print("✅ onCreate konum izni çağrısı eklendi")

# 2) requestBasicPermissions metodunu bul ve değiştir.
signature = "private void requestBasicPermissions()"
start, end = find_method_bounds(s, signature)

if start == -1 or end == -1:
    raise SystemExit("❌ requestBasicPermissions metodu brace-match ile bulunamadı")

new_block = r'''private void requestBasicPermissions() {
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
    }'''

# Eski V86 metodları daha önce yarım eklendiyse temizlemek yerine önce mevcut requestBasicPermissions'ı değiştiriyoruz.
s = s[:start] + new_block + s[end:]

# 3) duplicate metod oluştuysa basit güvenlik: aynı imzadan ikinci varsa bildir.
MAIN.write_text(s, encoding="utf-8")

print()
print("===== KONTROL =====")
checks = [
    "createLockAlarmChannelsV86();",
    "requestNotificationPermissionV86();",
    "private void requestBasicPermissions()",
    "private void requestNotificationPermissionV86()",
    "private void createLockAlarmChannelsV86()",
    "Manifest.permission.ACCESS_FINE_LOCATION",
    "Manifest.permission.ACCESS_COARSE_LOCATION",
    "Manifest.permission.POST_NOTIFICATIONS",
    "Manifest.permission.CAMERA",
    "Manifest.permission.RECORD_AUDIO",
]

for c in checks:
    print(c, "=>", s.count(c))

print()
if s != old:
    print("✅ V86C düzeltme yapıldı")
else:
    print("ℹ️ Değişiklik yok")

print("✅ V86C tamam.")
