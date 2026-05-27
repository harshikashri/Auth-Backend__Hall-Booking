from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str | None = None
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_HOST: str
    POSTGRES_PORT: int
    POSTGRES_DB: str
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int

    model_config = {
        "env_file": ".env"
    }


settings = Settings()