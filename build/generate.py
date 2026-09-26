#!/usr/bin/env python3
"""
First Spin DJ Bootcamp — static page generator.
Emits the shared-chrome pages (header + body + footer) as plain static HTML.
Run:  python3 build/generate.py   (from the site root)
Home, Miami and Broward are authored by hand; this generates the rest.
Edit the BODIES below and re-run to regenerate.
"""
import os, html

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com" />'
         '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />'
         '<link href="https://fonts.googleapis.com/css2?family=Bangers&family=Montserrat:wght@400;500;600;700;800;900&display=swap" rel="stylesheet" />')

HEADER = '''<a class="skip-link" href="#main">Skip to main content</a>
<header class="site-header">
  <div class="wrap">
    <nav class="nav" aria-label="Primary" data-open="false">
      <a class="brand" href="/" aria-label="First Spin DJ Bootcamp — home"><img class="brand-logo" src="/img/firstspin-logo.png" width="987" height="1086" alt="First Spin DJ Bootcamp logo." /></a>
      <div class="nav-links" id="nav-links">
        <div class="nav-item">
          <a href="/summer-2027/" aria-haspopup="true">Summer 2027 <svg class="caret" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" aria-hidden="true"><path d="m6 9 6 6 6-6"/></svg></a>
          <div class="subnav"><a href="/miami-dj-bootcamp/">Miami</a><a href="/broward-dj-bootcamp/">Broward</a></div>
        </div>
        <a href="/for-parents/">For Parents</a>
        <a href="/impact/">Our Impact</a>
        <a href="/sponsors/">Sponsors &amp; Partners</a>
        <a href="/host/">Host First Spin</a>
        <a href="/about/">About</a>
        <a href="/contact/">Contact</a>
      </div>
      <div class="nav-cta">
        <a class="btn btn-ghost" href="/donate/" data-cta="donate" data-track-loc="nav">Donate</a>
        <a class="btn btn-primary" href="/#interest" data-cta="interest" data-track-loc="nav">Join the 2027 Interest List</a>
      </div>
      <button class="nav-toggle" aria-expanded="false" aria-controls="nav-links" aria-label="Open menu"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" aria-hidden="true"><path d="M4 6h16M4 12h16M4 18h16"/></svg></button>
    </nav>
  </div>
</header>'''

def crumbs(items):
    # items: list of (name, href or None)
    lis = []
    for name, href in items:
        if href:
            lis.append(f'<li><a href="{href}">{name}</a></li>')
        else:
            lis.append(f'<li aria-current="page">{name}</li>')
    return ('<nav class="breadcrumbs" aria-label="Breadcrumb"><div class="wrap"><ol>'
            + ''.join(lis) + '</ol></div></nav>')

FOOTER = '''<footer class="site-footer">
  <div class="wrap">
    <div class="footer-grid">
      <div class="footer-brand">
        <a class="brand" href="/" aria-label="First Spin DJ Bootcamp — home"><img class="brand-logo footer-logo" src="/img/firstspin-logo.png" width="987" height="1086" alt="First Spin DJ Bootcamp logo." /></a>
        <p>Learn the Craft. Live the Culture. Free DJ education, mentorship and creative development for ages 7+ in South Florida. A nonprofit educational initiative of <a href="https://themixher.org" target="_blank" rel="noopener">MixHer Inc.</a>, a 501(c)(3) nonprofit organization.</p>
        <div class="footer-social" aria-label="Social media">
          <a href="https://www.instagram.com/FirstSpinDJBootcamp" target="_blank" rel="noopener" aria-label="Instagram"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r="1" fill="currentColor" stroke="none"/></svg></a>
          <a href="https://www.tiktok.com/@FirstSpinDJBootcamp" target="_blank" rel="noopener" aria-label="TikTok"><svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M16 3c.3 2.2 1.7 3.9 3.9 4.2v3c-1.5.1-2.8-.3-4-1v6.3A5.5 5.5 0 1 1 9 10.1v3.1a2.5 2.5 0 1 0 1.8 2.4V3H16Z"/></svg></a>
        </div>
      </div>
      <div class="footer-col"><h4>Program</h4><a href="/summer-2027/">Summer 2027</a><a href="/miami-dj-bootcamp/">Miami</a><a href="/broward-dj-bootcamp/">Broward</a><a href="/for-parents/">For Parents</a><a href="/impact/">Our Impact</a><a href="/about/">About</a></div>
      <div class="footer-col"><h4>Get Involved</h4><a href="/#interest" data-cta="interest">Join the 2027 Interest List</a><a href="/sponsors/">Sponsors &amp; Partners</a><a href="/donate/" data-cta="donate">Donate</a><a href="/host/">Host First Spin</a><a href="/contact/">Contact</a></div>
      <div class="footer-col"><h4>Connect</h4><a href="https://www.instagram.com/FirstSpinDJBootcamp" target="_blank" rel="noopener">Instagram</a><a href="https://www.tiktok.com/@FirstSpinDJBootcamp" target="_blank" rel="noopener">TikTok</a><a href="mailto:FirstSpinDJBootcamp@gmail.com">Email Us</a></div>
    </div>
    <div class="nonprofit">
      <div class="seal" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M12 2 4 5v6c0 5 3.4 8.5 8 11 4.6-2.5 8-6 8-11V5l-8-3Z"/><path d="m9 12 2 2 4-4"/></svg></div>
      <div><h4>Nonprofit Information</h4><dl><dt>Legal name</dt><dd>MixHer Inc.</dd><dt>EIN</dt><dd>99-1568393</dd><dt>Status</dt><dd>501(c)(3) tax-exempt nonprofit organization</dd><dt>Website</dt><dd><a href="https://themixher.org" target="_blank" rel="noopener">TheMixHer.org</a></dd><dt>Address</dt><dd>1000 5th St, Suite 200 Y8, Miami Beach, FL 33139</dd></dl></div>
    </div>
    <div class="footer-bottom">
      <span>&copy; <span data-year>2027</span> First Spin DJ Bootcamp / MixHer Inc.</span>
      <div class="links"><a href="/privacy/">Privacy Policy</a><a href="/accessibility/">Accessibility</a><a href="/donate/">Donation Information</a><a href="/contact/">Contact</a></div>
    </div>
    <p class="disclosure">First Spin DJ Bootcamp is a nonprofit educational initiative of MixHer Inc., a 501(c)(3) nonprofit organization. Contributions to MixHer Inc. designated for First Spin DJ Bootcamp are tax-deductible to the extent permitted by law. Please consult your tax adviser regarding your individual circumstances.</p>
  </div>
</footer>'''

