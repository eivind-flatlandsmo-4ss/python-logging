import logging
from sys import stdout
from utils.mass import calc_cube_mass


# Create logger instance
logger = logging.getLogger()

# Configure logger instance
stream_handler = logging.StreamHandler(stdout)
logger.addHandler(stream_handler)
formatter = logging.Formatter("%(name)s - %(levelname)s - %(message)s")
stream_handler.setFormatter(formatter)
logger.setLevel("DEBUG")


def main():
    logger.info("Start calculating. ")
    calc_cube_mass(sides_cm=10, density=1.0)
    logger.info("Finished calculating.")


if __name__ == "__main__":
    main()
