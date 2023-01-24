from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.db import get_db
from app.models.repositories import courses as courses_repo
from app.models.schemas.course import CourseCreate, CourseUpdate, Course

router = APIRouter()


@router.get("/{id}", response_model=Course, tags=['courses'])
def get_course(id: int, db: Session = Depends(get_db)):
    it = courses_repo.get_course(db, id)
    return it


@router.get("", response_model=list[Course], tags=['courses'])
async def get_courses(offset: int = 0, limit: int = 25, db: Session = Depends(get_db)):
    return courses_repo.get_courses(db, offset, limit)


@router.post("", response_model=Course, tags=['courses'])
def create_course(course: CourseCreate, db: Session = Depends(get_db)):
    it = courses_repo.create_course(db, course)
    return it


@router.put("/{course_id}", response_model=Course, tags=['courses'])
def update_course(course_id: int, course: CourseUpdate, db: Session = Depends(get_db)):
    it = courses_repo.update_course(db, course_id, course)
    return it
