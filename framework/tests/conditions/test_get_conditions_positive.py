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
        :return:
        """
        response = conditions.get_conditions(api_key=get_api_key)
        import pdb; pdb.set_trace()


