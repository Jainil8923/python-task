from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from db import get_db, engine
from models import Base, Project, Resource, ProjectResource
from schema import ProjectCreate, ProjectResponse, ResourceCreate, ResourceResponse, ProjectResource
from typing import List
import uuid

app = FastAPI()

Base.metadata.create_all(bind=engine)


@app.post("/projects/", response_model=ProjectResponse, status_code=status.HTTP_201_CREATED)
def create_project(project: ProjectCreate, db: Session = Depends(get_db)):
    db_project = Project(name=project.name, manager_id=project.manager_id, deadline=project.deadline)
    db.add(db_project)
    db.commit()
    db.refresh(db_project)
    return db_project

@app.get("/projects/", response_model=List[ProjectResponse], status_code=status.HTTP_200_OK)
def get_projects(db: Session = Depends(get_db)):
    return db.query(Project).filter(Project.is_deleted == False).all()


@app.put("/projects/{project_id}/complete", status_code=status.HTTP_200_OK)
def complete_project(project_id: int, db: Session = Depends(get_db)):
    project = db.query(Project).filter(Project.id == project_id, Project.is_deleted == False).first()
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    project.completed = True
    db.commit()
    for pr in project.resources:
        pr.resource.on_bench = True
    db.commit()
    return {"message": "Project marked as completed, resources moved to bench."}


@app.post("/resources/", response_model=ResourceResponse, status_code=status.HTTP_201_CREATED)
def create_resource(resource: ResourceCreate, db: Session = Depends(get_db)):
    new_resource = Resource(name=resource.name, role=resource.role)
    db.add(new_resource)
    db.commit()
    db.refresh(new_resource)
    return new_resource


@app.delete("/resource/{resource_id}/soft", status_code=status.HTTP_200_OK)
def soft_delete_resource(resource_id: int, db: Session = Depends(get_db)):
    resource = db.query(Resource).filter(Resource.id == resource_id).first()
    if not resource:
        raise HTTPException(status_code=400, detail=f"The id: {resource_id} you requested for does not exist")
    resource.is_deleted = True
    db.commit()
    return {"message": "Resource marked as deleted."}


@app.delete("/resource/{resource_id}/hard", status_code=status.HTTP_204_NO_CONTENT)
def hard_delete_resource(resource_id: uuid.UUID, db: Session = Depends(get_db)):
    resource = db.query(Resource).filter(Resource.id == resource_id).first()
    if not resource:
        raise HTTPException(status_code=400, detail=f"The id: {resource_id} you requested for does not exist")
    db.delete(resource)
    db.commit()


@app.get("/resources/", response_model=List[ResourceResponse], status_code=status.HTTP_200_OK)
def get_resources(db: Session = Depends(get_db)):
    return db.query(Resource).filter(Resource.is_deleted == False).all()


@app.delete("/projects/{project_id}/soft", status_code=status.HTTP_200_OK)
def soft_delete_project(project_id: int, db: Session = Depends(get_db)):
    project = db.query(Project).filter(Project.id == project_id).first()
    if not project:
        raise HTTPException(status_code=400, detail=f"The id: {project_id} you requested for does not exist")
    project.is_deleted = True
    db.commit()
    return {"message": "Project marked as deleted."}


@app.delete("/projects/{project_id}/hard", status_code=status.HTTP_204_NO_CONTENT)
def hard_delete_project(project_id: int, db: Session = Depends(get_db)):
    project = db.query(Project).filter(Project.id == project_id).first()
    if not project:
        raise HTTPException(status_code=400, detail=f"The id: {project_id} you requested for does not exist")
    db.delete(project)
    db.commit()


@app.get("/resources/on_bench", response_model=List[ResourceResponse], status_code=status.HTTP_200_OK)
def get_resources_on_bench(db: Session = Depends(get_db)):
    return db.query(Resource).filter(Resource.is_deleted == False and Resource.on_bench == True).all()


@app.get("/resources/{project_id}", response_model=List[ResourceResponse], status_code=status.HTTP_200_OK)
def get_resources_by_project(project_id: uuid.UUID, db: Session = Depends(get_db)):
    return db.query(Resource, ProjectResource).filter(ProjectResource.project_id == project_id).filter(
        ProjectResource.resource_id == Resource.id)

@app.post("/asignresource/{resource_id}/project/{project_id}",response_model=ProjectResponse, status_code=status.HTTP_200_OK)
def asign_resource(resource_id: uuid.UUID,project_id: uuid.UUID, db: Session = Depends(get_db)):
    resource_allocate = ProjectResource(resource_id=resource_id, project_id=project_id)
    db.add(resource_allocate)
    db.commit()
    db.refresh(resource_allocate)
    return resource_allocate