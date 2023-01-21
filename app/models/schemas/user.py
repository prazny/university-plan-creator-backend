from app.models.schemas.base import Base as BaseModel


class UserBase(BaseModel):
    login: str
    email: str
    password: str

    class Config:
        orm_mode = True


class User(UserBase):
    id: int


class UserCreate(UserBase):
    pass
