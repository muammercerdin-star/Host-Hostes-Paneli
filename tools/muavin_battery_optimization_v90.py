from pathlib import Path
from datetime import datetime
import shutil

ROOT = Path(".").resolve()
STAMP = datetime.now().strftime("%Y%m%d-%H%M%S")

SERVICE = ROOT / "android_app/app/src/main/java/com/muavinasistani/app/LiveStopAlertService.java"

print("===== V90 PİL OPTİMİZASYONU / AKILLI GPS =====")

if not SERVICE.exists():
    raise SystemExit("❌ LiveStopAlertService.java yok")

b = SERVICE.with_name(SERVICE.name + f".bak-v90-battery-{STAMP}")
shutil.copy2(SERVICE, b)
print("📦 Service yedeği:", b.relative_to(ROOT))

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

    private static final String CHANNEL_MONITOR = "muavin_live_monitor_v90";
    private static final String CHANNEL_ALERT = "muavin_live_alert_v90";

    private static final int MONITOR_NOTIFICATION_ID = 9001;
    private static final int ALERT_NOTIFICATION_ID = 9002;

    private static final String PREF = "muavin_lock_alarm_v85";

    private static final int MODE_NONE = 0;
    private static final int MODE_FAR = 1;        // 15 km üstü
    private static final int MODE_MID = 2;        // 5-15 km
    private static final int MODE_NEAR = 3;       // 2.2-5 km
    private static final int MODE_ALERT = 4;      // 2.2 km altı
    private static final int MODE_AFTER_ALERT = 5;

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
    private String displayKm = "";

    private int currentMode = MODE_NONE;
    private long lastMonitorUpdateMs = 0;
    private double lastMonitorKm = -999;
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
            updateForegroundMonitor(true);
            return START_STICKY;
        }

        loadTargetFromPrefs();
        updateForegroundMonitor(true);
        applyLocationMode(MODE_FAR);
        checkLastKnownLocation();

        return START_STICKY;
    }

    private void loadTargetFromPrefs() {
        tripId = prefs.getString("trip_id", "active");
        stopName = prefs.getString("stop_name", "");
        displayKm = prefs.getString("display_km", "");

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

    private String stopTitle() {
        return stopName != null && stopName.trim().length() > 0 ? stopName.trim() : "Canlı durak";
    }

    private String kmText() {
        if (displayKm != null && displayKm.trim().length() > 0) {
            String x = displayKm.trim();
            return x.toLowerCase(new Locale("tr", "TR")).contains("km") ? x : x + " km";
        }
        return "mesafe hesaplanıyor";
    }

    private String passengerText() {
        return offloadCount > 0 ? offloadCount + " yolcu inecek" : "İnecek yolcu yok";
    }

    private String bagText() {
        return bagCount > 0 ? bagCount + " bagaj var" : "0 bagaj";
    }

    private String batteryModeText() {
        if (currentMode == MODE_FAR) return "pil koruma";
        if (currentMode == MODE_MID) return "normal takip";
        if (currentMode == MODE_NEAR) return "yakın takip";
        if (currentMode == MODE_ALERT) return "alarm bölgesi";
        if (currentMode == MODE_AFTER_ALERT) return "alarm sonrası";
        return "takip";
    }

    private String monitorBody() {
        return stopTitle() + " • " + kmText() + " • " + passengerText() + " • " + bagText();
    }

    private String monitorBigText() {
        return "CANLI DURAK\n"
                + stopTitle()
                + "\nKalan mesafe: " + kmText()
                + "\n" + passengerText() + " • " + bagText()
                + "\nMod: " + batteryModeText();
    }

    private void updateForegroundMonitor(boolean force) {
        long now = System.currentTimeMillis();

        long minGap = 30000;
        if (currentMode == MODE_NEAR || currentMode == MODE_ALERT) minGap = 10000;
        if (currentMode == MODE_AFTER_ALERT) minGap = 30000;

        if (!force && now - lastMonitorUpdateMs < minGap) return;

        lastMonitorUpdateMs = now;
        startForegroundSafe(buildMonitorNotification());
    }

    private void maybeUpdateMonitorByKm(double km) {
        long now = System.currentTimeMillis();

        double diff = Math.abs(km - lastMonitorKm);
        long minGap = 30000;

        if (km <= 5.0) minGap = 10000;
        if (km <= 2.2) minGap = 7000;

        if (lastMonitorKm < -900 || diff >= 0.10 || now - lastMonitorUpdateMs >= minGap) {
            lastMonitorKm = km;
            updateForegroundMonitor(true);
        }
    }

    private Notification buildMonitorNotification() {
        Intent openIntent = new Intent(this, MainActivity.class);
        openIntent.setFlags(Intent.FLAG_ACTIVITY_SINGLE_TOP | Intent.FLAG_ACTIVITY_CLEAR_TOP);

        int piFlags = PendingIntent.FLAG_UPDATE_CURRENT;
        if (Build.VERSION.SDK_INT >= 23) piFlags |= PendingIntent.FLAG_IMMUTABLE;

        PendingIntent openPi = PendingIntent.getActivity(this, 10, openIntent, piFlags);

        Intent stopServiceIntent = new Intent(this, LiveStopAlertService.class);
        stopServiceIntent.setAction(ACTION_STOP_SERVICE);
        PendingIntent stopServicePi = PendingIntent.getService(this, 12, stopServiceIntent, piFlags);

        Notification.Builder b = new Notification.Builder(this, CHANNEL_MONITOR)
                .setSmallIcon(android.R.drawable.ic_dialog_map)
                .setContentTitle("Muavin Asistanı canlı takip")
                .setContentText(monitorBody())
                .setStyle(new Notification.BigTextStyle().bigText(monitorBigText()))
                .setContentIntent(openPi)
                .setOngoing(true)
                .setOnlyAlertOnce(true)
                .setShowWhen(true)
                .setVisibility(Notification.VISIBILITY_PUBLIC)
                .setCategory(Notification.CATEGORY_NAVIGATION)
                .addAction(android.R.drawable.ic_menu_close_clear_cancel, "Takibi kapat", stopServicePi);

        b.setPriority(Notification.PRIORITY_DEFAULT);

        return b.build();
    }

    private Notification buildAlertNotification(String message) {
        Intent openIntent = new Intent(this, MainActivity.class);
        openIntent.setFlags(Intent.FLAG_ACTIVITY_SINGLE_TOP | Intent.FLAG_ACTIVITY_CLEAR_TOP);

        int piFlags = PendingIntent.FLAG_UPDATE_CURRENT;
        if (Build.VERSION.SDK_INT >= 23) piFlags |= PendingIntent.FLAG_IMMUTABLE;

        PendingIntent openPi = PendingIntent.getActivity(this, 20, openIntent, piFlags);

        Intent stopAlarmIntent = new Intent(this, LiveStopAlertService.class);
        stopAlarmIntent.setAction(ACTION_STOP_ALARM);
        PendingIntent stopAlarmPi = PendingIntent.getService(this, 21, stopAlarmIntent, piFlags);

        String big = "CANLI DURAK ALARMI\n" + stopTitle() + "\n" + message;

        Notification.Builder b = new Notification.Builder(this, CHANNEL_ALERT)
                .setSmallIcon(android.R.drawable.ic_dialog_map)
                .setContentTitle("Canlı durak alarmı")
                .setContentText(message)
                .setStyle(new Notification.BigTextStyle().bigText(big))
                .setContentIntent(openPi)
                .setOngoing(true)
                .setOnlyAlertOnce(false)
                .setShowWhen(true)
                .setVisibility(Notification.VISIBILITY_PUBLIC)
                .setCategory(Notification.CATEGORY_ALARM)
                .addAction(android.R.drawable.ic_media_pause, "Alarmı durdur", stopAlarmPi)
                .addAction(android.R.drawable.ic_menu_view, "Uygulamayı aç", openPi);

        b.setPriority(Notification.PRIORITY_MAX);

        return b.build();
    }

    private void showAlarmNotification(String message) {
        alarmActive = true;
        startVibration();

        try {
            NotificationManager nm = (NotificationManager) getSystemService(NOTIFICATION_SERVICE);
            if (nm != null) {
                nm.notify(ALERT_NOTIFICATION_ID, buildAlertNotification(message));
            }
        } catch (Exception ignored) {}

        launchLockAlarmActivityIfAvailable();
        applyLocationMode(MODE_AFTER_ALERT);
    }

    private void launchLockAlarmActivityIfAvailable() {
        try {
            Intent i = new Intent();
            i.setClassName(getPackageName(), getPackageName() + ".LockAlarmActivity");
            i.setFlags(Intent.FLAG_ACTIVITY_NEW_TASK | Intent.FLAG_ACTIVITY_CLEAR_TOP | Intent.FLAG_ACTIVITY_SINGLE_TOP);
            startActivity(i);
        } catch (Exception ignored) {}
    }

    private void startForegroundSafe(Notification notification) {
        try {
            if (Build.VERSION.SDK_INT >= 29) {
                startForeground(
                        MONITOR_NOTIFICATION_ID,
                        notification,
                        ServiceInfo.FOREGROUND_SERVICE_TYPE_LOCATION
                );
            } else {
                startForeground(MONITOR_NOTIFICATION_ID, notification);
            }
        } catch (Exception e) {
            try {
                startForeground(MONITOR_NOTIFICATION_ID, notification);
            } catch (Exception ignored) {}
        }
    }

    private void createChannels() {
        if (Build.VERSION.SDK_INT < 26) return;

        NotificationManager nm = (NotificationManager) getSystemService(NOTIFICATION_SERVICE);
        if (nm == null) return;

        NotificationChannel monitor = new NotificationChannel(
                CHANNEL_MONITOR,
                "Canlı durak pil korumalı takip",
                NotificationManager.IMPORTANCE_DEFAULT
        );
        monitor.setDescription("Canlı durak, kalan mesafe, yolcu ve bagaj kartı");
        monitor.setLockscreenVisibility(Notification.VISIBILITY_PUBLIC);

        NotificationChannel alert = new NotificationChannel(
                CHANNEL_ALERT,
                "Canlı durak alarmı V90",
                NotificationManager.IMPORTANCE_HIGH
        );
        alert.setDescription("2 km kala sesli ve titreşimli uyarı");
        alert.enableVibration(true);
        alert.setVibrationPattern(new long[]{0, 700, 300, 700, 300, 1000});
        alert.setLockscreenVisibility(Notification.VISIBILITY_PUBLIC);

        nm.createNotificationChannel(monitor);
        nm.createNotificationChannel(alert);
    }

    private boolean hasLocationPermission() {
        return checkSelfPermission(Manifest.permission.ACCESS_FINE_LOCATION) == PackageManager.PERMISSION_GRANTED
                || checkSelfPermission(Manifest.permission.ACCESS_COARSE_LOCATION) == PackageManager.PERMISSION_GRANTED;
    }

    private int modeForKm(double km) {
        if (alarmActive) return MODE_AFTER_ALERT;
        if (km <= 2.20) return MODE_ALERT;
        if (km <= 5.00) return MODE_NEAR;
        if (km <= 15.00) return MODE_MID;
        return MODE_FAR;
    }

    private void applyLocationMode(int newMode) {
        if (newMode == currentMode && newMode != MODE_NONE) return;
        if (!hasLocationPermission()) return;
        if (locationManager == null) return;

        currentMode = newMode;

        try {
            locationManager.removeUpdates(this);
        } catch (Exception ignored) {}

        long gpsMs = 60000;
        float gpsM = 150f;
        long netMs = 45000;
        float netM = 150f;

        if (newMode == MODE_FAR) {
            gpsMs = 60000;
            gpsM = 150f;
            netMs = 45000;
            netM = 150f;
        } else if (newMode == MODE_MID) {
            gpsMs = 30000;
            gpsM = 70f;
            netMs = 30000;
            netM = 70f;
        } else if (newMode == MODE_NEAR) {
            gpsMs = 10000;
            gpsM = 25f;
            netMs = 15000;
            netM = 40f;
        } else if (newMode == MODE_ALERT) {
            gpsMs = 5000;
            gpsM = 10f;
            netMs = 7000;
            netM = 20f;
        } else if (newMode == MODE_AFTER_ALERT) {
            gpsMs = 30000;
            gpsM = 80f;
            netMs = 30000;
            netM = 80f;
        }

        try {
            locationManager.requestLocationUpdates(LocationManager.NETWORK_PROVIDER, netMs, netM, this);
        } catch (Exception ignored) {}

        try {
            locationManager.requestLocationUpdates(LocationManager.GPS_PROVIDER, gpsMs, gpsM, this);
        } catch (Exception ignored) {}

        updateForegroundMonitor(true);
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

        if (!validCoord()) {
            updateForegroundMonitor(false);
            return;
        }

        float[] result = new float[1];
        Location.distanceBetween(
                location.getLatitude(),
                location.getLongitude(),
                targetLat,
                targetLng,
                result
        );

        double km = result[0] / 1000.0;
        displayKm = formatKm(km);

        try {
            prefs.edit().putString("display_km", displayKm).apply();
        } catch (Exception ignored) {}

        applyLocationMode(modeForKm(km));
        maybeUpdateMonitorByKm(km);

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

    private String formatKm(double km) {
        try {
            return String.format(new Locale("tr", "TR"), "%.2f km", km);
        } catch (Exception e) {
            return "";
        }
    }

    private String buildSpeechMessage() {
        if (offloadCount > 0) {
            return stopTitle() + " durağına 2 kilometre kaldı. " + offloadCount + " yolcu inecek.";
        }
        return stopTitle() + " durağına 2 kilometre kaldı. İnecek yolcu yok.";
    }

    private String buildLockMessage() {
        String bag = bagCount > 0 ? bagCount + " bagaj var" : "Bagaj yok";
        return stopTitle() + " • 2 km kaldı • " + passengerText() + " • " + bag;
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
            tts.speak(msg, TextToSpeech.QUEUE_FLUSH, null, "muavin_lock_alarm_v90");
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

        try {
            NotificationManager nm = (NotificationManager) getSystemService(NOTIFICATION_SERVICE);
            if (nm != null) nm.cancel(ALERT_NOTIFICATION_ID);
        } catch (Exception ignored) {}

        applyLocationMode(MODE_AFTER_ALERT);
        updateForegroundMonitor(true);
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

        try {
            NotificationManager nm = (NotificationManager) getSystemService(NOTIFICATION_SERVICE);
            if (nm != null) {
                nm.cancel(MONITOR_NOTIFICATION_ID);
                nm.cancel(ALERT_NOTIFICATION_ID);
            }
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

SERVICE.write_text(SERVICE_CODE, encoding="utf-8")

print("✅ LiveStopAlertService V90 pil optimizasyonlu yazıldı")

print()
print("===== KONTROL =====")
txt = SERVICE.read_text(encoding="utf-8", errors="ignore")
for i, line in enumerate(txt.splitlines(), 1):
    if any(k in line for k in [
        "MODE_FAR",
        "MODE_MID",
        "MODE_NEAR",
        "MODE_ALERT",
        "MODE_AFTER_ALERT",
        "applyLocationMode",
        "gpsMs",
        "netMs",
        "maybeUpdateMonitorByKm",
        "muavin_live_monitor_v90",
        "muavin_live_alert_v90"
    ]):
        print(f"{i}: {line}")

print()
print("✅ V90 tamam.")