def page(path, title, desc, body, canonical, extra_head="", data_page="", robots=""):
    robots_tag = f'<meta name="robots" content="{robots}" />' if robots else ""
    doc = f'''<!DOCTYPE html>
<html lang="en" class="no-js">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>{title}</title>
<meta name="description" content="{html.escape(desc, quote=True)}" />
<link rel="canonical" href="{canonical}" />
<meta name="theme-color" content="#02090A" />{robots_tag}
<meta property="og:type" content="website" />
<meta property="og:site_name" content="First Spin DJ Bootcamp" />
<meta property="og:title" content="{html.escape(title, quote=True)}" />
<meta property="og:description" content="{html.escape(desc, quote=True)}" />
<meta property="og:url" content="{canonical}" />
<meta property="og:image" content="https://firstspindjbootcamp.org/img/og-card.png" />
<meta property="og:image:width" content="1200" /><meta property="og:image:height" content="630" />
<meta name="twitter:card" content="summary_large_image" />
<meta name="twitter:image" content="https://firstspindjbootcamp.org/img/og-card.png" />
<link rel="icon" href="/favicon.svg" type="image/svg+xml" />
<link rel="apple-touch-icon" href="/favicon.svg" />
<link rel="manifest" href="/site.webmanifest" />
{FONTS}
<link rel="stylesheet" href="/styles.css" />
{extra_head}
</head>
<body{(' data-page="'+data_page+'"') if data_page else ''}>
{HEADER}
{body}
{FOOTER}
<script src="/main.js"></script>
</body>
</html>'''
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w") as f:
        f.write(doc)
    print("wrote", path)

# reusable bits ------------------------------------------------------------
def hero(eyebrow, h1, lede, ctas, art=True, pills=None):
    art_cls = " has-art" if art else ""
    pill_html = ""
    if pills:
        pill_html = '<div class="hero-season">' + ''.join(f'<span class="pill">{p}</span>' if i==0 else f'<span>{p}</span>' for i,p in enumerate(pills)) + '</div>'
    return f'''<section class="hero{art_cls}" aria-labelledby="h1">
  <div class="wrap"><div class="hero-copy" style="max-width:760px">
    <span class="hero-badge"><span class="dot"></span> {eyebrow}</span>
    <h1 id="h1">{h1}</h1>
    <p class="lede">{lede}</p>
    {pill_html}
    <div class="hero-cta btn-row">{ctas}</div>
    <p class="credibility"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M12 2 4 5v6c0 5 3.4 8.5 8 11 4.6-2.5 8-6 8-11V5l-8-3Z"/><path d="m9 12 2 2 4-4"/></svg> A nonprofit educational initiative of MixHer Inc., a 501(c)(3)</p>
  </div></div>
</section>'''

def check_items(items):
    svg = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" aria-hidden="true"><path d="M20 6 9 17l-5-5"/></svg>'
    return ''.join(f'<li>{svg}{i}</li>' for i in items)

def faq(items):
    chev = '<svg class="chev" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" aria-hidden="true"><path d="m6 9 6 6 6-6"/></svg>'
    out = '<div class="faq-list">'
    for q, a in items:
        out += f'<details class="faq-item"><summary>{q}{chev}</summary><div class="faq-body"><p>{a}</p></div></details>'
    return out + '</div>'

INTEREST_BTN = '<a class="btn btn-primary btn-lg" href="/#interest" data-cta="interest" data-track-loc="{loc}">Join the 2027 Interest List</a>'

# ==========================================================================
# PAGES
# ==========================================================================

# ---- Summer 2027 ----
summer_body = crumbs([("Home","/"),("Summer 2027",None)]) + hero(
  "Summer 2027",
  'First Spin DJ Bootcamp &mdash; <span class="hl">Summer 2027</span>',
  "Seven weeks of music, creativity, confidence &amp; culture. First Spin returns in Summer 2027 serving families in both Miami-Dade and Broward County. The free seven-week experience gives students ages 7+ hands-on access to DJ education, mentorship, entrepreneurship and live performance.",
  INTEREST_BTN.format(loc="summer-hero") + '<a class="btn btn-ghost" href="/host/" data-track="host_click" data-track-loc="summer-hero">Help Us Secure a Location</a>',
  pills=["Summer 2027 · June–August","Miami-Dade & Broward County"]
) + '''
<div class="ticker" aria-hidden="true"><div class="ticker-track">
<div class="ticker-seg"><span class="word t">Summer 2027</span><span class="dotmark"></span><span class="word">Ages 7+</span><span class="dotmark"></span><span class="word o">100% Free</span><span class="dotmark"></span><span class="word">Seven Weeks</span><span class="dotmark"></span><span class="word t">Live Showcase</span><span class="dotmark"></span></div>
<div class="ticker-seg"><span class="word t">Summer 2027</span><span class="dotmark"></span><span class="word">Ages 7+</span><span class="dotmark"></span><span class="word o">100% Free</span><span class="dotmark"></span><span class="word">Seven Weeks</span><span class="dotmark"></span><span class="word t">Live Showcase</span><span class="dotmark"></span></div>
</div></div>
<section class="section-cream reveal"><div class="wrap">
<span class="eyebrow">The 2027 Season</span>
<h2 class="section-title">Everything You Need to <span class="accent">Know</span></h2>
<div class="feature-grid">
<div class="feature"><h3>Summer Season</h3><p>June&ndash;August 2027. Program dates and registration go to our interest list first.</p></div>
<div class="feature"><h3>Cost</h3><p>Free for participating families.</p></div>
<div class="feature"><h3>Experience</h3><p>Beginner-friendly. No prior DJ experience required.</p></div>
<div class="feature"><h3>Ages</h3><p>Open to students ages 7 and up.</p></div>
<div class="feature"><h3>Miami-Dade</h3><p>Summer 2027 &middot; Miami-Dade County. <a href="/miami-dj-bootcamp/" style="color:var(--orange-deep);font-weight:700">Miami interest list &rarr;</a></p></div>
<div class="feature"><h3>Broward</h3><p>Summer 2027 &middot; Broward County. <a href="/broward-dj-bootcamp/" style="color:var(--orange-deep);font-weight:700">Broward interest list &rarr;</a></p></div>
</div></div></section>
<section class="section-teal reveal"><div class="wrap">
<span class="eyebrow on-dark">The Seven-Week Experience</span>
<h2 class="section-title" style="color:#fff">Seven Weeks. Real Skills. <span class="accent-t">One Big Showcase.</span></h2>
<div class="timeline">
<div class="tl-card"><div class="num">1</div><div class="wk">Week 1</div><h3>Gear Setup &amp; Sound Basics</h3></div>
<div class="tl-card"><div class="num">2</div><div class="wk">Weeks 2–3</div><h3>Mixing, Beatmatching &amp; Flow</h3></div>
<div class="tl-card"><div class="num">3</div><div class="wk">Week 4</div><h3>Music Theory &amp; Playlist Building</h3></div>
<div class="tl-card"><div class="num">4</div><div class="wk">Week 5</div><h3>Branding &amp; Entrepreneurship</h3></div>
<div class="tl-card"><div class="num">5</div><div class="wk">Week 6</div><h3>Stage Confidence &amp; Crowd Control</h3></div>
<div class="tl-card finale"><div class="num">6</div><div class="wk">Week 7</div><h3>Live Showcase Performance</h3></div>
</div></div></section>
<section class="final-cta has-art reveal"><div class="wrap">
<h2>Join the 2027 <span class="hl">Priority List.</span></h2>
<p>Be first to receive program dates, locations and registration information for Summer 2027.</p>
<div class="btn-row"><a class="btn btn-primary btn-lg" href="/#interest" data-cta="interest" data-track-loc="summer-final">Join the 2027 Priority Interest List</a></div>
</div></section>'''
page("summer-2027/index.html",
     "First Spin DJ Bootcamp — Summer 2027 | Free Youth DJ Program",
     "First Spin DJ Bootcamp returns Summer 2027 (June–August) with a free seven-week DJ program for ages 7+ in Miami-Dade and Broward County. Join the 2027 priority interest list.",
     summer_body, "https://firstspindjbootcamp.org/summer-2027/", data_page="summer")

