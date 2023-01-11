from sqlalchemy.orm import Session

from app.models.domain.activity import Activity

import app.models.schemas.activity as activity_schema


def get_activity(db: Session, activity_id: int):
    return db.query(Activity).filter(Activity.id == activity_id).first()


def get_activities(db: Session, offset: int = 0, limit: int = 25):
    return db.query(Activity).offset(offset).limit(limit).all()


def create_activity(db: Session, activity: activity_schema.ActivityCreate):
    db_item = Activity(**activity.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def update_activity(db: Session, activity_id: int, activity: activity_schema.ActivityUpdate):
    activity_to_edit = db.query(Activity).filter(Activity.id == activity_id).first()

    activity_to_edit.ects = activity.ects
    activity_to_edit.bu = activity.bu
    activity_to_edit.cnps = activity.cnps
    activity_to_edit.zzu = activity.zzu

    db.add(activity_to_edit)
    db.commit()
    db.refresh(activity_to_edit)
    return activity_to_edit
