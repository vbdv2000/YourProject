# app/main.py
from fastapi import FastAPI, Depends, HTTPException
from contextlib import asynccontextmanager
from sqlmodel import SQLModel, Session, select
from app.database import engine, get_session
from app.models import (
    User, UserCreate, UserRead,
    Project, ProjectCreate, ProjectRead,
    Task, TaskCreate, TaskRead,
    Note, NoteCreate, NoteRead
)
from typing import List

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup tasks
    print("Starting up...")
    SQLModel.metadata.create_all(engine)  # Create the tables
    yield

    # Shutdown tasks (if any)
    print("Shutting down...")

app = FastAPI(lifespan=lifespan)

# User Endpoints
@app.post("/users/", response_model=UserRead)
def create_user(user: UserCreate, session: Session = Depends(get_session)):
    hashed_password = hash_password(user.password)
    db_user = User(name=user.name, email=user.email, hashed_password=hashed_password)
    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    return db_user

@app.get("/users/", response_model=List[UserRead])
def get_users(session: Session = Depends(get_session)):
    users = session.exec(select(User)).all()
    return users

# Project Endpoints
@app.post("/projects/", response_model=ProjectRead)
def create_project(project: ProjectCreate, session: Session = Depends(get_session)):
    db_project = Project.from_orm(project)
    session.add(db_project)
    session.commit()
    session.refresh(db_project)
    return db_project

# Task Endpoints
@app.post("/tasks/", response_model=TaskRead)
def create_task(task: TaskCreate, session: Session = Depends(get_session)):
    db_task = Task.from_orm(task)
    session.add(db_task)
    session.commit()
    session.refresh(db_task)
    return db_task

# Note Endpoints
@app.post("/notes/", response_model=NoteRead)
def create_note(note: NoteCreate, session: Session = Depends(get_session)):
    db_note = Note.from_orm(note)
    session.add(db_note)
    session.commit()
    session.refresh(db_note)
    return db_note

# Utility function to hash passwords
def hash_password(password: str) -> str:
    # Implement password hashing (e.g., using bcrypt)
    return password  # Placeholder, replace with actual hashing
