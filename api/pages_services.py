"""/services overview + /services/<slug> detail pages."""
from components import breadcrumbs, cta_band, service_card, work_card
from content import SERVICES, find_service, real_work
from seo import PageMeta, breadcrumb_list
from seo import service as service_ld
from shell import render_page

OVERVIEW_META = PageMeta(
    title="Services | Technical content for AI and developer companies | Praise James",
    description=(
        "Technical articles, developer tutorials, product-led content, and technical thought "
        "leadership for AI and developer-focused companies."
    ),
    path="/services",
)


def overview() -> str:
    body = f"""
<section class="section">
  <div class="container">
    <span class="eyebrow">Services</span>
    <h1>Technical content built for complex products.</h1>
    <p class="lede" style="margin-top:var(--sp-5)">I help AI and developer-focused companies explain
    what they are building, educate their audience, and build technical authority. Every engagement
    runs on the same principles: technical depth, a structure the reader can follow, and content
    written for the person who has to use it.</p>
    <div class="grid grid--4" style="margin-top:var(--sp-8)">{"".join(service_card(s) for s in SERVICES)}</div>
    <p style="margin-top:var(--sp-7)" class="muted">Not sure which fits? <a href="/contact">Describe the
    project</a> and I'll tell you.</p>
  </div>
</section>
{cta_band("Have a project in mind?", "Start a project →", "/contact")}
"""
    crumbs = breadcrumbs([("Home", "/"), ("Services", "/services")])
    ld = [breadcrumb_list([("Home", "/"), ("Services", "/services")])]
    return render_page(OVERVIEW_META, body, path="/services", breadcrumbs_html=crumbs, jsonld_blocks=ld)


def detail(slug: str):
    s = find_service(slug)
    if not s:
        return None
    meta = PageMeta(
        title=f"{s['title']} | Services | Praise James",
        description=f"{s['tagline']} {s['card']}",
        path=f"/services/{slug}",
        og_type="article",
    )
    deliverables = "".join(f"<li>{d}</li>" for d in s["deliverables"])
    examples = [w for w in real_work() if w["category"] in s["related_categories"]][:3]
    examples_html = ""
    if examples:
        examples_html = f"""
    <h2>Relevant work</h2>
    <div class="grid grid--3">{"".join(work_card(w) for w in examples)}</div>"""
    body = f"""
<section class="section">
  <div class="container prose" style="max-width:760px">
    <span class="eyebrow">{s['title']}</span>
    <h1>{s['tagline']}</h1>

    <h2>What it is</h2>
    <p>{s['what_it_is']}</p>

    <h2>Who it's for</h2>
    <p>{s['who_for']}</p>

    <h2>What gets delivered</h2>
    <ul>{deliverables}</ul>

    <h2>How I approach it</h2>
    <p>{s['approach']}</p>
    {examples_html}

    <p style="margin-top:var(--sp-8)">
      <a class="btn btn--accent" href="/contact">Start a project &rarr;</a>
    </p>
  </div>
</section>
{cta_band("Ready to brief a project?", "Start a project →", "/contact")}
"""
    trail = [("Home", "/"), ("Services", "/services"), (s["title"], f"/services/{slug}")]
    ld = [
        service_ld(s["title"], s["card"], f"/services/{slug}"),
        breadcrumb_list(trail),
    ]
    return render_page(meta, body, path=f"/services/{slug}",
                       breadcrumbs_html=breadcrumbs(trail), jsonld_blocks=ld)
