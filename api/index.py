from flask import Flask, render_template_string

app = Flask(__name__)

ARTICLES = [
    {
        "title": "Cold Start Problem in Recommender Systems",
        "url": "https://www.freecodecamp.org/news/cold-start-problem-in-recommender-systems/",
        "source": "freeCodeCamp",
        "tags": ["machine learning", "recommender systems", "AI"],
    },
    {
        "title": "What's Changing in Vector Databases in 2026",
        "url": "https://dev.to/actiandev/whats-changing-in-vector-databases-in-2026-3pbo",
        "source": "DEV.to",
        "tags": ["databases", "vector databases", "data engineering"],
    },
    {
        "title": "Adversarial Machine Learning: Preventing Bad Actors from Compromising AI Models",
        "url": "https://hackernoon.com/adversarial-machine-learning-is-preventing-bad-actors-from-compromising-ai-models",
        "source": "HackerNoon",
        "tags": ["machine learning", "security", "adversarial AI"],
    },
    {
        "title": "Explainable Artificial Intelligence (XAI): Making Sense of AI Decisions",
        "url": "https://medium.com/@techwithpraisejames/explainable-artificial-intelligence-xai-making-sense-of-ai-decisions-5fa655655490",
        "source": "Medium",
        "tags": ["AI", "explainability", "XAI"],
    },
    {
        "title": "Decision Trees in Python Scikit-Learn: A Complete Guide for Beginners",
        "url": "https://medium.com/@techwithpraisejames/decision-trees-in-python-scikit-learn-a-complete-guide-for-beginners-15cb0540180f",
        "source": "Medium",
        "tags": ["python", "scikit-learn", "decision trees", "beginners"],
    },
]

VIDEOS = [
    {
        "title": "Video 1",
        "url": "https://youtu.be/NiWYwSMqETk?si=4KhkAG0PIQCQLkzG",
        "embed_id": "NiWYwSMqETk",
    },
    {
        "title": "Video 2",
        "url": "https://youtu.be/iW7VrXRgg0A?si=5fG7hwZtIoJ7M2-u",
        "embed_id": "iW7VrXRgg0A",
    },
    {
        "title": "Video 3",
        "url": "https://youtu.be/Z0yx9Pt7-rQ?si=TGIPqqZNWGrtWZlw",
        "embed_id": "Z0yx9Pt7-rQ",
    },
]

SOCIALS = [
    {
        "name": "YouTube",
        "url": "https://www.youtube.com/channel/UCwVDq2mG2FuNCRzAf-ypLvg",
        "icon": "youtube",
        "color": "#FF0000",
        "description": "Tech tutorials, AI walkthroughs & more",
    },
    {
        "name": "Newsletter",
        "url": "https://techwithpraisejames.substack.com/",
        "icon": "newsletter",
        "color": "#FF6719",
        "description": "Weekly insights on technical storytelling",
    },
    {
        "name": "GitHub",
        "url": "https://github.com/Techwithpraisejames",
        "icon": "github",
        "color": "#ffffff",
        "description": "Beginner-friendly AI projects",
    },
    {
        "name": "LinkedIn",
        "url": "https://www.linkedin.com/in/praise-james-608b91284",
        "icon": "linkedin",
        "color": "#0A66C2",
        "description": "Professional network & career updates",
    },
    {
        "name": "Medium",
        "url": "https://medium.com/@techwithpraisejames",
        "icon": "medium",
        "color": "#ffffff",
        "description": "Long-form articles on AI & tech",
    },
]

