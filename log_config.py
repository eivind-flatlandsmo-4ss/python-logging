import logging

from sys import stdout

logger = logging.getLogger()
logger.setLevel("DEBUG")

formatter = logging.Formatter(logging.BASIC_FORMAT)
stream_handler = logging.StreamHandler(stdout)
logger.addHandler(stream_handler)
stream_handler.setFormatter(formatter)

# Configure file handler so that the log is stored after execution of the program
file_handler = logging.FileHandler("mylog.log", mode="w")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

logger.info(f"Hello from {__name__}")