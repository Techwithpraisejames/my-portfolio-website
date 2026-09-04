"""/insights — articles + newsletter hub."""
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
    <h1>Writing about how technical content gets made.</h1>
    <p class="lede" style="margin-top:var(--sp-5)">I publish <em>{esc(NEWSLETTER['name'])}</em>, a
    newsletter on the craft of technical writing &mdash; frameworks, structure, and the decisions that
    make a piece land. {esc(NEWSLETTER['pitch'])}</p>
    <div class="grid grid--3" style="margin-top:var(--sp-7)">{cards}
      <div class="card placeholder">[ADD ARTICLE]</div>
    </div>
  </div>
</section>
<section class="section">
  <div class="container">
    <span class="eyebrow">Newsletter</span>
    <h2>I write about making technical content easier to understand.</h2>
    <p class="lede" style="margin-top:var(--sp-4)">A newsletter for technical writers who want to
    become better storytellers.</p>
    <p style="margin-top:var(--sp-5)">
      <a class="btn btn--accent" href="{NEWSLETTER['url']}" rel="noopener">Subscribe &rarr;</a>
    </p>
  </div>
</section>
{cta_band("Need a writer who thinks about this?", "Discuss your project →", "/contact")}
"""
    trail = [("Home", "/"), ("Insights", "/insights")]
    ld = [
        breadcrumb_list(trail),
        item_list([(i["title"], i["url"]) for i in INSIGHTS]),
    ]
    return render_page(META, body, path="/insights", breadcrumbs_html=breadcrumbs(trail),
                       jsonld_blocks=ld)
