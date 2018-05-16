from enum import Enum
from abc import ABC, abstractmethod

class Entity:
	__ID = ""

	def set_id(self, ID):
		self.__ID = ID

class Sentient(Entity):
	def set_health(self, health):
		self.__health = health

	def get_health(self):
		return self.__health

	def pass_damage(self):
		pass


class Player(Sentient):
	def collect_treaure(self):
		pass

	def score_points(self):
		pass

	def get_points(self):
		pass

	def collect_pick(self):
		pass

	def assign_sprite(self):
		pass

	def set_stats(self):
		pass

	def set_equipment(self):
		pass


class MonsterKind(Enum):
	pass


class Monster(Sentient):
	def set_kind(self, kind):
		self.kind = kind

	def assign_sprite(self):
		pass

	def assign_algorithm(self):
		pass


class StillObject(Entity):
	pass

class DestructibleObject(StillObject):
	def set_durability(self):
		pass

	def get_condition(self):
		pass

	def destroy(self):
		pass


class InvincibleObject(StillObject):
	pass


class Treasure(StillObject):
	def set_kind(self):
		pass

	def set_amount(self):
		pass

class FieldTypes(Enum):
	DESTRUCTIBLE, \
	INVINCIBLE, \
	MONSTER, \
	AMMO, \
	WEAPON, \
	TREASURE, \
	LEVEL_SETTINGS, \
	= range(7)

class DestructibleTypes(Enum):
	BUSH, \
	BOX, \
	= range(2)

class InvincibleTypes(Enum):
	ROCK, \
	WALL, \
	= range(2)

class MonsterTypes(Enum):
	GHOST, \
	ROBOT, \
	ZOMBIE, \
	= range(3)

class AmmoTypes(Enum):
	WATER, \
	BOLT, \
	FIRE, \
	WIND, \
	= range(4)

class WeaponTypes(Enum):
	SHOT, \
	BOMB, \
	= range(2)

class TreasureTypes(Enum):
	POINTS, \
	TIME, \
	AMMO, \
	= range(3)

