import os

from src.utilities.asset_util import AssetTypes, AssetInfo

RESOLUTION_X = 640
RESOLUTION_Y = 640

TILE_SIZE = 20
TILES_NUM = RESOLUTION_X / TILE_SIZE
MAP_TILES_NUM = 2

FRAMES_PER_SECOND = 30

SPRITE_SPEED = 10

FADE_IN_TIME = 500
FADE_OUT_TIME = 500

ASSETS_PATH = os.path.join(os.getcwd(), "assets")
LEVEL_EXTENSION = ".pslvl"

fonts = {
    16: AssetInfo(AssetTypes.FONT, "Default16", "default.ttf"),
    20: AssetInfo(AssetTypes.FONT, "Default20", "default.ttf"),
    24: AssetInfo(AssetTypes.FONT, "Default24", "default.ttf"),
    32: AssetInfo(AssetTypes.FONT, "Default32", "default.ttf"),
}
