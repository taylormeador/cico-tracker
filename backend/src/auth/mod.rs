pub mod handlers;
pub mod jwt;
pub mod password;

use axum::{Router, routing::post};
use crate::AppState;

pub fn router() -> Router<AppState> {
    Router::new()
        .route("/register", post(handlers::register))
        .route("/login", post(handlers::login))
}
