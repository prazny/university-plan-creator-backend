from sqlalchemy.orm import Session
from fastapi.exceptions import HTTPException

from app.models.domain.plan import Plan
from app.models.domain.semester import Semester

import app.models.schemas.plan as plan_schema


def get_plan(db: Session, plan_id: int):
    db_item = db.query(Plan).filter(Plan.id == plan_id).first()
    return db_item


def get_plans(db: Session, offset: int = 0, limit: int = 25):
    db_item = db.query(Plan).offset(offset).limit(limit).all()
    # if (semesters_elems := db.query(Semester).filter(Semester.id.in_(plan.semesters_id))).count() == len(plan.semesters_id):
    #     db_item.semesters.extend(semesters_elems)
    return db_item

def create_plan(db: Session, plan: plan_schema.PlanCreate):
    db_item = Plan(year = plan.year, form = plan.form, number_of_semesters = plan.number_of_semesters, lang = plan.lang, field_id = plan.field_id)

    if plan.semestersIds is not None:
        if (semesters_elems := db.query(Semester).filter(Semester.id.in_(plan.semestersIds))).count() == len(plan.semestersIds):
            db_item.semesters.extend(semesters_elems)
        else:
            # even if at least one editor is not found, an error is raised
            # if existence is not matter you can skip this check and add relations only for existing data
            raise HTTPException(status_code=404, detail="semester not found")

    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
