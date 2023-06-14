Feature: Data controller can perform basic CRUD operations on Agreements

  @unit @positive
  Scenario: A data controller of an Organization can read an Agreement.

    This generic scenario implements UC-Post-Partum-001.

    Given A URL of a Consent Building Block instance
    And An Agreement for Test Organization's User Registration exists
    When A valid admin fetches an Agreement for Test Organization
    Then A valid Agreement is returned
