from typing import List

from pydantic import validator
from app.models.schemas.base import Base as BaseModel
from app.models.schemas.activity import Activity


class SemesterBase(BaseModel):
    max_ects_deficit: int
    semester_number: int
    # plan_id: int

    class Config:
        orm_mode = True


class Semester(SemesterBase):
    id: int


class SemesterCreate(SemesterBase):
    activities_id: List[int] = []


class SemesterUpdate(SemesterBase):
    pass
