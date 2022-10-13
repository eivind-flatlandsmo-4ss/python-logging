import logging

logger = logging.getLogger(__name__)


def calc_cube_volume(sides: float) -> float:
    """Calculate volume of a cube."""
    logger.info(f"Inside func: {calc_cube_volume.__name__}")
    return sides**3
