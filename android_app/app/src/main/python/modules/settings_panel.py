from flask import render_template, request, redirect, url_for, session


def register_settings_routes(app, deps):
    admin_profile_exists = deps["admin_profile_exists"]
    verify_admin_password = deps["verify_admin_password"]
    issue_csrf = deps["issue_csrf"]
    get_csrf = deps["get_csrf"]

    reset_admin_owner = deps["reset_admin_owner"]
    verify_recovery_code = deps["verify_recovery_code"]
    get_recovery_code_hash = deps["get_recovery_code_hash"]
    make_recovery_code = deps["make_recovery_code"]
    set_recovery_code = deps["set_recovery_code"]
    settings_get = deps["settings_get"]

    set_admin_password = deps["set_admin_password"]
    get_admin_profile = deps["get_admin_profile"]
    save_admin_profile = deps["save_admin_profile"]
    save_profile_photo = deps["save_profile_photo"]

    start_trial_if_missing = deps["start_trial_if_missing"]

    def reset_user_page():
        if not admin_profile_exists():
            return redirect(url_for("setup_page"))

        error = ""

        if request.method == "POST":
            recovery_code = (request.form.get("recovery_code") or "").strip()

            if not verify_recovery_code(recovery_code):
                error = "Kurtarma kodu yanlış."
            else:
                reset_admin_owner()
                session.clear()
                return redirect(url_for("onboarding_page"))

        return render_template("user_reset.html", error=error, csrf_token=get_csrf())

    def login():
        if not admin_profile_exists():
            return redirect(url_for("setup_page"))

        if request.method == "POST":
            pwd = (request.form.get("password") or "").strip()

            if verify_admin_password(pwd):
                session["auth_ok"] = True
                issue_csrf()
                nxt = request.args.get("next") or url_for("index")
                return redirect(nxt)

            return render_template("login.html", error="Hatalı şifre", csrf_token=get_csrf())

        return render_template("login.html", csrf_token=get_csrf())

    def logout():
        session.clear()
        return redirect(url_for("login"))

    def settings_password_page():
        msg = ""
        error = ""

        if request.method == "POST":
            old_password = (request.form.get("old_password") or "").strip()
            new_password = (request.form.get("new_password") or "").strip()
            new_password2 = (request.form.get("new_password2") or "").strip()

            if not verify_admin_password(old_password):
                error = "Eski şifre yanlış."
            elif len(new_password) < 4:
                error = "Yeni şifre en az 4 karakter olmalı."
            elif new_password != new_password2:
                error = "Yeni şifreler birbiriyle aynı değil."
            else:
                ok, text = set_admin_password(new_password)
                if ok:
                    msg = text
                else:
                    error = text

        return render_template("settings_password.html", msg=msg, error=error)

    def settings_recovery_code_page():
        code = None
        msg = ""
        error = ""

        current_hash = get_recovery_code_hash()

        if request.method == "POST":
            action = (request.form.get("action") or "").strip()

            if action == "generate":
                code = make_recovery_code()
                set_recovery_code(code)
                msg = "Yeni kurtarma kodu oluşturuldu. Bu kodu güvenli bir yere not et."
            else:
                error = "Geçersiz işlem."

        elif not current_hash:
            code = make_recovery_code()
            set_recovery_code(code)
            msg = "İlk kurtarma kodun oluşturuldu. Bu kodu güvenli bir yere not et."

        updated_at = settings_get("recovery_code_updated_at", "")

        return render_template(
            "settings_recovery.html",
            code=code,
            msg=msg,
            error=error,
            updated_at=updated_at,
        )

    def forgot_password_page():
        msg = ""
        error = ""

        if request.method == "POST":
            recovery_code = (request.form.get("recovery_code") or "").strip()
            new_password = (request.form.get("new_password") or "").strip()
            new_password2 = (request.form.get("new_password2") or "").strip()

            if not verify_recovery_code(recovery_code):
                error = "Kurtarma kodu yanlış."
            elif len(new_password) < 4:
                error = "Yeni şifre en az 4 karakter olmalı."
            elif new_password != new_password2:
                error = "Yeni şifreler aynı değil."
            else:
                ok, text = set_admin_password(new_password)
                if ok:
                    session.clear()
                    msg = "Şifre sıfırlandı. Yeni şifrenle giriş yapabilirsin."
                else:
                    error = text

        return render_template("forgot_password.html", msg=msg, error=error)

    def setup_page():
        if request.method == "GET" and request.args.get("tanitim") != "1":
            return redirect(url_for("onboarding_page"))

        # Profil varsa kurulum ekranını tekrar açtırma
        if admin_profile_exists():
            return redirect(url_for("login"))

        error = ""

        if request.method == "POST":
            full_name = (request.form.get("full_name") or "").strip()
            phone = (request.form.get("phone") or "").strip()
            password = (request.form.get("password") or "").strip()
            password2 = (request.form.get("password2") or "").strip()

            if len(full_name) < 3:
                error = "Ad soyad en az 3 karakter olmalı."
            elif len(phone) < 10:
                error = "Cep telefonu eksik görünüyor."
            elif len(password) < 4:
                error = "Şifre en az 4 karakter olmalı."
            elif password != password2:
                error = "Şifreler aynı değil."
            else:
                photo_path = save_profile_photo(request.files.get("profile_photo"))
                save_admin_profile(full_name, phone, photo_path)

                ok, text = set_admin_password(password)
                if not ok:
                    error = text
                else:
                    recovery_code = make_recovery_code()
                    set_recovery_code(recovery_code)
                    start_trial_if_missing()
                    session.clear()
                    return render_template("setup_done.html", recovery_code=recovery_code, full_name=full_name)

        return render_template("setup.html", error=error)

    def settings_profile_page():
        msg = ""
        error = ""
        prof = get_admin_profile()

        if request.method == "POST":
            full_name = (request.form.get("full_name") or "").strip()
            phone = (request.form.get("phone") or "").strip()

            if len(full_name) < 3:
                error = "Ad soyad en az 3 karakter olmalı."
            elif len(phone) < 10:
                error = "Cep telefonu eksik görünüyor."
            else:
                photo_path = save_profile_photo(request.files.get("profile_photo"))
                save_admin_profile(full_name, phone, photo_path)
                msg = "Profil bilgileri güncellendi."
                prof = get_admin_profile()

        return render_template("settings_profile.html", msg=msg, error=error, profile=prof)

    app.add_url_rule("/kullanici-sifirla", endpoint="reset_user_page", view_func=reset_user_page, methods=["GET", "POST"])
    app.add_url_rule("/login", endpoint="login", view_func=login, methods=["GET", "POST"])
    app.add_url_rule("/logout", endpoint="logout", view_func=logout, methods=["GET", "POST"])

    app.add_url_rule("/sifre-unuttum", endpoint="forgot_password_page", view_func=forgot_password_page, methods=["GET", "POST"])
    app.add_url_rule("/kurulum", endpoint="setup_page", view_func=setup_page, methods=["GET", "POST"])
    app.add_url_rule("/ayarlar/sifre", endpoint="settings_password_page", view_func=settings_password_page, methods=["GET", "POST"])
    app.add_url_rule("/ayarlar/kurtarma-kodu", endpoint="settings_recovery_code_page", view_func=settings_recovery_code_page, methods=["GET", "POST"])
    app.add_url_rule("/ayarlar/profil", endpoint="settings_profile_page", view_func=settings_profile_page, methods=["GET", "POST"])
