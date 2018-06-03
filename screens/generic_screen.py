from abc import ABC, abstractmethod
from graphics.drawable import Transitional, Drawable


class GenericScreen(ABC, Drawable, Transitional):

    @abstractmethod
    def generate_scene(self):
        pass


