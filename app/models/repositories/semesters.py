from sqlalchemy.orm import Session
from fastapi.exceptions import HTTPException

from app.models.domain.semester import Semester
from app.models.domain.activity import Activity

import app.models.schemas.semester as semester_schema


def get_semester(db: Session, semester_id: int):
    return db.query(Semester).filter(Semester.id == semester_id).first()


def get_semesters(db: Session, offset: int = 0, limit: int = 25):
    return db.query(Semester).offset(offset).limit(limit).all()


def create_semester(db: Session, semester_create: semester_schema.SemesterCreate):
    db_item = Semester(max_ects_deficit=semester_create.max_ects_deficit,
                       semester_number=semester_create.semester_number)

    if semester_create.activitiesIds != None:
        if (activities_elems := db.query(Activity).filter(
                Activity.id.in_(semester_create.activitiesIds))).count() == len(
                semester_create.activitiesIds):
            db_item.activities.extend(activities_elems)
        else:
            # even if at least one editor is not found, an error is raised
            # if existence is not matter you can skip this check and add relations only for existing data
            raise HTTPException(status_code=404, detail="activity not found")
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def delete_semester(db: Session, semester_id: int) -> bool:
    db_item = get_semester(db, semester_id)
    db.delete(db_item)
    db.commit()
    return True

def update_semester_with_activity(db: Session, semester_id: int, activity_id: int):
    semester_to_edit = db.query(Semester).filter(Semester.id == semester_id).first()

    if ((activities_elem := db.query(Activity).filter(Activity.id == activity_id)).count() == 1):
        semester_to_edit.activities.extend(activities_elem)

    db.add(semester_to_edit)
    db.commit()
    db.refresh(semester_to_edit)

    return semester_to_edit

def delete_semester_with_activity(db: Session, semester_id: int, activity_id: int):
    semester_to_edit = db.query(Semester).filter(Semester.id == semester_id).first()

    if ((activities_elem := db.query(Activity).filter(Activity.id == activity_id)).count() == 1):
        semester_to_edit.activities.remove(activities_elem.one())

    db.add(semester_to_edit)
    db.commit()
    db.refresh(semester_to_edit)

    return True
