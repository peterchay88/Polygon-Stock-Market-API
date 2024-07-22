import pytest
from framework.src.utils.logging_util import Logger
from framework.src.utils.ticker_details_util import TickerDetails

ticker = TickerDetails()
logger = Logger()
pytestmark = [pytest.mark.ticker_details_negative, pytest.mark.ticker_details, pytest.mark.negative]


class TestTickerDetailsNegative:

    @pytest.mark.parametrize("api_key, test_id, error_msg", [
        pytest.param("apiKey=123", "5", "Unknown API Key", marks=pytest.mark.tcid05),
        pytest.param("", "6", "API Key was not provided", marks=pytest.mark.tcid06)
    ])
    def test_get_ticker_details_wrong_api_key(self, api_key, test_id, error_msg):
        """
        This test confirms we get the correct error message when trying to send a GET request to the ticker details
        endpoint with the wrong API key
        :return:
        """
        logger.info(f"Running test case {test_id}")
        response = ticker.get_ticker_details(api_key=api_key, expected_status_code=401)
        logger.debug(f"Checking to see if received message '{response.json()['error']}' "
                     f"matches the expected message '{error_msg}'")
        assert response.json()['error'] == error_msg, \
            f"ERROR! Unexpected value, Expected: {error_msg}. Actual: {response.json()['error']}"

    @pytest.mark.tcid07
    def test_get_ticker_details_invalid_ticker(self, get_api_key):
        """
        This test confirms that we get the correct error and error message when sending a GET request to the
        ticker details endpoint with an invalid ticker
        :param get_api_key:
        :return:
        """
        logger.info("Running test case 7")
        response = ticker.get_ticker_details(api_key=get_api_key, ticker="asdf123!", expected_status_code=404)
        expected_msg = "Ticker not found."
        logger.debug(f"Checking to see if received message '{response.json()['message']}' "
                     f"matches the expected message '{expected_msg}'")
        assert response.json()['message'] == expected_msg, \
            f"ERROR! Unexpected value, Expected: {expected_msg}. Actual: {response.json()['message']}"
