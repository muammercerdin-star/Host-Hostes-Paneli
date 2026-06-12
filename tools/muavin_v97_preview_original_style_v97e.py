from pathlib import Path
from datetime import datetime
import shutil
import re

ROOT = Path(".").resolve()
CSS = ROOT / "static/continue/v97_proximity_preview.css"
JS = ROOT / "static/continue/v97_proximity_preview.js"
STAMP = datetime.now().strftime("%Y%m%d-%H%M%S")

print("===== V97E ORİJİNAL KİBAR STİL / RENK / FONT =====")

if not CSS.exists():
    raise SystemExit("❌ CSS yok")
if not JS.exists():
    raise SystemExit("❌ JS yok")

css = CSS.read_text(encoding="utf-8", errors="ignore")
js = JS.read_text(encoding="utf-8", errors="ignore")

MARK = "V97E_ORIGINAL_COMPACT_STYLE"

# Google font import en üstte olmalı
font_import = "@import url('https://fonts.googleapis.com/css2?family=Rajdhani:wght@400;500;600;700&family=JetBrains+Mono:wght@400;700&display=swap');\n"

if "fonts.googleapis.com/css2?family=Rajdhani" not in css:
    css = font_import + css

block = r'''

/* V97E_ORIGINAL_COMPACT_STYLE
   Kullanıcının attığı canli_durak.html tasarımındaki:
   - Rajdhani + JetBrains Mono yazı karakteri
   - koyu endüstriyel panel
   - kırmızı / amber / yeşil / mavi renk paleti
   - küçük, kibar, sade ölçüler
   preview ekranına uygulanır.
*/

:root{
  --bg:#0b0d10 !important;
  --panel:#12151a !important;
  --panel2:#181c23 !important;
  --border:#1f2530 !important;
  --red:#e03030 !important;
  --red-dim:#3a1010 !important;
  --amber:#e08820 !important;
  --amber-dim:#2c1f08 !important;
  --green:#1db87a !important;
  --green-dim:#0a2418 !important;
  --blue:#3a8bff !important;
  --blue-dim:#0d1e38 !important;
  --text:#d8dde8 !important;
  --muted:#5a6478 !important;
  --label:#8a95a8 !important;
}

*,
*::before,
*::after{
  box-sizing:border-box !important;
}

html,
body{
  background:var(--bg) !important;
  color:var(--text) !important;
  font-family:'Rajdhani',system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif !important;
  font-size:15px !important;
  overflow-x:hidden !important;
}

/* HEADER — eski kibar ölçü */
.v97-hdr{
  height:auto !important;
  min-height:64px !important;
  padding:14px 20px !important;
  background:var(--panel) !important;
  border-bottom:1px solid var(--border) !important;
}

.v97-brand{
  gap:10px !important;
}

.v97-logo{
  width:34px !important;
  height:34px !important;
  border-radius:8px !important;
  font-size:16px !important;
  background:var(--red) !important;
  box-shadow:0 0 12px #e0303055 !important;
}

.v97-title{
  font-size:18px !important;
  font-weight:700 !important;
  letter-spacing:3px !important;
  color:#fff !important;
  line-height:1.05 !important;
}

.v97-sub{
  font-family:'JetBrains Mono',monospace !important;
  font-size:10px !important;
  letter-spacing:2px !important;
  color:var(--muted) !important;
}

.v97-clock{
  font-family:'JetBrains Mono',monospace !important;
  font-size:22px !important;
  font-weight:700 !important;
  color:var(--amber) !important;
  text-shadow:0 0 16px #e0882055 !important;
  letter-spacing:2px !important;
}

/* ROUTE BAR — ince ve sade */
.v97-route{
  min-height:42px !important;
  height:auto !important;
  padding:10px 20px !important;
  background:var(--panel2) !important;
  border-bottom:1px solid var(--border) !important;
  display:flex !important;
  align-items:center !important;
  gap:12px !important;
  flex-wrap:nowrap !important;
  font-family:'JetBrains Mono',monospace !important;
  font-size:12px !important;
  color:var(--label) !important;
}

.v97-route b{
  color:var(--text) !important;
  font-size:13px !important;
  font-weight:700 !important;
  letter-spacing:1px !important;
  line-height:1.1 !important;
  max-width:none !important;
}

.v97-route em{
  margin-left:auto !important;
  display:flex !important;
  align-items:center !important;
  gap:6px !important;
  color:var(--red) !important;
  font-size:11px !important;
  letter-spacing:1px !important;
  font-weight:700 !important;
}

/* GAUGES — attığın koddaki kompakt ölçü */
.v97-gauges{
  display:grid !important;
  grid-template-columns:1fr 1fr 1fr !important;
  gap:1px !important;
  background:var(--border) !important;
  border-bottom:1px solid var(--border) !important;
}

.v97-gauges > div{
  min-height:86px !important;
  background:var(--panel) !important;
  padding:14px 12px !important;
  display:flex !important;
  flex-direction:column !important;
  align-items:center !important;
  justify-content:center !important;
  gap:4px !important;
}

.v97-gauges small{
  font-family:'JetBrains Mono',monospace !important;
  font-size:10px !important;
  letter-spacing:2px !important;
  color:var(--muted) !important;
  font-weight:700 !important;
}

.v97-gauges b{
  font-family:'JetBrains Mono',monospace !important;
  font-size:22px !important;
  font-weight:700 !important;
  color:var(--text) !important;
  line-height:1 !important;
}

.v97-gauges b.green{
  font-size:14px !important;
  letter-spacing:0 !important;
  color:var(--green) !important;
  text-shadow:0 0 10px #1db87a40 !important;
}

.v97-gauges span{
  font-size:10px !important;
  color:var(--muted) !important;
  letter-spacing:1px !important;
}

.v97-occ{
  width:80px !important;
  height:4px !important;
  background:var(--border) !important;
  border-radius:2px !important;
  margin-top:2px !important;
}

.v97-occ i{
  background:linear-gradient(90deg,var(--green),var(--amber)) !important;
}

.v97-gender{
  font-family:'JetBrains Mono',monospace !important;
  font-size:10px !important;
  color:#3a8bff !important;
}

/* Simülasyon butonları — eski koddaki sağ ince bar */
.v97-demo{
  position:fixed !important;
  top:70px !important;
  right:12px !important;
  left:auto !important;
  bottom:auto !important;
  z-index:200 !important;
  display:flex !important;
  flex-direction:column !important;
  gap:6px !important;
  background:transparent !important;
  border:0 !important;
  padding:0 !important;
  border-radius:0 !important;
  backdrop-filter:none !important;
}

.v97-demo small{
  display:block !important;
  font-size:9px !important;
  color:var(--muted) !important;
  text-align:center !important;
  letter-spacing:1px !important;
}

.v97-demo button{
  min-width:76px !important;
  max-width:92px !important;
  flex:none !important;
  padding:6px 12px !important;
  background:var(--panel2) !important;
  border:1px solid var(--border) !important;
  border-radius:6px !important;
  color:var(--label) !important;
  font-family:'JetBrains Mono',monospace !important;
  font-size:10px !important;
  line-height:1.1 !important;
  font-weight:700 !important;
}

/* PROXIMITY CARD — kibar, sıkı, endüstriyel */
.v97-shell{
  padding:20px 20px 0 !important;
}

.v97-prox-card{
  background:var(--panel) !important;
  border:1px solid var(--border) !important;
  border-radius:16px !important;
  padding:20px !important;
  position:relative !important;
  overflow:hidden !important;
  box-shadow:none !important;
}

.v97-prox-card::before{
  content:'' !important;
  position:absolute !important;
  inset:0 !important;
  width:auto !important;
  height:auto !important;
  background:repeating-linear-gradient(
    0deg,
    transparent,
    transparent 3px,
    rgba(255,255,255,.012) 3px,
    rgba(255,255,255,.012) 4px
  ) !important;
  pointer-events:none !important;
}

.v97-prox-top{
  position:relative !important;
  display:flex !important;
  grid-template-columns:none !important;
  align-items:flex-start !important;
  gap:20px !important;
}

/* Halka ölçüsü eski kod */
.v97-ring-wrap,
.v97-ring{
  width:110px !important;
  height:110px !important;
  flex-shrink:0 !important;
}

.v97-ring{
  transform:rotate(-90deg) !important;
}

.v97-ring-track{
  fill:none !important;
  stroke:var(--red-dim) !important;
  stroke-width:6 !important;
}

.v97-ring-fill{
  fill:none !important;
  stroke:var(--red) !important;
  stroke-width:6 !important;
  stroke-linecap:round !important;
  filter:drop-shadow(0 0 6px var(--red)) !important;
}

.v97-ring-center b{
  font-family:'JetBrains Mono',monospace !important;
  font-size:24px !important;
  font-weight:700 !important;
  color:var(--red) !important;
  text-shadow:0 0 14px var(--red) !important;
  line-height:1 !important;
}

.v97-ring-center span{
  font-family:'JetBrains Mono',monospace !important;
  font-size:10px !important;
  letter-spacing:2px !important;
  color:var(--muted) !important;
  margin-top:2px !important;
}

/* Sağ bilgi bloğu */
.v97-info{
  flex:1 !important;
  min-width:0 !important;
  display:flex !important;
  flex-direction:column !important;
  gap:8px !important;
}

.v97-info small{
  font-family:'JetBrains Mono',monospace !important;
  font-size:10px !important;
  letter-spacing:3px !important;
  color:var(--muted) !important;
  text-transform:uppercase !important;
  line-height:1.2 !important;
}

.v97-info h1{
  font-size:22px !important;
  font-weight:700 !important;
  color:#fff !important;
  line-height:1.1 !important;
  letter-spacing:.5px !important;
  margin:0 !important;
}

.v97-info p{
  display:flex !important;
  align-items:center !important;
  gap:8px !important;
  margin:0 !important;
}

.v97-info p b{
  font-family:'JetBrains Mono',monospace !important;
  font-size:18px !important;
  font-weight:700 !important;
  color:var(--amber) !important;
}

.v97-info p span{
  display:inline !important;
  margin:0 !important;
  font-size:11px !important;
  color:var(--muted) !important;
  letter-spacing:1px !important;
}

.v97-live-pill{
  display:inline-flex !important;
  align-items:center !important;
  gap:5px !important;
  width:fit-content !important;
  max-width:100% !important;
  margin-top:4px !important;
  padding:4px 10px !important;
  border-radius:20px !important;
  font-family:'JetBrains Mono',monospace !important;
  font-size:11px !important;
  font-weight:700 !important;
  letter-spacing:1.5px !important;
  text-transform:uppercase !important;
  background:var(--red-dim) !important;
  color:var(--red) !important;
  border:1px solid #e0303033 !important;
}

/* İnecek / bagaj kutuları — daha kibar */
.v97-mini-grid{
  display:grid !important;
  grid-template-columns:1fr 1fr !important;
  gap:10px !important;
  margin-top:16px !important;
}

.v97-mini-grid button{
  min-height:70px !important;
  background:var(--panel2) !important;
  border:1px solid var(--border) !important;
  border-radius:10px !important;
  padding:12px 14px !important;
  display:flex !important;
  align-items:center !important;
  gap:12px !important;
  color:var(--text) !important;
}

.v97-mini-grid i{
  font-size:20px !important;
  line-height:1 !important;
}

.v97-mini-grid b{
  font-family:'JetBrains Mono',monospace !important;
  font-size:18px !important;
  font-weight:700 !important;
  color:var(--text) !important;
  line-height:1 !important;
}

.v97-mini-grid span{
  font-size:10px !important;
  color:var(--muted) !important;
  letter-spacing:1.5px !important;
  margin-top:2px !important;
  line-height:1.1 !important;
}

/* Progress bar eski sadelik */
.v97-route-progress{
  margin-top:14px !important;
}

.v97-route-progress > div:first-child{
  display:flex !important;
  justify-content:space-between !important;
  gap:8px !important;
  font-family:'JetBrains Mono',monospace !important;
  font-size:10px !important;
  letter-spacing:0 !important;
  color:var(--muted) !important;
  margin-bottom:5px !important;
}

.v97-route-progress b{
  font-size:10px !important;
  font-weight:400 !important;
  letter-spacing:0 !important;
  color:var(--muted) !important;
}

.v97-progress-track{
  height:6px !important;
  background:var(--border) !important;
  border-radius:3px !important;
}

.v97-progress-track i{
  background:linear-gradient(90deg,var(--red-dim),var(--red)) !important;
  border-radius:3px !important;
}

/* Timeline — attığın kod gibi kompakt */
.v97-timeline-section{
  padding:20px 0 0 !important;
  margin-top:0 !important;
}

.v97-section-title{
  font-family:'JetBrains Mono',monospace !important;
  font-size:10px !important;
  letter-spacing:3px !important;
  color:var(--muted) !important;
  margin-bottom:14px !important;
  gap:8px !important;
}

.v97-tl-item{
  display:flex !important;
  gap:14px !important;
  position:relative !important;
}

.v97-spine{
  width:20px !important;
  flex-shrink:0 !important;
}

.v97-node{
  width:14px !important;
  height:14px !important;
  border-radius:50% !important;
  border:2px solid var(--muted) !important;
  background:var(--bg) !important;
  margin-top:14px !important;
}

.v97-node.live{
  border-color:var(--red) !important;
  background:var(--red) !important;
  box-shadow:0 0 10px var(--red) !important;
}

.v97-node.next{
  border-color:var(--amber) !important;
  background:transparent !important;
}

.v97-node.passed{
  border-color:var(--green) !important;
  background:var(--green) !important;
  opacity:.7 !important;
}

.v97-line{
  width:1px !important;
  background:var(--border) !important;
  flex:1 !important;
}

.v97-line.live{
  background:linear-gradient(var(--red),var(--border)) !important;
}

.v97-line.passed{
  background:var(--green) !important;
  opacity:.4 !important;
}

.v97-stop-card{
  flex:1 !important;
  background:var(--panel) !important;
  border:1px solid var(--border) !important;
  border-radius:10px !important;
  padding:12px 14px !important;
  margin-bottom:10px !important;
}

.v97-stop-card.live{
  border-color:#e0303044 !important;
  background:#12100e !important;
}

.v97-stop-card.next{
  border-color:#e0882033 !important;
}

.v97-stop-head h3{
  font-size:15px !important;
  font-weight:700 !important;
  color:#fff !important;
  letter-spacing:.3px !important;
}

.v97-pill{
  font-family:'JetBrains Mono',monospace !important;
  font-size:9px !important;
  font-weight:700 !important;
  letter-spacing:1.5px !important;
  padding:3px 8px !important;
  border-radius:20px !important;
}

.v97-stop-metrics{
  display:flex !important;
  grid-template-columns:none !important;
  gap:16px !important;
  margin-top:8px !important;
}

.v97-stop-metrics b{
  font-family:'JetBrains Mono',monospace !important;
  font-size:14px !important;
  font-weight:700 !important;
}

.v97-stop-metrics span{
  font-size:9px !important;
  color:var(--muted) !important;
  letter-spacing:1px !important;
}

/* Dock eski küçük tip */
.v97-dock{
  background:var(--panel) !important;
  border-top:1px solid var(--border) !important;
  min-height:72px !important;
  padding:8px 0 env(safe-area-inset-bottom,8px) !important;
}

.v97-dock button{
  font-family:'Rajdhani',sans-serif !important;
  font-size:20px !important;
  color:var(--muted) !important;
  gap:4px !important;
}

.v97-dock button span{
  font-size:11px !important;
  letter-spacing:1px !important;
}

.v97-dock button.active{
  color:var(--red) !important;
}

/* Dar ekran ince ayar */
@media(max-width:420px){
  .v97-shell{
    padding-left:20px !important;
    padding-right:20px !important;
  }

  .v97-route{
    overflow:hidden !important;
  }

  .v97-route b{
    font-size:13px !important;
    white-space:nowrap !important;
  }

  .v97-ring-wrap,
  .v97-ring{
    width:110px !important;
    height:110px !important;
  }

  .v97-info h1{
    font-size:22px !important;
  }

  .v97-stop-metrics{
    gap:13px !important;
  }
}
'''

