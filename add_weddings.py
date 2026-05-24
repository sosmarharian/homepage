#!/usr/bin/env python3
import re

filepath = '/Users/sosmarharyan/homepage/index.html'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# ============================================================
# 1. Добавить Google Font для свадебного шрифта (Great Vibes)
# ============================================================
font_link = '<link href="https://fonts.googleapis.com/css2?family=Great+Vibes&display=swap" rel="stylesheet">'
content = content.replace(
    '<link href="https://fonts.googleapis.com/css2?family=Cormorant',
    font_link + '\n  <link href="https://fonts.googleapis.com/css2?family=Cormorant'
)

# ============================================================
# 2. Добавить CSS стили для кнопки Weddings и раздела
# ============================================================
wedding_css = """
    /* ——— Weddings Nav Button ——— */
    .nav-wedding {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 8px 18px;
      background: transparent;
      border: 1.5px solid #e63030;
      border-radius: 4px;
      color: #e63030;
      font-family: 'Great Vibes', cursive;
      font-size: 20px;
      letter-spacing: 0.5px;
      cursor: pointer;
      transition: all 0.25s ease;
      text-decoration: none;
      line-height: 1;
    }
    .nav-wedding:hover {
      background: #e63030;
      color: #fff;
      transform: translateY(-1px);
    }

    /* ——— Weddings Section ——— */
    #weddings {
      background: var(--dark);
      color: var(--white);
      padding: 0;
    }

    .wedding-hero {
      position: relative;
      height: 85vh;
      min-height: 560px;
      overflow: hidden;
      display: flex;
      align-items: center;
      justify-content: center;
    }
    .wedding-hero img {
      position: absolute;
      inset: 0;
      width: 100%;
      height: 100%;
      object-fit: cover;
      object-position: center top;
      filter: brightness(0.45);
    }
    .wedding-hero-content {
      position: relative;
      z-index: 2;
      text-align: center;
      padding: 0 24px;
    }
    .wedding-hero-script {
      font-family: 'Great Vibes', cursive;
      font-size: clamp(52px, 10vw, 96px);
      color: #fff;
      line-height: 1.1;
      margin-bottom: 16px;
    }
    .wedding-hero-sub {
      font-family: var(--font-heading);
      font-size: clamp(13px, 2vw, 17px);
      letter-spacing: 0.3em;
      text-transform: uppercase;
      color: var(--gold);
      margin-bottom: 32px;
    }
    .wedding-hero-btn {
      display: inline-flex;
      align-items: center;
      gap: 10px;
      padding: 16px 36px;
      background: #e63030;
      color: #fff;
      font-family: var(--font-body);
      font-size: 13px;
      font-weight: 600;
      letter-spacing: 0.15em;
      text-transform: uppercase;
      border: none;
      cursor: pointer;
      transition: all 0.25s ease;
      text-decoration: none;
    }
    .wedding-hero-btn:hover { background: #c42020; transform: translateY(-2px); }

    /* Stats */
    .wedding-stats {
      display: flex;
      justify-content: center;
      gap: 0;
      background: #0d0d0d;
      border-top: 1px solid rgba(197,154,94,0.2);
      border-bottom: 1px solid rgba(197,154,94,0.2);
    }
    .wedding-stat {
      flex: 1;
      max-width: 240px;
      text-align: center;
      padding: 48px 24px;
      border-right: 1px solid rgba(197,154,94,0.15);
    }
    .wedding-stat:last-child { border-right: none; }
    .wedding-stat-num {
      font-family: var(--font-heading);
      font-size: clamp(40px, 6vw, 64px);
      font-weight: 300;
      color: var(--gold);
      line-height: 1;
      margin-bottom: 8px;
    }
    .wedding-stat-label {
      font-size: 12px;
      letter-spacing: 0.2em;
      text-transform: uppercase;
      color: rgba(255,255,255,0.5);
    }

    /* About duo */
    .wedding-about {
      display: grid;
      grid-template-columns: 1fr 1fr;
      min-height: 520px;
    }
    .wedding-about-img {
      position: relative;
      overflow: hidden;
    }
    .wedding-about-img img {
      width: 100%;
      height: 100%;
      object-fit: cover;
    }
    .wedding-about-text {
      padding: 80px 60px;
      display: flex;
      flex-direction: column;
      justify-content: center;
      background: #111;
    }
    .wedding-about-script {
      font-family: 'Great Vibes', cursive;
      font-size: 42px;
      color: var(--gold);
      margin-bottom: 8px;
    }
    .wedding-about-text h2 {
      font-family: var(--font-heading);
      font-size: clamp(22px, 3vw, 32px);
      font-weight: 300;
      letter-spacing: 0.1em;
      text-transform: uppercase;
      margin-bottom: 24px;
      color: #fff;
    }
    .wedding-about-text p {
      font-size: 16px;
      line-height: 1.8;
      color: rgba(255,255,255,0.65);
      margin-bottom: 16px;
    }

    /* Portfolio grid */
    .wedding-portfolio {
      padding: 80px 0 0;
      background: var(--dark);
    }
    .wedding-portfolio-header {
      text-align: center;
      padding: 0 24px 48px;
    }
    .wedding-portfolio-header .eyebrow { color: var(--gold); }
    .wedding-portfolio-header h2 {
      font-family: 'Great Vibes', cursive;
      font-size: clamp(40px, 7vw, 72px);
      color: #fff;
      font-weight: 400;
      margin-top: 8px;
    }
    .wedding-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 3px;
    }
    .wedding-grid-item {
      position: relative;
      overflow: hidden;
      aspect-ratio: 3/4;
    }
    .wedding-grid-item.wide {
      grid-column: span 2;
      aspect-ratio: 16/9;
    }
    .wedding-grid-item img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      transition: transform 0.6s ease;
      display: block;
    }
    .wedding-grid-item:hover img { transform: scale(1.04); }

    /* Why us */
    .wedding-why {
      padding: 80px 40px;
      background: #0d0d0d;
    }
    .wedding-why-header {
      text-align: center;
      margin-bottom: 56px;
    }
    .wedding-why-header .eyebrow { color: var(--gold); }
    .wedding-why-header h2 {
      font-family: var(--font-heading);
      font-size: clamp(24px, 3vw, 36px);
      font-weight: 300;
      letter-spacing: 0.1em;
      text-transform: uppercase;
      color: #fff;
      margin-top: 8px;
    }
    .wedding-why-grid {
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 24px;
      max-width: 900px;
      margin: 0 auto;
    }
    .wedding-why-card {
      background: rgba(255,255,255,0.04);
      border: 1px solid rgba(197,154,94,0.15);
      padding: 32px;
      border-radius: 2px;
    }
    .wedding-why-card h3 {
      font-family: var(--font-heading);
      font-size: 16px;
      letter-spacing: 0.1em;
      text-transform: uppercase;
      color: var(--gold);
      margin-bottom: 10px;
    }
    .wedding-why-card p {
      font-size: 15px;
      line-height: 1.7;
      color: rgba(255,255,255,0.55);
    }

    /* Process */
    .wedding-process {
      padding: 80px 40px;
      background: #111;
    }
    .wedding-process-header {
      text-align: center;
      margin-bottom: 56px;
    }
    .wedding-process-header .eyebrow { color: var(--gold); }
    .wedding-process-header h2 {
      font-family: 'Great Vibes', cursive;
      font-size: clamp(36px, 6vw, 60px);
      color: #fff;
      font-weight: 400;
      margin-top: 8px;
    }
    .wedding-steps {
      display: flex;
      justify-content: center;
      gap: 0;
      max-width: 900px;
      margin: 0 auto;
      position: relative;
    }
    .wedding-steps::before {
      content: '';
      position: absolute;
      top: 28px;
      left: 10%;
      right: 10%;
      height: 1px;
      background: rgba(197,154,94,0.3);
    }
    .wedding-step {
      flex: 1;
      text-align: center;
      padding: 0 12px;
      position: relative;
    }
    .wedding-step-num {
      width: 56px;
      height: 56px;
      border: 1px solid var(--gold);
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      font-family: var(--font-heading);
      font-size: 16px;
      color: var(--gold);
      margin: 0 auto 16px;
      background: #111;
      position: relative;
      z-index: 1;
    }
    .wedding-step h4 {
      font-family: var(--font-heading);
      font-size: 13px;
      letter-spacing: 0.1em;
      text-transform: uppercase;
      color: #fff;
      margin-bottom: 6px;
    }
    .wedding-step p {
      font-size: 13px;
      color: rgba(255,255,255,0.45);
      line-height: 1.5;
    }

    /* FAQ */
    .wedding-faq {
      padding: 80px 40px;
      background: var(--dark);
      max-width: 800px;
      margin: 0 auto;
    }
    .wedding-faq-header {
      text-align: center;
      margin-bottom: 48px;
    }
    .wedding-faq-header .eyebrow { color: var(--gold); }
    .wedding-faq-header h2 {
      font-family: var(--font-heading);
      font-size: clamp(22px, 3vw, 32px);
      font-weight: 300;
      letter-spacing: 0.1em;
      text-transform: uppercase;
      color: #fff;
      margin-top: 8px;
    }
    .faq-item {
      border-bottom: 1px solid rgba(255,255,255,0.08);
    }
    .faq-question {
      width: 100%;
      background: none;
      border: none;
      color: #fff;
      font-family: var(--font-heading);
      font-size: 14px;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      text-align: left;
      padding: 24px 0;
      cursor: pointer;
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 16px;
    }
    .faq-question span.faq-icon {
      color: var(--gold);
      font-size: 20px;
      flex-shrink: 0;
      transition: transform 0.3s;
    }
    .faq-item.open .faq-icon { transform: rotate(45deg); }
    .faq-answer {
      font-size: 15px;
      line-height: 1.8;
      color: rgba(255,255,255,0.55);
      max-height: 0;
      overflow: hidden;
      transition: max-height 0.4s ease, padding 0.3s;
    }
    .faq-item.open .faq-answer {
      max-height: 300px;
      padding-bottom: 24px;
    }

    /* Request form */
    .wedding-request {
      padding: 80px 40px;
      background: #0d0d0d;
      text-align: center;
    }
    .wedding-request-inner {
      max-width: 620px;
      margin: 0 auto;
    }
    .wedding-request .eyebrow { color: var(--gold); }
    .wedding-request h2 {
      font-family: 'Great Vibes', cursive;
      font-size: clamp(40px, 7vw, 68px);
      color: #fff;
      font-weight: 400;
      margin: 8px 0 12px;
    }
    .wedding-request p {
      font-size: 15px;
      color: rgba(255,255,255,0.5);
      margin-bottom: 40px;
      line-height: 1.7;
    }
    .wedding-form {
      display: flex;
      flex-direction: column;
      gap: 16px;
      text-align: left;
    }
    .wedding-form input,
    .wedding-form select {
      width: 100%;
      background: rgba(255,255,255,0.05);
      border: 1px solid rgba(255,255,255,0.12);
      border-radius: 2px;
      padding: 16px 20px;
      color: #fff;
      font-family: var(--font-body);
      font-size: 15px;
      outline: none;
      transition: border-color 0.2s;
      box-sizing: border-box;
    }
    .wedding-form input::placeholder { color: rgba(255,255,255,0.3); }
    .wedding-form input:focus,
    .wedding-form select:focus { border-color: var(--gold); }
    .wedding-form select { color: rgba(255,255,255,0.6); }
    .wedding-form select option { background: #111; color: #fff; }
    .wedding-form-row { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; }
    .wedding-submit {
      width: 100%;
      padding: 18px;
      background: #e63030;
      color: #fff;
      border: none;
      font-family: var(--font-body);
      font-size: 13px;
      font-weight: 600;
      letter-spacing: 0.15em;
      text-transform: uppercase;
      cursor: pointer;
      transition: all 0.25s ease;
      margin-top: 8px;
    }
    .wedding-submit:hover { background: #c42020; }
    .wedding-form-note {
      font-size: 12px;
      color: rgba(255,255,255,0.3);
      text-align: center;
      margin-top: 8px;
    }

    /* Mobile */
    @media (max-width: 768px) {
      .nav-wedding { font-size: 17px; padding: 6px 14px; }
      .wedding-about { grid-template-columns: 1fr; }
      .wedding-about-img { height: 300px; }
      .wedding-about-text { padding: 48px 24px; }
      .wedding-stats { flex-wrap: wrap; }
      .wedding-stat { min-width: 50%; border-right: none; border-bottom: 1px solid rgba(197,154,94,0.15); }
      .wedding-grid { grid-template-columns: 1fr 1fr; }
      .wedding-grid-item.wide { grid-column: span 2; aspect-ratio: 4/3; }
      .wedding-why-grid { grid-template-columns: 1fr; }
      .wedding-steps { flex-wrap: wrap; gap: 32px; }
      .wedding-steps::before { display: none; }
      .wedding-form-row { grid-template-columns: 1fr; }
      .wedding-faq { padding: 60px 24px; }
      .wedding-request { padding: 60px 24px; }
      .wedding-why { padding: 60px 24px; }
      .wedding-process { padding: 60px 24px; }
    }
"""

