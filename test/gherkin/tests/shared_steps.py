import os
from pytest_bdd import (
    scenarios,
    given,
    when,
    then,
)


@given(
    "A URL of a Consent Building Block instance",
    target_fixture="api_url"
)
def api_url():
    return "https://{}{}".format(
        os.environ["CONSENTBB_API_HOST"],
        os.environ["CONSENTBB_API_PATH"]
    )
