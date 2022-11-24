import logging

log = logging.getLogger(f"app.{__name__}")


def add_nrs(x, y):
    log.info(f"about to log: {x} and {y}")
    sum_nrs = x + y
    log.info(f"about to log: {sum_nrs}")


print(__name__)
