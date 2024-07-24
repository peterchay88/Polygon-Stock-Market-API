from framework.src.utils.logging_util import Logger
from framework.src.helpers.regex_helper import regular_expression_checker

logger = Logger()


def validate_conditions_response(conditions_response, **kwargs):
    """
    This function should help us validate the response returned from the conditions endpoint
    CURRENTLY ONLY WORKS FOR asset_class
    :return:
    """
    for key in kwargs:
        logger.debug(f"Checking if returned response only contain {key}: {kwargs[key]}")
        for response in conditions_response:  # Iterate through the list of returned dicts
            # import pdb; pdb.set_trace()
            for response_keys in response.keys():  # Iterate through the list of keys for the specific response
                match = regular_expression_checker(pattern=key, string=response_keys)
                if match:
                    # pdb.set_trace()
                    logger.debug(f"Checking to see if {response[response_keys]} matches {kwargs[key]}")
                    if response[response_keys] == kwargs[key]:
                        assert_value = True
                    else:
                        assert_value = False
                        break

            # if response[key] == kwargs[key]:
            #     assert_value = True
            # else:
            #     assert_value = False
            #     break
    return assert_value


def validate_data_type(conditions_response, **kwargs):
    """
    This function is used to validate 'data_type' in the response. Data types can be returned as lists with multiple
    parameters returned
    :param conditions_response:
    :param kwargs:
    :return:
    """
    for kwarg_key in kwargs:
        logger.debug(f"Checking if returned response only contain {kwarg_key}: {kwargs[kwarg_key]}")
        for response in conditions_response:  # Iterate through the list of returned dicts
            # import pdb; pdb.set_trace()
            for response_keys in response.keys():  # Iterate through the list of keys for the specific response
                match = regular_expression_checker(pattern=kwarg_key, string=response_keys)
                if match:
                    # pdb.set_trace()
                    logger.debug(f"Checking to see if {response[response_keys]} matches {kwargs[kwarg_key]}")
                    for key in response[response_keys]:
                        if key == kwargs[kwarg_key]:
                            assert_value = True
                        else:
                            assert_value = False
                            break
    return assert_value
