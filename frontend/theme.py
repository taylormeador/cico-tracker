import streamlit as st

_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Anton&family=Special+Elite&display=swap');

html, body, [data-testid="stAppViewContainer"] {
    font-family: 'Special Elite', serif !important;
}

h1 {
    font-family: 'Anton', sans-serif !important;
    color: #FFD700 !important;
    text-transform: uppercase !important;
    text-shadow: 3px 3px 0 #CC0000, 6px 6px 14px rgba(0,0,0,0.9) !important;
    letter-spacing: 3px !important;
    text-align: center !important;
}

h2 {
    font-family: 'Anton', sans-serif !important;
    color: #FFD700 !important;
    text-transform: uppercase !important;
    text-shadow: 2px 2px 0 #CC0000 !important;
    letter-spacing: 2px !important;
}

h3 {
    font-family: 'Anton', sans-serif !important;
    color: #FFF8DC !important;
    text-transform: uppercase !important;
    letter-spacing: 1px !important;
}

section[data-testid="stSidebar"] {
    background-color: #050200 !important;
    border-right: 3px solid #FFD700 !important;
}

section[data-testid="stSidebar"] h1,
section[data-testid="stSidebar"] h2,
section[data-testid="stSidebar"] h3 {
    text-align: left !important;
    font-size: 1rem !important;
    text-shadow: none !important;
    letter-spacing: 1px !important;
}

div.stButton > button {
    background-color: #CC0000 !important;
    color: #FFD700 !important;
    font-family: 'Anton', sans-serif !important;
    font-size: 0.9rem !important;
    text-transform: uppercase !important;
    border: 2px solid #FFD700 !important;
    letter-spacing: 2px !important;
    border-radius: 0 !important;
    transition: all 0.15s ease !important;
}

div.stButton > button:hover {
    background-color: #FFD700 !important;
    color: #CC0000 !important;
    border-color: #CC0000 !important;
    box-shadow: 0 0 14px rgba(255,215,0,0.4) !important;
}

div.stButton > button:active {
    transform: scale(0.98) !important;
}

div.stTextInput > div > div > input,
div.stNumberInput > div > div > input,
div.stTextArea > div > div > textarea {
    background-color: #1a0500 !important;
    color: #FFF8DC !important;
    border: 1px solid #FFD700 !important;
    border-radius: 0 !important;
    font-family: 'Special Elite', serif !important;
}

div.stTextInput > label,
div.stNumberInput > label,
div.stTextArea > label,
div.stSelectbox > label,
div.stDateInput > label,
div.stTimeInput > label {
    color: #FFF8DC !important;
    font-family: 'Special Elite', serif !important;
}

div.stSelectbox > div > div {
    background-color: #1a0500 !important;
    color: #FFF8DC !important;
    border: 1px solid #FFD700 !important;
    border-radius: 0 !important;
}

div.stTabs [role="tab"] {
    font-family: 'Anton', sans-serif !important;
    font-size: 0.8rem !important;
    letter-spacing: 1px !important;
    text-transform: uppercase !important;
    color: #888 !important;
}

div.stTabs [role="tab"][aria-selected="true"] {
    color: #FFD700 !important;
    border-bottom: 2px solid #FFD700 !important;
}

div[data-testid="metric-container"] {
    background-color: #1a0500 !important;
    border: 1px solid #FFD700 !important;
    border-radius: 0 !important;
    padding: 1rem !important;
}

div[data-testid="stMetricLabel"] {
    color: #FFF8DC !important;
    font-family: 'Special Elite', serif !important;
    text-transform: uppercase !important;
    letter-spacing: 1px !important;
}

div[data-testid="stMetricValue"] {
    color: #FFD700 !important;
    font-family: 'Anton', sans-serif !important;
}

.testimonial {
    background: #120300;
    border: 1px solid rgba(255,215,0,0.3);
    border-left: 4px solid #CC0000;
    padding: 1rem 1.25rem 0.85rem;
    margin: 0.75rem 0;
}

.testimonial p {
    font-style: italic;
    color: #FFF8DC;
    margin: 0 0 0.5rem 0;
    font-size: 0.9rem;
    line-height: 1.6;
    font-family: 'Special Elite', serif;
}

