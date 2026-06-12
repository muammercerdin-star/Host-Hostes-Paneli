from pathlib import Path
from datetime import datetime
import shutil
import re

ROOT = Path(".").resolve()
STAMP = datetime.now().strftime("%Y%m%d-%H%M%S")

JAVA = ROOT / "android_app/app/src/main/java/com/muavinasistani/app/LiveStopAlertService.java"
RES = ROOT / "android_app/app/src/main/res"
LAYOUT = RES / "layout"
DRAWABLE = RES / "drawable"

print("===== V93B KİLİT EKRANI ÖZEL CANLI DURAK KARTI =====")

if not JAVA.exists():
    raise SystemExit("❌ LiveStopAlertService.java yok")

LAYOUT.mkdir(parents=True, exist_ok=True)
DRAWABLE.mkdir(parents=True, exist_ok=True)

def write_file(path: Path, text: str):
    if path.exists():
        bak = path.with_name(path.name + f".bak-v93b-{STAMP}")
        shutil.copy2(path, bak)
        print("📦 Yedek:", bak.relative_to(ROOT))
    path.write_text(text, encoding="utf-8")
    print("✅ Yazıldı:", path.relative_to(ROOT))

write_file(DRAWABLE / "bg_muavin_notify_card_v93b.xml", '''<?xml version="1.0" encoding="utf-8"?>
<shape xmlns:android="http://schemas.android.com/apk/res/android">
    <solid android:color="#111722"/>
    <corners android:radius="22dp"/>
    <stroke android:width="1dp" android:color="#55ff2f63"/>
    <padding android:left="0dp" android:right="0dp" android:top="0dp" android:bottom="0dp"/>
</shape>
''')

write_file(DRAWABLE / "bg_muavin_notify_metric_v93b.xml", '''<?xml version="1.0" encoding="utf-8"?>
<shape xmlns:android="http://schemas.android.com/apk/res/android">
    <solid android:color="#151c29"/>
    <corners android:radius="16dp"/>
    <stroke android:width="1dp" android:color="#24324a"/>
</shape>
''')

write_file(DRAWABLE / "bg_muavin_notify_button_v93b.xml", '''<?xml version="1.0" encoding="utf-8"?>
<shape xmlns:android="http://schemas.android.com/apk/res/android">
    <solid android:color="#253246"/>
    <corners android:radius="999dp"/>
</shape>
''')

write_file(LAYOUT / "notification_live_stop_collapsed_v93b.xml", '''<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:id="@+id/muavinNotifyRoot"
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    android:orientation="horizontal"
    android:gravity="center_vertical"
    android:padding="12dp"
    android:background="@drawable/bg_muavin_notify_card_v93b">

    <TextView
        android:id="@+id/muavinNotifyMiniIcon"
        android:layout_width="42dp"
        android:layout_height="42dp"
        android:gravity="center"
        android:text="🚌"
        android:textSize="24sp"
        android:background="@drawable/bg_muavin_notify_metric_v93b" />

    <LinearLayout
        android:layout_width="0dp"
        android:layout_height="wrap_content"
        android:layout_weight="1"
        android:orientation="vertical"
        android:paddingLeft="12dp"
        android:paddingRight="8dp">

        <TextView
            android:id="@+id/muavinNotifyKickerSmall"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="● CANLI DURAK"
            android:textColor="#ff2f63"
            android:textStyle="bold"
            android:textSize="12sp"
            android:letterSpacing="0.12" />

        <TextView
            android:id="@+id/muavinNotifyStopSmall"
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:text="Ortahan"
            android:textColor="#ffffff"
            android:textStyle="bold"
            android:textSize="22sp"
            android:maxLines="1"
            android:ellipsize="end" />

        <TextView
            android:id="@+id/muavinNotifySubSmall"
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:text="4.42 km • 2 yolcu • 0 bagaj"
            android:textColor="#c9d3e4"
            android:textSize="13sp"
            android:maxLines="1"
            android:ellipsize="end" />
    </LinearLayout>
</LinearLayout>
''')

