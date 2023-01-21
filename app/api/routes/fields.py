from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.db import get_db
from app.models.schemas.field import *
from app.models.repositories import fields as fields_repo

router = APIRouter()


@router.get("", response_model=list[Field], tags=['fields'])
async def get_fields(offset: int = 0, limit: int = 25, db: Session = Depends(get_db)):
    return fields_repo.get_fields(db, offset, limit)

@router.get("/{id}", response_model=Field, tags=['fields'])
def get_field(id: int, db: Session = Depends(get_db)):
    it = fields_repo.get_field(db, id)
    return it

@router.post("", response_model=Field, tags=['fields'])
def create_fields(field: FieldCreate, db: Session = Depends(get_db)):
    it = fields_repo.create_field(db, field)
    return it
