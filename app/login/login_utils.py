from app.core.verify.token import (decode_jwt_token, 
                                   check_password, 
                                   hass_password, 
                                   generate_jwt_token, 
                                   generate_jwt_refresh_token)
from app.user.models.user import User, UserMeMe
from app.login.login_schema import Login
from app.core.exceptions import ErrorResponseException
from app.core.schema.api_response import get_error_code 
from datetime import datetime, timedelta
from app.core.database.rabbitmq_kombu import RabbitMQ
from app.core import constants

rabbitmq = RabbitMQ()


async def get_data_user_from_meme(email):
    check_user = await UserMeMe.find_one({
        "email" : email
    })
    if not check_user :
        raise ErrorResponseException(**get_error_code(9000))
    result = check_user.dump()
    result.pop("id")
    return result


async def insert_user_to_mongod_by_token(request : Login):
    data = {
        "email" : request.email,
        "password" : request.password
    }
    token = generate_jwt_token(data)
    refresh_token = generate_jwt_refresh_token(data)
    decode_data_user = decode_jwt_token(token)
    
    data_user = Login.parse_obj(decode_data_user)
    get_user_meme = await get_data_user_from_meme(data_user.email)
    query = {   
            "email" : request.email,
            "username" : get_user_meme.get("username")
        }
    if get_user_meme:
        check_user = await User.find_one(query)
        if check_user:
            decode_data_user.pop('password')
            result = {
                "username" : check_user.username,
                "token" : token,
                "refresh_token" : refresh_token,
                "password_exp" : None
            }
            if check_password(data_user.password,check_user.password.get('password')):
                user_password_exp = check_user.password_expr if check_user.password_expr else None
                if user_password_exp:
                    time_exp = datetime.utcfromtimestamp(float(user_password_exp)) - datetime.utcnow()
                    result["password_exp"] = datetime.utcfromtimestamp(float(user_password_exp)).date()
                    if time_exp.days < 15:
                        data = {
                            "email" : data_user.email,
                            "time_exp" : datetime.utcfromtimestamp(float(user_password_exp)).date()
                        }
                        message = {
                            "htype" : constants.HTYPE_MAPPING_CLASS_SEND_EMAIL,
                            "data" : [data]
                        }
                        rabbitmq.publish_message_exchange([message], constants.EXCHANGE_TASK_CELERY, constants.ROUTING_KEY_NOTI_USER)
                        
                return result
            
            raise ErrorResponseException(**get_error_code(9999))

        else :        
            hasspw_user = hass_password(data_user.password)
            get_user_meme["password"] = {"password" : hasspw_user}
            get_user_meme["password_expr"] = str(datetime.timestamp(datetime.utcnow()+ timedelta(days=30.0)))
            update = { "$set":{**get_user_meme}}
            update_or_create_user = await User.collection.update_one(
                query,
                update,
                upsert = True
            )
            return {
                "username" :get_user_meme.get("username"),
                "token" : token,
                "refresh_token" : refresh_token
            }