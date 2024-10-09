# app/models/project.py
from sqlmodel import SQLModel, Field, Relationship
from typing import List, Optional
from app.models.user import User

class ProjectBase(SQLModel):
    title: str
    description: str

class Project(ProjectBase, table=True):
    __tablename__ = "projects"

    id: Optional[int] = Field(default=None, primary_key=True)
    owner_id: int = Field(foreign_key="users.id")

    owner: Optional[User] = Relationship(back_populates="projects")
    tasks: List["Task"] = Relationship(back_populates="project")

class ProjectCreate(ProjectBase):
    owner_id: int

class ProjectRead(ProjectBase):
    id: int