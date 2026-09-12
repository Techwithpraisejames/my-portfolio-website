"""/insights page. Articles and newsletter hub."""
from components import breadcrumbs, cta_band, esc, insight_card
from content import INSIGHTS, NEWSLETTER
from seo import PageMeta, breadcrumb_list, item_list
from shell import render_page

META = PageMeta(
    title="Insights | Writing about technical content | Praise James",
    description=(
        "Frameworks, lessons, and notes on the craft of technical writing from Tech & Storytelling, "
        "Praise James's newsletter for technical writers."
    ),
    path="/insights",
)


def render() -> str:
    cards = "".join(insight_card(i) for i in INSIGHTS)
    body = f"""
<section class="section">
  <div class="container">
    <span class="eyebrow">Insights</span>
    <h1>Notes from the work of writing technical content.</h1>
    <p class="lede" style="margin-top:var(--sp-5)"><em>{esc(NEWSLETTER['name'])}</em> is where I share
    the frameworks, editorial decisions, and lessons shaping my work as a technical writer.</p>
    <div class="grid grid--3" style="margin-top:var(--sp-7)">{cards}
      <div class="card placeholder">[ADD ARTICLE]</div>
    </div>
  </div>
</section>
<section class="section">
  <div class="container">
    <span class="eyebrow">Newsletter</span>
    <h2>Technical writing lessons from published work.</h2>
    <p class="lede" style="margin-top:var(--sp-4)">A newsletter for technical writers who want to
    become better storytellers.</p>
    <p style="margin-top:var(--sp-5)">
      <a class="btn btn--accent" href="{NEWSLETTER['url']}" rel="noopener">Subscribe &rarr;</a>
    </p>
  </div>
</section>
{cta_band("Need a technical writer?", "Discuss your project →", "/contact")}
"""
    trail = [("Home", "/"), ("Insights", "/insights")]
    ld = [
        breadcrumb_list(trail),
        item_list([(i["title"], i["url"]) for i in INSIGHTS]),
    ]
    return render_page(META, body, path="/insights", breadcrumbs_html=breadcrumbs(trail),
                       jsonld_blocks=ld)
