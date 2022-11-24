import logging
from sys import stdout

from .sub2 import sub2funcs #This is a way to do relative imports

logger = logging.getLogger(__name__)
logger.info(f"Global scope in {__name__}.py")


def multiply_nrs(x, y):
    logger.info(f"Local scope in multiply_nrs")
    product = x * y
    logger.debug(f"Local scope in multiply_nrs: {product}")
    return product

sub2funcs.add_nrs(1, 2)
