import pytest
from framework.src.utils.conditions_util import Conditions
from framework.src.utils.logging_util import Logger

logger = Logger()
conditions = Conditions()
pytestmark = [pytest.mark.conditions, pytest.mark.conditions_negative, pytest.mark.negative]


class TestConditionsNegative:

    @pytest.mark.parametrize("api_key, test_id, error_msg", [
        pytest.param("", "11", "API Key was not provided", marks=pytest.mark.tcid11),
        pytest.param("apiKey=123", "12", "Unknown API Key", marks=pytest.mark.tcid12)
    ])
    def test_get_conditions_no_api_key(self, api_key, test_id, error_msg):
        """
        This test confirms that  we receive the correct error and error message when trying to send a GET request
        to the conditions endpoint with no api key and with an incorrect API Key.
        :return:
        """
        logger.info(f"Now running Test case {test_id}")
        response = conditions.get_conditions(api_key=api_key, expected_status_code=401)
        assert response.json()["error"] == error_msg, \
            f"Error! Unexpected value. Expected: {error_msg}. Actual {response.json()['error']}"

    @pytest.mark.tcid13
    def test_get_conditions_invalid_option_asset_class(self, get_api_key):
        """
        This test case confirms that when we give an invalid option for asset class the returned response is empty
        :return:
        """
        logger.info("Now running Test case 13")
        response = conditions.get_conditions(api_key=get_api_key, asset_class="Invalid_option")
        logger.debug("Checking to see if returned response is none")
        assert response.json()["results"] == [], \
            f"Error! Unexpected value. Expected returned response: []. Actual: {response.json()['results']} "



