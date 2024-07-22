import pytest
from framework.src.utils.aggregates_util import Aggregates
from framework.src.utils.logging_util import Logger

logger = Logger()
aggregates = Aggregates()
pytestmark = [pytest.mark.aggregates_negative, pytest.mark.aggregates, pytest.mark.negative]


class TestAggregatesNegative:

    @pytest.mark.parametrize("api_key, test_id, error_msg", [
        pytest.param("apiKey=123", "2", "Unknown API Key", marks=pytest.mark.tcid02),
        pytest.param("", "3", "API Key was not provided", marks=pytest.mark.tcid03)
    ])
    def test_get_aggregates_endpoint_invalid_api_key(self, api_key, test_id, error_msg):
        """
        This test case confirms we return the correct error when trying to hit the aggregates endpoint with an invalid
        API key and no API key
        :return:
        """
        logger.info(f"Running Test case {test_id}")
        api_response = aggregates.get_aggregates(api_key=api_key, expected_status_code=401)
        assert api_response.json()['error'] == error_msg, \
            f"Error! Unexpected value. Expected: {error_msg}. Actual: {api_response.json()['error']}"

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

    @pytest.mark.parametrize("multiplier_param, test_id", [
        pytest.param(0, "19", marks=pytest.mark.tcid19),
        pytest.param(-1, "20", marks=pytest.mark.tcid20),
        pytest.param(-100, "21", marks=pytest.mark.tcid21)
    ])
    def test_get_aggregates_endpoint_not_positive_multiplier(self, get_api_key, multiplier_param, test_id):
        """
        This test confirms that we get an error code and the correct error when sending a multiplier that is not
        positive to the aggregates endpoint via GET call
        :param get_api_key:
        :param multiplier_param:
        :param test_id:
        :return:
        """
        logger.info(f"Running Test Case {test_id}")
        response = aggregates.get_aggregates(api_key=get_api_key, multiplier=multiplier_param, expected_status_code=400)
        expected_msg = "The parameter 'multiplier' must be a positive number"
        assert response.json()['error'] == expected_msg, \
            f"Error! Unexpected value. Expected: {expected_msg}. Actual {response.json()['error']}"


