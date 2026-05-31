from typing import Optional
from pydantic import computed_field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # --- Base de datos PostgreSQL ---
    postgres_user:     str = "postgres"
    postgres_password: str = "postgres"
    postgres_db:       str = "foodstore_simple"
    postgres_host:     str = "localhost"
    postgres_port:     int = 5432

    @computed_field
    @property
    def DATABASE_URL(self) -> str:
        return (
            f"postgresql+psycopg2://{self.postgres_user}:{self.postgres_password}"
            f"@{self.postgres_host}:{self.postgres_port}/{self.postgres_db}"
        )

    # --- MercadoPago ---
    MP_ACCESS_TOKEN:  Optional[str] = None
    MP_PUBLIC_KEY:    Optional[str] = None
    MP_WEBHOOK_URL:   Optional[str] = None
    NGROK_URL:        Optional[str] = None

    # --- CORS ---
    CORS_ORIGINS:       str = "http://localhost:5173"
    VITE_FRONTEND_URL:  str = "http://localhost:5173"
    VITE_API_URL:       str = "http://localhost:8000"

    model_config = {
        "env_file":          ".env",
        "env_file_encoding": "utf-8",
        "extra":             "ignore",
    }


settings = Settings()
