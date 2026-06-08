from pathlib import Path
from datetime import datetime
import shutil
import re

ROOT = Path(".").resolve()
STAMP = datetime.now().strftime("%Y%m%d-%H%M%S")

APP_FILES = [
    ROOT / "app.py",
    ROOT / "android_app/app/src/main/python/app.py",
]

TPL_FILES = [
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
    ROOT / "static/continue/css_parts/72-seat-map-fullscreen-v45.css",
    ROOT / "android_app/app/src/main/python/static/continue/css_parts/72-seat-map-fullscreen-v45.css",
]

API_CODE = r'''
# ===== CONTINUE_SEAT_MAP_FULLSCREEN_V45_API_START =====
@app.route("/api/live-seat-map")
def api_live_seat_map_v45():
    tid = get_active_trip()
    if not tid:
        return jsonify({"ok": False, "error": "Aktif sefer yok."}), 400

    db = get_db()
    trip = db.execute("SELECT * FROM trips WHERE id=?", (tid,)).fetchone()
    if not trip:
        return jsonify({"ok": False, "error": "Sefer bulunamadı."}), 404

    trip_key = ((trip["route"] or "") + "|" + (trip["plate"] or "")).replace(" ", "_")

    def bag_count_for(seat_no):
        total = 0
        try:
            meta = get_counts(trip_key, str(seat_no))
        except Exception:
            meta = ()

        if isinstance(meta, (tuple, list)):
            for x in meta[:3]:
                try:
                    total += int(x or 0)
                except Exception:
                    pass
        elif isinstance(meta, dict):
            counts = meta.get("counts")
            if isinstance(counts, dict):
                for k in ("R", "LF", "LB"):
                    try:
                        total += int(counts.get(k) or 0)
                    except Exception:
                        pass
        return int(total or 0)

    rows = db.execute(
        """
        SELECT seat_no,
               COALESCE(from_stop,'') AS from_stop,
               COALESCE(to_stop,'') AS to_stop,
               COALESCE(passenger_name,'') AS passenger_name,
               COALESCE(gender,'') AS gender,
               COALESCE(service,0) AS service
        FROM seats
        WHERE trip_id=?
        ORDER BY CAST(seat_no AS INTEGER), seat_no
        """,
        (tid,),
    ).fetchall()

    by_seat = {}
    for r in rows:
        no = str(r["seat_no"])
        by_seat[no] = {
            "seat_no": no,
            "occupied": True,
            "from_stop": r["from_stop"] or "",
            "to_stop": r["to_stop"] or "",
            "passenger_name": r["passenger_name"] or "",
            "gender": r["gender"] or "",
            "service": int(r["service"] or 0),
            "bag_count": bag_count_for(no),
        }

    seats = []
    for n in SEAT_NUMBERS:
        key = str(n)
        if key in by_seat:
            seats.append(by_seat[key])
        else:
            seats.append({
                "seat_no": key,
                "occupied": False,
                "from_stop": "",
                "to_stop": "",
                "passenger_name": "",
                "gender": "",
                "service": 0,
                "bag_count": 0,
            })

    return jsonify({
        "ok": True,
        "seats": seats,
        "seat_positions": {
            str(k): [int(v[0]), int(v[1])]
            for k, v in SEAT_POSITIONS.items()
        },
        "total_seats": len(SEAT_NUMBERS),
    })
# ===== CONTINUE_SEAT_MAP_FULLSCREEN_V45_API_END =====
'''

