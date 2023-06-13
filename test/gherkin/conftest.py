import pytest
import requests

pytest_plugins = [
   "tests.shared_steps"
]


class TestClient(requests.Session):

    mock_soft_failure = False

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # We are self-signing SSL certificates in example deployments.
        self.verify = False

    def prepare_request(self, request):
        """
        We hook into this method in order to ensure that we are
        mocking failure whenever needed.

        TODO: When we mock failure, the request should be sent into oblivion
        """
        if self.mock_soft_failure:
            self.hooks["response"] = response_hook_soft_fail
        request = super().prepare_request(request)
        return request


def response_hook_soft_fail(response, **kwargs):
    """
    This is a hook for request.Session.

    Whenevever something happens, we fail. Except if it's a status API!
    """
    # TODO: This doesn't throw away the request so it still pass through
    # to the API backend
    # TODO: We really want to simulate that the backend is down, but
    # that's only possible if we can tell the example application to
    # play along.
    if "/status/" not in response.url:
        response.status_code = 502
    return response


@pytest.fixture(scope="module")
def client():
    """
    This is a very simple client, we can expand it to contain more state and to
    run fast.
    """
    return TestClient()
