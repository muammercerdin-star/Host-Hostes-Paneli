/* =========================================================
   SEATS TIME / PRAYER MODULE
   Saat ve namaz vakti göstergeleri.
========================================================= */

(function initClock(){
  const $ = (sel) => document.querySelector(sel);

  const topClock = $("#topClock");
  const main = $("#clockMain");
  const date = $("#clockDate");
  const sub = $("#clockSub");

  if(!topClock || !main || !date || !sub) return;

  const tf = new Intl.DateTimeFormat("tr-TR", {
    hour:"2-digit",
    minute:"2-digit",
    second:"2-digit",
    hour12:false
  });

  const sf = new Intl.DateTimeFormat("tr-TR", {
    hour:"2-digit",
    minute:"2-digit",
    hour12:false
  });

  const df = new Intl.DateTimeFormat("tr-TR", {
    weekday:"long",
    day:"2-digit",
    month:"long",
    year:"numeric"
  });

  const tick = () => {
    const n = new Date();
    topClock.textContent = sf.format(n);
    main.textContent = tf.format(n);
    date.textContent = df.format(n);
    sub.textContent = df.format(n);
  };

  tick();
  setInterval(tick, 1000);
})();


(function initPrayer(){
  const $ = (sel) => document.querySelector(sel);

  const PR_ORDER = ["Fajr","Sunrise","Dhuhr","Asr","Maghrib","Isha"];
  const TR_PR = {
    Fajr:"İmsak",
    Sunrise:"Güneş",
    Dhuhr:"Öğle",
    Asr:"İkindi",
    Maghrib:"Akşam",
    Isha:"Yatsı"
  };

  const METHOD = 13;
  const SCHOOL = 0;
  const FALLBACK = { lat:38.5190, lng:28.5192, place:"Alaşehir" };
  const lineEl = $("#prLine");

  if(!lineEl) return;

  const pad2 = n => String(n).padStart(2, "0");

  function fmtHM(d){
    return `${pad2(d.getHours())}:${pad2(d.getMinutes())}`;
  }

  function toTodayDate(s){
    if(!s) return null;
    if(s.includes("T")) return new Date(s);

    const [h,m] = s.split(":").map(x => parseInt(x, 10));
    const d = new Date();
    d.setHours(h || 0, m || 0, 0, 0);
    return d;
  }

  function humanLeft(ms){
    const sec = Math.max(0, Math.floor(ms / 1000));
    const h = Math.floor(sec / 3600);
    const m = Math.floor((sec % 3600) / 60);
    return (h ? `${h} saat ` : "") + `${m} dk`;
  }

  async function reverseGeocode(lat, lng){
    try{
      const r = await fetch(`https://nominatim.openstreetmap.org/reverse?format=jsonv2&lat=${lat}&lon=${lng}`);
      const a = (await r.json()).address || {};
      const town = a.village || a.town || a.hamlet || a.suburb || "";
      const dist = a.county || a.district || "";
      const prov = a.province || a.state || "";
      const right = dist && dist !== town ? dist : prov;
      return [town || right, right && right !== town ? right : ""].filter(Boolean).join(", ");
    }catch(_){
      return "";
    }
  }

  async function fetchTimings(lat, lng){
    const url = `https://api.aladhan.com/v1/timings?latitude=${lat}&longitude=${lng}&method=${METHOD}&school=${SCHOOL}&iso8601=true`;
    const j = await (await fetch(url)).json();

    if(!j?.data?.timings){
      throw new Error("timings yok");
    }

    return j.data.timings;
  }

  function computePrevNext(timings){
    const now = new Date();

    const list = PR_ORDER
      .map(k => ({ key:k, at:toTodayDate(timings[k]) }))
      .filter(x => x.at && !isNaN(x.at));

    const future = list.filter(x => x.at > now);

    if(future.length){
      const next = future[0];
      const i = list.indexOf(next);
      const prev = i > 0 ? list[i - 1] : list[list.length - 1];
      return { prev, next };
    }

    const prev = list[list.length - 1];
    const tmr = toTodayDate(timings["Fajr"]);
    tmr.setDate(tmr.getDate() + 1);

    return {
      prev,
      next:{ key:"Fajr", at:tmr }
    };
  }

  function render(place, timings){
    const { prev, next } = computePrevNext(timings);

    const placeTxt = place ? `${place}: ` : "";
    const curName = TR_PR[prev.key] || prev.key;
    const nxtName = TR_PR[next.key] || next.key;
    const curHH = fmtHM(prev.at);
    const nxtHH = fmtHM(next.at);
    const leftMs = next.at - new Date();
    const leftTxt = humanLeft(leftMs);

    lineEl.innerHTML =
      `${placeTxt}<span class="pr-accent">${curName} ${curHH}</span> · Sonraki: <b>${nxtName} ${nxtHH}</b> · ` +
      `<span class="pr-left ${leftMs <= 10 * 60 * 1000 ? "soon" : ""}">Kalan ${leftTxt}</span>`;
  }

  async function boot(lat, lng, placeHint=""){
    try{
      const timings = await fetchTimings(lat, lng);
      const place = (await reverseGeocode(lat, lng)) || placeHint;

      render(place, timings);

      let lastDay = new Date().getDate();

      setInterval(async () => {
        const today = new Date().getDate();

        if(today !== lastDay){
          lastDay = today;
          render(place, await fetchTimings(lat, lng));
        }else{
          render(place, timings);
        }
      }, 1000);

    }catch(_){
      lineEl.textContent = "Vakitler alınamadı";
    }
  }

  if("geolocation" in navigator){
    navigator.geolocation.getCurrentPosition(
      p => boot(p.coords.latitude, p.coords.longitude),
      _ => boot(FALLBACK.lat, FALLBACK.lng, FALLBACK.place),
      { enableHighAccuracy:true, timeout:10000, maximumAge:30000 }
    );
  }else{
    boot(FALLBACK.lat, FALLBACK.lng, FALLBACK.place);
  }
})();
