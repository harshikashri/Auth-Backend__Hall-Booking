from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL = settings.DATABASE_URL

    if DATABASE_URL is None:
        raise ValueError("DATABASE_URL is not set")

    model_config = {
        "env_file": ".env"
    }


settings = Settings()