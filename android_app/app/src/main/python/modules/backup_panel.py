import shutil
import zipfile
from pathlib import Path
from datetime import datetime

from flask import (
    render_template,
    request,
    redirect,
    url_for,
    send_file,
    abort,
    g,
)
from werkzeug.utils import secure_filename


def register_backup_routes(app, deps=None):
    deps = deps or {}

    def backup_dir_path():
        p = Path(app.root_path) / "storage" / "backups"
        p.mkdir(parents=True, exist_ok=True)
        return p

    def safe_backup_filename(name):
        name = (name or "").strip()
        if not name:
            return ""
        name = Path(name).name
        if not name.startswith("yedek_"):
            return ""
        if not name.endswith(".zip"):
            return ""
        return name

    def file_size_text(size):
        try:
            size = float(size)
        except Exception:
            return "0 B"

        units = ["B", "KB", "MB", "GB"]
        i = 0
        while size >= 1024 and i < len(units) - 1:
            size /= 1024
            i += 1

        if i == 0:
            return f"{int(size)} {units[i]}"
        return f"{size:.1f} {units[i]}"

    def list_backup_files():
        folder = backup_dir_path()
        items = []

        for f in sorted(folder.glob("yedek_*.zip"), key=lambda x: x.stat().st_mtime, reverse=True):
            st = f.stat()
            items.append({
                "name": f.name,
                "size": file_size_text(st.st_size),
                "mtime": datetime.fromtimestamp(st.st_mtime).strftime("%Y-%m-%d %H:%M:%S"),
            })

        return items

    def add_file_to_zip(zf, file_path, arcname):
        file_path = Path(file_path)
        if file_path.exists() and file_path.is_file():
            zf.write(str(file_path), arcname)

    def add_folder_to_zip(zf, folder_path, arc_prefix):
        folder_path = Path(folder_path)
        if not folder_path.exists() or not folder_path.is_dir():
            return

        for item in folder_path.rglob("*"):
            if item.is_file():
                rel = item.relative_to(folder_path)
                zf.write(str(item), str(Path(arc_prefix) / rel))

    def create_backup_zip():
        folder = backup_dir_path()
        now = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"yedek_{now}.zip"
        target = folder / filename

        root = Path(app.root_path)

        with zipfile.ZipFile(target, "w", zipfile.ZIP_DEFLATED) as zf:
            # Ana veritabanı
            add_file_to_zip(zf, root / "db.sqlite3", "db.sqlite3")

            # WAL modunda açık yazımlar için varsa yardımcı SQLite dosyaları
            add_file_to_zip(zf, root / "db.sqlite3-wal", "db.sqlite3-wal")
            add_file_to_zip(zf, root / "db.sqlite3-shm", "db.sqlite3-shm")

            # Sefer raporları
            add_folder_to_zip(zf, root / "storage" / "reports", "storage/reports")

            # Yüklenen profil fotoğrafları
            add_folder_to_zip(zf, root / "static" / "profile", "static/profile")

            # Uygulama içi yüklenen dosyalar/fotoğraflar
            add_folder_to_zip(zf, root / "uploads", "uploads")

            # Bilgi dosyası
            info = []
            info.append("Sarıkız Host/Hostes Paneli Yedek Dosyası")
            info.append(f"Oluşturma: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            info.append("")
            info.append("İçerik:")
            info.append("- db.sqlite3")
            info.append("- db.sqlite3-wal / db.sqlite3-shm varsa")
            info.append("- storage/reports")
            info.append("- static/profile")
            info.append("- uploads")
            zf.writestr("YEDEK_BILGI.txt", "\n".join(info))

        return filename

    def settings_backup_page():
        created = (request.args.get("created") or "").strip()
        deleted = (request.args.get("deleted") or "").strip()
        restored = (request.args.get("restored") or "").strip()
        emergency = (request.args.get("emergency") or "").strip()
        restore_error = (request.args.get("restore_error") or "").strip()
        items = list_backup_files()

        return render_template(
            "settings_backup.html",
            items=items,
            created=created,
            deleted=deleted,
            restored=restored,
            emergency=emergency,
            restore_error=restore_error,
        )

    def settings_backup_create():
        filename = create_backup_zip()
        return redirect(url_for("settings_backup_page", created=filename))

    def settings_backup_download(filename):
        filename = safe_backup_filename(filename)
        if not filename:
            abort(404)

        path = backup_dir_path() / filename
        if not path.exists():
            abort(404)

        return send_file(str(path), as_attachment=True, download_name=filename)

    def settings_backup_delete(filename):
        filename = safe_backup_filename(filename)
        if not filename:
            abort(404)

        path = backup_dir_path() / filename
        if path.exists():
            path.unlink()

        return redirect(url_for("settings_backup_page", deleted=filename))

    def restore_upload_dir_path():
        p = Path(app.root_path) / "storage" / "restore_uploads"
        p.mkdir(parents=True, exist_ok=True)
        return p

    def is_allowed_restore_member(name):
        name = (name or "").replace("\\", "/").strip()

        if not name or name.startswith("/") or name.startswith("../") or "/../" in name:
            return False

        allowed_exact = {"db.sqlite3", "db.sqlite3-wal", "db.sqlite3-shm", "YEDEK_BILGI.txt"}
        allowed_prefixes = (
            "storage/reports/",
            "static/profile/",
            "uploads/",
        )

        if name in allowed_exact:
            return True

        return any(name.startswith(prefix) for prefix in allowed_prefixes)

    def extract_restore_zip_safely(zip_path):
        zip_path = Path(zip_path)
        root = Path(app.root_path)
        temp_dir = root / "storage" / "restore_temp"

        if temp_dir.exists():
            shutil.rmtree(temp_dir)
        temp_dir.mkdir(parents=True, exist_ok=True)

        with zipfile.ZipFile(zip_path, "r") as zf:
            names = zf.namelist()

            if "db.sqlite3" not in names:
                raise ValueError("Bu yedek dosyasında db.sqlite3 bulunamadı.")

            for name in names:
                if name.endswith("/"):
                    continue

                if not is_allowed_restore_member(name):
                    continue

                target = temp_dir / name
                target.parent.mkdir(parents=True, exist_ok=True)

                with zf.open(name) as src, open(target, "wb") as dst:
                    shutil.copyfileobj(src, dst)

        return temp_dir

    def close_db_for_restore():
        # Açık SQLite bağlantısı varsa kapatmaya çalış
        try:
            db = getattr(g, "db", None)
            if db:
                db.close()
                g.db = None
        except Exception:
            pass

        try:
            db = getattr(g, "_database", None)
            if db:
                db.close()
                g._database = None
        except Exception:
            pass

    def restore_backup_from_zip(zip_path):
        root = Path(app.root_path)

        # Önce mevcut sistemi acil yedekle
        emergency_backup = create_backup_zip()

        temp_dir = extract_restore_zip_safely(zip_path)

        close_db_for_restore()

        # Veritabanı geri yükle
        src_db = temp_dir / "db.sqlite3"
        if src_db.exists():
            shutil.copy2(src_db, root / "db.sqlite3")

        # WAL yardımcı dosyaları varsa geri yükle
        for helper_name in ("db.sqlite3-wal", "db.sqlite3-shm"):
            src_helper = temp_dir / helper_name
            if src_helper.exists():
                shutil.copy2(src_helper, root / helper_name)

        # Raporlar geri yükle
        src_reports = temp_dir / "storage" / "reports"
        dst_reports = root / "storage" / "reports"
        if src_reports.exists():
            if dst_reports.exists():
                shutil.rmtree(dst_reports)
            dst_reports.parent.mkdir(parents=True, exist_ok=True)
            shutil.copytree(src_reports, dst_reports)

        # Profil fotoğrafları geri yükle
        src_profile = temp_dir / "static" / "profile"
        dst_profile = root / "static" / "profile"
        if src_profile.exists():
            if dst_profile.exists():
                shutil.rmtree(dst_profile)
            dst_profile.parent.mkdir(parents=True, exist_ok=True)
            shutil.copytree(src_profile, dst_profile)

        # Uploads geri yükle
        src_uploads = temp_dir / "uploads"
        dst_uploads = root / "uploads"
        if src_uploads.exists():
            if dst_uploads.exists():
                shutil.rmtree(dst_uploads)
            dst_uploads.parent.mkdir(parents=True, exist_ok=True)
            shutil.copytree(src_uploads, dst_uploads)

        try:
            shutil.rmtree(temp_dir)
        except Exception:
            pass

        return emergency_backup

    def settings_backup_restore():
        f = request.files.get("backup_file")

        if not f or not f.filename:
            return redirect(url_for("settings_backup_page", restore_error="Yedek dosyası seçilmedi."))

        filename = secure_filename(f.filename or "")

        if not filename.lower().endswith(".zip"):
            return redirect(url_for("settings_backup_page", restore_error="Sadece .zip yedek dosyası yüklenebilir."))

        upload_dir = restore_upload_dir_path()
        upload_path = upload_dir / f"restore_{datetime.now().strftime('%Y%m%d_%H%M%S')}_{filename}"
        f.save(str(upload_path))

        try:
            emergency = restore_backup_from_zip(upload_path)
        except zipfile.BadZipFile:
            try:
                upload_path.unlink()
            except Exception:
                pass
            return redirect(url_for("settings_backup_page", restore_error="Zip dosyası bozuk veya geçersiz."))
        except Exception as e:
            try:
                upload_path.unlink()
            except Exception:
                pass
            return redirect(url_for("settings_backup_page", restore_error=str(e)))

        try:
            upload_path.unlink()
        except Exception:
            pass

        return redirect(url_for(
            "settings_backup_page",
            restored=filename,
            emergency=emergency,
        ))

    app.add_url_rule("/ayarlar/yedekleme", endpoint="settings_backup_page", view_func=settings_backup_page, methods=["GET"])
    app.add_url_rule("/ayarlar/yedekleme/olustur", endpoint="settings_backup_create", view_func=settings_backup_create, methods=["POST"])
    app.add_url_rule("/ayarlar/yedekleme/indir/<filename>", endpoint="settings_backup_download", view_func=settings_backup_download, methods=["GET"])
    app.add_url_rule("/ayarlar/yedekleme/sil/<filename>", endpoint="settings_backup_delete", view_func=settings_backup_delete, methods=["POST"])
    app.add_url_rule("/ayarlar/yedekleme/geri-yukle", endpoint="settings_backup_restore", view_func=settings_backup_restore, methods=["POST"])

    # İleride başka modüller ihtiyaç duyarsa diye app'e bağla
    app.create_backup_zip = create_backup_zip
    app.restore_backup_from_zip = restore_backup_from_zip
