import asyncio
import aiormq
from app.config import settings
from typing import Callable
from app.core.exceptions import ErrorResponseException
from app.core.schema.api_response import get_error_code

class RabbitMQ():
    def __init__(self) -> None:
        self.rmq_server = None
        self.rmq_channel = None
        self.username = settings.RMQ_USERNAME
        self.password = ""
        self.virtual_host = settings.RMQ_VIRTUAL_HOST
    
    async def initialize_rmq(
        self,
        rmq_url = f'{settings.RMQ_TCP}://{settings.RMQ_USERNAME}:{settings.RMQ_PASSWORD}@{settings.RMQ_URL}/{settings.RMQ_VIRTUAL_HOST}',
        ):
        try  :
            self.rmq_server = await aiormq.connect(rmq_url)
            if self.rmq_server:
                print(f'Connected with RabbitMQ wiht user {self.username} and virtualhost {self.virtual_host}')
        except Exception as e:
            print(50*"@#")
            print(f'Connect with RabbitMQ got error {e}')
            print(50*"@#")     
        return self.rmq_server
        
    async def get_channel(self, **kwargs):
        if not self.rmq_server:
            self.rmq_server = await self.initialize_rmq()
            self.rmq_channel = await self.rmq_server.channel()
            return self.rmq_channel
        self.rmq_channel = await self.rmq_server.channel()
        return self.rmq_channel
    
    async def create_queue(self, queue_name : str):
        self.rmq_channel = await self.get_channel()
        self
        print(f'Create queue {queue_name}')
        return await self.rmq_channel.queue_declare(queue_name, durable=True)
    
    async def create_bind_queue(self,queue_name: str, exchange_name: str, routing_key: str = ""):
        # if not self.rmq_channel:
        #     self.rmq_channel = await self.get_channel()
        queue = await self.rmq_channel.queue_declare(queue_name, exclusive=True)
        return await self.rmq_channel.queue_bind(
        queue=queue['queue'],
        exchange=exchange_name,
        routing_key=routing_key,
        arguments={'x-match': 'any', 'key1': 'one', 'key2': 'two'})
        # async for message in self.rmq_channel.iterqueue(queue_name=queue["queue"]):
        #     print(f'Nhận dữ liệu {message.body}')
        
    async def handler_consumer(self, queue : str ,callback : Callable ,no_ack : bool, consumer_tag : str ):
        print(f'Start process consumer of {queue} - {callback}')
        await self.rmq_channel.basic_consume(queue=queue,consumer_callback=callback,no_ack=no_ack,consumer_tag=consumer_tag)
    
    async def create_exchange(self,ex :str, type : str ):
        # self.rmq_channel = await self.get_channel()
        if type not in ("direct","fanout","headers","topic","dlx"):
            print(40*"@#!@")
            print("Type exchange of RabbitMQ must in direct, fanout, headers, topic, dlx")
            print(40*"@#!@")
            # raise ErrorResponseException(**get_error_code(9000))
        return await self.rmq_channel.exchange_declare(exchange=ex,exchange_type=type,durable=True)
    
        
        
        
    