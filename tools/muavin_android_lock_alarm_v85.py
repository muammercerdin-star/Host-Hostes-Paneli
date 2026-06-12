from pathlib import Path
from datetime import datetime
import shutil
import re

ROOT = Path(".").resolve()
STAMP = datetime.now().strftime("%Y%m%d-%H%M%S")

MAIN = ROOT / "android_app/app/src/main/java/com/muavinasistani/app/MainActivity.java"
MANIFEST = ROOT / "android_app/app/src/main/AndroidManifest.xml"
SERVICE = ROOT / "android_app/app/src/main/java/com/muavinasistani/app/LiveStopAlertService.java"

JS_WEB = ROOT / "static/continue/continue_native_lock_alarm_v85.js"
JS_AND = ROOT / "android_app/app/src/main/python/static/continue/continue_native_lock_alarm_v85.js"

TPLS = [
    ROOT / "templates/continue_trip.html",
    ROOT / "android_app/app/src/main/python/templates/continue_trip.html",
]

print("===== V85 KİLİTLİ EKRAN ALARM + TİTREŞİM + DURDUR =====")

SERVICE_CODE = r'''package com.muavinasistani.app;

import android.Manifest;
import android.app.Notification;
import android.app.NotificationChannel;
import android.app.NotificationManager;
import android.app.PendingIntent;
import android.app.Service;
import android.content.Intent;
import android.content.SharedPreferences;
import android.content.pm.PackageManager;
import android.content.pm.ServiceInfo;
import android.location.Location;
import android.location.LocationListener;
import android.location.LocationManager;
import android.os.Build;
import android.os.Bundle;
import android.os.IBinder;
import android.os.VibrationEffect;
import android.os.Vibrator;
import android.speech.tts.TextToSpeech;

import java.util.Locale;
import java.util.Map;

public class LiveStopAlertService extends Service implements LocationListener {
    public static final String ACTION_START = "com.muavinasistani.app.LOCK_ALARM_START";
    public static final String ACTION_STOP_SERVICE = "com.muavinasistani.app.LOCK_ALARM_STOP_SERVICE";
    public static final String ACTION_STOP_ALARM = "com.muavinasistani.app.LOCK_ALARM_STOP_ALARM";
    public static final String ACTION_RESET = "com.muavinasistani.app.LOCK_ALARM_RESET";

    private static final String CHANNEL_MONITOR = "muavin_live_monitor_v85";
    private static final String CHANNEL_ALERT = "muavin_live_alert_v85";
    private static final int NOTIFICATION_ID = 8501;
    private static final String PREF = "muavin_lock_alarm_v85";

    private LocationManager locationManager;
    private TextToSpeech tts;
    private boolean ttsReady = false;
    private String pendingSpeech = "";

    private SharedPreferences prefs;

    private String tripId = "active";
    private String stopName = "";
    private double targetLat = Double.NaN;
    private double targetLng = Double.NaN;
    private int offloadCount = 0;
    private int bagCount = 0;

    private boolean alarmActive = false;

    @Override
    public void onCreate() {
        super.onCreate();

        prefs = getSharedPreferences(PREF, MODE_PRIVATE);
        createChannels();

        tts = new TextToSpeech(this, status -> {
            if (status == TextToSpeech.SUCCESS) {
                tts.setLanguage(new Locale("tr", "TR"));
                tts.setSpeechRate(0.95f);
                tts.setPitch(1.0f);
                ttsReady = true;

                if (pendingSpeech != null && pendingSpeech.trim().length() > 0) {
                    speakNow(pendingSpeech);
                    pendingSpeech = "";
                }
            }
        });

        locationManager = (LocationManager) getSystemService(LOCATION_SERVICE);
    }

    @Override
    public int onStartCommand(Intent intent, int flags, int startId) {
        String action = intent != null ? intent.getAction() : "";

        if (ACTION_STOP_ALARM.equals(action)) {
            stopAlarmOnly();
            return START_STICKY;
        }

        if (ACTION_STOP_SERVICE.equals(action)) {
            stopEverything();
            stopSelf();
            return START_NOT_STICKY;
        }

        if (ACTION_RESET.equals(action)) {
            resetAlertMemory();
            updateForegroundMonitor();
            return START_STICKY;
        }

        loadTargetFromPrefs();
        updateForegroundMonitor();
        startLocationUpdates();
        checkLastKnownLocation();

        return START_STICKY;
    }

    private void loadTargetFromPrefs() {
        tripId = prefs.getString("trip_id", "active");
        stopName = prefs.getString("stop_name", "");

        try {
            targetLat = Double.parseDouble(prefs.getString("target_lat", ""));
            targetLng = Double.parseDouble(prefs.getString("target_lng", ""));
        } catch (Exception e) {
            targetLat = Double.NaN;
            targetLng = Double.NaN;
        }

        try {
            offloadCount = Integer.parseInt(prefs.getString("offload_count", "0"));
        } catch (Exception e) {
            offloadCount = 0;
        }

        try {
            bagCount = Integer.parseInt(prefs.getString("bag_count", "0"));
        } catch (Exception e) {
            bagCount = 0;
        }
    }

    private boolean validCoord() {
        return !Double.isNaN(targetLat)
                && !Double.isNaN(targetLng)
                && !Double.isInfinite(targetLat)
                && !Double.isInfinite(targetLng);
    }

    private void updateForegroundMonitor() {
        String body = stopName != null && stopName.trim().length() > 0
                ? stopName + " durağı takip ediliyor"
                : "Canlı durak takip ediliyor";

        startForegroundSafe(buildNotification(
                CHANNEL_MONITOR,
                "Muavin Asistanı canlı takip",
                body,
                false
        ));
    }

    private void showAlarmNotification(String message) {
        alarmActive = true;
        startVibration();

        startForegroundSafe(buildNotification(
                CHANNEL_ALERT,
                "Canlı durak uyarısı",
                message,
                true
        ));
    }

    private Notification buildNotification(String channelId, String title, String body, boolean alertMode) {
        Intent openIntent = new Intent(this, MainActivity.class);
        openIntent.setFlags(Intent.FLAG_ACTIVITY_SINGLE_TOP | Intent.FLAG_ACTIVITY_CLEAR_TOP);

        int piFlags = PendingIntent.FLAG_UPDATE_CURRENT;
        if (Build.VERSION.SDK_INT >= 23) piFlags |= PendingIntent.FLAG_IMMUTABLE;

        PendingIntent openPi = PendingIntent.getActivity(this, 10, openIntent, piFlags);

        Intent stopAlarmIntent = new Intent(this, LiveStopAlertService.class);
        stopAlarmIntent.setAction(ACTION_STOP_ALARM);
        PendingIntent stopAlarmPi = PendingIntent.getService(this, 11, stopAlarmIntent, piFlags);

        Intent stopServiceIntent = new Intent(this, LiveStopAlertService.class);
        stopServiceIntent.setAction(ACTION_STOP_SERVICE);
        PendingIntent stopServicePi = PendingIntent.getService(this, 12, stopServiceIntent, piFlags);

        Notification.Builder b = new Notification.Builder(this, channelId)
                .setSmallIcon(android.R.drawable.ic_dialog_map)
                .setContentTitle(title)
                .setContentText(body)
                .setContentIntent(openPi)
                .setOngoing(!alertMode)
                .setOnlyAlertOnce(false)
                .setVisibility(Notification.VISIBILITY_PUBLIC)
                .setCategory(alertMode ? Notification.CATEGORY_ALARM : Notification.CATEGORY_SERVICE);

        if (Build.VERSION.SDK_INT >= 21) {
            b.setPriority(alertMode ? Notification.PRIORITY_MAX : Notification.PRIORITY_LOW);
        }

        if (alertMode) {
            b.addAction(android.R.drawable.ic_media_pause, "Alarmı durdur", stopAlarmPi);
            b.addAction(android.R.drawable.ic_menu_view, "Uygulamayı aç", openPi);
            b.setAutoCancel(false);
        } else {
            b.addAction(android.R.drawable.ic_menu_close_clear_cancel, "Takibi kapat", stopServicePi);
        }

        return b.build();
    }

    private void startForegroundSafe(Notification notification) {
        try {
            if (Build.VERSION.SDK_INT >= 29) {
                startForeground(
                        NOTIFICATION_ID,
                        notification,
                        ServiceInfo.FOREGROUND_SERVICE_TYPE_LOCATION
                );
            } else {
                startForeground(NOTIFICATION_ID, notification);
            }
        } catch (Exception e) {
            try {
                startForeground(NOTIFICATION_ID, notification);
            } catch (Exception ignored) {}
        }
    }

    private void createChannels() {
        if (Build.VERSION.SDK_INT < 26) return;

        NotificationManager nm = (NotificationManager) getSystemService(NOTIFICATION_SERVICE);
        if (nm == null) return;

        NotificationChannel monitor = new NotificationChannel(
                CHANNEL_MONITOR,
                "Canlı durak takip",
                NotificationManager.IMPORTANCE_LOW
        );
        monitor.setDescription("Canlı durak arka plan takibi");

        NotificationChannel alert = new NotificationChannel(
                CHANNEL_ALERT,
                "Canlı durak alarmı",
                NotificationManager.IMPORTANCE_HIGH
        );
        alert.setDescription("2 km kala sesli ve titreşimli uyarı");
        alert.enableVibration(true);
        alert.setVibrationPattern(new long[]{0, 600, 300, 600, 300, 900});

        nm.createNotificationChannel(monitor);
        nm.createNotificationChannel(alert);
    }

    private boolean hasLocationPermission() {
        return checkSelfPermission(Manifest.permission.ACCESS_FINE_LOCATION) == PackageManager.PERMISSION_GRANTED
                || checkSelfPermission(Manifest.permission.ACCESS_COARSE_LOCATION) == PackageManager.PERMISSION_GRANTED;
    }

    private void startLocationUpdates() {
        if (!hasLocationPermission()) return;
        if (locationManager == null) return;

        try {
            locationManager.requestLocationUpdates(LocationManager.GPS_PROVIDER, 5000, 10, this);
        } catch (Exception ignored) {}

        try {
            locationManager.requestLocationUpdates(LocationManager.NETWORK_PROVIDER, 7000, 20, this);
        } catch (Exception ignored) {}
    }

    private void checkLastKnownLocation() {
        if (!hasLocationPermission()) return;
        if (locationManager == null) return;

        try {
            Location gps = locationManager.getLastKnownLocation(LocationManager.GPS_PROVIDER);
            if (gps != null) onLocationChanged(gps);
        } catch (Exception ignored) {}

        try {
            Location net = locationManager.getLastKnownLocation(LocationManager.NETWORK_PROVIDER);
            if (net != null) onLocationChanged(net);
        } catch (Exception ignored) {}
    }

    @Override
    public void onLocationChanged(Location location) {
        loadTargetFromPrefs();

        if (location == null) return;
        if (stopName == null || stopName.trim().length() == 0) return;
        if (!validCoord()) return;

        float[] result = new float[1];
        Location.distanceBetween(
                location.getLatitude(),
                location.getLongitude(),
                targetLat,
                targetLng,
                result
        );

        double km = result[0] / 1000.0;

        if (km <= 2.05 && km >= 0.05) {
            String key = alertKey();
            if (!prefs.getBoolean(key, false)) {
                prefs.edit().putBoolean(key, true).apply();

                String msg = buildSpeechMessage();
                speak(msg);
                showAlarmNotification(buildLockMessage());
            }
        }
    }

    private String buildSpeechMessage() {
        if (offloadCount > 0) {
            return stopName + " durağına 2 kilometre kaldı. " + offloadCount + " yolcu inecek.";
        }
        return stopName + " durağına 2 kilometre kaldı. İnecek yolcu yok.";
    }

    private String buildLockMessage() {
        String yolcu = offloadCount > 0 ? offloadCount + " yolcu inecek" : "İnecek yolcu yok";
        String bag = bagCount > 0 ? bagCount + " bagaj var" : "Bagaj yok";
        return stopName + " • 2 km kaldı • " + yolcu + " • " + bag;
    }

    private String alertKey() {
        String safeStop = stopName == null ? "" : stopName.toLowerCase(new Locale("tr", "TR")).replaceAll("[^a-z0-9çğıöşü]+", "_");
        return "alerted_2km_" + tripId + "_" + safeStop;
    }

    private void speak(String msg) {
        if (msg == null || msg.trim().length() == 0) return;

        if (!ttsReady || tts == null) {
            pendingSpeech = msg;
            return;
        }

        speakNow(msg);
    }

    private void speakNow(String msg) {
        try {
            if (tts == null) return;
            tts.stop();
            tts.speak(msg, TextToSpeech.QUEUE_FLUSH, null, "muavin_lock_alarm_v85");
        } catch (Exception ignored) {}
    }

    private void startVibration() {
        try {
            Vibrator vibrator = (Vibrator) getSystemService(VIBRATOR_SERVICE);
            if (vibrator == null) return;

            long[] pattern = new long[]{0, 700, 300, 700, 300, 1000};

            if (Build.VERSION.SDK_INT >= 26) {
                vibrator.vibrate(VibrationEffect.createWaveform(pattern, 0));
            } else {
                vibrator.vibrate(pattern, 0);
            }
        } catch (Exception ignored) {}
    }

    private void stopVibration() {
        try {
            Vibrator vibrator = (Vibrator) getSystemService(VIBRATOR_SERVICE);
            if (vibrator != null) vibrator.cancel();
        } catch (Exception ignored) {}
    }

    private void stopAlarmOnly() {
        alarmActive = false;

        stopVibration();

        try {
            if (tts != null) tts.stop();
        } catch (Exception ignored) {}

        updateForegroundMonitor();
    }

    private void stopEverything() {
        stopAlarmOnly();

        try {
            if (locationManager != null) locationManager.removeUpdates(this);
        } catch (Exception ignored) {}

        try {
            if (tts != null) {
                tts.stop();
                tts.shutdown();
            }
        } catch (Exception ignored) {}

        try {
            stopForeground(true);
        } catch (Exception ignored) {}
    }

    private void resetAlertMemory() {
        try {
            SharedPreferences.Editor e = prefs.edit();
            Map<String, ?> all = prefs.getAll();

            for (String k : all.keySet()) {
                if (k != null && k.startsWith("alerted_2km_")) {
                    e.remove(k);
                }
            }

            e.apply();
        } catch (Exception ignored) {}
    }

    @Override public void onProviderEnabled(String provider) {}
    @Override public void onProviderDisabled(String provider) {}
    @Override public void onStatusChanged(String provider, int status, Bundle extras) {}

    @Override
    public void onDestroy() {
        stopEverything();
        super.onDestroy();
    }

    @Override
    public IBinder onBind(Intent intent) {
        return null;
    }
}
'''

