from abc import abstractmethod

import pygame

from graphics.drawable import Drawable


class Widget(Drawable):
    """
        Base class for drawable Widgets.
    """

    def __init__(self, w, h, x, y):
        self.w = w
        self.h = h
        self.x = x
        self.y = y

    @abstractmethod
    def handle_event(self, event):
        pass


class Caption(Widget):
    """
        A simple class to draw text.
    """

    def __init__(self, w, h, x, y):
        super().__init__(w, h, x, y)

        self.__text = None
        self.__font_name = None
        self.__color = None
        self.__font_size = None

    def set_text(self, text):
        self.__text = text

    def set_font_name(self, font_name):
        self.__font_name = font_name

    def set_color(self, color):
        self.__color = color

    def set_font_size(self, font_size):
        self.__font_size = font_size

    def get_font_size(self):
        return self.__font_size

    def handle_event(self, event):
        pass

    def render(self, surface, move_x=0, move_y=0):
        resulting_font = pygame.font.SysFont(self.__font_name, self.__font_size)
        text_surface = resulting_font.render(self.__text, True, self.__color)
        surface.blit(text_surface, text_surface.get_rect().move(move_x, move_y))


class Button(Widget):
    """
        A clickable button with a caption.
    """

    def __init__(self, w, h, x, y):
        super().__init__(w, h, x, y)

        self.__is_hovered = False
        self.__is_pressed = False

        self.__caption_text = None

        self.__background_color = None
        self.__border_color = None
        self.__border_width = None
        self.__action = None

    def set_background_color(self, background_color):
        self.__background_color = background_color

    def set_border_width(self, border_width):
        self.__border_width = border_width

    def set_caption_text(self, caption_text):
        self.__caption_text = caption_text

    def set_action(self, action):
        self.__action = action

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

        inner_background_color = pygame.Color()
        if self.__is_hovered:
            inner_background_color.r = max(255, self.__background_color.r + 50)
            inner_background_color.g = max(255, self.__background_color.g + 50)
            inner_background_color.b = max(255, self.__background_color.b + 50)
        else:
            inner_background_color.r = max(255, self.__background_color.r + 20)
            inner_background_color.g = max(255, self.__background_color.g + 20)
            inner_background_color.b = max(255, self.__background_color.b + 20)

        inner_surface.fill(inner_background_color)
        self.__caption_text.render(inner_surface,
                                   move_x=(inner_h - self.__caption_text.get_rect().x) / 2,
                                   move_y=(inner_w - self.__caption_text.get_rect().y) / 2)

        button_surface.blit(inner_surface, (self.__border_width, self.__border_width))

        screen.blit(button_surface, (self.x, self.y))


class Dialog(Widget):
    """
        A combined set of widgets to display a small window.
    """

    def __init__(self, w, h, x, y):
        super().__init__(w, h, x, y)

        self.__widgets = []

        self.__TITLE_BAR_OFFSET = 10

        self.__title_caption = None
        self.__title_bar_color = pygame.Color(64, 64, 64)

    def set_title_caption(self, title_caption):
        self.__title_caption = title_caption

    def set_title_bar_color(self, color):
        self.__title_bar_color = color

    def place_widget(self, widget):
        self.__widgets.append(widget)

    def handle_event(self, event):
        for widget in self.__widgets:
            widget.forward_event(event)

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
