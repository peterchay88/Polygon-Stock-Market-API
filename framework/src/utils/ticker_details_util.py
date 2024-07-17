from framework.src.utils.logging_util import Logger
from framework.src.utils.request_util import PolygonRequests

logger = Logger()


class TickerDetailsUtility:

    def __init__(self):
        self.endpoint = "/v3/reference/tickers/"
        self.api_request = PolygonRequests()

    def get_ticker_details(self, api_key, ticker="AAPL", expected_status_code=200):
        """
        Get Request for the Ticker Details API endpoint. If no ticket is specified then default to AAPL
        :param expected_status_code:
        :param api_key:
        :param ticker:
        :return:
        """
        logger.debug(f"Getting ticker details for {ticker}")
        response = self.api_request.get(endpoint=f"{self.endpoint}{ticker}?{api_key}")
        self.api_request.expected_status_code(status_code=response.status_code,
                                              expected_status_code=expected_status_code)
        return response
