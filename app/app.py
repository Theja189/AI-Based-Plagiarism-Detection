
import streamlit as st

st.set_page_config(
    page_title="AI-Based Plagiarism Detection System",
    page_icon="📘",
    layout="wide",
    initial_sidebar_state="collapsed",
)

from components.sidebar import render_sidebar

render_sidebar("Dashboard")

# =========================================================
# CSS
# =========================================================
st.html("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

:root {
    --navy: #092343;
    --blue: #1677f8;
    --cyan: #36c5f0;
    --text: #102b4e;
    --muted: #58708e;
}

.stApp {
    background: linear-gradient(135deg, #f8fbff, #eef5fc);
    color: var(--text);
    font-family: Inter, Arial, sans-serif;
}

[data-testid="stHeader"] {
    background: transparent;
}

[data-testid="stMain"] {
    background: transparent;
}

.block-container {
    max-width: 1450px;
    padding-top: 0.7rem;
    padding-bottom: 2rem;
}

[data-testid="collapsedControl"] {
    display: none;
}

/* HEADER */
.site-header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    flex-wrap: wrap;
    gap: 20px;
    padding: 8px 10px 15px;
    margin-bottom: 12px;
    border-bottom: 1px solid #e4edf7;
}

.logo {
    display: flex;
    align-items: center;
    gap: 12px;
    color: #0a2548;
    font-size: 1.15rem;
    font-weight: 800;
    letter-spacing: -0.5px;
}

.logo-icon {
    font-size: 34px;
    line-height: 1;
}

.nav-menu {
    display: flex;
    align-items: center;
    flex-wrap: wrap;
    gap: 9px;
}

.nav-item {
    color: #415a79;
    text-decoration: none;
    font-size: 0.82rem;
    font-weight: 600;
    padding: 10px 14px;
    border-radius: 10px;
}

.nav-item:hover,
.nav-item.active {
    color: #0875f5;
    background: #e7f1ff;
}

/* HERO BANNER */
.hero {
    position: relative;
    overflow: hidden;
    display: grid;
    grid-template-columns: 1.05fr 0.95fr;
    align-items: center;
    gap: 24px;
    min-height: 340px;
    padding: 36px 46px;
    margin: 0 0 26px;
    border-radius: 16px;
    color: white;
    background:
        radial-gradient(circle at 80% 20%, rgba(23, 133, 217, .38), transparent 35%),
        linear-gradient(112deg, #071a34 0%, #0b3158 54%, #12669c 100%);
    box-shadow: 0 20px 42px rgba(12, 48, 87, .15);
}

.hero:before {
    content: "";
    position: absolute;
    inset: 0;
    opacity: .16;
    background-image:
        linear-gradient(rgba(130, 205, 255, .2) 1px, transparent 1px),
        linear-gradient(90deg, rgba(130, 205, 255, .2) 1px, transparent 1px);
    background-size: 32px 32px;
    pointer-events: none;
}

.hero-copy, .hero-art {
    position: relative;
    z-index: 1;
}

.eyebrow {
    color: #c5e7ff;
    font-size: .68rem;
    font-weight: 800;
    letter-spacing: 2.2px;
    margin-bottom: 18px;
}

.hero h1 {
    color: #fff;
    font-size: clamp(2rem, 3.2vw, 3rem);
    line-height: 1.12;
    letter-spacing: -1.5px;
    font-weight: 800;
    margin: 0 0 18px;
}

.hero h1 span {
    color: #39c5f4;
}

.hero-description {
    color: #e0edfa;
    font-size: .92rem;
    line-height: 1.8;
    max-width: 570px;
    margin-bottom: 21px;
}

.hero-actions {
    display: flex;
    flex-wrap: wrap;
    gap: 13px;
}

.hero-button {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    gap: 10px;
    color: white;
    text-decoration: none;
    font-size: .82rem;
    font-weight: 700;
    padding: 13px 21px;
    border-radius: 10px;
    border: 1px solid rgba(255,255,255,.45);
}

.hero-button.primary {
    background: linear-gradient(110deg, #3478ff, #18a5f4);
    border-color: #54b9ff;
    box-shadow: 0 6px 18px rgba(0, 119, 255, .3);
}

.hero-button.secondary {
    background: rgba(4, 25, 49, .38);
}

.hero-button:hover {
    filter: brightness(1.12);
}

/* AI ILLUSTRATION */
.hero-art {
    min-height: 250px;
    display: flex;
    align-items: center;
    justify-content: center;
}

.ai-glow {
    position: absolute;
    width: 260px;
    height: 190px;
    border-radius: 50%;
    background: rgba(0, 125, 255, .2);
    filter: blur(35px);
}

.ai-badge {
    position: absolute;
    top: 0;
    left: 48%;
    transform: translateX(-50%);
    width: 58px;
    height: 58px;
    display: flex;
    align-items: center;
    justify-content: center;
    color: white;
    font-size: 1.5rem;
    font-weight: 800;
    border-radius: 12px;
    background: linear-gradient(135deg, #347bff, #1646a5);
    border: 1px solid #64c7ff;
    box-shadow: 0 0 28px rgba(29, 145, 255, .6);
    z-index: 3;
}

.paper {
    position: absolute;
    top: 72px;
    width: 35%;
    min-height: 170px;
    padding: 15px 13px;
    border-radius: 12px;
    background: linear-gradient(145deg, #ffffff, #dcecff);
    border: 1px solid #b8d8ff;
    box-shadow: 0 12px 28px rgba(0,0,0,.18);
    color: #16395e;
}

.paper.left {
    left: 2%;
}

.paper.right {
    right: 1%;
}

.paper-title {
    font-size: .62rem;
    font-weight: 800;
    margin-bottom: 13px;
    white-space: nowrap;
}

.line {
    height: 9px;
    background: #d2e0f2;
    border-radius: 4px;
    margin: 7px 0;
}

.line.short {
    width: 58%;
}

.line.medium {
    width: 78%;
}

.line.match {
    background: #ffaaaa;
    width: 83%;
}

.score-card {
    position: absolute;
    top: 100px;
    left: 50%;
    transform: translateX(-50%);
    width: 135px;
    padding: 13px 10px;
    text-align: center;
    border: 1px solid #d0e5ff;
    border-radius: 12px;
    background: #ffffff;
    color: #102b4e;
    box-shadow: 0 10px 25px rgba(0,0,0,.15);
    z-index: 2;
}

.score-label {
    font-size: .62rem;
    font-weight: 800;
    margin-bottom: 8px;
}

.score-circle {
    width: 78px;
    height: 78px;
    margin: 0 auto;
    display: flex;
    align-items: center;
    justify-content: center;
    border-radius: 50%;
    background: conic-gradient(#ff6268 0 68%, #d8e4f3 68% 100%);
    position: relative;
    font-size: 1.2rem;
    font-weight: 800;
}

.score-circle:before {
    content: "";
    position: absolute;
    width: 59px;
    height: 59px;
    border-radius: 50%;
    background: white;
}

.score-circle span {
    position: relative;
    z-index: 1;
}

.match-label {
    position: absolute;
    left: 50%;
    bottom: 1px;
    transform: translateX(-50%);
    white-space: nowrap;
    color: #c92d3b;
    background: #ffe8e9;
    border-radius: 7px;
    padding: 7px 10px;
    font-size: .61rem;
    font-weight: 800;
    z-index: 4;
}

/* SECTION TITLES */
.section-heading {
    color: #0b294d;
    font-size: 1.55rem;
    line-height: 1.3;
    font-weight: 800;
    letter-spacing: -.7px;
    margin: 0 0 5px;
}

.section-description {
    color: #5e7491;
    font-size: .84rem;
    margin: 0 0 18px;
}

/* FEATURE CARDS */
.feature-card {
    display: flex;
    align-items: flex-start;
    gap: 17px;
    min-height: 105px;
    height: 100%;
    padding: 18px;
    border-radius: 13px;
    background: #ffffff;
    border: 1px solid #e2ebf5;
    box-shadow: 0 6px 18px rgba(23, 56, 91, .055);
    box-sizing: border-box;
    transition: transform .2s ease, box-shadow .2s ease;
}

.feature-card:hover {
    transform: translateY(-3px);
    box-shadow: 0 12px 25px rgba(23, 56, 91, .1);
}

.feature-icon {
    flex: 0 0 54px;
    width: 54px;
    height: 54px;
    display: flex;
    align-items: center;
    justify-content: center;
    border-radius: 12px;
    font-size: 1.55rem;
}

.icon-blue {
    color: #147dff;
    background: #e5f1ff;
}

.icon-purple {
    color: #7452ff;
    background: #f0eaff;
}

.icon-green {
    color: #0aa86b;
    background: #dff8ed;
}

.feature-content {
    flex: 1;
}

.feature-content h3 {
    color: #102b4e;
    font-size: .9rem;
    font-weight: 800;
    margin: 3px 0 7px;
}

.feature-content p {
    color: #5c7290;
    font-size: .78rem;
    line-height: 1.65;
    margin: 0;
}

.feature-arrow {
    color: #ffffff;
    width: 23px;
    height: 23px;
    flex: 0 0 23px;
    display: flex;
    align-items: center;
    justify-content: center;
    border-radius: 50%;
    margin-top: 5px;
    background: #2389ff;
    font-size: .9rem;
    font-weight: 800;
}

/* WORKFLOW */
.workflow-card {
    display: flex;
    align-items: flex-start;
    gap: 17px;
    min-height: 112px;
    padding: 18px;
    border-radius: 13px;
    background: #ffffff;
    border: 1px solid #e2ebf5;
    box-shadow: 0 6px 18px rgba(23, 56, 91, .05);
    box-sizing: border-box;
}

.step-circle {
    flex: 0 0 58px;
    width: 58px;
    height: 58px;
    display: flex;
    align-items: center;
    justify-content: center;
    border-radius: 50%;
    font-size: 1.25rem;
    font-weight: 800;
}

.step-blue {
    color: #147dff;
    background: #e1efff;
}

.step-purple {
    color: #7452ff;
    background: #eee8ff;
}

.step-green {
    color: #0aa86b;
    background: #ddf7eb;
}

.workflow-content h3 {
    color: #102b4e;
    font-size: .88rem;
    font-weight: 800;
    margin: 3px 0 6px;
}

.workflow-content p {
    color: #5c7290;
    font-size: .78rem;
    line-height: 1.65;
    margin: 0;
}

.flow-arrow {
    display: flex;
    align-items: center;
    justify-content: center;
    height: 112px;
    color: #b2c3d8;
    font-size: 2rem;
    font-weight: 400;
}

/* INFORMATION BANNER */
.info-banner {
    display: flex;
    align-items: flex-start;
    gap: 12px;
    padding: 13px 17px;
    margin: 17px 0 15px;
    border-radius: 11px;
    border: 1px solid #c7e0ff;
    background: linear-gradient(100deg, #e0efff, #d6e9ff);
    color: #1768d5;
    font-size: .77rem;
    line-height: 1.65;
}

.info-icon {
    font-size: 1.1rem;
}

/* FOOTER CTA */
.footer-cta {
    margin-top: 15px;
}

.stButton > button {
    min-height: 45px;
    border-radius: 10px;
    font-family: Inter, Arial, sans-serif;
    font-weight: 700;
    transition: all .2s ease;
}

.stButton > button[kind="primary"] {
    color: white;
    background: linear-gradient(105deg, #10365b, #124b79);
    border: 1px solid #1b527f;
    box-shadow: 0 7px 18px rgba(10, 45, 80, .14);
}

.stButton > button[kind="primary"]:hover {
    color: white;
    background: linear-gradient(105deg, #155080, #1674ad);
    border-color: #49a7e9;
    transform: translateY(-1px);
}

.footer {
    text-align: center;
    color: #607795;
    font-size: .75rem;
    padding: 15px 0 0;
}

/* RESPONSIVE */
@media (max-width: 900px) {
    .hero {
        grid-template-columns: 1fr;
        padding: 32px 27px;
    }

    .hero-art {
        min-height: 270px;
    }

    .nav-menu {
        gap: 3px;
    }

    .nav-item {
        padding: 8px;
    }
}

@media (max-width: 600px) {
    .block-container {
        padding: .8rem;
    }

    .hero {
        padding: 25px 20px;
    }

    .hero h1 {
        font-size: 2.1rem;
    }

    .hero-art {
        transform: scale(.9);
        margin: -5px -15px;
    }

    .feature-card {
        min-height: auto;
    }

    .workflow-card {
        min-height: auto;
    }
}
/* Hide Streamlit sidebar completely */
[data-testid="stSidebar"] {
    display: none !important;
    width: 0 !important;
}

[data-testid="stSidebarCollapsedControl"] {
    display: none !important;
}

[data-testid="collapsedControl"] {
    display: none !important;
}
</style>
""")

# =========================================================
# HEADER
# =========================================================
st.html("""
<header class="site-header">
    <div class="logo">
        <span class="logo-icon">📖</span>
        <span>Plagiarism Checker</span>
    </div>

    <nav class="nav-menu">
        <a class="nav-item active" href="#home">⌂ &nbsp; Home</a>
        <a class="nav-item" href="#detect">▣ &nbsp; Detect Plagiarism</a>
        <a class="nav-item" href="#about">● &nbsp; About</a>
        <a class="nav-item" href="#help">? &nbsp; Help</a>
    </nav>
</header>
""")

# =========================================================
# HERO BANNER
# =========================================================
st.html("""
<section class="hero" id="home">
    <div class="hero-copy">
        <div class="eyebrow">
            ACADEMIC INTEGRITY &nbsp; · &nbsp; INTELLIGENT ANALYSIS
        </div>

        <h1>
            AI-Based Plagiarism<br>
            <span>Detection System</span>
        </h1>

        <p class="hero-description">
            Analyze academic text, compare documents, and identify
            potentially similar passages using text preprocessing,
            feature extraction, and machine learning techniques.
        </p>

        <div class="hero-actions">
            <a class="hero-button primary" href="#detect">
                Get Started &nbsp; → 
            </a>
            <a class="hero-button secondary" href="#about">
                Learn More
            </a>
        </div>
    </div>

    <div class="hero-art">
        <div class="ai-glow"></div>
        <div class="ai-badge">AI</div>

        <div class="paper left">
            <div class="paper-title">📄 &nbsp; Original Document</div>
            <div class="line medium"></div>
            <div class="line"></div>
            <div class="line medium"></div>
            <div class="line"></div>
            <div class="line short"></div>
            <div class="line medium"></div>
            <div class="line short"></div>
        </div>

        <div class="paper right">
            <div class="paper-title">📄 &nbsp; Compared Document</div>
            <div class="line medium"></div>
            <div class="line match"></div>
            <div class="line"></div>
            <div class="line match"></div>
            <div class="line medium"></div>
            <div class="line match"></div>
            <div class="line short"></div>
        </div>

        <div class="score-card">
            <div class="score-label">Similarity Score</div>
            <div class="score-circle"><span>68%</span></div>
        </div>

        <div class="match-label">⚠ Potential Match Found</div>
    </div>
</section>
""")

# =========================================================
# PLATFORM FEATURES
# =========================================================
st.html("""
<div class="section-heading" id="about">Explore the Platform</div>
<div class="section-description">
    Tools to help analyze and compare academic documents.
</div>
""")

feature_columns = st.columns(3, gap="medium")

features = [
    (
        "📄",
        "icon-blue",
        "Document Analysis",
        "Work with TXT, PDF, and DOCX documents or enter text directly for comparison.",
        "feature-blue",
    ),
    (
        "⌕",
        "icon-purple",
        "Similarity Detection",
        "Compare document content using TF-IDF features and cosine similarity.",
        "feature-purple",
    ),
    (
        "▥",
        "icon-green",
        "Analysis Results",
        "Review similarity scores, potential matching patterns, and analysis limitations.",
        "feature-green",
    ),
]

for column, feature in zip(feature_columns, features):
    icon, icon_class, title, description, _ = feature

    with column:
        st.html(f"""
        <div class="feature-card">
            <div class="feature-icon {icon_class}">{icon}</div>
            <div class="feature-content">
                <h3>{title}</h3>
                <p>{description}</p>
            </div>
            <div class="feature-arrow">→</div>
        </div>
        """)

st.write("")

# =========================================================
# HOW IT WORKS
# =========================================================
st.html("""
<div class="section-heading">How It Works</div>
<div class="section-description">
    The system follows three main steps to compare academic content.
</div>
""")

workflow_columns = st.columns([1, 0.12, 1, 0.12, 1], gap="small")

workflow = [
    (
        "01",
        "step-blue",
        "Upload Documents",
        "Upload supported documents or enter the text you want to compare.",
    ),
    (
        "02",
        "step-purple",
        "Analyze Text",
        "Extract and preprocess text, then calculate similarity between the provided documents.",
    ),
    (
        "03",
        "step-green",
        "Review Results",
        "Examine similarity scores and review potentially matching content.",
    ),
]

for index, (number, color, title, description) in enumerate(workflow):
    col_index = index * 2

    with workflow_columns[col_index]:
        st.html(f"""
        <div class="workflow-card">
            <div class="step-circle {color}">{number}</div>
            <div class="workflow-content">
                <h3>{title}</h3>
                <p>{description}</p>
            </div>
        </div>
        """)

    if index < 2:
        with workflow_columns[col_index + 1]:
            st.html('<div class="flow-arrow">→</div>')

# =========================================================
# RESPONSIBLE USE
# =========================================================
st.html("""
<div class="info-banner" id="help">
    <div class="info-icon">🔵</div>
    <div>
        <strong>Important:</strong>
        A similarity score is an indicator for review, not proof of plagiarism.
        This prototype compares the documents you provide; it does not scan the
        entire internet or every academic database. Results should be interpreted
        with human review.
    </div>
</div>
""")

# =========================================================
# BOTTOM GET STARTED BUTTON
# =========================================================
st.html('<div class="footer-cta" id="detect"></div>')

if st.button(
    "Get Started     →",
    type="primary",
    use_container_width=True,
    key="bottom_get_started",
):
    st.switch_page("pages/1_Detect_Plagiarism.py")

# =========================================================
# FOOTER
# =========================================================
st.html("""
<div class="footer">
    AI-Based Plagiarism Detection System &nbsp;•&nbsp;
    Academic Project Prototype
</div>
""")
