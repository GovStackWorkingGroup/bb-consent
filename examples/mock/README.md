# GovStack Consent BB - mock

A stand-alone docker-compose configuration simulating the Consent BB specification.

## Running the mock implementation

The mock application can be run on a local Docker environment using the following command:

```sh
# Run the basic dev.sh script
./dev.sh

# Or run directly from this folder
cd examples/mock/
docker-compose up
```

Once you have the mock application up and running, you can now access several interesting endpoints:

* http://localhost:8000/docs#/default - api docs served directly from the Django App.
* http://localhost:8080/api/ - Base URL root, behind Caddy HTTP proxy.
* http://localhost:8080/api/service/policy/123456/ -
  this is a static endpoint that just returns a policy mock.
  The approach isn't in use, please make sure to notify the Consent BB working group if you need to include static mocks in a test.

The docker compose environment has an HTTP proxy on ``localhost:8080`` and ``localhost:8888`` (HTTPS).
The proxy serves static mocks, but for all dynamic mocks there is a mock application where all other requests are forwarded to.

The mock application sits on ``http://localhost:8000`` (8000 is the default Django development port) and may be accessed directly in cases where you for instance need to see the raw traceback of an error that has occurred. You can access the Django Admin site with credentials ``admin:admin`` on http://localhost:8000/admin.

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
