from pathlib import Path
from datetime import datetime
import shutil

ROOT = Path(".").resolve()
STAMP = datetime.now().strftime("%Y%m%d-%H%M%S")

WEB_JS = ROOT / "static/continue/continue_trip_core.js"
WEB_CSS = ROOT / "static/continue/css_parts/50-live-v2-top-glow.css"

ANDROID_JS = ROOT / "android_app/app/src/main/python/static/continue/continue_trip_core.js"
ANDROID_CSS = ROOT / "android_app/app/src/main/python/static/continue/css_parts/50-live-v2-top-glow.css"

TARGETS = [WEB_JS, WEB_CSS, ANDROID_JS, ANDROID_CSS]

print("===== LIVE BORDER RUNNER V96C =====")

for p in TARGETS:
    if p.exists():
        bak = p.with_name(p.name + f".bak-v96c-{STAMP}")
        shutil.copy2(p, bak)
        print("YEDEK:", bak)

if not WEB_JS.exists():
    raise SystemExit("❌ continue_trip_core.js yok")
if not WEB_CSS.exists():
    raise SystemExit("❌ 50-live-v2-top-glow.css yok")

js = WEB_JS.read_text(encoding="utf-8", errors="ignore")
css = WEB_CSS.read_text(encoding="utf-8", errors="ignore")

# -------------------------------------------------
# CSS PATCH
# -------------------------------------------------
CSS_MARK = "LIVE_BORDER_RUNNER_PROGRESS_V96C"
css_block = r'''

/* ===== LIVE_BORDER_RUNNER_PROGRESS_V96C ===== */
#liveCurrentCard{
  overflow:hidden !important;
  isolation:isolate !important;
}

#liveCurrentCard.card.live::before{
  content:none !important;
  display:none !important;
}

#liveCurrentCard .live-border-progress-v96c{
  position:absolute;
  inset:0;
  pointer-events:none;
  z-index:1;
  border-radius:inherit;
}

#liveCurrentCard .live-border-progress-v96c svg{
  width:100%;
  height:100%;
  display:block;
  overflow:visible;
}

#liveCurrentCard .live-border-track-v96c{
  fill:none;
  stroke:rgba(255,72,110,.14);
  stroke-width:2.2;
}

#liveCurrentCard .live-border-runner-v96c{
  fill:none;
  stroke:#ff4a74;
  stroke-width:5.2;
  stroke-linecap:round;
  filter:
    drop-shadow(0 0 5px rgba(255,74,116,.95))
    drop-shadow(0 0 14px rgba(255,74,116,.58));
  transition:stroke-dashoffset .35s linear;
}

#liveCurrentCard > *{
  position:relative;
  z-index:2;
}
/* ===== END LIVE_BORDER_RUNNER_PROGRESS_V96C ===== */
'''

if CSS_MARK not in css:
    css = css.rstrip() + "\n" + css_block + "\n"
    print("CSS PATCH: eklendi")
else:
    print("CSS PATCH: zaten var")

# -------------------------------------------------
# JS PATCH BLOCK
# -------------------------------------------------
JS_MARK = "LIVE_BORDER_RUNNER_PROGRESS_V96C"

