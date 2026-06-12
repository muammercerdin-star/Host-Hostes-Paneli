#!/data/data/com.termux/files/usr/bin/bash
set -e

echo "===== V85D ANDROID SDK LİSANS DÜZELTME ====="

SDK="$HOME/android-sdk"

export ANDROID_HOME="$SDK"
export ANDROID_SDK_ROOT="$SDK"
export PATH="$SDK/cmdline-tools/latest/bin:$SDK/platform-tools:$PATH"

echo "SDK: $SDK"

mkdir -p "$SDK/licenses"

echo
echo "===== LİSANS DOSYALARI YAZILIYOR ====="

cat > "$SDK/licenses/android-sdk-license" <<EOF
8933bad161af4178b1185d1a37fbf41ea5269c55
d56f5187479451eabf01fb78af6dfcb131a6481e
24333f8a63b6825ea9c5514f83c2829b004d1fee
EOF

cat > "$SDK/licenses/android-sdk-preview-license" <<EOF
84831b9409646a918e30573bab4c9c91346d8abd
EOF

echo
echo "===== local.properties ====="
cat > "$HOME/Host-Hostes-Paneli/android_app/local.properties" <<EOF
sdk.dir=$SDK
EOF

cat "$HOME/Host-Hostes-Paneli/android_app/local.properties"

echo
echo "===== SDKMANAGER VAR MI ====="
if [ -x "$SDK/cmdline-tools/latest/bin/sdkmanager" ]; then
  echo "✅ sdkmanager var"
  yes | "$SDK/cmdline-tools/latest/bin/sdkmanager" --sdk_root="$SDK" --licenses || true

  echo
  echo "===== EKSİK SDK PAKETLERİ ====="
  "$SDK/cmdline-tools/latest/bin/sdkmanager" --sdk_root="$SDK" \
    "platforms;android-35" \
    "build-tools;34.0.0" \
    "build-tools;35.0.0" \
    "platform-tools" || true
else
  echo "⚠️ sdkmanager yok. Gradle lisans dosyalarıyla otomatik indirmeyi deneyecek."
fi

echo
echo "===== KONTROL ====="
ls -la "$SDK/licenses"
ls -ld "$SDK/platforms/android-35" 2>/dev/null || true
ls -ld "$SDK/build-tools/34.0.0" 2>/dev/null || true
ls -ld "$SDK/build-tools/35.0.0" 2>/dev/null || true

echo
echo "✅ V85D lisans düzeltme bitti."
