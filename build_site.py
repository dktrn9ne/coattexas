#!/usr/bin/env python3
"""
Static site generator for Precision Coatings of Texas.
Builds every page from shared nav/footer/chat-widget partials so markup
stays consistent, then writes plain .html files (no runtime templating —
Vercel serves these as static files, matching the existing deploy setup).
"""
import os

ROOT = os.path.dirname(os.path.abspath(__file__))

PHONE = "512-537-7951"
PHONE_TEL = "5125377951"
EMAIL = "precisioncoatingsoftx@gmail.com"

# ─────────────────────────── Real project photos (unchanged CDN URLs) ───────────────────────────
IMG = {
    "hero_home": "https://img1.wsimg.com/isteam/ip/0f231134-604e-4ca2-8a19-8f07d8fe5b53/20230612_083453.jpg/:/rs=w:1800,cg:true",
    "garage_bento": "https://img1.wsimg.com/isteam/ip/0f231134-604e-4ca2-8a19-8f07d8fe5b53/20240312_171440.jpg/:/rs=w:900,cg:true",
    "garage_alt": "https://img1.wsimg.com/isteam/ip/0f231134-604e-4ca2-8a19-8f07d8fe5b53/20230612_083453.jpg/:/rs=w:900,cg:true",
    "garage_2024": "https://img1.wsimg.com/isteam/ip/0f231134-604e-4ca2-8a19-8f07d8fe5b53/20240312_171445.jpg/:/rs=w:900,cg:true",
    "garage_signature": "https://img1.wsimg.com/isteam/ip/0f231134-604e-4ca2-8a19-8f07d8fe5b53/20230719_104958.jpg/:/rs=w:1200,cg:true",
    "patio_bento": "https://img1.wsimg.com/isteam/ip/0f231134-604e-4ca2-8a19-8f07d8fe5b53/20220921_112555.jpg/:/cr=t:29.26%25,l:13.24%25,w:73.53%25,h:41.46%25/rs=w:900,cg:true",
    "patio_wide": "https://img1.wsimg.com/isteam/ip/0f231134-604e-4ca2-8a19-8f07d8fe5b53/20220921_112555.jpg/:/rs=w:1400,cg:true",
    "tile_bento": "https://img1.wsimg.com/isteam/ip/0f231134-604e-4ca2-8a19-8f07d8fe5b53/20221202_122646.jpg/:/cr=t:16.67%25,l:0%25,w:100%25,h:66.67%25/rs=w:900,cg:true",
    "tile_wide": "https://img1.wsimg.com/isteam/ip/0f231134-604e-4ca2-8a19-8f07d8fe5b53/20221202_122646.jpg/:/rs=w:1400,cg:true",
    "tub_bento": "https://img1.wsimg.com/isteam/ip/0f231134-604e-4ca2-8a19-8f07d8fe5b53/20231213_101300.jpg/:/cr=t:5.41%25,l:0%25,w:100%25,h:79.01%25/rs=w:900,cg:true",
    "tub_wide": "https://img1.wsimg.com/isteam/ip/0f231134-604e-4ca2-8a19-8f07d8fe5b53/20231213_101300.jpg/:/rs=w:1400,cg:true",
    "sink": "https://img1.wsimg.com/isteam/ip/0f231134-604e-4ca2-8a19-8f07d8fe5b53/20231220_104620.jpg/:/cr=t:16.65%25,l:0%25,w:100%25,h:66.7%25/rs=w:900,cg:true",
    "vanity_bento": "https://img1.wsimg.com/isteam/ip/0f231134-604e-4ca2-8a19-8f07d8fe5b53/20230414_105142.jpg/:/cr=t:13.09%25,l:27.49%25,w:40.44%25,h:67.57%25/rs=w:900,cg:true",
    "vanity_wide": "https://img1.wsimg.com/isteam/ip/0f231134-604e-4ca2-8a19-8f07d8fe5b53/20230414_105142.jpg/:/rs=w:1400,cg:true",
    "counter_bento": "https://img1.wsimg.com/isteam/ip/0f231134-604e-4ca2-8a19-8f07d8fe5b53/20231201_092005.jpg/:/rs=w:900,cg:true",
    "counter_wide": "https://img1.wsimg.com/isteam/ip/0f231134-604e-4ca2-8a19-8f07d8fe5b53/20231201_092005.jpg/:/rs=w:1400,cg:true",
    "cabinet_bento": "https://img1.wsimg.com/isteam/ip/0f231134-604e-4ca2-8a19-8f07d8fe5b53/Resized_20220723_151233.jpeg/:/cr=t:21.8%25,l:0%25,w:100%25,h:56.39%25/rs=w:900,cg:true",
    "cabinet_wide": "https://img1.wsimg.com/isteam/ip/0f231134-604e-4ca2-8a19-8f07d8fe5b53/Resized_20220723_151233.jpeg/:/rs=w:1400,cg:true",
    "cabinet_tight": "https://img1.wsimg.com/isteam/ip/0f231134-604e-4ca2-8a19-8f07d8fe5b53/Resized_20220723_151233.jpeg/:/cr=t:10%25,l:15%25,w:70%25,h:80%25/rs=w:900,cg:true",
    "flake_before": "https://img1.wsimg.com/isteam/ip/0f231134-604e-4ca2-8a19-8f07d8fe5b53/Flake%20Floor%20Before.jpg/:/rs=w:1400,cg:true",
    "flake_after": "https://img1.wsimg.com/isteam/ip/0f231134-604e-4ca2-8a19-8f07d8fe5b53/Flake%20Floor%202.jpg/:/rs=w:1400,cg:true",
}

# ─────────────────────────── Nav / Footer / Chat / Mobile-bar partials ───────────────────────────

NAV_ITEMS = [
    ("Services", "/services.html", [
        ("Garages", "/services/garages.html"),
        ("Patios", "/services/patios.html"),
        ("Tile", "/services/tile.html"),
        ("Tubs", "/services/tubs.html"),
        ("Vanities", "/services/vanities.html"),
        ("Countertops", "/services/countertops.html"),
        ("Cabinets", "/services/cabinets.html"),
        (None, None),
        ("Colors & Finishes", "/colors.html"),
        ("Project Visualizer", "/visualizer.html"),
    ]),
    ("Gallery", "/gallery.html", None),
    ("Process", "/process.html", None),
    ("About", "/about.html", None),
    ("Service Areas", "/service-areas.html", None),
    ("FAQ", "/faq.html", None),
    ("Reviews", "/reviews.html", None),
]


def logo_svg():
    return """<svg width="32" height="38" viewBox="0 0 34 40" fill="none" aria-hidden="true">
      <path d="M17 1L32 7.5V20C32 29 24.5 36 17 39C9.5 36 2 29 2 20V7.5L17 1Z" fill="#131419" stroke="#2a2d36" stroke-width="1"/>
      <path d="M17 3.5L30 9.5V20C30 27.5 23.5 34 17 37C10.5 34 4 27.5 4 20V9.5L17 3.5Z" fill="#0d0e11" stroke="#d4141f" stroke-width="1"/>
      <path d="M17 7L27 12V20C27 26 22.5 31.5 17 34C11.5 31.5 7 26 7 20V12L17 7Z" fill="#d4141f" opacity="0.92"/>
      <text x="8.2" y="24.5" font-family="Arial Black,sans-serif" font-size="11.5" font-weight="900" fill="#fff">PCT</text>
      <path d="M17 3.5L30 9.5V12.5L17 6.5L4 12.5V9.5L17 3.5Z" fill="rgba(200,204,212,0.12)"/>
    </svg>"""


def nav_html(active=""):
    links = []
    for label, href, sub in NAV_ITEMS:
        is_active = "active" if label == active else ""
        if sub:
            sub_html = []
            for sl, sh in sub:
                if sl is None:
                    sub_html.append('<div class="nav-drop-div"></div>')
                else:
                    sub_html.append(f'<a href="{sh}">{sl}</a>')
            links.append(f'''<li>
      <a href="{href}" class="{is_active}">{label} <span class="nav-caret">▾</span></a>
      <div class="nav-drop">{''.join(sub_html)}</div>
    </li>''')
        else:
            links.append(f'<li><a href="{href}" class="{is_active}">{label}</a></li>')
    return f"""<nav aria-label="Main navigation">
  <a href="/index.html" class="nav-brand" aria-label="Precision Coatings of Texas home">
    {logo_svg()}
    <div class="nav-brand-text">
      <div class="nav-name">PRECISION <em>COATINGS</em></div>
      <div class="nav-tag">Of Texas</div>
    </div>
  </a>
  <ul class="nav-links">
    {''.join(links)}
  </ul>
  <div class="nav-right">
    <a href="tel:{PHONE_TEL}" class="nav-phone">{PHONE}</a>
    <a href="/contact.html" class="btn btn-red btn-sm">Free Estimate</a>
    <button class="nav-burger" id="navBurger" aria-label="Open menu" aria-expanded="false">
      <span></span><span></span><span></span>
    </button>
  </div>
</nav>"""


def mobile_nav_html():
    rows = ['<a href="/index.html">Home</a>']
    for label, href, sub in NAV_ITEMS:
        rows.append(f'<a href="{href}">{label}</a>')
        if sub:
            sub_rows = []
            for sl, sh in sub:
                if sl:
                    sub_rows.append(f'<a href="{sh}">{sl}</a>')
            rows.append(f'<div class="mn-sub">{"".join(sub_rows)}</div>')
    rows.append('<a href="/contact.html">Contact</a>')
    return f'<div class="mobile-nav" id="mobileNav">{"".join(rows)}</div>'


