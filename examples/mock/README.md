# GovStack Consent BB - mock

A stand-alone docker-compose configuration simulating the Consent BB
specification.

## Running the mock implementation

The mock application can be run on a local Docker environment using the
following command:

```
docker-compose up
```

After this, you can visit for instance https://localhost:8888/api/org/policy/ --
notice that Caddy produces a self-signed SSL certificate that you have to
accept.

## Components of the mock app

- An HTTP server (Caddy)
- The Consent BB OpenAPI spec
- A Caddy module for validating OpenAPI specs (caddy-openapi)
- Mocked static responses for static endpoints
- A mock application written in Django for dynamic endpoints
