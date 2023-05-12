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
fi

cd ./examples/mock/
docker-compose up -d
cd -

# Run gherkin test suite
cd ./test/gherkin
./test_entrypoint.sh
cd -