def footer_html():
    return f"""<footer>
  <div class="foot-grid">
    <div>
      <div class="foot-brand-name">PRECISION <em>COATINGS</em> TX</div>
      <p class="foot-about">Transforming Surfaces With Precision. Locally owned &amp; operated, serving Austin &amp; Central Texas with premium materials and meticulous craftsmanship. Warranties on our work.</p>
      <div class="foot-contact">
        <a href="tel:{PHONE_TEL}"><span aria-hidden="true">📞</span> {PHONE}</a>
        <a href="mailto:{EMAIL}"><span aria-hidden="true">✉️</span> {EMAIL}</a>
        <div><span aria-hidden="true">📍</span> Hutto, TX · Serving Austin &amp; Central Texas</div>
        <div><span aria-hidden="true">💳</span> Cash · Check · Card · Square · Zelle</div>
      </div>
    </div>
    <div>
      <div class="foot-h">Services</div>
      <ul class="foot-links">
        <li><a href="/services/garages.html">Garages</a></li>
        <li><a href="/services/patios.html">Patios</a></li>
        <li><a href="/services/tile.html">Tile</a></li>
        <li><a href="/services/tubs.html">Tubs</a></li>
        <li><a href="/services/vanities.html">Vanities</a></li>
        <li><a href="/services/countertops.html">Countertops</a></li>
        <li><a href="/services/cabinets.html">Cabinets</a></li>
      </ul>
    </div>
    <div>
      <div class="foot-h">Company</div>
      <ul class="foot-links">
        <li><a href="/gallery.html">Our Work</a></li>
        <li><a href="/process.html">Our Process</a></li>
        <li><a href="/about.html">About Us</a></li>
        <li><a href="/service-areas.html">Service Areas</a></li>
        <li><a href="/faq.html">FAQ</a></li>
        <li><a href="/reviews.html">Reviews</a></li>
        <li><a href="/contact.html">Contact</a></li>
        <li><a href="https://coattexas.com/privacy-policy">Privacy Policy</a></li>
        <li><a href="https://coattexas.com/terms-and-conditions">Terms &amp; Conditions</a></li>
      </ul>
    </div>
    <div>
      <div class="foot-h">Hours — Open 7 Days</div>
      <ul class="foot-links">
        <li><a href="/contact.html">Mon–Fri: 8:00am – 6:00pm</a></li>
        <li><a href="/contact.html">Saturday: 8:00am – 12:00pm</a></li>
        <li><a href="/contact.html">Sunday: 8:00am – 12:00pm</a></li>
        <li style="margin-top:14px;"><a href="/contact.html" style="color:var(--red2);">✓ Free On-Site Estimates</a></li>
        <li><a href="/contact.html" style="color:var(--red2);">✓ Seasonal Discounts</a></li>
        <li><a href="/contact.html" style="color:var(--red2);">✓ Warranty Backed</a></li>
      </ul>
    </div>
  </div>
  <div class="foot-bottom">
    <div class="foot-copy">© 2025 Precision Coatings of Texas LLC · All Rights Reserved</div>
    <div class="foot-copy">Hutto, TX · <span>{PHONE}</span> · coattexas.com</div>
  </div>
</footer>"""


def chat_widget_html():
    return f"""<div class="mobile-bar">
  <a href="tel:{PHONE_TEL}" class="btn btn-ghost btn-sm">📞 Call Now</a>
  <button class="btn btn-red btn-sm" onclick="openChat()">Free Estimate</button>
</div>

<div class="chat-fab-wrap">
  <div class="chat-hint" id="chatHint"><strong>👋 Free estimate</strong> in about 2 minutes — no phone call needed.</div>
  <button class="chat-fab" id="chatFab" onclick="toggleChat()" aria-label="Open AI estimator chat">
    <svg viewBox="0 0 24 24" id="fabIco" aria-hidden="true"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg>
    <span class="chat-dot" aria-hidden="true"></span>
  </button>
</div>

<div class="chat-win" id="chatWin" role="dialog" aria-label="AI Estimator chat">
  <div class="chat-hdr">
    <div class="chat-av" aria-hidden="true">PCT</div>
    <div>
      <div class="chat-name">PCT AI Estimator</div>
      <div class="chat-status">Online · Instant replies</div>
    </div>
    <button class="chat-x" onclick="toggleChat()" aria-label="Close chat">✕</button>
  </div>
  <div class="chat-msgs" id="chatMsgs" aria-live="polite"></div>
  <div class="qr-row" id="qrRow"></div>
  <div class="chat-inp-row">
    <textarea class="chat-inp" id="chatInp" placeholder="Ask about services or get a free estimate..." rows="1" onkeydown="handleKey(event)" oninput="autoResize(this)" aria-label="Type your message"></textarea>
    <button class="chat-send" id="sendBtn" onclick="sendMsg()" aria-label="Send message">
      <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M22 2L11 13M22 2l-7 20-4-9-9-4 20-7z"/></svg>
    </button>
  </div>
</div>"""


def page(*, title, description, active="", body, extra_js=None, canonical="/", og_image=None):
    extra_js_tags = "\n".join(f'<script src="{s}"></script>' for s in (extra_js or []))
    og = og_image or IMG["hero_home"]
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{description}">
<link rel="canonical" href="https://coattexas.com{canonical}">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 34 40'%3E%3Cpath d='M17 1L32 7.5V20C32 29 24.5 36 17 39C9.5 36 2 29 2 20V7.5L17 1Z' fill='%23131419' stroke='%232a2d36'/%3E%3Cpath d='M17 7L27 12V20C27 26 22.5 31.5 17 34C11.5 31.5 7 26 7 20V12L17 7Z' fill='%23d4141f'/%3E%3C/svg%3E">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:image" content="{og}">
<meta property="og:type" content="website">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800;900&family=DM+Mono:wght@400;500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/css/style.css">
</head>
<body>

{nav_html(active)}
{mobile_nav_html()}

{body}

{chat_widget_html()}

