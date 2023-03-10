from typing import List
from celery import bootsteps
import kombu
from app.core import constants
from app_celery.celery_re import celery as celery2
from abc import ABC, abstractmethod
import logging

logger = logging.getLogger(f'{__name__}')



class BaseWorker(bootsteps.ConsumerStep):
    def get_consumers(self, channel, **kwargs):
        call_back = kwargs.get('call_back')
        exchange_name = kwargs.get('exchange_name')
        type_exchange = kwargs.get('type_exchange')
        queue_name = kwargs.get('queue_name')
        routing_key = kwargs.get('routing_key')
        
        if call_back is None:
            logger.error("call_back MUST BE DECLARED")
            return None
        if exchange_name is None:
            logger.error("exchange_name MUST BE DECLARED")
            return None
        if type_exchange is None:
            logger.error("type_exchange MUST BE DECLARED")
            return None
        if queue_name is None:
            logger.error("queue_name MUST BE DECLARED")
            return None
        if routing_key is None:
            logger.error("routing_key MUST BE DECLARED")
            return None
        
        with celery2.pool.acquire(block=True) as conn:
            
            exchange = kombu.Exchange(
                name=exchange_name,
                type=type_exchange,
                durable=True,
                channel=conn,
            )
            exchange.declare()
            
            queue = kombu.Queue(
                name=queue_name,
                exchange=exchange,
                routing_key=routing_key,
                channel=conn,
                message_ttl=600,
                queue_arguments={
                    'x-queue-type': 'classic'
                },
                durable=True
            )
            queue.declare()

        consumer = kombu.Consumer(channel,
                                   queues=[queue],
                                   callbacks=[call_back],
                                   accept=['json'])
        return [consumer]

        