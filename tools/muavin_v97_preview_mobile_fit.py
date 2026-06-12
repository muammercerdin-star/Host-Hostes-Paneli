from pathlib import Path
from datetime import datetime
import shutil

ROOT = Path(".").resolve()
CSS = ROOT / "static/continue/v97_proximity_preview.css"
STAMP = datetime.now().strftime("%Y%m%d-%H%M%S")

print("===== V97B PREVIEW MOBILE FIT =====")

if not CSS.exists():
    raise SystemExit("❌ v97_proximity_preview.css yok")

s = CSS.read_text(encoding="utf-8", errors="ignore")

MARK = "V97B_MOBILE_FIT"

block = r'''

/* V97B_MOBILE_FIT
   Preview ekranını dar Android Chrome ekranına sığdırır.
   Mevcut canlı durak sistemine dokunmaz.
*/

body{
  overflow-x:hidden !important;
}

.v97-hdr{
  height:70px !important;
  padding:12px 16px !important;
}

.v97-logo{
  width:42px !important;
  height:42px !important;
  border-radius:12px !important;
}

.v97-title{
  font-size:22px !important;
  letter-spacing:7px !important;
}

.v97-sub{
  font-size:11px !important;
  letter-spacing:5px !important;
}

.v97-clock{
  font-size:28px !important;
  letter-spacing:4px !important;
}

.v97-route{
  height:auto !important;
  min-height:58px !important;
  padding:9px 16px !important;
  flex-wrap:wrap !important;
  gap:8px 12px !important;
}

.v97-route b{
  font-size:25px !important;
  line-height:1.12 !important;
  letter-spacing:5px !important;
  max-width:230px !important;
}

.v97-route em{
  margin-left:0 !important;
  font-size:20px !important;
  letter-spacing:5px !important;
}

.v97-gauges > div{
  min-height:88px !important;
}

.v97-gauges small{
  letter-spacing:4px !important;
  font-size:13px !important;
}

.v97-gauges b{
  font-size:42px !important;
}

.v97-gauges b.green{
  font-size:25px !important;
}

.v97-shell{
  padding:18px 14px !important;
}

.v97-prox-card{
  width:100% !important;
  max-width:100% !important;
  padding:22px 18px !important;
  border-radius:24px !important;
}

.v97-prox-top{
  gap:18px !important;
  align-items:center !important;
}

.v97-ring-wrap,
.v97-ring{
  width:118px !important;
  height:118px !important;
}

.v97-ring-center b{
  font-size:35px !important;
}

.v97-info small{
  letter-spacing:7px !important;
  line-height:1.25 !important;
}

.v97-info h1{
  font-size:38px !important;
}

.v97-info p b{
  font-size:31px !important;
}

.v97-info p span{
  display:block !important;
  margin-left:0 !important;
  margin-top:2px !important;
  letter-spacing:4px !important;
}

.v97-live-pill{
  padding:8px 18px !important;
  letter-spacing:5px !important;
  font-size:20px !important;
}

.v97-mini-grid{
  gap:14px !important;
}

.v97-mini-grid button{
  min-height:106px !important;
  border-radius:20px !important;
  grid-template-columns:54px 1fr !important;
}

.v97-mini-grid i{
  font-size:33px !important;
}

.v97-mini-grid b{
  font-size:42px !important;
}

.v97-mini-grid span{
  font-size:19px !important;
  letter-spacing:5px !important;
}

.v97-route-progress > div:first-child{
  letter-spacing:4px !important;
  font-size:18px !important;
  text-align:center !important;
}

.v97-timeline-section{
  margin-top:28px !important;
}

.v97-stop-card{
  padding:18px 18px !important;
  border-radius:20px !important;
}

.v97-stop-head h3{
  font-size:28px !important;
}

.v97-stop-metrics{
  grid-template-columns:repeat(4, minmax(0, 1fr)) !important;
  gap:8px !important;
}

.v97-stop-metrics b{
  font-size:24px !important;
}

.v97-stop-metrics span{
  font-size:11px !important;
  letter-spacing:2px !important;
}

/* Simülasyon paneli ekrana binmesin: dar ekranda alta yatay al */
.v97-demo{
  top:auto !important;
  right:8px !important;
  left:8px !important;
  bottom:90px !important;
  flex-direction:row !important;
  align-items:center !important;
  justify-content:center !important;
  gap:6px !important;
  background:rgba(8,11,16,.82) !important;
  backdrop-filter:blur(10px) !important;
  border:1px solid rgba(255,255,255,.08) !important;
  border-radius:16px !important;
  padding:8px !important;
}

.v97-demo small{
  display:none !important;
}

.v97-demo button{
  min-width:auto !important;
  flex:1 !important;
  padding:8px 5px !important;
  font-size:13px !important;
  border-radius:10px !important;
}

.v97-dock{
  min-height:78px !important;
}

@media(max-width:380px){
  .v97-title{
    font-size:20px !important;
    letter-spacing:6px !important;
  }

  .v97-clock{
    font-size:25px !important;
  }

  .v97-ring-wrap,
  .v97-ring{
    width:104px !important;
    height:104px !important;
  }

  .v97-info h1{
    font-size:34px !important;
  }

  .v97-live-pill{
    font-size:17px !important;
    letter-spacing:4px !important;
  }
}
'''

if MARK in s:
    print("ℹ️ V97B zaten var")
else:
    bak = CSS.with_name(CSS.name + f".bak-v97b-fit-{STAMP}")
    shutil.copy2(CSS, bak)
    CSS.write_text(s.rstrip() + "\n" + block + "\n", encoding="utf-8")
    print("✅ V97B mobile fit eklendi")
    print("backup:", bak.relative_to(ROOT))

print("Adres:")
print("http://127.0.0.1:5000/static/continue/v97_proximity_preview.html?v=v97b")
