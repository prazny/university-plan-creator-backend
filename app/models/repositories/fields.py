from sqlalchemy.orm import Session

from app.models.domain.field import Field

import app.models.schemas.field as field_schema


def get_module(db: Session, field_id: int):
    return db.query(Field).filter(Field.id == field_id).first()


def get_modules(db: Session, offset: int = 0, limit: int = 25):
    return db.query(Field).offset(offset).limit(limit).all()


def create_module(db: Session, faculty: field_schema.FieldCreate):
    db_item = Field(**faculty.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
