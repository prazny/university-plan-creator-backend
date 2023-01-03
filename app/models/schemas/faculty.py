from __future__ import annotations

from typing import TYPE_CHECKING, List
from pydantic import validator
from pydantic import BaseModel


class FacultyBase(BaseModel):
    name: str

    class Config:
        orm_mode = True

    @validator('name')
    def name_must_be_of_length_between_3_50(cls, v):
        if len(v) > 50 or len(v) < 3:
            raise ValueError('must be of length between 3 and 50')
        return v.title()


class Faculty(FacultyBase):
    id: int


class FacultyCreate(FacultyBase):
    pass


class FacultyUpdate(FacultyBase):
    pass
