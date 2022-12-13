#!/bin/bash
cmd_set_poetry_venv_in_project="poetry config virtualenvs.in-project true"
cmd_poetry_install="poetry install"
cmd_poetry_shell="poetry shell"

eval $cmd_set_poetry_venv_in_project
eval $cmd_poetry_install
eval $cmd_poetry_shell

echo "Done root"