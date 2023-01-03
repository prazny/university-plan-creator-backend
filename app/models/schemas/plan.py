from typing import List

from pydantic import validator
from app.models.schemas.base import Base as BaseModel


class PlanBase(BaseModel):
    year: int
    form: str
    number_of_semesters: int
    lang: str
    field_id: int

    class Config:
        orm_mode = True


class Plan(PlanBase):
    id: int


class PlanCreate(PlanBase):
    pass


class ModuleUpdate(ModuleBase):
    pass
