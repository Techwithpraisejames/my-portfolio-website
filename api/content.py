"""The content model.

Edit this file to add or change work, case studies, services, insights, and
proof. No component code needs to change. Anything not yet real is a clearly
marked [ADD ...] placeholder. Never fabricate clients, metrics, or quotes.
"""

# ------------------------------------------------------------------ proof

CLIENTS = ["Actian", "Bright Data", "Zenrows", "ToolJet"]

PUBLICATIONS = ["DEV.to", "Medium", "HackerNoon", "freeCodeCamp", "Data4AI"]

# Categories used across /work and the homepage filter.
CATEGORIES = [
    "AI/ML",
    "Developer Tools",
    "Technical Tutorials",
    "Product Content",
    "Thought Leadership",
]

# ------------------------------------------------------------------ work

WORK = [
    {
        "title": "Best Apify Alternative for Large-Scale Scraping",
        "url": "https://www.zenrows.com/blog/best-apify-alternative-for-large-scale-scraping",
        "publication": "Zenrows",
        "category": "Developer Tools",
        "summary": "An original benchmark of 200 requests across 7 targets, comparing performance and cost for large-scale scraping.",
        "featured": True,
    },
    {
        "title": "Build a Stateful Web Research Agent with Zenrows and LangGraph",
        "url": "https://dev.to/zenrows/how-to-build-a-stateful-web-research-agent-with-zenrows-and-langgraph-1co7",
        "publication": "DEV.to",
        "category": "Technical Tutorials",
        "summary": "A production-grade tutorial for a stateful AI agent with retry logic and live web scraping.",
        "featured": True,
    },
    {
        "title": "Integrating Zenrows into smolagents for Production Web Access",
        "url": "https://www.zenrows.com/blog/zenrows-smolagents",
        "publication": "Zenrows",
        "category": "Technical Tutorials",
        "summary": "A step-by-step guide to swapping smolagents' default web tool for a Zenrows-powered one so AI agents can read JavaScript-rendered and bot-protected pages.",
        "featured": True,
    },
    {
        "title": "5 Edge AI Architecture Patterns for Disconnected Environments",
        "url": "https://dev.to/actiandev/5-edge-ai-architecture-patterns-for-disconnected-environments-27of",
        "publication": "Actian / DEV.to",
        "category": "AI/ML",
        "summary": "An architecture guide for running AI at the edge with no cloud connection required.",
        "featured": True,
    },
    {
        "title": "What's Changing in Vector Databases in 2026",
        "url": "https://dev.to/actiandev/whats-changing-in-vector-databases-in-2026-3pbo",
        "publication": "Actian / DEV.to",
        "category": "Thought Leadership",
        "summary": "A market analysis of the vector database landscape and where it is heading.",
        "featured": True,
    },
    {
        "title": "State of Vector Database, Q2 2026",
        "url": "https://medium.com/actian-for-developers/vector-database-news-2026-5d707384be6b",
        "publication": "Actian / Medium",
        "category": "AI/ML",
        "summary": "A roundup of the biggest vector database developments and shifts of the quarter.",
        "featured": False,
    },
    {
        "title": "A CTO's 5-Phase Roadmap to AI-Native Internal Tools",
        "url": "https://dev.to/bennykillua/a-ctos-5-phase-roadmap-to-ai-native-internal-tools-and-why-most-pilots-stall-5ea5",
        "publication": "DEV.to",
        "category": "Thought Leadership",
        "summary": "Why most AI pilot programs stall before production, and a phased plan that avoids it.",
        "featured": False,
    },
    {
        "title": "Integrating Web Data into AI Knowledge Graphs",
        "url": "https://data4ai.com/blog/use-case-deep-dives/integrating-web-data-into-ai-knowledge-graphs/",
        "publication": "Data4AI",
        "category": "Product Content",
        "summary": "A use-case deep dive on building and maintaining knowledge graphs from live web data.",
        "featured": False,
    },
    {
        "title": "Adversarial Machine Learning: Keeping Bad Actors from Compromising AI Models",
        "url": "https://hackernoon.com/adversarial-machine-learning-is-preventing-bad-actors-from-compromising-ai-models",
        "publication": "HackerNoon",
        "category": "AI/ML",
        "summary": "How attackers target machine learning models and what a real defense looks like.",
        "featured": True,
    },
    {
        "title": "Explainable AI (XAI): Making Sense of AI Decisions",
        "url": "https://medium.com/@techwithpraisejames/explainable-artificial-intelligence-xai-making-sense-of-ai-decisions-5fa655655490",
        "publication": "Medium",
        "category": "AI/ML",
        "summary": "How AI systems reach their decisions and why that transparency matters in practice.",
        "featured": False,
    },
    {
        "title": "The Cold Start Problem in Recommender Systems",
        "url": "https://www.freecodecamp.org/news/cold-start-problem-in-recommender-systems/",
        "publication": "freeCodeCamp",
        "category": "Technical Tutorials",
        "summary": "How recommender systems handle new users and items with no history to learn from.",
        "featured": False,
    },
    {
        "title": "Decision Trees in Python with scikit-learn: A Complete Guide for Beginners",
        "url": "https://medium.com/@techwithpraisejames/decision-trees-in-python-scikit-learn-a-complete-guide-for-beginners-15cb0540180f",
        "publication": "Medium",
        "category": "Technical Tutorials",
        "summary": "A beginner-friendly walkthrough of building and interpreting decision tree models.",
        "featured": False,
    },
]

