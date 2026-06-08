from pathlib import Path
from datetime import datetime
import re
import hashlib

ROOT = Path(".").resolve()
REPORTS = ROOT / "reports"
REPORTS.mkdir(exist_ok=True)

TS = datetime.now().strftime("%Y%m%d-%H%M%S")
OUT = REPORTS / f"muavin_patch_risk_matrix_v11_{TS}.md"

WEB_TEMPLATE = ROOT / "templates/seats.html"
ANDROID_TEMPLATE = ROOT / "android_app/app/src/main/python/templates/seats.html"

ROOTS = {
    "WEB": ROOT,
    "ANDROID": ROOT / "android_app/app/src/main/python",
}

CRITICAL_PATTERNS = {
    "SAVE_DIRECT": [
        "btnSeatSave", "saveSeat", "currentSeat", "/api/seat",
        "seat_no", "openSeat", "closeSeat"
    ],
    "MODAL_DIRECT": [
        "seatModal", "seatBackdrop", "modal", "backdrop",
        "modal-actions", "sheet-modal"
    ],
    "EVENT_RISK": [
        "addEventListener", "onclick", "click", "touchstart",
        "touchend", "preventDefault", "stopPropagation",
        "stopImmediatePropagation"
    ],
    "CSS_BLOCK_RISK": [
        "pointer-events", "z-index", "position:fixed", "position: fixed",
        "display:none", "display: none", "visibility", "opacity",
        "transform", "overflow", "inset:", "bottom:", "top:"
    ],
    "SEAT_STATE": [
        ".seat", "seat-", "dataset.seat", "assigned", "has-stop",
        "multi-picked", "querySelector", "querySelectorAll"
    ],
    "STORAGE_STATE": [
        "localStorage", "sessionStorage", "TRIP_KEY", "boardsMap",
        "stopsMap", "stopFlow", "liveStop", "passedStops"
    ],
    "ASYNC_TIMING": [
        "setTimeout", "setInterval", "requestAnimationFrame",
        "DOMContentLoaded", "load", "resize", "orientationchange",
        "MutationObserver"
    ],
}

def read(p):
    return p.read_text(encoding="utf-8", errors="ignore") if p.exists() else ""

def sha(p):
    if not p.exists() or not p.is_file():
        return ""
    return hashlib.sha256(p.read_bytes()).hexdigest()[:12]

def line_count(p):
    return len(read(p).splitlines()) if p.exists() else 0

def mtime(p):
    if not p.exists():
        return ""
    return datetime.fromtimestamp(p.stat().st_mtime).strftime("%Y-%m-%d %H:%M:%S")

def extract_static_patch_links(template_path):
    s = read(template_path)
    found = []
    for i, line in enumerate(s.splitlines(), 1):
        for m in re.finditer(r'''(?:href|src)=["'](/static/[^"']+)["']''', line):
            raw = m.group(1)
            clean = raw.split("?", 1)[0].lstrip("/")
            if "/patches/" in clean:
                found.append((i, raw, clean))
    return found

def classify_file(path):
    s = read(path)
    lines = s.splitlines()
    counts = {}
    hits = []
    for cat, pats in CRITICAL_PATTERNS.items():
        c = 0
        for ln, line in enumerate(lines, 1):
            lowline = line.lower()
            for pat in pats:
                if pat.lower() in lowline:
                    c += 1
                    hits.append((cat, ln, line.strip()))
                    break
        counts[cat] = c

    score = 0
    score += counts["SAVE_DIRECT"] * 10
    score += counts["MODAL_DIRECT"] * 6
    score += counts["EVENT_RISK"] * 5
    score += counts["CSS_BLOCK_RISK"] * 4
    score += counts["SEAT_STATE"] * 5
    score += counts["STORAGE_STATE"] * 3
    score += counts["ASYNC_TIMING"] * 3

    ext = path.suffix.lower()

    if counts["SAVE_DIRECT"] or ("btnSeatSave" in s) or ("currentSeat" in s):
        level = "A-ÇOK KRİTİK"
    elif counts["MODAL_DIRECT"] and (counts["EVENT_RISK"] or counts["CSS_BLOCK_RISK"]):
        level = "B-KRİTİK"
    elif counts["EVENT_RISK"] or counts["CSS_BLOCK_RISK"] or counts["SEAT_STATE"]:
        level = "C-ORTA"
    else:
        level = "D-DÜŞÜK"

    return {
        "score": score,
        "level": level,
        "counts": counts,
        "hits": hits[:80],
        "ext": ext,
    }

rows = []
all_links = {}

