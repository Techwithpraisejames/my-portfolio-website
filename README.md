# Praise James portfolio and client-acquisition site

A specialist technical writer's site: positioning, proof, services, case studies,
and a single conversion path to `/contact`. Server-rendered, no client-side framework.

## Tech stack

- **Backend:** Python / Flask (server-rendered HTML, no build step)
- **Hosting:** Vercel (`@vercel/python` serverless runtime)

## Project structure

```
api/
  index.py          Flask app: routes, /sitemap.xml, /robots.txt, /media, /og.jpg, 404
  theme.py          Design system: tokens + the full stylesheet
  seo.py            Per-page metadata, canonical/OG/Twitter tags, JSON-LD builders
  shell.py          Full-document shell (head, nav, main, footer)
  components.py     Shared render helpers (nav, footer, cards, CTAs, breadcrumbs)
  content.py        The content model. Edit this to add work, case studies, etc.
  pages_*.py        One module per page group (home, work, services, about, insights, contact)
  photo_data.py     Base-64 profile photo (served by /media/praise.jpg and /og.jpg)
requirements.txt
vercel.json         Routes everything to api/index.py
```

## Routes

`/` · `/work` · `/work/case-studies` · `/work/case-studies/<slug>` · `/services` ·
`/services/<slug>` · `/about` · `/insights` · `/contact` · `/sitemap.xml` · `/robots.txt`

## Editing content

Everything editable lives in `api/content.py`; no component code needs to change.
Placeholders are written as `[ADD ...]` and render as clearly marked dashed blocks.
Never replace a placeholder with an unverified client, metric, testimonial, or quote.

To change the canonical domain, edit `SITE_URL` in `api/seo.py`.

## Local development

```bash
pip install -r requirements.txt
python -m flask --app api/index.py run --port 5000
```

## Links

- [YouTube](https://www.youtube.com/channel/UCwVDq2mG2FuNCRzAf-ypLvg)
- [Newsletter (Tech & Storytelling)](https://techwithpraisejames.substack.com/)
- [LinkedIn](https://www.linkedin.com/in/praise-james-608b91284)
- [Medium](https://medium.com/@techwithpraisejames)