# ------------------------------------------------------------------ case studies

CASE_STUDIES = [
    {
        "slug": "cross-functional-impact-research",
        "title": "What Senior Technical Writers Know About Cross-Functional Impact",
        "client": "Independent community research project",
        "service": "technical-thought-leadership",
        "summary": "Interviews with nine senior technical writers, turned into a resource on how technical communicators drive impact beyond documentation.",
        "brief": "The technical writing community talks constantly about tools and process, and rarely about business impact. The goal was a resource that made the senior-level view of the role visible to practitioners and the people who manage them.",
        "challenge": "The most valuable parts of the job, like shaping product decisions, reducing support load, and unblocking other teams, are diffuse and hard to point to. Nine practitioners meant nine different vocabularies for the same underlying work.",
        "approach": "Structured interviews with senior technical writers at companies including Google, Mastercard, and Novu. Answers were coded into recurring themes, then organized into a narrative a reader could act on rather than a transcript dump.",
        "work": "A long-form resource built around the interview findings, published and distributed to the technical writing community.",
        "outcome": "The resource sparked sustained discussion among senior practitioners on LinkedIn and shifted how several of them framed the value of the role inside their own organizations. Quantitative reach figures: [ADD VERIFIED METRIC].",
        "demonstrates": "Original research design, synthesis of many expert sources into one clear argument, and thought-leadership content that a specific professional audience engages with.",
        "quotes": [
            {
                "quote": "It should be required reading for anyone who still thinks technical writing is just a finishing step. The value is invisible by design and this makes it visible.",
                "name": "Adrian Ashley",
                "role": "Senior Technical Writer",
            },
            {
                "quote": "This made the invisible value of technical writers visible.",
                "name": "Kelley Bennett",
                "role": "Senior Technical Writer",
            },
        ],
    },
    {
        "slug": "zenrows-large-scale-scraping-benchmark",
        "title": "A Reproducible Benchmark for Large-Scale Web Scraping",
        "client": "Zenrows",
        "service": "product-led-content",
        "summary": "An original, reproducible benchmark comparing scraping platforms on performance and cost, written as a decision tool rather than a pitch.",
        "brief": "Zenrows needed a comparison piece for teams evaluating scraping infrastructure at scale: credible enough that an engineer would trust it, specific enough to act on.",
        "challenge": "Comparisons in this space are usually vague or self-serving. The piece had to define a fair methodology, run it across several real targets, and report results honestly, including where the product was not the fastest option.",
        "approach": "Ran a defined test of 200 requests across 7 target sites, compared the platforms on performance and cost, and documented the method so a reader could reproduce it.",
        "work": "A published benchmark article on the Zenrows blog, with the methodology, raw comparisons, and a clear read on which tool fits which use case.",
        "outcome": "Published as Zenrows' reference comparison for large-scale scraping, and ranks in search for \"Apify vs Zenrows\" and related evaluation queries.",
        "demonstrates": "Benchmark design, technical rigor, and product-led content that earns trust by being useful first.",
        "quotes": [
            {"quote": "Incredible as usual.", "name": "Henry", "role": "Content Marketer"},
        ],
    },
    {
        "slug": "edge-ai-architecture-patterns",
        "title": "Turning a Fragmented Topic Into Five Usable Architecture Patterns",
        "client": "Actian",
        "service": "technical-articles",
        "summary": "An architecture guide that organized the scattered field of disconnected edge AI into five named, comparable patterns engineers could design against.",
        "brief": "Actian wanted to reach engineers building AI for places where cloud connectivity cannot be assumed, like mining, offshore energy, manufacturing, and defense, and to establish authority on edge and offline-first data architecture.",
        "challenge": "Edge AI for disconnected environments is real but fragmented: the patterns are spread across separate industries and rarely named or compared. The piece had to make the space concrete without a cloud fallback to lean on, and stay useful to an architect rather than drifting into abstraction.",
        "approach": "Researched how inference and control actually run offline across those industries, then distilled the field into five distinct patterns (the Drone, the Factory, Hierarchical Federated Learning, Store-and-Forward, and the Network), each with its constraints, trade-offs, and the situations it fits.",
        "work": "A long-form architecture guide on Actian's developer blog, structured so a reader can match their own connectivity and data-sovereignty constraints to a pattern.",
        "outcome": "Published on Actian's developer blog as part of its edge and vector-data content track. Verified view and engagement figures: [ADD VERIFIED METRIC].",
        "demonstrates": "Synthesis of a fragmented topic into an original, usable framework, and architecture-level technical writing for a specialist engineering audience.",
        "quotes": [],
    },
]

