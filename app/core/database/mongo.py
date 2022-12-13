# -*- coding: utf-8 -*-
import asyncio
from umongo.frameworks import MotorAsyncIOInstance
from motor.motor_asyncio import AsyncIOMotorClient
from app.config import settings

# print(env.APP_DB_MONGO_URI)

client = AsyncIOMotorClient(settings.APP_DB_MONGO_URI)[settings.APP_DB_MONGO_NAME]
# fix mongo connection attached to a different loop
client.get_io_loop = asyncio.get_running_loop
umongo_cnx = MotorAsyncIOInstance(client)