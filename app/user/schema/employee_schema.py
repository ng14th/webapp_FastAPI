from pydantic import BaseModel, validator
from typing import Optional
from app.core.exceptions import ErrorResponseException
from app.core.schema.api_response import get_error_code

class EmployeeInfor(BaseModel):
    username : str 
    full_name : Optional[str]
    phone : Optional[str]
    
    @validator('phone')
    def is_correct_phone_number(cls, v):
        if v.isdigit():
            return v
        else:
            raise ErrorResponseException(**get_error_code(3001))
    
    @validator('username')
    def check_empty(cls,v):
        if v == "" or len(v) == 0:
            raise ErrorResponseException(**get_error_code(3002))
        return v
            
        
    
    
class UpdateEmployeeInfor(BaseModel):
    username : str
    new_tenant_id : Optional[str]
    new_username : Optional[str]
    new_phone : Optional[str]
    
    @validator('new_phone')
    def is_correct_phone_number(cls, v):
        if v.isdigit():
            return v
        else:
            raise ErrorResponseException(**get_error_code(3001))
