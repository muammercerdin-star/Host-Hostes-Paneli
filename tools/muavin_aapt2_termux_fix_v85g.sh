#!/data/data/com.termux/files/usr/bin/bash
set -e

echo "===== V85G TERMUX AAPT2 FIX ====="

cd "$HOME/Host-Hostes-Paneli" || exit

echo
echo "===== 1) MEVCUT AAPT2 VAR MI ====="
command -v aapt2 || true
command -v aapt || true

echo
echo "===== 2) AAPT PAKETİ KURMAYI DENE ====="
if ! command -v aapt2 >/dev/null 2>&1; then
  pkg install -y aapt || true
fi

echo
echo "===== 3) TEKRAR KONTROL ====="
AAPT2="$(command -v aapt2 || true)"

if [ -z "$AAPT2" ]; then
  echo "❌ Termux içinde aapt2 bulunamadı."
  echo "Şunu manuel dene:"
  echo "pkg search aapt"
  echo "pkg install aapt"
  exit 2
fi

echo "✅ AAPT2: $AAPT2"
"$AAPT2" version || true

echo
echo "===== 4) gradle.properties YEDEK + OVERRIDE ====="
GP="$HOME/Host-Hostes-Paneli/android_app/gradle.properties"
STAMP="$(date +%Y%m%d-%H%M%S)"

cp "$GP" "$GP.bak-aapt2-v85g-$STAMP"

# Eski override varsa kaldır
grep -v '^android.aapt2FromMavenOverride=' "$GP" > "$GP.tmp" || true
mv "$GP.tmp" "$GP"

cat >> "$GP" <<EOF

# V85G_TERMUX_NATIVE_AAPT2
android.aapt2FromMavenOverride=$AAPT2
EOF

echo
echo "===== 5) GRADLE CACHE TEMİZLİK ====="
rm -rf "$HOME/.gradle/caches/9.5.1/transforms" || true
rm -rf "$HOME/.gradle/caches/modules-2/files-2.1/com.android.tools.build/aapt2" || true
rm -rf "$HOME/Host-Hostes-Paneli/android_app/app/build/intermediates/compiled_local_resources" || true

echo
echo "===== 6) SON KONTROL ====="
grep -nE "aapt2FromMavenOverride|V85G_TERMUX_NATIVE_AAPT2" "$GP"
cat "$GP"

echo
echo "✅ V85G tamam. Gradle artık Termux native aapt2 kullanacak."
