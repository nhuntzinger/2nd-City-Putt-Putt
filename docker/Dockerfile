# syntax=docker/dockerfile:1
FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /opt/second-city/code
COPY requirements.txt /opt/second-city/code/
RUN pip install -r requirements.txt
COPY . /opt/second-city/code
