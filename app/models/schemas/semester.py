from typing import List, Union

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
    activities: Union[List[Activity], None]


class SemesterCreate(SemesterBase):
    activitiesIds: Union[List[int], None]


class SemesterUpdate(SemesterBase):
    pass
