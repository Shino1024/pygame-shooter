import pygame

import utilities.window
import utilities.system_settings
from screens import *

class MainLoop:
	__SCREEN = None
	__SURFACE = None

	__game_clock = pygame.Clock()

	__window = window.Window()

	def setup(self):
		pygame.font.init()
		__SCREEN = self.__window.start()
		__SURFACE = pygame.Surface(__SCREEN.get_rect())
	
	def run(self):
		self.__game_clock.tick(system_settings.FRAMES_PER_SECOND)
		__SCREEN.blit(__SURFACE, __SURFACE.get_rect())
		pygame.display.update()

	def quit(self):
		# Display exit screen?
		pygame.quit()

class EventHandling:
	pass
