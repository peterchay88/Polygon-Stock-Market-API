import pytest
from framework.src.utils.logging_util import Logger
from framework.src.utils.ticker_details_util import TickerDetailsUtility


ticker = TickerDetailsUtility()
logger = Logger()
pytestmark = [pytest.mark.ticker_details_positive]


class TestTickerDetailsPositive:

    @pytest.mark.tcid04
    def test_get_ticker_details_endpoint(self, get_api_key):
        """
        This test confirms that we are able to successfully send a GET request to the ticker details endpoint
        :return:
        """
        logger.info("Running test case 04 get ticker details endpoint positive")
        response = ticker.get_ticker_details(api_key=get_api_key)
        # No assert is necessary as we check if the status code matches the expected status code in the
        # Request wrapper

