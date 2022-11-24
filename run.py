import log_config
import logging
from sys import stdout
import sibling

logger = logging.getLogger(__name__)


logger.info(f"Global scope in run.py {__name__}") # This is logged to console.


sibling.divide_nrs(2, 5)
# sibling.add_nr_var_not_defined()
