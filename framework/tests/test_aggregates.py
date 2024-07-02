import pytest
from framework.src.utils.aggregates_util import Aggregates

pytestmark = [pytest.mark.aggregates]


class TestAggregates:

    @pytest.mark.tcid01
    def test_get_aggregates_aapl(self):
        """
        This test confirms we can get the aggregates endpoint and return data for AAPL
        :return:
        """
        aggregates = Aggregates(stocks_ticker="aapl")
        api_response = aggregates.get_aggregates()
        import pdb; pdb.set_trace()
        pass
