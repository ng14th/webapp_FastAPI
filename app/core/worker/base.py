from app.core.database.rabbitmq import RabbitMQ
import random

class BaseWorker(RabbitMQ):
    worker_type: str = 'base'
    def __init__(self) -> None:
        pass
    
    def _generate_worker_name(self) -> str:
        random_name = ''
        for i in range(10):
            random_name += chr(random.randint(97, 122))
        random_name = random_name.capitalize()
        return f'{self.worker_type}-{random_name}'
    