# Test plan for the Consent Building Block

This plan reflects the strategy and structure of tests for the Consent BB.

## Test strategy

The Consent BB working group has made the following decisions:

* We are pursuing a goal of basic test coverage, meaning that all APIs should be called during a test.
* We'll write at least 1 test for each configuration API
* We'll write at least 1 test for each service API
* We'll write at least 1 test for each audit API
* We'll write all tests as Gherkin scenarios
* We'll cleary mark scenarios that are not directly related to user scenarios (to keep it minimal)

The objectives of the strategy will be elaborated as we understand more about use cases and have reached the first goals of basic test coverage.

## Gherkin scenarios

Gherkin .feature files are stored here:

* `test/gherkin/features`

Their implementations are done with `pytest` and `pytest-bdd`.
Those files are available here:

* `test/gherkin/tests`

Please see the Development section further down for implementation details.

### Proposing a new scenario

Scenarios are discussed and approved by the Working Group.
But anyone is welcome to add a scenario.

1. Scenarios are proposed and discussed in the following Confluence document: https://govstack-global.atlassian.net/l/cp/Qh3koEkU
1. After a discussion, the scenario is approved and should be migrated to `test/gherkin/features`.
1. Once migrated to `test/gherkin/features`, it should be REMOVED from the Confluence document.

### Structure

APIs for the Consent BB are structured in the following top-level URL paths:

* `/config`
* `/service`
* `/audit`
* ...and a few more soon to come, for instance for PubSub.

Gherkin feature files should be prefixed with the API level that are their primary target (i.e. what is verified in the `then` clause).

## Development

The following is written for software developers implementing Gherkin scenarios and expanding the mock application.

### Development tools

As is noted in our [README.md](../README.md), you can use a `dev.sh` script to interact with both mocking application and test suite locally.

To run tests, simply invoke `./dev.sh test`

### Mock application

In `/examples/mock/`, you will find an application that implements all of our API endpoints.

This application is mostly auto-generated. So it's basically an artifact of our OpenAPI specification. If you want to update it, please take into consideration to avoid adding things manually that the test script should ideally have generated automatically.

All endpoints can be overwritten manually in `/examples/mock/djangoapp/consentbb/app/api.py`.

### Strategy and alignment

Everything implemented runs according to GovStack standards, including Docker Compose setups and `test_entrypoint.sh` scripts.

## Notes

(these notes/questions originate from the template)

At least three levels of testing...

1. can the BB be deployed via docker-compose? Yes
2. can the BB interact with the IM? Not currently
3. can an adaptor be deployed alongside it to test API compliance? Yes
4. do the required APIs respond to the required inputs and provide the required responses? No, the mock application needs to be expanded

