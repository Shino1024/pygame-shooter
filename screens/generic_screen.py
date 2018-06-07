from abc import ABC, abstractmethod, ABCMeta
from graphics.drawable import Transitional, Drawable


class GenericScreen(Drawable, metaclass=ABCMeta):
    """
        Base class for all screen, allowing to configure, run and exit with data.
    """

    is_finished = False
    is_fading = None

    __assets = {}
    __widgets = {}

    def display_widgets(self, surface):
        for widget in self.__widgets:
            widget.render(surface)

    @abstractmethod
    def setup(self, **kwargs):
        pass

    @abstractmethod
    def return_data(self):
        pass

    @abstractmethod
    def get_next_screen(self):
        pass
