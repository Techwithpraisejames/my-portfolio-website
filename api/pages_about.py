"""About Praise: technical depth, communication and community."""
from components import breadcrumbs, cta_band, esc
from content import METRICS, SOCIALS, VIDEOS, YOUTUBE_CHANNEL
from seo import PageMeta, breadcrumb_list, person
from shell import render_page

META = PageMeta(
    title="About Praise James | Developer Advocate and AI Engineer",
    description=(
        "Praise James is a developer advocate, technical writer and AI engineer who builds, "
        "explains and speaks about AI and developer technology."
    ),
    path="/about",
)


def render() -> str:
    metrics = "".join(
        f'<div class="cs-row"><dt>{esc(m["value"])}</dt><dd>{esc(m["label"])}</dd></div>'
        for m in METRICS
    )
    links = "".join(
        f'<li><a href="{s["url"]}" rel="noopener">{esc(s["name"])}</a></li>' for s in SOCIALS
    )
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
      <h1>I work where AI engineering, technical storytelling, and developer advocacy meet.</h1>
      <p class="lede">I build with AI, write about the systems behind it, teach what I learn, and help technical work reach the people it was made for.</p>
      <p>I started in travel writing, learned Python for data science, and moved into AI and machine learning. My mathematics background taught me to follow an argument until every step holds. That same habit now shapes how I test products, explain technical ideas, and lead developer conversations.</p>
    </div>
    <img class="about-intro__photo" src="/media/about-portrait.jpg" width="720" height="1280" alt="Praise James smiling at her desk">
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head">
      <span class="eyebrow">Across the work</span>
      <h2>Technical enough to build it. Clear enough to explain it.</h2>
    </div>
    <div class="capabilities">
      <article class="capability"><h3>Build</h3><p>I create AI projects, test developer tools, run benchmarks, and learn through working systems.</p></article>
      <article class="capability"><h3>Explain</h3><p>I turn that technical understanding into tutorials, analysis, videos, and product stories.</p></article>
      <article class="capability"><h3>Advocate</h3><p>I distribute content, teach developers, host conversations, and speak about storytelling in tech.</p></article>
    </div>
  </div>
</section>

<section class="section">
  <div class="container story-grid">
    <img class="story-photo" src="/media/storytelling-belief.webp" width="1024" height="1536" loading="lazy" alt="Praise James speaking about storytelling at DevFest Lagos">
    <div>
      <span class="eyebrow">My belief</span>
      <h2>Good technical storytelling respects how people think.</h2>
      <p class="lede">Clear content gives people context, follows a logical path, and makes the important idea easier to remember.</p>
      <p style="margin-top:var(--sp-5)">That principle runs through my writing, talks, workshops, videos, and developer education.</p>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head"><span class="eyebrow">Selected proof</span><h2>Results from the work.</h2></div>
    <dl>{metrics}</dl>
    <div class="prose" style="margin-top:var(--sp-8)">
      <h2>AI From Scratch</h2>
      <p>I teach AI engineering through practical explanations and visual breakdowns on YouTube and Instagram. <a href="{YOUTUBE_CHANNEL}" rel="noopener">See the YouTube channel</a>.</p>
    </div>
    <div class="video-grid" style="margin-top:var(--sp-6)">{videos}</div>
    <div class="prose" style="margin-top:var(--sp-8)"><h2>Elsewhere</h2><ul class="link-list">{links}</ul></div>
  </div>
</section>

{cta_band("Need someone who can build, explain, and advocate?", "Start a conversation →", "/contact")}
"""
    trail = [("Home", "/"), ("About", "/about")]
    return render_page(
        META, body, path="/about", breadcrumbs_html=breadcrumbs(trail),
        jsonld_blocks=[person(), breadcrumb_list(trail)],
    )
