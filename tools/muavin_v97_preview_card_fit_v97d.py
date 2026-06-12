from pathlib import Path
from datetime import datetime
import shutil

ROOT = Path(".").resolve()
CSS = ROOT / "static/continue/v97_proximity_preview.css"
STAMP = datetime.now().strftime("%Y%m%d-%H%M%S")

print("===== V97D PREVIEW CARD INNER FIT =====")

if not CSS.exists():
    raise SystemExit("❌ v97_proximity_preview.css yok")

s = CSS.read_text(encoding="utf-8", errors="ignore")
MARK = "V97D_CARD_INNER_FIT"

block = r'''

/* V97D_CARD_INNER_FIT
   Kart içi sağ taşmayı düzeltir.
   Bagaj / yolcu kutuları, progress etiketleri ve sağ kolon mobilde kesilmez.
   Sadece preview dosyasına uygulanır.
*/

html,
body{
  max-width:100vw !important;
  overflow-x:hidden !important;
}

.v97-shell,
.v97-prox-card,
.v97-timeline-section,
.v97-stop-card{
  max-width:100% !important;
  overflow-x:hidden !important;
}

.v97-prox-card{
  padding-left:16px !important;
  padding-right:16px !important;
}

.v97-prox-top{
  display:grid !important;
  grid-template-columns:116px minmax(0, 1fr) !important;
  gap:16px !important;
  width:100% !important;
}

.v97-ring-wrap,
.v97-ring{
  width:108px !important;
  height:108px !important;
}

.v97-ring-center b{
  font-size:32px !important;
}

.v97-ring-center span{
  font-size:12px !important;
  letter-spacing:3px !important;
}

.v97-info{
  min-width:0 !important;
  max-width:100% !important;
}

.v97-info small{
  display:block !important;
  letter-spacing:6px !important;
  font-size:16px !important;
  line-height:1.2 !important;
  word-break:normal !important;
}

.v97-info h1{
  font-size:36px !important;
  max-width:100% !important;
  white-space:normal !important;
  overflow-wrap:anywhere !important;
}

.v97-info p b{
  font-size:30px !important;
}

.v97-info p span{
  font-size:17px !important;
  letter-spacing:3px !important;
}

.v97-live-pill{
  max-width:100% !important;
  padding:8px 16px !important;
  font-size:19px !important;
  letter-spacing:4px !important;
  justify-content:center !important;
}

/* İnecek / Bagaj kutuları kesilmesin */
.v97-mini-grid{
  grid-template-columns:minmax(0, 1fr) minmax(0, 1fr) !important;
  gap:12px !important;
  width:100% !important;
}

.v97-mini-grid button{
  min-width:0 !important;
  width:100% !important;
  overflow:hidden !important;
  padding:12px 10px !important;
  grid-template-columns:42px minmax(0, 1fr) !important;
  min-height:96px !important;
}

.v97-mini-grid i{
  font-size:29px !important;
}

.v97-mini-grid b{
  font-size:36px !important;
  min-width:0 !important;
}

.v97-mini-grid span{
  font-size:16px !important;
  letter-spacing:3px !important;
  line-height:1.15 !important;
  white-space:normal !important;
  word-break:normal !important;
}

/* Alt progress yazıları taşmasın */
.v97-route-progress > div:first-child{
  display:grid !important;
  grid-template-columns:1fr auto 1fr !important;
  gap:6px !important;
  align-items:center !important;
  font-size:14px !important;
  letter-spacing:2px !important;
}

.v97-route-progress > div:first-child span:first-child{
  text-align:left !important;
}

.v97-route-progress > div:first-child span:last-child{
  text-align:right !important;
}

.v97-route-progress b{
  font-size:14px !important;
  letter-spacing:1px !important;
  white-space:normal !important;
  text-align:center !important;
}

/* Timeline kart içi dört kolon sıkışınca taşmasın */
.v97-stop-metrics{
  grid-template-columns:repeat(4, minmax(0, 1fr)) !important;
}

.v97-stop-metrics > div{
  min-width:0 !important;
}

.v97-stop-metrics b{
  font-size:22px !important;
  white-space:normal !important;
}

.v97-stop-metrics span{
  font-size:10px !important;
  letter-spacing:1.5px !important;
}

/* Demo bar mobilde biraz daha ince */
.v97-demo{
  padding:7px 8px !important;
  gap:6px !important;
}

.v97-demo button{
  font-size:15px !important;
  padding:9px 4px !important;
}

/* Çok dar ekran ekstra sıkıştırma */
@media(max-width:380px){
  .v97-prox-top{
    grid-template-columns:100px minmax(0, 1fr) !important;
    gap:12px !important;
  }

  .v97-ring-wrap,
  .v97-ring{
    width:96px !important;
    height:96px !important;
  }

  .v97-ring-center b{
    font-size:28px !important;
  }

  .v97-info h1{
    font-size:31px !important;
  }

  .v97-info small{
    font-size:14px !important;
    letter-spacing:5px !important;
  }

  .v97-live-pill{
    font-size:16px !important;
    letter-spacing:3px !important;
    padding:7px 12px !important;
  }

  .v97-mini-grid button{
    grid-template-columns:34px minmax(0, 1fr) !important;
    padding:10px 8px !important;
  }

  .v97-mini-grid b{
    font-size:32px !important;
  }

  .v97-mini-grid span{
    font-size:14px !important;
    letter-spacing:2.5px !important;
  }
}
'''

if MARK in s:
    print("ℹ️ V97D zaten var")
else:
    bak = CSS.with_name(CSS.name + f".bak-v97d-card-fit-{STAMP}")
    shutil.copy2(CSS, bak)
    CSS.write_text(s.rstrip() + "\n" + block + "\n", encoding="utf-8")
    print("✅ V97D card fit eklendi")
    print("backup:", bak.relative_to(ROOT))

print()
print("Adres:")
print("http://127.0.0.1:5000/static/continue/v97_proximity_preview.html?v=v97d")
