import pygame
import sys

from src.utilities import system_settings


class Window:
    """
        A helper class for convenient management of the window container.
    """

    __SCREEN_SURFACE = None

    @classmethod
    def start(cls):
        pygame.init()
        pygame.font.init()
        pygame.mixer.init()
        cls.__SCREEN_SURFACE = pygame.display.set_mode([system_settings.RESOLUTION_X, system_settings.RESOLUTION_Y])

    @classmethod
    def get_surface(cls):
        return cls.__SCREEN_SURFACE

    @classmethod
    def update(cls):
        pygame.display.flip()

    @staticmethod
    def exit():
        pygame.quit()
        sys.exit(0)
