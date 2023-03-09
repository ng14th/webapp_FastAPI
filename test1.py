from app.user.models.user import User
import asyncio
from app.core.verify.token import hass_password
from datetime import datetime, timedelta

loop = asyncio.get_event_loop()

async def sync_password_expr(time_now : float):
    new_password = hass_password("1234")
    datenow = datetime.utcnow() + timedelta(days=30)
    timestamps = datetime.timestamp(datenow)
    
    query = {'password_expr':{'$lte':str(time_now)}}
    update = {"$set":{"password": new_password,
                      "paswword_expr": str(timestamps)}}
    update_password = await User.collection.update_one(
        query,
        update,
        upsert = False
    )

    return True

loop.run_until_complete(sync_password_expr(1680083037))

