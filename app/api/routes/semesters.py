from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.db import get_db
from app.models.schemas.semester import Semester, SemesterCreate, SemesterUpdate
from app.models.repositories import semesters as Semester_repo

router = APIRouter()


@router.get("", response_model=list[Semester], tags=['semesters'])
async def get_semesters(offset: int = 0, limit: int = 25, db: Session = Depends(get_db)):
    return Semester_repo.get_semester(db, offset, limit)


@router.post("", response_model=Semester, tags=['semesters'])
def create_semesters(plan: SemesterCreate, db: Session = Depends(get_db)):
    it = Semester_repo.create_semester(db, plan)
    return it
