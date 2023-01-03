from sqlalchemy.orm import Session

from app.models.domain.module import Module

import app.models.schemas.module as module_schema


def get_module(db: Session, module_id: int):
    return db.query(Module).filter(Module.id == module_id).first()


def get_modules(db: Session, offset: int = 0, limit: int = 25):
    return db.query(Module).offset(offset).limit(limit).all()


def create_module(db: Session, faculty: module_schema.ModuleCreate):
    db_item = Module(**faculty.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
