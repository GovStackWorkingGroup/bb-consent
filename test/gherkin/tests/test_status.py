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
    assert data["status"] == "ERROR"
