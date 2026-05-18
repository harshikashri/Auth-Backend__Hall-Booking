from fastapi import (
    APIRouter,
    Depends,
    status,
)

from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

from src.core.services.userService import UserService

from src.schemas.user_schema import (
    UserCreate,
    UserOut,
)

from src.api.rest.dependencies import get_db_session


router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    response_model=UserOut,
)
async def create_user(
    user: UserCreate,
    db: AsyncSession = Depends(get_db_session),
):

    user_service = UserService(db)

    return await user_service.create_user(user)


@router.get(
    "/{id}",
    response_model=UserOut,
)
async def get_user(
    id: UUID,
    db: AsyncSession = Depends(get_db_session),
):

    user_service = UserService(db)
    return await user_service.get_user(id)