import pytest
import requests
import os


# This makes sure that shared steps are available for all.
pytest_plugins = [
   "tests.shared_steps"
]


def api_url():
    return "https://{}{}".format(
        os.environ["CONSENTBB_API_HOST"],
        os.environ["CONSENTBB_API_PATH"]
    )


@pytest.fixture(scope="session")
def client():
    """
    This is a very simple client, we can expand it to contain more state and to
    run fast.
    """
    
    def http():
        session = requests.Session()

        # Save our api_url on the session. This property doesn't have anything at all to do with
        # the requests library, it's our own little thing :)
        session.api_url = api_url()

        # We are self-signing SSL certificates in example deployments.
        session.verify = False
        return session
    
    return http()
