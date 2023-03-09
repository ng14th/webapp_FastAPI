# Rabbit Exchange
EXCHANGE_USER = 'exchange_user'
EXCHANGE_TASK_QUEUE = 'exchange_task_queue'
EXCHANGE_TASK_API = 'exchange_task_api'
EXCHANGE_TASK_CELERY = 'exchange_task_celery'
# Type exchange rabbitmq
TYPE_DIRECT = 'direct'
TYPE_FANOUT = 'fanout'
TYPE_HEADERS = 'headers'
TYPE_TOPIC = 'topic'
TYPE_DLX = 'dlx'
# TUPLE exchange rabbitmq
TUPLE_TYPE_EXCHANGE = (TYPE_DIRECT, TYPE_FANOUT, TYPE_HEADERS, TYPE_TOPIC, TYPE_DLX)
# BIND Queue Name
BIND_QUEUE_SYNC_USER = 'task_ex_user_sync_user'
BIND_QUEUE_DELETE_USER = 'task_ex_user_delete_user'
BIND_QUEUE_NOTI_USER = 'task_ex_user_noti_user'
BIND_QUEUE_CHANGE_PASSWORD = 'task_ex_change_password'
# Routing key
ROUTING_KEY_SYNC_USER = 'trigger_sync_user'
ROUTING_KEY_DELETE_USER = 'trigger_delete_user'
ROUTING_KEY_NOTI_USER = 'trigger_noti_user'
ROUTING_KEY_CHANGE_PASSWORD = 'trigger_change_password'
# Consumer
CONSUMER_HANDLER_USER_TASK = 'consumer_handler_user_task' 
CONSUMER_HANDLER_API_TASK = 'consumer_handler_api_task'
CONSUMER_HANDLER_CELERY_TASK = 'consumer_handler_celery_task'