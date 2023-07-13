import json
import os
from pytest_bdd import (
    scenarios,
    given,
    when,
    then,
)

scenarios("something_exists.feature")

@when(
    "I call a basic public API endpoint",
    target_fixture="when_api_basic_public_call"
)
def when_api_basic_public_call(api_url, client):
    return client.get(
        os.path.join(api_url, "service/policy/1/")
    )


@then("I get some valid JSON data back")
def json_data_is_valid(when_api_basic_public_call):
    if not when_api_basic_public_call.status_code == 200:
        raise AssertionError(f"Got status code {when_api_basic_public_call.status_code}\n\nContent:\n{when_api_basic_public_call.content}")
    response_data = json.loads(when_api_basic_public_call.content)
    assert isinstance(response_data, list)
    # This is the Policy object
    assert isinstance(response_data[0], dict)
    # This is the Revision object
    assert isinstance(response_data[1], dict)
