from abc import ABC, abstractmethod
import pygame
import utilities.system_settings

from utilities.drawable import Drawable

class Transitional(ABC):
	@abstractmethod
	def fade_in(self, surface):
		pass

	@abstractmethod
	def fade_out(self, surface):
		pass

class Animation:
	__step_length = 0
	__init_time = 0
	__movement_speed = 0

	class MovementOrientation(Enum):
		HORIZONTAL, \
		VERTICAL \
		= range(2)

	def __init__(self, sprite_list, step_length):
		assert step_length > 0
		self.__sprite_list = sprite_list
		self.__step_length = step_length

	def move

	def start_animation(self):
		self.__init_time = pygame.time.get_ticks()

	def step_get(self):
		assert time_delta > 0

		time_point = pygame.time.get_ticks()
		time_delta = time_point - self.__init_time
		num = (time_delta / self.__step_length) % len(self.__sprite_list)
		return self.__sprite_list[num]
"""
	def change_pace(self, animation_length):
		self.animation_length = animation_length
"""
	def receive_sprite(self):
		pass

class Sprite(Drawable):
	pass

class MapSprite:
#

class Map(Drawable):
	__sprites = {}

	def update_sprite(self, sprite_id):
		#self.__sprite_matrix[i][j] = sprite

	def move_sprite_x(self, sprite_id, x):
		self.__sprites[sprite_id].

	def move_sprite_y(self, sprite_id, y):
		pass

	def render(self, screen):
		for sprite in self.__sprites:
			screen.blit(sprite.get_surface(), sprite.get_surface().get_rect())

