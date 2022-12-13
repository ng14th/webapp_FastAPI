import aioredis 
from app.config import settings


redis = aioredis.from_url(url = f"redis://{settings.REDIS_URL}", db = settings.REDIS_DB)
