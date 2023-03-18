# -*- coding: utf-8 -*-
from typing import Any, List
from pydantic import BaseModel


ERROR_CODE = {
    1000: "Config error",
    2000: "username have already exist",
    2001: "employee not exist",
    2002: "Cant find user",
    2003: "Cant update user",
    3001: "Phone must be number",
    3002: "Name cannot empty",
    4000: "Type exchange of RabbitMQ must in direct, fanout, headers, topic, dlx",
    9000: "User not exist in system",
    9996: "New Password cant be empty",
    9997: "New Password is not a same",
    9998: "Old Password is not correct",
    9999: "Wrong Password"
    
}


def get_error_code(error_code: int, data : str = None):
    if data:
        error_detail = ERROR_CODE.get(error_code, "Error code is not define").replace('{values}', data)
    else:
        error_detail = ERROR_CODE.get(error_code, "Error code is not define")
        
    return {
        "success": False,
        "error_code": error_code,
        "error": error_detail
    }

class ApiResponse(BaseModel):
    success: bool = True
    data: List[Any] = []
    length: int = 0
    error: str = ""
    error_code: int = 0
