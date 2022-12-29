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
    
    BROKER_URL : str = "redis://172.27.230.25:6379/9"
    BACKEND_URL : str = "redis://172.27.230.25:6379/9"
    
    SECRET_KEY : str =  'nguyennt63'
    SECURITY_ALGORITHM : str = 'HS256'
    
    
    class Config:
        case_sensitive = True
        validate_assignment = True

settings = AppEnvConfig(_env_file='.env')
if __name__ == "__main__":
    pass



        
    