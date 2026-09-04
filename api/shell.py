"""The full-document shell: <head> with SEO, nav, <main>, footer."""
from components import NAV_SCRIPT, footer, nav
from seo import head_tags, json_ld
from theme import BASE_CSS, FONT_URL

FAVICON = (
    "data:image/svg+xml,"
    "%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E"
    "%3Crect width='32' height='32' rx='6' fill='%230C0E10'/%3E"
    "%3Ctext x='16' y='22' font-family='Georgia,serif' font-size='18' fill='%23E9A5DE' text-anchor='middle'%3EP%3C/text%3E"
    "%3C/svg%3E"
)


def render_page(meta, body_html: str, path: str, breadcrumbs_html: str = "",
                jsonld_blocks=()) -> str:
    ld = json_ld(*jsonld_blocks) if jsonld_blocks else ""
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="theme-color" content="#0C0E10">
  <meta name="color-scheme" content="dark">
  <link rel="icon" href="{FAVICON}">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="stylesheet" href="{FONT_URL}">
  {head_tags(meta)}
  {ld}
  <style>{BASE_CSS}</style>
</head>
<body>
{nav(path)}
{breadcrumbs_html}
<main id="main">
{body_html}
</main>
{footer()}
{NAV_SCRIPT}
<script defer src="/_vercel/insights/script.js"></script>
</body>
</html>"""
