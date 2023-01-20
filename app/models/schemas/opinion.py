import enum
from typing import List


from pydantic import validator

from app.models.domain.opinion import Status
from app.models.schemas.base import Base as BaseModel


class OpinionBase(BaseModel):
    is_approved: bool
    description: str
    status: Status
    user_id: int
    plan_id: int

    class Config:
        orm_mode = True


class Opinion(OpinionBase):
    id: int


class OpinionCreate(OpinionBase):
    pass
