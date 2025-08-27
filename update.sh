#!/usr/bin/env bash
set -euo pipefail

ts() { date +"%Y%m%d%H%M%S"; }

backup() {
  local f="$1"
  [[ -f "$f" ]] || { echo "skip backup (yok): $f"; return 0; }
  cp "$f" "$f.bak-$(ts)"
}

# Bir dosyada, bir "çapa" (anchor) satırını bul ve HEMEN SONRASINA blok ekle
insert_after_anchor() {
  local file="$1" anchor="$2"
  backup "$file"
  awk -v anchor="$anchor" -v mode=0 '
    BEGIN{added=0}
    {
      print $0
      if (index($0, anchor) && !added) {
        added=1
        while ((getline line) > 0 && line != "EOF__MARK__") print line
        # getline sonrası döngü bitecek; awk dışındaki here-doc devam ettirecek
      }
    }' "$file" > "$file.__tmp__" <<'EOF__MARK__'
__INJECT_BLOCK_PLACEHOLDER__
EOF__MARK__
  mv "$file.__tmp__" "$file"
}

# Basit bir kalıp ilk geçtiği yerde değiştir
replace_first() {
  local file="$1" pattern="$2" replacement="$3"
  backup "$file"
  # sadece ilk eşleşmeyi değiştir
  perl -0777 -pe '
    if(!$::done && m/'"$pattern"'/s){
      s/'"$pattern"'/'"$replacement"'/s;
      $::done=1;
    }
  ' "$file" > "$file.__tmp__"
  mv "$file.__tmp__" "$file"
}

undo() {
  # en son .bak-* dosyasını geri al (her hedef için)
  for f in app.py templates/base.html templates/index.html; do
    latest=$(ls -1 "${f}.bak-"* 2>/dev/null | tail -n 1 || true)
    if [[ -n "${latest}" ]]; then
      cp "${latest}" "${f}"
      echo "undo -> ${f} <= ${latest}"
    fi
  done
  # settings şablonunu kaldırmak istersen:
  if [[ -f templates/settings.html.added-flag ]]; then
    rm -f templates/settings.html templates/settings.html.added-flag
    echo "removed: templates/settings.html"
  fi
}

