import logging
# To confugure 
# Create a logger
logger = logging.getLogger("mylogger")

# To capture all the messages at DEBUG level, this will set a logging level 
logger.setLevel(logging.DEBUG)

# To log messages to a file 
file_handler = logging.FileHandler

# This directs the log messages to the output
output_handler = logging.StreamHandler()

# Formatting for the handlers 
file_handler.setFormatter(formatter)
output_handler.setFormatter(formatter)

# There will be 2 handlers, one to write log messages to a file and the other for printing the messages to the output
logger.addHandler(file_handler)
logger.addHandler(output_handler)

# Have a logger in place
def some_function():
    try: 
        result = perform_some_function()
except Exception as e:
# Log an error message if an exception occurs
logger.error ("An error has occurred")

if __name__ == "__main__": 
    logger.debug("Start of application")
    some_function()
    logger.debug ("Exiting the application")
    logger.info("Welcome Message")
    logger.warning("Warning error message")
    logger.error("This is an Erorr message")
    logger.critical("Critical Message")