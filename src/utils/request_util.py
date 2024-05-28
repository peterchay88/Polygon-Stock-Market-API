import requests


class PolygonRequests:

    def __init__(self):
        self.url = "https://api.polygon.io"

    def get(self, endpoint):
        response = requests.get(url=f"{self.url}{endpoint}")
        return response
