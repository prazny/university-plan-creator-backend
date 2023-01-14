from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.db import get_db
from app.models.schemas.activity import Activity, ActivityCreate, ActivityUpdate
from app.models.repositories import activities as activities_repo

router = APIRouter()


@router.get("", response_model=list[Activity], tags=['activities'])
async def get_activities(offset: int = 0, limit: int = 25, db: Session = Depends(get_db)):
    return activities_repo.get_activities(db, offset, limit)


@router.post("", response_model=Activity, tags=['activities'])
def create_activity(activity: ActivityCreate, db: Session = Depends(get_db)):
    it = activities_repo.create_activity(db, activity)
    return it


@router.put("/{activity_id}", response_model=Activity, tags=['activities'])
def update_activity(activity_id: int, activity: ActivityUpdate, db: Session = Depends(get_db)):
    it = activities_repo.update_activity(db, activity_id, activity)
    return it
