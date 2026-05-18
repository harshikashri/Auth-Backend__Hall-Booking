from fastapi import (
    APIRouter,
    Depends,
)

from sqlalchemy.ext.asyncio import AsyncSession

from src.core.services.authService import (
    AuthService,
)

from src.schemas.authSchema import (
    Token,
    UserLogin,
)

from src.api.rest.dependencies import (
    get_db_session,
)


router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)


@router.post(
    "/login",
    response_model=Token,
)
async def login(
    payload: UserLogin,
    db: AsyncSession = Depends(get_db_session),
):

    auth_service = AuthService(db)

    return await auth_service.login(
        username=payload.username,
        password=payload.password,
        role=payload.role,
    )


