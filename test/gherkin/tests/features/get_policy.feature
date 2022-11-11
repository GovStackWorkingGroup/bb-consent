Feature: The Consent Building Block exists

  Scenario: The platform and its API exists
      Given A URL of a Consent Building Block instance
      Given an Agreement for MCC Registration exists
      When I fetch an Agreement for MCC Registration
      Then I get a valid Agreement
