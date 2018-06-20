import os

import pygame

from src.logic.level_parser import LevelParser
from src.utilities import system_settings
from src.utilities.asset_util import AssetTypes


class AssetManager:
    """
        Allows to retrieve resources of any types.
    """

    __assets = {asset_type: {} for asset_type in AssetTypes}

    @classmethod
    def load_asset(cls, asset_info):
        print(cls.__assets)
        if asset_info.asset_type == AssetTypes.IMAGE:
            return cls.__load_image(asset_info.asset_name, asset_info.asset_src)
        elif asset_info.asset_type == AssetTypes.SOUND:
            return cls.__load_sound(asset_info.asset_name, asset_info.asset_src)
        elif asset_info.asset_type == AssetTypes.LEVEL:
            return cls.__load_level(asset_info.asset_name)
        elif asset_info.asset_type == AssetTypes.FONT:
            return cls.__load_font(asset_info.asset_name, asset_info.asset_src)
        else:
            return None

    @classmethod
    def __load_image(cls, image_name, image_src):
        absolute_image_folder = os.path.join(system_settings.ASSETS_PATH, AssetTypes.IMAGE.value)
        absolute_image_src = os.path.join(absolute_image_folder, image_src)
        try:
            cls.__assets[AssetTypes.IMAGE][image_name] = pygame.image.load(absolute_image_src)
            return True
        except pygame.error:
            return False

    @classmethod
    def __load_sound(cls, sound_name, sound_src):
        absolute_sound_folder = os.path.join(system_settings.ASSETS_PATH, AssetTypes.SOUND.value)
        absolute_sound_src = os.path.join(absolute_sound_folder, sound_src)
        try:
            cls.__assets[AssetTypes.SOUND][sound_name] = pygame.mixer.Sound(absolute_sound_src)
            return True
        except pygame.error:
            return False

    @classmethod
    def __load_level(cls, level_name):
        level = LevelParser.generate_map(level_name)
        if level is not None:
            cls.__assets[AssetTypes.LEVEL][level_name] = level
            return True
        else:
            return False

    @classmethod
    def __load_font(cls, font_name, font_src):
        absolute_font_folder = os.path.join(system_settings.ASSETS_PATH, AssetTypes.FONT.value)
        absolute_font_src = os.path.join(absolute_font_folder, font_src)
        try:
            font_size = int(font_name.split("/")[-1])
            cls.__assets[AssetTypes.FONT][font_name] = pygame.font.Font(absolute_font_src, font_size)
            return True
        except (IndexError, ValueError, pygame.error):
            return False

    @classmethod
    def get_asset(cls, asset_info):
        if asset_info.asset_name in cls.__assets[asset_info.asset_type]:
            return cls.__assets[asset_info.asset_type][asset_info.asset_name]
        else:
            return None

    @classmethod
    def clear_asset(cls, asset_info):
        if asset_info.asset_name in cls.__assets[asset_info.asset_type]:
            del cls.__assets[asset_info.asset_type][asset_info.asset_name]
