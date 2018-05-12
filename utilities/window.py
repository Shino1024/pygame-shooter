import pygame
import sys

import utilities.system_settings

class Window:
	def start(self, screen):
		screen = pygame.display.set_mode([system_settings.RESOLUTION_X, system_settings.RESOLUTION_Y])

	def exit(self):
		pygame.quit()
		sys.exit(0)