js_block = r'''
    /* ===== LIVE_BORDER_RUNNER_PROGRESS_V96C ===== */
    (function(){
      if(window.__continueLiveBorderProgress) return;

      const BOOT = window.CONTINUE_BOOT || {};
      const tripId = BOOT.tripId || 0;

      const state = {
        card:null,
        host:null,
        track:null,
        runner:null,
        totalLen:0,
        segLen:0,
        progress:0,
        baselineKm:NaN,
        stopKey:""
      };

      function clamp(n, min, max){
        return Math.max(min, Math.min(max, n));
      }

      function normStop(name){
        return String(name || "")
          .toLocaleLowerCase("tr-TR")
          .replace(/\s+/g, " ")
          .trim();
      }

      function parseDisplayKm(value){
        const raw = String(value ?? "").trim();
        if(!raw || raw === "—" || raw === "-") return NaN;

        const lower = raw.toLocaleLowerCase("tr-TR").replace(",", ".");
        const m = lower.match(/-?\d+(?:\.\d+)?/);
        if(!m) return NaN;

        const n = Number(m[0]);
        if(!Number.isFinite(n)) return NaN;

        if(/\bm\b/.test(lower) && !/\bkm\b/.test(lower)){
          return n / 1000;
        }
        return n;
      }

      function baseKey(stopKey){
        return `continueLiveRunnerBase:${tripId}:${stopKey}`;
      }

      function progKey(stopKey){
        return `continueLiveRunnerProg:${tripId}:${stopKey}`;
      }

      function readNum(key){
        try{
          const v = Number(localStorage.getItem(key));
          return Number.isFinite(v) ? v : NaN;
        }catch(_){
          return NaN;
        }
      }

      function writeNum(key, value){
        try{
          if(Number.isFinite(value)){
            localStorage.setItem(key, String(value));
          }
        }catch(_){}
      }

      function ensure(){
        const card = document.getElementById("liveCurrentCard");
        if(!card) return false;

        if(state.card !== card){
          state.card = card;

          let host = card.querySelector(".live-border-progress-v96c");
          if(!host){
            host = document.createElement("div");
            host.className = "live-border-progress-v96c";
            host.setAttribute("aria-hidden", "true");
            host.innerHTML = `
              <svg viewBox="0 0 100 100" preserveAspectRatio="none">
                <rect class="live-border-track-v96c" x="4" y="4" width="92" height="92" rx="18" ry="18"></rect>
                <rect class="live-border-runner-v96c" x="4" y="4" width="92" height="92" rx="18" ry="18"></rect>
              </svg>
            `;
            card.insertBefore(host, card.firstChild);
          }

          state.host = host;
          state.track = host.querySelector(".live-border-track-v96c");
          state.runner = host.querySelector(".live-border-runner-v96c");
        }

        layout();
        return !!state.runner;
      }

      function layout(){
        if(!state.card || !state.host || !state.track || !state.runner) return;

        const box = state.card.getBoundingClientRect();
        const w = Math.max(80, Math.round(box.width));
        const h = Math.max(80, Math.round(box.height));
        const pad = 4;
        const radius = Math.max(18, Math.min(28, Math.round(Math.min(w, h) * 0.08)));

        const svg = state.host.querySelector("svg");
        if(svg){
          svg.setAttribute("viewBox", `0 0 ${w} ${h}`);
        }

        [state.track, state.runner].forEach(node => {
          node.setAttribute("x", pad);
          node.setAttribute("y", pad);
          node.setAttribute("width", Math.max(10, w - (pad * 2)));
          node.setAttribute("height", Math.max(10, h - (pad * 2)));
          node.setAttribute("rx", radius);
          node.setAttribute("ry", radius);
        });

        const innerW = Math.max(10, w - (pad * 2));
        const innerH = Math.max(10, h - (pad * 2));
        const total = 2 * (innerW + innerH - (4 * radius)) + (2 * Math.PI * radius);

        state.totalLen = total;
        state.segLen = clamp(total * 0.14, 90, 180);

        apply();
      }

      function apply(){
        if(!state.runner || !Number.isFinite(state.totalLen)) return;

        const p = clamp(state.progress || 0, 0, 1);

        state.runner.style.strokeDasharray = `${state.segLen} ${Math.max(1, state.totalLen)}`;
        state.runner.style.strokeDashoffset = String(state.totalLen - (p * state.totalLen));
        state.runner.style.opacity = "1";
      }

      function reset(stopKey, km){
        state.stopKey = stopKey;
        state.progress = 0;
        state.baselineKm = (Number.isFinite(km) && km > 0) ? km : NaN;

        if(stopKey){
          writeNum(baseKey(stopKey), state.baselineKm);
          writeNum(progKey(stopKey), state.progress);
        }

        apply();
      }

      function update(stopName, kmValue){
        if(!ensure()) return;

        const stopKey = normStop(stopName);
        const km = parseDisplayKm(kmValue);

        if(!stopKey) return;

        if(state.stopKey !== stopKey){
          state.stopKey = stopKey;
          state.baselineKm = readNum(baseKey(stopKey));
          state.progress = readNum(progKey(stopKey));
          if(!Number.isFinite(state.progress)) state.progress = 0;
        }

        if(!Number.isFinite(state.baselineKm) || state.baselineKm <= 0 || (Number.isFinite(km) && km > state.baselineKm * 1.15)){
          reset(stopKey, km);
          return;
        }

        if(!Number.isFinite(km)){
          apply();
          return;
        }

        let next = 1 - (km / state.baselineKm);
        next = clamp(next, 0, 1);

        # gps zıplamasında geri sarmasın
        if(next < state.progress){
          next = state.progress;
        }

        state.progress = next;
        writeNum(progKey(stopKey), state.progress);
        apply();
      }

      window.__continueLiveBorderProgress = {
        update,
        layout,
        reset
      };

      function bootNow(){
        ensure();
        const stopEl = document.getElementById("liveCurrentStopName");
        const distEl = document.getElementById("liveDistanceValue");
        update(
          stopEl ? stopEl.textContent : "",
          distEl ? distEl.textContent : ""
        );
      }

      if(document.readyState === "loading"){
        document.addEventListener("DOMContentLoaded", bootNow);
      }else{
        bootNow();
      }

      window.addEventListener("resize", function(){
        setTimeout(layout, 60);
      });
    })();
    /* ===== END LIVE_BORDER_RUNNER_PROGRESS_V96C ===== */
'''.replace("# gps zıplamasında geri sarmasın", "// gps zıplamasında geri sarmasın")

