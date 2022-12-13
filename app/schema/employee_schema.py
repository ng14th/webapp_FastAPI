from pydantic import BaseModel, validator
from typing import Optional

class NewEmployee(BaseModel):
    tenant_id : str
    username : str
    full_name : str
    phone : Optional[str]