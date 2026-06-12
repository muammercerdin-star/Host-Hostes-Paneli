from pathlib import Path
from datetime import datetime
import shutil
import re
import sqlite3

ROOT = Path(".").resolve()
STAMP = datetime.now().strftime("%Y%m%d-%H%M%S")

JS_FILES = [
    ROOT / "static/continue/continue_trip_core.js",
    ROOT / "android_app/app/src/main/python/static/continue/continue_trip_core.js",
]

TPLS = [
    ROOT / "templates/continue_trip.html",
    ROOT / "android_app/app/src/main/python/templates/continue_trip.html",
]

print("===== V82 CANLI DURAK KİLİDİ =====")

for p in JS_FILES:
    if not p.exists():
        print("⚠️ Yok:", p.relative_to(ROOT))
        continue

    b = p.with_name(p.name + f".bak-live-stop-lock-v82-{STAMP}")
    shutil.copy2(p, b)
    print("📦 Yedek:", b.relative_to(ROOT))

    s = p.read_text(encoding="utf-8", errors="ignore")
    old = s

    # GPS midpoint motorunun canlı durak adını değiştiren hook'unu pasif yap.
    pattern = r'''      // MIDPOINT_LIVE_STOP_V67_HOOK
      const pickedLiveV67 = pickMidpointLiveStopV67\(liveName\);

      if\(pickedLiveV67\)\{
        const mustSwitchV67 =
          isEmptyLiveNameV67\(liveName\) \|\|
          norm\(pickedLiveV67\.name\) !== norm\(liveName \|\| ""\);

        if\(mustSwitchV67\)\{
          switchLiveStopMidpointV67\(liveName \|\| "", pickedLiveV67\);
          return;
        \}
      \}
'''

    repl = '''      // LIVE_STOP_LOCK_V82
      // GPS artık canlı durak SEÇMEZ.
      // Canlı durak sade koltuk modu / seçili durak / manuel işlem neyse o kalır.
      // GPS sadece mevcut canlı durağa kalan mesafe ve ETA hesaplar.
'''

    s = re.sub(pattern, repl, s)

    # Ek güvenlik: çağrı başka biçimde kaldıysa fonksiyonu da pasif bırak.
    s = re.sub(
        r'function switchLiveStopMidpointV67\(oldName, picked\)\{\n',
        'function switchLiveStopMidpointV67(oldName, picked){\n'
        '      // LIVE_STOP_LOCK_V82_GUARD\n'
        '      return false;\n',
        s,
        count=1
    )

    if s != old:
        p.write_text(s, encoding="utf-8")
        print("✅ GPS canlı durak değiştirme kapatıldı:", p.relative_to(ROOT))
    else:
        print("ℹ️ Değişiklik yapılmadı:", p.relative_to(ROOT))

print()
print("===== TEMPLATE CACHE V82 =====")

for p in TPLS:
    if not p.exists():
        print("⚠️ Yok:", p.relative_to(ROOT))
        continue

    b = p.with_name(p.name + f".bak-live-stop-lock-v82-cache-{STAMP}")
    shutil.copy2(p, b)

    s = p.read_text(encoding="utf-8", errors="ignore")
    s = re.sub(
        r"continue_trip_core\.js'\) }}\?v=[^\"']+",
        "continue_trip_core.js') }}?v=live-stop-lock-v82",
        s
    )
    p.write_text(s, encoding="utf-8")
    print("✅ Cache:", p.relative_to(ROOT))

print()
print("===== YANLIŞ RUNTIME DURAK KALINTILARINI TEMİZLE =====")

db_files = []
for ext in ("*.db", "*.sqlite", "*.sqlite3"):
    db_files.extend(ROOT.rglob(ext))

cleared = 0
for dbp in db_files:
    try:
        con = sqlite3.connect(str(dbp), timeout=2)
        cur = con.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='live_runtime_state'")
        if cur.fetchone():
            con.execute("DELETE FROM live_runtime_state")
            con.commit()
            cleared += 1
            print("✅ Temizlendi:", dbp.relative_to(ROOT))
        con.close()
    except Exception as e:
        print("⚠️ Atlandı:", dbp.relative_to(ROOT), "-", e)

if cleared == 0:
    print("ℹ️ live_runtime_state tablosu bulunan db temizlenmedi / bulunamadı.")

print()
print("✅ V82 tamam. Canlı durak GPS ile değişmeyecek.")
