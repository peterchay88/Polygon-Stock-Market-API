from framework.src.utils.request_util import PolygonRequests
from framework.src.utils.logging_util import Logger

logger = Logger()


class Aggregates:

    # def __init__(self, stocks_ticker="AAPL", multiplier=1, timespan="day",
    #              from_date="2023-01-09", to_date="2023-01-09"):
    #     # need to figure out logic for optional variables adjusted, sort, and limit
    #     # If variables are not defined go with example api call
    #
    #     self.endpoint = f"/v2/aggs/ticker/{stocks_ticker}/range/{multiplier}/{timespan}/{from_date}/{to_date}"
    #     self.request = PolygonRequests()

    def __init__(self):
        self.endpoint = "/v2/aggs/ticker/"
        self.request = PolygonRequests()

    def get_aggregates(self, api_key, expected_status_code=200, stocks_ticker="AAPL", multiplier=1,
                       timespan="day", from_date="2023-01-09", to_date="2023-01-09"):
        """
        Method used to hit aggregates endpoint with GET command. Default required variables are set with example
        values from Polygons documentation.
        :return:
        """
        logger.debug(f"Calling get aggregates")
        response = self.request.get(endpoint=f"{self.endpoint}{stocks_ticker}/range/{multiplier}/{timespan}"
                                             f"/{from_date}/{to_date}?{api_key}")
        logger.debug(response.json())
        self.request.expected_status_code(status_code=response.status_code, expected_status_code=expected_status_code)
        return response