# ---- For Parents ----
parents_body = crumbs([("Home","/"),("For Parents",None)]) + hero(
  "For Parents & Guardians",
  'Your Child Doesn&rsquo;t Need Experience. <span class="hl">They Just Need Curiosity.</span>',
  "First Spin is designed to welcome beginners. Students do not need to own DJ equipment or know how to DJ before joining. We create a supportive environment where young people learn at their own pace while being challenged to grow creatively and personally.",
  INTEREST_BTN.format(loc="parents-hero")
) + '''
<section class="section-cream reveal"><div class="wrap"><div class="split">
<div>
<span class="eyebrow">What Your Student Will Learn</span>
<h2 class="section-title">Real Skills, <span class="accent">Real Growth</span></h2>
<ul class="check-list">''' + check_items([
"DJ equipment and sound basics","Mixing and beatmatching","Song structure and music organization",
"Playlist building","DJ branding and entrepreneurship","Professionalism","Stage confidence and crowd awareness","Performance preparation"]) + '''</ul>
</div>
<div class="split-media"><div class="frame"><img src="/img/firstspin-hands-on.jpg" width="1600" height="1067" loading="lazy" alt="A First Spin mentor guiding two students on a DJ controller." /></div></div>
</div></div></section>
<section class="section-teal reveal"><div class="wrap">
<span class="eyebrow on-dark">Parents Are Part of the Team</span>
<h2 class="section-title" style="color:#fff">What Parents Can <span class="accent-t">Expect</span></h2>
<div class="parent-callout" style="background:rgba(255,255,255,.05);max-width:820px">
<h3>Parents Stay Connected</h3>
<p>First Spin believes parents are part of the team. Enrolled families receive ongoing program updates and access to our dedicated parent communication group throughout the summer, so you know what students are learning, what is coming next and how to prepare for important program moments.</p>
</div>
<ul class="check-list" style="margin-top:1.6rem">''' + check_items([
"Clear communication throughout the program","Program updates and reminders",
"A dedicated parent communication group for enrolled families","Information about showcase preparation",
"Advance notice about important dates and requirements","A team committed to helping students grow"]) + '''</ul>
<p class="loc-note" style="color:#9fc0bd;margin-top:1.2rem">Parents and guardians handle all registration and communication for minors. Children do not create website accounts.</p>
</div></section>
<section class="section-cream reveal"><div class="wrap">
<span class="eyebrow">Inside the Class</span>
<h2 class="section-title">See the Class in <span class="accent">Action</span></h2>
<p class="lede">Real First Spin students, learning hands-on from experienced instructors on professional gear.</p>
<div class="moment-gallery class-gallery">
<figure class="moment"><span class="live"><span class="rec"></span> Live class</span><video autoplay muted loop playsinline preload="metadata" poster="/img/class-clip-poster.jpg" aria-label="A First Spin student learning to mix during class."><source src="/img/class-clip.mp4" type="video/mp4" /></video><figcaption>In the mix &middot; live class</figcaption></figure>
<figure class="moment"><img src="/img/class-learning-1.jpg" width="1400" height="1050" loading="lazy" alt="A First Spin instructor teaching a young student to mix on a Pioneer DJ controller." /><figcaption>Hands-on coaching</figcaption></figure>
<figure class="moment"><img src="/img/class-learning-2.jpg" width="1400" height="1050" loading="lazy" alt="A young First Spin student learning to DJ on professional equipment." /><figcaption>Learning the gear</figcaption></figure>
<figure class="moment"><img src="/img/class-learning-3.jpg" width="1400" height="1050" loading="lazy" alt="A First Spin instructor guiding a student through cueing on the decks." /><figcaption>Cueing the next track</figcaption></figure>
</div>
</div></section>
<section class="section-cream reveal" style="background:linear-gradient(180deg,#eafaf8,var(--cream))"><div class="wrap">
<span class="eyebrow">Parent FAQ</span>
<h2 class="section-title">Parent Questions &amp; <span class="accent">Answers</span></h2>''' + faq([
("What ages can participate?","First Spin serves students ages 7 and up."),
("Does my child need DJ experience?","No. Beginners are welcome."),
("Does my child need their own equipment?","No. First Spin provides access to DJ equipment during class."),
("How much does the program cost?","The summer bootcamp is offered at no cost to participating families."),
("How long is the program?","Seven weeks."),
("When is the 2027 program?","Between June and August 2027. Dates and registration are announced to our interest list first."),
("Where will the program take place?","First Spin is expanding to both Miami-Dade and Broward County for Summer 2027. Program locations are shared with interest-list families first."),
("Is attendance important?","Yes. Because students build skills week by week and prepare for a final showcase, consistent attendance is important. Specific expectations are provided during enrollment."),
("Will parents receive updates?","Yes. Enrolled parents receive ongoing program communication and access to our parent communication group."),
("Is there a performance?","Yes. The curriculum includes preparation for a live showcase experience."),
("How do I get started?","Join the 2027 interest list. You'll receive a welcome email and future program announcements."),
]) + '''
<div class="btn-row" style="margin-top:1.8rem"><a class="btn btn-primary btn-lg" href="/#interest" data-cta="interest" data-track-loc="parents-faq">Join the 2027 Interest List</a></div>
</div></section>'''
page("for-parents/index.html",
     "DJ Summer Camp for Kids &amp; Teens | Parent Info | First Spin",
     "Learn what parents should know about First Spin DJ Bootcamp, a free seven-week summer DJ program for ages 7+ in Miami-Dade and Broward County.",
     parents_body, "https://firstspindjbootcamp.org/for-parents/", data_page="parents")

# ---- Impact ----
impact_body = crumbs([("Home","/"),("Our Impact",None)]) + hero(
  "Our Impact",
  'Skills You Can Hear. <span class="hl">Confidence You Can See.</span>',
  "First Spin is about more than learning how to mix songs. Students develop skills that extend beyond the DJ booth — creative confidence, preparation, communication, music knowledge, technology skills, entrepreneurial thinking, professionalism, teamwork and performance experience.",
  INTEREST_BTN.format(loc="impact-hero")
) + '''
<section class="section-cream reveal"><div class="wrap">
<span class="eyebrow">Our Growth</span>
<h2 class="section-title">From a Small Start to Serious <span class="accent-t">Momentum</span></h2>
<div class="impact-grid">
<div class="impact-card a"><div class="yr" data-editable>2024</div><p data-editable>One program location</p></div>
<div class="impact-card b"><div class="yr" data-editable>2025</div><p data-editable>Expanded to two program locations</p></div>
<div class="impact-card c"><div class="yr">2027</div><p>Build sustainable Miami-Dade and Broward programs while strengthening the operating structure needed for future growth.</p></div>
</div>
<div class="metric-grid" aria-label="Program facts">
<div class="metric"><b data-editable>2</b><span>Program locations</span></div>
<div class="metric"><b>7</b><span>Week program</span></div>
<div class="metric"><b>7+</b><span>Ages</span></div>
<div class="metric"><b>$0</b><span>Cost to families</span></div>
</div>
</div></section>
<section class="final-cta has-art reveal"><div class="wrap">
<h2>Help Us Reach <span class="hl">More Families.</span></h2>
<p>Cash operating support helps First Spin grow sustainably across Miami-Dade and Broward County.</p>
<div class="btn-row"><a class="btn btn-primary btn-lg" href="/sponsors/" data-track="sponsor_click" data-track-loc="impact-final">Fund First Spin</a><a class="btn btn-teal" href="/#interest" data-cta="interest" data-track-loc="impact-final">Join the 2027 Interest List</a></div>
</div></section>'''
page("impact/index.html",
     "Our Impact | Youth DJ Education in South Florida | First Spin",
     "First Spin DJ Bootcamp builds creative confidence, technology skills and entrepreneurial thinking for South Florida youth. See our growth and 2027 goals.",
     impact_body, "https://firstspindjbootcamp.org/impact/", data_page="impact")

