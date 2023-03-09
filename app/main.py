from fastapi import FastAPI, Request, BackgroundTasks
from app.config import settings
from app.user.view import router as employee_router
from app.login import router as login_router
from fastapi.responses import JSONResponse, HTMLResponse
from app.core.exceptions import ErrorResponseException
from app.core.startup_events.startup import events as event_startup
from app.core.shutdown_events.shutdown import events as event_shutdown
from fastapi.middleware.cors import CORSMiddleware
import logging

from app.core.database.rabbitmq_kombu import RabbitMQ
from app.core import constants
import asyncio
from fastapi import BackgroundTasks
import time
from kombu import Queue
import threading

rabbitmq = RabbitMQ()

log = logging.getLogger(__name__)

app = FastAPI(
    title=settings.APP_PROJECT_NAME,
    docs_url= settings.APP_DOCS_URL,
    openapi_url='/api/openapi.json',
    on_startup = event_startup,
    on_shutdown=event_shutdown,
)

app.add_middleware(CORSMiddleware,
                   allow_origins=["http://localhost:800*","*"],
                   allow_methods = ["POST", "GET", "DELETE", "PUT"],
                   allow_credentials = True,
                   allow_headers = ["*"])
for router in (
    {'module': employee_router, 'prefix': '/user',},
    {'module': login_router, 'prefix': '/login',},
):

    app.include_router(
        router.get('module'),
        prefix=router.get('prefix'),
        tags = router.get('tags')
    )


@app.exception_handler(ErrorResponseException)
async def error_response_exception_handler(request: Request, exception: ErrorResponseException):
    return JSONResponse(
        status_code=exception.status_code,
        content={
            "success": exception.success,
            "data": exception.data,
            "length": exception.length,
            "error": exception.error,
            "error_code": exception.error_code
        },
    )

# rabbitmq.initialize_rmq()

@app.get("/")
async def root():    
    
    return {"message": "Hello World"}


    