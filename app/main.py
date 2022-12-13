from fastapi import FastAPI
from app.config import settings
from app.view import router as employee_router
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



@app.get("/")
async def root():
    
    return {"message": "Hello World"}