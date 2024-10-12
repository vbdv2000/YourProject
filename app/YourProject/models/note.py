# app/models/note.py
from sqlmodel import SQLModel, Field, Relationship
from typing import Optional
from datetime import datetime
from .task import Task

class NoteBase(SQLModel):
    content: str

class Note(NoteBase, table=True):
    __tablename__ = "notes"

    id: Optional[int] = Field(default=None, primary_key=True)
    updated_at: datetime = Field(default_factory=datetime.utcnow, index=True)
    created_at: datetime = Field(default_factory=datetime.utcnow, index=True)
    task_id: int = Field(foreign_key="tasks.id", index=True)

    task: Optional[Task] = Relationship(back_populates="notes")

class NoteCreate(NoteBase):
    task_id: int

class NoteRead(NoteBase):
    id: int
    updated_at: datetime
    created_at: datetime
