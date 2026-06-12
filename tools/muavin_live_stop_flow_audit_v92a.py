from pathlib import Path
import re

ROOT = Path(".").resolve()

FILES = [
    "static/continue/continue_trip_core.js",
    "android_app/app/src/main/python/static/continue/continue_trip_core.js",
    "static/continue/continue_native_lock_voice_v85.js",
    "android_app/app/src/main/python/static/continue/continue_native_lock_voice_v85.js",
    "templates/continue_trip.html",
    "android_app/app/src/main/python/templates/continue_trip.html",
    "android_app/app/src/main/java/com/muavinasistani/app/LiveStopAlertService.java",
    "android_app/app/src/main/java/com/muavinasistani/app/MainActivity.java",
]

print("===== V92A CANLI DURAK AKIŞ DENETİMİ =====")
print("ROOT:", ROOT)
print()

def read(p):
    path = ROOT / p
    if not path.exists():
        return None
    return path.read_text(encoding="utf-8", errors="ignore")

def show_hits(title, patterns, files):
    print()
    print("===== " + title + " =====")
    any_hit = False
    for f in files:
        s = read(f)
        if s is None:
            continue
        lines = s.splitlines()
        for i, line in enumerate(lines, 1):
            for pat in patterns:
                if re.search(pat, line, re.I):
                    print(f"{f}:{i}: {line[:220]}")
                    any_hit = True
                    break
    if not any_hit:
        print("⚠️ İz bulunamadı")

print("===== DOSYA VARLIK KONTROL =====")
for f in FILES:
    p = ROOT / f
    print(("✅" if p.exists() else "❌"), f)

show_hits(
    "1) CANLI DURAK ADI / DOM / BOOT",
    [
        r"liveCurrentStopName",
        r"live_stop",
        r"runtimeStop",
        r"currentStop",
        r"selectedStop",
        r"stopName"
    ],
    FILES
)

show_hits(
    "2) GPS DURAK DEĞİŞTİRME / KİLİT KORUMA",
    [
        r"MIDPOINT",
        r"LIVE_STOP_LOCK",
        r"preserve_live_stop",
        r"switchLiveStop",
        r"pickMidpoint",
        r"location\.reload",
        r"gps_km"
    ],
    FILES
)

show_hits(
    "3) SIRADAKİ DURAK / AKIŞ İLERLETME İZLERİ",
    [
        r"nextStop",
        r"next_stop",
        r"Sıradaki",
        r"siradaki",
        r"upcoming",
        r"passed",
        r"geçildi",
        r"complete",
        r"advance",
        r"durak.*geç"
    ],
    FILES
)

show_hits(
    "4) NATIVE SERVİSE GİDEN VERİ",
    [
        r"AndroidLockVoice",
        r"updateTarget",
        r"startLiveStop",
        r"target_lat",
        r"target_lng",
        r"display_km",
        r"offload_count",
        r"bag_count"
    ],
    FILES
)

show_hits(
    "5) SERVİS ALARM EŞİĞİ / DURAK HAFIZASI",
    [
        r"2\.05",
        r"alerted_2km",
        r"alertKey",
        r"onLocationChanged",
        r"updateForegroundMonitor",
        r"showAlarmNotification",
        r"startVibration",
        r"stopAlarmOnly"
    ],
    FILES
)

print()
print("===== ÖZET KARAR NOKTALARI =====")

core = read("static/continue/continue_trip_core.js") or ""
native = read("static/continue/continue_native_lock_voice_v85.js") or ""
service = read("android_app/app/src/main/java/com/muavinasistani/app/LiveStopAlertService.java") or ""

print("LIVE_STOP_LOCK var mı:", "EVET" if "LIVE_STOP_LOCK" in core else "HAYIR")
print("MIDPOINT switch return false var mı:", "EVET" if "LIVE_STOP_LOCK_V82_GUARD" in core or "return false" in core and "switchLiveStopMidpoint" in core else "BELİRSİZ")
print("Native AndroidLockVoice var mı:", "EVET" if "AndroidLockVoice" in native else "HAYIR")
print("Servis 2 km alarm hafızası var mı:", "EVET" if "alerted_2km" in service else "HAYIR")
print("Servis foreground monitor var mı:", "EVET" if "updateForegroundMonitor" in service else "HAYIR")

print()
print("✅ V92A rapor tamam. Çıktıyı gönder reis.")
