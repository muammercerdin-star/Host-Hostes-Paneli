from pathlib import Path
from datetime import datetime
import shutil
import re

ROOT = Path(".").resolve()
STAMP = datetime.now().strftime("%Y%m%d-%H%M%S")

CSS_FILES = [
    ROOT / "static/continue/continue_v76.css",
    ROOT / "android_app/app/src/main/python/static/continue/continue_v76.css",
]

TPLS = [
    ROOT / "templates/continue_trip.html",
    ROOT / "android_app/app/src/main/python/templates/continue_trip.html",
]

PATCH = r'''

/* CONTINUE_SHEET_CARD_RESTORE_V80 */

/* V79'un genel kart kuralı sheet-list'i tek blok yapıyordu. Yolcu kartlarını tekrar ayrı ayrı göster. */
.sheet-body > .sheet-bulk-bar,
.sheet-body > .sheet-list{
  background:transparent !important;
  border:0 !important;
  box-shadow:none !important;
  padding:0 !important;
}

.sheet-bulk-bar{
  display:flex !important;
  justify-content:flex-end !important;
  margin:4px 0 18px !important;
}

.sheet-bulk-btn{
  min-height:54px !important;
  padding:0 24px !important;
  border-radius:22px !important;
  border:1px solid rgba(255,100,100,.55) !important;
  background:linear-gradient(180deg,#f04444,#b91c1c) !important;
  color:#fff !important;
  font-size:16px !important;
  font-weight:900 !important;
  letter-spacing:1px !important;
  box-shadow:0 16px 32px rgba(224,48,48,.35), inset 0 1px 0 rgba(255,255,255,.20) !important;
}

.sheet-list{
  display:flex !important;
  flex-direction:column !important;
  gap:14px !important;
  margin:0 !important;
}

.sheet-seat-row{
  display:grid !important;
  grid-template-columns:86px minmax(0,1fr) !important;
  gap:16px !important;
  align-items:center !important;
  background:
    radial-gradient(circle at 0% 0%, rgba(58,139,255,.16), transparent 34%),
    linear-gradient(180deg,rgba(24,28,35,.96),rgba(17,21,27,.96)) !important;
  border:1px solid rgba(58,139,255,.30) !important;
  border-radius:22px !important;
  padding:18px !important;
  box-shadow:0 14px 34px rgba(0,0,0,.38), inset 0 0 0 1px rgba(255,255,255,.025) !important;
}

.sheet-seat-no{
  width:76px !important;
  height:76px !important;
  border-radius:22px !important;
  display:grid !important;
  place-items:center !important;
  background:linear-gradient(180deg,#3a8bff,#2457db) !important;
  color:#fff !important;
  font-family:ui-monospace,Menlo,monospace !important;
  font-size:32px !important;
  font-weight:900 !important;
  box-shadow:0 16px 30px rgba(58,139,255,.34), inset 0 1px 0 rgba(255,255,255,.18) !important;
}

.sheet-seat-main{
  min-width:0 !important;
}

.sheet-seat-title{
  color:#fff !important;
  font-size:20px !important;
  font-weight:900 !important;
  line-height:1.15 !important;
  display:flex !important;
  align-items:center !important;
  gap:8px !important;
  flex-wrap:wrap !important;
}

.sheet-gender-chip{
  display:inline-flex !important;
  align-items:center !important;
  height:24px !important;
  padding:0 10px !important;
  border-radius:999px !important;
  background:rgba(58,139,255,.16) !important;
  border:1px solid rgba(58,139,255,.34) !important;
  color:#b8d2ff !important;
  font-size:12px !important;
  font-family:ui-monospace,Menlo,monospace !important;
  font-weight:900 !important;
}

.sheet-seat-row.gender-female .sheet-gender-chip{
  background:rgba(224,96,192,.15) !important;
  border-color:rgba(224,96,192,.34) !important;
  color:#ffb9ec !important;
}

.sheet-seat-route{
  margin-top:8px !important;
  color:#b8c0cf !important;
  font-size:18px !important;
  line-height:1.25 !important;
}

.sheet-seat-extra{
  grid-column:2 !important;
  display:flex !important;
  align-items:center !important;
  flex-wrap:wrap !important;
  gap:10px !important;
  margin-top:-4px !important;
}

.sheet-badge,
.sheet-bag-detail-btn{
  display:inline-flex !important;
  align-items:center !important;
  min-height:38px !important;
  padding:0 13px !important;
  border-radius:999px !important;
  background:rgba(255,255,255,.07) !important;
  border:1px solid rgba(255,255,255,.13) !important;
  color:#d8dde8 !important;
  font-size:15px !important;
  font-family:inherit !important;
  font-weight:700 !important;
  box-shadow:none !important;
}

.sheet-action-btn{
  min-height:40px !important;
  padding:0 16px !important;
  border-radius:15px !important;
  background:linear-gradient(180deg,rgba(30,45,70,.92),rgba(20,28,42,.92)) !important;
  border:1px solid rgba(90,140,210,.38) !important;
  color:#dbeafe !important;
  font-size:14px !important;
  font-weight:900 !important;
  letter-spacing:.2px !important;
  box-shadow:0 8px 18px rgba(0,0,0,.25) !important;
}

.sheet-offload-btn{
  min-height:42px !important;
  padding:0 18px !important;
  border-radius:16px !important;
  background:linear-gradient(180deg,#f04444,#b91c1c) !important;
  border:1px solid rgba(255,120,120,.48) !important;
  color:#fff !important;
  font-size:15px !important;
  font-weight:900 !important;
  letter-spacing:.7px !important;
  box-shadow:0 12px 24px rgba(224,48,48,.30) !important;
}

.sheet-offload-btn.danger{
  background:linear-gradient(180deg,#f04444,#b91c1c) !important;
  color:#fff !important;
}

/* Bagaj modal kartlarını da premium hale getir */
.sheet-bag-item,
.sheet-cargo-item{
  background:linear-gradient(180deg,rgba(24,28,35,.96),rgba(17,21,27,.96)) !important;
  border:1px solid rgba(58,139,255,.24) !important;
  border-radius:22px !important;
  padding:16px !important;
  margin:12px 0 !important;
  box-shadow:0 14px 34px rgba(0,0,0,.34) !important;
}

.sheet-bag-item-head,
.sheet-cargo-head{
  display:flex !important;
  align-items:center !important;
  gap:12px !important;
}

.sheet-bag-icon,
.sheet-cargo-icon{
  width:54px !important;
  height:54px !important;
  display:grid !important;
  place-items:center !important;
  border-radius:16px !important;
  background:linear-gradient(180deg,#3a8bff,#2457db) !important;
  box-shadow:0 12px 24px rgba(58,139,255,.30) !important;
}

.sheet-bag-item-title,
.sheet-cargo-title{
  color:#fff !important;
  font-size:20px !important;
  font-weight:900 !important;
}

.sheet-bag-item-sub,
.sheet-bag-mini,
.sheet-cargo-sub{
  color:#b8c0cf !important;
}

.sheet-bag-actions{
  display:flex !important;
  flex-wrap:wrap !important;
  gap:10px !important;
  margin-top:14px !important;
}

.sheet-bag-detail-open{
  min-height:40px !important;
  padding:0 16px !important;
  border-radius:15px !important;
  background:linear-gradient(180deg,rgba(30,45,70,.92),rgba(20,28,42,.92)) !important;
  border:1px solid rgba(90,140,210,.38) !important;
  color:#dbeafe !important;
  font-weight:900 !important;
}

/* Mobilde eski 2. foto gibi tek kart düzeni */
@media(max-width:420px){
  .sheet-bulk-bar{
    justify-content:flex-end !important;
    margin-bottom:16px !important;
  }

  .sheet-seat-row{
    grid-template-columns:76px minmax(0,1fr) !important;
    gap:14px !important;
    padding:16px !important;
    border-radius:20px !important;
  }

  .sheet-seat-no{
    width:68px !important;
    height:68px !important;
    border-radius:20px !important;
    font-size:28px !important;
  }

  .sheet-seat-title{
    font-size:18px !important;
  }

  .sheet-seat-route{
    font-size:16px !important;
  }

  .sheet-seat-extra{
    grid-column:1 / -1 !important;
    margin-top:2px !important;
    gap:9px !important;
  }

  .sheet-badge,
  .sheet-bag-detail-btn,
  .sheet-action-btn,
  .sheet-offload-btn{
    min-height:38px !important;
    font-size:13px !important;
    padding:0 12px !important;
  }

  .sheet-bulk-btn{
    min-height:50px !important;
    padding:0 22px !important;
    font-size:15px !important;
  }
}
'''

