from app.core.database.rabbitmq_kombu import RabbitMQ

rabbitmq = RabbitMQ()
        
async def event_shutdown_disconnect_rabbit_mq():
    await rabbitmq.release_connection()

events = [v for k, v in locals().items() if k.startswith('event_shutdown_')]
        

