import pytest
from framework.src.utils.logging_util import Logger
from framework.src.utils.ticker_details_util import TickerDetailsUtility

ticker = TickerDetailsUtility()
logger = Logger()


class TestTickerDetailsNegative:

    @pytest.mark.tcid05
    def test_get_ticker_details_wrong_api_key(self):
        """
        This test confirms we get the correct error message when trying to send a GET request to the ticker details
        endpoint with the wrong API key
        :return:
        """
        logger.info("Running test case 5")
        response = ticker.get_ticker_details(api_key="apiKey=123", expected_status_code=401)
        expected_msg = "Unknown API Key"
        logger.debug(f"Checking to see if received message '{response.json()['error']}' "
                     f"matches the expected message '{expected_msg}'")
        assert response.json()['error'] == expected_msg, \
            f"ERROR! Unexpected value, Expected: {expected_msg}. Actual: {response.json()['error']}"

    @pytest.mark.tcid06
    def test_get_ticker_details_no_api_key(self):
        """
        This test confirms we get the correct error message when trying to send a GET request to the ticker details
        endpoint with no API key
        :return:
        """
        logger.info("Running test case 6")
        response = ticker.get_ticker_details(api_key="", expected_status_code=401)
        expected_msg = "API Key was not provided"
        logger.debug(f"Checking to see if received message '{response.json()['error']}' "
                     f"matches the expected message '{expected_msg}'")
        assert response.json()['error'] == expected_msg, \
            f"ERROR! Unexpected value, Expected: {expected_msg}. Actual: {response.json()['error']}"

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
