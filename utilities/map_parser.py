import json
import system_settings
import os

from ..entities import FieldTypes, DestructibleTypes, InvincibleTypes, MonsterTypes, AmmoTypes, WeaponTypes, TreasureTypes
from monster_algorithms import BehaviourTypes
from ..map import *

class Parser:
	self.__levels_names = []
	
	__BASE_FIELDS = {
		"field_type": lambda field_type: return self.__in_enum_list(field_type, FieldTypes)
		"x": lambda x: return self.__in_range(x, 32),
		"y": lambda y: return self.__in_range(y, 32)
	}
	__DESTRUCTIBLE_FIELDS = {**BASE_FIELDS,
		"hp": lambda hp: return self.__in_range(hp, 1 << 8),
		"kind": lambda kind: return self.__in_enum_list(kind, DestructibleTypes)
	}
	__INVINCIBLE_FIELDS = {**BASE_FIELDS,
		"kind": lambda kind: return self.__in_enum_list(kind, InvincibleTypes)
	}
	__MONSTER_FIELDS = {**BASE_FIELDS,
		"hp": lambda hp: return self.__in_range(hp, 1 << 8),
		"algorithm": lambda algorithm: return self.__in_enum_list(algorithm, BehaviourTypes),
		"kind": lambda kind: return self.__in_enum_list(kind, MonsterTypes),
	}
	__PICK_FIELDS = {**BASE_FIELDS,
		"points": lambda points: return self.__in_range(points, 1000)
	}
	__TREASURE_FIELDS = {**BASE_FIELDS,
		"kind": lambda kind: return self.__in_enum_list(kind, TreasureTypes),
		"amount": lambda amount: return self.__in_range(amount, 1000)
	}
	
	__LEVEL_SETTINGS = {
		"difficulty": lambda difficulty: return self.__in_enum_list(difficulty, DifficultyLevels),
		"points": lambda points: return self.__correct_points(points),
		"time": lambda time: return self.__in_range(time, 10)
	}

	__OBJS = [
		DESTRUCTIBLE_FIELDS,
		INVINCIBLE_FIELDS,
		MONSTER_FIELDS,
		PICK_FIELDS,
		TREASURE_FIELDS,
		LEVEL_SETTINGS
	]

	def __init__(self):
		self.__fetch_levels_names()

	def __fetch_levels_names(self):
		levels_folder_path = os.path.join(os.getcwd(), system_settings.LEVELS_PATH);
		if os.path.isdir(levels_folder_path) is False:
			raise RuntimeError(f"The {system_settings.LEVELS_PATH} folder doesn't exist!")

		for filename in os.listdir(levels_folder_path):
			relative_filename = os.path.join(levels_folder_path, filename)
			if filename.endswith(system_settings.LEVEL_EXTENSION) \
				and os.path.is_file(relative_filename):
					self.__levels_names.append(os.path.splitext(filename))

	def get_levels_names(self):
		return self.__levels_names

	def __in_enum_list(self, name, enum):
		return name.uppercase() in list(map(lambda enum_field: return enum_field.name, enum))

	def __correct_points(self, points):
		if len(points) != 3:
			return False

		if all([data.isdigit() for data in points]) == False:
			return False

		points_int = [int(data) for data in points]

		for i in range(len(points_int) - 1):
			if points[i] < 1 or points[i - 1] >= points[i] or points[i] > 5000:
				return False

		return True

	def __in_range(self, string, max_range):
		return int(string) in range(max_range) if string.isdigit() else False

	def __validate_field(self, json_dump):
		try:
			field_type = obj["field_type"]
		except KeyError:
			return False
		
		for obj in json_dump:
			if self.__OBJS[FieldType[key]].keys() != obj.keys():
				return False

	def __json_cast(self, obj):
		if all(key in self.__BASE_FIELDS for key in obj.keys()):
			return MapElement(obj)
		elif all(key in self.__LEVEL_SETTINGS for key in obj.keys()):
			return LevelSettings(obj)
		else:
			raise ValueError

	def __parse_level(self, level_name):
		if level_name not in self.__level_names:
			raise ValueError("No level with such name.")

		level_path = os.path.join(os.getcwd(), system_settings.LEVELS_PATH + "/" + level_name + system_settings.LEVEL_EXTENSION)

		with open(level_path) as level_file:
			json_level = json.load(level_file, object_hook=self.__json_cast)
	
		return json_level

	def __validate_level(json_level):
		matrix = [[None for x in range(settings.MAP_TILES_NUM)] for y in range(settings.MAP_TILES_NUM)]
		for obj in json_level:
			if type(obj) is MapElement:
				matrix[obj.y][obj.x] = obj
			elif type(obj) is LevelSettings:
				pass
			else:
			 return False

		for row in matrix:
			for elem in row:
				if elem == None:
					return False

				if self.__validate_field(elem) == False:
					return False

		return True

	def generate_map(self, level_name):
		json_level = self__parse_level(level_name)
		if self.__validate_level(json_level):
			return json_level
		else:
			return None

