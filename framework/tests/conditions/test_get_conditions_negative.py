import pytest
from framework.src.utils.conditions_util import Conditions
from framework.src.utils.logging_util import Logger

logger = Logger()
conditions = Conditions()
pytestmark = [pytest.mark.conditions, pytest.mark.conditions_negative]


class TestConditionsNegative:

    @pytest.mark.tcid11
    def test_get_conditions_no_api_key(self):
        """
        This test confirms that  we receive the correct error and error message when trying to send a GET request
        to the conditions endpoint with no api key
        :return:
        """
        response = conditions.get_conditions(api_key="", expected_status_code=401)
        expected_msg = "API Key was not provided"
        assert response.json()["error"] == expected_msg, \
            f"Error! Unexpected value. Expected: {expected_msg}. Actual {response.json()['error']}"

    @pytest.mark.tcid12
    def test_get_conditions_wrong_api_key(self):
        """
        This test confirms that  we receive the correct error and error message when trying to send a GET request
        to the conditions endpoint with no api key
        :return:
        """
        response = conditions.get_conditions(api_key="apiKey=123", expected_status_code=401)
        expected_msg = "Unknown API Key"
        assert response.json()["error"] == expected_msg, \
            f"Error! Unexpected value. Expected: {expected_msg}. Actual {response.json()['error']}"

    @pytest.mark.tcid13
    def test_get_conditions_invalid_option_asset_class(self):
        """

        :return:
        """
        pass


