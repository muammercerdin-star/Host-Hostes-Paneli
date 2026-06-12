#!/data/data/com.termux/files/usr/bin/bash
set -e

echo "===== V85C ANDROID SDK KURULUMU ====="

SDK="$HOME/android-sdk"
ZIP="$HOME/commandlinetools-linux-14742923_latest.zip"
URL="https://dl.google.com/android/repository/commandlinetools-linux-14742923_latest.zip"

echo "SDK: $SDK"

echo
echo "===== GEREKLİ TERMUX PAKETLERİ ====="
pkg install -y curl unzip openjdk-21

echo
echo "===== SDK DİZİNLERİ ====="
mkdir -p "$SDK/cmdline-tools"

echo
echo "===== COMMAND LINE TOOLS İNDİR ====="
if [ ! -f "$ZIP" ]; then
  curl -L "$URL" -o "$ZIP"
else
  echo "Zip zaten var: $ZIP"
fi

echo
echo "===== COMMAND LINE TOOLS KUR ====="
rm -rf "$SDK/cmdline-tools/latest" "$SDK/cmdline-tools/cmdline-tools"
unzip -q "$ZIP" -d "$SDK/cmdline-tools"
mv "$SDK/cmdline-tools/cmdline-tools" "$SDK/cmdline-tools/latest"

export ANDROID_HOME="$SDK"
export ANDROID_SDK_ROOT="$SDK"
export PATH="$SDK/cmdline-tools/latest/bin:$SDK/platform-tools:$PATH"

echo
echo "===== LİSANSLAR ====="
yes | sdkmanager --licenses >/dev/null || true

echo
echo "===== SDK PAKETLERİ KUR ====="
sdkmanager \
  "cmdline-tools;latest" \
  "platform-tools" \
  "platforms;android-35" \
  "build-tools;35.0.0"

echo
echo "===== local.properties GÜNCELLE ====="
cat > "$HOME/Host-Hostes-Paneli/android_app/local.properties" <<EOF
sdk.dir=$SDK
EOF

echo
echo "===== BASH ENV KAYDET ====="
grep -q "ANDROID_HOME=$SDK" "$HOME/.bashrc" 2>/dev/null || cat >> "$HOME/.bashrc" <<EOF

export ANDROID_HOME=$SDK
export ANDROID_SDK_ROOT=$SDK
export PATH=\$ANDROID_HOME/cmdline-tools/latest/bin:\$ANDROID_HOME/platform-tools:\$PATH
EOF

echo
echo "===== KONTROL ====="
ls -lh "$SDK/platforms/android-35/android.jar"
ls -d "$SDK/build-tools/"*
cat "$HOME/Host-Hostes-Paneli/android_app/local.properties"

echo
echo "✅ Android SDK kuruldu."
