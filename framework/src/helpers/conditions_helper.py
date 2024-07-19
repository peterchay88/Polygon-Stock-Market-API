from framework.src.utils.logging_util import Logger


def validate_conditions_response(**kwargs):
    """
    This function should help us validate the response returned from the conditions endpoint
    :return:
    """
    for kwarg in kwargs:
        print(kwargs[kwarg])


validate_conditions_response(asset_class="stocks")