for label, base in ROOTS.items():
    tpl = WEB_TEMPLATE if label == "WEB" else ANDROID_TEMPLATE
    links = extract_static_patch_links(tpl)
    all_links[label] = links
    for line_no, raw, rel in links:
        p = base / rel
        info = classify_file(p)
        rows.append({
            "root": label,
            "template_line": line_no,
            "raw": raw,
            "rel": rel,
            "path": p,
            "exists": p.exists(),
            **info
        })

# WEB unique risk order
web_unique = {}
for r in rows:
    if r["root"] != "WEB":
        continue
    web_unique[r["rel"]] = r

ordered = sorted(web_unique.values(), key=lambda r: (-r["score"], r["level"], r["rel"]))

md = []
md.append("# Muavin Asistanı Patch Risk Matrix V11")
md.append("")
md.append(f"- Tarih: `{TS}`")
md.append("- Bu rapor sadece tespittir. Dosya değiştirmez, silmez, devre dışı bırakmaz.")
md.append("")
md.append("## 1) Özet")
md.append("")
md.append("| Kök | Aktif patch çağrısı | Benzersiz patch |")
md.append("| --- | ---: | ---: |")
for label, links in all_links.items():
    md.append(f"| {label} | {len(links)} | {len(set(x[2] for x in links))} |")

md.append("")
md.append("## 2) WEB Risk Sıralaması")
md.append("")
md.append("| Sıra | Seviye | Skor | Dosya | Satır | Hash | Mtime | SAVE | MODAL | EVENT | CSS | SEAT | STORAGE | ASYNC |")
md.append("| ---: | --- | ---: | --- | ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |")
for idx, r in enumerate(ordered, 1):
    c = r["counts"]
    md.append(
        f"| {idx} | {r['level']} | {r['score']} | `{r['rel']}` | {line_count(r['path'])} | {sha(r['path'])} | {mtime(r['path'])} | "
        f"{c['SAVE_DIRECT']} | {c['MODAL_DIRECT']} | {c['EVENT_RISK']} | {c['CSS_BLOCK_RISK']} | {c['SEAT_STATE']} | {c['STORAGE_STATE']} | {c['ASYNC_TIMING']} |"
    )

md.append("")
md.append("## 3) WEB ↔ ANDROID Patch Hash Kontrolü")
md.append("")
md.append("| Dosya | WEB | ANDROID | Durum |")
md.append("| --- | --- | --- | --- |")
all_rels = sorted(set([x[2] for x in all_links.get("WEB", [])] + [x[2] for x in all_links.get("ANDROID", [])]))
for rel in all_rels:
    wp = ROOT / rel
    ap = ROOT / "android_app/app/src/main/python" / rel
    wh = sha(wp) if wp.exists() else "-"
    ah = sha(ap) if ap.exists() else "-"
    if wh == "-" and ah != "-":
        durum = "SADECE ANDROID"
    elif wh != "-" and ah == "-":
        durum = "SADECE WEB"
    elif wh == ah:
        durum = "AYNI"
    else:
        durum = "FARKLI"
    md.append(f"| `{rel}` | {wh} | {ah} | {durum} |")

md.append("")
md.append("## 4) Kritik Satır İzleri")
md.append("")
for r in ordered:
    md.append(f"### {r['level']} / Skor {r['score']} / `{r['rel']}`")
    md.append("")
    if not r["exists"]:
        md.append("_Dosya bulunamadı._")
        md.append("")
        continue
    if not r["hits"]:
        md.append("_Kritik iz bulunmadı._")
        md.append("")
        continue
    md.append("| Kategori | Satır | İçerik |")
    md.append("| --- | ---: | --- |")
    for cat, ln, content in r["hits"]:
        content = content.replace("|", "\\|")
        if len(content) > 180:
            content = content[:180] + "..."
        md.append(f"| {cat} | {ln} | `{content}` |")
    md.append("")

md.append("")
md.append("## 5) İlk Teknik Yorum")
md.append("")
md.append("- `A-ÇOK KRİTİK` çıkan dosyalar doğrudan koltuk kaydetme/currentSeat/openSeat/saveSeat akışına temas ediyor olabilir.")
md.append("- `B-KRİTİK` çıkan dosyalar modal, backdrop, z-index, pointer-events veya click davranışıyla Kaydet butonunu dolaylı bozabilir.")
md.append("- `C-ORTA` daha çok görsel veya etkileşim katmanı olabilir.")
md.append("- Bu rapordan sonra devre dışı bırakma değil, önce en yüksek skorlu 2-3 dosyanın içeriği okunmalı.")

OUT.write_text("\n".join(md), encoding="utf-8")

print("✅ Patch risk matrix V11 hazır:")
print(OUT)
print()
print("===== KISA ÖZET =====")
for r in ordered[:10]:
    print(f"{r['level']} | skor={r['score']} | {r['rel']}")
print()
print("Görmek için:")
print(f"sed -n '1,260p' {OUT}")
