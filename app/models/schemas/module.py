from typing import List

from pydantic import validator
from app.models.schemas.base import Base as BaseModel


class ModuleBase(BaseModel):
    class Config:
        orm_mode = True


class Module(ModuleBase):
    id: int


class ModuleCreate(ModuleBase):
    pass


class ModuleUpdate(ModuleBase):
    pass
