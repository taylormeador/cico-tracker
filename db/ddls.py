CREATE_USERS = """
CREATE TABLE IF NOT EXISTS users (
    id            BIGSERIAL PRIMARY KEY,
    email         TEXT        NOT NULL UNIQUE,
    password_hash TEXT        NOT NULL,
    created_at    TIMESTAMPTZ NOT NULL DEFAULT NOW()
);
"""

CREATE_WEIGHT_LOG = """
CREATE TABLE IF NOT EXISTS weight_log (
    id         BIGSERIAL PRIMARY KEY,
    user_id    BIGINT      NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    weight     NUMERIC(5,1) NOT NULL,
    timestamp  TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE INDEX IF NOT EXISTS idx_weight_log_user_ts ON weight_log(user_id, timestamp);
"""

CREATE_FOOD_LOG = """
CREATE TABLE IF NOT EXISTS food_log (
    id              BIGSERIAL PRIMARY KEY,
    user_id         BIGINT       NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    description     TEXT         NOT NULL,
    calories        INTEGER      NOT NULL,
    carb_grams      NUMERIC(6,1) NOT NULL DEFAULT 0,
    protein_grams   NUMERIC(6,1) NOT NULL DEFAULT 0,
    fat_grams       NUMERIC(6,1) NOT NULL DEFAULT 0,
    timestamp       TIMESTAMPTZ  NOT NULL DEFAULT NOW()
);

CREATE INDEX IF NOT EXISTS idx_food_log_user_ts ON food_log(user_id, timestamp);
"""

CREATE_EXERCISE_LOG = """
CREATE TABLE IF NOT EXISTS exercise_log (
    id               BIGSERIAL PRIMARY KEY,
    user_id          BIGINT      NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    description      TEXT        NOT NULL,
    calories         INTEGER     NOT NULL DEFAULT 0,
    duration_minutes INTEGER     NOT NULL DEFAULT 0,
    timestamp        TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE INDEX IF NOT EXISTS idx_exercise_log_user_ts ON exercise_log(user_id, timestamp);
"""

ALL = [
    CREATE_USERS,
    CREATE_WEIGHT_LOG,
    CREATE_FOOD_LOG,
    CREATE_EXERCISE_LOG,
]
