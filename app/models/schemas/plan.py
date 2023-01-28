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
    form: str
    number_of_semesters: int
    lang: str
    field_id: int
    opinions: Union[list[Opinion], None]
    semesters: Union[List[Semester], None]

    class Config:
        orm_mode = True


class Plan(PlanBase):
    id: int


class PlanCreate(PlanBase):
    pass


class PlanUpdate(PlanBase):
    pass
