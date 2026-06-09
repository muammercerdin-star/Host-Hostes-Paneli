from pathlib import Path
from datetime import datetime
import shutil

STAMP = datetime.now().strftime("%Y%m%d-%H%M%S")

ROOTS = [
    Path("static/continue/continue_trip.css"),
    Path("android_app/app/src/main/python/static/continue/continue_trip.css"),
]

PARTS = [
    Path("static/continue/css_parts/71-seat-map-center-v48.css"),
    Path("android_app/app/src/main/python/static/continue/css_parts/71-seat-map-center-v48.css"),
]

IMPORT_LINE = '@import url("./css_parts/71-seat-map-center-v48.css");\n'

CSS = r'''/* CONTINUE_SEAT_MAP_CENTER_V48 */
/* Dış kaba çerçeveyi kaldır, seat map’i ortala, glow ile premium yap. */

#continueSeatMapOverlay,
.continue-seat-map-overlay,
[data-seatmap-overlay="continue"]{
  position: fixed !important;
  inset: 0 !important;
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
  padding: 16px 12px !important;
  background: rgba(2, 8, 23, 0.42) !important;
  backdrop-filter: blur(10px) saturate(120%) !important;
  -webkit-backdrop-filter: blur(10px) saturate(120%) !important;
  z-index: 9999 !important;
}

#continueSeatMapSheet,
.continue-seat-map-sheet,
[data-seatmap-sheet="continue"]{
  width: min(94vw, 680px) !important;
  max-width: 680px !important;
  height: min(90vh, 980px) !important;
  margin: auto !important;
  padding: 0 !important;
  border: none !important;
  outline: none !important;
  background: transparent !important;
  box-shadow: none !important;
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
  overflow: visible !important;
}

#continueSeatMapSheet::before,
#continueSeatMapSheet::after,
.continue-seat-map-sheet::before,
.continue-seat-map-sheet::after,
[data-seatmap-sheet="continue"]::before,
[data-seatmap-sheet="continue"]::after{
  content: none !important;
  display: none !important;
}

/* Asıl oturan panel */
#continueSeatMapBoard,
.continue-seat-map-board,
[data-seatmap-board="continue"],
#continueSeatMapSheet .deck-wrap,
.continue-seat-map-sheet .deck-wrap,
[data-seatmap-sheet="continue"] .deck-wrap{
  width: min(88vw, 620px) !important;
  max-width: 620px !important;
  height: min(84vh, 900px) !important;
  margin: 0 auto !important;
  padding: 20px 14px 24px !important;
  border-radius: 28px !important;
  border: none !important;
  background:
    radial-gradient(circle at 18% 24%, rgba(59,130,246,.12), transparent 28%),
    radial-gradient(circle at 82% 12%, rgba(244,63,94,.10), transparent 26%),
    linear-gradient(180deg, rgba(8,20,48,.92), rgba(3,10,28,.95)) !important;
  box-shadow:
    0 20px 60px rgba(0,0,0,.50),
    0 0 30px rgba(59,130,246,.10),
    0 0 48px rgba(244,63,94,.08),
    inset 0 1px 0 rgba(255,255,255,.08) !important;
  overflow: hidden !important;
  position: relative !important;
}

/* Tutma çizgisi daha zarif */
#continueSeatMapSheet .sheet-handle,
.continue-seat-map-sheet .sheet-handle,
[data-seatmap-sheet="continue"] .sheet-handle,
#continueSeatMapBoard .sheet-handle,
.continue-seat-map-board .sheet-handle{
  width: 120px !important;
  height: 10px !important;
  border-radius: 999px !important;
  margin: 2px auto 12px auto !important;
  background: linear-gradient(180deg, rgba(255,255,255,.34), rgba(255,255,255,.16)) !important;
  box-shadow:
    inset 0 1px 1px rgba(255,255,255,.22),
    0 0 12px rgba(255,255,255,.08) !important;
}

/* Kapatma butonu daha yumuşak */
#continueSeatMapSheet .sheet-close,
.continue-seat-map-sheet .sheet-close,
#continueSeatMapClose,
.continue-seat-map-close{
  position: absolute !important;
  top: 16px !important;
  right: 16px !important;
  width: 60px !important;
  height: 60px !important;
  border-radius: 22px !important;
  border: 1px solid rgba(255,255,255,.12) !important;
  background: linear-gradient(180deg, rgba(13,24,52,.88), rgba(9,17,36,.78)) !important;
  box-shadow:
    0 10px 30px rgba(0,0,0,.25),
    inset 0 1px 0 rgba(255,255,255,.08) !important;
  backdrop-filter: blur(8px) !important;
  -webkit-backdrop-filter: blur(8px) !important;
}

/* Deck ortalama */
#continueSeatMapBoard .deck,
.continue-seat-map-board .deck,
#continueSeatMapSheet .deck,
.continue-seat-map-sheet .deck{
  margin-left: auto !important;
  margin-right: auto !important;
}

/* Koridoru görünür yap */
.corridor,
.koridor,
.deck-corridor,
.seat-corridor,
[class*="corridor"],
[class*="koridor"]{
  opacity: .34 !important;
  color: rgba(197,213,255,.38) !important;
  text-shadow: 0 0 12px rgba(96,165,250,.10) !important;
  z-index: 2 !important;
}

.corridor::before,
.corridor::after,
.koridor::before,
.koridor::after,
.deck-corridor::before,
.deck-corridor::after,
.seat-corridor::before,
.seat-corridor::after,
[class*="corridor"]::before,
[class*="corridor"]::after,
[class*="koridor"]::before,
[class*="koridor"]::after{
  opacity: .28 !important;
}

/* Seat kartlar dursun ama board daha ferah olsun */
#continueSeatMapBoard .seat,
.continue-seat-map-board .seat,
#continueSeatMapSheet .seat,
.continue-seat-map-sheet .seat{
  transform: translateZ(0);
}

/* Küçük ekranlarda sıkışmayı azalt */
@media (max-width: 480px){
  #continueSeatMapSheet,
  .continue-seat-map-sheet,
  [data-seatmap-sheet="continue"]{
    width: 96vw !important;
    height: 92vh !important;
  }

  #continueSeatMapBoard,
  .continue-seat-map-board,
  [data-seatmap-board="continue"],
  #continueSeatMapSheet .deck-wrap,
  .continue-seat-map-sheet .deck-wrap{
    width: 92vw !important;
    height: 86vh !important;
    border-radius: 24px !important;
    padding: 18px 10px 20px !important;
  }

  #continueSeatMapSheet .sheet-close,
  .continue-seat-map-sheet .sheet-close,
  #continueSeatMapClose,
  .continue-seat-map-close{
    top: 14px !important;
    right: 14px !important;
    width: 56px !important;
    height: 56px !important;
    border-radius: 20px !important;
  }
}
'''

def backup(path: Path):
    if path.exists():
        bak = path.with_name(path.name + f".bak-v48-{STAMP}")
        shutil.copy2(path, bak)
        print("YEDEK:", bak)

def ensure_import(css_file: Path):
    if not css_file.exists():
        print("EKSİK:", css_file)
        return
    backup(css_file)
    txt = css_file.read_text(encoding="utf-8", errors="ignore")
    if IMPORT_LINE not in txt:
        txt = txt.rstrip() + "\n" + IMPORT_LINE
        css_file.write_text(txt, encoding="utf-8")
        print("IMPORT EKLENDİ:", css_file)
    else:
        print("IMPORT ZATEN VAR:", css_file)

def write_part(part_file: Path):
    part_file.parent.mkdir(parents=True, exist_ok=True)
    if part_file.exists():
        backup(part_file)
    part_file.write_text(CSS, encoding="utf-8")
    print("CSS YAZILDI:", part_file)

print("===== CONTINUE SEAT MAP CENTER V48 =====")

for p in PARTS:
    write_part(p)

for p in ROOTS:
    ensure_import(p)

print()
print("✅ V48 override hazır.")
print("Not: Bu script commit/push yapmaz. Sadece yama uygular.")
