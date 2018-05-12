from enum import Enum
from abc import ABC, abstractmethod

class Entity:
	__ID = ""

	@abstractmethod
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
	*_ = range(10)

class DestructibleTypes(Enum):
	BUSH, \
	BOX, \
	*_ = range(10)

class InvincibleTypes(Enum):
	ROCK, \
	WALL, \
	*_ = range(10)

class MonsterTypes(Enum):
	GHOST, \
	ROBOT, \
	ZOMBIE, \
	*_ = range(10)

class AmmoTypes(Enum):
	WATER, \
	BOLT, \
	FIRE, \
	WIND, \
	*_ = range(10)

class WeaponTypes(Enum):
	SHOT, \
	BOMB, \
	*_ = range(10)

class TresasureTypes(Enum):
	POINTS, \
	TIME, \
	AMMO, \
	*_ = range(10)