write_file(LAYOUT / "notification_live_stop_big_v93b.xml", '''<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:id="@+id/muavinNotifyRootBig"
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    android:orientation="vertical"
    android:background="@drawable/bg_muavin_notify_card_v93b"
    android:padding="14dp">

    <LinearLayout
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:gravity="center_vertical"
        android:orientation="horizontal">

        <TextView
            android:id="@+id/muavinNotifyLive"
            android:layout_width="0dp"
            android:layout_height="wrap_content"
            android:layout_weight="1"
            android:text="● CANLI"
            android:textColor="#ff2f63"
            android:textStyle="bold"
            android:textSize="15sp"
            android:letterSpacing="0.18" />

        <TextView
            android:id="@+id/muavinNotifyMode"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="yakın takip"
            android:textColor="#d9deea"
            android:textStyle="bold"
            android:textSize="13sp"
            android:paddingLeft="14dp"
            android:paddingRight="14dp"
            android:paddingTop="8dp"
            android:paddingBottom="8dp"
            android:background="@drawable/bg_muavin_notify_button_v93b" />
    </LinearLayout>

    <TextView
        android:id="@+id/muavinNotifyStopBig"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:text="Ortahan"
        android:textColor="#ffffff"
        android:textStyle="bold"
        android:textSize="34sp"
        android:maxLines="1"
        android:ellipsize="end"
        android:paddingTop="8dp" />

    <TextView
        android:id="@+id/muavinNotifyDistanceBig"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:text="Kalan mesafe: 4.42 km"
        android:textColor="#d2d8e6"
        android:textStyle="bold"
        android:textSize="18sp"
        android:paddingTop="4dp"
        android:paddingBottom="12dp" />

    <LinearLayout
        android:layout_width="match_parent"
        android:layout_height="1dp"
        android:background="#263248" />

    <LinearLayout
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:orientation="horizontal"
        android:paddingTop="12dp">

        <LinearLayout
            android:id="@+id/muavinNotifyPassengerBox"
            android:layout_width="0dp"
            android:layout_height="92dp"
            android:layout_weight="1"
            android:orientation="vertical"
            android:gravity="center_vertical"
            android:padding="12dp"
            android:background="@drawable/bg_muavin_notify_metric_v93b">

            <TextView
                android:layout_width="wrap_content"
                android:layout_height="wrap_content"
                android:text="👤"
                android:textSize="22sp" />

            <TextView
                android:id="@+id/muavinNotifyPassengerCount"
                android:layout_width="wrap_content"
                android:layout_height="wrap_content"
                android:text="2 yolcu"
                android:textColor="#ff2f63"
                android:textStyle="bold"
                android:textSize="24sp" />

            <TextView
                android:layout_width="wrap_content"
                android:layout_height="wrap_content"
                android:text="İNECEK"
                android:textColor="#aab4c7"
                android:textStyle="bold"
                android:textSize="12sp"
                android:letterSpacing="0.18" />
        </LinearLayout>

        <Space
            android:layout_width="10dp"
            android:layout_height="1dp" />

        <LinearLayout
            android:id="@+id/muavinNotifyBagBox"
            android:layout_width="0dp"
            android:layout_height="92dp"
            android:layout_weight="1"
            android:orientation="vertical"
            android:gravity="center_vertical"
            android:padding="12dp"
            android:background="@drawable/bg_muavin_notify_metric_v93b">

            <TextView
                android:layout_width="wrap_content"
                android:layout_height="wrap_content"
                android:text="🧳"
                android:textSize="22sp" />

            <TextView
                android:id="@+id/muavinNotifyBagCount"
                android:layout_width="wrap_content"
                android:layout_height="wrap_content"
                android:text="0"
                android:textColor="#e6e9f2"
                android:textStyle="bold"
                android:textSize="26sp" />

            <TextView
                android:layout_width="wrap_content"
                android:layout_height="wrap_content"
                android:text="BAGAJ"
                android:textColor="#aab4c7"
                android:textStyle="bold"
                android:textSize="12sp"
                android:letterSpacing="0.18" />
        </LinearLayout>
    </LinearLayout>

    <TextView
        android:id="@+id/muavinNotifyStopButton"
        android:layout_width="match_parent"
        android:layout_height="42dp"
        android:layout_marginTop="12dp"
        android:gravity="center"
        android:text="Takibi kapat"
        android:textColor="#ffffff"
        android:textStyle="bold"
        android:textSize="14sp"
        android:background="@drawable/bg_muavin_notify_button_v93b" />
</LinearLayout>
''')

bak = JAVA.with_name(JAVA.name + f".bak-v93b-{STAMP}")
shutil.copy2(JAVA, bak)
print("📦 Java yedek:", bak.relative_to(ROOT))

s = JAVA.read_text(encoding="utf-8", errors="ignore")
old = s

if "import android.widget.RemoteViews;" not in s:
    s = s.replace("import android.widget.Toast;", "import android.widget.Toast;\nimport android.widget.RemoteViews;")

