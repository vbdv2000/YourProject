# app/models/task.py
from sqlmodel import SQLModel, Field, Relationship
from typing import List, Optional
from datetime import datetime
from app.models.project import Project

class TaskBase(SQLModel):
    title: str
    description: str
    due_date: datetime
    status: str  # e.g., 'pending', 'completed'

class Task(TaskBase, table=True):
    __tablename__ = "tasks"

    id: Optional[int] = Field(default=None, primary_key=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    project_id: int = Field(foreign_key="projects.id")

    project: Optional[Project] = Relationship(back_populates="tasks")
    notes: List["Note"] = Relationship(back_populates="task")

class TaskCreate(TaskBase):
    project_id: int

class TaskRead(TaskBase):
    id: int
    created_at: datetime
