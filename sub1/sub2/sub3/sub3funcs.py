import logging 

logger = logging.getLogger(f"app.{__name__}")

print(f"Print statement from sub3funcs __name__: {__name__}")

logger.info("Global scope. Logging from sub3funcs,")


def subtrackt_nrs(x, y):
    difference = y - x
    logger.info(f"The difference is: {difference}")
    return difference