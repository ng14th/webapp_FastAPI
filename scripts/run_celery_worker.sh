#!/bin/bash
# example: run_dev.sh dev will use dev.env file

base_dir=$(pwd)

run_command="celery -A app_celery.email_worker worker --loglevel=info"

echo "$run_command"
echo "$base_dir"
eval $run_command