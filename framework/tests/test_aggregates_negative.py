import pytest
from framework.src.utils.aggregates_util import Aggregates
from framework.src.utils.logging_util import Logger

logger = Logger()
pytestmark = [pytest.mark.aggregates_negative]


class TestAggregatesNegative:

    @pytest.mark.tcid02
    def test_get_aggregates_endpoint_invalid_api_key(self):
        """
        This test case confirms we return the correct error when trying to hit the aggregates endpoint with an invalid
        API key
        :return:
        """
        logger.info(f"Running Test case 02")
        aggregates = Aggregates()
        api_response = aggregates.get_aggregates(api_key="apiKey=123", expected_status_code=401)
        assert api_response.json()['error'] == "Unknown API Key", \
            f"Error! Unexpected value. Expected: 'Unknown API Key'. Actual: {api_response.json()['error']}"

    @pytest.mark.tcid03
    def test_get_aggregates_endpoint_no_api_key(self):
        """
        This test case confirms we return the correct error when trying to hit the aggregates endpoint with no API key
        :return:
        """
        logger.info(f"Running Test case 03")
        aggregates = Aggregates()
        api_response = aggregates.get_aggregates(api_key="", expected_status_code=401)
        assert api_response.json()['error'] == "API Key was not provided", \
            f"Error! Unexpected value. Expected: 'API Key was not provided'. Actual: {api_response.json()['error']}"