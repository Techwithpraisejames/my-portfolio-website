"""/about page. Human, not a resume."""
from components import breadcrumbs, cta_band, esc
from content import METRICS, SOCIALS, VIDEOS, YOUTUBE_CHANNEL
from seo import PageMeta, breadcrumb_list, person
from shell import render_page

META = PageMeta(
    title="About Praise James | AI and developer tools writer",
    description=(
        "Praise James is a technical writer covering AI, machine learning, developer tools, and "
        "software infrastructure, with a background in mathematics."
    ),
    path="/about",
)


def render() -> str:
    metrics = "".join(
        f'<div class="cs-row"><dt>{esc(m["value"])}</dt><dd>{esc(m["label"])}</dd></div>' for m in METRICS
    )
    links = "".join(f'<li><a href="{s["url"]}" rel="noopener">{esc(s["name"])}</a></li>' for s in SOCIALS)
    videos = "".join(
        f'<iframe src="https://www.youtube.com/embed/{v}" title="Praise James on YouTube" '
        f'loading="lazy" allow="encrypted-media; picture-in-picture" allowfullscreen></iframe>'
        for v in VIDEOS[:4]
    )
    body = f"""
<section class="section">
  <div class="container prose" style="max-width:720px">
    <span class="eyebrow">About</span>
    <h1>I'm Praise James, a technical writer covering AI, machine learning, developer tools, and software infrastructure.</h1>

    <p>My background in mathematics shaped how I approach technical subjects. I trace ideas back to the source, follow the reasoning, and check each claim before deciding how to explain it.</p>

    <p>That process may involve reading a research paper, testing an API, running a benchmark, reviewing documentation, or speaking with an engineer. The method changes with the assignment, but the standard stays the same. I need to understand the subject before I can write about it.</p>

    <h2>What I write</h2>
    <p>My work includes developer tutorials, architecture guides, technical comparisons, industry analysis, and thought leadership. I have written for companies including Actian, Bright Data, Zenrows, and ToolJet.</p>

    <h2>What the reader leaves with</h2>
    <p>The strongest technical content gives the reader something useful to carry away. Sometimes that is working code. Sometimes it is a framework, a technical decision, or a clearer view of the market. I decide what that outcome should be before I begin the draft.</p>

    <h2>Selected proof</h2>
    <dl>{metrics}</dl>

    <h2>Elsewhere</h2>
    <ul class="link-list">{links}</ul>

    <h2>On YouTube</h2>
    <p>I explain AI and machine learning concepts for people building their understanding of the field.
    <a href="{YOUTUBE_CHANNEL}" rel="noopener">See the channel</a>.</p>
  </div>
  <div class="container" style="margin-top:var(--sp-6)">
    <div class="video-grid">{videos}</div>
  </div>
  <div class="container" style="margin-top:var(--sp-8)">
    <div class="btn-row">
      <a class="btn btn--accent" href="/contact">Start a project &rarr;</a>
      <a class="btn btn--ghost" href="/work">Read my work &rarr;</a>
    </div>
  </div>
</section>
{cta_band("Need a technical writer for your product?", "Start a project →", "/contact")}
"""
    trail = [("Home", "/"), ("About", "/about")]
    return render_page(META, body, path="/about", breadcrumbs_html=breadcrumbs(trail),
                       jsonld_blocks=[person(), breadcrumb_list(trail)])
