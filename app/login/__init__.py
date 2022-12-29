from fastapi import APIRouter
from app.login.login_view import router as login_router


router = APIRouter()

router.include_router(login_router)