import pytest
import requests

pytest_plugins = [
   "tests.shared_steps"
]

@pytest.fixture(scope="session")
def client():
    """
    This is a very simple client, we can expand it to contain more state and to
    run fast.
    """
    
    def http():
        session = requests.Session()
        
        # We are self-signing SSL certificates in example deployments.
        session.verify = False
        return session
    
    return http()
