from pathlib import Path
from datetime import datetime
import shutil

ROOT = Path(".").resolve()
STAMP = datetime.now().strftime("%Y%m%d-%H%M%S")

TARGETS = [
    {
        "tpl": ROOT / "templates/live_map.html",
        "css": ROOT / "static/live_map/live-seats-overlay-v40.css",
        "js": ROOT / "static/live_map/live-seats-overlay-v40.js",
    },
    {
        "tpl": ROOT / "android_app/app/src/main/python/templates/live_map.html",
        "css": ROOT / "android_app/app/src/main/python/static/live_map/live-seats-overlay-v40.css",
        "js": ROOT / "android_app/app/src/main/python/static/live_map/live-seats-overlay-v40.js",
    },
]

CSS = r'''/* =========================================================
   LIVE_SEATS_OVERLAY_V40
   Canlı takip ekranına koltuklar açılır paneli.
   Sadece UI katmanı. Backend / kayıt mantığına dokunmaz.
========================================================= */

.v40-live-seats-lock,
.v40-live-seats-lock body{
  overflow:hidden !important;
}

.v40-live-seats-btn{
  position:fixed;
  right:14px;
  bottom:calc(82px + env(safe-area-inset-bottom));
  z-index:1040;

  min-width:128px;
  height:54px;
  padding:0 16px;
  border:1px solid rgba(255,255,255,.18);
  border-radius:999px;

  display:flex;
  align-items:center;
  justify-content:center;
  gap:8px;

  color:#fff;
  background:
    radial-gradient(circle at 20% 15%, rgba(255,255,255,.28), transparent 30%),
    linear-gradient(135deg, rgba(37,99,235,.98), rgba(14,165,233,.88));
  box-shadow:
    0 18px 45px rgba(0,0,0,.42),
    0 0 0 1px rgba(59,130,246,.18),
    inset 0 1px 0 rgba(255,255,255,.24);

  font:900 15px/1 system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  letter-spacing:.2px;
  cursor:pointer;
  -webkit-tap-highlight-color:transparent;
}

.v40-live-seats-btn:active{
  transform:scale(.97);
}

.v40-live-seats-btn .v40-ico{
  width:28px;
  height:28px;
  border-radius:14px;
  display:grid;
  place-items:center;
  background:rgba(255,255,255,.16);
  box-shadow:inset 0 1px 0 rgba(255,255,255,.18);
}

#liveSeatsOverlayV40{
  position:fixed;
  inset:0;
  z-index:9998;
  display:none;
  align-items:flex-end;
  justify-content:center;
  padding:14px 10px calc(14px + env(safe-area-inset-bottom));

  background:rgba(3,7,18,.58);
  backdrop-filter:blur(14px);
  -webkit-backdrop-filter:blur(14px);
}

#liveSeatsOverlayV40.v40-show{
  display:flex;
}

.v40-live-seats-panel{
  width:min(720px, 100%);
  max-height:94vh;
  overflow:hidden;
  border-radius:30px;
  border:1px solid rgba(148,163,184,.22);
  background:
    radial-gradient(circle at 15% 0%, rgba(37,99,235,.22), transparent 34%),
    radial-gradient(circle at 85% 0%, rgba(244,63,94,.16), transparent 32%),
    linear-gradient(180deg, rgba(15,23,42,.98), rgba(2,6,23,.98));
  box-shadow:
    0 34px 90px rgba(0,0,0,.62),
    inset 0 1px 0 rgba(255,255,255,.08);
  color:#fff;
  transform:translateY(18px);
  opacity:.96;
  animation:v40SeatPanelIn .22s ease-out forwards;
}

@keyframes v40SeatPanelIn{
  from{ transform:translateY(38px); opacity:.72; }
  to{ transform:translateY(0); opacity:1; }
}

.v40-live-seats-head{
  padding:18px 18px 12px;
  display:flex;
  align-items:center;
  justify-content:space-between;
  gap:12px;
  border-bottom:1px solid rgba(148,163,184,.14);
}

.v40-live-seats-title{
  display:flex;
  flex-direction:column;
  gap:4px;
}

.v40-live-seats-title strong{
  font-size:24px;
  line-height:1;
  letter-spacing:-.7px;
  font-weight:1000;
}

.v40-live-seats-title span{
  color:rgba(226,232,240,.72);
  font-size:12px;
  font-weight:800;
}

.v40-live-seats-close{
  width:44px;
  height:44px;
  border:0;
  border-radius:18px;
  color:#fff;
  background:rgba(255,255,255,.10);
  box-shadow:inset 0 1px 0 rgba(255,255,255,.10);
  font-size:22px;
  font-weight:1000;
  cursor:pointer;
}

.v40-live-stop-strip{
  padding:12px 14px 10px;
  display:flex;
  gap:10px;
  overflow-x:auto;
  overscroll-behavior-x:contain;
  scrollbar-width:none;
}

.v40-live-stop-strip::-webkit-scrollbar{
  display:none;
}

.v40-stop-clone{
  flex:0 0 auto;
  width:min(260px, 74vw);
  min-height:86px;
  max-height:156px;
  overflow:hidden;

  border-radius:22px;
  border:1px solid rgba(255,255,255,.14);
  background:
    radial-gradient(circle at 20% 20%, rgba(255,255,255,.12), transparent 34%),
    rgba(15,23,42,.82);
  box-shadow:
    0 15px 35px rgba(0,0,0,.30),
    inset 0 1px 0 rgba(255,255,255,.08);

  padding:10px;
  color:#fff;
  pointer-events:none;
}

.v40-stop-clone,
.v40-stop-clone *{
  max-width:100% !important;
  box-sizing:border-box !important;
}

.v40-stop-clone *{
  font-family:system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif !important;
}

.v40-stop-empty{
  width:100%;
  border:1px dashed rgba(148,163,184,.28);
  border-radius:22px;
  padding:14px;
  color:rgba(226,232,240,.72);
  font-size:13px;
  font-weight:800;
  background:rgba(15,23,42,.48);
}

.v40-live-seat-frame-wrap{
  margin:0 12px 12px;
  border-radius:26px;
  overflow:hidden;
  border:1px solid rgba(148,163,184,.16);
  background:#07111f;
  box-shadow:inset 0 1px 0 rgba(255,255,255,.06);
}

#liveSeatsFrameV40{
  width:100%;
  height:68vh;
  min-height:430px;
  border:0;
  display:block;
  background:#07111f;
}

@media(max-width:420px){
  .v40-live-seats-btn{
    right:12px;
    bottom:calc(76px + env(safe-area-inset-bottom));
    min-width:116px;
    height:50px;
    padding:0 13px;
    font-size:14px;
  }

  .v40-live-seats-panel{
    border-radius:27px;
  }

  .v40-live-seats-head{
    padding:16px 15px 10px;
  }

  .v40-live-seats-title strong{
    font-size:22px;
  }

  #liveSeatsFrameV40{
    height:66vh;
    min-height:410px;
  }
}
'''

