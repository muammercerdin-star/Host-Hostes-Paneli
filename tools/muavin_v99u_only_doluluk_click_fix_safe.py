from pathlib import Path
from datetime import datetime
import shutil

ROOT = Path(".").resolve()
STAMP = datetime.now().strftime("%Y%m%d-%H%M%S")

WEB_JS = ROOT / "static/continue/continue_trip_v99_clean.js"
AND_JS = ROOT / "android_app/app/src/main/python/static/continue/continue_trip_v99_clean.js"

print("===== V99U SAFE - SADECE DOLULUK TIKLAMA FIX =====")

if not WEB_JS.exists():
    raise SystemExit("❌ JS yok: " + str(WEB_JS))

for p in [WEB_JS, AND_JS]:
    if p.exists():
        bak = p.with_name(p.name + f".bak-v99u-safe-{STAMP}")
        shutil.copy2(p, bak)
        print("📦 backup:", bak)

s = WEB_JS.read_text(encoding="utf-8", errors="ignore")

marker = "/* V99M_OCCUPANCY_PANEL_START */"
mpos = s.find(marker)
if mpos < 0:
    raise SystemExit("❌ V99M panel bloğu bulunamadı")

start = s.find("function isDolulukTarget(el)", mpos)
if start < 0:
    raise SystemExit("❌ function isDolulukTarget(el) bulunamadı")

click_line = 'document.addEventListener("click", function(ev){'
end = s.find(click_line, start)
if end < 0:
    raise SystemExit("❌ click handler başlangıcı bulunamadı")

replacement = '''
  function v99uNormText(v){
    return String(v || "")
      .toLocaleUpperCase("tr-TR")
      .replace(/\\s+/g, " ")
      .trim();
  }

  function v99uNearestTopCard(el){
    if(!el || !el.closest) return null;

    /*
      V99U SAFE:
      Sadece üstteki küçük bilgi kartının kendisini yakala.
      Ortak satır/container yakalanırsa HIZ ve DURUM da yanlışlıkla
      DOLULUK panelini açıyor.
    */
    return el.closest(
      ".v99-gauge, .v99-stat, .v99-top-stat, .v99-info-cell, .v99-stat-card"
    );
  }

  function isDolulukTarget(el){
    var card = v99uNearestTopCard(el);
    if(!card) return false;

    if(card.closest(".v99m-overlay, .v99m-panel, .v99-prox-card, .v99-tl-card, .v99-dock, nav")){
      return false;
    }

    var label = card.querySelector(
      ".v99-gauge-label, .v99-stat-label, .v99-info-label, .card-label, .label, .l"
    );

    var labelText = v99uNormText(label ? label.textContent : "");

    return labelText === "DOLULUK";
  }

  function markDolulukCards(){
    all(".v99m-occ-clickable").forEach(function(el){
      el.classList.remove("v99m-occ-clickable");
    });

    all(".v99-gauge, .v99-stat, .v99-top-stat, .v99-info-cell, .v99-stat-card").forEach(function(el){
      if(isDolulukTarget(el)){
        el.classList.add("v99m-occ-clickable");
        el.setAttribute("data-v99u-doluluk-click", "1");
      }else{
        el.removeAttribute("data-v99u-doluluk-click");
      }
    });
  }

  document.addEventListener("click", function(ev){
'''

s2 = s[:start] + replacement + s[end + len(click_line):]

WEB_JS.write_text(s2, encoding="utf-8")
print("✅ web JS yazıldı:", WEB_JS)

if AND_JS.parent.exists():
    shutil.copy2(WEB_JS, AND_JS)
    print("✅ android JS senkron:", AND_JS)

print()
print("===== KONTROL =====")
txt = WEB_JS.read_text(encoding="utf-8", errors="ignore")

for key in [
    "V99U SAFE",
    "function v99uNearestTopCard",
    "return labelText === \"DOLULUK\"",
    "data-v99u-doluluk-click",
]:
    print(("VAR  " if key in txt else "YOK  ") + key)

print()
print("✅ Bitti. Tarayıcıda /continue-trip?v=v99u-safe ile yenile.")
