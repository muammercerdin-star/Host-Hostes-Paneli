from pathlib import Path
from datetime import datetime
import shutil

ROOT = Path(".").resolve()
STAMP = datetime.now().strftime("%Y%m%d-%H%M%S")

SERVICE = ROOT / "android_app/app/src/main/java/com/muavinasistani/app/LiveStopAlertService.java"
ACTIVITY = ROOT / "android_app/app/src/main/java/com/muavinasistani/app/LockAlarmActivity.java"
MANIFEST = ROOT / "android_app/app/src/main/AndroidManifest.xml"

print("===== V89 TAM EKRAN KİLİT ALARMI =====")

if not SERVICE.exists():
    raise SystemExit("❌ LiveStopAlertService.java yok")

if not MANIFEST.exists():
    raise SystemExit("❌ AndroidManifest.xml yok")

ACTIVITY_CODE = r'''package com.muavinasistani.app;

import android.app.Activity;
import android.content.Intent;
import android.content.SharedPreferences;
import android.graphics.Color;
import android.graphics.Typeface;
import android.os.Build;
import android.os.Bundle;
import android.view.Gravity;
import android.view.WindowManager;
import android.widget.Button;
import android.widget.LinearLayout;
import android.widget.TextView;

import java.util.Locale;

public class LockAlarmActivity extends Activity {
    private static final String PREF = "muavin_lock_alarm_v85";

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        try {
            getWindow().addFlags(
                    WindowManager.LayoutParams.FLAG_SHOW_WHEN_LOCKED
                            | WindowManager.LayoutParams.FLAG_TURN_SCREEN_ON
                            | WindowManager.LayoutParams.FLAG_KEEP_SCREEN_ON
            );

            if (Build.VERSION.SDK_INT >= 27) {
                setShowWhenLocked(true);
                setTurnScreenOn(true);
            }
        } catch (Exception ignored) {}

        buildUi();
    }

    private String clean(String v) {
        return v == null ? "" : v.trim();
    }

    private void buildUi() {
        SharedPreferences prefs = getSharedPreferences(PREF, MODE_PRIVATE);

        String stopName = clean(prefs.getString("stop_name", "Canlı durak"));
        String km = clean(prefs.getString("display_km", ""));
        if (km.length() == 0) km = "2 km";

        int offload = 0;
        int bag = 0;

        try {
            offload = Integer.parseInt(prefs.getString("offload_count", "0"));
        } catch (Exception ignored) {}

        try {
            bag = Integer.parseInt(prefs.getString("bag_count", "0"));
        } catch (Exception ignored) {}

        String yolcu = offload > 0 ? offload + " yolcu inecek" : "İnecek yolcu yok";
        String bagaj = bag > 0 ? bag + " bagaj var" : "0 bagaj";

        LinearLayout root = new LinearLayout(this);
        root.setOrientation(LinearLayout.VERTICAL);
        root.setGravity(Gravity.CENTER);
        root.setPadding(42, 42, 42, 42);
        root.setBackgroundColor(Color.rgb(10, 12, 20));

        TextView badge = new TextView(this);
        badge.setText("CANLI DURAK ALARMI");
        badge.setTextColor(Color.rgb(255, 45, 96));
        badge.setTextSize(18);
        badge.setTypeface(Typeface.DEFAULT_BOLD);
        badge.setLetterSpacing(0.14f);
        badge.setGravity(Gravity.CENTER);
        root.addView(badge, new LinearLayout.LayoutParams(
                LinearLayout.LayoutParams.MATCH_PARENT,
                LinearLayout.LayoutParams.WRAP_CONTENT
        ));

        TextView stop = new TextView(this);
        stop.setText(stopName.toLocaleUpperCase(new Locale("tr", "TR")));
        stop.setTextColor(Color.WHITE);
        stop.setTextSize(48);
        stop.setTypeface(Typeface.DEFAULT_BOLD);
        stop.setGravity(Gravity.CENTER);
        stop.setPadding(0, 28, 0, 8);
        root.addView(stop, new LinearLayout.LayoutParams(
                LinearLayout.LayoutParams.MATCH_PARENT,
                LinearLayout.LayoutParams.WRAP_CONTENT
        ));

        TextView dist = new TextView(this);
        dist.setText("Kalan mesafe: " + km);
        dist.setTextColor(Color.rgb(230, 230, 235));
        dist.setTextSize(24);
        dist.setTypeface(Typeface.DEFAULT_BOLD);
        dist.setGravity(Gravity.CENTER);
        dist.setPadding(0, 4, 0, 22);
        root.addView(dist, new LinearLayout.LayoutParams(
                LinearLayout.LayoutParams.MATCH_PARENT,
                LinearLayout.LayoutParams.WRAP_CONTENT
        ));

        TextView info = new TextView(this);
        info.setText(yolcu + "  •  " + bagaj);
        info.setTextColor(Color.rgb(220, 220, 225));
        info.setTextSize(22);
        info.setGravity(Gravity.CENTER);
        info.setPadding(0, 0, 0, 38);
        root.addView(info, new LinearLayout.LayoutParams(
                LinearLayout.LayoutParams.MATCH_PARENT,
                LinearLayout.LayoutParams.WRAP_CONTENT
        ));

        Button stopBtn = new Button(this);
        stopBtn.setText("ALARMı DURDUR");
        stopBtn.setTextSize(20);
        stopBtn.setTypeface(Typeface.DEFAULT_BOLD);
        stopBtn.setTextColor(Color.WHITE);
        stopBtn.setBackgroundColor(Color.rgb(255, 45, 96));
        stopBtn.setAllCaps(false);
        stopBtn.setOnClickListener(v -> {
            try {
                Intent i = new Intent(this, LiveStopAlertService.class);
                i.setAction(LiveStopAlertService.ACTION_STOP_ALARM);
                startService(i);
            } catch (Exception ignored) {}
            finish();
        });

        LinearLayout.LayoutParams stopLp = new LinearLayout.LayoutParams(
                LinearLayout.LayoutParams.MATCH_PARENT,
                120
        );
        stopLp.setMargins(0, 0, 0, 22);
        root.addView(stopBtn, stopLp);

        Button openBtn = new Button(this);
        openBtn.setText("Uygulamayı aç");
        openBtn.setTextSize(18);
        openBtn.setAllCaps(false);
        openBtn.setOnClickListener(v -> {
            try {
                Intent i = new Intent(this, MainActivity.class);
                i.setFlags(Intent.FLAG_ACTIVITY_CLEAR_TOP | Intent.FLAG_ACTIVITY_SINGLE_TOP);
                startActivity(i);
            } catch (Exception ignored) {}
            finish();
        });

        LinearLayout.LayoutParams openLp = new LinearLayout.LayoutParams(
                LinearLayout.LayoutParams.MATCH_PARENT,
                105
        );
        root.addView(openBtn, openLp);

        setContentView(root);
    }
}
'''

