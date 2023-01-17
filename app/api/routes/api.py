from fastapi import APIRouter
from app.api.routes import faculties, activities, courses, opinions, plans, fields, semesters
from fastapi.responses import RedirectResponse

router = APIRouter()


@router.get('/', include_in_schema=False)
def get_docs():
    return RedirectResponse('/docs')


router.include_router(faculties.router, tags=["faculties"], prefix="/faculties")
router.include_router(activities.router, tags=["activities"], prefix="/activities")
router.include_router(courses.router, tags=["courses"], prefix="/courses")
router.include_router(opinions.router, tags=["opinions"], prefix="/opinions")
router.include_router(plans.router, tags=["plans"], prefix="/plans")
router.include_router(fields.router, tags=["fields"], prefix="/fields")
router.include_router(semesters.router, tags=["semesters"], prefix="/semesters")