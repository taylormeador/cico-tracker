use chrono::Utc;
use jsonwebtoken::{decode, encode, DecodingKey, EncodingKey, Header, Validation};
use serde::{Deserialize, Serialize};
use crate::error::AppError;

#[derive(Serialize, Deserialize)]
pub struct Claims {
    pub sub: i64,
    pub exp: i64,
}

pub fn create_token(user_id: i64, secret: &str) -> Result<String, AppError> {
    let exp = Utc::now()
        .checked_add_signed(chrono::Duration::days(30))
        .unwrap()
        .timestamp();

    encode(
        &Header::default(),
        &Claims { sub: user_id, exp },
        &EncodingKey::from_secret(secret.as_bytes()),
    )
    .map_err(|e| AppError::BadRequest(format!("token creation failed: {e}")))
}

pub fn verify_token(token: &str, secret: &str) -> Result<i64, AppError> {
    decode::<Claims>(
        token,
        &DecodingKey::from_secret(secret.as_bytes()),
        &Validation::default(),
    )
    .map(|data| data.claims.sub)
    .map_err(|_| AppError::Unauthorized)
}
