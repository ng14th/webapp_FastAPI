from app.login.login_schema import Login
from fastapi import APIRouter
from app.core.verify.token import login_refresh_token
from app.login.login_utils import insert_user_to_mongod_by_token

router = APIRouter(tags=['Login'])

@router.post('/login')
async def user_login(request : Login):
    return await insert_user_to_mongod_by_token(request)

@router.post('/refresh_token')
async def refresh_token(refresh):
    return login_refresh_token(refresh)