CSS = r'''
/* CONTINUE_SEAT_MAP_FULLSCREEN_V45 */

#continueSeatMapFullscreenV45{
  position:fixed;
  inset:0;
  z-index:999999;
  background:#06101f;
  color:#fff;
}

#continueSeatMapFullscreenV45 *{
  box-sizing:border-box;
  -webkit-tap-highlight-color:transparent;
}

.v45-seatmap-close{
  position:fixed;
  top:calc(12px + env(safe-area-inset-top));
  right:14px;
  z-index:3;
  width:52px;
  height:52px;
  border-radius:18px;
  border:1px solid rgba(255,255,255,.18);
  background:rgba(15,23,42,.82);
  color:#fff;
  font-size:32px;
  font-weight:800;
  line-height:1;
  box-shadow:0 14px 32px rgba(0,0,0,.36), inset 0 1px 0 rgba(255,255,255,.10);
}

.v45-seatmap-page{
  position:absolute;
  inset:0;
  padding:calc(76px + env(safe-area-inset-top)) 12px calc(14px + env(safe-area-inset-bottom));
  overflow:auto;
  background:
    radial-gradient(circle at 50% -10%, rgba(37,99,235,.26), transparent 34%),
    radial-gradient(circle at 0% 20%, rgba(244,63,94,.10), transparent 30%),
    linear-gradient(180deg, #071225 0%, #020817 100%);
}

.v45-seatmap-board{
  min-height:100%;
  display:grid;
  grid-template-columns:repeat(5, minmax(46px, 1fr));
  grid-auto-rows:64px;
  gap:9px;
  align-content:start;
  padding:14px;
  border-radius:28px;
  border:1px solid rgba(148,163,184,.20);
  background:
    radial-gradient(circle at 50% 0%, rgba(59,130,246,.18), transparent 36%),
    linear-gradient(180deg, rgba(15,23,42,.92), rgba(2,6,23,.96));
  box-shadow:inset 0 1px 0 rgba(255,255,255,.07), 0 18px 48px rgba(0,0,0,.38);
}

.v45-seatmap-corridor{
  grid-column:3;
  grid-row:1 / span 14;
  border-radius:18px;
  border:1px dashed rgba(148,163,184,.22);
  background:rgba(15,23,42,.42);
  display:grid;
  place-items:center;
  color:rgba(226,232,240,.28);
  font-size:10px;
  font-weight:1000;
  letter-spacing:1.4px;
  writing-mode:vertical-rl;
  pointer-events:none;
}

.v45-seat{
  position:relative;
  border:1px solid rgba(148,163,184,.20);
  border-radius:17px;
  background:linear-gradient(180deg, rgba(51,65,85,.62), rgba(15,23,42,.86));
  color:rgba(226,232,240,.80);
  box-shadow:0 8px 18px rgba(0,0,0,.22), inset 0 1px 0 rgba(255,255,255,.07);
  display:flex;
  flex-direction:column;
  align-items:center;
  justify-content:center;
  text-align:center;
  overflow:hidden;
  padding:5px;
}

.v45-seat b{
  display:block;
  font-size:20px;
  font-weight:1000;
  line-height:1;
  letter-spacing:-.4px;
}

.v45-seat small{
  display:block;
  width:100%;
  margin-top:5px;
  color:rgba(226,232,240,.68);
  font-size:10px;
  font-weight:850;
  white-space:nowrap;
  overflow:hidden;
  text-overflow:ellipsis;
}

.v45-seat.is-empty{
  opacity:.48;
}

.v45-seat.is-full{
  background:linear-gradient(180deg, rgba(37,99,235,.92), rgba(30,64,175,.92));
  border-color:rgba(147,197,253,.54);
  color:#fff;
}

.v45-seat.is-female{
  background:linear-gradient(180deg, rgba(219,39,119,.92), rgba(157,23,77,.92));
  border-color:rgba(251,207,232,.50);
}

.v45-seat.is-male{
  background:linear-gradient(180deg, rgba(37,99,235,.92), rgba(30,64,175,.92));
  border-color:rgba(147,197,253,.54);
}

.v45-seat.is-due{
  outline:3px solid rgba(250,204,21,.68);
  outline-offset:1px;
  box-shadow:0 0 28px rgba(250,204,21,.18), inset 0 1px 0 rgba(255,255,255,.09);
}

.v45-seat .bag{
  position:absolute;
  right:5px;
  bottom:4px;
  font-size:10px;
  font-weight:1000;
  color:#fef3c7;
}

.v45-seatmap-loading{
  min-height:100vh;
  display:grid;
  place-items:center;
  font-size:18px;
  font-weight:1000;
  color:rgba(226,232,240,.82);
}

@media(max-width:420px){
  .v45-seatmap-page{
    padding-left:9px;
    padding-right:9px;
  }

  .v45-seatmap-board{
    grid-auto-rows:60px;
    gap:8px;
    padding:12px;
  }

  .v45-seat b{
    font-size:19px;
  }

  .v45-seat small{
    font-size:9px;
  }
}
'''