# ------------------------------------------------------------------ services

SERVICES = [
    {
        "slug": "technical-articles",
        "title": "Technical Articles",
        "card": "In-depth explainers, architecture deep dives, and research-backed content for technical audiences.",
        "tagline": "Explainers and deep dives that hold up to a technical reader.",
        "what_it_is": "Long-form articles that explain a technology, an architecture, or a problem space in enough depth that an engineer learns something and a decision-maker can act. Explainers, architecture deep dives, research-backed pieces, industry analysis, and educational content.",
        "who_for": "AI and developer-focused companies that need to establish authority on a topic, teams launching something that needs explaining, and founders who want their category understood on their terms.",
        "deliverables": [
            "Explainer and \"what is\" articles",
            "Architecture and system deep dives",
            "Research-backed and benchmark-driven pieces",
            "Industry and market analysis",
            "Educational series and evergreen reference content",
        ],
        "approach": "Time spent understanding the subject before a word is written: reading the docs, running the thing, talking to the engineers. Then a structure that carries the reader from problem to understanding, not a wall of correct facts.",
        "related_categories": ["AI/ML", "Thought Leadership"],
    },
    {
        "slug": "developer-tutorials",
        "title": "Developer Tutorials",
        "card": "Step-by-step how-to guides, API walkthroughs, and integration tutorials developers can actually follow.",
        "tagline": "Tutorials a developer can follow start to finish without getting stuck.",
        "what_it_is": "Hands-on guides that take a developer from nothing to a working result. How-to guides, API tutorials, integration guides, implementation walkthroughs, and technical walkthroughs, all tested end to end.",
        "who_for": "Developer tool companies, API-first products, and platforms whose adoption depends on a smooth first integration.",
        "deliverables": [
            "How-to and getting-started guides",
            "API and SDK tutorials",
            "Integration and implementation guides",
            "End-to-end technical walkthroughs",
            "Sample projects and runnable code",
        ],
        "approach": "Every step is run in a clean environment before it ships. Code is complete and copy-pasteable, error states are named, and the reader always knows what success looks like at each stage.",
        "related_categories": ["Technical Tutorials", "Developer Tools"],
    },
    {
        "slug": "product-led-content",
        "title": "Product-Led Content",
        "card": "Technical use cases, comparison pieces, and workflow guides that show what a product does and why it matters.",
        "tagline": "Content that shows what the product does and where it fits.",
        "what_it_is": "Content that connects a product to the work a reader is trying to do. Technical use cases, product tutorials, comparison pieces, workflow guides, and solution-focused content that informs rather than sells.",
        "who_for": "Product and marketing teams at technical companies who need content that converts because it is genuinely useful, not because it is loud.",
        "deliverables": [
            "Technical use cases and solution guides",
            "Product tutorials and workflow guides",
            "Honest comparison and alternative pieces",
            "Migration and adoption guides",
            "Feature deep dives tied to real jobs to be done",
        ],
        "approach": "Start from the reader's workflow, not the feature list. Show the product in the context where it earns its place, and be straight about where it does and does not fit.",
        "related_categories": ["Product Content", "Developer Tools"],
    },
    {
        "slug": "technical-thought-leadership",
        "title": "Technical Thought Leadership",
        "card": "Founder POVs, industry analysis, and technical narratives that build credibility and category authority.",
        "tagline": "A point of view your audience takes seriously.",
        "what_it_is": "Content that carries a perspective. Founder POV pieces, technical essays, industry analysis, research interpretation, and technical narratives that position a company or a person as a voice worth listening to.",
        "who_for": "Founders, DevRel leads, and technical executives who have a point of view and need it expressed with the depth their audience expects.",
        "deliverables": [
            "Founder and executive POV pieces",
            "Technical essays and argument-driven articles",
            "Industry analysis and trend interpretation",
            "Research interpretation and commentary",
            "Narrative-driven category positioning",
        ],
        "approach": "Interview the person to find the real argument, pressure-test it, then write it so the reasoning is visible and the reader can follow how the conclusion was reached.",
        "related_categories": ["Thought Leadership", "AI/ML"],
    },
]

