# app/database.py
import os
from sqlmodel import SQLModel, create_engine, Session
from dotenv import load_dotenv
from YourProject.models import User

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL, echo=True)

def get_session():
    with Session(engine) as session:
        yield session

def get_user_from_db(email: str):
    session = next(get_session())
    user = session.query(User).filter(User.email == email).first()
    return user