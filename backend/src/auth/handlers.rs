use axum::{Json, extract::State};
use serde::{Deserialize, Serialize};
use crate::{AppState, error::AppError, models::user::User};
use super::{jwt, password};

#[derive(Deserialize)]
pub struct AuthRequest {
    email: String,
    password: String,
}

#[derive(Serialize)]
pub struct AuthResponse {
    token: String,
}

pub async fn register(
    State(state): State<AppState>,
    Json(body): Json<AuthRequest>,
) -> Result<Json<AuthResponse>, AppError> {
    let existing = sqlx::query_as::<_, User>(
        "SELECT id, email, password_hash, created_at FROM users WHERE email = $1",
    )
    .bind(&body.email)
    .fetch_optional(&state.db)
    .await?;

    if existing.is_some() {
        return Err(AppError::Conflict("email already in use".to_string()));
    }

    let hash = password::hash(&body.password)?;

    let user = sqlx::query_as::<_, User>(
        "INSERT INTO users (email, password_hash) VALUES ($1, $2)
         RETURNING id, email, password_hash, created_at",
    )
    .bind(&body.email)
    .bind(&hash)
    .fetch_one(&state.db)
    .await?;

    let token = jwt::create_token(user.id, &state.jwt_secret)?;
    Ok(Json(AuthResponse { token }))
}

pub async fn login(
    State(state): State<AppState>,
    Json(body): Json<AuthRequest>,
) -> Result<Json<AuthResponse>, AppError> {
    let user = sqlx::query_as::<_, User>(
        "SELECT id, email, password_hash, created_at FROM users WHERE email = $1",
    )
    .bind(&body.email)
    .fetch_optional(&state.db)
    .await?
    .ok_or(AppError::Unauthorized)?;

    if !password::verify(&body.password, &user.password_hash) {
        return Err(AppError::Unauthorized);
    }

    let token = jwt::create_token(user.id, &state.jwt_secret)?;
    Ok(Json(AuthResponse { token }))
}
