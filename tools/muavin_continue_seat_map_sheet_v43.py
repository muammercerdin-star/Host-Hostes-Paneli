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
    ROOT / "static/continue/css_parts/70-seat-map-sheet-v43.css",
    ROOT / "android_app/app/src/main/python/static/continue/css_parts/70-seat-map-sheet-v43.css",
]

API_CODE = r'''
# ===== CONTINUE_SEAT_MAP_SHEET_V43_API_START =====
@app.route("/api/live-seat-map")
def api_live_seat_map_v43():
    tid = get_active_trip()
    if not tid:
        return jsonify({"ok": False, "error": "Aktif sefer yok."}), 400

    db = get_db()
    trip = db.execute("SELECT * FROM trips WHERE id=?", (tid,)).fetchone()
    if not trip:
        return jsonify({"ok": False, "error": "Sefer bulunamadı."}), 404

    trip_key = ((trip["route"] or "") + "|" + (trip["plate"] or "")).replace(" ", "_")
    route_stops = get_stops(trip["route"])

    try:
        live_runtime = fetch_live_runtime_state(tid)
    except Exception:
        live_runtime = {}

    def _bag_count_for_seat(seat_no):
        try:
            meta = get_counts(trip_key, str(seat_no))
        except Exception:
            meta = ()

        total = 0

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
               COALESCE(passenger_phone,'') AS passenger_phone,
               COALESCE(gender,'') AS gender,
               COALESCE(payment,'') AS payment,
               COALESCE(amount,0) AS amount,
               COALESCE(service,0) AS service
        FROM seats
        WHERE trip_id=?
        ORDER BY CAST(seat_no AS INTEGER), seat_no
        """,
        (tid,),
    ).fetchall()

    occupied = {}
    counts_by_stop = {}

    for r in rows:
        seat_no = str(r["seat_no"])
        to_stop = (r["to_stop"] or "").strip()
        bag_count = _bag_count_for_seat(seat_no)

        item = {
            "seat_no": seat_no,
            "occupied": True,
            "from_stop": r["from_stop"] or "",
            "to_stop": to_stop,
            "passenger_name": r["passenger_name"] or "",
            "passenger_phone": r["passenger_phone"] or "",
            "gender": r["gender"] or "",
            "payment": r["payment"] or "",
            "amount": float(r["amount"] or 0),
            "service": int(r["service"] or 0),
            "bag_count": int(bag_count or 0),
        }

        occupied[seat_no] = item

        if to_stop:
            counts_by_stop[to_stop] = int(counts_by_stop.get(to_stop, 0) or 0) + 1

    seats = []
    for n in SEAT_NUMBERS:
        key = str(n)
        if key in occupied:
            seats.append(occupied[key])
        else:
            seats.append({
                "seat_no": key,
                "occupied": False,
                "from_stop": "",
                "to_stop": "",
                "passenger_name": "",
                "passenger_phone": "",
                "gender": "",
                "payment": "",
                "amount": 0,
                "service": 0,
                "bag_count": 0,
            })

    return jsonify({
        "ok": True,
        "trip_id": tid,
        "route": trip["route"] or "",
        "plate": trip["plate"] or "",
        "live_stop": (live_runtime or {}).get("live_stop", "") or "",
        "route_stops": route_stops,
        "seat_positions": {
            str(k): [int(v[0]), int(v[1])]
            for k, v in SEAT_POSITIONS.items()
        },
        "seats": seats,
        "total_seats": len(SEAT_NUMBERS),
        "occupied_count": len(occupied),
        "empty_count": max(len(SEAT_NUMBERS) - len(occupied), 0),
        "counts_by_stop": counts_by_stop,
    })
# ===== CONTINUE_SEAT_MAP_SHEET_V43_API_END =====
'''

