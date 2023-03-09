from pydantic import BaseModel, validator
from typing import Optional
from app.core.exceptions import ErrorResponseException
from app.core.schema.api_response import get_error_code


class ChangePassword(BaseModel):
    email : str
    old_password : str
    new_password : str
    new_password_retype : str
    
    @validator("new_password")
    def check_new_password(cls,v):
        if v == None or v == "":
            raise ErrorResponseException(**get_error_code(9996))
        return v
        