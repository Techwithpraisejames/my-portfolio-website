from flask import Flask, render_template_string
import json as _json

app = Flask(__name__)

ARTICLES = [
    {
        "title": "Best Apify Alternative for Large-Scale Scraping",
        "url": "https://www.zenrows.com/blog/best-apify-alternative-for-large-scale-scraping",
        "source": "ZenRows",
        "descriptor": "Original benchmark. 200 requests across 7 targets, performance and cost analysis",
        "tags": ["web scraping", "benchmarks", "developer tools"],
    },
    {
        "title": "How to Build a Stateful Web Research Agent with ZenRows and LangGraph",
        "url": "https://dev.to/zenrows/how-to-build-a-stateful-web-research-agent-with-zenrows-and-langgraph-1co7",
        "source": "DEV.to",
        "descriptor": "Production tutorial. Stateful AI agent with retry logic and live web scraping",
        "tags": ["LangGraph", "AI agents", "ZenRows"],
    },
    {
        "title": "5 Edge AI Architecture Patterns for Disconnected Environments",
        "url": "https://dev.to/actiandev/5-edge-ai-architecture-patterns-for-disconnected-environments-27of",
        "source": "DEV.to",
        "descriptor": "Architecture guide for AI at the edge, no cloud required",
        "tags": ["edge AI", "architecture", "databases"],
    },
    {
        "title": "What's Changing in Vector Databases in 2026",
        "url": "https://dev.to/actiandev/whats-changing-in-vector-databases-in-2026-3pbo",
        "source": "DEV.to",
        "descriptor": "Market analysis of the vector database landscape and where it's headed",
        "tags": ["vector databases", "data engineering"],
    },
    {
        "title": "A CTO's 5-Phase Roadmap to AI-Native Internal Tools",
        "url": "https://dev.to/bennykillua/a-ctos-5-phase-roadmap-to-ai-native-internal-tools-and-why-most-pilots-stall-5ea5",
        "source": "DEV.to",
        "descriptor": "Thought leadership on why most AI pilot programs stall and how to fix it",
        "tags": ["AI", "leadership", "internal tools"],
    },
    {
        "title": "Integrating Web Data into AI Knowledge Graphs",
        "url": "https://data4ai.com/blog/use-case-deep-dives/integrating-web-data-into-ai-knowledge-graphs/",
        "source": "Data4AI",
        "descriptor": "Deep dive into building knowledge graphs with live web data",
        "tags": ["knowledge graphs", "web data", "AI"],
    },
    {
        "title": "Adversarial Machine Learning: Preventing Bad Actors from Compromising AI Models",
        "url": "https://hackernoon.com/adversarial-machine-learning-is-preventing-bad-actors-from-compromising-ai-models",
        "source": "HackerNoon",
        "descriptor": "A breakdown of how bad actors attack AI models and what it takes to defend against them",
        "tags": ["machine learning", "security", "adversarial AI"],
    },
    {
        "title": "Explainable Artificial Intelligence (XAI): Making Sense of AI Decisions",
        "url": "https://medium.com/@techwithpraisejames/explainable-artificial-intelligence-xai-making-sense-of-ai-decisions-5fa655655490",
        "source": "Medium",
        "descriptor": "Making sense of how AI systems reach their decisions and why that transparency matters",
        "tags": ["AI", "explainability", "XAI"],
    },
    {
        "title": "Cold Start Problem in Recommender Systems",
        "url": "https://www.freecodecamp.org/news/cold-start-problem-in-recommender-systems/",
        "source": "freeCodeCamp",
        "descriptor": "How recommender systems handle new users and items with no historical data to learn from",
        "tags": ["machine learning", "recommender systems"],
    },
    {
        "title": "Decision Trees in Python Scikit-Learn: A Complete Guide for Beginners",
        "url": "https://medium.com/@techwithpraisejames/decision-trees-in-python-scikit-learn-a-complete-guide-for-beginners-15cb0540180f",
        "source": "Medium",
        "descriptor": "A beginner-friendly guide to building and interpreting decision tree models with Scikit-Learn",
        "tags": ["Python", "scikit-learn", "beginners"],
    },
]

VIDEOS = [
    {"embed_id": "NiWYwSMqETk"},
    {"embed_id": "iW7VrXRgg0A"},
    {"embed_id": "Z0yx9Pt7-rQ"},
    {"embed_id": "x-PyeOhqXi0"},
    {"embed_id": "84oDAPn7kls"},
]

SOCIALS = [
    {"name": "YouTube", "url": "https://www.youtube.com/channel/UCwVDq2mG2FuNCRzAf-ypLvg", "icon": "YT", "color": "#FF0000"},
    {"name": "Newsletter", "url": "https://techwithpraisejames.substack.com/", "icon": "NS", "color": "#FF6719"},
    {"name": "LinkedIn", "url": "https://www.linkedin.com/in/praise-james-608b91284", "icon": "in", "color": "#0A66C2"},
    {"name": "GitHub", "url": "https://github.com/Techwithpraisejames", "icon": "GH", "color": "#ffffff"},
    {"name": "Medium", "url": "https://medium.com/@techwithpraisejames", "icon": "M", "color": "#ffffff"},
]

