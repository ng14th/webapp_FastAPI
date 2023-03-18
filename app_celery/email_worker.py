from app_celery.celery_re import celery as celery2
import asyncio
from app.core import constants
import kombu
from app_celery.worker.base_consumer import BaseWorker

loop = asyncio.get_event_loop()
class PasswordNotificationWorker(BaseWorker):

    def get_consumers(self, channel):
        exchange_name = constants.EXCHANGE_TASK_CELERY
        type_exchange = constants.TYPE_DIRECT
        queue_name = constants.BIND_QUEUE_NOTI_USER
        routing_key = constants.ROUTING_KEY_NOTI_USER

        return super().get_consumers(channel,
                                     exchange_name=exchange_name, 
                                     type_exchange=type_exchange, 
                                     queue_name=queue_name, 
                                     routing_key=routing_key)
# class PasswordNotificationWorker1(BaseWorker):

#     def get_consumers(self, channel):
#         call_back = password_notification
#         exchange_name = constants.EXCHANGE_TASK_CELERY
#         type_exchange = constants.TYPE_DIRECT
#         queue_name = "123"
#         routing_key = "456"
#         return super().get_consumers(channel,
#                                      call_back = call_back,
#                                      exchange_name=exchange_name, 
#                                      type_exchange=type_exchange, 
#                                      queue_name=queue_name, 
#                                      routing_key=routing_key)
            
# setting consumer
celery2.steps['consumer'].add(PasswordNotificationWorker)
# celery2.steps['consumer'].add(PasswordNotificationWorker1)


# from app_celery.celery_re import celery as celery2
# import asyncio
# from app.core import constants
# from celery import shared_task, Task, bootsteps
# from app_celery.processor_handler_send_email import password_notification, handler_email
# import kombu


# loop = asyncio.get_event_loop()


# @celery2.task(name ="schedule_send_msg_noti_password")
# def schedule_send_msg_noti_password():
#     loop.run_until_complete(handler_email.send_msg_to_email_worker())



# with celery2.pool.acquire(block=True) as conn: 
#     exchange = kombu.Exchange(
#         name=constants.EXCHANGE_TASK_CELERY,
#         # name = 'exchange_task_celery'
#         type=constants.TYPE_DIRECT,
#         durable=True,
#         channel=conn,
#     )
#     exchange.declare()
#     # queue webhook facebook
#     queue_noti = kombu.Queue(
#         name=constants.BIND_QUEUE_NOTI_USER,
#         # queue_nbame = 'task_ex_user_noti_user'
#         exchange=exchange,
#         routing_key=constants.ROUTING_KEY_NOTI_USER,
#         # routing_key = 'trigger_noti_user'
#         channel=conn,
#         message_ttl=600,
#         queue_arguments={
#             'x-queue-type': 'classic'
#         },
#         durable=True
#     )
#     queue_noti.declare()
    
#     # queue_change_password = kombu.Queue(
#     #     name=constants.BIND_QUEUE_CHANGE_PASSWORD,
#     #     # queue_nbame = 'task_ex_user_delete_user'
#     #     exchange=exchange,
#     #     routing_key=constants.ROUTING_KEY_CHANGE_PASSWORD,
#     #     # routing_key = 'trigger_change_password'
#     #     channel=conn,
#     #     message_ttl=600,
#     #     queue_arguments={
#     #         'x-queue-type': 'classic'
#     #     },
#     #     durable=True
#     # )
#     # queue_change_password.declare()

# class BasicConsumer(bootsteps.ConsumerStep):
#     def get_consumers(self, channel):
#         consumer_noti = kombu.Consumer(channel,
#                                        queues=[queue_noti],
#                                        callbacks=[password_notification],
#                                        accept=['json'])
#         # consumer_change_password = kombu.Consumer(channel,
#         #                                queues=[queue_change_password],
#         #                                callbacks=[change_password_exp],
#         #                                accept=['json'])
#         return [consumer_noti]
# # setting consumer
# celery2.steps['consumer'].add(BasicConsumer)