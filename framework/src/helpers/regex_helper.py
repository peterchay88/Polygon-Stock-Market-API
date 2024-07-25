import re


def regular_expression_checker(pattern, string):
    """
    This function uses regular expression to check and return if the pattern
    matches the string
    :param pattern:
    :param string:
    :return:
    """
    search = re.search(pattern=pattern, string=string)
    return search
