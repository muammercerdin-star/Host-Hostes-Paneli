{% extends "base.html" %}
{% block content %}
<link rel="stylesheet" href="/static/style.css">

<style>
/* ===== Temel değişkenler ===== */
:root{
  --bg:#2f353a; --card:#1e2327; --muted:#3b4248; --text:#e8edf2;
  --brand:#1f6b2d; --danger:#8a3a3a; --primary:#2563eb; --warn:#d4a100; --accent:#0ea5e9;
}

/* ===== Resetler / temel ===== */
body{color:var(--text); background:var(--bg)}
.coach{width:960px;max-width:96vw;margin:16px auto}
.head{font-weight:700;margin-bottom:10px}

/* ===== İstatistik paneli ===== */
.stats{
  display:grid; grid-template-columns:repeat(5,1fr);
  gap:10px; margin:12px auto; max-width:960px;
}
.stat{
  background:var(--card); border:1px solid var(--muted); border-radius:12px;
  padding:10px; display:flex; flex-direction:column; gap:4px;
  box-shadow:0 10px 20px rgba(0,0,0,.25);
}
.stat .k{opacity:.85; font-size:12px}
.stat .v{font-weight:900; font-size:20px}

/* ===== Saat kutusu ===== */
.clock-tile{
  position:sticky; bottom:12px; left:0; right:0;
  z-index:1100;
  display:flex; align-items:center; gap:12px;
  padding:10px 14px;
  background:var(--card); border:1px solid var(--muted); border-radius:12px;
  box-shadow:0 12px 28px rgba(0,0,0,.35);
  font-weight:700;
}
/* iç hizalama yardımcı sınıflar */
.clock-actions{display:flex; align-items:center; gap:12px}
.clock-right{margin-left:auto; text-align:right}
.clock-tile .time{font-size:24px; letter-spacing:1px; font-variant-numeric:tabular-nums}
.clock-tile .date{font-size:13px; opacity:.85}

