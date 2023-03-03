#!/bin/bash

echo "Consent BB development script"
echo ""
echo "This runs a developer-version of what happens in the Circle CI configuration."

if [ "$1" == "build" ]
then
  cd ./test/gherkin/
  docker build . -t test:latest
  cd -
  cd ./examples/mock/
  docker-compose build
  cd -
  exit
fi

cd ./examples/mock/

if [ "$1" == "test" ]
then
  docker-compose up -d
else
  docker-compose up
fi
cd -


docker container run --network mock_web \
  docker.io/jwilder/dockerize \
  -wait tcp://caddy:80 \
  -wait-retry-interval 2s \
  -timeout 20s

echo ""
echo "Consent BB mocking application is ready and responsive"
echo ""
echo "Navigate to:"
echo "http://localhost:8080 or https://localhost:8888 (HTTPS)"

if [ "$1" == "test" ]
then
  echo "Running the tests"
  docker container run --network mock_web test:latest
fi
