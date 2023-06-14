import json
import os
from pytest_bdd import (
    scenarios,
    given,
    when,
    then,
)

from .utils import assert_response_code

scenarios("get_agreement.feature")


@given(
    "an Agreement for Test Organization's User Registration exists",
    target_fixture="basic_agreement"
)
def agreement_create(api_url, client):
    data = {
        "name": "Test data policy",
        "jurisdiction": "EU",
        "version": "1.0",
        "url": "https://example.com",
    }
    policy_create = api_url + "/config/policy/"
    response = client.post(policy_create, json=data)
    assert_response_code(response, 200)
    response_json = json.loads(response.content)
    return response_json


@when(
    "I fetch an Agreement for Test Organization",
    target_fixture="api_mcc_registration"
)
def when_api_basic_public_call(api_url, basic_agreement, client):
    return client.get(
        os.path.join(api_url, f"service/agreement/{basic_agreement['id']}/")
    )


@then("I get a valid Agreement")
def json_data_is_valid(api_mcc_registration):
    assert api_mcc_registration.status_code == 200
    json_data = json.loads(api_mcc_registration.content)
    assert json_data["id"] == "1"
