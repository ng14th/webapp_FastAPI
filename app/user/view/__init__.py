from fastapi import APIRouter
from app.user.view.employee_view import router as employee_router


router = APIRouter()

router.include_router(employee_router)