NEWSLETTERS = [
    {"title": "The Hierarchy of Technical Content", "url": "https://techwithpraisejames.substack.com/p/the-hierarchy-of-technical-content"},
    {"title": "Bridging Product and People in Technical Writing", "url": "https://techwithpraisejames.substack.com/p/bridging-product-and-people-in-technical"},
    {"title": "The PTS Framework: Problem, Tension, Solution", "url": "https://techwithpraisejames.substack.com/p/the-pts-framework-problem-tension"},
    {"title": "The Questions You Ask Shape the Content", "url": "https://techwithpraisejames.substack.com/p/the-questions-you-ask-shape-the-content"},
    {"title": "The 5C Framework for What Is Articles", "url": "https://techwithpraisejames.substack.com/p/the-5c-framework-for-what-is-articles"},
]

TESTIMONIALS = [
    {"quote": "You are amazing and so responsible! I will for sure ask for more of your services for some other prototypes and events marketing.", "name": "Ornella", "title": "Founder and CEO", "company": "MindyMinds"},
    {"quote": "Whenever I get a task of reviewing your document, it becomes one of my favourite activities. Amazing work as always.", "name": "Asjad", "title": "Developer Advocate", "company": "Hackmamba"},
    {"quote": "This is a strong piece. Love how technically-grounded and exhaustive it is.", "name": "Henry", "title": "Head of Content", "company": "Hackmamba"},
    {"quote": "It should be required reading for anyone who still thinks technical writing is just a finishing step. The value is invisible by design and this makes it visible.", "name": "Adrian", "title": "Senior Technical Writer", "company": ""},
    {"quote": "Your content is the benchmark for others on the team.", "name": "Blessing", "title": "Head of Operations", "company": "Hackmamba"},
]

