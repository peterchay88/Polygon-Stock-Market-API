from framework.src.utils.request_util import PolygonRequests
from framework.src.utils.logging_util import Logger

logger = Logger()


class Conditions:

    def __init__(self):
        self.endpoint = "/v3/reference/conditions?"
        self.api_request = PolygonRequests()

    # def get_conditions(self, api_key, asset_class="", data_type="", condition_id="",
    #                    sip="", order="", limit="", sort=""):
    #     """
    #     Get response for the conditions endpoint.
    #     :param api_key:
    #     :return:
    #     """
    #     response = self.api_request.get(endpoint=f"{self.endpoint}{asset_class}")

    def get_conditions(self, api_key, **kwargs):
        """
        Get response for the conditions endpoint.
        :param api_key:
        :return:
        """
        arguments = []
        parameters = ["asset_class", "data_type", "id", "sip", "order", "limit", "sort"]
        index = 0
        for parameter in parameters:
            if kwargs.get(parameters[index]):
                arguments.append(f"{parameters[index]}={kwargs[parameters[index]]}")
                index += 1
        appended_args = '&'.join(arguments)
        endpoint = f"{self.endpoint}{appended_args}"
        response = self.api_request.get(endpoint=f"{endpoint}&{api_key}")
        return response
