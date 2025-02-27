from uuid import uuid4

from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, Date
from sqlalchemy.orm import relationship
from db import Base
from sqlalchemy.dialects.postgresql import UUID
import uuid


class Project(Base):
    __tablename__ = "projects"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, unique=True, index=True)
    manager_id = Column(UUID, ForeignKey("resources.id"), nullable=True)
    deadline = Column(Date, nullable=True)
    completed = Column(Boolean, default=False)
    is_deleted = Column(Boolean, default=False)
    resources = relationship("ProjectResource", back_populates="project")

class Resource(Base):
    __tablename__ = "resources"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, index=True)
    role = Column(String)
    on_bench = Column(Boolean, default=False)
    is_deleted = Column(Boolean, default=False)
    projects = relationship("ProjectResource", back_populates="resource")

class ProjectResource(Base):
    __tablename__ = "project_resources"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    project_id = Column(UUID, ForeignKey("projects.id"))
    resource_id = Column(UUID, ForeignKey("resources.id"))
    project = relationship("Project", back_populates="resources")
    resource = relationship("Resource", back_populates="projects")