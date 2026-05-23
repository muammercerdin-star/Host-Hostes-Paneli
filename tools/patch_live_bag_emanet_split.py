from pathlib import Path
import re, shutil, time

TS = time.strftime("%Y%m%d_%H%M%S")

targets = [
    Path("templates/continue_trip.html"),
    Path("android_app/app/src/main/python/templates/continue_trip.html"),
]

style_block = r'''
<style id="live-bag-emanet-split-style">
/* =========================================================
   LIVE BAGAJ + EMANET AYIRMA
   2 BAGAJ +1 emanet şeklinde gösterir.
========================================================= */

#liveBagajMetric{
  position:relative !important;
}

#liveBagajCount{
  line-height:.95 !important;
}

#liveEmanetCount.live-bag-extra{
  display:block;
  margin-top:5px;
  color:#fbbf24;
  font-size:11px;
  line-height:1;
  font-weight:1000;
  letter-spacing:.02em;
  white-space:nowrap;
  opacity:.96;
  text-shadow:0 0 12px rgba(251,191,36,.18);
}

#liveEmanetCount[hidden]{
  display:none !important;
}

@media(max-width:430px){
  #liveEmanetCount.live-bag-extra{
    font-size:10px;
    margin-top:4px;
  }
}
</style>
'''.strip()

script_block = r'''
<script id="live-bag-emanet-split-script">
(function(){
  if(window.__LIVE_BAG_EMANET_SPLIT_ACTIVE__) return;
  window.__LIVE_BAG_EMANET_SPLIT_ACTIVE__ = true;

  const tripId = {{ trip['id'] | tojson | safe }};

  function text(v){
    return String(v == null ? "" : v).trim();
  }

  function num(v){
    const n = Number(String(v ?? "0").replace(",", "."));
    return Number.isFinite(n) ? n : 0;
  }

  function currentStopName(){
    const el = document.getElementById("liveCurrentStopName");
    return text(el && el.textContent);
  }

  function ensureExtraLine(){
    const main = document.getElementById("liveBagajCount");
    if(!main) return null;

    let extra = document.getElementById("liveEmanetCount");

    if(!extra){
      extra = document.createElement("span");
      extra.id = "liveEmanetCount";
      extra.className = "live-bag-extra";
      extra.hidden = true;
      main.insertAdjacentElement("afterend", extra);
    }

    return { main, extra };
  }

  function normalizePayload(j){
    if(!j) return null;

    if(j.data) return j.data;
    if(j.detail) return j.detail;
    if(j.summary) return j.summary;
    if(j.stop_detail) return j.stop_detail;

    return j;
  }

  function passengerBagTotal(data){
    const passengers = Array.isArray(data && data.passengers) ? data.passengers : [];
    return passengers.reduce((sum, p) => {
      return sum + Math.max(
        num(p.bag_count),
        num(p.bagaj_count),
        num(p.bag),
        num(p.baggage_count)
      );
    }, 0);
  }

  function consignmentTotal(data){
    if(!data) return 0;

    if(Array.isArray(data.consignments)) return data.consignments.length;
    if(Array.isArray(data.emanets)) return data.emanets.length;
    if(Array.isArray(data.cargos)) return data.cargos.length;

    return Math.max(
      num(data.consignment_count),
      num(data.emanet_count),
      num(data.cargo_count),
      num(data.parcel_count)
    );
  }

  function bagTotal(data){
    if(!data) return 0;

    const direct = Math.max(
      num(data.bag_total),
      num(data.bag_count),
      num(data.bagaj_real_count),
      num(data.real_bag_count)
    );

    if(direct > 0) return direct;

    return passengerBagTotal(data);
  }

  function applyBagEmanetSplit(data){
    const els = ensureExtraLine();
    if(!els || !data) return;

    const bag = bagTotal(data);
    const emanet = consignmentTotal(data);

    els.main.textContent = String(bag);

    if(emanet > 0){
      els.extra.hidden = false;
      els.extra.textContent = `+${emanet} emanet`;
    }else{
      els.extra.hidden = true;
      els.extra.textContent = "";
    }
  }

  async function fetchJson(url){
    const r = await fetch(url, {
      method:"GET",
      credentials:"same-origin",
      cache:"no-store",
      headers:{ "Accept":"application/json" }
    });

    if(!r.ok) throw new Error("HTTP " + r.status);
    return await r.json();
  }

  async function refreshBagEmanetSplit(){
    const stop = currentStopName();
    if(!stop || stop === "Durak seçilmedi") return;

    const qs = `trip_id=${encodeURIComponent(tripId)}&stop=${encodeURIComponent(stop)}&_=${Date.now()}`;

    const urls = [
      `/api/live-stop-detail?${qs}`,
      `/api/live-stop-summary?${qs}`,
      `/api/live-stop-info?${qs}`
    ];

    for(const url of urls){
      try{
        const j = await fetchJson(url);
        const payload = normalizePayload(j);

        if(payload){
          applyBagEmanetSplit(payload);
          return;
        }
      }catch(_){}
    }
  }

  function start(){
    ensureExtraLine();
    refreshBagEmanetSplit();

    setTimeout(refreshBagEmanetSplit, 700);
    setTimeout(refreshBagEmanetSplit, 1800);

    setInterval(refreshBagEmanetSplit, 4000);
  }

  document.addEventListener("click", function(e){
    if(e.target.closest("#liveCurrentCard, #liveOffloadMetric, #liveBagajMetric")){
      setTimeout(refreshBagEmanetSplit, 500);
      setTimeout(refreshBagEmanetSplit, 1400);
    }
  }, true);

  window.LiveBagEmanetSplit = {
    refresh: refreshBagEmanetSplit,
    apply: applyBagEmanetSplit
  };

  if(document.readyState === "loading"){
    document.addEventListener("DOMContentLoaded", start);
  }else{
    start();
  }
})();
</script>
'''.strip()

for p in targets:
    if not p.exists():
        print(f"YOK: {p}")
        continue

    shutil.copy2(p, str(p) + f".bak_bag_emanet_split_{TS}")

    s = p.read_text(encoding="utf-8", errors="ignore")

    # Eski aynı yamayı temizle
    s = re.sub(
        r'\n?\s*<style id="live-bag-emanet-split-style">.*?</style>\s*',
        "\n",
        s,
        flags=re.S
    )
    s = re.sub(
        r'\n?\s*<script id="live-bag-emanet-split-script">.*?</script>\s*',
        "\n",
        s,
        flags=re.S
    )

    # Önceden eklenmiş emanet satırı varsa temizle
    s = re.sub(
        r'\s*<span\s+id="liveEmanetCount"[^>]*>.*?</span>',
        "",
        s,
        flags=re.S
    )

    # BAGAJ sayısının altına + emanet satırı için yer aç
    s = re.sub(
        r'(<b\s+id="liveBagajCount"[^>]*>.*?</b>)',
        r'\1\n              <span id="liveEmanetCount" class="live-bag-extra" hidden></span>',
        s,
        count=1,
        flags=re.S
    )

    # CSS'i head kapanmadan önce ekle
    if "</head>" in s:
      s = s.replace("</head>", style_block + "\n\n</head>", 1)
    else:
      s = style_block + "\n\n" + s

    # JS'i body kapanmadan önce ekle
    if "</body>" in s:
      s = s.replace("</body>", script_block + "\n\n</body>", 1)
    else:
      s = s.rstrip() + "\n\n" + script_block + "\n"

    p.write_text(s, encoding="utf-8")
    print(f"✅ patched: {p}")

