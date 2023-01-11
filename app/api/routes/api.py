from fastapi import APIRouter
from app.api.routes import faculties, activities, courses
from fastapi.responses import RedirectResponse

router = APIRouter()


@router.get('/', include_in_schema=False)
def get_docs():
    return RedirectResponse('/docs')


router.include_router(faculties.router, tags=["faculties"], prefix="/faculties")
router.include_router(activities.router, tags=["activities"], prefix="/activities")
router.include_router(courses.router, tags=["courses"], prefix="/courses")
