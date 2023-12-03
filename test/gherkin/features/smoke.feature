@method=GET @endpoint=/service/policy/{policyId}/
Feature: The Consent Building Block exists

  @smoke
  Scenario: The platform and its API exists
      Given A URL of a Consent Building Block instance
      When I call a basic public API endpoint
      Then I get some valid JSON data back
