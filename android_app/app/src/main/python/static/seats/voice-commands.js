/* =========================================================
   VOICE COMMANDS MODULE
   Sesli komut + konuşma + insancıl durak özeti
========================================================= */

const VOICE_HELP = [
  "kaç yolcu var",
  "ayakta kaç kişi var",
  "hesap aç",
  "emanet aç",
  "sıradaki durak [durak adı]",
  "durak seç [durak adı]",
  "[durak adı] kaç yolcu var",
  "bir sonraki durak",
  "rötar kaç",
  "hangi duraktayız",
  "sesli yardım",
  "bu durakta işlem var mı",
  "bu durakta kimler inecek",
  "bu durakta bagaj var mı",
  "inecekleri indir",
];

function stopHumanVoiceSummary(stopName){
  const stop = String(stopName || "").trim();
  if(!stop) return "Durak bilgisi bulunamadı.";

  let seats = [];
  let parcelCt = 0;
  let standingCt = 0;

  try{
    seats = seatsForStop(stop).map(Number).filter(Boolean);
  }catch(_){
    seats = [];
  }

  try{
    parcelCt = computeParcelCountsByStop()[stop] || 0;
  }catch(_){
    parcelCt = 0;
  }

  try{
    standingCt = computeStandingCountsByStop()[stop] || 0;
  }catch(_){
    standingCt = 0;
  }

  let bay = 0;
  let bayan = 0;
  let yolcu = 0;

  seats.forEach(seatNo => {
    const g = genders[String(seatNo)] || "";
    if(g === "bay") bay++;
    else if(g === "bayan") bayan++;
    else yolcu++;
  });

  // Ayakta yolcuyu "ayakta" diye söyleme; normal yolcu gibi ekle.
  yolcu += Number(standingCt || 0);

  const parts = [];
  if(bay > 0) parts.push(`${bay} bay`);
  if(bayan > 0) parts.push(`${bayan} bayan`);
  if(yolcu > 0) parts.push(`${yolcu} yolcu`);

  let msg = "";

  if(parts.length > 0){
    msg = `${stop} durağında ${parts.join(", ")} inecek.`;
  }else{
    msg = `${stop} durağı için inecek yolcu görünmüyor.`;
  }

  if(parcelCt > 0){
    msg += ` Ayrıca ${parcelCt} emanet teslim var.`;
  }

  try{
    const bagMsg = bagVoiceSummaryForStop(stop);
    if(bagMsg){
      msg += ` ${bagMsg}`;
    }
  }catch(_){}

  return msg;
}

/* --- voice stop ops helpers start --- */
function stopOperationVoiceSummary(stopName){
  const stop = String(stopName || "").trim();
  if(!stop) return "Durak bilgisi bulunamadı.";

  let seats = [];
  let standingCt = 0;
  let parcelCt = 0;
  let serviceCt = 0;
  let bagMsg = "";

  try{
    seats = seatsForStop(stop).map(Number).filter(Boolean);
  }catch(_){
    seats = [];
  }

  try{
    standingCt = computeStandingCountsByStop()[stop] || 0;
  }catch(_){
    standingCt = 0;
  }

  try{
    parcelCt = computeParcelCountsByStop()[stop] || 0;
  }catch(_){
    parcelCt = 0;
  }

  try{
    serviceCt = seats.filter(n => !!serviceMap[String(n)]).length;
  }catch(_){
    serviceCt = 0;
  }

  try{
    bagMsg = bagVoiceSummaryForStop(stop) || "";
  }catch(_){
    bagMsg = "";
  }

  const hasPassengerOps = seats.length > 0 || standingCt > 0;
  const hasParcelOps = parcelCt > 0;
  const hasServiceOps = serviceCt > 0;
  const hasBagOps = !!String(bagMsg || "").trim();

  if(!hasPassengerOps && !hasParcelOps && !hasServiceOps && !hasBagOps){
    return `${stop} durağı için işlem görünmüyor.`;
  }

  let msg = `${stop} durağında işlem var. `;

  if(hasPassengerOps){
    msg += stopHumanVoiceSummary(stop);
  }else{
    msg += `${stop} durağında yolcu inişi görünmüyor.`;
  }

  if(hasServiceOps){
    msg += ` Ayrıca ${serviceCt} servisli koltuk var.`;
  }

  return msg.trim();
}

