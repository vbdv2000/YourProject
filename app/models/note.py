# app/models/note.py
from sqlmodel import SQLModel, Field, Relationship
from typing import Optional
from datetime import datetime
from app.models.task import Task

class NoteBase(SQLModel):
    content: str

class Note(NoteBase, table=True):
    __tablename__ = "notes"

    id: Optional[int] = Field(default=None, primary_key=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    task_id: int = Field(foreign_key="tasks.id")

    task: Optional[Task] = Relationship(back_populates="notes")

class NoteCreate(NoteBase):
    task_id: int

class NoteRead(NoteBase):
    id: int
    created_at: datetime
