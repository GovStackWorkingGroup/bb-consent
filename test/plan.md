# Test plan for the Consent Building Block

This Test Plan contains a set of high-level integration tests which align with the outlined [Test Strategy](#Strategy).
Test cases are written to closely conform to the Gherkin/Cucumber standard.
A fully implemented test suite will ultimately make it possible to implement this specification through BDD (Behaviour Driven Development).

The intended next step for the test plan is to be implementended as a parsable set of Gherkin tests and finally implemented in an executing test framework feeding back to a test management setup. Thus, we can verify on a very detailed level if a particular Consent implementation lives up to a particular released version of the Consent Building Block Specification.

## Strategy

* This test plan focuses on validating the compliance between an implementation of the Consent Building Block and the specification of the Consent Building Block.
* This test plan **does not** specify all test cases possible, it only outlines important examples.
* This test plan **is versioned** together with the entire Building Block definition.

## Gherkin Reference

Test scenarious are written with Gherkin and can be implemented with several tools. Please read the [Official Gherkin Reference](https://cucumber.io/docs/gherkin/reference/).

## Tests

We write Gherkin features in the following structure:

```
=> Topic (as a folder)
   => Feature (as a .feature file)
      => Scenario (as part of a .feature file)
```

For example:

```
auditing/
  external_real_time.feature
  
     Feature: Notifications are sent to external auditor
  
       Scenario: External auditor is notified of a new consent record
       
       Background:
         Given an auditor named "A&B"
         Given an individual named "Jane Doe"
         Given an agreement named "Data Agreement"
      
       Given auditor "A&B" signs up for notifications
       When individual "Jane Doe" consents to agreement "Data Agreement"
       Then an auditing notification is sent to "A&B"


```

### 1. Topic name

Description: One-liner about the topic.
Use-cases: Enumerated use-case mapping.

#### 1.1 Scenario name

Description: One-liner about the scenario
Use-cases: Enumerated use-case mapping.

##### 1.1.a Test name

Comment: Here, we write a description of the test, unless it's clear from the Gherkin.

```
Feature: Google Searching
  As a web surfer, I want to search Google, so that I can learn new things.
  
  Scenario: Simple Google search
    Given a web browser is on the Google page
    When the search phrase "panda" is entered
    Then results for "panda" are shown
```
