import pygame

from utilities.drawable import Drawable

class Widget(Drawable):
	def __init__(self, rect):
		self.rect = rect

class Caption(Widget):
	def set_text(self, text):
		self.text = text

	def set_font_name(self, font_name):
		self.font_name = font_name

	def set_color(self, color):
		self.color = color

	def set_font_size(self, font_size):
		self.font_size = font_size

	def render(self, screen):
		resulting_font = pygame.font.SysFont(self.font_name, self.font_size)
		text_surface = resulting_font.render(self.text, True, self.color)
		screen.blit(text_surface, text_surface.get_rect())

	def emphasize(self):
		pass

class Button(Widget):
	def set_background_color(self, background_color):
		self.__background_color = background_color

	def set_border_color(self, border_color):
		self.__border_color = border_color

	def set_caption_text(self, caption_text):
		self.__caption_text = caption_text

	def set_action(self, action):
		self.__action = action

	def emphasize(self):
		pass

	def press(self, event):
		pass

class Dialog(Widget):
	__widgets = []

	def __init__(self):
		pass

	def set_title(self, title):
		self.__title = title

	def place_widget(self, widget):
		self.__widgets.append(widget)

	def forward_event(self, event):
		pass

	def render(self):
		pass

