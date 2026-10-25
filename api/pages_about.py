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
        f'<iframe src="https://www.youtube.com/embed/{v["id"]}" title="{esc(v["title"])}" '
        f'loading="lazy" allow="encrypted-media; picture-in-picture" allowfullscreen></iframe>'
        for v in VIDEOS[:4]
    )
    body = f"""
<section class="section">
  <div class="container about-intro">
    <div class="prose">
      <span class="eyebrow">About</span>
      <h1>I'm Praise James, a technical writer covering AI, machine learning, developer tools, and software infrastructure.</h1>

      <p>I started in travel writing, then learned Python for data science and found my way into AI and machine learning.</p>

      <p>Mathematics trained me to follow an argument until every step holds. That habit now shapes how I research, test, and explain technical subjects.</p>
    </div>
    <img class="about-intro__photo" src="/media/about-portrait.jpg" width="720" height="1280"
         alt="Praise James smiling at her desk">
  </div>

  <div class="container prose" style="max-width:720px;margin-top:var(--sp-8)">
    <h2>How I work</h2>
    <p>I read the source material, test the product, and check each claim before I write. The method changes with the assignment, but the standard stays the same.</p>

    <h2>What I write</h2>
    <p>My work includes developer tutorials, architecture guides, technical comparisons, industry analysis, and thought leadership. I have written for companies including Actian, Bright Data, Zenrows, and ToolJet.</p>

    <h2>Beyond client work</h2>
    <p>I publish Tech &amp; Storytelling for technical writers, make AI videos for beginners, and speak about research, editing, and technical storytelling.</p>
  </div>

  <div class="container" style="margin-top:var(--sp-7)">
    <div class="speaking-grid">
      <figure>
        <img src="/media/devfest-speaking.jpg" width="800" height="1200" loading="lazy"
             alt="Praise James speaking on stage at DevFest Lagos 2025">
        <figcaption>Speaking about technical storytelling at DevFest Lagos 2025.</figcaption>
      </figure>
      <figure>
        <img src="/media/workshop-speaking.jpg" width="1200" height="588" loading="lazy"
             alt="Praise James teaching an editing session with a microphone">
        <figcaption>Teaching writers to ask “so what?” of every fact.</figcaption>
      </figure>
    </div>
  </div>

  <div class="container prose" style="max-width:720px;margin-top:var(--sp-8)">
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
