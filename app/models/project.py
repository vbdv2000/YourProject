from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Project(Base):
    __tablename__ = "projects"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String)
    owner_id = Column(Integer, ForeignKey("users.id"))

    # Many-to-one relationship: A project belongs to one user (owner)
    owner = relationship("User", back_populates="projects")
    tasks = relationship("Task", back_populates="project")
