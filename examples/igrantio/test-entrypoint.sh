#!/bin/bash
set +e

docker-compose -f docker-compose.yaml up -d mongo postgresql keycloak api caddy

CONTAINER_API="api"
TIMEOUT=120  # Timeout value in seconds
WAIT_INTERVAL=1  # Interval to check

# Wait for Consent BB API to start
echo "Waiting for Consent BB API to start..."
elapsed_time=0

while [ $elapsed_time -lt $TIMEOUT ]; do
    if docker logs "$CONTAINER_API" 2>&1 | grep -q "Listening port 80"; then
        echo "Consent BB API started!"
        docker-compose -f docker-compose.yaml up fixtures
        break
    else
        sleep $WAIT_INTERVAL
        elapsed_time=$((elapsed_time + WAIT_INTERVAL))
    fi
done

if [ $elapsed_time -ge $TIMEOUT ]; then
    echo "Timeout: Consent BB API did not start within $TIMEOUT seconds."
    exit 1
fi
