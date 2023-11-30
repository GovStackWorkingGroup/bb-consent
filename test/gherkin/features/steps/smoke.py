import json
import os

from behave import given, when, then


@given(u'A URL of a Consent Building Block instance')
def step_impl(context):

    # We just use the API url given from the context, a more advanced
    # setup could try other API base urls.
    assert context.session.api_url
    context.api_url = context.session.api_url


@when(u'I call a basic public API endpoint')
def step_impl(context):
    context.response = context.session.get(
        os.path.join(context.api_url, "service/policy/1/")
    )


@then(u'I get some valid JSON data back')
def step_impl(context):
    if not context.response.status_code == 200:
        raise AssertionError(f"Got status code {context.response.status_code}\n\nContent:\n{context.response.content}")
    response_data = json.loads(context.response.content)
    assert isinstance(response_data, dict)
    # This is the Policy object
    assert isinstance(response_data["policy"], dict)
    # This is the Revision object
    assert isinstance(response_data["revision"], dict)
