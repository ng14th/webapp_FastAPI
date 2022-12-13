#!/bin/bash
# example: run_dev.sh dev will use dev.env file

base_dir=$(pwd)
python_path="$base_dir/.venv/bin/python"

run_command="$python_path run_app.py"

echo "$run_command"
eval $run_command