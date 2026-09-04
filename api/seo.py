"""SEO helpers: per-page metadata, head tags, and JSON-LD builders.

Change SITE_URL in one place when a custom domain is added.
"""
import html
import json
from dataclasses import dataclass, field

SITE_URL = "https://techwithpraisejames.vercel.app"
SITE_NAME = "Praise James"
# [ADD DEDICATED 1200x630 OG IMAGE] — currently reuses the profile photo, served by /og.jpg
OG_IMAGE = SITE_URL + "/og.jpg"

# Verified profiles only (carried from the previous site).
SAME_AS = [
    "https://www.linkedin.com/in/praise-james-608b91284",
    "https://www.youtube.com/channel/UCwVDq2mG2FuNCRzAf-ypLvg",
    "https://medium.com/@techwithpraisejames",
    "https://github.com/Techwithpraisejames",
    "https://x.com/causingheadache",
    "https://techwithpraisejames.substack.com/",
]


@dataclass
class PageMeta:
    title: str
    description: str
    path: str = "/"
    og_type: str = "website"
    image: str = OG_IMAGE

    @property
    def canonical(self) -> str:
        return SITE_URL + self.path


def _esc(s: str) -> str:
    return html.escape(str(s), quote=True)


def head_tags(meta: PageMeta) -> str:
    t, d, url, img = _esc(meta.title), _esc(meta.description), _esc(meta.canonical), _esc(meta.image)
    return f"""
  <title>{t}</title>
  <meta name="description" content="{d}">
  <link rel="canonical" href="{url}">
  <meta property="og:site_name" content="{_esc(SITE_NAME)}">
  <meta property="og:title" content="{t}">
  <meta property="og:description" content="{d}">
  <meta property="og:type" content="{_esc(meta.og_type)}">
  <meta property="og:url" content="{url}">
  <meta property="og:image" content="{img}">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{t}">
  <meta name="twitter:description" content="{d}">
  <meta name="twitter:image" content="{img}">
""".strip("\n")


def json_ld(*blocks: dict) -> str:
    out = []
    for b in blocks:
        if not b:
            continue
        out.append(
            '<script type="application/ld+json">'
            + json.dumps(b, ensure_ascii=False, separators=(",", ":"))
            + "</script>"
        )
    return "\n".join(out)


# ---------- JSON-LD builders ----------

def person() -> dict:
    return {
        "@context": "https://schema.org",
        "@type": "Person",
        "name": "Praise James",
        "url": SITE_URL + "/about",
        "image": OG_IMAGE,
        "jobTitle": "Technical Writer & Content Strategist",
        "description": (
            "Technical writer for AI and developer-focused companies. Turns complex "
            "technologies into clear, technically grounded content."
        ),
        "knowsAbout": [
            "Technical writing", "Artificial intelligence", "Machine learning",
            "Developer tools", "Developer education", "Content strategy", "Vector databases",
        ],
        "sameAs": SAME_AS,
    }


def website() -> dict:
    return {
        "@context": "https://schema.org",
        "@type": "WebSite",
        "name": SITE_NAME,
        "url": SITE_URL,
    }


def breadcrumb_list(trail: list[tuple[str, str]]) -> dict:
    """trail: [(name, path), ...] — last item is the current page."""
    return {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {
                "@type": "ListItem",
                "position": i + 1,
                "name": name,
                "item": SITE_URL + path,
            }
            for i, (name, path) in enumerate(trail)
        ],
    }


def service(name: str, description: str, path: str) -> dict:
    return {
        "@context": "https://schema.org",
        "@type": "Service",
        "serviceType": name,
        "name": name,
        "description": description,
        "url": SITE_URL + path,
        "provider": {"@type": "Person", "name": "Praise James", "url": SITE_URL},
        "areaServed": "Worldwide",
    }


def article(headline: str, description: str, path: str) -> dict:
    return {
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": headline,
        "description": description,
        "url": SITE_URL + path,
        "author": {"@type": "Person", "name": "Praise James", "url": SITE_URL},
        "publisher": {"@type": "Person", "name": "Praise James"},
        "image": OG_IMAGE,
    }


def item_list(items: list[tuple[str, str]]) -> dict:
    """items: [(name, url), ...] — url may be external."""
    return {
        "@context": "https://schema.org",
        "@type": "ItemList",
        "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "name": name, "url": url}
            for i, (name, url) in enumerate(items)
        ],
    }