function stopBagVoiceOnly(stopName){
  const stop = String(stopName || "").trim();
  if(!stop) return "Durak bilgisi bulunamadı.";

  try{
    const bagMsg = String(bagVoiceSummaryForStop(stop) || "").trim();
    if(bagMsg) return `${stop} için ${bagMsg}`;
  }catch(_){}

  return `${stop} durağı için bagaj görünmüyor.`;
}

async function offloadSelectedStopByVoice(){
  const stop = getSelectedStopName() || speedState.liveStop || "";
  if(!stop){
    toast("Önce durak seç");
    speak("Önce durak seç.");
    return true;
  }

  const seats = (() => {
    try{
      return seatsForStop(stop)
        .map(Number)
        .filter(n => !!assigned[String(n)]);
    }catch(_){
      return [];
    }
  })();

  let standingCt = 0;
  try{
    standingCt = computeStandingCountsByStop()[stop] || 0;
  }catch(_){
    standingCt = 0;
  }

  if(!seats.length && !standingCt){
    toast("Bu durakta indirilecek yolcu yok");
    speak("Bu durakta indirilecek yolcu yok.");
    return true;
  }

  const btn = $("#btnOffloadNowPane") || $("#btnOffloadNow");
  if(btn){
    btn.click();
    speak(`${stop} için indirilecek yolcular işleme alındı.`);
    return true;
  }

  if(typeof bulkOffload === "function" && seats.length){
    await bulkOffload(seats);
    speak(`${stop} için indirilecek yolcular indirildi.`);
    return true;
  }

  speak("İndirme işlemi başlatılamadı.");
  return true;
}
/* --- voice stop ops helpers end --- */

function maybeSpeakApproachStop(stopName, km){
  if(!stopName) return;
  if(!Number.isFinite(km)) return;
  if(km > 5) return;

  const key = `${TRIP_KEY}:${stopName}`;
  if(lastApproachVoiceStop === key) return;

  lastApproachVoiceStop = key;
  speak(`${stopName} durağına yaklaşılıyor. ${stopHumanVoiceSummary(stopName)}`);
}

function speak(text){
  const msg = String(text || "").trim();
  if(!msg) return;

  const soundToggle = $("#soundToggle");

  if(soundToggle && !soundToggle.checked) return;

  try{
    if(typeof window.SeatsSpeak === "function"){
      window.SeatsSpeak(msg);
    }else if(
      window.SeatsVoice &&
      typeof window.SeatsVoice.speak === "function" &&
      window.SeatsVoice.speak !== speak
    ){
      window.SeatsVoice.speak(msg);
    }else if("speechSynthesis" in window){
      speechSynthesis.cancel();

      const u = new SpeechSynthesisUtterance(msg);
      const voices = speechSynthesis.getVoices ? speechSynthesis.getVoices() : [];
      const trVoice = voices.find(v => (v.lang || "").toLowerCase().startsWith("tr"));

      if(trVoice) u.voice = trVoice;
      u.lang = trVoice ? trVoice.lang : "tr-TR";
      u.rate = 1;
      u.pitch = 1;
      u.volume = 1;

      setTimeout(() => {
        speechSynthesis.speak(u);
      }, 80);
    }
  }catch(e){
    console.warn("Sesli okuma hatası:", e);
  }

  if(navigator.vibrate) navigator.vibrate([140, 70, 140]);
}

function speakFinalStopSequence(name){
  speak(stopHumanVoiceSummary(name));
  setTimeout(() => {
    speak("Sarıkız Turizm ailesini tercih ettiğiniz için teşekkür ederiz. Bir sonraki yolculukta görüşmek üzere.");
  }, 1800);
}

function findStopMention(text){
  const ntext = norm(text);
  const list = allStopsList();
  let best = "";

  for(const stop of list){
    const ns = norm(stop);
    if(ns && ntext.includes(ns) && ns.length > best.length){
      best = stop;
    }
  }

  return best;
}

function extractSeatNumbersFromText(text){
  const nums = String(text || "").match(/\b\d{1,2}\b/g) || [];
  const out = [];

  nums.forEach(n => {
    const x = parseInt(n, 10);
    if(Number.isInteger(x) && x > 0 && x <= 60 && !out.includes(x)){
      out.push(x);
    }
  });

  return out;
}

function detectGenderFromText(text){
  const t = norm(text);

  if(/\b(erkek|bay|adam)\b/.test(t)) return "bay";
  if(/\b(kadin|kadın|bayan|kiz|kız)\b/.test(t)) return "bayan";
  if(/\b(bos yap|boş yap|cinsiyeti kaldir|cinsiyeti kaldır|temizle|sil|sifirla|sıfırla)\b/.test(t)) return "";

  return null;
}

