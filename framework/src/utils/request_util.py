import requests
from framework.src.utils.logging_util import Logger

logger = Logger()


class PolygonRequests:

    def __init__(self):
        self.url = "https://api.polygon.io"

    @staticmethod
    def expected_status_code(status_code, expected_status_code):
        """
        This method is used to assert if the expected status code was returned from the API response call
        :param status_code:Status code passed in
        :param expected_status_code:Expected status code
        :return:
        """
        logger.debug(f"Checking if status code received {status_code}, matches status code expected "
                     f"{expected_status_code}.")
        assert status_code == expected_status_code, \
            f"Unexpected status code. Expected {expected_status_code}. Actual {status_code}."

    def get(self, endpoint):
        logger.debug(f"Running a GET request to the following endpoint:{self.url}{endpoint}")
        response = requests.get(url=f"{self.url}{endpoint}")
        logger.debug(f'GET Request successful')
        return response
