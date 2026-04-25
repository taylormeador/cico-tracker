# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project

`cico-tracker` is a personal-use web app (1–2 users) for tracking calories, exercise, and weight during a weight loss goal. Accessible at `fatass.taylor-meador.com` via Cloudflare tunnel to a Proxmox VM. Frontend is Streamlit (Python); backend is a Rust REST API the owner writes himself.

## Running Locally

```bash
cp .env.example .env        # fill in DB_PASSWORD and JWT_SECRET
docker compose up --build
```

Frontend: `http://localhost:8501` — Backend: `http://localhost:8080`

Streamlit only (no Docker):
```bash
cd frontend
pip install -r requirements.txt
streamlit run app.py
```

## Linting

```bash
cd frontend
ruff check .
ruff format .
```

## Architecture

```
frontend/        Streamlit multipage app
  app.py         Login/landing page (unauthenticated entry point)
  api_client.py  All HTTP calls to the Rust API
  theme.py       CSS injection + infomercial UI helpers
  pages/
    1_Log_Your_Crimes.py              Food / exercise / weight input
    2_The_Evidence.py                 Plotly charts
    3_Chronicle_of_Poor_Decisions.py  Daily timeline

backend/         Rust REST API (owner writes this)
  Dockerfile     Multi-stage Rust build

docker-compose.yml   frontend + backend + postgres:16-alpine
```

**Auth flow:** Rust API issues JWTs on login/register. Streamlit stores the token in `st.session_state["token"]` and sends it as `Authorization: Bearer <token>` on every API call. `user_id` is resolved server-side from the JWT. Each page checks `st.session_state.get("token")` and calls `st.switch_page("app.py")` if missing.

## Database Schema

```
weight_log:   id, user_id, weight (float, lbs), timestamp
food_log:     id, user_id, description, calories, carb_grams, protein_grams, fat_grams, timestamp
exercise_log: id, user_id, description, calories_burned, duration_minutes, timestamp
```

Future table (not yet built): `notes` — timestamped free-text for correlating feelings/events with health data. Intended for eventual pattern analysis ("you were tired on rides when you ate <X carbs beforehand").

## Expected API Endpoints

```
POST /auth/register     { email, password }  →  { token }
POST /auth/login        { email, password }  →  { token }

POST /food              food log entry
GET  /food?start=&end=  list entries

POST /exercise
GET  /exercise?start=&end=

POST /weight
GET  /weight?start=&end=
```

## Theme System

The UI is a late-night infomercial / hall-of-shame mashup. All CSS lives in `theme.py` (`_CSS` string). Call `inject_css()` at the top of every page.

Helper components in `theme.py`:
- `testimonial(quote, attribution)` — styled fake testimonial card
- `badge(text)` — small red/gold "AS SEEN ON TV" style label
- `urgent_box(text)` — full-width red CTA bar
- `gold_divider()` — gradient gold horizontal rule
- `ticker(text)` — scrolling red news ticker
- `star_rating(filled, total)` — gold stars
- `sidebar_nav()` — standard sidebar with logout button (call on every authenticated page)
- `hide_sidebar()` — hides sidebar entirely (call on login page)

Copy/label conventions: food log = "crimes", exercise = "redemption", weight = "face the scale", charts = "the evidence", timeline = "chronicle of poor decisions".

## Planned Features (not yet built)

- **Plotly charts** (`2_The_Evidence.py`): weight + N-day moving average, daily food calories, daily exercise calories. One chart, legend toggles per-series. Default: weight only.
- **Timeline** (`3_Chronicle_of_Poor_Decisions.py`): all events for a selected day in chronological order.
- **TDEE estimation**: linear regression over `calories_in`, `calories_burned`, and daily weight. Baseline: `TDEE ≈ avg_calories_in − (avg_daily_weight_change × 3500)`.
- **Notes table**: timestamped free-text entries visible on the timeline.

## Units

All imperial. Weight in lbs. Duration in minutes. Calories are kcal.
