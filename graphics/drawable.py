from abc import ABC, abstractmethod


class Transitional(ABC):

	@abstractmethod
	def fade_in(self, surface, time_length):
		pass

	@abstractmethod
	def fade_out(self, surface, time_length):
		pass


class Drawable(ABC):
	@abstractmethod
	def render(self, surface):
		pass