HELPERS = r'''
    // V93B_CUSTOM_NOTIFICATION_CARD
    private String v93bText(String value, String fallback) {
        String v = value == null ? "" : value.trim();
        return v.length() > 0 ? v : fallback;
    }

    private String v93bStopName() {
        return v93bText(stopName, "Canlı durak");
    }

    private String v93bDistanceText() {
        String d = v93bText(displayKm, "");
        if (d.length() == 0) return "Kalan mesafe: —";
        if (d.toLowerCase(new Locale("tr", "TR")).contains("km")) return "Kalan mesafe: " + d;
        return "Kalan mesafe: " + d + " km";
    }

    private String v93bSmallSubText() {
        String d = v93bText(displayKm, "—");
        if (!d.toLowerCase(new Locale("tr", "TR")).contains("km") && !d.equals("—")) d = d + " km";
        return d + " • " + offloadCount + " yolcu • " + bagCount + " bagaj";
    }

    private PendingIntent v93bOpenAppIntent() {
        Intent i = new Intent(this, MainActivity.class);
        i.setFlags(Intent.FLAG_ACTIVITY_NEW_TASK | Intent.FLAG_ACTIVITY_CLEAR_TOP);
        return PendingIntent.getActivity(
                this,
                93021,
                i,
                PendingIntent.FLAG_UPDATE_CURRENT | PendingIntent.FLAG_IMMUTABLE
        );
    }

    private PendingIntent v93bStopTrackingIntent() {
        Intent i = new Intent(this, LiveStopAlertService.class);
        i.setAction(ACTION_STOP_SERVICE);
        return PendingIntent.getService(
                this,
                93022,
                i,
                PendingIntent.FLAG_UPDATE_CURRENT | PendingIntent.FLAG_IMMUTABLE
        );
    }

    private RemoteViews buildLiveStopCollapsedV93B() {
        RemoteViews rv = new RemoteViews(getPackageName(), R.layout.notification_live_stop_collapsed_v93b);
        rv.setTextViewText(R.id.muavinNotifyStopSmall, v93bStopName());
        rv.setTextViewText(R.id.muavinNotifySubSmall, v93bSmallSubText());
        rv.setOnClickPendingIntent(R.id.muavinNotifyRoot, v93bOpenAppIntent());
        return rv;
    }

    private RemoteViews buildLiveStopBigV93B() {
        RemoteViews rv = new RemoteViews(getPackageName(), R.layout.notification_live_stop_big_v93b);
        rv.setTextViewText(R.id.muavinNotifyStopBig, v93bStopName());
        rv.setTextViewText(R.id.muavinNotifyDistanceBig, v93bDistanceText());
        rv.setTextViewText(R.id.muavinNotifyPassengerCount, offloadCount + " yolcu");
        rv.setTextViewText(R.id.muavinNotifyBagCount, String.valueOf(bagCount));
        rv.setTextViewText(R.id.muavinNotifyMode, "yakın takip");

        PendingIntent open = v93bOpenAppIntent();
        rv.setOnClickPendingIntent(R.id.muavinNotifyRootBig, open);
        rv.setOnClickPendingIntent(R.id.muavinNotifyPassengerBox, open);
        rv.setOnClickPendingIntent(R.id.muavinNotifyBagBox, open);
        rv.setOnClickPendingIntent(R.id.muavinNotifyStopButton, v93bStopTrackingIntent());
        return rv;
    }

'''

if "V93B_CUSTOM_NOTIFICATION_CARD" not in s:
    anchor = "    private void updateForegroundMonitor("
    if anchor in s:
        s = s.replace(anchor, HELPERS + "\n" + anchor, 1)
    else:
        anchor2 = "    @Override\n    public void onLocationChanged"
        if anchor2 in s:
            s = s.replace(anchor2, HELPERS + "\n" + anchor2, 1)
        else:
            raise SystemExit("❌ Java içine helper ekleme noktası bulunamadı")

# Notification builder zincirlerine custom view ekle.
# Daha önce eklenmişse tekrar ekleme.
if "setCustomBigContentView(buildLiveStopBigV93B())" not in s:
    s = s.replace(
        ".setSmallIcon(R.drawable.ic_muavin_notify)",
        ".setSmallIcon(R.drawable.ic_muavin_notify)\n"
        "                .setCustomContentView(buildLiveStopCollapsedV93B())\n"
        "                .setCustomBigContentView(buildLiveStopBigV93B())\n"
        "                .setStyle(new Notification.DecoratedCustomViewStyle())"
    )

# Eğer daha sonra BigTextStyle setStyle custom style'ı ezdiyse, onu kaldır.
s = re.sub(
    r"\n\s*\.setStyle\(new Notification\.BigTextStyle\(\)\.bigText\([^;]+?\)\)",
    "",
    s,
    flags=re.S
)

JAVA.write_text(s, encoding="utf-8")

print()
print("===== JAVA KONTROL =====")
for i, line in enumerate(s.splitlines(), 1):
    if any(k in line for k in [
        "V93B_CUSTOM_NOTIFICATION_CARD",
        "RemoteViews",
        "setCustomContentView",
        "setCustomBigContentView",
        "DecoratedCustomViewStyle",
        "muavinNotify"
    ]):
        print(f"{i}: {line.strip()}")

print()
print("✅ V93B tamam. Özel canlı durak bildirim kartı eklendi.")
