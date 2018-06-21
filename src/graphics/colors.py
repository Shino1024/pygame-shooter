from enum import Enum


class Colors(Enum):
    """
        An enum class which maps English color names to their RGB equivalents
        (pygame.Color compatible).
    """

    WHITE = (255, 255, 255, 255)
    RED = (255, 0, 0, 255)
    GREEN = (0, 255, 0, 255)
    BLUE = (0, 0, 255, 255)
    YELLOW = (255, 255, 0, 255)
    MAGENTA = (255, 0, 255, 255)
    CYAN = (0, 255, 255, 255)

    GRAY = (255, 255, 255, 127)
    LIGHT_RED = (255, 0, 0, 127)
    LIGHT_GREEN = (0, 255, 0, 127)
    LIGHT_BLUE = (0, 0, 255, 127)
    LIGHT_YELLOW = (255, 255, 0, 127)
    LIGHT_MAGENTA = (255, 0, 255, 127)
    LIGHT_CYAN = (0, 255, 255, 127)

    BLACK = (0, 0, 0, 255)
