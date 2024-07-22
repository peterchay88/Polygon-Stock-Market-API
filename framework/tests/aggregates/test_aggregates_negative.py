import pytest
from framework.src.utils.aggregates_util import Aggregates
from framework.src.utils.logging_util import Logger

logger = Logger()
aggregates = Aggregates()
pytestmark = [pytest.mark.aggregates_negative, pytest.mark.aggregates]


class TestAggregatesNegative:

    @pytest.mark.tcid02
    def test_get_aggregates_endpoint_invalid_api_key(self):
        """
        This test case confirms we return the correct error when trying to hit the aggregates endpoint with an invalid
        API key
        :return:
        """
        logger.info("Running Test case 2")
        api_response = aggregates.get_aggregates(api_key="apiKey=123", expected_status_code=401)
        expected_msg = "Unknown API Key"
        assert api_response.json()['error'] == expected_msg, \
            f"Error! Unexpected value. Expected: {expected_msg}. Actual: {api_response.json()['error']}"

    @pytest.mark.tcid03
    def test_get_aggregates_endpoint_no_api_key(self):
        """
        This test case confirms we return the correct error when trying to hit the aggregates endpoint with no API key
        :return:
        """
        logger.info("Running Test case 3")
        api_response = aggregates.get_aggregates(api_key="", expected_status_code=401)
        expected_msg = "API Key was not provided"
        assert api_response.json()['error'] == expected_msg, \
            f"Error! Unexpected value. Expected: {expected_msg}'. Actual: {api_response.json()['error']}"

    @pytest.mark.tcid08
    def test_get_aggregates_endpoint_no_ticker(self, get_api_key):
        """
        This test case confirms we return the correct error and error message when trying to hit the aggregates endpoint
        with no ticket specified
        :param get_api_key:
        :return:
        """
        logger.info("Running Test case 8")
        api_response = aggregates.get_aggregates(api_key=get_api_key, expected_status_code=400, stocks_ticker="")
        expected_msg = "Ticker was incorrectly formatted"
        assert api_response.json()['error'] == expected_msg, \
            f"Error! Unexpected value. Expected: {expected_msg}. Actual: {api_response.json()['error']}"

    @pytest.mark.tcid18
    def test_get_aggregates_endpoint_invalid_ticker(self, get_api_key):
        """
        This test confirms that when we send an invalid ticker to the aggregates endpoint we return an empty query
        :param get_api_key:
        :return:
        """
        logger.info("Running test case 18")
        api_response = aggregates.get_aggregates(api_key=get_api_key, expected_status_code=200,
                                                 stocks_ticker="Invalid_ticker")
        assert api_response.json()['queryCount'] == 0, \
            f"Error! Unexpected value. Expected value for queryCount: 0. Actual {api_response.json()['queryCount']}"
        assert api_response.json()['resultsCount'] == 0, \
            f"Error! Unexpected value. Expected value for resultsCount: 0. Actual {api_response.json()['resultsCount']}"

