#!/bin/bash

docker build . -t test:latest

docker container run \
  docker.io/jwilder/dockerize \
  -wait tcp://caddy:80 \
  -wait-retry-interval 2s \
  -timeout 20s

docker container run test:latest
