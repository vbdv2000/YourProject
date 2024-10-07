from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from app.database import Base

class Task(Base):
    __tablename__ = "tasks"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String)
    created_at = Column(DateTime)
    due_date = Column(DateTime)
    status = Column(String)
    project_id = Column(Integer, ForeignKey("projects.id"))

    # Many-to-one relationship: A task belongs to one project
    project = relationship("Project", back_populates="tasks")