from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.db import get_db
from app.models.schemas.plan import Plan, PlanCreate, PlanUpdate
from app.models.repositories import plans as Plan_repo

router = APIRouter()


@router.get("", response_model=list[Plan], tags=['plans'])
async def get_plans(offset: int = 0, limit: int = 25, db: Session = Depends(get_db)):
    return Plan_repo.get_plans(db, offset, limit)


@router.post("", response_model=Plan, tags=['plans'])
def create_plans(plan: PlanCreate, db: Session = Depends(get_db)):
    it = Plan_repo.create_plan(db, plan)
    return it

@router.get("/{id}", response_model=Plan, tags=['plans'])
def get_plan(id: int, db: Session = Depends(get_db)):
    it = Plan_repo.get_plan(db, id)
    return it


# @router.put("/{plan_id}", response_model=Plan, tags=['plans'])
# def update_plans(plan_id: int, plan: PlanUpdate, db: Session = Depends(get_db)):
#     it = Plan_repo.(db, plan_id, plan)
#     return it
