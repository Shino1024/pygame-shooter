from enum import Enum


class AssetTypes(Enum):
    IMAGE, \
        MUSIC, \
        LEVEL, \
        = range(3)


class AssetManager:
    """
        Allows to retrieve resources of any types.
    """

    __assets = {**{asset_type: {} for asset_type in AssetTypes}}

    @classmethod
    def get_asset(cls, asset_type, asset_name):
        if asset_type not in cls.__assets:
            raise KeyError("No asssets of given type have been assigned.")

        if asset_name not in cls.__assets[asset_type]:
            raise KeyError("Couldn't find asset with a given name.")

        return cls.__assets[asset_type][asset_type]

    @classmethod
    def load_asset(cls, asset_type, asset_name, asset):
        if asset_type not in AssetTypes:
            raise ValueError("Can't handle assets of unknown types.")

        if asset_name in cls.__assets[asset_type]:
            raise ValueError("C")

        cls.__assets[asset_type][asset_name] = asset

    @classmethod
    def erase_asset(cls, asset_type, asset_name):
        if asset_type not in cls.__assets:
            raise KeyError("No asssets of given type have been assigned.")

        if asset_name not in cls.__assets[asset_type]:
            raise KeyError("Couldn't find asset with a given name.")

        del cls.__assets[asset_type]


