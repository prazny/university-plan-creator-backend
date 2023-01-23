from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.db import get_db
from app.models.repositories import opinions as opinions_repo
from app.models.schemas.opinion import OpinionCreate, Opinion

router = APIRouter()


@router.get("", response_model=list[Opinion], tags=['opinions'])
async def get_opinions(offset: int = 0, limit: int = 25, db: Session = Depends(get_db)):
    return opinions_repo.get_opinions(db, offset, limit)


@router.get("/{id}", response_model=Opinion, tags=['opinions'])
def get_opinion(id: int, db: Session = Depends(get_db)):
    it = opinions_repo.get_opinion(db, id)
    return it


@router.post("", response_model=Opinion, tags=['opinions'])
def create_opinion(opinion: OpinionCreate, db: Session = Depends(get_db)):
    it = opinions_repo.create_opinion(db, opinion)
    return it
