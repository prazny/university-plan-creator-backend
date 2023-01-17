from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.db import get_db
from app.models.schemas.user import User, UserCreate
from app.models.repositories import users as users_repo

router = APIRouter()


@router.get("", response_model=list[User], tags=['users'])
async def get_users(offset: int = 0, limit: int = 25, db: Session = Depends(get_db)):
    return users_repo.get_users(db, offset, limit)


@router.post("", response_model=User, tags=['users'])
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    it = users_repo.create_user(db, user)
    return it
