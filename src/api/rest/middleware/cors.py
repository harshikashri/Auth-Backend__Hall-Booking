import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


DEFAULT_FRONTEND_ORIGINS = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "https://frontend-159108267686.asia-south1.run.app",
]


def _get_frontend_origins() -> list[str]:
    configured_origins = os.getenv("FRONTEND_ORIGINS", "")
    if configured_origins.strip():
        return [origin.strip() for origin in configured_origins.split(",") if origin.strip()]

    return DEFAULT_FRONTEND_ORIGINS


def add_cors_middleware(app: FastAPI) -> None:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=_get_frontend_origins(),
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
