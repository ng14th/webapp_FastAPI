from fastapi import APIRouter
from app.user.view.employee_view import router as employee_router
from app.user.view.user_view import router as user_router


router = APIRouter()

router.include_router(employee_router)
router.include_router(user_router)