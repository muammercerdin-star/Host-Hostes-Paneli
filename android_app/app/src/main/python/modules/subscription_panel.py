import os
from datetime import datetime, timedelta

from flask import render_template, request, redirect, url_for, jsonify, abort


TRIAL_DAYS = 30

PLAN_LEVELS = {
    "": 0,
    "Deneme": 2,      # Deneme süresinde Pro özellikleri açık
    "Standart": 1,
    "Pro": 2,
    "Sınırsız": 3,
}

FEATURE_RULES = [
    ("/sefer-raporu-son", "Pro", "Gelişmiş sefer raporları"),
    ("/api/report-archive", "Pro", "Rapor arşivi API"),
    ("/ayarlar/yedekleme/geri-yukle", "Pro", "Yedekten geri yükleme"),
]

GOOGLE_PLAY_PRODUCT_TO_PLAN = {
    "standart_monthly": "Standart",
    "pro_monthly": "Pro",
    "unlimited_monthly": "Sınırsız",
}


def register_subscription_routes(app, deps):
    settings_get = deps["settings_get"]
    settings_set = deps["settings_set"]

    def parse_dt_safe(value):
        try:
            return datetime.fromisoformat(str(value))
        except Exception:
            return None

    def format_dt_tr(value):
        dt = parse_dt_safe(value)
        if not dt:
            return value or "-"
        return dt.strftime("%d.%m.%Y %H:%M")

    def subscription_defaults():
        now = datetime.now()
        ends = now + timedelta(days=TRIAL_DAYS)

        return {
            "subscription_status": "trial",
            "trial_started_at": now.isoformat(timespec="seconds"),
            "trial_ends_at": ends.isoformat(timespec="seconds"),
            "subscription_plan": "Deneme",
            "payment_method_added": "0",
            "subscription_started_at": "",
            "subscription_ends_at": "",
            "last_payment_at": "",
        }

    def ensure_subscription_state():
        status = settings_get("subscription_status", "")

        if status:
            return

        data = subscription_defaults()
        for k, v in data.items():
            settings_set(k, v)

    def get_subscription_info():
        ensure_subscription_state()

        status = settings_get("subscription_status", "trial") or "trial"
        trial_started_at = settings_get("trial_started_at", "") or ""
        trial_ends_at = settings_get("trial_ends_at", "") or ""
        plan = settings_get("subscription_plan", "Deneme") or "Deneme"
        payment_method_added = settings_get("payment_method_added", "0") or "0"
        subscription_started_at = settings_get("subscription_started_at", "") or ""
        last_payment_at = settings_get("last_payment_at", "") or ""

        now = datetime.now()
        end_dt = parse_dt_safe(trial_ends_at)

        days_left = 0
        expired = False

        if status == "trial" and end_dt:
            diff = end_dt - now
            days_left = max(0, diff.days + (1 if diff.seconds > 0 else 0))
            expired = now > end_dt

        if status == "active":
            expired = False
            days_left = None

        if status in {"past_due", "canceled", "expired"}:
            expired = True

        return {
            "status": status,
            "plan": plan,
            "trial_started_at": trial_started_at,
            "trial_ends_at": trial_ends_at,
            "trial_started_text": format_dt_tr(trial_started_at),
            "trial_ends_text": format_dt_tr(trial_ends_at),
            "payment_method_added": payment_method_added == "1",
            "subscription_started_at": subscription_started_at,
            "subscription_started_text": format_dt_tr(subscription_started_at),
            "last_payment_at": last_payment_at,
            "last_payment_text": format_dt_tr(last_payment_at),
            "days_left": days_left,
            "expired": expired,
        }

    def subscription_allows_access():
        info = get_subscription_info()

        if info["status"] == "active":
            return True

        if info["status"] == "trial" and not info["expired"]:
            return True

        return False

    def start_trial_if_missing():
        ensure_subscription_state()

    def activate_subscription_manually(plan="Standart"):
        settings_set("subscription_status", "active")
        settings_set("subscription_plan", plan or "Standart")
        settings_set("payment_method_added", "1")
        settings_set("subscription_started_at", datetime.now().isoformat(timespec="seconds"))
        settings_set("last_payment_at", datetime.now().isoformat(timespec="seconds"))

    def force_expire_trial_for_test():
        settings_set("subscription_status", "expired")
        settings_set("trial_ends_at", (datetime.now() - timedelta(minutes=1)).isoformat(timespec="seconds"))

    def subscription_dev_mode():
        try:
            return os.getenv("SHOW_TEST_CONTROLS", "").strip().lower() in {"1", "true", "yes", "on"}
        except Exception:
            return False

    def get_effective_plan():
        info = get_subscription_info()

        if info.get("status") == "trial" and not info.get("expired"):
            return "Deneme"

        if info.get("status") == "active":
            return info.get("plan") or "Standart"

        return ""

    def plan_level(plan):
        return PLAN_LEVELS.get(plan or "", 0)

    def plan_allows(required_plan):
        current = get_effective_plan()
        return plan_level(current) >= plan_level(required_plan)

    def find_feature_rule_for_path(path):
        path = path or ""
        for prefix, required_plan, feature_name in FEATURE_RULES:
            if path.startswith(prefix):
                return {
                    "prefix": prefix,
                    "required_plan": required_plan,
                    "feature_name": feature_name,
                }
        return None

    def google_play_plan_from_product(product_id: str) -> str:
        product_id = (product_id or "").strip()
        return GOOGLE_PLAY_PRODUCT_TO_PLAN.get(product_id, "")

    def ensure_package_requests_table():
        db = deps["get_db"]()
        db.execute("""
            CREATE TABLE IF NOT EXISTS package_requests(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                requested_plan TEXT NOT NULL,
                current_plan TEXT,
                subscription_status TEXT,
                note TEXT,
                user_agent TEXT,
                created_at TEXT NOT NULL,
                is_done INTEGER NOT NULL DEFAULT 0
            )
        """)
        db.commit()

    @app.context_processor
    def inject_subscription_info():
        try:
            return {"subscription_info": get_subscription_info()}
        except Exception:
            return {"subscription_info": None}

    def package_required_page():
        feature = (request.args.get("feature") or "Bu özellik").strip()
        required = (request.args.get("required") or "Pro").strip()
        current = get_effective_plan() or "Yok"

        return render_template(
            "package_required.html",
            feature=feature,
            required=required,
            current=current,
        )

    def settings_subscription_page():
        msg = ""
        error = ""

        if request.method == "POST":
            action = (request.form.get("action") or "").strip()

            if action in {"activate_manual", "expire_test", "restart_trial"} and not subscription_dev_mode():
                error = "Bu test işlemi müşteri sürümünde kapalıdır."

            elif action == "activate_manual":
                activate_subscription_manually(request.form.get("plan") or "Standart")
                msg = "Abonelik manuel olarak aktif edildi. Ödeme sistemi bağlanınca bu işlem otomatik olacak."

            elif action == "expire_test":
                force_expire_trial_for_test()
                msg = "Test için deneme süresi bitmiş hale getirildi."

            elif action == "restart_trial":
                data = subscription_defaults()
                for k, v in data.items():
                    settings_set(k, v)
                msg = "Deneme süresi yeniden başlatıldı."

            else:
                error = "Geçersiz işlem."

        upgrade_required = (request.args.get("required") or "").strip()
        upgrade_feature = (request.args.get("feature") or "").strip()

        return render_template(
            "settings_subscription.html",
            info=get_subscription_info(),
            msg=msg,
            error=error,
            dev_mode=subscription_dev_mode(),
            upgrade_required=upgrade_required,
            upgrade_feature=upgrade_feature,
        )

    def subscription_required_page():
        return render_template("subscription_required.html", info=get_subscription_info())

    def settings_page():
        return render_template("settings.html")

    def api_package_request():
        if not subscription_dev_mode():
            return jsonify({
                "ok": False,
                "error": "Paket talebi müşteri sürümünde kapalıdır. Satın alma Google Play üzerinden yapılacaktır."
            }), 403

        ensure_package_requests_table()

        payload = request.get_json(silent=True) or {}
        requested_plan = (
            request.form.get("plan")
            or payload.get("plan")
            or ""
        ).strip()

        if requested_plan not in {"Standart", "Pro", "Sınırsız"}:
            return jsonify({"ok": False, "error": "Geçersiz paket seçimi."}), 400

        info = get_subscription_info()
        current_plan = get_effective_plan() or info.get("plan") or ""
        status = info.get("status") or ""

        note = f"{requested_plan} paketi için talep oluşturuldu."

        db = deps["get_db"]()
        db.execute(
            """
            INSERT INTO package_requests(
                requested_plan,
                current_plan,
                subscription_status,
                note,
                user_agent,
                created_at,
                is_done
            )
            VALUES(?,?,?,?,?,?,0)
            """,
            (
                requested_plan,
                current_plan,
                status,
                note,
                request.headers.get("User-Agent", ""),
                datetime.now().isoformat(timespec="seconds"),
            ),
        )
        db.commit()

        return jsonify({
            "ok": True,
            "message": f"{requested_plan} paket talebiniz kaydedildi."
        })

    def settings_package_requests_page():
        if not subscription_dev_mode():
            abort(404)

        ensure_package_requests_table()

        rows = deps["get_db"]().execute(
            """
            SELECT *
            FROM package_requests
            ORDER BY id DESC
            LIMIT 100
            """
        ).fetchall()

        return render_template("settings_package_requests.html", rows=rows)

    def settings_package_request_done(req_id):
        if not subscription_dev_mode():
            abort(404)

        ensure_package_requests_table()

        db = deps["get_db"]()
        db.execute(
            "UPDATE package_requests SET is_done=1 WHERE id=?",
            (req_id,),
        )
        db.commit()

        return redirect(url_for("settings_package_requests_page"))

    def api_google_play_purchase_success():
        payload = request.get_json(silent=True) or {}

        product_id = (
            request.form.get("product_id")
            or payload.get("product_id")
            or ""
        ).strip()

        purchase_token = (
            request.form.get("purchase_token")
            or payload.get("purchase_token")
            or ""
        ).strip()

        plan = google_play_plan_from_product(product_id)

        if not plan:
            return jsonify({
                "ok": False,
                "error": "Geçersiz Google Play ürün kodu.",
                "product_id": product_id,
            }), 400

        # Şimdilik yerel aktivasyon.
        # Gerçek Play Store sürümünde burada token doğrulama yapılmalı.
        activate_subscription_manually(plan)

        try:
            settings_set("google_play_product_id", product_id)
            settings_set("google_play_purchase_token", purchase_token)
            settings_set("google_play_last_purchase_at", datetime.now().isoformat(timespec="seconds"))
        except Exception:
            pass

        return jsonify({
            "ok": True,
            "plan": plan,
            "product_id": product_id,
            "message": f"{plan} paketi Google Play satın alma sonrası aktif edildi.",
        })

    def api_google_play_purchase_cancelled():
        payload = request.get_json(silent=True) or {}

        product_id = (
            request.form.get("product_id")
            or payload.get("product_id")
            or ""
        ).strip()

        try:
            settings_set("google_play_last_cancelled_product_id", product_id)
            settings_set("google_play_last_cancelled_at", datetime.now().isoformat(timespec="seconds"))
        except Exception:
            pass

        return jsonify({
            "ok": True,
            "message": "Satın alma iptal bilgisi kaydedildi.",
        })

    app.add_url_rule("/paket-gerekli", endpoint="package_required_page", view_func=package_required_page, methods=["GET"])
    app.add_url_rule("/ayarlar/abonelik", endpoint="settings_subscription_page", view_func=settings_subscription_page, methods=["GET", "POST"])
    app.add_url_rule("/abonelik-gerekli", endpoint="subscription_required_page", view_func=subscription_required_page, methods=["GET"])
    app.add_url_rule("/ayarlar", endpoint="settings_page", view_func=settings_page, methods=["GET"])

    app.add_url_rule("/api/package-request", endpoint="api_package_request", view_func=api_package_request, methods=["POST"])
    app.add_url_rule("/ayarlar/paket-talepleri", endpoint="settings_package_requests_page", view_func=settings_package_requests_page, methods=["GET"])
    app.add_url_rule("/ayarlar/paket-talepleri/<int:req_id>/tamamla", endpoint="settings_package_request_done", view_func=settings_package_request_done, methods=["POST"])

    app.add_url_rule("/api/google-play/purchase-success", endpoint="api_google_play_purchase_success", view_func=api_google_play_purchase_success, methods=["POST"])
    app.add_url_rule("/api/google-play/purchase-cancelled", endpoint="api_google_play_purchase_cancelled", view_func=api_google_play_purchase_cancelled, methods=["POST"])

    return {
        "parse_dt_safe": parse_dt_safe,
        "format_dt_tr": format_dt_tr,
        "subscription_defaults": subscription_defaults,
        "ensure_subscription_state": ensure_subscription_state,
        "get_subscription_info": get_subscription_info,
        "subscription_allows_access": subscription_allows_access,
        "start_trial_if_missing": start_trial_if_missing,
        "activate_subscription_manually": activate_subscription_manually,
        "force_expire_trial_for_test": force_expire_trial_for_test,
        "subscription_dev_mode": subscription_dev_mode,
        "get_effective_plan": get_effective_plan,
        "plan_level": plan_level,
        "plan_allows": plan_allows,
        "find_feature_rule_for_path": find_feature_rule_for_path,
        "google_play_plan_from_product": google_play_plan_from_product,
    }