JS_CODE = r'''/* CONTINUE_NATIVE_LOCK_ALARM_V85
   WebView -> Android kilit ekranı alarm servisi.
   V82 kuralı: canlı durak GPS ile değişmez.
*/
(function(){
  if(window.CONTINUE_NATIVE_LOCK_ALARM_V85_READY) return;
  window.CONTINUE_NATIVE_LOCK_ALARM_V85_READY = true;

  const BOOT = window.CONTINUE_BOOT || {};
  const tripId = String(BOOT.tripId || BOOT.trip_id || "active");
  const routeCoords = Array.isArray(BOOT.routeCoords) ? BOOT.routeCoords : [];

  let started = false;
  let lastSig = "";

  function clean(v){
    return String(v == null ? "" : v).replace(/\s+/g, " ").trim();
  }

  function norm(v){
    return clean(v).toLocaleLowerCase("tr-TR");
  }

  function numFromText(v){
    const m = clean(v).match(/\d+/);
    return m ? Number(m[0]) : 0;
  }

  function currentStop(){
    const el = document.getElementById("liveCurrentStopName");
    return clean(el && el.textContent);
  }

  function offloadCount(){
    const el = document.getElementById("liveOffloadCount");
    return numFromText(el && el.textContent);
  }

  function bagCount(){
    const selectors = [
      "#liveBagajCount",
      "#liveBagCount",
      "#liveBagajMetric",
      "#liveBagMetric",
      "[data-live-bag-count]"
    ];

    for(const sel of selectors){
      const el = document.querySelector(sel);
      if(el){
        const n = numFromText(el.textContent);
        if(Number.isFinite(n)) return n;
      }
    }

    return 0;
  }

  function findCoord(stop){
    const key = norm(stop);
    if(!key) return null;

    for(const item of routeCoords){
      const name = clean(item.stop || item.name || "");
      if(norm(name) !== key) continue;

      const lat = Number(item.lat ?? item.latitude);
      const lng = Number(item.lng ?? item.lon ?? item.longitude);

      if(Number.isFinite(lat) && Number.isFinite(lng)){
        return { lat, lng };
      }
    }

    return null;
  }

  function sync(){
    try{
      if(!window.AndroidLockAlarm) return;

      const stop = currentStop();
      if(!stop) return;

      const c = findCoord(stop);
      if(!c) return;

      const off = offloadCount();
      const bag = bagCount();

      const sig = [tripId, stop, c.lat, c.lng, off, bag].join("|");

      if(sig !== lastSig){
        lastSig = sig;
        window.AndroidLockAlarm.updateTarget(
          tripId,
          stop,
          String(c.lat),
          String(c.lng),
          String(off),
          String(bag)
        );
      }

      if(!started){
        started = true;
        window.AndroidLockAlarm.start();
      }
    }catch(err){
      console.warn("CONTINUE_NATIVE_LOCK_ALARM_V85 sync error", err);
    }
  }

  function stopService(){
    try{
      if(window.AndroidLockAlarm) window.AndroidLockAlarm.stopService();
    }catch(_){}
  }

  window.continueNativeLockAlarmV85 = {
    sync,
    stopAlarm(){
      try{
        if(window.AndroidLockAlarm) window.AndroidLockAlarm.stopAlarm();
      }catch(_){}
    },
    stopService,
    reset(){
      try{
        if(window.AndroidLockAlarm) window.AndroidLockAlarm.reset();
      }catch(_){}
    }
  };

  if(document.readyState === "loading"){
    document.addEventListener("DOMContentLoaded", sync);
  }else{
    sync();
  }

  setInterval(sync, 3000);

  if(window.MutationObserver){
    const targets = [
      document.getElementById("liveCurrentStopName"),
      document.getElementById("liveOffloadCount"),
      document.getElementById("liveBagajCount"),
      document.getElementById("liveBagajMetric")
    ].filter(Boolean);

    const obs = new MutationObserver(sync);
    targets.forEach(el => obs.observe(el, { childList:true, characterData:true, subtree:true }));
  }
})();
'''

