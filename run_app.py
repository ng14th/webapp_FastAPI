# -*- coding: utf-8 -*-
import argparse
import sys
import os
import uvloop
import uvicorn
from app.config import settings


uvloop.install()

# --------------ATTENTION--------------

# os.environ['DEV'] = "True"
# os.environ['ENV_NAME'] = 'your_env_file_name_here'

# to use your environment
# use command "export ENV_NAME=your_name"

# to use production environment
# use command "unset ENV_NAME"

if __name__ == '__main__':
    uvicorn.run(
        'app.main:app',
        loop='uvloop',
        reload=True,
        host=settings.GUNICORN_HOST,
        port=int(settings.GUNICORN_PORT),
        timeout_keep_alive=0 
    )
