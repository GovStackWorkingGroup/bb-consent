import json
import os
from pytest_bdd import (
    scenarios,
    given,
    when,
    then,
)

scenarios("config_policy.feature")


@given(
    "I have an Agreement for MCC Registration",
    target_fixture="mcc_registration_agreement"
)
def mcc_i_have_an_agreement(api_url, client):
    agreement = client.get(
        os.path.join(api_url, f"service/agreement/1/")
    )
    return json.loads(agreement.content)

@when(
    "I fetch the Policy of the MCC Registration Agreement",
    target_fixture="api_mcc_registration_policy"
)
def when_api_policy_call(api_url, mcc_registration_agreement, client):
    return client.get(
        os.path.join(api_url, "service/policy/{}/".format(mcc_registration_agreement["id"]))
    )


@then("I get a valid Policy")
def json_data_is_valid(api_mcc_registration_policy):
    assert api_mcc_registration_policy.status_code == 200
    json_data = json.loads(api_mcc_registration_policy.content)
    assert json_data["id"] == 1
