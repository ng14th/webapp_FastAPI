#!/bin/bash
# example: run_dev.sh dev will use dev.env file

base_dir=$(pwd)

run_command="celery -A $base_dir.app_celery.task_re beat -l info"

echo "$run_command"
eval $run_command