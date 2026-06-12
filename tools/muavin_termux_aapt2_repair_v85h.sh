#!/data/data/com.termux/files/usr/bin/bash
set -e

echo "===== V85H TERMUX CURL + AAPT2 ONARIM ====="

echo
echo "===== 1) PAKET SİSTEMİNİ TOPARLA ====="
apt update || true
apt full-upgrade -y || true

echo
echo "===== 2) CURL / LIBCURL ONAR ====="
apt install -y curl libcurl openssl || true
hash -r || true

echo
echo "===== 3) CURL TEST ====="
curl --version || true

echo
echo "===== 4) AAPT2 ARA ====="
apt search aapt 2>/dev/null | head -80 || true
apt search aapt2 2>/dev/null | head -80 || true

echo
echo "===== 5) AAPT / AAPT2 KURMAYI DENE ====="
pkg install -y aapt || true
pkg install -y aapt2 || true
pkg install -y android-tools || true

echo
echo "===== 6) AAPT2 SON KONTROL ====="
AAPT2="$(command -v aapt2 || true)"

if [ -z "$AAPT2" ]; then
  echo "❌ aapt2 hâlâ bulunamadı."
  echo
  echo "Manuel kontrol:"
  echo "apt search aapt"
  echo "apt search aapt2"
  echo "pkg install aapt"
  exit 2
fi

echo "✅ AAPT2 bulundu: $AAPT2"
"$AAPT2" version || true

echo
echo "===== 7) GRADLE AAPT2 OVERRIDE ====="
GP="$HOME/Host-Hostes-Paneli/android_app/gradle.properties"
STAMP="$(date +%Y%m%d-%H%M%S)"

cp "$GP" "$GP.bak-aapt2-v85h-$STAMP"

grep -v '^android.aapt2FromMavenOverride=' "$GP" > "$GP.tmp" || true
mv "$GP.tmp" "$GP"

cat >> "$GP" <<EOF

# V85H_TERMUX_NATIVE_AAPT2
android.aapt2FromMavenOverride=$AAPT2
EOF

echo
echo "===== 8) GRADLE CACHE TEMİZLE ====="
rm -rf "$HOME/.gradle/caches/9.5.1/transforms" || true
rm -rf "$HOME/.gradle/caches/modules-2/files-2.1/com.android.tools.build/aapt2" || true
rm -rf "$HOME/Host-Hostes-Paneli/android_app/app/build/intermediates/compiled_local_resources" || true

echo
echo "===== 9) SON DURUM ====="
grep -nE "aapt2FromMavenOverride|V85H_TERMUX_NATIVE_AAPT2" "$GP"
cat "$GP"

echo
echo "✅ V85H tamam."
