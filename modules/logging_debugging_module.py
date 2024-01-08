import logging
# To configure 
# Create a logger
logger = logging.getLogger("mylogger")

# To capture all the messages at DEBUG level, this will set a logging level 
logger.setLevel(logging.DEBUG)

# To log messages to a file 
file_handler = logging.FileHandler('mylogfile.log')

# This directs the log messages to the output
output_handler = logging.StreamHandler()

# There will be 2 handlers, one to write log messages to a file and the other for printing the messages to the output
logger.addHandler(file_handler)
logger.addHandler(output_handler)

# Have a logger in place
def some_function():
    try: 
        result = perform_some_function()
    except Exception as e:
        logger.error(f"Exception: {e}")

# Log an error message if an exception occurs, this will determine the level of detail captured in the logs
    logger.debug("Start of application")
    some_function()
    logger.debug ("Exiting the application")
    logger.info("Info Message")
    logger.warning("Warning error message")
    logger.error("This is an Erorr message")
    logger.critical("Critical Message")