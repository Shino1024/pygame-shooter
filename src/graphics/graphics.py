from enum import Enum
import pygame

from src.graphics import Drawable
from src.utilities import system_settings


class Animation:
    """
        Lets objects on screen be animated.
    """

    __step_length = 0
    __init_time = 0
    __movement_speed = 0

    class MovementOrientation(Enum):
        HORIZONTAL, \
            VERTICAL, \
            *_ = range(100)

    def __init__(self, sprite_list, step_length):
        assert step_length > 0
        self.__sprite_list = sprite_list
        self.__step_length = step_length

    def start_animation(self):
        self.__init_time = pygame.time.get_ticks()

    def step_get(self):
        time_point = pygame.time.get_ticks()
        time_delta = time_point - self.__init_time
        num = (time_delta / self.__step_length) % len(self.__sprite_list)
        return self.__sprite_list[num]
    """
        def change_pace(self, animation_length):
            self.animation_length = animation_length
    """
    def receive_sprite(self):
        pass


class Sprite(Drawable):
    """
        A class which allows to hold a sprite and its information.
    """

    __resource = None
    __id = None

    def __init__(self, _w, _h, x, y):
        super().__init__(system_settings.TILE_SIZE, system_settings.TILE_SIZE, x, y)
        assert x % system_settings.TILE_SIZE == 0
        assert y % system_settings.TILE_SIZE == 0

    def render(self, surface):
        surface.blit()


class DrawableEntity(Drawable):
    """
        A container for sprites. It is specialized to hold a few sprites.
    """

    def render(self, surface):
        pass


class Map(Drawable):
    """
        Contains sprites and allows to display the whole map grid.
    """

    __sprites = {}

    def add_sprite(self, entity_id, sprite):
        self.__sprites[entity_id] = sprite

    def remove_sprite(self, entity_id):
        # TODO: Sprite shown being destroyed?
        del self.__sprites[entity_id]

    def move_sprite_x(self, entity_id, dx):
        self.__sprites[entity_id].x += dx

    def move_sprite_y(self, entity_id, dy):
        self.__sprites[entity_id].y += dy

    def render(self, surface):
        for sprite in self.__sprites:
            sprite.render(surface)
