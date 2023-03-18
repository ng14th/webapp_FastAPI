FROM rabbitmq:3.9.11

# Set variables
ARG RABBITMQ_USERNAME=admin
ARG RABBITMQ_PASSWORD=admin
ARG RABBITMQ_VIRTUAL_HOST=vhost

# Enable plugins
RUN rabbitmq-plugins enable rabbitmq_management rabbitmq_prometheus

# Create user
RUN rabbitmqctl add_user $RABBITMQ_USERNAME $RABBITMQ_PASSWORD && \
    rabbitmqctl set_user_tags $RABBITMQ_USERNAME administrator && \
    rabbitmqctl set_permissions -p $RABBITMQ_VIRTUAL_HOST $RABBITMQ_USERNAME ".*" ".*" ".*"

# Expose ports
EXPOSE 5672 15672

# Set node name
ENV RABBITMQ_NODENAME=rabbit@my-rabbitmq

# Start rabbitmq server
CMD ["rabbitmq-server"]