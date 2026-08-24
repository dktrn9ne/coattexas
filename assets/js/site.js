/* ═══════════════════════════════════════════════════════════
   PRECISION COATINGS OF TEXAS — SHARED SITE SCRIPT
   Scroll reveal, nav (desktop dropdown + mobile drawer), and the
   AI estimator chat widget. Loaded on every page.
   ═══════════════════════════════════════════════════════════ */

/* ══════ SCROLL REVEAL ══════ */
(function(){
  const io = new IntersectionObserver(entries => {
    entries.forEach(e => { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } });
  }, { threshold: 0.12 });
  document.querySelectorAll('.rv').forEach(el => io.observe(el));
})();

/* ══════ MOBILE NAV ══════ */
(function(){
  const burger = document.getElementById('navBurger');
  const panel = document.getElementById('mobileNav');
  if (!burger || !panel) return;
  burger.addEventListener('click', () => {
    const open = burger.classList.toggle('open');
    panel.classList.toggle('open', open);
    document.body.style.overflow = open ? 'hidden' : '';
  });
  panel.querySelectorAll('a').forEach(a => a.addEventListener('click', () => {
    burger.classList.remove('open');
    panel.classList.remove('open');
    document.body.style.overflow = '';
  }));
})();

/* ══════ CHAT WIDGET (AI Estimator) ══════ */
let chatOpen = false, busy = false, hist = [], lead = {};
document.addEventListener('DOMContentLoaded', () => {
  setTimeout(() => { const h = document.getElementById('chatHint'); if (h) h.style.display = 'none'; }, 7000);
});

function toggleChat(){
  chatOpen = !chatOpen;
  document.getElementById('chatWin').classList.toggle('open', chatOpen);
  document.getElementById('chatFab').classList.toggle('open', chatOpen);
  const ic = document.getElementById('fabIco');
  if (chatOpen) {
    ic.innerHTML = '<line x1="18" y1="6" x2="6" y2="18" stroke="#fff" stroke-width="2.5"/><line x1="6" y1="6" x2="18" y2="18" stroke="#fff" stroke-width="2.5"/>';
    if (!hist.length) initChat();
    setTimeout(() => document.getElementById('chatInp').focus(), 320);
  } else {
    ic.innerHTML = '<path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/>';
  }
}
function openChat(){ if (!chatOpen) toggleChat(); }
function chatAbout(topic){
  openChat();
  if (hist.length) sendUserMsg('Tell me about ' + topic);
  else setTimeout(() => sendUserMsg('Tell me about ' + topic), 600);
}

function initChat(){
  addBot("Hey! 👋 I'm the PCT AI estimator. I can get you a free quote, answer questions about any of our services, or schedule a consultation.\n\nWhat surface are we transforming today?");
  setTimeout(() => showQR(['Get a free estimate','Garage floor','Patio','Tub or vanity','Cabinets or countertops']), 500);
}
function showQR(opts){
  const r = document.getElementById('qrRow'); r.innerHTML = '';
  opts.forEach(o => {
    const b = document.createElement('button');
    b.className = 'qr'; b.textContent = o;
    b.onclick = () => { r.innerHTML = ''; sendUserMsg(o); };
    r.appendChild(b);
  });
}
function addBot(txt){
  const m = document.getElementById('chatMsgs');
  const d = document.createElement('div'); d.className = 'msg bot';
  d.innerHTML = `<div class="msg-av">🔴</div><div class="msg-bub">${txt.replace(/\n/g,'<br>')}</div>`;
  m.appendChild(d); m.scrollTop = m.scrollHeight;
}
function addUser(txt){
  const m = document.getElementById('chatMsgs');
  const d = document.createElement('div'); d.className = 'msg user';
  d.innerHTML = `<div class="msg-av">👤</div><div class="msg-bub">${txt}</div>`;
  m.appendChild(d); m.scrollTop = m.scrollHeight;
}
function showTyping(){
  const m = document.getElementById('chatMsgs');
  const d = document.createElement('div'); d.className = 'msg bot'; d.id = 'typer';
  d.innerHTML = `<div class="msg-av">🔴</div><div class="typing-bub"><span></span><span></span><span></span></div>`;
  m.appendChild(d); m.scrollTop = m.scrollHeight;
}
function rmTyping(){ const t = document.getElementById('typer'); if (t) t.remove(); }
function handleKey(e){ if (e.key === 'Enter' && !e.shiftKey) { e.preventDefault(); sendMsg(); } }
function autoResize(el){ el.style.height = 'auto'; el.style.height = Math.min(el.scrollHeight, 90) + 'px'; }
function sendMsg(){
  const inp = document.getElementById('chatInp');
  const txt = inp.value.trim();
  if (!txt || busy) return;
  inp.value = ''; inp.style.height = 'auto';
  sendUserMsg(txt);
}

