import json
import os
from pytest_bdd import (
    scenarios,
    given,
    when,
    then,
)

scenarios("get_agreement.feature")


@given(
    "an Agreement for MCC Registration exists",
    target_fixture="mcc_registration_create"
)
def mcc_registration_create():
    # Currently, this is just mocked in Caddy, so we don't create the object,
    # we just return a hard-coded ID
    return 1


@when(
    "I fetch an Agreement for MCC Registration",
    target_fixture="api_mcc_registration"
)
def when_api_basic_public_call(api_url, mcc_registration_create, client):
    return client.get(
        os.path.join(api_url, f"service/agreement/{mcc_registration_create}/")
    )


@then("I get a valid Agreement")
def json_data_is_valid(api_mcc_registration):
    assert api_mcc_registration.status_code == 200
    json_data = json.loads(api_mcc_registration.content)
    assert json_data["id"] == "1"
