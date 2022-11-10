# Consent BB test suite

This folder contains containerized test applications that verify the
Consent BB specification against a deployment specified in the `examples/`
folder of this repository.

The test applications receive two environment variables:

```
CONSENTBB_API_HOST="hostname"  # for instance the name of a docker container
CONSENTBB_API_PATH="/api/"  # the root location of the API to be called on the host
```

This entire setup also comes with a Circle CI configuration which you may refer to
in `.circleci/config.yml`

## Gherkin test application

You can execute the Gherkin tests by building and running the container:

```
cd gherkin
docker build -t consentgherkin:latest .
docker run consentgherkin --network consent-web1 consentgherkin
```

Notice that we are connecting the test application to a docker network. This network
is where the example or mock application runs and is reachable.
