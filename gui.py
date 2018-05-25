import pygame

from utilities.drawable import Drawable

class Widget(Drawable):
	def __init__(self, w, h):
		self.__w = w
		self.__h = h

	def get_w(self):
		return self.__w

	def get_h(self):
		return self.__h


class Caption(Widget):
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

	def render(self, screen, move_x=0, move_y=0):
		resulting_font = pygame.font.SysFont(self.__font_name, self.__font_size)
		text_surface = resulting_font.render(self.__text, True, self.__color)
		screen.blit(text_surface, text_surface.get_rect().move(move_x, move_y))


class Button(Widget):
	self.__is_hovered = False

	def set_background_color(self, background_color):
		self.__background_color = background_color

	def set_border_color(self, border_color):
		self.__border_color = border_color

	def set_border_width(self, border_width):
		self.__border_width = border_width

	def set_caption(self, caption):
		self.__caption = caption

	def set_action(self, action):
		self.__action = action

	def hover(self):
		self.__is_hovered = True

	def press(self, args):
		action(*args)

	def render(self, screen):
		font_size = self.__caption_text.get_font_size()
		w = self.__w
		h = self.__h
		button_surface = pygame.Surface((w, h))
		button_surface.set_colorkey(self.__border_color)

		inner_w = w - 2 * self.__border_width
		inner_h = h - 2 * self.__border_width
		inner_surface = pygame.Surface((inner_w, inner_h))
		background_color = self.__background_color
		if self.__is_hoevered:
			background_color.r += 200
			background_color.g += 20
			background_color.b += 20
		inner_surface.set_colorkey(background_color)
		self.__caption_text.render(inner_surface, move_x=(inner_h - self.__caption.get_h()) / 2, move_y=(inner_w - self.__caption.get_w()) / 2)

		button_surface.blit(inner_surface)
		screen.blit(button_surface)


class Dialog(Widget):
	__widgets = []

	def __init__(self):
		pass

	def set_title(self, title_caption):
		self.__title_caption = title_caption

	def place_widget(self, widget):
		self.__widgets.append(widget)

	def forward_event(self, event):
		for widget in self.__widgets:
			pass

	def render(self, screen):
		pass

