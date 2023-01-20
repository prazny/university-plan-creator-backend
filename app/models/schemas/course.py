import enum
from typing import List


from pydantic import validator

from app.models.domain.course import Type, Form
from app.models.schemas.base import Base as BaseModel
from app.models.schemas.activity import ActivityBase


class CourseBase(ActivityBase):
    hours_count: int
    code: str
    type: Type
    completing_form: str
    course_form: Form

    class Config:
        orm_mode = True


class Course(CourseBase):
    id: int


class CourseCreate(CourseBase):
    pass


class CourseUpdate(CourseBase):
    pass