# ---- About ----
about_body = crumbs([("Home","/"),("About",None)]) + hero(
  "About First Spin",
  'Why First Spin <span class="hl">Exists</span>',
  "First Spin was created from a simple belief: young people deserve access. Access to equipment, mentorship, creative spaces, professionals who can show them what is possible — and opportunities that build both talent and confidence. Founder DJ ReRe knows what it feels like to learn without a roadmap. First Spin is her way of creating one for the next generation.",
  INTEREST_BTN.format(loc="about-hero")
) + '''
<section class="section-cream reveal"><div class="wrap"><div class="split">
<div class="split-media"><div class="frame"><img src="/img/dj-rere-on-the-decks.jpg" width="1000" height="1500" loading="lazy" alt="DJ ReRe, founder of First Spin, at the DJ controller." /></div></div>
<div>
<span class="eyebrow">Mission &amp; Vision</span>
<h2 class="section-title">Access, Creativity &amp; <span class="accent">Confidence</span></h2>
<p><strong>Our Mission.</strong> To empower youth and beginners through no-cost DJ education that merges creativity, entrepreneurship and confidence.</p>
<p><strong>Our Vision.</strong> A future where diverse DJs help lead the sound of tomorrow, equipped with technical skills, business knowledge, confidence and opportunity.</p>
<blockquote class="quote" style="border-color:var(--teal);color:var(--teal-900)">&ldquo;Music connects people. Learning to DJ can also teach you how to lead.&rdquo;<cite style="color:var(--teal-dark)">— DJ ReRe, Founder</cite></blockquote>
</div>
</div></div></section>
<section class="section-teal reveal"><div class="wrap" style="max-width:820px">
<span class="eyebrow on-dark">Our Nonprofit Home</span>
<h2 class="section-title" style="color:#fff">Powered by <span class="accent-t">MixHer Inc.</span></h2>
<p class="lede">First Spin DJ Bootcamp is a nonprofit educational initiative of MixHer Inc., a 501(c)(3) nonprofit organization. Through MixHer Inc., First Spin combines music education, mentorship, entrepreneurship and community engagement to create greater access to the creative industries.</p>
<div class="btn-row" style="margin-top:1.4rem"><a class="btn btn-teal" href="https://themixher.org" target="_blank" rel="noopener">Visit TheMixHer.org</a><a class="btn btn-ghost" href="/impact/">See Our Impact</a></div>
</div></section>'''
page("about/index.html",
     "About First Spin DJ Bootcamp | Free Youth DJ Education",
     "First Spin DJ Bootcamp is a nonprofit educational initiative of MixHer Inc. (501(c)(3)) providing free DJ education, mentorship and creative opportunity for South Florida youth.",
     about_body, "https://firstspindjbootcamp.org/about/", data_page="about")

# ---- Sponsors & Partners ----
priorities = [
 ("Fund the Program","Provide unrestricted or program-designated financial support that helps First Spin operate consistently.","FUND FIRST SPIN","/donate/","donate"),
 ("Fund an Instructor","Help compensate experienced DJs, mentors and educators for the time and expertise they bring to students.","FUND INSTRUCTOR TIME","/donate/","donate"),
 ("Help Secure a Studio","Provide or underwrite a safe, reliable classroom or studio space in Miami-Dade or Broward County.","HOST FIRST SPIN","/host/",""),
 ("Sponsor the Showcase","Help cover the production, venue, staffing and experience surrounding the students' final performance.","UNDERWRITE THE SHOWCASE","#sponsor-form",""),
 ("Donate Laptops or Technology","DJ stations still need dependable supporting technology — laptops, accessories, software and approved tech.","OFFER TECHNOLOGY","#sponsor-form",""),
 ("Cover Student Hospitality","Help provide snacks, water and basic hospitality throughout the seven-week program.","COVER WEEKLY SNACKS","#sponsor-form",""),
]
prio_html = '<div class="priority-grid">'
for i,(h,p,btn,href,cta) in enumerate(priorities,1):
    cta_attr = f' data-cta="{cta}"' if cta else ''
    prio_html += f'<div class="priority"><div class="n">{i}</div><h3>{h}</h3><p>{p}</p><a class="btn btn-teal" href="{href}"{cta_attr}>{btn.title()}</a></div>'
prio_html += '</div>'

tiers = [
 ("$1,000+","Community Partner","Help cover a specific program need such as student hospitality, materials, technology support or part of an instructor stipend.",["Website recognition","Social media thank-you","Showcase recognition"],"Become a Community Partner",False),
 ("$2,500+","Program Partner","Help fund instructional support, operating costs, student experiences or showcase expenses.",["Website logo placement","Social media feature","Showcase recognition","Invitation to attend the showcase"],"Become a Program Partner",True),
 ("$5,000+","Impact Partner","Help underwrite a meaningful portion of the seven-week experience.",["Prominent website placement","Program &amp; showcase recognition","Dedicated social feature","Community-impact storytelling"],"Become an Impact Partner",False),
 ("$10,000+","Presenting Partner","Help provide major operating support for First Spin's Miami-Dade and Broward growth. Benefits customized with First Spin.",["Premier website recognition","Major showcase recognition","Approved co-branded visibility","Year-round recognition"],"Discuss a Presenting Partnership",False),
]
tier_html = '<div class="tier-grid">'
for amt,name,desc,benefits,btn,feat in tiers:
    bl = ''.join(f'<li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" aria-hidden="true"><path d="M20 6 9 17l-5-5"/></svg>{b}</li>' for b in benefits)
    tier_html += f'<div class="tier{" feature" if feat else ""}"><div class="amt">{amt}</div><h3>{name}</h3><p style="color:var(--muted);font-size:.92rem">{desc}</p><ul>{bl}</ul><a class="btn btn-primary" href="#sponsor-form">{btn}</a></div>'
tier_html += '</div>'

