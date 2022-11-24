import logging

from .sub3 import sub3funcs

log = logging.getLogger(__name__)


def add_nrs(x, y):
    log.info(f"about to log: {x} and {y}")
    sum_nrs = x + y
    log.info(f"about to log: {sum_nrs}")
    sub3funcs.subtrackt_nrs(10, 14)
    return sum_nrs



