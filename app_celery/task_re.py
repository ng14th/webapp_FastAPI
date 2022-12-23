from app_celery.celery_re import celery as celery2
from app.core.database.redis import redis
from app.tools.tools import _dumps_dict_for_hash_map
import asyncio
from datetime import datetime

loop = asyncio.get_event_loop()


async def create_hash_data_employee_in_redis(data):
    name = f'sync_information_employeee__{data.get("tenant_id")}__{data.get("username")}'
    mapping = _dumps_dict_for_hash_map(data)
    print(mapping)
    await redis.hset(name=name, mapping=mapping)
    return mapping

async def sync_information_employee(data):
    await create_hash_data_employee_in_redis(data)
 
async def set_time_example_for_beat_in_redis():
    await redis.set("time",str(datetime.utcnow()))
       

@celery2.task(name='sync_list_user')
def auto_sync_list_employee_from_fast_api(*args, **kwargs):
    loop.run_until_complete(sync_information_employee(kwargs))
    print("Done")
    
# run when beat
@celery2.task(name='sync_time_by_beat')
def schedule_beat_sync_information_employeer(*args, **kwargs):
    
    print("BEAT SCHEDULE")
    loop.run_until_complete(set_time_example_for_beat_in_redis())

 
    

