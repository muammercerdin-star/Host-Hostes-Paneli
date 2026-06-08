from pathlib import Path
from datetime import datetime
import shutil
import re

ROOT = Path(".").resolve()
STAMP = datetime.now().strftime("%Y%m%d-%H%M%S")

TEMPLATE_FILES = [
    ROOT / "templates/continue_trip.html",
    ROOT / "android_app/app/src/main/python/templates/continue_trip.html",
]

CORE_FILES = [
    ROOT / "static/continue/continue_trip_core.js",
    ROOT / "android_app/app/src/main/python/static/continue/continue_trip_core.js",
]

CSS_MAIN_FILES = [
    ROOT / "static/continue/continue_trip.css",
    ROOT / "android_app/app/src/main/python/static/continue/continue_trip.css",
]

CSS_PART_FILES = [
    ROOT / "static/continue/css_parts/70-seat-map-sheet-v44.css",
    ROOT / "android_app/app/src/main/python/static/continue/css_parts/70-seat-map-sheet-v44.css",
]

def backup(p: Path):
    if p.exists():
        b = p.with_name(p.name + f".bak-seatmap-minimal-v44-{STAMP}")
        shutil.copy2(p, b)
        print("📦 Yedek:", b.relative_to(ROOT))

print("===== CONTINUE SEAT MAP MINIMAL V44 =====")

# 1) template cache version güncelle
for p in TEMPLATE_FILES:
    if not p.exists():
        print("⚠️ Yok:", p.relative_to(ROOT))
        continue
    backup(p)
    s = p.read_text(encoding="utf-8", errors="ignore")
    old = s

    s = s.replace("seat-map-v43", "seat-map-v44")
    s = s.replace("core-split-1", "seat-map-v44")

    p.write_text(s, encoding="utf-8")
    print("✅ Template güncellendi:" if s != old else "ℹ️ Değişiklik yok:", p.relative_to(ROOT))

# 2) CSS dosyası yaz
css_text = r'''
/* CONTINUE_SEAT_MAP_MINIMAL_V44 */
#continueSeatMapFullscreen{
  position: fixed;
  inset: 0;
  z-index: 999999;
}
#continueSeatMapFullscreen .csm-backdrop{
  position: absolute;
  inset: 0;
  background: rgba(2,8,24,.78);
  backdrop-filter: blur(10px);
}
#continueSeatMapFullscreen .csm-panel{
  position: absolute;
  inset: 0;
  background:
    radial-gradient(circle at top, rgba(28,63,132,.22), transparent 32%),
    linear-gradient(180deg, #081327 0%, #07101f 100%);
  padding: 14px;
  display: flex;
  flex-direction: column;
}
#continueSeatMapFullscreen .csm-close{
  position: absolute;
  top: 14px;
  right: 14px;
  width: 52px;
  height: 52px;
  border-radius: 16px;
  border: 1px solid rgba(255,255,255,.16);
  background: rgba(255,255,255,.08);
  color: #fff;
  font-size: 30px;
  line-height: 1;
  z-index: 3;
}
#continueSeatMapFullscreen .csm-onlywrap{
  flex: 1;
  min-height: 0;
  display: flex;
  padding-top: 56px;
}
#continueSeatMapFullscreen .csm-deck{
  width: 100%;
  height: 100%;
  overflow: auto;
  border-radius: 24px;
  padding: 18px 14px 24px;
  background: linear-gradient(180deg, rgba(38,72,138,.18), rgba(10,21,45,.78));
  border: 1px solid rgba(255,255,255,.08);
  box-shadow: inset 0 1px 0 rgba(255,255,255,.06);
  display: grid;
  grid-template-columns: repeat(4, minmax(0, 1fr));
  gap: 12px;
  align-content: start;
}
#continueSeatMapFullscreen .csm-seat{
  min-height: 88px;
  border-radius: 18px;
  border: 1px solid rgba(255,255,255,.10);
  background: rgba(255,255,255,.05);
  color: #fff;
  padding: 8px 6px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  text-align: center;
}
#continueSeatMapFullscreen .csm-seat b{
  font-size: 18px;
  line-height: 1.1;
  margin-bottom: 6px;
}
#continueSeatMapFullscreen .csm-seat small{
  font-size: 11px;
  line-height: 1.15;
  opacity: .88;
}
#continueSeatMapFullscreen .csm-seat.empty{
  background: rgba(255,255,255,.04);
  color: rgba(255,255,255,.78);
}
#continueSeatMapFullscreen .csm-seat.occupied{
  background: rgba(54,95,180,.18);
}
#continueSeatMapFullscreen .csm-seat.highlight{
  border-color: rgba(255,198,64,.55);
  box-shadow: 0 0 0 1px rgba(255,198,64,.24), inset 0 0 0 1px rgba(255,198,64,.12);
  background: rgba(255,198,64,.12);
}
'''

for p in CSS_PART_FILES:
    p.parent.mkdir(parents=True, exist_ok=True)
    backup(p) if p.exists() else None
    p.write_text(css_text.strip() + "\n", encoding="utf-8")
    print("✅ CSS yazıldı:", p.relative_to(ROOT))

