from pathlib import Path
from datetime import datetime
import shutil
import re

ROOT = Path(".").resolve()
STAMP = datetime.now().strftime("%Y%m%d-%H%M%S")

APP = ROOT / "app.py"
AND_APP = ROOT / "android_app/app/src/main/python/app.py"

print("===== V99N KOLTUK DETAY API PATCH =====")

if not APP.exists():
    raise SystemExit("❌ app.py yok")

for p in [APP, AND_APP]:
    if p.exists():
        bak = p.with_name(p.name + f".bak-v99n-seat-api-{STAMP}")
        shutil.copy2(p, bak)
        print("📦 backup:", bak)

s = APP.read_text(encoding="utf-8", errors="ignore")
old = s
changes = []

# api_live-seat-map SELECT alanlarına detay ekle
needle = """COALESCE(passenger_name,'') AS passenger_name,"""
add = """COALESCE(passenger_name,'') AS passenger_name,
               COALESCE(passenger_phone,'') AS passenger_phone,
               COALESCE(ticket_type,'') AS ticket_type,
               COALESCE(payment,'') AS payment,
               COALESCE(amount,0) AS amount,"""

if needle in s and "COALESCE(passenger_phone,'') AS passenger_phone" not in s[s.find("@app.route(\"/api/live-seat-map\")"):s.find("@app.route(\"/api/live-seat-destination\"", s.find("@app.route(\"/api/live-seat-map\")"))]:
    s = s.replace(needle, add, 1)
    changes.append("live-seat-map SELECT içine passenger_phone/ticket_type/payment/amount eklendi")
else:
    print("⚠️ SELECT alanları zaten ekli olabilir veya kalıp bulunamadı")

# occupied dict içine alanları ekle
needle2 = '''"passenger_name": r["passenger_name"] or "",'''
add2 = '''"passenger_name": r["passenger_name"] or "",
            "passenger_phone": r["passenger_phone"] or "",
            "ticket_type": r["ticket_type"] or "",
            "payment": r["payment"] or "",
            "amount": float(r["amount"] or 0),'''

start = s.find("@app.route(\"/api/live-seat-map\")")
end = s.find("@app.route(\"/api/live-seat-destination\"", start)
block = s[start:end] if start >= 0 and end > start else ""

if needle2 in block and '"ticket_type": r["ticket_type"] or ""' not in block:
    s = s[:start] + block.replace(needle2, add2, 1) + s[end:]
    changes.append("occupied koltuk JSON içine detay alanları eklendi")
else:
    print("⚠️ occupied JSON alanları zaten ekli olabilir veya kalıp bulunamadı")

# boş koltuk dict içine default alanlar ekle
needle3 = '''"passenger_name": "",'''
add3 = '''"passenger_name": "",
                    "passenger_phone": "",
                    "ticket_type": "",
                    "payment": "",
                    "amount": 0,'''

start = s.find("@app.route(\"/api/live-seat-map\")")
end = s.find("@app.route(\"/api/live-seat-destination\"", start)
block = s[start:end] if start >= 0 and end > start else ""

if needle3 in block and '"ticket_type": ""' not in block:
    s = s[:start] + block.replace(needle3, add3, 1) + s[end:]
    changes.append("boş koltuk JSON default detayları eklendi")
else:
    print("⚠️ boş koltuk JSON alanları zaten ekli olabilir veya kalıp bulunamadı")

if s == old:
    print("⚠️ app.py değişmedi")
else:
    APP.write_text(s, encoding="utf-8")
    print("✅ web app.py yazıldı")

    if AND_APP.parent.exists():
        shutil.copy2(APP, AND_APP)
        print("✅ android app.py senkronlandı")

print()
print("===== DEĞİŞİKLİKLER =====")
for c in changes:
    print("✅", c)

print()
print("===== KONTROL =====")
txt = APP.read_text(encoding="utf-8", errors="ignore")
area = txt[txt.find("@app.route(\"/api/live-seat-map\")"):txt.find("@app.route(\"/api/live-seat-destination\"", txt.find("@app.route(\"/api/live-seat-map\")"))]

for key in [
    "passenger_phone",
    "ticket_type",
    "payment",
    "amount",
]:
    print(("VAR  " if key in area else "YOK  ") + key)

print()
print("✅ V99N API patch bitti")
