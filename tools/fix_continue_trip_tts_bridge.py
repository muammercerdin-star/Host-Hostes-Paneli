from pathlib import Path
import re
import shutil

targets = [
    Path("templates/continue_trip.html"),
    Path("android_app/app/src/main/python/templates/continue_trip.html"),
]

bridge_block = '''
<!-- CONTINUE_TTS_BRIDGE_START -->
<script src="/static/seats/voice-tts.js?v=continue-tts-bridge-1"></script>
<!-- CONTINUE_TTS_BRIDGE_END -->
'''

new_func = r'''  function speakStopSummary(data){
    const msg = buildStopSummarySentence(data);

    function setSpeakState(text){
      try{
        const btn = document.getElementById("sheetSummarySpeak");
        if(!btn) return;

        if(!btn.dataset.originalText){
          btn.dataset.originalText = btn.textContent || "Sesli Oku";
        }

        btn.textContent = text || btn.dataset.originalText || "Sesli Oku";

        setTimeout(function(){
          btn.textContent = btn.dataset.originalText || "Sesli Oku";
        }, 900);
      }catch(_){}
    }

    if(!msg){
      setSpeakState("Metin yok");
      return;
    }

    // 1) Ortak ses köprüsü: APK'da AndroidTTS, tarayıcıda speechSynthesis kullanır.
    try{
      if(window.SeatsSpeak && typeof window.SeatsSpeak === "function"){
        window.SeatsSpeak(msg, { force:true });
        setSpeakState("Okunuyor...");
        return;
      }
    }catch(err){
      console.warn("SeatsSpeak summary error", err);
    }

    // 2) APK native TTS köprüsü
    try{
      if(window.AndroidTTS && typeof window.AndroidTTS.speak === "function"){
        if(typeof window.AndroidTTS.stop === "function"){
          try{ window.AndroidTTS.stop(); }catch(_){}
        }

        window.AndroidTTS.speak(msg);
        setSpeakState("Okunuyor...");
        return;
      }
    }catch(err){
      console.warn("AndroidTTS summary error", err);
    }

    // 3) Tarayıcı fallback
    try{
      if(window.speechSynthesis && window.SpeechSynthesisUtterance){
        window.speechSynthesis.cancel();

        const u = new SpeechSynthesisUtterance(msg);
        u.lang = "tr-TR";
        u.rate = 0.95;
        u.pitch = 1;

        const voices = window.speechSynthesis.getVoices ? window.speechSynthesis.getVoices() : [];
        const trVoice = voices.find(v => String(v.lang || "").toLowerCase().startsWith("tr"));
        if(trVoice) u.voice = trVoice;

        window.speechSynthesis.speak(u);
        setSpeakState("Okunuyor...");
        return;
      }
    }catch(err){
      console.error("summary speak error", err);
    }

    setSpeakState("Ses yok");
  }

'''

changed_any = False

for p in targets:
    if not p.exists():
        continue

    shutil.copy2(p, str(p) + f".bak_tts_bridge_{'{TS}'}")

    s = p.read_text(encoding="utf-8", errors="ignore")
    old = s

    # Eski bridge bloğu varsa temizle
    s = re.sub(
        r'\n?\s*<!-- CONTINUE_TTS_BRIDGE_START -->.*?<!-- CONTINUE_TTS_BRIDGE_END -->\s*\n?',
        "\n",
        s,
        flags=re.S
    )

    # voice-tts.js başka şekilde eklenmişse tekrar ekleme
    if "voice-tts.js" not in s:
        marker = '<script id="live-stop-sheet-script">'
        if marker in s:
            s = s.replace(marker, bridge_block + "\n" + marker, 1)
        elif "</body>" in s:
            s = s.replace("</body>", bridge_block + "\n</body>", 1)
        else:
            s += "\n" + bridge_block + "\n"

    # speakStopSummary fonksiyonunu APK uyumlu hale getir
    pattern = r'  function speakStopSummary\(data\)\{.*?\n  async function completeStopFromSummary'
    s, n = re.subn(
        pattern,
        new_func + "  async function completeStopFromSummary",
        s,
        count=1,
        flags=re.S
    )

    if n == 0:
        print(f"❌ speakStopSummary bulunamadı: {p}")
    else:
        print(f"✅ speakStopSummary güncellendi: {p}")

    if s != old:
        p.write_text(s, encoding="utf-8")
        changed_any = True
        print(f"✅ yazıldı: {p}")
    else:
        print(f"ℹ️ değişiklik yok: {p}")

if not changed_any:
    print("⚠️ Hiç dosya değişmedi.")
