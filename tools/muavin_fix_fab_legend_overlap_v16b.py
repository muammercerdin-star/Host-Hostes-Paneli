from pathlib import Path
from datetime import datetime
import shutil

ROOT = Path(".").resolve()
STAMP = datetime.now().strftime("%Y%m%d-%H%M%S")

JS_TARGETS = [
    ROOT / "static/seats/patches/seat-layout-fab-pack.js",
    ROOT / "android_app/app/src/main/python/static/seats/patches/seat-layout-fab-pack.js",
]

TPL_TARGETS = [
    ROOT / "templates/seats.html",
    ROOT / "android_app/app/src/main/python/templates/seats.html",
]

FIX = r'''

/* =========================================================
   FAB_LEGEND_OVERLAP_FIX_V16B
   Sol hızlı işlem paneli, alttaki Bay/Bayan/Bagaj/İniş/Servis
   legend barının üstüne binmesin.
========================================================= */
(function(){
  if(window.__FAB_LEGEND_OVERLAP_FIX_V16B__) return;
  window.__FAB_LEGEND_OVERLAP_FIX_V16B__ = true;

  function visible(el){
    if(!el) return false;
    const cs = getComputedStyle(el);
    const r = el.getBoundingClientRect();
    return cs.display !== "none" && cs.visibility !== "hidden" && r.width > 0 && r.height > 0;
  }

  function px(v){
    const n = parseFloat(String(v || "").replace("px",""));
    return Number.isFinite(n) ? n : 0;
  }

  function clampFabAboveLegend(){
    const col =
      document.querySelector(".fab-column.fab-left-gap-moved") ||
      document.querySelector(".fab-column");

    if(!col || !visible(col)) return;

    const legend =
      document.querySelector("body.drive-mode .board-head-right .legend") ||
      document.querySelector("html.drive-mode .board-head-right .legend");

    const simpleBar = document.querySelector(".seat-simple-bottom-bar");

    let barrierTop = window.innerHeight - 12;

    if(visible(legend)){
      barrierTop = Math.min(barrierTop, legend.getBoundingClientRect().top);
    }

    if(visible(simpleBar)){
      barrierTop = Math.min(barrierTop, simpleBar.getBoundingClientRect().top);
    }

    const gap = 12;
    const r = col.getBoundingClientRect();
    const overflow = r.bottom - (barrierTop - gap);

    if(overflow <= 0) return;

    const currentTop =
      px(col.style.getPropertyValue("--fab-left-gap-top")) ||
      px(col.style.top) ||
      0;

    const nextTop = Math.max(8, currentTop - overflow);

    col.style.setProperty("--fab-left-gap-top", Math.round(nextTop) + "px");
  }

  function schedule(){
    requestAnimationFrame(function(){
      clampFabAboveLegend();
      setTimeout(clampFabAboveLegend, 80);
      setTimeout(clampFabAboveLegend, 220);
    });
  }

  window.addEventListener("load", schedule, {passive:true});
  window.addEventListener("resize", schedule, {passive:true});
  window.addEventListener("orientationchange", schedule, {passive:true});
  window.addEventListener("scroll", schedule, {passive:true, capture:true});
  document.addEventListener("click", schedule, true);
  document.addEventListener("touchend", schedule, true);

  const mo = new MutationObserver(schedule);
  mo.observe(document.documentElement, {
    attributes:true,
    childList:true,
    subtree:true,
    attributeFilter:["class","style"]
  });

  schedule();
})();
'''

def backup(p: Path):
    b = p.with_name(p.name + f".bak-fab-overlap-v16b-{STAMP}")
    shutil.copy2(p, b)
    return b

for p in JS_TARGETS:
    if not p.exists():
        print("⚠️ JS yok:", p)
        continue

    b = backup(p)
    s = p.read_text(encoding="utf-8", errors="ignore")

    if "FAB_LEGEND_OVERLAP_FIX_V16B" not in s:
        s = s.rstrip() + "\n" + FIX + "\n"
        p.write_text(s, encoding="utf-8")
        print("✅ JS overlap düzeltmesi eklendi:", p.relative_to(ROOT))
        print("   Yedek:", b.relative_to(ROOT))
    else:
        print("ℹ️ Marker zaten var:", p.relative_to(ROOT))

for p in TPL_TARGETS:
    if not p.exists():
        print("⚠️ Template yok:", p)
        continue

    b = backup(p)
    s = p.read_text(encoding="utf-8", errors="ignore")
    old = s

    s = s.replace(
        'seat-layout-fab-pack.js?v=1',
        'seat-layout-fab-pack.js?v=fab-overlap-v16b'
    )

    if s != old:
        p.write_text(s, encoding="utf-8")
        print("✅ JS cache versiyonu güncellendi:", p.relative_to(ROOT))
        print("   Yedek:", b.relative_to(ROOT))
    else:
        print("ℹ️ Template değişmedi:", p.relative_to(ROOT))

print()
print("===== KONTROL =====")
for p in JS_TARGETS:
    if p.exists():
        txt = p.read_text(encoding="utf-8", errors="ignore")
        print(p.relative_to(ROOT), "FAB_LEGEND_OVERLAP_FIX_V16B:", txt.count("FAB_LEGEND_OVERLAP_FIX_V16B"))

for p in TPL_TARGETS:
    if p.exists():
        txt = p.read_text(encoding="utf-8", errors="ignore")
        print(p.relative_to(ROOT), "fab-overlap-v16b:", txt.count("fab-overlap-v16b"))

print()
print("✅ V16B tamamlandı.")