sponsor_body = crumbs([("Home","/"),("Sponsors & Partners",None)]) + hero(
  "Sponsors & Partners",
  'Invest in the Culture. <span class="hl">Help Build What Comes Next.</span>',
  "First Spin has made major progress securing the equipment students need. Now we need partners who can help us operate consistently, compensate talented instructors and mentors, secure strong learning spaces and bring the complete seven-week experience to more families.",
  '<a class="btn btn-primary btn-lg" href="#sponsor-form" data-track="sponsor_click" data-track-loc="sponsors-hero">Start a Partnership Conversation</a><a class="btn btn-ghost" href="/donate/" data-cta="donate" data-track-loc="sponsors-hero">Donate Now</a>',
  art=True
) + f'''
<section class="support reveal"><div class="wrap">
<span class="eyebrow on-dark">Our #1 Need</span>
<h2 class="section-title" style="color:#fff">Operating <span class="accent-t">Funding</span></h2>
<p class="lede">Cash funding gives First Spin the flexibility to cover the real costs required to operate a professional youth program.</p>
<div class="need-1"><div class="head"><span class="tag">1st</span> Cash Operating Support</div><div class="body">
<ul class="give-list">''' + ''.join(f'<li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" aria-hidden="true"><path d="M20 6 9 17l-5-5"/></svg>{x}</li>' for x in [
"Instructor compensation","Mentor compensation","Guest instructor stipends","Program coordination","Administrative &amp; operating costs","Studio and classroom expenses","Student materials","Showcase production","Transportation &amp; logistics when needed","Snacks and water","Music software &amp; subscriptions","Remaining technology needs"]) + '''</ul>
<div class="btn-row" style="margin-top:1.2rem"><a class="btn btn-primary" href="/donate/" data-cta="donate" data-track-loc="sponsors-need1">Fund First Spin</a></div>
</div></div>
<p class="fineprint">Professional equipment support has helped First Spin make major progress. Our next stage is making sure the program has the people, space and operating resources required to deliver a consistent, high-quality experience every summer.</p>
</div></section>
<section class="section-cream reveal"><div class="wrap">
<span class="eyebrow">Industry Equipment Support</span>
<h2 class="section-title">Professional Tools. <span class="accent">Real Access.</span></h2>
<p class="lede"><strong>AlphaTheta</strong> has committed equipment support for six First Spin DJ stations, including controllers, studio monitors and headphones. This commitment is a major step toward giving students access to professional-quality tools without requiring families to purchase equipment &mdash; and evidence that industry leaders believe in what First Spin is building.</p>
<div style="margin:1.5rem 0 0"><div class="alphatheta-logo"><img src="/img/alphatheta-logo.png" width="720" height="250" alt="AlphaTheta logo" loading="lazy" /></div><p class="logo-cap">Confirmed Equipment Partner &middot; 6 DJ Stations</p></div>
</div></section>
<section class="section-cream reveal" style="background:linear-gradient(180deg,#eafaf8,var(--cream))"><div class="wrap">
<span class="eyebrow">What We Need Now</span>
<h2 class="section-title">Help Us Build the Program <span class="accent-t">Around the Equipment</span></h2>
<p class="lede">Equipment alone does not run a seven-week youth program. First Spin needs partners who can help pay the professionals who teach and mentor, secure dependable spaces in Miami-Dade and Broward, and cover the operational costs that let families participate at no cost.</p>
''' + prio_html + '''
</div></section>
<section class="section-teal reveal"><div class="wrap">
<span class="eyebrow on-dark">Why Partner With First Spin?</span>
<h2 class="section-title" style="color:#fff">Your Investment Creates <span class="accent-t">Access</span></h2>
<p class="lede">When your business, foundation or organization partners with First Spin, your support helps remove the financial barriers that can prevent young people from exploring creative technology and professional DJ education.</p>
<ul class="two-col-list" style="color:#eafaf8">''' + ''.join(f'<li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" aria-hidden="true"><path d="M20 6 9 17l-5-5"/></svg>{x}</li>' for x in [
"Professional instruction","Mentorship","Creative confidence","Technology experience","Entrepreneurship skills","Performance experience","Community","Exposure to creative careers"]) + '''</ul>
</div></section>
<section class="section-cream reveal"><div class="wrap">
<span class="eyebrow">Partnership Levels</span>
<h2 class="section-title">Flexible Ways to <span class="accent">Partner</span></h2>
<p class="lede">Benefits are customized around your goals and the program's actual needs. Recognition options are potential and confirmed with First Spin; we do not promise benefits that cannot be delivered.</p>
''' + tier_html + '''
<p class="loc-note">Have another idea? We welcome conversations with businesses, foundations and community organizations. In-kind partners (studio space, laptops, software, printing, food &amp; beverage, photography/video, professional services) are welcome too — all in-kind contributions are discussed and approved before delivery to match an actual program need.</p>
</div></section>
<section id="sponsor-form" class="forms reveal"><div class="wrap">
<span class="eyebrow">Partnership Inquiry</span>
<h2 class="section-title">Start a Partnership <span class="accent">Conversation</span></h2>
<div class="form-card wide" style="margin-top:1.6rem">
<h3>Sponsor &amp; Partner Inquiry</h3><p class="sub">Tell us how you'd like to get involved — a team member will follow up personally.</p>
<form data-form="sponsor" novalidate>
<div class="field-grid">
<div class="field"><label for="s-name">Contact Name <span class="req" aria-hidden="true">*</span></label><input id="s-name" name="contact_name" type="text" required /></div>
<div class="field"><label for="s-org">Company or Organization</label><input id="s-org" name="organization" type="text" /></div>
<div class="field"><label for="s-title">Title</label><input id="s-title" name="title" type="text" /></div>
<div class="field"><label for="s-email">Work Email <span class="req" aria-hidden="true">*</span></label><input id="s-email" name="email" type="email" required /></div>
<div class="field"><label for="s-phone">Phone</label><input id="s-phone" name="phone" type="tel" /></div>
<div class="field"><label for="s-web">Website</label><input id="s-web" name="website" type="url" /></div>
<div class="field"><label for="s-type">Type of Interest</label><select id="s-type" name="interest_type"><option value="">Select…</option><option>Financial sponsorship</option><option>Studio or classroom space</option><option>Technology donation</option><option>Showcase support</option><option>Food or beverage support</option><option>Professional services</option><option>Employee volunteer engagement</option><option>Guest instruction</option><option>Other</option></select></div>
<div class="field"><label for="s-level">Approximate Level</label><select id="s-level" name="level"><option value="">Not sure yet</option><option>Under $1,000</option><option>$1,000–$2,499</option><option>$2,500–$4,999</option><option>$5,000–$9,999</option><option>$10,000+</option><option>In-kind / non-cash</option></select></div>
<div class="field full"><label for="s-msg">Message</label><textarea id="s-msg" name="message"></textarea></div>
</div>
<div class="form-actions"><button type="submit" class="btn btn-primary btn-lg">Start a Partnership Conversation</button><span class="form-hint">We'll follow up personally.</span></div>
<div class="form-success" role="status"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" aria-hidden="true"><path d="M20 6 9 17l-5-5"/></svg><span>Thank you! Your inquiry is in — we'll reach out to explore the best way to partner.</span></div>
</form>
</div>
</div></section>'''
page("sponsors/index.html",
     "Sponsor Youth Music Education in South Florida | First Spin",
     "Partner with First Spin DJ Bootcamp to fund instructors, program operations, studio space and free youth DJ education in Miami-Dade and Broward County.",
     sponsor_body, "https://firstspindjbootcamp.org/sponsors/", data_page="sponsors")

