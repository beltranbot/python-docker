FROM python:3

RUN useradd -u 1000 python

RUN mkdir /app

RUN chown python:python /app

RUN mkhomedir_helper python

ENV PATH="/home/python/.local/bin:${PATH}"

USER python

RUN python -m pip install -U autopep8
