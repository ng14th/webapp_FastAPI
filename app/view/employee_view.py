from app.utils.new_employee import add_new_employee
from app.schema.employee_schema import NewEmployee
from fastapi import APIRouter

router = APIRouter(tags=['Employee'])

@router.post('/add_new_employee')
async def new_employee(
    infor : NewEmployee
):
    result = await add_new_employee(infor)
    return result