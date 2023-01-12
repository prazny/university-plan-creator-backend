import enum
from typing import List


from pydantic import validator

from app.models.domain.course import Type, Form
from app.models.schemas.base import Base as BaseModel


class CourseBase(BaseModel):
    ects: int
    cnps: int
    zzu: int
    bu: int
    hours_count: int
    direction: str
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
