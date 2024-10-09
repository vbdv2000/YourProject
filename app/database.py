# app/database.py
from sqlmodel import SQLModel, create_engine, Session

DATABASE_URL = "postgresql+psycopg2://victor:victor@localhost/your_project"

engine = create_engine(DATABASE_URL, echo=True)

def get_session():
    with Session(engine) as session:
        yield session
