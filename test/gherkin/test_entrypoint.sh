#!/bin/bash

set -e

sleep 2s

# Waits for the application to be responsive.
# We could do a more thorough healthcheck once more
# is know/specified about what being 'ready' means.
docker container \
  run \
  --network host \
  --rm \
  docker.io/jwilder/dockerize \
  -wait tcp://localhost:8888 \
  -wait-retry-interval 2s \
  -timeout 20s \

# Once the container is ready, we need to wait a bit more
# TODO: Replace this with some real wait command, since our mock
# application is returning 502s in the beginning
sleep 2s

mkdir -p test-data-volume

docker-compose up --build

mkdir -p ./result
cp ./test_data/results.json ./result/example_result.message
