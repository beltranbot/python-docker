FROM python:3.11-rc-bullseye

RUN useradd -u 1000 python

RUN mkdir /app

RUN chown python:python /app

USER python
