#!/bin/bash
# example: run_dev.sh dev will use dev.env file

base_dir=$(pwd)

run_command="celery -A app_celery.task_re flower --address=172.27.230.25 --port=8090"

echo "$run_command"
eval $run_command