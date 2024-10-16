from fastapi import FastAPI, Depends, HTTPException, Query
from fastapi.security import OAuth2PasswordRequestForm
from sqlmodel import Session, select
from YourProject.database import get_session
from YourProject.models import (
    User, UserCreate, UserRead,
    Project, ProjectCreate, ProjectRead,
    Task, TaskCreate, TaskRead,
    Note, NoteCreate, NoteRead
)
from YourProject.auth import hash_password, login_for_access_token, get_current_user
from pydantic import BaseModel, Field
from typing import List, Optional
from typing_extensions import Annotated, Literal

app = FastAPI()

# Route to login and get the JWT token
@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    return await login_for_access_token(form_data)

# Example of a protected route that requires a valid JWT token
@app.get("/users/me", response_model=UserRead)
async def get_user_me(current_user: User = Depends(get_current_user)):
    return current_user


# Manage Filters
class FilterParams(BaseModel):
    limit: int = Field(100, gt=0, le=100)
    offset: int = Field(0, ge=0)
    order_by: Literal["created_at", "updated_at"] = "created_at"
    tags: Optional[List[str]] = []


# User Endpoints
@app.post("/user", response_model=UserRead)
def create_user(user: UserCreate, session: Session = Depends(get_session)):
    hashed_password = hash_password(user.password)
    db_user = User(name=user.name, email=user.email, hashed_password=hashed_password)
    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    return db_user

@app.get("/users", response_model=List[UserRead])
def get_users(filter_query: Annotated[FilterParams, Query()], session: Session = Depends(get_session)):
    query = select(User).offset(filter_query.offset).limit(filter_query.limit).order_by(filter_query.order_by)
    users = session.exec(query).all()

    return users

@app.get("/users/{user_id}", response_model=UserRead)
def get_user_by_id(user_id: int, session: Session = Depends(get_session)):
    user = session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


# Project Endpoints
@app.post("/project", response_model=ProjectRead)
def create_project(project: ProjectCreate, session: Session = Depends(get_session)):
    db_project = Project.from_orm(project)
    session.add(db_project)
    session.commit()
    session.refresh(db_project)
    return db_project

@app.get("/projects", response_model=List[ProjectRead])
def get_projects(filter_query: Annotated[FilterParams, Query()], session: Session = Depends(get_session)):
    query = select(Project).offset(filter_query.offset).limit(filter_query.limit).order_by(filter_query.order_by)
    projects = session.exec(query).all()

    return projects

@app.get("/projects/{project_id}", response_model=ProjectRead)
def get_project_by_id(project_id: int, session: Session = Depends(get_session)):
    project = session.get(Project, project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    return project


# Task Endpoints
@app.post("/task", response_model=TaskRead)
def create_task(task: TaskCreate, session: Session = Depends(get_session)):
    db_task = Task.from_orm(task)
    session.add(db_task)
    session.commit()
    session.refresh(db_task)
    return db_task

@app.get("/tasks", response_model=List[TaskRead])
def get_tasks(filter_query: Annotated[FilterParams, Query()], session: Session = Depends(get_session)):
    query = select(Task).offset(filter_query.offset).limit(filter_query.limit).order_by(filter_query.order_by)
    tasks = session.exec(query).all()

    return tasks

@app.get("/tasks/{task_id}", response_model=TaskRead)
def get_task_by_id(task_id: int, session: Session = Depends(get_session)):
    task = session.get(Task, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


# Note Endpoints
@app.post("/note", response_model=NoteRead)
def create_note(note: NoteCreate, session: Session = Depends(get_session)):
    db_note = Note.from_orm(note)
    session.add(db_note)
    session.commit()
    session.refresh(db_note)
    return db_note

@app.get("/notes", response_model=List[NoteRead])
def get_notes(filter_query: Annotated[FilterParams, Query()], session: Session = Depends(get_session)):
    query = select(Note).offset(filter_query.offset).limit(filter_query.limit).order_by(filter_query.order_by)
    notes = session.exec(query).all()

    return notes

@app.get("/notes/{note_id}", response_model=NoteRead)
def get_note_by_id(note_id: int, session: Session = Depends(get_session)):
    note = session.get(Note, note_id)
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    return note
