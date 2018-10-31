FROM python:3.6-slim-stretch

ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8

WORKDIR /home/app

RUN pip3 install -U pip
RUN pip3 install pipenv

COPY Pipfile Pipfile
COPY Pipfile.lock Pipfile.lock
COPY boot.sh boot.sh

RUN pipenv install --deploy --system

EXPOSE 5000
ENTRYPOINT ['./boot.sh']