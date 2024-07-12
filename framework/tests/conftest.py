import pytest
import os
from framework.src.utils.logging_util import Logger

api_key = os.getenv('API_KEY')
logger = Logger()


@pytest.fixture(scope="session")
def get_api_key():
    logger.debug(f"Fetching APJ KEY: {api_key}")
    yield f"apiKey={api_key}"
