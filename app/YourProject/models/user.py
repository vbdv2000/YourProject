# app/models/user.py
from sqlmodel import SQLModel, Field, Relationship
from typing import List, Optional

class UserBase(SQLModel):
    name: str
    email: str = Field(index=True)

class User(UserBase, table=True):
    __tablename__ = "users"

    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    hashed_password: str

    projects: List["Project"] = Relationship(back_populates="owner")

class UserCreate(UserBase):
    password: str

class UserRead(UserBase):
    id: int