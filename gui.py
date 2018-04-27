from utilities.drawable import Drawable

class Widget(Drawable):
	def __init__(self, x, y, width, height):
		self.x = x
		self.y = y
		self.width = width
		self.height = height


class Caption(Widget):
	def set_text(self, text):
		this.text = text

	def set_font(self):
		pass

	def set_color(self):
		pass

	def set_height(self, height):
		this.height = height

	def emphasize(self):
		pass


class Button(Widget):
	def set_background(self):
		pass

	def set_caption(self, caption):
		self.caption = caption

	def emphasize(self):
		pass

	def press(self):
		pass


class Dialog(Widget):
	def __init__(self):
		pass

	def set_title(self, title):
		self.title = title

	def place_widget(self, widget, x, y):
		pass

	def forward_event(self, event):
		pass

