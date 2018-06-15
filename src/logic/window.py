import pygame
import sys

from src.utilities import system_settings


class Window:
    """
        A helper class for convenient management of the window container.
    """

    SCREEN_SURFACE = None

    @classmethod
    def start(cls):
        cls.SCREEN_SURFACE = pygame.display.set_mode([system_settings.RESOLUTION_X, system_settings.RESOLUTION_Y])

    @staticmethod
    def exit():
        pygame.quit()
        sys.exit(0)
