import streamlit as st
import api_client
from theme import (
    inject_css, hide_sidebar, testimonial, badge,
    disclaimer, urgent_box, gold_divider, star_rating, ticker,
)

st.set_page_config(
    page_title="FATASS TRACKER",
    page_icon="🍔",
    layout="wide",
    initial_sidebar_state="collapsed",
)

inject_css()
hide_sidebar()

if st.session_state.get("token"):
    st.switch_page("pages/1_Log_Your_Crimes.py")

# ── Header ────────────────────────────────────────────────────────────────────

st.markdown("# 🍔 ARE YOU A FATASS? 🍔")
st.markdown(
    "<p style='text-align:center;color:#FFD700;font-size:1.1rem;"
    "text-transform:uppercase;letter-spacing:3px;margin-top:-0.5rem;'>"
    "Finally — a solution for people just like you.</p>",
    unsafe_allow_html=True,
)

ticker("NEW LOWS EVERY DAY  ✦  RESULTS NOT GUARANTEED  ✦  SHAME INCLUDED AT NO EXTRA CHARGE  ✦  "
       "CONSULT NOBODY  ✦  YOUR SCALE DOESN'T LIE  ✦  BUT WAIT — THERE'S MORE  ✦  ")

gold_divider()

# ── Two-column layout ─────────────────────────────────────────────────────────

col_form, col_gap, col_reviews = st.columns([2, 0.3, 2])

with col_form:
    badge("LIMITED TIME OFFER")
    badge("ACT NOW")
    badge("OPERATORS STANDING BY")

    st.markdown("### Step 1: Admit You Have a Problem")

    tab_login, tab_signup = st.tabs(["I ALREADY KNOW I'M A FATASS", "FIRST TIME ADMITTING IT"])

    with tab_login:
        email = st.text_input("Email Address", placeholder="your@email.com", key="login_email")
        password = st.text_input("Password *(the only thing keeping this private)*",
                                 type="password", key="login_password")
        st.markdown("")

        if st.button("LOG IN AND FACE THE MUSIC", use_container_width=True, key="btn_login"):
            if email and password:
                try:
                    data = api_client.login(email, password)
                    st.session_state["token"] = data["token"]
                    st.session_state["email"] = email
                    st.switch_page("pages/1_Log_Your_Crimes.py")
                except api_client.APIError as e:
                    st.error(f"Login failed: {e}")
            else:
                st.error("Fill in both fields. You can't escape this that easily.")

    with tab_signup:
        new_email = st.text_input("Email Address", placeholder="your@email.com", key="reg_email")
        new_password = st.text_input("Choose a Password", type="password", key="reg_password")
        confirm = st.text_input("Confirm Password *(yes, again)*", type="password", key="reg_confirm")
        st.markdown("")

        if st.button("YES. I AM A FATASS. SIGN ME UP.", use_container_width=True, key="btn_register"):
            if not (new_email and new_password and confirm):
                st.error("All fields required. No shortcuts.")
            elif new_password != confirm:
                st.error("Passwords don't match. Much like your calorie goals.")
            else:
                try:
                    data = api_client.register(new_email, new_password)
                    st.session_state["token"] = data["token"]
                    st.session_state["email"] = new_email
                    st.switch_page("pages/1_Log_Your_Crimes.py")
                except api_client.APIError as e:
                    st.error(f"Registration failed: {e}")

with col_reviews:
    st.markdown("### What Our Sufferers Say")

    testimonial(
        "I logged my first meal and the calorie count said 'wow.' Changed my life. "
        "Not for the better, but it changed.",
        "D.W., Nashville TN"
    )

    testimonial(
        "The DAMAGE REPORT section made me realize I eat 4,000 calories a day. "
        "I thought I was being good. I was not being good.",
        "BigBoned in Birmingham, AL"
    )

    testimonial(
        "Lost 23 lbs after this app started calling me out every single day. "
        "Highly recommend if you enjoy emotional damage.",
        "T.M., Internet"
    )

    testimonial(
        "Before: sad and fat. After: sad and less fat. "
        "I cannot overstate how much this app judged me.",
        "Anonymous (it's Taylor)"
    )

    star_rating(5)
    st.markdown(
        "<div style='font-size:0.72rem;color:#888;margin-top:0.25rem;'>"
        "4.8 / 5 stars &nbsp;·&nbsp; based on 2 reviews (both by Taylor)"
        "</div>",
        unsafe_allow_html=True,
    )

gold_divider()

urgent_box("⚡ THIS IS NOT A DRILL. YOUR ARTERIES, HOWEVER, ARE. ⚡")

disclaimer(
    "* Results not typical. Individual results may vary. Taylor Meador is not a doctor, nutritionist, "
    "or responsible adult. This app will not make you attractive, popular, or happy. It will make you "
    "more aware of your choices, which is somehow worse. Side effects include: shame, mild motivation, "
    "unexpected self-awareness, and a complicated relationship with bread. "
    "Do not use while eating. Consult nobody before beginning any diet program. "
    "fatass.taylor-meador.com is not responsible for hurt feelings, broken scales, crying in the kitchen, "
    "or existential crises triggered by a pie chart of your macros."
)
