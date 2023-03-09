from kombu import Connection, Consumer, Exchange, Queue
from app.config import settings
from app.core.abstractions.singleton import SingletonClass
from typing import Callable

import asyncio
loop = asyncio.get_event_loop()


class RabbitMQ(SingletonClass):
    def _singleton_init(self, **kwargs):
        self.rmq_server = None
        self.rmq_channel = None
        self.username = settings.RMQ_USERNAME
        self.password = settings.RMQ_PASSWORD
        self.virtual_host = settings.RMQ_VIRTUAL_HOST
        self.args = None
        

    def initialize_rmq(
        self,
        rmq_url = f'{settings.RMQ_TCP}://{settings.RMQ_USERNAME}:{settings.RMQ_PASSWORD}@{settings.RMQ_URL}/{settings.RMQ_VIRTUAL_HOST}',
        ):
        try:
            self.rmq_server = Connection(rmq_url)
            if self.rmq_server:
                print(f'Connected with RabbitMQ wiht user {self.username} and virtualhost {self.virtual_host}')
                self.rmq_channel = self.rmq_server.channel()
                print(f'Created connection with channel {self.rmq_channel}')
                return self.rmq_server, self.rmq_channel
        except Exception as e:
            print(5*"@#")
            print(f'Connect with RabbitMQ got error {e}')
            print(5*"@#")
            return None
        
    def release_connection(self):
        self.rmq_server.release()
    
    def create_exchange_and_bind_queue(self,name_exchange : str, type : str = "direct",queue : str =""):
        if type not in ("direct","fanout","headers","topic","dlx"):
            print(40*"@#!@")
            print("Type exchange of RabbitMQ must in direct, fanout, headers, topic, dlx")
            print(40*"@#!@")
            return
        print(self.rmq_channel)
        exchange = Exchange(name=name_exchange,
                            type=type,
                            durable= True,
                            channel=self.rmq_channel
                            )
        queue_name = f'queue_{queue}'
        queue_name = Queue(
            name=queue_name,
            exchange=exchange,
            routing_key=f'key_{queue}',
            message_ttl=600,
            queue_arguments={
                'x-queue-type': 'classic'
            },
            durable=True)
        queue_name.bind(self.rmq_channel)
        
        return queue_name
    
    def create_queue(self, queue_name : str,exchange : str = None):
        print(self.rmq_channel, self.rmq_server)
        queue = Queue(name=queue_name, durable= True, exchange= None)
        queue.declare(channel=self.rmq_channel)
        return queue
    
    def create_exchange(self,exchange_name : str, type : str):
        exchange = Exchange(
            name=exchange_name,
            type=type,
            channel=self.rmq_channel
        )
        exchange.declare()
        return exchange
    
    # create consumer to handler message and process message 
    def handler_consumer(self,channel, callback : Callable,name_exchange : str, type : str = "direct",queue : str ="",name_consumer : str = ""):
        
        consumer = Consumer(channel=channel,
                            queues=[self.create_exchange_and_bind_queue(name_exchange,type,queue)],
                            callbacks=callback,
                            accept=['json'],
                            no_ack=False,
                            prefetch_count=2,
                            tag_prefix=name_consumer)
        return consumer
    
    # def handler_process_message_from_queue(self, queue : Queue, callback: Callable):
    #     channel = self.rmq_server.channel()
    #     print(channel)
    #     queue.bind(channel)
    #     consumer = queue.consume(callback=callback)
    #publish a message to exchange with routing key -> send message to bind queue have registed
    def publish_message_exchange(self, message, exchange, routing_key):
        producer = self.rmq_server.Producer()
        try :
            producer.publish(
                body = message,
                exchange = exchange,
                routing_key = routing_key,
                serializer='json'
                )
        finally:
            self.rmq_channel.close()
            
    def publish_message_queue(self,message, declare):
        producer = self.rmq_server.Producer()
        print(self.rmq_channel)
        try :
            producer.publish(
                body = message,
                declare=[declare],
                routing_key=declare.name,
                serializer='json'
                )
        finally:
            self.rmq_channel.close()
        
    def handler_message_from_queue(self):
        pass
    
            
            