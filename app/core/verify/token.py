import jwt
import uvicorn

from datetime import datetime, timedelta
from typing import Union, Any
from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from app.config import settings
from fastapi.security import HTTPBearer
import bcrypt
# from app.login.login_utils import find_user

def generate_jwt_token(data_user : Union[dict, Any]):
    expire = datetime.utcnow() + timedelta(seconds=60*60) # 1 hour
    to_encode = {"exp": expire, "data_user": data_user}
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, settings.SECURITY_ALGORITHM)
    return encoded_jwt

def generate_jwt_refresh_token(data_user : Union[dict, Any]):
    expire = datetime.utcnow() + timedelta(seconds=3600*24) # 1 day
    to_encode = {"exp": expire, "data_user": data_user}
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, settings.SECURITY_ALGORITHM)
    return encoded_jwt

reusable_oauth2 = HTTPBearer(
    scheme_name='Authorization'
)

def validator_token(http_authorization_credentials=Depends(reusable_oauth2)) -> str:
    try:
        payload = jwt.decode(http_authorization_credentials.credentials, settings.SECRET_KEY, algorithms=[settings.SECURITY_ALGORITHM])
        print(payload)
        if payload.get('exp') < int(datetime.now().timestamp()):
            raise HTTPException(status_code=403, detail="Token expired")
        return payload.get('data_user')
    except:
        raise HTTPException(
            status_code=403,
            detail=f"Could not validate credentials",
        )

def decode_jwt_token(token):
    try :
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.SECURITY_ALGORITHM])
        if payload.get('exp') < int(datetime.now().timestamp()):
            raise HTTPException(status_code=403, detail="Token expired")
        return payload.get('data_user')
    except:
        raise HTTPException(
            status_code=403,
            detail=f"Could not validate credentials",
        )

def hass_password(password):
    password = bytes(password, 'utf-8')
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password,salt)
    return hashed

def check_password(password, password_hash):
    password = bytes(password, 'utf-8')
    if bcrypt.checkpw(password,password_hash):
        return True
    else:
        return False

def login_refresh_token(refresh_token: str):
    try:
        refresh_token_payload = jwt.decode(refresh_token, settings.SECRET_KEY, algorithms=["HS256"])
        username = refresh_token_payload["data_user"]
        access_token = generate_jwt_token(username)
        return {"access_token": access_token, "username": username}
    except :
        raise HTTPException(status_code=401, detail="Invalid token")
            