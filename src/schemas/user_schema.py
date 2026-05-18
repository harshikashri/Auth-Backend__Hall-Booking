from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field


class UserCreate(BaseModel):
	name: str = Field(min_length=1, max_length=100)
	password: str
	role: str = Field(default="user", min_length=1, max_length=20)


class UserOut(BaseModel):
	model_config = ConfigDict(from_attributes=True)

	id: UUID
	name: str
	role: str
	is_active: bool
	created_at: datetime
	updated_at: datetime






