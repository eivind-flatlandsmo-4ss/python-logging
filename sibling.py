import logging
from sys import stdout

log = logging.getLogger(f"app.{__name__}")
log.info("After func")


def divide_nrs(x, y):
    try:
        divident = x / y
        log.info(f"inside divide_nrs: {divident}")
        return divident
    except ZeroDivisionError:
        log.exception(f"input {y} cannot be zero.")
