from enum import Enum


class AssetTypes(Enum):
    """
        All asset types are gathered here. Each type has been assigned a name of corresponding folder.
    """

    IMAGE = "images"
    SOUND = "sounds"
    LEVEL = "levels"
    FONT = "fonts"


class AssetInfo:
    """
        A class that represents information for AssetManager about a given asset.
    """

    def __init__(self, asset_type, asset_name, asset_src=None):
        self.asset_type = asset_type
        self.asset_name = asset_name
        self.asset_src = asset_src
