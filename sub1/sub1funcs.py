import logging
from sys import stdout


logger = logging.getLogger(f"app.{__name__}")
print(logger)

logger.info(f"THis is info from {__file__}.py")


def multiply_nrs(x, y):
    logger.info(
        "Called inside of func, after logger in main has set its level to debug. "
    )
    product = x * y
    logger.debug(f"Multiply nrs: {product}")


add_nrs(1, 2)