<script src="/assets/js/site.js"></script>
{extra_js_tags}
</body>
</html>
"""


def write(path, html):
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w") as f:
        f.write(html)
    print("wrote", path, len(html), "bytes")


# ─────────────────────────── Reusable content blocks ───────────────────────────

def marquee_html():
    items = ["Garages","Patios","Tile","Tubs","Vanities","Countertops","Cabinets","Free Estimates"]
    row = "".join(f'<span class="marquee-item">{i}</span>' for i in items)
    return f'''<div class="marquee-strip" aria-hidden="true">
  <div class="marquee-track">{row}{row}</div>
</div>'''


def cta_band_html(title_html, sub):
    return f'''<div class="cta-band rv">
  <div>
    <h2 class="cta-title">{title_html}</h2>
    <p class="cta-sub">{sub}</p>
  </div>
  <div class="cta-actions">
    <button class="btn btn-white btn-lg" onclick="openChat()">
      <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" aria-hidden="true"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg>
      Chat with AI Estimator
    </button>
    <a href="tel:{PHONE_TEL}" class="btn btn-white-ol btn-lg">📞 {PHONE}</a>
  </div>
</div>'''


TESTIMONIALS = [
    {
        "text": "Our old cast iron tub was reglazed and the result was stunning — it genuinely looks brand new. I'd recommend Precision Coatings to anyone without hesitation.",
        "initials": "TB", "name": "Tub Reglazing Client", "loc": "Verified Review · Thumbtack",
    },
    {
        "text": "Chris arrived exactly when promised, kept the entire work area spotless, and communicated every step. The tub resurfacing looks wonderful.",
        "initials": "TR", "name": "Tub Resurfacing Client", "loc": "Verified Review · Thumbtack",
    },
    {
        "text": "I wanted new countertops but resurfacing turned out far more economical. They changed the whole look of my bathroom in a single day — then came back to make sure I was satisfied.",
        "initials": "KF", "name": "Kimberly F.", "loc": "Verified Review · HomeAdvisor",
    },
]


def testimonials_html(intro=True):
    cards = []
    for t in TESTIMONIALS:
        cards.append(f'''<div class="testi rv">
        <div class="testi-stars" aria-label="5 out of 5 stars">★★★★★</div>
        <p class="testi-text">{t['text']}</p>
        <div class="testi-who">
          <div class="testi-av" aria-hidden="true">{t['initials']}</div>
          <div><div class="testi-name">{t['name']}</div><div class="testi-loc">{t['loc']}</div></div>
        </div>
      </div>''')
    head = '''<div class="sec-head rv">
      <div class="sec-kicker">Client Reviews</div>
      <h2 class="sec-title">Texas <span class="thin">approved.</span></h2>
    </div>''' if intro else ''
    return f'''<section id="reviews">
  <div class="wrap">
    {head}
    <div class="testis">
      {''.join(cards)}
    </div>
    <p style="text-align:center;margin-top:24px;font-size:12px;color:var(--muted);">Rated 5.0 on HomeAdvisor · Top Pro on Thumbtack · Reviews paraphrased from verified public profiles</p>
  </div>
</section>'''


PROCESS_STEPS = [
    ("💬", "Free Consultation", "Chat with our AI estimator or call us direct. Tell us about your surface — no pressure, no obligation.",
     "We'll ask about the surface, approximate size, and what look you're going for so we can point you toward the right system before anyone sets foot on site."),
    ("📐", "On-Site Assessment", "We inspect your surface, take measurements, and deliver a detailed written quote with coating options.",
     "Our team checks for moisture, cracking, prior coatings, and substrate condition — the things that determine which prep method and system will actually last."),
    ("🛠", "Expert Installation", "Full prep — grinding, repair, priming — then precision coating application with professional-grade systems.",
     "Every job starts with mechanical surface prep, not just a quick clean. Cracks and chips are repaired before any coating goes down."),
    ("✅", "Final Walkthrough", "We inspect every inch with you before we leave. 100% satisfaction — that's the PCT guarantee.",
     "We walk the finished surface with you, point out cure-time care instructions, and make sure you're fully happy before we call the job done."),
]


def process_steps_html(detailed=False):
    cards = []
    for ico, name, desc, detail in PROCESS_STEPS:
        extra = f'<p class="step-detail">{detail}</p>' if detailed else ''
        cards.append(f'''<div class="step rv">
        <div class="step-chip">{ico}</div>
        <div class="step-name">{name}</div>
        <p class="step-desc">{desc}</p>
        {extra}
      </div>''')
    return f'''<div class="steps">
      {''.join(cards)}
    </div>'''


VALUE_PROPS = [
    ("🏆", "10+ Years Experience", "Serving Austin & Central Texas homeowners since 2014."),
    ("⭐", "5.0★ HomeAdvisor Rated", "Top Pro on Thumbtack with verified 5-star reviews."),
    ("💵", "$0 On-Site Estimates", "Free, no-obligation quotes — every project, every time."),
    ("🛡", "Warranty Backed", "Workmanship warranties on every coating system we install."),
]


def value_grid_html():
    cards = "".join(f'''<div class="value-card rv">
      <div class="value-ico">{ico}</div>
      <div class="value-name">{name}</div>
      <div class="value-desc">{desc}</div>
    </div>''' for ico, name, desc in VALUE_PROPS)
    return f'<div class="value-grid">{cards}</div>'


# ─────────────────────────── Service catalog (shared by hub + detail pages) ───────────────────────────

SERVICES = [
    {
        "slug": "garages", "name": "Garages", "tag": "Most Popular",
        "hero_img": IMG["hero_home"], "card_img": IMG["garage_bento"],
        "shot_a": IMG["garage_alt"], "shot_b": IMG["garage_2024"],
        "short": "Flake, metallic & solid epoxy systems built for Texas heat, hot tires, and decades of daily use.",
        "kicker": "Garage Floor Coatings",
        "title_html": "Garage floors that<br><span class=\"thin\">outlast the heat.</span>",
        "intro": "A bare or worn concrete garage floor takes a beating in Central Texas — hot tires, dropped tools, oil, and UV exposure through an open door. We resurface it with a professional-grade epoxy or polyaspartic system engineered to handle all of it, without the dust and mess of a full tear-out.",
        "sections": [
            ("What's included", [
                "Full mechanical surface prep — diamond grinding, not just acid etching",
                "Crack, pit, and spall repair before any coating goes down",
                "Flake, metallic, solid color, or natural-accent finish systems",
                "UV-stable topcoat so color doesn't yellow or fade in direct sun",
                "Optional non-slip texture additive",
                "Finished floor ready for vehicle traffic on the timeline we confirm on-site",
            ]),
            ("Why resurface instead of replace", [
                "Covers stains, cracking, and pitting without repouring concrete",
                "A sealed, seamless surface is far easier to sweep and hose down than bare concrete",
                "Professional-grade systems resist hot tire pickup and everyday chemicals",
                "Finished in a fraction of the time a full concrete replacement would take",
            ]),
        ],
        "sidebar_facts": [
            ("Best for", "Garage floors, workshop floors, shop bays"),
            ("Finish families", "Flake · Metallic · Solid · Natural Accent"),
            ("Popular colors", "Quicksilver, Stonehenge, Chrome Silver"),
        ],
        "related": ["patios", "tile", "countertops"],
    },
    {
        "slug": "patios", "name": "Patios", "tag": None,
        "hero_img": IMG["patio_wide"], "card_img": IMG["patio_bento"],
        "shot_a": IMG["patio_wide"], "shot_b": IMG["garage_bento"],
        "short": "UV-stable overlays, stains & non-slip finishes for outdoor living.",
        "kicker": "Patio & Outdoor Coatings",
        "title_html": "Outdoor surfaces,<br><span class=\"thin\">built for real weather.</span>",
        "intro": "Patios take direct sun, rain, and foot traffic year-round. We apply UV-stable overlays, stains, and non-slip finishes designed to hold their color and texture outdoors — including our Natural Accent Texas Sand system, a customer favorite for pool decks and covered patios alike.",
        "sections": [
            ("What's included", [
                "Surface prep and repair of cracked or spalled concrete",
                "UV-stable overlays and stains that resist sun fading",
                "Non-slip texture additive for pool decks and entryways",
                "Natural Accent and stone-look finish options",
                "Seamless coverage over expansion joints and control joints where appropriate",
            ]),
            ("A real project", [
                "One recent patio was finished in our Natural Accent Texas Sand system with a non-slip additive — a warm, stone-like look that stays cool underfoot and grips well when wet.",
            ]),
        ],
        "sidebar_facts": [
            ("Best for", "Patios, pool decks, walkways, covered porches"),
            ("Finish families", "Natural Accent · Stain · Solid"),
            ("Popular colors", "Texas Sand, Walnut, Aged Leather"),
        ],
        "related": ["garages", "tile", "countertops"],
    },
    {
        "slug": "tile", "name": "Tile", "tag": None,
        "hero_img": IMG["tile_wide"], "card_img": IMG["tile_bento"],
        "shot_a": IMG["tile_wide"], "shot_b": IMG["tub_bento"],
        "short": "Seamless epoxy over existing tile — no demo, no grout lines, easy clean.",
        "kicker": "Tile Resurfacing",
        "title_html": "Skip the demo.<br><span class=\"thin\">Resurface the tile.</span>",
        "intro": "Dated or cracked tile doesn't always need to be torn out. We apply a seamless epoxy resurfacing system directly over existing tile — eliminating grout lines, closing up cracks, and leaving an easy-to-clean surface without the dust, demolition, or downtime of a full retile.",
        "sections": [
            ("What's included", [
                "Deep clean and mechanical prep of the existing tile surface",
                "Repair of cracked or missing tile sections before coating",
                "Seamless epoxy application that closes grout lines for easier cleaning",
                "Satin, gloss, or matte topcoat options",
                "No demolition — dramatically less mess and downtime than a retile",
            ]),
        ],
        "sidebar_facts": [
            ("Best for", "Kitchen & bath floors, entryways, existing tile in good structural condition"),
            ("Finish families", "Solid · Flake"),
            ("Turnaround", "Confirmed on your free on-site estimate"),
        ],
        "related": ["tubs", "vanities", "countertops"],
    },
    {
        "slug": "tubs", "name": "Tubs", "tag": None,
        "hero_img": IMG["tub_wide"], "card_img": IMG["tub_bento"],
        "shot_a": IMG["tub_wide"], "shot_b": IMG["sink"],
        "short": "Chip & rust repair, reglazing — most tubs done in 2 days. Cast iron, porcelain, fiberglass & acrylic.",
        "kicker": "Tub Reglazing & Repair",
        "title_html": "A brand-new tub,<br><span class=\"thin\">without the demo.</span>",
        "intro": "Chipped, rusted, or dull tubs and sinks are one of the most economical restorations we do. We repair chips and rust damage, then reglaze the surface for a like-new finish — on cast iron, porcelain, fiberglass, and acrylic. Most tubs are completed in about two days.",
        "sections": [
            ("What's included", [
                "Chip and rust repair before reglazing",
                "Full reglazing on cast iron, porcelain, fiberglass, or acrylic",
                "Sink refinishing available alongside tub work",
                "Most tubs completed in about 2 days",
            ]),
            ("What clients say", [
                "\"Our old cast iron tub was reglazed and the result was stunning — it genuinely looks brand new.\" — Verified Thumbtack review",
            ]),
        ],
        "sidebar_facts": [
            ("Best for", "Cast iron, porcelain, fiberglass & acrylic tubs and sinks"),
            ("Typical timeline", "Most tubs done in about 2 days"),
            ("Also covers", "Chip repair · Rust repair · Sink refinishing"),
        ],
        "related": ["vanities", "countertops", "cabinets"],
    },
    {
        "slug": "vanities", "name": "Vanities", "tag": None,
        "hero_img": IMG["vanity_wide"], "card_img": IMG["vanity_bento"],
        "shot_a": IMG["vanity_wide"], "shot_b": IMG["counter_bento"],
        "short": "Dated vanities transformed without the cost of replacement.",
        "kicker": "Vanity Refinishing",
        "title_html": "Update the vanity.<br><span class=\"thin\">Skip the remodel.</span>",
        "intro": "A dated bathroom vanity can drag down an otherwise updated room. We refinish the vanity top — and coordinate with our cabinet and countertop work when you want the whole vanity refreshed — for a fraction of what a full replacement and plumbing rework would cost.",
        "sections": [
            ("What's included", [
                "Surface prep and repair of chips, cracks, or worn finish",
                "Refinishing in solid, stone-look, or custom-matched colors",
                "Optional pairing with cabinet refinishing for a full vanity refresh",
                "Sink and faucet areas carefully masked and protected",
            ]),
        ],
        "sidebar_facts": [
            ("Best for", "Bathroom vanity tops and integrated sinks"),
            ("Pairs well with", "Cabinets · Countertops · Tile"),
            ("Finish families", "Solid · Stone-look"),
        ],
        "related": ["cabinets", "countertops", "tubs"],
    },
    {
        "slug": "countertops", "name": "Countertops", "tag": None,
        "hero_img": IMG["counter_wide"], "card_img": IMG["counter_bento"],
        "shot_a": IMG["counter_wide"], "shot_b": IMG["cabinet_bento"],
        "short": "Fresh stone-look finishes at a fraction of replacement cost.",
        "kicker": "Countertop Refinishing",
        "title_html": "Stone-look counters,<br><span class=\"thin\">without the slab price.</span>",
        "intro": "Replacing a countertop means new templates, fabrication, and installation — often days of disruption. Refinishing gets you a fresh stone-look surface, usually completed far faster, at a fraction of the cost of replacement.",
        "sections": [
            ("What's included", [
                "Surface prep, degreasing, and repair of chips or seams",
                "Stone-look and solid finish systems",
                "Food-safe topcoat options for kitchen counters",
                "Backsplash refinishing available alongside countertops",
            ]),
            ("What a client said", [
                "\"I wanted new countertops but resurfacing turned out far more economical. They changed the whole look of my bathroom in a single day.\" — Kimberly F., verified HomeAdvisor review",
            ]),
        ],
        "sidebar_facts": [
            ("Best for", "Kitchen & bathroom countertops, backsplashes"),
            ("Finish families", "Stone-look · Solid"),
            ("Pairs well with", "Cabinets · Vanities · Tile"),
        ],
        "related": ["cabinets", "vanities", "tile"],
    },
    {
        "slug": "cabinets", "name": "Cabinets", "tag": "New",
        "hero_img": IMG["cabinet_wide"], "card_img": IMG["cabinet_bento"],
        "shot_a": IMG["cabinet_wide"], "shot_b": IMG["cabinet_tight"],
        "short": "Kitchen & bath cabinets refinished — skip the demo mess.",
        "kicker": "Cabinet Refinishing",
        "title_html": "Cabinets refinished,<br><span class=\"thin\">not torn out.</span>",
        "intro": "Full cabinet replacement means weeks of lead time, demolition, and a kitchen or bathroom out of commission. Refinishing gives dated or worn kitchen and bathroom cabinets a like-new, durable enamel finish — doors, drawer fronts, and boxes — without the demo mess or the replacement price tag.",
        "sections": [
            ("What's included", [
                "Doors and drawer fronts cleaned, degreased, and prepped",
                "Sanding or deglossing so the new finish bonds properly",
                "Professional-grade enamel finish, sprayed or hand-finished",
                "Hardware removed and reinstalled (or updated on request)",
                "Kitchen and bathroom cabinets both in scope",
            ]),
            ("Why refinish instead of replace", [
                "No demolition, no waiting on custom cabinet lead times",
                "A fraction of the disruption of a full kitchen or bathroom remodel",
                "Durable enamel finish built to handle daily kitchen and bath use",
                "Coordinates cleanly with our countertop and vanity refinishing for a full-room refresh",
            ]),
            ("Finish options", [
                "Solid enamel colors — Onyx Black, Pearl White, and Slate Gray are popular cabinet choices from our Solid collection",
                "Full custom color matching available on every project",
                "Satin, gloss, or matte topcoat",
            ]),
        ],
        "sidebar_facts": [
            ("Best for", "Kitchen cabinets, bathroom vanity cabinet boxes"),
            ("Finish families", "Solid enamel · Custom match"),
            ("Pairs well with", "Countertops · Vanities · Tile"),
        ],
        "related": ["vanities", "countertops", "tile"],
    },
]

SERVICES_BY_SLUG = {s["slug"]: s for s in SERVICES}


def bento_html():
    cells = []
    css_area = {"garages":"b-garage","patios":"b-patio","tile":"b-tile","tubs":"b-tubs",
                "vanities":"b-vanity","countertops":"b-counter","cabinets":"b-cabinet"}
    for s in SERVICES:
        tag = f'<div class="bento-tag">{s["tag"]}</div>' if s["tag"] else ''
        cells.append(f'''<a class="bento-cell {css_area[s['slug']]} rv" href="/services/{s['slug']}.html">
        <img src="{s['card_img']}" alt="{s['name']} coating by Precision Coatings of Texas" loading="lazy">
        <div class="bento-grad"></div>
        {tag}
        <div class="bento-arrow" aria-hidden="true">→</div>
        <div class="bento-content">
          <div class="bento-name">{s['name']}</div>
          <div class="bento-desc">{s['short']}</div>
        </div>
      </a>''')
    return f'''<div class="bento">
      {''.join(cells)}
    </div>'''


def related_services_html(slugs):
    chips = "".join(f'<a class="related-chip" href="/services/{s}.html">{SERVICES_BY_SLUG[s]["name"]} →</a>' for s in slugs)
    return f'<div class="related-svcs">{chips}</div>'


def breadcrumb(*crumbs):
    """crumbs: list of (label, href_or_None-for-current)"""
    parts = []
    for label, href in crumbs:
        if href:
            parts.append(f'<a href="{href}">{label}</a>')
        else:
            parts.append(f'<span>{label}</span>')
    return f'<div class="breadcrumb">{" <span>/</span> ".join(parts)}</div>'


def page_hero(kicker, title_html, sub, img=None, crumbs=None, ctas=""):
    cls = "page-hero" if img else "page-hero no-img"
    bg = f'''<div class="page-hero-bg" aria-hidden="true"><img src="{img}" alt="" loading="eager"></div>
  <div class="page-hero-veil"></div>''' if img else ''
    bc = breadcrumb(*crumbs) if crumbs else ''
    return f'''<header class="{cls}">
  {bg}
  <div class="page-hero-inner">
    {bc}
    <div class="page-kicker">{kicker}</div>
    <h1 class="page-title">{title_html}</h1>
    <p class="page-sub">{sub}</p>
    {ctas}
  </div>
</header>'''


# ═══════════════════════════════════════════════════════════════════════════
# HOME
# ═══════════════════════════════════════════════════════════════════════════

def build_home():
    body = f'''<header class="hero" id="top">
  <div class="hero-bg" aria-hidden="true">
    <img src="{IMG['hero_home']}" alt="" loading="eager">
    <div class="hero-veil"></div>
  </div>
  <div class="hero-inner">
    <div class="hero-kicker">Transforming Surfaces With Precision · Serving Austin &amp; Central Texas</div>
    <h1 class="hero-title">
      EVERY SURFACE<br>
      <span class="thin">deserves a</span> <span class="red">second life.</span>
    </h1>
    <p class="hero-sub">Garages, patios, tile, tubs, vanities, countertops &amp; cabinets — restored to better-than-new with professional-grade coatings. Serving Central Texas since 2014.</p>
    <div class="hero-ctas">
      <button class="btn btn-red btn-lg" onclick="openChat()">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2.4" aria-hidden="true"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg>
        Get Free Estimate
      </button>
      <a href="/visualizer.html" class="btn btn-red btn-lg">Try Visualizer</a>
      <a href="/gallery.html" class="btn btn-ghost btn-lg">See Transformations</a>
    </div>
    <div class="hero-proof">
      <div class="proof-item"><span class="proof-num">10<em>+</em></span><span class="proof-lbl">Years Experience</span></div>
      <div class="proof-item"><span class="proof-num">5.0<em>★</em></span><span class="proof-lbl">HomeAdvisor Rated</span></div>
      <div class="proof-item"><span class="proof-num">7<em>/7</em></span><span class="proof-lbl">Open Every Day</span></div>
      <div class="proof-item"><span class="proof-num">$0</span><span class="proof-lbl">On-Site Estimates</span></div>
    </div>
  </div>
</header>

{marquee_html()}

<section id="services">
  <div class="wrap">
    <div class="sec-head rv">
      <div class="sec-kicker">What We Refinish</div>
      <h2 class="sec-title">Seven surfaces.<br><span class="thin">One standard — flawless.</span></h2>
      <p class="sec-sub">Each service has its own dedicated page with full details, finish options, and real project photos.</p>
    </div>
    {bento_html()}
    <div style="text-align:center;margin-top:36px;" class="rv">
      <a href="/services.html" class="btn btn-ghost">See All Services →</a>
    </div>
  </div>
</section>

<section id="gallery-teaser" class="tight">
  <div class="wrap">
    <div class="sec-head rv">
      <div class="sec-kicker">Gallery</div>
      <h2 class="sec-title">Real jobs.<br><span class="thin">Real results.</span></h2>
      <p class="sec-sub">Drag the slider to watch a transformation, then browse the full gallery.</p>
    </div>
    <div class="ba-slider rv" id="baSlider" role="slider" aria-label="Before and after comparison slider" aria-valuemin="0" aria-valuemax="100" aria-valuenow="50" tabindex="0">
      <div class="ba-img ba-before-wrap">
        <img src="{IMG['flake_before']}" alt="Garage floor before coating — bare cracked concrete" loading="lazy">
      </div>
      <div class="ba-img ba-after-wrap" id="baAfter">
        <img src="{IMG['flake_after']}" alt="Same garage floor after professional flake epoxy coating" loading="lazy">
      </div>
      <div class="ba-divider" id="baDivider"></div>
      <div class="ba-handle" id="baHandle" aria-hidden="true">⇄</div>
      <div class="ba-label before">Before</div>
      <div class="ba-label after">After</div>
    </div>
    <p class="ba-hint">← Drag the handle or use arrow keys →</p>
    <div style="text-align:center;margin-top:36px;" class="rv">
      <a href="/gallery.html" class="btn btn-ghost">View Full Gallery →</a>
    </div>
  </div>
</section>

<section id="process" class="process-band">
  <div class="wrap">
    <div class="sec-head rv">
      <div class="sec-kicker">How It Works</div>
      <h2 class="sec-title">Four steps.<br><span class="thin">Zero hassle.</span></h2>
    </div>
    {process_steps_html()}
    <div style="text-align:center;margin-top:36px;" class="rv">
      <a href="/process.html" class="btn btn-ghost">More About Our Process →</a>
    </div>
  </div>
</section>

{testimonials_html()}

{cta_band_html("Ready to transform<br>your surface?", "Free on-site estimates · Open 7 days a week · Warranty backed · Serving Austin &amp; Central Texas")}

{footer_html()}'''
    write("index.html", page(
        title="Precision Coatings of Texas — Surface Refinishing Specialists | Austin, TX",
        description="Austin's premier surface coating specialists. Garages, patios, tile, tubs, vanities, countertops & cabinets. Free estimates — 512-537-7951.",
        active="",
        body=body,
        extra_js=["/assets/js/ba-slider.js"],
        canonical="/",
    ))


# ═══════════════════════════════════════════════════════════════════════════
# SERVICES HUB
# ═══════════════════════════════════════════════════════════════════════════

def build_services_hub():
    cards = []
    for i, s in enumerate(SERVICES, 1):
        tag = f'<div class="svc-card-num">{"NEW" if s["tag"]=="New" else f"0{i}"}</div>'
        cards.append(f'''<a class="svc-card rv" href="/services/{s['slug']}.html">
      <div class="svc-card-img">
        <img src="{s['card_img']}" alt="{s['name']} refinishing by Precision Coatings of Texas" loading="lazy">
        {tag}
      </div>
      <div class="svc-card-body">
        <div class="svc-card-name">{s['name']}</div>
        <p class="svc-card-desc">{s['short']}</p>
        <span class="svc-card-link">Explore {s['name']} →</span>
      </div>
    </a>''')

    body = f'''{page_hero(
        "What We Refinish",
        'Seven surfaces.<br><span class="thin">One standard of craftsmanship.</span>',
        "From garage floors to kitchen cabinets, every surface gets the same mechanical prep, professional-grade coating systems, and final walkthrough — backed by a workmanship warranty.",
        img=IMG['hero_home'],
        crumbs=[("Home","/index.html"),("Services",None)],
    )}

<section class="tight">
  <div class="wrap">
    <div class="svc-grid">
      {''.join(cards)}
    </div>
  </div>
</section>

<section class="tight">
  <div class="wrap">
    <div class="sec-head rv">
      <div class="sec-kicker">Finish It Off</div>
      <h2 class="sec-title">Colors &amp; the <span class="thin">Project Visualizer.</span></h2>
      <p class="sec-sub">Every service ships with dozens of finish options and free custom color matching. Not sure what it'll look like? Upload a photo and preview it first.</p>
    </div>
    <div class="value-grid">
      <a class="value-card rv" href="/colors.html" style="text-decoration:none;display:block;">
        <div class="value-ico">🎨</div>
        <div class="value-name">Browse Colors &amp; Finishes</div>
        <div class="value-desc">Flake, metallic, solid, stain, natural accent &amp; StoneFlecks Ultra™ collections.</div>
      </a>
      <a class="value-card rv" href="/visualizer.html" style="text-decoration:none;display:block;">
        <div class="value-ico">🖼</div>
        <div class="value-name">Try the AI Visualizer</div>
        <div class="value-desc">Upload a photo of your space and preview a finish before you commit.</div>
      </a>
      <a class="value-card rv" href="/process.html" style="text-decoration:none;display:block;">
        <div class="value-ico">📐</div>
        <div class="value-name">See Our Process</div>
        <div class="value-desc">Consultation → assessment → installation → walkthrough.</div>
      </a>
      <a class="value-card rv" href="/contact.html" style="text-decoration:none;display:block;">
        <div class="value-ico">💬</div>
        <div class="value-name">Get a Free Estimate</div>
        <div class="value-desc">No-obligation on-site quotes, every time.</div>
      </a>
    </div>
  </div>
</section>

{cta_band_html("Not sure which service<br>you need?", "Chat with our AI estimator — describe your project and we'll point you to the right fix.")}

{footer_html()}'''
    write("services.html", page(
        title="All Services — Garages, Patios, Tile, Tubs, Vanities, Countertops & Cabinets | Precision Coatings of Texas",
        description="Every surface coating service Precision Coatings of Texas offers in Austin & Central Texas: garages, patios, tile, tubs, vanities, countertops, and cabinets.",
        active="Services",
        body=body,
        canonical="/services.html",
    ))


# ═══════════════════════════════════════════════════════════════════════════
# SERVICE DETAIL PAGES
# ═══════════════════════════════════════════════════════════════════════════

def build_service_page(s):
    sections_html = []
    for heading, items in s["sections"]:
        lis = "".join(f'<li>{it}</li>' for it in items)
        sections_html.append(f'<h2>{heading}</h2><ul class="svc-list">{lis}</ul>')

    sidebar_rows = "".join(
        f'<div class="sb-row"><span>{k}</span><strong>{v}</strong></div>' for k, v in s["sidebar_facts"]
    )

    svc_ctas = ('<div class="page-ctas">'
                '<button class="btn btn-red btn-lg" onclick="openChat()">Get Free Estimate</button>'
                '<a href="/colors.html" class="btn btn-ghost btn-lg">Browse Finishes</a>'
                '</div>')

    body = f'''{page_hero(
        s["kicker"],
        s["title_html"],
        s["intro"],
        img=s["hero_img"],
        crumbs=[("Home","/index.html"),("Services","/services.html"),(s["name"],None)],
        ctas=svc_ctas,
    )}

<section class="tight">
  <div class="wrap">
    <div class="svc-layout">
      <div class="svc-body">
        {''.join(sections_html)}
        <div class="svc-shot-row rv">
          <div class="svc-shot"><img src="{s['shot_a']}" alt="{s['name']} project by Precision Coatings of Texas" loading="lazy"></div>
          <div class="svc-shot"><img src="{s['shot_b']}" alt="{s['name']} detail by Precision Coatings of Texas" loading="lazy"></div>
        </div>
        <h2>Other services to consider</h2>
        {related_services_html(s["related"])}
      </div>
      <div class="svc-sidebar">
        <div class="sb-card rv">
          <div class="sb-h">Quick Facts</div>
          {sidebar_rows}
          <button class="btn btn-red" onclick="openChat()">Get Free Estimate</button>
          <a href="tel:{PHONE_TEL}" class="btn btn-ghost">📞 {PHONE}</a>
        </div>
        <div class="sb-card rv">
          <div class="sb-h">Why PCT</div>
          <div class="sb-row" style="border-top:none;"><span>Experience</span><strong>10+ Years</strong></div>
          <div class="sb-row"><span>Rating</span><strong>5.0★ HomeAdvisor</strong></div>
          <div class="sb-row"><span>Estimates</span><strong>Free, On-Site</strong></div>
          <div class="sb-row"><span>Warranty</span><strong>Backed</strong></div>
        </div>
      </div>
    </div>
  </div>
</section>

{testimonials_html(intro=False)}

{cta_band_html(f"Ready to refinish your {s['name'].lower()}?", "Free on-site estimates · Open 7 days a week · Warranty backed · Serving Austin &amp; Central Texas")}

{footer_html()}'''
    write(f"services/{s['slug']}.html", page(
        title=f"{s['name']} Refinishing — Precision Coatings of Texas | Austin, TX",
        description=f"{s['short']} Free on-site estimates. Serving Austin & Central Texas. 512-537-7951.",
        active="Services",
        body=body,
        canonical=f"/services/{s['slug']}.html",
        og_image=s["hero_img"],
    ))


# ═══════════════════════════════════════════════════════════════════════════
# GALLERY
# ═══════════════════════════════════════════════════════════════════════════

WORK_ITEMS = [
    (IMG["garage_signature"], "Featured Project", "PCT Signature Finish", "tall",
     "Precision Coatings flagship floor project"),
    (IMG["garage_alt"], "Garage · Flake System", "Built for Vehicles & Equipment", "",
     "Garage floor coated for maximum durability"),
    (IMG["patio_bento"], "Patio · Natural Accent", "Texas Sand + Non-Slip", "",
     "Patio resurfaced in Natural Accent Texas Sand with non-slip additive"),
    (IMG["sink"], "Sink Refinishing", "Restored Original Luster", "",
     "Refinished sink with restored luster"),
    (IMG["garage_2024"], "Garage · 2024", "Flake Detail", "",
     "Recent garage flake coating detail 2024"),
    (IMG["tub_bento"], "Tub Refinishing", "Cast Iron Reglazed", "",
     "Professionally refinished bathtub and shower by PCT"),
    (IMG["tile_bento"], "Tile Resurfacing", "Seamless Epoxy Over Tile", "",
     "Resurfaced tile floor"),
    (IMG["counter_bento"], "Countertop Refinishing", "Stone-Look Finish", "",
     "Refinished countertop"),
    (IMG["vanity_bento"], "Vanity Refinishing", "Bathroom Vanity Update", "",
     "Refinished bathroom vanity"),
    (IMG["cabinet_bento"], "Cabinet Refinishing", "Kitchen Cabinets Refreshed", "",
     "Refinished kitchen cabinets"),
]


def build_gallery():
    cards = "".join(f'''<div class="work-card {tall} rv">
        <img src="{img}" alt="{alt}" loading="lazy">
        <div class="work-info"><div class="work-type">{typ}</div><div class="work-name">{name}</div></div>
      </div>''' for img, typ, name, tall, alt in WORK_ITEMS)

    body = f'''{page_hero(
        "Gallery",
        'Real jobs.<br><span class="thin">Real results.</span>',
        "Every photo here is an actual Precision Coatings of Texas project. Drag the slider below to see a full garage floor transformation, then browse recent work across every service.",
        img=IMG['garage_signature'],
        crumbs=[("Home","/index.html"),("Gallery",None)],
    )}

<section class="tight">
  <div class="wrap">
    <div class="ba-slider rv" id="baSlider" role="slider" aria-label="Before and after comparison slider" aria-valuemin="0" aria-valuemax="100" aria-valuenow="50" tabindex="0">
      <div class="ba-img ba-before-wrap">
        <img src="{IMG['flake_before']}" alt="Garage floor before coating — bare cracked concrete" loading="lazy">
      </div>
      <div class="ba-img ba-after-wrap" id="baAfter">
        <img src="{IMG['flake_after']}" alt="Same garage floor after professional flake epoxy coating" loading="lazy">
      </div>
      <div class="ba-divider" id="baDivider"></div>
      <div class="ba-handle" id="baHandle" aria-hidden="true">⇄</div>
      <div class="ba-label before">Before</div>
      <div class="ba-label after">After</div>
    </div>
    <p class="ba-hint">← Drag the handle or use arrow keys →</p>

    <div class="work-grid" style="margin-top:48px;">
      {cards}
    </div>
  </div>
</section>

{cta_band_html("Want results like these<br>on your surface?", "Free on-site estimates · Open 7 days a week · Warranty backed · Serving Austin &amp; Central Texas")}

{footer_html()}'''
    write("gallery.html", page(
        title="Project Gallery — Before & After Photos | Precision Coatings of Texas",
        description="Real before-and-after photos from Precision Coatings of Texas projects across Austin & Central Texas — garages, patios, tile, tubs, vanities, countertops & cabinets.",
        active="Gallery",
        body=body,
        extra_js=["/assets/js/ba-slider.js"],
        canonical="/gallery.html",
        og_image=IMG["garage_signature"],
    ))


# ═══════════════════════════════════════════════════════════════════════════
# COLORS
# ═══════════════════════════════════════════════════════════════════════════

def swatch(name, cat, img=None, style=None, note=""):
    inner = f'<img src="{img}" alt="{name} texture swatch" loading="lazy">' if img else ''
    chip_style = f' style="{style}"' if style else ''
    chip_cls = "swatch-chip" if img else "swatch-chip generated-swatch" if style is None and not img else "swatch-chip"
    if img:
        chip = f'<div class="swatch-chip">{inner}</div>'
    elif style:
        chip = f'<div class="swatch-chip" style="{style}"></div>'
    else:
        chip = f'<div class="swatch-chip generated-swatch" role="img" aria-label="{name} blend" data-swatch="{name} blend"></div>'
    return f'''<div class="swatch" data-cat="{cat}" onclick="chatAbout('{name} {note}')">
        {chip}
        <div class="swatch-meta"><div class="swatch-name">{name}</div><div class="swatch-cat">{cat_label(cat, name)}</div></div>
      </div>'''


def cat_label(cat, name):
    return {
        "natural": "Natural Accent",
        "flake": f"Flake · {FLAKE_CODES.get(name,'')}".strip(" ·"),
        "metallic": "Metallic",
        "solid": "Solid",
        "stain": "Stain",
        "multispec": "Multi-Spec",
    }.get(cat, cat)


FLAKE_CODES = {
    "Quicksilver": "FB-424", "Stonehenge": "FB-427", "Feather Gray": "FB-905",
    "Houndstooth": "FB-910", "Rocky Ridge": "FB-801", "Trail Mix": "FB-613",
    "Cabin Fever": "FB-127", "Sand Dollar": "FB-951", "Shoreline": "FB-421",
    "Tidal Wave": "FB-807", "Soapstone": "Marble", "Blizzard": "Marble",
}


def sf_divider(label):
    return f'''<div class="swatch sf-divider" data-cat="multispec" style="grid-column:1/-1;pointer-events:none;background:none;border:none;border-top:1px solid var(--border);padding:10px 0 4px;display:flex;align-items:center;gap:12px;">
        <span style="font-size:9px;font-weight:700;letter-spacing:3px;text-transform:uppercase;color:var(--muted);">{label}</span>
        <span style="flex:1;height:1px;background:var(--border);"></span>
      </div>'''


def build_colors():
    sw = []
    sw.append(swatch("Texas Sand", "natural", img="/assets/color-swatches/natural-texas-sand.png", note="Natural Accent"))
    sw.append(swatch("Cliff", "natural", img="/assets/color-swatches/natural-cliff.png", note="Natural Accent"))
    for name, file in [("Quicksilver","flake-quicksilver"),("Stonehenge","flake-stonehenge"),
                        ("Feather Gray","flake-feather-gray"),("Houndstooth","flake-houndstooth"),
                        ("Rocky Ridge","flake-rocky-ridge"),("Trail Mix","flake-trail-mix"),
                        ("Cabin Fever","flake-cabin-fever"),("Sand Dollar","flake-sand-dollar"),
                        ("Shoreline","flake-shoreline"),("Tidal Wave","flake-tidal-wave"),
                        ("Soapstone","flake-soapstone"),("Blizzard","flake-blizzard")]:
        sw.append(swatch(name, "flake", img=f"/assets/color-swatches/{file}.png", note="flake floor"))
    metallics = [
        ("Chrome Silver","linear-gradient(125deg,#d8dce2 0%,#888e98 30%,#c8ccd4 50%,#6a7078 70%,#b8bcc4 100%)"),
        ("Crimson Fire","linear-gradient(125deg,#8a1018 0%,#d4141f 35%,#6a0a10 60%,#b01620 85%,#4a060a 100%)"),
        ("Midnight Blue","linear-gradient(125deg,#141a3a 0%,#2a3a7a 35%,#0e1228 60%,#22306a 85%,#0a0e20 100%)"),
        ("Copper Canyon","linear-gradient(125deg,#6a3a1a 0%,#c87838 35%,#4a280e 60%,#a86028 85%,#3a1e0a 100%)"),
    ]
    for name, grad in metallics:
        sw.append(swatch(name, "metallic", style=f"background:{grad};", note="metallic epoxy"))
    solids = [
        ("Onyx Black","linear-gradient(135deg,#16171a 0%,#26282e 50%,#101114 100%)"),
        ("Pearl White","linear-gradient(135deg,#ece8e0 0%,#d4d0c8 50%,#e8e4dc 100%)"),
        ("Slate Gray","linear-gradient(135deg,#4e525a 0%,#3a3e46 50%,#565a62 100%)"),
    ]
    for name, grad in solids:
        sw.append(swatch(name, "solid", style=f"background:{grad};", note="solid color floor"))
    stains = [
        ("Terra Bronze","radial-gradient(ellipse at 30% 30%, #8a5a30 0%, transparent 60%), radial-gradient(ellipse at 75% 70%, #5a3a1e 0%, transparent 55%), linear-gradient(135deg,#6a4a28,#4a3018)"),
        ("Walnut","radial-gradient(ellipse at 65% 25%, #5a4030 0%, transparent 55%), radial-gradient(ellipse at 25% 75%, #38281c 0%, transparent 60%), linear-gradient(135deg,#483424,#2e2014)"),
        ("Aged Leather","radial-gradient(ellipse at 40% 35%, #9a6a3a 0%, transparent 55%), radial-gradient(ellipse at 70% 80%, #6a4424 0%, transparent 60%), linear-gradient(135deg,#7e5630,#56381c)"),
    ]
    for name, grad in stains:
        sw.append(swatch(name, "stain", style=f"background:{grad};", note="concrete stain"))
    for name in ["Opal","Moon Mist","Caraway","Woven"]:
        sw.append(swatch(name, "multispec", note="multi-spec floor"))

    sw.append(sf_divider("StoneFlecks Ultra™ — Loft Collection"))
    for name, file, extra in [("Niagara","stoneflecks-loft-niagara",""),("Oyster Bay","stoneflecks-loft-oyster-bay",""),
                               ("Dove Gray","stoneflecks-loft-dove-gray",""),("Morning Mist","stoneflecks-loft-morning-mist",""),
                               ("Slate Gray","stoneflecks-loft-slate-gray",""),("Smoke Cement","stoneflecks-loft-smoke-cement"," · NEW")]:
        sw.append(f'''<div class="swatch" data-cat="multispec" onclick="chatAbout('StoneFlecks {name} coating')">
        <div class="swatch-chip"><img src="/assets/color-swatches/{file}.png" alt="{name} StoneFlecks Loft texture swatch" loading="lazy"></div>
        <div class="swatch-meta"><div class="swatch-name">{name}</div><div class="swatch-cat">StoneFlecks · Loft{extra}</div></div>
      </div>''')

    sw.append(sf_divider("StoneFlecks Ultra™ — Mineral Collection"))
    for name, file, extra in [("Espresso","stoneflecks-mineral-espresso",""),("Andromeda","stoneflecks-mineral-andromeda"," · NEW"),
                               ("Yukon","stoneflecks-mineral-yukon",""),("White Vein","stoneflecks-mineral-white-vein",""),
                               ("Granite","stoneflecks-mineral-granite",""),("Feldspar","stoneflecks-mineral-feldspar"," · NEW")]:
        sw.append(f'''<div class="swatch" data-cat="multispec" onclick="chatAbout('StoneFlecks {name} coating')">
        <div class="swatch-chip"><img src="/assets/color-swatches/{file}.png" alt="{name} StoneFlecks Mineral texture swatch" loading="lazy"></div>
        <div class="swatch-meta"><div class="swatch-name">{name}</div><div class="swatch-cat">StoneFlecks · Mineral{extra}</div></div>
      </div>''')

    sw.append(sf_divider("StoneFlecks Ultra™ — Earth Collection"))
    earth = [("Clay","stoneflecks-earth-clay"," · Close Out"),("Castlerock","stoneflecks-earth-castlerock",""),
             ("Basalt","stoneflecks-earth-basalt"," · Close Out"),("Muir Woods","stoneflecks-earth-muir-woods",""),
             ("Charcoal","stoneflecks-earth-charcoal",""),("Midnight Sky","stoneflecks-earth-midnight-sky",""),
             ("Neptunite","stoneflecks-earth-neptunite"," · NEW"),("Fossil","stoneflecks-earth-fossil",""),
             ("Sandstone","stoneflecks-earth-sandstone"," · Close Out"),("Cliff","stoneflecks-earth-cliff",""),
             ("Beach Sand","stoneflecks-earth-beach-sand",""),("Landslide","stoneflecks-earth-landslide","")]
    for name, file, extra in earth:
        dim = ' style="opacity:0.6;"' if "Close Out" in extra else ''
        cat_style = ' style="color:var(--muted);"' if "Close Out" in extra else ''
        sw.append(f'''<div class="swatch" data-cat="multispec" onclick="chatAbout('StoneFlecks {name} coating')"{dim}>
        <div class="swatch-chip"><img src="/assets/color-swatches/{file}.png" alt="{name} StoneFlecks Earth texture swatch" loading="lazy"></div>
        <div class="swatch-meta"><div class="swatch-name">{name}</div><div class="swatch-cat"{cat_style}>StoneFlecks · Earth{extra}</div></div>
      </div>''')

    body = f'''{page_hero(
        "Signature Collections",
        'Choose your <span class="thin">finish.</span>',
        "Flake, metallic, solid, stain, multi-spec &amp; natural accent systems — these are starting points. Custom color matching is available on every job, for every service we offer.",
        crumbs=[("Home","/index.html"),("Colors",None)],
    )}

<section class="tight">
  <div class="wrap">
    <div class="color-filters rv" role="group" aria-label="Filter colors by collection">
      <button class="cf-btn active" onclick="filterColors('all',this)">All</button>
      <button class="cf-btn" onclick="filterColors('flake',this)">Flake</button>
      <button class="cf-btn" onclick="filterColors('metallic',this)">Metallic</button>
      <button class="cf-btn" onclick="filterColors('solid',this)">Solid</button>
      <button class="cf-btn" onclick="filterColors('stain',this)">Stain</button>
      <button class="cf-btn" onclick="filterColors('natural',this)">Natural Accent</button>
      <button class="cf-btn" onclick="filterColors('multispec',this)">Multi-Spec</button>
    </div>
    <div class="swatches rv" id="swatchGrid">
      {''.join(sw)}
    </div>
    <div style="text-align:center;margin-top:36px;" class="rv">
      <button class="btn btn-ghost" onclick="openChat()">Discuss Custom Colors with Our AI Estimator →</button>
    </div>
    <p style="text-align:center;margin-top:18px;font-size:11px;color:var(--muted);max-width:640px;margin-left:auto;margin-right:auto;line-height:1.7;">StoneFlecks™ Ultra colors by Hawk Research Laboratories. Final colors may vary due to batch manufacturing variation, application technique, and environmental conditions. Close Out items subject to availability. All colors representative only.</p>
  </div>
</section>

{cta_band_html("Can't decide on a finish?", "Upload a photo to the Project Visualizer and preview a color before you commit.")}

{footer_html()}'''
    write("colors.html", page(
        title="Colors & Finishes — Flake, Metallic, Solid, Stain & StoneFlecks Ultra™ | Precision Coatings of Texas",
        description="Browse every coating finish Precision Coatings of Texas offers: flake, metallic, solid, stain, natural accent & StoneFlecks Ultra™ collections. Custom color matching available.",
        active="Services",
        body=body,
        extra_js=["/assets/js/colors.js"],
        canonical="/colors.html",
    ))


# ═══════════════════════════════════════════════════════════════════════════
# VISUALIZER
# ═══════════════════════════════════════════════════════════════════════════

def build_visualizer():
    body = f'''{page_hero(
        "Project Visualizer",
        'Upload a photo.<br><span class="thin">Preview the finish.</span>',
        "Choose a surface, finish, and gloss level, then generate a preview image to picture the requested work before scheduling an estimate.",
        crumbs=[("Home","/index.html"),("Visualizer",None)],
    )}

<section id="visualizer" class="visualizer-band tight">
  <div class="wrap">
    <div class="viz-shell">
      <div class="viz-panel rv">
        <div class="viz-row">
          <label class="viz-label" for="visualizerUpload">Project Photo</label>
          <label class="viz-upload" id="visualizerDrop">
            <input id="visualizerUpload" type="file" accept="image/*">
            <span>
              <strong id="visualizerUploadTitle">Upload a room, garage, patio, tub, or cabinet photo</strong>
              <span id="visualizerUploadHint">JPG, PNG, or HEIC from a phone works best.</span>
            </span>
          </label>
        </div>

        <div class="viz-row">
          <span class="viz-label">Surface</span>
          <div class="viz-grid" id="visualizerSurface">
            <button class="viz-choice active" type="button" data-value="Garage Floor">Garage Floor</button>
            <button class="viz-choice" type="button" data-value="Patio">Patio</button>
            <button class="viz-choice" type="button" data-value="Tile">Tile</button>
            <button class="viz-choice" type="button" data-value="Tub or Vanity">Tub or Vanity</button>
            <button class="viz-choice" type="button" data-value="Countertop">Countertop</button>
            <button class="viz-choice" type="button" data-value="Cabinets">Cabinets</button>
          </div>
        </div>

        <div class="viz-row">
          <label class="viz-label" for="visualizerFinish">Finish</label>
          <select class="viz-select" id="visualizerFinish">
            <option value="quicksilver">Quicksilver Flake</option>
            <option value="stonehenge">Stonehenge Flake</option>
            <option value="shoreline">Shoreline Flake</option>
            <option value="chrome">Chrome Silver Metallic</option>
            <option value="copper">Copper Canyon Metallic</option>
            <option value="slate">Slate Gray Solid</option>
            <option value="pearl">Pearl White Solid</option>
            <option value="texas-sand">Texas Sand Natural Accent</option>
            <option value="walnut">Walnut Stain</option>
            <option value="cabinet">Cabinet Enamel White</option>
            <option value="cabinet-dark">Cabinet Espresso Enamel</option>
          </select>
        </div>

        <div class="viz-row">
          <label class="viz-label" for="visualizerGloss">Topcoat</label>
          <select class="viz-select" id="visualizerGloss">
            <option value="satin">Satin</option>
            <option value="gloss">High Gloss</option>
            <option value="matte">Matte</option>
            <option value="non-slip">Non-Slip Texture</option>
          </select>
        </div>

        <div class="viz-row">
          <span class="viz-label">Selected Look</span>
          <div class="viz-finish-preview" id="visualizerFinishPreview"></div>
        </div>

        <div class="viz-actions">
          <button class="btn btn-red" type="button" id="visualizerGenerate">Generate Preview</button>
          <button class="btn btn-ghost" type="button" id="visualizerDownload" disabled>Download Image</button>
        </div>
        <p class="viz-note">Preview images are for planning only. Final color, texture, masking, and coverage are confirmed during the free on-site estimate.</p>
      </div>

      <div class="viz-stage rv">
        <div class="viz-canvas-wrap">
          <canvas id="visualizerCanvas" width="1280" height="900" aria-label="Generated coating preview"></canvas>
          <div class="viz-empty" id="visualizerEmpty">
            <div>
              <strong>Your generated preview appears here.</strong>
              <span>Upload a project photo and click Generate Preview.</span>
            </div>
          </div>
        </div>
        <div class="viz-status" id="visualizerStatus">Waiting for a project photo. <span>AI PREVIEW</span></div>
      </div>
    </div>
  </div>
</section>

{cta_band_html("Like what you see?", "Turn your preview into a free on-site estimate — no obligation.")}

{footer_html()}'''
    write("visualizer.html", page(
        title="AI Project Visualizer — Preview Your Finish | Precision Coatings of Texas",
        description="Upload a photo of your garage, patio, tub, countertop, or cabinets and preview a coating finish before you schedule your free estimate.",
        active="Services",
        body=body,
        extra_js=["/assets/js/visualizer.js"],
        canonical="/visualizer.html",
    ))


# ═══════════════════════════════════════════════════════════════════════════
# PROCESS
# ═══════════════════════════════════════════════════════════════════════════

def build_process():
    body = f'''{page_hero(
        "How It Works",
        'Four steps.<br><span class="thin">Zero hassle.</span>',
        "Every project — no matter the surface — follows the same process: a free consultation, an honest on-site assessment, expert installation, and a walkthrough before we consider the job done.",
        crumbs=[("Home","/index.html"),("Process",None)],
    )}

<section class="tight">
  <div class="wrap">
    {process_steps_html(detailed=True)}
  </div>
</section>

<section class="tight">
  <div class="wrap">
    <div class="sec-head rv">
      <div class="sec-kicker">What To Expect</div>
      <h2 class="sec-title">Before, during,<br><span class="thin">and after.</span></h2>
    </div>
    <div class="value-grid">
      <div class="value-card rv">
        <div class="value-ico">🗓</div>
        <div class="value-name">Scheduling</div>
        <div class="value-desc">We're open 7 days a week — Mon–Fri 8am–6pm, weekends 8am–12pm — so booking a free on-site estimate rarely means waiting long.</div>
      </div>
      <div class="value-card rv">
        <div class="value-ico">🧰</div>
        <div class="value-name">Surface Prep</div>
        <div class="value-desc">Every job starts with real mechanical prep — grinding, repair, priming — not a quick coat over an unprepared surface.</div>
      </div>
      <div class="value-card rv">
        <div class="value-ico">🕐</div>
        <div class="value-name">Cure Time</div>
        <div class="value-desc">Timelines vary by system and surface. Your technician will walk you through exact cure and return-to-use guidance for your specific project.</div>
      </div>
      <div class="value-card rv">
        <div class="value-ico">🛡</div>
        <div class="value-name">The Guarantee</div>
        <div class="value-desc">We inspect the finished surface with you before we leave, and back our workmanship with a warranty.</div>
      </div>
    </div>
  </div>
</section>

{cta_band_html("Ready to start<br>the process?", "Step one is a free, no-obligation conversation — chat now or call us direct.")}

{footer_html()}'''
    write("process.html", page(
        title="Our Process — Free Estimate to Final Walkthrough | Precision Coatings of Texas",
        description="How Precision Coatings of Texas works: free consultation, on-site assessment, expert installation, and a final walkthrough backed by a workmanship warranty.",
        active="Process",
        body=body,
        canonical="/process.html",
    ))


# ═══════════════════════════════════════════════════════════════════════════
# ABOUT
# ═══════════════════════════════════════════════════════════════════════════

def build_about():
    body = f'''{page_hero(
        "About Precision Coatings of Texas",
        'Locally owned.<br><span class="thin">Texas built.</span>',
        "Precision Coatings of Texas has been restoring surfaces across Austin and Central Texas since 2014 — one garage, patio, tub, and kitchen at a time.",
        img=IMG['cabinet_wide'],
        crumbs=[("Home","/index.html"),("About",None)],
    )}

<section class="tight">
  <div class="wrap">
    <div class="about-split">
      <div class="about-photo rv"><img src="{IMG['garage_signature']}" alt="Precision Coatings of Texas signature garage floor project" loading="lazy"></div>
      <div class="rv">
        <div class="sec-kicker">Our Story</div>
        <h2 class="sec-title" style="font-size:clamp(28px,3.4vw,42px);">Every surface deserves<br><span class="thin">a second life.</span></h2>
        <p style="font-size:14.5px;font-weight:300;line-height:1.85;color:var(--text);margin-top:20px;">Precision Coatings of Texas is a locally owned and operated surface refinishing company based in Hutto, TX, serving Austin and the greater Central Texas area. For more than 10 years we've helped homeowners restore garages, patios, tile, tubs, vanities, countertops, and cabinets to better-than-new condition — without the cost, mess, and downtime of full replacement.</p>
        <p style="font-size:14.5px;font-weight:300;line-height:1.85;color:var(--text);margin-top:14px;">We're rated 5.0 on HomeAdvisor and recognized as a Top Pro on Thumbtack. Every project starts with a free, no-obligation on-site estimate, and every job is backed by a workmanship warranty.</p>
        <div class="stat-row">
          <div class="stat-box"><div class="stat-num">10<em>+</em></div><div class="stat-lbl">Years in Business</div></div>
          <div class="stat-box"><div class="stat-num">7</div><div class="stat-lbl">Services Offered</div></div>
          <div class="stat-box"><div class="stat-num">5.0<em>★</em></div><div class="stat-lbl">HomeAdvisor Rating</div></div>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="tight">
  <div class="wrap">
    <div class="sec-head rv">
      <div class="sec-kicker">Why Homeowners Choose PCT</div>
      <h2 class="sec-title">What we <span class="thin">stand on.</span></h2>
    </div>
    {value_grid_html()}
  </div>
</section>

<section class="tight">
  <div class="wrap">
    <div class="sec-head rv">
      <div class="sec-kicker">Every Job, Every Time</div>
      <h2 class="sec-title">Our commitment <span class="thin">to you.</span></h2>
    </div>
    <ul class="svc-list rv" style="max-width:640px;font-size:15px;">
      <li>Locally owned &amp; operated — based in Hutto, TX</li>
      <li>Free, no-obligation on-site estimates on every project</li>
      <li>Workmanship warranty on every coating system we install</li>
      <li>Open 7 days a week: Mon–Fri 8am–6pm, weekends 8am–12pm</li>
      <li>Seasonal discounts offered throughout the year</li>
      <li>Flexible payment — cash, check, card, Square, or Zelle</li>
    </ul>
  </div>
</section>

{testimonials_html(intro=False)}

{cta_band_html("Let's talk about<br>your project.", "Free on-site estimates · Open 7 days a week · Warranty backed · Serving Austin &amp; Central Texas")}

{footer_html()}'''
    write("about.html", page(
        title="About Us — Locally Owned Since 2014 | Precision Coatings of Texas",
        description="Precision Coatings of Texas is a locally owned, 5.0-star rated surface refinishing company based in Hutto, TX, serving Austin & Central Texas since 2014.",
        active="About",
        body=body,
        canonical="/about.html",
    ))


# ═══════════════════════════════════════════════════════════════════════════
# SERVICE AREAS
# ═══════════════════════════════════════════════════════════════════════════

AREA_CITIES = [
    "Austin", "Hutto", "Round Rock", "Pflugerville", "Georgetown", "Cedar Park",
    "Leander", "Taylor", "Elgin", "Manor", "Jarrell", "Liberty Hill",
]


def build_service_areas():
    chips = "".join(f'<div class="area-chip rv">{c}</div>' for c in AREA_CITIES)
    body = f'''{page_hero(
        "Service Areas",
        'Serving Austin<br><span class="thin">& Central Texas.</span>',
        "Based in Hutto, TX, Precision Coatings of Texas serves homeowners throughout the Austin metro and greater Central Texas region.",
        crumbs=[("Home","/index.html"),("Service Areas",None)],
    )}

<section class="tight">
  <div class="wrap">
    <div class="sec-head rv">
      <div class="sec-kicker">Where We Work</div>
      <h2 class="sec-title">Central Texas,<br><span class="thin">covered.</span></h2>
      <p class="sec-sub">Here's the general area we serve. Don't see your city listed? Reach out anyway — if you're within a reasonable drive of Central Texas, we probably cover it.</p>
    </div>
    <div class="areas-grid">
      {chips}
    </div>
    <div class="area-map-note rv">
      <strong style="color:var(--white);">📍 Based in Hutto, TX</strong> — centrally located to reach the Austin metro area quickly for on-site estimates and scheduled installations. Every estimate is free and on-site, so we can confirm exact service availability for your specific address when you reach out.
    </div>
  </div>
</section>

{cta_band_html("Not sure if we<br>cover your area?", "Call, text, or chat with our AI estimator — we'll confirm availability for your address.")}

{footer_html()}'''
    write("service-areas.html", page(
        title="Service Areas — Austin & Central Texas | Precision Coatings of Texas",
        description="Precision Coatings of Texas is based in Hutto, TX and serves Austin, Round Rock, Pflugerville, Georgetown, Cedar Park, and the greater Central Texas area.",
        active="Service Areas",
        body=body,
        canonical="/service-areas.html",
    ))


# ═══════════════════════════════════════════════════════════════════════════
# FAQ
# ═══════════════════════════════════════════════════════════════════════════

FAQS = [
    ("Do you offer free estimates?",
     "Yes — every estimate is free and on-site, with no obligation. We inspect the surface, take measurements, and give you a detailed written quote before any work begins."),
    ("What areas do you serve?",
     "We're based in Hutto, TX and serve Austin and the greater Central Texas area. See our <a href=\"/service-areas.html\" style=\"color:var(--red2);\">Service Areas</a> page, or just reach out and we'll confirm coverage for your address."),
    ("How long does a coating project take?",
     "It depends on the surface and system. Most tubs are completed in about two days; other project timelines are confirmed during your free on-site estimate once we know the size and condition of the surface."),
    ("Do I need to move out or stay off the surface during the project?",
     "Surface prep and coating application do require the work area to be clear and undisturbed. Your technician will walk you through exact access and cure-time guidance for your specific project during the estimate."),
    ("Can you match a custom color?",
     "Yes. Beyond our Flake, Metallic, Solid, Stain, Natural Accent, and StoneFlecks Ultra™ collections, custom color matching is available on every job."),
    ("Is resurfacing durable enough for daily use?",
     "Our systems are professional-grade and built for real-world use — garage floors are engineered to resist hot tire pickup and Texas heat, tubs are reglazed for daily bathing use, and countertops get a food-safe topcoat option. Every system is backed by a workmanship warranty."),
    ("What payment methods do you accept?",
     "Cash, check, credit card, Square, and Zelle."),
    ("Are you licensed and insured?",
     "Give us a call at 512-537-7951 and we're happy to walk you through our credentials for your specific project."),
    ("What's the difference between resurfacing and replacement?",
     "Resurfacing restores the existing surface — garage floor, tub, countertop, cabinet, or tile — with a new coating system, avoiding the demolition, lead time, and cost of a full replacement. In most cases it's faster and significantly more affordable while still delivering a durable, like-new finish."),
    ("Do you offer discounts?",
     "We offer seasonal discounts throughout the year — ask about current promotions when you request your free estimate."),
]


def build_faq():
    items = "".join(f'''<div class="faq-item rv">
        <button class="faq-q"><span>{q}</span><span class="faq-plus">+</span></button>
        <div class="faq-a"><div class="faq-a-inner">{a}</div></div>
      </div>''' for q, a in FAQS)

    body = f'''{page_hero(
        "Frequently Asked Questions",
        "Questions?<br><span class='thin'>We've got answers.</span>",
        "Everything homeowners typically ask before booking a surface refinishing project with Precision Coatings of Texas.",
        crumbs=[("Home","/index.html"),("FAQ",None)],
    )}

<section class="tight">
  <div class="wrap narrow">
    <div class="faq-list">
      {items}
    </div>
  </div>
</section>

{cta_band_html("Still have<br>a question?", "Chat with our AI estimator or call us direct — we're open 7 days a week.")}

{footer_html()}'''
    write("faq.html", page(
        title="FAQ — Frequently Asked Questions | Precision Coatings of Texas",
        description="Answers to common questions about surface refinishing, timelines, pricing, service areas, and more from Precision Coatings of Texas.",
        active="FAQ",
        body=body,
        extra_js=["/assets/js/faq.js"],
        canonical="/faq.html",
    ))


# ═══════════════════════════════════════════════════════════════════════════
# REVIEWS
# ═══════════════════════════════════════════════════════════════════════════

def build_reviews():
    body = f'''{page_hero(
        "Client Reviews",
        'Texas <span class="thin">approved.</span>',
        "Rated 5.0 on HomeAdvisor and recognized as a Top Pro on Thumbtack. Here's what homeowners say after working with us.",
        crumbs=[("Home","/index.html"),("Reviews",None)],
    )}

{testimonials_html(intro=False)}

<section class="tight">
  <div class="wrap">
    <div class="value-grid" style="grid-template-columns:repeat(2,1fr);max-width:640px;margin:0 auto;">
      <a class="value-card rv" href="https://www.homeadvisor.com" target="_blank" rel="noopener" style="text-decoration:none;display:block;text-align:center;">
        <div class="value-ico">⭐</div>
        <div class="value-name">5.0 on HomeAdvisor</div>
        <div class="value-desc">Verified customer reviews</div>
      </a>
      <a class="value-card rv" href="https://www.thumbtack.com" target="_blank" rel="noopener" style="text-decoration:none;display:block;text-align:center;">
        <div class="value-ico">🏅</div>
        <div class="value-name">Top Pro on Thumbtack</div>
        <div class="value-desc">Verified customer reviews</div>
      </a>
    </div>
  </div>
</section>

{cta_band_html("Ready to become<br>our next 5-star review?", "Free on-site estimates · Open 7 days a week · Warranty backed")}

{footer_html()}'''
    write("reviews.html", page(
        title="Client Reviews — 5.0★ Rated | Precision Coatings of Texas",
        description="Read verified 5-star reviews from Precision Coatings of Texas customers on HomeAdvisor and Thumbtack.",
        active="Reviews",
        body=body,
        canonical="/reviews.html",
    ))


# ═══════════════════════════════════════════════════════════════════════════
# CONTACT
# ═══════════════════════════════════════════════════════════════════════════

def build_contact():
    body = f'''{page_hero(
        "Contact Us",
        "Let's talk about<br><span class='thin'>your surface.</span>",
        "Free on-site estimates, seven days a week. Reach out however's easiest — call, email, or chat with our AI estimator right now.",
        crumbs=[("Home","/index.html"),("Contact",None)],
    )}

<section class="tight">
  <div class="wrap">
    <div class="contact-grid">
      <div class="contact-card rv">
        <div class="contact-ico">📞</div>
        <div class="contact-h">Call or Text</div>
        <div class="contact-d">The fastest way to reach us directly.</div>
        <a href="tel:{PHONE_TEL}" class="btn btn-red">{PHONE}</a>
      </div>
      <div class="contact-card rv">
        <div class="contact-ico">✉️</div>
        <div class="contact-h">Email</div>
        <div class="contact-d">Send project details or photos anytime.</div>
        <a href="mailto:{EMAIL}" class="btn btn-ghost">{EMAIL}</a>
      </div>
      <div class="contact-card rv">
        <div class="contact-ico">💬</div>
        <div class="contact-h">Chat with the AI Estimator</div>
        <div class="contact-d">Get a free estimate in about 2 minutes — no phone call needed.</div>
        <button class="btn btn-red" onclick="openChat()">Start Chat</button>
      </div>
      <div class="contact-card rv">
        <div class="contact-ico">📍</div>
        <div class="contact-h">Based In</div>
        <div class="contact-d">Hutto, TX — serving Austin &amp; Central Texas.</div>
        <a href="/service-areas.html" class="btn btn-ghost">See Service Areas</a>
      </div>
    </div>

    <div class="svc-layout" style="margin-top:40px;">
      <div class="svc-body">
        <h2>What to have ready</h2>
        <p>To make your free estimate as fast as possible, it helps to know: which surface you're looking to refinish, its approximate size, and your general timeline. Photos help too — you can even try the <a href="/visualizer.html" style="color:var(--red2);">Project Visualizer</a> first to preview a finish.</p>
        <h2>Payment</h2>
        <p>We accept cash, check, credit card, Square, and Zelle.</p>
      </div>
      <div class="svc-sidebar">
        <div class="sb-card rv">
          <div class="sb-h">Hours — Open 7 Days</div>
          <table class="hours-table">
            <tr><td>Monday – Friday</td><td>8:00am – 6:00pm</td></tr>
            <tr><td>Saturday</td><td>8:00am – 12:00pm</td></tr>
            <tr><td>Sunday</td><td>8:00am – 12:00pm</td></tr>
          </table>
        </div>
      </div>
    </div>
  </div>
</section>

{footer_html()}'''
    write("contact.html", page(
        title="Contact Us — Free Estimates | Precision Coatings of Texas",
        description="Contact Precision Coatings of Texas for a free on-site estimate. Call 512-537-7951, email, or chat with our AI estimator. Serving Austin & Central Texas, open 7 days a week.",
        active="",
        body=body,
        canonical="/contact.html",
    ))


# ═══════════════════════════════════════════════════════════════════════════
# BUILD ALL
# ═══════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    build_home()
    build_services_hub()
    for svc in SERVICES:
        build_service_page(svc)
    build_gallery()
    build_colors()
    build_visualizer()
    build_process()
    build_about()
    build_service_areas()
    build_faq()
    build_reviews()
    build_contact()
    print("\nDone.")