async function applySeatGender(seats, gender){
  const validSeats = (Array.isArray(seats) ? seats : [])
    .map(x => Number(x))
    .filter(x => Number.isInteger(x) && x > 0);

  if(!validSeats.length){
    toast("Koltuk bulunamadı");
    speak("Koltuk bulunamadı.");
    return true;
  }

  const occupiedSeats = validSeats.filter(n => !!assigned[String(n)]);
  const emptySeats = validSeats.filter(n => !assigned[String(n)]);

  if(!occupiedSeats.length){
    toast("Önce koltuğa yolcu ekle");
    speak("Önce koltuğa yolcu eklemelisin.");
    return true;
  }

  const j = await safeJsonFetch("/api/seats/gender", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRF-Token": csrf
    },
    body: JSON.stringify({
      seats: occupiedSeats,
      gender: gender
    })
  });

  if(!j.ok) throw new Error(j.msg || "Cinsiyet güncellenemedi");

  occupiedSeats.forEach(n => {
    genders[String(n)] = gender;
    setSeatVisual(n);
  });

  const genderLabel =
    gender === "bay" ? "bay" :
    gender === "bayan" ? "bayan" : "boş";

  let msg = `${occupiedSeats.join(", ")} numara ${genderLabel} yapıldı`;
  if(emptySeats.length){
    msg += `. Boş olduğu için atlanan: ${emptySeats.join(", ")}`;
  }

  toast(msg, 3200);
  speak(msg);
  return true;
}

function parseVoiceCommand(text){
  const t = norm(text);
  const mentionedStop = findStopMention(text);
  const seats = extractSeatNumbersFromText(text);
  const gender = detectGenderFromText(text);

  if(/^(hesap ac|hesap aç)$/.test(t)) return { type:"open_hesap" };
  if(/^(emanet ac|emanet aç|emanetler ac|emanetler aç)$/.test(t)) return { type:"open_emanet" };
  if(/^(sesli yardim|sesli yardım|yardim|yardım)$/.test(t)) return { type:"help" };
  if(/(kac yolcu var|kaç yolcu var|toplam yolcu)/.test(t)) return { type:"ask_total" };
  if(/(ayakta kac|ayakta kaç)/.test(t)) return { type:"ask_standing" };
  if(/(hangi duraktayiz|hangi duraktayız|neredeyiz)/.test(t)) return { type:"ask_live_stop" };
  if(/(rotar kac|rötar kaç|gecikme kac|gecikme kaç)/.test(t)) return { type:"ask_delay" };
  if(/(bir sonraki durak|siradaki saatli|sıradaki saatli)/.test(t)) return { type:"ask_next_timed" };

  if(mentionedStop && /(kaç yolcu var|kac yolcu var|orada kaç yolcu var|orada kac yolcu var|kaç kişi var|kac kisi var)/.test(t)){
    return { type:"ask_stop_count", stop: mentionedStop };
  }

  if(seats.length && gender !== null){
    return { type:"set_gender", seats, gender };
  }

  if((/(siradaki durak|sıradaki durak|durak sec|durak seç)/.test(t)) && mentionedStop){
    return { type:"set_stop", stop: mentionedStop };
  }

  if(mentionedStop && /(durak|sec|seç)/.test(t)){
    return { type:"set_stop", stop: mentionedStop };
  }


  if(/(bu durakta islem var mi|bu durakta işlem var mı|secili durakta islem var mi|seçili durakta işlem var mı|bu durakta ne var)/.test(t)){
    return { type:"ask_stop_ops" };
  }

  if(/(bu durakta kimler inecek|secili durakta kim inecek|seçili durakta kim inecek|inecekleri soyle|inecekleri söyle)/.test(t)){
    return { type:"ask_selected_stop_passengers" };
  }

  if(mentionedStop && /(bagaj var mi|bagaj var mı)/.test(t)){
    return { type:"ask_stop_bags", stop: mentionedStop };
  }

  if(/(bu durakta bagaj var mi|bu durakta bagaj var mı|secili durakta bagaj var mi|seçili durakta bagaj var mı|bagajli var mi|bagajlı var mı)/.test(t)){
    return { type:"ask_stop_bags" };
  }

  if(/(inecekleri indir|bu durakta indir|secili duraktakileri indir|seçili duraktakileri indir)/.test(t)){
    return { type:"offload_selected_stop" };
  }

  return { type:"unknown", raw:text };
}

