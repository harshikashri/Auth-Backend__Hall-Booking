from __future__ import annotations

import hashlib
import os

from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.data.models.postgres.user import User
from src.utils.hash_password import hash_password


class UserRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    

    async def create_user(self, user_data: dict) -> User:
        user = User(
            name=user_data["name"],
            password_hash=hash_password(user_data["password"]),
            role=user_data.get("role", "user"),
        )

        self.session.add(user)
        await self.session.commit()
        await self.session.refresh(user)
        return user

    async def get_user_by_id(self, user_id: UUID) -> User | None:
        result = await self.session.execute(select(User).where(User.id == user_id))
        return result.scalar_one_or_none()

    async def get_user_by_name_and_role(self, name: str, role: str) -> User | None:
        result = await self.session.execute(
            select(User).where(User.name == name, User.role == role)
        )
        return result.scalar_one_or_none()
