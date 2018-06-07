import pygame
import sys

from utilities import system_settings


class Window:
    """
        A helper class for convenient management of the window container.
    """

    def start(self):
        return pygame.display.set_mode([system_settings.RESOLUTION_X, system_settings.RESOLUTION_Y])

    def exit(self):
        pygame.quit()
        sys.exit(0)
