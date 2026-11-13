"""Focused portfolio homepage."""
from components import arrow_link, cta_band, work_card
from content import CASE_STUDIES, CLIENTS, featured_work
from seo import PageMeta, person, website
from shell import render_page

META = PageMeta(
    title="Praise James | Developer Advocate, Technical Writer and AI Engineer",
    description=(
        "Praise James builds with AI, explains complex technology through clear stories, "
        "and helps developer products reach the people they were made for."
    ),
    path="/",
)


def _hero() -> str:
    return """
<section class="hero">
  <div class="container hero__grid">
    <div>
      <span class="availability">Open to remote and global opportunities</span>
      <h1 class="hero__title">I build, explain, and <span class="accent">advocate</span> for AI products.</h1>
      <p class="hero__sub">I'm a developer advocate, technical writer, and AI engineer. I create technical content, teach AI engineering, speak about storytelling in tech, and help developer products reach the right communities.</p>
      <div class="btn-row">
        <a class="btn btn--accent" href="/work">Explore my work</a>
        <a class="btn btn--ghost" href="/contact">Discuss a project</a>
      </div>
      <p class="location-line">Based in Lagos · Working with global teams</p>
    </div>
    <div class="hero__photo-wrap">
      <img class="hero__photo" src="/media/praise-720.jpg"
           srcset="/media/praise-320.jpg 320w, /media/praise-720.jpg 720w, /media/praise.jpg 1225w"
           sizes="(max-width:820px) 280px, 390px" width="390" height="488" fetchpriority="high"
           alt="Praise James, developer advocate, technical writer and AI engineer">
    </div>
  </div>
</section>
""".strip()


def _proof() -> str:
    return """
<section class="section--tight">
  <div class="container">
    <div class="proof-grid" aria-label="Selected outcomes">
      <div class="proof-item"><strong>125K+</strong><span>organic views across 50+ published technical articles</span></div>
      <div class="proof-item"><strong>300K+</strong><span>impressions across LinkedIn and X in three months</span></div>
      <div class="proof-item"><strong>700+</strong><span>subscribers for Mamba Brief, a developer-focused newsletter I grew in less than six months</span></div>
    </div>
  </div>
</section>
""".strip()


def _capabilities() -> str:
    return """
<section class="section">
  <div class="container">
    <div class="section-head">
      <span class="eyebrow">How I help</span>
      <h2>From technical idea to developer impact.</h2>
      <p>I work across the full content cycle, from understanding the technology to helping the finished work reach its audience.</p>
    </div>
    <div class="capabilities">
      <article class="capability">
        <h3>Build</h3>
        <p>AI engineering projects, working demos, technical experiments, and reproducible benchmarks.</p>
      </article>
      <article class="capability">
        <h3>Explain</h3>
        <p>Developer tutorials, product-led content, technical analysis, videos, and visual AI lessons.</p>
      </article>
      <article class="capability">
        <h3>Advocate</h3>
        <p>Content distribution, developer education, community conversations, and product storytelling.</p>
      </article>
    </div>
    <p style="margin-top:var(--sp-6)">""" + arrow_link("See my services", "/services") + """</p>
  </div>
</section>
""".strip()


def _selected_work() -> str:
    cards = "".join(work_card(w) for w in featured_work(4))
    names = " · ".join(CLIENTS)
    return f"""
<section class="section">
  <div class="container">
    <div class="section-head">
      <span class="eyebrow">Selected work</span>
      <h2>Technical work you can evaluate.</h2>
      <p>Published for <strong class="client-list">{names}.</strong> Read the research, code, explanations, and decisions behind the work.</p>
    </div>
    <div class="grid grid--2">{cards}</div>
    <p style="margin-top:var(--sp-6)">{arrow_link("Browse the full portfolio", "/work")}</p>
  </div>
</section>
""".strip()


def _storytelling() -> str:
    return """
<section class="section">
  <div class="container story-grid">
    <img class="story-photo" src="/media/storytelling-belief.webp" width="1024" height="1536" loading="lazy"
         alt="Praise James speaking at DevFest Lagos beside a slide explaining storytelling">
    <div>
      <span class="eyebrow">My approach</span>
      <h2>Technical content should work with how people think.</h2>
      <p class="lede">I use narrative structure and human psychology to make complex ideas easier to understand, remember, and act on.</p>
      <ul class="story-points">
        <li>Structure information around human cognition</li>
        <li>Validate the reader's problem before offering a solution</li>
        <li>Create context that makes technical ideas memorable</li>
      </ul>
    </div>
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
      <p>{c['summary']}</p>
      <span class="card__foot"><span class="arrow-link">View case study</span></span>
    </a>""" for c in real)
    return f"""
<section class="section">
  <div class="container">
    <div class="section-head">
      <span class="eyebrow">Case studies</span>
      <h2>How the work came together.</h2>
      <p>The research, technical decisions, editorial process, and outcomes behind selected projects.</p>
    </div>
    <div class="grid grid--3">{cards}</div>
    <p style="margin-top:var(--sp-6)">{arrow_link("See all case studies", "/work/case-studies")}</p>
  </div>
</section>
""".strip()


def _speaking() -> str:
    return """
<section class="section">
  <div class="container">
    <div class="section-head">
      <span class="eyebrow">Speaking</span>
      <h2>I speak about storytelling in tech.</h2>
      <p>My talks and conversations explore how narrative structure improves technical education, product communication, and the way people relate to technology.</p>
    </div>
    <div class="speaking-grid">
      <figure>
        <img src="/media/devfest-speaking.jpg" width="800" height="1200" loading="lazy" alt="Praise James speaking at DevFest Lagos 2025">
        <figcaption>Speaker · Technical storytelling at DevFest Lagos 2025</figcaption>
      </figure>
      <figure>
        <img src="/media/workshop-speaking.jpg" width="1200" height="588" loading="lazy" alt="Praise James teaching technical writers">
        <figcaption>Speaker · Teaching writers to ask “so what?” of every fact at TWMP Meetup 1.0</figcaption>
      </figure>
    </div>
    <div class="event-strip" aria-label="Selected hosted and moderated events">
      <figure><img src="/media/event-distribution.webp" width="786" height="968" loading="lazy" alt="You Shipped Something. Now What? event poster"><figcaption>Moderator · Distribution Strategies for Builders</figcaption></figure>
      <figure><img src="/media/event-ai-citations.webp" width="1536" height="1536" loading="lazy" alt="How to Get Your Content Cited by AI event poster"><figcaption>Moderator · Content visibility in AI search</figcaption></figure>
      <figure><img src="/media/event-emotional-storytelling.webp" width="709" height="1536" loading="lazy" alt="Emotional Storytelling in AI event poster"><figcaption>Conversation · Emotional Storytelling in AI</figcaption></figure>
    </div>
  </div>
</section>
""".strip()


def render() -> str:
    body = "\n".join([
        _hero(), _proof(), _capabilities(), _selected_work(), _storytelling(),
        _case_studies(), _speaking(),
        cta_band(
            "Need someone who can understand the technology and make people care?",
            "Discuss a project →", "/contact",
            "Bring me the product, the technical brief, or the idea your audience needs to understand.",
        ),
    ])
    return render_page(META, body, path="/", jsonld_blocks=(person(), website()))
