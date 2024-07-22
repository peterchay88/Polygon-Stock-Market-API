import pytest
from framework.src.utils.aggregates_util import Aggregates
from framework.src.utils.logging_util import Logger

aggregates = Aggregates()
logger = Logger()
pytestmark = [pytest.mark.aggregates, pytest.mark.aggregates_positive, pytest.mark.positive]


class TestAggregatesPositive:

    @pytest.mark.parametrize("ticker, test_id", [
        pytest.param("AAPL", "1", marks=pytest.mark.tcid01),
        pytest.param("KLR", "16", marks=pytest.mark.tcid16),
        pytest.param("GERN", "17", marks=pytest.mark.tcid17)
    ])
    def test_get_aggregates_endpoint(self, get_api_key, ticker, test_id):
        """
        This test confirms we can hit the aggregates endpoint and return a 200. We are using known working tickers.
        :return:
        """
        logger.info(f"Running Test case {test_id}")
        api_response = aggregates.get_aggregates(api_key=get_api_key, stocks_ticker=ticker)
        # No assert is necessary as we check if the status code  matches the expected status code in the
        # Request wrapper
