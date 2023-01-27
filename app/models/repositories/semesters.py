from sqlalchemy.orm import Session
from fastapi.exceptions import HTTPException


from app.models.domain.semester import Semester
from app.models.domain.activity import Activity

import app.models.schemas.semester as semester_schema


def get_semester(db: Session, semester_id: int):
    return db.query(Semester).filter(Semester.id == semester_id).first()


def get_semester(db: Session, offset: int = 0, limit: int = 25):
    return db.query(Semester).offset(offset).limit(limit).all()


def create_semester(db: Session, semester_create: semester_schema.SemesterCreate):
    db_item = Semester(max_ects_deficit = semester_create.max_ects_deficit, semester_number = semester_create.semester_number)
    if (activities_elems := db.query(Activity).filter(Activity.id.in_([semester.id for semester in semester_create.activities]))).count() == len(semester_create.activities):
        db_item.activities.extend(activities_elems)
    else:
        # even if at least one editor is not found, an error is raised
        # if existence is not matter you can skip this check and add relations only for existing data
        raise HTTPException(status_code=404, detail="activity not found")
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def delete_semester(db: Session, semester_id: int) -> bool:
    db_item = get_semester(db, semester_id)
    db.delete(db_item)
    db.commit()
    return True
