import pytest
from framework.src.utils.logging_util import Logger
from framework.src.utils.conditions_util import Conditions
from framework.src.helpers.conditions_helper import validate_conditions_response

conditions = Conditions()
pytestmark = [pytest.mark.conditions, pytest.mark.conditions_positive]
logger = Logger()


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

    @pytest.mark.parametrize("asset_class_param,test_id", [
        pytest.param("stocks", "10", marks=pytest.mark.tcid10),
        pytest.param("options", "14", marks=pytest.mark.tcid14),
        pytest.param("crypto", "15", marks=pytest.mark.tcid15),
    ])
    def test_get_conditions_asset_class_stocks(self, get_api_key, asset_class_param, test_id):
        """
        This test case confirms if we specify only stocks for the asset class when calling the conditions endpoint
        only data for stocks return

        :return:
        """
        logger.info(f"Now running Test case {test_id}")
        params = {"asset_class": asset_class_param}
        response = conditions.get_conditions(api_key=get_api_key, **params)
        logger.debug(response.json())
        assert_response = validate_conditions_response(response.json()["results"], **params)
        assert assert_response is True, \
            f"Error! Response returned an unexpected value"
