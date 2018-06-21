import os

from src.utilities.asset_util import AssetTypes, AssetInfo

RESOLUTION_X = 640
RESOLUTION_Y = 640

TILE_SIZE = 20
TILES_NUM = RESOLUTION_X / TILE_SIZE
MAP_TILES_NUM = 2

FRAMES_PER_SECOND = 30

SPRITE_SPEED = 10

FADE_IN_TIME = 2
FADE_OUT_TIME = 2

ASSETS_PATH = os.path.join(os.getcwd(), "assets")
LEVEL_EXTENSION = ".pslvl"

fonts = {
    16: AssetInfo(AssetTypes.FONT, "Default/16", "default.ttf"),
    20: AssetInfo(AssetTypes.FONT, "Default/20", "default.ttf"),
    24: AssetInfo(AssetTypes.FONT, "Default/24", "default.ttf"),
    32: AssetInfo(AssetTypes.FONT, "Default/32", "default.ttf")
}