JS = r'''/* =========================================================
   LIVE_SEATS_OVERLAY_V40
   Canlı takip ekranında Koltuklar butonu + açılır panel.
========================================================= */
(function(){
  const MARK = "LIVE_SEATS_OVERLAY_V40_READY";
  if (window[MARK]) return;
  window[MARK] = true;

  function ready(fn){
    if (document.readyState === "loading"){
      document.addEventListener("DOMContentLoaded", fn);
    } else {
      fn();
    }
  }

  function cleanIds(root){
    if (!root) return;
    if (root.removeAttribute) root.removeAttribute("id");
    root.querySelectorAll("[id]").forEach(function(n){
      n.removeAttribute("id");
    });
  }

  function makeOverlay(){
    if (document.getElementById("liveSeatsOverlayV40")) return;

    const overlay = document.createElement("div");
    overlay.id = "liveSeatsOverlayV40";
    overlay.setAttribute("aria-hidden", "true");

    overlay.innerHTML = `
      <div class="v40-live-seats-panel" role="dialog" aria-modal="true" aria-label="Koltuklar">
        <div class="v40-live-seats-head">
          <div class="v40-live-seats-title">
            <strong>🪑 Koltuklar</strong>
            <span>Canlı takipten çıkmadan hızlı kontrol</span>
          </div>
          <button type="button" class="v40-live-seats-close" id="liveSeatsCloseV40" aria-label="Kapat">×</button>
        </div>

        <div class="v40-live-stop-strip" id="liveStopCardsV40"></div>

        <div class="v40-live-seat-frame-wrap">
          <iframe id="liveSeatsFrameV40" title="Koltuk Planı"></iframe>
        </div>
      </div>
    `;

    document.body.appendChild(overlay);

    overlay.addEventListener("click", function(e){
      if (e.target === overlay) closeOverlay();
    });

    const closeBtn = document.getElementById("liveSeatsCloseV40");
    if (closeBtn) closeBtn.addEventListener("click", closeOverlay);

    document.addEventListener("keydown", function(e){
      if (e.key === "Escape") closeOverlay();
    });

    const frame = document.getElementById("liveSeatsFrameV40");
    if (frame){
      frame.addEventListener("load", function(){
        injectFrameStyle(frame);
      });
    }
  }

  function makeButton(){
    if (document.getElementById("liveSeatsOpenBtnV40")) return;

    const btn = document.createElement("button");
    btn.type = "button";
    btn.id = "liveSeatsOpenBtnV40";
    btn.className = "v40-live-seats-btn";
    btn.innerHTML = `<span class="v40-ico">🪑</span><b>Koltuklar</b>`;

    btn.addEventListener("click", function(e){
      e.preventDefault();
      e.stopPropagation();
      openOverlay();
    });

    document.body.appendChild(btn);
  }

  function isVisible(el){
    try{
      const r = el.getBoundingClientRect();
      const st = window.getComputedStyle(el);
      return (
        r.width > 80 &&
        r.height > 38 &&
        r.height < 260 &&
        st.display !== "none" &&
        st.visibility !== "hidden" &&
        Number(st.opacity || 1) > 0.05
      );
    }catch(e){
      return false;
    }
  }

  function findStopCards(){
    const words = /(canlı|sıradaki|bekliyor|durak|otogar|ortahan|belenyaka|alaşehir|inecek|bagaj|kalan|plan\/eta|eta)/i;
    const bad = /(koltuklar|muavin asistanı açılıyor|aktif sefer var)/i;
    const nodes = Array.from(document.body.querySelectorAll("article, section, div, button"));
    const picked = [];

    for (const el of nodes){
      if (el.closest("#liveSeatsOverlayV40")) continue;
      if (el.id === "liveSeatsOpenBtnV40") continue;
      if (!isVisible(el)) continue;

      const txt = (el.innerText || "").trim().replace(/\s+/g, " ");
      const cls = (el.className && el.className.toString ? el.className.toString() : "");

      if (!txt || txt.length < 5 || txt.length > 320) continue;
      if (bad.test(txt)) continue;
      if (!words.test(txt + " " + cls)) continue;

      const r = el.getBoundingClientRect();

      for (let i = picked.length - 1; i >= 0; i--){
        const old = picked[i];
        try{
          const or = old.getBoundingClientRect();
          if (el.contains(old) && r.height <= 220 && r.width <= 540){
            picked.splice(i, 1);
          }
        }catch(e){}
      }

      if (picked.some(function(x){ return x.contains(el); })) continue;

      picked.push(el);
      if (picked.length >= 4) break;
    }

    return picked;
  }

  function fillStopCards(){
    const box = document.getElementById("liveStopCardsV40");
    if (!box) return;

    box.innerHTML = "";

    const cards = findStopCards();

    if (!cards.length){
      const empty = document.createElement("div");
      empty.className = "v40-stop-empty";
      empty.textContent = "Durak kartları okunamadı. Koltuk planı aşağıda açılıyor.";
      box.appendChild(empty);
      return;
    }

    cards.forEach(function(card){
      const wrap = document.createElement("div");
      wrap.className = "v40-stop-clone";

      const clone = card.cloneNode(true);
      cleanIds(clone);

      wrap.appendChild(clone);
      box.appendChild(wrap);
    });
  }

  function injectFrameStyle(frame){
    try{
      const doc = frame.contentDocument || frame.contentWindow.document;
      if (!doc || doc.getElementById("liveSeatsFrameStyleV40")) return;

      const style = doc.createElement("style");
      style.id = "liveSeatsFrameStyleV40";
      style.textContent = `
        html,body{
          background:#07111f !important;
          overflow:auto !important;
        }

        .topbar,
        #driveInlineDock,
        .driveInlineDock,
        .bottom-nav,
        .bottom-bar,
        .simple-bottom-bar,
        #seatSimpleBottomBar,
        #bottomNav,
        .seat-bottom-nav,
        .fab-column{
          display:none !important;
        }

        .seats-shell,
        .layout{
          margin:0 !important;
          padding:0 !important;
          max-width:none !important;
          background:transparent !important;
        }

        .layout{
          gap:8px !important;
        }

        .board-card,
        .board-inner{
          margin:0 !important;
          padding:8px !important;
          border-radius:24px !important;
          background:#07111f !important;
        }

        .board-head,
        .legend,
        .voice-row,
        .drive-voice-row,
        #driveVoiceRow,
        .selected-stop-chip{
          display:none !important;
        }

        .deck,
        .deck-wrap,
        .seat-grid{
          margin-top:0 !important;
        }
      `;

      doc.head.appendChild(style);
    }catch(e){
      // Aynı origin değilse sessiz geç.
    }
  }

  function openOverlay(){
    makeOverlay();
    fillStopCards();

    const overlay = document.getElementById("liveSeatsOverlayV40");
    const frame = document.getElementById("liveSeatsFrameV40");

    if (frame && !frame.dataset.loaded){
      frame.src = "/seats?live_overlay_v40=1";
      frame.dataset.loaded = "1";
    }

    if (overlay){
      overlay.classList.add("v40-show");
      overlay.setAttribute("aria-hidden", "false");
      document.documentElement.classList.add("v40-live-seats-lock");
    }
  }

  function closeOverlay(){
    const overlay = document.getElementById("liveSeatsOverlayV40");
    if (overlay){
      overlay.classList.remove("v40-show");
      overlay.setAttribute("aria-hidden", "true");
    }
    document.documentElement.classList.remove("v40-live-seats-lock");
  }

  ready(function(){
    makeOverlay();
    makeButton();
  });
})();
'''

