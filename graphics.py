class Animation:
	def __init__(self, sprite_map, animation_length):
		self.sprite_map = sprite_map
		self.animation_length = animation_length

	def start_animation(self, initial_ticks):
		pass

	def step(self, ticks):
		pass

	def change_pace(self, animation_length):
		self.animation_length = animation_length

	def receive_sprite(self):
        pass

class Sprite:
    pass