from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from src.data.repositories.userRepo import UserRepository
from src.schemas.user_schema import UserCreate


class UserService:
    def __init__(self, session: AsyncSession):
        self.user_repository = UserRepository(session)

    async def create_user(self, user: UserCreate):
        user_data = user.model_dump()
        return await self.user_repository.create_user(user_data)

    async def get_user(self, user_id):
        user = await self.user_repository.get_user_by_id(user_id)

        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"User with id {user_id} not found",
            )

        return user