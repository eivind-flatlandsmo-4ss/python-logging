import logging 

logger = logging.getLogger(f"app.{__name__}")
msg = f"""Print statement from: {__name__}. 
Print statements are not inclued in the log.
They are also fired on import statements when written in the global scope. 
"""
print(msg)

logger.info("Global scope. Logging from sub3funcs,")


def subtrackt_nrs(x, y):
    difference = y - x
    logger.info(f"The difference is: {difference}")
    return difference