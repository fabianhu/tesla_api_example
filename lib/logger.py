# implement a logger, so that tesla_api can log messages

import logging

# create a logger
Logger = logging.getLogger('tesla_api_example')
Logger.setLevel(logging.DEBUG)
