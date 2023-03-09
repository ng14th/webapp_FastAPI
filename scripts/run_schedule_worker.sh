#!/bin/bash
# example: run_dev.sh dev will use dev.env file

base_dir=$(pwd)

run_command="celery -A app_celery.schedule_worker worker --loglevel=info --concurrency=1"

echo "$run_command"
eval $run_command