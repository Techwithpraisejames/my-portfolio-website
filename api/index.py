import base64
import html
import json
import os
import sys
import urllib.error
import urllib.request

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from flask import Flask, Response, abort, jsonify, request, send_from_directory

import pages_about
import pages_contact
import pages_home
import pages_insights
import pages_services
import pages_work
from photo_data import HERO_PHOTO_DATA_URI
from seo import SITE_URL

app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = 20 * 1024

# Routes that should appear in sitemap.xml (indexable pages only).
SITEMAP_PATHS = [
    "/", "/work", "/work/case-studies", "/services",
    "/services/technical-articles", "/services/developer-tutorials",
    "/services/product-led-content", "/services/technical-thought-leadership",
    "/about", "/insights", "/contact",
]

_PHOTO_BYTES = base64.b64decode(HERO_PHOTO_DATA_URI.split(",", 1)[1])


def _html(markup: str) -> Response:
    return Response(markup, mimetype="text/html")


@app.route("/")
def home():
    return _html(pages_home.render())


@app.route("/work")
def work():
    return _html(pages_work.index())


@app.route("/work/case-studies")
def case_studies():
    return _html(pages_work.case_studies_index())


@app.route("/work/case-studies/<slug>")
def case_study(slug):
    page = pages_work.case_study(slug)
    if page is None:
        abort(404)
    return _html(page)


@app.route("/services")
def services():
    return _html(pages_services.overview())


@app.route("/services/<slug>")
def service_detail(slug):
    page = pages_services.detail(slug)
    if page is None:
        abort(404)
    return _html(page)


@app.route("/about")
def about():
    return _html(pages_about.render())


@app.route("/insights")
def insights():
    return _html(pages_insights.render())


@app.route("/contact")
def contact():
    return _html(pages_contact.render())


@app.post("/api/contact")
def submit_contact():
    from content import CONTACT_EMAIL

    api_key = os.environ.get("RESEND_API_KEY", "").strip()
    from_email = os.environ.get("RESEND_FROM_EMAIL", "").strip()
    if not api_key or not from_email:
        return jsonify({"error": "Direct submission is temporarily unavailable."}), 503

    data = request.get_json(silent=True) or {}
    if data.get("website_check"):
        return jsonify({"ok": True})

    fields = {
        key: str(data.get(key, "")).strip()[:limit]
        for key, limit in {
            "name": 120, "email": 254, "company": 160, "website": 500,
            "need": 160, "timeline": 160, "budget": 160, "details": 5000,
        }.items()
    }
    if not fields["name"] or "@" not in fields["email"]:
        return jsonify({"error": "Please add a valid name and email."}), 400

    subject = f"Portfolio inquiry from {fields['name']}"
    body = "\n".join([
        f"Name: {fields['name']}", f"Email: {fields['email']}",
        f"Company: {fields['company']}", f"Website: {fields['website']}",
        f"What they need: {fields['need']}", f"Timeline: {fields['timeline']}",
        f"Budget range: {fields['budget']}", "", "Project:", fields["details"],
    ])
    payload = json.dumps({
        "from": from_email,
        "to": [CONTACT_EMAIL],
        "reply_to": fields["email"],
        "subject": subject,
        "text": body,
        "html": f"<pre style=\"font:16px/1.5 system-ui;white-space:pre-wrap\">{html.escape(body)}</pre>",
    }).encode("utf-8")
    resend_request = urllib.request.Request(
        "https://api.resend.com/emails",
        data=payload,
        headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(resend_request, timeout=10) as response:
            if response.status >= 300:
                raise urllib.error.HTTPError(response.url, response.status, "Send failed", response.headers, None)
    except (urllib.error.URLError, TimeoutError):
        return jsonify({"error": "Your message could not be sent. Please use Email directly."}), 502
    return jsonify({"ok": True})


# ---------------- media ----------------

@app.route("/media/praise.jpg")
def media_praise():
    return Response(_PHOTO_BYTES, mimetype="image/jpeg",
                    headers={"Cache-Control": "public, max-age=31536000, immutable"})


@app.route("/media/<name>")
def media_responsive(name):
    if name not in {"praise-320.jpg", "praise-720.jpg"}:
        abort(404)
    static_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "static")
    return send_from_directory(static_dir, f"praiseface-{name.split('-')[1]}", max_age=31536000)


@app.route("/og.jpg")
def og_image():
    # [ADD DEDICATED 1200x630 OG IMAGE]. Reuses the profile photo for now.
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
    return Response(page, status=404, mimetype="text/html")


# Vercel expects the module-level `app`.
if __name__ == "__main__":
    app.run(port=5000, debug=True)
