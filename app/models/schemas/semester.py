from typing import List

from pydantic import validator
from app.models.schemas.base import Base as BaseModel


class SemesterBase(BaseModel):
    max_ects_deficit: int
    semester_number: int

    class Config:
        orm_mode = True


class Semester(SemesterBase):
    id: int


class SemesterCreate(SemesterBase):
    pass


class SemesterUpdate(SemesterBase):
    pass
