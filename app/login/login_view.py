from app.login.login_schema import Login
from fastapi import APIRouter
from app.core.verify.token import generate_jwt_token
from app.login.login_utils import insert_user_to_mongod_by_token

router = APIRouter(tags=['Login'])

@router.post('/login')
async def user_login(request : Login):
    
    username, token = await insert_user_to_mongod_by_token(request)
    return {
        'username' : username,
        'token' : token
    }