from sqlalchemy.orm import Session

from app.models.domain.plan import Plan

import app.models.schemas.plan as plan_schema


def get_plan(db: Session, plan_id: int):
    return db.query(Plan).filter(Plan.id == plan_id).first()


def get_plans(db: Session, offset: int = 0, limit: int = 25):
    return db.query(Plan).offset(offset).limit(limit).all()


def create_plan(db: Session, plan: plan_schema.PlanCreate):
    db_item = Plan(**plan.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