# 3) ana css import ekle
for p in CSS_MAIN_FILES:
    if not p.exists():
        print("⚠️ Yok:", p.relative_to(ROOT))
        continue
    backup(p)
    s = p.read_text(encoding="utf-8", errors="ignore")
    old = s

    line = '@import url("./css_parts/70-seat-map-sheet-v44.css");'
    if line not in s:
        s = s.rstrip() + "\n" + line + "\n"

    p.write_text(s, encoding="utf-8")
    print("✅ CSS import eklendi:" if s != old else "ℹ️ CSS import zaten vardı:", p.relative_to(ROOT))

# 4) core js içindeki seat map bloğunu minimal hale getir
new_block = r'''
/* ===== CONTINUE_SEAT_MAP_MINIMAL_V44_START ===== */
(function(){
  const btn = document.getElementById("continueSeatMapBtn");
  if(!btn) return;

  function esc(v){
    return String(v == null ? "" : v)
      .replaceAll("&","&amp;")
      .replaceAll("<","&lt;")
      .replaceAll(">","&gt;")
      .replaceAll('"',"&quot;")
      .replaceAll("'","&#039;");
  }

  function norm(v){
    return String(v || "")
      .toLowerCase()
      .replace(/[–\-_\/\\\.,()\[\]]/g, " ")
      .replace(/\s+/g, " ")
      .trim();
  }

  function currentStop(){
    const el = document.getElementById("liveCurrentStopName");
    return (el && el.textContent ? el.textContent : "").trim();
  }

  function closeSeatMap(){
    document.getElementById("continueSeatMapFullscreen")?.remove();
    document.body.style.overflow = "";
  }

  function seatCard(seat){
    const seatNo = seat.seat_no || seat.no || seat.number || "";
    const fromStop = seat.from_stop || "";
    const toStop = seat.to_stop || seat.stop || "";
    const occupied = !!(seat.occupied || seat.full || toStop || fromStop || seat.passenger_name);
    const cls = occupied ? "occupied" : "empty";
    const hi = toStop && currentStop() && norm(toStop) === norm(currentStop()) ? "highlight" : "";
    const label = occupied ? (toStop || fromStop || "Dolu") : "Boş";

    return `
      <div class="csm-seat ${cls} ${hi}">
        <b>${esc(seatNo)}</b>
        <small>${esc(label)}</small>
      </div>
    `;
  }

  function renderSheet(data){
    closeSeatMap();

    const seats = Array.isArray(data?.seats) ? data.seats : [];

    const host = document.createElement("div");
    host.id = "continueSeatMapFullscreen";
    host.innerHTML = `
      <div class="csm-backdrop"></div>
      <div class="csm-panel">
        <button class="csm-close" type="button" aria-label="Kapat">×</button>
        <div class="csm-onlywrap">
          <div class="csm-deck">
            ${seats.map(seatCard).join("") || '<div class="csm-seat empty"><b>—</b><small>Koltuk verisi yok</small></div>'}
          </div>
        </div>
      </div>
    `;

    document.body.appendChild(host);
    document.body.style.overflow = "hidden";

    host.querySelector(".csm-close")?.addEventListener("click", closeSeatMap);
    host.querySelector(".csm-backdrop")?.addEventListener("click", closeSeatMap);
  }

  async function openSeatMap(e){
    e.preventDefault();

    try{
      const stop = currentStop();
      const res = await fetch(`/api/live-seat-map?stop=${encodeURIComponent(stop)}&_=${Date.now()}`, {
        method: "GET",
        credentials: "same-origin",
        cache: "no-store"
      });
      const j = await res.json();
      if(!j || !j.ok) throw new Error((j && (j.error || j.msg)) || "Koltuk planı alınamadı");
      renderSheet(j);
    }catch(err){
      console.error("continue seat map minimal v44 error", err);
      alert("Koltuk planı açılamadı.");
    }
  }

  btn.addEventListener("click", openSeatMap);

  document.addEventListener("keydown", function(e){
    if(e.key === "Escape"){
      closeSeatMap();
    }
  });
})();
/* ===== CONTINUE_SEAT_MAP_MINIMAL_V44_END ===== */
'''

patterns = [
    r'/\* ===== CONTINUE_SEAT_MAP_SHEET_V43_START ===== \*/.*?/\* ===== CONTINUE_SEAT_MAP_SHEET_V43_END ===== \*/',
    r'/\* ===== CONTINUE_SEAT_MAP_MINIMAL_V44_START ===== \*/.*?/\* ===== CONTINUE_SEAT_MAP_MINIMAL_V44_END ===== \*/',
]

for p in CORE_FILES:
    if not p.exists():
        print("⚠️ Yok:", p.relative_to(ROOT))
        continue
    backup(p)
    s = p.read_text(encoding="utf-8", errors="ignore")
    old = s

    replaced = False
    for pat in patterns:
        if re.search(pat, s, flags=re.S):
            s = re.sub(pat, new_block, s, flags=re.S)
            replaced = True
            break

    if not replaced:
        s = s.rstrip() + "\n\n" + new_block + "\n"

    p.write_text(s, encoding="utf-8")
    print("✅ Core JS güncellendi:" if s != old else "ℹ️ Core JS değişmedi:", p.relative_to(ROOT))

print()
print("✅ Minimal V44 uygulandı.")
