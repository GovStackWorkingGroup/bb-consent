@method=GET @endpoint=/service/policy/{policyId}/
# here we paste the title
Feature: The Consent Building Block exists
# recommended - here we can paste the user stories to make it more readable


# Background: this will be executed one for each
# Given a URL of Consent BB


# we can extend it with the test category that may be useful with hooks like @consent_bb_exists
  @smoke
  Scenario: The platform and its API exists
  # step can be parametrized, lets pass URL here
      Given A URL of a Consent Building Block instance 
      When I call a basic public API endpoint
      Then I get some valid JSON data back


# also we can paste the example template here
