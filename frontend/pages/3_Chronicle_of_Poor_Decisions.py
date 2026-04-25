import streamlit as st
from theme import inject_css, sidebar_nav, gold_divider, badge

st.set_page_config(
    page_title="Chronicle of Poor Decisions — FATASS TRACKER",
    page_icon="💀",
    layout="wide",
)

inject_css()

if not st.session_state.get("token"):
    st.switch_page("Home.py")

sidebar_nav()

st.markdown("# 💀 Chronicle of Poor Decisions")
st.markdown(
    "<p style='text-align:center;color:#888;font-size:0.95rem;"
    "text-transform:uppercase;letter-spacing:2px;'>"
    "A minute-by-minute account of how you got here.</p>",
    unsafe_allow_html=True,
)
gold_divider()

badge("TODAY'S RECORD")

st.info("Timeline coming once the backend is wired up. This page will show all food, exercise, "
        "and weight events for a selected day in chronological order.")
