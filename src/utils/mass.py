import logging

from .volume import calc_cube_volume

logger = logging.getLogger(__name__)
logger.info("inside mass")


def calc_cube_mass(sides_cm: float, density: float) -> float:
    """Calculate mass of a cube."""
    volume = calc_cube_volume(sides_cm)
    mass = density * volume
    logger.info(f"Inside func: {calc_cube_mass.__name__}")
    return mass