function aiIntentTitle(intent){
  const map = {
    seat_add_single: "Tek koltuk ekleme",
    seat_add_group: "Çoklu koltuk ekleme",
    seat_remove_single: "Tek koltuk boşaltma",
    seat_remove_group: "Çoklu koltuk boşaltma",
    standing_add: "Ayakta ekleme",
    service_mark: "Servis işaretleme",
    query: "Sorgu"
  };

  return map[intent] || intent || "Bilinmeyen işlem";
}

async function resolveVoiceWithBackendAI(text){
  const j = await safeJsonFetch("/api/ai/resolve", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRF-Token": csrf
    },
    body: JSON.stringify({ command: text })
  });

  return j?.result || null;
}

function extractFirstNumberFromText(text, fallback=1){
  const m = String(text || "").match(/\b\d+\b/);
  if(!m) return fallback;

  const n = parseInt(m[0], 10);
  return Number.isFinite(n) && n > 0 ? n : fallback;
}

async function openSingleSeatAddFlow(seatNo){
  await populateStops();
  openSeat(seatNo);

  const selectedStop = getSelectedStopName() || "";
  if(selectedStop && $("#pickup")) $("#pickup").value = selectedStop;

  toast(`Koltuk ${seatNo} için giriş formu açıldı`);
  speak(`Koltuk ${seatNo} için giriş formu açıldı.`);
}

async function openBulkSeatAddFlow(seats){
  await populateStops();

  openModal("#bulkBackdrop", "#bulkModal");

  const selectedStop = getSelectedStopName() || "";
  if(selectedStop && $("#bulkTo")) $("#bulkTo").value = selectedStop;

  clearMultiPicks();
  setMultiMode(true);

  seats.forEach(seatNo => {
    const el = $("#seat-" + seatNo);
    if(!el) return;
    if(assigned[String(seatNo)]) return;
    if(!multiSelected.has(el)) toggleSeatPick(el);
  });

  if($("#bulkCount")) $("#bulkCount").value = String(seats.length || 1);

  toast("Toplu giriş formu hazırlandı");
  speak("Toplu giriş formu açıldı.");
}

async function openStandingAddFlow(text, resolved){
  await populateStops();

  openModal("#cashBackdrop", "#cashModal");

  const selectedStop = getSelectedStopName() || "";
  if(selectedStop && $("#cashTo")) $("#cashTo").value = selectedStop;

  const inferred =
    (Array.isArray(resolved?.seats) && resolved.seats.length === 1)
      ? Number(resolved.seats[0] || 1)
      : extractFirstNumberFromText(text, 1);

  if($("#cashCount")) $("#cashCount").value = String(inferred > 0 ? inferred : 1);

  toast("Ayakta satış formu açıldı");
  speak("Ayakta satış formu açıldı.");
}

async function applyServiceMark(seats){
  if(!Array.isArray(seats) || !seats.length){
    toast("Servis için koltuk bulunamadı");
    speak("Servis için koltuk bulunamadı.");
    return;
  }

  const note = "Sesli komut";

  const j = await safeJsonFetch("/api/seats/service", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRF-Token": csrf
    },
    body: JSON.stringify({
      seats,
      service: 1,
      service_note: note
    })
  });

  if(!j.ok) throw new Error(j.msg || "Servis işaretleme başarısız");

  seats.forEach(n => {
    serviceMap[String(n)] = true;
    serviceNotes[String(n)] = note;
    setSeatVisual(n);
  });

  updateStats();
  renderAI();
  renderTimeline();
  updateCompactHeader();

  toast(`Servis işlendi: ${seats.join(", ")}`);
  speak(`Servis işlendi. Koltuklar ${seats.join(", ")}`);
}

async function executeResolvedAiOnSeats(resolved, rawText){
  if(!resolved) return false;

  const intent = resolved.intent || "";
  const seats = Array.isArray(resolved.seats) ? resolved.seats.map(Number).filter(Number.isFinite) : [];

  if(resolved.status === "suggest"){
    toast(`Düşük güven: ${aiIntentTitle(intent)}`);
    speak(`Komut düşük güvenle algılandı. Tahmin edilen işlem ${aiIntentTitle(intent)}.`);
    return true;
  }

  if(resolved.status !== "matched"){
    return false;
  }

  if(intent === "seat_remove_single" || intent === "seat_remove_group"){
    if(!seats.length){
      toast("Boşaltılacak koltuk bulunamadı");
      speak("Boşaltılacak koltuk bulunamadı.");
      return true;
    }

    await bulkOffload(seats);
    speak(`${seats.join(" ve ")} numaralı koltuk boşaltıldı.`);
    return true;
  }

  if(intent === "service_mark"){
    await applyServiceMark(seats);
    return true;
  }

  if(intent === "seat_add_single"){
    if(!seats.length){
      toast("Koltuk bulunamadı");
      speak("Koltuk bulunamadı.");
      return true;
    }

    await openSingleSeatAddFlow(seats[0]);
    return true;
  }

  if(intent === "seat_add_group"){
    if(!seats.length){
      toast("Koltuk listesi bulunamadı");
      speak("Koltuk listesi bulunamadı.");
      return true;
    }

    await openBulkSeatAddFlow(seats);
    return true;
  }

  if(intent === "standing_add"){
    await openStandingAddFlow(rawText, resolved);
    return true;
  }

  if(intent === "query"){
    return false;
  }

  return false;
}