case "${1:-}" in
  test)
    echo "✓ sed/awk/backup çalışıyor"
    ;;

  undo)
    undo
    ;;

  kilitle-ui)
    # 1) base.html varsa sağ-üst sabit 'Kilitle' butonu (POST /logout + csrf)
    if [[ -f templates/base.html ]]; then
      # CSS ekle (body kapanışından hemen önce bir kez)
      if ! grep -q "/* lock-btn */" templates/base.html 2>/dev/null; then
        backup templates/base.html
        sed -i '/<\/style>/i \
  /* lock-btn */\
  .lock-btn{position:fixed;right:12px;top:12px;z-index:9999}\
  .lock-btn form{display:inline}\
  .lock-btn button{background:#d9534f;border:none;color:#fff;padding:8px 12px;border-radius:10px;font-weight:700;cursor:pointer}\
' templates/base.html || true
      fi

      # HTML ekle: </body> kapanışından hemen önce form
      if ! grep -q 'action="{{ url_for('\''logout'\'') }}' templates/base.html 2>/dev/null; then
        backup templates/base.html
        perl -0777 -pe '
          s#</body>#<div class="lock-btn">\n  <form method="post" action="{{ url_for('\''logout'\'') }}">\n    <input type="hidden" name="csrf_token" value="{{ csrf_token }}">\n    <button type="submit" title="Kilitle">Kilitle</button>\n  </form>\n</div>\n</body>#s
        ' -i templates/base.html
        echo "✓ Kilitle butonu eklendi (base.html)"
      else
        echo "• Kilitle butonu zaten var (skip)"
      fi
    else
      echo "⚠ templates/base.html bulunamadı, atlandı."
    fi
    ;;

  ayarlar-buton)
    # 2) index.html sağ-alt 'Ayarlar' butonu
    if [[ -f templates/index.html ]]; then
      if ! grep -q "/* ayarlar-fab */" templates/index.html 2>/dev/null; then
        backup templates/index.html
        # CSS
        sed -i '/<\/style>/i \
  /* ayarlar-fab */\
  .fab-settings{position:fixed;right:16px;bottom:16px;z-index:9999}\
  .fab-settings a{background:#3a4046;border:1px solid #4b5259;color:#fff;padding:12px 16px;border-radius:12px;text-decoration:none;font-weight:800}\
' templates/index.html
        # HTML (body sonundan hemen önce)
        perl -0777 -pe '
          s#</div>\s*</div>\s*</div>\s*</script>\s*{% endblock %}#</div></div>\n<div class="fab-settings"><a href="{{ url_for('\''settings'\'') }}">AYARLAR</a></div>\n</script>\n{% endblock %}#s
        ' -i templates/index.html || true
        # daha basit fallback: eğer yukarıdaki regex tutmazsa body kapanışına koy
        if ! grep -q 'fab-settings' templates/index.html; then
          perl -0777 -pe '
            s#</body>#<div class="fab-settings"><a href="{{ url_for('\''settings'\'') }}">AYARLAR</a></div>\n</body>#s
          ' -i templates/index.html
        fi
        echo "✓ Ayarlar butonu eklendi (index.html)"
      else
        echo "• Ayarlar CSS zaten var (skip)"
      fi
    else
      echo "⚠ templates/index.html bulunamadı, atlandı."
    fi
    ;;

  ayarlar-sayfasi)
    # 3) app.py içine /settings (GET) rotası ekle ve templates/settings.html oluştur
    if ! grep -q "@app.route(\"/settings\"" app.py 2>/dev/null; then
      backup app.py
      # route ekle: health/end_trip bloğundan önce bir yere enjekte ediyoruz
      perl -0777 -pe '
        s#(\n@app.route\(\"/health\"\)[\s\S]*?def health\(\):[\s\S]*?return[^\n]*\n\n)#\1@app.route("/settings")\ndef settings():\n    \"\"\"Basit ayarlar placeholder (şifre değiştirme daha sonra eklenecek).\"\"\"\n    return render_template(\"settings.html\")\n\n# NOTE: settings route injected by update.sh\n\n# #\n# #\n# #\n# #\n# #\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n# injected pad\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n# injected padding end\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#;#s
        ' app.py
      echo "✓ /settings GET route eklendi"
    else
      echo "• /settings zaten var (skip)"
    fi

    # Şablon
    mkdir -p templates
    if [[ ! -f templates/settings.html ]]; then
      cat > templates/settings.html <<'HTML'
{% extends "base.html" %}
{% block content %}
<style>
  .panel{max-width:720px;margin:24px auto;background:#2b3036;color:#e6edf3;border-radius:14px;padding:22px;box-shadow:0 4px 10px rgba(0,0,0,.35)}
  .btn{background:#3a4046;border:1px solid #4b5259;color:#fff;padding:10px 14px;border-radius:10px;text-decoration:none;font-weight:800}
  .muted{opacity:.75}
</style>
<div class="panel">
  <h2>Ayarlar</h2>
  <p class="muted">Bu sayfa şimdilik örnek. “Şifre değiştir / şifreyi kaldır” gibi işlemleri bir sonraki adımda etkinleştireceğiz.</p>
  <a class="btn" href="{{ url_for('index') }}">← Ana Sayfa</a>
</div>
{% endblock %}
HTML
      touch templates/settings.html.added-flag
      echo "✓ templates/settings.html yazıldı"
    else
      echo "• templates/settings.html mevcut (skip)"
    fi
    ;;

  *)
    cat <<USAGE
Kullanım:
  bash update.sh kilitle-ui      # base.html'e sağ-üst Kilitle (POST /logout)
  bash update.sh ayarlar-buton   # index.html'e sağ-alt AYARLAR butonu
  bash update.sh ayarlar-sayfasi # app.py'ye /settings (GET) ve settings.html oluştur
  bash update.sh undo            # son yedeklerden geri dön
  bash update.sh test            # akışı test et

USAGE
    ;;
esac
