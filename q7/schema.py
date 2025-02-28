import datetime
import uuid
from typing import List, Optional
from pydantic import BaseModel
from datetime import date

class ResourceBase(BaseModel):
    name: str
    role: str

class ResourceCreate(ResourceBase):
    pass

class ResourceResponse(ResourceBase):
    id: uuid.UUID
    on_bench: bool
    is_deleted: bool
    time_joined: datetime.datetime
    time_updated: Optional[datetime.datetime] = None
    time_leaved: Optional[datetime.datetime] = None

    class Config:
        from_attributes = True

class ProjectBase(BaseModel):
    name: str
    manager_id: Optional[uuid.UUID] = None
    deadline: Optional[date] = None

class ProjectCreate(ProjectBase):
    pass

class ProjectResponse(ProjectBase):
    id: uuid.UUID
    completed: bool
    is_deleted: bool
    time_started: Optional[datetime.datetime] = None
    time_updated: Optional[datetime.datetime] = None
    # resources: List[ResourceResponse] = []

    class Config:
        from_attributes = True

class ProjectResourceSchema(BaseModel):
    project_id: uuid.UUID
    resource_id: uuid.UUID

class ProjectResourceSchemaResponse(ProjectResourceSchema):
    id: uuid.UUID

    class Config:
        from_attributes = True