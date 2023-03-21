from typing import List
from celery import bootsteps
import kombu
from app.core import constants
from app_celery.celery_re import celery as celery2
import logging
from . import process_send_email
logger = logging.getLogger(f'{__name__}')


handler_packet = (process_send_email, )


class BaseWorker(bootsteps.ConsumerStep):
    
    def search_classes_by_htype(self, modules, type_search):
        matching_classes = []
        for module in modules:
            for attribute_name in dir(module):
                attribute = getattr(module, attribute_name)
                if isinstance(attribute, type):
                    try:
                        if attribute.htype == type_search:
                            matching_classes.append(attribute)
                    except AttributeError:
                        pass
        return matching_classes
    
    
    def handler_message(self, body, message, **kwargs):
        try:
            htype = body.get('htype')
            data = body.get('data')
            matching_classes = self.search_classes_by_htype(handler_packet, htype)
            if matching_classes:
                for class_obj in matching_classes:
                    handler_instance = class_obj()
                    handler_instance.handler(data, message)
            else:
                logger.error(f"No classes found in the modules with htype attribute {body.get('htype')}")
                message.ack()
        except Exception as e:
            message.ack()
            logger.error(f'handler message {message} got error {e}')
            
            
    def get_consumers(self, channel, **kwargs):
        exchange_name = kwargs.get('exchange_name')
        type_exchange = kwargs.get('type_exchange')
        queue_name = kwargs.get('queue_name')
        routing_key = kwargs.get('routing_key')
        
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
                                   callbacks=[self.handler_message],
                                   accept=['json'])
        return [consumer]

        