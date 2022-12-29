from app.core.verify.token import decode_jwt_token, check_password, hass_password, generate_jwt_token
from app.login.user import User, UserMeMe
from app.login.login_schema import Login
from app.core.exceptions import ErrorResponseException
from app.core.schema.api_response import get_error_code


async def get_data_user_from_meme(tenant_id, email):
    check_user = await UserMeMe.find_one({
        "tenant_id" : tenant_id,
        "email" : email
    })
    if not check_user :
        raise ErrorResponseException(**get_error_code(9000))
    result = check_user.dump()
    result.pop("id")
    return result



async def insert_user_to_mongod_by_token(request : Login):
    
    
    data = {
        "tenant_id" : request.tenant_id,
        "email" : request.email,
        "password" : request.password
    }
    token = generate_jwt_token(data)
    
    decode_data_user = decode_jwt_token(token)
    
    data_user = Login.parse_obj(decode_data_user)
    get_user_meme = await get_data_user_from_meme(data_user.tenant_id, data_user.email)
    query = {
            "tenant_id" : request.tenant_id,
            "email" : request.email,
            "username" : get_user_meme.get("username")
        }
    if get_user_meme:
        check_user = await User.find_one(query)
        if check_user:
            decode_data_user.pop('password') 
            if check_password(data_user.password,check_user.password):
                return check_user.username, token
            else:
                raise ErrorResponseException(**get_error_code(9999))

        else :        
            hasspw_user = hass_password(data_user.password)
            get_user_meme["password"] = hasspw_user
            update = { "$set":{**get_user_meme}}
            update_or_create_user = await User.collection.update_one(
                query,
                update,
                upsert = True
            )
            return get_user_meme.get("username"), token
            
    