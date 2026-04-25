mod auth;
mod db;
mod error;
mod models;

use axum::Router;
use dotenvy::dotenv;
use std::env;

#[derive(Clone)]
pub struct AppState {
    pub db: sqlx::PgPool,
    pub jwt_secret: String,
}

#[tokio::main]
async fn main() {
    dotenv().ok();

    let database_url = env::var("DATABASE_URL").expect("DATABASE_URL must be set");
    let jwt_secret = env::var("JWT_SECRET").expect("JWT_SECRET must be set");

    let db = db::create_pool(&database_url).await;
    println!("connected to database");

    let state = AppState { db, jwt_secret };

    let app = Router::new()
        .nest("/auth", auth::router())
        .with_state(state);

    let listener = tokio::net::TcpListener::bind("0.0.0.0:8080").await.unwrap();
    println!("listening on 0.0.0.0:8080");
    axum::serve(listener, app).await.unwrap();
}
