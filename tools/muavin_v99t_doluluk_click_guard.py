from pathlib import Path
from datetime import datetime
import shutil
import re

ROOT = Path(".").resolve()
STAMP = datetime.now().strftime("%Y%m%d-%H%M%S")

TPL = ROOT / "templates/continue_trip.html"
AND_TPL = ROOT / "android_app/app/src/main/python/templates/continue_trip.html"

JS = ROOT / "static/continue/continue_doluluk_click_guard_v99t.js"
AND_JS = ROOT / "android_app/app/src/main/python/static/continue/continue_doluluk_click_guard_v99t.js"

print("===== V99T DOLULUK TIKLAMA ALANI KİLİT =====")

for p in [TPL, AND_TPL]:
    if p.exists():
        bak = p.with_name(p.name + f".bak-v99t-doluluk-click-{STAMP}")
        shutil.copy2(p, bak)
        print("📦 backup:", bak)

guard_js = r'''
/* V99T_DOLULUK_CLICK_GUARD_START */
(function(){
  "use strict";

  function norm(s){
    return String(s || "")
      .toLocaleLowerCase("tr-TR")
      .replace(/\s+/g, " ")
      .trim();
  }

  function txt(el){
    return el ? norm(el.innerText || el.textContent || "") : "";
  }

  function rectOk(el){
    if(!el || !el.getBoundingClientRect) return false;
    var r = el.getBoundingClientRect();
    return r.width > 40 && r.height > 30 && r.height < 260 && r.width < (window.innerWidth + 40);
  }

  function allCandidates(){
    var sels = [
      ".v99-stat",
      ".v99-kpi",
      ".v99-metric",
      ".v99-top-stat",
      ".v99-info-card",
      ".v99-hud-card",
      ".v99-summary-card",
      ".v99-dashboard-card",
      "[class*='stat']",
      "[class*='metric']",
      "[class*='kpi']"
    ];

    var out = [];
    sels.forEach(function(sel){
      document.querySelectorAll(sel).forEach(function(el){
        if(out.indexOf(el) < 0 && rectOk(el)) out.push(el);
      });
    });

    return out;
  }

  function pickCard(word){
    var w = norm(word);
    var arr = allCandidates().filter(function(el){
      return txt(el).indexOf(w) >= 0;
    });

    arr.sort(function(a,b){
      var ra = a.getBoundingClientRect();
      var rb = b.getBoundingClientRect();
      return (ra.width * ra.height) - (rb.width * rb.height);
    });

    return arr[0] || null;
  }

  function findRow(dol, hiz, durum){
    if(!dol) return null;

    var p = dol.parentElement;
    var depth = 0;

    while(p && depth < 7){
      var r = p.getBoundingClientRect ? p.getBoundingClientRect() : null;

      if(
        r &&
        r.height > 40 &&
        r.height < 260 &&
        r.width > window.innerWidth * 0.45 &&
        (!hiz || p.contains(hiz)) &&
        (!durum || p.contains(durum))
      ){
        return p;
      }

      p = p.parentElement;
      depth++;
    }

    return null;
  }

  function bind(){
    var dol = pickCard("doluluk");
    var hiz = pickCard("hiz");
    var durum = pickCard("durum");

    if(!dol) return null;

    var row = findRow(dol, hiz, durum);

    document.querySelectorAll(".v99t-doluluk-click-target").forEach(function(el){
      el.classList.remove("v99t-doluluk-click-target");
    });

    document.querySelectorAll(".v99t-doluluk-row-guard").forEach(function(el){
      el.classList.remove("v99t-doluluk-row-guard");
    });

    dol.classList.add("v99t-doluluk-click-target");
    dol.setAttribute("role", "button");
    dol.setAttribute("tabindex", "0");
    dol.setAttribute("title", "Doluluk panelini aç");

    if(row){
      row.classList.add("v99t-doluluk-row-guard");
    }

    if(hiz) hiz.setAttribute("data-v99t-no-panel", "1");
    if(durum) durum.setAttribute("data-v99t-no-panel", "1");

    return { dol:dol, hiz:hiz, durum:durum, row:row };
  }

  function ensureStyle(){
    if(document.getElementById("v99tDolulukClickGuardStyle")) return;

    var st = document.createElement("style");
    st.id = "v99tDolulukClickGuardStyle";
    st.textContent = `
      .v99t-doluluk-row-guard{
        pointer-events:none !important;
      }

      .v99t-doluluk-click-target{
        pointer-events:auto !important;
        cursor:pointer !important;
        touch-action:manipulation !important;
      }

      .v99t-doluluk-click-target:active{
        transform:scale(.985);
        filter:brightness(1.12);
      }
    `;

    document.head.appendChild(st);
  }

  ensureStyle();
  bind();

  document.addEventListener("click", function(ev){
    var b = bind();
    if(!b || !b.dol) return;

    var t = ev.target;
    if(!(t instanceof Element)) return;

    if(b.dol.contains(t)){
      return;
    }

    if(
      (b.row && b.row.contains(t)) ||
      (b.hiz && b.hiz.contains(t)) ||
      (b.durum && b.durum.contains(t))
    ){
      ev.preventDefault();
      ev.stopPropagation();
      ev.stopImmediatePropagation();
      return false;
    }
  }, true);

  document.addEventListener("touchstart", function(){
    bind();
  }, true);

  if(document.readyState === "loading"){
    document.addEventListener("DOMContentLoaded", bind);
  }

  window.addEventListener("load", bind);

  var left = 20;
  var timer = setInterval(function(){
    bind();
    left--;
    if(left <= 0) clearInterval(timer);
  }, 500);

  window.MuavinV99DolulukClickGuardBind = bind;
})();
/* V99T_DOLULUK_CLICK_GUARD_END */
'''

JS.parent.mkdir(parents=True, exist_ok=True)
JS.write_text(guard_js, encoding="utf-8")
print("✅ guard JS yazıldı:", JS)

if AND_JS.parent.exists():
    AND_JS.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(JS, AND_JS)
    print("✅ android JS senkron:", AND_JS)

script_tag = '<script src="/static/continue/continue_doluluk_click_guard_v99t.js?v=v99t-doluluk-click"></script>'

for p in [TPL, AND_TPL]:
    if not p.exists():
        continue

    s = p.read_text(encoding="utf-8", errors="ignore")

    s = re.sub(
        r'\n?\s*<script src="/static/continue/continue_doluluk_click_guard_v99t\.js[^"]*"></script>\s*\n?',
        "\n",
        s
    )

    if "</body>" in s:
        s = s.replace("</body>", script_tag + "\n</body>")
    else:
        s = s.rstrip() + "\n" + script_tag + "\n"

    p.write_text(s, encoding="utf-8")
    print("✅ template script eklendi:", p)

print()
print("===== KONTROL =====")
for p in [TPL, AND_TPL, JS, AND_JS]:
    if p.exists():
        txt = p.read_text(encoding="utf-8", errors="ignore")
        print(("✅ VAR  " if "continue_doluluk_click_guard_v99t" in txt or "V99T_DOLULUK_CLICK_GUARD" in txt else "⚠️ YOK  ") + str(p))

print()
print("✅ Bitti. Sayfayı şununla yenile:")
print("http://127.0.0.1:5000/continue-trip?v=v99t-doluluk-click")
