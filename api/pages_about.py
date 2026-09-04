"""/about page. Human, not a resume."""
from components import breadcrumbs, cta_band, esc
from content import METRICS, SOCIALS, VIDEOS, YOUTUBE_CHANNEL
from seo import PageMeta, breadcrumb_list, person
from shell import render_page

META = PageMeta(
    title="About Praise James | AI technical writer",
    description=(
        "Praise James writes about AI and developer technology for a living, with a background "
        "in mathematics and machine learning and a focus on technical storytelling."
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
    <h1>I'm Praise. I write about technology for a living.</h1>

    <p>I came into technical writing from writing. The move into AI and developer tools came from a
    background in mathematics and hands-on work with machine learning: enough to read a paper,
    run a model, and know when an explanation is hiding something.</p>

    <p>What I learned along the way is that understanding the technology is the easy half. The hard
    half is knowing what your reader actually needs to walk away with, and building the piece so they
    get there without friction.</p>

    <h2>What I work on</h2>
    <p>Technical articles, developer tutorials, product-led content, and technical thought leadership
    for AI and developer-focused companies: explainers, benchmarks, integration guides, and
    founder points of view. Topics range across AI/ML, developer tooling, vector databases, web data,
    and the systems developers build with.</p>

    <h2>How I think about writing</h2>
    <p><strong>Technical depth.</strong> I spend real time with the subject before writing:
    reading the docs, running the thing, talking to the engineers.</p>
    <p><strong>Storytelling.</strong> I structure content so a reader can follow the argument and act
    on it, rather than presenting a wall of correct information.</p>
    <p><strong>Reader-first.</strong> I write for the person who has to use the content, not the
    person who assigned it.</p>

    <h2>Selected proof</h2>
    <dl>{metrics}</dl>

    <h2>Elsewhere</h2>
    <ul class="link-list">{links}</ul>

    <h2>On YouTube</h2>
    <p>I break down AI and ML concepts for developers who want to understand the technology behind
    their tools. <a href="{YOUTUBE_CHANNEL}" rel="noopener">See the channel</a>.</p>
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
{cta_band("Building an AI product that needs explaining?", "Start a project →", "/contact")}
"""
    trail = [("Home", "/"), ("About", "/about")]
    return render_page(META, body, path="/about", breadcrumbs_html=breadcrumbs(trail),
                       jsonld_blocks=[person(), breadcrumb_list(trail)])
