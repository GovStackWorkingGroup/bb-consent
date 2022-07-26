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
    assert when_api_basic_public_call.status_code == 200
    assert isinstance(json.loads(when_api_basic_public_call.content), dict)
