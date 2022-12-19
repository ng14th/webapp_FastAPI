from app.schema.employee_schema import ( EmployeeInfor, 
                                        UpdateEmployeeInfor,
                                        GetEmployByTeanantID)
from app.models.employee import EmployeeInformations
from app.core.exceptions import ErrorResponseException
from app.core.schema.api_response import get_error_code
import json
import ujson

async def add_new_employee(infor : EmployeeInfor):
    is_exist_username : EmployeeInformations = await EmployeeInformations.find_one({
        "tenant_id" : infor.tenant_id,
        "username" : infor.username
    })
    if is_exist_username : 
        raise ErrorResponseException(**get_error_code(2000))
    new_employee = EmployeeInformations(
        tenant_id = infor.tenant_id,
        username = infor.username,
        full_name = infor.full_name,
        phone = infor.phone
    )
    await new_employee.commit()
    if new_employee:
        resp = {
            "tenant_id" : new_employee.tenant_id,
            "username" : new_employee.username
        }
        return resp

async def delete_employee(delete_employee : EmployeeInfor):
    is_exist_employee : EmployeeInformations = await EmployeeInformations.find_one(
        {
            "tenant_id": delete_employee.tenant_id,
            "username" : delete_employee.username
        }
    )
    if not is_exist_employee:
        raise ErrorResponseException(**get_error_code(2001))
    await is_exist_employee.delete()
    return True

async def update_information_employee(update : UpdateEmployeeInfor):
    is_exist_employee : EmployeeInformations = await EmployeeInformations.find_one(
        {
            "tenant_id": update.tenant_id,
            "username" : update.username
        }
    )
    if not is_exist_employee:
        raise ErrorResponseException(**get_error_code(2001))
    if update.new_tenant_id:
        is_exist_employee["tenant_id"] = update.new_tenant_id
    if update.new_username:
        is_exist_employee["username"] = update.new_username
    if update.new_phone:
        is_exist_employee["phone"] = update.new_phone
        
    await is_exist_employee.commit()
    if is_exist_employee :
        
        rsp = {
            "tenant_id" : is_exist_employee.tenant_id,
            "username" : is_exist_employee.username,
            "full_name" : is_exist_employee.full_name,
            "phone" : is_exist_employee.phone
        }
        return rsp

async def get_list_employ_by_tenant_id(teant_id):
    result = []
    employees : EmployeeInformations = EmployeeInformations.find({"tenant_id":teant_id})
    async for employee in employees:
        employee_dict = employee.dump()
        employee_dict.pop("id")
        result.append(employee_dict)
        
    return result

async def get_list_employee():
    result = []
    employees : EmployeeInformations = EmployeeInformations.find({})
    async for employee in employees:
        employee_dict = employee.dump()
        employee_dict.pop("id")
        result.append(employee_dict)
    return result
        

