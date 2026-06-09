from pathlib import Path
from datetime import datetime
import shutil
import re

ROOT = Path(".").resolve()
STAMP = datetime.now().strftime("%Y%m%d-%H%M%S")

FILES = [
    ROOT / "static/continue/continue_trip_core.js",
    ROOT / "android_app/app/src/main/python/static/continue/continue_trip_core.js",
]

TPLS = [
    ROOT / "templates/continue_trip.html",
    ROOT / "android_app/app/src/main/python/templates/continue_trip.html",
]

def backup(p):
    if p.exists():
        b = p.with_name(p.name + f".bak-live-switch-distance-v65-{STAMP}")
        shutil.copy2(p, b)
        print("📦 Yedek:", b.relative_to(ROOT))

print("===== LIVE SWITCH DISTANCE FIX V65 =====")

for p in FILES:
    if not p.exists():
        print("⚠️ Yok:", p.relative_to(ROOT))
        continue

    backup(p)
    s = p.read_text(encoding="utf-8", errors="ignore")
    old = s

    if "LIVE_SWITCH_DISTANCE_FIX_V65" in s:
        print("ℹ️ V65 zaten var:", p.relative_to(ROOT))
        continue

    marker = '      const displaySpeed = liveDisplaySpeed();'
    insert = '''      const displaySpeed = liveDisplaySpeed();

      // LIVE_SWITCH_DISTANCE_FIX_V65
      // Canlı durak aktarılırken yeni durağın mesafesini boş yazma.
      // GPS konumu ve rota koordinatı varsa mesafeyi hemen hesapla.
      let newGpsKm = "";
      try{
        const newCoord = findCoord(toName);
        if(lastPos && newCoord){
          const newKm = distKm(lastPos, newCoord);
          if(Number.isFinite(newKm)){
            newGpsKm = formatKm(newKm);
          }
        }
      }catch(_){}'''

    if marker in s:
        s = s.replace(marker, insert, 1)
        print("✅ Yeni canlı durak mesafe hesabı eklendi:", p.relative_to(ROOT))
    else:
        print("❌ displaySpeed marker bulunamadı:", p.relative_to(ROOT))
        continue

    s = s.replace(
        '`&gps_km=` +',
        '`&gps_km=${encodeURIComponent(newGpsKm || "")}` +',
        1
    )

    s = s.replace(
        'if(distEl) distEl.textContent = "yakalanıyor";',
        'if(distEl) distEl.textContent = newGpsKm || "yakalanıyor";',
        1
    )

    if s != old:
        p.write_text(s, encoding="utf-8")
        print("✅ V65 uygulandı:", p.relative_to(ROOT))
    else:
        print("⚠️ Değişiklik olmadı:", p.relative_to(ROOT))

for p in TPLS:
    if not p.exists():
        print("⚠️ Yok:", p.relative_to(ROOT))
        continue

    backup(p)
    s = p.read_text(encoding="utf-8", errors="ignore")
    old = s

    s = re.sub(
        r"continue_trip_core\.js'\) }}\?v=[^\"']+",
        "continue_trip_core.js') }}?v=live-switch-distance-v65",
        s
    )
    s = re.sub(
        r'continue_trip_core\.js"\) }}\?v=[^"\']+',
        'continue_trip_core.js") }}?v=live-switch-distance-v65',
        s
    )

    if s != old:
        p.write_text(s, encoding="utf-8")
        print("✅ Cache kırıldı:", p.relative_to(ROOT))

print()
print("✅ V65 tamam. Yeni canlı durağa geçerken mesafe artık boş yazılmayacak.")
