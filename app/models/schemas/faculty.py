from typing import List

from pydantic import validator
from pydantic.main import BaseModel


class FacultyBase(BaseModel):
    name: str
    profile: str
    level: str

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