CSS = r'''/* =========================================================
   CONTINUE_SEAT_MAP_SHEET_V43
   Canlı Durak Akışı içinde mevcut sheet ile koltuk planı.
========================================================= */

.continue-seat-map-loading{
  min-height:180px;
  display:grid;
  place-items:center;
  border-radius:22px;
  border:1px dashed rgba(148,163,184,.28);
  background:rgba(15,23,42,.50);
  color:rgba(226,232,240,.82);
  font-weight:900;
}

.v43-seatmap-wrap{
  display:flex;
  flex-direction:column;
  gap:12px;
}

.v43-seatmap-summary{
  display:grid;
  grid-template-columns:repeat(3,1fr);
  gap:8px;
}

.v43-seatmap-stat{
  border:1px solid rgba(148,163,184,.18);
  border-radius:18px;
  padding:10px 8px;
  background:linear-gradient(180deg, rgba(15,23,42,.88), rgba(2,6,23,.72));
  box-shadow:inset 0 1px 0 rgba(255,255,255,.06);
}

.v43-seatmap-stat small{
  display:block;
  color:rgba(226,232,240,.58);
  font-size:10px;
  font-weight:900;
  letter-spacing:.3px;
  text-transform:uppercase;
}

.v43-seatmap-stat b{
  display:block;
  margin-top:4px;
  color:#fff;
  font-size:18px;
  font-weight:1000;
  letter-spacing:-.4px;
}

.v43-seatmap-stop-strip{
  display:flex;
  gap:8px;
  overflow-x:auto;
  padding-bottom:2px;
  scrollbar-width:none;
}

.v43-seatmap-stop-strip::-webkit-scrollbar{
  display:none;
}

.v43-seatmap-stop{
  flex:0 0 auto;
  max-width:170px;
  border:1px solid rgba(148,163,184,.20);
  border-radius:999px;
  padding:9px 12px;
  background:rgba(15,23,42,.72);
  color:rgba(226,232,240,.88);
  font-size:12px;
  font-weight:900;
  white-space:nowrap;
  overflow:hidden;
  text-overflow:ellipsis;
}

.v43-seatmap-stop b{
  margin-left:6px;
  color:#38bdf8;
}

.v43-seatmap-stop.is-live{
  border-color:rgba(34,197,94,.45);
  background:linear-gradient(135deg, rgba(22,101,52,.76), rgba(15,23,42,.74));
  color:#dcfce7;
}

.v43-seatmap-stop.is-active{
  border-color:rgba(250,204,21,.55);
  background:linear-gradient(135deg, rgba(113,63,18,.86), rgba(15,23,42,.74));
  color:#fef9c3;
}

.v43-seatmap-filter-note{
  display:flex;
  align-items:center;
  justify-content:space-between;
  gap:8px;
  border-radius:18px;
  padding:10px 12px;
  background:rgba(2,6,23,.56);
  border:1px solid rgba(148,163,184,.16);
  color:rgba(226,232,240,.76);
  font-size:12px;
  font-weight:850;
}

.v43-seatmap-clear{
  border:0;
  border-radius:999px;
  padding:7px 10px;
  background:rgba(255,255,255,.10);
  color:#fff;
  font-weight:900;
}

.v43-seatmap-board{
  position:relative;
  display:grid;
  grid-template-columns:repeat(5,minmax(42px,1fr));
  grid-auto-rows:54px;
  gap:8px;
  padding:14px;
  border-radius:26px;
  border:1px solid rgba(148,163,184,.20);
  background:
    radial-gradient(circle at 20% 0%, rgba(59,130,246,.16), transparent 35%),
    linear-gradient(180deg, rgba(15,23,42,.95), rgba(2,6,23,.96));
  box-shadow:inset 0 1px 0 rgba(255,255,255,.06);
}

.v43-seatmap-corridor{
  grid-column:3;
  grid-row:1 / span 11;
  border-radius:18px;
  border:1px dashed rgba(148,163,184,.18);
  background:rgba(15,23,42,.40);
  display:grid;
  place-items:center;
  color:rgba(226,232,240,.36);
  font-size:10px;
  font-weight:1000;
  letter-spacing:1.5px;
  writing-mode:vertical-rl;
  pointer-events:none;
}

.v43-seat{
  position:relative;
  min-width:0;
  min-height:0;
  border:1px solid rgba(148,163,184,.18);
  border-radius:17px;
  padding:5px 4px;
  background:linear-gradient(180deg, rgba(51,65,85,.58), rgba(15,23,42,.80));
  color:rgba(226,232,240,.72);
  box-shadow:
    0 8px 18px rgba(0,0,0,.22),
    inset 0 1px 0 rgba(255,255,255,.06);
  font-family:system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;
  overflow:hidden;
}

.v43-seat b{
  display:block;
  font-size:15px;
  line-height:1;
  font-weight:1000;
}

.v43-seat small{
  display:block;
  margin-top:4px;
  font-size:9px;
  line-height:1.05;
  font-weight:850;
  color:rgba(226,232,240,.62);
  white-space:nowrap;
  overflow:hidden;
  text-overflow:ellipsis;
}

.v43-seat em{
  position:absolute;
  right:5px;
  bottom:4px;
  font-style:normal;
  font-size:10px;
  font-weight:1000;
  color:#fef3c7;
}

.v43-seat.is-occupied{
  background:linear-gradient(180deg, rgba(37,99,235,.88), rgba(30,64,175,.88));
  border-color:rgba(147,197,253,.55);
  color:#fff;
}

.v43-seat.is-female{
  background:linear-gradient(180deg, rgba(219,39,119,.88), rgba(157,23,77,.88));
  border-color:rgba(251,207,232,.50);
}

.v43-seat.is-male{
  background:linear-gradient(180deg, rgba(37,99,235,.88), rgba(30,64,175,.88));
  border-color:rgba(147,197,253,.55);
}

.v43-seat.is-service{
  box-shadow:
    0 0 0 2px rgba(34,197,94,.28),
    0 8px 18px rgba(0,0,0,.24),
    inset 0 1px 0 rgba(255,255,255,.08);
}

.v43-seat.is-due{
  outline:3px solid rgba(250,204,21,.62);
  outline-offset:1px;
}

.v43-seat.is-dim{
  opacity:.22;
  filter:grayscale(.7);
}

.v43-seat:not(.is-occupied){
  opacity:.54;
}

.v43-seat.is-occupied:active{
  transform:scale(.96);
}

.v43-seat-detail{
  display:flex;
  flex-direction:column;
  gap:12px;
}

.v43-seat-detail-card{
  border:1px solid rgba(148,163,184,.20);
  border-radius:24px;
  padding:14px;
  background:linear-gradient(180deg, rgba(15,23,42,.92), rgba(2,6,23,.92));
}

.v43-seat-detail-title{
  display:flex;
  align-items:center;
  justify-content:space-between;
  gap:10px;
}

.v43-seat-detail-title b{
  font-size:22px;
  font-weight:1000;
  color:#fff;
}

.v43-seat-detail-title span{
  border-radius:999px;
  padding:6px 9px;
  background:rgba(59,130,246,.18);
  color:#bfdbfe;
  font-size:11px;
  font-weight:900;
}

.v43-seat-detail-line{
  margin-top:10px;
  color:rgba(226,232,240,.76);
  font-size:13px;
  font-weight:800;
  line-height:1.45;
}

.v43-seat-detail-actions{
  display:grid;
  grid-template-columns:1fr 1fr;
  gap:8px;
}

.v43-seat-detail-actions button,
.v43-seat-detail-actions a{
  min-height:44px;
  border:0;
  border-radius:16px;
  display:grid;
  place-items:center;
  text-decoration:none;
  color:#fff;
  font-weight:1000;
  background:rgba(255,255,255,.10);
}

.v43-seat-detail-actions .danger{
  background:linear-gradient(135deg, rgba(220,38,38,.92), rgba(127,29,29,.92));
}

@media(max-width:420px){
  .v43-seatmap-board{
    grid-auto-rows:50px;
    gap:7px;
    padding:12px;
  }

  .v43-seat b{
    font-size:14px;
  }

  .v43-seat small{
    font-size:8px;
  }

  .v43-seatmap-summary{
    gap:7px;
  }

  .v43-seatmap-stat b{
    font-size:17px;
  }
}
'''

