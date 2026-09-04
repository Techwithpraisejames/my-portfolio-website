"""Design system: tokens + the entire stylesheet as one string.

Dark editorial direction. The pink accent (#E9A5DE) is the brand constant and is
used sparingly: primary CTA fill, links, section eyebrows, focus ring, hover.
Two typefaces: Fraunces (display) + IBM Plex Sans (body/UI).
"""

FONT_URL = (
    "https://fonts.googleapis.com/css2?"
    "family=Fraunces:opsz,wght@9..144,400;9..144,500;9..144,600&"
    "family=IBM+Plex+Sans:wght@400;500;600&display=swap"
)

BASE_CSS = r"""
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}

:root{
  --ink:#0C0E10;
  --surface:#15181B;
  --surface-2:#1D2126;
  --hairline:rgba(236,233,228,.12);
  --hairline-strong:rgba(236,233,228,.22);
  --text:#ECE9E4;
  --text-dim:#9BA1A6;
  --accent:#E9A5DE;
  --accent-ink:#20141E;

  --measure:66ch;
  --container:1120px;
  --gutter:clamp(20px,5vw,40px);
  --radius:4px;
  --radius-card:8px;

  --step--1:.85rem;
  --step-0:1.0625rem;
  --step-1:1.2rem;
  --step-2:clamp(1.3rem,2.4vw,1.55rem);
  --step-3:clamp(1.85rem,3.5vw,2.5rem);
  --step-4:clamp(2.5rem,5vw,3.7rem);

  --sp-1:4px;--sp-2:8px;--sp-3:12px;--sp-4:16px;--sp-5:24px;
  --sp-6:32px;--sp-7:48px;--sp-8:64px;--sp-9:96px;--sp-10:128px;
}

html{-webkit-text-size-adjust:100%;scroll-behavior:smooth}
@media (prefers-reduced-motion:reduce){
  html{scroll-behavior:auto}
  *,*::before,*::after{animation-duration:.001ms!important;animation-iteration-count:1!important;transition-duration:.001ms!important}
}

body{
  background:var(--ink);
  color:var(--text);
  font-family:"IBM Plex Sans","Segoe UI",system-ui,-apple-system,sans-serif;
  font-size:var(--step-0);
  line-height:1.62;
  font-weight:400;
  -webkit-font-smoothing:antialiased;
  text-rendering:optimizeLegibility;
  overflow-x:hidden;
}

h1,h2,h3,h4{
  font-family:"Fraunces",Georgia,"Times New Roman",serif;
  font-optical-sizing:auto;
  font-weight:500;
  line-height:1.1;
  letter-spacing:-.015em;
  color:var(--text);
  text-wrap:balance;
}
h1{font-size:var(--step-4);line-height:1.04;font-weight:500}
h2{font-size:var(--step-3);margin-bottom:var(--sp-4)}
h3{font-size:var(--step-2);font-weight:500}
h4{font-size:var(--step-1);font-weight:600;font-family:"IBM Plex Sans",system-ui,sans-serif;letter-spacing:0}

p{max-width:var(--measure)}
strong{font-weight:600;color:var(--text)}

a{color:var(--accent);text-decoration:none;text-underline-offset:3px}
a:hover{text-decoration:underline}

img{max-width:100%;height:auto;display:block}

:focus-visible{outline:2px solid var(--accent);outline-offset:3px;border-radius:2px}
:focus:not(:focus-visible){outline:none}

::selection{background:var(--accent);color:var(--accent-ink)}

/* ---------- skip link ---------- */
.skip{
  position:absolute;left:var(--sp-4);top:-60px;z-index:300;
  background:var(--accent);color:var(--accent-ink);
  padding:10px 16px;border-radius:var(--radius);font-weight:600;
  transition:top .15s ease;
}
.skip:focus{top:var(--sp-4);text-decoration:none}

/* ---------- layout ---------- */
.container{max-width:var(--container);margin-inline:auto;padding-inline:var(--gutter)}
.section{padding-block:clamp(56px,9vw,104px)}
.section--tight{padding-block:clamp(40px,6vw,64px)}
.section + .section{border-top:1px solid var(--hairline)}
.stack > * + *{margin-top:var(--sp-5)}
.lede{font-size:var(--step-1);color:var(--text-dim);line-height:1.6;max-width:60ch}

.eyebrow{
  display:inline-block;
  font-size:.75rem;
  font-weight:600;
  letter-spacing:.14em;
  text-transform:uppercase;
  color:var(--accent);
  margin-bottom:var(--sp-4);
}

.section-head{max-width:60ch;margin-bottom:var(--sp-7)}
.section-head p{color:var(--text-dim);margin-top:var(--sp-3)}

/* ---------- buttons ---------- */
.btn{
  display:inline-flex;align-items:center;gap:.5em;
  font-family:inherit;font-size:.95rem;font-weight:600;
  padding:12px 22px;border-radius:var(--radius);
  border:1px solid transparent;cursor:pointer;
  transition:background-color .18s ease,border-color .18s ease,color .18s ease,transform .18s ease;
  text-decoration:none;line-height:1;
}
.btn:hover{text-decoration:none}
.btn--accent{background:var(--accent);color:var(--accent-ink);border-color:var(--accent)}
.btn--accent:hover{background:#f2bfea;border-color:#f2bfea}
.btn--ghost{background:transparent;color:var(--text);border-color:var(--hairline-strong)}
.btn--ghost:hover{border-color:var(--accent);color:var(--accent)}
.btn--on-accent{background:var(--accent-ink);color:var(--text);border-color:var(--accent-ink)}
.btn--on-accent:hover{background:#301f2c}
.btn-row{display:flex;flex-wrap:wrap;gap:var(--sp-4);align-items:center}

.arrow-link{
  display:inline-flex;align-items:center;gap:.4em;
  font-weight:600;font-size:.95rem;color:var(--accent);
}
.arrow-link::after{content:"\2192";transition:transform .18s ease}
.arrow-link:hover{text-decoration:none}
.arrow-link:hover::after{transform:translateX(3px)}

/* ---------- header / nav ---------- */
.site-header{
  position:sticky;top:0;z-index:200;
  background:color-mix(in srgb,var(--ink) 88%,transparent);
  backdrop-filter:blur(10px);
  border-bottom:1px solid var(--hairline);
}
.nav{
  max-width:var(--container);margin-inline:auto;padding:14px var(--gutter);
  display:flex;align-items:center;gap:var(--sp-7);
}
.nav__brand{
  font-family:"Fraunces",Georgia,serif;font-weight:600;font-size:1.15rem;
  color:var(--text);letter-spacing:-.01em;white-space:nowrap;
}
.nav__brand:hover{text-decoration:none;color:var(--text)}
.nav__links{display:flex;gap:var(--sp-5);list-style:none;flex:1}
.nav__links a{
  color:var(--text-dim);font-weight:500;font-size:.95rem;
  padding-block:4px;border-bottom:1px solid transparent;
}
.nav__links a:hover{color:var(--text);text-decoration:none}
.nav__links a[aria-current="page"]{color:var(--text);border-bottom-color:var(--accent)}
.nav__links > li:last-child{display:none}
.nav__cta{margin-left:auto}
.nav__toggle{display:none}

@media (max-width:860px){
  .nav{gap:var(--sp-4)}
  .nav__cta{display:none}
  .nav__links{
    position:fixed;left:0;right:0;top:0;
    height:100vh;height:100dvh;
    flex-direction:column;justify-content:center;align-items:flex-start;
    gap:var(--sp-5);padding:var(--gutter);
    background:var(--ink);
    transform:translateY(-100%);transition:transform .25s ease;
    z-index:250;
  }
  .nav__links.is-open{transform:translateY(0)}
  .nav__links > li:last-child{display:block}
  .nav__links a{font-size:1.5rem;font-family:"Fraunces",Georgia,serif;color:var(--text)}
  .nav__links .nav__menu-cta{
    color:var(--accent-ink);background:var(--accent);
    padding:12px 22px;border-radius:var(--radius);font-family:"IBM Plex Sans",sans-serif;
    font-size:1rem;
  }
  .nav__toggle{
    display:inline-flex;align-items:center;justify-content:center;
    margin-left:auto;width:44px;height:44px;
    background:transparent;border:1px solid var(--hairline-strong);border-radius:var(--radius);
    color:var(--text);cursor:pointer;z-index:260;position:relative;
  }
}

/* ---------- breadcrumbs ---------- */
.breadcrumbs{padding:var(--sp-5) 0 0}
.breadcrumbs ol{list-style:none;display:flex;flex-wrap:wrap;gap:.5em;font-size:var(--step--1);color:var(--text-dim)}
.breadcrumbs li::after{content:"/";margin-left:.5em;color:var(--hairline-strong)}
.breadcrumbs li:last-child::after{content:""}
.breadcrumbs a{color:var(--text-dim)}
.breadcrumbs a:hover{color:var(--accent)}
.breadcrumbs [aria-current="page"]{color:var(--text)}

/* ---------- hero ---------- */
.hero{padding-block:clamp(48px,8vw,88px)}
.hero__grid{display:grid;grid-template-columns:1.35fr .9fr;gap:clamp(32px,6vw,72px);align-items:center}
.hero__title{margin-bottom:var(--sp-5)}
.hero__sub{font-size:var(--step-1);color:var(--text-dim);max-width:52ch;margin-bottom:var(--sp-6);line-height:1.55}
.hero__cred{margin-top:var(--sp-6);font-size:var(--step--1);color:var(--text-dim);letter-spacing:.01em}
.hero__photo{
  width:100%;max-width:360px;aspect-ratio:1/1;object-fit:cover;object-position:center top;
  border-radius:var(--radius-card);border:1px solid var(--hairline);
  justify-self:end;filter:grayscale(.15) contrast(1.03);
}
@media (prefers-reduced-motion:no-preference){
  .hero__reveal{opacity:0;transform:translateY(12px);animation:heroIn .5s ease forwards}
  .hero__reveal:nth-child(2){animation-delay:.06s}
  .hero__reveal:nth-child(3){animation-delay:.12s}
  .hero__reveal:nth-child(4){animation-delay:.18s}
  @keyframes heroIn{to{opacity:1;transform:none}}
}
@media (max-width:820px){
  .hero__grid{grid-template-columns:1fr;gap:var(--sp-6)}
  .hero__photo{order:-1;justify-self:start;max-width:220px}
}

/* ---------- proof strip ---------- */
.proof{padding-block:var(--sp-7)}
.proof p{max-width:none}
.proof__label{font-size:.75rem;letter-spacing:.14em;text-transform:uppercase;color:var(--text-dim);margin-bottom:var(--sp-3)}
.proof__names{font-family:"Fraunces",Georgia,serif;font-size:var(--step-1);color:var(--text);line-height:1.5}
.proof__pubs{margin-top:var(--sp-3);color:var(--text-dim);font-size:var(--step--1)}

/* ---------- generic grid of cards ---------- */
.grid{display:grid;gap:var(--sp-5)}
.grid--2{grid-template-columns:repeat(2,1fr)}
.grid--3{grid-template-columns:repeat(3,1fr)}
.grid--4{grid-template-columns:repeat(2,1fr)}
@media (min-width:900px){.grid--4{grid-template-columns:repeat(4,1fr)}}
@media (max-width:760px){
  .grid--2,.grid--3,.grid--4{grid-template-columns:1fr}
}

.card{
  background:var(--surface);
  border:1px solid var(--hairline);
  border-radius:var(--radius-card);
  padding:var(--sp-6);
  display:flex;flex-direction:column;gap:var(--sp-3);
  transition:border-color .18s ease;
}
.card:hover{border-color:var(--hairline-strong)}
a.card:hover{text-decoration:none}
.card__kicker{font-size:.72rem;letter-spacing:.12em;text-transform:uppercase;color:var(--accent);font-weight:600}
.card__meta{font-size:var(--step--1);color:var(--text-dim)}
.card__title{font-family:"Fraunces",Georgia,serif;font-size:var(--step-1);font-weight:500;color:var(--text);line-height:1.25}
.card p{color:var(--text-dim);font-size:.95rem}
.card__foot{margin-top:auto;padding-top:var(--sp-3)}
a.card:hover .card__title{color:var(--accent)}

/* ---------- pillars ---------- */
.pillars{display:grid;grid-template-columns:repeat(3,1fr);gap:var(--sp-6)}
.pillar{border-top:2px solid var(--accent);padding-top:var(--sp-4)}
.pillar h3{margin-bottom:var(--sp-3)}
.pillar p{color:var(--text-dim);font-size:.98rem}
@media (max-width:760px){.pillars{grid-template-columns:1fr;gap:var(--sp-5)}}

/* ---------- process ---------- */
.process{display:grid;grid-template-columns:repeat(5,1fr);gap:var(--sp-5);counter-reset:step}
.process__step{counter-increment:step;border-top:1px solid var(--hairline-strong);padding-top:var(--sp-4)}
.process__step::before{
  content:counter(step);
  font-family:"Fraunces",Georgia,serif;font-size:1.1rem;color:var(--accent);
  display:block;margin-bottom:var(--sp-3);
}
.process__step h3{font-size:var(--step-1);margin-bottom:var(--sp-2)}
.process__step p{color:var(--text-dim);font-size:.9rem}
@media (max-width:900px){.process{grid-template-columns:1fr;gap:0}
  .process__step{border-top:none;border-left:1px solid var(--hairline-strong);padding:var(--sp-3) 0 var(--sp-5) var(--sp-5)}
}

/* ---------- case study block ---------- */
.cs-row{display:grid;grid-template-columns:160px 1fr;gap:var(--sp-5);padding-block:var(--sp-5);border-top:1px solid var(--hairline)}
.cs-row dt{font-size:.75rem;letter-spacing:.12em;text-transform:uppercase;color:var(--text-dim);font-weight:600}
.cs-row dd{color:var(--text);max-width:var(--measure)}
@media (max-width:700px){.cs-row{grid-template-columns:1fr;gap:var(--sp-2)}}

/* ---------- filter bar ---------- */
.filter-bar{display:flex;flex-wrap:wrap;gap:var(--sp-2);margin-bottom:var(--sp-7)}
.filter-bar button{
  font-family:inherit;font-size:.85rem;font-weight:500;
  padding:8px 14px;border-radius:var(--radius);
  background:transparent;border:1px solid var(--hairline-strong);color:var(--text-dim);
  cursor:pointer;transition:color .15s,border-color .15s,background-color .15s;
}
.filter-bar button:hover{color:var(--text)}
.filter-bar button[aria-pressed="true"]{background:var(--accent);border-color:var(--accent);color:var(--accent-ink)}
.is-hidden{display:none!important}

/* ---------- forms ---------- */
.field{display:flex;flex-direction:column;gap:6px;margin-bottom:var(--sp-5)}
.field label{font-size:.9rem;font-weight:500;color:var(--text)}
.field .req{color:var(--accent)}
.field input,.field select,.field textarea{
  font-family:inherit;font-size:var(--step-0);color:var(--text);
  background:var(--surface);border:1px solid var(--hairline-strong);border-radius:var(--radius);
  padding:11px 13px;width:100%;
}
.field input:focus,.field select:focus,.field textarea:focus{outline:2px solid var(--accent);outline-offset:1px;border-color:transparent}
.field textarea{min-height:130px;resize:vertical}
.field--error input,.field--error textarea{border-color:#e88}
.field__err{font-size:.8rem;color:#e88}
.form-grid{display:grid;grid-template-columns:1fr 1fr;gap:0 var(--sp-5)}
@media (max-width:640px){.form-grid{grid-template-columns:1fr}}

/* ---------- cta band ---------- */
.cta-band{background:var(--accent);color:var(--accent-ink);text-align:center}
.cta-band h2,.cta-band p{color:var(--accent-ink);margin-inline:auto}
.cta-band p{margin-top:var(--sp-3);margin-bottom:var(--sp-6);opacity:.85}

/* ---------- video ---------- */
.video-grid{display:grid;grid-template-columns:repeat(2,1fr);gap:var(--sp-5)}
.video-grid iframe{width:100%;aspect-ratio:16/9;border:1px solid var(--hairline);border-radius:var(--radius-card)}
@media (max-width:700px){.video-grid{grid-template-columns:1fr}}

/* ---------- links list ---------- */
.link-list{list-style:none;display:flex;flex-wrap:wrap;gap:var(--sp-4)}
.link-list a{color:var(--text-dim);font-size:.95rem}
.link-list a:hover{color:var(--accent)}

/* ---------- footer ---------- */
.site-footer{border-top:1px solid var(--hairline);padding-block:var(--sp-8)}
.site-footer__grid{display:flex;flex-wrap:wrap;gap:var(--sp-6);justify-content:space-between;align-items:flex-start}
.site-footer__brand{font-family:"Fraunces",Georgia,serif;font-size:1.05rem;color:var(--text);margin-bottom:var(--sp-2)}
.site-footer__tag{color:var(--text-dim);font-size:var(--step--1);max-width:34ch}
.site-footer nav{display:flex;flex-wrap:wrap;gap:var(--sp-5)}
.site-footer nav a{color:var(--text-dim);font-size:.9rem}
.site-footer nav a:hover{color:var(--accent)}
.site-footer__legal{margin-top:var(--sp-6);color:var(--text-dim);font-size:.8rem}

/* ---------- misc ---------- */
.placeholder{
  border:1px dashed var(--hairline-strong);border-radius:var(--radius-card);
  padding:var(--sp-5);color:var(--text-dim);font-size:.9rem;
  background:repeating-linear-gradient(45deg,transparent,transparent 10px,rgba(236,233,228,.02) 10px,rgba(236,233,228,.02) 20px);
}
.prose > * + *{margin-top:var(--sp-5)}
.prose h2{margin-top:var(--sp-8)}
.prose h3{margin-top:var(--sp-6)}
.prose ul{padding-left:1.2em;color:var(--text-dim)}
.prose li + li{margin-top:var(--sp-2)}
.muted{color:var(--text-dim)}
.center{text-align:center}
"""
