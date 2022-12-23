#!/bin/bash
# example: run_dev.sh dev will use dev.env file

base_dir=$(pwd)

run_command="celery -A app_celery.task_re worker --loglevel=info"

echo "$run_command"
eval $run_command