import streamlit as st
from datetime import datetime
import api_client
from theme import inject_css, sidebar_nav, gold_divider, urgent_box, badge

st.set_page_config(page_title="Log Your Crimes — FATASS TRACKER", page_icon="🍔", layout="wide")

inject_css()

if not st.session_state.get("token"):
    st.switch_page("app.py")

sidebar_nav()

# ── Header ────────────────────────────────────────────────────────────────────

st.markdown("# ☠️ Log Your Crimes")
st.markdown(
    "<p style='text-align:center;color:#888;font-size:0.95rem;"
    "text-transform:uppercase;letter-spacing:2px;'>Confess. It's the first step.</p>",
    unsafe_allow_html=True,
)
gold_divider()

token = st.session_state["token"]
now = datetime.now()

tab_food, tab_exercise, tab_weight = st.tabs([
    "🍕  FOOD CRIMES",
    "💪  ATTEMPTED REDEMPTION",
    "⚖️  FACE THE SCALE",
])

# ── Food ──────────────────────────────────────────────────────────────────────

with tab_food:
    st.markdown("### Today's Offenses")
    badge("EXHIBIT A")

    with st.form("food_form"):
        description = st.text_input("What did you eat?", placeholder="Be specific. Own it.")
        col1, col2 = st.columns(2)
        with col1:
            calories = st.number_input("Calories", min_value=0, step=1)
            carbs = st.number_input("Carbs (g)", min_value=0.0, step=0.5)
        with col2:
            protein = st.number_input("Protein (g)", min_value=0.0, step=0.5)
            fat = st.number_input("Fat (g)", min_value=0.0, step=0.5)

        col_date, col_time = st.columns(2)
        with col_date:
            log_date = st.date_input("Date", value=now.date())
        with col_time:
            log_time = st.time_input("Time", value=now.time())

        submitted = st.form_submit_button("CONFESS THIS CRIME", use_container_width=True)

    if submitted:
        if not description:
            st.error("You have to name the crime.")
        else:
            timestamp = datetime.combine(log_date, log_time).isoformat()
            try:
                api_client.log_food(token, description, int(calories), carbs, protein, fat, timestamp)
                st.success(f"CRIME LOGGED: {description} ({int(calories)} cal). God is watching.")
            except api_client.APIError as e:
                st.error(f"Failed to log: {e}")

# ── Exercise ──────────────────────────────────────────────────────────────────

with tab_exercise:
    st.markdown("### Attempted Redemption")
    badge("EXHIBIT B")

    with st.form("exercise_form"):
        description = st.text_input("What did you do?", placeholder="This had better be good.")
        col1, col2 = st.columns(2)
        with col1:
            calories = st.number_input("Calories Burned", min_value=0, step=1)
        with col2:
            duration = st.number_input("Duration (minutes)", min_value=0, step=1)

        col_date, col_time = st.columns(2)
        with col_date:
            log_date = st.date_input("Date", value=now.date(), key="ex_date")
        with col_time:
            log_time = st.time_input("Time", value=now.time(), key="ex_time")

        submitted = st.form_submit_button("LOG MY REDEMPTION", use_container_width=True)

    if submitted:
        if not description:
            st.error("Describe what you did, hero.")
        else:
            timestamp = datetime.combine(log_date, log_time).isoformat()
            try:
                api_client.log_exercise(token, description, int(calories), int(duration), timestamp)
                st.success(f"REDEMPTION LOGGED: {description}. The scale acknowledges your effort. Barely.")
            except api_client.APIError as e:
                st.error(f"Failed to log: {e}")

# ── Weight ────────────────────────────────────────────────────────────────────

with tab_weight:
    st.markdown("### Face the Scale")
    badge("THE TRUTH")

    with st.form("weight_form"):
        weight = st.number_input("Current Weight (lbs)", min_value=0.0, step=0.1,
                                 placeholder="No rounding down.")

        col_date, col_time = st.columns(2)
        with col_date:
            log_date = st.date_input("Date", value=now.date(), key="wt_date")
        with col_time:
            log_time = st.time_input("Time", value=now.time(), key="wt_time")

        submitted = st.form_submit_button("I WEIGH WHAT I WEIGH", use_container_width=True)

    if submitted:
        if weight <= 0:
            st.error("Enter a real weight.")
        else:
            timestamp = datetime.combine(log_date, log_time).isoformat()
            try:
                api_client.log_weight(token, weight, timestamp)
                st.success(f"RECORDED: {weight} lbs. It's just a number. A number that haunts you, but still.")
            except api_client.APIError as e:
                st.error(f"Failed to log: {e}")

gold_divider()
urgent_box("REMEMBER: THE ONLY BAD WORKOUT IS THE ONE YOU DIDN'T LOG")
