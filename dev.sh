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
fi

cd ./examples/mock/
docker-compose up -d
cd -

docker container run --network mock_web \
  docker.io/jwilder/dockerize \
  -wait tcp://caddy:80 \
  -wait-retry-interval 2s \
  -timeout 20s

docker container run --network mock_web test:latest

