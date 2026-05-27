from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager

from src.data.models.postgres.base import Base

from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from src.config.settings import settings


DATABASE_URL = settings.DATABASE_URL

if DATABASE_URL is None:
    raise ValueError("DATABASE_URL is not set")


_engine: AsyncEngine | None = None


def get_or_create_engine() -> AsyncEngine:

    global _engine

    if _engine is None:

        _engine = create_async_engine(
            DATABASE_URL,

            pool_size=10,
            max_overflow=10,
            pool_timeout=10,
            pool_recycle=3600,
            pool_pre_ping=True,

            connect_args={
                "timeout": 180,
                "command_timeout": 2400,
                "server_settings": {
                    "statement_timeout": "2400000",
                },
            },

            echo=True,
        )

    return _engine


def get_session_factory() -> async_sessionmaker[AsyncSession]:

    return async_sessionmaker(
        bind=get_or_create_engine(),
        class_=AsyncSession,
        autocommit=False,
        autoflush=False,
        expire_on_commit=False,
    )