/* ===== Koltuk ızgarası ===== */
.deck{
  position:relative;
  display:grid; grid-template-columns:70px 70px 70px 70px; grid-auto-rows:70px;
  gap:24px; justify-content:center; margin-top:8px;
}
.cell{display:flex; flex-direction:column; align-items:center; justify-content:flex-start}
.seat{
  position:relative; width:56px; height:56px; border-radius:14px;
  background:#1f6b2d; color:#fff; display:flex; align-items:center; justify-content:center;
  font-weight:800; cursor:pointer; box-shadow:0 8px 22px rgba(0,0,0,.35);
}
.seat:hover{filter:brightness(1.08)}
.seat.selected{outline:3px solid #9ad1ff}
.seat.isAssigned{filter:saturate(1)}
.label{font-size:11px; color:#e6d48a; margin-top:4px; min-height:14px}

.corr{
  grid-column:2; grid-row:1/15; width:56px; border-radius:12px;
  background:#8a2b2b; display:flex; align-items:center; justify-content:center;
  color:#fff; font-weight:900; writing-mode:vertical-rl; text-orientation:mixed; letter-spacing:4px;
}
.door{
  grid-column:3/5; grid-row:8; height:28px; border-radius:10px;
  background:#7d602b; color:#fff; display:flex; align-items:center; justify-content:center; font-weight:900;
}

/* Servis rozeti */
.svc-badge{
  position:absolute; right:-6px; top:-6px; background:var(--accent); color:#fff;
  font-size:12px; border-radius:999px; padding:2px 6px; display:none;
}
.seat.has-service .svc-badge{display:flex}

/* Uyarı animasyonu */
@keyframes blinkWarn{
  0%,100%{box-shadow:0 0 0 0 rgba(212,161,0,.00); filter:brightness(1)}
  50%{box-shadow:0 0 0 8px rgba(212,161,0,.35); filter:brightness(1.1)}
}
.seat.blink-yellow{animation:blinkWarn 1s linear infinite; outline:3px solid var(--warn)}

/* ===== Tek koltuk formu ===== */
#seatForm{
  display:none; position:fixed; left:0; top:0;
  background:var(--card); color:#fff; border:1px solid var(--muted); border-radius:14px;
  padding:14px; width:420px; max-width:96vw; box-shadow:0 20px 40px rgba(0,0,0,.45);
  z-index:1700; /* panellerden düşük, ama diğer her şeyden yüksek */
}
#seatForm .row{margin:8px 0; display:flex; gap:12px; align-items:center; flex-wrap:wrap}

/* Butonlar & inputlar */
.btn{background:var(--brand); color:#fff; border:none; padding:8px 12px; border-radius:10px; font-weight:700; cursor:pointer}
.btn.secondary{background:#444}
.btn.danger{background:var(--danger)}
.btn.primary{background:var(--primary)}
.btn.warn{background:var(--warn); color:#242424}
select, input[type="number"], input[type="text"], textarea{
  background:#0f1215; color:#fff; border:1px solid var(--muted); border-radius:10px; padding:6px 8px;
}

/* ===== Uyarı barları ===== */
.alertbar{
  max-width:960px; margin:16px auto; padding:12px;
  border:1px solid var(--muted); border-radius:14px; background:var(--card);
  display:flex; align-items:flex-end; gap:12px; flex-wrap:wrap;
  box-shadow:0 12px 24px rgba(0,0,0,.35);
}
.alertbar .field{display:flex; flex-direction:column; gap:6px; min-width:180px}
.alertbar .spacer{flex:1}
.muted{opacity:.8; font-size:13px}

/* Toast en üst */
#toast{position:fixed; right:16px; top:16px; background:#000c; color:#fff; padding:8px 12px; border-radius:10px; display:none; z-index:3000}

/* ===== FAB’ler (yüzen butonlar) ===== */
.fab{
  position:fixed; height:56px; min-width:56px; padding:0 16px; border-radius:999px;
  border:1px solid var(--muted); background:var(--primary); color:#fff; font-weight:800;
  display:flex; align-items:center; gap:10px; box-shadow:0 14px 30px rgba(0,0,0,.45);
  cursor:grab; z-index:2200; user-select:none;
}
.fab.secondary{background:#16a34a}
.fab .dot{width:8px; height:8px; border-radius:999px; background:#a3ff9f}

/* Izgara içinde sabitlenen FAB’ler (sürüklemesiz) – modalların da önünde */
.fab-col{display:flex; flex-direction:column; gap:12px}
.fab.in-grid{
  position:relative; /* z-index aktif olsun */
  left:auto; right:auto; top:auto; bottom:auto;
  cursor:pointer; user-select:auto;
  z-index:2600; /* .panel(2400) ve .backdrop(2300)’un üstü */
}

/* Yuvarlak mini butonlar (saatte) */
.circle-btn{
  width:48px; height:48px; border-radius:50%; border:none; background:#222;
  display:flex; align-items:center; justify-content:center;
  box-shadow:0 4px 10px rgba(0,0,0,.5); cursor:pointer; transition:all .2s ease;
}
.circle-btn svg{width:24px; height:24px}
.circle-btn.green{color:#22c55e}
.circle-btn.red{color:#ef4444}
.circle-btn:hover{filter:brightness(1.2)}

/* ===== Modal katmanları ===== */
.backdrop{display:none; position:fixed; inset:0; background:rgba(0,0,0,.45); z-index:2300}
.panel{
  display:none; position:fixed; left:50%; top:50%; transform:translate(-50%,-50%);
  background:var(--card); color:#fff; border:1px solid var(--muted); border-radius:14px;
  padding:14px; width:560px; max-width:96vw; box-shadow:0 22px 44px rgba(0,0,0,.5); z-index:2400;
}
.panel .row{display:flex; gap:8px; margin:8px 0; flex-wrap:wrap}

/* Ayakta popover */
#standingBackdrop{display:none; position:fixed; inset:0; background:transparent; z-index:2350}
#standingPopover{
  display:none; position:fixed; z-index:2360;
  width:360px; max-width:94vw; padding:12px; background:var(--card); color:var(--text);
  border:1px solid var(--muted); border-radius:12px; box-shadow:0 14px 30px rgba(0,0,0,.45);
}
#standingPopover .head{font-weight:800; margin-bottom:8px}
#standingPopover .hint{opacity:.85; font-size:13px; margin-bottom:6px}
#standingPopover .item{
  display:flex; align-items:center; gap:8px; padding:6px 0;
  border-bottom:1px dashed rgba(255,255,255,.08);
}
#standingPopover .item:last-child{border-bottom:none}
#standingPopover{max-width:min(94vw,420px)}
#standingPopover .who{flex:1 1 auto; min-width:0; white-space:nowrap; overflow:hidden; text-overflow:ellipsis}
#standingPopover .actions{flex:0 0 auto; display:flex; gap:8px}
#standingPopover .actions .btn{padding:6px 10px; font-size:12px; line-height:1.1}

/* Koridor başı hayali BOŞALT */
#btnGhostOffload{
  display:none; position:absolute; left:50%; transform:translateX(-50%); top:-56px;
  padding:10px 16px; border-radius:12px; background:#ef4444; color:#fff; font-weight:900;
  border:1px solid #7f1d1d; box-shadow:0 10px 20px rgba(0,0,0,.35); z-index:1200;
}

/* ===== Geofence barı katmanları ===== */
#alertBar{position:relative; z-index:50}
#alertStop{position:relative; z-index:60}
#coordPanel{position:relative; z-index:40; margin-top:12px}

/* Saat kutusu (genel katman) */
#clockTile{z-index:30}
</style>

<div class="coach" aria-label="Otobüs Koltuk Planı">
  <div class="head">
    Sefer: {{ trip['route'] }} — Plaka: {{ trip['plate'] }} —
    1. Kaptan: {{ trip['captain1'] or '-' }} — 2. Kaptan: {{ trip['captain2'] or '-' }} — Muavin: {{ trip['attendant'] or '-' }}
  </div>

  <!-- İstatistikler -->
  <div class="stats">
    <div class="stat"><div class="k">Toplam Yolcu</div><div class="v" id="st_totalPax">0</div></div>
    <div class="stat"><div class="k">Boş Koltuk</div><div class="v" id="st_empty">0</div></div>
    <div class="stat"><div class="k">Doluluk Oranı</div><div class="v" id="st_occupancy">0%</div></div>
    <div class="stat" id="tileStanding"><div class="k">Ayakta Yolcu</div><div class="v" id="st_standing">0</div></div>
    <div class="stat"><div class="k">Ayakta Tahsilat</div><div class="v" id="st_standingTL">₺0.00</div></div>
  </div>

  <!-- Saat + kısayol butonları -->
  <div id="clockTile" class="clock-tile" aria-live="polite">
    <div class="clock-actions">
      <a href="{{ url_for('index') }}" class="circle-btn green" title="Ana Sayfa" aria-label="Ana Sayfa">
        <svg xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 24 24" aria-hidden="true">
          <path d="M12 3l9 9h-3v9h-12v-9h-3z"/>
        </svg>
      </a>

      <form method="post" action="{{ url_for('end_trip') }}"
            onsubmit="try{
              localStorage.removeItem(LSK);
              localStorage.removeItem(LSK+':items');
              localStorage.removeItem(LSK+':boards');
            }catch(_){}
            return confirm('Sefer sonlandırılsın mı?');">
        <input type="hidden" name="csrf_token" value="{{ csrf_token }}">
        <button type="submit" class="circle-btn red" title="Seferi Sonlandır" aria-label="Seferi Sonlandır">
          <svg xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 24 24" aria-hidden="true">
            <path d="M6 6h12v12h-12z"/>
          </svg>
        </button>
      </form>
    </div>

    <div class="clock-right">
      <div class="time" id="clockMain"></div>
      <div class="date" id="clockSub"></div>
    </div>
  </div>

  <!-- Koltuk ızgarası -->
  <div class="deck" id="deck">
    <button id="btnGhostOffload" class="btn danger">BOŞALT</button>
    <div class="corr">KORİDOR</div>

    {% set seats_map = {
      1:[1,1],3:[1,3],4:[1,4], 5:[2,1],7:[2,3],8:[2,4],
      9:[3,1],11:[3,3],12:[3,4], 13:[4,1],15:[4,3],16:[4,4],
      17:[5,1],19:[5,3],20:[5,4], 21:[6,1],23:[6,3],24:[6,4],
      25:[7,1],27:[7,3],28:[7,4],
      29:[8,1],
      31:[9,1],33:[9,3],34:[9,4],
      35:[10,1],37:[10,3],38:[10,4],
      39:[11,1],41:[11,3],42:[11,4],
      43:[12,1],45:[12,3],46:[12,4],
      49:[13,3],50:[13,4],
      51:[14,1],52:[14,2],53:[14,3],54:[14,4]
    } %}
    {% for n, pos in seats_map.items() %}
      {% if n == 29 %}<div class="door">KAPI</div>{% endif %}
      <div class="cell" style="grid-row:{{pos[0]}};grid-column:{{pos[1]}};">
        <div class="seat" onclick="handleSeatClick({{n}})" id="seat-{{n}}" data-seat="{{n}}" role="button" aria-label="Koltuk {{n}}">
          {{n}} <span class="svc-badge" title="Servis">🚌</span>
        </div>
        <div class="label" id="label-{{n}}"></div>
      </div>
    {% endfor %}

    <!-- Sabit FAB’ler -->
    <div class="cell" style="grid-row:13;grid-column:1;">
      <div class="fab-col">
        <button id="fabBulkFixed" class="fab in-grid"><span class="dot"></span> Toplu Giriş</button>
        <button id="fabCashFixed" class="fab secondary in-grid"><span class="dot"></span> Hızlı Tahsilat</button>
      </div>
    </div>
  </div>

  <!-- Geofence -->
  <div class="alertbar" id="alertBar">
    <div class="field" style="min-width:220px">
      <label for="alertStop">Sıradaki Durak</label>
      <select id="alertStop"><option value="">—</option></select>
    </div>
    <div class="field" style="max-width:140px">
      <label for="alertRadius">Eşik (km)</label>
      <input type="number" id="alertRadius" step="0.1" min="0.1" value="3">
    </div>
    <div class="field" style="min-width:140px">
      <label for="soundToggle">Sesli Uyarı</label>
      <label style="display:flex;align-items:center;gap:8px">
        <input type="checkbox" id="soundToggle" checked> Açık
      </label>
    </div>
    <button class="btn primary" id="btnGeoWatch">Konumu İzle: KAPALI</button>
    <button class="btn warn" id="btnTriggerNow">Şimdi Uyar</button>
    <div class="spacer"></div>
    <div class="muted" id="geoHint">Durak seç.</div>
  </div>

  <!-- Koordinat Paneli -->
  <div class="alertbar" id="coordPanel" style="display:none">
    <div class="field" style="min-width:200px">
      <label>Seçili Durak</label><input type="text" id="coordStopName" readonly>
    </div>
    <div class="field"><label>Lat</label><input type="number" id="coordLat" step="0.000001" placeholder="37.xxxxxx"></div>
    <div class="field"><label>Lng</label><input type="number" id="coordLng" step="0.000001" placeholder="29.xxxxxx"></div>
    <button class="btn" id="btnSaveCoord">Koordinatı Kaydet</button>
    <div class="spacer"></div><div class="muted">Koordinat kaydı: route_stop_coords</div>
  </div>

  <!-- Yaklaşma Paneli -->
  <div id="approachBackdrop" class="backdrop"></div>
  <div id="approachPanel" class="panel" role="dialog" aria-modal="true" aria-labelledby="approachTitle">
    <h3 id="approachTitle" style="margin:0 0 10px 0">Durak Yaklaşıyor</h3>
    <div id="approachInfo" class="hint">—</div>
    <div id="approachList" class="list" style="max-height:240px; overflow:auto; margin-top:8px"></div>
    <div class="row" style="justify-content:flex-end">
      <button class="btn danger" id="approachOffload">Toplu İndir</button>
      <button class="btn secondary" id="approachClose">Kapat</button>
      <button class="btn secondary" id="approachSnooze">Ertele (5 dk)</button>
    </div>
  </div>

  <!-- Toplu Giriş FAB + Panel -->
  <div id="bulkBackdrop" class="backdrop"></div>
  <div id="bulkPanel" class="panel">
    <h3 style="margin:0 0 10px 0">Toplu Giriş</h3>
    <div class="row">
      <label style="flex:1">Nereden <select id="bulkFrom"><option value="">—</option></select></label>
      <label style="flex:1">Nereye <select id="bulkTo"><option value="">—</option></select></label>
      <label>Adet <input type="number" id="bulkCount" min="1" value="1" style="width:100px"></label>
    </div>
    <div class="row">
      <label><input type="radio" name="bulkTicket" value="biletsiz" checked> Biletsiz</label>
      <label><input type="radio" name="bulkTicket" value="biletli"> Biletli</label>
      <label style="margin-left:auto; display:flex; align-items:center; gap:6px"><input type="checkbox" id="multiPick"> Çoklu seçim</label>
      <label style="margin-left:auto"><input type="checkbox" id="bulkService"> Servis</label>
    </div>
    <div class="row" style="justify-content:flex-end">
      <button type="button" class="btn secondary" id="bulkClose">Kapat</button>
      <button type="button" class="btn primary" id="bulkSave">Kaydet</button>
    </div>
    <div class="muted" style="margin-top:6px">
      Çoklu seçim: işaretle → paneli kapat → koltuklara dokunarak seç → tekrar açıp Kaydet.<br>
      Çoklu seçim kapalıysa: seçim yoksa boş koltuklardan rastgele doldurur.
    </div>
  </div>

  <!-- Hızlı Tahsilat FAB + Panel -->
  <div id="cashBackdrop" class="backdrop"></div>
  <div id="cashPanel" class="panel">
    <h3 style="margin:0 0 10px 0">Hızlı Tahsilat (Ayakta)</h3>
    <div class="row">
      <label>Adet <input type="number" id="cashCount" min="1" value="1" style="width:100px"></label>
      <label>Tutar (₺/kişi) <input type="number" id="cashPrice" min="0" step="0.01" value="0" style="width:140px"></label>
      <label>Ödeme
        <select id="cashPay">
          <option value="nakit">Nakit</option>
          <option value="iban">IBAN</option>
          <option value="pos">POS</option>
          <option value="online">Online</option>
        </select>
      </label>
    </div>
    <div class="row">
      <label>Nereden <select id="cashFrom"><option value="">—</option></select></label>
      <label>Nereye <select id="cashTo"><option value="">—</option></select></label>
    </div>
    <div class="row">
      <label style="flex:1">Not <input type="text" id="cashNote" placeholder="Kısa not..."></label>
    </div>
    <div class="row" style="justify-content:flex-end">
      <button class="btn secondary" id="cashClose">Kapat</button>
      <button class="btn primary" id="cashSave">Ekle</button>
    </div>
    <div class="muted">Koltuk ataması yapmaz; ayakta yolcu ve tahsilat toplamını artırır.</div>
  </div>

  <!-- Tek koltuk formu -->
  <div id="seatForm" role="dialog" aria-modal="true" aria-labelledby="seatTitle">
    <h3 id="seatTitle">Koltuk</h3>
    <div class="row">
      <label>Biniş Yeri: <select id="pickup"><option value="">—</option></select></label>
    </div>
    <div class="row">
      <label>İniş Yeri: <select id="dropoff"><option value="">—</option></select></label>
    </div>
    <div class="row">
      <label>Bilet:</label>
      <label><input type="radio" name="ticket" value="biletli"> Biletli</label>
      <label><input type="radio" name="ticket" value="biletsiz" checked> Biletsiz</label>
      <label><input type="radio" name="ticket" value="ucretsiz"> Ücretsiz</label>
    </div>
    <div class="row">
      <label>Ödeme:</label>
      <label><input type="radio" name="pay" value="nakit" checked> Nakit</label>
      <label><input type="radio" name="pay" value="iban"> IBAN</label>
      <label><input type="radio" name="pay" value="online"> Online</label>
      <label><input type="radio" name="pay" value="pos"> POS</label>
      <label><input type="radio" name="pay" value="ucretsiz"> Ücretsiz</label>
    </div>
    <div class="row"><label>Tutar (₺): <input type="number" id="price" value="0.00" min="0" step="0.01"></label></div>
    <div class="row">
      <label>Cinsiyet:</label>
      <label><input type="radio" name="gender" value="bay"> Bay</label>
      <label><input type="radio" name="gender" value="bayan"> Bayan</label>
      <label><input type="radio" name="gender" value="" checked> Boş</label>
    </div>
    <div class="row"><label><input type="checkbox" id="pairOk"> Yan yana istisna</label></div>
    <div class="row"><label><input type="checkbox" id="serviceChk"> Servis kullanacak</label></div>
    <div class="row"><label style="flex:1">Servis notu <input type="text" id="serviceNote" placeholder="Mahalle / konum (opsiyonel)"></label></div>
    <div class="row" style="justify-content:flex-end;">
      <button class="btn" onclick="saveSeat()">Kaydet</button>
      <button class="btn danger" onclick="offloadSeat()">İniş (Boşalt)</button>
      <button class="btn secondary" onclick="closeForm()">Kapat (ESC)</button>
    </div>
  </div>

  <!-- Ayakta Yolcu popover -->
  <div id="standingBackdrop" onclick="closeStandingPopover()"></div>
  <div id="standingPopover" role="dialog" aria-modal="true" aria-labelledby="standingTitle">
    <div class="head" id="standingTitle">Ayakta Yolcular</div>
    <div class="hint" id="standingSummary">—</div>
    <div id="standingList"></div>
    <div style="display:flex; justify-content:flex-end; gap:8px; margin-top:8px">
      <button class="btn danger" id="standingBulkOff" style="display:none">Toplu İndir</button>
      <button class="btn secondary" id="standingClose" onclick="closeStandingPopover()">Kapat</button>
    </div>
  </div>
</div>

</script>
{% endblock %}