BRIDGE_CODE = r'''
    public class LockAlarmBridge {
        @JavascriptInterface
        public void updateTarget(String tripId, String stopName, String lat, String lng, String offloadCount, String bagCount) {
            try {
                android.content.SharedPreferences prefs = getSharedPreferences("muavin_lock_alarm_v85", MODE_PRIVATE);
                prefs.edit()
                        .putString("trip_id", tripId == null ? "active" : tripId.trim())
                        .putString("stop_name", stopName == null ? "" : stopName.trim())
                        .putString("target_lat", lat == null ? "" : lat.trim())
                        .putString("target_lng", lng == null ? "" : lng.trim())
                        .putString("offload_count", offloadCount == null ? "0" : offloadCount.trim())
                        .putString("bag_count", bagCount == null ? "0" : bagCount.trim())
                        .putBoolean("enabled", true)
                        .apply();
            } catch (Exception ignored) {}
        }

        @JavascriptInterface
        public void start() {
            runOnUiThread(() -> startLiveStopAlarmService());
        }

        @JavascriptInterface
        public void stopAlarm() {
            runOnUiThread(() -> sendLiveStopAlarmAction(LiveStopAlertService.ACTION_STOP_ALARM));
        }

        @JavascriptInterface
        public void stopService() {
            runOnUiThread(() -> sendLiveStopAlarmAction(LiveStopAlertService.ACTION_STOP_SERVICE));
        }

        @JavascriptInterface
        public void reset() {
            runOnUiThread(() -> sendLiveStopAlarmAction(LiveStopAlertService.ACTION_RESET));
        }
    }

    private void startLiveStopAlarmService() {
        try {
            Intent i = new Intent(this, LiveStopAlertService.class);
            i.setAction(LiveStopAlertService.ACTION_START);

            if (android.os.Build.VERSION.SDK_INT >= 26) {
                startForegroundService(i);
            } else {
                startService(i);
            }
        } catch (Exception e) {
            Toast.makeText(this, "Kilitli ekran alarmı başlatılamadı", Toast.LENGTH_SHORT).show();
        }
    }

    private void sendLiveStopAlarmAction(String action) {
        try {
            Intent i = new Intent(this, LiveStopAlertService.class);
            i.setAction(action);
            startService(i);
        } catch (Exception ignored) {}
    }

'''