JS_INSERT = r'''
  /* ===== CONTINUE_SEAT_MAP_SHEET_V43_START ===== */
  let v43SeatMapData = null;
  let v43SeatMapFilter = "";

  function v43Norm(v){
    return text(v).trim().toLocaleLowerCase("tr-TR")
      .replace(/[–\-_/\\.,()[\]]/g, " ")
      .replace(/\s+/g, " ")
      .trim();
  }

  function v43Short(v, maxLen){
    const s = text(v).trim();
    if(!s) return "—";
    return s.length > maxLen ? s.slice(0, maxLen - 1) + "…" : s;
  }

  function v43GenderClass(g){
    const x = v43Norm(g);
    if(x.includes("kad") || x.includes("bayan") || x === "k" || x === "female") return "is-female";
    if(x.includes("erk") || x === "e" || x === "male") return "is-male";
    return "";
  }

  function v43SeatByNo(seatNo){
    const list = v43SeatMapData && Array.isArray(v43SeatMapData.seats) ? v43SeatMapData.seats : [];
    return list.find(x => text(x.seat_no) === text(seatNo)) || null;
  }

  async function openSeatMapV43(){
    lastKind = "seatmap";
    openSheet();

    kickerEl.textContent = "Koltuklar";
    titleEl.textContent = "Koltuk Planı";
    subEl.textContent = "Canlı takipten çıkmadan koltuk kontrolü";
    bodyEl.innerHTML = '<div class="continue-seat-map-loading">Koltuklar yükleniyor...</div>';

    try{
      const res = await fetch(`/api/live-seat-map?_=${Date.now()}`, {
        method:"GET",
        credentials:"same-origin",
        cache:"no-store"
      });

      const data = await res.json();

      if(!data || !data.ok){
        renderEmpty((data && (data.error || data.msg)) || "Koltuk planı alınamadı.");
        return;
      }

      v43SeatMapData = data;
      if(!v43SeatMapFilter){
        v43SeatMapFilter = currentStopName() || data.live_stop || "";
      }

      renderSeatMapV43();

    }catch(err){
      console.error("seat map v43 error", err);
      renderEmpty("Bağlantı hatası. Koltuk planı yüklenemedi.");
    }
  }

  function renderSeatMapV43(){
    const data = v43SeatMapData || {};
    const seats = Array.isArray(data.seats) ? data.seats : [];
    const positions = data.seat_positions || {};
    const routeStopsForMap = Array.isArray(data.route_stops) && data.route_stops.length ? data.route_stops : routeStops;
    const counts = data.counts_by_stop || {};
    const liveStop = currentStopName() || data.live_stop || "";
    const filter = v43SeatMapFilter || "";

    const byNo = {};
    seats.forEach(s => { byNo[text(s.seat_no)] = s; });

    const seatNumbers = Object.keys(positions).sort((a,b) => Number(a) - Number(b));

    const stopStrip = routeStopsForMap.map(stop => {
      const c = Number(counts[stop] || 0);
      const liveCls = v43Norm(stop) === v43Norm(liveStop) ? " is-live" : "";
      const activeCls = filter && v43Norm(stop) === v43Norm(filter) ? " is-active" : "";
      return `
        <button class="v43-seatmap-stop${liveCls}${activeCls}" type="button" data-v43-stop-filter="${escapeHtml(stop)}">
          ${escapeHtml(v43Short(stop, 22))}<b>${c}</b>
        </button>
      `;
    }).join("");

    const filterNote = filter ? `
      <div class="v43-seatmap-filter-note">
        <span>Filtre: <b>${escapeHtml(filter)}</b> durağında inecek koltuklar vurgulu</span>
        <button class="v43-seatmap-clear" type="button" data-v43-clear-filter="1">Tümü</button>
      </div>
    ` : `
      <div class="v43-seatmap-filter-note">
        <span>Tüm koltuklar gösteriliyor</span>
      </div>
    `;

    const seatHtml = seatNumbers.map(no => {
      const pos = positions[no] || [1,1];
      const row = Number(pos[0] || 1);
      const col = Number(pos[1] || 1);
      const s = byNo[no] || { seat_no:no, occupied:false };
      const occupied = !!s.occupied;
      const due = occupied && filter && v43Norm(s.to_stop || "") === v43Norm(filter);
      const dim = filter && occupied && !due;
      const cls = [
        "v43-seat",
        occupied ? "is-occupied" : "",
        occupied ? v43GenderClass(s.gender || "") : "",
        Number(s.service || 0) ? "is-service" : "",
        due ? "is-due" : "",
        dim ? "is-dim" : ""
      ].filter(Boolean).join(" ");

      const routeLabel = occupied ? v43Short(s.to_stop || "İniş yok", 12) : "Boş";
      const bag = Number(s.bag_count || 0);

      return `
        <button class="${cls}" type="button"
          style="grid-row:${row};grid-column:${col};"
          data-v43-seat-no="${escapeHtml(no)}"
          aria-label="Koltuk ${escapeHtml(no)}">
          <b>${escapeHtml(no)}</b>
          <small>${escapeHtml(routeLabel)}</small>
          ${bag > 0 ? `<em>🧳${bag}</em>` : ""}
        </button>
      `;
    }).join("");

    bodyEl.innerHTML = `
      <div class="v43-seatmap-wrap">
        <div class="v43-seatmap-summary">
          <div class="v43-seatmap-stat"><small>Toplam</small><b>${Number(data.total_seats || seatNumbers.length || 0)}</b></div>
          <div class="v43-seatmap-stat"><small>Dolu</small><b>${Number(data.occupied_count || 0)}</b></div>
          <div class="v43-seatmap-stat"><small>Boş</small><b>${Number(data.empty_count || 0)}</b></div>
        </div>

        <div class="v43-seatmap-stop-strip">
          ${stopStrip || '<button class="v43-seatmap-stop" type="button">Durak yok</button>'}
        </div>

        ${filterNote}

        <div class="v43-seatmap-board">
          <div class="v43-seatmap-corridor">KORİDOR</div>
          ${seatHtml}
        </div>
      </div>
    `;
  }

  function renderSeatDetailV43(seatNo){
    const s = v43SeatByNo(seatNo);

    if(!s || !s.occupied){
      kickerEl.textContent = "Boş koltuk";
      titleEl.textContent = `Koltuk ${seatNo}`;
      subEl.textContent = "Bu koltukta kayıt görünmüyor.";
      bodyEl.innerHTML = `
        <div class="v43-seat-detail">
          <div class="v43-seat-detail-card">
            <div class="v43-seat-detail-title">
              <b>Koltuk ${escapeHtml(seatNo)}</b>
              <span>Boş</span>
            </div>
            <div class="v43-seat-detail-line">Bu koltuk şu an boş görünüyor.</div>
          </div>
          <div class="v43-seat-detail-actions">
            <button type="button" data-v43-seatmap-back="1">Geri</button>
            <a href="/seats">Koltuk ekranı</a>
          </div>
        </div>
      `;
      return;
    }

    const bag = Number(s.bag_count || 0);

    kickerEl.textContent = "Koltuk detayı";
    titleEl.textContent = `Koltuk ${s.seat_no}`;
    subEl.textContent = `${s.from_stop || "Biniş yok"} → ${s.to_stop || "İniş yok"}`;

    bodyEl.innerHTML = `
      <div class="v43-seat-detail">
        <div class="v43-seat-detail-card">
          <div class="v43-seat-detail-title">
            <b>Koltuk ${escapeHtml(s.seat_no)}</b>
            <span>${escapeHtml(s.gender || "Yolcu")}</span>
          </div>

          <div class="v43-seat-detail-line">
            <b>Yolcu:</b> ${escapeHtml(s.passenger_name || "İsim yok")}<br>
            <b>Güzergâh:</b> ${escapeHtml(s.from_stop || "Biniş yok")} → ${escapeHtml(s.to_stop || "İniş yok")}<br>
            <b>Ödeme:</b> ${escapeHtml(s.payment || "-")} ${Number(s.amount || 0) ? "• " + Number(s.amount || 0).toLocaleString("tr-TR") + " ₺" : ""}<br>
            <b>Bagaj:</b> ${bag} adet
          </div>
        </div>

        <div class="v43-seat-detail-actions">
          <button type="button" data-v43-seatmap-back="1">Geri</button>
          <button class="sheet-bag-detail-btn" type="button" data-bag-seat="${escapeHtml(s.seat_no)}">🧳 Bagaj</button>
          <button class="sheet-action-btn" type="button" data-change-seat="${escapeHtml(s.seat_no)}">İniş Değiştir</button>
          <button class="sheet-offload-btn danger" type="button" data-offload-seat="${escapeHtml(s.seat_no)}">İndir</button>
        </div>
      </div>
    `;
  }

  const seatMapBtnV43 = document.getElementById("continueSeatMapBtn");
  if(seatMapBtnV43){
    seatMapBtnV43.addEventListener("click", function(e){
      e.preventDefault();
      e.stopPropagation();
      openSeatMapV43();
    });
  }

  if(bodyEl){
    bodyEl.addEventListener("click", function(e){
      const seatBtn = e.target.closest("[data-v43-seat-no]");
      if(seatBtn){
        e.preventDefault();
        renderSeatDetailV43(seatBtn.getAttribute("data-v43-seat-no"));
        return;
      }

      const stopBtn = e.target.closest("[data-v43-stop-filter]");
      if(stopBtn){
        e.preventDefault();
        v43SeatMapFilter = stopBtn.getAttribute("data-v43-stop-filter") || "";
        renderSeatMapV43();
        return;
      }

      const clearBtn = e.target.closest("[data-v43-clear-filter]");
      if(clearBtn){
        e.preventDefault();
        v43SeatMapFilter = "";
        renderSeatMapV43();
        return;
      }

      const backBtn = e.target.closest("[data-v43-seatmap-back]");
      if(backBtn){
        e.preventDefault();
        renderSeatMapV43();
        return;
      }
    });
  }
  /* ===== CONTINUE_SEAT_MAP_SHEET_V43_END ===== */
'''

