from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.db import get_db
from app.models.schemas.semester import Semester, SemesterCreate, SemesterUpdate
from app.models.repositories import semesters as Semester_repo

router = APIRouter()


@router.get("", response_model=list[Semester], tags=['semesters'])
async def get_semesters(offset: int = 0, limit: int = 25, db: Session = Depends(get_db)):
    return Semester_repo.get_semesters(db, offset, limit)


@router.get("/{id}", response_model=Semester, tags=['semesters'])
async def get_semester(id: int, db: Session = Depends(get_db)):
    return Semester_repo.get_semester(db, id)


@router.post("", response_model=Semester, tags=['semesters'])
def create_semesters(plan: SemesterCreate, db: Session = Depends(get_db)):
    it = Semester_repo.create_semester(db, plan)
    return it

@router.patch("/{semester_id}/{activity_id}", response_model=Semester, tags=['semesters'])
def update_semester_with_activity(semester_id: int, activity_id: int, db: Session = Depends(get_db)):
    it = Semester_repo.update_semester_with_activity(db, semester_id, activity_id)
    return it

@router.delete("/{semester_id}/{activity_id}", response_model=bool, tags=['semesters'])
def delete_semester_with_activity(semester_id: int, activity_id: int, db: Session = Depends(get_db)):
    it = Semester_repo.delete_semester_with_activity(db, semester_id, activity_id)
    return it