NEW_PERMISSION_METHOD = r'''    private void requestBasicPermissions() {
        if (android.os.Build.VERSION.SDK_INT >= 33) {
            requestPermissions(new String[]{
                    Manifest.permission.ACCESS_FINE_LOCATION,
                    Manifest.permission.ACCESS_COARSE_LOCATION,
                    Manifest.permission.CAMERA,
                    Manifest.permission.RECORD_AUDIO,
                    Manifest.permission.POST_NOTIFICATIONS
            }, 100);
            return;
        }

        if (android.os.Build.VERSION.SDK_INT >= 23) {
            requestPermissions(new String[]{
                    Manifest.permission.ACCESS_FINE_LOCATION,
                    Manifest.permission.ACCESS_COARSE_LOCATION,
                    Manifest.permission.CAMERA,
                    Manifest.permission.RECORD_AUDIO
            }, 100);
        }
    }
'''

# 1) Service yaz
SERVICE.parent.mkdir(parents=True, exist_ok=True)
if SERVICE.exists():
    b = SERVICE.with_name(SERVICE.name + f".bak-v85-{STAMP}")
    shutil.copy2(SERVICE, b)
    print("📦 Service yedeği:", b.relative_to(ROOT))

SERVICE.write_text(SERVICE_CODE, encoding="utf-8")
print("✅ Service yazıldı:", SERVICE.relative_to(ROOT))

