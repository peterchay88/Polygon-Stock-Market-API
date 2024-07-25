from framework.src.utils.logging_util import Logger
from framework.src.helpers.regex_helper import regular_expression_checker

logger = Logger()


def validate_response_data(conditions_response, **kwargs):
    """
    This function is used to

    :param conditions_response:
    :param kwargs:
    :return:
    """
    for kwarg_key in kwargs:
        logger.debug(f"Checking if returned response only contain {kwarg_key}: {kwargs[kwarg_key]}")
        for response in conditions_response:  # Iterate through the list of returned dicts
            for response_keys in response.keys():  # Iterate through the list of keys for the specific response
                match = regular_expression_checker(pattern=kwarg_key, string=response_keys)
                if match:
                    logger.debug(f"Checking to see if returned response: {response[response_keys]} contains "
                                 f"{kwargs[kwarg_key]}")
                    assert_value = False
                    if type(response[response_keys]) is list:
                        for key in response[response_keys]:
                            if key == kwargs[kwarg_key]:
                                assert_value = True
                    elif type(response[response_keys]) is dict:
                        # Add logic for iterating through a dictionary here
                        pass
                    else:
                        if response[response_keys] == kwargs[kwarg_key]:
                            assert_value = True
                        else:
                            assert_value = False
                            break
    return assert_value
