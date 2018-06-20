from abc import abstractmethod, ABCMeta

import pygame

from graphics.reactable import Reactable
from src.graphics.drawable import Drawable
from src.utilities import system_settings
from src.utilities.asset_manager import AssetManager


class GenericScreen(Drawable, Reactable, metaclass=ABCMeta):
    """
        Base class for all screen, allowing to configure, run and exit with data.
    """

    def __init__(self):
        self.has_finished = False
        self.has_advanced = False
        self.is_fading_in = False
        self.is_fading_out = False

        self.widgets = {}
        self.assets = {}
        self.data = {}
        self.next_screen = None

        self.__FADING_IN_FRAMES = system_settings.FRAMES_PER_SECOND * system_settings.FADE_IN_TIME
        self.__FADING_OUT_FRAMES = system_settings.FRAMES_PER_SECOND * system_settings.FADE_OUT_TIME
        self.__fading_frames = 0

        self.__INNER_PADDING = 10

    def display_widgets(self, surface):
        for widget in self.widgets:
            widget.render(surface)

    def return_data(self):
        return self.data

    def clear_data(self):
        self.data = {}

    def setup(self, data):
        self.data = data

    def get_next_screen(self):
        return self.next_screen

    def render(self, surface):
        self.render_screen(surface)

        if self.is_fading_in:
            fading_surface = pygame.Surface(surface.get_size())
            fading_surface.blit(surface, (0, 0))
            alpha_level = int(255 * float(self.__fading_frames) / float(self.__FADING_IN_FRAMES))
            self.__fading_frames -= 1
            fading_surface.set_alpha(alpha_level)
            surface.blit(fading_surface, (0, 0))

        elif self.is_fading_out:
            fading_surface = pygame.Surface(surface.get_size())
            fading_surface.blit(surface, (0, 0))
            alpha_level = int(255 * (1 - float(self.__fading_frames) / float(self.__FADING_IN_FRAMES)))
            self.__fading_frames -= 1
            fading_surface.set_alpha(alpha_level)
            surface.blit(fading_surface, (0, 0))

    @abstractmethod
    def setup_assets(self):
        pass

    def load_assets(self):
        for _, asset_info in self.assets.items():
            AssetManager.load_asset(asset_info)

    def handle_event(self, event):
        for widget in self.widgets:
            widget.handle_event(event)

    @abstractmethod
    def render_screen(self, surface):
        pass

    @abstractmethod
    def finalize(self):
        pass

    def __del__(self):
        del self.widgets
        for _, asset_info in self.assets.items():
            AssetManager.clear_asset(asset_info)