# Вставить CSS перед закрывающим </style>
content = content.replace('</style>', wedding_css + '\n  </style>', 1)

# ============================================================
# 3. Добавить кнопку Weddings в навигацию
# ============================================================
old_nav = '      <li><a href="#about">About us</a></li>'
new_nav = '''      <li><a href="#weddings" class="nav-wedding">Weddings</a></li>
      <li><a href="#about">About us</a></li>'''
content = content.replace(old_nav, new_nav)

# ============================================================
# 4. Добавить раздел Weddings перед </body>
# ============================================================
wedding_section = """
  <!-- ===== WEDDINGS SECTION ===== -->
  <section id="weddings">

    <!-- Hero -->
    <div class="wedding-hero">
      <img src="DSC04976-2.jpg" alt="Wedding Photography Hamburg">
      <div class="wedding-hero-content">
        <div class="wedding-hero-script">Your Day. Our Craft.</div>
        <div class="wedding-hero-sub">Wedding Photography &amp; Film · Hamburg &amp; Deutschlandweit</div>
        <a href="#wedding-request" class="wedding-hero-btn" onclick="document.getElementById('wedding-request').scrollIntoView({behavior:'smooth'});return false;">
          Request Price List
        </a>
      </div>
    </div>

    <!-- Stats -->
    <div class="wedding-stats">
      <div class="wedding-stat">
        <div class="wedding-stat-num">7+</div>
        <div class="wedding-stat-label">Years of Experience</div>
      </div>
      <div class="wedding-stat">
        <div class="wedding-stat-num">30+</div>
        <div class="wedding-stat-label">Weddings Captured</div>
      </div>
      <div class="wedding-stat">
        <div class="wedding-stat-num">2</div>
        <div class="wedding-stat-label">Creatives, One Vision</div>
      </div>
    </div>

    <!-- About -->
    <div class="wedding-about">
      <div class="wedding-about-img">
        <img src="DSC08642.jpg" alt="Marharian Production Wedding">
      </div>
      <div class="wedding-about-text">
        <div class="wedding-about-script">Wir sind</div>
        <h2>Marharian Production</h2>
        <p>We are a creative duo offering wedding photography and film from a single source — an experienced team that knows how to work together seamlessly on your most important day.</p>
        <p>Our style is cinematic and emotional. We capture real moments, genuine feelings, and the small details that make your story unique. Whether photo, film, or both together — we adapt to your vision.</p>
      </div>
    </div>

    <!-- Portfolio -->
    <div class="wedding-portfolio">
      <div class="wedding-portfolio-header">
        <span class="eyebrow">Portfolio</span>
        <h2>Beloved Moments</h2>
      </div>
      <div class="wedding-grid">
        <div class="wedding-grid-item wide">
          <img src="DSC03319.jpg" alt="Wedding moment">
        </div>
        <div class="wedding-grid-item">
          <img src="DSC08202.jpg" alt="Bride portrait">
        </div>
        <div class="wedding-grid-item">
          <img src="DSC04400.jpg" alt="Wedding detail">
        </div>
        <div class="wedding-grid-item">
          <img src="DSC04409-2.jpg" alt="Bride">
        </div>
        <div class="wedding-grid-item wide">
          <img src="DSC04362-2.jpg" alt="Wedding couple">
        </div>
        <div class="wedding-grid-item">
          <img src="DSC02043-2.jpg" alt="Wedding rings">
        </div>
        <div class="wedding-grid-item">
          <img src="DSC04037-2.jpg" alt="Wedding ceremony">
        </div>
      </div>
    </div>

    <!-- Why us -->
    <div class="wedding-why">
      <div class="wedding-why-header">
        <span class="eyebrow">Why Us</span>
        <h2>What Sets Us Apart</h2>
      </div>
      <div class="wedding-why-grid">
        <div class="wedding-why-card">
          <h3>Creative Duo</h3>
          <p>Photo &amp; film from one team — perfectly coordinated, no communication gaps, pure focus on your day.</p>
        </div>
        <div class="wedding-why-card">
          <h3>All of Germany</h3>
          <p>Based in Hamburg, we travel throughout Germany and beyond for your wedding — without hidden costs.</p>
        </div>
        <div class="wedding-why-card">
          <h3>Cinematic Style</h3>
          <p>Every image and every film frame is crafted with a director's eye — emotional, timeless, cinematic.</p>
        </div>
        <div class="wedding-why-card">
          <h3>Photo &amp; Video Together</h3>
          <p>Book photo only, video only, or both combined — fully flexible to your wishes and budget.</p>
        </div>
      </div>
    </div>

    <!-- Process -->
    <div class="wedding-process">
      <div class="wedding-process-header">
        <span class="eyebrow">How It Works</span>
        <h2>So einfach</h2>
      </div>
      <div class="wedding-steps">
        <div class="wedding-step">
          <div class="wedding-step-num">01</div>
          <h4>Inquiry</h4>
          <p>Via form or email</p>
        </div>
        <div class="wedding-step">
          <div class="wedding-step-num">02</div>
          <h4>Consultation</h4>
          <p>Get to know each other &amp; plan</p>
        </div>
        <div class="wedding-step">
          <div class="wedding-step-num">03</div>
          <h4>Booking</h4>
          <p>Date &amp; deposit</p>
        </div>
        <div class="wedding-step">
          <div class="wedding-step-num">04</div>
          <h4>Your Day</h4>
          <p>We are there for you</p>
        </div>
        <div class="wedding-step">
          <div class="wedding-step-num">05</div>
          <h4>Delivery</h4>
          <p>Gallery within 4–6 weeks</p>
        </div>
      </div>
    </div>

    <!-- FAQ -->
    <div style="background: var(--dark); padding: 80px 40px;">
      <div class="wedding-faq" style="padding: 0;">
        <div class="wedding-faq-header">
          <span class="eyebrow">FAQ</span>
          <h2>Everything You Need to Know</h2>
        </div>
        <div class="faq-item">
          <button class="faq-question" onclick="toggleFaq(this)">
            In which regions do you cover weddings?
            <span class="faq-icon">+</span>
          </button>
          <div class="faq-answer">We are based in Hamburg and cover weddings throughout Germany — from Hamburg to Munich, Berlin, Cologne and beyond. Travel costs for locations outside Hamburg are discussed individually.</div>
        </div>
        <div class="faq-item">
          <button class="faq-question" onclick="toggleFaq(this)">
            Do you offer photo and video together?
            <span class="faq-icon">+</span>
          </button>
          <div class="faq-answer">Yes — we offer photography only, videography only, or both combined. Our combo packages are especially popular as you get a perfectly coordinated result from a single creative team.</div>
        </div>
        <div class="faq-item">
          <button class="faq-question" onclick="toggleFaq(this)">
            How does the booking process work?
            <span class="faq-icon">+</span>
          </button>
          <div class="faq-answer">You send us an inquiry via the form below, we get in touch within 24 hours for a consultation call, then confirm your date with a contract and deposit. Simple and stress-free.</div>
        </div>
        <div class="faq-item">
          <button class="faq-question" onclick="toggleFaq(this)">
            How would you describe your style?
            <span class="faq-icon">+</span>
          </button>
          <div class="faq-answer">Cinematic and emotional. We focus on real moments, authentic feelings, and artistic composition. Every wedding is unique — we adapt to your style, not the other way around.</div>
        </div>
      </div>
    </div>

    <!-- Request form -->
    <div class="wedding-request" id="wedding-request">
      <div class="wedding-request-inner">
        <span class="eyebrow">Price List</span>
        <h2>Request Your Offer</h2>
        <p>Fill in your details and receive our complete price list as a PDF — directly and without obligation.</p>
        <form class="wedding-form" onsubmit="handleWeddingForm(event)">
          <div class="wedding-form-row">
            <input type="text" name="name" placeholder="Your Name *" required>
            <input type="email" name="email" placeholder="Your Email *" required>
          </div>
          <div class="wedding-form-row">
            <input type="date" name="date" placeholder="Wedding Date">
            <select name="package">
              <option value="" disabled selected>What are you interested in?</option>
              <option value="photo-video">Photo + Video Combined</option>
              <option value="photo">Photography Only</option>
              <option value="video">Videography Only</option>
              <option value="unsure">Not sure yet</option>
            </select>
          </div>
          <input type="text" name="location" placeholder="Wedding Location / City">
          <button type="submit" class="wedding-submit">Download Price List as PDF →</button>
          <p class="wedding-form-note">No spam. We'll also get in touch personally within 24 hours.</p>
        </form>
      </div>
    </div>

  </section>

  <script>
    function toggleFaq(btn) {
      const item = btn.closest('.faq-item');
      const isOpen = item.classList.contains('open');
      document.querySelectorAll('.faq-item.open').forEach(el => el.classList.remove('open'));
      if (!isOpen) item.classList.add('open');
    }

    function handleWeddingForm(e) {
      e.preventDefault();
      // Trigger PDF download
      const link = document.createElement('a');
      link.href = 'Marharian-Preisliste-Hochzeit-2026.pdf';
      link.download = 'Marharian-Preisliste-Hochzeit-2026.pdf';
      document.body.appendChild(link);
      link.click();
      document.body.removeChild(link);
      // Show thank you message
      const form = e.target;
      form.innerHTML = '<p style="color: var(--gold); font-family: var(--font-heading); font-size: 18px; letter-spacing: 0.1em; text-align: center; padding: 32px 0;">Thank you! Your price list is downloading.<br><span style=\\"font-size:14px; color: rgba(255,255,255,0.5); font-family: var(--font-body); letter-spacing: normal;\\">We will be in touch within 24 hours.</span></p>';
    }
  </script>
"""

content = content.replace('</body>', wedding_section + '\n</body>')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ Done! Weddings section added successfully.")
print("Now run: cd /Users/sosmarharyan/homepage && git add -A && git commit -m 'Add Weddings section with portfolio, FAQ and price request form' && git push")
