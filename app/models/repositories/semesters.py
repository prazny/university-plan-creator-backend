from sqlalchemy.orm import Session

from app.models.domain.semester import Semester

import app.models.schemas.semester as semester_schema


def get_semester(db: Session, semester_id: int):
    return db.query(Semester).filter(Semester.id == semester_id).first()


def get_semester(db: Session, offset: int = 0, limit: int = 25):
    return db.query(Semester).offset(offset).limit(limit).all()


def create_semester(db: Session, faculty: semester_schema.Semester):
    db_item = Semester(**faculty.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def delete_semester(db: Session, semester_id: int) -> bool:
    db_item = get_semester(db, semester_id)
    db.delete(db_item)
    db.commit()
    return Truae
