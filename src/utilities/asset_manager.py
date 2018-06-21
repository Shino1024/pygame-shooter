import os

import pygame

from src.logic.level_parser import LevelParser
from src.utilities import system_settings
from src.utilities.asset_util import AssetTypes, AssetInfo


class AssetManager:
    """
        Allows to retrieve resources of any types.
    """

    __assets = {asset_type.value: {} for asset_type in AssetTypes}
    print("Help")
    print(__assets)

    @classmethod
    def load_asset(cls, asset_info: AssetInfo):
        print(cls.__assets)
        print("Matching")
        print(asset_info.asset_type)
        print(AssetTypes.IMAGE)
        print(asset_info.asset_type.value == AssetTypes.IMAGE.value)
        if asset_info.asset_type.value == AssetTypes.IMAGE.value:
            return cls.__load_image(asset_info.asset_name, asset_info.asset_src)
        elif asset_info.asset_type.value == AssetTypes.SOUND.value:
            return cls.__load_sound(asset_info.asset_name, asset_info.asset_src)
        elif asset_info.asset_type.value == AssetTypes.LEVEL.value:
            return cls.__load_level(asset_info.asset_name)
        elif asset_info.asset_type.value == AssetTypes.FONT.value:
            return cls.__load_font(asset_info.asset_name, asset_info.asset_src)
        else:
            print("Unmatched")
            return False

    @classmethod
    def __load_image(cls, image_name, image_src):
        absolute_image_folder = os.path.join(system_settings.ASSETS_PATH, AssetTypes.IMAGE.value)
        absolute_image_src = os.path.join(absolute_image_folder, image_src)
        try:
            cls.__assets[AssetTypes.IMAGE.value][image_name] = pygame.image.load(absolute_image_src)
            return True
        except pygame.error:
            return False

    @classmethod
    def __load_sound(cls, sound_name, sound_src):
        absolute_sound_folder = os.path.join(system_settings.ASSETS_PATH, AssetTypes.SOUND.value)
        absolute_sound_src = os.path.join(absolute_sound_folder, sound_src)
        try:
            cls.__assets[AssetTypes.SOUND.value][sound_name] = pygame.mixer.Sound(absolute_sound_src)
            return True
        except pygame.error:
            return False

    @classmethod
    def __load_level(cls, level_name):
        level = LevelParser.generate_map(level_name)
        if level is not None:
            cls.__assets[AssetTypes.LEVEL.value][level_name] = level
            return True
        else:
            return False

    @classmethod
    def __load_font(cls, font_name, font_src):
        absolute_font_folder = os.path.join(system_settings.ASSETS_PATH, AssetTypes.FONT.value)
        absolute_font_src = os.path.join(absolute_font_folder, font_src)
        try:
            font_size = int(font_name.split("/")[-1])
            cls.__assets[AssetTypes.FONT.value][font_name] = pygame.font.Font(absolute_font_src, font_size)
            print(absolute_font_src)
            print(cls.__assets[AssetTypes.FONT.value][font_name])
            print("LA BOMBA " + str(font_size))
            return True
        except (IndexError, ValueError, pygame.error) as e:
            print(e)
            return False

    @classmethod
    def get_asset(cls, asset_info: AssetInfo):
        # print("hepl pls")
        # print(cls.__assets.get(AssetTypes.IMAGE))
        # print(AssetTypes.IMAGE)
        # print(asset_info.asset_type)
        # print(cls.__assets.get(asset_info.asset_type))
        print("Getting")
        print(asset_info.asset_name)
        print(cls.__assets.get(asset_info.asset_type.value).get(asset_info.asset_name))
        return cls.__assets.get(asset_info.asset_type.value).get(asset_info.asset_name)

    @classmethod
    def clear_asset(cls, asset_info: AssetInfo):
        print("CLEARING")
        if asset_info.asset_name in cls.__assets[asset_info.asset_type.value]:
            del cls.__assets[asset_info.asset_type.value][asset_info.asset_name]
