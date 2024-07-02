import pytest
from framework.src.utils.aggregates_util import Aggregates
import logging as logger

pytestmark = [pytest.mark.aggregates]


class TestAggregates:

    @pytest.mark.tcid01
    def test_get_aggregates_endpoint(self):
        """
        This test confirms we can hit the aggregates endpoint and return a 200. Default ticker is AAPL.
        :return:
        """
        logger.info(f"Running Test case 01")
        aggregates = Aggregates()
        api_response = aggregates.get_aggregates()
