from celery import Celery
from celery.schedules import crontab
from app.config import settings
from datetime import timedelta
from celery.utils.imports import symbol_by_name
from celery import shared_task
from celery.worker.consumer import Consumer
from time import sleep
from app.core import constants

celery = Celery('hello', backend='rpc://', broker="amqp://admin:admin@172.27.230.14:5672/nguyennt63")

celery.backend.cleanup()
# Disable task result save in redis
celery.conf.task_ignore_result = True
celery.conf.task_store_errors_even_if_ignored = True
celery.conf.timezone = 'UTC'

celery.conf.task_always_eager = False
celery.conf.task_eager_propagates = False
celery.conf.worker_loop = 'asyncio'

#Conf BEAT SCHEDULE FOR CELERY
celery.conf.beat_schedule = {
    'Sync Information Employeer BEAT' : {
        'task' : 'schedule_send_msg_noti_password',
        'schedule' : 15.0,
        # 'schedule': crontab(hour=7, minute=30, day_of_week=1)
    },
}

# @celery.task(name = "schedule_send_msg_noti_password")
# def test():
#     pass