ACTIVITY.write_text(ACTIVITY_CODE, encoding="utf-8")
print("✅ LockAlarmActivity yazıldı:", ACTIVITY.relative_to(ROOT))

# Manifest patch
mb = MANIFEST.with_name(MANIFEST.name + f".bak-v89-{STAMP}")
shutil.copy2(MANIFEST, mb)
print("📦 Manifest yedeği:", mb.relative_to(ROOT))

m = MANIFEST.read_text(encoding="utf-8", errors="ignore")

if "android.permission.USE_FULL_SCREEN_INTENT" not in m:
    m = m.replace(
        "    <application",
        '    <uses-permission android:name="android.permission.USE_FULL_SCREEN_INTENT" />\n\n    <application'
    )
    print("✅ USE_FULL_SCREEN_INTENT izni eklendi")

activity_tag = r'''        <activity
            android:name=".LockAlarmActivity"
            android:exported="false"
            android:excludeFromRecents="true"
            android:showWhenLocked="true"
            android:turnScreenOn="true"
            android:screenOrientation="portrait" />
'''

if ".LockAlarmActivity" not in m:
    if "        <service" in m:
        m = m.replace("        <service", activity_tag + "\n        <service", 1)
    else:
        m = m.replace("        <activity", activity_tag + "\n        <activity", 1)
    print("✅ LockAlarmActivity manifest kaydı eklendi")