async function handleLocalVoiceCommand(text){
  const cmd = parseVoiceCommand(text);

  if(cmd.type === "help"){
    const help = "Temel komutlar: " + VOICE_HELP.join(", ");
    toast(help, 4200);
    speak(help);
    return true;
  }

  if(cmd.type === "open_hesap"){
    speak("Hesap sayfası açılıyor.");
    location.href = URLS.hesap || "/hesap";
    return true;
  }

  if(cmd.type === "open_emanet"){
    speak("Emanet sayfası açılıyor.");
    location.href = URLS.consignments || "/emanetler";
    return true;
  }

  if(cmd.type === "set_gender"){
    await applySeatGender(cmd.seats, cmd.gender);
    return true;
  }

  if(cmd.type === "ask_total"){
    const seated = Object.values(assigned || {}).filter(Boolean).length;
    const total = seated + (standingCount || 0);
    const msg = `Toplam ${total} yolcu var. ${seated} oturan, ${standingCount || 0} ayakta.`;
    toast(msg, 3600);
    speak(msg);
    return true;
  }

  if(cmd.type === "ask_standing"){
    const msg = `Ayakta ${standingCount || 0} kişi var. Tahsilat ${fmtTL(standingRevenue || 0)}.`;
    toast(msg, 3600);
    speak(msg);
    return true;
  }


  if(cmd.type === "ask_stop_ops"){
    const stop = getSelectedStopName() || speedState.liveStop || "";
    const msg = stopOperationVoiceSummary(stop);

    toast(msg, 4200);
    speak(msg);
    return true;
  }

  if(cmd.type === "ask_selected_stop_passengers"){
    const stop = getSelectedStopName() || speedState.liveStop || "";
    const msg = stopHumanVoiceSummary(stop);

    toast(msg, 4200);
    speak(msg);
    return true;
  }

  if(cmd.type === "ask_stop_bags"){
    const stop = cmd.stop || getSelectedStopName() || speedState.liveStop || "";
    const msg = stopBagVoiceOnly(stop);

    toast(msg, 4200);
    speak(msg);
    return true;
  }

  if(cmd.type === "offload_selected_stop"){
    return await offloadSelectedStopByVoice();
  }

  if(cmd.type === "ask_stop_count"){
    const stop = cmd.stop;
    const msg = stopHumanVoiceSummary(stop);

    toast(msg, 4200);
    speak(msg);
    return true;
  }

  if(cmd.type === "ask_live_stop"){
    const live = speedState.liveStop || getSelectedStopName() || "henüz belli değil";
    const msg = `Şu an ${live} civarındasın.`;
    toast(msg, 3200);
    speak(msg);
    return true;
  }

  if(cmd.type === "ask_delay"){
    const nextTimed = speedState.etaItems.find(x => !x.passed) || null;
    if(!nextTimed){
      const msg = "Saatli durak bilgisi yok.";
      toast(msg, 3200);
      speak(msg);
      return true;
    }

    const msg = `${nextTimed.stop} için ${fmtSignedMin(nextTimed.delayMin)}. Plan ${nextTimed.plan}, tahmini ${fmtHour(nextTimed.etaDate)}.`;
    toast(msg, 4200);
    speak(msg);
    return true;
  }

  if(cmd.type === "ask_next_timed"){
    const nextTimed = speedState.etaItems.find(x => !x.passed) || null;
    if(!nextTimed){
      const msg = "Sıradaki saatli durak bulunamadı.";
      toast(msg, 3200);
      speak(msg);
      return true;
    }

    const msg = `Sıradaki saatli nokta ${nextTimed.stop}. Plan ${nextTimed.plan}, tahmini ${fmtHour(nextTimed.etaDate)}.`;
    toast(msg, 4200);
    speak(msg);
    return true;
  }

  if(cmd.type === "set_stop"){
    const ok = setSelectedStop(cmd.stop, { silent:true, voiceReply:false });
    if(!ok){
      toast("Bu durak güzergâhta yok");
      speak("Bu durak bu güzergâhta bulunmuyor.");
      return true;
    }

    const stop = getSelectedStopName();
    const msg = stopHumanVoiceSummary(stop);
    toast(msg, 3600);
    speak(msg);
    return true;
  }

  return false;
}

