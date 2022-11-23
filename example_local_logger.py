import logging
from datetime import datetime

# Soruce: https://docs.python.org/3/howto/logging.html#logging-basic-tutorial

# Method 1
logging.basicConfig(filename="example.log", encoding="utf-8", level=logging.DEBUG)
logging.debug("This message should go to the log file")
logging.info("So should this")
logging.warning("And this, too")
logging.error("And non-ASCII stuff, too, like Øresund and Malmö")


# Method 2 - writing the log to local dir.

logger = logging.getLogger("root")
logger.setLevel(logging.DEBUG)
filename = datetime.now().strftime("%Y%m%d_%H%M%S")
file_handler = logging.FileHandler(f"mylog_{filename}.txt")
logger.addHandler(file_handler)
file_logging_format = "%(levelname)s: %(asctime)s: %(message)s"
formatter = logging.Formatter(file_logging_format)
file_handler.setFormatter(formatter)


logger.error("Write this line to 'mylog.log'")
logger.info("Write this line to 'mylog.log'")
logger.debug("Write this line to 'mylog.log'")
