import json
import os
from pytest_bdd import (
    scenarios,
    given,
    when,
    then,
)

scenarios("smoke_status.feature")

@given(
    "Everything is operational"
)
def given_everything_is_operational(api_url, client):
    return True


@given(
    "The platform simulates a soft failure"
)
def given_soft_failure(api_url, client):
    """
    We manipulate the client to send back failure codes on all APIs except status API
    """
    client.mock_soft_failure = True
    return True

@when(
    "I call a basic public API endpoint",
    target_fixture="when_api_basic_public_call"
)
def when_api_basic_public_call(api_url, client):
    return client.get(
        os.path.join(api_url, "service/policy/1/")
    )

@when(
    "I call the status API for a startup status",
    target_fixture="when_api_status_startup"
)
def when_api_status_startup(api_url, client):
    return client.get(
        os.path.join(api_url, "status/startup/")
    )


@then("I get back a Status OK response")
def then_api_status_ok(when_api_status_startup):
    assert when_api_status_startup.status_code == 200
    data = json.loads(when_api_status_startup.content)
    assert isinstance(data, dict)
    assert data["status"] == "OK"


@then("I get a valid status error message")
def then_api_status_error(when_api_status_startup):
    assert when_api_status_startup.status_code == 200
    data = json.loads(when_api_status_startup.content)
    assert isinstance(data, dict)
    # TODO: We cannot currently tell an application to respond with error
    # messages. It's also not really relevant for a test to start mocking out
    # the response of the entire API, so we just check that there exists
    # a status message, not what it is.
    assert data["status"]


@then("I get a gateway error")
def then_gateway_error_error(when_api_basic_public_call):
    assert when_api_basic_public_call.status_code == 502
