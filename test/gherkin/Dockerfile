FROM python:3.10

COPY requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

COPY ./features /tests

WORKDIR /tests/

#ENV CONSENTBB_API_HOST=localhost:8080
ENV CONSENTBB_API_HOST=localhost:8888
ENV CONSENTBB_API_PATH=/api

CMD behave --format json --summary --outfile=/data/results.json /tests