if MARK in css:
    print("ℹ️ V97E CSS zaten var")
else:
    bak = CSS.with_name(CSS.name + f".bak-v97e-original-style-{STAMP}")
    shutil.copy2(CSS, bak)
    CSS.write_text(css.rstrip() + "\n" + block + "\n", encoding="utf-8")
    print("✅ V97E CSS eklendi")
    print("backup:", bak.relative_to(ROOT))

# JS renk mantığını kullanıcının attığı koda yaklaştır: uzak mavi, orta amber, yakın kırmızı.
old = '''  let color = "#3a8bff";
  if(currentKm <= 0){
    color = "#22c982";
  }else if(currentKm <= 5){
    color = "#ff304f";
  }else if(currentKm <= 15){
    color = "#f0a229";
  }

  ring.style.stroke = color;
  ring.style.filter = "drop-shadow(0 0 12px " + color + ")";
  txt.style.color = color;
  txt.style.textShadow = "0 0 18px " + color;'''

new = '''  let color = "#3a8bff";
  if(currentKm <= 5){
    color = "#e03030";
  }else if(currentKm <= 15){
    color = "#e08820";
  }

  ring.style.stroke = color;
  ring.style.filter = "drop-shadow(0 0 8px " + color + ")";
  txt.style.color = color;
  txt.style.textShadow = "0 0 14px " + color;'''

if old in js:
    bak = JS.with_name(JS.name + f".bak-v97e-original-color-{STAMP}")
    shutil.copy2(JS, bak)
    js = js.replace(old, new, 1)
    JS.write_text(js, encoding="utf-8")
    print("✅ JS renk mantığı orijinal stile alındı")
    print("backup:", bak.relative_to(ROOT))
else:
    print("ℹ️ JS renk bloğu birebir bulunamadı, CSS uygulanmış olabilir")

print()
print("Adres:")
print("http://127.0.0.1:5000/static/continue/v97_proximity_preview.html?v=v97e")
