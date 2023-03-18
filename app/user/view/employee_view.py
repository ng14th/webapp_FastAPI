from app.user.utils.employee import ( 
add_new_employee, 
delete_employee, 
update_information_employee,
get_list_employ_by_tenant_id,
get_list_employee)
from app.user.schema.employee_schema import ( EmployeeInfor, 
                                        UpdateEmployeeInfor)
from fastapi import APIRouter, Depends
from app.core.schema.api_response import ApiResponse
from app.core.verify.token import generate_jwt_token, validator_token
from app.user.models.user import User
from app.user.utils.user import verify_user

router = APIRouter(tags=['Employee'], prefix='/employee')

@router.post('/add_new_employee',response_model=ApiResponse)
async def new_employee(
    infor : EmployeeInfor,
    user : User = Depends(verify_user)
):
    result = await add_new_employee(infor, user.tenant_id)
    if result :
        return {'success' : True,
                'data' : [result]}
    return {'success': False}

@router.post('/delete_employee',response_model=ApiResponse)
async def delete_employee_mongod(
    employee : EmployeeInfor,
    user : User = Depends(verify_user)
):
    result = await delete_employee(employee, user.tenant_id)
    if result:
        return {'success': True}
    return {'success': False}

@router.post('/update_employee',response_model=ApiResponse)
async def update_employee(
    update : UpdateEmployeeInfor,
    user : User = Depends(verify_user)
):
    result = await update_information_employee(update, user.tenant_id)
    if result :
        return {'success' : True,
                'data' : [result]}
    return {'success': False}

@router.post('/list_employee_tenant_id',response_model=ApiResponse)
async def get_list_employ(
    user : User = Depends(verify_user)
):
    result = await get_list_employ_by_tenant_id(user.tenant_id)
    if result :
        return {'success' : True,
                'data' : [result]}
    return {'success': False}

@router.post('/list_employee',response_model=ApiResponse)
async def get_list_employ_all(user: User = Depends(verify_user)):
    result = await get_list_employee()
    if result :
        return {'success' : True,
                'data' : [result]}
    return {'success': False}

    
    