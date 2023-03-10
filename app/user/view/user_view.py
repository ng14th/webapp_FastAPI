from app.user.utils.user import change_password
from app.user.schema.user_schema import ChangePassword
from app.core.schema.api_response import ApiResponse
from fastapi import APIRouter

router = APIRouter(tags=['User'])


@router.post('/change_password',response_model=ApiResponse)
async def change_password_user(
    data : ChangePassword
):
    result = await change_password(data)
    if result :
        return {'success' : True,
                'data' : [result]}
    return {'success': False}