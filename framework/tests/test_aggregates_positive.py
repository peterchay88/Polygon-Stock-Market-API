import pytest
from framework.src.utils.aggregates_util import Aggregates
from framework.src.utils.logging_util import Logger

aggregates = Aggregates()
logger = Logger()
pytestmark = [pytest.mark.aggregates_positive]


class TestAggregatesPositive:

    @pytest.mark.tcid01
    def test_get_aggregates_endpoint(self, get_api_key):
        """
        This test confirms we can hit the aggregates endpoint and return a 200. Default ticker is AAPL.
        :return:
        """
        logger.info(f"Running Test case 01")
        api_response = aggregates.get_aggregates(api_key=get_api_key)
        # No assert is necessary as we check if the status code  matches the expected status code in the
        # Request wrapper