async function handleBasicVoiceCommand(text){
  const localHandled = await handleLocalVoiceCommand(text);
  if(localHandled) return;

  try{
    const resolved = await resolveVoiceWithBackendAI(text);
    const handled = await executeResolvedAiOnSeats(resolved, text);

    if(handled) return;

    if(resolved?.intent === "query"){
      const cmd = parseVoiceCommand(text);

      if(cmd.type === "ask_stop_count"){
        const stop = cmd.stop;
        const msg = stopHumanVoiceSummary(stop);
        toast(msg, 4200);
        speak(msg);
        return;
      }

      if(cmd.type === "ask_total"){
        const seated = Object.values(assigned || {}).filter(Boolean).length;
        const total = seated + (standingCount || 0);
        const msg = `Toplam ${total} yolcu var. ${seated} oturan, ${standingCount || 0} ayakta.`;
        toast(msg, 3600);
        speak(msg);
        return;
      }

      if(cmd.type === "ask_standing"){
        const msg = `Ayakta ${standingCount || 0} kişi var. Tahsilat ${fmtTL(standingRevenue || 0)}.`;
        toast(msg, 3600);
        speak(msg);
        return;
      }
    }

    toast("Komut anlaşılmadı");
    speak("Komutu anlayamadım. Sesli yardım diyebilirsin.");
  }catch(e){
    console.error("AI voice resolve error:", e);
    toast("AI sesli komut hatası");
    speak("AI sesli komut tarafında bir hata oluştu.");
  }
}

function getVoiceCommandButtons(){
  const out = [];
  const mainBtn = $("#btnDeckAI");
  const driveBtn = document.getElementById("btnDeckAIDrive");

  if(mainBtn) out.push(mainBtn);
  if(driveBtn) out.push(driveBtn);

  return out;
}

function setVoiceCommandButtonsListening(buttons, on){
  (buttons || []).forEach(btn => {
    btn.classList.toggle("listening", !!on);
    btn.innerHTML = on
      ? '🔴 <span>Dinliyor</span>'
      : '🎤 <span>Sesli Komut</span>';
  });
}

function startDeckAIVoice(){
  const buttons = getVoiceCommandButtons();
  const SR = window.SpeechRecognition || window.webkitSpeechRecognition;

  if(!SR){
    toast("Bu tarayıcı sesli komutu desteklemiyor");
    setVoiceBadge("Destek yok");
    return;
  }

  const rec = new SR();
  rec.lang = "tr-TR";
  rec.continuous = false;
  rec.interimResults = false;
  rec.maxAlternatives = 1;

  setVoiceCommandButtonsListening(buttons, true);

  setVoiceBadge("Dinleniyor");

  rec.onresult = async (e) => {
    const text = e.results?.[0]?.[0]?.transcript?.trim() || "";

    if(!text){
      toast("Ses algılandı ama metin çıkarılamadı");
      setVoiceBadge("Tekrar dene");
      return;
    }

    toast("Algılandı: " + text, 1600);
    setVoiceBadge(text.length > 18 ? text.slice(0, 18) + "…" : text);
    await handleBasicVoiceCommand(text);
  };

  rec.onerror = (e) => {
    toast("Sesli komut hatası: " + (e.error || "bilinmiyor"));
    setVoiceBadge("Hata");
  };

  rec.onend = () => {
    setVoiceCommandButtonsListening(buttons, false);

    setTimeout(() => setVoiceBadge("Hazır"), 900);
  };

  try{
    rec.start();
  }catch(_){
    setVoiceCommandButtonsListening(buttons, false);

    setVoiceBadge("Başlatılamadı");
    toast("Mikrofon başlatılamadı");
  }
}

window.SeatsVoice = {
  stopHumanVoiceSummary,
  maybeSpeakApproachStop,
  speak,
  speakFinalStopSequence,
  parseVoiceCommand,
  handleBasicVoiceCommand,
  startDeckAIVoice
};
