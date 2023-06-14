Feature: Consent Agreements can be fetched in a variety of scenarios.

  @unit @positive
  Scenario: As the data controller of an Organization, my application has read access for Agreements when performing user registration processes
  
    This generic scenario implements UC-Post-Partum-001.
  
    Given A URL of a Consent Building Block instance
    And an Agreement for Test Organization's User Registration exists
    When I fetch an Agreement for Test Organization
    Then I get a valid Agreement
