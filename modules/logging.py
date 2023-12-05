import logging.config
from . import settings  # Import the logging configuration from settings.py


# Configure logging using the settings defined in settings.py
logging.config.dictConfig(settings.LOGGING_CONFIG)


# The logging configuration is loaded from settings.py, which defines the structure and settings for different loggers,
# # formatters, and handlers.


