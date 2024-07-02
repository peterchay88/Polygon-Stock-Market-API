import requests


class PolygonRequests:

    def __init__(self):
        self.url = "https://api.polygon.io"

    @staticmethod
    def expected_status_code(status_code, expected_status_code=200):
        """
        This method is used to assert if the expected status code was returned from the API response call
        :param status_code:Status code passed in
        :param expected_status_code:Expected status code
        :return:
        """
        assert status_code == expected_status_code, \
            f"Unexpected status code. Expected {expected_status_code}. Actual {status_code}."

    def get(self, endpoint):
        response = requests.get(url=f"{self.url}{endpoint}")
        return response
