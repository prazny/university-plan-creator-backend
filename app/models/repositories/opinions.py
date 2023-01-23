from sqlalchemy.orm import Session

from app.models.domain.opinion import Opinion

import app.models.schemas.opinion as opinion_schema


def get_opinion(db: Session, opinion_id: int):
    return db.query(Opinion).filter(Opinion.id == opinion_id).first()


def get_opinion(db: Session, opinion_id: int):
    db_item = db.query(Opinion).filter(Opinion.id == opinion_id).first()
    return db_item


def get_opinions(db: Session, offset: int = 0, limit: int = 25):
    return db.query(Opinion).offset(offset).limit(limit).all()


def create_opinion(db: Session, opinion: opinion_schema.OpinionCreate):
    db_item = Opinion(**opinion.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
