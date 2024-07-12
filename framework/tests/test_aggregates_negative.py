import pytest
from framework.src.utils.aggregates_util import Aggregates
from framework.src.utils.logging_util import Logger

logger = Logger()
pytestmark = [pytest.mark.aggregates_negative]


class TestAggregatesNegative:

    @pytest.mark.tcid02
    def test_get_aggregates_endpoint_invalid_api_key(self):
        pass
