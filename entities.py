from enum import Enum

class Entity:
	pass


class Sentient(Entity):
	def set_health(self):
		pass

	def get_health(self):
		pass

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


class TreasureKind(Enum):
	pass


class Treasure(StillObject):
	def set_kind(self):
		pass

	def set_amount(self):
		pass

