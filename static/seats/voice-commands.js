/* =========================================================
   VOICE COMMANDS MODULE
   Sesli komut + konuşma + insancıl durak özeti
========================================================= */

const VOICE_HELP = [
  "kaç yolcu var",
  "ayakta kaç kişi var",
  "hesap aç",
  "emanet aç",
  "harita aç",
  "sıradaki durak [durak adı]",
  "durak seç [durak adı]",
  "5 numaralı yolcu [durak]",
  "5 numara erkek [durak]",
  "5 numara bayan [durak]",
  "15 numara biletsiz yolcu",
  "[durak adı] kaç yolcu var",
  "bir sonraki durak",
  "rötar kaç",
  "hangi duraktayız",
  "sesli yardım",
  "bu durakta işlem var mı",
  "bu durakta kimler inecek",
  "bu durakta bagaj var mı",
  "inecekleri indir",
  "özet ver",
  "durumu söyle",
  "sefer özeti",
];

/* VOICE_SUMMARY_PATCH_START */
function buildTripVoiceSummary(){
  let seated = 0;
  let standing = 0;

  try{
    seated = Object.values(assigned || {}).filter(Boolean).length;
  }catch(_){
    seated = 0;
  }

  try{
    standing = Number(standingCount || 0);
  }catch(_){
    standing = 0;
  }

  const total = seated + standing;
  const parts = [];

  if(standing > 0){
    parts.push(`Toplam ${total} yolcu var. Bunun ${standing} kişisi ayakta.`);
  }else{
    parts.push(`Toplam ${total} yolcu var.`);
  }

  let selected = "";

  try{
    if(typeof getSelectedStopName === "function"){
      selected = getSelectedStopName() || "";
    }
  }catch(_){}

  try{
    if(!selected && speedState && speedState.liveStop){
      selected = speedState.liveStop || "";
    }
  }catch(_){}

  selected = String(selected || "").trim();

  if(selected){
    parts.push(`Seçili durak ${selected}.`);

    let seatCt = 0;
    let standingCt = 0;
    let parcelCt = 0;
    let bagMsg = "";

    try{
      seatCt = seatsForStop(selected).map(Number).filter(Boolean).length;
    }catch(_){
      seatCt = 0;
    }

    try{
      standingCt = Number((computeStandingCountsByStop() || {})[selected] || 0);
    }catch(_){
      standingCt = 0;
    }

    try{
      parcelCt = Number((computeParcelCountsByStop() || {})[selected] || 0);
    }catch(_){
      parcelCt = 0;
    }

    try{
      bagMsg = String(bagVoiceSummaryForStop(selected) || "").trim();
    }catch(_){
      bagMsg = "";
    }

    const ops = [];
    const passengerTotal = seatCt + standingCt;

    if(passengerTotal > 0){
      ops.push(`${passengerTotal} yolcu inecek`);
    }

    if(parcelCt > 0){
      ops.push(`${parcelCt} emanet teslim`);
    }

    if(bagMsg){
      ops.push(bagMsg.replace(/\.$/, ""));
    }

    if(ops.length){
      parts.push(`Bu durakta ${ops.join(", ")}.`);
    }else{
      parts.push("Bu durakta görünen işlem yok.");
    }
  }

  let next = "";

  try{
    if(speedState && Array.isArray(speedState.etaItems)){
      const nextTimed = speedState.etaItems.find(x => !x.passed);
      if(nextTimed && nextTimed.stop) next = nextTimed.stop;
    }
  }catch(_){}

  try{
    if(!next && typeof computeNextStopName === "function"){
      next = computeNextStopName(selected || "", "nextWithSeats") || "";
    }
  }catch(_){}

  next = String(next || "").trim();

  if(next){
    parts.push(`Sıradaki işlem ${next}.`);
  }

  return parts.join(" ");
}
/* VOICE_SUMMARY_PATCH_END */

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
  if(/^(harita ac|harita aç|haritayi ac|haritayı aç|canli harita ac|canlı harita aç|yol haritasi ac|yol haritası aç)$/.test(t)) return { type:"open_map" };
  if(/^(sesli yardim|sesli yardım|yardim|yardım)$/.test(t)) return { type:"help" };
  if(/(ozet ver|özet ver|durumu soyle|durumu söyle|sefer ozeti|sefer özeti|genel ozet|genel özet)/.test(t)) return { type:"trip_summary" };
  if(/(kac yolcu var|kaç yolcu var|toplam yolcu)/.test(t)) return { type:"ask_total" };
  if(/(ayakta kac|ayakta kaç)/.test(t)) return { type:"ask_standing" };
  if(/(hangi duraktayiz|hangi duraktayız|neredeyiz)/.test(t)) return { type:"ask_live_stop" };
  if(/(rotar kac|rötar kaç|gecikme kac|gecikme kaç)/.test(t)) return { type:"ask_delay" };
  if(/(bir sonraki durak|siradaki saatli|sıradaki saatli)/.test(t)) return { type:"ask_next_timed" };

  if(mentionedStop && /(kaç yolcu var|kac yolcu var|orada kaç yolcu var|orada kac yolcu var|kaç kişi var|kac kisi var)/.test(t)){
    return { type:"ask_stop_count", stop: mentionedStop };
  }

  if(seats.length && /(biletsiz|biletsiz yolcu|biletsiz yap|biletsiz isaretle|biletsiz işaretle)/.test(t)){
    return { type:"mark_biletsiz", seats };
  }

  if(seats.length && mentionedStop && /(yolcu|bindir|binis|biniş|al|ekle|yaz|kaydet|gitsin|gidecek|numara|numaralı)/.test(t)){
    return { type:"direct_board", seats, stop: mentionedStop, gender };
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

/* VOICE_DIRECT_BOARD_GENERAL_START */
function voiceCleanStopValue(v){
  v = String(v || "").replace(/\s+/g, " ").trim();
  if(!v || v === "-" || v === "—") return "";
  v = v.replace(/^🎯\s*/g, "");
  v = v.replace(/^Seçili\s+durak\s*:\s*/i, "");
  return v.trim();
}

function voiceCurrentBoardingStop(){
  let stop = "";

  /*
    Öncelik seçili durakta olmalı.
    Çünkü liveStop localStorage'dan eski Sarıgöl gibi bir değeri geri getirebilir.
  */

  try{
    const alertStop = document.querySelector("#alertStop");
    if(alertStop){
      stop = voiceCleanStopValue(alertStop.value);
    }
  }catch(_){}

  try{
    if(!stop && typeof getSelectedStopName === "function"){
      stop = voiceCleanStopValue(getSelectedStopName());
    }
  }catch(_){}

  try{
    if(!stop){
      const badge = document.querySelector("#selectedStopBadge");
      if(badge) stop = voiceCleanStopValue(badge.textContent);
    }
  }catch(_){}

  try{
    if(!stop){
      const simpleStop = document.querySelector("#seatSimpleStop");
      if(simpleStop) stop = voiceCleanStopValue(simpleStop.textContent);
    }
  }catch(_){}

  /*
    Canlı durak en son fallback.
    Böylece eski liveStop hafızası seçili durağı ezmez.
  */
  try{
    if(!stop && typeof getDisplayLiveStop === "function"){
      stop = voiceCleanStopValue(getDisplayLiveStop());
    }
  }catch(_){}

  try{
    if(!stop && speedState && speedState.liveStop){
      stop = voiceCleanStopValue(speedState.liveStop);
    }
  }catch(_){}

  try{
    if(stop && typeof findCanonicalStopName === "function"){
      const fixed = findCanonicalStopName(stop);
      if(fixed) stop = fixed;
    }
  }catch(_){}

  return stop;
}

async function voiceDirectBoardSeats(seats, toStop, genderValue=""){
  const seatList = (Array.isArray(seats) ? seats : [seats])
    .map(x => Number(x))
    .filter(x => Number.isInteger(x) && x > 0);

  if(!seatList.length){
    toast("Koltuk numarası bulunamadı");
    speak("Koltuk numarası bulunamadı.");
    return true;
  }

  let fromStop = voiceCurrentBoardingStop();
  toStop = voiceCleanStopValue(toStop);

  genderValue = String(genderValue || "").trim().toLowerCase();

  if(genderValue === "erkek"){
    genderValue = "bay";
  }else if(genderValue === "kadın" || genderValue === "kadin" || genderValue === "kız" || genderValue === "kiz"){
    genderValue = "bayan";
  }

  if(genderValue !== "bay" && genderValue !== "bayan"){
    genderValue = "";
  }

  try{
    if(toStop && typeof findCanonicalStopName === "function"){
      const fixedTo = findCanonicalStopName(toStop);
      if(fixedTo) toStop = fixedTo;
    }

    if(fromStop && typeof findCanonicalStopName === "function"){
      const fixedFrom = findCanonicalStopName(fromStop);
      if(fixedFrom) fromStop = fixedFrom;
    }
  }catch(_){}

  if(!fromStop){
    toast("Canlı durak veya seçili durak yok");
    speak("Önce canlı durak ya da seçili durak belirlenmeli.");
    return true;
  }

  if(!toStop){
    toast("İniş durağı bulunamadı");
    speak("İniş durağı bulunamadı.");
    return true;
  }

  if(typeof norm === "function" && norm(fromStop) === norm(toStop)){
    toast("Biniş ve iniş durağı aynı olamaz");
    speak("Biniş ve iniş durağı aynı olamaz.");
    return true;
  }

  const csrfToken =
    (typeof csrf !== "undefined" && csrf) ||
    (window.SEATS_BOOT && window.SEATS_BOOT.csrf) ||
    "";

  async function postSeat(payload){
    const opts = {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "X-CSRF-Token": csrfToken
      },
      body: JSON.stringify(payload)
    };

    if(typeof safeJsonFetch === "function"){
      return await safeJsonFetch("/api/seat", opts);
    }

    const r = await fetch("/api/seat", opts);
    return await r.json();
  }

  const saved = [];
  const failed = [];

  for(const seatNo of seatList){
    try{
      const payload = {
        seat_no: seatNo,
        from_stop: fromStop,
        to_stop: toStop,
        ticket_type: "biletsiz",
        payment: "nakit",
        amount: 0,
        gender: genderValue,
        pair_ok: 0,
        service: 0,
        service_note: "",
        passenger_name: "",
        passenger_phone: ""
      };

      const j = await postSeat(payload);

      if(!j || j.ok === false){
        throw new Error((j && (j.msg || j.error)) || "Kayıt başarısız");
      }

      const key = String(seatNo);

      try{ assigned[key] = true; }catch(_){}
      try{ boardsMap[key] = fromStop; }catch(_){}
      try{ stopsMap[key] = toStop; }catch(_){}
      try{ genders[key] = genderValue || ""; }catch(_){}

      try{ if(typeof setSeatVisual === "function") setSeatVisual(seatNo); }catch(_){}
      try{ if(typeof updateStats === "function") updateStats(); }catch(_){}
      try{ if(typeof renderAI === "function") renderAI(); }catch(_){}
      try{ if(typeof renderTimeline === "function") renderTimeline(); }catch(_){}
      try{ if(typeof updateCompactHeader === "function") updateCompactHeader(); }catch(_){}
      try{ if(typeof updateStopSeatBadges === "function") updateStopSeatBadges(); }catch(_){}
      try{ if(typeof refreshStopBadges === "function") refreshStopBadges(); }catch(_){}

      saved.push(seatNo);
    }catch(e){
      console.warn("Sesli direkt bindirme hatası:", seatNo, e);
      failed.push(seatNo);
    }
  }

  if(saved.length){
    const seatText = saved.length === 1
      ? `${saved[0]} numara`
      : `${saved.join(", ")} numaralar`;

    const genderText =
      genderValue === "bay" ? " Erkek." :
      genderValue === "bayan" ? " Bayan." : "";

    const msg = `${seatText} yolcu alındı. Biniş ${fromStop}. İniş ${toStop}.${genderText}`;
    toast(msg, 4200);
    speak(msg);
  }

  if(failed.length){
    speak(`${failed.join(", ")} numarada kayıt yapılamadı.`);
  }

  return true;
}
/* VOICE_DIRECT_BOARD_GENERAL_END */

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

  if(cmd.type === "trip_summary"){
    const msg = buildTripVoiceSummary();
    toast(msg, 5200);
    speak(msg);
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

  if(cmd.type === "open_map"){
    speak("Canlı harita tam ekran açılıyor.");
    location.href = "/canli-harita?fullscreen=1";
    return true;
  }

  if(cmd.type === "set_gender"){
    await applySeatGender(cmd.seats, cmd.gender);
    return true;
  }

  if(cmd.type === "direct_board"){
    await voiceDirectBoardSeats(cmd.seats, cmd.stop, cmd.gender);
    return true;
  }

  if(cmd.type === "mark_biletsiz"){
    if(typeof window.markBiletsizSeatBadges !== "function"){
      toast("Biletsiz işaretleme hazır değil");
      speak("Biletsiz işaretleme hazır değil.");
      return true;
    }

    const res = window.markBiletsizSeatBadges(cmd.seats || []);
    const done = (res && res.done) || [];
    const failed = (res && res.failed) || [];

    if(done.length){
      const txt = done.length === 1 ? `${done[0]} numara` : `${done.join(", ")} numaralar`;
      toast(`${txt} biletsiz işaretlendi`, 3600);
      speak(`${txt} biletsiz yolcu olarak işaretlendi.`);
    }

    if(failed.length){
      speak(`${failed.join(", ")} numarada dolu yolcu bulunamadı.`);
    }

    return true;
  }

  if(cmd.type === "ask_total"){
    const seated = Object.values(assigned || {}).filter(Boolean).length;
    const total = seated + (standingCount || 0);
    const standing = Number(standingCount || 0);
      const msg = standing > 0
        ? `Toplam ${total} yolcu var. Bunun ${standing} kişisi ayakta.`
        : `Toplam ${total} yolcu var.`;
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
        const standing = Number(standingCount || 0);
      const msg = standing > 0
        ? `Toplam ${total} yolcu var. Bunun ${standing} kişisi ayakta.`
        : `Toplam ${total} yolcu var.`;
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
  const bottomBtn = document.getElementById("seatSimpleVoiceBtn");

  if(mainBtn) out.push(mainBtn);
  if(driveBtn) out.push(driveBtn);
  if(bottomBtn) out.push(bottomBtn);

  return out;
}

function setVoiceCommandButtonsListening(buttons, on){
  (buttons || []).forEach(btn => {
    btn.classList.toggle("listening", !!on);

    if(btn.id === "seatSimpleVoiceBtn"){
      btn.innerHTML = on
        ? '<span class="ico">🔴</span><span class="voice-bottom-text">Dinliyor</span>'
        : '<span class="ico">🎙️</span><span class="voice-bottom-text">Sesli<br>Komut</span>';
      btn.setAttribute("title", on ? "Dinliyor" : "Sesli Komut");
      btn.setAttribute("aria-label", on ? "Dinliyor" : "Sesli Komut");
      return;
    }

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