MANIFEST.write_text(m, encoding="utf-8")

# Service patch
sb = SERVICE.with_name(SERVICE.name + f".bak-v89-{STAMP}")
shutil.copy2(SERVICE, sb)
print("📦 Service yedeği:", sb.relative_to(ROOT))

s = SERVICE.read_text(encoding="utf-8", errors="ignore")

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

# buildAlertNotification içine fullScreenIntent ekle
start, end = find_method_bounds(s, "private Notification buildAlertNotification")
if start == -1:
    print("⚠️ buildAlertNotification bulunamadı, sadece startActivity kullanılacak")
else:
    seg = s[start:end]
    if "LockAlarmActivity.class" not in seg:
        seg = seg.replace(
            '        PendingIntent openPi = PendingIntent.getActivity(this, 20, openIntent, piFlags);\n',
            '        PendingIntent openPi = PendingIntent.getActivity(this, 20, openIntent, piFlags);\n\n'
            '        Intent alarmScreenIntent = new Intent(this, LockAlarmActivity.class);\n'
            '        alarmScreenIntent.setFlags(Intent.FLAG_ACTIVITY_NEW_TASK | Intent.FLAG_ACTIVITY_CLEAR_TOP | Intent.FLAG_ACTIVITY_SINGLE_TOP);\n'
            '        PendingIntent alarmScreenPi = PendingIntent.getActivity(this, 22, alarmScreenIntent, piFlags);\n'
        )

        seg = seg.replace(
            '                .setContentIntent(openPi)\n',
            '                .setContentIntent(openPi)\n'
            '                .setFullScreenIntent(alarmScreenPi, true)\n',
            1
        )

        s = s[:start] + seg + s[end:]
        print("✅ Alert notification fullScreenIntent eklendi")
    else:
        print("ℹ️ fullScreenIntent zaten var")

# showAlarmNotification sonunda activity launch ekle
start, end = find_method_bounds(s, "private void showAlarmNotification")
if start == -1:
    print("⚠️ showAlarmNotification bulunamadı")
else:
    seg = s[start:end]
    if "launchLockAlarmActivityV89();" not in seg:
        seg = seg.replace(
            "        } catch (Exception ignored) {}",
            "        } catch (Exception ignored) {}\n\n"
            "        launchLockAlarmActivityV89();",
            1
        )
        s = s[:start] + seg + s[end:]
        print("✅ showAlarmNotification içine activity launch eklendi")

# launch method ekle
if "private void launchLockAlarmActivityV89()" not in s:
    insert = r'''
    private void launchLockAlarmActivityV89() {
        try {
            Intent i = new Intent(this, LockAlarmActivity.class);
            i.setFlags(Intent.FLAG_ACTIVITY_NEW_TASK | Intent.FLAG_ACTIVITY_CLEAR_TOP | Intent.FLAG_ACTIVITY_SINGLE_TOP);
            startActivity(i);
        } catch (Exception ignored) {}
    }

'''
    marker = "    private void startForegroundSafe"
    if marker not in s:
        raise SystemExit("❌ startForegroundSafe marker bulunamadı")
    s = s.replace(marker, insert + marker, 1)
    print("✅ launchLockAlarmActivityV89 metodu eklendi")

SERVICE.write_text(s, encoding="utf-8")

print()
print("===== KONTROL =====")
for p in [ACTIVITY, SERVICE, MANIFEST]:
    txt = p.read_text(encoding="utf-8", errors="ignore")
    for i, line in enumerate(txt.splitlines(), 1):
        if any(k in line for k in [
            "LockAlarmActivity",
            "USE_FULL_SCREEN_INTENT",
            "setFullScreenIntent",
            "launchLockAlarmActivityV89",
            "ALARMı DURDUR",
            "ACTION_STOP_ALARM"
        ]):
            print(f"{p.relative_to(ROOT)}:{i}: {line}")

print()
print("✅ V89 tamam.")