LINK_CSS = '<link rel="stylesheet" href="/static/live_map/live-seats-overlay-v40.css?v=40">'
LINK_JS = '<script src="/static/live_map/live-seats-overlay-v40.js?v=40"></script>'

print("===== LIVE SEATS OVERLAY V40 =====")

for t in TARGETS:
    tpl = t["tpl"]
    css = t["css"]
    js = t["js"]

    css.parent.mkdir(parents=True, exist_ok=True)
    js.parent.mkdir(parents=True, exist_ok=True)

    css.write_text(CSS, encoding="utf-8")
    js.write_text(JS, encoding="utf-8")

    print("✅ CSS yazıldı:", css.relative_to(ROOT))
    print("✅ JS yazıldı:", js.relative_to(ROOT))

    if not tpl.exists():
        print("⚠️ Template yok:", tpl.relative_to(ROOT))
        continue

    backup = tpl.with_name(tpl.name + f".bak-live-seats-overlay-v40-{STAMP}")
    shutil.copy2(tpl, backup)

    s = tpl.read_text(encoding="utf-8", errors="ignore")

    if "live-seats-overlay-v40.css" not in s:
        if "</head>" in s:
            s = s.replace("</head>", "  " + LINK_CSS + "\n</head>", 1)
        else:
            s = LINK_CSS + "\n" + s
        print("✅ CSS link eklendi:", tpl.relative_to(ROOT))
    else:
        print("ℹ️ CSS link zaten var:", tpl.relative_to(ROOT))

    if "live-seats-overlay-v40.js" not in s:
        if "</body>" in s:
            s = s.replace("</body>", "  " + LINK_JS + "\n</body>", 1)
        else:
            s = s + "\n" + LINK_JS + "\n"
        print("✅ JS link eklendi:", tpl.relative_to(ROOT))
    else:
        print("ℹ️ JS link zaten var:", tpl.relative_to(ROOT))

    tpl.write_text(s, encoding="utf-8")
    print("📦 Yedek:", backup.relative_to(ROOT))

print()
print("===== KONTROL =====")
for t in TARGETS:
    for key, p in t.items():
        if p.exists():
            txt = p.read_text(encoding="utf-8", errors="ignore")
            print(p.relative_to(ROOT), "v40-css:", txt.count("live-seats-overlay-v40.css"), "v40-js:", txt.count("live-seats-overlay-v40.js"), "marker:", txt.count("LIVE_SEATS_OVERLAY_V40"))

print()
print("✅ V40 tamam. Canlı takip ekranında sağ altta 'Koltuklar' butonu çıkacak.")
