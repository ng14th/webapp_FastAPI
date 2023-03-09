from app.core.exceptions import ErrorResponseException
from app.core.schema.api_response import get_error_code
from app.user.models.user import User
from app.user.schema.user_schema import ChangePassword
from fastapi import Depends
from app.core.verify.token import validator_token, check_password, hass_password
from datetime import datetime, timedelta


async def find_user(email):
    user = await User.find_one({"email":email})
    if not user :
        raise ErrorResponseException(**get_error_code(2002))
    return user

async def verify_user(data_user = Depends(validator_token)):
    email = data_user.get("email")
    return await find_user(email)


async def change_password(data : ChangePassword):
    user = await User.find_one({"email" : data.email})
    if not user :
        raise ErrorResponseException(**get_error_code(2002))
    if not check_password(data.old_password,user.password.get('password')):
        raise ErrorResponseException(**get_error_code(9998))
    if data.new_password != data.new_password_retype:
        raise ErrorResponseException(**get_error_code(9997))
    new_password = hass_password(data.new_password)
    user['password'] = {"password" : new_password}
    user['password_expr'] = str(datetime.timestamp(datetime.utcnow()+ timedelta(days=30.0)))
    await user.commit()
    return user.email
        
    