print("===== CONTINUE SEAT MAP SHEET V43 =====")

# 1) API ekle
for p in APP_FILES:
    if not p.exists():
        print("❌ Yok:", p.relative_to(ROOT))
        continue

    backup = p.with_name(p.name + f".bak-seat-map-v43-{STAMP}")
    shutil.copy2(p, backup)

    s = p.read_text(encoding="utf-8", errors="ignore")

    if "CONTINUE_SEAT_MAP_SHEET_V43_API_START" not in s:
        marker = '@app.route("/api/live-seat-bag-detail")'
        if marker not in s:
            print("❌ API marker bulunamadı:", p.relative_to(ROOT))
            raise SystemExit
        s = s.replace(marker, API_CODE + "\n\n" + marker, 1)
        print("✅ API eklendi:", p.relative_to(ROOT))
    else:
        print("ℹ️ API zaten var:", p.relative_to(ROOT))

    p.write_text(s, encoding="utf-8")
    print("📦 Yedek:", backup.relative_to(ROOT))

# 2) Template butonu bağla + cache versiyonlarını yükselt
for p in TPL_FILES:
    if not p.exists():
        print("❌ Yok:", p.relative_to(ROOT))
        continue

    backup = p.with_name(p.name + f".bak-seat-map-v43-{STAMP}")
    shutil.copy2(p, backup)

    s = p.read_text(encoding="utf-8", errors="ignore")

    if "continueSeatMapBtn" not in s:
        needle = 'class="dock-item" href="{{ url_for(\'seats_page\') }}"'
        repl = 'class="dock-item" id="continueSeatMapBtn" data-seat-map-sheet="1" href="{{ url_for(\'seats_page\') }}"'
        if needle not in s:
            print("❌ Koltuk dock link marker bulunamadı:", p.relative_to(ROOT))
            raise SystemExit
        s = s.replace(needle, repl, 1)
        s = s.replace("<span>Koltuk</span>", "<span>Koltuklar</span>", 1)
        print("✅ Koltuk dock butonu sheet butonuna bağlandı:", p.relative_to(ROOT))
    else:
        print("ℹ️ continueSeatMapBtn zaten var:", p.relative_to(ROOT))

    s = s.replace("continue_trip.css') }}?v=css-parts-1", "continue_trip.css') }}?v=seat-map-v43")
    s = s.replace("continue_trip_core.js') }}?v=core-split-1", "continue_trip_core.js') }}?v=seat-map-v43")

    p.write_text(s, encoding="utf-8")
    print("📦 Yedek:", backup.relative_to(ROOT))

