from fastapi import FastAPI, Request
from app.config import settings
from app.view import router as employee_router
from fastapi.responses import JSONResponse, HTMLResponse
from app.core.exceptions import ErrorResponseException

app = FastAPI(
    title=settings.APP_PROJECT_NAME,
    docs_url= settings.APP_DOCS_URL,
    openapi_url='/api/openapi.json'
)

for router in (
    {'module': employee_router, 'prefix': '/employee', },
):
    print(router)
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

@app.get("/")
async def root():
    
    return {"message": "Hello World"}