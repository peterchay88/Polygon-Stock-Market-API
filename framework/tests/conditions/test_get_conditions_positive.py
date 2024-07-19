import pytest
from framework.src.utils.logging_util import Logger
from framework.src.utils.conditions_util import Conditions

conditions = Conditions()
pytestmark = [pytest.mark.conditions_positive]


class TestConditionsPositive:

    @pytest.mark.tcid09
    def test_get_conditions(self, get_api_key):
        """
        This test case confirms we are able to successfully make a GET request to the conditions endpoint
        no optional arguments are passed here
        :return:
        """
        response = conditions.get_conditions(api_key=get_api_key)
        # No assert is necessary as we check if the status code matches the expected status code in the
        # Request wrapper

    @pytest.mark.tcid10
    def test_get_conditions_asset_class_stocks(self, get_api_key):
        """
        This test case confirms if we specify only stocks for the asset class when calling the conditions endpoint
        only data for stocks return
        :return:
        """
        response = conditions.get_conditions(api_key=get_api_key, asset_class="stocks")







