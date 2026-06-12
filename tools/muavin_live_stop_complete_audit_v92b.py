from pathlib import Path
import sqlite3
import re

ROOT = Path(".").resolve()
OUT_DIR = Path("/sdcard/Download/MuavinAsistani")
OUT_DIR.mkdir(parents=True, exist_ok=True)
OUT = OUT_DIR / "v92b-live-stop-complete-audit.txt"

KEYS = [
    "live-stop-complete",
    "live_stop_complete",
    "completeStop",
    "complete_stop",
    "api/live-stop",
    "passedStops",
    "live_stop",
    "offload",
    "bagaj",
    "bag_count",
    "emanet",
    "consignment",
    "cargo",
]

SKIP_DIRS = {
    ".git", "__pycache__", ".gradle", "build", ".idea",
    "node_modules", ".venv", "venv"
}

def should_skip(p: Path):
    return any(part in SKIP_DIRS for part in p.parts)

def read_text(p: Path):
    return p.read_text(encoding="utf-8", errors="ignore")

def add(lines, s=""):
    lines.append(str(s))

def context(lines, path, line_no, around=55):
    txt = read_text(path).splitlines()
    start = max(1, line_no - around)
    end = min(len(txt), line_no + around)
    add(lines, f"\n--- {path.relative_to(ROOT)}:{start}-{end} ---")
    for i in range(start, end + 1):
        add(lines, f"{i:5}: {txt[i-1]}")

def main():
    lines = []
    add(lines, "===== V92B LIVE STOP COMPLETE BACKEND AUDIT =====")
    add(lines, f"ROOT: {ROOT}")

    py_files = [
        p for p in ROOT.rglob("*.py")
        if not should_skip(p)
        and "site-packages" not in str(p)
    ]

    js_html_files = [
        p for ext in ("*.js", "*.html")
        for p in ROOT.rglob(ext)
        if not should_skip(p)
        and "android_app/app/build" not in str(p)
    ]

    add(lines, "\n===== 1) PYTHON ROUTE / BACKEND İZLERİ =====")
    hit_count = 0
    route_hits = []

    for p in py_files:
        txt = read_text(p)
        for idx, line in enumerate(txt.splitlines(), 1):
            if any(k.lower() in line.lower() for k in KEYS):
                add(lines, f"{p.relative_to(ROOT)}:{idx}: {line[:240]}")
                hit_count += 1
                if "live-stop-complete" in line or "complete" in line.lower():
                    route_hits.append((p, idx))

    if hit_count == 0:
        add(lines, "⚠️ Backend iz bulunamadı.")

    add(lines, "\n===== 2) ROUTE CONTEXT =====")
    if route_hits:
        seen = set()
        for p, idx in route_hits[:12]:
            key = (str(p), idx)
            if key in seen:
                continue
            seen.add(key)
            context(lines, p, idx, around=70)
    else:
        add(lines, "⚠️ /api/live-stop-complete context bulunamadı.")

    add(lines, "\n===== 3) FRONTEND TAMAMLA / CANLI DURAK İZLERİ =====")
    f_hits = 0
    for p in js_html_files:
        txt = read_text(p)
        for idx, line in enumerate(txt.splitlines(), 1):
            low = line.lower()
            if (
                "live-stop-complete" in low
                or "sheetsummarycomplete" in low
                or "tamamla" in low
                or "completeStopFromSummary".lower() in low
                or "liveCurrentStopName".lower() in low
                or "AndroidLockVoice".lower() in low
                or "updateTargetV87".lower() in low
            ):
                add(lines, f"{p.relative_to(ROOT)}:{idx}: {line[:240]}")
                f_hits += 1

    if f_hits == 0:
        add(lines, "⚠️ Frontend iz bulunamadı.")

    add(lines, "\n===== 4) DB ŞEMA HARİTASI =====")
    db = ROOT / "db.sqlite3"
    if not db.exists():
        add(lines, "❌ db.sqlite3 yok")
    else:
        con = sqlite3.connect(db)
        con.row_factory = sqlite3.Row
        cur = con.cursor()

        tables = [r[0] for r in cur.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name").fetchall()]
        add(lines, "Tablolar:")
        for t in tables:
            add(lines, f"  - {t}")

        important = []
        for t in tables:
            cols = cur.execute(f"PRAGMA table_info({t})").fetchall()
            col_names = [c[1] for c in cols]
            joined = (t + " " + " ".join(col_names)).lower()
            if any(k in joined for k in [
                "passenger", "yolcu", "seat", "koltuk",
                "bag", "bagaj", "luggage",
                "emanet", "cargo", "consignment",
                "stop", "durak", "trip", "sefer", "live"
            ]):
                important.append(t)

        add(lines, "\nÖnemli görünen tablolar ve kolonlar:")
        for t in important:
            add(lines, f"\n--- TABLE {t} ---")
            cols = cur.execute(f"PRAGMA table_info({t})").fetchall()
            for c in cols:
                add(lines, f"  {c[1]} | {c[2]} | pk={c[5]} | default={c[4]}")
            try:
                count = cur.execute(f"SELECT COUNT(*) FROM {t}").fetchone()[0]
                add(lines, f"  ROW COUNT: {count}")
            except Exception as e:
                add(lines, f"  COUNT ERROR: {e}")

        add(lines, "\n===== 5) ORTAHAN / BELENYAKA DB ÖRNEKLERİ =====")
        for t in important:
            cols = cur.execute(f"PRAGMA table_info({t})").fetchall()
            text_cols = [c[1] for c in cols if "CHAR" in str(c[2]).upper() or "TEXT" in str(c[2]).upper() or c[2] == ""]
            if not text_cols:
                continue

            where = " OR ".join([f"{c} LIKE ?" for c in text_cols])
            params = []
            for _ in text_cols:
                params.append("%Ortahan%")

            try:
                rows = cur.execute(f"SELECT * FROM {t} WHERE {where} LIMIT 8", params).fetchall()
            except Exception:
                continue

            if rows:
                add(lines, f"\n--- {t} içinde Ortahan örnekleri ---")
                for r in rows:
                    add(lines, dict(r))

            params = []
            for _ in text_cols:
                params.append("%Belenyaka%")

            try:
                rows = cur.execute(f"SELECT * FROM {t} WHERE {where} LIMIT 8", params).fetchall()
            except Exception:
                continue

            if rows:
                add(lines, f"\n--- {t} içinde Belenyaka örnekleri ---")
                for r in rows:
                    add(lines, dict(r))

        con.close()

    add(lines, "\n===== 6) KARAR İÇİN BAKILACAKLAR =====")
    add(lines, "1. /api/live-stop-complete hangi Python dosyasında?")
    add(lines, "2. Yolcu tablosunda 'indi/tamamlandı' gibi kolon var mı?")
    add(lines, "3. Bagaj ve emanet ayrı tablo mu, yolcu satırında mı?")
    add(lines, "4. Tamamla sonrası backend live_stop'u sıradaki durağa çekiyor mu?")
    add(lines, "5. Android servise yeni durak bilgisi hangi JS/bridge ile gidiyor?")

    text = "\n".join(lines)
    OUT.write_text(text, encoding="utf-8")
    print(text)
    print()
    print(f"✅ Rapor yazıldı: {OUT}")

if __name__ == "__main__":
    main()
