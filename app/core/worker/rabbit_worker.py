from .base import BaseWorker
from app.core import constants
import asyncio


async def test(message):
    print("Received message:", message.body.decode())



class RabbitWorker(BaseWorker):
    worker_type = "RabbitWorker"
    def __init__(self) -> None:
        super().__init__()
    
    
        
    async def handler_consumer_rabbit(self):
        await self.handler_consumer(
            queue= f'{constants.BIND_QUEUE_SYNC_USER}_{constants.TYPE_DIRECT}',
            callback= test,
            no_ack= True,
            consumer_tag= self._generate_worker_name()
        )
    
    async def run(self):
        await asyncio.gather(
            *(getattr(self, i)() for i in {
                "handler_consumer_rabbit",
            })
        )
        