# ---- Donate ----
gift_areas = [
 ("Instructors &amp; Mentors","Help compensate the professionals who teach, guide and encourage First Spin students."),
 ("Program Operations","Help cover the day-to-day costs required to plan, organize and deliver a seven-week program."),
 ("Studio &amp; Classroom Space","Help First Spin secure safe, reliable learning environments in Miami-Dade and Broward County."),
 ("Guest Professionals","Help bring working DJs and creative-industry professionals into the classroom."),
 ("Student Technology","Help provide laptops, software and the supporting technology required for modern DJ education."),
 ("Showcase Experience","Help students perform in front of family and community."),
 ("Student Hospitality","Help provide water, snacks and basic student support during sessions."),
]
gift_html = '<div class="feature-grid">' + ''.join(f'<div class="feature"><h3>{h}</h3><p>{p}</p></div>' for h,p in gift_areas) + '</div>'
donate_body = crumbs([("Home","/"),("Donate",None)]) + hero(
  "Donate",
  'Give a Young Person Access to the <span class="hl">Booth</span>',
  "Talent can be everywhere. Access is not. Your gift helps First Spin provide no-cost DJ education, professional mentorship and real performance experiences to young people in South Florida.",
  '<a class="btn btn-primary btn-lg" href="#" data-cta="donate" data-track-loc="donate-hero">Donate to First Spin</a><a class="btn btn-ghost" href="#monthly" data-track="monthly_click" data-track-loc="donate-hero">Give Monthly</a>'
) + f'''
<section class="section-cream reveal"><div class="wrap" style="max-width:840px">
<p class="lede">First Spin DJ Bootcamp is a nonprofit educational initiative of MixHer Inc., a 501(c)(3) nonprofit organization. <strong>Contributions to MixHer Inc. designated for First Spin DJ Bootcamp are tax-deductible to the extent permitted by law.</strong></p>
</div></section>
<section class="section-cream reveal" style="background:linear-gradient(180deg,#eafaf8,var(--cream))"><div class="wrap">
<span class="eyebrow">Where Your Gift Goes</span>
<h2 class="section-title">Every Gift Keeps the Program <span class="accent">Free</span></h2>
{gift_html}
<div class="parent-callout" style="margin-top:1.8rem;max-width:820px"><h3>Give Where It Matters Most</h3><p>Unrestricted gifts give First Spin the flexibility to direct funding toward the most important needs at the time of your donation. You may also designate: Instructor &amp; Mentor Fund, Miami Program, Broward Program, Student Showcase, or Technology.</p></div>
<div class="btn-row" style="margin-top:1.6rem"><a class="btn btn-primary btn-lg" href="#" data-cta="donate" data-track-loc="donate-mid">Donate to First Spin</a></div>
<p class="loc-note" style="font-size:.86rem">Donations are processed through MixHer Inc. and may be designated for First Spin DJ Bootcamp.</p>
</div></section>
<section id="monthly" class="section-teal reveal"><div class="wrap" style="max-width:820px">
<span class="eyebrow on-dark">Monthly Giving</span>
<h2 class="section-title" style="color:#fff">Keep the Beat Going <span class="accent-t">All Year</span></h2>
<p class="lede">A monthly gift helps First Spin plan ahead, retain talented people and build a stronger program from one summer to the next. Whether it's $10, $25, $50 or more each month, recurring support creates dependable funding before the first student ever walks into class.</p>
<div class="btn-row" style="margin-top:1.2rem"><a class="btn btn-teal" href="#" data-cta="donate" data-track-loc="donate-monthly">Become a Monthly Donor</a></div>
</div></section>'''
page("donate/index.html",
     "Donate to Free Youth DJ Education | First Spin DJ Bootcamp",
     "Help keep First Spin free for families. Donate through MixHer Inc. to support instructors, program operations, studio space and creative education for South Florida youth.",
     donate_body, "https://firstspindjbootcamp.org/donate/", data_page="donate")

# ---- Host ----
host_who = ["Recording studios","Music studios","Creative studios","Schools","Colleges &amp; universities","Community centers","Churches","Youth centers","Parks &amp; recreation facilities","Arts organizations","Cultural centers","Libraries with creative spaces","Corporate community spaces","Event venues","Rehearsal facilities"]
host_need = ["Safe and appropriate for youth","Accessible to families","Available consistently during the seven-week program","Large enough for students, instructors and DJ stations","Climate controlled","Dependable electrical access","Able to accommodate reasonable sound levels","Accessible for equipment loading","Near restrooms","Supports parent drop-off and pickup","Parking or transit access ideal"]
host_brings = ["Established curriculum","Program leadership","Professional DJ instruction","Industry relationships","DJ equipment support","Parent communication","Program branding","Community outreach","Showcase planning","A growing network of families &amp; supporters"]
def two_col(items):
    svg='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" aria-hidden="true"><path d="M20 6 9 17l-5-5"/></svg>'
    return '<ul class="two-col-list">'+''.join(f'<li>{svg}{i}</li>' for i in items)+'</ul>'
