from typing import List
import enum

from pydantic import validator
from app.models.schemas.base import Base as BaseModel
from app.models.schemas.opinion import Opinion


class Form(enum.Enum):
    fulltime = 'fulltime'
    parttime = 'parttime'


class PlanBase(BaseModel):
    year: int
    form: str
    number_of_semesters: int
    lang: str
    field_id: int
    opinions: list[Opinion]

    class Config:
        orm_mode = True


class Plan(PlanBase):
    id: int


class PlanCreate(PlanBase):
    semesters_id: List[int] = []


class PlanUpdate(PlanBase):
    pass
