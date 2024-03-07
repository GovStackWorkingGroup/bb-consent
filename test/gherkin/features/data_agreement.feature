@method=GET @endpoint=/config/data-agreement/{dataAgreementId}
Feature: Retrieve Data Agreement Configuration
  I want to be able to retrieve configuration details of a data agreement by
  its ID to ensure that the correct configurations are in place.

  Background:
    Given A URL of a Consent Building Block instance

  @positive @get_data_agreement
  Scenario Outline: Retrieve data agreement configuration by valid ID
    Given a data agreement ID "<dataAgreementId>"
    When I make a GET request to /config/data-agreement/"<dataAgreementId>"
    Then The response should have a status code of 200
    And The response should contain the data agreement details for "<dataAgreementId>"

    Examples: Valid data
    | dataAgreementId |
    | 1               |

  @negative @get_data_agreement
  Scenario Outline: Attempt to retrieve data agreement configuration with invalid ID
    Given a data agreement ID "<dataAgreementId>"
    When I make a GET request to /config/data-agreement/"<dataAgreementId>"
    Then The response should have a status code of 400

    Examples:
      | dataAgreementId |
      | invalid_id      |
      | 123!%40%23      |