JS = r'''
/* ===== CONTINUE_SEAT_MAP_FULLSCREEN_V45_START ===== */
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
      .toLocaleLowerCase("tr-TR")
      .replace(/[–\-_\/\\\.,()\[\]]/g, " ")
      .replace(/\s+/g, " ")
      .trim();
  }

  function currentStop(){
    const el = document.getElementById("liveCurrentStopName");
    return (el && el.textContent ? el.textContent : "").trim();
  }

  function short(v, n){
    const s = String(v || "").trim();
    if(!s) return "Boş";
    return s.length > n ? s.slice(0, n - 1) + "…" : s;
  }

  function close(){
    const old = document.getElementById("continueSeatMapFullscreenV45");
    if(old) old.remove();
    document.body.style.overflow = "";
  }

  function genderClass(g){
    const x = norm(g);
    if(x.includes("kad") || x.includes("bayan") || x === "k" || x === "female") return "is-female";
    if(x.includes("erk") || x === "e" || x === "male") return "is-male";
    return "";
  }

  function render(data){
    close();

    const host = document.createElement("div");
    host.id = "continueSeatMapFullscreenV45";
    host.innerHTML = `
      <button class="v45-seatmap-close" type="button" aria-label="Kapat">×</button>
      <div class="v45-seatmap-page">
        <div class="v45-seatmap-loading">Koltuklar yükleniyor...</div>
      </div>
    `;

    document.body.appendChild(host);
    document.body.style.overflow = "hidden";

    host.querySelector(".v45-seatmap-close").addEventListener("click", close);

    const page = host.querySelector(".v45-seatmap-page");
    const positions = data.seat_positions || {};
    const seats = Array.isArray(data.seats) ? data.seats : [];
    const live = currentStop();

    const byNo = {};
    seats.forEach(s => byNo[String(s.seat_no)] = s);

    const nums = Object.keys(positions).length
      ? Object.keys(positions).sort((a,b) => Number(a) - Number(b))
      : seats.map(s => String(s.seat_no)).sort((a,b) => Number(a) - Number(b));

    const cards = nums.map((no, idx) => {
      const s = byNo[no] || { seat_no:no, occupied:false };
      const pos = positions[no] || [Math.floor(idx / 4) + 1, (idx % 4) + 1];
      const row = Number(pos[0] || 1);
      const col = Number(pos[1] || 1);
      const full = !!s.occupied;
      const due = full && live && norm(s.to_stop || "") === norm(live);
      const bag = Number(s.bag_count || 0);

      const cls = [
        "v45-seat",
        full ? "is-full" : "is-empty",
        full ? genderClass(s.gender || "") : "",
        due ? "is-due" : ""
      ].filter(Boolean).join(" ");

      const label = full ? short(s.to_stop || s.from_stop || "Dolu", 12) : "Boş";

      return `
        <div class="${cls}" style="grid-row:${row};grid-column:${col};">
          <b>${esc(no)}</b>
          <small>${esc(label)}</small>
          ${bag > 0 ? `<span class="bag">🧳${bag}</span>` : ""}
        </div>
      `;
    }).join("");

    page.innerHTML = `
      <div class="v45-seatmap-board">
        <div class="v45-seatmap-corridor">KORİDOR</div>
        ${cards}
      </div>
    `;
  }

  async function open(e){
    e.preventDefault();
    e.stopPropagation();

    close();

    const loading = document.createElement("div");
    loading.id = "continueSeatMapFullscreenV45";
    loading.innerHTML = `
      <button class="v45-seatmap-close" type="button" aria-label="Kapat">×</button>
      <div class="v45-seatmap-loading">Koltuklar yükleniyor...</div>
    `;
    document.body.appendChild(loading);
    document.body.style.overflow = "hidden";
    loading.querySelector(".v45-seatmap-close").addEventListener("click", close);

    try{
      const res = await fetch(`/api/live-seat-map?_=${Date.now()}`, {
        method:"GET",
        credentials:"same-origin",
        cache:"no-store"
      });

      const data = await res.json();

      if(!data || !data.ok){
        throw new Error((data && (data.error || data.msg)) || "Koltuk planı alınamadı");
      }

      render(data);
    }catch(err){
      console.error("V45 seat map error", err);
      close();
      alert("Koltuk planı açılamadı.");
    }
  }

  btn.addEventListener("click", open, true);

  document.addEventListener("keydown", function(e){
    if(e.key === "Escape") close();
  });
})();
/* ===== CONTINUE_SEAT_MAP_FULLSCREEN_V45_END ===== */
'''

def backup(p):
    if p.exists():
        b = p.with_name(p.name + f".bak-seatmap-v45-{STAMP}")
        shutil.copy2(p, b)
        print("📦 Yedek:", b.relative_to(ROOT))

print("===== CONTINUE SEAT MAP FULLSCREEN V45 =====")

# 1) API ekle
for p in APP_FILES:
    if not p.exists():
        print("⚠️ Yok:", p.relative_to(ROOT))
        continue

    backup(p)
    s = p.read_text(encoding="utf-8", errors="ignore")

    if '"/api/live-seat-map"' not in s and '"/api/live-seat-map"' not in s:
        marker = '@app.route("/api/live-seat-bag-detail")'
        if marker not in s:
            print("❌ API marker bulunamadı:", p.relative_to(ROOT))
            raise SystemExit
        s = s.replace(marker, API_CODE + "\n\n" + marker, 1)
        print("✅ API eklendi:", p.relative_to(ROOT))
    else:
        print("ℹ️ /api/live-seat-map zaten var:", p.relative_to(ROOT))

    p.write_text(s, encoding="utf-8")

