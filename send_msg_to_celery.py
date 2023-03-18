import asyncio
import aiormq
from app.core.database.rabbitmq_kombu import RabbitMQ
from app.core import constants
from kombu import Producer, Queue
connection = RabbitMQ()

async def main():


# create a queue
    # queue = Queue('myqueue', durable=True)

    # publish a message to the queue
    message1 = {"htype":constants.HTYPE_MAPPING_CLASS_SEND_EMAIL,
                "data" : [{'email':'nguyennt63@fpt.com.vn',
                            "time_exp" : 123}]}
    # message1 = [{'email':'nguyennt63@fpt.com.vn',
    #              "time_exp" : 123}]
    # b = event_startup_queue()
    # connection.publish_message_queue(message1,b)
    server, channel = connection.initialize_rmq()
    connection.publish_message_exchange(message1,constants.EXCHANGE_TASK_CELERY,constants.ROUTING_KEY_NOTI_USER)
    server.close()
                    
if __name__ == "__main__":
    asyncio.run(main())