HTML_TEMPLATE = r"""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Praise James — Tech, AI & Everything In Between</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Gamja+Flower&family=Raleway:wght@300;400;500;600;700&display=swap" rel="stylesheet">
<style>
*,*::before,*::after{margin:0;padding:0;box-sizing:border-box}
:root{
  --bg:#000000;--surface:#111111;--surface2:#1a1a1a;
  --text:#ffffff;--text2:#bbbbbb;
  --pink:#E9A5DE;--pink-bright:#E9A5DE;--pink-glow:rgba(233,165,222,.15);
  --accent:#E9A5DE;--accent2:#E9A5DE;
}
html{scroll-behavior:smooth;overflow-x:hidden;scroll-snap-type:y mandatory}
body{
  font-family:'Raleway',sans-serif;
  background:var(--bg);color:var(--text);
  overflow-x:hidden;font-weight:400;
}
h1,h2,h3,.section-label,.social-name{
  font-family:'Gamja Flower',cursive;
}

/* SCROLLBAR */
::-webkit-scrollbar{width:6px;height:6px}
::-webkit-scrollbar-track{background:var(--bg)}
::-webkit-scrollbar-thumb{background:var(--pink);border-radius:3px}

/* SECTIONS */
section{
  min-height:100vh;padding:60px 24px;
  scroll-snap-align:start;
  position:relative;
}

/* HERO */
.hero{
  display:flex;flex-direction:column;justify-content:center;align-items:center;
  text-align:center;gap:24px;
  background:radial-gradient(ellipse at 50% 0%,rgba(255,182,193,.1) 0%,transparent 60%);
}
.hero h1{
  font-size:clamp(2.8rem,7vw,5.5rem);font-weight:400;
  letter-spacing:1px;line-height:1.1;
}
.hero h1 .highlight{
  background:linear-gradient(135deg,var(--pink),var(--pink-bright));
  -webkit-background-clip:text;-webkit-text-fill-color:transparent;
}
.hero p{font-size:1.1rem;color:var(--text2);max-width:540px;line-height:1.7;font-weight:300}
.scroll-hint{
  position:absolute;bottom:32px;left:50%;transform:translateX(-50%);
  display:flex;flex-direction:column;align-items:center;gap:8px;
  color:var(--text2);font-size:.85rem;animation:bounce 2s infinite;
}
@keyframes bounce{0%,100%{transform:translateX(-50%) translateY(0)}50%{transform:translateX(-50%) translateY(8px)}}

/* NAV PILLS */
.nav-pills{
  position:fixed;top:20px;left:50%;transform:translateX(-50%);z-index:100;
  display:flex;gap:4px;padding:6px;
  background:rgba(0,0,0,.85);backdrop-filter:blur(12px);
  border:1px solid rgba(255,182,193,.15);border-radius:40px;
}
.nav-pills a{
  padding:8px 18px;border-radius:30px;font-size:.82rem;font-weight:600;
  color:var(--text2);text-decoration:none;transition:.25s;white-space:nowrap;
  font-family:'Raleway',sans-serif;
}
.nav-pills a:hover,.nav-pills a.active{
  color:#000;background:var(--pink);
}

/* HORIZONTAL SCROLL TRACK */
.h-section{padding-bottom:40px}
.h-section h2{
  font-size:clamp(2rem,5vw,3rem);font-weight:400;
  margin-bottom:8px;padding-left:max(24px,calc((100vw - 1100px)/2));
}
.h-section .subtitle{
  color:var(--text2);font-size:.95rem;margin-bottom:28px;
  padding-left:max(24px,calc((100vw - 1100px)/2));
  font-weight:300;
}
.h-track{
  display:flex;gap:20px;overflow-x:auto;scroll-snap-type:x mandatory;
  padding:0 max(24px,calc((100vw - 1100px)/2)) 16px;
  -webkit-overflow-scrolling:touch;
}
.h-track::-webkit-scrollbar{height:4px}

/* ARTICLE CARD */
.card{
  flex:0 0 340px;scroll-snap-align:start;
  background:var(--surface);border:1px solid rgba(255,182,193,.1);
  border-radius:16px;padding:28px;
  display:flex;flex-direction:column;gap:14px;
  transition:transform .3s,box-shadow .3s,border-color .3s;
  text-decoration:none;color:var(--text);cursor:pointer;
}
.card:hover{
  transform:translateY(-4px);
  box-shadow:0 12px 40px var(--pink-glow);
  border-color:var(--pink);
}
.card .source{
  font-size:.75rem;font-weight:700;text-transform:uppercase;
  letter-spacing:1.5px;color:var(--pink);
}
.card .card-title{font-size:1.05rem;font-weight:500;line-height:1.4}
.card .tags{display:flex;flex-wrap:wrap;gap:6px;margin-top:auto}
.card .tag{
  font-size:.7rem;padding:4px 10px;border-radius:20px;
  background:rgba(255,182,193,.1);color:var(--pink);font-weight:600;
}

/* SOCIAL CARD */
.social-card{
  flex:0 0 280px;scroll-snap-align:start;
  border-radius:16px;padding:32px;
  display:flex;flex-direction:column;gap:16px;
  transition:transform .3s,box-shadow .3s;
  text-decoration:none;color:var(--text);
  border:1px solid rgba(255,182,193,.1);
  position:relative;overflow:hidden;
  background:var(--surface);
}
.social-card::before{
  content:'';position:absolute;top:0;left:0;right:0;height:3px;
  background:var(--card-accent);
}
.social-card:hover{
  transform:translateY(-4px) scale(1.01);
  box-shadow:0 16px 48px rgba(255,182,193,.12);
}
.social-icon{
  width:52px;height:52px;border-radius:14px;
  display:flex;align-items:center;justify-content:center;
  font-size:1.5rem;font-weight:800;
  background:rgba(255,182,193,.08);
}
.social-card .social-name{font-size:1.6rem;font-weight:400}
.social-card .social-desc{font-size:.9rem;color:var(--text2);line-height:1.5;font-weight:300}
.social-card .visit{
  margin-top:auto;font-size:.85rem;font-weight:600;
  color:var(--pink);display:flex;align-items:center;gap:6px;
}

/* VIDEO SECTION */
.video-section{padding-bottom:40px}
.video-track{
  display:flex;gap:20px;overflow-x:auto;scroll-snap-type:x mandatory;
  padding:0 max(24px,calc((100vw - 1100px)/2)) 16px;
  -webkit-overflow-scrolling:touch;
}
.video-track::-webkit-scrollbar{height:4px}
.video-card{
  flex:0 0 400px;scroll-snap-align:start;
  border-radius:16px;overflow:hidden;
  border:1px solid rgba(255,182,193,.1);
  transition:transform .3s,box-shadow .3s,border-color .3s;
  background:var(--surface);
}
.video-card:hover{
  transform:translateY(-4px);
  box-shadow:0 12px 40px var(--pink-glow);
  border-color:var(--pink);
}
.video-card iframe{
  width:100%;aspect-ratio:16/9;display:block;border:none;
}
@media(max-width:640px){
  .video-card{flex:0 0 300px}
}

/* NEWSLETTER SECTION */
.newsletter-section{
  display:flex;flex-direction:column;align-items:center;
  justify-content:center;text-align:center;gap:20px;
  background:radial-gradient(ellipse at 50% 50%,rgba(255,182,193,.06) 0%,transparent 60%);
}
.newsletter-section h2{font-size:clamp(2rem,5vw,3rem);font-weight:400}
.newsletter-section p{color:var(--text2);max-width:500px;line-height:1.7;font-weight:300}

/* SEARCH */
.search-wrap{
  width:100%;max-width:560px;position:relative;margin:0 auto;
}
.search-wrap input{
  width:100%;padding:16px 20px 16px 52px;
  background:var(--surface);border:1px solid rgba(255,182,193,.15);
  border-radius:14px;color:var(--text);font-size:1rem;
  font-family:'Raleway',sans-serif;font-weight:400;
  outline:none;transition:border-color .25s,box-shadow .25s;
}
.search-wrap input:focus{
  border-color:var(--pink);
  box-shadow:0 0 0 3px var(--pink-glow);
}
.search-wrap input::placeholder{color:var(--text2)}
.search-wrap .search-icon{
  position:absolute;left:18px;top:50%;transform:translateY(-50%);
  color:var(--text2);font-size:1.1rem;pointer-events:none;
}

/* SEARCH RESULTS */
.search-results{
  width:100%;max-width:560px;margin:0 auto;
  display:flex;flex-direction:column;gap:12px;
  max-height:360px;overflow-y:auto;
}
.search-result{
  background:var(--surface);border:1px solid rgba(255,182,193,.08);
  border-radius:12px;padding:18px 22px;text-align:left;
  text-decoration:none;color:var(--text);
  transition:border-color .2s,transform .2s;display:block;
}
.search-result:hover{border-color:var(--pink);transform:translateX(4px)}
.search-result .sr-source{
  font-size:.7rem;font-weight:700;text-transform:uppercase;
  letter-spacing:1.5px;color:var(--pink-bright);margin-bottom:6px;
}
.search-result .sr-title{font-size:1rem;font-weight:500}
.no-results{color:var(--text2);font-size:.9rem;padding:20px}

/* CTA BUTTON */
.cta{
  display:inline-flex;align-items:center;gap:8px;
  padding:14px 32px;border-radius:40px;font-weight:700;
  font-size:.95rem;text-decoration:none;color:#000;
  background:linear-gradient(135deg,var(--pink),var(--pink-bright));
  transition:transform .2s,box-shadow .2s;
  font-family:'Raleway',sans-serif;
}
.cta:hover{transform:translateY(-2px);box-shadow:0 8px 30px var(--pink-glow)}
.cta.secondary{
  background:transparent;color:var(--pink);
  border:2px solid var(--pink);
}
.cta.secondary:hover{background:rgba(255,182,193,.08)}

/* FOOTER */
footer{
  padding:40px 24px;text-align:center;
  border-top:1px solid rgba(255,182,193,.1);
}
footer p{color:var(--text2);font-size:.85rem;font-weight:300}
footer .footer-links{display:flex;justify-content:center;gap:20px;margin-top:16px;flex-wrap:wrap}
footer a{color:var(--text2);text-decoration:none;font-size:.85rem;transition:color .2s;font-weight:500}
footer a:hover{color:var(--pink)}

/* SWIPE INDICATOR */
.swipe-indicator{
  display:flex;gap:6px;justify-content:center;padding:12px 0;
}
.swipe-dot{
  width:8px;height:8px;border-radius:50%;
  background:rgba(255,182,193,.2);transition:background .3s,transform .3s;
}
.swipe-dot.active{background:var(--pink);transform:scale(1.3)}

/* RESPONSIVE */
@media(max-width:640px){
  .nav-pills{top:auto;bottom:16px;left:8px;right:8px;
    transform:none;justify-content:center;overflow-x:auto}
  .nav-pills a{padding:8px 14px;font-size:.75rem}
  section{padding:48px 16px;min-height:auto}
  .hero{min-height:100vh}
  .card{flex:0 0 280px;padding:22px}
  .social-card{flex:0 0 260px;padding:24px}
}

/* VERTICAL ARTICLE LIST */
.v-articles{
  max-width:700px;margin:40px auto 0;
  display:flex;flex-direction:column;gap:16px;
}
.v-article{
  background:var(--surface);border:1px solid rgba(255,182,193,.08);
  border-radius:14px;padding:24px;
  display:flex;gap:18px;align-items:center;
  text-decoration:none;color:var(--text);
  transition:border-color .2s,transform .2s;
}
.v-article:hover{border-color:var(--pink);transform:translateX(6px)}
.v-article .v-num{
  font-size:2rem;font-weight:400;color:rgba(255,182,193,.3);
  flex-shrink:0;width:48px;text-align:center;
  font-family:'Gamja Flower',cursive;
}
.v-article .v-info{display:flex;flex-direction:column;gap:4px}
.v-article .v-source{
  font-size:.7rem;font-weight:700;text-transform:uppercase;
  letter-spacing:1.5px;color:var(--pink);
}
.v-article .v-title{font-size:1rem;font-weight:500;line-height:1.4}

/* READ MORE LINK */
.read-more-wrap{
  max-width:700px;margin:28px auto 0;text-align:center;
}

/* SECTION LABELS */
.section-label{
  font-size:1rem;font-weight:400;text-transform:uppercase;
  letter-spacing:2px;color:var(--pink);margin-bottom:8px;
  padding-left:max(24px,calc((100vw - 1100px)/2));
  font-family:'Gamja Flower',cursive;
}
</style>
</head>
<body>

<!-- NAV -->
<nav class="nav-pills" id="nav">
  <a href="#hero">Home</a>
  <a href="#articles">Articles</a>
  <a href="#videos">Videos</a>
  <a href="#connect">Connect</a>
  <a href="#newsletter">Newsletter</a>
</nav>

<!-- HERO -->
<section class="hero" id="hero">
  <p style="font-size:.95rem;font-weight:400;letter-spacing:3px;text-transform:uppercase;color:var(--pink);font-family:'Gamja Flower',cursive;font-size:1.2rem">
    Tech Writer &bull; Content Creator &bull; AI Storyteller
  </p>
  <h1>Hey, I'm <span class="highlight">Praise James</span></h1>
  <p>
    I write about AI, machine learning, and emerging tech.
    This is your one-stop hub for everything I create &mdash; articles, videos, code, and more.
  </p>
  <div style="display:flex;gap:12px;flex-wrap:wrap;justify-content:center">
    <a class="cta" href="#articles">Explore My Work &darr;</a>
    <a class="cta secondary" href="https://techwithpraisejames.substack.com/" target="_blank">
      Subscribe &nearr;
    </a>
  </div>
  <div class="scroll-hint">
    <span>Scroll to explore</span>
    <span style="font-size:1.4rem">&darr;</span>
  </div>
</section>

<!-- ARTICLES — HORIZONTAL SWIPE -->
<section class="h-section" id="articles">
  <p class="section-label">Published Work</p>
  <h2>Articles & Tutorials</h2>
  <p class="subtitle">Swipe or drag to browse &rarr;</p>
  <div class="h-track" id="articleTrack">
    {% for a in articles %}
    <a class="card" href="{{ a.url }}" target="_blank" rel="noopener">
      <span class="source">{{ a.source }}</span>
      <span class="card-title">{{ a.title }}</span>
      <div class="tags">
        {% for t in a.tags %}<span class="tag">{{ t }}</span>{% endfor %}
      </div>
    </a>
    {% endfor %}
  </div>
  <div class="swipe-indicator" id="articleDots"></div>

  <!-- VERTICAL LIST — just the 5 articles -->
  <div class="v-articles" id="vArticles">
    {% for a in articles %}
    <a class="v-article" href="{{ a.url }}" target="_blank" rel="noopener">
      <span class="v-num">{{ "%02d"|format(loop.index) }}</span>
      <div class="v-info">
        <span class="v-source">{{ a.source }}</span>
        <span class="v-title">{{ a.title }}</span>
      </div>
    </a>
    {% endfor %}
  </div>
  <div class="read-more-wrap">
    <a class="cta secondary" href="https://medium.com/@techwithpraisejames" target="_blank" rel="noopener">
      Read more on Medium &nearr;
    </a>
  </div>
</section>

<!-- VIDEOS — HORIZONTAL SWIPE -->
<section class="h-section video-section" id="videos">
  <p class="section-label">Watch</p>
  <h2>YouTube Videos</h2>
  <p class="subtitle">Swipe to watch &rarr;</p>
  <div class="h-track video-track" id="videoTrack">
    {% for v in videos %}
    <div class="video-card">
      <iframe src="https://www.youtube.com/embed/{{ v.embed_id }}" title="{{ v.title }}"
              allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
              allowfullscreen loading="lazy"></iframe>
    </div>
    {% endfor %}
  </div>
  <div class="swipe-indicator" id="videoDots"></div>
  <div class="read-more-wrap" style="margin-top:20px">
    <a class="cta secondary" href="https://www.youtube.com/channel/UCwVDq2mG2FuNCRzAf-ypLvg" target="_blank">
      See all videos on YouTube &nearr;
    </a>
  </div>
</section>

<!-- CONNECT — HORIZONTAL SWIPE -->
<section class="h-section" id="connect">
  <p class="section-label">Stay Connected</p>
  <h2>Find Me Everywhere</h2>
  <p class="subtitle">Swipe to see all platforms &rarr;</p>
  <div class="h-track" id="socialTrack">
    {% for s in socials %}
    <a class="social-card" href="{{ s.url }}" target="_blank" rel="noopener"
       style="--card-accent:{{ s.color }}">
      <div class="social-icon" style="color:{{ s.color }}">
        {% if s.icon == 'youtube' %}&#9654;
        {% elif s.icon == 'newsletter' %}&#9993;
        {% elif s.icon == 'github' %}{ }
        {% elif s.icon == 'linkedin' %}in
        {% elif s.icon == 'medium' %}M
        {% endif %}
      </div>
      <span class="social-name">{{ s.name }}</span>
      <span class="social-desc">{{ s.description }}</span>
      <span class="visit">Visit &rarr;</span>
    </a>
    {% endfor %}
  </div>
  <div class="swipe-indicator" id="socialDots"></div>
</section>

<!-- NEWSLETTER + SEARCH -->
<section class="newsletter-section" id="newsletter">
  <p class="section-label">Newsletter</p>
  <h2>Search My Content</h2>
  <p>Find articles by topic, keyword, or technology. Or subscribe to get new ones in your inbox.</p>
  <div class="search-wrap">
    <span class="search-icon">&#128269;</span>
    <input type="text" id="searchInput" placeholder="Search articles... (e.g. AI, vector databases, Python)"
           autocomplete="off">
  </div>
  <div class="search-results" id="searchResults"></div>
  <a class="cta" href="https://techwithpraisejames.substack.com/" target="_blank"
     style="margin-top:12px">
    Subscribe to Newsletter &nearr;
  </a>
</section>

<!-- FOOTER -->
<footer>
  <p>&copy; 2026 Praise James. Built with purpose.</p>
  <div class="footer-links">
    <a href="https://www.youtube.com/channel/UCwVDq2mG2FuNCRzAf-ypLvg" target="_blank">YouTube</a>
    <a href="https://techwithpraisejames.substack.com/" target="_blank">Newsletter</a>
    <a href="https://github.com/Techwithpraisejames" target="_blank">GitHub</a>
    <a href="https://www.linkedin.com/in/praise-james-608b91284" target="_blank">LinkedIn</a>
    <a href="https://medium.com/@techwithpraisejames" target="_blank">Medium</a>
  </div>
</footer>

<script>
const articles = {{ articles_json | safe }};

// SEARCH
const searchInput = document.getElementById('searchInput');
const searchResults = document.getElementById('searchResults');

searchInput.addEventListener('input', function() {
  const q = this.value.toLowerCase().trim();
  searchResults.innerHTML = '';
  if (!q) return;

  const matches = articles.filter(a =>
    a.title.toLowerCase().includes(q) ||
    a.source.toLowerCase().includes(q) ||
    a.tags.some(t => t.toLowerCase().includes(q))
  );

  if (matches.length === 0) {
    searchResults.innerHTML = '<div class="no-results">No articles found. Try a different keyword.</div>';
    return;
  }

  matches.forEach(a => {
    const el = document.createElement('a');
    el.className = 'search-result';
    el.href = a.url;
    el.target = '_blank';
    el.rel = 'noopener';
    el.innerHTML = `<div class="sr-source">${a.source}</div><div class="sr-title">${a.title}</div>`;
    searchResults.appendChild(el);
  });
});

// SWIPE DOTS
function setupDots(trackId, dotsId) {
  const track = document.getElementById(trackId);
  const dotsContainer = document.getElementById(dotsId);
  const cards = track.children;
  if (!cards.length) return;

  for (let i = 0; i < cards.length; i++) {
    const dot = document.createElement('div');
    dot.className = 'swipe-dot' + (i === 0 ? ' active' : '');
    dotsContainer.appendChild(dot);
  }

  track.addEventListener('scroll', () => {
    const scrollLeft = track.scrollLeft;
    const cardWidth = cards[0].offsetWidth + 20;
    const idx = Math.round(scrollLeft / cardWidth);
    dotsContainer.querySelectorAll('.swipe-dot').forEach((d, i) => {
      d.classList.toggle('active', i === idx);
    });
  });
}
setupDots('articleTrack', 'articleDots');
setupDots('socialTrack', 'socialDots');
setupDots('videoTrack', 'videoDots');

// NAV ACTIVE STATE
const sections = document.querySelectorAll('section');
const navLinks = document.querySelectorAll('.nav-pills a');

const observer = new IntersectionObserver(entries => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      const id = entry.target.id;
      navLinks.forEach(l => {
        l.classList.toggle('active', l.getAttribute('href') === '#' + id);
      });
    }
  });
}, { threshold: 0.4 });

sections.forEach(s => observer.observe(s));
</script>

</body>
</html>
"""


@app.route("/")
def home():
    import json

    return render_template_string(
        HTML_TEMPLATE,
        articles=ARTICLES,
        socials=SOCIALS,
        videos=VIDEOS,
        articles_json=json.dumps(ARTICLES),
    )


# Vercel expects the app object