# 2) MainActivity patch
if not MAIN.exists():
    raise SystemExit("❌ MainActivity.java yok")

b = MAIN.with_name(MAIN.name + f".bak-lock-alarm-v85-{STAMP}")
shutil.copy2(MAIN, b)
print("📦 MainActivity yedeği:", b.relative_to(ROOT))

s = MAIN.read_text(encoding="utf-8", errors="ignore")

if 'webView.addJavascriptInterface(new LockAlarmBridge(), "AndroidLockAlarm");' not in s:
    s = s.replace(
        '        webView.addJavascriptInterface(new PrintBridge(), "PrintBridge");',
        '        webView.addJavascriptInterface(new PrintBridge(), "PrintBridge");\n'
        '        webView.addJavascriptInterface(new LockAlarmBridge(), "AndroidLockAlarm");'
    )
    print("✅ AndroidLockAlarm bridge bağlandı")
else:
    print("ℹ️ AndroidLockAlarm bridge zaten var")

if "public class LockAlarmBridge" not in s:
    s = s.replace(
        "    public class VoiceBridge {",
        BRIDGE_CODE + "\n    public class VoiceBridge {"
    )
    print("✅ LockAlarmBridge class eklendi")
else:
    print("ℹ️ LockAlarmBridge class zaten var")

