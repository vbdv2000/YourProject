from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional

# Schema for creating a user
class UserCreate(BaseModel):
    name: str
    email: str
    hashed_password: str

class User(UserCreate):
    id: int
    projects: List[int] = []

    class Config:
        orm_mode = True

# Schema for creating a project
class ProjectCreate(BaseModel):
    title: str
    description: str
    owner_id: int

class Project(ProjectCreate):
    id: int
    tasks: List[int] = []

    class Config:
        orm_mode = True

# Schema for creating a task
class TaskCreate(BaseModel):
    title: str
    description: str
    created_at: datetime
    due_date: datetime
    status: str
    project_id: int

class Task(TaskCreate):
    id: int

    class Config:
        orm_mode = True
