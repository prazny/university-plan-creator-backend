from typing import List, Union

from pydantic import validator
from app.models.schemas.base import Base as BaseModel
from app.models.schemas.activity import Activity


class SemesterBase(BaseModel):
   
    class Config:
        orm_mode = True


class Semester(SemesterBase):
    id: int
    max_ects_deficit: int
    semester_number: int
    # plan_id: int
    activities: Union[List[Activity], None]


class SemesterCreate(SemesterBase):
    max_ects_deficit: int
    semester_number: int
    # plan_id: int
    activitiesIds: Union[List[int], None]


class SemesterUpdate(SemesterBase):
    activitiesIds: Union[List[int], None]
