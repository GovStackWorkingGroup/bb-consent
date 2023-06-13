@method=GET @endpoint=/{GovStackInstance}/{memberClass}/{memberCode}/{applicationCode}/statusStartup
Feature: The Consent Building Block responds to status requests

  @smoke
  Scenario: The platform is functional and sends back correct status
      Given A URL of a Consent Building Block instance
      Given Everything is operational
      When I call the status API for a startup status
      Then I get back a Status OK response

  @smoke
  Scenario: The platform suffers from issues and sends back correct status
      Given A URL of a Consent Building Block instance
      Given The platform simulates a soft failure
      When I call the status API for a startup status
      Then I get a valid status error message

  @smoke
  Scenario: The platform suffers from issues and endpoints are down
      Given A URL of a Consent Building Block instance
      Given The platform simulates a soft failure
      When I call a basic public API endpoint
      Then I get a gateway error
