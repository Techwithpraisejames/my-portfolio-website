import base64
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from flask import Flask, Response

import pages_home
from photo_data import HERO_PHOTO_DATA_URI
from seo import SITE_URL

app = Flask(__name__)

# Routes that should appear in sitemap.xml (indexable pages only).
SITEMAP_PATHS = [
    "/", "/work", "/work/case-studies", "/services",
    "/services/technical-articles", "/services/developer-tutorials",
    "/services/product-led-content", "/services/technical-thought-leadership",
    "/about", "/insights", "/contact",
]

_PHOTO_BYTES = base64.b64decode(HERO_PHOTO_DATA_URI.split(",", 1)[1])


def _html(markup: str) -> Response:
    return Response(markup, mimetype="text/html; charset=utf-8")


@app.route("/")
def home():
    return _html(pages_home.render())


# ---------------- media ----------------

@app.route("/media/praise.jpg")
def media_praise():
    return Response(_PHOTO_BYTES, mimetype="image/jpeg",
                    headers={"Cache-Control": "public, max-age=31536000, immutable"})


@app.route("/og.jpg")
def og_image():
    # [ADD DEDICATED 1200x630 OG IMAGE] — reuses the profile photo for now.
    return Response(_PHOTO_BYTES, mimetype="image/jpeg",
                    headers={"Cache-Control": "public, max-age=86400"})


# ---------------- SEO infra ----------------

@app.route("/robots.txt")
def robots():
    body = f"User-agent: *\nAllow: /\n\nSitemap: {SITE_URL}/sitemap.xml\n"
    return Response(body, mimetype="text/plain")


@app.route("/sitemap.xml")
def sitemap():
    urls = "".join(
        f"<url><loc>{SITE_URL}{p}</loc><changefreq>monthly</changefreq></url>"
        for p in SITEMAP_PATHS
    )
    # case study detail pages
    try:
        from content import CASE_STUDIES
        for c in CASE_STUDIES:
            if not c.get("placeholder"):
                urls += f"<url><loc>{SITE_URL}/work/case-studies/{c['slug']}</loc><changefreq>monthly</changefreq></url>"
    except Exception:
        pass
    xml = ('<?xml version="1.0" encoding="UTF-8"?>'
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
           f"{urls}</urlset>")
    return Response(xml, mimetype="application/xml")


@app.errorhandler(404)
def not_found(_e):
    from shell import render_page
    from seo import PageMeta
    body = """
<section class="section"><div class="container stack">
  <span class="eyebrow">404</span>
  <h1>This page moved or never existed.</h1>
  <p class="lede">Try the <a href="/work">work</a>, the <a href="/services">services</a>, or
  <a href="/contact">get in touch</a>.</p>
</div></section>
"""
    page = render_page(
        PageMeta(title="Page not found | Praise James",
                 description="This page could not be found.", path="/404"),
        body, path="/404",
    )
    return Response(page, status=404, mimetype="text/html; charset=utf-8")


# Vercel expects the module-level `app`.
if __name__ == "__main__":
    app.run(port=5000, debug=True)
