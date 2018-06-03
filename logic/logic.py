import pygame
from utilities import system_settings


class MainLoop:

	__SCREEN = None
	__SURFACE = None

	__game_clock = pygame.Clock()

	__window = pygame.window.Window()

	def setup(self):
		pygame.font.init()
		self.__SCREEN = self.__window.start()
	
	def run(self):
		self.__game_clock.tick(system_settings.FRAMES_PER_SECOND)
		pygame.display.update()

	def quit(self):
		# Display exit screen?
		pygame.quit()

class EventHandling:
	pass
