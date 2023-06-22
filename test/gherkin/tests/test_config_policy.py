import json
import os
from pytest_bdd import (
    scenarios,
    given,
    when,
    then,
)

from .utils import assert_response_code

scenarios(
    # "config_policy_create.feature",
    "config_policy_read.feature",
)


@given(
    "an organization admin user with access to read configuration",
    target_fixture="user",
)
def organization_admin(client):
    # We don't do anything with users for now, we have no idea how to map them
    return object()


@given(
    "an Example Policy for Test Organization exists",
    target_fixture="example_policy"
)
def mcc_i_have_an_agreement(client, user):
    response = client.post(
        os.path.join(client.api_url, "service/policy/")
    )
    assert_response_code(response, 200)
    policy = json.loads(response.content)
    return policy


@when(
    "The User fetches Example Policy for Test Organization",
    target_fixture="example_policy"
)
def when_api_policy_call(client, user, example_policy):
    response = client.get(
        os.path.join(client.api_url, "service/policy/{}/".format(example_policy["id"]))
    )
    assert_response_code(response, 200)
    policy = json.loads(response.content)
    return policy


@then("Example Policy for Test Organization is returned")
def json_data_is_valid(client, user, example_policy):
    assert example_policy["id"]
