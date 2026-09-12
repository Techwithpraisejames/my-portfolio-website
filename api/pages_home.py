"""Homepage sales page. Section order is fixed by the brief."""
from components import arrow_link, cta_band, insight_card, service_card, work_card
from content import (
    CASE_STUDIES, CLIENTS, INSIGHTS, NEWSLETTER, PILLARS, PROCESS, SERVICES, featured_work,
)
from seo import PageMeta, person, website
from shell import render_page

META = PageMeta(
    title="Praise James | AI and Developer Tools Technical Writer",
    description=(
        "Praise James writes developer tutorials, technical articles, benchmarks, and thought "
        "leadership for AI, machine learning, and developer tool companies."
    ),
    path="/",
)


def _hero() -> str:
    return """
<section class="section hero">
  <div class="container">
    <div class="hero__grid">
      <div>
        <h1 class="hero__title hero__reveal">Technical writer for AI and developer tool companies.</h1>
        <p class="hero__sub hero__reveal">I write benchmarks, developer tutorials, architecture guides, and technical analysis for companies building products developers need to understand and use.</p>
        <div class="btn-row hero__reveal">
          <a class="btn btn--accent" href="/work">See my work &rarr;</a>
          <a class="btn btn--ghost" href="/contact">Hire me &rarr;</a>
        </div>
      </div>
      <img class="hero__photo" src="/media/praise.jpg" width="360" height="360" fetchpriority="high"
           alt="Praise James, technical writer for AI and developer-focused companies">
    </div>
  </div>
</section>
""".strip()


def _proof() -> str:
    names = " &middot; ".join(c for c in CLIENTS)
    return f"""
<section class="proof">
  <div class="container">
    <p class="proof__label">Written for</p>
    <p class="proof__names">{names}</p>
  </div>
</section>
""".strip()


def _services() -> str:
    cards = "".join(service_card(s) for s in SERVICES)
    return f"""
<section class="section">
  <div class="container">
    <div class="section-head">
      <span class="eyebrow">Services</span>
      <h2>Technical content backed by research and hands-on testing.</h2>
      <p>I help AI and developer tool companies publish articles that developers can learn from, follow, and use to make technical decisions.</p>
    </div>
    <div class="grid grid--4">{cards}</div>
  </div>
</section>
""".strip()


def _selected_work() -> str:
    cards = "".join(work_card(w) for w in featured_work(4))
    return f"""
<section class="section">
  <div class="container">
    <div class="section-head">
      <span class="eyebrow">Selected work</span>
      <h2>Read the work and judge for yourself.</h2>
      <p>My portfolio includes original benchmarks, developer tutorials, AI architecture guides, and analysis published by technical companies and developer publications.</p>
    </div>
    <div class="grid grid--2">{cards}</div>
    <p style="margin-top:var(--sp-6)">{arrow_link("See the full portfolio", "/work")}</p>
  </div>
</section>
""".strip()


def _why() -> str:
    pillars = "".join(
        f'<div class="pillar"><h3>{p["title"]}</h3><p>{p["body"]}</p></div>' for p in PILLARS
    )
    return f"""
<section class="section">
  <div class="container">
    <div class="section-head">
      <span class="eyebrow">Why Praise</span>
      <h2>I do the work behind the writing.</h2>
    </div>
    <div class="pillars">{pillars}</div>
  </div>
</section>
""".strip()


def _case_studies() -> str:
    real = [c for c in CASE_STUDIES if not c.get("placeholder")][:3]
    cards = "".join(f"""
    <a class="card" href="/work/case-studies/{c['slug']}">
      <span class="card__kicker">Case study</span>
      <span class="card__title">{c['title']}</span>
      <span class="card__meta">{c['client']}</span>
      <p><strong>Challenge.</strong> {c['challenge']}</p>
      <p><strong>Approach.</strong> {c['approach']}</p>
      <p><strong>Outcome.</strong> {c['outcome']}</p>
      <span class="card__foot"><span class="arrow-link">View case study</span></span>
    </a>""" for c in real)
    return f"""
<section class="section">
  <div class="container">
    <div class="section-head">
      <span class="eyebrow">Case studies</span>
      <h2>See how I approach the brief.</h2>
      <p>Each case study covers the research, editorial decisions, finished work, and results behind a published project.</p>
    </div>
    <div class="grid grid--3">{cards}</div>
    <p style="margin-top:var(--sp-6)">{arrow_link("All case studies", "/work/case-studies")}</p>
  </div>
</section>
""".strip()


def _process() -> str:
    steps = "".join(
        f'<div class="process__step"><h3>{s["title"]}</h3><p>{s["body"]}</p></div>' for s in PROCESS
    )
    return f"""
<section class="section">
  <div class="container">
    <div class="section-head">
      <span class="eyebrow">Process</span>
      <h2>How I work</h2>
    </div>
    <div class="process">{steps}</div>
  </div>
</section>
""".strip()


def _about_teaser() -> str:
    return f"""
<section class="section">
  <div class="container">
    <div class="section-head">
      <span class="eyebrow">About</span>
      <h2>I trace ideas back to the source.</h2>
    </div>
    <div class="stack" style="max-width:60ch">
      <p>My background in mathematics taught me to follow an argument until every step holds. That habit now shapes how I write about AI, machine learning, developer tools, and the systems built around them.</p>
      <p>{arrow_link("More about how I work", "/about")}</p>
    </div>
  </div>
</section>
""".strip()


def _insights() -> str:
    cards = "".join(insight_card(i) for i in INSIGHTS[:3])
    return f"""
<section class="section">
  <div class="container">
    <div class="section-head">
      <span class="eyebrow">Insights</span>
      <h2>Notes from the work of writing technical content.</h2>
      <p>Frameworks and editorial lessons from <em>Tech &amp; Storytelling</em>.</p>
    </div>
    <div class="grid grid--3">{cards}</div>
    <p style="margin-top:var(--sp-6)">{arrow_link("Read more insights", "/insights")}</p>
  </div>
</section>
""".strip()


def _newsletter() -> str:
    return f"""
<section class="section section--tight">
  <div class="container">
    <div class="section-head" style="margin-bottom:var(--sp-5)">
      <span class="eyebrow">Newsletter</span>
      <h2>Technical writing lessons from published work.</h2>
      <p>{NEWSLETTER["pitch"]}</p>
    </div>
    <a class="btn btn--ghost" href="{NEWSLETTER['url']}" rel="noopener">Subscribe &rarr;</a>
  </div>
</section>
""".strip()


def render() -> str:
    body = "\n".join([
        _hero(), _proof(), _services(), _selected_work(), _why(), _case_studies(),
        _process(), _about_teaser(), _insights(), _newsletter(),
        cta_band(
            "Need technical content for your product?",
            "Let's work together →", "/contact",
        ),
    ])
    return render_page(META, body, path="/", jsonld_blocks=(person(), website()))
