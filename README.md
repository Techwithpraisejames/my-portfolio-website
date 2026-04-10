# Praise James — Portfolio Website

A personal portfolio website built with Python (Flask) and deployed on Vercel. One-stop hub for articles, YouTube videos, newsletter, and social links.

## Features

- **Horizontal swipe cards** for articles and social platforms
- **YouTube video embeds** with swipeable carousel
- **Article search** by title, source, or tags
- **Responsive design** optimized for mobile and desktop
- **Brand styling** with Gamja Flower + Raleway fonts and #E9A5DE pink accents on black

## Tech Stack

- **Backend:** Python / Flask
- **Hosting:** Vercel (serverless Python runtime)
- **Fonts:** Google Fonts (Gamja Flower, Raleway)
- **Analytics:** Vercel Analytics

## Project Structure

```
├── api/
│   └── index.py          # Flask app with all routes and HTML template
├── requirements.txt      # Python dependencies
├── vercel.json           # Vercel routing configuration
└── README.md
```

## Local Development

```bash
pip install -r requirements.txt
cd api
flask --app index run
```

Then open `http://localhost:5000`.

## Deployment

This app is configured for Vercel:

1. Push to GitHub
2. Import the repo on [vercel.com](https://vercel.com)
3. Vercel auto-detects the Python config from `vercel.json`
4. Enable Analytics in Project Settings if desired

## Links

- [YouTube](https://www.youtube.com/channel/UCwVDq2mG2FuNCRzAf-ypLvg)
- [Newsletter (Substack)](https://techwithpraisejames.substack.com/)
- [GitHub](https://github.com/Techwithpraisejames)
- [LinkedIn](https://www.linkedin.com/in/praise-james-608b91284)
- [Medium](https://medium.com/@techwithpraisejames)
