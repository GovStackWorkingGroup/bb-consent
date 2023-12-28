@method=GET @endpoint=/service/policy/{policyId}/
# Here we paste the title.
Feature: The Consent Building Block Exists
# Recommended - Here we can paste the user stories to make it more readable.


# Background: This will be executed once for each
# Given a URL of Consent BB.


# We can extend it with the test category that may be useful with hooks like @consent_bb_exists
  @smoke
  Scenario: The Platform and Its API Exists
  # Step can be parameterized; let's pass URL here.
      Given A URL of a Consent Building Block instance 
      When I call a basic public API endpoint
      Then I get some valid JSON data back


# Also, we can paste the example template here.
