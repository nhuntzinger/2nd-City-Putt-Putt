# syntax=docker/dockerfile:1
FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /opt/second-city/code
COPY requirements.txt /opt/second-city/code/
RUN pip install -r requirements.txt
# Second COPY statement so that when code is updated it rebuilds from
# here without running pip install again
COPY . /opt/second-city/code
EXPOSE 8000
CMD [ "./entry_point.sh" ]
