# Consent Building Block (Govstack)

[![CircleCI](https://circleci.com/gh/GovStackWorkingGroup/bb-consent.svg?style=shield)](https://circleci.com/gh/GovStackWorkingGroup/bb-consent)
[![latest spec on GitBook](https://img.shields.io/badge/GitBook-Latest-blue.svg?style=flat)](https://govstack.gitbook.io/bb-consent/)
[![last commits](https://img.shields.io/github/last-commit/GovStackWorkingGroup/bb-consent?style=flat)](../commits/)
[![open issues](https://img.shields.io/badge/jira-open%20issues-green.svg?style=flat)](https://govstack-global.atlassian.net/jira/software/c/projects/CON/issues)
[![license](https://img.shields.io/badge/License-Apache%202.0-green.svg?style=flat)](./LICENSE/)

<!--TODO: Update the TOC-->
<p>
  <a href="#about">About</a> •
  <a href="#release-status">Release Status</a> •
  <a href="#core-team">Core Team</a> •
  <a href="#contributing">Contributing</a> •
  <a href="#consent-specs-in-gitbook">Specification</a> •
  <a href="#repo-structure">Repo structure</a>
  <a href="#devsh">Development</a>
</p>

## About

Consent BB defines the principles, functions and architecture of an information system that enables services for individuals to approve the use of her/his personal data and for information system operators that process personal data of individuals to know the will of the individual and legitimately process such personal data.

It is a process-oriented GovStack BB facilitating auditable bilateral agreement within a multi-agent environment, that integrates with most other BBs.

This repository contains the deliverables from Consent BB team, as part of the Govstack project.

## Core Team

* Ain Aaviksoo ([ain.aaviksoo@guardtime.com](ain.aaviksoo@guardtime.com))
* Benjamin Balder Bach ([balder@overtag.dk](balder@overtag.dk)) 
* Philippe Page ([philippe.page@humancolossus.org](philippe.page@humancolossus.org))
* Lal Chandran ([lal@igrant.io](lal@igrant.io))

Working Group Representative: Ramkumar ([psramkumar2@gmail.com](psramkumar2@gmail.com))

## Release Status

All diagrams and API specifications contained here are subject to ongoing changes by a GovStack Working Group.
You can find more details about our release history and roadmap in the specification itself:

https://govstack.gitbook.io/bb-consent/

## Contributing

Feel free to improve the plugin and send us a pull request. If you found any problems, please create an issue in our Jira project: https://govstack-global.atlassian.net/jira/software/c/projects/CON/issues

## Consent specs in Gitbook

Govstack specs are published at [Gitbook - Govstack Global](https://docs.govstack.global/).

You may view the Consent BB's latest publication directly on [https://govstack.gitbook.io/bb-consent/](https://govstack.gitbook.io/bb-consent/).

Note that pushes to the `main` branch will automatically trigger a Gitbook build
and deployment from the `/spec` directory.

## Repo Structure

```sh
README.md
/dev.sh # A utility script for the Consent BB, see README.md
/spec # the markdown files which are used to build the specification in GitBook
/api # the openapi specification
/test # the test plan and tests
  plan.md
/examples # examples for deploying, configuring, and testing applications which implement the behaviors specified by this building block
  /mock
    README.md # instructions for deployment/testing
    docker-compose.yaml # example deployment file
      db
      web
      adaptor
      security-server
    Caddyfile # example config for "adaptor"
    Dockerfile # dockerfile to build "adaptor"
  /application-a
  /application-b
  /application-c
```


## dev.sh

This file is written to closely reproduce the same environment that otherwise runs on Circle CI.
The intention is to help with shortcuts for local demos and development of the mock application and test suites.

```sh
# Auto-generate all OpenAPI assets from CSV exports
./dev.sh build-openapi-assets

# Build docker images
./dev.sh build

# Launch docker-compose mock application
./dev.sh

# Output API spec markdown for GitBook
./dev.sh gitbook-api-spec
```

Once you have the mock application up and running, you can now access several interesting endpoints:

* http://localhost:8000/docs#/default - api docs served directly from the Django App.
* http://localhost:8080/api/ - Base URL root, behind Caddy HTTP proxy.
* http://localhost:8080/api/service/policy/123456/ -
  this is a static endpoint that just returns a policy mock.
  The approach isn't in use, please make sure to notify the Consent BB working group if you need to include static mocks in a test.

To get a terminal prompt for the Django app container, run `docker-compose exec -it consent /bin/bash`.

The docker compose environment has an HTTP proxy on `localhost:8080` and `localhost:8888` (HTTPS).
The proxy serves static mocks, but for all dynamic mocks there is a mock application where all other requests are forwarded to.

The mock application sits on `http://localhost:8000` (8000 is the default Django development port) and may be accessed directly in cases where you for instance need to see the raw traceback of an error that has occurred. You can access the Django Admin site with credentials `admin:admin` on http://localhost:8000/admin.

### Running tests
```sh
# Run mock application for testing + test suite
# NB! Close the other development environment
./dev.sh test
```

### Prerequisites

* Docker
* Docker Compose v2
