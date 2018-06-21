from abc import abstractmethod

import pygame

from graphics.reactable import Reactable
from src.graphics.drawable import Drawable
from src.utilities import system_settings
from src.utilities.asset_manager import AssetManager
from src.graphics.colors import Colors


class Widget(Drawable):
    """
        Base class for drawable Widgets.
    """

    def __init__(self):
        self.w = 0
        self.h = 0
        self.x = 0
        self.y = 0

    def center(self):
        self.x = (system_settings.RESOLUTION_X - self.w) / 2.


class Caption(Widget):
    """
        A simple class to draw text.
    """

    def __init__(self, text):
        super().__init__()

        self.__text = text
        self.__bold_style = False
        self.__font_info = None
        self.__color = None
        self.__font_size = None

    def set_bold(self, bold_style):
        self.__bold_style = bold_style

    def set_font_info(self, font_info):
        self.__font_info = font_info

    def set_color(self, color):
        self.__color = color

    def render(self, surface, move_x=0, move_y=0):
        font = AssetManager.get_asset(self.__font_info)
        font.set_bold(self.__bold_style)
        text_surface = font.render(self.__text, True, self.__color)
        surface.blit(text_surface, text_surface.get_rect().move(move_x, move_y))
        font.set_bold(False)

    def get_rect(self):
        print("font_info")
        print(self.__font_info.asset_name)
        font = AssetManager.get_asset(self.__font_info)
        print("NNNNNGHHHHHHHHH")
        print(font)
        font.set_bold(self.__bold_style)
        text_surface = font.render(self.__text, True, self.__color)
        font.set_bold(False)
        return text_surface.get_rect()


class Button(Widget, Reactable):
    """
        A clickable button with a caption.
    """

    def __init__(self):
        super().__init__()

        self.__is_hovered = False
        self.__is_pressed = False

        self.__caption = None

        self.__background_color = None
        self.__border_color = Colors.BLACK.value
        self.__border_width = 2
        self.__action = None

        self.__INNER_PADDING = 10
        self.__BORDER_WIDTH = 10

    def set_background_color(self, background_color):
        self.__background_color = background_color

    def set_border_width(self, border_width):
        self.__border_width = border_width

    def set_caption(self, caption):
        self.__caption = caption
        print("SET::::")
        print(self.__caption)

    def set_action(self, action):
        self.__action = action

    def auto_size(self):
        if self.__caption is None:
            print("NOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO")
            return

        print("YAAAAAAAAAAAAAAAAAAAY")
        print(self.__caption)

        caption_surface = self.__caption.get_rect()
        self.w = caption_surface.w + self.__INNER_PADDING + self.__BORDER_WIDTH
        self.h = caption_surface.h + self.__INNER_PADDING + self.__BORDER_WIDTH
        del caption_surface

    def handle_event(self, event):
        if pygame.mouse.get_pos().x in (self.x, self.x + self.w) \
                and pygame.mouse.get_pos().y in (self.y, self.y + self.h):
            if event.type == pygame.MOUSEMOTION:
                self.__is_hovered = True

            elif event.type == pygame.MOUSEBUTTONUP:
                if self.__is_pressed:
                    self.__action()

                self.__is_pressed = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.__is_pressed = True

        else:
            if event.type == pygame.MOUSEMOTION:
                self.__is_hovered = False
                self.__is_pressed = False

    def hover(self):
        self.__is_hovered = True

    def press(self, args):
        self.__action(*args)

    def render(self, screen):
        button_surface = pygame.Surface((self.w, self.h))
        button_surface.fill(self.__border_color, button_surface.get_rect())

        inner_w = self.w - 2 * self.__border_width
        inner_h = self.h - 2 * self.__border_width
        inner_surface = pygame.Surface((inner_w, inner_h))

        inner_background_color = [0, 0, 0, 0]
        inner_background_color[3] = 255
        if self.__is_hovered:
            inner_background_color[0] = max(255, self.__background_color[0] + 50)
            inner_background_color[1] = max(255, self.__background_color[1] + 50)
            inner_background_color[2] = max(255, self.__background_color[2] + 50)
        else:
            inner_background_color[0] = max(255, self.__background_color[0] + 20)
            inner_background_color[1] = max(255, self.__background_color[1] + 20)
            inner_background_color[2] = max(255, self.__background_color[2] + 20)

        inner_surface.fill(tuple(inner_background_color))
        self.__caption.render(inner_surface,
                                move_x=(inner_h - self.__caption.get_rect().x) / 2,
                                move_y=(inner_w - self.__caption.get_rect().y) / 2)

        button_surface.blit(inner_surface, (self.__border_width, self.__border_width))

        screen.blit(button_surface, (self.x, self.y))


class Dialog(Widget, Reactable):
    """
        A combined set of widgets to display a small window.
    """

    def __init__(self):
        super().__init__()

        self.__widgets = []

        self.__TITLE_BAR_OFFSET = 10

        self.__title_caption = None
        self.__title_bar_color = Colors.GRAY

    def set_title_caption(self, title_caption):
        self.__title_caption = title_caption

    def set_title_bar_color(self, color):
        self.__title_bar_color = color

    def place_widget(self, widget):
        self.__widgets.append(widget)

    def handle_event(self, event):
        for widget in self.__widgets:
            widget.handle_event(event)

    def render(self, surface):
        dialog_surface = pygame.Surface((self.w, self.h))
        if self.__title_caption is not None:
            title_bar = pygame.Surface((self.w, self.__title_caption.get_font_size() + self.__TITLE_BAR_OFFSET))
            title_bar.fill(self.__title_bar_color)
            title_bar.blit(self.__title_caption, (3, 5))

            dialog_surface.blit(title_bar, (0, 0))

        for widget in self.__widgets:
            if self.__title_caption is None:
                dialog_surface.blit(widget, (self.x, self.y))
            else:
                title_bar_offset_y = self.y + self.__TITLE_BAR_OFFSET + self.__title_caption.get_font_size
                dialog_surface.blit(widget, (self.x, title_bar_offset_y))

        surface.blit(dialog_surface, (self.x, self.y))
