from typing import List, Optional
from typing import TYPE_CHECKING, List
from pydantic import validator
from pydantic import BaseModel
from app.models.schemas.faculty import Faculty


class FieldBase(BaseModel):
    name: str
    profile: str
    level: str
    faculty_id: int

    class Config:
        orm_mode = True


class Field(FieldBase):
    id: int
    #faculties: Optional[List[Faculty]]


class FieldCreate(FieldBase):
    pass


class FieldUpdate(FieldBase):
    pass
