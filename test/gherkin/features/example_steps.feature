# # Features/Scenarios are written in Gherkin language

# Feature: Title of the Feature
#   # Optional: A brief description of the feature
#   # User Story: As a [role], I want [feature], so that [benefit].

#   Background:
#     # Steps here are run before each scenario, but after any Before hooks
#     Given some initial context

#   Scenario: Title of the first scenario
#     Given some initial condition
#     When an action is taken
#     Then expect a specific outcome

#   Scenario Outline: Title of a scenario with examples
#     Given some <condition>
#     When an action is <action>
#     Then I expect <outcome>

#     Examples:
#       | condition | action | outcome |
#       | good      | do     | success |
#       | bad       | fail   | error   |