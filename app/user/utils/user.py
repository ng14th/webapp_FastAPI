from app.core.exceptions import ErrorResponseException
from app.core.schema.api_response import get_error_code
from app.user.models.user import User
from app.user.schema.user_schema import ChangePassword
from fastapi import Depends
from app.core.verify.token import validator_token, check_password, hass_password
from datetime import datetime, timedelta
from app.core.database.rabbitmq_kombu import RabbitMQ
from app.core import constants

connection = RabbitMQ()


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
        
async def find_user_exp_password():
    list_user = []
    time_now = datetime.timestamp(datetime.utcnow()+timedelta(days=15))
    users = User.find({'password_expr':{'$lte':str(time_now)}})
    async for user in users:
        time_user_exp = datetime.utcfromtimestamp(float(user.password_expr)).date()
        list_user.append({
            "email" : user.email,
            "time_exp" : time_user_exp
        })
    return list_user

async def sync_password_expr():
    time_now =  datetime.timestamp(datetime.utcnow())
    date_exp_new = datetime.utcnow() + timedelta(days=30)
    timestamp_sexp_new = datetime.timestamp(date_exp_new)
    new_password = hass_password("12345")
    query = {'password_expr':{'$lte':str(time_now)}}
    update = {"$set":{"password": {"password" : new_password},
                      "password_expr": str(timestamp_sexp_new)}}
    update_password = await User.collection.update_one(
        query,
        update,
        upsert = False
    )
    return True
    
    

    