async function sendUserMsg(txt){
  document.getElementById('qrRow').innerHTML = '';
  addUser(txt); hist.push({ role: 'user', content: txt });
  busy = true; document.getElementById('sendBtn').disabled = true;
  setTimeout(showTyping, 180);

  const sys = `You are the AI estimator and client intake assistant for Precision Coatings of Texas LLC — a professional surface coating and refinishing company in Austin, Texas.

Services offered (the ONLY seven services):
• Garages — flake, metallic epoxy, solid color, natural accent floor systems
• Patios — overlays, stains, non-slip outdoor coatings
• Tile — epoxy resurfacing over existing tile, no demo needed
• Tubs — reglazing, chip & rust repair
• Vanities — bathroom vanity refinishing
• Countertops — kitchen/bath countertop & backsplash refinishing
• Cabinets — kitchen & bathroom cabinet refinishing

General pricing (always recommend free on-site estimate):
• 2-car garage flake system: $1,200–$1,800
• 2-car garage metallic: $1,800–$2,800
• Patio coating: $3–$6/sq ft
• Tub reglazing: $450–$700
• Vanity refinishing: $300–$600
• Countertop refinishing: $35–$50/sq ft
• Cabinet refinishing: quoted by door/drawer count
• All include surface prep

Multi-Spec colors available (StoneFlecks Ultra™ by Hawk Research Labs):
Loft Collection: Niagara, Oyster Bay, Dove Gray, Morning Mist, Slate Gray, Smoke Cement (NEW)
Mineral Collection: Espresso, Andromeda (NEW), Yukon, White Vein, Granite, Feldspar (NEW)
Earth Collection: Neptunite (NEW), Fossil, Cliff, Beach Sand, Landslide, Castlerock, Muir Woods, Charcoal, Midnight Sky
(Clay, Basalt, Sandstone are close-out — ask about availability)

Lead info to collect naturally (ONE question at a time): name → phone or email → which surface → approx size → timeline.
Once you have name + contact, confirm the PCT team will reach out within 24 business hours.

Business facts (verified):
• Based in Hutto, TX — serving Austin & all of Central Texas
• Hours: Mon–Fri 8am–6pm, Sat 8am–12pm, Sun 8am–12pm (open 7 days!)
• Free on-site estimates — never a charge
• Seasonal discounts offered throughout the year
• Warranties on workmanship
• Payment: Cash, Check, Credit Card, Square, Zelle
• Locally owned & operated · Rated 5.0 on HomeAdvisor · Top Pro on Thumbtack

Contact: 512-537-7951 | precisioncoatingsoftx@gmail.com
Keep replies warm, concise (2–4 sentences), never pushy.

Lead info collected so far: ${JSON.stringify(lead)}`;

  try {
    const res = await fetch('https://api.anthropic.com/v1/messages', {
      method: 'POST', headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ model: 'claude-sonnet-4-20250514', max_tokens: 1000, system: sys, messages: hist })
    });
    const data = await res.json(); rmTyping();
    const reply = data.content?.[0]?.text || "Quick hiccup — call us at 512-537-7951 and we'll get you squared away!";
    hist.push({ role: 'assistant', content: reply }); addBot(reply);

    const em = txt.match(/[\w.-]+@[\w.-]+\.\w+/); if (em) lead.email = em[0];
    const ph = txt.match(/(\d{3}[-.\s]?\d{3}[-.\s]?\d{4})/); if (ph) lead.phone = ph[0];
    const sf = txt.match(/(\d+)\s*(sq|square|sf)/i); if (sf) lead.sqft = sf[1];

    const combo = (txt + ' ' + reply).toLowerCase();
    let qrs = [];
    if (hist.length <= 3) qrs = ['Get free estimate','Garage floor','Patio','Tub refinishing'];
    else if (combo.includes('garage')) qrs = ['Flake or metallic?','Price range?','Schedule a visit'];
    else if (combo.includes('patio')) qrs = ['Patio colors?','Timeline?','Get quote'];
    else if (combo.includes('tub') || combo.includes('vanity')) qrs = ['How long does it take?','Price range?','Schedule a visit'];
    else if (combo.includes('cabinet') || combo.includes('countertop')) qrs = ['How does refinishing work?','Price range?','Get quote'];
    else if (combo.includes('price') || combo.includes('estimate')) qrs = ['Schedule on-site estimate','What info do you need?'];
    else if (hist.length > 7) qrs = ['Schedule a call','📞 512-537-7951'];
    if (qrs.length) setTimeout(() => showQR(qrs), 400);
  } catch (err) {
    rmTyping();
    addBot("Quick hiccup on my end! Reach us at <strong>512-537-7951</strong> or <strong>precisioncoatingsoftx@gmail.com</strong> — Mon–Fri 8am–6:30pm.");
  }
  busy = false; document.getElementById('sendBtn').disabled = false;
  document.getElementById('chatInp').focus();
}
