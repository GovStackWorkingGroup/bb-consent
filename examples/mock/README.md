# GovStack Consent BB - mock

A stand-alone docker-compose configuration simulating the Consent BB specification.

## Running the mock implementation

The mock application can be run on a local Docker environment using the following command:

```
docker-compose up
```

After this, you can visit for instance https://localhost:8888/api/service/policy/ -- notice that Caddy produces a self-signed SSL certificate that you have to accept.

## Components of the mock app

- An HTTP server (Caddy)
- The Consent BB OpenAPI spec
- A Caddy module for validating OpenAPI specs (caddy-openapi)
- Mocked static responses for static endpoints
- A mock application written in Django for dynamic endpoints


## Notes

The entire repository root becomes build context for the mock application, otherwise source files would have to be linked or managed in multiple locations.

Invalid JSON responses will trigger a rather cryptic blank 500 error.
This is because the OpenAPI validator doesn't return a proper error page.
Check the Docker output in your commandline.

For development to be efficient, we link the following resources in a volume, so you don't have to rebuild the Docker containers each time:

* `caddy/Caddyfile` - the main Caddy configuration.