# ------------------------------------------------------------------ insights / newsletter

NEWSLETTER = {
    "name": "Tech & Storytelling",
    "url": "https://techwithpraisejames.substack.com/",
    "pitch": "A newsletter for technical writers who want to become better storytellers.",
}

INSIGHTS = [
    {
        "title": "The Hierarchy of Technical Content",
        "url": "https://techwithpraisejames.substack.com/p/the-hierarchy-of-technical-content",
        "category": "Craft",
        "date": "[ADD DATE]",
        "summary": "A model for ranking technical content by how much work it does for the reader.",
    },
    {
        "title": "Bridging Product and People in Technical Writing",
        "url": "https://techwithpraisejames.substack.com/p/bridging-product-and-people-in-technical",
        "category": "Craft",
        "date": "[ADD DATE]",
        "summary": "Writing that serves the product and the person using it at the same time.",
    },
    {
        "title": "The PTS Framework: Problem, Tension, Solution",
        "url": "https://techwithpraisejames.substack.com/p/the-pts-framework-problem-tension",
        "category": "Frameworks",
        "date": "[ADD DATE]",
        "summary": "A structure for technical pieces that keeps a reader moving through the argument.",
    },
    {
        "title": "The Questions You Ask Shape the Content",
        "url": "https://techwithpraisejames.substack.com/p/the-questions-you-ask-shape-the-content",
        "category": "Process",
        "date": "[ADD DATE]",
        "summary": "Why the interview and research questions decide how good the draft can be.",
    },
    {
        "title": "The 5C Framework for \"What Is\" Articles",
        "url": "https://techwithpraisejames.substack.com/p/the-5c-framework-for-what-is-articles",
        "category": "Frameworks",
        "date": "[ADD DATE]",
        "summary": "A repeatable way to write definition articles that do not read like a glossary.",
    },
]

# ------------------------------------------------------------------ testimonials

