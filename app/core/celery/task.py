from app.core.celery.celery import celery
from app.core.database.redis import redis
from app.tools.tools import _dumps_dict_for_hash_map
from app.utils.employee import get_list_employee
import asyncio

loop = asyncio.get_event_loop()

async def create_hash_data_employee_in_redis(data):
    name = f'sync_information_employeee__{data.get("tenant_id")}__{data.get("username")}'
    mapping = _dumps_dict_for_hash_map(data)
    print(mapping)
    await redis.hset(name=name, mapping=mapping)
    return mapping

async def sync_information_employee():
    list_information = await get_list_employee()
    for employee_information in list_information:
        await create_hash_data_employee_in_redis(employee_information)

# # run when start up app FASTAPI
# @celery.task()
# def auto_sync_information():
#     print("CALLING TASK REPEAT")
#     loop.run_until_complete(sync_information_employee())

# run when beat
# @celery.task('')
# def schedule_beat_sync_information_employeer(*args, **kwargs):
#     print("BEAT SCHEDULE")
#     loop.run_until_complete(sync_information_employee())

    
    
