from pydantic import BaseModel
from typing import Optional

class Login(BaseModel):
    email : str
    password : str