s2 = re.sub(
    r'    private void requestBasicPermissions\(\) \{[\s\S]*?\n    \}\n\n\n    @Override\n    protected void onDestroy',
    NEW_PERMISSION_METHOD + "\n\n\n    @Override\n    protected void onDestroy",
    s,
    count=1
)

if s2 != s:
    s = s2
    print("✅ Runtime izin metodu güncellendi")
else:
    print("⚠️ Runtime izin metodu otomatik değişmedi")

MAIN.write_text(s, encoding="utf-8")

# 3) Manifest patch
if not MANIFEST.exists():
    raise SystemExit("❌ AndroidManifest.xml yok")

b = MANIFEST.with_name(MANIFEST.name + f".bak-lock-alarm-v85-{STAMP}")
shutil.copy2(MANIFEST, b)
print("📦 Manifest yedeği:", b.relative_to(ROOT))

m = MANIFEST.read_text(encoding="utf-8", errors="ignore")

perms = [
    "android.permission.FOREGROUND_SERVICE",
    "android.permission.FOREGROUND_SERVICE_LOCATION",
    "android.permission.POST_NOTIFICATIONS",
    "android.permission.WAKE_LOCK",
    "android.permission.VIBRATE",
]

insert = ""
for perm in perms:
    if perm not in m:
        insert += f'    <uses-permission android:name="{perm}" />\n'

