#!/bin/bash
# example: run_dev.sh dev will use dev.env file

base_dir=$(pwd)

run_command="celery -A app.core.celery.task worker --loglevel=info"

echo "$run_command"
eval $run_command