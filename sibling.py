import logging
from sys import stdout
from sub1 import sub1funcs

logger = logging.getLogger(__name__) 
logger.info("Sibling global scope") # Is this logged on 'import sibling' in run.py? 
# No. The 'logger' object is by default set to WARNING. 
# But! If the import statement 'import sibling' is located after setting the 
# the logger lever to "DEBUG", than this will be logged to console.


def divide_nrs(x, y):
    try:
        divident = x / y
        logger.info(f"Info local scope: inside divide_nrs: {divident}")
        return divident
    except Exception as e:
        logger.exception(f"{e} SOME EXTRA MESSAGE")


def add_nr_var_not_defined():
    try:
        y = 10
        return x + y
    except Exception as e:
        logger.exception(e)

sub1funcs.multiply_nrs(10, 2)
