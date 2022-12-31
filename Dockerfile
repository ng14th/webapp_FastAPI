FROM python:3.9-slim-bullseye

ENV http_proxy=http://proxy.fpt.vn:80
ENV https_proxy=http://proxy.fpt.vn:80
ENV no_proxy=172.27.230.14,localhost,127.0.0.1

RUN mkdir /fastapi_app
WORKDIR /fastapi_app

RUN pip install poetry
RUN poetry --version
RUN pip install celery
RUN pip install pydantic
RUN pip install pydantic[dotenv]
RUN pip install redis
RUN pip install aioredis
RUN pip install ujson



COPY ./app /fastapi_app/app
COPY ./app_celery /fastapi_app/app_celery
COPY ./scripts /fastapi_app/scripts
COPY ./tests /fastapi_app/tests
COPY ./poetry.lock /fastapi_app/
COPY ./pyproject.toml /fastapi_app/
COPY ./run_app.py /fastapi_app/



COPY .env /fastapi_app


RUN ./scripts/initialize_project.sh
RUN poetry update 




