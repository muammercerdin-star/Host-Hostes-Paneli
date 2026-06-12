from pathlib import Path
import re
import hashlib

ROOT = Path(".").resolve()

print("===== V84 APK KİLİTLİ EKRAN SESLİ UYARI DENETİMİ =====")
print("ROOT:", ROOT)

paths = {
    "manifest": ROOT / "android_app/app/src/main/AndroidManifest.xml",
    "app_gradle": ROOT / "android_app/app/build.gradle",
    "project_gradle": ROOT / "android_app/build.gradle",
    "settings": ROOT / "android_app/settings.gradle",
}

print("\n===== 1) TEMEL DOSYALAR =====")
for name, p in paths.items():
    print(f"{name:14}:", "✅" if p.exists() else "❌", p.relative_to(ROOT) if p.exists() else p)

print("\n===== 2) ANDROID KAYNAK DOSYALARI =====")
src_root = ROOT / "android_app/app/src/main"
for ext in ("*.java", "*.kt", "*.xml"):
    files = list(src_root.rglob(ext)) if src_root.exists() else []
    if files:
        print(f"\n--- {ext} ({len(files)}) ---")
        for f in files[:80]:
            print(f.relative_to(ROOT))

print("\n===== 3) MANIFEST ÖZETİ =====")
manifest = paths["manifest"]
if manifest.exists():
    s = manifest.read_text(encoding="utf-8", errors="ignore")

    pkg = re.search(r'package="([^"]+)"', s)
    print("package:", pkg.group(1) if pkg else "manifest package yok / namespace gradle’da olabilir")

    print("\n--- izinler ---")
    for m in re.finditer(r'<uses-permission[^>]+android:name="([^"]+)"', s):
        print("PERMISSION:", m.group(1))

    print("\n--- activity/service/receiver/provider ---")
    for tag in ("activity", "service", "receiver", "provider"):
        for m in re.finditer(rf'<{tag}\b[\s\S]*?(?:/>|</{tag}>)', s):
            block = m.group(0)
            name = re.search(r'android:name="([^"]+)"', block)
            exported = re.search(r'android:exported="([^"]+)"', block)
            fgs_type = re.search(r'android:foregroundServiceType="([^"]+)"', block)
            print(f"{tag.upper()}:", name.group(1) if name else "?", 
                  "| exported:", exported.group(1) if exported else "-",
                  "| fgsType:", fgs_type.group(1) if fgs_type else "-")

    print("\n--- manifest içinde foreground/location izleri ---")
    for key in ["FOREGROUND_SERVICE", "FOREGROUND_SERVICE_LOCATION", "ACCESS_FINE_LOCATION", "ACCESS_COARSE_LOCATION", "POST_NOTIFICATIONS", "WAKE_LOCK"]:
        print(key, "=>", "✅ var" if key in s else "❌ yok")
else:
    print("❌ AndroidManifest.xml bulunamadı")

print("\n===== 4) GRADLE ÖZETİ =====")
for label in ("app_gradle", "project_gradle", "settings"):
    p = paths[label]
    print(f"\n--- {label} ---")
    if not p.exists():
        print("❌ yok")
        continue
    s = p.read_text(encoding="utf-8", errors="ignore")
    for pat in [
        r'namespace\s+[\'"]([^\'"]+)[\'"]',
        r'applicationId\s+[\'"]([^\'"]+)[\'"]',
        r'minSdk\s+(\d+)',
        r'targetSdk\s+(\d+)',
        r'compileSdk\s+(\d+)',
        r'com\.chaquo\.python',
        r'kotlin',
        r'java',
    ]:
        found = re.findall(pat, s, flags=re.I)
        if found:
            print(pat, "=>", found[:8])

print("\n===== 5) WEBVIEW / JS BRIDGE / GPS İZLERİ =====")
patterns = [
    "WebView", "addJavascriptInterface", "JavascriptInterface",
    "GeolocationPermissions", "onGeolocationPermissionsShowPrompt",
    "requestPermissions", "ACCESS_FINE_LOCATION", "TextToSpeech",
    "startForegroundService", "ForegroundService", "Service",
    "SharedPreferences", "getSharedPreferences"
]

code_files = []
for ext in ("*.java", "*.kt"):
    code_files.extend(src_root.rglob(ext) if src_root.exists() else [])

for f in code_files:
    txt = f.read_text(encoding="utf-8", errors="ignore")
    hits = [p for p in patterns if p in txt]
    if hits:
        print("\n---", f.relative_to(ROOT), "---")
        print("HITS:", ", ".join(hits))
        lines = txt.splitlines()
        for i, line in enumerate(lines, 1):
            if any(p in line for p in patterns):
                print(f"{i:4}: {line[:220]}")

print("\n===== 6) CONTINUE TEMPLATE / BOOT / API SES İÇİN GEREKEN VERİLER =====")
for p in [
    ROOT / "templates/continue_trip.html",
    ROOT / "android_app/app/src/main/python/templates/continue_trip.html",
    ROOT / "static/continue/continue_trip_core.js",
    ROOT / "android_app/app/src/main/python/static/continue/continue_trip_core.js",
    ROOT / "app.py",
    ROOT / "android_app/app/src/main/python/app.py",
]:
    if not p.exists():
        print("❌ yok:", p.relative_to(ROOT))
        continue
    txt = p.read_text(encoding="utf-8", errors="ignore")
    print("\n---", p.relative_to(ROOT), "---")
    for key in ["CONTINUE_BOOT", "routeCoords", "liveCurrentStopName", "liveDistanceValue", "liveOffloadCount", "live_runtime_state", "api/live-runtime-state", "api/live-stop-detail"]:
        print(f"{key:24}:", txt.count(key))

print("\n===== 7) APK SERVİS PLANINA UYGUNLUK =====")
print("Kontrol sonucu:")
print("- Manifest izinleri eksikse V85'te eklenecek.")
print("- MainActivity Java ise servis Java yazılacak; Kotlin ise Kotlin.")
print("- JS bridge varsa canlı durak/rota verisini native servise SharedPreferences ile aktaracağız.")
print("- JS bridge yoksa V85'te küçük AndroidBridge eklenecek.")
print("- Servis GPS + TTS ile kilitli ekranda konuşacak.")
print("- V82 kuralı korunacak: GPS canlı durak adını değiştirmeyecek.")

print("\n✅ V84 denetim bitti. Çıktıyı buraya gönder reis.")
