from request_util import PolygonRequests


class Aggregates:

    def __init__(self, stocks_ticker="aapl", multiplier=1, timespan="day",
                 from_date="2023-01-09", to_date="2023-01-09",):
        # need to figure out logic for optional variables adjusted, sort, and limit
        # If variables are not defined go with example api call
        self.endpoint = f"/v2/aggs/ticker/{stocks_ticker}/range/{multiplier}/{timespan}/{from_date}/{to_date}"

