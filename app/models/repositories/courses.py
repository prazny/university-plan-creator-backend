from sqlalchemy.orm import Session

from app.models.domain.course import Course

import app.models.schemas.course as course_schema


def get_course(db: Session, course_id: int):
    return db.query(Course).filter(Course.id == course_id).first()


def get_courses(db: Session, offset: int = 0, limit: int = 25):
    return db.query(Course).offset(offset).limit(limit).all()


def create_course(db: Session, course: course_schema.CourseCreate):
    db_item = Course(**course.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def update_course(db: Session, course_id: int, course: course_schema.CourseUpdate):
    course_to_edit = db.query(Course).filter(Course.id == course_id).first()

    course_to_edit.name = course.name
    course_to_edit.ects = course.ects
    course_to_edit.cnps = course.cnps
    course_to_edit.zzu = course.zzu
    course_to_edit.bu = course.bu
    course_to_edit.hours_count = course.hours_count
    course_to_edit.code = course.code
    course_to_edit.type = course.type
    course_to_edit.completing_form = course.completing_form
    course_to_edit.course_form = course.course_form

    db.add(course_to_edit)
    db.commit()
    db.refresh(course_to_edit)

    return course_to_edit
