from pathlib import Path
from datetime import datetime
import shutil
import re

ROOT = Path(".").resolve()
STAMP = datetime.now().strftime("%Y%m%d-%H%M%S")

MAIN = ROOT / "android_app/app/src/main/java/com/muavinasistani/app/MainActivity.java"
MANIFEST = ROOT / "android_app/app/src/main/AndroidManifest.xml"

JS_FILES = [
    ROOT / "static/continue/continue_native_lock_alarm_v85.js",
    ROOT / "android_app/app/src/main/python/static/continue/continue_native_lock_alarm_v85.js",
]

TPLS = [
    ROOT / "templates/continue_trip.html",
    ROOT / "android_app/app/src/main/python/templates/continue_trip.html",
]

print("===== V86 BİLDİRİM İZNİ + KANAL GARANTİ FIX =====")

if not MAIN.exists():
    raise SystemExit("❌ MainActivity.java yok")

b = MAIN.with_name(MAIN.name + f".bak-notification-v86-{STAMP}")
shutil.copy2(MAIN, b)
print("📦 MainActivity yedeği:", b.relative_to(ROOT))

s = MAIN.read_text(encoding="utf-8", errors="ignore")

# 1) onCreate içinde bildirim kanalını requestBasicPermissions öncesi oluştur.
if "createLockAlarmChannelsV86();" not in s:
    s = s.replace(
        "        requestBasicPermissions();",
        "        createLockAlarmChannelsV86();\n"
        "        requestBasicPermissions();\n"
        "        requestNotificationPermissionV86();"
    )
    print("✅ onCreate içine kanal + bildirim izni çağrısı eklendi")
else:
    print("ℹ️ onCreate V86 çağrıları zaten var")

# 2) requestBasicPermissions metodunu sadeleştir: ilk açılışta kamera/mikrofon istemesin.
NEW_PERM = r'''    private void requestBasicPermissions() {
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

s2 = re.sub(
    r'    private void requestBasicPermissions\(\) \{[\s\S]*?\n    \}\n\n\n    @Override\n    protected void onDestroy',
    NEW_PERM + "\n\n\n    @Override\n    protected void onDestroy",
    s,
    count=1
)

if s2 != s:
    s = s2
    print("✅ requestBasicPermissions sadeleştirildi + notification V86 metodları eklendi")
else:
    print("⚠️ requestBasicPermissions otomatik değişmedi")

MAIN.write_text(s, encoding="utf-8")

# 3) Manifestte izinler garanti olsun.
if MANIFEST.exists():
    mb = MANIFEST.with_name(MANIFEST.name + f".bak-notification-v86-{STAMP}")
    shutil.copy2(MANIFEST, mb)

    m = MANIFEST.read_text(encoding="utf-8", errors="ignore")
    for perm in [
        "android.permission.POST_NOTIFICATIONS",
        "android.permission.FOREGROUND_SERVICE",
        "android.permission.FOREGROUND_SERVICE_LOCATION",
        "android.permission.VIBRATE",
        "android.permission.WAKE_LOCK",
    ]:
        if perm not in m:
            m = m.replace("    <application", f'    <uses-permission android:name="{perm}" />\n\n    <application')
            print("✅ Manifest izin eklendi:", perm)

    MANIFEST.write_text(m, encoding="utf-8")

# 4) JS fallback: koordinat bulunmasa bile Android servisi başlasın.
JS_CODE = r'''/* CONTINUE_NATIVE_LOCK_ALARM_V86
   WebView -> Android kilit ekranı alarm servisi.
   V82 kuralı: canlı durak GPS ile değişmez.
   V86: Koordinat eşleşmese bile takip bildirimi başlatılır.
*/
(function(){
  if(window.CONTINUE_NATIVE_LOCK_ALARM_V86_READY) return;
  window.CONTINUE_NATIVE_LOCK_ALARM_V86_READY = true;

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
      const name = clean(item.stop || item.name || item.title || item.durak || "");
      if(norm(name) !== key) continue;

      const lat = Number(item.lat ?? item.latitude ?? item.enlem);
      const lng = Number(item.lng ?? item.lon ?? item.longitude ?? item.boylam);

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

      const off = offloadCount();
      const bag = bagCount();
      const c = findCoord(stop);

      const sig = [tripId, stop, c ? c.lat : "NO_LAT", c ? c.lng : "NO_LNG", off, bag].join("|");

      if(sig !== lastSig){
        lastSig = sig;

        window.AndroidLockAlarm.updateTarget(
          tripId,
          stop,
          c ? String(c.lat) : "",
          c ? String(c.lng) : "",
          String(off),
          String(bag)
        );
      }

      // V86: Koordinat yoksa bile servis başlasın, bildirim kanalı canlansın.
      if(!started){
        started = true;
        window.AndroidLockAlarm.start();
      }

    }catch(err){
      console.warn("CONTINUE_NATIVE_LOCK_ALARM_V86 sync error", err);
    }
  }

  window.continueNativeLockAlarmV86 = {
    sync,
    stopAlarm(){
      try{ if(window.AndroidLockAlarm) window.AndroidLockAlarm.stopAlarm(); }catch(_){}
    },
    stopService(){
      try{ if(window.AndroidLockAlarm) window.AndroidLockAlarm.stopService(); }catch(_){}
    },
    reset(){
      try{ if(window.AndroidLockAlarm) window.AndroidLockAlarm.reset(); }catch(_){}
    }
  };

  if(document.readyState === "loading"){
    document.addEventListener("DOMContentLoaded", sync);
  }else{
    sync();
  }

  setTimeout(sync, 800);
  setTimeout(sync, 2000);
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

for p in JS_FILES:
    if p.exists():
        jb = p.with_name(p.name + f".bak-v86-{STAMP}")
        shutil.copy2(p, jb)
        p.write_text(JS_CODE, encoding="utf-8")
        print("✅ JS V86 yazıldı:", p.relative_to(ROOT))
    else:
        print("⚠️ JS yok:", p.relative_to(ROOT))

# 5) Cache parametresi V86.
for p in TPLS:
    if p.exists():
        tb = p.with_name(p.name + f".bak-v86-{STAMP}")
        shutil.copy2(p, tb)
        t = p.read_text(encoding="utf-8", errors="ignore")
        t = t.replace("?v=native-lock-alarm-v85", "?v=native-lock-alarm-v86")
        p.write_text(t, encoding="utf-8")
        print("✅ Template V86 cache:", p.relative_to(ROOT))

print()
print("===== KONTROL =====")
for p in [MAIN] + JS_FILES + TPLS:
    if not p.exists():
        continue
    txt = p.read_text(encoding="utf-8", errors="ignore")
    for i, line in enumerate(txt.splitlines(), 1):
        if any(k in line for k in [
            "createLockAlarmChannelsV86",
            "requestNotificationPermissionV86",
            "POST_NOTIFICATIONS",
            "CONTINUE_NATIVE_LOCK_ALARM_V86",
            "native-lock-alarm-v86"
        ]):
            print(f"{p.relative_to(ROOT)}:{i}: {line}")

print()
print("✅ V86 native notification fix tamam.")
