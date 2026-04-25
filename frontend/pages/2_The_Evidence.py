import streamlit as st
from theme import inject_css, sidebar_nav, gold_divider, badge

st.set_page_config(page_title="The Evidence — FATASS TRACKER", page_icon="📊", layout="wide")

inject_css()

if not st.session_state.get("token"):
    st.switch_page("app.py")

sidebar_nav()

st.markdown("# 📊 The Evidence")
st.markdown(
    "<p style='text-align:center;color:#888;font-size:0.95rem;"
    "text-transform:uppercase;letter-spacing:2px;'>"
    "The numbers don't lie. Neither do your pants.</p>",
    unsafe_allow_html=True,
)
gold_divider()

badge("EXHIBIT C")
badge("IRREFUTABLE")

st.info("Charts coming once the backend is wired up. This page will show: weight + moving average, "
        "daily food calories, and daily exercise calories — all on one Plotly chart with toggleable series.")