.testimonial .attr {
    color: #FFD700;
    font-size: 0.7rem;
    text-transform: uppercase;
    letter-spacing: 1.5px;
    font-family: 'Special Elite', serif;
}

.info-badge {
    display: inline-block;
    background: #CC0000;
    color: #FFD700;
    font-family: 'Anton', sans-serif;
    font-size: 0.62rem;
    text-transform: uppercase;
    padding: 0.2rem 0.7rem;
    letter-spacing: 2px;
    margin: 0 0.2rem 0.4rem;
    vertical-align: middle;
}

.urgent-box {
    background: linear-gradient(135deg, #8B0000, #CC0000);
    border: 2px solid #FFD700;
    padding: 1rem 1.5rem;
    text-align: center;
    margin: 1.5rem 0;
}

.urgent-box p {
    color: #FFD700;
    font-family: 'Anton', sans-serif;
    font-size: 1.05rem;
    text-transform: uppercase;
    letter-spacing: 3px;
    margin: 0;
    text-shadow: 1px 1px 4px rgba(0,0,0,0.6);
}

.gold-rule {
    border: none;
    height: 2px;
    background: linear-gradient(to right, transparent, #FFD700, transparent);
    margin: 1.5rem 0;
    opacity: 0.6;
}

.small-print {
    font-size: 0.55rem;
    color: #444;
    text-align: center;
    line-height: 1.8;
    max-width: 720px;
    margin: 2rem auto 0;
    font-family: 'Special Elite', serif;
}

.star-rating {
    color: #FFD700;
    font-size: 1rem;
    letter-spacing: 3px;
    margin: 0.25rem 0;
}

.ticker-wrap {
    overflow: hidden;
    background: #CC0000;
    border-top: 1px solid #FFD700;
    border-bottom: 1px solid #FFD700;
    padding: 0.4rem 0;
    margin: 1rem 0;
}

.ticker {
    display: inline-block;
    white-space: nowrap;
    animation: ticker-scroll 28s linear infinite;
    color: #FFD700;
    font-family: 'Anton', sans-serif;
    font-size: 0.75rem;
    letter-spacing: 4px;
    text-transform: uppercase;
}

@keyframes ticker-scroll {
    0%   { transform: translateX(100vw); }
    100% { transform: translateX(-100%); }
}
</style>
"""

_HIDE_SIDEBAR_CSS = """
<style>
section[data-testid="stSidebarNav"] { display: none !important; }
[data-testid="collapsedControl"]     { display: none !important; }
</style>
"""


def inject_css():
    st.markdown(_CSS, unsafe_allow_html=True)


def hide_sidebar():
    st.markdown(_HIDE_SIDEBAR_CSS, unsafe_allow_html=True)


def sidebar_nav():
    with st.sidebar:
        st.markdown("## 🍔 FATASS TRACKER")
        gold_divider()
        if "email" in st.session_state:
            st.markdown(
                f"<div style='color:#888;font-size:0.75rem;'>Logged in as:</div>"
                f"<div style='color:#FFD700;font-size:0.8rem;margin-bottom:1rem;'>{st.session_state['email']}</div>",
                unsafe_allow_html=True,
            )
        if st.button("SIGN OUT", use_container_width=True):
            st.session_state.clear()
            st.switch_page("app.py")


def testimonial(quote: str, attribution: str):
    st.markdown(
        f'<div class="testimonial"><p>"{quote}"</p>'
        f'<div class="attr">— {attribution}</div></div>',
        unsafe_allow_html=True,
    )


def badge(text: str):
    st.markdown(f'<span class="info-badge">{text}</span>', unsafe_allow_html=True)


def disclaimer(text: str):
    st.markdown(f'<div class="small-print">{text}</div>', unsafe_allow_html=True)


def urgent_box(text: str):
    st.markdown(f'<div class="urgent-box"><p>{text}</p></div>', unsafe_allow_html=True)


def gold_divider():
    st.markdown('<hr class="gold-rule">', unsafe_allow_html=True)


def star_rating(filled: int = 5, total: int = 5):
    stars = "★" * filled + "☆" * (total - filled)
    st.markdown(f'<div class="star-rating">{stars}</div>', unsafe_allow_html=True)


def ticker(text: str):
    st.markdown(
        f'<div class="ticker-wrap"><span class="ticker">{text}</span></div>',
        unsafe_allow_html=True,
    )
