from app.schema.employee_schema import NewEmployee
from app.models.employee import EmployeeInformations

async def add_new_employee(infor : NewEmployee):
    is_exist_username : EmployeeInformations = await EmployeeInformations.find_one({
        "tenant_id" : infor.tenant_id,
        "username" : infor.username
    })
    if is_exist_username : 
        print("đã có")
        return
    new_employee = EmployeeInformations(
        tenant_id = infor.tenant_id,
        username = infor.username,
        full_name = infor.full_name,
        phone = infor.phone
    )
    await new_employee.commit()
    return True
    