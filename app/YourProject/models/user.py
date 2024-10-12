# app/models/user.py
from sqlmodel import SQLModel, Field, Relationship
from typing import List, Optional
from datetime import datetime


class UserBase(SQLModel):
    name: str
    email: str = Field(index=True)

class User(UserBase, table=True):
    __tablename__ = "users"

    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    hashed_password: str
    updated_at: datetime = Field(default_factory=datetime.utcnow, index=True)
    created_at: datetime = Field(default_factory=datetime.utcnow, index=True)

    projects: List["Project"] = Relationship(back_populates="owner")

class UserCreate(UserBase):
    password: str

class UserRead(UserBase):
    id: int
    updated_at: datetime
    created_at: datetime