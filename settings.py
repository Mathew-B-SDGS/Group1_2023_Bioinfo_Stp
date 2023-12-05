import os

# Define the log file path
LOG_FILE = os.path.join(os.path.expanduser('~'), 'panelsearchapp.log')

LOGGING_CONFIG = {
    'version': 1,
    'formatters': {
        'simple': {
            'format': '%(levelname)s: %(message)s'
        },
        'detailed': {
            'format': '%(asctime)s %(name)-5s %(funcName)-10s (line %(lineno)d) %(levelname)-8s %(message)s'
            # - '%(asctime)s': Log record's time in a human-readable format.
            # - '%(name)-5s': Logger name, left-aligned with a minimum width of 5 characters.
            # - '%(funcName)-10s': Function name, left-aligned with a minimum width of 10 characters.
            # - '(line %(lineno)d)': Line number of the logging call.
            # - '%(levelname)-8s': Log level, left-aligned with a minimum width of 8 characters.
            # - '%(message)s': The log message.
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'DEBUG',
            'formatter': 'simple'
        },
        'file': {
            'class': 'logging.FileHandler',
            'level': 'ERROR',
            'filename': LOG_FILE,
            'mode': 'a',
            'formatter': 'detailed',
        },
    },
    'loggers': {
        'PanelSearchApp': {  # Root logger named 'MyAwesomeApp'
            'level': 'INFO',
            'handlers': ['console', 'file']
        }
    }
}