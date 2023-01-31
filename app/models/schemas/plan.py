from typing import List
import enum
from typing import Union

from pydantic import validator
from app.models.schemas.base import Base as BaseModel
from app.models.schemas.opinion import Opinion
from app.models.schemas.semester import Semester


class Form(enum.Enum):
    fulltime = 'fulltime'
    parttime = 'parttime'


class PlanBase(BaseModel):
    year: int
    form: str | None
    number_of_semesters:  int | None
    lang:  str | None
    field_id: int

    class Config:
        orm_mode = True


class Plan(PlanBase):
    id: int
    semesters: Union[List[Semester], None]
    opinions: Union[List[Opinion], None]


class PlanCreate(PlanBase):
    semestersIds: Union[List[int], None]
    opinionsIds: Union[List[int], None]


class PlanUpdate(PlanBase):
    pass