print("===== CONTINUE SHEET CARD RESTORE V80 =====")

for p in CSS_FILES:
    if not p.exists():
        print("⚠️ Yok:", p.relative_to(ROOT))
        continue

    b = p.with_name(p.name + f".bak-sheet-card-v80-{STAMP}")
    shutil.copy2(p, b)
    print("📦 Yedek:", b.relative_to(ROOT))

    s = p.read_text(encoding="utf-8", errors="ignore")

    if "CONTINUE_SHEET_CARD_RESTORE_V80" in s:
        print("ℹ️ V80 zaten var:", p.relative_to(ROOT))
        continue

    s = s.rstrip() + "\n" + PATCH + "\n"
    p.write_text(s, encoding="utf-8")
    print("✅ Yolcu kart modal tasarımı eklendi:", p.relative_to(ROOT))

print()
print("===== CACHE KIR =====")
for p in TPLS:
    b = p.with_name(p.name + f".bak-sheet-card-v80-cache-{STAMP}")
    shutil.copy2(p, b)

    s = p.read_text(encoding="utf-8", errors="ignore")
    s = re.sub(
        r"continue/continue_v76\.css'\) }}\?v=[^\"']+",
        "continue/continue_v76.css') }}?v=prototype-layout-v80",
        s
    )
    p.write_text(s, encoding="utf-8")
    print("✅ Cache:", p.relative_to(ROOT))

print()
print("✅ V80 tamam.")
