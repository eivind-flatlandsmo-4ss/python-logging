import logging

from .volume import calc_cube_volume

logger = logging.getLogger(f"root.{__name__}")


def calc_cube_mass(sides_cm: float, density: float) -> float:
    """Calculate mass of a cube."""
    volume = calc_cube_volume(sides_cm)
    mass = density * volume
    logger.info(f"Inside func: {calc_cube_mass.__name__}")
    return mass
