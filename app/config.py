from typing import Optional, List, Union, Tuple
from pydantic import BaseSettings
import os


class AppEnvConfig(BaseSettings):
    
    APP_PROJECT_NAME: str = "FastApi-App"
    APP_DEBUG: bool = True
    APP_DOCS_URL: Optional[str] = '/docs'

    GUNICORN_HOST: str = '0.0.0.0'
    GUNICORN_PORT: str = '8000'
    
    APP_DB_MONGO_URI : str = ""
    APP_DB_MONGO_NAME : str = ""
    

    REDIS_URL: str = "172.27.230.25"
    REDIS_RESPONSE: bool = True
    REDIS_DB: int = 0
    
    BROKER_URL : str = f'amqp://admin:admin@172.27.230.14/nguyennt63'
    BACKEND_URL : str = "redis://172.27.230.14:6379/9"
    
    SECRET_KEY : str =  'nguyennt63'
    SECURITY_ALGORITHM : str = 'HS256'
    
    RMQ_TCP : str = "amqp"
    RMQ_URL : str = "172.27.230.14"
    RMQ_USERNAME : str = "admin"
    RMQ_PASSWORD : str = "admin"
    RMQ_VIRTUAL_HOST : str = "nguyennt63"
    RMQ_CHANNEL : int = 9
    
    EMAIL_SENDER : str = 'nguyennt63@fpt.com.vn'
    EMAIL_PASSWORD : str = '@Phuonglinh14'
    EMAIL_HOST : str = 'mail.fpt.com.vn'
    EMAIL_PORT : int = 587

    
    
    class Config:
        case_sensitive = True
        validate_assignment = True
        
        
    

settings = AppEnvConfig(_env_file='.env')
if __name__ == "__main__":
    pass



        
    