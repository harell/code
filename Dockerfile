FROM python:3.9-slim-buster

RUN apt-get update -qq && apt-get -y --no-install-recommends install \
    build-essential \
    git

COPY requirements.txt /tmp/
RUN pip install -r /tmp/requirements.txt

RUN mkdir -p /src
COPY src/ /src/
RUN pip install -e /src
COPY tests/ /tests/

WORKDIR /src
