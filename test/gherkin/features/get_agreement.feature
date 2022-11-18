Feature: The Consent Building Block exists

  Scenario: As the data controller for the Mother & Child Center, I can give an application read access to Agreements
      Given A URL of a Consent Building Block instance
      Given an Agreement for MCC Registration exists
      When I fetch an Agreement for MCC Registration
      Then I get a valid Agreement
