# from fastapi_utils.tasks import repeat_every
# from app.core.celery.task import auto_sync_information


# # @repeat_every(seconds=20)
# # def event_startup_sync_information():
# #     auto_sync_information.delay()


from app.core.database.rabbitmq_kombu import RabbitMQ
from app.core import constants
import asyncio
from fastapi import BackgroundTasks
import time
from kombu import Queue
# from app_celery.task_re import event_startup_handler_consumer_rabbitmq
import threading

loop = asyncio.get_event_loop()

rabbitmq = RabbitMQ()


def event_startup_initialize_rabbitmq():
    return rabbitmq.initialize_rmq()

# def event_startup_queue():
#     rabbitmq.handler_consumer(
#                     channel = rabbitmq.rmq_channel,
#                     callback=[test1],
#                     name_exchange='my_exchange1',
#                     type='direct',
#                     queue="queue2",
#                     name_consumer="linhcute")
    
# def event_startup_exchange():
#     rabbitmq.create_exchange(exchange_name="linhfanout",type="fanout")
    
    


#     message = a.get(rabbitmq.rmq_channel)
#     print(message)
#     message.ack()
    # print(1)
    # print(message)
    # message.ack()
# async def event_startup_create_exchange():
#     await rabbitmq.create_exchange_and_bind_queue(name_exchange='my_exchange1',type='direct',list_queue=['queue1'])
    
    # await rabbitmq.create_exchange("my_exchange",constants.TYPE_DIRECT)
    # await rabbitmq.create_exchange(f'{constants.EXCHANGE_USER}_{constants.TYPE_DIRECT}',constants.TYPE_DIRECT)
    # await rabbitmq.create_exchange(f'{constants.EXCHANGE_USER}_{constants.TYPE_FANOUT}',constants.TYPE_FANOUT)
    # await rabbitmq.create_exchange(f'{constants.EXCHANGE_USER}_{constants.TYPE_HEADERS}',constants.TYPE_HEADERS)
    # await rabbitmq.create_exchange(f'{constants.EXCHANGE_USER}_{constants.TYPE_TOPIC}',constants.TYPE_TOPIC)
# async def event_startup_create_link_queue_and_exchange():
#     # await rabbitmq.create_bind_queue(queue_name = 'task_ex_user_sync_user_direct',
#     #                                  exchange_name = 'exchange_user_direct',
#     #                                  routing_key= '123')
#     await rabbitmq.create_bind_queue(queue_name="my_queue",exchange_name="my_exchange",routing_key="key")
#     # await rabbitmq.create_bind_queue(queue_name = f'{constants.BIND_QUEUE_DELETE_USER}_{constants.TYPE_DIRECT}',
#     #                                  exchange_name = f'{constants.EXCHANGE_USER}_{constants.TYPE_DIRECT}',
#     #                                  routing_key= f'{constants.ROUTING_KEY_DELETE_USER}_{constants.TYPE_DIRECT}')
# # async def event_startup_handler_consumer_rabbitmq():
# #     await rabbitmq.handler_consumer(queue = f'{constants.BIND_QUEUE_DELETE_USER}_{constants.TYPE_DIRECT}',
# #                                     callback = test1,
# #                                     no_ack = True,
# #                                     consumer_tag = f'{constants.CONSUMER_HANDLER_USER_TASK}_delete_user_direct')



events = [v for k, v in locals().items() if k.startswith('event_startup_')]