#!/bin/bash

set -e

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

  echo ""
  echo "Running the consent BB mocking application."
  echo ""
  echo "By default, you can reach it on:"
  echo "http://localhost:8080 or https://localhost:8888 (HTTPS)"

  docker-compose up
fi
cd -

if [ "$1" == "test" ]
then
  echo "Running test suites..."
  echo ""
  cd ./test/gherkin
  ./test_entrypoint.sh
  cd -
fi

