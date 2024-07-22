import os
import logging
from urllib3.connectionpool import log as connectionpool_log # Trying to figure out how to hide API key from connectionpool.py

logger = logging.getLogger()


class Logger:

    def __init__(self):
        self.log = logger

    def debug(self, string):
        """
        Wrapper method for debug logging msg
        :param string:
        :return:
        """
        self.log.debug(string)

    def info(self, string):
        """
        Wrapper method for info logging msg
        :param string:
        :return:
        """
        self.log.info(string)

    def error(self, string):
        """
        wrapper method for error logging msg
        :param string:
        :return:
        """
        self.log.error(string)


class HideSensitiveData(logging.Filter):
    """
    This class is used to hide sensitive messages in the log
    """
    def filter(self, record):
        record.msg = str(record.msg).replace(os.getenv("API_KEY"), "****")
        return True


logger.addFilter(HideSensitiveData())
connectionpool_log.addFilter(HideSensitiveData()) # Trying to figure out how to hide API key from connectionpool.py
