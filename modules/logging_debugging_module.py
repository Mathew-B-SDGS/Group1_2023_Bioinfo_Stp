import logging
from logging.handlers import RotatingFileHandler

# To configure
# Create a logger
logger = logging.getLogger("mylogger")

# To capture all the messages at DEBUG level, this will set a logging level
logger.setLevel(logging.DEBUG)

# Create a rotating file handler
log_file = 'app.log'
max_bytes = 10  # Size in bytes before rollover
backup_count = 3  # Number of backup files to keep
rotation_handler = RotatingFileHandler(log_file, maxBytes=max_bytes,
                                       backupCount=backup_count)


# To log messages to a file
file_handler = logging.FileHandler('app.log')

# This directs the log messages to the output
output_handler = logging.StreamHandler()

# There will be 3 handlers, one to write log messages to a file and the other
# for printing the messages to the output
logger.addHandler(file_handler)
logger.addHandler(output_handler)
logger.addHandler(rotation_handler)

# Log an error message if an exception occurs, this will determine the level
# of detail captured in the logs
logger.debug("Start of application")
# some_function()
logger.debug("Exiting the application")
logger.info("Info Message")
logger.warning("Warning error message")
logger.error("This is an Erorr message")
logger.critical("Critical Message")
