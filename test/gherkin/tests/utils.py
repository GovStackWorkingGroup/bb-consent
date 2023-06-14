"""
This module contains utility functions.

Keep out actual Gherkin steps and individual test logic.
"""


def assert_response_code(response, expected_code):
    if not response.status_code == expected_code:
        raise AssertionError(f"Expected HTTP 200, got {response.status_code}\n\nContent:\n{response.content}")
