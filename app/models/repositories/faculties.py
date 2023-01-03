from sqlalchemy.orm import Session

from app.models.domain.faculty import Faculty

from app.models.schemas.faculty import FacultyUpdate, FacultyCreate, Faculty as schemaFac


def get_faculty(db: Session, faculty_id: int):
    return db.query(Faculty).filter(Faculty.id == faculty_id).first()


def get_faculties(db: Session, offset: int = 0, limit: int = 25):
    return db.query(Faculty).offset(offset).limit(limit).all()


def create_faculty(db: Session, faculty: FacultyCreate) -> schemaFac:
    db_item = Faculty(**faculty.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
