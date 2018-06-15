from enum import Enum

RESOLUTION_X = 640
RESOLUTION_Y = 640

TILE_SIZE = 20
TILES_NUM = RESOLUTION_X / TILE_SIZE
MAP_TILES_NUM = 2

FRAMES_PER_SECOND = 30

SPRITE_SPEED = 10

FADE_IN_TIME = 500
FADE_OUT_TIME = 500

LEVEL_EXTENSION = ".pslvl"


class DifficultyLevels(Enum):
    """
        All available levels. They add up to bonuses.
    """

    EASY, \
        NORMAL, \
        HARD, \
        = range(3)
