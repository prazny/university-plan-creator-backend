from sqlalchemy.orm import Session

from app.models.domain.activity import Activity

import app.models.schemas.activity as activity_schema


def get_module(db: Session, activity_id: int):
    return db.query(Activity).filter(Activity.id == activity_id).first()


def get_modules(db: Session, offset: int = 0, limit: int = 25):
    return db.query(Activity).offset(offset).limit(limit).all()


def create_module(db: Session, faculty: activity_schema.ActivityCreate):
    db_item = Activity(**faculty.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