host_body = crumbs([("Home","/"),("Host First Spin",None)]) + hero(
  "Host First Spin",
  'Help Give First Spin a <span class="hl">Home</span>',
  "First Spin already has the curriculum, professional leadership, growing industry support and families who want the program. Now we need dependable spaces where young people can learn. Our goal for Summer 2027 is to operate in both Miami-Dade and Broward County.",
  '<a class="btn btn-primary btn-lg" href="#venue-form" data-track="host_click" data-track-loc="host-hero">Offer a Studio or Classroom</a>'
) + f'''
<section class="host reveal"><div class="wrap">
<span class="eyebrow">Who Can Host?</span>
<h2 class="section-title">We&rsquo;re Looking for a <span class="accent">Community Partner</span></h2>
<p class="lede">We are seeking community-minded organizations that may be able to provide, donate, sponsor or significantly discount classroom and showcase space.</p>
<div class="tag-cloud">''' + ''.join(f'<span class="tag">{w}</span>' for w in host_who) + f'''</div>
</div></section>
<section class="section-cream reveal"><div class="wrap"><div class="split">
<div><span class="eyebrow">What We&rsquo;re Looking For</span><h2 class="section-title">The Ideal <span class="accent-t">Space</span></h2>{two_col(host_need)}<p class="loc-note" style="font-size:.86rem">Exact requirements vary by class size and location.</p></div>
<div><span class="eyebrow">What First Spin Brings</span><h2 class="section-title">Not Just an <span class="accent">Empty Room</span></h2>{two_col(host_brings)}</div>
</div></div></section>
<section class="section-teal reveal"><div class="wrap"><div class="loc-grid">
<div class="loc-card miami"><h3>Miami-Dade</h3><span class="status">Summer 2027</span><p>Help us bring First Spin to Miami-Dade for Summer 2027.</p><a class="btn btn-teal" href="#venue-form">Offer a Miami Space</a></div>
<div class="loc-card broward"><h3>Broward</h3><span class="status">Summer 2027</span><p>Help us build First Spin in Broward County for Summer 2027.</p><a class="btn btn-teal" href="#venue-form">Offer a Broward Space</a></div>
</div></div></section>
<section id="venue-form" class="forms reveal"><div class="wrap">
<span class="eyebrow">Tell Us About Your Space</span>
<h2 class="section-title">Offer a <span class="accent">Venue</span></h2>
<div class="form-card wide" style="margin-top:1.6rem">
<h3>Venue &amp; Space Offer</h3><p class="sub">Share the details and we'll be in touch to explore a fit.</p>
<form data-form="venue" novalidate>
<div class="field-grid">
<div class="field"><label for="v-name">Contact Name <span class="req" aria-hidden="true">*</span></label><input id="v-name" name="contact_name" type="text" required /></div>
<div class="field"><label for="v-org">Organization</label><input id="v-org" name="organization" type="text" /></div>
<div class="field"><label for="v-email">Email <span class="req" aria-hidden="true">*</span></label><input id="v-email" name="email" type="email" required /></div>
<div class="field"><label for="v-phone">Phone</label><input id="v-phone" name="phone" type="tel" /></div>
<div class="field"><label for="v-vname">Venue Name</label><input id="v-vname" name="venue_name" type="text" /></div>
<div class="field"><label for="v-county">County</label><select id="v-county" name="county"><option value="">Select…</option><option>Miami-Dade</option><option>Broward</option><option>Other</option></select></div>
<div class="field full"><label for="v-addr">Venue Address</label><input id="v-addr" name="venue_address" type="text" /></div>
<div class="field"><label for="v-space">Type of Space</label><input id="v-space" name="space_type" type="text" placeholder="e.g. classroom, studio, hall" /></div>
<div class="field"><label for="v-cap">Approximate Capacity</label><input id="v-cap" name="capacity" type="text" /></div>
<div class="field"><label for="v-avail">Availability (June–Aug 2027)</label><input id="v-avail" name="availability" type="text" /></div>
<div class="field"><label for="v-offer">Offered As</label><select id="v-offer" name="offered_as"><option value="">Select…</option><option>Donated</option><option>Discounted</option><option>Sponsored</option><option>Standard rental</option><option>Open to discussion</option></select></div>
<div class="field full"><label for="v-notes">Parking, accessibility &amp; notes</label><textarea id="v-notes" name="notes"></textarea></div>
</div>
<div class="form-actions"><button type="submit" class="btn btn-primary btn-lg">Tell Us About Your Space</button><span class="form-hint">We approve all spaces against real program needs.</span></div>
<div class="form-success" role="status"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" aria-hidden="true"><path d="M20 6 9 17l-5-5"/></svg><span>Thank you! We received your space offer and will follow up soon.</span></div>
</form>
</div>
</div></section>'''
page("host/index.html",
     "Host a Youth DJ Program in Miami or Broward | First Spin",
     "Have a studio, classroom or community space? Help First Spin DJ Bootcamp provide free youth DJ education in Miami-Dade or Broward County in Summer 2027.",
     host_body, "https://firstspindjbootcamp.org/host/", data_page="host")

# ---- Contact ----
contact_body = crumbs([("Home","/"),("Contact",None)]) + hero(
  "Contact",
  'Let&rsquo;s <span class="hl">Connect</span>',
  "Whether you are a parent, donor, potential sponsor, venue partner, instructor or community organization, we'd love to hear from you.",
  INTEREST_BTN.format(loc="contact-hero"), art=True
) + '''
<section class="section-cream reveal"><div class="wrap">
<div class="feature-grid">
<div class="feature"><h3>Parents</h3><p>Interested in Summer 2027? The fastest way to stay informed is to join the interest list.</p><a class="btn btn-primary" href="/#interest" data-cta="interest" style="margin-top:.6rem">Join the 2027 Interest List</a></div>
<div class="feature"><h3>Sponsors &amp; Partners</h3><p>Interested in funding or partnering with First Spin?</p><a class="btn btn-teal" href="/sponsors/" style="margin-top:.6rem">Become a Partner</a></div>
<div class="feature"><h3>Venues</h3><p>Have a space in Miami-Dade or Broward County?</p><a class="btn btn-outline" href="/host/" style="margin-top:.6rem">Host First Spin</a></div>
</div>
<p class="loc-note" style="margin-top:1.4rem">General contact: <a href="mailto:FirstSpinDJBootcamp@gmail.com" style="color:var(--orange-deep);font-weight:700">FirstSpinDJBootcamp@gmail.com</a> · Instagram &amp; TikTok <strong>@FirstSpinDJBootcamp</strong></p>
</div></section>
<section class="forms reveal"><div class="wrap">
<span class="eyebrow">Send a Message</span>
<h2 class="section-title">Get in <span class="accent">Touch</span></h2>
<div class="form-card" style="margin-top:1.6rem">
<h3>Contact First Spin</h3><p class="sub">We read every message and reply as soon as we can.</p>
<form data-form="contact" novalidate>
<div class="field-grid">
<div class="field"><label for="c-name">Name <span class="req" aria-hidden="true">*</span></label><input id="c-name" name="name" type="text" required /></div>
<div class="field"><label for="c-email">Email <span class="req" aria-hidden="true">*</span></label><input id="c-email" name="email" type="email" required /></div>
<div class="field"><label for="c-phone">Phone (optional)</label><input id="c-phone" name="phone" type="tel" /></div>
<div class="field"><label for="c-role">I am contacting First Spin as</label><select id="c-role" name="role"><option value="">Select…</option><option>Parent/guardian</option><option>Donor</option><option>Sponsor/business</option><option>Venue/community partner</option><option>Instructor/mentor</option><option>Volunteer</option><option>Media</option><option>School/community organization</option><option>Other</option></select></div>
<div class="field full"><label for="c-msg">Message <span class="req" aria-hidden="true">*</span></label><textarea id="c-msg" name="message" required></textarea></div>
</div>
<div class="form-actions"><button type="submit" class="btn btn-primary btn-lg">Send Message</button></div>
<div class="form-success" role="status"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" aria-hidden="true"><path d="M20 6 9 17l-5-5"/></svg><span>Thanks for reaching out — we'll get back to you soon.</span></div>
</form>
</div>
</div></section>'''
page("contact/index.html",
     "Contact First Spin DJ Bootcamp | Parents, Sponsors &amp; Venues",
     "Contact First Spin DJ Bootcamp — join the 2027 interest list, become a sponsor, offer a venue, or send a message. Serving Miami-Dade and Broward County.",
     contact_body, "https://firstspindjbootcamp.org/contact/", data_page="contact")

# ---- News & Resources ----
news_cats = [
 ("For Parents",["What Parents Should Know Before Their Child's First DJ Class","What Does a Child Actually Learn in DJ Bootcamp?","How DJing Can Help Young People Build Confidence","How First Spin Keeps Parents Connected Throughout the Summer"]),
 ("DJ Education",["What Is Beatmatching? A Beginner-Friendly Explanation","How DJs Build Playlists","Why Learning Song Structure Matters","What Does a DJ Controller Actually Do?"]),
 ("Entrepreneurship",["Why First Spin Teaches Business Alongside DJ Skills","What Young DJs Can Learn About Branding","How Creative Skills Can Become Career Skills"]),
 ("Community Impact",["Why Access to Creative Technology Matters","The Role of Mentorship in Youth Music Programs","How Businesses Can Support Youth Arts Education in Miami","How Broward Organizations Can Invest in Young Creatives"]),
]
news_html = ''
for cat,arts in news_cats:
    news_html += f'<div class="feature"><h3>{cat}</h3><ul style="margin:.4rem 0 0;padding-left:1.1rem;color:var(--muted)">' + ''.join(f'<li style="margin:.3rem 0">{a}</li>' for a in arts) + '</ul></div>'
