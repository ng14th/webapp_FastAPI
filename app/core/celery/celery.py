from celery import Celery
from app.config import settings
from datetime import timedelta

celery = Celery('hello', backend=settings.BACKEND_URL, broker=settings.BROKER_URL)

celery.backend.cleanup()
# Disable task result save in redis
celery.conf.task_ignore_result = True
celery.conf.task_store_errors_even_if_ignored = True


# celery.conf.update(
# #     result_expires=timedelta(hours=1),
# )