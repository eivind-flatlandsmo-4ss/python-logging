import logging
from sys import stdout
from datetime import datetime
from utils.mass import calc_cube_mass


# Create logger instance
logger = logging.getLogger("root")
formatter = logging.Formatter("%(name)s - %(levelname)s - %(message)s")

# Configure logger instance
stream_handler = logging.StreamHandler(stdout)
logger.addHandler(stream_handler)
stream_handler.setFormatter(formatter)

filename = datetime.now().strftime("%Y%m%d_%H%M%S")
file_handler = logging.FileHandler(f"logs\{filename}.log")
logger.addHandler(file_handler)
file_handler.setFormatter(formatter)

logger.setLevel("DEBUG")


def main():
    logger.info("Start calculating. ")
    mass = calc_cube_mass(sides_cm=10, density=1.0)
    logger.info("Finished calculating.")
    logger.info(f"The calculated mass is: {mass} grams.")

    return mass


if __name__ == "__main__":
    main()
