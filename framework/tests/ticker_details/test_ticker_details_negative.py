import pytest
from framework.src.utils.logging_util import Logger
from framework.src.utils.ticker_details_util import TickerDetailsUtility

ticker = TickerDetailsUtility()


class TestTickerDetailsNegative:

    @pytest.mark.tcid05
    def test_get_ticker_details_wrong_api_key(self):
        """
        This test confirms we get the correct error message when trying to send a GET request to the ticker details
        endpoint with the wrong API key
        :return:
        """
        response = ticker.get_ticker_details(api_key="apiKey=123", expected_status_code=401)
        expected_msg = "Unknown API Key"
        assert response.json()['error'] == expected_msg, \
            f"ERROR! Unexpected value, Expected: {expected_msg}. Actual: {response.json()['error']}"

    @pytest.mark.tcid06
    def test_get_ticker_details_no_api_key(self):
        """
        This test confirms we get the correct error message when trying to send a GET request to the ticker details
        endpoint with no API key
        :return:
        """
        response = ticker.get_ticker_details(api_key="", expected_status_code=401)
        expected_msg = "API Key was not provided"
        assert response.json()['error'] == expected_msg, \
            f"ERROR! Unexpected value, Expected: {expected_msg}. Actual: {response.json()['error']}"