news_body = crumbs([("Home","/"),("News & Resources",None)]) + hero(
  "News & Resources",
  'First Spin News, Stories &amp; <span class="hl">Resources</span>',
  "Follow the growth of First Spin, meet the people behind the program and learn more about DJ culture, youth creativity and creative career development.",
  INTEREST_BTN.format(loc="news-hero"), art=True
) + f'''
<section class="section-cream reveal"><div class="wrap">
<span class="eyebrow">News &amp; Stories</span>
<h2 class="section-title">Follow the First Spin <span class="accent">Journey</span></h2>
<p class="lede">First Spin news, parent guides, DJ education explainers, entrepreneurship lessons and student stories — all in one place. Join the email community to get new posts and program news each month.</p>
<div class="feature-grid" style="margin-top:2rem">{news_html}</div>
<div class="btn-row" style="margin-top:1.8rem"><a class="btn btn-primary" href="/#interest" data-cta="interest" data-track-loc="news">Join the 2027 Interest List</a></div>
</div></section>'''
page("news/index.html",
     "First Spin News, Stories &amp; Resources | DJ Education",
     "First Spin DJ Bootcamp news, parent resources, DJ education explainers and community stories from South Florida. Follow along and join the email community.",
     news_body, "https://firstspindjbootcamp.org/news/", data_page="news")

# ---- Thank You ----
ty_body = '''<section class="hero has-art" aria-labelledby="h1"><div class="wrap"><div class="hero-copy" style="max-width:760px">
<span class="hero-badge"><span class="dot"></span> Confirmed</span>
<h1 id="h1">You&rsquo;re on the <span class="hl">List!</span></h1>
<p class="lede">Thanks for your interest in First Spin DJ Bootcamp. We're excited to keep you updated as we prepare for Summer 2027. You should receive a welcome email shortly — please add First Spin to your contacts so our updates don't end up in spam.</p>
<div class="hero-cta btn-row"><a class="btn btn-primary btn-lg" href="https://www.instagram.com/FirstSpinDJBootcamp" target="_blank" rel="noopener">Follow First Spin</a><a class="btn btn-ghost" href="/summer-2027/">Explore the Program</a></div>
</div></div></section>
<section class="section-cream reveal"><div class="wrap" style="max-width:760px">
<span class="eyebrow">What&rsquo;s Next</span>
<h2 class="section-title">Between Now &amp; <span class="accent">Summer</span></h2>
<ul class="check-list">''' + check_items([
"Miami-Dade and Broward location updates","Program dates","Registration information","First Spin news &amp; community events","Student stories &amp; important parent information"]) + '''</ul>
</div></section>'''
page("thank-you/index.html",
     "You're on the List | First Spin DJ Bootcamp",
     "Thanks for joining the First Spin DJ Bootcamp 2027 interest list. Watch for a welcome email with Summer 2027 updates for Miami-Dade and Broward County.",
     ty_body, "https://firstspindjbootcamp.org/thank-you/", data_page="thankyou", robots="noindex,follow")

# ---- Privacy ----
priv_body = crumbs([("Home","/"),("Privacy Policy",None)]) + '''<main></main>
<section class="section-cream"><div class="wrap" style="max-width:820px">
<span class="eyebrow">Privacy</span>
<h2 class="section-title">Privacy <span class="accent">Policy</span></h2>
<p class="lede">First Spin DJ Bootcamp (a nonprofit educational initiative of MixHer Inc.) respects your privacy. This site is designed primarily for parents and adults.</p>
<p><strong>Who submits information.</strong> Parents and guardians complete interest forms and registration on behalf of minors. Children do not create website accounts.</p>
<p><strong>What we collect.</strong> Our public interest form intentionally collects only what we need to follow up: parent/guardian name, email, phone, participant age, city, ZIP code and preferred program area, plus an optional note about how you heard about us. Additional information required for enrollment is collected later through our approved parent enrollment process.</p>
<p><strong>How we use it.</strong> To send program announcements, location and registration updates, and monthly First Spin news. We do not sell your information, and we do not publicly display parent contact details, private group links or student information.</p>
<p><strong>Email consent.</strong> Marketing emails are sent only to people who opt in, and every email includes an unsubscribe option.</p>
<p><strong>Questions.</strong> Contact <a href="mailto:FirstSpinDJBootcamp@gmail.com" style="color:var(--orange-deep);font-weight:700">FirstSpinDJBootcamp@gmail.com</a>.</p>
<p class="loc-note" style="font-size:.85rem">This summary is provided for transparency and is not legal advice. First Spin will publish a full policy as the program formalizes.</p>
</div></section>'''
page("privacy/index.html","Privacy Policy | First Spin DJ Bootcamp",
     "How First Spin DJ Bootcamp (MixHer Inc.) collects and uses information. Parents complete forms for minors; we never sell data or expose contact details.",
     priv_body, "https://firstspindjbootcamp.org/privacy/", data_page="privacy")

# ---- Accessibility ----
acc_body = crumbs([("Home","/"),("Accessibility",None)]) + '''<main></main>
<section class="section-cream"><div class="wrap" style="max-width:820px">
<span class="eyebrow">Accessibility</span>
<h2 class="section-title">Accessibility <span class="accent">Statement</span></h2>
<p class="lede">First Spin DJ Bootcamp is committed to making this website usable for everyone, and we work toward WCAG 2.1 AA best practices.</p>
<ul class="check-list">''' + check_items([
"Semantic HTML with a clear heading structure","Keyboard-operable navigation and visible focus states",
"Color choices reviewed for contrast","Descriptive alternative text for meaningful images",
"Labeled form fields and descriptive buttons","Reduced-motion support for animations"]) + '''</ul>
<p style="margin-top:1.2rem">If you encounter an accessibility barrier, please tell us at <a href="mailto:FirstSpinDJBootcamp@gmail.com" style="color:var(--orange-deep);font-weight:700">FirstSpinDJBootcamp@gmail.com</a> and we'll work to fix it.</p>
</div></section>'''
page("accessibility/index.html","Accessibility | First Spin DJ Bootcamp",
     "First Spin DJ Bootcamp is committed to WCAG 2.1 AA accessibility best practices. Report barriers to FirstSpinDJBootcamp@gmail.com.",
     acc_body, "https://firstspindjbootcamp.org/accessibility/", data_page="accessibility")

# ---- 404 ----
notfound_body = '''<section class="hero has-art" style="min-height:60vh;display:flex;align-items:center"><div class="wrap"><div class="hero-copy" style="max-width:640px">
<span class="hero-badge"><span class="dot"></span> 404</span>
<h1 id="h1">This Track Skipped a <span class="hl">Beat.</span></h1>
<p class="lede">We couldn't find that page. Let's get you back to the mix.</p>
<div class="hero-cta btn-row"><a class="btn btn-primary btn-lg" href="/">Back to Home</a><a class="btn btn-ghost" href="/#interest" data-cta="interest">Join the 2027 Interest List</a></div>
</div></div></section>'''
page("404.html","Page Not Found | First Spin DJ Bootcamp",
     "The page you're looking for isn't here. Head back to First Spin DJ Bootcamp.",
     notfound_body, "https://firstspindjbootcamp.org/404.html", data_page="404", robots="noindex,follow")

print("done.")
