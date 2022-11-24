import logging
from sys import stdout
from sub1 import sub1funcs

logger = logging.getLogger(__name__) 
logger.info("Sibling global scope") # Is this logged on 'import sibling' in run.py? 


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
        logger.exception(e) #This is how you capture the traceback. 
        # With a fileHandler configured to write to a file the traceback is 
        # stored after execution. 

sub1funcs.multiply_nrs(10, 2)
