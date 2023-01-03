from typing import List

from pydantic import validator
from app.models.schemas.base import Base as BaseModel


class ActivityBase(BaseModel):
    ects: int
    cnps: int
    zzu: int
    bu: int

    class Config:
        orm_mode = True


class Activity(ActivityBase):
    id: int


class ActivityCreate(ActivityBase):
    pass


class ActivityUpdate(ActivityBase):
    pass