# 2) Template butonunu bağla
for p in TPL_FILES:
    if not p.exists():
        print("⚠️ Yok:", p.relative_to(ROOT))
        continue

    backup(p)
    s = p.read_text(encoding="utf-8", errors="ignore")

    if "continueSeatMapBtn" not in s:
        s = s.replace(
            'class="dock-item" href="{{ url_for(\'seats_page\') }}"',
            'class="dock-item" id="continueSeatMapBtn" href="{{ url_for(\'seats_page\') }}"',
            1
        )
        s = s.replace(
            'class="dock-item" href="{{ url_for("seats_page") }}"',
            'class="dock-item" id="continueSeatMapBtn" href="{{ url_for("seats_page") }}"',
            1
        )
        s = s.replace("<span>Koltuk</span>", "<span>Koltuklar</span>", 1)
        print("✅ Koltuk butonu bağlandı:", p.relative_to(ROOT))
    else:
        print("ℹ️ Buton zaten bağlı:", p.relative_to(ROOT))

    s = re.sub(r"continue_trip\.css'\) }}\?v=[^\"']+", "continue_trip.css') }}?v=seat-map-v45", s)
    s = re.sub(r'continue_trip\.css"\) }}\?v=[^"\']+', 'continue_trip.css") }}?v=seat-map-v45', s)
    s = re.sub(r"continue_trip_core\.js'\) }}\?v=[^\"']+", "continue_trip_core.js') }}?v=seat-map-v45", s)
    s = re.sub(r'continue_trip_core\.js"\) }}\?v=[^"\']+', 'continue_trip_core.js") }}?v=seat-map-v45', s)

    p.write_text(s, encoding="utf-8")

# 3) CSS yaz
for p in CSS_PART_FILES:
    p.parent.mkdir(parents=True, exist_ok=True)
    backup(p)
    p.write_text(CSS.strip() + "\n", encoding="utf-8")
    print("✅ CSS yazıldı:", p.relative_to(ROOT))

for p in CSS_MAIN_FILES:
    if not p.exists():
        print("⚠️ Yok:", p.relative_to(ROOT))
        continue

    backup(p)
    s = p.read_text(encoding="utf-8", errors="ignore")

    lines = []
    for line in s.splitlines():
        if "70-seat-map-sheet-v43.css" in line:
            continue
        if "70-seat-map-sheet-v44.css" in line:
            continue
        if "72-seat-map-fullscreen-v45.css" in line:
            continue
        lines.append(line)

    lines.append('@import url("./css_parts/72-seat-map-fullscreen-v45.css");')
    p.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    print("✅ CSS import güncellendi:", p.relative_to(ROOT))

# 4) JS ekle
for p in CORE_FILES:
    if not p.exists():
        print("⚠️ Yok:", p.relative_to(ROOT))
        continue

    backup(p)
    s = p.read_text(encoding="utf-8", errors="ignore")

    patterns = [
        r'/\* ===== CONTINUE_SEAT_MAP_SHEET_V43_START ===== \*/.*?/\* ===== CONTINUE_SEAT_MAP_SHEET_V43_END ===== \*/',
        r'/\* ===== CONTINUE_SEAT_MAP_MINIMAL_V44_START ===== \*/.*?/\* ===== CONTINUE_SEAT_MAP_MINIMAL_V44_END ===== \*/',
        r'/\* ===== CONTINUE_SEAT_MAP_FULLSCREEN_V45_START ===== \*/.*?/\* ===== CONTINUE_SEAT_MAP_FULLSCREEN_V45_END ===== \*/',
    ]

    for pat in patterns:
        s = re.sub(pat, "", s, flags=re.S)

    s = s.rstrip() + "\n\n" + JS + "\n"
    p.write_text(s, encoding="utf-8")
    print("✅ JS V45 eklendi:", p.relative_to(ROOT))

print()
print("===== KONTROL =====")
for p in APP_FILES + TPL_FILES + CORE_FILES + CSS_MAIN_FILES + CSS_PART_FILES:
    if p.exists():
        txt = p.read_text(encoding="utf-8", errors="ignore")
        print(
            p.relative_to(ROOT),
            "API:", txt.count("/api/live-seat-map"),
            "BTN:", txt.count("continueSeatMapBtn"),
            "JS:", txt.count("CONTINUE_SEAT_MAP_FULLSCREEN_V45"),
            "CSS:", txt.count("v45-seatmap")
        )

print()
print("✅ V45 yama tamam.")
