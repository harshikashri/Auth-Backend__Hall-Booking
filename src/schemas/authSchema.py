from typing import Optional

from pydantic import BaseModel, Field


class UserLogin(BaseModel):
    username: str = Field(min_length=1, max_length=100)
    password: str
    role: str = Field(min_length=1, max_length=20)


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[str] = None
    username: Optional[str] = None
    role: Optional[str] = None