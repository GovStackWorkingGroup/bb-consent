Feature: The Consent Building Block exists

  Scenario: As the data controller for the Mother & Child Center, I can give an application read access to the Policy of an Agreement
      Given A URL of a Consent Building Block instance
      Given I have an Agreement for MCC Registration
      When I fetch the Policy of the MCC Registration Agreement
      Then I get a valid Policy
