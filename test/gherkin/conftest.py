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
        request = super().prepare_request(request)
        if self.mock_soft_failure:
            self.hooks["response"] = response_hook_soft_fail
        elif response_hook_soft_fail == self.hooks["response"]:
            self.hooks["response"] = []
        return request


def response_hook_soft_fail(response):
    """
    This is a hook for request.Session.

    Whenevever something happens, we fail. Except if it's a status API!
    """
    if "/status/" not in response.url:
        response.status_code = 502
        response.content = "we down"
    return response


@pytest.fixture(scope="class")
def client():
    """
    This is a very simple client, we can expand it to contain more state and to
    run fast.
    """
    return TestClient()
