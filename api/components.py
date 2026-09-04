"""Shared HTML render helpers. Trusted content only (from content.py); esc() is
applied to text fields as good practice, not as a security boundary."""
import html

NAV_LINKS = [
    ("Work", "/work"),
    ("Services", "/services"),
    ("About", "/about"),
    ("Insights", "/insights"),
]


def esc(s) -> str:
    return html.escape("" if s is None else str(s))


def _current(path: str, href: str) -> bool:
    if href == "/":
        return path == "/"
    return path == href or path.startswith(href + "/")


def nav(path: str) -> str:
    links = "".join(
        f'<li><a href="{href}"{" aria-current=\"page\"" if _current(path, href) else ""}>{esc(label)}</a></li>'
        for label, href in NAV_LINKS
    )
    return f"""
<a class="skip" href="#main">Skip to content</a>
<header class="site-header">
  <nav class="nav" aria-label="Primary">
    <a class="nav__brand" href="/">Praise James</a>
    <button class="nav__toggle" aria-expanded="false" aria-controls="nav-menu" aria-label="Open menu" data-nav-toggle>
      <svg width="20" height="20" viewBox="0 0 20 20" aria-hidden="true"><path d="M2 5h16M2 10h16M2 15h16" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg>
    </button>
    <ul class="nav__links" id="nav-menu">
      {links}
      <li><a class="nav__menu-cta" href="/contact"{" aria-current=\"page\"" if _current(path, "/contact") else ""}>Hire me</a></li>
    </ul>
    <a class="btn btn--accent nav__cta" href="/contact">Hire me &rarr;</a>
  </nav>
</header>
""".strip()


def footer() -> str:
    from content import SOCIALS
    social = "".join(
        f'<a href="{s["url"]}" rel="noopener">{esc(s["name"])}</a>' for s in SOCIALS
    )
    pages = "".join(
        f'<a href="{href}">{esc(label)}</a>'
        for label, href in NAV_LINKS + [("Contact", "/contact")]
    )
    return f"""
<footer class="site-footer">
  <div class="container">
    <div class="site-footer__grid">
      <div>
        <div class="site-footer__brand">Praise James</div>
        <p class="site-footer__tag">Technical content for AI and developer-focused companies.</p>
      </div>
      <nav aria-label="Footer">{pages}</nav>
      <nav aria-label="Elsewhere">{social}</nav>
    </div>
    <p class="site-footer__legal">&copy; 2026 Praise James. Technical writer &middot; AI/ML &middot; Developer tools.</p>
  </div>
</footer>
""".strip()


def breadcrumbs(trail: list[tuple[str, str]]) -> str:
    """trail: [(name, path), ...] including the current page last."""
    items = []
    for i, (name, path) in enumerate(trail):
        last = i == len(trail) - 1
        if last:
            items.append(f'<li aria-current="page">{esc(name)}</li>')
        else:
            items.append(f'<li><a href="{path}">{esc(name)}</a></li>')
    return f'<nav class="breadcrumbs container" aria-label="Breadcrumb"><ol>{"".join(items)}</ol></nav>'


def arrow_link(label: str, href: str, external: bool = False) -> str:
    rel = ' rel="noopener"' if external else ""
    return f'<a class="arrow-link" href="{href}"{rel}>{esc(label)}</a>'


def work_card(item: dict) -> str:
    if item.get("placeholder"):
        return f'<div class="card placeholder">{esc(item["title"])} &mdash; {esc(item["summary"])}</div>'
    meta = esc(item["publication"])
    return f"""
<a class="card" href="{item['url']}" rel="noopener" data-category="{esc(item['category'])}">
  <span class="card__kicker">{esc(item['category'])}</span>
  <span class="card__title">{esc(item['title'])}</span>
  <span class="card__meta">{meta}</span>
  <p>{esc(item['summary'])}</p>
  <span class="card__foot"><span class="arrow-link">Read</span></span>
</a>
""".strip()


def service_card(item: dict) -> str:
    return f"""
<a class="card" href="/services/{item['slug']}">
  <span class="card__title">{esc(item['title'])}</span>
  <p>{esc(item['card'])}</p>
  <span class="card__foot"><span class="arrow-link">Learn more</span></span>
</a>
""".strip()


def insight_card(item: dict) -> str:
    if item.get("placeholder"):
        return f'<div class="card placeholder">[ADD ARTICLE]</div>'
    date = "" if item["date"].startswith("[ADD") else f' &middot; {esc(item["date"])}'
    return f"""
<a class="card" href="{item['url']}" rel="noopener">
  <span class="card__kicker">{esc(item['category'])}</span>
  <span class="card__title">{esc(item['title'])}</span>
  <span class="card__meta">Tech &amp; Storytelling{date}</span>
  <p>{esc(item['summary'])}</p>
  <span class="card__foot"><span class="arrow-link">Read</span></span>
</a>
""".strip()


def case_study_card(item: dict) -> str:
    if item.get("placeholder"):
        return f'<div class="card placeholder">[ADD CASE STUDY]</div>'
    return f"""
<a class="card" href="/work/case-studies/{item['slug']}">
  <span class="card__kicker">Case study</span>
  <span class="card__title">{esc(item['title'])}</span>
  <span class="card__meta">{esc(item['client'])}</span>
  <p>{esc(item['summary'])}</p>
  <span class="card__foot"><span class="arrow-link">View case study</span></span>
</a>
""".strip()


def cta_band(heading: str, button_label: str, button_href: str, sub: str = "") -> str:
    sub_html = f"<p>{esc(sub)}</p>" if sub else ""
    return f"""
<section class="section cta-band">
  <div class="container">
    <h2>{esc(heading)}</h2>
    {sub_html}
    <a class="btn btn--on-accent" href="{button_href}">{esc(button_label)}</a>
  </div>
</section>
""".strip()


NAV_SCRIPT = """
<script>
(function(){
  var t=document.querySelector('[data-nav-toggle]'),m=document.getElementById('nav-menu');
  if(!t||!m)return;
  t.addEventListener('click',function(){
    var open=m.classList.toggle('is-open');
    t.setAttribute('aria-expanded',open);
    t.setAttribute('aria-label',open?'Close menu':'Open menu');
    document.body.style.overflow=open?'hidden':'';
  });
  m.addEventListener('click',function(e){if(e.target.tagName==='A'){m.classList.remove('is-open');t.setAttribute('aria-expanded','false');document.body.style.overflow='';}});
})();
</script>
""".strip()
