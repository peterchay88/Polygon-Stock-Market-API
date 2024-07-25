import pytest
from framework.src.utils.logging_util import Logger
from framework.src.utils.conditions_util import Conditions
from framework.src.helpers.response_data_validator import validate_response_data

conditions = Conditions()
pytestmark = [pytest.mark.conditions, pytest.mark.conditions_positive, pytest.mark.positive]
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
    def test_get_conditions_asset_class(self, get_api_key, asset_class_param, test_id):
        """
        This test case confirms if we specify an argument for the asset class parameter when calling the conditions
        endpoint only data for that argument return
        :return:
        """
        logger.info(f"Now running Test case {test_id}")
        params = {"asset_class": asset_class_param}
        response = conditions.get_conditions(api_key=get_api_key, **params)
        logger.debug(response.json())
        assert_response = validate_response_data(response.json()["results"], **params)
        assert assert_response is True, \
            f"Error! Response returned an unexpected value"

    @pytest.mark.parametrize("data_type_param,test_id", [
        pytest.param("trade", "22", marks=pytest.mark.tcid22),
        pytest.param("bbo", "23", marks=pytest.mark.tcid23),
        pytest.param("nbbo", "24", marks=pytest.mark.tcid24)
    ])
    def test_get_conditions_data_type(self, get_api_key, data_type_param, test_id):
        """
        This test case confirms if we specify an argument for the data type parameter when calling the conditions
        endpoint only data for that argument return
        :param get_api_key:
        :param data_type_param:
        :param test_id:
        :return:
        """
        logger.info(f"Now running Test case {test_id}")
        params = {"data_type": data_type_param}
        response = conditions.get_conditions(api_key=get_api_key, **params)
        logger.debug(response.json())
        assert_response = validate_response_data(response.json()["results"], **params)
        assert assert_response is True, \
            f"Error! Response returned an unexpected value"
