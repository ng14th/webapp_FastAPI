from pydantic import BaseModel, validator
from typing import Optional

class EmployeeInfor(BaseModel):
    tenant_id : str
    username : str
    full_name : Optional[str]
    phone : Optional[str]
    
    
class UpdateEmployeeInfor(BaseModel):
    tenant_id : str
    username : str
    new_tenant_id : Optional[str]
    new_username : Optional[str]
    new_phone : Optional[str]

class GetEmployByTeanantID(BaseModel):
    tenant_id : str

