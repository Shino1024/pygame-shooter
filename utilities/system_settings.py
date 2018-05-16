from enum import Enum

RESOLUTION_X = 640
RESOLUTION_Y = 640

TILE_SIZE = 20
MAP_TILES_NUM = 2

FRAMES_PER_SECOND = 30

LEVEL_EXTENSION = ".pslvl"

LEVELS_PATH = "assets/levels"
SOUNDS_PATH = "assets/sounds"
SPRITES_PATH = "assets/sprites"

class DifficultyLevels(Enum):
	EASY, \
	NORMAL, \
	HARD \
	= range(3)

