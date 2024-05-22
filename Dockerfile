# set base image (host OS)
FROM python:3.12-slim as base

# Setup env
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8

# Python
# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE 1
# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED 1
# enable Python tracebacks on segfaults
ENV PYTHONFAULTHANDLER 1

# Poetry
# https://python-poetry.org/docs/configuration/#using-environment-variables
ENV POETRY_VERSION=1.8.3

# make poetry install to this location
ENV POETRY_HOME="/opt/poetry"

# do not ask any interactive question
ENV POETRY_NO_INTERACTION=1

# never create virtual environment automaticly, only use env prepared by use
ENV POETRY_VIRTUALENVS_CREATE=false

# this is where our requirements + virtual environment will live
ENV VIRTUAL_ENV="/venv"

# prepend poetry and venv to path
ENV PATH="$POETRY_HOME/bin:$VIRTUAL_ENV/bin:$PATH"

# prepare virtual env
RUN python -m venv $VIRTUAL_ENV

# working directory and Python path
WORKDIR /app

ENV PYTHONPATH="/app:$PYTHONPATH"


FROM base AS builder-base

RUN \
  apt-get update && \
  apt-get install -y curl ca-certificates build-essential

# install poetry - respects $POETRY_VERSION & $POETRY_HOME
# The --mount will mount the buildx cache directory to where
# Poetry and Pip store their cache so that they can re-use it
RUN --mount=type=cache,target=/root/.cache \
    curl -sSL https://install.python-poetry.org | python -

# used to init dependencies
WORKDIR /app

# copy the dependencies file to the working directory
COPY poetry.lock pyproject.toml ./

# install runtime deps to $VIRTUAL_ENV
RUN --mount=type=cache,target=/root/.cache \
    poetry install --no-root --only main

FROM base as runtime

RUN \
  apt-get update && \
  apt-get install -y gettext-base

LABEL maintainer="fleer"

ENV STAGE prod

ARG BUILD_VERSION="0.0.0-dev"
ENV VERSION=$BUILD_VERSION

EXPOSE 8000

# used to init dependencies
WORKDIR /app

RUN DEBIAN_FRONTEND=noninteractive apt-get update && \
    apt-get install -y --no-install-recommends \
    ca-certificates \
    libpq-dev && \
    apt-get clean

# copy in our built poetry + venv
COPY --from=builder-base $POETRY_HOME $POETRY_HOME
COPY --from=builder-base $VIRTUAL_ENV $VIRTUAL_ENV

# copy the content of the local src directory to the working directory
COPY service/ ./service/
COPY config/ ./config/
COPY replace_placeholders.sh .
COPY README.md .


ENTRYPOINT [ "sh", "./replace_placeholders.sh" ]
# command to run on container start
CMD uvicorn service.api:app --host 0.0.0.0 --port 8000
