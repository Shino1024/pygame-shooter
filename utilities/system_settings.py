from enum import Enum

RESOLUTION_X = 640
RESOLUTION_Y = 640

TILE_SIZE = 20
TILES_NUM = RESOLUTION_X / TILE_SIZE
MAP_TILES_NUM = 2

FRAMES_PER_SECOND = 30

SPRITE_SPEED = 10

TRANSITION_TIME = 1000

LEVEL_EXTENSION = ".pslvl"

LEVELS_PATH = "assets/levels"
SOUNDS_PATH = "assets/sounds"
SPRITES_PATH = "assets/sprites"


class DifficultyLevels(Enum):
    """
        All available levels. They add up to bonuses.
    """

    EASY, \
        NORMAL, \
        HARD, \
        = range(3)
