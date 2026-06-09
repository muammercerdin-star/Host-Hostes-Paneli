from pathlib import Path
from datetime import datetime
import shutil
import subprocess

ROOT = Path(".").resolve()
STAMP = datetime.now().strftime("%Y%m%d-%H%M%S")

FILES = [
    ROOT / "modules/backup_panel.py",
    ROOT / "android_app/app/src/main/python/modules/backup_panel.py",
]

INIT_FILES = [
    ROOT / "modules/__init__.py",
    ROOT / "android_app/app/src/main/python/modules/__init__.py",
]

STUB = r'''# BACKUP_PANEL_SAFE_STUB_V50
"""
Muavin Asistanı backup_panel güvenli modülü.

Bu modül APK içinde eksik kaldığında Flask başlangıcını düşürmemek için
güvenli yedek olarak kullanılır.
"""

try:
    from flask import Blueprint, jsonify
except Exception:
    Blueprint = None
    jsonify = None


if Blueprint:
    backup_bp = Blueprint("backup_panel", __name__)

    @backup_bp.route("/backup-panel")
    def backup_panel_home():
        return jsonify({
            "ok": True,
            "module": "backup_panel",
            "status": "safe_stub",
            "message": "Backup panel güvenli modda."
        })
else:
    backup_bp = None


backup_panel_bp = backup_bp
bp = backup_bp
backup_panel = backup_bp


def register_backup_panel(app=None):
    try:
        if app is not None and backup_bp is not None:
            app.register_blueprint(backup_bp)
    except Exception:
        pass
    return app


def register_backup_routes(app=None):
    return register_backup_panel(app)


def init_backup_panel(app=None):
    return register_backup_panel(app)


def init_app(app=None):
    return register_backup_panel(app)


def setup_backup_panel(app=None):
    return register_backup_panel(app)


def _noop(*args, **kwargs):
    return None


def __getattr__(name):
    # from modules.backup_panel import herhangi_bir_isim
    # şeklindeki importların APK'yı düşürmemesi için güvenli dönüş.
    return _noop
'''

print("===== MISSING BACKUP PANEL FIX V50 =====")
print("ROOT:", ROOT)

for init in INIT_FILES:
    init.parent.mkdir(parents=True, exist_ok=True)
    if not init.exists():
        init.write_text("", encoding="utf-8")
        print("✅ __init__.py oluşturuldu:", init.relative_to(ROOT))

# 1) Önce git içinden geri getirmeyi dene
for f in FILES:
    if not f.exists():
        try:
            subprocess.run(["git", "checkout", "HEAD", "--", str(f.relative_to(ROOT))], cwd=ROOT, check=False)
        except Exception:
            pass

# 2) Bir tarafta varsa diğer tarafa kopyala
web_file = FILES[0]
android_file = FILES[1]

if web_file.exists() and not android_file.exists():
    android_file.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(web_file, android_file)
    print("✅ Web backup_panel Android'e kopyalandı")

elif android_file.exists() and not web_file.exists():
    web_file.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(android_file, web_file)
    print("✅ Android backup_panel Web'e kopyalandı")

# 3) Hâlâ yoksa güvenli stub oluştur
for f in FILES:
    f.parent.mkdir(parents=True, exist_ok=True)

    if f.exists():
        txt = f.read_text(encoding="utf-8", errors="ignore")
        if "BACKUP_PANEL_SAFE_STUB_V50" in txt:
            print("ℹ️ Stub zaten var:", f.relative_to(ROOT))
        else:
            bak = f.with_name(f.name + f".bak-before-v50-{STAMP}")
            shutil.copy2(f, bak)
            print("📦 Mevcut dosya yedeklendi:", bak.relative_to(ROOT))
            print("✅ Mevcut backup_panel korunuyor:", f.relative_to(ROOT))
    else:
        f.write_text(STUB, encoding="utf-8")
        print("✅ Güvenli backup_panel oluşturuldu:", f.relative_to(ROOT))

print()
print("===== KONTROL =====")
for f in FILES + INIT_FILES:
    print(("✅ VAR " if f.exists() else "❌ YOK "), f.relative_to(ROOT))

print()
print("===== APP.PY IMPORT KONTROL =====")
for p in [ROOT / "app.py", ROOT / "android_app/app/src/main/python/app.py"]:
    if p.exists():
        hits = []
        for i, line in enumerate(p.read_text(encoding="utf-8", errors="ignore").splitlines(), 1):
            if "backup_panel" in line:
                hits.append(f"{i}: {line}")
        print(p.relative_to(ROOT), "backup_panel satırı:", len(hits))
        for h in hits[:20]:
            print(" ", h)

print()
print("✅ V50 onarım tamam.")
