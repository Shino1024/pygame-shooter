import json
import os

# from src.models.entities import FieldTypes, DestructibleTypes, InvincibleTypes, MonsterTypes, TreasureTypes
# from src.utilities import difficulty_levels
# from src.models import entities
# from src.logic import monster_algorithms
# from . import difficulty_levels
# # from src.logic.monster_algorithms import BehaviourTypes
# from src.models import game_map
# from src.utilities import system_settings, asset_util
# from src.utilities.system_settings import DifficultyLevels
# from src.utilities.asset_manager import AssetTypes
# from src.utilities.asset_manager import AssetTypes
from logic.difficulty_levels import DifficultyLevels
from logic.monster_algorithms import BehaviourTypes
from models.entities import FieldTypes, DestructibleTypes, InvincibleTypes, MonsterTypes, TreasureTypes
from models.game_map import MapElement, LevelSettings
from utilities import system_settings
from utilities.asset_util import AssetTypes


class LevelParser:
    """
        Responsible for parsing the map from JSON.
    """

    __level_names = []

    __BASE_FIELDS = {
        "field_type": lambda field_type: LevelParser.in_enum_list(field_type, FieldTypes),
        "x": lambda x: LevelParser.in_range(x, 32),
        "y": lambda y: LevelParser.in_range(y, 32),
    }
    __DESTRUCTIBLE_FIELDS = {**__BASE_FIELDS,
                             "hp": lambda hp: LevelParser.in_range(hp, 1 << 8),
                             "kind": lambda kind: LevelParser.in_enum_list(kind, DestructibleTypes),
                             }
    __INVINCIBLE_FIELDS = {**__BASE_FIELDS,
                           "kind": lambda kind: LevelParser.in_enum_list(kind, InvincibleTypes),
                           }
    __MONSTER_FIELDS = {**__BASE_FIELDS,
                        "hp": lambda hp: LevelParser.in_range(hp, 1 << 8),
                        "algorithm": lambda algorithm: LevelParser.in_enum_list(algorithm, BehaviourTypes),
                        "kind": lambda kind: LevelParser.in_enum_list(kind, MonsterTypes),
                        }
    __PICK_FIELDS = {**__BASE_FIELDS,
                     "points": lambda points: LevelParser.in_range(points, 1000),
                     }
    __TREASURE_FIELDS = {**__BASE_FIELDS,
                         "kind": lambda kind: LevelParser.in_enum_list(kind, TreasureTypes),
                         "amount": lambda amount: LevelParser.in_range(amount, 1000),
                         }

    __LEVEL_SETTINGS = {
        "difficulty": lambda difficulty: LevelParser.in_enum_list(difficulty, DifficultyLevels),
        "points": lambda points: LevelParser.correct_points(points),
        "time": lambda time: LevelParser.in_range(time, 10),
    }

    __OBJS = [
        __DESTRUCTIBLE_FIELDS,
        __INVINCIBLE_FIELDS,
        __MONSTER_FIELDS,
        __PICK_FIELDS,
        __TREASURE_FIELDS,
        __LEVEL_SETTINGS
    ]

    __LEVELS_FOLDER_PATH = os.path.join(system_settings.ASSETS_PATH, AssetTypes.LEVEL.value)

    @classmethod
    def fetch_levels_names(cls):
        if os.path.isdir(cls.__LEVELS_FOLDER_PATH) is False:
            raise RuntimeError("")

        for filename in os.listdir(cls.__LEVELS_FOLDER_PATH):
            relative_filename = os.path.join(cls.__LEVELS_FOLDER_PATH, filename)
            if filename.endswith(system_settings.LEVEL_EXTENSION) \
                    and os.path.isfile(relative_filename):
                cls.__level_names.append(os.path.splitext(filename)[0])

    @classmethod
    def get_levels_names(cls):
        return cls.__level_names

    @staticmethod
    def in_enum_list(name, enum):
        return name.uppercase() in list(map(lambda enum_field: enum_field.name, enum))

    @staticmethod
    def correct_points(points):
        if len(points) != 3:
            return False

        for i in range(len(points) - 1):
            if points[i] < 1 or points[i - 1] >= points[i] or points[i] > 5000:
                return False

        return True

    @staticmethod
    def in_range(string, max_range):
        return int(string) in range(max_range) if string.isdigit() else False

    @classmethod
    def validate_field(cls, json_dump):
        if "field_type" not in json_dump:
            return False

        try:
            if int(json_dump["x"]) < 0 or int(json_dump["x"]) >= system_settings.TILES_NUM \
                    or int(json_dump["y"]) < 0 or int(json_dump["y"]) >= system_settings.TILES_NUM:
                return False
        except (ValueError, KeyError):
            return False

        for obj in json_dump:
            if cls.__OBJS[obj["field_type"]].keys() != obj.keys():  # TODO: ????????
                return False

        return True

    @staticmethod
    def keys_equal(obj0, obj1):
        return all(key in obj0 for key in obj1)

    @classmethod
    def json_cast(cls, obj):
        if LevelParser.keys_equal(obj, cls.__BASE_FIELDS):
            return MapElement(obj)
        elif LevelParser.keys_equal(obj, cls.__LEVEL_SETTINGS):
            return LevelSettings(obj)
        else:
            raise ValueError

    @classmethod
    def __parse_level(cls, level_name):
        if level_name not in cls.__level_names:
            raise ValueError("No level with such name.")

        level_filename = level_name + system_settings.LEVEL_EXTENSION
        level_path = os.path.join(cls.__LEVELS_FOLDER_PATH, level_filename)

        try:
            with open(level_path) as level_file:
                json_level = json.load(level_file, object_hook=cls.json_cast)
        except ValueError:
            return None

        return json_level

    @classmethod
    def __validate_level(cls, json_level):
        matrix = [[None for _ in range(system_settings.MAP_TILES_NUM)] for _ in range(system_settings.MAP_TILES_NUM)]
        level_settings_present = False

        for obj in json_level:
            if type(obj) is MapElement:
                matrix[obj.y][obj.x] = obj
            elif type(obj) is LevelSettings:
                level_settings_present = True
            else:
                return False

        if level_settings_present is False:
            return False

        for row in matrix:
            for elem in row:
                if elem is None:
                    return False

                if cls.validate_field(elem) is False:
                    return False

        return True

    @classmethod
    def generate_map(cls, level_name):
        json_level = cls.__parse_level(level_name)
        if json_level is None:
            return None

        if cls.__validate_level(json_level):
            return json_level
        else:
            return None
