# app/models/task.py
from sqlmodel import SQLModel, Field, Relationship
from typing import List, Optional
from datetime import datetime
from .project import Project

class TaskBase(SQLModel):
    title: str
    description: str
    due_date: datetime
    status: str  # e.g., 'pending', 'completed'

class Task(TaskBase, table=True):
    __tablename__ = "tasks"

    id: Optional[int] = Field(default=None, primary_key=True)
    updated_at: datetime = Field(default_factory=datetime.utcnow, index=True)
    created_at: datetime = Field(default_factory=datetime.utcnow, index=True)
    project_id: int = Field(foreign_key="projects.id", index=True)  
    status: str = Field(index=True)
    due_date: datetime = Field(index=True)

    project: Optional[Project] = Relationship(back_populates="tasks")
    notes: List["Note"] = Relationship(back_populates="task")

class TaskCreate(TaskBase):
    project_id: int

class TaskRead(TaskBase):
    id: int
    updated_at: datetime
    created_at: datetime
