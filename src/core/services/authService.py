from fastapi import (
    HTTPException,
    status,
)

from sqlalchemy.ext.asyncio import AsyncSession

from src.data.repositories.userRepo import (
    UserRepository,
)

from src.utils.hash_password import (
    verify_password,
)

from src.utils.jwt import (
    create_access_token,
)


class AuthService:

    def __init__(self, session: AsyncSession):

        self.user_repository = UserRepository(session)


    async def login(
        self,
        username: str,
        password: str,
        role: str,
    ):

        user = await self.user_repository.get_user_by_name_and_role(
            username,
            role,
        )

        if not user:

            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Invalid credentials",
            )

        if not verify_password(
            password,
            user.password_hash,
        ):

            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Invalid credentials",
            )

        access_token = create_access_token(
            data={
                "user_id": str(user.id),
                "username": user.name,
                "role": user.role,
            }
        )

        return {
            "access_token": access_token,
            "token_type": "bearer",
        }