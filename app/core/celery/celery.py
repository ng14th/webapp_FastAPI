from celery import Celery
from celery.schedules import crontab
from app.config import settings
from datetime import timedelta

celery = Celery('hello', backend=settings.BACKEND_URL, broker=settings.BROKER_URL)

celery.backend.cleanup()
# Disable task result save in redis
celery.conf.task_ignore_result = False
celery.conf.task_store_errors_even_if_ignored = True
celery.conf.timezone = 'UTC'

#Conf BEAT SCHEDULE FOR CELERY
# celery.conf.beat_schedule = {
#     'Sync Information Employeer BEAT' : {
#         'task' : 'app.core.celery.task.schedule_beat_sync_information_employeer',
#         'schedule' : 10.0,
#         # 'schedule': crontab(hour=7, minute=30, day_of_week=1)
#     },
# }