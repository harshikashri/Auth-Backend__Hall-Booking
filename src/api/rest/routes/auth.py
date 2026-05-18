from fastapi import APIRouter, Depends, Form
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.services.authService import AuthService
from src.schemas.authSchema import Token
from src.api.rest.dependencies import get_db_session


router = APIRouter(prefix="/auth", tags=["Authentication"])


class OAuth2PasswordRequestFormWithRole(OAuth2PasswordRequestForm):
    def __init__(
        self,
        grant_type: str | None = Form(default=None),
        username: str = Form(),
        password: str = Form(),
        scope: str = Form(default=""),
        client_id: str | None = Form(default=None),
        client_secret: str | None = Form(default=None),
        role: str = Form(default="user"),
    ):
        super().__init__(
            grant_type=grant_type,
            username=username,
            password=password,
            scope=scope,
            client_id=client_id,
            client_secret=client_secret,
        )
        self.role = role


@router.post("/login", response_model=Token)
async def login(
    form_data: OAuth2PasswordRequestFormWithRole = Depends(),
    db: AsyncSession = Depends(get_db_session),
):
    """OAuth2 password flow login. Pass role in the `role` form field.

    Example form fields: username, password, role
    """
    auth_service = AuthService(db)

    return await auth_service.login(
        username=form_data.username,
        password=form_data.password,
        role=form_data.role,
    )


