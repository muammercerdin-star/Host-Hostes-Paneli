from pathlib import Path
from datetime import datetime
import shutil
import re

ROOT = Path(".").resolve()
STAMP = datetime.now().strftime("%Y%m%d-%H%M%S")

TPL_FILES = [
    ROOT / "templates/continue_trip.html",
    ROOT / "android_app/app/src/main/python/templates/continue_trip.html",
]

CSS_MAIN_FILES = [
    ROOT / "static/continue/continue_trip.css",
    ROOT / "android_app/app/src/main/python/static/continue/continue_trip.css",
]

CSS_PART_FILES = [
    ROOT / "static/continue/css_parts/75-refresh-button-v49.css",
    ROOT / "android_app/app/src/main/python/static/continue/css_parts/75-refresh-button-v49.css",
]

JS_FILES = [
    ROOT / "static/continue/continue_refresh_button_v49.js",
    ROOT / "android_app/app/src/main/python/static/continue/continue_refresh_button_v49.js",
]

CSS = r'''
/* CONTINUE_REFRESH_BUTTON_V49 */

.continue-refresh-v49-btn{
  position:fixed;
  top:calc(18px + env(safe-area-inset-top));
  right:16px;
  z-index:6000;

  width:52px;
  height:52px;
  border-radius:20px;
  border:1px solid rgba(255,255,255,.15);

  display:grid;
  place-items:center;

  color:#fff;
  background:
    radial-gradient(circle at 28% 18%, rgba(255,255,255,.24), transparent 34%),
    linear-gradient(180deg, rgba(15,23,42,.86), rgba(2,6,23,.78));

  box-shadow:
    0 18px 42px rgba(0,0,0,.36),
    0 0 0 1px rgba(59,130,246,.08),
    inset 0 1px 0 rgba(255,255,255,.13);

  backdrop-filter:blur(12px) saturate(1.18);
  -webkit-backdrop-filter:blur(12px) saturate(1.18);

  font-family:system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;
  cursor:pointer;
  -webkit-tap-highlight-color:transparent;
}

.continue-refresh-v49-btn:active{
  transform:scale(.94);
}

.continue-refresh-v49-btn .refresh-ico{
  font-size:25px;
  line-height:1;
  font-weight:1000;
  transform:translateY(-1px);
}

.continue-refresh-v49-btn.is-refreshing .refresh-ico{
  animation:continueRefreshSpinV49 .65s linear infinite;
}

@keyframes continueRefreshSpinV49{
  from{ transform:rotate(0deg); }
  to{ transform:rotate(360deg); }
}

/* Koltuk tam ekran overlay açıldığında arkada kalsın */
#continueSeatMapFullscreenV45 ~ .continue-refresh-v49-btn,
body:has(#continueSeatMapFullscreenV45) .continue-refresh-v49-btn{
  display:none !important;
}

@media(max-width:420px){
  .continue-refresh-v49-btn{
    top:calc(16px + env(safe-area-inset-top));
    right:12px;
    width:48px;
    height:48px;
    border-radius:18px;
  }

  .continue-refresh-v49-btn .refresh-ico{
    font-size:23px;
  }
}
'''

JS = r'''
/* CONTINUE_REFRESH_BUTTON_V49 */
(function(){
  if(window.CONTINUE_REFRESH_BUTTON_V49_READY) return;
  window.CONTINUE_REFRESH_BUTTON_V49_READY = true;

  function ready(fn){
    if(document.readyState === "loading"){
      document.addEventListener("DOMContentLoaded", fn);
    }else{
      fn();
    }
  }

  function hardRefresh(){
    try{
      const url = new URL(window.location.href);
      url.searchParams.set("_refresh", String(Date.now()));
      window.location.replace(url.toString());
    }catch(e){
      window.location.reload();
    }
  }

  ready(function(){
    if(document.getElementById("continueRefreshBtnV49")) return;

    const btn = document.createElement("button");
    btn.type = "button";
    btn.id = "continueRefreshBtnV49";
    btn.className = "continue-refresh-v49-btn";
    btn.setAttribute("aria-label", "Sayfayı yenile");
    btn.setAttribute("title", "Sayfayı yenile");
    btn.innerHTML = '<span class="refresh-ico">↻</span>';

    btn.addEventListener("click", function(e){
      e.preventDefault();
      e.stopPropagation();
      btn.classList.add("is-refreshing");
      hardRefresh();
    }, true);

    document.body.appendChild(btn);
  });
})();
'''

SCRIPT_LINE = '  <script src="{{ url_for(\'static\', filename=\'continue/continue_refresh_button_v49.js\') }}?v=refresh-v49"></script>'
IMPORT_LINE = '@import url("./css_parts/75-refresh-button-v49.css");'

def backup(p):
    if p.exists():
        b = p.with_name(p.name + f".bak-refresh-v49-{STAMP}")
        shutil.copy2(p, b)
        print("📦 Yedek:", b.relative_to(ROOT))

print("===== CONTINUE REFRESH BUTTON V49 =====")

for p in CSS_PART_FILES:
    p.parent.mkdir(parents=True, exist_ok=True)
    backup(p)
    p.write_text(CSS.strip() + "\n", encoding="utf-8")
    print("✅ CSS yazıldı:", p.relative_to(ROOT))

for p in JS_FILES:
    p.parent.mkdir(parents=True, exist_ok=True)
    backup(p)
    p.write_text(JS.strip() + "\n", encoding="utf-8")
    print("✅ JS yazıldı:", p.relative_to(ROOT))

for p in CSS_MAIN_FILES:
    if not p.exists():
        print("⚠️ Yok:", p.relative_to(ROOT))
        continue

    backup(p)
    s = p.read_text(encoding="utf-8", errors="ignore")

    lines = [line for line in s.splitlines() if "75-refresh-button-v49.css" not in line]
    lines.append(IMPORT_LINE)

    p.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    print("✅ CSS import eklendi:", p.relative_to(ROOT))

for p in TPL_FILES:
    if not p.exists():
        print("⚠️ Yok:", p.relative_to(ROOT))
        continue

    backup(p)
    s = p.read_text(encoding="utf-8", errors="ignore")

    if "continue_refresh_button_v49.js" not in s:
        if "</body>" not in s:
            print("❌ </body> bulunamadı:", p.relative_to(ROOT))
            raise SystemExit
        s = s.replace("</body>", SCRIPT_LINE + "\n</body>", 1)
        print("✅ Refresh script eklendi:", p.relative_to(ROOT))
    else:
        print("ℹ️ Script zaten var:", p.relative_to(ROOT))

    s = re.sub(r"continue_trip\.css'\) }}\?v=[^\"']+", "continue_trip.css') }}?v=refresh-v49", s)
    s = re.sub(r'continue_trip\.css"\) }}\?v=[^"\']+', 'continue_trip.css") }}?v=refresh-v49', s)

    p.write_text(s, encoding="utf-8")

print()
print("===== KONTROL =====")
for p in TPL_FILES + CSS_MAIN_FILES + CSS_PART_FILES + JS_FILES:
    if p.exists():
        txt = p.read_text(encoding="utf-8", errors="ignore")
        print(
            p.relative_to(ROOT),
            "V49:",
            txt.count("continue_refresh_button_v49") +
            txt.count("75-refresh-button-v49") +
            txt.count("CONTINUE_REFRESH_BUTTON_V49") +
            txt.count("continueRefreshBtnV49")
        )

print()
print("✅ V49 yenileme butonu hazır.")
