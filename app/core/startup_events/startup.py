from fastapi_utils.tasks import repeat_every
from app.core.celery.task import auto_sync_information


@repeat_every(seconds=20)
def event_startup_sync_information():
    auto_sync_information.delay()


events = [v for k, v in locals().items() if k.startswith('event_startup_')]