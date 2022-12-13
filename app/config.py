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
    
    SENTINEL_NAMESPACE: str = 'mymaster'
    SENTINEL_URLS: List[Tuple[str, int]] = [
        ('172.27.230.25' , 26379, )
    ]
    SENTINEL_PASSWORD: str = '02011993'
    SENTINEL_DECODE_RESPONSE: bool = True
    SENTINEL_DB: int = 0
    
    
    class Config:
        case_sensitive = True
        validate_assignment = True

settings = AppEnvConfig(_env_file='.env')
if __name__ == "__main__":
    pass



        
    