TESTIMONIALS = [
    {"quote": "Your content is the benchmark for others on the team.", "name": "Blessing", "role": "Head of Operations", "company": "Hackmamba", "visible": True},
    {"quote": "This is a strong piece. Love how technically grounded and exhaustive it is.", "name": "Henry", "role": "Head of Content", "company": "Hackmamba", "visible": True},
    {"quote": "It should be required reading for anyone who still thinks technical writing is just a finishing step. The value is invisible by design and this makes it visible.", "name": "Adrian Ashley", "role": "Senior Technical Writer", "company": "", "visible": True},
    {"quote": "Whenever I get a task of reviewing your document, it becomes one of my favourite activities. Amazing work as always.", "name": "Asjad", "role": "Developer Advocate", "company": "Hackmamba", "visible": True},
    {"quote": "You are amazing and so responsible. I will for sure ask for more of your services for other prototypes and events marketing.", "name": "Ornella", "role": "Founder and CEO", "company": "MindyMinds", "visible": True},
]

# ------------------------------------------------------------------ pillars / process

PILLARS = [
    {
        "title": "Technical depth",
        "body": "Real time spent understanding the subject before writing a word: reading the docs, running the code, talking to the engineers. Not a generalist summarizing.",
    },
    {
        "title": "Storytelling",
        "body": "Content structured so readers can follow the argument and act on it. A clear thread from problem to solution, not a wall of correct information.",
    },
    {
        "title": "Reader-first",
        "body": "Written for the person who has to use the content (integrate the API, make the call, ship the thing), not the person who assigned it.",
    },
]

PROCESS = [
    {"title": "Understand", "body": "Learn what you are building and who it is for. The content can only be as clear as the understanding behind it."},
    {"title": "Research", "body": "Read the docs, run the product, talk to your engineers. Claims get checked so you are not defending the piece later."},
    {"title": "Structure", "body": "Decide the one thing the reader should walk away with, then build the outline around that. Structure is where a piece is won or lost."},
    {"title": "Write", "body": "Draft for the reader who has to act on it. Plain sentences, complete code, no filler between the reader and the point."},
    {"title": "Refine", "body": "Edit for accuracy, flow, and length. Every round removes friction between your product and the person evaluating it."},
]

# ------------------------------------------------------------------ media / social

VIDEOS = ["NiWYwSMqETk", "iW7VrXRgg0A", "Z0yx9Pt7-rQ", "x-PyeOhqXi0", "84oDAPn7kls"]
YOUTUBE_CHANNEL = "https://www.youtube.com/channel/UCwVDq2mG2FuNCRzAf-ypLvg"

SOCIALS = [
    {"name": "LinkedIn", "url": "https://www.linkedin.com/in/praise-james-608b91284"},
    {"name": "YouTube", "url": YOUTUBE_CHANNEL},
    {"name": "Newsletter", "url": "https://techwithpraisejames.substack.com/"},
    {"name": "Medium", "url": "https://medium.com/@techwithpraisejames"},
    {"name": "GitHub", "url": "https://github.com/Techwithpraisejames"},
    {"name": "X", "url": "https://x.com/causingheadache"},
]

CONTACT_EMAIL = "techwithpraisejames@gmail.com"

# The owner's own figures. Not re-derived, not added to. Adjust values here only.
METRICS = [
    {"value": "125K+", "label": "organic views across 50+ published articles"},
    {"value": "300K+", "label": "impressions across LinkedIn and X in three months"},
    {"value": "500", "label": "newsletter subscribers in the first month"},
]

PROJECT_TYPES = [
    "Technical article",
    "Developer tutorial",
    "Product-led content",
    "Thought leadership",
    "Content strategy",
    "Other",
]


def find_service(slug: str):
    return next((s for s in SERVICES if s["slug"] == slug), None)


def find_case_study(slug: str):
    return next((c for c in CASE_STUDIES if c["slug"] == slug), None)


def featured_work(limit: int = 4):
    return [w for w in WORK if w.get("featured") and not w.get("placeholder")][:limit]


def real_work():
    return [w for w in WORK if not w.get("placeholder")]
