from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.db import get_db
from app.models.schemas.faculty import *
from app.models.repositories import faculties as faculties_repo

router = APIRouter()


@router.get("", response_model=list[Faculty], tags=['faculties'])
async def get_faculties(offset: int = 0, limit: int = 25, db: Session = Depends(get_db)):
    return faculties_repo.get_faculties(db, offset, limit)


@router.post("", response_model=Faculty, tags=['faculties'])
def create_faculty(faculty: FacultyCreate, db: Session = Depends(get_db)):
    it = faculties_repo.create_faculty(db, faculty)
    return it


@router.delete("/{id}", response_model=bool, tags=['faculties'])
def create_faculty(id: int, db: Session = Depends(get_db)):
    it = faculties_repo.delete_faculty(db, id)
    return it
