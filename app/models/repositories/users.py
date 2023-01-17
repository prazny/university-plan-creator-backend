import random

from sqlalchemy.orm import Session

from app.models.domain.users import User

import app.models.schemas.user as user_schema


def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def get_users(db: Session, offset: int = 0, limit: int = 25):
    return db.query(User).offset(offset).limit(limit).all()


def create_user(db: Session, user: user_schema.UserCreate):
    db_item = User(**user.dict())
    db_item.login = user.login
    db_item.email = user.email
    db_item.password = user.password

    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
