"""/work portfolio index, /work/case-studies index, and case study detail."""
from components import breadcrumbs, case_study_card, cta_band, esc, work_card
from content import CASE_STUDIES, CATEGORIES, WORK, find_case_study, find_service, real_work
from seo import PageMeta, article, breadcrumb_list, item_list
from shell import render_page

WORK_META = PageMeta(
    title="Work | Technical writing portfolio | Praise James",
    description=(
        "Selected technical articles, developer tutorials, benchmarks, and analysis published "
        "for AI and developer-focused companies and publications."
    ),
    path="/work",
)

CS_META = PageMeta(
    title="Case studies | Praise James",
    description=(
        "How specific technical content projects were briefed, researched, structured, and "
        "delivered, and what happened next."
    ),
    path="/work/case-studies",
)

FILTER_SCRIPT = """
<script>
(function(){
  var bar=document.querySelector('[data-filter]');
  if(!bar)return;
  var cards=[].slice.call(document.querySelectorAll('[data-category]'));
  bar.addEventListener('click',function(e){
    var b=e.target.closest('button');if(!b)return;
    var cat=b.getAttribute('data-cat');
    bar.querySelectorAll('button').forEach(function(x){x.setAttribute('aria-pressed',x===b);});
    cards.forEach(function(c){
      c.classList.toggle('is-hidden', cat!=='all' && c.getAttribute('data-category')!==cat);
    });
  });
})();
</script>
"""


def index() -> str:
    buttons = '<button data-cat="all" aria-pressed="true">All</button>' + "".join(
        f'<button data-cat="{esc(c)}" aria-pressed="false">{esc(c)}</button>' for c in CATEGORIES
    )
    cards = "".join(work_card(w) for w in real_work())
    ph = "".join(work_card(w) for w in WORK if w.get("placeholder"))
    body = f"""
<section class="section">
  <div class="container">
    <span class="eyebrow">Work</span>
    <h1>Published work, selected for what it shows.</h1>
    <p class="lede" style="margin-top:var(--sp-5)">Benchmarks, tutorials, explainers, and analysis for
    AI and developer audiences. Filter by focus area.</p>
    <div class="filter-bar" data-filter role="group" aria-label="Filter work by category"
         style="margin-top:var(--sp-7)">{buttons}</div>
    <div class="grid grid--3">{cards}{ph}</div>
  </div>
</section>
{cta_band("Want work like this for your product?", "Discuss your project →", "/contact")}
{FILTER_SCRIPT}
"""
    trail = [("Home", "/"), ("Work", "/work")]
    ld = [
        breadcrumb_list(trail),
        item_list([(w["title"], w["url"]) for w in real_work() if w.get("url")]),
    ]
    return render_page(WORK_META, body, path="/work",
                       breadcrumbs_html=breadcrumbs(trail), jsonld_blocks=ld)


def case_studies_index() -> str:
    real = [c for c in CASE_STUDIES if not c.get("placeholder")]
    ph = [c for c in CASE_STUDIES if c.get("placeholder")]
    cards = "".join(case_study_card(c) for c in real + ph)
    body = f"""
<section class="section">
  <div class="container">
    <span class="eyebrow">Case studies</span>
    <h1>The work behind the work.</h1>
    <p class="lede" style="margin-top:var(--sp-5)">Each case study covers the brief, the technical
    challenge, the approach, what was produced, and the outcome.</p>
    <div class="grid grid--3" style="margin-top:var(--sp-7)">{cards}</div>
  </div>
</section>
{cta_band("Need this kind of content?", "Hire me →", "/contact")}
"""
    trail = [("Home", "/"), ("Work", "/work"), ("Case studies", "/work/case-studies")]
    return render_page(CS_META, body, path="/work/case-studies",
                       breadcrumbs_html=breadcrumbs(trail),
                       jsonld_blocks=[breadcrumb_list(trail)])


_SECTIONS = [
    ("The brief", "brief"),
    ("The challenge", "challenge"),
    ("The approach", "approach"),
    ("The work", "work"),
    ("The outcome", "outcome"),
    ("What this demonstrates", "demonstrates"),
]


def case_study(slug: str):
    c = find_case_study(slug)
    if not c or c.get("placeholder"):
        return None
    rows = "".join(
        f'<div class="cs-row"><dt>{label}</dt><dd>{esc(c[key])}</dd></div>' for label, key in _SECTIONS
    )
    quotes = ""
    if c.get("quotes"):
        quotes = "".join(
            f'<figure class="card" style="margin-top:var(--sp-4)"><blockquote>{esc(q["quote"])}</blockquote>'
            f'<figcaption class="card__meta">{esc(q["name"])}, {esc(q["role"])}</figcaption></figure>'
            for q in c["quotes"]
        )
        quotes = f'<div style="margin-top:var(--sp-7)">{quotes}</div>'
    resource = ""
    if c.get("resource_url"):
        label = esc(c.get("resource_label", "Read the resource"))
        resource = (f'<p style="margin-top:var(--sp-7)">'
                    f'<a class="btn btn--ghost" href="{esc(c["resource_url"])}" rel="noopener">'
                    f'{label} &rarr;</a></p>')
    service_link = ""
    if c.get("service"):
        s = find_service(c["service"])
        if s:
            service_link = (f'<p style="margin-top:var(--sp-7)">Related service: '
                            f'<a href="/services/{s["slug"]}">{esc(s["title"])}</a></p>')
    meta = PageMeta(
        title=f"{c['title']} | Case study | Praise James",
        description=c["summary"],
        path=f"/work/case-studies/{slug}",
        og_type="article",
    )
    body = f"""
<section class="section">
  <div class="container" style="max-width:820px">
    <span class="eyebrow">Case study</span>
    <h1>{esc(c['title'])}</h1>
    <p class="lede" style="margin-top:var(--sp-5)">{esc(c['summary'])}</p>
    <p class="card__meta" style="margin-top:var(--sp-4)">Client: {esc(c['client'])}</p>
    <dl style="margin-top:var(--sp-7)">{rows}</dl>
    {resource}
    {quotes}
    {service_link}
    <p style="margin-top:var(--sp-8)">Need this kind of content?
      <a class="btn btn--accent" href="/contact" style="margin-left:var(--sp-3)">Hire me &rarr;</a>
    </p>
  </div>
</section>
"""
    trail = [("Home", "/"), ("Work", "/work"), ("Case studies", "/work/case-studies"),
             (c["title"], f"/work/case-studies/{slug}")]
    ld = [article(c["title"], c["summary"], f"/work/case-studies/{slug}"), breadcrumb_list(trail)]
    return render_page(meta, body, path=f"/work/case-studies/{slug}",
                       breadcrumbs_html=breadcrumbs(trail), jsonld_blocks=ld)
