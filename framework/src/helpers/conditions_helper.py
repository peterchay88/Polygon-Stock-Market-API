from framework.src.utils.logging_util import Logger


def validate_conditions_response(conditions_response, **kwargs):
    """
    This function should help us validate the response returned from the conditions endpoint
    CURRENTLY ONLY WORKS FOR asset_class
    :return:
    """
    for key in kwargs:
        for response_key in conditions_response:
            if response_key[key] == kwargs[key]:
                assert_value = True
            else:
                assert_value = False
                break
    return assert_value



# validate_conditions_response(asset_class="stocks", data_type="test")