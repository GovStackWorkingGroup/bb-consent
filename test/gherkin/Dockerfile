FROM python:3.8

COPY requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

COPY . /tests

WORKDIR /tests/

#ENV CONSENTBB_API_HOST=localhost:8080
ENV CONSENTBB_API_HOST=localhost:8888
ENV CONSENTBB_API_PATH=/api

CMD pytest --cucumberjson=/data/results.json /tests
