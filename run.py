import logging
from sys import stdout
import sibling
import sub1.sub1funcs
import sub1.sub2.sub2funcs


logger = logging.getLogger("app")
logger.info("logging message before config")


formatter = logging.Formatter(logging.BASIC_FORMAT)
stream_handler = logging.StreamHandler(stdout)
logger.addHandler(stream_handler)
stream_handler.setFormatter(formatter)
logger.setLevel("DEBUG")

msg = f"EIVIND run.py {__name__}"
logger.info(msg)


sibling.divide_nrs(2, 5)
sub1.sub1funcs.multiply_nrs(3, 4)
sub1.sub2.sub2funcs.add_nrs(2, 5)
