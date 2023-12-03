import os
import requests


from behave import fixture, use_fixture


@fixture
def client(context):
    url = "https://{}{}".format(
            os.environ["CONSENTBB_API_HOST"],
            os.environ["CONSENTBB_API_PATH"]
        )

    context.session = requests.Session()

    # Save our api_url on the session. This property doesn't have anything at all to do with
    # the requests library, it's our own little thing :)
    context.session.api_url = url

    # We are self-signing SSL certificates in example deployments.
    context.session.verify = False
    yield context.session
    context.session.close()


def before_all(context):
    use_fixture(client, context,)
