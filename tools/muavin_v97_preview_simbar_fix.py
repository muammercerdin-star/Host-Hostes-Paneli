from pathlib import Path
from datetime import datetime
import shutil
import re

ROOT = Path(".").resolve()
HTML = ROOT / "static/continue/v97_proximity_preview.html"
CSS = ROOT / "static/continue/v97_proximity_preview.css"
STAMP = datetime.now().strftime("%Y%m%d-%H%M%S")

print("===== V97C SİMÜLASYON BAR YERLEŞİM FIX =====")

if not HTML.exists():
    raise SystemExit("❌ HTML yok")
if not CSS.exists():
    raise SystemExit("❌ CSS yok")

def backup(p):
    b = p.with_name(p.name + f".bak-v97c-simbar-{STAMP}")
    shutil.copy2(p, b)
    print("backup:", b.relative_to(ROOT))

html = HTML.read_text(encoding="utf-8", errors="ignore")
css = CSS.read_text(encoding="utf-8", errors="ignore")

# 1) Demo barı body sonunda sabit durmaktan çıkarıp gauges altına taşı
demo_re = re.compile(r'\n<div class="v97-demo">[\s\S]*?</div>\s*\n\n<script src=', re.M)
m = demo_re.search(html)

if not m:
    print("ℹ️ Demo blok bulunamadı veya zaten taşınmış")
else:
    demo_block = m.group(0).replace('\n\n<script src=', '\n')
    html = html[:m.start()] + '\n<script src=' + html[m.end():]

    insert_after = '</section>\n\n<main class="v97-shell">'
    replacement = '</section>\n' + demo_block + '\n<main class="v97-shell">'

    if insert_after in html:
      html = html.replace(insert_after, replacement, 1)
      backup(HTML)
      HTML.write_text(html, encoding="utf-8")
      print("✅ Demo bar gauges altına taşındı")
    else:
      print("❌ insert noktası bulunamadı")

# 2) CSS: demo bar artık fixed değil, normal flow test barı
MARK = "V97C_SIMBAR_FLOW_FIX"
block = r'''

/* V97C_SIMBAR_FLOW_FIX
   Simülasyon butonları artık kartın üstüne binmez.
   Preview içindir; gerçek canlı durak ekranına dokunmaz.
*/
.v97-demo{
  position:relative !important;
  top:auto !important;
  right:auto !important;
  left:auto !important;
  bottom:auto !important;
  z-index:20 !important;

  display:flex !important;
  flex-direction:row !important;
  align-items:center !important;
  justify-content:center !important;
  gap:8px !important;

  margin:0 !important;
  padding:10px 10px !important;

  background:#0f141d !important;
  border-top:1px solid rgba(255,255,255,.06) !important;
  border-bottom:1px solid rgba(255,255,255,.06) !important;
  border-left:0 !important;
  border-right:0 !important;
  border-radius:0 !important;
  backdrop-filter:none !important;
}

.v97-demo small{
  display:none !important;
}

.v97-demo button{
  flex:1 1 0 !important;
  min-width:0 !important;
  max-width:98px !important;
  padding:10px 5px !important;
  border-radius:13px !important;
  font-size:16px !important;
  line-height:1.1 !important;
}

.v97-shell{
  padding-top:20px !important;
}

/* Kart alt metrikleri sim bar yüzünden kesilmesin */
.v97-prox-card{
  padding-bottom:24px !important;
}

.v97-mini-grid{
  margin-top:24px !important;
  position:relative !important;
  z-index:5 !important;
}

/* Dock ile içerik arasında daha rahat boşluk */
body{
  padding-bottom:96px !important;
}
'''

if MARK in css:
    print("ℹ️ V97C CSS zaten var")
else:
    backup(CSS)
    CSS.write_text(css.rstrip() + "\n" + block + "\n", encoding="utf-8")
    print("✅ V97C CSS eklendi")

print()
print("Adres:")
print("http://127.0.0.1:5000/static/continue/v97_proximity_preview.html?v=v97c")