if insert:
    m = m.replace("    <application", insert + "\n    <application")
    print("✅ Manifest izinleri eklendi")
else:
    print("ℹ️ Manifest izinleri zaten var")

service_tag = r'''        <service
            android:name=".LiveStopAlertService"
            android:exported="false"
            android:foregroundServiceType="location" />
'''

if ".LiveStopAlertService" not in m:
    m = m.replace("        <activity", service_tag + "\n        <activity")
    print("✅ Manifest service kaydı eklendi")
else:
    print("ℹ️ Manifest service kaydı zaten var")

MANIFEST.write_text(m, encoding="utf-8")

# 4) JS yaz
for p in [JS_WEB, JS_AND]:
    p.parent.mkdir(parents=True, exist_ok=True)
    if p.exists():
        b = p.with_name(p.name + f".bak-v85-{STAMP}")
        shutil.copy2(p, b)
        print("📦 JS yedeği:", b.relative_to(ROOT))

    p.write_text(JS_CODE, encoding="utf-8")
    print("✅ JS yazıldı:", p.relative_to(ROOT))

# 5) Template çağrısı ekle
SCRIPT = """<script src="{{ url_for('static', filename='continue/continue_native_lock_alarm_v85.js') }}?v=native-lock-alarm-v85"></script>"""

for p in TPLS:
    if not p.exists():
        print("⚠️ Template yok:", p.relative_to(ROOT))
        continue

    b = p.with_name(p.name + f".bak-lock-alarm-v85-{STAMP}")
    shutil.copy2(p, b)
    print("📦 Template yedeği:", b.relative_to(ROOT))

    t = p.read_text(encoding="utf-8", errors="ignore")

    # Eski ses uyarısı çağrıları varsa temizle.
    t = re.sub(
        r'\n?\s*<script src="{{ url_for\(\'static\', filename=\'continue/continue_voice_alert_v8[0-9]\.js\'\) }}\?v=[^"]+"></script>\s*',
        '\n',
        t
    )

    t = re.sub(
        r'\n?\s*<script src="{{ url_for\(\'static\', filename=\'continue/continue_native_lock_voice_v85\.js\'\) }}\?v=[^"]+"></script>\s*',
        '\n',
        t
    )

    if "continue_native_lock_alarm_v85.js" not in t:
        t = t.replace("</body>", SCRIPT + "\n</body>")
        print("✅ Native lock alarm script eklendi:", p.relative_to(ROOT))
    else:
        print("ℹ️ Native lock alarm script zaten var:", p.relative_to(ROOT))

    p.write_text(t, encoding="utf-8")

print()
print("✅ V85 tamam.")
