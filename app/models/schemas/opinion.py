import enum
from typing import List


from pydantic import validator

from app.models.domain.opinion import OpinionStatus
from app.models.schemas.base import Base as BaseModel


class OpinionBase(BaseModel):
    is_approved: bool
    description: str
    status: OpinionStatus

    class Config:
        orm_mode = True


class Opinion(OpinionBase):
    id: int


class OpinionCreate(OpinionBase):
    pass