HTML_TEMPLATE = r"""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Praise James — AI/ML Technical Writer and Developer Relations</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Gamja+Flower&family=Raleway:ital,wght@0,300;0,400;0,500;0,600;0,700;1,300;1,400&display=swap" rel="stylesheet">
<style>
*,*::before,*::after{margin:0;padding:0;box-sizing:border-box}
:root{
  --bg:#000000;
  --surface:#0d0d0d;
  --surface2:#161616;
  --text:#ffffff;
  --text2:#aaaaaa;
  --pink:#E9A5DE;
  --pink-dim:rgba(233,165,222,.12);
  --pink-glow:rgba(233,165,222,.18);
}
html{scroll-behavior:smooth;overflow-x:hidden}
body{font-family:'Raleway',sans-serif;background:var(--bg);color:var(--text);overflow-x:hidden;font-weight:400;line-height:1.6}

/* SCROLLBAR */
::-webkit-scrollbar{width:5px;height:5px}
::-webkit-scrollbar-track{background:var(--bg)}
::-webkit-scrollbar-thumb{background:var(--pink);border-radius:3px}

/* NAV */
.nav{
  position:fixed;top:0;left:0;right:0;z-index:200;
  display:flex;align-items:center;justify-content:center;
  padding:16px 24px;
  background:rgba(0,0,0,.8);backdrop-filter:blur(16px);
  border-bottom:1px solid rgba(233,165,222,.08);
}
.nav-inner{display:flex;gap:4px;align-items:center}
.nav a{
  padding:7px 16px;border-radius:30px;font-size:.8rem;font-weight:600;
  color:var(--text2);text-decoration:none;transition:.2s;white-space:nowrap;
  font-family:'Raleway',sans-serif;letter-spacing:.3px;
}
.nav a:hover,.nav a.active{color:#000;background:var(--pink)}

/* SECTIONS */
section{padding:72px 24px 64px;max-width:1200px;margin:0 auto}
section.full-width{max-width:none;padding-left:0;padding-right:0}

/* SECTION LABEL */
.label{
  font-family:'Gamja Flower',cursive;
  font-size:.9rem;letter-spacing:3px;text-transform:uppercase;
  color:var(--pink);margin-bottom:10px;display:block;
}
.label.center{text-align:center}

/* HEADINGS */
h2{font-family:'Gamja Flower',cursive;font-size:clamp(2.2rem,5vw,3.4rem);font-weight:400;line-height:1.15;margin-bottom:14px}
h3{font-family:'Gamja Flower',cursive;font-size:1.5rem;font-weight:400;margin-bottom:8px}

/* HERO */
#hero{
  min-height:100vh;display:flex;flex-direction:column;
  justify-content:center;align-items:flex-start;
  padding-top:80px;padding-bottom:48px;
  position:relative;overflow:hidden;
}
#hero::before{
  content:'';position:absolute;top:-20%;right:-10%;
  width:60vw;height:60vw;max-width:700px;max-height:700px;
  background:radial-gradient(circle,rgba(233,165,222,.06) 0%,transparent 70%);
  pointer-events:none;
}

/* HERO BADGE — corner-bracket frame */
@keyframes badgeFade{from{opacity:0;transform:translateY(-4px)}to{opacity:1;transform:translateY(0)}}
@keyframes cornerDraw{from{opacity:0}to{opacity:1}}
.hero-tag{
  display:inline-block;
  position:relative;
  padding:10px 18px;
  margin-bottom:20px;
  font-family:'Raleway',sans-serif;
  font-size:11px;font-weight:600;
  letter-spacing:.15em;text-transform:uppercase;
  color:var(--text);
  background:none;border:none;border-radius:0;
  animation:badgeFade .5s ease both;
}
.hero-tag .corner{
  position:absolute;width:12px;height:12px;
  border-color:var(--pink);border-style:solid;
  animation:cornerDraw .4s ease .6s both;
}
.hero-tag .corner.tl{top:0;left:0;border-width:2px 0 0 2px}
.hero-tag .corner.tr{top:0;right:0;border-width:2px 2px 0 0}
.hero-tag .corner.bl{bottom:0;left:0;border-width:0 0 2px 2px}
.hero-tag .corner.br{bottom:0;right:0;border-width:0 2px 2px 0}

.hero-headline{
  font-family:'Gamja Flower',cursive;
  font-size:clamp(2.4rem,4.5vw,3.8rem);
  font-weight:400;line-height:1.15;
  margin-bottom:18px;
}
.hero-headline .static{display:block;color:var(--text)}
.hero-headline .typewriter-wrap{
  display:block;color:var(--pink);
  min-height:1.2em;
}
#typewriter{border-right:3px solid var(--pink);padding-right:4px;animation:blink .75s step-end infinite}
@keyframes blink{0%,100%{border-color:var(--pink)}50%{border-color:transparent}}

.hero-sub{
  font-size:1rem;color:var(--text2);max-width:560px;
  line-height:1.75;font-weight:300;margin-bottom:28px;
}
.hero-sub strong{color:var(--text);font-weight:600}
.hero-actions{display:flex;gap:12px;flex-wrap:wrap}

@media(max-width:640px){
  #hero{padding-top:72px;padding-bottom:36px}
  .hero-headline{margin-bottom:14px}
  .hero-sub{font-size:.95rem;margin-bottom:24px}
}

/* BUTTONS */
.btn{
  display:inline-flex;align-items:center;gap:8px;
  padding:13px 28px;border-radius:40px;font-weight:700;
  font-size:.9rem;text-decoration:none;transition:.2s;
  font-family:'Raleway',sans-serif;cursor:pointer;border:none;
}
.btn-primary{background:var(--pink);color:#000}
.btn-primary:hover{transform:translateY(-2px);box-shadow:0 8px 30px var(--pink-glow)}
.btn-outline{background:transparent;color:var(--pink);border:2px solid var(--pink)}
.btn-outline:hover{background:var(--pink-dim)}

/* METRICS BAR */
.metrics-bar{
  background:var(--surface);
  border-top:1px solid rgba(233,165,222,.1);
  border-bottom:1px solid rgba(233,165,222,.1);
  padding:40px 24px;
}
.metrics-inner{
  max-width:900px;margin:0 auto;
  display:grid;grid-template-columns:repeat(3,1fr);gap:24px;
}
.metric{text-align:center;padding:16px}
.metric-num{
  font-family:'Gamja Flower',cursive;
  font-size:clamp(2.2rem,4vw,3rem);
  color:var(--pink);line-height:1;margin-bottom:8px;display:block;
}
.metric-label{font-size:.85rem;color:var(--text2);font-weight:400;line-height:1.4}
@media(max-width:640px){.metrics-inner{grid-template-columns:1fr}}

/* HORIZONTAL TRACK */
.track-section{padding:64px 0}
.track-header{padding:0 max(24px,calc((100vw - 1150px)/2));margin-bottom:24px}
.h-track{
  display:flex;gap:20px;overflow-x:auto;
  padding:4px max(24px,calc((100vw - 1150px)/2)) 20px;
  scroll-snap-type:x mandatory;-webkit-overflow-scrolling:touch;
}
.h-track::-webkit-scrollbar{height:3px}
.dots{display:flex;gap:5px;justify-content:center;padding:8px 0 0}
.dot{width:6px;height:6px;border-radius:50%;background:rgba(233,165,222,.2);transition:.3s}
.dot.active{background:var(--pink);transform:scale(1.4)}

/* ARTICLE CARD */
.art-card{
  flex:0 0 320px;scroll-snap-align:start;
  background:var(--surface);border:1px solid rgba(233,165,222,.08);
  border-radius:16px;padding:26px;
  display:flex;flex-direction:column;gap:12px;
  text-decoration:none;color:var(--text);
  transition:transform .25s,border-color .25s,box-shadow .25s;
}
.art-card:hover{transform:translateY(-4px);border-color:var(--pink);box-shadow:0 12px 40px var(--pink-glow)}
.art-src{font-size:.7rem;font-weight:700;text-transform:uppercase;letter-spacing:1.5px;color:var(--pink)}
.art-title{font-size:1rem;font-weight:600;line-height:1.4}
.art-desc{font-size:.85rem;color:var(--text2);font-weight:300;line-height:1.5;font-style:italic}
.art-tags{display:flex;flex-wrap:wrap;gap:6px;margin-top:auto}
.tag{font-size:.68rem;padding:3px 10px;border-radius:20px;background:var(--pink-dim);color:var(--pink);font-weight:600}

/* FEATURED PROJECT */
#project{background:var(--surface);border-top:1px solid rgba(233,165,222,.08);border-bottom:1px solid rgba(233,165,222,.08)}
.project-inner{max-width:1100px;margin:0 auto;padding:80px 24px;display:grid;grid-template-columns:1fr 1fr;gap:60px;align-items:center}
.project-quotes{display:flex;flex-direction:column;gap:20px}
.proj-quote{
  background:var(--surface2);border-left:3px solid var(--pink);
  border-radius:0 12px 12px 0;padding:20px 24px;
}
.proj-quote p{font-size:.9rem;color:var(--text2);line-height:1.7;font-style:italic;font-weight:300}
.proj-quote cite{font-size:.78rem;color:var(--pink);font-weight:600;letter-spacing:.5px;margin-top:8px;display:block;font-style:normal}
@media(max-width:768px){.project-inner{grid-template-columns:1fr;gap:36px}}

/* DEVREL */
.devrel-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:24px;margin-top:40px}
.devrel-card{
  background:var(--surface);border:1px solid rgba(233,165,222,.08);
  border-radius:16px;padding:28px;
  transition:border-color .25s,transform .25s;
}
.devrel-card:hover{border-color:var(--pink);transform:translateY(-3px)}
.devrel-num{font-family:'Gamja Flower',cursive;font-size:2rem;color:var(--pink);line-height:1;margin-bottom:12px}
.devrel-title{font-size:1rem;font-weight:700;margin-bottom:8px;color:var(--text)}
.devrel-desc{font-size:.88rem;color:var(--text2);line-height:1.65;font-weight:300}

/* VIDEO CARD */
.vid-card{
  flex:0 0 400px;scroll-snap-align:start;
  border-radius:16px;overflow:hidden;
  border:1px solid rgba(233,165,222,.08);
  transition:transform .25s,border-color .25s;
  background:var(--surface);
}
.vid-card:hover{transform:translateY(-4px);border-color:var(--pink)}
.vid-card iframe{width:100%;aspect-ratio:16/9;display:block;border:none}
@media(max-width:640px){.vid-card{flex:0 0 300px}}

/* ABOUT */
.about-grid{display:grid;grid-template-columns:1fr 1fr;gap:60px;align-items:start;margin-top:40px}
.about-text p{font-size:1rem;color:var(--text2);line-height:1.85;font-weight:300;margin-bottom:20px}
.about-text p:last-child{margin-bottom:0}
.about-text strong{color:var(--pink);font-weight:600}
.about-pills{display:flex;flex-direction:column;gap:16px}
.about-pill{
  background:var(--surface);border:1px solid rgba(233,165,222,.08);
  border-radius:14px;padding:22px;
  transition:border-color .25s;
}
.about-pill:hover{border-color:var(--pink)}
.about-pill h4{font-family:'Gamja Flower',cursive;font-size:1.2rem;color:var(--text);margin-bottom:6px}
.about-pill p{font-size:.85rem;color:var(--text2);line-height:1.6;font-weight:300}
@media(max-width:768px){.about-grid{grid-template-columns:1fr;gap:32px}}

/* TESTIMONIALS */
.test-card{
  flex:0 0 360px;scroll-snap-align:start;
  background:var(--surface);border:1px solid rgba(233,165,222,.08);
  border-radius:16px;padding:30px;
  display:flex;flex-direction:column;gap:14px;
  transition:transform .25s,border-color .25s;
}
.test-card:hover{transform:translateY(-4px);border-color:var(--pink)}
.test-mark{font-family:'Gamja Flower',cursive;font-size:3.5rem;line-height:.8;color:var(--pink);opacity:.35}
.test-quote{font-size:.92rem;color:var(--text2);line-height:1.75;font-weight:300;font-style:italic}
.test-author{margin-top:auto;padding-top:14px;border-top:1px solid rgba(233,165,222,.1)}
.test-name{font-size:.85rem;font-weight:700;color:var(--text)}
.test-role{font-size:.78rem;color:var(--pink);margin-top:3px}

/* CONNECT */
.connect-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:16px;margin-top:40px}
.connect-card{
  background:var(--surface);border:1px solid rgba(233,165,222,.08);
  border-radius:16px;padding:28px 24px;
  text-decoration:none;color:var(--text);
  display:flex;flex-direction:column;gap:12px;
  transition:border-color .25s,transform .25s;
  position:relative;overflow:hidden;
}
.connect-card::before{content:'';position:absolute;top:0;left:0;right:0;height:3px;background:var(--card-color)}
.connect-card:hover{border-color:var(--pink);transform:translateY(-3px)}
.connect-icon{font-family:'Gamja Flower',cursive;font-size:1.8rem;color:var(--card-color)}
.connect-name{font-size:1rem;font-weight:700}
.connect-arrow{font-size:.85rem;color:var(--pink);margin-top:auto}

/* NEWSLETTER */
.nl-issues{display:flex;flex-direction:column;gap:12px;margin:28px 0}
.nl-issue{
  display:flex;align-items:center;gap:14px;
  background:var(--surface);border:1px solid rgba(233,165,222,.08);
  border-radius:14px;padding:18px 22px;
  text-decoration:none;color:var(--text);
  transition:border-color .2s,transform .2s;
}
.nl-issue:hover{border-color:var(--pink);transform:translateX(6px)}
.nl-issue-icon{color:var(--pink);font-size:1.1rem;flex-shrink:0}
.nl-issue-title{font-size:.92rem;font-weight:500;line-height:1.4}
.nl-issue-arrow{margin-left:auto;color:var(--pink);flex-shrink:0}

/* HIRE */
#hire{
  text-align:center;
  background:var(--surface);
  border-top:1px solid rgba(233,165,222,.1);
  border-bottom:1px solid rgba(233,165,222,.1);
}
.hire-inner{max-width:680px;margin:0 auto}
.hire-inner h2{margin-bottom:20px}
.hire-inner p{color:var(--text2);font-size:1rem;line-height:1.8;font-weight:300;margin-bottom:32px}

/* FOOTER */
footer{padding:40px 24px;text-align:center;border-top:1px solid rgba(255,255,255,.05)}
footer p{color:var(--text2);font-size:.82rem;font-weight:300}
.footer-links{display:flex;justify-content:center;gap:20px;flex-wrap:wrap;margin-top:14px}
.footer-links a{color:var(--text2);text-decoration:none;font-size:.82rem;font-weight:500;transition:color .2s}
.footer-links a:hover{color:var(--pink)}

/* RESPONSIVE NAV */
@media(max-width:640px){
  .nav-inner{overflow-x:auto;padding:0 4px;gap:2px}
  .nav a{padding:7px 12px;font-size:.75rem}
  section{padding:56px 20px 48px}
  .hero-headline{font-size:clamp(2rem,9vw,2.8rem)}
  .art-card{flex:0 0 280px;padding:20px}
  .track-section{padding:48px 0}
}

/* DIVIDER */
.divider{height:1px;background:rgba(233,165,222,.08);max-width:1150px;margin:0 auto}

/* HERO GRID */
.hero-grid{
  display:grid;grid-template-columns:1.1fr 0.9fr;
  gap:48px;align-items:center;width:100%;
}
.hero-left{display:flex;flex-direction:column;align-items:flex-start}

/* TERMINAL */
.hero-terminal{
  font-family:'Courier New',Courier,monospace;
  font-size:15px;line-height:2em;
  display:flex;flex-direction:column;gap:0;
  min-width:0;align-self:center;
}
.term-line{
  display:flex;align-items:baseline;gap:10px;
  white-space:nowrap;overflow:hidden;
}
.term-prompt{color:var(--pink);flex-shrink:0;user-select:none}
.term-text{color:#ffffff}
.term-cursor{
  display:inline-block;width:9px;height:1em;
  background:var(--pink);vertical-align:text-bottom;
  animation:blink .75s step-end infinite;
  margin-left:2px;
}

@media(max-width:900px){
  .hero-grid{grid-template-columns:1fr;gap:32px}
  .hero-terminal{font-size:13px}
  .term-line{white-space:normal;word-break:break-word}
}
</style>
</head>
<body>

<!-- NAV -->
<nav class="nav" id="nav">
  <div class="nav-inner">
    <a href="#hero">Home</a>
    <a href="#articles">Articles</a>
    <a href="#devrel">DevRel</a>
    <a href="#videos">Videos</a>
    <a href="#about">About</a>
    <a href="#connect">Connect</a>
    <a href="#newsletter">Newsletter</a>
  </div>
</nav>

<!-- HERO -->
<section id="hero" style="max-width:1200px;margin:0 auto;padding-left:max(24px,calc((100vw - 1200px)/2));padding-right:max(24px,calc((100vw - 1200px)/2))">
  <div class="hero-grid">
    <div class="hero-left">
      <div class="hero-tag">
        <span class="corner tl"></span>
        <span class="corner tr"></span>
        <span class="corner bl"></span>
        <span class="corner br"></span>
        AI/ML Technical Writer and Developer Advocate
      </div>
      <h1 class="hero-headline">
        <span class="static">I write technical content</span>
        <span class="typewriter-wrap"><span id="typewriter"></span></span>
      </h1>
      <p class="hero-sub">
        I write technical content that makes developers understand not just what a product does, but why it matters. Then I make sure they find it.
      </p>
      <div class="hero-actions">
        <a class="btn btn-primary" href="#articles">Read My Work</a>
        <a class="btn btn-outline" href="#hire">Work With Me</a>
      </div>
    </div>
    <div class="hero-terminal" id="heroTerminal"></div>
  </div>
</section>

<!-- METRICS BAR -->
<div class="metrics-bar" id="metrics">
  <div class="metrics-inner">
    <div class="metric">
      <span class="metric-num">760K+</span>
      <span class="metric-label">organic visits across 50+ articles</span>
    </div>
    <div class="metric">
      <span class="metric-num">300K+</span>
      <span class="metric-label">impressions in 3 months across LinkedIn and X</span>
    </div>
    <div class="metric">
      <span class="metric-num">500</span>
      <span class="metric-label">Mamba Brief subscribers in month one</span>
    </div>
  </div>
</div>

<!-- ARTICLES -->
<div class="track-section" id="articles">
  <div class="track-header">
    <span class="label">Published Work</span>
    <h2>Articles &amp; Tutorials</h2>
    <p style="color:var(--text2);font-size:.95rem;font-weight:300">Swipe to browse &rarr;</p>
  </div>
  <div class="h-track" id="articleTrack">
    {% for a in articles %}
    <a class="art-card" href="{{ a.url }}" target="_blank" rel="noopener">
      <span class="art-src">{{ a.source }}</span>
      <span class="art-title">{{ a.title }}</span>
      {% if a.descriptor %}<span class="art-desc">{{ a.descriptor }}</span>{% endif %}
      <div class="art-tags">{% for t in a.tags %}<span class="tag">{{ t }}</span>{% endfor %}</div>
    </a>
    {% endfor %}
  </div>
  <div class="dots" id="articleDots"></div>
  <div style="text-align:center;margin-top:28px">
    <a class="btn btn-outline" href="https://medium.com/@techwithpraisejames" target="_blank" rel="noopener">Read more on Medium &nearr;</a>
  </div>
</div>

<!-- FEATURED PROJECT -->
<section id="project" class="full-width">
  <div class="project-inner">
    <div>
      <span class="label">Featured Project</span>
      <h2>What Senior Technical Writers Know About Cross-Functional Impact</h2>
      <p style="color:var(--text2);font-size:1rem;line-height:1.8;font-weight:300;margin-top:16px">
        A community research project. I interviewed 9 senior technical writers at Google, Mastercard, Novu, and other companies to surface what the industry rarely talks about: how technical communicators drive business impact beyond documentation.
      </p>
      <p style="color:var(--text2);font-size:1rem;line-height:1.8;font-weight:300;margin-top:12px">
        The resource sparked conversation among senior practitioners on LinkedIn and reshaped how they think about the role of technical writing inside product organizations.
      </p>
    </div>
    <div class="project-quotes">
      <div class="proj-quote">
        <p>"It should be required reading for anyone who still thinks technical writing is just a finishing step. The value is invisible by design and this makes it visible."</p>
        <cite>Adrian, Senior Technical Writer</cite>
      </div>
      <div class="proj-quote">
        <p>"This made the invisible value of technical writers visible."</p>
        <cite>Kelley Bennett, Senior Technical Writer</cite>
      </div>
    </div>
  </div>
</section>

<!-- DEVREL -->
<section id="devrel">
  <span class="label">Developer Relations</span>
  <h2>Distribution is part of the work</h2>
  <p style="color:var(--text2);font-size:1rem;line-height:1.8;font-weight:300;max-width:620px">
    I don't hand off content and disappear. I get it in front of the right developers, build the communities that read it, and track what actually lands.
  </p>
  <div class="devrel-grid">
    <div class="devrel-card">
      <div class="devrel-num">300K+</div>
      <div class="devrel-title">LinkedIn and X Impressions</div>
      <div class="devrel-desc">Drove developer reach across LinkedIn and X in 3 months, distributing client content to targeted developer audiences.</div>
    </div>
    <div class="devrel-card">
      <div class="devrel-num">500</div>
      <div class="devrel-title">The Mamba Brief</div>
      <div class="devrel-desc">Launched a weekly developer content roundup. Grew to 500 subscribers in its first month.</div>
    </div>
    <div class="devrel-card">
      <div class="devrel-num">&#9679;</div>
      <div class="devrel-title">Hackmamba Creators Community</div>
      <div class="devrel-desc">Discord and community management for Hackmamba's developer author ecosystem.</div>
    </div>
    <div class="devrel-card">
      <div class="devrel-num">&#9679;</div>
      <div class="devrel-title">Off the Docs</div>
      <div class="devrel-desc">Co-hosted a technical writer interview series featuring senior practitioners including John Kunney Jr. at Mastercard and Sarah Dugan at Gitbook.</div>
    </div>
  </div>
</section>

<!-- VIDEOS -->
<div class="track-section" id="videos">
  <div class="track-header">
    <span class="label">Watch</span>
    <h2>YouTube Videos</h2>
    <p style="color:var(--text2);font-size:.95rem;font-weight:300">Swipe to watch &rarr;</p>
  </div>
  <div class="h-track" id="videoTrack">
    {% for v in videos %}
    <div class="vid-card">
      <iframe src="https://www.youtube.com/embed/{{ v.embed_id }}"
              title="YouTube video"
              allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
              allowfullscreen loading="lazy"></iframe>
    </div>
    {% endfor %}
  </div>
  <div class="dots" id="videoDots"></div>
  <div style="text-align:center;margin-top:28px">
    <a class="btn btn-outline" href="https://www.youtube.com/channel/UCwVDq2mG2FuNCRzAf-ypLvg" target="_blank" rel="noopener">See all videos &nearr;</a>
  </div>
</div>

<!-- ABOUT -->
<section id="about">
  <span class="label">About</span>
  <h2>The Story Behind the Stories</h2>
  <div class="about-grid">
    <div class="about-text">
      <p>I work with <strong>AI companies</strong> to create product-led content that engineers understand and use: technical tutorials, DevTool explainers, thought leadership, and benchmark-driven research.</p>
      <p>My background in mathematics and hands-on experience in machine learning means I understand AI at its core. But what sets me apart is <strong>storytelling</strong>. I don't simplify content by stripping out depth. I build narrative arcs around complex concepts so readers follow a clear thread from problem to solution and understand not just what a product does, but why it matters and how it fits their workflow.</p>
      <p>I also own distribution. In 3 months, I drove <strong>300,000 impressions</strong> across LinkedIn and X, putting client articles directly in front of developer audiences. I launched The Mamba Brief, a roundup of weekly developer reads, which grew to <strong>500 subscribers</strong> in its first month.</p>
      <p>The result is content that positions your product as the long-term solution in your space, and reaches the developers who need to see it. <strong style="color:var(--pink)">If you're building AI tools and need a writer who gets both the tech and the narrative, you're in the right place.</strong></p>
    </div>
    <div class="about-pills">
      <div class="about-pill">
        <h4>Technical Writing</h4>
        <p>Benchmark articles, agentic AI tutorials, architecture guides, and thought leadership for developer tool companies.</p>
      </div>
      <div class="about-pill">
        <h4>Developer Relations</h4>
        <p>Content distribution, community management, and audience building that puts your product in front of the right developers.</p>
      </div>
      <div class="about-pill">
        <h4>Domain Expertise</h4>
        <p>Mathematics background with hands-on machine learning experience. I understand AI at its core, not just at the surface.</p>
      </div>
      <div class="about-pill">
        <h4>Video and Education</h4>
        <p>YouTube channel breaking down AI and ML concepts for developers who want to understand the technology they're building with.</p>
      </div>
    </div>
  </div>
</section>

<!-- TESTIMONIALS -->
<div class="track-section" id="testimonials" style="background:var(--surface);padding-top:80px;padding-bottom:80px">
  <div class="track-header">
    <span class="label">Social Proof</span>
    <h2>What Clients Say</h2>
  </div>
  <div class="h-track" id="testimonialTrack">
    {% for t in testimonials %}
    <div class="test-card">
      <span class="test-mark">&ldquo;</span>
      <p class="test-quote">{{ t.quote }}</p>
      <div class="test-author">
        <div class="test-name">{{ t.name }}</div>
        <div class="test-role">{{ t.title }}{% if t.company %}, {{ t.company }}{% endif %}</div>
      </div>
    </div>
    {% endfor %}
  </div>
  <div class="dots" id="testimonialDots"></div>
</div>

<!-- CONNECT -->
<section id="connect">
  <span class="label">Stay Connected</span>
  <h2>Find Me Everywhere</h2>
  <div class="connect-grid">
    {% for s in socials %}
    <a class="connect-card" href="{{ s.url }}" target="_blank" rel="noopener" style="--card-color:{{ s.color }}">
      <span class="connect-icon" style="color:{{ s.color }}">{{ s.icon }}</span>
      <span class="connect-name">{{ s.name }}</span>
      <span class="connect-arrow">Visit &rarr;</span>
    </a>
    {% endfor %}
  </div>
</section>

<!-- NEWSLETTER -->
<section id="newsletter" style="background:var(--surface);padding:80px 24px;max-width:none">
  <div style="max-width:680px;margin:0 auto">
    <span class="label center">Newsletter</span>
    <h2 style="text-align:center">Tech and Storytelling</h2>
    <p style="color:var(--pink);text-align:center;font-size:.95rem;margin-bottom:8px">A weekly newsletter on the craft of technical writing</p>
    <p style="color:var(--text2);text-align:center;font-size:.9rem;font-weight:300;margin-bottom:32px;line-height:1.7">Frameworks, lessons, and behind-the-scenes insights for writers who want their content to actually matter.</p>
    <div class="nl-issues">
      {% for nl in newsletters %}
      <a class="nl-issue" href="{{ nl.url }}" target="_blank" rel="noopener">
        <span class="nl-issue-icon">&#9993;</span>
        <span class="nl-issue-title">{{ nl.title }}</span>
        <span class="nl-issue-arrow">&rarr;</span>
      </a>
      {% endfor %}
    </div>
    <div style="text-align:center;margin-top:28px">
      <a class="btn btn-primary" href="https://techwithpraisejames.substack.com/" target="_blank" rel="noopener">Subscribe to Tech and Storytelling &nearr;</a>
    </div>
  </div>
</section>

<!-- HIRE -->
<section id="hire" class="full-width" style="padding:80px 24px">
  <div class="hire-inner">
    <span class="label center">Work With Me</span>
    <h2>Let's build something developers will actually read</h2>
    <p>If you're building AI tools and need a writer who gets both the tech and the narrative and can get it in front of the right developers, let's talk.</p>
    <a class="btn btn-primary" href="mailto:techwithpraisejames@gmail.com">Get in Touch &rarr;</a>
  </div>
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
// TYPEWRITER
const phrases = [
  "that developers actually read.",
  "that drives developer reach.",
  "that builds communities.",
];
let pi = 0, ci = 0, deleting = false;
const el = document.getElementById('typewriter');

function type() {
  const current = phrases[pi];
  if (!deleting) {
    el.textContent = current.slice(0, ci + 1);
    ci++;
    if (ci === current.length) { deleting = true; setTimeout(type, 2000); return; }
  } else {
    el.textContent = current.slice(0, ci - 1);
    ci--;
    if (ci === 0) { deleting = false; pi = (pi + 1) % phrases.length; }
  }
  setTimeout(type, deleting ? 40 : 70);
}
type();

// TERMINAL
const termLines = [
  "writing for ZenRows and Actian",
  "300k+ developer eyeballs on client content",
  "shipping technical content for devtool companies",
];
const termEl = document.getElementById('heroTerminal');
let tli = 0, tci = 0;

function buildLine(index) {
  const row = document.createElement('div');
  row.className = 'term-line';
  const prompt = document.createElement('span');
  prompt.className = 'term-prompt';
  prompt.textContent = '>';
  const text = document.createElement('span');
  text.className = 'term-text';
  row.appendChild(prompt);
  row.appendChild(text);
  termEl.appendChild(row);
  return text;
}

function typeTerminal() {
  if (tli >= termLines.length) return;
  if (tci === 0) {
    const textEl = buildLine(tli);
    termEl._currentText = textEl;
    // remove cursor from previous line if any
    const prev = termEl.querySelector('.term-cursor');
    if (prev) prev.remove();
  }
  const textEl = termEl._currentText;
  textEl.textContent = termLines[tli].slice(0, tci + 1);
  tci++;
  if (tci < termLines[tli].length) {
    setTimeout(typeTerminal, 45);
  } else {
    tli++;
    tci = 0;
    if (tli < termLines.length) {
      setTimeout(typeTerminal, 280);
    } else {
      // add blinking cursor after last line
      const cursor = document.createElement('span');
      cursor.className = 'term-cursor';
      textEl.appendChild(cursor);
    }
  }
}
setTimeout(typeTerminal, 900);

// SWIPE DOTS
function setupDots(trackId, dotsId) {
  const track = document.getElementById(trackId);
  const dotsEl = document.getElementById(dotsId);
  if (!track || !dotsEl) return;
  const cards = track.children;
  if (!cards.length) return;
  for (let i = 0; i < cards.length; i++) {
    const d = document.createElement('div');
    d.className = 'dot' + (i === 0 ? ' active' : '');
    dotsEl.appendChild(d);
  }
  track.addEventListener('scroll', () => {
    const idx = Math.round(track.scrollLeft / (cards[0].offsetWidth + 20));
    dotsEl.querySelectorAll('.dot').forEach((d, i) => d.classList.toggle('active', i === idx));
  }, {passive: true});
}
setupDots('articleTrack', 'articleDots');
setupDots('videoTrack', 'videoDots');
setupDots('testimonialTrack', 'testimonialDots');

// NAV ACTIVE
const navLinks = document.querySelectorAll('.nav a');
const sectionEls = document.querySelectorAll('section[id], div[id]');
const obs = new IntersectionObserver(entries => {
  entries.forEach(e => {
    if (e.isIntersecting) {
      navLinks.forEach(l => l.classList.toggle('active', l.getAttribute('href') === '#' + e.target.id));
    }
  });
}, {threshold: 0.3});
sectionEls.forEach(s => obs.observe(s));
</script>

<script defer src="/_vercel/insights/script.js"></script>
</body>
</html>
"""


@app.route("/")
def home():
    return render_template_string(
        HTML_TEMPLATE,
        articles=ARTICLES,
        videos=VIDEOS,
        socials=SOCIALS,
        newsletters=NEWSLETTERS,
        testimonials=TESTIMONIALS,
        articles_json=_json.dumps(ARTICLES),
    )


# Vercel expects the app object
