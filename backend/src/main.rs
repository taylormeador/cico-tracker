use axum::{routing::get, Router};
use sqlx::{PgPool, postgres::PgPoolOptions};
use dotenvy::dotenv;
use std::env;

#[derive(Debug)]
struct User {
    id: i64,
    email: String,
    password_hash: String,
    created_at: chrono::DateTime<chrono::Utc>,
}

async fn get_users(pool: &PgPool) -> Result<Vec<User>, sqlx::Error> {
    let users = sqlx::query_as!(
        User,
        r#"SELECT id, email, password_hash, created_at FROM users"#
    )
    .fetch_all(pool)
    .await?;

    Ok(users)
}

#[tokio::main]
async fn main() {
    dotenv().ok();
    println!("welcome to CICO backend");

    let database_url = env::var("DATABASE_URL").expect("DATABASE_URL must be set");
    let pool = PgPoolOptions::new()
        .connect(&database_url)
        .await
        .expect("failed to connect to database");

    println!("connected to database");

    let app = Router::new()
        .route("/", get(|| async { "Hello, World!" }))
        .with_state(pool);

    let listener = tokio::net::TcpListener::bind("0.0.0.0:8080").await.unwrap();
    axum::serve(listener, app).await.unwrap();
}