anchor = "      // MIDPOINT_LIVE_STOP_V67"
if JS_MARK not in js:
    if anchor not in js:
        raise SystemExit("❌ JS anchor bulunamadı")
    js = js.replace(anchor, js_block + "\n\n" + anchor, 1)
    print("JS BLOCK: eklendi")
else:
    print("JS BLOCK: zaten var")

# -------------------------------------------------
# setInitial içine progress update
# -------------------------------------------------
old_initial = """      if(distEl && runtimeGpsKm){
        distEl.textContent = formatGpsKm(runtimeGpsKm);
      }"""

new_initial = """      if(distEl && runtimeGpsKm){
        distEl.textContent = formatGpsKm(runtimeGpsKm);
      }

      if(window.__continueLiveBorderProgress){
        window.__continueLiveBorderProgress.update(
          runtimeStop || (stopEl ? stopEl.textContent : ""),
          runtimeGpsKm || (distEl ? distEl.textContent : "")
        );
      }"""

if old_initial in js and new_initial not in js:
    js = js.replace(old_initial, new_initial, 1)
    print("setInitial: update hook eklendi")

# -------------------------------------------------
# sync içine progress update
# -------------------------------------------------
old_sync = """        if(etaEl && s.eta_main){
          etaEl.textContent = s.eta_main;
        }"""

new_sync = """        if(etaEl && s.eta_main){
          etaEl.textContent = s.eta_main;
        }

        if(window.__continueLiveBorderProgress){
          window.__continueLiveBorderProgress.update(
            s.live_stop || (stopEl ? stopEl.textContent : ""),
            s.gps_km || (distEl ? distEl.textContent : "")
          );
        }"""

if old_sync in js and new_sync not in js:
    js = js.replace(old_sync, new_sync, 1)
    print("sync: update hook eklendi")

# -------------------------------------------------
# compute içine progress update
# -------------------------------------------------
old_compute = """      gpsKm = formatKm(liveKm);
      setText("#liveDistanceValue", gpsKm);"""

new_compute = """      gpsKm = formatKm(liveKm);
      setText("#liveDistanceValue", gpsKm);

      if(window.__continueLiveBorderProgress){
        window.__continueLiveBorderProgress.update(liveName, gpsKm);
      }"""

if old_compute in js and new_compute not in js:
    js = js.replace(old_compute, new_compute, 1)
    print("compute: update hook eklendi")

WEB_JS.write_text(js, encoding="utf-8")
WEB_CSS.write_text(css, encoding="utf-8")

print("WEB yazıldı")

# android kopyaya sync
if ANDROID_JS.parent.exists():
    ANDROID_JS.write_text(WEB_JS.read_text(encoding="utf-8", errors="ignore"), encoding="utf-8")
    print("ANDROID JS sync tamam")

if ANDROID_CSS.parent.exists():
    ANDROID_CSS.write_text(WEB_CSS.read_text(encoding="utf-8", errors="ignore"), encoding="utf-8")
    print("ANDROID CSS sync tamam")

print("===== TAMAM =====")
