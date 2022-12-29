from app.user.utils.employee import ( 
add_new_employee, 
delete_employee, 
update_information_employee,
get_list_employ_by_tenant_id,
get_list_employee)
from app.user.schema.employee_schema import ( EmployeeInfor, 
                                        UpdateEmployeeInfor,
                                        GetEmployByTeanantID)
from fastapi import APIRouter, Depends
from app.core.schema.api_response import ApiResponse
from app.core.verify.token import generate_jwt_token, validator_token

router = APIRouter(tags=['Employee'])

@router.post('/add_new_employee',response_model=ApiResponse)
async def new_employee(
    infor : EmployeeInfor
):
    result = await add_new_employee(infor)
    if result :
        return {'success' : True,
                'data' : [result]}
    return {'success': False}

@router.post('/delete_employee',response_model=ApiResponse)
async def new_employee(
    employee : EmployeeInfor
):
    result = await delete_employee(employee)
    if result:
        return {'success': True}
    return {'success': False}

@router.post('/update_employee',response_model=ApiResponse)
async def update_employee(
    update : UpdateEmployeeInfor
):
    result = await update_information_employee(update)
    if result :
        return {'success' : True,
                'data' : [result]}
    return {'success': False}

@router.post('/list_employee_tenant_id',response_model=ApiResponse)
async def get_list_employ(
    data : GetEmployByTeanantID
):
    result = await get_list_employ_by_tenant_id(data.tenant_id)
    if result :
        return {'success' : True,
                'data' : [result]}
    return {'success': False}

@router.post('/list_employee',response_model=ApiResponse)
async def get_list_employ_all(user = Depends(validator_token)):
    tenant_id = user.get("tenant_id")
    print(tenant_id)
    result = await get_list_employee()
    if result :
        return {'success' : True,
                'data' : [result]}
    return {'success': False}

    
    