# 3) CSS parçasını yaz ve import et
for p in CSS_PART_FILES:
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(CSS, encoding="utf-8")
    print("✅ CSS part yazıldı:", p.relative_to(ROOT))

for p in CSS_MAIN_FILES:
    if not p.exists():
        print("❌ CSS main yok:", p.relative_to(ROOT))
        continue

    backup = p.with_name(p.name + f".bak-seat-map-v43-{STAMP}")
    shutil.copy2(p, backup)

    s = p.read_text(encoding="utf-8", errors="ignore")

    if "70-seat-map-sheet-v43.css" not in s:
        s = s.rstrip() + '\n@import url("./css_parts/70-seat-map-sheet-v43.css");\n'
        print("✅ CSS import eklendi:", p.relative_to(ROOT))
    else:
        print("ℹ️ CSS import zaten var:", p.relative_to(ROOT))

    p.write_text(s, encoding="utf-8")
    print("📦 Yedek:", backup.relative_to(ROOT))

# 4) JS mevcut sheet içine koltuk modu ekle
for p in CORE_FILES:
    if not p.exists():
        print("❌ Core JS yok:", p.relative_to(ROOT))
        continue

    backup = p.with_name(p.name + f".bak-seat-map-v43-{STAMP}")
    shutil.copy2(p, backup)

    s = p.read_text(encoding="utf-8", errors="ignore")

    if "CONTINUE_SEAT_MAP_SHEET_V43_START" not in s:
        marker = '  if(closeBtn) closeBtn.addEventListener("click", closeSheet);'
        if marker not in s:
            print("❌ closeBtn marker bulunamadı:", p.relative_to(ROOT))
            raise SystemExit
        s = s.replace(marker, JS_INSERT + "\n\n" + marker, 1)
        print("✅ JS sheet koltuk modu eklendi:", p.relative_to(ROOT))
    else:
        print("ℹ️ JS zaten var:", p.relative_to(ROOT))

    p.write_text(s, encoding="utf-8")
    print("📦 Yedek:", backup.relative_to(ROOT))

print()
print("===== KONTROL =====")
check_files = APP_FILES + TPL_FILES + CORE_FILES + CSS_MAIN_FILES + CSS_PART_FILES
for p in check_files:
    if p.exists():
        txt = p.read_text(encoding="utf-8", errors="ignore")
        print(
            p.relative_to(ROOT),
            "API:", txt.count("api/live-seat-map"),
            "BTN:", txt.count("continueSeatMapBtn"),
            "JS:", txt.count("CONTINUE_SEAT_MAP_SHEET_V43"),
            "CSS:", txt.count("v43-seatmap")
        )

print()
print("✅ V43 tamam.")
