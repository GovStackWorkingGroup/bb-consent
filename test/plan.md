# Test plan for the Consent Building Block

The following tests are integration tests (intended for BDD), mean to be described as closely as possible to Gherkin/Cucumber language.

## Strategy

* This test plan focuses on validating the compliance between an implementation of the Consent Building Block and the specification of the Consent Building Block.
* This test plan **does not** specify all test cases possible, it only outlines important examples.

## Tests

### 1. Topic name

One-liner about the topic. Use-case mapping.

#### 1.1 Scenario name

One-liner about the scenario and use-case mapping.

##### 1.1.a Test name

Here, we write the concrete test.

```
Feature: Google Searching
  As a web surfer, I want to search Google, so that I can learn new things.
  
  Scenario: Simple Google search
    Given a web browser is on the Google page
    When the search phrase "panda" is entered
    Then results for "panda" are shown
```
