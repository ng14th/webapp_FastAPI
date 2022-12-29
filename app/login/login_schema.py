from pydantic import BaseModel
from typing import Optional

class Login(BaseModel):
    tenant_id : str
    email : str
    password : str